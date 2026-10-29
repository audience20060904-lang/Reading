import {readFileSync} from 'node:fs';
import {describe,it,expect} from 'vitest';
const read=(p:string)=>JSON.parse(readFileSync(p,'utf8'));
const all=read('src/data/question-revision-catalog.json').questions;
const q=(id:string)=>all.find((v:any)=>v.id===id);
const old=read('source/question-revisions/review-098-baseline.json').questions;
const b=(id:string)=>old.find((v:any)=>v.id===id);
describe('第九十八批：完整条件、推测归属与东京同学',()=>{
 it('蜡烛双条件和MBA样本范围完整定位，旧引身份保持',()=>{
  expect(q('q-c10-106').evidence[0].quote).toContain('Can you attach a candle to a wall');expect(q('q-c10-106').evidence[0].quote).toContain('won’t drip wax on the table or floor');expect(q('q-c10-107').evidence[0].quote).toContain('Among MBA students');
  for(const id of ['q-c10-106','q-c10-107','q-c10-108','q-c10-111']){const now=q(id),before=b(id);expect(now.evidence[0].quote).toContain(before.evidence[0].quote);expect(now.evidence[0].sources).toEqual(before.evidence[0].sources);expect(now.evidence[0].sentenceIds).toEqual(before.evidence[0].sentenceIds);}
 });
 it('机制推测归属及微笑礼貌反馈两侧齐全',()=>{
  expect(q('q-c10-108').evidence[0].quote).toContain('Leung and colleagues speculate');
  const smile=q('q-c10-111');expect(smile.evidence[0].quote).toContain('also speculate');expect(smile.evidence[1].quote).toContain('could come across as impolite');expect(smile.evidence[2].quote).toContain('smile more because it would be more polite');
 });
 it('在东京的大学同学不误指东京大学，解析不借后段DIY',()=>{
  expect(q('qe-c10-0198').promptZh).toContain('在东京的大学同学');expect(q('qe-c10-0193').optionsZh[0]).toContain('在东京的大学同学');expect(q('qe-c10-0193').analyses[3]).not.toContain('下一段');expect(q('qe-c10-0186').analyses[2]).not.toContain('下一段');expect(q('qe-c10-0192').analyses[3]).not.toContain('后段');
 });
 it('22题22候选保留11题，原文答案和审阅边界保持',()=>{
  const r=read('source/question-revisions/review-098-report.json');expect(r.manual.questionCount).toBe(22);expect(r.manual.sourceCandidatesReviewed).toBe(22);expect(r.manual.revisedQuestionCount).toBe(11);expect(r.manual.questionReviews.filter((v:any)=>v.decision==='retained')).toHaveLength(11);expect(r.manual.pdfPagesVisuallyReviewed).toEqual([119,120]);expect(r.manual.pdfSourceBlocksTextMatched).toBe(4);expect(r.remainingQuestionReviews).toBe(765);expect(r.fullQuestionBankHumanReview).toBe(false);
  for(const before of old){expect(q(before.id).answer).toBe(before.answer);expect(q(before.id).passage).toBe(before.passage);}
 });
});
