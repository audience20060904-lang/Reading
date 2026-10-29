import {readFileSync} from 'node:fs';
import {describe,it,expect} from 'vitest';
const read=(p:string)=>JSON.parse(readFileSync(p,'utf8'));
const all=read('src/data/question-revision-catalog.json').questions;
const q=(id:string)=>all.find((v:any)=>v.id===id);
const old=read('source/question-revisions/review-109-baseline.json').questions;
const b=(id:string)=>old.find((v:any)=>v.id===id);
describe('第一百零九批：实录、回忆与客观表现',()=>{
 it('不确定回顾转纵向的理由可定位，旧过渡证据不动',()=>{
  const a=q('q-c12-012');expect(a.evidence[0]).toEqual(b(a.id).evidence[0]);expect(a.evidence[1].quote).toContain('might have indeed');expect(a.vocabulary[0].example).toBe('A longitudinal study follows participants over time.');
 });
 it('正确项用当前可见的约两个月前，完整比较不借九月月份',()=>{
  const a=q('q-c12-013');expect(a.options[2]).toContain('about two months earlier');expect(a.options[2]).not.toContain('September');expect(a.optionsZh[2]).not.toContain('九月');expect(a.evidence[0].quote).toContain('By assessing their current selves');expect(a.evidence[0].quote).toContain(b(a.id).evidence[0].quote);expect(a.evidence[0].sentenceIds).toEqual(b(a.id).evidence[0].sentenceIds);expect(a.evidence[0].sources).toEqual(b(a.id).evidence[0].sources);
 });
 it('回忆评分完整显示在十一月作出，其他两个实录不动',()=>{
  const a=q('q-c12-014');expect(a.evidence.slice(0,2)).toEqual(b(a.id).evidence.slice(0,2));expect(a.evidence[2].quote).toContain('Yet, in November');expect(a.evidence[2].quote).toContain('remembered September self-rating was 5.74');expect(a.evidence[2].quote).toContain(b(a.id).evidence[2].quote);expect(a.evidence[2].sources).toEqual(b(a.id).evidence[2].sources);
  expect(q('qe-c12-0022').analyses[3]).not.toContain('前面');expect(q('qe-c12-0025').analyses[1]).not.toContain('随后');expect(q('qe-c12-0016').analyses[3]).not.toContain('编造');
 });
 it('20题25候选，13题原样保留，原答案片段不改',()=>{
  const r=read('source/question-revisions/review-109-report.json');expect(r.manual.questionCount).toBe(20);expect(r.manual.sourceCandidatesReviewed).toBe(25);expect(r.manual.revisedQuestionCount).toBe(7);expect(r.manual.questionReviews.filter((v:any)=>v.decision==='retained')).toHaveLength(13);expect(r.manual.pdfPagesVisuallyReviewed).toEqual([135,136]);expect(r.manual.pdfSourceBlocksTextMatched).toBe(3);expect(r.remainingQuestionReviews).toBe(529);expect(r.fullQuestionBankHumanReview).toBe(false);
  for(const before of old){expect(q(before.id).answer).toBe(before.answer);expect(q(before.id).passage).toBe(before.passage);}
 });
});
