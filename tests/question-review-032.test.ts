import {readFileSync} from 'node:fs';
import {describe,it,expect} from 'vitest';
const read=(p:string)=>JSON.parse(readFileSync(p,'utf8')),catalog=read('src/data/question-revision-catalog.json'),book=read('public/data/book.json');
const q=(id:string)=>catalog.questions.find((v:any)=>v.id===id);
describe('第三十二批：逻辑或、频率与直接反例',()=>{
 it('award-winning不凭空增加多次频率，三题同段译文一致',()=>{
  const v=q('q-c03-030');expect(v.translation).toContain('获过奖的科学家');expect(v.translation).not.toContain('屡获');for(const id of ['qe-c03-0037','qe-c03-0038'])expect(q(id).translation).toBe(v.translation);
 });
 it('non-neurotic括号保留or并与已有主问题译文一致',()=>{
  const primary=q('q-c03-032'),published=catalog.batches.find((b:any)=>b.id==='question-review-2026-10-28-002');expect(published.questionFingerprints[primary.id]).toBe('ce355b73c05364adfc7ebbb18f8619f95602c679920025c39268728f19f71f4b');expect(read('source/question-revisions/review-032.json').questions.some((v:any)=>v.id===primary.id)).toBe(false);for(const id of ['qe-c03-0040','qe-c03-0041']){expect(q(id).translation).toBe(primary.translation);expect(q(id).translation).toContain('或不那么容易受压力影响');}
 });
 it('科学家反例引用追加且原引用身份完整保留',()=>{
  const v=q('q-c03-030'),old=read('source/question-revisions/review-032-baseline.json').questions.find((v:any)=>v.id==='q-c03-030');expect(v.evidence.slice(0,old.evidence.length)).toEqual(old.evidence);const added=v.evidence.at(-1);expect(added.quote).toContain('Some well-respected, well-liked, award-winning scientists');expect(v.passage).toContain(added.quote);const s=book.sentences.find((s:any)=>s.id===added.sentenceIds[0]);expect(added.quote).toBe(s.text);expect(added.sources).toEqual(s.sources);
 });
 it('当前假设对象不换成狱内或私人名声，体验不借未来段作道德保证',()=>{
  const v=q('qe-c03-0046');expect(v.answer).toBe(3);expect(v.options[v.answer]).toBe('U.S. national security.');expect(v.analyses[2]).toContain('缩小范围');expect(q('qe-c03-0042').analyses[2]).not.toContain('后文');
 });
});
