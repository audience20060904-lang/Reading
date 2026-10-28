import {readFileSync} from 'node:fs';
import {describe,it,expect} from 'vitest';
const read=(p:string)=>JSON.parse(readFileSync(p,'utf8')),catalog=read('src/data/question-revision-catalog.json');
const q=(id:string)=>catalog.questions.find((v:any)=>v.id===id);
describe('第三十三批：限定程度与情绪负担',()=>{
 it('从冻结检查点恢复而不改原文和答案位置',()=>{
  const frozen=read('source/question-revisions/review-033-current-questions.json'),targets=read('source/question-revisions/review-033-targets.json'),base=read('source/question-revisions/review-033-baseline.json');expect(frozen.questions.map((q:any)=>q.id)).toEqual(targets.questionIds);expect(targets.questionIds).toHaveLength(12);for(const old of base.questions){expect(old).toEqual(frozen.questions.find((q:any)=>q.id===old.id));expect(q(old.id).version).toBe(old.version+1);expect(q(old.id).passage).toBe(old.passage);expect(q(old.id).answer).toBe(old.answer);}
 });
 it('not so good的程度和may保留，不强成所有生活都客观坏',()=>{
  const v=q('q-c03-038');expect(v.answer).toBe(3);expect(v.options[v.answer]).toContain('may');expect(v.options[v.answer]).toContain('not so good');expect(v.optionsZh[v.answer]).toContain('并不那么好');
 });
 it('taxing四题译文统一为负担，失败感不是已证明客观失败',()=>{
  const ids=['q-c03-043','qe-c03-0053','qe-c03-0054','qe-c03-0055'];for(const id of ids)expect(q(id).translation).toBe(q(ids[0]).translation);expect(q(ids[0]).translation).toContain('沉重的情绪负担');expect(q(ids[0]).translation).not.toContain('情绪耗竭');const v=q('qe-c03-0054');expect(v.options[v.answer]).toBe('It can make them feel like failures.');expect(v.analyses[1]).toContain('主观感受');
 });
});
