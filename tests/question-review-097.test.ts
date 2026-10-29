import {readFileSync} from 'node:fs';
import {describe,it,expect} from 'vitest';
const read=(p:string)=>JSON.parse(readFileSync(p,'utf8'));
const all=read('src/data/question-revision-catalog.json').questions;
const q=(id:string)=>all.find((v:any)=>v.id===id);
const old=read('source/question-revisions/review-097-baseline.json').questions;
const b=(id:string)=>old.find((v:any)=>v.id===id);
describe('第九十七批：通勤比较与个案归因',()=>{
 it('自报结果完整指明独处和控制比较，旧引用身份不动',()=>{
  const now=q('q-c10-101'),before=b(now.id);expect(now.evidence[0].quote).toContain('than those assigned to the solitude or control conditions');expect(now.evidence[0].quote).toContain(before.evidence[0].quote);expect(now.evidence[0].sentenceIds).toEqual(before.evidence[0].sentenceIds);expect(now.evidence[0].sources).toEqual(before.evidence[0].sources);
 });
 it('105人的题干只问当前想象任务，回卷数字选项不借后文',()=>{
  const imagine=q('qe-c10-0177');expect(imagine.prompt).toContain('task were the additional 105');expect(imagine.options[0]).toContain('Imagine how they would feel');expect(imagine.options[0]).not.toContain('actual ride');
  expect(q('qe-c10-0176').options[1]).toBe('One hundred and five.');expect(q('qe-c10-0172').analyses[0]).not.toContain('回卷');expect(q('qe-c10-0173').analyses[3]).not.toContain('车程末');
 });
 it('Jobs归因和向广泛证据过渡完整定位',()=>{
  const jobs=q('q-c10-104');expect(jobs.evidence[0].quote).toContain('Yet, years later, he credits');
  const general=q('q-c10-105');expect(general.evidence[1].quote).toContain('have amassed evidence');expect(general.evidence[1].quote).toContain('seem to increase creativity');
  for(const [id,index]of [['q-c10-104',0],['q-c10-105',1]] as const){expect(q(id).evidence[index].sources).toEqual(b(id).evidence[index].sources);expect(q(id).evidence[index].sentenceIds).toEqual(b(id).evidence[index].sentenceIds);}
 });
 it('22题24候选保留11题，额外120页为原段上下文',()=>{
  const r=read('source/question-revisions/review-097-report.json');expect(r.manual.questionCount).toBe(22);expect(r.manual.sourceCandidatesReviewed).toBe(24);expect(r.manual.revisedQuestionCount).toBe(11);expect(r.manual.questionReviews.filter((v:any)=>v.decision==='retained')).toHaveLength(11);
  expect(r.manual.pdfPagesVisuallyReviewed).toEqual([118,119,120]);expect(r.manual.pdfPagesForQuestionEvidence).toEqual([118,119]);expect(r.manual.additionalParagraphContextPages).toEqual([120]);expect(r.manual.pdfSourceBlocksTextMatched).toBe(6);expect(r.remainingQuestionReviews).toBe(787);expect(r.fullQuestionBankHumanReview).toBe(false);
  for(const before of old){expect(q(before.id).answer).toBe(before.answer);expect(q(before.id).passage).toBe(before.passage);}
 });
});
