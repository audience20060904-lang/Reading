import {readFileSync} from 'node:fs';
import {describe,it,expect} from 'vitest';
import {getWordLookups} from '../src/wordLookups';
import {grade,emptyState,exportBackup,parseBackup} from '../src/core';
const read=(p:string)=>JSON.parse(readFileSync(p,'utf8')),catalog=read('src/data/question-revision-catalog.json'),baseline=read('source/question-revisions/review-017-baseline.json');
const q=(id:string)=>catalog.questions.find((v:any)=>v.id===id);
describe('第十七批：棒球与人生意义的词义边界',()=>{
 it('同一棒球片段译文一致，hits不泛化为球棒触球',()=>{
  const qs=['q-c01-025','qe-c01-0042','qe-c01-0043','qe-c01-0044','qe-c01-0045'].map(q);
  expect(new Set(qs.map(v=>v.translation)).size).toBe(1);expect(qs[0].translation).toContain('安打出现的频率');expect(qs[0].translation).toContain('打击率');expect(qs[0].translation).not.toContain('击中球');
 });
 it('两个位置的查词精确覆盖，不影响已有celibate修订',()=>{
  const corrections=read('src/data/word-lookup-revisions.json'),raw=read('src/data/word-lookups.json'),batch=corrections.updates.filter((r:any)=>r.revisionId==='question-review-2026-10-28-017');expect(batch).toHaveLength(2);
  for(const r of batch){const o=Object.values(raw.paragraphs).flat().find((o:any)=>o.id===r.occurrenceId) as any;expect(o.contextMeaning).toBe(r.baselineContextMeaning);const v=getWordLookups(o.paragraphId,o.text,o.start)[0];expect(v.text).toBe('batting average');expect(v.contextMeaning).toContain('安打');expect(v.start).toBe(o.start);expect(v.sentenceIds).toContain(r.sourceCandidateId);}
  const previous=corrections.updates.find((r:any)=>r.revisionId.endsWith('-014'));expect(getWordLookups('c01-s02-p010-05625','celibate',390)[0].contextMeaning).toBe(previous.contextMeaning);
 });
 it('人生point译为目的，分析不引用未显示的歌曲或条件',()=>{
  const v=q('q-c01-027');expect(v.translation).toContain('“目的”');expect(v.vocabulary[0].context).toContain('不是物理方向');expect(v.analyses[0]).not.toContain('when efforts');expect(v.analyses[1]).not.toContain('后面');
 });
 it('旧译文导出恢复后仍在旧快照中，新练习才使用新译文',()=>{
  const old=baseline.questions.find((v:any)=>v.id==='q-c01-025'),next=q(old.id),s=emptyState();s.attempts=[grade(old,old.answer,s,1000)];const saved=parseBackup(exportBackup(s));expect(saved.attempts[0].snapshot.translation).toContain('击球率');const retry=grade(next,next.answer,s,2000);expect(retry.snapshot.translation).toContain('打击率');expect(retry.fingerprint).not.toBe(saved.attempts[0].fingerprint);
 });
});
