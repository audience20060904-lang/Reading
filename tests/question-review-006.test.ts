import {describe,it,expect} from 'vitest';
import {readFileSync} from 'node:fs';
import {activeReading} from '../src/activeReading';
const read=(p:string)=>JSON.parse(readFileSync(p,'utf8'));
const catalog=read('src/data/question-revision-catalog.json');
const q=(id:string)=>catalog.questions.find((q:any)=>q.id===id);

describe('第六批断句修复与研究范围校对',()=>{
 it('修订叠加在真实断句版本上，不把相邻段落的187人再次混入',()=>{
  const fixed=read('src/data/sentence-repair-catalog.json').questions.find((q:any)=>q.id==='q-c06-031'),revised=q(fixed.id);
  expect(revised.passage).toBe(fixed.passage);expect(revised.sourceSegments).toEqual(fixed.sourceSegments);expect(revised.version).toBe(fixed.version+1);
  expect(revised.options.join(' ')).not.toContain('187');expect(revised.options.join(' ')).not.toContain('1,710');
  const active=activeReading(read('public/data/questions.json'),read('public/data/reading-plan.json'),read('public/data/evidence-questions.json'));
  expect(active.questions.find((q:any)=>q.id===fixed.id)).toEqual(revised);
 });
 it('另一场聚会保留概率，单句运动路径题不擅自添加年龄条件',()=>{
  const party=q('q-c06-059');expect(party.options[party.answer]).toContain('may encourage attending another');expect(party.optionsZh[party.answer]).toContain('另一场');
  const comparison=q('q-c07-017');expect(comparison.options[comparison.answer]).not.toContain('early');expect(comparison.analyses[comparison.answer]).toContain('没有额外规定开始年龄');
 });
 it('体育建议和人物解释保留条件、观点归属与限定语',()=>{
  const recommendation=q('q-c07-024');expect(recommendation.evidence[0].quote).toContain('suggest that if you are an elite athlete');
  const example=q('q-c07-033');expect(example.evidence[1].quote).toContain('appears to help');expect(example.evidence[0].quote).toContain('jokingly');
  const hypothesis=q('q-c06-082');expect(hypothesis.options[hypothesis.answer]).toContain('rather than a diagnosis');
 });
});
