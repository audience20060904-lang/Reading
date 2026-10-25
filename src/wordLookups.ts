import catalog from './data/word-lookups.json';

export type WordEntry={id:string;headword:string;kind:'difficult'|'shifted';otherMeanings:string[]};
export type WordOccurrence={id:string;paragraphId:string;start:number;end:number;text:string;entryId:string;contextMeaning:string;sentenceIds:string[]};
export type WordSelection=WordOccurrence & {entry:WordEntry};
const entries=new Map((catalog.entries as WordEntry[]).map(e=>[e.id,e]));
const paragraphs=catalog.paragraphs as Record<string,WordOccurrence[]>;

// Offsets identify a specific occurrence, not every use of the same spelling.
// A changed or historical source slice safely remains plain text.
export function getWordLookups(paragraphId:string,text:string,start:number):WordSelection[] {
 if(start<0)return [];
 return (paragraphs[paragraphId]??[]).filter(o=>o.start>=start&&o.end<=start+text.length&&text.slice(o.start-start,o.end-start)===o.text&&entries.has(o.entryId)).map(o=>({...o,entry:entries.get(o.entryId)!}));
}
