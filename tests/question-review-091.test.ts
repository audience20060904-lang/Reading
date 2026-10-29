import {readFileSync} from 'node:fs';
import {describe,it,expect} from 'vitest';
const read=(p:string)=>JSON.parse(readFileSync(p,'utf8'));
const all=read('src/data/question-revision-catalog.json').questions;
const q=(id:string)=>all.find((v:any)=>v.id===id);
const old=read('source/question-revisions/review-091-baseline.json').questions;
const b=(id:string)=>old.find((v:any)=>v.id===id);
describe('第九十一批：机制、条件预测和实验材料',()=>{
 it('路线到偶遇的机制完整入证，原引用身份不动',()=>{
  const now=q('q-c10-044'),e=now.evidence[1],before=b(now.id).evidence[1];
  expect(now.evidence[0]).toEqual(b(now.id).evidence[0]);expect(e.quote).toContain('physical and functional distance');expect(e.quote).toContain('probability of a chance meeting');
  expect(e.quote).toContain(before.quote);expect(e.sentenceIds).toEqual(before.sentenceIds);expect(e.sources).toEqual(before.sources);
 });
 it('跨材料结论包含汉字复现，原词和照片引用保留',()=>{
  const now=q('q-c10-051');expect(now.evidence.slice(0,2)).toEqual(b(now.id).evidence);expect(now.evidence[2].quote).toContain('replicated this initial finding with Chinese characters');
 });
 it('评分反差不写成因果，解析不借后段课堂或材料数量',()=>{
  expect(q('qe-c10-0087').analyses[2]).toContain('不证明词频单独造成偏好');expect(q('qe-c10-0088').analyses[1]).not.toContain('后续原书');expect(q('qe-c10-0089').analyses[3]).not.toContain('后文');
  expect(q('qe-c10-0086').analyses[2]).not.toContain('后面');expect(q('q-c10-050').analyses[2]).not.toContain('后续材料数量');
  expect(q('qe-c10-0094').analyses[1]).toContain('当前要求猜测好坏');expect(q('qe-c10-0092').analyses[3]).not.toContain('网站');
 });
 it('22题24候选有6题保留，答案原文和审阅界限保持',()=>{
  const r=read('source/question-revisions/review-091-report.json');
  expect(r.manual.questionCount).toBe(22);expect(r.manual.sourceCandidatesReviewed).toBe(24);expect(r.manual.revisedQuestionCount).toBe(16);
  expect(r.manual.questionReviews.filter((v:any)=>v.decision==='retained')).toHaveLength(6);
  expect(r.manual.pdfPagesVisuallyReviewed).toEqual([110,111,112]);expect(r.manual.pdfSourceBlocksTextMatched).toBe(6);
  expect(r.remainingQuestionReviews).toBe(916);expect(r.fullQuestionBankHumanReview).toBe(false);
  for(const before of old){expect(q(before.id).answer).toBe(before.answer);expect(q(before.id).passage).toBe(before.passage);}
 });
});
