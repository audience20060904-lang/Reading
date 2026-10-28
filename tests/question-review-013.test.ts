import {readFileSync} from 'node:fs';
import {describe,it,expect} from 'vitest';
const read=(p:string)=>JSON.parse(readFileSync(p,'utf8')),catalog=read('src/data/question-revision-catalog.json');
const q=(id:string)=>catalog.questions.find((v:any)=>v.id===id);
describe('第十三批的推想范围与单元独立性',()=>{
 it('多数人的推想不泛化成全部读者的调查结果',()=>{
  const v=q('qe-c01-0014');expect(v.options[v.answer]).toBe('Most have repeatedly asked themselves the same question.');expect(v.analyses[v.answer]).toContain('不是读者问卷结果');expect(v.passage).toContain('I imagine most of you');
 });
 it('题干不强定指代，取舍解析不引用上一段的Some/Others',()=>{
  const areas=q('qe-c01-0013');expect(areas.prompt).toContain('question described here');expect(areas.prompt).not.toContain('stay-or-go');
  const choices=q('q-c01-010');expect(choices.analyses[3]).not.toContain('Some');expect(choices.evidence[0].quote).toContain('trade-offs');
 });
 it('正确项不加后文证明或将愿望当已经发生的事实',()=>{
  const literary=q('q-c01-012');expect(literary.analyses[0]).toContain('没有');expect(literary.analyses[0]).not.toContain('后文');
  const wish=q('qe-c01-0060');expect(wish.passage).toContain('I wish I could');expect(wish.analyses[1]).toContain('每周一个晚上');
 });
});
