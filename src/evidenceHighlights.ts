import type {Book,Question} from './types';
export type TextHighlight={start:number;end:number};
export function evidenceHighlights(q:Question,book:Book):TextHighlight[]{
 const paragraph=book.paragraphs.find(p=>p.id===q.paragraphId),start=paragraph?.text.indexOf(q.passage)??-1;
 const segments=q.sourceSegments??(start>=0?[{paragraphId:q.paragraphId,start,end:start+q.passage.length,text:q.passage,separator:''}]:[]);
 const windows=new Map<string,TextHighlight>();let offset=0;
 for(const segment of segments){offset+=segment.separator.length;for(const sentence of book.sentences.filter(s=>s.paragraphId===segment.paragraphId&&s.start<segment.end&&s.end>segment.start))windows.set(sentence.id,{start:offset+Math.max(0,sentence.start-segment.start),end:offset+Math.min(segment.text.length,sentence.end-segment.start)});offset+=segment.text.length;}
 const ranges:TextHighlight[]=[];
 for(const e of q.evidence){if(!e.quote)continue;const matches:TextHighlight[]=[];let at=q.passage.indexOf(e.quote);while(at>=0){matches.push({start:at,end:at+e.quote.length});at=q.passage.indexOf(e.quote,at+1);}
  const located=matches.length<=1?matches:matches.filter(m=>e.sentenceIds.some(id=>{const w=windows.get(id);return w&&m.start<w.end&&m.end>w.start;}));
  // Ambiguous repeated fragments stay unmarked rather than implying a location.
  if(located.length===1)ranges.push(located[0]);
 }
 ranges.sort((a,b)=>a.start-b.start);const merged:TextHighlight[]=[];
 for(const range of ranges){const previous=merged.at(-1);if(previous&&range.start<=previous.end)previous.end=Math.max(previous.end,range.end);else merged.push({...range});}return merged;
}
export function sliceHighlights(ranges:TextHighlight[],start:number,length:number):TextHighlight[]{return ranges.filter(r=>r.start<start+length&&r.end>start).map(r=>({start:Math.max(0,r.start-start),end:Math.min(length,r.end-start)}));}
