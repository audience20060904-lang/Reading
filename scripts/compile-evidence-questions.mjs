// Compile authored question records and exact PDF-derived evidence. Never invent a question.
import {readFile,writeFile,readdir} from 'node:fs/promises';
import {createHash} from 'node:crypto';
import assert from 'node:assert/strict';
import {matchEvidence,assertPlannedEvidence,validateTargetGroups} from './evidence-source.mjs';
const read=async p=>JSON.parse(await readFile(p,'utf8'));
const canonical=v=>Array.isArray(v)?'['+v.map(canonical).join(',')+']':v&&typeof v==='object'?'{'+Object.keys(v).sort().map(k=>JSON.stringify(k)+':'+canonical(v[k])).join(',')+'}':JSON.stringify(v);
const hash=s=>createHash('sha256').update(s).digest('hex');
async function save(p,v){const text=JSON.stringify(v,null,2)+'\n';if(await readFile(p,'utf8').catch(()=>null)!==text)await writeFile(p,text);}
const book=await read('public/data/book.json'),base=await read('public/data/questions.json'),repair=await read('src/data/sentence-repair-catalog.json'),rep=new Map(repair.questions.map(q=>[q.id,q])),primary=base.map(q=>rep.get(q.id)??q),locked=await read('source/evidence-questions/primary-baseline-fingerprints.json');
assert.deepEqual(Object.fromEntries(primary.map(q=>[q.id,q.fingerprint])),locked,'Do not rewrite primary questions while filling evidence gaps');
const sentences=new Map(book.sentences.map(s=>[s.id,s])),originalEvidence=new Set(primary.flatMap(q=>q.evidence.flatMap(e=>e.sentenceIds))),all=[...primary],supplemental=[],ids=new Set(primary.map(q=>q.id)),authoredTargets=new Set(),batches=[];
for(const name of (await readdir('source/evidence-questions')).filter(n=>/^batch\d+-author\.json$/.test(n)).sort()){
 const author=await read('source/evidence-questions/'+name),targets=await read('source/evidence-questions/'+name.replace('-author','-targets'));
 assert.equal(targets.pdfSha256,book.pdfSha256);assert.equal(author.id,targets.id);assert(targets.targets.length<=25);const groups=validateTargetGroups(targets.targets,author.questions);
 const beforeBatch=new Set(all.flatMap(q=>q.evidence.flatMap(e=>e.sentenceIds)));assert.equal(targets.previousRemaining,book.sentences.length-beforeBatch.size);
 const order=new Set();for(const row of author.questions){
  assert(!order.has(row.order));order.add(row.order);const group=groups.get(row.order),t=group[0],s=sentences.get(t.sentenceId),parent=primary.find(q=>q.id===t.parentQuestionId);assert(s&&parent);for(const member of group){const source=sentences.get(member.sentenceId);assert(source&&!originalEvidence.has(source.id));assert(!authoredTargets.has(source.id),'Do not target the same gap twice');authoredTargets.add(source.id);assert(parent.sentenceIds.includes(source.id));assert.equal(hash(source.text),member.sentenceSha256);assert.equal(source.text,member.sentenceText);assert.equal(parent.fingerprint,member.parentFingerprint);assert.equal(hash(parent.passage),member.passageSha256);assert.equal(parent.readingUnitId,member.readingUnitId);assert(!beforeBatch.has(source.id),'Target was already evidenced before this batch');}assert(!ids.has(t.questionId));ids.add(t.questionId);
  assert(typeof row.prompt==='string'&&row.prompt.endsWith('?'));assert(row.promptZh);for(const field of ['options','optionsZh','analyses'])assert(row[field].length===4&&row[field].every(x=>typeof x==='string'&&x.trim()));assert.equal(new Set(row.options).size,4);assert(Number.isInteger(row.answer)&&row.answer>=0&&row.answer<4);assert(row.vocabulary.length>0);assert(parent.passage.includes(s.text),'Evidence must be an exact source substring');
  for(const v of row.vocabulary){assert(v.word&&v.meaning&&v.context&&v.example&&v.collocations.length);assert(parent.passage.toLowerCase().includes(v.word.toLowerCase()),v.word);}
  assert(!beforeBatch.has(s.id),'Target was already evidenced before this batch');
  const q={id:t.questionId,version:1,family:'sentence-evidence',batchId:author.id,parentQuestionId:parent.id,chapterId:s.chapterId,sectionId:s.sectionId,paragraphId:parent.paragraphId,readingUnitId:parent.readingUnitId,sentenceIds:[...parent.sentenceIds],passage:parent.passage,prompt:row.prompt,promptZh:row.promptZh,options:row.options,optionsZh:row.optionsZh,answer:row.answer,type:row.type,support:row.support,analyses:row.analyses,vocabulary:row.vocabulary,translation:parent.translation,evidenceTargetIds:group.map(x=>x.sentenceId),evidence:[matchEvidence(book,parent,s.id,row.evidenceQuote??s.text)],editorialStatus:'逐题作者稿；已核对实际PDF原页；定位到此前未直接配题的候选句，不改写原句、不把上下文当作直接证据。',...(parent.sourceSegments?{sourceSegments:parent.sourceSegments}:{})};
  assert(q.evidenceTargetIds.every(id=>q.evidence[0].sentenceIds.includes(id)),'Grouped targets must all be in the actual exact quotation');
  assert(q.translation);q.fingerprint=hash(canonical(q));supplemental.push(q);all.push(q);
 }
 const receipt=`source/releases/evidence-${String(Number(name.match(/\d+/)[0])).padStart(3,'0')}.json`;const released=await read(receipt).catch(()=>null);
 const reviewed=await read('source/evidence-questions/'+name.replace('-author','-review')).catch(()=>null),produced=supplemental.filter(q=>q.batchId===author.id);
 assertPlannedEvidence(produced,beforeBatch,targets.targets.map(t=>t.sentenceId));
 if(reviewed){assert.equal(reviewed.status,'source-and-editorial-reviewed');for(const q of produced)assert.equal(reviewed.questions.find(x=>x.questionId===q.id)?.fingerprint,q.fingerprint,'Review does not match author draft');const pages=new Set(reviewed.reviewedPages.map(p=>p.pdfPage));assert(targets.targets.every(t=>t.pdfPages.every(p=>pages.has(p))),'Review full parent source pages');}
 if(released?.status==='published-and-verified')for(const q of produced)assert.equal(released.questionFingerprints[q.id],q.fingerprint,'Never silently change a published question');
 batches.push({id:author.id,status:released?.status==='published-and-verified'?'published-and-verified':reviewed?'prepared-not-yet-published':'prepared-needs-source-review',questionCount:author.questions.length,questionIds:author.questions.map(row=>targets.targets.find(t=>t.order===row.order).questionId),targetRecord:'source/evidence-questions/'+name.replace('-author','-targets'),authorRecord:'source/evidence-questions/'+name,receipt:released?receipt:null});
}
// Semantic corrections supplement old questions without changing their fingerprints.
const corrections=await read('source/semantic-evidence/questions.json');
assert.equal(corrections.pdfSha256,book.pdfSha256);
const correctionReceipt=await read('source/releases/semantic-001.json').catch(()=>null);
for(const row of corrections.questions){
 const s=sentences.get(row.targetSentenceId),parent=primary.find(q=>q.id===row.parentQuestionId);
 assert(s&&parent&&originalEvidence.has(s.id)&&parent.sentenceIds.includes(s.id));
 assert.equal(hash(s.text),row.sentenceSha256);assert.equal(parent.fingerprint,row.parentFingerprint);assert.equal(row.evidenceQuote,s.text);
 assert(!ids.has(row.id));ids.add(row.id);assert(row.reason&&row.prompt.endsWith('?')&&row.promptZh);
 for(const field of ['options','optionsZh','analyses'])assert(row[field].length===4&&row[field].every(x=>typeof x==='string'&&x.trim()));
 assert.equal(new Set(row.options).size,4);assert(Number.isInteger(row.answer)&&row.answer>=0&&row.answer<4);
 for(const v of row.vocabulary){assert(v.word&&v.meaning&&v.context&&v.example&&v.collocations.length);assert(parent.passage.toLowerCase().includes(v.word.toLowerCase()));}
 const q={id:row.id,version:1,family:'sentence-evidence',semanticAudit:true,batchId:'semantic-001',parentQuestionId:parent.id,chapterId:s.chapterId,sectionId:s.sectionId,paragraphId:parent.paragraphId,readingUnitId:parent.readingUnitId,sentenceIds:[...parent.sentenceIds],passage:parent.passage,prompt:row.prompt,promptZh:row.promptZh,options:row.options,optionsZh:row.optionsZh,answer:row.answer,type:row.type,support:row.support,analyses:row.analyses,vocabulary:row.vocabulary,translation:parent.translation,evidenceTargetIds:[s.id],evidence:[matchEvidence(book,parent,s.id,row.evidenceQuote)],editorialStatus:'原题证据关联中仅作背景的句子，已核对 PDF 原页并补充直接考查；保留原题和历史。',...(parent.sourceSegments?{sourceSegments:parent.sourceSegments}:{})};
 q.fingerprint=hash(canonical(q));if(correctionReceipt?.status==='published-and-verified')assert.equal(correctionReceipt.questionFingerprints[q.id],q.fingerprint,'Never silently change a published correction');
 supplemental.push(q);all.push(q);
}
if(corrections.questions.length)batches.push({id:'semantic-001',status:correctionReceipt?.status==='published-and-verified'?'published-and-verified':'prepared-not-yet-published',questionCount:corrections.questions.length,questionIds:corrections.questions.map(q=>q.id),targetRecord:'source/semantic-evidence/audit.json',authorRecord:'source/semantic-evidence/questions.json',receipt:correctionReceipt?'source/releases/semantic-001.json':null});
supplemental.sort((a,b)=>book.sentences.findIndex(s=>s.id===a.evidenceTargetIds[0])-book.sentences.findIndex(s=>s.id===b.evidenceTargetIds[0]));
const direct=new Set(all.flatMap(q=>q.evidence.flatMap(e=>e.sentenceIds))),remaining=book.sentences.filter(s=>!direct.has(s.id)).map(s=>s.id);
await save('public/data/evidence-questions.json',supplemental);
await save('source/evidence-tasks.json',{schemaVersion:1,pdfSha256:book.pdfSha256,objective:'Cover remaining candidate source IDs with authored, source-specific question evidence; group structural markers and page fragments with their context',initialRemaining:1661,status:remaining.length?'in-progress':batches.every(b=>b.status==='published-and-verified')?'candidate-evidence-published':'candidate-evidence-prepared',preparedQuestionCount:supplemental.length,publishedQuestionCount:batches.filter(b=>b.status==='published-and-verified').reduce((n,b)=>n+b.questionCount,0),directEvidence:direct.size,remainingSentenceIds:remaining,nextSentenceId:remaining[0]??null,batches,notice:'Prepared is distinct from published. Candidate IDs include structural markers and original automatic segmentation; they are not a final human sentence count. Old questions, original source units and real study history are preserved.'});
console.log(JSON.stringify({prepared:supplemental.length,directEvidence:direct.size,remaining:remaining.length,batches:batches.length}));
const published=batches.filter(b=>b.status==='published-and-verified').reduce((n,b)=>n+b.questionCount,0),readme=await readFile('README.md','utf8');
const progress=`<!-- evidence-progress:start -->\n## 直接证据补题 · ${remaining.length?'进行中':'候选来源 ID 已覆盖'}\n\n当前本地已准备${supplemental.length}道补题，已验证发布${published}道；尚未发布的本地批次不得当作线上完成。总题库${all.length}题（1056道主问题＋${supplemental.length}道补题），${direct.size}个候选来源 ID 关联到题目证据引文（关联本身不保证该句直接支持正确答案），仍有${remaining.length}个待补。后文1499/1661等数值记录此前修复阶段，当前以本节、public/data/coverage.json及真实发布回执为准。\n\n该 ID 清单包含列表编号、标点、签名及跨页片段，并非人工定稿的完整句子数；原有主问题的证据有时只是句子中的片段。编号和断句可与相邻正文共用一道题。不能据此声称全书人工逐句审校完成，fullCoverage 保持 false。\n\n<!-- evidence-progress:end -->`;
const updated=readme.replace(/<!-- evidence-progress:start -->[\s\S]*?<!-- evidence-progress:end -->/,progress);if(updated!==readme)await writeFile('README.md',updated);
