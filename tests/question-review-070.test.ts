import {readFileSync} from 'node:fs';
import {describe,it,expect} from 'vitest';
const read=(p:string)=>JSON.parse(readFileSync(p,'utf8'));
const all=read('src/data/question-revision-catalog.json').questions;
const q=(id:string)=>all.find((v:any)=>v.id===id);
const old=read('source/question-revisions/review-070-baseline.json').questions;
const b=(id:string)=>old.find((v:any)=>v.id===id);
describe('第七十批：当前证据、分配层级与平均产量',()=>{
 it('比较与人均产量证据补齐主语且旧引用身份不变',()=>{
  for(const id of ['q-c08-024','q-c08-028']){
   const v=q(id),previous=b(id);expect(v.evidence[0].quote).toContain(previous.evidence[0].quote);
   expect(v.evidence[0].sentenceIds).toEqual(previous.evidence[0].sentenceIds);expect(v.evidence[0].sources).toEqual(previous.evidence[0].sources);
  }
  expect(q('q-c08-024').evidence[0].quote).toContain('being part of a big team');
  expect(q('q-c08-024').evidence[0].quote).toContain('perhaps not as alienating');
  expect(q('q-c08-024').evidence[1]).toEqual(b('q-c08-024').evidence[1]);
  expect(q('q-c08-028').evidence[0].quote).toContain('When every member completed the whole production by themselves');
  expect(q('q-c08-028').evidence[0].quote).toContain('an average of fifteen');
 });
 it('三问作用追加完整首问，原先后两问证据保留',()=>{
  const v=q('q-c08-025'),book=read('public/data/book.json'),s=book.sentences.find((v2:any)=>v2.id===v.sentenceIds[0]);
  expect(v.evidence[0]).toEqual(b(v.id).evidence[0]);expect(v.evidence.at(-1)).toEqual({quote:s.text,sentenceIds:[s.id],sources:s.sources});
  expect(s.text).toContain('a full range of emotional experiences');expect(v.analyses[3]).not.toContain('IELTS');
  expect(q('qe-c08-0031').options[2]).toContain('the full range');expect(q('qe-c08-0031').options[2]).not.toContain('fuller');
 });
 it('分配与转向只据当前，不借后文等待或评分',()=>{
  expect(q('q-c08-027').analyses[3]).toContain('没有说明随机分派');expect(q('q-c08-027').analyses[3]).not.toContain('等待');
  expect(q('qe-c08-0033').analyses[3]).not.toContain('实验结束');
  const shift=q('qe-c08-0039');expect(shift.prompt).not.toContain('after the output');
  expect(shift.options[shift.answer]).toContain('happiness and meaning considered separately');
  expect(q('q-c08-029').analyses[3]).not.toContain('十五');
  expect(q('qe-c08-0032').options[1]).toContain('the 1985');
 });
 it('19题25候选已审，7题保留，84页为跨页上下文',()=>{
  const r=read('source/question-revisions/review-070-report.json');expect(r.manual.questionCount).toBe(19);expect(r.manual.sourceCandidatesReviewed).toBe(25);expect(r.manual.revisedQuestionCount).toBe(12);
  expect(r.manual.questionReviews.filter((v:any)=>v.decision==='retained')).toHaveLength(7);
  expect(r.manual.pdfPagesForQuestionEvidence).toEqual([82,83]);expect(r.manual.additionalParagraphContextPages).toEqual([84]);
  expect(r.remainingQuestionReviews).toBe(1371);expect(r.fullQuestionBankHumanReview).toBe(false);
 });
});
