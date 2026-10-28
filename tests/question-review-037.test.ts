import {readFileSync} from 'node:fs';
import {describe,it,expect} from 'vitest';
const read=(p:string)=>JSON.parse(readFileSync(p,'utf8')),catalog=read('src/data/question-revision-catalog.json');
const q=(id:string)=>catalog.questions.find((v:any)=>v.id===id);
describe('第三十七批：冻结恢复和引语精度',()=>{
 it('冻结快照与修订基线一致，原文、答案和来源不变',()=>{
  const old=read('source/question-revisions/review-037-current-questions.json'),targets=read('source/question-revisions/review-037-targets.json'),base=read('source/question-revisions/review-037-baseline.json');expect(old.questions.map((v:any)=>v.id)).toEqual(targets.questionIds);expect(targets.sourceCandidateIds).toHaveLength(24);for(const before of base.questions){expect(before).toEqual(old.questions.find((v:any)=>v.id===before.id));const after=q(before.id);expect(after.version).toBe(before.version+1);expect(after.answer).toBe(before.answer);expect(after.passage).toBe(before.passage);expect(after.sentenceIds).toEqual(before.sentenceIds);}
 });
 it('历史推断译文与旧主问题一致，相关线索不成为全面照抄结论',()=>{
  for(const id of ['qe-c04-0038','qe-c04-0039','qe-c04-0040'])expect(q(id).translation).toBe(q('q-c04-021').translation);expect(q('qe-c04-0040').options[1]).toContain('origin of Buddhism');expect(q('qe-c04-0040').analyses[3]).toContain('每位思想家');
 });
 it('instead不加比较数量，is not保留否定，个人回顾归属保留',()=>{
  const a=q('qe-c04-0050'),b=q('qe-c04-0051');expect(a.translation).toBe(b.translation);expect(a.translation).toContain('而是使用直觉');expect(a.translation).toContain('在另一些方面则并非如此');expect(a.translation).not.toContain('未必');expect(b.analyses[3]).toContain('个人反思');
 });
 it('词义不伪造章节位置；基线已审题不重计',()=>{
  expect(q('q-c04-027').vocabulary[0].context).not.toContain('下一章');expect(q('qe-c04-0045').prompt).not.toContain('Gopnik');const audit=read('source/question-semantic-audit.json'),targets=read('source/question-revisions/review-037-targets.json');expect(targets.questionIds.some((id:string)=>audit.baselineReviewedQuestions.includes(id))).toBe(false);expect(targets.questionIds).not.toContain('q-c04-028');expect(read('source/question-revisions/review-037-report.json').fullQuestionBankHumanReview).toBe(false);
 });
});
