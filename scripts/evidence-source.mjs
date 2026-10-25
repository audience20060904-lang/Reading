import assert from 'node:assert/strict';
// Map an authored exact quote to immutable source IDs, including reviewed cross-page joins.
export function matchEvidence(book,parent,targetId,quote){
 const ss=parent.sentenceIds.map(id=>book.sentences.find(s=>s.id===id)),target=ss.find(s=>s.id===targetId);assert(target);
 const segments=parent.sourceSegments??[{paragraphId:parent.paragraphId,start:ss[0].start,end:ss.at(-1).end,text:parent.passage,separator:''}];
 let offset=0;const ranges=[];
 for(const segment of segments){offset+=segment.separator.length;for(const s of ss.filter(s=>s.paragraphId===segment.paragraphId&&s.start>=segment.start&&s.end<=segment.end))ranges.push({s,start:offset+s.start-segment.start,end:offset+s.end-segment.start});offset+=segment.text.length;}
 const targetRange=ranges.find(r=>r.s.id===targetId);assert(targetRange);let start=parent.passage.indexOf(quote),chosen;
 while(start>=0){const end=start+quote.length;if(start<=targetRange.start&&end>=targetRange.end){chosen=ranges.filter(r=>r.start<end&&r.end>start);break;}start=parent.passage.indexOf(quote,start+1);}
 assert(chosen?.length,'Authored evidence must contain the target sentence and match its actual location');
 const sources=[];for(const r of chosen)for(const source of r.s.sources)if(!sources.some(x=>JSON.stringify(x)===JSON.stringify(source)))sources.push(source);
 return {quote,sentenceIds:chosen.map(r=>r.s.id),sources};
}
