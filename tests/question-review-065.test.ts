import {readFileSync} from 'node:fs';
import {describe,it,expect} from 'vitest';
const read=(p:string)=>JSON.parse(readFileSync(p,'utf8'));
const catalog=read('src/data/question-revision-catalog.json').questions;
const q=(id:string)=>catalog.find((v:any)=>v.id===id);
const baseline=read('source/question-revisions/review-065-baseline.json').questions;
const original=(id:string)=>baseline.find((v:any)=>v.id===id);
const book=read('public/data/book.json');

describe('第六十五批：当前可见条件、观点归属与可能性',()=>{
 it('家庭交友证据包含伴侣和孩子条件，旧引用的来源身份不变',()=>{
  const v=q('q-c07-056'),b=original(v.id);
  for(let i=0;i<b.evidence.length;i++){
   expect(v.evidence[i].quote).toContain(b.evidence[i].quote);
   expect(v.evidence[i].sentenceIds).toEqual(b.evidence[i].sentenceIds);
   expect(v.evidence[i].sources).toEqual(b.evidence[i].sources);
  }
  expect(v.evidence[0].quote).toContain('When you add a child or two');
  expect(v.evidence[0].quote).toContain('can feel nearly impossible');
  expect(v.evidence[1].quote).toContain('really challenging');
  const s=book.sentences.find((s:any)=>s.id===v.sentenceIds[0]);
  expect(v.evidence.at(-1)).toEqual({quote:s.text,sentenceIds:[s.id],sources:s.sources});
  expect(s.sources.map((r:any)=>r.pdfPage)).toEqual([75,76]);
 });
 it('D’Cruz解释的证据保留同一句观点归属，旧第二引用原样保留',()=>{
  const v=q('q-c07-059'),b=original(v.id);
  expect(v.evidence[0].quote).toContain('D’Cruz argues');
  expect(v.evidence[0].quote).toContain('but nonetheless');
  expect(v.evidence[0].sentenceIds).toEqual(b.evidence[0].sentenceIds);
  expect(v.evidence[0].sources).toEqual(b.evidence[0].sources);
  expect(v.evidence[1]).toEqual(b.evidence[1]);
 });
 it('假想旅人选项中英身份一致，感受题不要求未显示的人物设定',()=>{
  const p=q('qe-c07-0094');expect(p.options[3]).toContain('hypothetical traveller');
  expect(p.optionsZh[3]).toContain('假想旅人');expect(p.optionsZh[3]).not.toContain('而非');
  const v=q('qe-c07-0098');expect(v.passage).not.toContain('hypothetical');
  expect(v.options[v.answer]).not.toContain('hypothetical');
  expect(v.optionsZh[v.answer]).not.toContain('假想');
  expect(v.options[v.answer]).toContain('Immediately after the train leaves Dresden');
 });
 it('共享译文保留BFF词义和could通话可能，正确时点不被改成已经通话',()=>{
  for(const id of ['q-c07-054','qe-c07-0088','qe-c07-0089','qe-c07-0090']){
   expect(q(id).translation).toContain('B.F.F.（永远最好的朋友）');
   expect(q(id).translation).toContain('可能悄悄出现');
   expect(q(id).translation).toContain('至少暂时');
  }
  for(const id of ['q-c07-058','qe-c07-0096','qe-c07-0097']){
   expect(q(id).translation).toContain('心想自己可以给朋友打个电话');
   expect(q(id).translation).not.toContain('只要打电话');
  }
  expect(q('qe-c07-0088').options[1]).toContain('the 49-team');
 });
 it('冻结23题24候选且仅18题修订，保留5题，77页仅为跨页上下文',()=>{
  const r=read('source/question-revisions/review-065-report.json');
  expect(r.manual.questionCount).toBe(23);expect(r.manual.sourceCandidatesReviewed).toBe(24);
  expect(r.manual.revisedQuestionCount).toBe(18);
  expect(r.manual.questionReviews.filter((v:any)=>v.decision==='retained')).toHaveLength(5);
  expect(r.manual.pdfPagesForQuestionEvidence).toEqual([75,76]);
  expect(r.manual.additionalParagraphContextPages).toEqual([77]);
  expect(r.remainingQuestionReviews).toBe(1474);expect(r.fullQuestionBankHumanReview).toBe(false);
 });
});
