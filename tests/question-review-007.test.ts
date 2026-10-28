import {describe,it,expect} from 'vitest';
import {readFileSync} from 'node:fs';
const read=(p:string)=>JSON.parse(readFileSync(p,'utf8'));
const catalog=read('src/data/question-revision-catalog.json');
const q=(id:string)=>catalog.questions.find((q:any)=>q.id===id);
describe('第七批已测结果、预期与独立片段校对',()=>{
 it('不把心理丰富的作者猜测当成测量结果，完整保留推测证据',()=>{
  const x=q('q-c07-042');expect(x.options[x.answer]).toContain('unmeasured expectation');expect(x.evidence[1].quote).toContain('I suspect');expect(x.evidence[1].quote).toContain('would be particularly effective');
  const prediction=q('q-c08-036');expect(prediction.options[prediction.answer]).toContain('was expected');
 });
 it('姓名和图示背景不混入当前短段的必需信息',()=>{
  expect(q('q-c08-018').prompt).not.toContain('Marx');expect(q('q-c09-009').prompt).not.toContain('Stevens');
  const finals=q('q-c09-075');expect(finals.options.join(' ')).not.toContain('Houston');expect(finals.options[finals.answer]).toContain('without losing a game');
  expect(q('q-c09-064').options.join(' ')).not.toContain('beer');expect(q('q-c08-016').prompt).not.toContain('Kagan');
 });
 it('情绪证据涵盖成功与失败，外包警示保留无意和潜在机会成本',()=>{
  const x=q('q-c08-015');expect(x.evidence[1].quote).toContain('pride');expect(x.evidence[1].quote).toContain('frustration and sadness');
  const hiring=q('q-c08-058');expect(hiring.options[hiring.answer]).toContain('may unintentionally');expect(hiring.options[hiring.answer]).toContain('potentially');
 });
});
