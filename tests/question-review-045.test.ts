import {readFileSync} from 'node:fs';
import {describe,it,expect} from 'vitest';
const read=(p:string)=>JSON.parse(readFileSync(p,'utf8'));
const revisions=read('src/data/question-revision-catalog.json').questions;
const q=(id:string)=>revisions.find((v:any)=>v.id===id);
describe('第四十五批：短段自足、对话与回忆范围',()=>{
 it('设想题不要求识别片段未显示的导师身份，且不将预期当保证',()=>{
  const v=q('qe-c05-0056');expect(v.prompt).not.toContain('advisor');expect(v.options[v.answer]).toContain('would');expect(v.analyses[v.answer]).toContain('没有保证实际结果');expect(v.passage).toContain('His assumption was that');
 });
 it('音乐发问分析可用当前段核对，不预告后续答案及室友情节',()=>{
  expect(q('qe-c05-0058').analyses.join(' ')).not.toMatch(/后面的 Jazz|后面另一问|保留原页/);expect(q('qe-c05-0059').analyses.join(' ')).not.toMatch(/下一段作答|电话故事|候选ID/);expect(q('qe-c05-0059').analyses[1]).toContain('Dean Reese asked');
 });
 it('四题完整译文保留字面引语与I thought的认知归属',()=>{
  const ids=['q-c05-037','qe-c05-0063','qe-c05-0064','qe-c05-0065'];for(const id of ids){const v=q(id);expect(v.translation).toBe(q(ids[0]).translation);expect(v.translation).toContain('字面是');expect(v.translation).toContain('我以为');expect(v.passage).toContain('I thought');}
 });
 it('四题共享回忆译文不将don’t remember many扩大为没有任何回忆，冻结恢复范围真实',()=>{
  for(const id of ['q-c05-039','qe-c05-0066','qe-c05-0067','qe-c05-0068']){expect(q(id).translation).toContain('能记起来的不多');expect(q(id).translation).toContain('许多事情');}
  const r=read('source/question-revisions/review-045-report.json');expect(r.manual.questionCount).toBe(21);expect(r.manual.sourceCandidatesReviewed).toBe(25);expect(r.manual.pdfPagesVisuallyReviewed).toEqual([48,49]);expect(r.fullQuestionBankHumanReview).toBe(false);expect(r.frozenCheckpoint).toContain('045-checkpoint');
 });
});
