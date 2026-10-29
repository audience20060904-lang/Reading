import {readFileSync} from 'node:fs';
import {describe,it,expect} from 'vitest';
const read=(p:string)=>JSON.parse(readFileSync(p,'utf8'));
const all=read('src/data/question-revision-catalog.json').questions;
const q=(id:string)=>all.find((v:any)=>v.id===id);
const old=read('source/question-revisions/review-075-baseline.json').questions;
const b=(id:string)=>old.find((v:any)=>v.id===id);

describe('第七十五批：当前片段、文学引文和作者观点',()=>{
 it('完整手动活动证据保留偶尔限定及原引用身份',()=>{
  const v=q('q-c08-061'),before=b(v.id);
  expect(v.evidence[0]).toEqual(before.evidence[0]);
  expect(v.evidence[0].quote).toContain('once in a while');
  expect(v.evidence[1].quote).toContain('bake your own bread');
  expect(v.evidence[1].quote).toContain('add some spice to your life');
  expect(v.evidence[1].sentenceIds).toEqual(before.evidence[1].sentenceIds);
  expect(v.evidence[1].sources).toEqual(before.evidence[1].sources);
 });
 it('排除项依当前数值，不引入后续人物背景或书店规模',()=>{
  expect(q('qe-c09-0004').analyses[1]).not.toContain('十五岁');
  expect(q('qe-c09-0006').analyses[0]).toContain('没有给出每天工作的时数');
  expect(q('qe-c09-0005').analyses[0]).toContain('没有交代书店大小');
  expect(q('qe-c09-0013').analyses[0]).not.toContain('后文');
  expect(q('qe-c09-0013').analyses[0]).toContain('二十八');
  expect(q('qe-c09-0013').options).toEqual(b('qe-c09-0013').options);
 });
 it('文学情绪例证与作者可能性结论同时可定位，观点对照完整',()=>{
  const v=q('q-c09-006');expect(v.evidence[0]).toEqual(b(v.id).evidence[0]);
  expect(v.evidence[1].quote).toContain('joys and sorrows');
  expect(v.evidence[1].quote).toContain('would never be revealed to us');
  expect(v.options[v.answer]).toContain('possible');
  expect(v.analyses[3]).not.toContain('Proust');
  const t=q('q-c09-007'),previous=b(t.id);
  expect(t.evidence[0].quote).toMatch(/^To me,/);
  expect(t.evidence[0].quote).toContain('not just');
  expect(t.evidence[0].quote).toContain(previous.evidence[0].quote);
  expect(t.evidence[0].sentenceIds).toEqual(previous.evidence[0].sentenceIds);
  expect(t.evidence[0].sources).toEqual(previous.evidence[0].sources);
 });
 it('完整审阅22题，13题保留，跨页原始片段和答案不改',()=>{
  const r=read('source/question-revisions/review-075-report.json');
  expect(r.manual.questionCount).toBe(22);expect(r.manual.sourceCandidatesReviewed).toBe(23);
  expect(r.manual.revisedQuestionCount).toBe(9);
  expect(r.manual.questionReviews.filter((v:any)=>v.decision==='retained')).toHaveLength(13);
  expect(r.manual.pdfPagesVisuallyReviewed).toEqual([88,89,90]);
  expect(r.manual.pdfSourceBlocksTextMatched).toBe(6);expect(r.remainingQuestionReviews).toBe(1265);
  expect(r.fullQuestionBankHumanReview).toBe(false);
  for(const before of old){expect(q(before.id).answer).toBe(before.answer);expect(q(before.id).passage).toBe(before.passage);}
 });
});
