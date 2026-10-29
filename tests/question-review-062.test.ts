import {readFileSync} from 'node:fs';
import {describe,it,expect} from 'vitest';
const read=(p:string)=>JSON.parse(readFileSync(p,'utf8'));
const all=read('src/data/question-revision-catalog.json').questions;
const q=(id:string)=>all.find((v:any)=>v.id===id);
describe('第六十二批：在场者预测及访谈证据',()=>{
 it('访谈引用补全Shaq said，旧候选来源身份保持',()=>{
  const v=q('q-c07-035'),b=read('source/question-revisions/review-062-baseline.json').questions.find((r:any)=>r.id===v.id),s=read('public/data/book.json').sentences.find((r:any)=>r.id===v.evidence[0].sentenceIds[0]);expect(v.evidence[0].quote).toBe(s.text);expect(v.evidence[0].quote).toContain('Shaq said');expect(v.evidence[0].quote).toContain(b.evidence[0].quote);expect(v.evidence[0].sentenceIds).toEqual(b.evidence[0].sentenceIds);expect(v.evidence[0].sources).toEqual(b.evidence[0].sources);expect(v.passage).toBe(b.passage);
 });
 it('当前未给讲座地点的预测题只据在场教授，不预告后段结果',()=>{
  const v=q('qe-c07-0050');expect(v.options[v.answer]).toContain('in attendance');expect(v.options[v.answer]).not.toContain('lecture');expect(v.analyses[3]).not.toContain('Harvard');expect(v.vocabulary[0].context).toContain('未给出');expect(q('qe-c07-0049').analyses[3]).not.toContain('后段');
 });
 it('四题共享burnout译名保留可能性，不把人物状态当人人因果',()=>{
  for(const id of ['q-c07-030','qe-c07-0050','qe-c07-0051','qe-c07-0052']){expect(q(id).translation).toBe(q('q-c07-030').translation);expect(q(id).translation).toContain('Sidis 陷入了倦怠');expect(q(id).translation).toContain('也可能导致');expect(q(id).passage).toContain('might');expect(q(id).passage).toContain('could');}
 });
 it('19题22来源审阅真实，12题保留，未称全库审完',()=>{
  const r=read('source/question-revisions/review-062-report.json');expect(r.manual.questionCount).toBe(19);expect(r.manual.sourceCandidatesReviewed).toBe(22);expect(r.manual.revisedQuestionCount).toBe(7);expect(r.manual.questionReviews.filter((v:any)=>v.decision==='retained')).toHaveLength(12);expect(r.manual.additionalParagraphContextPages).toEqual([73]);expect(r.frozenCheckpoint).toContain('062-checkpoint');expect(r.remainingQuestionReviews).toBe(1539);expect(r.fullQuestionBankHumanReview).toBe(false);
 });
});
