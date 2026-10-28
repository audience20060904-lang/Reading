import {readFileSync} from 'node:fs';
import {describe,it,expect} from 'vitest';
const read=(p:string)=>JSON.parse(readFileSync(p,'utf8')),catalog=read('src/data/question-revision-catalog.json');
const q=(id:string)=>catalog.questions.find((v:any)=>v.id===id);
describe('第三十五批：文学价值与当前片段',()=>{
 it('姓名未显示时以当前生活指代，不要求回读人物身份',()=>{
  const v=q('q-c04-008');expect(v.passage.startsWith('His life')).toBe(true);expect(v.options[3]).toBe('The first life described lacks both happiness and meaning.');expect(v.options[v.answer]).toContain('despite');expect(v.evidence[0].quote).toContain('According to Hesse');
 });
 it('核心两难与价值等同、身份核实、文学形式区分',()=>{
  const v=q('qe-c04-0019');expect(v.answer).toBe(3);expect(v.options.join(' ')).not.toMatch(/UVA|Cornell/);expect(v.analyses[1]).toContain('presumably');expect(v.analyses[2]).toContain('相似主题');expect(v.options[v.answer]).toBe('Whether to pursue an aesthetic life or a virtuous life.');
 });
 it('人物分析不借未显示经历，六次修订保留原文及答案',()=>{
  expect(q('qe-c04-0013').analyses[1]).not.toContain('前面 Goldmund');expect(q('qe-c04-0020').analyses[0]).not.toContain('后面');expect(q('qe-c04-0024').analyses[2]).toContain('当前句');const baseline=read('source/question-revisions/review-035-baseline.json');expect(baseline.questions).toHaveLength(6);for(const old of baseline.questions){const v=q(old.id);expect(v.version).toBe(old.version+1);expect(v.passage).toBe(old.passage);expect(v.answer).toBe(old.answer);}
 });
});
