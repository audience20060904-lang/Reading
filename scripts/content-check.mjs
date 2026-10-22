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
,
 {id:'batch-009',status:'saved',chapters:['c02','c03'],newQuestionIds:[...Array.from({length:10},(_,i)=>'q-c02-'+String(i+77).padStart(3,'0')),...Array.from({length:40},(_,i)=>'q-c03-'+String(i+1).padStart(3,'0'))],reviewedPdfPages:[25,26,27,28,29,30,31,32],note:'按阅读顺序补齐 50 个缺口：第 2 章末 10 段、第 3 章前 40 段；保留原有 153 题和印刷措辞。新增第 3 章 17 个原页审阅段落。调查自报、相关、文学与假设分别说明，仍非逐句直接证据全覆盖。'}
,
 {id:'batch-010',status:'saved',chapters:['c03','c04'],newQuestionIds:[...Array.from({length:7},(_,i)=>'q-c03-'+String(i+41).padStart(3,'0')),...Array.from({length:18},(_,i)=>'q-c04-'+String(i+1).padStart(3,'0'))],reviewedPdfPages:[33,34,35,36,37,38],note:'连续补齐 25 个短段：第 3 章末 7 段和第 4 章前 18 段；保留此前 203 题指纹。新增 11 个完整原页审阅段落，文学、论述和真实个案分别处理，不扩大为普遍因果。'}
,
 {id:'batch-011',status:'saved',chapter:'c04',newQuestionIds:Array.from({length:25},(_,i)=>'q-c04-'+String(i+19).padStart(3,'0')),reviewedPdfPages:[38,39,40,41],note:'连续补齐第 4 章接下来的 25 个短段；保留此前 228 题指纹。新增 14 个完整原页审阅段落；Gopnik、Jobs、Joy 与 Brad 的个案和引语分别说明，保留原书历史措辞，不扩大为普遍因果。'}
,
 {id:'batch-012',status:'saved',chapters:['c04','c05'],newQuestionIds:[...Array.from({length:11},(_,i)=>'q-c04-'+String(i+44).padStart(3,'0')),...Array.from({length:39},(_,i)=>'q-c05-'+String(i+1).padStart(3,'0'))],reviewedPdfPages:[41,42,43,44,45,46,47,48,49],note:'连续补齐 50 个短段：第 4 章末 11 段和第 5 章前 39 段；原有 253 题不变。新增 25 个整段原页审阅记录，区分个人叙事、焦点小组、日记自报与诗歌，不扩大因果或研究范围。'}
,
 {id:'batch-013',status:'saved',chapters:['c05','c06'],newQuestionIds:[...Array.from({length:20},(_,i)=>'q-c05-'+String(i+40).padStart(3,'0')),...Array.from({length:5},(_,i)=>'q-c06-'+String(i+1).padStart(3,'0'))],reviewedPdfPages:[49,50,51,52,53,54],note:'连续补齐第 5 章末 20 段和第 6 章前 5 段；此前 303 题不变。新增 12 个整段原页审阅，区分个人经历、留学周报观察、回顾写作实验与讣告评分，不扩大因果和样本代表性。'}
,
 {id:'batch-014',status:'saved',chapter:'c06',newQuestionIds:Array.from({length:25},(_,i)=>'q-c06-'+String(i+6).padStart(3,'0')),reviewedPdfPages:[54,55,56,57],sourceNotes:'source/short-questions/batch014-source-notes.json',note:'第 6 章连续补齐 25 段；原有 328 题不变。新增 12 个完整原页审阅记录。保留《海峡时报》111、40、34.5% 等印文并标记无法一致换算，不猜分母或篡改英文；区分样本评分、文学假设与人格词汇史。'}
,
 {id:'batch-015',status:'saved',chapter:'c06',newQuestionIds:Array.from({length:25},(_,i)=>'q-c06-'+String(i+31).padStart(3,'0')),reviewedPdfPages:[58,59,60,61,62],note:'连续补齐第 6 章接下来的 25 个既有短段单元；此前 353 题不变。核对完整原页与跨页题项；区分自报、相关、作者双向关系解释和人物叙事；保留 .47 的非决定性及概率措辞。and so on 尾段保留既有稳定 ID，不冒充独立完整句。'}
,
 {id:'batch-016',status:'saved',chapter:'c06',newQuestionIds:Array.from({length:25},(_,i)=>'q-c06-'+String(i+56).padStart(3,'0')),reviewedPdfPages:[61,62,63,64,65],note:'第 6 章继续补齐 25 个单元；此前 378 题不变。逐页核对社交活动、幸福人格、Thunberg/Huckabee 例子；保留 potential、probably 及概率，区别节目角色、相关与人物推测。花生引语归于人物，不作实际难民风险证据。'}
,
 {id:'batch-017',status:'saved',chapters:['c06','c07'],newQuestionIds:[...Array.from({length:11},(_,i)=>'q-c06-'+String(i+81).padStart(3,'0')),...Array.from({length:14},(_,i)=>'q-c07-'+String(i+1).padStart(3,'0'))],reviewedPdfPages:[65,66,67,68,69],note:'补齐第6章末11个缺口和第7章前14个单元；此前403题不变。核对跨页结尾与开篇原页，保留概率、非决定性、研究样本和条件语气；句子补全不当成实际家务行为，人物特质不作临床诊断，竞技运动叙事不推广为普遍因果。'}
,
 {id:'batch-018',status:'saved',chapter:'c07',newQuestionIds:Array.from({length:25},(_,i)=>'q-c07-'+String(i+15).padStart(3,'0')),reviewedPdfPages:[69,70,71,72,73],note:'第7章连续补齐25个单元；此前428题不变。核对运动元分析、科学获奖者比较、Nietzsche引语、Sidis与球员叙事；区分关联和作者建议、文学比喻、up to上限与历史时点，以及Shaq反事实的两个可能结果。'}
,
 {id:'batch-019',status:'saved',chapter:'c07',newQuestionIds:Array.from({length:25},(_,i)=>'q-c07-'+String(i+40).padStart(3,'0')),reviewedPdfPages:[73,74,75,76,77],note:'第7章连续补齐25单元；此前453题不变。核对玩心记录随机干预、未测维度推测、49团队调查、教授及记者叙事、Moritz假设、运动多因素与电影例子；保留实测/未测、调查/因果、主观感受/总体及偶尔/永远的区别。'}
,
 {id:'batch-020',status:'saved',chapters:['c07','c08'],newQuestionIds:[...Array.from({length:8},(_,i)=>'q-c07-'+String(i+65).padStart(3,'0')),...Array.from({length:17},(_,i)=>'q-c08-'+String(i+1).padStart(3,'0'))],reviewedPdfPages:[77,78,79,80,81,82],note:'补齐第7章末8单元、第8章前17单元；此前478题不变。核对完整原页，保留个人反事实、近似转述、针厂估算、Ford时间限定和原书时点；区分团队产出与Kagan心理体验观点、Marx推测。书中AI描述不触发运行操作。'}
,
 {id:'batch-021',status:'saved',chapter:'c08',newQuestionIds:Array.from({length:25},(_,i)=>'q-c08-'+String(i+18).padStart(3,'0')),reviewedPdfPages:[81,82,83,84,85],note:'第8章连续补齐25个单元；此前503题不变。完整核对Marx跨页引述、Erikson观点、Kohn调查、线上组装、假想咨询及等待任务；保留理论/关联/实验/自报/预测/行为指标的区别，条件按团队分配不冒称随机，15对60为同人数团队基线。'}
];
const tasks={schemaVersion:1,pdfSha256:book.pdfSha256,extractionVersion:book.extractionVersion,batches,readingPlan:{units:readingPlan.units.length,includedCandidateSentences:flattened.length,duplicateSentenceIds:[],missingSentenceIds:[],remainingUnitIds:readingPlan.units.filter(u=>!u.questionId).map(u=>u.id),legacyArchive:'source/archive/questions-v1.json',currentQuestionVersion:2,completedSections:book.sections.filter(s=>readingPlan.units.filter(u=>u.sectionId===s.id).every(u=>u.questionId)).map(s=>s.id)},chapters:book.chapters.map(c=>({id:c.id,title:c.title,pdfPage:c.pdfPage,status:qs.some(q=>q.chapterId===c.id)?'partial':'not-authored',candidateSentences:book.sentences.filter(s=>s.chapterId===c.id).length,remainingReadingUnitIds:readingPlan.units.filter(u=>u.chapterId===c.id&&!u.questionId).map(u=>u.id),remainingProofreadIds:book.sentences.filter(s=>s.chapterId===c.id&&s.review!=='visual-proofread').map(s=>s.id),remainingEvidenceIds:book.sentences.filter(s=>s.chapterId===c.id&&!evidence.has(s.id)).map(s=>s.id),sections:book.sections.filter(s=>s.chapterId===c.id).map(s=>({id:s.id,title:s.title,status:qs.some(q=>q.sectionId===s.id)?'partial':'not-authored',questionIds:qs.filter(q=>q.sectionId===s.id).map(q=>q.id)}))})),nextBatch:{chapterId:readingPlan.units.find(u=>!u.questionId)?.chapterId,readingUnitId:readingPlan.units.find(u=>!u.questionId)?.id,action:'按全书短段顺序补齐尚无题目和中文材料的片段；原文完整纳入不等于全书题库完成。旧 v1 快照已归档，当前短段题为 v2。'},excluded:book.excluded};
await writeFile('source/content-tasks.json',JSON.stringify(tasks,null,2));
console.log(JSON.stringify({...report,byChapter:undefined},null,2));
