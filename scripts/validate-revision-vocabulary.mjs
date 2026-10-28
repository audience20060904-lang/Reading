import assert from 'node:assert/strict';
export function validateRevisionVocabulary(vocabulary){
 assert(Array.isArray(vocabulary)&&vocabulary.length,'Vocabulary revision must contain complete authored entries');
 for(const v of vocabulary){
  assert(v&&['word','meaning','context','example'].every(k=>typeof v[k]==='string'&&v[k].trim()),'Vocabulary revision is incomplete');
  assert(Array.isArray(v.collocations)&&v.collocations.length&&v.collocations.every(c=>typeof c==='string'&&c.trim()),'Vocabulary collocations are incomplete');
 }
}
