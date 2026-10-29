import {readFileSync} from 'node:fs';
import {describe,it,expect} from 'vitest';
const read=(p:string)=>JSON.parse(readFileSync(p,'utf8')),catalog=read('src/data/question-revision-catalog.json');
const q=(id:string)=>catalog.questions.find((v:any)=>v.id===id);
describe('第四十三批：意义范围与额外推断',()=>{
 it('四题pointless译文只表达意义判断，选项译文保持一致',()=>{
  const ids=['q-c05-016','qe-c05-0030','qe-c05-0031','qe-c05-0032'];for(const id of ids){expect(q(id).translation).toBe(q(ids[0]).translation);expect(q(id).translation).not.toContain('全然没有价值');expect(q(id).translation).toContain('全无意义');}expect(q('qe-c05-0032').optionsZh[0]).toContain('全无意义');
 });
 it('完成活动不额外添加主观感受，必要休息不指定生理机制',()=>{
  const a=q('q-c05-018'),b=q('q-c05-019');expect(a.options[a.answer]).toContain('being entirely wasted');expect(a.options[a.answer]).not.toContain('feeling');expect(b.optionsZh[b.answer]).not.toContain('恢复体力');expect(b.optionsZh[b.answer]).toContain('可能');
 });
 it('诗歌比较与维度识别不借未显示标题、研究者或编号',()=>{
  expect(q('qe-c05-0036').analyses[0]).not.toContain('Happiness');expect(q('qe-c05-0036').analyses[2]).not.toContain('后面');expect(q('qe-c05-0040').analyses[3]).not.toContain('第三');expect(q('qe-c05-0040').vocabulary[0].context).not.toContain('前面');
 });
 it('extraordinarily定位保持副词，与原句逐字相符',()=>{
  const v=q('qe-c05-0041'),phrase='we don’t have to be extraordinarily good or virtuous';expect(v.passage).toContain(phrase);expect(v.analyses[1]).toContain(phrase);expect(v.analyses[1]).not.toContain('extraordinary good');
 });
});
