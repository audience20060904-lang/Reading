import {readFileSync} from 'node:fs';
import {describe,it,expect} from 'vitest';
const read=(p:string)=>JSON.parse(readFileSync(p,'utf8'));
const all=read('src/data/question-revision-catalog.json').questions;
const q=(id:string)=>all.find((v:any)=>v.id===id);
const old=read('source/question-revisions/review-094-baseline.json').questions;
describe('第九十四批：当前指代与住房时序',()=>{
 it('过早定下的两种倾向和压力句有完整主语，引用身份保留',()=>{
  const now=q('q-c10-076'),before=old.find((v:any)=>v.id===now.id);
  expect(now.evidence[0].quote).toContain('Psychological research shows');
  expect(now.evidence[1].quote).toContain('Our own research further shows');
  for(let i=0;i<2;i++){expect(now.evidence[i].quote).toContain(before.evidence[i].quote);expect(now.evidence[i].sentenceIds).toEqual(before.evidence[i].sentenceIds);expect(now.evidence[i].sources).toEqual(before.evidence[i].sources);}
 });
 it('指代和搜索要求只依赖当前考虑一打伴侣',()=>{
  expect(q('qe-c10-0125').options[1]).toBe('Seriously consider a dozen potential mates.');
  expect(q('qe-c10-0126').options[3]).toContain('Seriously considering a dozen potential mates');
  expect(q('qe-c10-0126').options[3]).not.toContain('unfamiliar');
  expect(q('qe-c10-0125').optionsZh[1]).toContain('潜在伴侣');
 });
 it('举例功能及住房题解析没有未显示的研究或购房身份',()=>{
  expect(q('qe-c10-0132').options[0]).toContain('questions about rental and purchase locations');
  expect(q('qe-c10-0135').analyses[0]).not.toContain('后来');
  expect(q('qe-c10-0136').analyses[1]).not.toContain('随后');
  expect(q('qe-c10-0137').analyses[1]).not.toContain('前段');
  expect(q('qe-c10-0138').analyses[3]).toContain('没有说已完成购买');
 });
 it('21题24候选保留7题，PDF和范围界限真实',()=>{
  const r=read('source/question-revisions/review-094-report.json');
  expect(r.manual.questionCount).toBe(21);expect(r.manual.sourceCandidatesReviewed).toBe(24);expect(r.manual.revisedQuestionCount).toBe(14);
  expect(r.manual.questionReviews.filter((v:any)=>v.decision==='retained')).toHaveLength(7);
  expect(r.manual.pdfPagesVisuallyReviewed).toEqual([115,116]);expect(r.manual.pdfSourceBlocksTextMatched).toBe(4);
  expect(r.remainingQuestionReviews).toBe(852);expect(r.fullQuestionBankHumanReview).toBe(false);
  for(const before of old){expect(q(before.id).answer).toBe(before.answer);expect(q(before.id).passage).toBe(before.passage);}
 });
});
