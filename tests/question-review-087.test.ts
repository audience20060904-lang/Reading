import {readFileSync} from 'node:fs';
import {describe,it,expect} from 'vitest';
const read=(p:string)=>JSON.parse(readFileSync(p,'utf8'));
const all=read('src/data/question-revision-catalog.json').questions;
const frozen=read('source/question-revisions/review-087-current-questions.json').questions;
const q=(id:string)=>all.find((v:any)=>v.id===id)??frozen.find((v:any)=>v.id===id);
const old=read('source/question-revisions/review-087-baseline.json').questions;
const b=(id:string)=>old.find((v:any)=>v.id===id);
describe('第八十七批：模型、假设与实际行为的区别',()=>{
 it('秘书问题的引入及紧后任务均可定位，旧引不动',()=>{
  const now=q('qe-c10-0027');expect(now.evidence[0]).toEqual(b(now.id).evidence[0]);
  expect(now.evidence[1].quote).toContain('best possible hiring decision based on a series of interviews');
  expect(now.options[0]).not.toContain('website');expect(now.optionsZh[0]).toContain('任命');expect(now.analyses[2]).not.toContain('直接覆盖');
 });
 it('数量词义不依赖ID记账，37%仍为比较样本而非跟随者比例',()=>{
  const few=q('q-c10-015');expect(few.options[few.answer]).toContain('not necessarily zero');expect(few.translation).toBe('极少数。');expect(few.analyses.join('')).not.toContain('ID');
  const rule=q('q-c10-014');expect(rule.options[rule.answer]).toContain('forming a benchmark');expect(rule.analyses[3]).toContain('不是参与者遵循率');
  expect(q('qe-c10-0029').vocabulary[0].context).toContain('停止搜索');expect(q('qe-c10-0029').analyses[3]).not.toContain('网站');
 });
 it('词义和相互选择只依当前片段，未显示后段不进入解析',()=>{
  expect(q('qe-c10-0028').analyses[3]).not.toContain('后面');expect(q('qe-c10-0031').analyses[3]).not.toContain('下一短段');
  expect(q('q-c10-017').analyses[3]).not.toContain('被拒绝');expect(q('q-c10-017').analyses[3]).toContain('双方条件');
  expect(q('qe-c10-0033').vocabulary[0].context).not.toContain('用户');
  const lab=q('q-c10-018');expect(lab.passage).toContain('only a fraction');expect(lab.options[lab.answer]).toContain('only some');
 });
 it('21题23候选有13题保留，原文、答案与审阅界限保持',()=>{
  const r=read('source/question-revisions/review-087-report.json');
  expect(r.manual.questionCount).toBe(21);expect(r.manual.sourceCandidatesReviewed).toBe(23);expect(r.manual.revisedQuestionCount).toBe(8);
  expect(r.manual.questionReviews.filter((v:any)=>v.decision==='retained')).toHaveLength(13);
  expect(r.manual.pdfPagesVisuallyReviewed).toEqual([105,106]);expect(r.manual.pdfSourceBlocksTextMatched).toBe(4);
  expect(r.remainingQuestionReviews).toBe(1006);expect(r.fullQuestionBankHumanReview).toBe(false);
  for(const before of old){expect(q(before.id).answer).toBe(before.answer);expect(q(before.id).passage).toBe(before.passage);}
 });
});
