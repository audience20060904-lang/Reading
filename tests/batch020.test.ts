import {originalReadingPool} from './original-reading-pool';
import {describe,it,expect} from 'vitest';
import {readFileSync} from 'node:fs';
import {createHash} from 'node:crypto';
import baseline from './fixtures/batch019-fingerprints.json';
import type {Book,Question,ReadingPlan} from '../src/types';
import {emptyState,grade,exportBackup,parseBackup,restoreReadingState,statistics} from '../src/core';
import {getQuestionTranslation} from '../src/questionTranslations';
const read=(p:string)=>JSON.parse(readFileSync(p,'utf8'));
const b=read('public/data/book.json') as Book,qs=read('public/data/questions.json') as Question[],plan=originalReadingPool(read('public/data/reading-plan.json') as ReadingPlan);
const targets=read('source/short-questions/batch020-targets.json').targets as {questionId:string;readingUnitId:string;passageSha256:string}[];
const hash=(s:string)=>createHash('sha256').update(s).digest('hex');
describe('第 7–8 章继续补齐 25 个单元',()=>{
 it('保留此前 478 道题的内容指纹',()=>{
  expect(Object.keys(baseline)).toHaveLength(478);
  for(const [id,fp] of Object.entries(baseline))expect(qs.find(q=>q.id===id)?.fingerprint,id).toBe(fp);
 });
 it('恰好填补接下来的 25 个缺口且保留原句和双语材料',()=>{
  const originalPending=plan.units.filter(u=>!u.questionId||!(u.questionId in baseline));
  expect(targets).toHaveLength(25);expect(originalPending.slice(0,25).map(u=>u.id)).toEqual(targets.map(t=>t.readingUnitId));
  const added=targets.map(t=>qs.find(q=>q.id===t.questionId)!);expect(added.filter(q=>q.chapterId==='c07')).toHaveLength(8);expect(added.filter(q=>q.chapterId==='c08')).toHaveLength(17);
  for(const [i,q] of added.entries()){expect(q.readingUnitId).toBe(targets[i].readingUnitId);expect(hash(q.passage)).toBe(targets[i].passageSha256);expect(q.translation).toMatch(/[\u4e00-\u9fff]/);expect(getQuestionTranslation(q)?.options).toHaveLength(4);expect(q.analyses).toHaveLength(4);expect(q.vocabulary.length).toBeGreaterThan(0);}
  expect(added[0].id).toBe('q-c07-065');expect(added.at(-1)?.id).toBe('q-c08-017');
 });
 it('原页审阅哈希及证据的句子与页码精确对应',()=>{
  const reviews=read('source/short-questions/review-chapter07-08-next25.json');expect(reviews.questionIds).toEqual(targets.map(t=>t.questionId));
  for(const t of targets){const q=qs.find(q=>q.id===t.questionId)!,p=b.paragraphs.find(p=>p.id===q.paragraphId)!;
   expect(reviews.paragraphs.find((r:any)=>r.id===p.id)?.textSha256).toBe(hash(p.text));
   for(const id of q.sentenceIds)expect(b.sentences.find(s=>s.id===id)?.review).toBe('visual-proofread');
   for(const e of q.evidence){const start=p.text.indexOf(q.passage)+q.passage.indexOf(e.quote),end=start+e.quote.length;expect(e.sentenceIds).toEqual(q.sentenceIds.filter(id=>{const s=b.sentences.find(s=>s.id===id)!;return s.start<end&&s.end>start;}));for(const r of e.sources)expect(reviews.checkedPdfPages).toContain(r.pdfPage);}
  }
 });
 it('503 段有题、550 段待办，拒绝虚假全覆盖',()=>{
  const c=read('public/data/coverage.json'),tasks=read('source/content-tasks.json'),historicalIds=new Set([...Object.keys(baseline),...targets.map(t=>t.questionId)]);expect(qs.filter(q=>historicalIds.has(q.id))).toHaveLength(503);expect(plan.units.filter(u=>!u.questionId||!historicalIds.has(u.questionId))).toHaveLength(550);expect(c.fullCoverage).toBe(false);expect(c.contextOnlySentences).toBe(c.contextSentences-c.evidenceSentences);expect(read('source/releases/batch-020.json').coverage.contextOnlySentences).toBeGreaterThan(0);expect(c.notDirectlyQuestioned).toBe(c.candidateSentences-c.evidenceSentences);expect(read('source/releases/batch-020.json').coverage.notDirectlyQuestioned).toBeGreaterThan(0);
  expect(plan.units.filter(u=>u.chapterId==='c07').every(u=>u.questionId)).toBe(true);
  expect(tasks.readingPlan.remainingUnitIds).toEqual(plan.units.filter(u=>!u.questionId).map(u=>u.id));expect(tasks.nextBatch.readingUnitId).toBe(tasks.readingPlan.remainingUnitIds[0]);
 });
 it('跨章新增后保留旧题位置、历史成绩与快照',()=>{
  const q=qs.find(q=>q.id==='q-c07-064')!,s=emptyState();s.readingLayoutVersion=2;s.readingUnitId=q.readingUnitId;s.attempts=[grade(q,q.answer,s,1200)];s.session={questionId:q.id,attemptId:s.attempts[0].id,selected:q.answer,startedAt:1,elapsedBefore:0};
  const restored=restoreReadingState(parseBackup(exportBackup(s)),qs,plan);expect(restored).toEqual(s);expect(restored.attempts[0].fingerprint).toBe(baseline['q-c07-064']);expect(statistics(restored).correct).toBe(1);
 });
});

it('保留近似转述、反事实、针厂估算和Ford的最终产量限定，不把Kagan体验批评改成产量否定',()=>{
 const recollection=qs.find(q=>q.id==='q-c08-004')!,counterfactual=qs.find(q=>q.id==='q-c08-005')!,estimate=qs.find(q=>q.id==='q-c08-007')!,ford=qs.find(q=>q.id==='q-c08-009')!,kagan=qs.find(q=>q.id==='q-c08-017')!;
 expect(recollection.passage).toContain('something along the lines');expect(recollection.analyses.join(' ')).toContain('不是逐字');
 expect(counterfactual.passage).toContain('might have chosen');expect(counterfactual.analyses.join(' ')).toContain('未实现');
 expect(estimate.passage).toContain('estimated');expect(estimate.passage).toContain('48,000');expect(estimate.analyses.join(' ')).toContain('不是所有工厂保证值');
 expect(ford.passage).toContain('eventually');expect(ford.analyses.join(' ')).toContain('精确第一天');
 expect(kagan.passage).toContain('not complaining about the productivity');expect(kagan.analyses.join(' ')).toContain('体验批评');
 const historicalIds=new Set([...Object.keys(baseline),...targets.map(t=>t.questionId)]),historicalContext=new Set(qs.filter(q=>historicalIds.has(q.id)).flatMap(q=>q.sentenceIds));expect(read('public/data/coverage.json').proofreadSentences).toBeGreaterThan(historicalContext.size);
});
