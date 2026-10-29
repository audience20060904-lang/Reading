import {readFileSync} from 'node:fs';
import {describe,it,expect} from 'vitest';
const read=(p:string)=>JSON.parse(readFileSync(p,'utf8'));
const all=read('src/data/question-revision-catalog.json').questions;
const q=(id:string)=>all.find((v:any)=>v.id===id);
const old=read('source/question-revisions/review-096-baseline.json').questions;
const b=(id:string)=>old.find((v:any)=>v.id===id);
describe('第九十六批：实施、期望值与条件链',()=>{
 it('实施阶段和两收益方案有完整定位',()=>{
  expect(q('q-c10-093').evidence[0].quote).toContain('In the implementation phase, however');expect(q('q-c10-093').evidence[0].quote).toContain('a long flight to Switzerland');
  const ev=q('q-c10-095');expect(ev.evidence[0].quote).toContain('choose the former');expect(ev.evidence[1].quote).toContain('50 percent chance of winning £1,000');expect(ev.evidence[1].quote).toContain('100 percent chance of winning £450');
  expect(0.5*1000).toBe(500);expect(500).toBeGreaterThan(450);
 });
 it('两if链保总选稳妥到不出舒适区再不遇意外',()=>{
  const chain=q('q-c10-097');expect(chain.evidence[0]).toEqual(b(chain.id).evidence[0]);expect(chain.evidence[1].quote).toContain('if we always chose a sure bet');expect(chain.evidence[1].quote).toContain('never venture outside');expect(chain.evidence[0].quote).toContain('never encounter anything unexpected');
 });
 it('旧引身份和已正确题目不变，概念题不借前章定义',()=>{
  for(const id of ['q-c10-093','q-c10-095']){const now=q(id),before=b(id);expect(now.evidence[0].quote).toContain(before.evidence[0].quote);expect(now.evidence[0].sentenceIds).toEqual(before.evidence[0].sentenceIds);expect(now.evidence[0].sources).toEqual(before.evidence[0].sources);}
  expect(q('qe-c10-0161').options[3]).toBe('Essentialism.');expect(q('qe-c10-0168').analyses[0]).not.toContain('parent');expect(q('qe-c10-0155').vocabulary[0].context).not.toContain('下一');
 });
 it('23题24候选保留14题，额外119页只作原段上下文',()=>{
  const r=read('source/question-revisions/review-096-report.json');expect(r.manual.questionCount).toBe(23);expect(r.manual.sourceCandidatesReviewed).toBe(24);expect(r.manual.revisedQuestionCount).toBe(9);
  expect(r.manual.questionReviews.filter((v:any)=>v.decision==='retained')).toHaveLength(14);expect(r.manual.pdfPagesVisuallyReviewed).toEqual([117,118,119]);expect(r.manual.pdfPagesForQuestionEvidence).toEqual([117,118]);expect(r.manual.additionalParagraphContextPages).toEqual([119]);expect(r.manual.pdfSourceBlocksTextMatched).toBe(5);
  expect(r.remainingQuestionReviews).toBe(809);expect(r.fullQuestionBankHumanReview).toBe(false);
  for(const before of old){expect(q(before.id).answer).toBe(before.answer);expect(q(before.id).passage).toBe(before.passage);}
 });
});
