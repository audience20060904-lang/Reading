import {readFileSync} from 'node:fs';
import {describe,it,expect} from 'vitest';
const read=(p:string)=>JSON.parse(readFileSync(p,'utf8')),catalog=read('src/data/question-revision-catalog.json');
const q=(id:string)=>catalog.questions.find((v:any)=>v.id===id);
describe('第二十七批：可见心态、回指与设想立场',()=>{
 it('this mindset单句风险不要求辨认未显示的标签',()=>{
  const v=q('q-c02-012');expect(v.passage).not.toContain('satisficer');expect(v.prompt).not.toContain('satisficer');expect(v.options[v.answer]).toContain('status quo');expect(v.analyses[3]).not.toContain('actively use');
 });
 it('secret回指仅来自当前幸福探寻，不靠学费或录取故事',()=>{
  const v=q('qe-c02-0097');expect(v.answer).toBe(3);expect(v.evidence[0].quote).toContain('key to happiness');expect(v.options.join(' ')).not.toMatch(/UVA|tuition|university/);
 });
 it('尼采赞同是作者设想，原文与引文出处不被改写',()=>{
  const v=q('q-c02-081');expect(v.passage).toContain('would have approved');expect(v.translation).toContain('想来会赞同');expect(q('qe-c02-0102').translation).toBe(v.translation);expect(q('qe-c02-0102').analyses.join(' ')).not.toMatch(/第一章|后面诗歌|前面另一小说/);
 });
});
