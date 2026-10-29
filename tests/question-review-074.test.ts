import {readFileSync} from 'node:fs';
import {describe,it,expect} from 'vitest';
const read=(p:string)=>JSON.parse(readFileSync(p,'utf8'));
const all=read('src/data/question-revision-catalog.json').questions;
const q=(id:string)=>all.find((v:any)=>v.id===id);
const originals=read('source/question-revisions/review-074-baseline.json').questions;
const b=(id:string)=>originals.find((v:any)=>v.id===id);
describe('第七十四批：时域、情绪及共同例证',()=>{
 it('And yet只考当前转折，自评译文保留动手领域',()=>{
  const v=q('q-c08-054');expect(v.options[v.answer]).toContain('introduces a contrast');expect(v.options[v.answer]).not.toContain('earlier difficulties');
  for(const id of ['q-c08-055','qe-c08-0087','qe-c08-0088','qe-c08-0089'])expect(q(id).translation).toContain('在动手能力方面，我对自己的评价很低');
  expect(q('qe-c08-0089').analyses[0]).not.toContain('此前');
 });
 it('短期反事实与长期实际故事不混，情绪引用完整保留身份',()=>{
  const v=q('q-c08-056'),old=b(v.id);expect(v.options[v.answer]).toContain('would have increased short-run happiness');
  expect(v.options[v.answer]).toContain('far more stories');expect(v.evidence[0]).toEqual(old.evidence[0]);
  expect(v.evidence[1].quote).toContain('a sense of accomplishment');expect(v.evidence[1].quote).toContain('memories of agony and pain');
  expect(v.evidence[1].sentenceIds).toEqual(old.evidence[1].sentenceIds);expect(v.evidence[1].sources).toEqual(old.evidence[1].sources);
  for(const id of ['q-c08-056','qe-c08-0090'])expect(q(id).translation).toContain('多得多的故事');
  expect(q('q-c08-057').evidence[1].quote).toContain('because it could have some opportunity cost');
 });
 it('三例和两个自问均入证，所有原引用身份保持',()=>{
  const v=q('q-c08-059'),old=b(v.id);expect(v.evidence[0].quote).toContain('To foster psychological richness');expect(v.evidence[1]).toEqual(old.evidence[1]);
  expect(v.evidence.some((e:any)=>e.quote.startsWith('Assembling a whole motorcycle'))).toBe(true);
  expect(v.evidence.some((e:any)=>e.quote.startsWith('Building a brick patio'))).toBe(true);
  const s=q('q-c08-060'),previous=b(s.id);expect(s.evidence[0].quote).toContain(previous.evidence[0].quote);expect(s.evidence[0].sentenceIds).toEqual(previous.evidence[0].sentenceIds);expect(s.evidence[0].sources).toEqual(previous.evidence[0].sources);
  expect(s.evidence.some((e:any)=>e.quote.includes('Could I do it myself?'))).toBe(true);expect(s.evidence.some((e:any)=>e.quote.includes('Would I have an interesting story'))).toBe(true);
  for(const id of ['q-c08-060','qe-c08-0095','qe-c08-0096','qe-c08-0097'])expect(q(id).translation).toContain('长期也可能增添');
 });
 it('20题23候选实际审阅，保留5题，原始来源未改',()=>{
  const r=read('source/question-revisions/review-074-report.json');expect(r.manual.questionCount).toBe(20);expect(r.manual.sourceCandidatesReviewed).toBe(23);expect(r.manual.revisedQuestionCount).toBe(15);
  expect(r.manual.questionReviews.filter((v:any)=>v.decision==='retained')).toHaveLength(5);expect(r.manual.pdfPagesVisuallyReviewed).toEqual([87,88]);expect(r.remainingQuestionReviews).toBe(1287);expect(r.fullQuestionBankHumanReview).toBe(false);
 });
});
