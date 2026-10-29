import {readFileSync} from 'node:fs';
import {describe,it,expect} from 'vitest';
const read=(p:string)=>JSON.parse(readFileSync(p,'utf8'));
const all=read('src/data/question-revision-catalog.json').questions;
const q=(id:string)=>all.find((v:any)=>v.id===id);
const originals=read('source/question-revisions/review-073-baseline.json').questions;
const b=(id:string)=>originals.find((v:any)=>v.id===id);
describe('第七十三批：条件范围、预计节省与自嘲动机',()=>{
 it('To the extent that不被译成只要式充分保证',()=>{
  for(const id of ['q-c08-047','qe-c08-0071','qe-c08-0072','qe-c08-0073']){
   expect(q(id).translation).not.toContain('只要');expect(q(id).translation).toContain('就你付钱');
   expect(q(id).translation).toContain('这应该会增加');
  }
  expect(q('qe-c08-0072').options[1]).toContain('spending, regardless');
  expect(q('q-c08-048').analyses[3]).not.toContain('IELTS');
 });
 it('报价证据保留身份并追加完整条件性省钱想法',()=>{
  const v=q('q-c08-049'),old=b(v.id),book=read('public/data/book.json');
  expect(v.evidence[0].quote).toContain(old.evidence[0].quote);expect(v.evidence[0].quote).toContain('After getting a few estimates');
  expect(v.evidence[0].sentenceIds).toEqual(old.evidence[0].sentenceIds);expect(v.evidence[0].sources).toEqual(old.evidence[0].sources);
  const s=book.sentences.find((v2:any)=>v2.id===v.sentenceIds.at(-1));expect(v.evidence.at(-1)).toEqual({quote:s.text,sentenceIds:[s.id],sources:s.sources});
  expect(s.text).toContain('if it meant saving at least $5,000');
 });
 it('Being cheap保留人物动机，初始印象引用补完整视频语境',()=>{
  for(const id of ['q-c08-050','qe-c08-0076','qe-c08-0077'])expect(q(id).translation).toContain('因为舍不得花钱');
  const v=q('q-c08-050'),old=b(v.id);expect(v.evidence[0].quote).toContain('YouTube videos');expect(v.evidence[0].quote).toContain(old.evidence[0].quote);
  expect(v.evidence[0].sentenceIds).toEqual(old.evidence[0].sentenceIds);expect(v.evidence[0].sources).toEqual(old.evidence[0].sources);expect(v.evidence[1]).toEqual(old.evidence[1]);
  expect(q('qe-c08-0082').analyses[1]).not.toContain('英寸');expect(q('qe-c08-0083').analyses[3]).not.toContain('五千');
 });
 it('20题24来源已审，保留8题且旧原文和答案位置不变',()=>{
  const r=read('source/question-revisions/review-073-report.json');expect(r.manual.questionCount).toBe(20);expect(r.manual.sourceCandidatesReviewed).toBe(24);expect(r.manual.revisedQuestionCount).toBe(12);
  expect(r.manual.questionReviews.filter((v:any)=>v.decision==='retained')).toHaveLength(8);expect(r.manual.pdfPagesVisuallyReviewed).toEqual([86,87]);
  expect(r.remainingQuestionReviews).toBe(1307);expect(r.fullQuestionBankHumanReview).toBe(false);
  for(const old of originals){expect(q(old.id).passage).toBe(old.passage);expect(q(old.id).answer).toBe(old.answer);}
 });
});
