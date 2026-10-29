import {readFileSync} from 'node:fs';
import {describe,it,expect} from 'vitest';
const read=(p:string)=>JSON.parse(readFileSync(p,'utf8'));
const revised=read('src/data/question-revision-catalog.json').questions;
const originals=read('public/data/questions.json');
const q=(id:string)=>revised.find((v:any)=>v.id===id)??originals.find((v:any)=>v.id===id);
describe('第四十六批：指代自足、目的与频率',()=>{
 it('him姓名未显示时，正确项不要求前段Mike信息',()=>{
  const v=q('qe-c05-0069');expect(v.passage).not.toContain('Mike');expect(v.options[v.answer]).not.toContain('Mike');expect(v.options[v.answer]).toContain('Pass on the message');expect(v.evidence[0].quote).toContain('Could you tell him');
 });
 it('主问题考原因、补充题考so I could write it down目的',()=>{
  expect(q('q-c05-040').prompt).toContain('Why');const v=q('qe-c05-0070');expect(v.prompt).toContain('What purpose');expect(v.analyses[v.answer]).toContain('so I could write it down');expect(v.options[v.answer]).toContain('write down');
 });
 it('拼写确认不预告下一短段理解的父亲身份，authentic不额外要求深入',()=>{
  const v=q('qe-c05-0073');expect(v.analyses[1]).not.toContain('后文才');expect(v.analyses[1]).toContain('不能推出');expect(q('qe-c05-0079').translation).not.toContain('深入');expect(q('qe-c05-0079').optionsZh[0]).toContain('很少');
 });
 it('实际审阅范围保留12题且不冒充全库，研究频率为weekly',()=>{
  const r=read('source/question-revisions/review-046-report.json');expect(r.manual.questionCount).toBe(19);expect(r.manual.sourceCandidatesReviewed).toBe(25);expect(r.manual.revisedQuestionCount).toBe(7);expect(r.manual.questionReviews.filter((v:any)=>v.decision==='retained')).toHaveLength(12);expect(r.fullQuestionBankHumanReview).toBe(false);const v=read('public/data/evidence-questions.json').find((v:any)=>v.id==='qe-c05-0081');expect(v.options[v.answer]).toContain('Every week');
 });
});
