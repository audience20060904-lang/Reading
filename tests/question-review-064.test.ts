import {readFileSync} from 'node:fs';
import {describe,it,expect} from 'vitest';
const read=(p:string)=>JSON.parse(readFileSync(p,'utf8'));
const all=read('src/data/question-revision-catalog.json').questions;
const q=(id:string)=>all.find((v:any)=>v.id===id);
describe('第六十四批：回复时点与调查比较强度',()=>{
 it('回复题仅据当前时点，追加right now引用且保留旧引用',()=>{
  const v=q('q-c07-047'),b=read('source/question-revisions/review-064-baseline.json').questions.find((r:any)=>r.id===v.id),s=read('public/data/book.json').sentences.find((r:any)=>r.id===v.sentenceIds[0]);expect(v.options[0]).not.toContain('coffee');expect(v.optionsZh[0]).not.toContain('咖啡');expect(v.evidence[0]).toEqual(b.evidence[0]);expect(v.evidence.at(-1)).toEqual({quote:s.text,sentenceIds:[s.id],sources:s.sources});expect(s.text).toContain('right now');
 });
 it('分散团队的两处far及集中团队比较组完整保留',()=>{
  const v=q('q-c07-050'),b=read('source/question-revisions/review-064-baseline.json').questions.find((r:any)=>r.id===v.id),s=read('public/data/book.json').sentences.find((r:any)=>r.id===v.sentenceIds[1]);expect(v.options[2]).toContain('Far less');expect(v.options[2]).toContain('far more');expect(v.evidence[0].quote).toBe(s.text);expect(v.evidence[0].quote).toContain('than those in geographically concentrated teams');expect(v.evidence[0].sentenceIds).toEqual(b.evidence[0].sentenceIds);expect(v.evidence[0].sources).toEqual(b.evidence[0].sources);for(const id of ['q-c07-050','qe-c07-0082','qe-c07-0083'])expect(q(id).translation).toContain('任务冲突多得多');
 });
 it('few共享译文仍保留机会，分析不借前后咖啡场景',()=>{
  for(const id of ['q-c07-049','qe-c07-0079','qe-c07-0080','qe-c07-0081']){expect(q(id).translation).toContain('留下很少随兴活动的机会');expect(q(id).translation).not.toContain('几乎不留');}expect(q('qe-c07-0078').analyses[0]).not.toContain('咖啡');expect(q('qe-c07-0075').analyses[0]).not.toContain('后面');expect(q('q-c07-048').analyses[3]).not.toContain('网站');
 });
 it('21题25来源已审，10题保留，未宣称全库完成',()=>{
  const r=read('source/question-revisions/review-064-report.json');expect(r.manual.questionCount).toBe(21);expect(r.manual.sourceCandidatesReviewed).toBe(25);expect(r.manual.revisedQuestionCount).toBe(11);expect(r.manual.questionReviews.filter((v:any)=>v.decision==='retained')).toHaveLength(10);expect(r.manual.pdfPagesVisuallyReviewed).toEqual([74,75]);expect(r.remainingQuestionReviews).toBe(1497);expect(r.fullQuestionBankHumanReview).toBe(false);
 });
});
