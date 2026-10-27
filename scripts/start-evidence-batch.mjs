import {readFile,writeFile,readdir} from 'node:fs/promises';
import {createHash} from 'node:crypto';
const read=async p=>JSON.parse(await readFile(p,'utf8'));
const folder='source/evidence-questions';
const frozen=(await readdir(folder)).filter(n=>/^batch\d+-targets\.json$/.test(n)).sort();
for(const name of frozen){const targets=await read(folder+'/'+name),number=name.match(/\d+/)[0],receipt=await read(`source/releases/evidence-${number}.json`).catch(()=>null);if(receipt?.status!=='published-and-verified'){console.log(JSON.stringify({action:'resume-existing-batch',batch:targets.id,targets:folder+'/'+name,author:folder+'/'+name.replace('-targets','-author'),count:targets.targets.length}));process.exit(0);}}
const book=await read('public/data/book.json'),base=await read('public/data/questions.json'),repairs=await read('src/data/sentence-repair-catalog.json'),extras=await read('public/data/evidence-questions.json'),replacements=new Map(repairs.questions.map(q=>[q.id,q])),primary=base.map(q=>replacements.get(q.id)??q),plan=await read('public/data/reading-plan.json'),units=plan.units.map(u=>repairs.units.find(r=>r.id===u.id)??u);
const covered=new Set([...primary,...extras].flatMap(q=>q.evidence.flatMap(e=>e.sentenceIds))),missing=book.sentences.filter(s=>!covered.has(s.id));
if(!missing.length){console.log(JSON.stringify({action:'audit-final-report',remaining:0}));process.exit(0);}
const sequence=frozen.length+1,number=String(sequence).padStart(3,'0'),id=`evidence-${number}`,chapterNext={};
for(const q of extras){const match=q.id.match(/^qe-(c\d+)-(\d+)$/);if(match)chapterNext[match[1]]=Math.max(chapterNext[match[1]]??0,Number(match[2]));}
// IDs allocated to grouped targets remain reserved even if no separate question uses them.
for(const name of frozen)for(const t of (await read(folder+'/'+name)).targets){const match=t.questionId.match(/^qe-(c\d+)-(\d+)$/);if(match)chapterNext[match[1]]=Math.max(chapterNext[match[1]]??0,Number(match[2]));}
const hash=s=>createHash('sha256').update(s).digest('hex'),targets=missing.slice(0,25).map((s,i)=>{const unit=units.find(u=>u.sentenceIds.includes(s.id)),parent=primary.find(q=>q.id===unit.questionId),n=(chapterNext[s.chapterId]??0)+1;chapterNext[s.chapterId]=n;return {order:i+1,questionId:`qe-${s.chapterId}-${String(n).padStart(4,'0')}`,sentenceId:s.id,sentenceText:s.text,sentenceSha256:hash(s.text),readingUnitId:unit.id,parentQuestionId:parent.id,parentFingerprint:parent.fingerprint,passageSha256:hash(parent.passage),pdfPages:unit.pdfPages};});
const targetPath=`${folder}/batch${number}-targets.json`,authorPath=`${folder}/batch${number}-author.json`;
await writeFile(targetPath,JSON.stringify({schemaVersion:1,id,status:'targets-frozen',pdfSha256:book.pdfSha256,previousRemaining:missing.length,evidenceRule:'Each authored question must genuinely require its frozen target sentence. Preserve exact PDF-derived text.',targets},null,2)+'\n',{flag:'wx'});
await writeFile(authorPath,JSON.stringify({schemaVersion:1,id,status:'authoring',evidenceRule:'frozen-target-sentence',questions:[]},null,2)+'\n',{flag:'wx'});
const task=await read('source/evidence-tasks.json');task.batches.push({id,status:'authoring',targetRecord:targetPath,authorRecord:authorPath,targetCount:targets.length});task.currentBatch=id;await writeFile('source/evidence-tasks.json',JSON.stringify(task,null,2)+'\n');
console.log(JSON.stringify({action:'author-new-batch',batch:id,targetPath,authorPath,targets:targets.length,pdfPages:[...new Set(targets.flatMap(t=>t.pdfPages))].sort((a,b)=>a-b),remaining:missing.length}));
