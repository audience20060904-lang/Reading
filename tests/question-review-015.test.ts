import {readFileSync} from 'node:fs';
import {describe,it,expect} from 'vitest';
const read=(p:string)=>JSON.parse(readFileSync(p,'utf8')),catalog=read('src/data/question-revision-catalog.json');
const q=(id:string)=>catalog.questions.find((v:any)=>v.id===id);
describe('第十五批的类比、研究贡献和信息平行性',()=>{
 it('巧克力仅为体验类比，正确概括仍有混合性质',()=>{
  const v=q('q-c01-019');expect(v.options[v.answer]).toContain('mixture of qualities');expect(v.analyses[1]).toContain('complexity');expect(v.passage).toContain('not just good or bad');
 });
 it('导师论文题各选项平行，不以唯一最长项作为正确线索',()=>{
  const v=q('q-c01-055');for(const option of v.options)expect(option).toContain('1984');expect(v.options[v.answer].length).toBeLessThan(Math.max(...v.options.map((s:string)=>s.length)));expect(v.analyses[2]).toContain('one of the first');
 });
 it('研究贡献解析不泄露未显示的后续人物或基因内容',()=>{
  const contribution=q('q-c01-020');expect(contribution.prompt).toContain('Ed and his students');expect(contribution.analyses[2]).not.toContain('Ryff');
  const debate=q('qe-c01-0032');expect(debate.analyses[2]).not.toContain('后面');expect(debate.analyses[2]).toContain('本句没有');
 });
});
