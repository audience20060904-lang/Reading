import {readFileSync} from 'node:fs';
import {describe,it,expect} from 'vitest';
const read=(p:string)=>JSON.parse(readFileSync(p,'utf8'));
const all=read('src/data/question-revision-catalog.json').questions;
const q=(id:string)=>all.find((v:any)=>v.id===id);
const old=read('source/question-revisions/review-103-baseline.json').questions;
const b=(id:string)=>old.find((v:any)=>v.id===id);
describe('第一百零三批：时间范围、救援与持续影响',()=>{
 it('本人interesting与作者psychologically rich归属区分且不借姓名',()=>{
  const label=q('q-c11-021');expect(label.options[1]).toContain("the person's own description");expect(label.options[1]).not.toContain('Kahneman');expect(label.analyses[3]).not.toContain('Kahneman');
 });
 it('for life明确持续终生，返城和回顾日期不混且共享译文去续读备注',()=>{
  for(const id of ['q-c11-024','qe-c11-0045','qe-c11-0046','qe-c11-0047'])expect(q(id).translation).toContain('影响将持续终生');
  for(const id of ['q-c11-026','qe-c11-0050','qe-c11-0051','qe-c11-0052']){expect(q(id).translation).not.toContain('引语续后段');expect(q(id).translation).toContain('2006年1月');expect(q(id).translation).toContain('2018年');}
  expect(q('q-c11-026').optionsZh[0]).toContain('New Orleans');
 });
 it('救援与社区对照完整入证，旧引用身份不变',()=>{
  const rescue=q('q-c11-023');expect(rescue.evidence[0].quote).toContain('called for an ambulance');expect(rescue.evidence[1].quote).toContain('thirty-seven days');
  const community=q('q-c11-025');expect(community.evidence[0].quote).toContain('same basement apartment');expect(community.evidence[1].quote).toContain('far from intentional');
  for(const id of ['q-c11-023','q-c11-025']){for(let i=0;i<b(id).evidence.length;i++){expect(q(id).evidence[i].quote).toContain(b(id).evidence[i].quote);expect(q(id).evidence[i].sources).toEqual(b(id).evidence[i].sources);expect(q(id).evidence[i].sentenceIds).toEqual(b(id).evidence[i].sentenceIds);}}
 });
 it('22题24候选保留6题，答案原文和范围界限保持',()=>{
  const r=read('source/question-revisions/review-103-report.json');expect(r.manual.questionCount).toBe(22);expect(r.manual.sourceCandidatesReviewed).toBe(24);expect(r.manual.revisedQuestionCount).toBe(16);expect(r.manual.questionReviews.filter((v:any)=>v.decision==='retained')).toHaveLength(6);expect(r.manual.pdfPagesVisuallyReviewed).toEqual([125,126]);expect(r.manual.pdfSourceBlocksTextMatched).toBe(5);expect(r.remainingQuestionReviews).toBe(660);expect(r.fullQuestionBankHumanReview).toBe(false);
  for(const before of old){expect(q(before.id).answer).toBe(before.answer);expect(q(before.id).passage).toBe(before.passage);}
 });
});
