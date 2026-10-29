import {readFileSync} from 'node:fs';
import {describe,it,expect} from 'vitest';
const read=(p:string)=>JSON.parse(readFileSync(p,'utf8'));
const all=read('src/data/question-revision-catalog.json').questions;
const q=(id:string)=>all.find((v:any)=>v.id===id);
const old=read('source/question-revisions/review-088-baseline.json').questions;
const b=(id:string)=>old.find((v:any)=>v.id===id);
describe('第八十八批：条件、比较主体与当前片段',()=>{
 it('外推前提与离婚比较主体完整入证，旧定位身份不变',()=>{
  for(const [id,term] of [['q-c10-020','If people make a selection too early in a task with little search cost'],['q-c10-023','those who spend less time exploring']] as const){
   const e=q(id).evidence[0],before=b(id).evidence[0];expect(e.quote).toContain(term);expect(e.quote).toContain(before.quote);expect(e.sentenceIds).toEqual(before.sentenceIds);expect(e.sources).toEqual(before.sources);
  }
  expect(q('q-c10-023').evidence[0].quote).toContain('than those who spend more time exploring before marriage');
 });
 it('探索必要性保留明显最好时的假设例外',()=>{
  const now=q('q-c10-022');expect(now.evidence[0]).toEqual(b(now.id).evidence[0]);
  expect(now.evidence[1].quote).toContain('if one mate were far better than the rest');expect(now.evidence[1].quote).toContain('there would be no need to explore');
  expect(now.analyses[3]).not.toContain('前文');expect(now.analyses[3]).not.toContain('CDC');
 });
 it('观点归属和数据相符只据当前，不前借后续或省略解释',()=>{
  expect(q('qe-c10-0038').analyses[3]).not.toContain('后续');expect(q('qe-c10-0038').analyses[1]).toContain('economists argue');
  expect(q('qe-c10-0046').analyses[2]).toContain('没有说明');expect(q('qe-c10-0046').analyses[3]).not.toContain('平均关联');
  expect(q('qe-c10-0048').analyses[3]).not.toContain('critical');expect(q('qe-c10-0043').analyses[3]).not.toContain('网站');
 });
 it('22题24候选有12题保留，答案原文和审阅界限保持',()=>{
  const r=read('source/question-revisions/review-088-report.json');
  expect(r.manual.questionCount).toBe(22);expect(r.manual.sourceCandidatesReviewed).toBe(24);expect(r.manual.revisedQuestionCount).toBe(10);
  expect(r.manual.questionReviews.filter((v:any)=>v.decision==='retained')).toHaveLength(12);
  expect(r.manual.pdfPagesVisuallyReviewed).toEqual([106,107]);expect(r.manual.pdfSourceBlocksTextMatched).toBe(5);
  expect(r.remainingQuestionReviews).toBe(984);expect(r.fullQuestionBankHumanReview).toBe(false);
  for(const before of old){expect(q(before.id).answer).toBe(before.answer);expect(q(before.id).passage).toBe(before.passage);}
 });
});
