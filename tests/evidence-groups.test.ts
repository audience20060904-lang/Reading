import {describe,it,expect} from 'vitest';
import {validateTargetGroups} from '../scripts/evidence-source.mjs';
import {readFileSync} from 'node:fs';

const targets=[
 {order:1,parentQuestionId:'p',sentenceText:'8.'},
 {order:2,parentQuestionId:'p',sentenceText:'A heading: A complete sentence.'},
 {order:3,parentQuestionId:'q',sentenceText:'Stop by a'},
 {order:4,parentQuestionId:'q',sentenceText:'gallery, a shop, or a bookstore.'},
];
describe('grouped evidence targets',()=>{
 it('allows markers and split continuations to share their own contextual question',()=>{
  const groups=validateTargetGroups(targets,[{order:1,targetOrders:[1,2]},{order:3,targetOrders:[3,4]}]);
  expect(groups.get(1)?.map((t:any)=>t.order)).toEqual([1,2]);expect(groups.get(3)?.map((t:any)=>t.order)).toEqual([3,4]);
 });
 it('rejects missing, duplicate, unrelated and complete-sentence pairings',()=>{
  expect(()=>validateTargetGroups(targets,[{order:1,targetOrders:[1,2]}])).toThrow();
  expect(()=>validateTargetGroups(targets,[{order:1,targetOrders:[1,2]},{order:2},{order:3,targetOrders:[3,4]}])).toThrow();
  expect(()=>validateTargetGroups(targets,[{order:1,targetOrders:[1,3]},{order:2},{order:4}])).toThrow();
  expect(()=>validateTargetGroups([{order:1,parentQuestionId:'p',sentenceText:'A complete sentence.'},{order:2,parentQuestionId:'p',sentenceText:'Another sentence.'}],[{order:1,targetOrders:[1,2]}])).toThrow();
 });
 it('covers the real grouped batch once while retaining exact source text',()=>{
  const targets=JSON.parse(readFileSync('source/evidence-questions/batch066-targets.json','utf8')).targets;
  const questions=JSON.parse(readFileSync('public/data/evidence-questions.json','utf8')).filter((q:any)=>q.batchId==='evidence-066');
  expect(questions).toHaveLength(18);
  const ids=questions.flatMap((q:any)=>q.evidenceTargetIds);
  expect(ids).toHaveLength(25);expect(new Set(ids).size).toBe(25);
  expect([...ids].sort()).toEqual(targets.map((t:any)=>t.sentenceId).sort());
  for(const q of questions)for(const id of q.evidenceTargetIds){const t=targets.find((x:any)=>x.sentenceId===id);expect(q.evidence[0].quote).toContain(t.sentenceText);}
 });
});
