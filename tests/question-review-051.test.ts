import {readFileSync} from 'node:fs';
import {describe,it,expect} from 'vitest';
const read=(p:string)=>JSON.parse(readFileSync(p,'utf8'));
const revised=read('src/data/question-revision-catalog.json').questions;
const q=(id:string)=>revised.find((v:any)=>v.id===id);
describe('第五十一批：论证结果、括号回应与特质词义',()=>{
 it('补充题考反事实条件的结果，保留引文归属与原答案D',()=>{
  const v=q('qe-c06-0041');expect(v.prompt).toContain('what would not have happened');expect(v.answer).toBe(3);expect(v.options[v.answer]).toContain('permanent place in language');expect(v.analyses[v.answer]).toContain('两位研究者所述论证');expect(v.analyses.join(' ')).not.toContain('后文还批评');
 });
 it('Not really单独考回应功能，不重复主问题对同义词的询问',()=>{
  const v=q('qe-c06-0042');expect(v.prompt).toContain('Not really');expect(v.promptZh).toContain('回应');expect(v.answer).toBe(0);expect(v.options[0]).toContain('rejects');expect(q('q-c06-028').translation).toContain('两个词都有“爱冒险的”意思');expect(v.analyses.join(' ')).not.toContain('后续另一批评');
 });
 it('Big Five四题共享译文保留touchy敏感性、fearful害怕及persistent坚持',()=>{
  const ids=['q-c06-033','qe-c06-0048','qe-c06-0049','qe-c06-0050'];for(const id of ids){expect(q(id).translation).toBe(q(ids[0]).translation);expect(q(id).translation).toContain('敏感易恼、容易害怕');expect(q(id).translation).toContain('坚持不懈');}expect(q('qe-c06-0048').optionsZh[1]).toContain('容易害怕');
 });
 it('完整审阅与有限推断保留范围，不将队列归零或声称全库已审',()=>{
  const r=read('source/question-revisions/review-051-report.json');expect(r.manual.questionCount).toBe(20);expect(r.manual.sourceCandidatesReviewed).toBe(24);expect(r.manual.revisedQuestionCount).toBe(9);expect(r.manual.questionReviews.filter((v:any)=>v.decision==='retained')).toHaveLength(11);expect(r.remainingQuestionReviews).toBe(1771);expect(r.fullQuestionBankHumanReview).toBe(false);const v=read('public/data/evidence-questions.json').find((v:any)=>v.id==='qe-c06-0052');expect(v.support).toBe('limited-inference');
 });
});
