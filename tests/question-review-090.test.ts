import {readFileSync} from 'node:fs';
import {describe,it,expect} from 'vitest';
const read=(p:string)=>JSON.parse(readFileSync(p,'utf8'));
const all=read('src/data/question-revision-catalog.json').questions;
const frozen=read('source/question-revisions/review-090-current-questions.json').questions;
const q=(id:string)=>all.find((v:any)=>v.id===id)??frozen.find((v:any)=>v.id===id);
const old=read('source/question-revisions/review-090-baseline.json').questions;
describe('第九十批：统计单位、时点和片段范围',()=>{
 it('只修解析，正确题的选项、译文、引文和答案不改',()=>{
  const author=read('source/question-revisions/review-090.json');expect(author.questions).toHaveLength(7);
  for(const entry of author.questions)expect(Object.keys(entry.updates)).toEqual(['analyses']);
  for(const before of old){for(const key of ['prompt','promptZh','options','optionsZh','evidence','translation','vocabulary','answer','passage'])expect(q(before.id)[key]).toEqual(before[key]);}
 });
 it('众数题只据当前一公里，出生地中位数题只据当前22.9',()=>{
  expect(q('qe-c10-0072').analyses[0]).toContain('最常见的是一公里');expect(q('qe-c10-0072').analyses[0]).not.toContain('后段');
  expect(q('qe-c10-0072').analyses[1]).toContain('选项所称');expect(q('q-c10-040').analyses[0]).not.toContain('前文');expect(q('q-c10-040').analyses[0]).toContain('22.9公里');
  const p=q('q-c10-040').passage;for(const term of ['6.2 kilometers','7.8 kilometers','22.9 kilometers','13 percent','10.5 percent'])expect(p).toContain(term);
 });
 it('个人与提名单位保留，解析不前借后段比例方法或功能距离',()=>{
  expect(q('q-c10-038').options[q('q-c10-038').answer]).toContain('289,248 individuals');
  expect(q('qe-c10-0070').analyses[2]).not.toContain('13%');expect(q('q-c10-042').analyses[1]).not.toContain('提问');
  expect(q('qe-c10-0080').analyses[3]).not.toContain('功能');expect(q('qe-c10-0080').analyses[3]).toContain('不计楼梯数');
  expect(q('q-c10-043').options[q('q-c10-043').answer]).toContain('Friendship nominations');
 });
 it('23题23候选有16题保留，跨页上下文与审阅界限真实记录',()=>{
  const r=read('source/question-revisions/review-090-report.json');
  expect(r.manual.questionCount).toBe(23);expect(r.manual.sourceCandidatesReviewed).toBe(23);expect(r.manual.revisedQuestionCount).toBe(7);
  expect(r.manual.questionReviews.filter((v:any)=>v.decision==='retained')).toHaveLength(16);
  expect(r.manual.pdfPagesVisuallyReviewed).toEqual([109,110,111]);expect(r.manual.additionalParagraphContextPages).toEqual([111]);expect(r.manual.pdfSourceBlocksTextMatched).toBe(7);
  expect(r.remainingQuestionReviews).toBe(938);expect(r.fullQuestionBankHumanReview).toBe(false);
 });
});
