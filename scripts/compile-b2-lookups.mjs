// Assemble prewritten, source-specific lexical records. No runtime dictionary or sense inference.
import {readFile,writeFile} from 'node:fs/promises';
import assert from 'node:assert/strict';
const read=async p=>JSON.parse(await readFile(p,'utf8'));
const book=await read('public/data/book.json'),author=await read('source/b2-vocabulary/author-notes.json'),base=await read(author.baseline);
assert.equal(author.pdfSha256,book.pdfSha256);assert.equal(base.pdfSha256,book.pdfSha256);
const entries=new Map(base.entries.map(e=>[e.id,e])),paragraphs=structuredClone(base.paragraphs),sources=new Map(book.paragraphs.map(p=>[p.id,p])),sentences=new Map(book.sentences.map(s=>[s.id,s]));
for(const entry of author.entries){assert(!entries.has(entry.id));assert(entry.headword&&['difficult','shifted'].includes(entry.kind)&&Array.isArray(entry.otherMeanings));entries.set(entry.id,entry);}
for(const {occurrence:o,origin} of author.additions){
 const p=sources.get(o.paragraphId);assert(p&&origin);assert(entries.has(o.entryId));assert.equal(o.id,`${p.id}@${o.start}:${o.end}`);assert.equal(p.text.slice(o.start,o.end),o.text);
 assert(o.contextMeaning&&!/正确答案|选项|答案为/.test(o.contextMeaning));
 assert.deepEqual(o.sentenceIds,p.sentenceIds.filter(id=>sentences.get(id).start<o.end&&sentences.get(id).end>o.start));assert(o.sentenceIds.length);
 const group=paragraphs[p.id]??=[];assert(!group.some(x=>x.start<o.end&&o.start<x.end),'Do not overwrite or overlap preserved lexical notes');group.push(o);
}
for(const group of Object.values(paragraphs))group.sort((a,b)=>a.start-b.start);
const used=new Set(Object.values(paragraphs).flat().map(o=>o.entryId));assert.equal(used.size,entries.size);
const catalog={...base,selection:'B2+ headword screening plus independently authored specialist terms and advanced contextual senses; exact prewritten occurrences, not a certified complete CEFR dictionary.',entries:[...entries.values()],paragraphs};
const save=async(p,v)=>{const s=JSON.stringify(v,null,2)+'\n';if(await readFile(p,'utf8').catch(()=>null)!==s)await writeFile(p,s);};
await save('src/data/word-lookups.json',catalog);
const previous=await read('source/word-lookup-review.json'),all=Object.values(paragraphs).flat();
await save('source/word-lookup-review.json',{...previous,date:'2026-10-28',entryCount:entries.size,occurrenceCount:all.length,paragraphCount:Object.keys(paragraphs).length,byChapter:Object.fromEntries(book.chapters.map(c=>[c.id,all.filter(o=>sources.get(o.paragraphId).chapterId===c.id).length])),sources:[author.baseline,'source/b2-vocabulary/author-notes.json','source/b2-vocabulary/corpus-glosses.tsv','public/data/book.json: exact original offsets'],rules:[...new Set([...previous.rules,'Oxford B2/C1 headwords screen candidates; levels do not certify every sense, and unlisted words are not automatically C2.','A recorded annotation count is not proof that every B2/C1/C2 sense has been reviewed. See source/b2-vocabulary/coverage.json.'])],unmatchedDraftEntries:previous.unmatchedDraftEntries});
console.log(JSON.stringify({entries:entries.size,occurrences:all.length,added:author.additions.length}));
