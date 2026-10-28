import {readFileSync} from 'node:fs';
import {describe,it,expect} from 'vitest';
const read=(p:string)=>JSON.parse(readFileSync(p,'utf8')),catalog=read('src/data/question-revision-catalog.json'),book=read('public/data/book.json');
const q=(id:string)=>catalog.questions.find((v:any)=>v.id===id);
describe('第二十五批：满足所需的证据与择校情境译文',()=>{
 it('UVA选择题的逐字证据直接展示everything I want，而不仅申请/录取',()=>{
  const v=q('q-c02-021'),old=read('source/question-revisions/review-025-baseline.json').questions.find((q:any)=>q.id===v.id);expect(v.answer).toBe(0);expect(v.evidence[0]).toEqual(old.evidence[0]);const added=v.evidence[1];expect(added.quote).toContain('has everything I want.');expect(added.quote).toContain('You apply only to UVA and get in.');expect(added.sentenceIds).toHaveLength(3);expect(v.passage).toContain(added.quote);expect(added.quote).toBe(added.sentenceIds.map((id:string)=>book.sentences.find((s:any)=>s.id===id).text).join(' '));
 });
 it('同段GPA精确译为绩点，almost保留且不补分制或SAT门槛',()=>{
  const ids=['q-c02-069','qe-c02-0071','qe-c02-0072','qe-c02-0073'];for(const id of ids)expect(q(id).translation).toBe(q(ids[0]).translation);expect(q(ids[0]).translation).toContain('平均学分绩点（GPA）接近满分');expect(q('qe-c02-0072').analyses[2]).not.toContain('后文');
 });
 it('满意即可的选择者五题译文一致，解释不借其他段落的专名与时间',()=>{
  const ids=['q-c02-021','qe-c02-0074','qe-c02-0075','qe-c02-0076','qe-c02-0077'];for(const id of ids)expect(q(id).translation).toBe(q(ids[0]).translation);expect(q(ids[0]).translation).toContain('“满意即可”的选择者');expect(q('qe-c02-0069').analyses.join(' ')).not.toMatch(/此前|后面/);expect(q('qe-c02-0079').analyses[2]).not.toContain('此前');
 });
});
