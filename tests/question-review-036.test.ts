import {readFileSync} from 'node:fs';
import {describe,it,expect} from 'vitest';
const read=(p:string)=>JSON.parse(readFileSync(p,'utf8')),catalog=read('src/data/question-revision-catalog.json');
const q=(id:string)=>catalog.questions.find((v:any)=>v.id===id);
describe('第三十六批：叙述时点与坚持词义',()=>{
 it('after排除依据是缺少任职与先后证据，非只否定因果',()=>{
  const v=q('q-c04-015');expect(v.options[1]).toContain('after');expect(v.analyses[1]).toContain('没有说她接受新职位');expect(v.analyses[1]).toContain('先后关系');expect(q('qe-c04-0027').analyses[1]).toContain('2015');expect(q('qe-c04-0027').analyses[1]).not.toContain('后面');
 });
 it('当前she无需未显示姓名，stuck仅指做法持续而非疗效证据',()=>{
  const v=q('q-c04-016');expect(v.prompt).toBe('Which of the three prescribed approaches did she continue with?');expect(v.passage).not.toContain('Gopnik');expect(v.vocabulary[0].meaning).toBe('坚持下来；持续存在');expect(v.vocabulary[0].context).toContain('未单独证明治疗效果');expect(q('qe-c04-0030').analyses[1]).not.toContain('前段');
 });
 it('学术休假地点干扰只用当前地点和角色错配，不借外段年份',()=>{
  const v=q('qe-c04-0037');expect(v.options.join(' ')).not.toMatch(/1723|2015/);expect(v.options[v.answer]).toContain('At Caltech');expect(v.analyses[3]).toContain('会面地点');expect(v.analyses[2]).toContain('没有任命');expect(q('qe-c04-0032').analyses[1]).not.toContain('之后资料');
 });
});
