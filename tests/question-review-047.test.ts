import {readFileSync} from 'node:fs';
import {describe,it,expect} from 'vitest';
const read=(p:string)=>JSON.parse(readFileSync(p,'utf8'));
const revisions=read('src/data/question-revision-catalog.json').questions;
const q=(id:string)=>revisions.find((v:any)=>v.id===id);
describe('第四十七批：比较程度、主张归属与报告指标',()=>{
 it('两组活动译文保留far与likely，不改写固定英文原文',()=>{
  const ids=['q-c05-049','qe-c05-0082','qe-c05-0083','qe-c05-0084'];for(const id of ids){const v=q(id);expect(v.translation).toBe(q(ids[0]).translation);expect(v.translation).toContain('可能性高得多');expect(v.translation).toContain('可能性低得多');expect(v.passage).toContain('far more likely');expect(v.passage).toContain('far less likely');}
 });
 it('popular不擅增销量断言，Cain归属排除不需下一章信息',()=>{
  for(const id of ['q-c05-051','qe-c05-0086','qe-c05-0087']){expect(q(id).translation).toContain('广受欢迎的书');expect(q(id).translation).not.toContain('畅销');}
  expect(q('qe-c05-0086').analyses.join(' ')).not.toContain('下一章');expect(q('qe-c05-0086').analyses[2]).toContain('Susan Cain contends that');
 });
 it('less happiness是感受水平低而不是报告数量少，原答案与旧稿保留',()=>{
  const ids=['q-c05-055','qe-c05-0093','qe-c05-0094'];for(const id of ids){const v=q(id);expect(v.translation).toBe(q(ids[0]).translation);expect(v.translation).toContain('自报的幸福感就越低');expect(v.translation).not.toContain('幸福报告越少');}
  const v=q(ids[0]),baseline=read('source/question-revisions/review-047-baseline.json').questions.find((v:any)=>v.id===ids[0]);expect(v.answer).toBe(baseline.answer);expect(v.version).toBe(baseline.version+1);expect(baseline.translation).toContain('幸福报告越少');expect(v.optionsZh[v.answer]).toContain('幸福感更低');
 });
 it('本批保留正确题，范围与待审不假称全库完成',()=>{
  const r=read('source/question-revisions/review-047-report.json');expect(r.manual.questionCount).toBe(22);expect(r.manual.sourceCandidatesReviewed).toBe(24);expect(r.manual.revisedQuestionCount).toBe(11);expect(r.manual.questionReviews.filter((v:any)=>v.decision==='retained')).toHaveLength(11);expect(r.fullQuestionBankHumanReview).toBe(false);expect(r.remainingQuestionReviews).toBe(1853);
 });
});
