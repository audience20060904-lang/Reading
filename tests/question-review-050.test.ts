import {readFileSync} from 'node:fs';
import {describe,it,expect} from 'vitest';
const read=(p:string)=>JSON.parse(readFileSync(p,'utf8'));
const revisions=read('src/data/question-revision-catalog.json').questions;
const q=(id:string)=>revisions.find((v:any)=>v.id===id);
describe('第五十批：人物角色、限定语气与完整译文',()=>{
 it('不将Goldmund例证误称研究评分者，中文保留without high限定',()=>{
  const v=q('q-c06-017');expect(v.analyses[1]).toContain('没有说他是评分者');expect(v.optionsZh[v.answer]).toContain('不高');expect(q('qe-c06-0027').analyses.join(' ')).not.toContain('作品人物');expect(q('qe-c06-0027').analyses[3]).toContain('没有提供');
 });
 it('Jobs补充题区分于主问题用途，考查might not和but且不变原答案位置',()=>{
  const v=q('qe-c06-0029'),b=read('source/question-revisions/review-050-baseline.json').questions.find((v:any)=>v.id==='qe-c06-0029');expect(v.prompt).toContain('might not ... but');expect(v.prompt).not.toBe(q('q-c06-019').prompt);expect(v.answer).toBe(b.answer);expect(v.version).toBe(b.version+1);expect(v.options[v.answer]).toContain('possible unhappiness');expect(v.analyses[v.answer]).toContain('并存');
 });
 it('段落译文补出暂时状态和评价词的意思，不把解释尾注当原文翻译',()=>{
  for(const id of ['q-c06-024','qe-c06-0034','qe-c06-0035','qe-c06-0036']){expect(q(id).translation).toContain('frantic（慌乱的）');expect(q(id).translation).toContain('rejoicing（欢欣的）');}
  for(const id of ['q-c06-025','qe-c06-0037','qe-c06-0038','qe-c06-0039']){expect(q(id).translation).toContain('不带褒贬判断');expect(q(id).translation).toContain('insignificant（无足轻重的）');}
  for(const id of ['q-c06-019','qe-c06-0028','qe-c06-0029','qe-c06-0030'])expect(q(id).translation).not.toContain('这里的人物例证');
 });
 it('恢复冻结批次保持真实审阅范围，六题直接保留',()=>{
  const r=read('source/question-revisions/review-050-report.json');expect(r.manual.questionCount).toBe(20);expect(r.manual.sourceCandidatesReviewed).toBe(22);expect(r.manual.revisedQuestionCount).toBe(14);expect(r.manual.questionReviews.filter((v:any)=>v.decision==='retained')).toHaveLength(6);expect(r.frozenCheckpoint).toContain('050-checkpoint');expect(r.fullQuestionBankHumanReview).toBe(false);
 });
});
