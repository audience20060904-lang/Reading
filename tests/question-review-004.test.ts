import {describe,it,expect} from 'vitest';
import {readFileSync} from 'node:fs';
import {validateRevisionEvidence} from '../scripts/validate-revision-evidence.mjs';
const read=(p:string)=>JSON.parse(readFileSync(p,'utf8'));
const book=read('public/data/book.json'),catalog=read('src/data/question-revision-catalog.json'),baseline=read('source/question-revisions/review-004-baseline.json');
const current=(id:string)=>catalog.questions.find((q:any)=>q.id===id);

describe('第四批来源证据与人物叙述校对',()=>{
 it('概括中的丧亲有独立、完整且可定位的证据；旧引文完整保留',()=>{
  const before=baseline.questions.find((q:any)=>q.id==='q-c04-038'),q=current(before.id);
  expect(q.evidence.slice(0,before.evidence.length)).toEqual(before.evidence);
  const added=q.evidence.at(-1);expect(added.quote).toContain('her husband died of cancer in 1994');
  expect(added.quote).toContain('she lost two of her adult children');
  expect(()=>validateRevisionEvidence(before,q,book)).not.toThrow();
  for(const change of [
   {quote:'A made-up bereavement.'},
   {sentenceIds:['c04-s05-p040-04575-s005']},
   {sources:[{...added.sources[0],pdfPage:41}]}
  ])expect(()=>validateRevisionEvidence(before,{...q,evidence:[...before.evidence,{...added,...change}]},book)).toThrow();
  expect(()=>validateRevisionEvidence(before,{...q,evidence:[q.evidence[1]]},book)).toThrow();
  expect(()=>validateRevisionEvidence(before,{...q,evidence:[{...before.evidence[0],sentenceIds:added.sentenceIds},...q.evidence.slice(1)]},book)).toThrow();
 });
 it('退休和和解的完整引文保留条件与过程；亲属译文不再含混',()=>{
  const retirement=current('q-c04-052');expect(retirement.evidence[1].quote).toContain('Once she had enough');expect(retirement.evidence[1].quote).toContain('work here and there');
  const trip=current('q-c04-041');expect(trip.evidence[0].quote).toContain('twenty-eight days');expect(trip.evidence[0].quote).toContain('became a journey of reconciliation');
  const family=current('q-c04-047');expect(family.translation).toContain('这七个孙辈中，有两个');expect(family.options[family.answer]).toContain('four children and seven grandchildren');
  const assessment=current('q-c04-054');expect(assessment.options[assessment.answer]).toContain('The author sees');expect(assessment.analyses[assessment.answer]).toContain('seems');
 });
});
