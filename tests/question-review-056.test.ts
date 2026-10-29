import {readFileSync} from 'node:fs';
import {describe,it,expect} from 'vitest';
const read=(p:string)=>JSON.parse(readFileSync(p,'utf8'));
const revised=read('src/data/question-revision-catalog.json').questions;
const q=(id:string)=>revised.find((v:any)=>v.id===id);
describe('第五十六批：完整条件证据与当前片段自足性',()=>{
 it('探索正面条件和离校目的追加完整原句，旧引用映射不改',()=>{
  const base=read('source/question-revisions/review-056-baseline.json').questions,book=read('public/data/book.json');
  for(const [id,index] of [['q-c06-072',2],['q-c06-076',0]] as const){const v=q(id),b=base.find((r:any)=>r.id===id),s=book.sentences.find((r:any)=>r.id===v.sentenceIds[index]);expect(v.evidence.slice(0,b.evidence.length)).toEqual(b.evidence);expect(v.evidence.at(-1)).toEqual({quote:s.text,sentenceIds:[s.id],sources:s.sources});expect(v.answer).toBe(b.answer);expect(v.passage).toBe(b.passage);}
 });
 it('主题转换及离校目的的正确解答不要求知道未显示章节或姓名',()=>{
  const t=q('qe-c06-0120'),s=q('qe-c06-0125');expect(t.options[0]).toContain('meaningful lives');expect(t.options[0]).not.toContain('happiness');expect(s.prompt).not.toContain('Greta');expect(s.promptZh).not.toContain('Greta');expect(s.prompt).toContain('2019');expect(s.answer).toBe(0);
 });
 it('出生地和运动名称分析只据当前，避免跨章节人物混用',()=>{
  const a=q('qe-c06-0127').analyses.join('');expect(a).not.toMatch(/前章|前一个人物|另一人物职业/);expect(a).toContain('Arkansas');expect(q('qe-c06-0122').analyses[2]).toContain('Her movement');expect(q('q-c06-070').vocabulary[0].context).not.toContain('承接');
 });
 it('23题25来源候选审阅和跨页上下文范围明确，16题保留',()=>{
  const r=read('source/question-revisions/review-056-report.json');expect(r.manual.questionCount).toBe(23);expect(r.manual.sourceCandidatesReviewed).toBe(25);expect(r.manual.revisedQuestionCount).toBe(7);expect(r.manual.questionReviews.filter((v:any)=>v.decision==='retained')).toHaveLength(16);expect(r.manual.pdfPagesForQuestionEvidence).toEqual([63,64]);expect(r.manual.additionalParagraphContextPages).toEqual([65]);expect(r.remainingQuestionReviews).toBe(1663);expect(r.fullQuestionBankHumanReview).toBe(false);
 });
});
