import {readFileSync} from 'node:fs';
import {describe,it,expect} from 'vitest';
const read=(p:string)=>JSON.parse(readFileSync(p,'utf8'));
const catalog=read('src/data/question-revision-catalog.json'),audit=read('source/question-semantic-audit.json'),targets=read('source/question-revisions/review-012-targets.json');
const q=(id:string)=>catalog.questions.find((v:any)=>v.id===id);
describe('第十二批的单片段可答性和续审清单',()=>{
 it('不要求由前一单元识别国籍或暑期项目，保留当前原句',()=>{
  const student=q('qe-c01-0005');expect(student.prompt).toContain('“She”');expect(student.prompt).not.toContain('Korean');expect(student.passage.startsWith('She was about to start')).toBe(true);
  const contrast=q('q-c01-006');expect(contrast.prompt).not.toContain('summer');expect(contrast.analyses[2]).not.toContain('出行目的是');
 });
 it('无意读研不升级为明确排除；单句解析不捏造首尾句',()=>{
  const plans=q('q-c01-038');expect(plans.options[plans.answer]).toContain('had not intended');expect(plans.options[plans.answer]).not.toContain('excluded');
  const family=q('q-c01-002');expect(family.analyses[0]).not.toContain('首尾句');expect(family.evidence[0].quote).toBe(family.passage);
 });
 it('新清单排除已审题、保留基线并按阅读顺序恢复',()=>{
  expect(new Set(audit.records.map((r:any)=>r.id)).size).toBe(audit.records.length);
  for(const r of audit.records)expect(audit.baselineReviewedQuestions).not.toContain(r.id);
  expect(targets.sourceCandidateIds.length).toBeLessThanOrEqual(25);
  expect(audit.records.slice(0,targets.questionIds.length).map((r:any)=>r.id)).toEqual(targets.questionIds);
  expect(audit.pending).toBe(audit.records.filter((r:any)=>r.status!=='reviewed').length);
  for(const r of audit.records.filter((r:any)=>r.reviewRecord==='source/question-revisions/review-012-report.json'))expect(read(r.reviewRecord).manual.questionIds).toContain(r.id);
 });
});
