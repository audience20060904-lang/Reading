import {readFileSync} from 'node:fs';
import {describe,it,expect} from 'vitest';
import {getWordLookups} from '../src/wordLookups';
import {grade,emptyState,exportBackup,parseBackup} from '../src/core';
import {validateRevisionVocabulary} from '../scripts/validate-revision-vocabulary.mjs';
const read=(p:string)=>JSON.parse(readFileSync(p,'utf8')),catalog=read('src/data/question-revision-catalog.json'),baseline=read('source/question-revisions/review-014-baseline.json');
const q=(id:string)=>catalog.questions.find((v:any)=>v.id===id);
describe('第十四批：性禁欲的语境义和旧版保留',()=>{
 it('拒绝缺少例句、搭配或释义的词汇修订',()=>{
  const v=q('qe-c01-0025').vocabulary[0];expect(()=>validateRevisionVocabulary([v])).not.toThrow();
  expect(()=>validateRevisionVocabulary([{...v,example:''}])).toThrow('incomplete');
  expect(()=>validateRevisionVocabulary([{...v,meaning:''}])).toThrow('incomplete');
  expect(()=>validateRevisionVocabulary([{...v,collocations:[]}])).toThrow('incomplete');
 });
 it('三题同段译文一致，celibate不等于未婚',()=>{
  const qs=['q-c01-017','qe-c01-0024','qe-c01-0025'].map(q);
  expect(new Set(qs.map(v=>v.translation)).size).toBe(1);
  for(const v of qs){expect(v.translation).toContain('三十五年没有性生活');expect(v.translation).not.toContain('三十五年保持独身');}
  expect(q('qe-c01-0025').vocabulary[0].meaning).toBe('不发生性关系的；禁欲的');
 });
 it('查词修订只覆盖目标位置的释义，词形、偏移和原始词库保留',()=>{
  const corrections=read('src/data/word-lookup-revisions.json'),raw=read('src/data/word-lookups.json');
  for(const r of corrections.updates.filter((r:any)=>r.revisionId==='question-review-2026-10-28-014')){const o=Object.values(raw.paragraphs).flat().find((o:any)=>o.id===r.occurrenceId) as any;expect(o.contextMeaning).toBe(r.baselineContextMeaning);const word=getWordLookups(o.paragraphId,o.text,o.start)[0];expect(word.contextMeaning).toBe(r.contextMeaning);expect(word.start).toBe(o.start);expect(word.end).toBe(o.end);expect(word.text).toBe('celibate');expect(word.sentenceIds).toContain(r.sourceCandidateId);}
 });
 it('新旧题目快照及词汇可分别备份，不改写历史译义',()=>{
  const old=baseline.questions.find((v:any)=>v.id==='qe-c01-0025'),next=q(old.id),s=emptyState();
  s.attempts=[grade(old,old.answer,s,1000)];const saved=parseBackup(exportBackup(s));
  expect(saved.attempts[0].snapshot.vocabulary[0].meaning).toContain('独身');
  expect(saved.attempts[0].snapshot.translation).toContain('保持独身');
  const retry=grade(next,next.answer,s,2000);expect(retry.snapshot.vocabulary[0].meaning).toBe('不发生性关系的；禁欲的');expect(retry.attemptNumber).toBe(2);expect(retry.fingerprint).not.toBe(saved.attempts[0].fingerprint);
 });
});
