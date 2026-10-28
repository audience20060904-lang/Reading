import {readFile,writeFile} from 'node:fs/promises';
import {createHash} from 'node:crypto';
import assert from 'node:assert/strict';
const read=async p=>JSON.parse(await readFile(p,'utf8'));
const canonical=v=>Array.isArray(v)?'['+v.map(canonical).join(',')+']':v&&typeof v==='object'?'{'+Object.keys(v).sort().map(k=>JSON.stringify(k)+':'+canonical(v[k])).join(',')+'}':JSON.stringify(v);
const book=await read('public/data/book.json'),draft=await read('source/question-revisions/review-001.json'),frozen=await read('source/question-revisions/review-001-baseline.json'),base=await read('public/data/questions.json'),rep=await read('src/data/sentence-repair-catalog.json'),extras=await read('public/data/evidence-questions.json'),translations=await read('src/data/question-translations.json');
assert.equal(draft.pdfSha256,book.pdfSha256);assert.equal(frozen.pdfSha256,book.pdfSha256);
const sources=new Map([...base.map(q=>rep.questions.find(r=>r.id===q.id)??q),...extras].map(q=>[q.id,q])),seen=new Set(),questions=[],baselineFingerprints={};
for(const row of draft.questions){
 assert(!seen.has(row.id));seen.add(row.id);assert(row.reason);const q=sources.get(row.id);assert(q);assert.deepEqual(q,frozen.questions.find(x=>x.id===q.id),'Published baseline changed');
 const allowed=new Set(['promptZh','options','optionsZh','analyses','translation','evidence']);assert(Object.keys(row.updates).every(k=>allowed.has(k)));
 const t=q.family==='sentence-evidence'?{promptZh:q.promptZh,optionsZh:q.optionsZh}:translations.entries.find(t=>t.questionId===q.id&&t.prompt===q.prompt&&t.options.every((o,i)=>o===q.options[i]));assert(t?.promptZh&&t.optionsZh?.length===4);
 const next={...q,promptZh:t.promptZh,optionsZh:t.optionsZh,...row.updates,version:q.version+1,contentRevision:draft.id};delete next.fingerprint;
 assert.equal(next.answer,q.answer);assert.equal(next.passage,q.passage);assert.equal(next.readingUnitId,q.readingUnitId);
 assert.equal(next.evidence.length,q.evidence.length);
 for(const [i,e] of next.evidence.entries()){assert(next.passage.includes(e.quote));assert(e.quote.includes(q.evidence[i].quote));assert.deepEqual(e.sentenceIds,q.evidence[i].sentenceIds);assert.deepEqual(e.sources,q.evidence[i].sources);}
 for(const key of ['options','optionsZh','analyses'])assert(next[key].length===4&&next[key].every(v=>typeof v==='string'&&v.trim()),key);
 assert(new Set(next.options).size===4);assert(next.promptZh&&next.translation);
 next.fingerprint=createHash('sha256').update(canonical(next)).digest('hex');baselineFingerprints[q.id]=q.fingerprint;questions.push(next);
}
assert.equal(seen.size,frozen.questions.length);
const receipt=await read('source/releases/question-review-001.json').catch(error=>{if(error.code==='ENOENT')return null;throw error;});
if(receipt?.status==='published-and-verified')for(const q of questions)assert.equal(q.fingerprint,receipt.questionFingerprints[q.id],'Published editorial batch is immutable; create a new revision batch and increment its versions');
const content=JSON.stringify({schemaVersion:1,id:draft.id,pdfSha256:book.pdfSha256,baselineFingerprints,questions},null,2)+'\n',path='src/data/question-revision-catalog.json';if(await readFile(path,'utf8').catch(()=>null)!==content)await writeFile(path,content);
console.log(JSON.stringify({revisedQuestions:questions.length,answerPositionsChanged:0,sourcePassagesChanged:0}));
