import {readFileSync} from 'node:fs';
import {describe,it,expect} from 'vitest';
const read=(p:string)=>JSON.parse(readFileSync(p,'utf8')),catalog=read('src/data/question-revision-catalog.json');
const q=(id:string)=>catalog.questions.find((v:any)=>v.id===id);
describe('第四十一批：局部证据与不确定程度',()=>{
 it('当前First/Then顺序题不使用未显示Finally作为排除依据',()=>{
  const v=q('qe-c05-0004');expect(v.passage).not.toContain('Finally');expect(v.options[v.answer]).toBe('The happiest event.');expect(v.analyses.join(' ')).not.toMatch(/更后|Finally/);expect(v.analyses[0]).toContain('Then');
 });
 it('人物出处和地点排除不再提前指认另一人物故事',()=>{
  expect(q('qe-c05-0008').analyses[0]).not.toContain('Rachel');expect(q('qe-c05-0008').analyses[3]).not.toMatch(/候选ID|人工定稿/);expect(q('qe-c05-0010').analyses.join(' ')).not.toMatch(/出租车|Joy|前面 Grace/);expect(q('qe-c05-0011').analyses[3]).toContain('时间联系');
 });
 it('三题译文保留could not quite和动机未确定的限定',()=>{
  const ids=['q-c05-008','qe-c05-0012','qe-c05-0013'];for(const id of ids){expect(q(id).translation).toBe(q(ids[0]).translation);expect(q(id).translation).toContain('没能完全弄明白');}expect(q('qe-c05-0013').options[q('qe-c05-0013').answer]).toContain('not established with certainty');
 });
 it('温度干扰区分程度扩大、无据比较与原因推断，不伪造实测',()=>{
  const v=q('qe-c05-0012');expect(v.options[v.answer]).toBe('Not warm.');expect(v.options.join(' ')).not.toMatch(/Extremely freezing|thermometer/);expect(v.analyses[0]).toContain('程度');expect(v.analyses[2]).toContain('没有比较');expect(v.analyses[3]).toContain('已确认的解释');
 });
});
