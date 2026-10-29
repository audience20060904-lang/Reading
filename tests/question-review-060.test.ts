import {readFileSync} from 'node:fs';
import {describe,it,expect} from 'vitest';
const read=(p:string)=>JSON.parse(readFileSync(p,'utf8'));
const catalog=read('src/data/question-revision-catalog.json').questions;
const q=(id:string)=>catalog.find((v:any)=>v.id===id);
describe('第六十批：人物指代与翻译强度',()=>{
 it('当前只显示Simone的三题不要求知道姓氏，仍按周训练单位作答',()=>{
  for(const id of ['q-c07-011','qe-c07-0022','qe-c07-0023']){expect(q(id).prompt).toContain('Simone');expect(q(id).prompt).not.toContain('Biles');expect(q(id).promptZh).not.toContain('Biles');expect(q(id).passage).toContain('twenty to thirty-two hours per week');expect(q(id).translation).toContain('无与伦比的投入');}
 });
 it('excelled不添加最高级，原文could的可能性保留在分析',()=>{
  for(const id of ['q-c07-014','qe-c07-0029','qe-c07-0030']){expect(q(id).translation).toContain('表现出色');expect(q(id).translation).not.toContain('最擅长');expect(q(id).translation).toContain('过度专注可能');}expect(q('q-c07-012').analyses[3]).toContain('可能毁掉');expect(q('q-c07-012').analyses[3]).toContain('could');
 });
 it('another非额外总序数，年龄及追加活动不借未显示前后段',()=>{
  expect(q('qe-c07-0019').options[3]).toContain('another');expect(q('qe-c07-0019').options[3]).not.toContain('second');expect(q('qe-c07-0015').analyses[2]).not.toContain('Biles');expect(q('qe-c07-0018').prompt).not.toContain('swimming');expect(q('qe-c07-0018').analyses[0]).not.toContain('前面');expect(q('qe-c07-0021').analyses[2]).not.toContain('段出现');
 });
 it('23题24来源已核，12题保留且未冒称全库审完',()=>{
  const r=read('source/question-revisions/review-060-report.json');expect(r.manual.questionCount).toBe(23);expect(r.manual.sourceCandidatesReviewed).toBe(24);expect(r.manual.revisedQuestionCount).toBe(11);expect(r.manual.questionReviews.filter((v:any)=>v.decision==='retained')).toHaveLength(12);expect(r.manual.pdfPagesVisuallyReviewed).toEqual([69]);expect(r.remainingQuestionReviews).toBe(1582);expect(r.fullQuestionBankHumanReview).toBe(false);
 });
});
