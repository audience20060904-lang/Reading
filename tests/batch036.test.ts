import {describe,it,expect} from 'vitest';
import {readFileSync} from 'node:fs';
import {createHash} from 'node:crypto';
import baseline from './fixtures/batch035-fingerprints.json';
import type {Book,Question,ReadingPlan} from '../src/types';
import {emptyState,grade,exportBackup,parseBackup,restoreReadingState,statistics,assertCoverageClaim} from '../src/core';
import {getQuestionTranslation} from '../src/questionTranslations';
const read=(p:string)=>JSON.parse(readFileSync(p,'utf8'));
const b=read('public/data/book.json') as Book,qs=read('public/data/questions.json') as Question[],plan=read('public/data/reading-plan.json') as ReadingPlan;
const targets=read('source/short-questions/batch036-targets.json').targets as {questionId:string;readingUnitId:string;passageSha256:string}[];
const hash=(s:string)=>createHash('sha256').update(s).digest('hex');
const q=(id:string)=>qs.find(q=>q.id===id)!;
describe('批次036连续25单元',()=>{
 it('保留此前878题的全部内容指纹',()=>{
  expect(Object.keys(baseline)).toHaveLength(878);
  for(const [id,fp] of Object.entries(baseline))expect(q(id)?.fingerprint,id).toBe(fp);
 });
 it('按顺序补齐25个缺口并保持来源原句及双语材料',()=>{
  const pending=plan.units.filter(u=>!u.questionId||!(u.questionId in baseline));
  expect(targets).toHaveLength(25);expect(pending.slice(0,25).map(u=>u.id)).toEqual(targets.map(t=>t.readingUnitId));
  expect(targets[0].questionId).toBe('q-c12-065');expect(targets.at(-1)?.questionId).toBe('q-c13-023');
  for(const t of targets){const a=q(t.questionId);expect(a.readingUnitId).toBe(t.readingUnitId);expect(hash(a.passage)).toBe(t.passageSha256);expect(a.translation).toMatch(/[\u4e00-\u9fff]/);expect(getQuestionTranslation(a)?.options).toHaveLength(4);expect(a.analyses).toHaveLength(4);expect(a.vocabulary.length).toBeGreaterThan(0);}
 });
 it('原页审阅、证据句子范围与PDF页码吻合',()=>{
  const reviews=read('source/short-questions/review-chapter12-13-moving25.json');expect(reviews.questionIds).toEqual(targets.map(t=>t.questionId));expect(reviews.checkedPdfPages).toEqual([142, 143, 144, 145, 146, 147]);
  for(const t of targets){const a=q(t.questionId),p=b.paragraphs.find(p=>p.id===a.paragraphId)!;
   expect(reviews.paragraphs.find((r:any)=>r.id===p.id)?.textSha256).toBe(hash(p.text));
   for(const id of a.sentenceIds)expect(b.sentences.find(s=>s.id===id)?.review).toBe('visual-proofread');
   for(const e of a.evidence){const start=p.text.indexOf(a.passage)+a.passage.indexOf(e.quote),end=start+e.quote.length;expect(e.sentenceIds).toEqual(a.sentenceIds.filter(id=>{const s=b.sentences.find(s=>s.id===id)!;return s.start<end&&s.end>start;}));for(const r of e.sources)expect(reviews.checkedPdfPages).toContain(r.pdfPage);}
  }
 });
 it('记录本批903已配/150待办的历史快照并拒绝虚假全覆盖',()=>{
  const c=read('public/data/coverage.json'),tasks=read('source/content-tasks.json'),ids=new Set([...Object.keys(baseline),...targets.map(t=>t.questionId)]);
  expect(qs.filter(a=>ids.has(a.id))).toHaveLength(903);expect(plan.units.filter(u=>!u.questionId||!ids.has(u.questionId))).toHaveLength(150);expect(c.fullCoverage).toBe(false);expect(c.contextOnlySentences).toBeGreaterThan(0);expect(c.notDirectlyQuestioned).toBeGreaterThan(0);
  expect(tasks.readingPlan.remainingUnitIds).toEqual(plan.units.filter(u=>!u.questionId).map(u=>u.id));expect(tasks.nextBatch.readingUnitId).toBe(tasks.readingPlan.remainingUnitIds[0]);
 });
 it('追加后仍能导出、导入和恢复之前的成绩、指纹及位置',()=>{
  const a=q('q-c12-064'),s=emptyState();s.readingLayoutVersion=2;s.readingUnitId=a.readingUnitId;s.attempts=[grade(a,a.answer,s,1200)];s.session={questionId:a.id,attemptId:s.attempts[0].id,selected:a.answer,startedAt:1,elapsedBefore:0};
  const restored=restoreReadingState(parseBackup(exportBackup(s)),qs,plan);expect(restored).toEqual(s);expect(restored.attempts[0].fingerprint).toBe(baseline['q-c12-064']);expect(statistics(restored).correct).toBe(1);
 });
 it('保留来信性质、跨页同句及额外正文审计缺口',()=>{
  const notes=read('source/short-questions/batch036-source-notes.json');expect(notes.crossPageContinuation.questionIds).toEqual(['q-c13-018','q-c13-019']);
  expect(q('q-c13-018').passage).toMatch(/Once we$/);expect(q('q-c13-019').passage).toMatch(/^actually lived/);expect(q('q-c13-019').options[q('q-c13-019').answer]).toContain('Four years in one house');
  expect(q('q-c13-006').analyses.join('')).toContain('个人经历');expect(q('q-c13-015').passage).toContain('not a clinical psychologist');expect(q('q-c13-016').passage).toContain('might be able');
  const a=read('source/content-audit-tasks.json'),c=read('public/data/coverage.json'),snapshot=read('source/releases/batch-036.json').coverage;expect(a.tasks.find((t:any)=>t.id==='audit-c13-opening-p144-b005').text).toContain('Before reaching the book’s conclusion');expect(snapshot.sourceAudit.knownPendingBodyBlocks).toBe(1);expect(c.sourceAudit.knownPendingBodyBlocks).toBe(a.tasks.filter((t:any)=>t.status==='pending-body-inclusion').length);if(c.sourceAudit.pendingTaskIds.length)expect(c.notice).toContain('不能当作全书完整分段');expect(c.fullCoverage).toBe(false);
  expect(()=>assertCoverageClaim({...c,notDirectlyQuestioned:0,proofreadSentences:c.candidateSentences,sourceAudit:{...c.sourceAudit,pendingTaskIds:['unresolved-source-gap']}},true)).toThrow('虚假全覆盖');
 });
});
