import {readFile,writeFile} from 'node:fs/promises';
import {createHash} from 'node:crypto';
import assert from 'node:assert/strict';
const book=JSON.parse(await readFile('public/data/book.json','utf8')),qs=JSON.parse(await readFile('public/data/questions.json','utf8'));
export function canonical(v){if(Array.isArray(v))return '['+v.map(canonical).join(',')+']';if(v&&typeof v==='object')return '{'+Object.keys(v).sort().map(k=>JSON.stringify(k)+':'+canonical(v[k])).join(',')+'}';return JSON.stringify(v);}
assert.equal(book.sentences[0].text,'Yoshi was born in a small mountain town on the island of Kyushu, Japan, known for its green tea and clementines.');
const sentences=new Map(book.sentences.map(s=>[s.id,s])),paragraphs=new Map(book.paragraphs.map(p=>[p.id,p]));
const ids=new Set();let last=-1;
for(const q of qs){assert(!ids.has(q.id));ids.add(q.id);const p=paragraphs.get(q.paragraphId);assert(p);assert(p.text.includes(q.passage),`passage ${q.id}`);assert(q.sentenceIds.length);assert.equal(q.chapterId,p.chapterId);assert.equal(q.sectionId,p.sectionId);assert.equal(q.options.length,4);assert.equal(q.analyses.length,4);assert(new Set(q.options).size===4);assert(q.answer>=0&&q.answer<4);const n=Math.min(...q.evidence.flatMap(e=>e.sentenceIds.map(id=>book.sentences.findIndex(s=>s.id===id))));assert(n>=last,`order ${q.id}`);last=n;
 for(const id of q.sentenceIds)assert(sentences.get(id)?.paragraphId===q.paragraphId,`context ${q.id}`);
 for(const e of q.evidence){assert(q.passage.includes(e.quote),`evidence ${q.id}`);assert(e.sentenceIds.length);for(const id of e.sentenceIds){const s=sentences.get(id);assert(q.sentenceIds.includes(id));assert(s);assert(s.sources.every(r=>e.sources.some(t=>r.pdfPage===t.pdfPage&&r.block===t.block)));}}
 const {fingerprint,...content}=q;assert.equal(createHash('sha256').update(canonical(content)).digest('hex'),fingerprint,`fingerprint ${q.id}`);
}
const readingPlan=JSON.parse(await readFile('public/data/reading-plan.json','utf8'));
const flattened=readingPlan.units.flatMap(u=>u.sentenceIds);
assert.deepEqual(flattened,book.sentences.map(s=>s.id),'Reading plan omits, duplicates or reorders sentences');
assert.equal(new Set(flattened).size,book.sentences.length);
assert.equal(readingPlan.coverage.allQuestionsPrepared,readingPlan.units.every(u=>u.questionId));
for(const q of qs){const unit=readingPlan.units.find(u=>u.id===q.readingUnitId);assert.equal(unit.questionId,q.id);assert.deepEqual(unit.sentenceIds,q.sentenceIds);}
const context=new Set(qs.flatMap(q=>q.sentenceIds)),evidence=new Set(qs.flatMap(q=>q.evidence.flatMap(e=>e.sentenceIds)));
const report={pdfPages:book.pdfPages,chapters:book.chapters.length,sections:book.sections.length,candidateParagraphs:book.paragraphs.length,candidateSentences:book.sentences.length,proofreadSentences:book.sentences.filter(s=>s.review==='visual-proofread').length,contextSentences:context.size,contextOnlySentences:[...context].filter(id=>!evidence.has(id)).length,evidenceSentences:evidence.size,notDirectlyQuestioned:book.sentences.length-evidence.size,questions:qs.length,excludedBlocks:book.excluded.length,fullCoverage:false,byChapter:book.chapters.map(c=>{const ss=book.sentences.filter(s=>s.chapterId===c.id);return {id:c.id,candidates:ss.length,proofread:ss.filter(s=>s.review==='visual-proofread').length,context:ss.filter(s=>context.has(s.id)).length,evidence:ss.filter(s=>evidence.has(s.id)).length,questions:qs.filter(q=>q.chapterId===c.id).length};}),notice:'自动分句仅为候选；审校、上下文和直接证据分别计数。即使每节有题，也不等于逐句覆盖。未配题内容保留原文及待办，不生成占位题。'};
await writeFile('public/data/coverage.json',JSON.stringify(report,null,2));
const batches=[
 {id:'batch-001',status:'saved',chapter:'c01',questionIds:qs.filter(q=>q.chapterId==='c01'&&Number(q.id.slice(-3))<=33).map(q=>q.id),note:'第 1 章逐题编写；不代表逐句配题完成'},
 {id:'batch-002',status:'saved',chapter:'c02',questionIds:qs.filter(q=>q.chapterId==='c02'&&Number(q.id.slice(-3))<=12).map(q=>q.id),note:'第 2 章最初 12 题；原 v1 指纹保存在归档，当前已修订为 v2'},
 {id:'batch-003',status:'saved',chapter:'c02',questionIds:qs.filter(q=>q.chapterId==='c02'&&Number(q.id.slice(-3))>=13&&Number(q.id.slice(-3))<=27).map(q=>q.id),reviewedPdfPages:[17,18,19,20,21,22,23,24,25,26],note:'新增 15 道具体原文题及整段译文；核对第 2 章 30 个叙事段落。句子边界仍为候选，未逐句配题'}
,
 {id:'batch-004',status:'saved',type:'short-reading-revision',revisedQuestionIds:qs.filter(q=>q.version===2).map(q=>q.id),newQuestionIds:qs.filter(q=>q.chapterId==='c01'&&Number(q.id.slice(-3))>=34&&Number(q.id.slice(-3))<=40).map(q=>q.id),note:'解析精简为选项分析、词汇、译文；全书原句无遗漏无重复分段。开篇第 1 小节短段已逐段配题，其余待办如实保留'},
 {id:'batch-005',status:'saved',chapter:'c01',newQuestionIds:qs.filter(q=>q.chapterId==='c01'&&Number(q.id.slice(-3))>=41&&Number(q.id.slice(-3))<=77).map(q=>q.id),reviewedPdfPages:[9,10,11,12,13,14,15,16],note:'补齐第 1 章其余 37 个短段；该章 77 段均有题目与中文材料，仍不能把每段一题当成每句直接证据覆盖。此前 67 题指纹不变。'},
 {id:'batch-006',status:'saved',chapter:'c02',newQuestionIds:['q-c02-028','q-c02-029'],reviewedPdfPages:[17],note:'按阅读顺序补齐两个短段；James 引述与 Diener 调查比例分别配题，保留原句和已发布题目。'},
 {id:'batch-007',status:'saved',chapter:'c02',newQuestionIds:['q-c02-030','q-c02-031'],reviewedPdfPages:[17,18],note:'补齐 Madison 两个短段，核对跨页原句；区分线上表象、本人感受和因果解释；保留全部已发布题目。'},
 {id:'batch-008',status:'saved',chapter:'c02',newQuestionIds:Array.from({length:45},(_,i)=>'q-c02-'+String(i+32).padStart(3,'0')),reviewedPdfPages:[18,19,20,21,22,23,24,25],note:'按原阅读顺序补齐接下来的 45 个未配题短段；冻结目标 ID 与原文指纹，逐段双语材料；原有 108 题保持不变，仍非逐句直接证据全覆盖。'}
];
const tasks={schemaVersion:1,pdfSha256:book.pdfSha256,extractionVersion:book.extractionVersion,batches,readingPlan:{units:readingPlan.units.length,includedCandidateSentences:flattened.length,duplicateSentenceIds:[],missingSentenceIds:[],remainingUnitIds:readingPlan.units.filter(u=>!u.questionId).map(u=>u.id),legacyArchive:'source/archive/questions-v1.json',currentQuestionVersion:2,completedSections:book.sections.filter(s=>readingPlan.units.filter(u=>u.sectionId===s.id).every(u=>u.questionId)).map(s=>s.id)},chapters:book.chapters.map(c=>({id:c.id,title:c.title,pdfPage:c.pdfPage,status:qs.some(q=>q.chapterId===c.id)?'partial':'not-authored',candidateSentences:book.sentences.filter(s=>s.chapterId===c.id).length,remainingReadingUnitIds:readingPlan.units.filter(u=>u.chapterId===c.id&&!u.questionId).map(u=>u.id),remainingProofreadIds:book.sentences.filter(s=>s.chapterId===c.id&&s.review!=='visual-proofread').map(s=>s.id),remainingEvidenceIds:book.sentences.filter(s=>s.chapterId===c.id&&!evidence.has(s.id)).map(s=>s.id),sections:book.sections.filter(s=>s.chapterId===c.id).map(s=>({id:s.id,title:s.title,status:qs.some(q=>q.sectionId===s.id)?'partial':'not-authored',questionIds:qs.filter(q=>q.sectionId===s.id).map(q=>q.id)}))})),nextBatch:{chapterId:readingPlan.units.find(u=>!u.questionId)?.chapterId,readingUnitId:readingPlan.units.find(u=>!u.questionId)?.id,action:'按全书短段顺序补齐尚无题目和中文材料的片段；原文完整纳入不等于全书题库完成。旧 v1 快照已归档，当前短段题为 v2。'},excluded:book.excluded};
await writeFile('source/content-tasks.json',JSON.stringify(tasks,null,2));
console.log(JSON.stringify({...report,byChapter:undefined},null,2));
