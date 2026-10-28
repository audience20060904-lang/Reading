import {readFileSync} from 'node:fs';
import {describe,it,expect} from 'vitest';
const read=(p:string)=>JSON.parse(readFileSync(p,'utf8')),catalog=read('src/data/question-revision-catalog.json');
const q=(id:string)=>catalog.questions.find((v:any)=>v.id===id);
describe('第三十四批：两途限制与文学角色',()=>{
 it('限制是只关注两途，保留道路本身的益处',()=>{
  const v=q('q-c03-046');expect(v.options[v.answer]).toBe('To widen the possibilities beyond an exclusive focus on two beneficial paths.');expect(v.optionsZh[v.answer]).toContain('只关注');expect(v.passage).toContain('countless benefits');
 });
 it('奖项修饰作者、描写对象仍在寻找道路，不混电影制作史',()=>{
  const v=q('qe-c04-0005');expect(v.options[0]).toContain('1946');expect(v.options[2]).toContain('2020');expect(v.options[v.answer]).toContain('struggling');expect(v.analyses[0]).toContain('作者 Hesse');expect(v.analyses[2]).toContain('制作史');expect(q('qe-c04-0006').analyses[3]).not.toContain('Kierkegaard');
 });
 it('角色回指、职位和怀疑的排除依据来自当前段落',()=>{
  expect(q('qe-c04-0007').analyses[0]).toContain('最近');expect(q('qe-c04-0009').analyses[3]).toContain('head of his monastery');expect(q('qe-c04-0011').analyses[3]).toContain('当前段落');expect(q('qe-c04-0011').analyses[3]).not.toContain('不同道路');
 });
 it('第三章106道现有题都有记录，仍明确全库尚未审完',()=>{
  const audit=read('source/question-semantic-audit.json'),reviewed=new Set([...audit.baselineReviewedQuestions,...audit.records.filter((r:any)=>r.status==='reviewed').map((r:any)=>r.id)]),questions=[...read('public/data/questions.json'),...read('public/data/evidence-questions.json')].filter((v:any)=>v.chapterId==='c03');
  expect(questions).toHaveLength(106);for(const v of questions)expect(reviewed.has(v.id),v.id).toBe(true);expect(audit.pending).toBeGreaterThan(0);expect(read('source/question-revisions/review-034-report.json').fullQuestionBankHumanReview).toBe(false);
 });
});
