// Compile reviewed, prewritten corrections. No runtime question generation.
import {readFile,writeFile} from 'node:fs/promises';
import {createHash} from 'node:crypto';
import assert from 'node:assert/strict';
const read=async p=>JSON.parse(await readFile(p,'utf8'));
const canonical=v=>Array.isArray(v)?'['+v.map(canonical).join(',')+']':v&&typeof v==='object'?'{'+Object.keys(v).sort().map(k=>JSON.stringify(k)+':'+canonical(v[k])).join(',')+'}':JSON.stringify(v);
const hash=v=>createHash('sha256').update(typeof v==='string'?v:canonical(v)).digest('hex');
async function save(p,v){const text=JSON.stringify(v,null,2)+'\n';if(await readFile(p,'utf8').catch(()=>null)!==text)await writeFile(p,text);}
const book=await read('public/data/book.json'),bank=await read('public/data/questions.json'),plan=await read('public/data/reading-plan.json'),author=await read('source/sentence-repairs.json');
assert.equal(book.pdfSha256,author.pdfSha256);
const sentences=new Map(book.sentences.map(s=>[s.id,s])),paragraphs=new Map(book.paragraphs.map(p=>[p.id,p])),units=structuredClone(plan.units),active=structuredClone(bank),changed=new Set();
for(const pair of author.pairs){
 const l=units.find(u=>u.questionId===pair.left),r=units.find(u=>u.questionId===pair.right);assert.equal(units.indexOf(l)+1,units.indexOf(r));assert.equal(l.sectionId,r.sectionId);
 const n=pair.sentenceIds.length;
 if(pair.direction==='left-to-right'){assert.deepEqual(l.sentenceIds.slice(-n),pair.sentenceIds);l.sentenceIds.splice(-n);r.sentenceIds.unshift(...pair.sentenceIds);}
 else{assert.deepEqual(r.sentenceIds.slice(0,n),pair.sentenceIds);r.sentenceIds.splice(0,n);l.sentenceIds.push(...pair.sentenceIds);}
 for(const u of [l,r]){
  assert(u.sentenceIds.length);const segments=[];
  for(const id of u.sentenceIds){const s=sentences.get(id),last=segments.at(-1);assert.equal(s.sectionId,u.sectionId);if(last?.paragraphId===s.paragraphId)last.end=s.end;else segments.push({paragraphId:s.paragraphId,start:s.start,end:s.end,separator:segments.length?(pair.join??' '):''});}
  for(const s of segments){s.text=paragraphs.get(s.paragraphId).text.slice(s.start,s.end);assert(s.text);}
  const passage=segments.map(s=>s.separator+s.text).join('');u.sourceSegments=segments;u.wordCount=passage.trim().split(/\s+/).length;assert(u.wordCount<=110,`${u.questionId}: ${u.wordCount} words`);u.pdfPages=[...new Set(u.sentenceIds.flatMap(id=>sentences.get(id).sources.map(s=>s.pdfPage)))].sort((a,b)=>a-b);
  const q=active.find(q=>q.id===u.questionId),original=bank.find(x=>x.id===q.id);q.passage=passage;q.sentenceIds=[...u.sentenceIds];q.version=original.version+1;q.sourceSegments=segments;q.boundaryRepair=author.id;q.translation=author.translations[q.id];assert(q.translation);q.editorialStatus='按实际PDF修复相邻单元断句；原字符、源ID与阅读次序保留，旧版本和作答快照不改写。';
  for(const [i,text] of Object.entries(author.analysisReplacements[q.id]??{}))q.analyses[Number(i)]=text;
  if(q.id==='q-c06-032')q.vocabulary[0].context='表示列出的自评问题并非全部，后面还可以有同类问题。';
  changed.add(q.id);
 }
}
const replacement=author.questionReplacement,q=active.find(q=>q.id===replacement.id);
for(const field of ['prompt','options','answer','type','support','analyses','vocabulary'])q[field]=replacement[field];
assert(q.passage.includes(replacement.evidenceQuote));
q.evidence=[{quote:replacement.evidenceQuote,sentenceIds:[...q.sentenceIds],sources:q.sentenceIds.flatMap(id=>sentences.get(id).sources).filter((s,i,a)=>a.findIndex(x=>x.pdfPage===s.pdfPage&&x.block===s.block)===i)}];
for(const id of changed){const q=active.find(q=>q.id===id);for(const e of q.evidence){assert(q.passage.includes(e.quote),`evidence ${id}`);assert(e.sentenceIds.every(s=>q.sentenceIds.includes(s)),`evidence IDs ${id}`);}delete q.fingerprint;q.fingerprint=hash(q);}
assert.deepEqual(units.flatMap(u=>u.sentenceIds),book.sentences.map(s=>s.id));
const catalog={schemaVersion:1,id:author.id,pdfSha256:author.pdfSha256,rule:author.rule,baselineFingerprints:Object.fromEntries(bank.filter(q=>changed.has(q.id)).map(q=>[q.id,q.fingerprint])),questions:active.filter(q=>changed.has(q.id)),units:units.filter(u=>changed.has(u.questionId)),coverage:{...plan.coverage,over90Words:units.filter(u=>u.wordCount>90).map(u=>u.id),maxWords:Math.max(...units.map(u=>u.wordCount))}};
await save('src/data/sentence-repair-catalog.json',catalog);
const translations=await read('src/data/passage-translations.json');
for(const q of catalog.questions)if(!translations.entries.some(e=>e.questionId===q.id&&e.passage===q.passage))translations.entries.push({questionId:q.id,passage:q.passage,sourceFingerprint:q.fingerprint,translation:q.translation});
await save('src/data/passage-translations.json',translations);
const questionTranslations=await read('src/data/question-translations.json');
if(!questionTranslations.entries.some(e=>e.questionId===q.id&&e.prompt===q.prompt))questionTranslations.entries.push({questionId:q.id,prompt:q.prompt,options:q.options,promptZh:replacement.promptZh,optionsZh:replacement.optionsZh});
await save('src/data/question-translations.json',questionTranslations);
console.log(JSON.stringify({repairedBoundaries:author.pairs.length,revisedQuestions:changed.size,units:units.length,over90:catalog.coverage.over90Words.length,maxWords:catalog.coverage.maxWords}));
