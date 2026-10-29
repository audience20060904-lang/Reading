import {readFileSync} from 'node:fs';
import {describe,it,expect} from 'vitest';
const read=(p:string)=>JSON.parse(readFileSync(p,'utf8'));
const revised=read('src/data/question-revision-catalog.json').questions;
const q=(id:string)=>revised.find((v:any)=>v.id===id);
describe('第五十八批：目标完整引用与原文限定',()=>{
 it('目标证据扩至同一完整原句，保留旧映射和其他引文',()=>{
  const v=q('q-c06-086'),b=read('source/question-revisions/review-058-baseline.json').questions.find((r:any)=>r.id===v.id),s=read('public/data/book.json').sentences.find((r:any)=>r.id===v.sentenceIds[1]);
  expect(v.evidence[0].quote).toBe(s.text);expect(v.evidence[0].quote).toContain('open to new experiences');expect(v.evidence[0].quote).toContain(b.evidence[0].quote);expect(v.evidence[0].sentenceIds).toEqual(b.evidence[0].sentenceIds);expect(v.evidence[0].sources).toEqual(b.evidence[0].sources);expect(v.evidence.slice(1)).toEqual(b.evidence.slice(1));expect(v.passage).toBe(b.passage);
 });
 it('conflict-free不弱化为少冲突，同时保留tend与perhaps限定',()=>{
  for(const id of ['q-c06-087','qe-c06-0147']){expect(q(id).translation).toContain('温暖、没有冲突的关系');expect(q(id).translation).toContain('往往');expect(q(id).translation).toContain('或许部分');expect(q(id).translation).not.toContain('少冲突');}expect(q('q-c06-087').translation).toBe(q('qe-c06-0147').translation);
 });
 it('原书secondarily不改，常见搭配规范；作者归属不依赖下一章姓名',()=>{
  const s=q('qe-c06-0145');expect(s.passage).toContain('secondarily predictors');expect(s.vocabulary[0].collocations).toEqual(['secondary predictors','secondarily important']);expect(q('qe-c06-0151').options[1]).toContain('author');expect(q('qe-c06-0151').options[1]).not.toContain('Oishi');expect(q('qe-c06-0151').analyses[3]).not.toContain('下一章');expect(q('qe-c06-0143').options[1]).toContain('does not rule out');expect(q('q-c06-091').analyses[3]).not.toContain('程序');
 });
 it('19题23来源候选已审，10题保留且余1625题待审',()=>{
  const r=read('source/question-revisions/review-058-report.json');expect(r.manual.questionCount).toBe(19);expect(r.manual.sourceCandidatesReviewed).toBe(23);expect(r.manual.revisedQuestionCount).toBe(9);expect(r.manual.questionReviews.filter((v:any)=>v.decision==='retained')).toHaveLength(10);expect(r.manual.pdfPagesVisuallyReviewed).toEqual([65,66,67]);expect(r.remainingQuestionReviews).toBe(1625);expect(r.fullQuestionBankHumanReview).toBe(false);
 });
});
