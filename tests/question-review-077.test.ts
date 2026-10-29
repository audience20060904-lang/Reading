import {readFileSync} from 'node:fs';
import {describe,it,expect} from 'vitest';
const read=(p:string)=>JSON.parse(readFileSync(p,'utf8'));
const all=read('src/data/question-revision-catalog.json').questions;
const q=(id:string)=>all.find((v:any)=>v.id===id);
const old=read('source/question-revisions/review-077-baseline.json').questions;
const b=(id:string)=>old.find((v:any)=>v.id===id);

describe('第七十七批：限定、类比映射和叙事冲突',()=>{
 it('间接丰富的可能性与not all限定同时有原文证据',()=>{
  const v=q('qe-c09-0028');expect(v.evidence[0]).toEqual(b(v.id).evidence[0]);
  expect(v.evidence[0].quote).toContain('possible');
  expect(v.evidence[1].quote).toBe('But not all reading or watching experiences are rich.');
  expect(v.options[v.answer]).toContain('without every such experience necessarily doing so');
 });
 it('类比两侧与some和seem限定完整，旧引用身份保持',()=>{
  const v=q('q-c09-018'),before=b(v.id);
  expect(v.evidence[0].quote).toMatch(/^Just as material wealth/);
  expect(v.evidence[0].quote).toContain('directly or indirectly');
  expect(v.evidence[0].sentenceIds).toEqual(before.evidence[0].sentenceIds);
  expect(v.evidence[0].sources).toEqual(before.evidence[0].sources);
  expect(v.evidence[1]).toEqual(before.evidence[1]);
  expect(v.evidence[2].quote).toContain('Some sensation-seekers');
  expect(v.evidence[2].quote).toContain('do not seem');
  expect(v.evidence[3].quote).toBe('They constantly need new experiences.');
  const saving=q('q-c09-019');expect(saving.evidence[0].quote).toContain('need to save money');
  expect(saving.evidence[0].quote).toContain(b(saving.id).evidence[0].quote);
 });
 it('四人同一事件与同等说服力都可定位，解析不用未显示条件或考试标签',()=>{
  const v=q('q-c09-021'),before=b(v.id);
  expect(v.evidence[0].quote).toContain('a single event');
  expect(v.evidence[0].quote).toContain('four main characters');
  expect(v.evidence[0].sentenceIds).toEqual(before.evidence[0].sentenceIds);
  expect(v.evidence[0].sources).toEqual(before.evidence[0].sources);
  expect(v.evidence[1].quote).toContain('contradict the previous one just as convincingly');
  expect(q('q-c09-017').analyses[3]).not.toContain('IELTS');
  expect(q('qe-c09-0037').analyses[1]).not.toContain('沉浸');
  expect(q('qe-c09-0039').analyses[0]).not.toContain('网站');
 });
 it('审阅21题，14题保留，原文和所有旧答案位置不变',()=>{
  const r=read('source/question-revisions/review-077-report.json');
  expect(r.manual.questionCount).toBe(21);expect(r.manual.sourceCandidatesReviewed).toBe(23);
  expect(r.manual.revisedQuestionCount).toBe(7);expect(r.manual.questionReviews.filter((v:any)=>v.decision==='retained')).toHaveLength(14);
  expect(r.manual.pdfPagesVisuallyReviewed).toEqual([91,92]);expect(r.manual.pdfSourceBlocksTextMatched).toBe(4);
  expect(r.remainingQuestionReviews).toBe(1224);expect(r.fullQuestionBankHumanReview).toBe(false);
  expect(r.manual.questionReviews.find((v:any)=>v.questionId==='q-c09-020').decision).toBe('retained');
  for(const before of old){expect(q(before.id).answer).toBe(before.answer);expect(q(before.id).passage).toBe(before.passage);}
 });
});
