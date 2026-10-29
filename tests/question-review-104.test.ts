import {readFileSync} from 'node:fs';
import {describe,it,expect} from 'vitest';
const read=(p:string)=>JSON.parse(readFileSync(p,'utf8'));
const all=read('src/data/question-revision-catalog.json').questions;
const q=(id:string)=>all.find((v:any)=>v.id===id);
const old=read('source/question-revisions/review-104-baseline.json').questions;
const b=(id:string)=>old.find((v:any)=>v.id===id);
describe('第一百零四批：损害两侧、调查与长期比较',()=>{
 it('正面评价同时有废屋证据，正确项只据当前引语',()=>{
  const contrast=q('q-c11-027');expect(contrast.evidence[0]).toEqual(b(contrast.id).evidence[0]);expect(contrast.evidence[1].quote).toContain('could still see abandoned homes');expect(q('q-c11-028').options[0]).toContain('quoted reflection');expect(q('qe-c11-0054').prompt).not.toContain('Joe');
  for(const id of ['q-c11-027','qe-c11-0053','qe-c11-0054','qe-c11-0055'])expect(q(id).translation).not.toContain('引语续后段');
 });
 it('分类完整、地区对照到So及基线到后来结果均可定位',()=>{
  expect(q('q-c11-032').evidence[0].quote).toContain('complete damage, half, partial, and none');expect(q('q-c11-031').evidence[1].quote).toContain('So this earthquake');expect(q('q-c11-034').evidence[1].quote).toContain('For instance, in 2001 Kobe residents');expect(q('q-c11-034').evidence[1].quote).toContain('than those whose houses had suffered no damage');
  for(const id of ['q-c11-031','q-c11-032','q-c11-034']){expect(q(id).evidence[0].quote).toContain(b(id).evidence[0].quote);expect(q(id).evidence[0].sources).toEqual(b(id).evidence[0].sources);expect(q(id).evidence[0].sentenceIds).toEqual(b(id).evidence[0].sentenceIds);}
 });
 it('年份干扰项不借后续研究，调查和休假分别核对',()=>{
  expect(q('qe-c11-0064').options[2]).toBe('1989, 1995, and 2000.');expect(q('qe-c11-0064').analyses[2]).not.toContain('另一个研究');expect(q('qe-c11-0063').options[0]).not.toContain('earthquake');expect(q('q-c11-032').analyses[0]).not.toContain('后续');
 });
 it('21题22候选保留9题，旧答案原文不变',()=>{
  const r=read('source/question-revisions/review-104-report.json');expect(r.manual.questionCount).toBe(21);expect(r.manual.sourceCandidatesReviewed).toBe(22);expect(r.manual.revisedQuestionCount).toBe(12);expect(r.manual.questionReviews.filter((v:any)=>v.decision==='retained')).toHaveLength(9);expect(r.manual.pdfPagesVisuallyReviewed).toEqual([126,127]);expect(r.manual.pdfSourceBlocksTextMatched).toBe(5);expect(r.remainingQuestionReviews).toBe(639);expect(r.fullQuestionBankHumanReview).toBe(false);
  for(const before of old){expect(q(before.id).answer).toBe(before.answer);expect(q(before.id).passage).toBe(before.passage);}
 });
});
