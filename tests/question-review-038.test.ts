import {readFileSync} from 'node:fs';
import {describe,it,expect} from 'vitest';
const read=(p:string)=>JSON.parse(readFileSync(p,'utf8')),catalog=read('src/data/question-revision-catalog.json');
const q=(id:string)=>catalog.questions.find((v:any)=>v.id===id);
describe('第三十八批：原书日期与当前指代',()=>{
 it('按原书产品日期设题，译文不混入编辑说明',()=>{
  const a=q('qe-c04-0053'),b=q('qe-c04-0054');expect(a.translation).toBe(b.translation);expect(b.passage).toContain('the iMac in 2002');expect(b.options[b.answer]).toBe('The iPhone.');expect(a.translation).not.toMatch(/这里保留|原书依次/);expect(b.analyses[1]).toContain('2002');
 });
 it('单句he不依赖未显示姓名，日期和年龄直接匹配',()=>{
  const v=q('q-c04-032');expect(v.passage).not.toContain('Jobs');expect(v.prompt).not.toContain('Jobs');expect(v.translation).not.toContain('Jobs');expect(v.options[v.answer]).toBe('Forty-eight, in 2003.');expect(v.analyses[0]).not.toContain('此前');
 });
 it('对话解析不借未显示说话人或传记作者，原文姓名不改',()=>{
  expect(q('q-c04-034').analyses[2]).not.toContain('Bowers');const v=q('qe-c04-0055');expect(v.passage).toContain('Ann Bower,');expect(v.passage).toContain('Bowers replied');expect(v.analyses[1]).not.toContain('Isaacson');expect(v.translation).not.toContain('原页');expect(q('qe-c04-0056').translation).toBe(v.translation);
 });
 it('mid-80s保留年龄阶段，a decade不额外加about',()=>{
  const a=q('qe-c04-0060'),b=q('qe-c04-0061');expect(a.translation).toBe(b.translation);expect(a.translation).toContain('八十五岁左右');expect(a.translation).not.toContain('按原书');expect(b.options[b.answer]).toContain('a decade later');expect(b.options[b.answer]).not.toContain('about');
 });
});
