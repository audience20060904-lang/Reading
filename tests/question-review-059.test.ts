import {readFileSync} from 'node:fs';
import {describe,it,expect} from 'vitest';
const read=(p:string)=>JSON.parse(readFileSync(p,'utf8'));
const catalog=read('src/data/question-revision-catalog.json').questions;
const q=(id:string)=>catalog.find((v:any)=>v.id===id);
describe('第五十九批：个例证据及当前片段自足',()=>{
 it('保留旧引文映射，追加完整俏皮回应句支持比较',()=>{
  const v=q('q-c07-002'),b=read('source/question-revisions/review-059-baseline.json').questions.find((r:any)=>r.id===v.id),s=read('public/data/book.json').sentences.find((r:any)=>r.id===v.sentenceIds[0]);expect(v.evidence.slice(0,b.evidence.length)).toEqual(b.evidence);expect(v.evidence.at(-1)).toEqual({quote:s.text,sentenceIds:[s.id],sources:s.sources});expect(s.text).toContain('invented an urgent excuse');expect(v.passage).toBe(b.passage);expect(v.answer).toBe(b.answer);
 });
 it('共享急事借口译文保留条件回应和研究者观察',()=>{
  for(const id of ['q-c07-002','qe-c07-0004','qe-c07-0005']){expect(q(id).translation).toBe(q('q-c07-002').translation);expect(q(id).translation).toContain('有急事的借口');expect(q(id).translation).toContain('条件语气');expect(q(id).translation).toContain('McCrae 与 Costa');}
 });
 it('排除分析不依赖后段奥运训练量或前章幸福组合',()=>{
  expect(q('qe-c07-0001').analyses[0]).not.toContain('前面');expect(q('qe-c07-0001').analyses[3]).not.toContain('幸福部分');expect(q('qe-c07-0009').analyses[1]).not.toContain('后续');expect(q('qe-c07-0012').analyses[1]).toContain('八岁');expect(q('qe-c07-0014').analyses[0]).not.toContain('下一');expect(q('q-c07-005').analyses[3]).not.toContain('网站');expect(q('q-c07-006').vocabulary[0].context).not.toContain('网站');
 });
 it('冻结20题22来源实际审阅，8题保留且未称全库完成',()=>{
  const r=read('source/question-revisions/review-059-report.json');expect(r.manual.questionCount).toBe(20);expect(r.manual.sourceCandidatesReviewed).toBe(22);expect(r.manual.revisedQuestionCount).toBe(12);expect(r.manual.questionReviews.filter((v:any)=>v.decision==='retained')).toHaveLength(8);expect(r.manual.pdfPagesVisuallyReviewed).toEqual([68,69]);expect(r.frozenCheckpoint).toContain('059-checkpoint');expect(r.remainingQuestionReviews).toBe(1605);expect(r.fullQuestionBankHumanReview).toBe(false);
 });
});
