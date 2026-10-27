import {readFileSync} from 'node:fs';
import {describe,it,expect} from 'vitest';
import {assertCoverageClaim} from '../src/core';
const read=(p:string)=>JSON.parse(readFileSync(p,'utf8'));
describe('final candidate evidence inventory',()=>{
 it('covers every existing candidate ID with direct evidence without declaring final sentence coverage',()=>{
  const book=read('public/data/book.json'),base=read('public/data/questions.json'),rep=read('src/data/sentence-repair-catalog.json'),extras=read('public/data/evidence-questions.json'),coverage=read('public/data/coverage.json');
  const primary=base.map((q:any)=>rep.questions.find((r:any)=>r.id===q.id)??q),ids=new Set([...primary,...extras].flatMap((q:any)=>q.evidence.flatMap((e:any)=>e.sentenceIds)));
  expect([...ids].sort()).toEqual(book.sentences.map((s:any)=>s.id).sort());
  expect(coverage.evidenceSentences).toBe(book.sentences.length);expect(coverage.notDirectlyQuestioned).toBe(0);expect(coverage.fullCoverage).toBe(false);expect(()=>assertCoverageClaim(coverage,true)).toThrow();
 });
 it('groups the final numbered headings with contextual questions while preserving their source IDs',()=>{
  const targets=read('source/evidence-questions/batch067-targets.json').targets,qs=read('public/data/evidence-questions.json').filter((q:any)=>q.batchId==='evidence-067');
  expect(qs).toHaveLength(9);expect(qs.flatMap((q:any)=>q.evidenceTargetIds)).toHaveLength(11);
  for(const order of [1,5]){const first=targets.find((t:any)=>t.order===order),second=targets.find((t:any)=>t.order===order+1),q=qs.find((x:any)=>x.evidenceTargetIds.includes(first.sentenceId));expect(q.evidenceTargetIds).toContain(second.sentenceId);expect(q.evidence[0].quote).toContain(first.sentenceText);expect(q.evidence[0].quote).toContain(second.sentenceText);}
 });
});
