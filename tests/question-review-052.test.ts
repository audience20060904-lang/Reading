import {readFileSync} from 'node:fs';
import {describe,it,expect} from 'vitest';
const read=(p:string)=>JSON.parse(readFileSync(p,'utf8'));
const revised=read('src/data/question-revision-catalog.json').questions;
const q=(id:string)=>revised.find((v:any)=>v.id===id);
describe('第五十二批：比较证据、指代与传记时序',()=>{
 it('比较题逐字证据包含than比较对象，来源ID不变且仍是当前原句',()=>{
  const v=q('q-c06-041'),b=read('source/question-revisions/review-052-baseline.json').questions.find((row:any)=>row.id==='q-c06-041');expect(v.evidence[0].quote).toContain('than those low in openness.');expect(v.passage).toContain(v.evidence[0].quote);expect(v.evidence[0].sentenceIds).toEqual(b.evidence[0].sentenceIds);expect(v.passage).toBe(b.passage);
 });
 it('She短段题干不依赖未显示Joy姓名，当前hooked分析不预告下一段',()=>{
  const v=q('qe-c06-0063');expect(v.passage).not.toContain('Joy');expect(v.prompt).toBe('What did she want to do thereafter?');expect(v.analyses[1]).not.toContain('前面的');expect(q('qe-c06-0062').analyses[2]).not.toContain('后面才');expect(q('qe-c06-0061').analyses[3]).not.toContain('父段');
 });
 it('Ramo四题共享译文保留职业范围与数字时序，正确项无需Caltech缩写知识',()=>{
  const ids=['q-c06-045','qe-c06-0064','qe-c06-0065','qe-c06-0066'];for(const id of ids){const v=q(id);expect(v.translation).toBe(q(ids[0]).translation);expect(v.translation).toContain('航空航天工程师');expect(v.translation).toContain('三十岁以前就有二十五项专利');expect(v.translation).toContain('一百岁时取得最后一项专利');}
  const v=q('qe-c06-0066');expect(v.options[v.answer]).toContain('California Institute of Technology');expect(v.analyses.join(' ')).not.toContain('制作细节');expect(q('qe-c06-0065').analyses.join(' ')).not.toMatch(/Louis Cha|Joy/);
 });
 it('本批20题22来源候选，保留11题且不宣称全库已审',()=>{
  const r=read('source/question-revisions/review-052-report.json');expect(r.manual.questionCount).toBe(20);expect(r.manual.sourceCandidatesReviewed).toBe(22);expect(r.manual.revisedQuestionCount).toBe(9);expect(r.manual.questionReviews.filter((v:any)=>v.decision==='retained')).toHaveLength(11);expect(r.remainingQuestionReviews).toBe(1751);expect(r.fullQuestionBankHumanReview).toBe(false);
 });
});
