import {readFileSync} from 'node:fs';
import assert from 'node:assert/strict';
import type {ReadingPlan} from '../src/types';

// Batches 008–042 describe the historical 1053-unit pool. Additive source
// corrections must not change those snapshots or silently erase an old unit.
export function originalReadingPool(plan:ReadingPlan):ReadingPlan {
 const original=JSON.parse(readFileSync('source/archive/reading-units-original-v1.json','utf8')) as {id:string;sentenceIds:string[];questionId:string}[];
 const ids=new Set(original.map(u=>u.id)),units=plan.units.filter(u=>ids.has(u.id));
 assert.deepEqual(units.map(u=>({id:u.id,sentenceIds:u.sentenceIds,questionId:u.questionId})),original);
 return {...plan,units};
}
