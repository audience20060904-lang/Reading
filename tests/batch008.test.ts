import {originalReadingPool} from './original-reading-pool';
import {describe,it,expect} from 'vitest';
import {readFileSync} from 'node:fs';
import {createHash} from 'node:crypto';
import baseline from './fixtures/batch007-fingerprints.json';
import type {Book,Question,ReadingPlan} from '../src/types';
import {emptyState,grade,exportBackup,parseBackup,restoreReadingState,statistics} from '../src/core';
import {getQuestionTranslation} from '../src/questionTranslations';
const read=(p:string)=>JSON.parse(readFileSync(p,'utf8'));
const b=read('public/data/book.json') as Book,qs=read('public/data/questions.json') as Question[],plan=originalReadingPool(read('public/data/reading-plan.json') as ReadingPlan);
const targets=read('source/short-questions/batch008-targets.json').targets as {questionId:string;readingUnitId:string;passageSha256:string}[];
const hash=(s:string)=>createHash('sha256').update(s).digest('hex');
describe('按阅读顺序补齐 45 段',()=>{
 it('此前发布的 108 道题内容指纹不变',()=>{
  expect(Object.keys(baseline)).toHaveLength(108);
  for(const [id,fp] of Object.entries(baseline))expect(qs.find(q=>q.id===id)?.fingerprint,id).toBe(fp);
 });
 it('补齐的恰好是原先接下来的 45 个缺口，不跳到其他片段',()=>{
  const originalPending=plan.units.filter(u=>!u.questionId||!(u.questionId in baseline));
  expect(targets).toHaveLength(45);expect(originalPending.slice(0,45).map(u=>u.id)).toEqual(targets.map(t=>t.readingUnitId));
  for(const t of targets){const q=qs.find(q=>q.id===t.questionId)!;expect(q.readingUnitId).toBe(t.readingUnitId);expect(hash(q.passage)).toBe(t.passageSha256);expect(q.translation).toMatch(/[\u4e00-\u9fff]/);expect(getQuestionTranslation(q)?.options).toHaveLength(4);expect(q.vocabulary.length).toBeGreaterThan(0);}
 });
 it('审阅记录绑定已核对段落，新增证据准确列出实际触及的句子',()=>{
  const reviews=read('source/short-questions/review-chapter-02-forty-five.json');expect(reviews.questionIds).toHaveLength(45);
  for(const t of targets){const q=qs.find(q=>q.id===t.questionId)!,p=b.paragraphs.find(p=>p.id===q.paragraphId)!;
   expect(reviews.paragraphs.find((r:any)=>r.id===p.id)?.textSha256).toBe(hash(p.text));
   for(const e of q.evidence){const start=p.text.indexOf(q.passage)+q.passage.indexOf(e.quote),end=start+e.quote.length;expect(e.sentenceIds).toEqual(q.sentenceIds.filter(id=>{const s=b.sentences.find(s=>s.id===id)!;return s.start<end&&s.end>start;}));for(const r of e.sources)expect(reviews.checkedPdfPages).toContain(r.pdfPage);}
  }
 });
 it('新增 45 段不伪称逐句证据全覆盖，剩余缺口仍完整可恢复',()=>{
  const c=read('public/data/coverage.json'),tasks=read('source/content-tasks.json');const historicalIds=new Set([...Object.keys(baseline),...targets.map(t=>t.questionId)]);expect(qs.length).toBeGreaterThanOrEqual(153);expect(historicalIds.size).toBe(153);expect(plan.units.filter(u=>!u.questionId||!historicalIds.has(u.questionId))).toHaveLength(900);expect(c.fullCoverage).toBe(false);expect(c.contextOnlySentences).toBe(c.contextSentences-c.evidenceSentences);expect(read('source/releases/batch-008.json').coverage.contextOnlySentences).toBeGreaterThan(0);
  expect(tasks.readingPlan.remainingUnitIds).toEqual(plan.units.filter(u=>!u.questionId).map(u=>u.id));expect(tasks.nextBatch.readingUnitId).toBe(tasks.readingPlan.remainingUnitIds[0]);
 });
 it('批量插入后旧位置、旧答案与历史快照按稳定 ID 恢复',()=>{
  const q=qs.find(q=>q.id==='q-c02-013')!,s=emptyState();s.readingLayoutVersion=2;s.readingUnitId=q.readingUnitId;s.attempts=[grade(q,q.answer,s,1200)];s.session={questionId:q.id,attemptId:s.attempts[0].id,selected:q.answer,startedAt:1,elapsedBefore:0};
  const restored=restoreReadingState(parseBackup(exportBackup(s)),qs,plan);expect(restored).toEqual(s);expect(restored.attempts[0].fingerprint).toBe(baseline['q-c02-013']);expect(statistics(restored).correct).toBe(1);
 });
});
