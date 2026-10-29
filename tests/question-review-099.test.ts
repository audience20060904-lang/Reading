import {readFileSync} from 'node:fs';
import {describe,it,expect} from 'vitest';
const read=(p:string)=>JSON.parse(readFileSync(p,'utf8'));
const all=read('src/data/question-revision-catalog.json').questions;
const q=(id:string)=>all.find((v:any)=>v.id===id);
const old=read('source/question-revisions/review-099-baseline.json').questions;
const b=(id:string)=>old.find((v:any)=>v.id===id);
describe('第九十九批：个人期待、研究归属和综述范围',()=>{
 it('研究者argue与两项综述完整主语入证，旧引用身份保持',()=>{
  expect(q('q-c10-114').evidence[0].quote).toContain('Leung and colleagues argue');expect(q('q-c10-115').evidence[0].quote).toContain('time spent living abroad');expect(q('q-c10-115').evidence[1].quote).toContain('Individuals who have more foreign experiences');
  for(const id of ['q-c10-114','q-c10-115']){const now=q(id),before=b(id);for(let i=0;i<before.evidence.length;i++){expect(now.evidence[i].quote).toContain(before.evidence[i].quote);expect(now.evidence[i].sources).toEqual(before.evidence[i].sources);expect(now.evidence[i].sentenceIds).toEqual(before.evidence[i].sentenceIds);}}
 });
 it('规范不被当全员实际一致，解析不借前后故事',()=>{
  expect(q('qe-c10-0207').options[1]).toContain('everyone in Japan behaves identically');expect(q('qe-c10-0207').analyses[1]).toContain('并不保证');expect(q('qe-c10-0203').analyses[3]).not.toContain('前文');expect(q('qe-c10-0204').analyses[1]).not.toContain('后面');expect(q('qe-c10-0209').analyses[3]).not.toContain('保留的原文片段');expect(q('qe-c10-0215').analyses[2]).not.toContain('后面');
 });
 it('人物对照两例可定位，原有道德与创意并置引文不动',()=>{
  const now=q('q-c10-117');expect(now.evidence[0]).toEqual(b(now.id).evidence[0]);expect(now.evidence[1].quote).toContain('particular device functions');expect(now.evidence[2].quote).toContain('Whole Foods');expect(now.evidence[1].quote).toContain('several product launches');
 });
 it('21题23候选保留10题，相关不当因果且原文答案保持',()=>{
  const r=read('source/question-revisions/review-099-report.json');expect(r.manual.questionCount).toBe(21);expect(r.manual.sourceCandidatesReviewed).toBe(23);expect(r.manual.revisedQuestionCount).toBe(11);expect(r.manual.questionReviews.filter((v:any)=>v.decision==='retained')).toHaveLength(10);expect(r.manual.pdfPagesVisuallyReviewed).toEqual([120,121]);expect(r.manual.pdfSourceBlocksTextMatched).toBe(4);expect(r.remainingQuestionReviews).toBe(744);expect(r.fullQuestionBankHumanReview).toBe(false);
  for(const before of old){expect(q(before.id).answer).toBe(before.answer);expect(q(before.id).passage).toBe(before.passage);}
 });
});
