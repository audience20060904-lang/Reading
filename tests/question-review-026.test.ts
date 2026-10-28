import {readFileSync} from 'node:fs';
import {describe,it,expect} from 'vitest';
const read=(p:string)=>JSON.parse(readFileSync(p,'utf8')),catalog=read('src/data/question-revision-catalog.json');
const q=(id:string)=>catalog.questions.find((v:any)=>v.id===id);
describe('第二十六批：条件预期、可见身份与内部感受证据',()=>{
 it('当前只写He的三道题无需未显示的Clark身份即可作答',()=>{
  for(const id of ['q-c02-022','qe-c02-0083','qe-c02-0085']){expect(q(id).passage).not.toContain('Clark');expect(q(id).prompt).not.toContain('Clark');}
 });
 it('财务目标序列不推定已测得的内心不满，if译为如果就而非只有才',()=>{
  const v=q('q-c02-022');expect(v.answer).toBe(3);expect(v.options[v.answer]).toContain('higher or comparative wealth targets');expect(v.options[v.answer]).not.toContain('dissatisfaction');expect(v.translation).toContain('如果赚到一亿美元，自己就会幸福');expect(v.translation).not.toContain('才会幸福');for(const id of ['qe-c02-0083','qe-c02-0084','qe-c02-0085','qe-c02-0086'])expect(q(id).translation).toBe(v.translation);
 });
 it('good enough指选择标准而非心态自身质量，当前解释不用前后段落',()=>{
  const v=q('q-c02-073');expect(v.translation).toContain('“足够好就行”的选择心态');expect(q('qe-c02-0081').translation).toBe(v.translation);expect(q('qe-c02-0082').analyses[0]).not.toContain('后文');expect(q('qe-c02-0080').analyses[2]).not.toContain('前文');
 });
});
