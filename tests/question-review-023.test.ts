import {readFileSync} from 'node:fs';
import {describe,it,expect} from 'vitest';
const read=(p:string)=>JSON.parse(readFileSync(p,'utf8')),catalog=read('src/data/question-revision-catalog.json');
const q=(id:string)=>catalog.questions.find((v:any)=>v.id===id);
describe('第二十三批：轶事当前证据与时间顺序',()=>{
 it('困惑的解释依回应及误认，不靠前后片段的开门或受辱',()=>{
  const v=q('q-c02-016');expect(v.options[v.answer]).toBe('confused by an unexpected response.');expect(v.analyses[0]).not.toContain('给作者开了门');expect(v.analyses[2]).not.toContain('后来感到受辱');expect(v.analyses[2]).toContain('身份被误认');
 });
 it('导师词汇不凭空添加转述后才通话的时间顺序',()=>{
  const v=q('qe-c02-0050');expect(v.vocabulary[0].context).toContain('转述的故事');expect(v.vocabulary[0].context).not.toContain('后来在电话中');expect(v.options[v.answer]).toBe('When he was a fifth-year PhD student.');
 });
 it('面试结果不扩成录用或撤回申请，词汇限于当前带引号描述',()=>{
  const v=q('q-c02-017');expect(v.analyses[3]).toContain('没有导师撤回申请的信息');expect(v.vocabulary.find((w:any)=>w.word==='cocky').context).toContain('不等于已获聘');expect(v.evidence[0].quote).toContain('did not get the job interview');
 });
});
