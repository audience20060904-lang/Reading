import {readFileSync} from 'node:fs';
import {describe,it,expect} from 'vitest';
const read=(p:string)=>JSON.parse(readFileSync(p,'utf8')),catalog=read('src/data/question-revision-catalog.json');
const q=(id:string)=>catalog.questions.find((v:any)=>v.id===id);
describe('第三十一批：调查解释范围和报告对象',()=>{
 it('自报对象不换成亲友或成就，题干不凭空规定实际先后',()=>{
  const v=q('qe-c03-0031');expect(v.prompt).not.toContain('first');expect(v.promptZh).not.toContain('首先');expect(v.answer).toBe(2);expect(v.options[v.answer]).toBe('How meaningful they felt their own lives were.');expect(v.vocabulary[0].context).not.toContain('随后');
 });
 it('问法解释保留might，不能把是非形式变成所有回答都是幻觉',()=>{
  const v=q('qe-c03-0027');expect(v.answer).toBe(3);expect(v.options[v.answer]).toContain('might help explain');expect(v.options[0]).toContain('every yes response');expect(v.analyses[0]).toContain('扩大范围');expect(v.evidence[0].quote).toContain('One answer might lie in');
 });
 it('当前逻辑不借未来亲友研究，灾难困难不偷换成比例计算',()=>{
  expect(q('qe-c03-0030').analyses[2]).not.toContain('后文');const v=q('qe-c03-0035');expect(v.answer).toBe(1);expect(v.options[v.answer]).toContain('why the catastrophe');expect(v.analyses[3]).toContain('不是居民在灾后难以理解的对象');
 });
});
