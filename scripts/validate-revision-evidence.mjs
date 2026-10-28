import assert from 'node:assert/strict';

// Existing citations keep their identity and can only expand. New citations
// must quote whole source candidates and carry their exact PDF references.
export function validateRevisionEvidence(previous,next,book){
 assert(next.evidence.length>=previous.evidence.length,'Existing citations cannot be removed');
 for(const [i,old] of previous.evidence.entries()){
  const e=next.evidence[i];
  assert(next.passage.includes(e.quote));assert(e.quote.includes(old.quote));
  assert.deepEqual(e.sentenceIds,old.sentenceIds);assert.deepEqual(e.sources,old.sources);
 }
 const sources=new Map((book.sentences??[]).map(s=>[s.id,s]));
 for(const e of next.evidence.slice(previous.evidence.length)){
  assert(e.quote&&next.passage.includes(e.quote),'New citation must match the shown passage');
  assert(e.sentenceIds.length&&new Set(e.sentenceIds).size===e.sentenceIds.length);
  const expected=[];
  for(const id of e.sentenceIds){
   const s=sources.get(id);assert(s&&next.sentenceIds.includes(id),'New citation must use a source in this passage');
   assert(e.quote.includes(s.text),'New citation must include its complete source candidate');
   for(const ref of s.sources)if(!expected.some(r=>JSON.stringify(r)===JSON.stringify(ref)))expected.push(ref);
  }
  assert.deepEqual(e.sources,expected,'New citation must preserve exact PDF references');
  assert(!next.evidence.slice(0,next.evidence.indexOf(e)).some(old=>old.quote===e.quote&&JSON.stringify(old.sentenceIds)===JSON.stringify(e.sentenceIds)),'Duplicate citation');
 }
}
