import {readFileSync} from 'node:fs';
import {describe,it,expect} from 'vitest';
const read=(p:string)=>JSON.parse(readFileSync(p,'utf8'));
const all=read('src/data/question-revision-catalog.json').questions;
const q=(id:string)=>all.find((v:any)=>v.id===id);
const old=read('source/question-revisions/review-085-baseline.json').questions;
const b=(id:string)=>old.find((v:any)=>v.id===id);
describe('第八十五批：艺术体验与探索设问的范围',()=>{
 it('当前单句让步题不要求未显示身份或具体疾病',()=>{
  const now=q('q-c09-081');expect(now.prompt).not.toContain('Proust');expect(now.promptZh).toContain('本句');
  expect(now.analyses[2]).not.toContain('常病');expect(now.analyses[2]).toContain('没有具体说明');
  expect(now.passage).toBe(b(now.id).passage);expect(now.answer).toBe(b(now.id).answer);
 });
 it('好电影条件、三例及消遣质疑完整定位，旧引身份保留',()=>{
  const f=q('q-c09-082').evidence[0],before=b('q-c09-082').evidence[0];
  expect(f.quote).toContain('if you pay attention');expect(f.quote).toContain('At least, the good ones will.');expect(f.quote).toContain(before.quote);expect(f.sources).toEqual(before.sources);expect(f.sentenceIds).toEqual(before.sentenceIds);
  const list=q('q-c10-001');expect(list.evidence.slice(0,2)).toEqual(b(list.id).evidence);expect(list.evidence[2].quote).toContain('Schindler’s List');
  const role=q('qe-c10-0002');expect(role.evidence[0]).toEqual(b(role.id).evidence[0]);expect(role.evidence[2].quote).toContain('genuine benefits');
 });
 it('共享比较译文不缩成深度，选项和解析去网站与后续调查依赖',()=>{
  for(const id of ['q-c09-083','qe-c09-0148','qe-c09-0149']){expect(q(id).translation).toContain('受到的触动越多');expect(q(id).translation).not.toContain('被触动越深');}
  expect(q('qe-c10-0003').options[0]).toContain('actual reader');expect(q('qe-c10-0003').options[0]).not.toContain('website');
  expect(q('qe-c10-0005').options[2]).toContain('How quickly');expect(q('qe-c10-0008').analyses[3]).not.toContain('后面');
  expect(q('qe-c09-0150').analyses[3]).toContain('sometimes');expect(q('qe-c09-0150').analyses[3]).not.toContain('expands');
 });
 it('23题25候选有9题保留，答案、原文与审阅界限保持',()=>{
  const r=read('source/question-revisions/review-085-report.json');
  expect(r.manual.questionCount).toBe(23);expect(r.manual.sourceCandidatesReviewed).toBe(25);expect(r.manual.revisedQuestionCount).toBe(14);
  expect(r.manual.questionReviews.filter((v:any)=>v.decision==='retained')).toHaveLength(9);
  expect(r.manual.pdfPagesVisuallyReviewed).toEqual([102,103,104]);expect(r.manual.pdfSourceBlocksTextMatched).toBe(6);
  expect(r.remainingQuestionReviews).toBe(1048);expect(r.fullQuestionBankHumanReview).toBe(false);
  for(const before of old){expect(q(before.id).answer).toBe(before.answer);expect(q(before.id).passage).toBe(before.passage);}
 });
});
