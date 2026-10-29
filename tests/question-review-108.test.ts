import {readFileSync} from 'node:fs';
import {describe,it,expect} from 'vitest';
const read=(p:string)=>JSON.parse(readFileSync(p,'utf8'));
const q=(id:string)=>read('src/data/question-revision-catalog.json').questions.find((v:any)=>v.id===id);
describe('第一百零八批：故事框架、当前身份与作者示范',()=>{
 it('人物变化题不依赖未显示的儿子姓名，叛逆起点与could可定位',()=>{
  const a=q('q-c12-004'),b=read('source/question-revisions/review-108-baseline.json').questions.find((v:any)=>v.id===a.id);
  expect(a.prompt).toBe('What change does the suggested narrative emphasize?');expect(a.evidence[0].quote).toContain('You could add his rebellious years');expect(a.evidence[0].quote).toContain(b.evidence[0].quote);expect(a.evidence[0].sentenceIds).toEqual(b.evidence[0].sentenceIds);expect(a.evidence[0].sources).toEqual(b.evidence[0].sources);
 });
 it('解析不借前后研究身份或原排版处理说明',()=>{
  expect(q('qe-c12-0001').analyses.join(' ')).not.toMatch(/上一章还|前章限定/);expect(q('qe-c12-0003').analyses[3]).not.toContain('quality');expect(q('q-c12-005').analyses[3]).not.toContain('Anne');
  expect(q('qe-c12-0010').analyses.slice(0,3).join(' ')).not.toMatch(/前面|后面/);expect(q('q-c12-006').analyses[3]).not.toMatch(/排版|空格/);expect(q('q-c12-006').analyses[3]).toContain('作者提出的叙述示范');
 });
 it('15道正确题保留实际冻结版本和指纹',()=>{
  const report=read('source/question-revisions/review-108-report.json'),frozen=read('source/question-revisions/review-108-current-questions.json').questions,audit=read('source/question-semantic-audit.json');
  const retained=report.manual.questionReviews.filter((v:any)=>v.decision==='retained');expect(retained).toHaveLength(15);
  for(const r of retained){const before=frozen.find((v:any)=>v.id===r.questionId),after=audit.records.find((v:any)=>v.id===r.questionId);expect(after.reviewedFingerprint).toBe(before.fingerprint);expect(after.reviewedVersion).toBe(before.version);}
 });
 it('22题23候选，补读135页并保留原答案与片段',()=>{
  const r=read('source/question-revisions/review-108-report.json');expect(r.manual.questionCount).toBe(22);expect(r.manual.sourceCandidatesReviewed).toBe(23);expect(r.manual.revisedQuestionCount).toBe(7);expect(r.manual.pdfPagesForQuestionEvidence).toEqual([133,134]);expect(r.manual.additionalParagraphContextPages).toEqual([135]);expect(r.manual.pdfPagesVisuallyReviewed).toEqual([133,134,135]);expect(r.manual.pdfSourceBlocksTextMatched).toBe(6);expect(r.remainingQuestionReviews).toBe(549);expect(r.fullQuestionBankHumanReview).toBe(false);
  for(const before of read('source/question-revisions/review-108-baseline.json').questions){expect(q(before.id).answer).toBe(before.answer);expect(q(before.id).passage).toBe(before.passage);}
 });
});
