import {readFileSync} from 'node:fs';
import {describe,it,expect} from 'vitest';
const read=(p:string)=>JSON.parse(readFileSync(p,'utf8'));
const revised=read('src/data/question-revision-catalog.json').questions;
const q=(id:string)=>revised.find((v:any)=>v.id===id);
describe('第五十三批：传记年代、局部指代与强推断',()=>{
 it('年代英文恢复1950s与1960s，popular不擅称畅销',()=>{
  expect(q('qe-c06-0072').options[1]).toContain('1950s');expect(q('qe-c06-0076').prompt).toContain('1960s');expect(q('qe-c06-0073').promptZh).toContain('受欢迎');expect(q('qe-c06-0073').promptZh).not.toContain('畅销');
 });
 it('当前首句死亡年龄与Instead活动题不要求未显示的前段数字或替代项',()=>{
  const v=q('qe-c06-0067');expect(v.prompt).toContain('opening sentence');expect(v.analyses.join(' ')).not.toMatch(/前段|此前专利|书数/);expect(v.passage.startsWith('He died at age 103.')).toBe(true);expect(q('q-c06-049').prompt).toContain('What activity');expect(q('q-c06-049').prompt).not.toContain('producing new novels');
 });
 it('must have been共享译文保持强推断地位，原作者措辞和历史不改',()=>{
  const ids=['q-c06-051','qe-c06-0078','qe-c06-0079'];for(const id of ids){const v=q(id);expect(v.translation).toBe(q(ids[0]).translation);expect(v.translation).toContain('作者推断');expect(v.translation).toContain('想必很高');expect(v.passage).toContain('must have been');}
  expect(q('qe-c06-0079').vocabulary[0].example).toContain('ground is wet');const b=read('source/question-revisions/review-053-baseline.json').questions.find((row:any)=>row.id===ids[0]);expect(q(ids[0]).version).toBe(b.version+1);expect(q(ids[0]).answer).toBe(b.answer);expect(q(ids[0]).passage).toBe(b.passage);
 });
 it('19题22来源候选的核对范围完整，原书历史记述不冒称独立史料核验',()=>{
  const r=read('source/question-revisions/review-053-report.json');expect(r.manual.questionCount).toBe(19);expect(r.manual.sourceCandidatesReviewed).toBe(22);expect(r.manual.revisedQuestionCount).toBe(11);expect(r.manual.questionReviews.filter((v:any)=>v.decision==='retained')).toHaveLength(8);expect(r.manual.findings.join(' ')).toContain('没有冒称独立史料核验');expect(r.fullQuestionBankHumanReview).toBe(false);expect(r.remainingQuestionReviews).toBe(1732);
 });
});
