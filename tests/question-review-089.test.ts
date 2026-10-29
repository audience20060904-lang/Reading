import {readFileSync} from 'node:fs';
import {describe,it,expect} from 'vitest';
const read=(p:string)=>JSON.parse(readFileSync(p,'utf8'));
const all=read('src/data/question-revision-catalog.json').questions;
const q=(id:string)=>all.find((v:any)=>v.id===id);
const old=read('source/question-revisions/review-089-baseline.json').questions;
const b=(id:string)=>old.find((v:any)=>v.id===id);
describe('第八十九批：反问、局部配对与接触机会',()=>{
 it('十二段关系的反问完整定位，旧引不动',()=>{
  const now=q('q-c10-028');expect(now.evidence[0]).toEqual(b(now.id).evidence[0]);
  expect(now.evidence[1].quote).toContain('twelve serious relationships before marriage');
 });
 it('庞大候选池与局部选择对照及跨页比喻均可定位',()=>{
  const e=q('q-c10-033').evidence[0],before=b('q-c10-033').evidence[0];
  expect(e.quote).toContain('hundreds of thousands');expect(e.quote).toContain(before.quote);expect(e.sources).toEqual(before.sources);expect(e.sentenceIds).toEqual(before.sentenceIds);
  const comment=q('q-c10-033').evidence[1];expect(comment.quote).toContain('Cupid may have wings');expect(comment.sources.map((v:any)=>v.pdfPage)).toEqual([108,109]);
 });
 it('互动机制补全，清单和历史解释不借未显示背景',()=>{
  const now=q('q-c10-034');expect(now.evidence.slice(0,2)).toEqual(b(now.id).evidence);expect(now.evidence[2].quote).toContain('more likely to have interactions nearby');
  expect(q('qe-c10-0052').analyses[2]).not.toContain('Ebert');expect(q('qe-c10-0052').analyses[3]).not.toContain('网站');
  expect(q('qe-c10-0059').analyses[0]).not.toContain('2004');expect(q('qe-c10-0064').analyses[3]).not.toContain('许可证');
 });
 it('23题24候选有15题保留，答案原文和审阅界限保持',()=>{
  const r=read('source/question-revisions/review-089-report.json');
  expect(r.manual.questionCount).toBe(23);expect(r.manual.sourceCandidatesReviewed).toBe(24);expect(r.manual.revisedQuestionCount).toBe(8);
  expect(r.manual.questionReviews.filter((v:any)=>v.decision==='retained')).toHaveLength(15);
  expect(r.manual.pdfPagesVisuallyReviewed).toEqual([107,108,109]);expect(r.manual.pdfSourceBlocksTextMatched).toBe(8);
  expect(r.remainingQuestionReviews).toBe(961);expect(r.fullQuestionBankHumanReview).toBe(false);
  for(const before of old){expect(q(before.id).answer).toBe(before.answer);expect(q(before.id).passage).toBe(before.passage);}
 });
});
