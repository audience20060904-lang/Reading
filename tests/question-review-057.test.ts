import {readFileSync} from 'node:fs';
import {describe,it,expect} from 'vitest';
const read=(p:string)=>JSON.parse(readFileSync(p,'utf8'));
const revised=read('src/data/question-revision-catalog.json').questions;
const q=(id:string)=>revised.find((v:any)=>v.id===id);
describe('第五十七批：说话人归属、数量范围及非决定性',()=>{
 it('仅有He的片段可独立解题，无需先知道Huckabee姓名',()=>{
  for(const id of ['q-c06-078','qe-c06-0129','qe-c06-0130','qe-c06-0131','q-c06-079','qe-c06-0132']){const v=q(id);expect(v.passage).not.toContain('Huckabee');expect(v.prompt).not.toContain('Huckabee');expect(v.promptZh).not.toContain('Huckabee');expect(v.options.join(' ')).not.toContain('Huckabee');expect(v.optionsZh.join(' ')).not.toContain('Huckabee');}
  expect(q('qe-c06-0130').options[0]).toContain('conditional analogy');expect(q('qe-c06-0131').options[1]).toContain('quoted speaker');
 });
 it('重量单位与颗数区分，移除候选分句实现说明',()=>{
  const v=q('qe-c06-0129');expect(v.answer).toBe(2);expect(v.analyses[2]).toContain('5 lb. bag of peanuts');expect(v.analyses[0]).toContain('about 10');expect(v.analyses.join('')).not.toContain('候选');expect(v.vocabulary[0].context).not.toContain('句界');
 });
 it('四份共享译文与选项保留small minority及could，不当群体实测',()=>{
  for(const id of ['q-c06-083','qe-c06-0137','qe-c06-0138','qe-c06-0139']){expect(q(id).translation).toBe(q('q-c06-083').translation);expect(q(id).translation).toContain('一小部分人可能');expect(q(id).translation).toContain('保持开放是困难的');expect(q(id).translation).toContain('人物信念归属');}
  expect(q('qe-c06-0138').optionsZh[2]).toContain('一小部分人可能');expect(q('qe-c06-0134').analyses[3]).not.toContain('后文');expect(q('qe-c06-0140').options[3]).not.toContain('chapter');
 });
 it('本批19题22来源候选，7题保留且审阅范围不夸大',()=>{
  const r=read('source/question-revisions/review-057-report.json');expect(r.manual.questionCount).toBe(19);expect(r.manual.sourceCandidatesReviewed).toBe(22);expect(r.manual.revisedQuestionCount).toBe(12);expect(r.manual.questionReviews.filter((v:any)=>v.decision==='retained')).toHaveLength(7);expect(r.manual.pdfPagesForQuestionEvidence).toEqual([64,65]);expect(r.manual.additionalParagraphContextPages).toEqual([66]);expect(r.remainingQuestionReviews).toBe(1644);expect(r.fullQuestionBankHumanReview).toBe(false);
 });
});
