import {readFileSync} from 'node:fs';
import {describe,it,expect} from 'vitest';
const read=(p:string)=>JSON.parse(readFileSync(p,'utf8'));
const revised=read('src/data/question-revision-catalog.json').questions;
const q=(id:string)=>revised.find((v:any)=>v.id===id);
describe('第五十五批：情感定义证据及主要原因范围',()=>{
 it('保留旧幸福定义引文并追加当前学者情感概念化的完整原句',()=>{
  const v=q('q-c06-065'),b=read('source/question-revisions/review-055-baseline.json').questions.find((r:any)=>r.id===v.id),s=read('public/data/book.json').sentences.find((r:any)=>r.id===v.sentenceIds[1]);
  expect(v.evidence.slice(0,b.evidence.length)).toEqual(b.evidence);expect(v.evidence.at(-1)).toEqual({quote:s.text,sentenceIds:[s.id],sources:s.sources});expect(s.text).toContain('Some personality scholars');expect(v.passage).toContain(s.text);expect(v.answer).toBe(b.answer);
 });
 it('共享译文保留lacking的程度且不把人格特质当临床诊断',()=>{
  for(const id of ['q-c06-064','qe-c06-0103','qe-c06-0104']){expect(q(id).translation).toContain('缺乏神经质倾向');expect(q(id).translation).not.toContain('较少神经质');expect(q(id).translation).toBe(q('q-c06-064').translation);}
 });
 it('补充题独立考Primarily主要而非唯一，并保留正确答案位置',()=>{
  const v=q('qe-c06-0108');expect(v.prompt).toContain('Primarily');expect(v.promptZh).toContain('范围');expect(v.answer).toBe(1);expect(v.options[1]).toContain('without being the only');expect(v.optionsZh[1]).toContain('未说它是唯一');expect(v.analyses[1]).toContain('排他');expect(v.vocabulary[0].context).not.toMatch(/Second|Third/);
 });
 it('22题23来源候选实际审阅，13题保留且不宣称全库完成',()=>{
  const r=read('source/question-revisions/review-055-report.json');expect(r.manual.questionCount).toBe(22);expect(r.manual.sourceCandidatesReviewed).toBe(23);expect(r.manual.revisedQuestionCount).toBe(9);expect(r.manual.questionReviews.filter((v:any)=>v.decision==='retained')).toHaveLength(13);expect(r.manual.pdfPagesVisuallyReviewed).toEqual([62,63]);expect(r.remainingQuestionReviews).toBe(1686);expect(r.fullQuestionBankHumanReview).toBe(false);
 });
});
