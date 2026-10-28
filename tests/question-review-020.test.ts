import {readFileSync} from 'node:fs';
import {describe,it,expect} from 'vitest';
const read=(p:string)=>JSON.parse(readFileSync(p,'utf8')),catalog=read('src/data/question-revision-catalog.json');
const q=(id:string)=>catalog.questions.find((v:any)=>v.id===id);
describe('第二十批：统计对象、归属与时间限定',()=>{
 it('尝试与意念统计不同，不把中文连接词读成互斥人群',()=>{
  const qs=['q-c02-034','qe-c02-0011','qe-c02-0012','qe-c02-0013'].map(q);expect(new Set(qs.map(v=>v.translation)).size).toBe(1);
  for(const v of qs){expect(v.translation).not.toContain('另有');expect(v.translation).toContain('以及');expect(v.passage).toContain('1.2 million suicide attempts and 12.2 million American adults');}
 });
 it('六个月内和似乎保留，不偷换成约六个月或第六个月固定时点',()=>{
  const v=q('q-c02-040');expect(v.options[v.answer]).toBe('Its effect seems to disappear within six months.');expect(v.options[v.answer]).not.toContain('about');expect(v.analyses[0]).toContain('不能换成固定');
 });
 it('负面标签明确属于被分析的文化叙事',()=>{
  expect(q('q-c02-039').translation).toBe(q('qe-c02-0020').translation);expect(q('q-c02-039').translation.startsWith('按照这里描述的文化叙事')).toBe(true);
  expect(q('qe-c02-0020').prompt).toContain('people who are unhappy');
 });
 it('当前片段分析不借前后研究，预测误差保留倾向',()=>{
  expect(q('qe-c02-0008').analyses[1]).not.toContain('另一组');expect(q('qe-c02-0015').analyses[0]).not.toContain('前面');expect(q('q-c02-003').analyses[3]).not.toContain('strong association');expect(q('q-c02-004').analyses[1]).toContain('所有人每次');
 });
});
