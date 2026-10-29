import {readFileSync} from 'node:fs';
import {describe,it,expect} from 'vitest';
const read=(p:string)=>JSON.parse(readFileSync(p,'utf8'));
const all=read('src/data/question-revision-catalog.json').questions;
const q=(id:string)=>all.find((v:any)=>v.id===id);
describe('第六十三批：当前依据、否定与条件句',()=>{
 it('Samantha朋友证据在同句内保留条件和主语，旧引用映射不变',()=>{
  const v=q('q-c07-043'),b=read('source/question-revisions/review-063-baseline.json').questions.find((r:any)=>r.id===v.id),s=read('public/data/book.json').sentences.find((r:any)=>r.id===v.sentenceIds[2]);expect(v.evidence[1].quote).toBe(s.text);expect(v.evidence[1].quote).toContain('If you aren’t naturally spontaneous');expect(v.evidence[1].quote).toContain('Samantha');expect(v.evidence[1].sentenceIds).toEqual(b.evidence[1].sentenceIds);expect(v.evidence[1].sources).toEqual(b.evidence[1].sources);expect(v.evidence[0]).toEqual(b.evidence[0]);
 });
 it('四份共享译文保留not worrying，不弱化成较少担忧',()=>{
  for(const id of ['q-c07-039','qe-c07-0066','qe-c07-0067','qe-c07-0068']){expect(q(id).translation).toBe(q('q-c07-039').translation);expect(q(id).translation).toContain('不为自己的能力表现担忧');expect(q(id).translation).not.toContain('不那么担心');expect(q(id).translation).toContain('相对较少');expect(q(id).translation).toContain('我认识');}
 });
 it('工作后及经验证据题不用未显示的训练与运动员起点',()=>{
  expect(q('q-c07-036').prompt).toContain('after work');expect(q('q-c07-036').promptZh).toContain('工作后');expect(q('q-c07-036').analyses[3]).not.toContain('训练后');expect(q('qe-c07-0066').options[0]).toContain('adult playfulness');expect(q('qe-c07-0066').options[0]).not.toContain('athlete');expect(q('qe-c07-0062').analyses[0]).not.toContain('后面再列');
 });
 it('21题25来源已审，14题保留，剩余不是已知错误数',()=>{
  const r=read('source/question-revisions/review-063-report.json');expect(r.manual.questionCount).toBe(21);expect(r.manual.sourceCandidatesReviewed).toBe(25);expect(r.manual.revisedQuestionCount).toBe(7);expect(r.manual.questionReviews.filter((v:any)=>v.decision==='retained')).toHaveLength(14);expect(r.manual.pdfPagesVisuallyReviewed).toEqual([72,73,74]);expect(r.remainingQuestionReviews).toBe(1518);expect(r.fullQuestionBankHumanReview).toBe(false);
 });
});
