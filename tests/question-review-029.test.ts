import {readFileSync} from 'node:fs';
import {describe,it,expect} from 'vitest';
const read=(p:string)=>JSON.parse(readFileSync(p,'utf8')),catalog=read('src/data/question-revision-catalog.json');
const q=(id:string)=>catalog.questions.find((v:any)=>v.id===id);
describe('第二十九批：恢复冻结批次与当前片段解释',()=>{
 it('已冻结题目按原顺序恢复，修订保留原文、来源及版本链',()=>{
  const frozen=read('source/question-revisions/review-029-current-questions.json'),targets=read('source/question-revisions/review-029-targets.json'),base=read('source/question-revisions/review-029-baseline.json');expect(frozen.questions.map((q:any)=>q.id)).toEqual(targets.questionIds);expect(targets.questionIds).toHaveLength(14);
  for(const old of base.questions){expect(old).toEqual(frozen.questions.find((q:any)=>q.id===old.id));expect(q(old.id).version).toBe(old.version+1);expect(q(old.id).passage).toBe(old.passage);expect(q(old.id).sentenceIds).toEqual(old.sentenceIds);expect(q(old.id).answer).toBe(old.answer);}
  expect(read('source/question-revisions/review-029-report.json').manual.questionCount).toBe(14);
 });
 it('down on区分批评态度、本人难过及全部目标排序',()=>{
  const v=q('qe-c03-0004');expect(v.answer).toBe(3);expect(v.options[1]).toContain('Feeling sad');expect(v.options[v.answer]).toBe('Being critical or disapproving of happiness.');expect(v.analyses[1]).toContain('批评态度');
 });
 it('搭配与意义解释不借未显示的未来段落',()=>{
  const phrase=q('qe-c03-0006').vocabulary[0];for(const c of phrase.collocations)expect(c).toMatch(/^at the expense of /);
  expect(q('qe-c03-0007').vocabulary[0].context).not.toContain('后文');expect(q('qe-c03-0010').analyses[2]).not.toContain('前述');expect(q('qe-c03-0011').analyses.join(' ')).not.toMatch(/属于后面|是前面/);
 });
});
