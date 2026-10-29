import {readFileSync} from 'node:fs';
import {describe,it,expect} from 'vitest';
const read=(p:string)=>JSON.parse(readFileSync(p,'utf8'));
const all=read('src/data/question-revision-catalog.json').questions;
const q=(id:string)=>all.find((v:any)=>v.id===id);
const old=read('source/question-revisions/review-083-baseline.json').questions;
const b=(id:string)=>old.find((v:any)=>v.id===id);
describe('第八十三批：结果、时序和书中体育叙述',()=>{
 it('更有趣的结果及常规赛球队归属完整，原定位不动',()=>{
  for(const [id,term] of [['q-c09-062','more interesting, intriguing, and refreshing'],['q-c09-070','The Rockets ultimately ended the regular season']] as const){
   const e=q(id).evidence[0],before=b(id).evidence[0];expect(e.quote).toContain(term);expect(e.quote).toContain(before.quote);expect(e.sentenceIds).toEqual(before.sentenceIds);expect(e.sources).toEqual(before.sources);
   expect(q(id).evidence[1]).toEqual(b(id).evidence[1]);
  }
  const sport=q('q-c09-066');expect(sport.evidence[0]).toEqual(b(sport.id).evidence[0]);expect(sport.evidence[1].quote).toContain('could miss a routine groundball');expect(sport.evidence[2].quote).toContain('at the least expected moments');
 });
 it('Perhaps只据当前多物，不借下一段；首冠与1995叙事时序准确',()=>{
  expect(q('qe-c09-0119').analyses[1]).not.toContain('后文');
  expect(q('qe-c09-0126').analyses[1]).not.toContain('随后对手');
  expect(q('qe-c09-0127').analyses[1]).toContain('1995是当前引入');
  expect(q('qe-c09-0127').analyses[1]).not.toContain('后面谈');
  expect(q('qe-c09-0129').analyses[1]).toContain('没有在这里描述 Utah 后来季后赛的结果');
 });
 it('干扰项贴合历史叙述和熟词义，去网站赛况与读者通信',()=>{
  expect(q('qe-c09-0124').options[2]).toContain('next World Series');expect(q('qe-c09-0124').options[2]).not.toContain('website');
  expect(q('qe-c09-0128').options[2]).toContain('criticism of their performance');expect(q('qe-c09-0128').options[2]).not.toContain('reader');
 });
 it('审阅19题22候选，10题保留，来源与答案位置保留',()=>{
  const r=read('source/question-revisions/review-083-report.json');
  expect(r.manual.questionCount).toBe(19);expect(r.manual.sourceCandidatesReviewed).toBe(22);expect(r.manual.revisedQuestionCount).toBe(9);
  expect(r.manual.questionReviews.filter((v:any)=>v.decision==='retained')).toHaveLength(10);
  expect(r.manual.pdfPagesVisuallyReviewed).toEqual([99,100,101]);expect(r.manual.pdfSourceBlocksTextMatched).toBe(6);
  expect(r.remainingQuestionReviews).toBe(1093);expect(r.fullQuestionBankHumanReview).toBe(false);
  for(const before of old){expect(q(before.id).answer).toBe(before.answer);expect(q(before.id).passage).toBe(before.passage);}
 });
});
