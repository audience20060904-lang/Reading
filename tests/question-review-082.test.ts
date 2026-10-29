import {readFileSync} from 'node:fs';
import {describe,it,expect} from 'vitest';
const read=(p:string)=>JSON.parse(readFileSync(p,'utf8'));
const all=read('src/data/question-revision-catalog.json').questions;
const q=(id:string)=>all.find((v:any)=>v.id===id);
const old=read('source/question-revisions/review-082-baseline.json').questions;
describe('第八十二批：保留程序题与当前范围',()=>{
 it('解析不夹数据结构或网页提交显图说明',()=>{
  expect(q('qe-c09-0110').analyses[0]).not.toContain('current parent');
  expect(q('q-c09-057').analyses[3]).not.toContain('显示的图像');
  expect(q('qe-c09-0107').analyses[3]).not.toContain('网页');
  expect(q('qe-c09-0109').vocabulary[0].context).not.toContain('网站');
  expect(q('qe-c09-0113').analyses[2]).not.toContain('下一');
 });
 it('程序与复现边界只据当前，不前借其他研究',()=>{
  expect(q('qe-c09-0104').analyses[2]).toContain('没有给出随机分派童年阅读的程序');
  expect(q('qe-c09-0107').analyses[2]).not.toContain('前面');
  expect(q('qe-c09-0109').analyses[3]).not.toContain('混入前面');
  expect(q('q-c09-061').analyses[0]).not.toContain('前文');
  expect(q('qe-c09-0116').analyses[2]).not.toContain('前面');
 });
 it('全部八题保留正确选项、充分证据及原始译文，仅修订实际问题字段',()=>{
  for(const before of old){const v=q(before.id);expect(v.options).toEqual(before.options);expect(v.optionsZh).toEqual(before.optionsZh);expect(v.evidence).toEqual(before.evidence);expect(v.translation).toBe(before.translation);expect(v.answer).toBe(before.answer);expect(v.passage).toBe(before.passage);}
 });
 it('审阅22题24候选，保留14题，原图与改图只在本地核对',()=>{
  const r=read('source/question-revisions/review-082-report.json');
  expect(r.manual.questionCount).toBe(22);expect(r.manual.sourceCandidatesReviewed).toBe(24);expect(r.manual.revisedQuestionCount).toBe(8);
  expect(r.manual.questionReviews.filter((v:any)=>v.decision==='retained')).toHaveLength(14);
  expect(r.manual.pdfPagesVisuallyReviewed).toEqual([96,97,98,99]);expect(r.manual.pdfSourceBlocksTextMatched).toBe(7);
  expect(r.remainingQuestionReviews).toBe(1112);expect(r.fullQuestionBankHumanReview).toBe(false);
 });
});
