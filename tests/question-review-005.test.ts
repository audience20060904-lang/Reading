import {describe,it,expect} from 'vitest';
import {readFileSync} from 'node:fs';
const read=(p:string)=>JSON.parse(readFileSync(p,'utf8'));
const catalog=read('src/data/question-revision-catalog.json');
const q=(id:string)=>catalog.questions.find((q:any)=>q.id===id);

describe('第五批数字、片段独立性与研究范围校对',()=>{
 it('不把十四天的记录要求改成每人确实交齐；费用清单有逐字证据',()=>{
  const diary=q('q-c05-024');expect(diary.options[diary.answer]).toContain('were asked');expect(diary.analyses[diary.answer]).toContain('不能额外断言每人交齐十四份');
  const support=q('q-c05-033');for(const detail of ['full tuition','room and board','textbooks','round-trip airfare','one-month summer English class'])expect(support.evidence[0].quote).toContain(detail);
 });
 it('单句问题不要求辨认前文姓名，类比问题不依赖未显示的任务设置',()=>{
  const detail=q('q-c05-038');expect(detail.passage).not.toContain('Dean Reese');expect(detail.prompt).not.toContain('Dean Reese');expect(detail.promptZh).toContain('另一位');
  const analogy=q('q-c05-056');expect(analogy.options[analogy.answer]).not.toContain('task');expect(analogy.evidence[1].quote).toContain('made the participants’ lives psychologically richer');
 });
 it('未见组间差异保持报告范围，讣告评级保留信息缺漏的可能',()=>{
  const comparison=q('q-c05-048');expect(comparison.options[comparison.answer]).toContain('no reported gap');expect(comparison.translation).toContain('未见两组差异');expect(comparison.analyses[comparison.answer]).toContain('不等于');
  const limitation=q('q-c06-009');expect(limitation.options[limitation.answer]).toContain('may have left out');
  const denominator=q('q-c06-018');expect(denominator.options[denominator.answer]).toContain('fifteen people rated psychologically rich');
 });
});
