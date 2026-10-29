import {readFileSync} from 'node:fs';
import {describe,it,expect} from 'vitest';
const read=(p:string)=>JSON.parse(readFileSync(p,'utf8'));
const all=read('src/data/question-revision-catalog.json').questions;
const q=(id:string)=>all.find((v:any)=>v.id===id);
const originals=read('source/question-revisions/review-069-baseline.json').questions;
const b=(id:string)=>originals.find((v:any)=>v.id===id);
describe('第六十九批：完整比较、任务证据及调查范围',()=>{
 it('分工扩展证据包含过去场景和时间范围，旧引用身份保持',()=>{
  const v=q('q-c08-011'),old=b(v.id),book=read('public/data/book.json');
  expect(v.evidence[0].quote).toContain('Over the last two decades');
  expect(v.evidence[0].quote).toContain(old.evidence[0].quote);
  expect(v.evidence[0].sentenceIds).toEqual(old.evidence[0].sentenceIds);expect(v.evidence[0].sources).toEqual(old.evidence[0].sources);
  expect(v.evidence[1]).toEqual(old.evidence[1]);
  const past=book.sentences.find((s:any)=>s.id===v.sentenceIds[0]);
  expect(v.evidence.at(-1)).toEqual({quote:past.text,sentenceIds:[past.id],sources:past.sources});
  expect(past.text).toContain('mostly limited to workplaces');
 });
 it('大团队数据任务和Marx观点归属补全，旧第二引用不改',()=>{
  const team=q('q-c08-013'),old=b(team.id);
  expect(team.evidence[0].quote).toContain('clean up the data');expect(team.evidence[0].quote).toContain('analyze it');
  expect(team.evidence[0].sources).toEqual(old.evidence[0].sources);expect(team.evidence[0].sentenceIds).toEqual(old.evidence[0].sentenceIds);
  expect(team.evidence[1]).toEqual(old.evidence[1]);
  const marx=q('q-c08-019');expect(marx.evidence[0].quote).toContain('Marx was further concerned');
  expect(marx.evidence[0].quote).toContain('social productive power');expect(marx.evidence[1]).toEqual(b(marx.id).evidence[1]);
 });
 it('程度、通顺译义和非军职调查范围保留，正文译文无网站备注',()=>{
  for(const id of ['q-c08-010','qe-c08-0018'])expect(q(id).translation).toContain('远超一百年');
  for(const id of ['q-c08-011','qe-c08-0019','qe-c08-0020']){
   expect(q(id).translation).toContain('讲求经济效率的习惯');expect(q(id).translation).toContain('直到 1990 年代');
  }
  for(const id of ['q-c08-012','qe-c08-0021'])expect(q(id).translation).not.toContain('网站');
  const survey=q('q-c08-022');expect(survey.options[survey.answer]).toContain('3,101 Americans employed in civilian occupations');
  expect(survey.options[survey.answer]).toContain('survey data');expect(survey.optionsZh[survey.answer]).toContain('非军职');
  expect(q('qe-c08-0028').analyses[3]).not.toContain('雇员');
 });
 it('19题23候选实际审阅，保留4题，未宣称全库完成',()=>{
  const r=read('source/question-revisions/review-069-report.json');expect(r.manual.questionCount).toBe(19);expect(r.manual.sourceCandidatesReviewed).toBe(23);
  expect(r.manual.revisedQuestionCount).toBe(15);expect(r.manual.questionReviews.filter((v:any)=>v.decision==='retained')).toHaveLength(4);
  expect(r.manual.pdfPagesVisuallyReviewed).toEqual([80,81,82]);expect(r.remainingQuestionReviews).toBe(1390);expect(r.fullQuestionBankHumanReview).toBe(false);
 });
});
