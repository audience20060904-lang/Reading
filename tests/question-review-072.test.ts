import {readFileSync} from 'node:fs';
import {describe,it,expect} from 'vitest';
const read=(p:string)=>JSON.parse(readFileSync(p,'utf8'));
const all=read('src/data/question-revision-catalog.json').questions;
const q=(id:string)=>all.find((v:any)=>v.id===id);
const originals=read('source/question-revisions/review-072-baseline.json').questions;
const b=(id:string)=>originals.find((v:any)=>v.id===id);
describe('第七十二批：条件、类比本体及调查方向',()=>{
 it('医疗顾问只是条件例子，原引用身份不变',()=>{
  const v=q('q-c08-041'),old=b(v.id);expect(v.evidence[0].quote).toContain('If you are a healthcare consultant');expect(v.evidence[0].quote).toContain('might need to ignore');
  expect(v.evidence[0].quote).toContain(old.evidence[0].quote);expect(v.evidence[0].sentenceIds).toEqual(old.evidence[0].sentenceIds);expect(v.evidence[0].sources).toEqual(old.evidence[0].sources);
 });
 it('Louvre比喻含完整标记与兴趣收窄本体',()=>{
  const v=q('q-c08-042'),old=b(v.id),book=read('public/data/book.json');
  expect(v.evidence[0].quote).toContain('It’s like going to the Louvre');expect(v.evidence[0].quote).toContain(old.evidence[0].quote);
  expect(v.evidence[0].sentenceIds).toEqual(old.evidence[0].sentenceIds);expect(v.evidence[0].sources).toEqual(old.evidence[0].sources);
  const s=book.sentences.find((v2:any)=>v2.id===v.sentenceIds[0]);expect(v.evidence.at(-1)).toEqual({quote:s.text,sentenceIds:[s.id],sources:s.sources});expect(s.text).toContain('uninterested in other areas of life');
  expect(v.vocabulary[0].context).toContain('不表示此前必然无法预见');
 });
 it('调查支持较少时间压力，旧引用身份及部分解释保持',()=>{
  const v=q('q-c08-044'),old=b(v.id);
  for(let i=0;i<old.evidence.length;i++){
   expect(v.evidence[i].quote).toContain(old.evidence[i].quote);expect(v.evidence[i].sentenceIds).toEqual(old.evidence[i].sentenceIds);expect(v.evidence[i].sources).toEqual(old.evidence[i].sources);
  }
  expect(v.evidence[0].quote).toContain('Ashley Whillans');expect(v.evidence[0].quote).toContain('4,469 respondents');
  expect(v.evidence[1].quote).toContain('in part');expect(v.evidence.at(-1).quote).toContain('less stressed about time');
  expect(v.options[v.answer]).toContain('linked with');
 });
 it('much better程度和檐槽义保留，24题范围不冒称全库完成',()=>{
  for(const id of ['q-c08-043','qe-c08-0063','qe-c08-0064','qe-c08-0065']){
   expect(q(id).translation).toContain('屋檐排水槽');expect(q(id).translation).toContain('好得多');expect(q(id).translation).not.toContain('通常');
  }
  expect(q('q-c08-043').analyses[3]).not.toContain('网站');expect(q('qe-c08-0069').analyses[1]).not.toContain('随访');
  const r=read('source/question-revisions/review-072-report.json');expect(r.manual.questionCount).toBe(24);expect(r.manual.sourceCandidatesReviewed).toBe(25);
  expect(r.manual.revisedQuestionCount).toBe(12);expect(r.manual.questionReviews.filter((v:any)=>v.decision==='retained')).toHaveLength(12);
  expect(r.manual.pdfPagesForQuestionEvidence).toEqual([85,86]);expect(r.manual.additionalParagraphContextPages).toEqual([84]);expect(r.remainingQuestionReviews).toBe(1327);expect(r.fullQuestionBankHumanReview).toBe(false);
 });
});
