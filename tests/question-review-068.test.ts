import {readFileSync} from 'node:fs';
import {describe,it,expect} from 'vitest';
const read=(p:string)=>JSON.parse(readFileSync(p,'utf8'));
const catalog=read('src/data/question-revision-catalog.json').questions;
const q=(id:string)=>catalog.find((v:any)=>v.id===id);
describe('第六十八批：转述、产量单位与限定语',()=>{
 it('unintended不与无法预见等同，far more保留比较程度',()=>{
  const v=q('q-c08-003');expect(v.optionsZh[v.answer]).toContain('并非本意');
  expect(v.translation).toContain('并非本意');expect(v.vocabulary[0].meaning).not.toContain('未预期');
  expect(v.vocabulary[0].context).toContain('不说明后果此前无法预见');
  for(const id of ['q-c08-009','qe-c08-0015','qe-c08-0016','qe-c08-0017']){
   expect(q(id).translation).toContain('效率高得多的分工');
   expect(q(id).translation).toContain('最终');
  }
 });
 it('大意转述证据补导言归属但旧引文身份保留',()=>{
  const v=q('q-c08-004'),old=read('source/question-revisions/review-068-baseline.json').questions.find((r:any)=>r.id===v.id);
  expect(v.options[v.answer]).toContain('approximate paraphrase');expect(v.options[v.answer]).not.toContain('recollection');
  expect(v.evidence[0].quote).toContain('Alan Krueger');expect(v.evidence[0].quote).toContain('something along the lines');
  expect(v.evidence[0].quote).toContain(old.evidence[0].quote);
  expect(v.evidence[0].sources).toEqual(old.evidence[0].sources);expect(v.evidence[0].sentenceIds).toEqual(old.evidence[0].sentenceIds);
  expect(v.evidence[1]).toEqual(old.evidence[1]);
 });
 it('命名题只据当前英文范围，原书数字与历史时点不改',()=>{
  const named=q('qe-c08-0008');expect(named.options[named.answer]).toContain('first book written in English');
  expect(named.options[named.answer]).toContain('The Psychological Wealth of Nations');expect(named.options[named.answer]).not.toContain('appreciation');
  expect(q('q-c08-007').analyses[3]).toContain('48,000 pins a day');expect(q('q-c08-007').analyses[3]).toContain('4,800 per worker');
  expect(q('qe-c08-0015').options[3]).toBe('The 1990s.');
  expect(q('qe-c08-0017').prompt).toContain('Model T');expect(q('qe-c08-0017').analyses[3]).not.toContain('候选');
 });
 it('25题25候选已审，14题保留，旧原文与答案位置保持',()=>{
  const r=read('source/question-revisions/review-068-report.json');expect(r.manual.questionCount).toBe(25);expect(r.manual.sourceCandidatesReviewed).toBe(25);
  expect(r.manual.revisedQuestionCount).toBe(11);expect(r.manual.questionReviews.filter((v:any)=>v.decision==='retained')).toHaveLength(14);
  expect(r.manual.pdfPagesVisuallyReviewed).toEqual([79,80]);expect(r.remainingQuestionReviews).toBe(1409);
  expect(r.manual.answerKeysChanged).toBe(0);expect(r.fullQuestionBankHumanReview).toBe(false);
 });
});
