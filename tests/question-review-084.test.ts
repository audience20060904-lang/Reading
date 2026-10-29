import {readFileSync} from 'node:fs';
import {describe,it,expect} from 'vitest';
const read=(p:string)=>JSON.parse(readFileSync(p,'utf8'));
const all=read('src/data/question-revision-catalog.json').questions;
const q=(id:string)=>all.find((v:any)=>v.id===id);
const old=read('source/question-revisions/review-084-baseline.json').questions;
const b=(id:string)=>old.find((v:any)=>v.id===id);
describe('第八十四批：季后赛时序、归属和条件',()=>{
 it('罚球后的加时及主客顺序均可定位，原定位保持',()=>{
  const now=q('q-c09-074');expect(now.evidence.slice(0,2)).toEqual(b(now.id).evidence);
  expect(now.evidence[2].quote).toContain('toward the end of regulation and the game went into overtime');
  expect(now.evidence[0].quote).toContain('game five in Phoenix');
  expect(now.evidence[1].quote).toContain('game six at home and game seven in Phoenix');
 });
 it('罕见逆转同时包括种子与五场、七场两种比分',()=>{
  const e=q('q-c09-076').evidence[0],before=b('q-c09-076').evidence[0];
  for(const term of ['number-six-seeded','1-2 in a best of five','1-3 in a best of seven'])expect(e.quote).toContain(term);
  expect(e.quote).toContain(before.quote);expect(e.sentenceIds).toEqual(before.sentenceIds);expect(e.sources).toEqual(before.sources);
 });
 it('排除项不提前要求其他轮次种子或球员身份',()=>{
  expect(q('qe-c09-0138').analyses[1]).toContain('未给 Utah 第六种子身份');
  expect(q('qe-c09-0138').analyses[3]).toContain('轮次不同');
  expect(q('qe-c09-0141').analyses[1]).not.toContain('前锋');
  expect(q('qe-c09-0141').analyses[2]).not.toContain('球员');
  expect(q('q-c09-077').vocabulary[0].context).toContain('不表示绝无胜算');
 });
 it('审阅22题24候选，11题保留，答案原文和审阅界限保持',()=>{
  const r=read('source/question-revisions/review-084-report.json');
  expect(r.manual.questionCount).toBe(22);expect(r.manual.sourceCandidatesReviewed).toBe(24);expect(r.manual.revisedQuestionCount).toBe(11);
  expect(r.manual.questionReviews.filter((v:any)=>v.decision==='retained')).toHaveLength(11);
  expect(r.manual.pdfPagesVisuallyReviewed).toEqual([100,101,102]);expect(r.manual.pdfSourceBlocksTextMatched).toBe(6);
  expect(r.remainingQuestionReviews).toBe(1071);expect(r.fullQuestionBankHumanReview).toBe(false);
  for(const before of old){expect(q(before.id).answer).toBe(before.answer);expect(q(before.id).passage).toBe(before.passage);}
 });
});
