import {readFile,writeFile} from 'node:fs/promises';
import {createHash} from 'node:crypto';
import assert from 'node:assert/strict';
import {validateRevisionEvidence} from './validate-revision-evidence.mjs';
const read=async p=>JSON.parse(await readFile(p,'utf8'));
const canonical=v=>Array.isArray(v)?'['+v.map(canonical).join(',')+']':v&&typeof v==='object'?'{'+Object.keys(v).sort().map(k=>JSON.stringify(k)+':'+canonical(v[k])).join(',')+'}':JSON.stringify(v);
const book=await read('public/data/book.json'),manifest=await read('source/question-revisions/manifest.json'),base=await read('public/data/questions.json'),rep=await read('src/data/sentence-repair-catalog.json'),extras=await read('public/data/evidence-questions.json'),translations=await read('src/data/question-translations.json');
const sources=new Map([...base.map(q=>rep.questions.find(r=>r.id===q.id)??q),...extras].map(q=>[q.id,q])),latest=new Map(),baselineFingerprints={},revisionDepths={},batches=[];
assert.equal(manifest.schemaVersion,1);assert(manifest.batches.length);assert.equal(new Set(manifest.batches.map(b=>b.id)).size,manifest.batches.length);
for(const batch of manifest.batches){
 const draft=await read(batch.author),frozen=await read(batch.baseline),seen=new Set(),compiled=[];
 assert.equal(draft.id,batch.id);assert.equal(draft.pdfSha256,book.pdfSha256);assert.equal(frozen.pdfSha256,book.pdfSha256);
 for(const row of draft.questions){
 assert(!seen.has(row.id));seen.add(row.id);assert(row.reason);const q=latest.get(row.id)??sources.get(row.id);assert(q);assert.deepEqual(q,frozen.questions.find(x=>x.id===q.id),'Published baseline changed');
 const allowed=new Set(['prompt','promptZh','options','optionsZh','analyses','translation','evidence']);assert(Object.keys(row.updates).every(k=>allowed.has(k)));
 if('prompt' in row.updates)assert(row.updates.promptZh,'Changed prompt requires its own translation');
 const t=q.family==='sentence-evidence'||q.contentRevision?{promptZh:q.promptZh,optionsZh:q.optionsZh}:translations.entries.find(t=>t.questionId===q.id&&t.prompt===q.prompt&&t.options.every((o,i)=>o===q.options[i]));assert(t?.promptZh&&t.optionsZh?.length===4);
 const next={...q,promptZh:t.promptZh,optionsZh:t.optionsZh,...row.updates,version:q.version+1,contentRevision:draft.id};delete next.fingerprint;
 assert.equal(next.answer,q.answer);assert.equal(next.passage,q.passage);assert.equal(next.readingUnitId,q.readingUnitId);
 validateRevisionEvidence(q,next,book);
 for(const key of ['options','optionsZh','analyses'])assert(next[key].length===4&&next[key].every(v=>typeof v==='string'&&v.trim()),key);
 assert(new Set(next.options).size===4);assert(next.promptZh&&next.translation);
 next.fingerprint=createHash('sha256').update(canonical(next)).digest('hex');baselineFingerprints[q.id]??=q.fingerprint;revisionDepths[q.id]=(revisionDepths[q.id]??0)+1;compiled.push(next);latest.set(q.id,next);
}
assert.equal(seen.size,frozen.questions.length);
const receipt=await read(batch.receipt).catch(error=>{if(error.code==='ENOENT')return null;throw error;});
if(receipt?.status==='published-and-verified'){assert.deepEqual(Object.keys(receipt.questionFingerprints).sort(),compiled.map(q=>q.id).sort());for(const q of compiled)assert.equal(q.fingerprint,receipt.questionFingerprints[q.id],'Published editorial batch is immutable; create a new revision batch and increment its versions');}
batches.push({id:batch.id,questionIds:compiled.map(q=>q.id),questionFingerprints:Object.fromEntries(compiled.map(q=>[q.id,q.fingerprint]))});
}
const questions=[...latest.values()],content=JSON.stringify({schemaVersion:1,id:batches.at(-1).id,revisionIds:batches.map(b=>b.id),batches,pdfSha256:book.pdfSha256,baselineFingerprints,revisionDepths,questions},null,2)+'\n',path='src/data/question-revision-catalog.json';if(await readFile(path,'utf8').catch(()=>null)!==content)await writeFile(path,content);
console.log(JSON.stringify({revisedQuestions:questions.length,answerPositionsChanged:0,sourcePassagesChanged:0}));
