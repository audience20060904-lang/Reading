import {readFileSync} from 'node:fs';
import {describe,it,expect} from 'vitest';
const read=(p:string)=>JSON.parse(readFileSync(p,'utf8')),catalog=read('src/data/question-revision-catalog.json');
const q=(id:string)=>catalog.questions.find((v:any)=>v.id===id);
describe('第二十二批：实验角色、当前证据与条件译文',()=>{
 it('未知的是总体信念，表情操作与漫画评价不可混为一谈',()=>{
  const belief=q('qe-c02-0035');expect(belief.answer).toBe(3);expect(belief.evidence[0].quote).toContain('don’t know definitively whether most Americans assume');
  expect(belief.options.join(' ')).not.toMatch(/iPhone|tenure/);const task=q('qe-c02-0036');expect(task.answer).toBe(0);expect(task.options[task.answer]).toContain('smiling or not smiling');
 });
 it('两句来源中不存在的末句和假笑对比不进入当前证据解释',()=>{
  const result=q('q-c02-014');expect(result.analyses[1]).toContain('没有比较');expect(result.analyses[1]).not.toContain('末句把');
  const failure=q('q-c02-008');expect(failure.analyses[3]).toContain('everyone failed');expect(failure.analyses[3]).not.toContain('末句');
  expect(q('q-c02-007').prompt).not.toContain('pen-in-the-mouth');expect(q('q-c02-009').analyses[0]).toContain('国家层面');
 });
 it('同段译文一致，保留评分方向、倾向和即使条件',()=>{
  const cartoon=q('q-c02-048');expect(cartoon.translation).toContain('好笑程度评分，高于');expect(q('qe-c02-0038').translation).toBe(cartoon.translation);
  const tendency=q('q-c02-049');expect(tendency.translation).toContain('即使假笑没有这种效果');expect(tendency.translation).toContain('往往');expect(q('qe-c02-0043').translation).toBe(tendency.translation);
  expect(q('qe-c02-0045').translation).toBe(q('q-c02-053').translation);
 });
});
