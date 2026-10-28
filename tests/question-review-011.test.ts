import {readFileSync} from 'node:fs';
import {describe,it,expect} from 'vitest';
const read=(p:string)=>JSON.parse(readFileSync(p,'utf8'));
const catalog=read('src/data/question-revision-catalog.json');
const q=(id:string)=>catalog.questions.find((v:any)=>v.id===id);
describe('末批语义校对的范围和数值',()=>{
 it('两种交通购买的金额和期限准确配对',()=>{
  const travel=q('q-c14-026');expect(travel.options[travel.answer]).toBe('Flights from Tokyo to LA for about $700 and a thirty-day Greyhound pass for about $250.');
  expect(Math.max(...travel.options.map((v:string)=>v.length))-Math.min(...travel.options.map((v:string)=>v.length))).toBeLessThan(12);
 });
 it('榜单玩心不变成疗效排名，均值问题不变个体排序',()=>{
  const list=q('q-c14-049');expect(list.options[list.answer]).toBe('To end the book in a playful way.');expect(list.analyses[3]).toContain('alternative summary');
  const jobs=q('q-c14-010');expect(jobs.options[jobs.answer]).toContain('above the average');expect(jobs.analyses[3]).toContain('非同一职业');
 });
 it('已结束清单的每项都有可追溯审阅，不能推断全库人工审校',()=>{
  const audit=read('source/semantic-evidence/audit.json');expect(audit.pending).toBe(0);expect(audit.records.filter((r:any)=>r.status==='pending-semantic-review')).toHaveLength(0);expect(audit.reviewed).toBe(audit.records.length);
  for(const r of audit.records){expect(r.review).toBeTruthy();if(r.reviewRecord){const report=read(r.reviewRecord);expect(report.manual.sourceCandidateIdsReviewed).toContain(r.sentenceId);expect(report.fullQuestionBankHumanReview).toBe(false);}}
 });
});
