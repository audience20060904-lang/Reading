import {readFileSync} from 'node:fs';
import {describe,it,expect} from 'vitest';
const read=(p:string)=>JSON.parse(readFileSync(p,'utf8'));
const all=read('src/data/question-revision-catalog.json').questions;
const q=(id:string)=>all.find((v:any)=>v.id===id);
const old=read('source/question-revisions/review-101-baseline.json').questions;
const b=(id:string)=>old.find((v:any)=>v.id===id);
describe('第一百零一批：传记范围、日期和当前身份',()=>{
 it('潜力解释、个人故事和逗留太晚的完整句可定位',()=>{
  expect(q('q-c11-007').evidence[0].quote).toContain('Nietzsche credited his illness');expect(q('q-c11-007').evidence[0].quote).toContain('suggesting');expect(q('q-c11-010').evidence[0].quote).toContain('But Kahneman');expect(q('q-c11-011').evidence[1].quote).toContain('I had gone to play with a Christian friend');
  for(const [id,index]of [['q-c11-007',0],['q-c11-010',0],['q-c11-011',1]] as const){expect(q(id).evidence[index].quote).toContain(b(id).evidence[index].quote);expect(q(id).evidence[index].sources).toEqual(b(id).evidence[index].sources);expect(q(id).evidence[index].sentenceIds).toEqual(b(id).evidence[index].sentenceIds);}
 });
 it('题干不要求未显示姓名，数字干扰项不借另一传记',()=>{
  expect(q('qe-c11-0012').prompt).toContain('the scholar');expect(q('qe-c11-0023').prompt).toContain('the narrator');expect(q('qe-c11-0021').options[2]).toBe('Twenty-four.');expect(q('qe-c11-0018').analyses[3]).not.toContain('后文');expect(q('qe-c11-0022').analyses[2]).not.toContain('父亲');
 });
 it('共享译文用间接叙述保留约略时间，去续后段内部说明',()=>{
  for(const id of ['q-c11-010','qe-c11-0021','qe-c11-0022']){expect(q(id).translation).toContain('说那应该是1941年底或1942年初');expect(q(id).translation).not.toContain('引语续后段');}
  expect(q('q-c11-011').analyses[3]).not.toContain('后段');expect(q('qe-c11-0023').analyses[1]).not.toContain('士兵');
 });
 it('20题24候选保留10题，日期核对不改原文或旧答案',()=>{
  const r=read('source/question-revisions/review-101-report.json');expect(r.manual.questionCount).toBe(20);expect(r.manual.sourceCandidatesReviewed).toBe(24);expect(r.manual.revisedQuestionCount).toBe(10);expect(r.manual.questionReviews.filter((v:any)=>v.decision==='retained')).toHaveLength(10);expect(r.manual.pdfPagesVisuallyReviewed).toEqual([122,123,124]);expect(r.manual.pdfSourceBlocksTextMatched).toBe(5);expect(r.remainingQuestionReviews).toBe(703);expect(r.fullQuestionBankHumanReview).toBe(false);
  for(const before of old){expect(q(before.id).answer).toBe(before.answer);expect(q(before.id).passage).toBe(before.passage);}
 });
});
