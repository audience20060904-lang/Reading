import {readFileSync} from 'node:fs';
import {describe,it,expect} from 'vitest';
const read=(p:string)=>JSON.parse(readFileSync(p,'utf8'));
const all=read('src/data/question-revision-catalog.json').questions;
const q=(id:string)=>all.find((v:any)=>v.id===id);
const old=read('source/question-revisions/review-106-baseline.json').questions;
const b=(id:string)=>old.find((v:any)=>v.id===id);
describe('第一百零六批：损害与价值并存、奖金选择和问卷',()=>{
 it('不可欲立场不借后文，价值意象有条件及所指',()=>{
  expect(q('qe-c11-0087').options[2]).toBe('That the tragedy is not something people wish to undergo.');expect(q('qe-c11-0087').analyses[2]).not.toContain('后文');
  expect(q('q-c11-049').evidence[1].quote).toContain('happiness and normalcy');expect(q('q-c11-049').evidence[2].quote).toBe('No one wishes to suffer such a tragedy.');
  const e=q('q-c11-050').evidence;expect(e[0]).toEqual(b('q-c11-050').evidence[0]);expect(e[1].quote).toContain('even if happiness is impossible');expect(e[2].quote).toContain('many survivors become more prosocial');expect(e[3].quote).toContain('a treasure amidst ruins');
 });
 it('接触定义与奖金、部分捐赠和加倍均可定位',()=>{
  expect(q('q-c11-051').evidence[0].quote).toContain('during the early phase');expect(q('q-c11-051').evidence[0].quote).toContain('a family member, or an acquaintance');
  expect(q('q-c11-052').evidence[1].quote).toContain('$5 in the U.S. and €4 in Italy');expect(q('q-c11-052').evidence[2].quote).toContain('if they would like to donate some of the money');
  for(const id of ['q-c11-049','q-c11-051','q-c11-052']){expect(q(id).evidence[0].quote).toContain(b(id).evidence[0].quote);expect(q(id).evidence[0].sources).toEqual(b(id).evidence[0].sources);expect(q(id).evidence[0].sentenceIds).toEqual(b(id).evidence[0].sentenceIds);}
 });
 it('问卷归属不借贴纸列车或未显示的六月调查',()=>{
  expect(q('qe-c11-0098').options[0]).toBe('Jean Decety and his colleagues.');expect(q('qe-c11-0098').options[1]).toBe('Epley and Schroeder.');expect(q('qe-c11-0098').options[3]).toBe('Nietzsche and Rebecca Solnit.');
  expect(q('qe-c11-0099').analyses[1]).not.toContain('第二调查');expect(q('qe-c11-0097').analyses.join(' ')).not.toMatch(/前节|前段|另一调查/);
 });
 it('25题25候选，12保留，旧片段答案不变',()=>{
  const r=read('source/question-revisions/review-106-report.json');expect(r.manual.questionCount).toBe(25);expect(r.manual.sourceCandidatesReviewed).toBe(25);expect(r.manual.revisedQuestionCount).toBe(13);expect(r.manual.questionReviews.filter((v:any)=>v.decision==='retained')).toHaveLength(12);expect(r.manual.pdfPagesVisuallyReviewed).toEqual([129,130]);expect(r.manual.pdfSourceBlocksTextMatched).toBe(4);expect(r.remainingQuestionReviews).toBe(595);expect(r.fullQuestionBankHumanReview).toBe(false);
  for(const before of old){expect(q(before.id).answer).toBe(before.answer);expect(q(before.id).passage).toBe(before.passage);}
 });
});
