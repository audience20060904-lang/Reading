import {readFileSync} from 'node:fs';
import {describe,it,expect} from 'vitest';
const read=(p:string)=>JSON.parse(readFileSync(p,'utf8')),catalog=read('src/data/question-revision-catalog.json');
const q=(id:string)=>catalog.questions.find((v:any)=>v.id===id);
describe('第四十二批：冻结恢复与诗歌片段',()=>{
 it('冻结目标和旧快照对应实际修订基线，来源和答案不变',()=>{
  const f=read('source/question-revisions/review-042-current-questions.json'),t=read('source/question-revisions/review-042-targets.json'),b=read('source/question-revisions/review-042-baseline.json');expect(f.questions.map((v:any)=>v.id)).toEqual(t.questionIds);expect(t.questionIds).toHaveLength(22);expect(t.sourceCandidateIds).toHaveLength(24);for(const old of b.questions){expect(old).toEqual(f.questions.find((v:any)=>v.id===old.id));expect(q(old.id).passage).toBe(old.passage);expect(q(old.id).sentenceIds).toEqual(old.sentenceIds);expect(q(old.id).answer).toBe(old.answer);}
 });
 it('定位线索逐字存在于当前原文，不以lots of替代原句',()=>{
  const v=q('q-c05-010'),phrase='a lot of different, intense emotions';expect(v.passage).toContain(phrase);expect(v.analyses[3]).toContain(phrase);expect(v.analyses[3]).not.toContain('lots of');expect(q('qe-c05-0021').analyses[2]).not.toContain('前文');
 });
 it('咖啡场景四题译文一致，不额外添加手持动作或补英文引号',()=>{
  const ids=['q-c05-013','qe-c05-0024','qe-c05-0025','qe-c05-0026'];for(const id of ids){expect(q(id).translation).toBe(q(ids[0]).translation);expect(q(id).translation).not.toContain('端着');expect(q(id).passage.endsWith('It comes on unexpectedly.')).toBe(true);}expect(q('qe-c05-0025').optionsZh[0]).not.toContain('端着');
 });
 it('比较和归属分析不借未显示的时间、诗人及榜样关系',()=>{
  expect(q('qe-c05-0014').analyses[3]).not.toContain('同一周末');expect(q('qe-c05-0024').analyses[1]).not.toContain('后面');expect(q('qe-c05-0019').analyses[2]).toContain('崇拜');expect(q('qe-c05-0019').analyses[2]).not.toContain('榜样');
 });
});
