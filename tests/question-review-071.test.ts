import {readFileSync} from 'node:fs';
import {describe,it,expect} from 'vitest';
const read=(p:string)=>JSON.parse(readFileSync(p,'utf8'));
const all=read('src/data/question-revision-catalog.json').questions;
const q=(id:string)=>all.find((v:any)=>v.id===id);
const originals=read('source/question-revisions/review-071-baseline.json').questions;
const b=(id:string)=>originals.find((v:any)=>v.id===id);
describe('第七十一批：显著比较、设想归属与唯一限定',()=>{
 it('结果和预期比较均补全同句引用，旧引用身份不变',()=>{
  for(const [id,indices] of [['q-c08-031',[0,1]],['q-c08-035',[0,2]]] as const){
   for(const i of indices){const v=q(id),old=b(id);expect(v.evidence[i].quote).toContain(old.evidence[i].quote);
    expect(v.evidence[i].sentenceIds).toEqual(old.evidence[i].sentenceIds);expect(v.evidence[i].sources).toEqual(old.evidence[i].sources);}
  }
  expect(q('q-c08-031').evidence[1].quote).toContain('than those in the whole production condition');
  expect(q('q-c08-031').options[0]).toContain('significantly lower');
  expect(q('q-c08-035').evidence[0].quote).toContain('students expected');
  expect(q('q-c08-035').evidence[2].quote).toContain('students thought');expect(q('q-c08-035').evidence[1]).toEqual(b('q-c08-035').evidence[1]);
 });
 it('合作设定和行为替代方法追加完整候选，旧引用保留',()=>{
  const book=read('public/data/book.json');
  for(const [id,index] of [['q-c08-033',0],['q-c08-037',-1]] as const){
   const v=q(id),old=b(id),s=book.sentences.find((r:any)=>r.id===v.sentenceIds.at(index));
   expect(v.evidence.slice(0,old.evidence.length)).toEqual(old.evidence);
   expect(v.evidence.at(-1)).toEqual({quote:s.text,sentenceIds:[s.id],sources:s.sources});
  }
  expect(q('q-c08-033').evidence.at(-1).quote).toContain('big collaborative project');
  expect(q('q-c08-037').evidence.at(-1).quote).toContain('instead of asking');
  expect(q('q-c08-037').evidence.at(-1).quote).toContain('trivia task');
 });
 it('only唯一入译，Even so不要求未显示前文属性',()=>{
  for(const id of ['q-c08-038','qe-c08-0052','qe-c08-0053'])expect(q(id).translation).toContain('唯一还持有一项发明专利');
  const v=q('q-c08-032');expect(v.options[v.answer]).toContain('concessive');expect(v.options[v.answer]).not.toContain('negative assessment');
  expect(v.vocabulary[0].context).toContain('短段没有重述');
  expect(q('q-c08-038').vocabulary[0].example).not.toContain('return');
  expect(q('qe-c08-0053').analyses[2]).not.toContain('后面');
 });
 it('20题24候选已审，保留7题，未冒称全库人工完成',()=>{
  const r=read('source/question-revisions/review-071-report.json');expect(r.manual.questionCount).toBe(20);expect(r.manual.sourceCandidatesReviewed).toBe(24);
  expect(r.manual.revisedQuestionCount).toBe(13);expect(r.manual.questionReviews.filter((v:any)=>v.decision==='retained')).toHaveLength(7);
  expect(r.manual.pdfPagesVisuallyReviewed).toEqual([83,84,85]);expect(r.remainingQuestionReviews).toBe(1351);expect(r.fullQuestionBankHumanReview).toBe(false);
 });
});
