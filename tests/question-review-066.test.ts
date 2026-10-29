import {readFileSync} from 'node:fs';
import {describe,it,expect} from 'vitest';
const read=(p:string)=>JSON.parse(readFileSync(p,'utf8'));
const all=read('src/data/question-revision-catalog.json').questions;
const q=(id:string)=>all.find((v:any)=>v.id===id);
const baseline=read('source/question-revisions/review-066-baseline.json').questions;
const b=(id:string)=>baseline.find((v:any)=>v.id===id);
const book=read('public/data/book.json');

describe('第六十六批：限定词、人物对应与完整论据',()=>{
 it('可能原因和玩心助益的证据保留条件、对象及旧来源身份',()=>{
  const cause=q('q-c07-061'),old=b(cause.id);
  expect(cause.evidence[0].quote).toContain('might be one of the reasons');
  expect(cause.evidence[0].quote).toContain('suffered from burnout');
  expect(cause.evidence[0].sentenceIds).toEqual(old.evidence[0].sentenceIds);
  expect(cause.evidence[0].sources).toEqual(old.evidence[0].sources);
  expect(cause.evidence[1]).toEqual(old.evidence[1]);
  const focus=book.sentences.find((s:any)=>s.id===cause.sentenceIds[0]);
  expect(cause.evidence.at(-1)).toEqual({quote:focus.text,sentenceIds:[focus.id],sources:focus.sources});
  const play=q('q-c07-064'),previous=b(play.id);
  expect(play.evidence[1].quote).toContain('A playful mindset can help');
  expect(play.evidence[1].quote).toContain('psychologically stuck');
  expect(play.evidence[1].sentenceIds).toEqual(previous.evidence[1].sentenceIds);
  expect(play.evidence[1].sources).toEqual(previous.evidence[1].sources);
 });
 it('补充题改核对人物对应，区别主问题的非唯一解释',()=>{
  const extra=q('qe-c07-0106'),main=read('public/data/questions.json').find((v:any)=>v.id==='q-c07-062');
  expect(main.prompt).toContain('Why');expect(extra.prompt).toContain('matched');
  expect(extra.options[extra.answer]).toContain('Parental divorce is mentioned in Phelps’s case');
  expect(extra.options[extra.answer]).toContain('sexual abuse in Biles’s case');
  expect(extra.answer).toBe(b(extra.id).answer);
  expect(extra.evidence).toEqual(b(extra.id).evidence);
 });
 it('without和often不被弱化或省略，专攻与专业精神中文分开',()=>{
  const cost=q('qe-c07-0104');expect(cost.options[cost.answer]).toContain('without fun or laughter');
  expect(cost.optionsZh[cost.answer]).toContain('没有趣味或笑声');
  const often=q('qe-c07-0114');expect(often.options[often.answer]).toContain('often');
  expect(often.optionsZh[often.answer]).toContain('往往');
  for(const id of ['q-c07-064','qe-c07-0111','qe-c07-0112'])expect(q(id).translation).toContain('专攻与专业精神');
  for(const id of ['q-c07-061','qe-c07-0104','qe-c07-0105'])expect(q(id).translation).toContain('很强的坚毅');
 });
 it('回应及顺序只据当前，完整回应入证且19题范围不夸大',()=>{
  const sequence=q('q-c07-066'),old=b(sequence.id);
  expect(sequence.prompt).not.toContain('family');expect(q('qe-c07-0116').prompt).not.toContain('family');
  expect(sequence.evidence[0]).toEqual(old.evidence[0]);
  const response=book.sentences.find((s:any)=>s.id===sequence.sentenceIds[0]);
  expect(sequence.evidence.at(-1)).toEqual({quote:response.text,sentenceIds:[response.id],sources:response.sources});
  expect(q('qe-c07-0115').analyses[0]).not.toContain('后面');
  const r=read('source/question-revisions/review-066-report.json');
  expect(r.manual.questionCount).toBe(19);expect(r.manual.sourceCandidatesReviewed).toBe(22);
  expect(r.manual.revisedQuestionCount).toBe(11);
  expect(r.manual.questionReviews.filter((v:any)=>v.decision==='retained')).toHaveLength(8);
  expect(r.manual.pdfPagesVisuallyReviewed).toEqual([76,77]);
  expect(r.remainingQuestionReviews).toBe(1455);expect(r.fullQuestionBankHumanReview).toBe(false);
 });
});
