import assert from 'node:assert/strict';
// Group only an adjacent list marker or an obviously incomplete continuation with
// its neighbour. Every frozen target must still be accounted for exactly once.
export function validateTargetGroups(targets,rows){
 const byOrder=new Map(targets.map(t=>[t.order,t])),seen=new Set(),groups=new Map();
 for(const row of rows){const orders=row.targetOrders??[row.order];assert(Array.isArray(orders)&&orders.length>=1&&orders.length<=2);assert.equal(orders[0],row.order);
  const group=orders.map((order,i)=>{assert(Number.isInteger(order)&&!seen.has(order),'Duplicate target order');seen.add(order);const t=byOrder.get(order);assert(t,'Unknown target order');if(i){assert.equal(order,orders[i-1]+1,'Grouped targets must be adjacent');assert.equal(t.parentQuestionId,byOrder.get(orders[0]).parentQuestionId,'Grouped targets must share one reading unit');}return t;});
  if(group.length===2){const first=group[0].sentenceText;assert(/^\d+\.$/.test(first)||!/[.!?…][”’"']?$/.test(first),'Group only list markers or incomplete continuations');}
  groups.set(row.order,group);
 }
 assert.equal(seen.size,targets.length,'Each frozen target must be assigned once');return groups;
}
// A longer quotation must not silently consume an unassigned gap from a future batch.
export function assertPlannedEvidence(questions,previouslyEvidenced,targetIds){
 const planned=new Set(targetIds);
 for(const q of questions)for(const evidence of q.evidence)for(const id of evidence.sentenceIds)
  assert(previouslyEvidenced.has(id)||planned.has(id),`Evidence quote covers unassigned gap ${id}; trim the quote to the evidence needed for the authored question`);
}
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
