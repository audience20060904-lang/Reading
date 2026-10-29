import {readFileSync} from 'node:fs';
import {describe,it,expect} from 'vitest';
const read=(p:string)=>JSON.parse(readFileSync(p,'utf8'));
const all=read('src/data/question-revision-catalog.json').questions;
const q=(id:string)=>all.find((v:any)=>v.id===id);
const old=read('source/question-revisions/review-102-baseline.json').questions;
const b=(id:string)=>old.find((v:any)=>v.id===id);
describe('第一百零二批：当前身份、担忧与自我描述',()=>{
 it('未给姓名的第一人称题只问叙述者，不额外要求孩子年龄',()=>{
  for(const id of ['qe-c11-0024','qe-c11-0025','qe-c11-0026','qe-c11-0027','qe-c11-0028']){expect(q(id).prompt).toContain('narrator');expect(q(id).prompt).not.toContain('Kahneman');}
  expect(q('q-c11-012').options[0]).toContain('narrator');expect(q('qe-c11-0026').prompt).not.toContain('past');expect(q('qe-c11-0027').options[3]).not.toContain('Kahneman');expect(q('q-c11-014').options[0]).toBe('His father.');
 });
 it('合作前课题及本人坚持interesting完整入证，旧身份保持',()=>{
  const interests=q('q-c11-016');expect(interests.evidence[0].quote).toContain('including subliminal perception');expect(interests.evidence[1].quote).toContain('Before he started his famous collaboration');
  const own=q('q-c11-019');expect(own.evidence[0].quote).toContain('I insisted');expect(own.evidence[0].quote).toContain('I still think this today');
  for(const id of ['q-c11-016','q-c11-018','q-c11-019']){expect(q(id).evidence[0].quote).toContain(b(id).evidence[0].quote);expect(q(id).evidence[0].sources).toEqual(b(id).evidence[0].sources);expect(q(id).evidence[0].sentenceIds).toEqual(b(id).evidence[0].sentenceIds);}
 });
 it('共享译文去续后段，尝试说服不偷换成功',()=>{
  for(const id of ['q-c11-018','qe-c11-0035','qe-c11-0036']){expect(q(id).translation).not.toContain('引语续后段');expect(q(id).translation).toContain('2018年');expect(q(id).translation).toContain('试图说服');}
  expect(q('qe-c11-0036').analyses[3]).not.toContain('后段');expect(q('qe-c11-0030').analyses[2]).not.toContain('获释');expect(q('qe-c11-0031').analyses[3]).not.toContain('覆盖');
 });
 it('21题23候选保留5题，123页为原段上下文且答案原文不变',()=>{
  const r=read('source/question-revisions/review-102-report.json');expect(r.manual.questionCount).toBe(21);expect(r.manual.sourceCandidatesReviewed).toBe(23);expect(r.manual.revisedQuestionCount).toBe(16);expect(r.manual.questionReviews.filter((v:any)=>v.decision==='retained')).toHaveLength(5);expect(r.manual.pdfPagesVisuallyReviewed).toEqual([123,124,125]);expect(r.manual.additionalParagraphContextPages).toEqual([123]);expect(r.manual.pdfSourceBlocksTextMatched).toBe(4);expect(r.remainingQuestionReviews).toBe(682);expect(r.fullQuestionBankHumanReview).toBe(false);
  for(const before of old){expect(q(before.id).answer).toBe(before.answer);expect(q(before.id).passage).toBe(before.passage);}
 });
});
