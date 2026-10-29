import {readFileSync} from 'node:fs';
import {describe,it,expect} from 'vitest';
const read=(p:string)=>JSON.parse(readFileSync(p,'utf8'));
const all=read('src/data/question-revision-catalog.json').questions;
const q=(id:string)=>all.find((v:any)=>v.id===id);
const old=read('source/question-revisions/review-100-baseline.json').questions;
const b=(id:string)=>old.find((v:any)=>v.id===id);
describe('第一百批：探索结语与非自愿经历',()=>{
 it('共享译文明确自然灾害或疾病并列，限定通常与问句保持',()=>{
  for(const id of ['q-c11-002','qe-c11-0004','qe-c11-0005']){expect(q(id).translation).toContain('地震、飓风等自然灾害，或疾病');expect(q(id).translation).toContain('通常');expect(q(id).translation).toContain('会增加人生的心理丰富吗');}
 });
 it('艺术原则和有意到非自愿的转折两侧可定位',()=>{
  expect(q('q-c10-118').evidence[0].quote).toContain('Jobs said');expect(q('q-c10-118').evidence[1].quote).toContain('That’s what I’ve always tried to do');
  const shift=q('q-c11-001');expect(shift.evidence[0]).toEqual(b(shift.id).evidence[0]);expect(shift.evidence[1].quote).toContain('Most psychologically rich experiences are intentional');expect(shift.evidence[2].quote).toContain('one chooses');
 });
 it('地震引语保哲学归属及破坏、意志两侧，旧引身份保持',()=>{
  const now=q('q-c11-003'),before=b(now.id);expect(now.evidence[0].quote).toContain('Friedrich Nietzsche');expect(now.evidence[0].quote).toContain('leave many languishing');expect(now.evidence[1].quote).toContain('In ancient Greeks');
  for(let i=0;i<2;i++){expect(now.evidence[i].quote).toContain(before.evidence[i].quote);expect(now.evidence[i].sources).toEqual(before.evidence[i].sources);expect(now.evidence[i].sentenceIds).toEqual(before.evidence[i].sentenceIds);}
 });
 it('21题22候选保留11题，123页仅作原段上下文',()=>{
  const r=read('source/question-revisions/review-100-report.json');expect(r.manual.questionCount).toBe(21);expect(r.manual.sourceCandidatesReviewed).toBe(22);expect(r.manual.revisedQuestionCount).toBe(10);expect(r.manual.questionReviews.filter((v:any)=>v.decision==='retained')).toHaveLength(11);expect(r.manual.pdfPagesVisuallyReviewed).toEqual([121,122,123]);expect(r.manual.additionalParagraphContextPages).toEqual([123]);expect(r.manual.pdfSourceBlocksTextMatched).toBe(5);expect(r.remainingQuestionReviews).toBe(723);expect(r.fullQuestionBankHumanReview).toBe(false);
  for(const before of old){expect(q(before.id).answer).toBe(before.answer);expect(q(before.id).passage).toBe(before.passage);}
 });
});
