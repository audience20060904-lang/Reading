import {readFileSync} from 'node:fs';
import {describe,it,expect} from 'vitest';
const read=(p:string)=>JSON.parse(readFileSync(p,'utf8'));
const all=read('src/data/question-revision-catalog.json').questions;
const q=(id:string)=>all.find((v:any)=>v.id===id);
const old=read('source/question-revisions/review-092-baseline.json').questions;
const b=(id:string)=>old.find((v:any)=>v.id===id);
describe('第九十二批：可见身份与独立可答的过渡题',()=>{
 it('They片段只要求当前行动者，不要求未显示女性助理身份',()=>{
  expect(q('q-c10-053').prompt).toContain('people in this passage');expect(q('q-c10-053').prompt).not.toContain('assistants');expect(q('q-c10-053').promptZh).toContain('片段中的人');
  const now=q('qe-c10-0099');expect(now.options[now.answer]).toContain('The people instructed');expect(now.options[now.answer]).not.toContain('women');expect(now.optionsZh[now.answer]).toContain('的人');expect(now.answer).toBe(b(now.id).answer);
 });
 it('过渡正确项不要求未显示前主题，购物例证齐全且旧引保留',()=>{
  const next=q('qe-c10-0097');expect(next.options[next.answer]).toContain('further example');expect(next.options[next.answer]).not.toContain('earlier laboratory');
  const mall=q('q-c10-060');expect(mall.options[mall.answer]).toContain('city and shopping');expect(mall.options[mall.answer]).not.toContain('interpersonal');expect(mall.evidence[0]).toEqual(b(mall.id).evidence[0]);expect(mall.evidence[1].quote).toContain('American cities and suburbs');expect(mall.evidence[2].quote).toContain('shopping mall in Staten Island');
  const city=q('qe-c10-0104');expect(city.options[city.answer]).toContain('possible exposure effects');expect(city.options[1]).not.toContain('current reader');
 });
 it('同课程完整定位，身份和would不借前章或用户记录',()=>{
  const e=q('q-c10-052').evidence[0],before=b('q-c10-052').evidence[0];expect(e.quote).toContain('an introduction to psychology class');expect(e.quote).toContain(before.quote);expect(e.sentenceIds).toEqual(before.sentenceIds);expect(e.sources).toEqual(before.sources);
  expect(q('qe-c10-0107').analyses.join('')).not.toContain('前章');expect(q('qe-c10-0108').options[0]).toContain('author');expect(q('qe-c10-0108').options[0]).not.toContain('user');expect(q('qe-c10-0102').analyses[3]).not.toContain('未配句');
 });
 it('20题23候选有8题保留，答案原文和审阅界限保持',()=>{
  const r=read('source/question-revisions/review-092-report.json');
  expect(r.manual.questionCount).toBe(20);expect(r.manual.sourceCandidatesReviewed).toBe(23);expect(r.manual.revisedQuestionCount).toBe(12);
  expect(r.manual.questionReviews.filter((v:any)=>v.decision==='retained')).toHaveLength(8);
  expect(r.manual.pdfPagesVisuallyReviewed).toEqual([112,113]);expect(r.manual.pdfSourceBlocksTextMatched).toBe(5);
  expect(r.remainingQuestionReviews).toBe(896);expect(r.fullQuestionBankHumanReview).toBe(false);
  for(const before of old){expect(q(before.id).answer).toBe(before.answer);expect(q(before.id).passage).toBe(before.passage);}
 });
});
