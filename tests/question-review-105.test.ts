import {readFileSync} from 'node:fs';
import {describe,it,expect} from 'vitest';
const read=(p:string)=>JSON.parse(readFileSync(p,'utf8'));
const all=read('src/data/question-revision-catalog.json').questions;
const q=(id:string)=>all.find((v:any)=>v.id===id);
const old=read('source/question-revisions/review-105-baseline.json').questions;
const b=(id:string)=>old.find((v:any)=>v.id===id);
describe('第一百零五批：相伴损失、引语范围与儿童研究',()=>{
 it('共同分析可定位到相伴理由，厨房事件和支援完整',()=>{
  expect(q('q-c11-036').evidence[2].quote).toContain('the more likely it was that they had lost a loved one');
  expect(q('q-c11-036').evidence[1].quote).toContain('they reported');
  expect(q('q-c11-038').evidence[0].quote).toContain('1906 San Francisco earthquake');
  expect(q('q-c11-038').evidence[1].quote).toContain('With the support from Oakland');
  for(const id of ['q-c11-036','q-c11-038','q-c11-039'])for(let i=0;i<b(id).evidence.length;i++){
   expect(q(id).evidence[i].quote).toContain(b(id).evidence[i].quote);expect(q(id).evidence[i].sources).toEqual(b(id).evidence[i].sources);expect(q(id).evidence[i].sentenceIds).toEqual(b(id).evidence[i].sentenceIds);
  }
 });
 it('Solnit引语保伤害侧与can，并将电视愿望和研究分开',()=>{
  const s=q('q-c11-039');expect(s.evidence[0].quote).toContain('the wounded, killed, orphaned');expect(s.evidence[1].quote).toContain('can be rich');
  expect(q('q-c11-041').options[2]).toBe('Only police officers and social workers.');
  expect(q('qe-c11-0074').options[0]).not.toContain('Decety');expect(q('qe-c11-0075').options[2]).not.toContain('train');
 });
 it('选项解析和词汇不夹带网站说明或未显示的操作任务',()=>{
  expect(q('qe-c11-0073').options[1]).toBe('A newly conducted online survey.');expect(q('qe-c11-0073').analyses[1]).not.toContain('网站');expect(q('qe-c11-0075').analyses[3]).not.toContain('网站');
  for(const id of ['q-c11-043','qe-c11-0076'])expect(q(id).vocabulary[0].context).not.toMatch(/贴纸|同学/);
 });
 it('19题24候选，9题原样保留且旧答案和片段不动',()=>{
  const r=read('source/question-revisions/review-105-report.json');expect(r.manual.questionCount).toBe(19);expect(r.manual.sourceCandidatesReviewed).toBe(24);expect(r.manual.revisedQuestionCount).toBe(10);expect(r.manual.questionReviews.filter((v:any)=>v.decision==='retained')).toHaveLength(9);expect(r.manual.pdfPagesVisuallyReviewed).toEqual([127,128,129]);expect(r.manual.pdfSourceBlocksTextMatched).toBe(7);expect(r.remainingQuestionReviews).toBe(620);expect(r.fullQuestionBankHumanReview).toBe(false);
  for(const before of old){expect(q(before.id).answer).toBe(before.answer);expect(q(before.id).passage).toBe(before.passage);}
 });
});
