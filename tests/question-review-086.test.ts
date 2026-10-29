import {readFileSync} from 'node:fs';
import {describe,it,expect} from 'vitest';
const read=(p:string)=>JSON.parse(readFileSync(p,'utf8'));
const all=read('src/data/question-revision-catalog.json').questions;
const frozen=read('source/question-revisions/review-086-current-questions.json').questions;
const q=(id:string)=>all.find((v:any)=>v.id===id)??frozen.find((v:any)=>v.id===id);
const old=read('source/question-revisions/review-086-baseline.json').questions;
const b=(id:string)=>old.find((v:any)=>v.id===id);
describe('第八十六批：模拟比较、调查偏好与专家归属',()=>{
 it('调查引文包含偏好、样本和日期，旧引身份保留',()=>{
  const e=q('q-c10-006').evidence[0],before=b('q-c10-006').evidence[0];
  for(const term of ['fall 2019','585 UVA students','chose the psychologically rich life','what year of college'])expect(e.quote).toContain(term);
  expect(e.quote).toContain(before.quote);expect(e.sentenceIds).toEqual(before.sentenceIds);expect(e.sources).toEqual(before.sources);
  expect(q('q-c10-006').evidence[1]).toEqual(b('q-c10-006').evidence[1]);
 });
 it('保留近似比较和调查倾向，当前排序不依赖未显示表格数值',()=>{
  const sim=q('q-c10-005');expect(sim.passage).toContain('almost identical');expect(sim.options[sim.answer]).toContain('closely matched');
  expect(q('q-c10-007').analyses[3]).not.toContain('33.9');expect(q('q-c10-007').analyses[3]).not.toContain('图4');
  expect(q('q-c10-008').analyses[3]).toContain('seem、tend');expect(q('q-c10-008').analyses[3]).toContain('并未描述对同一批人的四年追踪');
 });
 it('人物和代词只据当前信息，不提前借下段概率推测',()=>{
  expect(q('qe-c10-0010').analyses[2]).not.toContain('后例');
  expect(q('qe-c10-0019').analyses[3]).toContain('承接紧前点名');expect(q('qe-c10-0019').analyses[3]).not.toContain('后面');
  expect(q('qe-c10-0020').analyses[0]).not.toContain('Krebs');expect(q('qe-c10-0020').analyses[3]).not.toContain('项目');
  expect(q('qe-c10-0022').analyses[2]).not.toContain('probably');expect(q('qe-c10-0022').analyses[2]).toContain('当前没有提供');
 });
 it('21题23候选有11题保留，原文、答案与审阅界限保持',()=>{
  const r=read('source/question-revisions/review-086-report.json');
  expect(r.manual.questionCount).toBe(21);expect(r.manual.sourceCandidatesReviewed).toBe(23);expect(r.manual.revisedQuestionCount).toBe(10);
  expect(r.manual.questionReviews.filter((v:any)=>v.decision==='retained')).toHaveLength(11);
  expect(r.manual.pdfPagesVisuallyReviewed).toEqual([103,104,105]);expect(r.manual.pdfSourceBlocksTextMatched).toBe(7);
  expect(r.remainingQuestionReviews).toBe(1027);expect(r.fullQuestionBankHumanReview).toBe(false);
  for(const before of old){expect(q(before.id).answer).toBe(before.answer);expect(q(before.id).passage).toBe(before.passage);}
 });
});
