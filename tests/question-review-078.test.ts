import {readFileSync} from 'node:fs';
import {describe,it,expect} from 'vitest';
const read=(p:string)=>JSON.parse(readFileSync(p,'utf8'));
const all=read('src/data/question-revision-catalog.json').questions;
const q=(id:string)=>all.find((v:any)=>v.id===id);
const old=read('source/question-revisions/review-078-baseline.json').questions;
const b=(id:string)=>old.find((v:any)=>v.id===id);
describe('第七十八批：电影归属、家庭范围及当前片段',()=>{
 it('年轻读者限定与the Parks家庭范围在共享译文中保留',()=>{
  for(const id of ['q-c09-023','qe-c09-0043','qe-c09-0044','qe-c09-0045']){
   expect(q(id).translation).toContain('若你太年轻');expect(q(id).translation).not.toContain('没看过');
  }
  for(const id of ['q-c09-027','qe-c09-0053','qe-c09-0054','qe-c09-0055'])expect(q(id).translation).toContain('如果你太年轻');
  for(const id of ['q-c09-028','qe-c09-0056','qe-c09-0057','qe-c09-0058']){
   expect(q(id).translation).toContain('Park 家的人友善而天真');expect(q(id).translation).not.toContain('Park 夫妇');
  }
 });
 it('变化方向和声称身份的证据完整，原引用定位保持',()=>{
  for(const [id,index,term] of [['q-c09-022',0,'seems to end on a depressing note'],['q-c09-022',1,'During a time when I came to view the world as a terrible place'],['q-c09-028',0,'They lie to the Parks and claim']] as const){
   const v=q(id).evidence[index],before=b(id).evidence[index];
   expect(v.quote).toContain(term);expect(v.quote).toContain(before.quote);
   expect(v.sentenceIds).toEqual(before.sentenceIds);expect(v.sources).toEqual(before.sources);
  }
 });
 it('解析不借后文because、年份或网站通信探测作为已知内容',()=>{
  expect(q('qe-c09-0057').analyses[0]).not.toContain('随后');
  expect(q('qe-c09-0057').vocabulary[0].context).not.toContain('下一');
  expect(q('qe-c09-0053').analyses[0]).not.toContain('1999');
  expect(q('qe-c09-0056').analyses[2]).not.toContain('上一段');
  expect(q('qe-c09-0047').options[1]).not.toContain('website');
  expect(q('qe-c09-0049').analyses[3]).toContain('不是本书作者在现实中采访');
  expect(q('qe-c09-0050').options[0]).not.toContain('website');
 });
 it('24题25候选实际审阅，5题保留，答案位置与原文不变',()=>{
  const r=read('source/question-revisions/review-078-report.json');
  expect(r.manual.questionCount).toBe(24);expect(r.manual.sourceCandidatesReviewed).toBe(25);expect(r.manual.revisedQuestionCount).toBe(19);
  expect(r.manual.questionReviews.filter((v:any)=>v.decision==='retained')).toHaveLength(5);
  expect(r.manual.pdfPagesVisuallyReviewed).toEqual([92,93]);expect(r.manual.pdfSourceBlocksTextMatched).toBe(4);
  expect(r.remainingQuestionReviews).toBe(1200);expect(r.fullQuestionBankHumanReview).toBe(false);
  for(const before of old){expect(q(before.id).answer).toBe(before.answer);expect(q(before.id).passage).toBe(before.passage);}
 });
});
