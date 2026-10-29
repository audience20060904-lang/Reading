import {readFileSync} from 'node:fs';
import {describe,it,expect} from 'vitest';
const read=(p:string)=>JSON.parse(readFileSync(p,'utf8'));
const catalog=read('src/data/question-revision-catalog.json').questions;
const q=(id:string)=>catalog.find((v:any)=>v.id===id);
describe('第六十七批：alone、requires及建议对象',()=>{
 it('人格不能单独决定，培养路径与原句一致',()=>{
  for(const id of ['q-c07-067','qe-c07-0117','qe-c07-0118','qe-c07-0119'])expect(q(id).translation).toContain('仅凭人格特质并不能决定');
  const v=q('q-c07-067');expect(v.options[v.answer]).toContain('learn to foster it through playfulness and spontaneity');
  expect(v.optionsZh[v.answer]).toContain('通过玩心与自发性来培养');
  expect(q('qe-c07-0120').analyses[2]).not.toContain('结合');
 });
 it('requires不降为可能需要且可敬目标证据引用身份保留',()=>{
  const v=q('q-c07-068'),b=read('source/question-revisions/review-067-baseline.json').questions.find((r:any)=>r.id===v.id);
  expect(v.options[v.answer]).toContain('requires sustained attention');expect(v.options[v.answer]).not.toContain('can require');
  expect(v.evidence[0].quote).toContain('admirable goals, but');
  expect(v.evidence[0].quote).toContain(b.evidence[0].quote);
  expect(v.evidence[0].sentenceIds).toEqual(b.evidence[0].sentenceIds);expect(v.evidence[0].sources).toEqual(b.evidence[0].sources);
  expect(v.evidence[1]).toEqual(b.evidence[1]);
 });
 it('建议频率和同事对象完整保留，over不另加时间限定',()=>{
  const v=q('q-c07-071');expect(v.options[v.answer]).toContain('at least once a day');
  expect(v.options[v.answer]).toContain('partner, friend or coworker');expect(v.optionsZh[v.answer]).toContain('每天至少');
  for(const id of ['q-c07-070','qe-c07-0125','qe-c07-0126','qe-c07-0127']){
   expect(q(id).translation).toContain('爱好优先于职责');expect(q(id).translation).not.toContain('暂胜');
  }
  expect(q('qe-c07-0122').options[0]).toContain('The 2016');
  expect(q('qe-c07-0122').analyses.join(' ')).not.toContain('Ohtani');
  expect(q('qe-c07-0129').analyses[2]).not.toContain('小孩');
 });
 it('21题24候选实际审阅，8题保留，待审数不是错误数',()=>{
  const r=read('source/question-revisions/review-067-report.json');
  expect(r.manual.questionCount).toBe(21);expect(r.manual.sourceCandidatesReviewed).toBe(24);expect(r.manual.revisedQuestionCount).toBe(13);
  expect(r.manual.questionReviews.filter((v:any)=>v.decision==='retained')).toHaveLength(8);
  expect(r.manual.pdfPagesVisuallyReviewed).toEqual([77,78]);expect(r.remainingQuestionReviews).toBe(1434);
  expect(r.fullQuestionBankHumanReview).toBe(false);
 });
});
