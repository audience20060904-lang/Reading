import {readFileSync} from 'node:fs';
import {describe,it,expect} from 'vitest';
const read=(p:string)=>JSON.parse(readFileSync(p,'utf8'));
const all=read('src/data/question-revision-catalog.json').questions;
const q=(id:string)=>all.find((v:any)=>v.id===id);
const old=read('source/question-revisions/review-079-baseline.json').questions;
const b=(id:string)=>old.find((v:any)=>v.id===id);
describe('第七十九批：合目的性、同位解释和引文否定',()=>{
 it('哲学让步保持，purposive for itself译自身具有合目的性',()=>{
  for(const id of ['q-c09-031','qe-c09-0062']){
   expect(q(id).translation).toContain('自身具有合目的性的表现方式');
   expect(q(id).translation).toContain('尽管没有［明确的］目的，却促进');
   expect(q(id).evidence).toEqual(b(id).evidence);
  }
  expect(q('qe-c09-0062').analyses[1]).not.toContain('前段');
 });
 it('intuition与心中感受是解释关系，haven’t否定不弱化成未必',()=>{
  for(const id of ['q-c09-033','qe-c09-0065','qe-c09-0066'])expect(q(id).translation).toContain('直觉，也就是我们心中所感到的东西');
  expect(q('qe-c09-0065').options[2]).toBe('Intuition, described as what we feel in our hearts.');
  for(const id of ['q-c09-035','qe-c09-0070']){
   expect(q(id).translation).toContain('你并没有学到新事实，却获得了新体验');
   expect(q(id).translation).not.toContain('你未必学到');
  }
 });
 it('人物条件论辩和物质生存对照完整定位，原引文身份保持',()=>{
  const v=q('q-c09-029');expect(v.evidence[0]).toEqual(b(v.id).evidence[0]);
  expect(v.evidence[1].quote).toBe('She’s nice because she’s rich.');
  expect(v.evidence[2].quote).toContain('if I had all this money');
  const c=q('q-c09-032'),before=b(c.id);
  expect(c.evidence[0].quote).toContain('We can eat, sleep, look at screens, make money');
  expect(c.evidence[0].quote).toContain(before.evidence[0].quote);
  expect(c.evidence[0].sentenceIds).toEqual(before.evidence[0].sentenceIds);
  expect(c.evidence[0].sources).toEqual(before.evidence[0].sources);
 });
 it('19题22候选实际审阅，9题保留，答案与原文保持',()=>{
  const r=read('source/question-revisions/review-079-report.json');
  expect(r.manual.questionCount).toBe(19);expect(r.manual.sourceCandidatesReviewed).toBe(22);expect(r.manual.revisedQuestionCount).toBe(10);
  expect(r.manual.questionReviews.filter((v:any)=>v.decision==='retained')).toHaveLength(9);
  expect(r.manual.pdfPagesVisuallyReviewed).toEqual([93,94]);expect(r.manual.pdfSourceBlocksTextMatched).toBe(5);
  expect(r.remainingQuestionReviews).toBe(1181);expect(r.fullQuestionBankHumanReview).toBe(false);
  for(const before of old){expect(q(before.id).answer).toBe(before.answer);expect(q(before.id).passage).toBe(before.passage);}
 });
});
