import {readFileSync} from 'node:fs';
import {describe,it,expect} from 'vitest';
const read=(p:string)=>JSON.parse(readFileSync(p,'utf8'));
const all=read('src/data/question-revision-catalog.json').questions;
const q=(id:string)=>all.find((v:any)=>v.id===id);
const old=read('source/question-revisions/review-095-baseline.json').questions;
const b=(id:string)=>old.find((v:any)=>v.id===id);
describe('第九十五批：节目观察、所有权和未来计划',()=>{
 it('观看范围和典型估值比率完整入证，旧引身份不动',()=>{
  for(const id of ['q-c10-086','q-c10-088','q-c10-089']){const now=q(id),before=b(id);expect(now.evidence[0].quote).toContain(before.evidence[0].quote);expect(now.evidence[0].sources).toEqual(before.evidence[0].sources);expect(now.evidence[0].sentenceIds).toEqual(before.evidence[0].sentenceIds);}
  expect(q('q-c10-086').evidence[0].quote).toContain('every time I’ve watched');
  expect(q('q-c10-088').evidence[0].quote).toContain('Typically');
  expect(q('q-c10-089').evidence[0].quote).toContain('Once you own something');
 });
 it('假设买回及used价值预期有完整证据，首句结果题自足',()=>{
  const mug=q('q-c10-087');expect(mug.evidence[1].quote).toContain('less than $5');expect(mug.evidence[2].quote).toContain('a week later');expect(mug.evidence[2].quote).toContain('buy it back');
  const result=q('qe-c10-0146');expect(result.prompt).toContain('opening sentence report');expect(result.options[0]).toContain('Most people want substantially more than five dollars');expect(result.optionsZh[0]).toContain('多数人');
 });
 it('角色、人物和计划解析不借前后文或网站信息',()=>{
  expect(q('qe-c10-0144').options[0]).toBe('Bob Zajonc.');expect(q('qe-c10-0144').options[2]).toBe('Johannes Kepler.');
  expect(q('qe-c10-0141').analyses[0]).not.toContain('后面');expect(q('qe-c10-0142').vocabulary[0].context).not.toContain('联系人');
  expect(q('qe-c10-0152').analyses[0]).not.toContain('later');expect(q('qe-c10-0153').analyses[3]).not.toContain('后面');
 });
 it('20题22候选保留8题，答案和原文不变',()=>{
  const r=read('source/question-revisions/review-095-report.json');expect(r.manual.questionCount).toBe(20);expect(r.manual.sourceCandidatesReviewed).toBe(22);expect(r.manual.revisedQuestionCount).toBe(12);
  expect(r.manual.questionReviews.filter((v:any)=>v.decision==='retained')).toHaveLength(8);expect(r.manual.pdfPagesVisuallyReviewed).toEqual([116,117]);expect(r.manual.pdfSourceBlocksTextMatched).toBe(4);
  expect(r.remainingQuestionReviews).toBe(832);expect(r.fullQuestionBankHumanReview).toBe(false);
  for(const before of old){expect(q(before.id).answer).toBe(before.answer);expect(q(before.id).passage).toBe(before.passage);}
 });
});
