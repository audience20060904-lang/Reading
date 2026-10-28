import {readFileSync} from 'node:fs';
import {describe,it,expect} from 'vitest';
const read=(p:string)=>JSON.parse(readFileSync(p,'utf8')),catalog=read('src/data/question-revision-catalog.json');
const q=(id:string)=>catalog.questions.find((v:any)=>v.id===id);
describe('第二十八批：第二章收尾与第三章书信',()=>{
 it('自述选项保持漫游/登山身份及said to himself，不借择校故事',()=>{
  const v=q('qe-c02-0105');expect(v.answer).toBe(2);expect(v.options[v.answer]).toBe('A wanderer and a mountain climber.');expect(v.options.join(' ')).not.toContain('university');expect(v.analyses[3]).toContain('自我描述');
 });
 it('四题章末译文一致并保留可能和偶尔，不变成抛弃一切舒适',()=>{
  const ids=['q-c02-027','qe-c02-0108','qe-c02-0109','qe-c02-0110'];for(const id of ids)expect(q(id).translation).toBe(q(ids[0]).translation);expect(q(ids[0]).translation).toContain('自己“满意即可”的选择心态');expect(q(ids[0]).translation).toContain('至少偶尔，人生或许');
 });
 it('书信观点归属不能改成斯多葛的中立定义',()=>{
  const v=q('qe-c03-0002');expect(v.answer).toBe(2);expect(v.options[1]).toContain('Stoics');expect(v.evidence[0].quote).toContain('Flaubert wrote to Louise Colet');expect(v.analyses[1]).toContain('福楼拜书信');
 });
 it('第二章全部现有题目均有基线或逐题记录，仍不宣称全库人工审完',()=>{
  const audit=read('source/question-semantic-audit.json'),reviewed=new Set([...audit.baselineReviewedQuestions,...audit.records.filter((r:any)=>r.status==='reviewed').map((r:any)=>r.id)]),questions=[...read('public/data/questions.json'),...read('public/data/evidence-questions.json')].filter((q:any)=>q.chapterId==='c02');
  expect(questions.length).toBeGreaterThan(150);for(const q of questions)expect(reviewed.has(q.id),q.id).toBe(true);expect(audit.pending).toBeGreaterThan(0);expect(read('source/question-revisions/review-028-report.json').fullQuestionBankHumanReview).toBe(false);
 });
});
