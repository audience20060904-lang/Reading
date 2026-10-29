import {readFileSync} from 'node:fs';
import {describe,it,expect} from 'vitest';
const read=(p:string)=>JSON.parse(readFileSync(p,'utf8'));
const revisions=read('src/data/question-revision-catalog.json').questions;
const originals=[...read('public/data/questions.json'),...read('public/data/evidence-questions.json')];
const q=(id:string)=>revisions.find((v:any)=>v.id===id)??originals.find((v:any)=>v.id===id);
describe('第四十九批：比较概率、比例与印文',()=>{
 it('less likely不是不可能，could假说不加确实',()=>{
  const ids=['q-c06-011','qe-c06-0016','qe-c06-0017','qe-c06-0018'];for(const id of ids){const v=q(id);expect(v.translation).toBe(q(ids[0]).translation);expect(v.translation).toContain('可能性真的更低');expect(v.translation).toContain('一种可能');expect(v.translation).not.toMatch(/更不可能|确实/);}
 });
 it('开放追问比较分类比例，不偷换平均分，也不称反问',()=>{
  const v=q('qe-c06-0017');expect(v.options[v.answer]).toContain('lower proportion classified as rich');expect(v.analyses[v.answer]).toContain('开放追问');expect(v.analyses[v.answer]).not.toContain('反问');expect(q('qe-c06-0011').analyses[2]).not.toContain('十五');
 });
 it('111、Forty及后段印文百分比原样保存，实际换算不一致提醒保留',()=>{
  for(const id of ['q-c06-014','qe-c06-0021','qe-c06-0022','qe-c06-0023']){const v=q(id);expect(v.passage).toContain('111 obituaries');expect(v.passage).toContain('Forty!');expect(v.translation).not.toContain('此处人数按原页保留');}
  expect(q('qe-c06-0023').analyses.join(' ')).not.toContain('34.5');const v=q('q-c06-015');expect(v.passage).toContain('34.5 percent');expect(v.passage).toContain('Eight individuals (6.9 percent)');expect(v.translation).toContain('不能一致换算');
 });
 it('实际范围22题23候选，保留原答案与未完成范围',()=>{
  const r=read('source/question-revisions/review-049-report.json');expect(r.manual.questionCount).toBe(22);expect(r.manual.sourceCandidatesReviewed).toBe(23);expect(r.manual.revisedQuestionCount).toBe(11);expect(r.manual.answerKeysChanged).toBe(0);expect(r.remainingQuestionReviews).toBe(1811);expect(r.fullQuestionBankHumanReview).toBe(false);
 });
});
