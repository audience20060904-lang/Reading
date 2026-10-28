import {readFileSync} from 'node:fs';
import {describe,it,expect} from 'vitest';
const read=(p:string)=>JSON.parse(readFileSync(p,'utf8'));
const catalog=read('src/data/question-revision-catalog.json');
const q=(id:string)=>catalog.questions.find((v:any)=>v.id===id);
describe('第十批的限定语、单句可答性与测量范围',()=>{
 it('人群与推测限定不扩成所有搬迁者的确定结果',()=>{
  const v=q('q-c13-004');expect(v.options[v.answer]).toMatch(/may.*introverts/);
  const polley=q('q-c13-036');expect(polley.analyses.join('')).toContain('might consider');expect(polley.translation).not.toContain('网站');
 });
 it('条件时态及代词不增加前文依赖',()=>{
  const contrast=q('q-c13-024');expect(contrast.options[contrast.answer]).toBe('Staying would have distressed the speaker; moving would be unthinkable for his friend.');
  const walls=q('q-c13-042');expect(walls.options[walls.answer]).toBe('They are decorated with her numerous paintings.');expect(walls.passage).not.toContain('wife');
 });
 it('正确影像比较与直接化学测量的干扰明确分开',()=>{
  const brain=q('q-c13-063');expect(brain.options[brain.answer]).toContain('stronger reward-region activation');expect(brain.options[3]).toContain('directly measured amount of dopamine');expect(brain.analyses[3]).toContain('不是直接测量');
 });
});
