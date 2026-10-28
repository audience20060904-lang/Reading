import {readFileSync} from 'node:fs';
import {describe,it,expect} from 'vitest';
const read=(p:string)=>JSON.parse(readFileSync(p,'utf8')),catalog=read('src/data/question-revision-catalog.json');
const q=(id:string)=>catalog.questions.find((v:any)=>v.id===id);
describe('第三十九批：叙述位置与片段自足',()=>{
 it('匿名第一人称引语不要求前段性别和姓名',()=>{
  for(const id of ['qe-c04-0068','qe-c04-0069']){const v=q(id);expect(v.options[v.answer]).toContain("speaker's");expect(v.passage).not.toContain('Joy');}for(const id of ['q-c04-048','qe-c04-0076']){const v=q(id);expect(v.prompt).not.toContain('Linda');expect(v.passage).not.toContain('Linda');}
 });
 it('年龄、访谈和出租车分析以当前明示信息为据',()=>{
  expect(q('qe-c04-0062').analyses[0]).not.toContain('后面旅行');expect(q('qe-c04-0066').analyses[0]).toContain('首句访谈');expect(q('q-c04-046').analyses[1]).not.toContain('乘客的身份');expect(q('qe-c04-0070').analyses[3]).not.toContain('访问背景');expect(q('qe-c04-0072').analyses[3]).not.toContain('另一个人物');
 });
 it('妊娠原因与配子来源分开，不把未显示的家庭数量写作排除事实',()=>{
  const v=q('q-c04-048');expect(v.answer).toBe(0);expect(v.evidence[0].quote).toContain('because her daughter had medical conditions');expect(v.analyses[3]).toContain('because');expect(v.analyses[3]).not.toContain('孙辈总数');expect(q('qe-c04-0076').analyses[3]).toContain('不是特定年龄');expect(q('qe-c04-0065').translation).not.toContain('叙述保留');
 });
});
