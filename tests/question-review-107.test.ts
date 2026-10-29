import {readFileSync} from 'node:fs';
import {describe,it,expect} from 'vitest';
const read=(p:string)=>JSON.parse(readFileSync(p,'utf8'));
const all=read('src/data/question-revision-catalog.json').questions;
const q=(id:string)=>all.find((v:any)=>v.id===id);
const old=read('source/question-revisions/review-107-baseline.json').questions;
const b=(id:string)=>old.find((v:any)=>v.id===id);
describe('第一百零七批：复现与因果、谣言定性、韧性范围',()=>{
 it('八题共享译文去内部续读，保留看来与多数限定',()=>{
  for(const id of ['q-c11-056','qe-c11-0101','qe-c11-0102','qe-c11-0103']){expect(q(id).translation).not.toContain('下一短段');expect(q(id).translation).toContain('因此看来');}
  for(const id of ['q-c11-060','qe-c11-0109','qe-c11-0110','qe-c11-0111']){expect(q(id).translation).not.toContain('续下段');expect(q(id).translation).toContain('Ann Masten总结数十年研究时指出');expect(q(id).translation).toContain('多数');}
  expect(q('qe-c11-0101').options[0]).not.toContain('973');expect(q('qe-c11-0103').analyses[2]).not.toContain('随后');
 });
 it('完整比较、谣言及旧观念归属和其他价值有证据',()=>{
  expect(q('q-c11-055').evidence[0].quote).toContain('than those without the experience');
  expect(q('q-c11-058').evidence[2].quote).toContain('a rumor that');expect(q('q-c11-058').evidence[3].quote).toContain('at least 6,000');
  expect(q('q-c11-060').evidence[0].quote).toContain('Ann Masten');expect(q('q-c11-060').evidence[1].quote).toContain('has lingered');expect(q('q-c11-063').evidence[1].quote).toContain('other values');
  for(const id of ['q-c11-055','q-c11-058','q-c11-060','q-c11-063'])for(let i=0;i<b(id).evidence.length;i++){
   expect(q(id).evidence[i].quote).toContain(b(id).evidence[i].quote);expect(q(id).evidence[i].sources).toEqual(b(id).evidence[i].sources);expect(q(id).evidence[i].sentenceIds).toEqual(b(id).evidence[i].sentenceIds);
  }
 });
 it('严重后果正确项不依赖随后韧性，画家与角色不借未显示评论者',()=>{
  expect(q('qe-c11-0108').options[0]).toBe('To acknowledge that disaster can have severe and lasting personal consequences.');expect(q('qe-c11-0108').analyses[0]).not.toContain('后续');
  expect(q('qe-c11-0114').options.slice(0,2).join(' ')).not.toContain('James');expect(q('q-c11-058').analyses[3]).not.toContain('本工具');expect(q('qe-c11-0115').analyses[2]).not.toContain('Guido');
 });
 it('24题25候选，5保留，边界修复和旧答案片段保留',()=>{
  const r=read('source/question-revisions/review-107-report.json');expect(r.manual.questionCount).toBe(24);expect(r.manual.sourceCandidatesReviewed).toBe(25);expect(r.manual.revisedQuestionCount).toBe(19);expect(r.manual.questionReviews.filter((v:any)=>v.decision==='retained')).toHaveLength(5);expect(r.manual.pdfPagesVisuallyReviewed).toEqual([130,131,132]);expect(r.manual.pdfSourceBlocksTextMatched).toBe(7);expect(r.remainingQuestionReviews).toBe(571);expect(r.fullQuestionBankHumanReview).toBe(false);
  for(const before of old){expect(q(before.id).answer).toBe(before.answer);expect(q(before.id).passage).toBe(before.passage);}
  expect(q('q-c11-061').sourceSegments).toEqual(b('q-c11-061').sourceSegments);expect(q('q-c11-061').version).toBe(b('q-c11-061').version+1);
 });
});
