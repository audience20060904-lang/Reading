import {describe,it,expect} from 'vitest';
import {readFileSync} from 'node:fs';
const read=(p:string)=>JSON.parse(readFileSync(p,'utf8'));
const catalog=read('src/data/question-revision-catalog.json');
const q=(id:string)=>catalog.questions.find((q:any)=>q.id===id);
describe('第八批主观评分、心态诱导及灾难叙述范围',()=>{
 it('相似感以评分者为参照，搬迁资料不误作实际实验分派',()=>{
  const similarity=q('q-c10-054');expect(similarity.options[similarity.answer]).toContain('student giving the rating');
  const proxy=q('q-c10-067');expect(proxy.options[proxy.answer]).toContain('indirect indicator');
  const comparison=q('q-c10-070');expect(comparison.prompt).not.toContain('reported');expect(comparison.analyses[0]).toContain('grew up');
 });
 it('隔年搬迁与至少十年是想象条件，完整证据保留think和控制组',()=>{
  const x=q('q-c10-071');expect(x.options[x.answer]).toContain('Imagining');expect(x.options[x.answer]).toContain('every other year');expect(x.options[x.answer]).toContain('at least ten years');
  expect(x.evidence[0].quote).toContain('asking some participants to think');expect(x.evidence[0].quote).toContain('(the control group)');
 });
 it('物理修复不是心理康复，Solnit引述保留解释层次和限定',()=>{
  const reconstruction=q('q-c11-033');expect(reconstruction.evidence[0].quote).toContain('current living conditions');expect(reconstruction.evidence[0].quote).toContain('had been spared');expect(reconstruction.analyses[2]).toContain('没有确立心理恢复');
  const quote=q('q-c11-040');expect(quote.evidence[0].quote).toContain('Solnit seems to argue');expect(quote.evidence[1].quote).toContain('sometimes');expect(quote.analyses[1]).toContain('本书作者');
 });
});
