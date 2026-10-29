import {readFileSync} from 'node:fs';
import {describe,it,expect} from 'vitest';
const read=(p:string)=>JSON.parse(readFileSync(p,'utf8'));
const catalog=read('src/data/question-revision-catalog.json').questions;
const q=(id:string)=>catalog.find((v:any)=>v.id===id);
describe('第六十一批：概率比较、身份和职业时长',()=>{
 it('两项相对概率及完整比较组保留在题目、译文与同句证据中',()=>{
  const v=q('q-c07-019'),b=read('source/question-revisions/review-061-baseline.json').questions.find((r:any)=>r.id===v.id),s=read('public/data/book.json').sentences.find((r:any)=>r.id===v.sentenceIds[0]);expect(v.options[3]).toContain('lower likelihood');expect(v.options[3]).toContain('greater likelihood');expect(v.evidence[0].quote).toBe(s.text);expect(v.evidence[0].quote).toContain('than elite athletes');expect(v.evidence[0].sentenceIds).toEqual(b.evidence[0].sentenceIds);expect(v.evidence[0].sources).toEqual(b.evidence[0].sources);
  for(const id of ['q-c07-019','qe-c07-0033','qe-c07-0034']){expect(q(id).translation).toContain('出现倦怠的可能性较低');expect(q(id).translation).toContain('取得成功的可能性较高');}
 });
 it('首句只有he的译文和暂离题不依赖未显示Jordan姓名',()=>{
  for(const id of ['q-c07-020','qe-c07-0035','qe-c07-0036']){expect(q(id).passage).not.toContain('Jordan');expect(q(id).translation).not.toContain('Jordan');expect(q(id).translation).toContain('他在巅峰期');}expect(q('qe-c07-0035').prompt).not.toContain('Jordan');expect(q('q-c07-020').vocabulary[0].context).not.toContain('Jordan');
 });
 it('晋升表达明确所花时长及比较组，哲学引文译被迫而非命定',()=>{
  for(const id of ['q-c07-026','qe-c07-0044','qe-c07-0045']){expect(q(id).translation).toContain('所花的时间');expect(q(id).translation).toContain('比 Leibniz 得主探索了更多样');expect(q(id).translation).toContain('未陷入倦怠');}
  for(const id of ['q-c07-027','qe-c07-0046']){expect(q(id).translation).toContain('被迫过早选择职业');expect(q(id).translation).not.toContain('注定');expect(q(id).translation).toContain('不是实验结果');}expect(q('qe-c07-0041').analyses[3]).not.toContain('后面');
 });
 it('24题25来源已审，11题保留且余1558题不称已知错误',()=>{
  const r=read('source/question-revisions/review-061-report.json');expect(r.manual.questionCount).toBe(24);expect(r.manual.sourceCandidatesReviewed).toBe(25);expect(r.manual.revisedQuestionCount).toBe(13);expect(r.manual.questionReviews.filter((v:any)=>v.decision==='retained')).toHaveLength(11);expect(r.manual.pdfPagesVisuallyReviewed).toEqual([69,70,71]);expect(r.remainingQuestionReviews).toBe(1558);expect(r.fullQuestionBankHumanReview).toBe(false);
 });
});
