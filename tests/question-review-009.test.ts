import {describe,it,expect} from 'vitest';
import {readFileSync} from 'node:fs';
const read=(p:string)=>JSON.parse(readFileSync(p,'utf8'));
const catalog=read('src/data/question-revision-catalog.json');
const q=(id:string)=>catalog.questions.find((q:any)=>q.id===id);
describe('第九批自然实验、均值和叙述范围',()=>{
 it('自然实验保留可比性推定，反向解释不增加精确先后',()=>{
  const design=q('q-c11-044');expect(design.evidence[0].quote).toContain('as if randomly');expect(design.evidence[0].quote).toContain('presumably');
  const alternative=q('q-c11-057');expect(alternative.options[alternative.answer]).not.toContain('preceded');expect(alternative.options[alternative.answer]).toContain('may explain');
 });
 it('行为均值证据给出前后时点，年龄均值配对完整',()=>{
  const giving=q('q-c11-046');expect(giving.evidence[0].quote).toContain('Before the earthquake');expect(giving.evidence[1].quote).toContain('One month after');
  const ratings=q('q-c12-010');expect(ratings.evidence[1].quote).toContain('roughly age twenty');expect(ratings.evidence[2].quote).toContain('roughly forty-nine years old');expect(ratings.options[ratings.answer]).toContain('7.21 around thirty-five');
 });
 it('人生角色限定为故事呈现，作品公开时点不扩成额外策展安排',()=>{
  const role=q('q-c12-047');expect(role.evidence[0].quote).toContain('hero of the story or as an observer');expect(role.options[role.answer]).toContain('described as likely');
  const art=q('q-c12-055');expect(art.options[art.answer]).toContain('did not want it seen publicly while she lived');
 });
});
