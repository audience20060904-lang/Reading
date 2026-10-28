import {readFileSync} from 'node:fs';
import {describe,it,expect} from 'vitest';
const read=(p:string)=>JSON.parse(readFileSync(p,'utf8')),catalog=read('src/data/question-revision-catalog.json');
const q=(id:string)=>catalog.questions.find((v:any)=>v.id===id);
describe('第二十四批：单句足够、监护安排与压力范围',()=>{
 it('soma只依当前可见作品引文归属，不借作者后段做法',()=>{
  const v=q('q-c02-018');expect(v.answer).toBe(3);expect(v.options[v.answer]).toBe('As a quotation from Aldous Huxley’s Brave New World.');expect(v.analyses.join(' ')).not.toContain('personally 后');expect(v.evidence[0].quote).toContain('Aldous Huxley writes');
 });
 it('自然能力单句无需下一段的心理免疫名称才能作答',()=>{
  const v=q('q-c02-010');expect(v.prompt).not.toContain('psychological immune system');expect(v.answer).toBe(3);expect(v.options[v.answer]).toContain('natural capacity');expect(v.analyses[2]).toContain('承认这些主动策略有效');
 });
 it('视角段译文保留前妻监护、假设和could效果，不借下一段比喻',()=>{
  const v=q('q-c02-019');expect(v.translation).toContain('孩子由前妻监护');expect(v.translation).toContain('可能');expect(v.analyses[3]).not.toContain('小颠簸');for(const id of ['qe-c02-0061','qe-c02-0062'])expect(q(id).translation).toBe(v.translation);
 });
 it('无压力人群不放宽为任何较少压力者，也不说完全不主动改变',()=>{
  const v=q('q-c02-066');expect(v.prompt).toContain('do not feel pressure');expect(v.translation).toContain('不会那么努力');const ref=q('qe-c02-0064');expect(ref.options[ref.answer]).toContain('do not feel pressure');expect(ref.translation).toBe(v.translation);expect(q('qe-c02-0065').translation).toBe(v.translation);
 });
});
