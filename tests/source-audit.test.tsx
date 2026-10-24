import {describe,it,expect} from 'vitest';
import {readFileSync,existsSync} from 'node:fs';
import {createHash} from 'node:crypto';
import {renderToStaticMarkup} from 'react-dom/server';
import type {Book,Question,ReadingPlan} from '../src/types';
import {coverage,assertCoverageClaim,emptyState,grade,exportBackup,parseBackup,restoreReadingState} from '../src/core';
import {getQuestionTranslation} from '../src/questionTranslations';
import SourceSupport,{sectionItems} from '../src/SourceSupport';
import {originalReadingPool} from './original-reading-pool';
const read=(p:string)=>JSON.parse(readFileSync(p,'utf8'));
const book=read('public/data/book.json') as Book,plan=read('public/data/reading-plan.json') as ReadingPlan,qs=read('public/data/questions.json') as Question[];
const additions=read('source/additive-body.json').additions,audit=read('source/source-audit-review.json'),targets=read('source/short-questions/batch043-targets.json').targets;
const hash=(text:string)=>createHash('sha256').update(text).digest('hex');

describe('正文遗漏补回与最终来源审计',()=>{
 it('保留1053已发布题的指纹及原有阅读单元，修正仅为增量',()=>{
  const baseline=read('tests/fixtures/batch042-fingerprints.json');expect(Object.keys(baseline)).toHaveLength(1053);
  for(const [id,fingerprint] of Object.entries(baseline))expect(qs.find(q=>q.id===id)?.fingerprint,id).toBe(fingerprint);
  expect(originalReadingPool(plan).units).toHaveLength(1053);expect(qs).toHaveLength(1056);expect(plan.units).toHaveLength(1056);
 });
 it('两段作者正文在真实原页位置插入，并使用原书副标题区分未编号分组',()=>{
  expect(additions.map((a:any)=>a.paragraph.sources[0].pdfPage)).toEqual([144,160]);
  for(const a of additions){const s=book.sections.find(s=>s.id===a.section.id)!;expect(s.kind).toBe('opening');expect(s.number).toBe(0);expect(s.title).toBe(a.section.title);const pos=book.paragraphs.findIndex(p=>p.id===a.paragraph.id);expect(book.paragraphs[pos+1].chapterId).toBe(a.paragraph.chapterId);expect(book.paragraphs[pos+1].sectionId).toMatch(/-s01$/);}
  expect(book.sections.filter(s=>s.number>0)).toHaveLength(87);expect(book.sections).toHaveLength(89);
 });
 it('新增8句逐字对应原始提取，全文候选句无重复遗漏',()=>{
  const pages=read('source/pages.json');expect(additions.flatMap((a:any)=>a.sentences)).toHaveLength(8);
  for(const a of additions){const p=book.paragraphs.find(p=>p.id===a.paragraph.id)!;expect(p.text).toBe(a.paragraph.text);expect(p.raw).toBe(a.paragraph.raw);expect(pages[p.sources[0].pdfPage-1].raw.replace(/\s+/g,' ')).toContain(p.text);expect(p.sentenceIds.map(id=>book.sentences.find(s=>s.id===id)!.text).join(' ')).toBe(p.text);}
  expect(plan.units.flatMap(u=>u.sentenceIds)).toEqual(book.sentences.map(s=>s.id));expect(new Set(plan.units.flatMap(u=>u.sentenceIds)).size).toBe(3160);
 });
 it('3道新增题含完整双语材料、逐字证据与匹配的来源范围',()=>{
  expect(targets).toHaveLength(3);
  for(const t of targets){const q=qs.find(q=>q.id===t.questionId)!;expect(hash(q.passage)).toBe(t.passageSha256);expect(getQuestionTranslation(q)?.options).toHaveLength(4);expect(q.analyses).toHaveLength(4);expect(q.translation).toMatch(/[\u4e00-\u9fff]/);expect(q.vocabulary.length).toBeGreaterThan(0);for(const e of q.evidence){expect(q.passage).toContain(e.quote);expect(e.sentenceIds.every(id=>q.sentenceIds.includes(id))).toBe(true);expect(e.sources.every(s=>[144,160].includes(s.pdfPage))).toBe(true);}}
 });
 it('49个原排除块均有实际原页审阅、指纹与明确分类',()=>{
  expect(audit.records).toHaveLength(49);expect(audit.checkedPdfPages).toHaveLength(21);
  for(const r of audit.records){expect(hash(r.text)).toBe(r.textSha256);expect(r.review).toBe('actual-pdf-page-visually-checked');expect(r.reason.length).toBeGreaterThan(0);}
  expect(audit.records.filter((r:any)=>r.classification==='authorial-body')).toHaveLength(2);expect(audit.records.filter((r:any)=>r.classification==='structural-support')).toHaveLength(17);
 });
 it('8组辅助材料均可浏览，表格数值和来源块保持精确',()=>{
  expect(book.supportMaterials).toHaveLength(8);expect(book.excluded.some(e=>e.kind==='table-or-subheading')).toBe(false);
  const table=book.supportMaterials!.find(m=>m.sources[0].pdfPage===104)!;expect(table.rows?.[0]).toEqual(['Freshman','43.4%','34.1%','22.5%']);expect(table.rows?.[3]).toEqual(['Senior','13.6%','40.9%','45.5%']);
  const raw=table.sources.map(s=>s.text).join(' ');for(const row of table.rows!)for(const cell of row)expect(raw).toContain(cell);
 });
 it('图像来自实际PDF，源文浏览恢复表格与原始提取而不伪造作答',()=>{
  for(const m of book.supportMaterials!){const html=renderToStaticMarkup(<SourceSupport material={m}/>);expect(html).toContain(m.id);expect(html).toContain('原始提取与来源位置');if(m.kind==='table')expect(html).toContain('<table');if(m.image){expect(existsSync('public/'+m.image)).toBe(true);expect(html).toContain('<img');}expect(html).not.toContain('提交答案');}
 });
 it('辅助材料插入同小节的原页块顺序，短段自身仍保持原阅读顺序',()=>{
  for(const section of book.sections){const items=sectionItems(book,plan,section.id);expect(items.filter(i=>i.kind==='unit').map(i=>i.unit.id)).toEqual(plan.units.filter(u=>u.sectionId===section.id).map(u=>u.id));const pos=items.map(i=>{const s=i.kind==='support'?i.material.sources[0]:book.paragraphs.find(p=>p.id===i.unit.paragraphId)!.sources[0];return s.pdfPage*1000+s.block;});expect(pos).toEqual([...pos].sort((a,b)=>a-b));}
 });
 it('所有已知正文待办已完成，但逐句直接证据缺口仍阻止全覆盖声明',()=>{
  const c=coverage(book,qs),tasks=read('source/content-tasks.json');expect(c).toEqual(read('public/data/coverage.json'));expect(c.sourceAudit?.pendingTaskIds).toEqual([]);expect(c.supportMaterials).toBe(8);expect(c.notDirectlyQuestioned).toBe(1662);expect(c.evidenceSentences).toBe(1498);expect(plan.coverage.unitsWithoutQuestions).toBe(0);expect(tasks.readingPlan.remainingUnitIds).toEqual([]);expect(()=>assertCoverageClaim(c,true)).toThrow('虚假全覆盖');
 });
 it('增量插入后历史作答、指纹和位置仍可备份与恢复',()=>{
  const q=qs.find(q=>q.id==='q-c13-001')!,s=emptyState();s.readingLayoutVersion=2;s.readingUnitId=q.readingUnitId;s.attempts=[grade(q,q.answer,s,900)];s.session={questionId:q.id,attemptId:s.attempts[0].id,selected:q.answer,startedAt:1,elapsedBefore:0};expect(restoreReadingState(parseBackup(exportBackup(s)),qs,plan)).toEqual(s);
 });
});
