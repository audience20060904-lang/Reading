import {readFileSync} from 'node:fs';
import {describe,it,expect} from 'vitest';
const read=(p:string)=>JSON.parse(readFileSync(p,'utf8'));
const all=read('src/data/question-revision-catalog.json').questions;
const q=(id:string)=>all.find((v:any)=>v.id===id);
const old=read('source/question-revisions/review-076-baseline.json').questions;
const b=(id:string)=>old.find((v:any)=>v.id===id);

describe('第七十六批：道德设问、人物观点及时间范围',()=>{
 it('道德问题的干扰项不再重复正确主题，答案和原问句证据保留',()=>{
  const v=q('q-c09-010'),before=b(v.id);
  expect(before.options[0]).toContain('clear purpose necessarily proves');
  expect(v.options[0]).toBe('Whether Stevens had ever dedicated himself to any cause at all.');
  expect(v.options[v.answer]).toEqual(before.options[before.answer]);expect(v.answer).toBe(2);
  expect(v.analyses[0]).toContain('首句已明确');
  expect(v.evidence[0]).toEqual(before.evidence[0]);
  expect(v.evidence[1].quote).toContain('ultimately harmed England');
 });
 it('首次职业假期、至少选择过及首次自问均有完整证据且不改旧身份',()=>{
  for(const [id,index,term] of [['q-c09-008',1,'For the first time in his professional life'],['q-c09-011',0,'he can say that at least'],['q-c09-013',0,'For the first time, I wondered']] as const){
   const v=q(id),before=b(id);expect(v.evidence[index].quote).toContain(term);
   expect(v.evidence[index].quote).toContain(before.evidence[index].quote);
   expect(v.evidence[index].sentenceIds).toEqual(before.evidence[index].sentenceIds);
   expect(v.evidence[index].sources).toEqual(before.evidence[index].sources);
  }
  expect(q('q-c09-012').evidence[1].quote).toContain('All those years I served him');
 });
 it('his lordship第三人尊称准确，角色辩护分析不前借未显示伤害',()=>{
  for(const id of ['q-c09-011','qe-c09-0018','qe-c09-0019','qe-c09-0020','q-c09-012','qe-c09-0021','qe-c09-0022']){
   expect(q(id).translation).toContain('勋爵大人');expect(q(id).translation).not.toContain('阁下');
  }
  expect(q('qe-c09-0022').optionsZh[1]).toBe('信任勋爵大人的智慧。');
  expect(q('qe-c09-0018').analyses[3]).not.toContain('前段');
  expect(q('qe-c09-0019').analyses[3]).toContain('misguided');
 });
 it('审阅20题22候选，保留8题，来源与答案位置不变',()=>{
  const r=read('source/question-revisions/review-076-report.json');
  expect(r.manual.questionCount).toBe(20);expect(r.manual.sourceCandidatesReviewed).toBe(22);
  expect(r.manual.revisedQuestionCount).toBe(12);expect(r.manual.questionReviews.filter((v:any)=>v.decision==='retained')).toHaveLength(8);
  expect(r.manual.pdfPagesVisuallyReviewed).toEqual([90,91]);expect(r.manual.pdfSourceBlocksTextMatched).toBe(3);
  expect(r.remainingQuestionReviews).toBe(1245);expect(r.fullQuestionBankHumanReview).toBe(false);
  for(const before of old){expect(q(before.id).answer).toBe(before.answer);expect(q(before.id).passage).toBe(before.passage);}
 });
});
