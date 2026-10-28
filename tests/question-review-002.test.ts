import {describe,it,expect} from 'vitest';
import {readFileSync,writeFileSync,mkdtempSync,mkdirSync,rmSync} from 'node:fs';
import {tmpdir} from 'node:os';
import {resolve,sep,dirname,join} from 'node:path';
import {execFileSync} from 'node:child_process';
const read=(p:string)=>JSON.parse(readFileSync(p,'utf8'));
const catalog=read('src/data/question-revision-catalog.json'),first=read('source/releases/question-review-001.json'),draft=read('source/question-revisions/review-002.json');

describe('第二批语义校对及追加批次保护',()=>{
 it('首批12题的完整发布指纹不变，追加15题且题目总数不变',()=>{
  expect(catalog.batches.length).toBeGreaterThanOrEqual(2);expect(draft.questions).toHaveLength(15);
  for(const [id,fingerprint] of Object.entries(first.questionFingerprints))expect(catalog.batches[0].questionFingerprints[id]).toBe(fingerprint);
  expect(catalog.questions.filter((q:any)=>q.contentRevision===draft.id)).toHaveLength(15);
  expect(read('public/data/questions.json').length+read('public/data/evidence-questions.json').length).toBe(2709);
 });
 it('保留可能性、相关与伴随关系，不把or翻成必须同时具备',()=>{
  const q=(id:string)=>catalog.questions.find((q:any)=>q.id===id);
  expect(q('q-c03-003').options[q('q-c03-003').answer]).not.toContain('must');
  expect(q('q-c03-027').options[0]).toContain('correlations');expect(q('q-c03-027').options[0]).not.toContain('agreement');
  expect(q('q-c03-034').options[3]).toContain('associated');expect(q('q-c03-018').translation).toContain('容易遭遇失败');
  expect(q('q-c03-032').translation).toContain('或不那么容易');expect(q('q-c03-037').analyses[1]).toContain('假设人物');
 });
 it('同一题可以在后续新批次再次升版，但不能改写先前已发布批次',()=>{
  const root=resolve(mkdtempSync(join(tmpdir(),'reading-review-compiler-'))),script=resolve('scripts/compile-question-revisions.mjs'),book=read('public/data/book.json'),old=read('source/question-revisions/review-002-baseline.json').questions[0];
  const put=(p:string,v:unknown)=>{const path=join(root,p);mkdirSync(dirname(path),{recursive:true});writeFileSync(path,JSON.stringify(v));};
  const run=()=>execFileSync(process.execPath,[script],{cwd:root,encoding:'utf8',stdio:'pipe'});
  const entry=(id:string)=>({id,author:id+'.json',baseline:id+'-base.json',receipt:id+'-receipt.json'});
  const a=entry('one'),b=entry('two');
  try{
   put('public/data/book.json',{pdfSha256:book.pdfSha256});put('public/data/questions.json',[old]);put('public/data/evidence-questions.json',[]);put('src/data/sentence-repair-catalog.json',{questions:[]});put('src/data/question-translations.json',{entries:[{questionId:old.id,prompt:old.prompt,options:old.options,promptZh:'问题译文',optionsZh:['甲','乙','丙','丁']}]});
   put('source/question-revisions/manifest.json',{schemaVersion:1,batches:[a]});const one={id:a.id,pdfSha256:book.pdfSha256,questions:[{id:old.id,reason:'第一次校对',updates:{translation:'第一版译文'}}]};put(a.author,one);put(a.baseline,{pdfSha256:book.pdfSha256,questions:[old]});run();
   const firstCompiled=JSON.parse(readFileSync(join(root,'src/data/question-revision-catalog.json'),'utf8')).questions[0];put(a.receipt,{status:'published-and-verified',questionFingerprints:{[old.id]:firstCompiled.fingerprint}});
   put('source/question-revisions/manifest.json',{schemaVersion:1,batches:[a,b]});put(b.author,{id:b.id,pdfSha256:book.pdfSha256,questions:[{id:old.id,reason:'第二次校对',updates:{translation:'第二版译文'}}]});put(b.baseline,{pdfSha256:book.pdfSha256,questions:[firstCompiled]});run();
   const result=JSON.parse(readFileSync(join(root,'src/data/question-revision-catalog.json'),'utf8'));expect(result.questions[0].version).toBe(old.version+2);expect(result.revisionDepths[old.id]).toBe(2);expect(result.baselineFingerprints[old.id]).toBe(old.fingerprint);expect(result.batches[0].questionFingerprints[old.id]).toBe(firstCompiled.fingerprint);
   one.questions[0].updates.translation='悄悄改写已发布版本';put(a.author,one);expect(run).toThrow();
  }finally{const allowed=resolve(tmpdir())+sep;expect(root.startsWith(allowed)&&root.includes('reading-review-compiler-')).toBe(true);if(root.startsWith(allowed)&&root.includes('reading-review-compiler-'))rmSync(root,{recursive:true,force:true});}
 });
});
