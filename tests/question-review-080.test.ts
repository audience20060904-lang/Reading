import {readFileSync} from 'node:fs';
import {describe,it,expect} from 'vitest';
const read=(p:string)=>JSON.parse(readFileSync(p,'utf8'));
const all=read('src/data/question-revision-catalog.json').questions;
const q=(id:string)=>all.find((v:any)=>v.id===id);
const old=read('source/question-revisions/review-080-baseline.json').questions;
const b=(id:string)=>old.find((v:any)=>v.id===id);
describe('第八十批：当前证据、可能性与图形条件',()=>{
 it('闲谈正确项中的独立深思及分心均可定位，保留旧来源身份',()=>{
  const v=q('q-c09-036'),before=b(v.id);
  expect(v.evidence[0].quote).toContain('passing the word along');
  expect(v.evidence[0].quote).toContain(before.evidence[0].quote);
  expect(v.evidence[0].sentenceIds).toEqual(before.evidence[0].sentenceIds);
  expect(v.evidence[0].sources).toEqual(before.evidence[0].sources);
  expect(v.evidence[1].quote).toContain('without thinking deeply on our own');
  expect(v.evidence[2].quote).toContain('constant possibility of distraction');
  const c=q('q-c09-037');expect(c.evidence[0].quote).toContain('Between our to-do lists and endless distractions');expect(c.evidence[0].quote).toContain('rarely');
 });
 it('maybe只据当前背景知识，解析不夹候选计数或后文研究',()=>{
  const v=q('q-c09-039');expect(v.options[v.answer]).toContain('background knowledge just mentioned');expect(v.options[v.answer]).not.toContain('biography');
  expect(v.analyses[3]).not.toContain('上一段');
  expect(q('qe-c09-0078').analyses[3]).not.toContain('候选');
  expect(q('qe-c09-0080').analyses[0]).not.toContain('缩写');
  expect(q('qe-c09-0083').analyses[0]).not.toContain('Scott');
  expect(q('qe-c09-0087').analyses[2]).not.toContain('后文');
 });
 it('数量vs对比和对称同质程度译清，现有操纵证据不重写',()=>{
  for(const id of ['q-c09-042','qe-c09-0085','qe-c09-0086','qe-c09-0087']){
   expect(q(id).translation).toContain('元素在多大程度上对称且同质');
   expect(q(id).translation).toContain('一至五个元素与大量元素的对比');
   expect(q(id).translation).not.toContain('或许多个');
  }
  expect(q('q-c09-042').evidence).toEqual(b('q-c09-042').evidence);
  expect(q('qe-c09-0086').options[q('qe-c09-0086').answer]).toBe('Complex and symmetrical.');
 });
 it('25题25候选实际审阅，14题保留，答案与原始片段不改',()=>{
  const r=read('source/question-revisions/review-080-report.json');
  expect(r.manual.questionCount).toBe(25);expect(r.manual.sourceCandidatesReviewed).toBe(25);expect(r.manual.revisedQuestionCount).toBe(11);
  expect(r.manual.questionReviews.filter((v:any)=>v.decision==='retained')).toHaveLength(14);
  expect(r.manual.pdfPagesVisuallyReviewed).toEqual([94,95]);expect(r.manual.pdfSourceBlocksTextMatched).toBe(5);
  expect(r.remainingQuestionReviews).toBe(1156);expect(r.fullQuestionBankHumanReview).toBe(false);
  for(const before of old){expect(q(before.id).answer).toBe(before.answer);expect(q(before.id).passage).toBe(before.passage);}
 });
});
