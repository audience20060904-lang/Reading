import {readFileSync} from 'node:fs';
import {describe,it,expect} from 'vitest';
const read=(p:string)=>JSON.parse(readFileSync(p,'utf8'));
const revised=read('src/data/question-revision-catalog.json').questions;
const q=(id:string)=>revised.find((v:any)=>v.id===id);
describe('第五十四批：旧引文身份与初次结识语义',()=>{
 it('旧引文完整保留，追加熟人句使用原候选句及精确来源',()=>{
  const v=q('q-c06-054'),b=read('source/question-revisions/review-054-baseline.json').questions.find((row:any)=>row.id===v.id),book=read('public/data/book.json'),s=book.sentences.find((row:any)=>row.id===v.sentenceIds[1]);expect(v.evidence[0]).toEqual(b.evidence[0]);expect(v.evidence).toHaveLength(b.evidence.length+1);expect(v.evidence.at(-1)).toEqual({quote:s.text,sentenceIds:[s.id],sources:s.sources});expect(s.text).toContain('already know');expect(v.passage).toBe(b.passage);
 });
 it('四题译文不把meeting a new person直接当成已成为朋友，仍保留自信条件',()=>{
  const ids=['q-c06-057','qe-c06-0089','qe-c06-0090','qe-c06-0091'];for(const id of ids){expect(q(id).translation).toBe(q(ids[0]).translation);expect(q(id).translation).toContain('当你自信时');expect(q(id).translation).toContain('认识一个新的人');expect(q(id).translation).not.toContain('新朋友');}
 });
 it('省略结构与one factor解释只据当前，去网站和未显示段落信息',()=>{
  expect(q('qe-c06-0080').analyses[0]).toContain('might not be');expect(q('qe-c06-0080').analyses[0]).not.toContain('might not obvious');expect(q('qe-c06-0083').analyses[0]).not.toContain('网站');expect(q('qe-c06-0089').analyses[0]).not.toContain('另一段');expect(q('qe-c06-0095').vocabulary[0].context).not.toContain('此前');
 });
 it('24题24来源候选审阅范围真实，16题保留且不冒称全库完成',()=>{
  const r=read('source/question-revisions/review-054-report.json');expect(r.manual.questionCount).toBe(24);expect(r.manual.sourceCandidatesReviewed).toBe(24);expect(r.manual.revisedQuestionCount).toBe(8);expect(r.manual.questionReviews.filter((row:any)=>row.decision==='retained')).toHaveLength(16);expect(r.frozenCheckpoint).toContain('054-checkpoint');expect(r.remainingQuestionReviews).toBe(1708);expect(r.fullQuestionBankHumanReview).toBe(false);
 });
});
