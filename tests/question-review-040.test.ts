import {readFileSync} from 'node:fs';
import {describe,it,expect} from 'vitest';
const read=(p:string)=>JSON.parse(readFileSync(p,'utf8')),catalog=read('src/data/question-revision-catalog.json');
const q=(id:string)=>catalog.questions.find((v:any)=>v.id===id);
describe('第四十批：括号续接和第四章收尾',()=>{
 it('完整双胞胎原句仍跨两个来源ID引用，解析只讲阅读内容',()=>{
  const v=q('qe-c04-0081');expect(v.evidence[0].quote).toBe('She had had two of the four (twins!) at age eighteen before they met.');expect(v.evidence[0].sentenceIds).toHaveLength(2);expect(v.analyses[3]).not.toMatch(/候选ID|误分/);expect(v.vocabulary[0].context).not.toContain('后来亲自');
 });
 it('年龄和伦理解释不借上段52岁55岁或标签反应',()=>{
  expect(q('qe-c04-0082').analyses.join(' ')).not.toMatch(/此前|候选ID|续接片段/);expect(q('qe-c04-0082').analyses[3]).toContain('before they met');expect(q('qe-c04-0083').analyses[1]).not.toContain('前段');expect(q('qe-c04-0083').analyses[1]).toContain('当前');
 });
 it('she开头的独立片段无需未显示姓名',()=>{
  for(const id of ['qe-c04-0080','qe-c04-0085']){const v=q(id);expect(v.passage).not.toContain('Linda');expect(v.prompt).not.toContain('Linda');}expect(q('qe-c04-0080').options[q('qe-c04-0080').answer]).toBe('Her ex-husband.');
 });
 it('第四章141道现有题均有记录，但全库审阅仍在继续',()=>{
  const audit=read('source/question-semantic-audit.json'),reviewed=new Set([...audit.baselineReviewedQuestions,...audit.records.filter((r:any)=>r.status==='reviewed').map((r:any)=>r.id)]),questions=[...read('public/data/questions.json'),...read('public/data/evidence-questions.json')].filter((v:any)=>v.chapterId==='c04');expect(questions).toHaveLength(141);for(const v of questions)expect(reviewed.has(v.id),v.id).toBe(true);expect(audit.pending).toBeGreaterThan(0);expect(read('source/question-revisions/review-040-report.json').fullQuestionBankHumanReview).toBe(false);
 });
});
