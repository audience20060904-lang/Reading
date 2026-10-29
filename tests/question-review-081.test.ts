import {readFileSync} from 'node:fs';
import {describe,it,expect} from 'vitest';
const read=(p:string)=>JSON.parse(readFileSync(p,'utf8'));
const all=read('src/data/question-revision-catalog.json').questions;
const q=(id:string)=>all.find((v:any)=>v.id===id);
const old=read('source/question-revisions/review-081-baseline.json').questions;
const b=(id:string)=>old.find((v:any)=>v.id===id);
describe('第八十一批：各自比较基准及当前片段',()=>{
 it('两种体裁分别比较未大量读该体裁者，不误作直接组间排名',()=>{
  const v=q('q-c09-051');expect(v.options[v.answer]).toContain('respective genre in childhood');
  expect(v.options[v.answer]).toContain('heavy literary-fiction readers');expect(v.options[v.answer]).toContain('heavy romance readers');
  expect(v.analyses[1]).toContain('各以未大量阅读相应体裁者为对照');
  for(const i of [0,1]){
   expect(v.evidence[i].quote).toContain('than those who did not');
   expect(v.evidence[i].quote).toContain(b(v.id).evidence[i].quote);
   expect(v.evidence[i].sentenceIds).toEqual(b(v.id).evidence[i].sentenceIds);
   expect(v.evidence[i].sources).toEqual(b(v.id).evidence[i].sources);
  }
  expect(q('qe-c09-0102').analyses[3]).toContain('分别与未大量阅读相应体裁者比较');
 });
 it('完整调查句保留超过五千与自报三项，原来源身份保持',()=>{
  const v=q('q-c09-049'),before=b(v.id);expect(v.evidence[0].quote).toContain('So we asked over 5,000 people');
  expect(v.evidence[0].quote).toContain('perceived levels of psychological richness');
  expect(v.evidence[0].quote).toContain(before.evidence[0].quote);
  expect(v.evidence[0].sentenceIds).toEqual(before.evidence[0].sentenceIds);expect(v.evidence[0].sources).toEqual(before.evidence[0].sources);
 });
 it('姓名与实验预测解析不夹候选误分或未显示后研究',()=>{
  expect(q('qe-c09-0089').analyses[0]).not.toContain('句子');
  expect(q('qe-c09-0090').analyses[2]).not.toContain('误断');
  expect(q('q-c09-045').analyses[1]).not.toContain('下一部分');
  expect(q('qe-c09-0094').analyses[2]).not.toContain('前面');
  expect(q('qe-c09-0095').analyses[1]).not.toContain('前项');
  expect(q('qe-c09-0096').analyses[0]).not.toContain('前面画家');
 });
 it('22题24候选审阅，11题保留，答案与原文未变',()=>{
  const r=read('source/question-revisions/review-081-report.json');
  expect(r.manual.questionCount).toBe(22);expect(r.manual.sourceCandidatesReviewed).toBe(24);expect(r.manual.revisedQuestionCount).toBe(11);
  expect(r.manual.questionReviews.filter((v:any)=>v.decision==='retained')).toHaveLength(11);
  expect(r.manual.pdfPagesVisuallyReviewed).toEqual([95,96,97]);expect(r.manual.pdfSourceBlocksTextMatched).toBe(6);
  expect(r.remainingQuestionReviews).toBe(1134);expect(r.fullQuestionBankHumanReview).toBe(false);
  for(const before of old){expect(q(before.id).answer).toBe(before.answer);expect(q(before.id).passage).toBe(before.passage);}
 });
});
