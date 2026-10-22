import {describe,it,expect} from 'vitest';
import {readFileSync} from 'node:fs';
import {createHash} from 'node:crypto';
import baseline from './fixtures/batch015-fingerprints.json';
import type {Book,Question,ReadingPlan} from '../src/types';
import {emptyState,grade,exportBackup,parseBackup,restoreReadingState,statistics} from '../src/core';
import {getQuestionTranslation} from '../src/questionTranslations';
const read=(p:string)=>JSON.parse(readFileSync(p,'utf8'));
const b=read('public/data/book.json') as Book,qs=read('public/data/questions.json') as Question[],plan=read('public/data/reading-plan.json') as ReadingPlan;
const targets=read('source/short-questions/batch016-targets.json').targets as {questionId:string;readingUnitId:string;passageSha256:string}[];
const hash=(s:string)=>createHash('sha256').update(s).digest('hex');
describe('第 6 章幸福与意义连续补齐 25 个单元',()=>{
 it('保留此前 378 道题的内容指纹',()=>{
  expect(Object.keys(baseline)).toHaveLength(378);
  for(const [id,fp] of Object.entries(baseline))expect(qs.find(q=>q.id===id)?.fingerprint,id).toBe(fp);
 });
 it('恰好填补接下来的 25 个缺口且保留原句和双语材料',()=>{
  const originalPending=plan.units.filter(u=>!u.questionId||!(u.questionId in baseline));
  expect(targets).toHaveLength(25);expect(originalPending.slice(0,25).map(u=>u.id)).toEqual(targets.map(t=>t.readingUnitId));
  const added=targets.map(t=>qs.find(q=>q.id===t.questionId)!);expect(added.filter(q=>q.chapterId==='c06')).toHaveLength(25);
  for(const [i,q] of added.entries()){expect(q.readingUnitId).toBe(targets[i].readingUnitId);expect(hash(q.passage)).toBe(targets[i].passageSha256);expect(q.translation).toMatch(/[\u4e00-\u9fff]/);expect(getQuestionTranslation(q)?.options).toHaveLength(4);expect(q.analyses).toHaveLength(4);expect(q.vocabulary.length).toBeGreaterThan(0);}
  expect(added[0].id).toBe('q-c06-056');expect(added.at(-1)?.id).toBe('q-c06-080');
 });
 it('原页审阅哈希及证据的句子与页码精确对应',()=>{
  const reviews=read('source/short-questions/review-chapter06-happiness25.json');expect(reviews.questionIds).toEqual(targets.map(t=>t.questionId));
  for(const t of targets){const q=qs.find(q=>q.id===t.questionId)!,p=b.paragraphs.find(p=>p.id===q.paragraphId)!;
   expect(reviews.paragraphs.find((r:any)=>r.id===p.id)?.textSha256).toBe(hash(p.text));
   for(const id of q.sentenceIds)expect(b.sentences.find(s=>s.id===id)?.review).toBe('visual-proofread');
   for(const e of q.evidence){const start=p.text.indexOf(q.passage)+q.passage.indexOf(e.quote),end=start+e.quote.length;expect(e.sentenceIds).toEqual(q.sentenceIds.filter(id=>{const s=b.sentences.find(s=>s.id===id)!;return s.start<end&&s.end>start;}));for(const r of e.sources)expect(reviews.checkedPdfPages).toContain(r.pdfPage);}
  }
 });
 it('403 段有题、650 段待办，拒绝虚假全覆盖',()=>{
  const c=read('public/data/coverage.json'),tasks=read('source/content-tasks.json'),historicalIds=new Set([...Object.keys(baseline),...targets.map(t=>t.questionId)]);expect(qs.length).toBeGreaterThanOrEqual(403);expect(historicalIds.size).toBe(403);expect(plan.units.filter(u=>!u.questionId||!historicalIds.has(u.questionId))).toHaveLength(650);expect(c.fullCoverage).toBe(false);expect(c.contextOnlySentences).toBeGreaterThan(0);expect(c.notDirectlyQuestioned).toBeGreaterThan(0);
  expect(plan.units.filter(u=>u.chapterId==='c05').every(u=>u.questionId)).toBe(true);
  expect(tasks.readingPlan.remainingUnitIds).toEqual(plan.units.filter(u=>!u.questionId).map(u=>u.id));expect(tasks.nextBatch.readingUnitId).toBe(tasks.readingPlan.remainingUnitIds[0]);
 });
 it('跨章新增后保留旧题位置、历史成绩与快照',()=>{
  const q=qs.find(q=>q.id==='q-c06-055')!,s=emptyState();s.readingLayoutVersion=2;s.readingUnitId=q.readingUnitId;s.attempts=[grade(q,q.answer,s,1200)];s.session={questionId:q.id,attemptId:s.attempts[0].id,selected:q.answer,startedAt:1,elapsedBefore:0};
  const restored=restoreReadingState(parseBackup(exportBackup(s)),qs,plan);expect(restored).toEqual(s);expect(restored.attempts[0].fingerprint).toBe(baseline['q-c06-055']);expect(statistics(restored).correct).toBe(1);
 });
});

it('保留可能解释与人物引语归属，不将假设类比当成群体风险数据',()=>{
 const potential=qs.find(q=>q.id==='q-c06-072')!,quotation=qs.find(q=>q.id==='q-c06-078')!,probable=qs.find(q=>q.id==='q-c06-079')!;
 expect(potential.passage).toContain('One potential reason');expect(potential.analyses.join(' ')).toContain('不确定性');
 expect(quotation.passage).toContain('he said');expect(quotation.analyses.join(' ')).toContain('不是关于难民风险的科学样本');expect(quotation.translation).toContain('不是关于难民实际风险的研究数据');
 expect(probable.passage).toContain('He probably thinks');expect(probable.analyses.join(' ')).toContain('没有问卷');
 const c=read('public/data/coverage.json');expect(c.contextOnlySentences).toBeGreaterThan(0);expect(c.notDirectlyQuestioned).toBeGreaterThan(0);expect(c.fullCoverage).toBe(false);
});
