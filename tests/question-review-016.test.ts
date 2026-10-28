import {readFileSync} from 'node:fs';
import {describe,it,expect} from 'vitest';
const read=(p:string)=>JSON.parse(readFileSync(p,'utf8')),catalog=read('src/data/question-revision-catalog.json');
const q=(id:string)=>catalog.questions.find((v:any)=>v.id===id);
describe('第十六批：观点区分与当前片段定位',()=>{
 it('相同重要性不偷换成所有研究者主张完全相同',()=>{
  const v=q('q-c01-022');expect(v.answer).toBe(1);expect(v.analyses[3]).toContain('不同主张');expect(v.analyses[3]).toContain('每位研究者');
 });
 it('在学校学到概念与技能改善地点明确区分',()=>{
  const v=q('q-c01-062');expect(v.analyses[0]).toContain('没有限定改善地点');expect(v.analyses[0]).toContain('不是证明');expect(v.options[v.answer]).toContain('can develop');
 });
 it('表1和三概念题的解析不借用前段材料',()=>{
  const concepts=q('qe-c01-0040');expect(concepts.analyses[1]).not.toContain('前面');
  const table=q('qe-c01-0041');expect(table.analyses[0]).toContain('Table 1');expect(table.analyses[1]).not.toContain('前面');expect(table.analyses[3]).not.toContain('故事');
 });
});
