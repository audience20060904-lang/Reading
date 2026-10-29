import {readFileSync} from 'node:fs';
import {describe,it,expect} from 'vitest';
const read=(p:string)=>JSON.parse(readFileSync(p,'utf8'));
const revisions=read('src/data/question-revision-catalog.json').questions;
const q=(id:string)=>revisions.find((v:any)=>v.id===id);
describe('第四十八批：评分范围与分类门槛',()=>{
 it('正确阈值只声明三名评分者与四项平均，不增加未展开的汇总算法',()=>{
  const v=q('q-c06-006');expect(v.options[v.answer]).toContain('at least 3.67 out of 5 across four items');expect(v.options[v.answer]).toContain('assigned by the three raters');expect(v.options[v.answer]).not.toContain('averaged across four items and the raters');expect(v.analyses[v.answer]).toContain('没有进一步展开');
 });
 it('一至五分与十二主题不混同，选项数字与词语有正常间距',()=>{
  const v=q('qe-c06-0007');expect(v.analyses[2]).toContain('on a scale of 1 to 5');expect(v.analyses[3]).not.toContain('十二主题');expect(q('qe-c06-0009').options[2]).toContain('all 101');expect(q('qe-c06-0009').options[3]).toContain('exactly 5');expect(q('qe-c06-0010').options[3]).toContain("month's 101");
 });
 it('记录正确解答的遗留题型标签问题，不隐藏为全库完美',()=>{
  const r=read('source/question-revisions/review-048-report.json');expect(r.manual.questionCount).toBe(20);expect(r.manual.sourceCandidatesReviewed).toBe(25);expect(r.manual.revisedQuestionCount).toBe(7);expect(r.manual.questionReviews.find((v:any)=>v.questionId==='q-c06-005').judgement).toContain('分类待专项核对');expect(r.fullQuestionBankHumanReview).toBe(false);const t=read('source/optimization-tasks.json');expect(t.semanticReview.relatedFollowUpFindings.some((v:any)=>v.questionId==='q-c06-005')).toBe(true);expect(t.semanticReview.relatedFollowUpFindings.some((v:any)=>v.questionId==='q-c04-028')).toBe(true);
 });
});
