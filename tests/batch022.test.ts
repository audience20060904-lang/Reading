import {originalReadingPool} from './original-reading-pool';
import {describe,it,expect} from 'vitest';
import {readFileSync} from 'node:fs';
import {createHash} from 'node:crypto';
import baseline from './fixtures/batch021-fingerprints.json';
import type {Book,Question,ReadingPlan} from '../src/types';
import {emptyState,grade,exportBackup,parseBackup,restoreReadingState,statistics} from '../src/core';
import {getQuestionTranslation} from '../src/questionTranslations';
const read=(p:string)=>JSON.parse(readFileSync(p,'utf8'));
const b=read('public/data/book.json') as Book,qs=read('public/data/questions.json') as Question[],plan=originalReadingPool(read('public/data/reading-plan.json') as ReadingPlan);
const targets=read('source/short-questions/batch022-targets.json').targets as {questionId:string;readingUnitId:string;passageSha256:string}[];
const hash=(s:string)=>createHash('sha256').update(s).digest('hex'),q=(id:string)=>qs.find(q=>q.id===id)!;
describe('第8章末与第9章开篇连续25单元',()=>{
 it('保留此前528题的全部内容指纹',()=>{expect(Object.keys(baseline)).toHaveLength(528);for(const [id,fp] of Object.entries(baseline))expect(q(id)?.fingerprint,id).toBe(fp);});
 it('按顺序补齐25个缺口并保持原句指纹及双语材料',()=>{
  const pending=plan.units.filter(u=>!u.questionId||!(u.questionId in baseline));expect(targets).toHaveLength(25);expect(pending.slice(0,25).map(u=>u.id)).toEqual(targets.map(t=>t.readingUnitId));
  const added=targets.map(t=>q(t.questionId));expect(added.filter(a=>a.chapterId==='c08')).toHaveLength(19);expect(added.filter(a=>a.chapterId==='c09')).toHaveLength(6);expect(added[0].id).toBe('q-c08-043');expect(added.at(-1)?.id).toBe('q-c09-006');
  for(const t of targets){const a=q(t.questionId);expect(a.readingUnitId).toBe(t.readingUnitId);expect(hash(a.passage)).toBe(t.passageSha256);expect(a.translation).toMatch(/[\u4e00-\u9fff]/);expect(getQuestionTranslation(a)?.options).toHaveLength(4);expect(a.analyses).toHaveLength(4);expect(a.vocabulary.length).toBeGreaterThan(0);}
 });
 it('原页审阅哈希、证据句子范围及PDF页码精确匹配',()=>{
  const reviews=read('source/short-questions/review-chapter08-09-next25.json');expect(reviews.questionIds).toEqual(targets.map(t=>t.questionId));expect(reviews.checkedPdfPages).toEqual([85,86,87,88,89,90]);
  for(const t of targets){const a=q(t.questionId),p=b.paragraphs.find(p=>p.id===a.paragraphId)!;expect(reviews.paragraphs.find((r:any)=>r.id===p.id)?.textSha256).toBe(hash(p.text));
   for(const id of a.sentenceIds)expect(b.sentences.find(s=>s.id===id)?.review).toBe('visual-proofread');
   for(const e of a.evidence){const start=p.text.indexOf(a.passage)+a.passage.indexOf(e.quote),end=start+e.quote.length;expect(e.sentenceIds).toEqual(a.sentenceIds.filter(id=>{const s=b.sentences.find(s=>s.id===id)!;return s.start<end&&s.end>start;}));for(const r of e.sources)expect(reviews.checkedPdfPages).toContain(r.pdfPage);}
  }
 });
 it('保留本批553已配/500待办快照，不宣称全书逐句证据覆盖',()=>{
  const c=read('public/data/coverage.json'),tasks=read('source/content-tasks.json'),ids=new Set([...Object.keys(baseline),...targets.map(t=>t.questionId)]);
  expect(qs.filter(a=>ids.has(a.id))).toHaveLength(553);expect(plan.units.filter(u=>!u.questionId||!ids.has(u.questionId))).toHaveLength(500);expect(plan.units.filter(u=>u.chapterId==='c08').every(u=>u.questionId)).toBe(true);expect(c.fullCoverage).toBe(false);expect(c.contextOnlySentences).toBeGreaterThan(0);expect(c.notDirectlyQuestioned).toBeGreaterThan(0);
  expect(tasks.readingPlan.remainingUnitIds).toEqual(plan.units.filter(u=>!u.questionId).map(u=>u.id));expect(tasks.nextBatch.readingUnitId).toBe(tasks.readingPlan.remainingUnitIds[0]);
 });
 it('追加后仍能导出、导入和恢复旧题成绩、快照与位置',()=>{
  const a=q('q-c08-042'),s=emptyState();s.readingLayoutVersion=2;s.readingUnitId=a.readingUnitId;s.attempts=[grade(a,a.answer,s,1200)];s.session={questionId:a.id,attemptId:s.attempts[0].id,selected:a.answer,startedAt:1,elapsedBefore:0};
  const restored=restoreReadingState(parseBackup(exportBackup(s)),qs,plan);expect(restored).toEqual(s);expect(restored.attempts[0].fingerprint).toBe(baseline['q-c08-042']);expect(statistics(restored).correct).toBe(1);
 });
 it('保留未实证、反事实、原书时点和文学比喻的证据边界',()=>{
  expect(q('q-c08-044').passage).toContain('4,469');expect(q('q-c08-044').analyses.join(' ')).toContain('只是部分解释');
  expect(q('q-c08-045').passage).toContain('the other $40');expect(q('q-c08-045').analyses.join(' ')).toContain('没说周末顺序如何随机化');
  expect(q('q-c08-048').passage).toContain('not empirically tested');expect(q('q-c08-048').analyses.join(' ')).toContain('未实证');
  expect(q('q-c08-053').analyses.join(' ')).toContain('不是已经雇人后实测');expect(q('q-c08-055').analyses.join(' ')).toContain('反事实');
  expect(q('q-c09-003').analyses.join(' ')).toContain('引语在既有短段边界处');expect(q('q-c09-004').analyses.join(' ')).toContain('是比喻');expect(q('q-c09-006').analyses.join(' ')).toContain('文学引述');
 });
});
