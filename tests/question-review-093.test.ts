import {readFileSync} from 'node:fs';
import {describe,it,expect} from 'vitest';
const read=(p:string)=>JSON.parse(readFileSync(p,'utf8'));
const all=read('src/data/question-revision-catalog.json').questions;
const q=(id:string)=>all.find((v:any)=>v.id===id);
const old=read('source/question-revisions/review-093-baseline.json').questions;
const b=(id:string)=>old.find((v:any)=>v.id===id);
describe('第九十三批：比较两侧、回忆时态和想象条件',()=>{
 it('城市对照两侧和统计控制的比较对象齐全，旧引不动',()=>{
  const city=q('q-c10-063');expect(city.evidence[0]).toEqual(b(city.id).evidence[0]);expect(city.evidence[1].quote).toContain('Tokyo and Osaka');expect(city.evidence[2].quote).toContain('In American suburbs');
  const controls=q('q-c10-069');expect(controls.evidence[0]).toEqual(b(controls.id).evidence[0]);expect(controls.evidence[1].quote).toContain('more national chain stores in mobile states than in stable states');
 });
 it('共享译文保留一次实际招呼和almost，题干不要求未显示身份',()=>{
  for(const id of ['q-c10-064','qe-c10-0112','qe-c10-0113','qe-c10-0114']){expect(q(id).translation).toContain('见到同一名学生时，我说：');expect(q(id).translation).not.toContain('我会说：');expect(q(id).translation).toContain('差点拥抱');}
  expect(q('q-c10-065').prompt).not.toContain('near-hug');expect(q('qe-c10-0115').prompt).not.toContain('student');expect(q('qe-c10-0114').analyses[3]).not.toContain('原候选');
 });
 it('旅行变化的当地基线、想象条件和模型应用可以定位',()=>{
  const warm=q('q-c10-064'),before=b(warm.id);expect(warm.evidence[0]).toEqual(before.evidence[0]);expect(warm.evidence[1].quote).toContain(before.evidence[1].quote);expect(warm.evidence[1].sources).toEqual(before.evidence[1].sources);expect(warm.evidence[1].sentenceIds).toEqual(before.evidence[1].sentenceIds);expect(warm.evidence[2].quote).toContain('never went to Starbucks');expect(warm.evidence[3].quote).toContain('very curt');
  const move=q('q-c10-073');expect(move.evidence[0]).toEqual(b(move.id).evidence[0]);expect(move.evidence[1].quote).toContain('thought about moving around frequently');expect(move.evidence[1].quote).toContain('a typical day');
  const model=q('q-c10-075');expect(model.evidence.slice(0,2)).toEqual(b(model.id).evidence);expect(model.evidence[2].quote).toContain('finding a partner');
 });
 it('23题25候选有9题保留，答案原文和审阅界限保持',()=>{
  const r=read('source/question-revisions/review-093-report.json');
  expect(r.manual.questionCount).toBe(23);expect(r.manual.sourceCandidatesReviewed).toBe(25);expect(r.manual.revisedQuestionCount).toBe(14);
  expect(r.manual.questionReviews.filter((v:any)=>v.decision==='retained')).toHaveLength(9);
  expect(r.manual.pdfPagesVisuallyReviewed).toEqual([113,114,115]);expect(r.manual.pdfSourceBlocksTextMatched).toBe(5);
  expect(r.remainingQuestionReviews).toBe(873);expect(r.fullQuestionBankHumanReview).toBe(false);
  for(const before of old){expect(q(before.id).answer).toBe(before.answer);expect(q(before.id).passage).toBe(before.passage);}
 });
});
