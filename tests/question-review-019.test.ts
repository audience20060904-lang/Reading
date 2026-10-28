import {readFileSync} from 'node:fs';
import {describe,it,expect} from 'vitest';
const read=(p:string)=>JSON.parse(readFileSync(p,'utf8')),catalog=read('src/data/question-revision-catalog.json');
const q=(id:string)=>catalog.questions.find((v:any)=>v.id===id);
describe('第十九批：归属、推断语气与章节审阅范围',()=>{
 it('must have been保留过去推断，不改成临床因果确认',()=>{
  const qs=['q-c02-032','qe-c02-0006','qe-c02-0007'].map(q);expect(new Set(qs.map(v=>v.translation)).size).toBe(1);
  for(const v of qs){expect(v.passage).toContain('must have been driven');expect(v.translation).toContain('想必不只是');expect(v.translation).not.toContain('一定不只是');}
  expect(q('q-c02-032').analyses[2]).toContain('没有');expect(q('q-c02-032').analyses[2]).toContain('临床因果测量');
 });
 it('first-year不被当作学位层级判断，日期不借后面统计',()=>{
  expect(q('qe-c02-0004').analyses[1]).toContain('不是区分本科与研究生的充分信息');
  const date=q('qe-c02-0005');expect(date.analyses[0]).not.toContain('后文');expect(date.evidence[0].quote).toContain('January 17, 2014');
 });
 it('第1章当前137题均有审阅记录，但不推出全书人工定稿',()=>{
  const audit=read('source/question-semantic-audit.json'),known=new Set([...audit.baselineReviewedQuestions,...audit.records.filter((r:any)=>r.status==='reviewed').map((r:any)=>r.id)]),questions=[...read('public/data/questions.json'),...read('public/data/evidence-questions.json')].filter((q:any)=>q.chapterId==='c01');
  expect(questions).toHaveLength(137);for(const v of questions)expect(known.has(v.id),v.id).toBe(true);
  expect(audit.records.filter((r:any)=>r.status!=='reviewed'&&r.id.includes('c01'))).toHaveLength(0);expect(audit.pending).toBeGreaterThan(0);expect(read('source/question-revisions/review-019-report.json').fullQuestionBankHumanReview).toBe(false);
 });
});
