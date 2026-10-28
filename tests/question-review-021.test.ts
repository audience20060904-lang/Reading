import {readFileSync} from 'node:fs';
import {describe,it,expect} from 'vitest';
const read=(p:string)=>JSON.parse(readFileSync(p,'utf8')),catalog=read('src/data/question-revision-catalog.json');
const q=(id:string)=>catalog.questions.find((v:any)=>v.id===id);
describe('第二十一批：预期比较和当前片段的充分性',()=>{
 it('未获tenure的实际感受与预期比较，不偷换成已获tenure者',()=>{
  const v=q('q-c02-005');expect(v.options[v.answer]).toContain('far happier');expect(v.options[v.answer]).toContain('current assistant professors had imagined');expect(v.analyses[0]).not.toContain('已经访谈');
 });
 it('三句频率关系不借前段事件大小，role不升级为决定',()=>{
  const v=q('q-c02-006');expect(v.options[v.answer]).toBe('Frequent positive events and close relationships.');expect(v.prompt).not.toContain('long-term');expect(v.analyses[3]).not.toContain('coffee');
  const role=q('qe-c02-0024');expect(role.options[role.answer]).toContain('role of success');expect(role.options[role.answer]).not.toContain('determines');
 });
 it('手机叙述明确修复内存，不把显示五格当成修好连接',()=>{
  const v=q('qe-c02-0034');expect(v.answer).toBe(1);expect(v.options[v.answer]).toBe('The memory problem.');expect(v.evidence[0].quote).toBe('Eventually, Apple fixed the memory problem.');expect(v.analyses[0]).toContain('没有说修好该连接');
 });
});
