import {originalReadingPool} from './original-reading-pool';
import {describe,it,expect} from 'vitest';
import {readFileSync} from 'node:fs';
import {createHash} from 'node:crypto';
import baseline from './fixtures/batch024-fingerprints.json';
import type {Book,Question,ReadingPlan} from '../src/types';
import {emptyState,grade,exportBackup,parseBackup,restoreReadingState,statistics} from '../src/core';
import {getQuestionTranslation} from '../src/questionTranslations';
const read=(p:string)=>JSON.parse(readFileSync(p,'utf8'));
const b=read('public/data/book.json') as Book,qs=read('public/data/questions.json') as Question[],plan=originalReadingPool(read('public/data/reading-plan.json') as ReadingPlan);
const targets=read('source/short-questions/batch025-targets.json').targets as {questionId:string;readingUnitId:string;passageSha256:string}[];
const hash=(s:string)=>createHash('sha256').update(s).digest('hex');
const q=(id:string)=>qs.find(q=>q.id===id)!;
describe('批次025连续25单元',()=>{
 it('保留此前603题的全部内容指纹',()=>{
  expect(Object.keys(baseline)).toHaveLength(603);
  for(const [id,fp] of Object.entries(baseline))expect(q(id)?.fingerprint,id).toBe(fp);
 });
 it('按顺序补齐25个缺口并保持来源原句及双语材料',()=>{
  const pending=plan.units.filter(u=>!u.questionId||!(u.questionId in baseline));
  expect(targets).toHaveLength(25);expect(pending.slice(0,25).map(u=>u.id)).toEqual(targets.map(t=>t.readingUnitId));
  expect(targets[0].questionId).toBe('q-c09-057');expect(targets.at(-1)?.questionId).toBe('q-c09-081');
  for(const t of targets){const a=q(t.questionId);expect(a.readingUnitId).toBe(t.readingUnitId);expect(hash(a.passage)).toBe(t.passageSha256);expect(a.translation).toMatch(/[\u4e00-\u9fff]/);expect(getQuestionTranslation(a)?.options).toHaveLength(4);expect(a.analyses).toHaveLength(4);expect(a.vocabulary.length).toBeGreaterThan(0);}
 });
 it('原页审阅、证据句子范围与PDF页码吻合',()=>{
  const reviews=read('source/short-questions/review-chapter09-figures-sports25.json');expect(reviews.questionIds).toEqual(targets.map(t=>t.questionId));expect(reviews.checkedPdfPages).toEqual([98, 99, 100, 101, 102]);
  for(const t of targets){const a=q(t.questionId),p=b.paragraphs.find(p=>p.id===a.paragraphId)!;
   expect(reviews.paragraphs.find((r:any)=>r.id===p.id)?.textSha256).toBe(hash(p.text));
   for(const id of a.sentenceIds)expect(b.sentences.find(s=>s.id===id)?.review).toBe('visual-proofread');
   for(const e of a.evidence){const start=p.text.indexOf(a.passage)+a.passage.indexOf(e.quote),end=start+e.quote.length;expect(e.sentenceIds).toEqual(a.sentenceIds.filter(id=>{const s=b.sentences.find(s=>s.id===id)!;return s.start<end&&s.end>start;}));for(const r of e.sources)expect(reviews.checkedPdfPages).toContain(r.pdfPage);}
  }
 });
 it('记录本批628已配/425待办的历史快照并拒绝虚假全覆盖',()=>{
  const c=read('public/data/coverage.json'),tasks=read('source/content-tasks.json'),ids=new Set([...Object.keys(baseline),...targets.map(t=>t.questionId)]);
  expect(qs.filter(a=>ids.has(a.id))).toHaveLength(628);expect(plan.units.filter(u=>!u.questionId||!ids.has(u.questionId))).toHaveLength(425);expect(c.fullCoverage).toBe(false);expect(c.contextOnlySentences).toBe(c.contextSentences-c.evidenceSentences);expect(read('source/releases/batch-025.json').coverage.contextOnlySentences).toBeGreaterThan(0);expect(c.notDirectlyQuestioned).toBe(c.candidateSentences-c.evidenceSentences);expect(read('source/releases/batch-025.json').coverage.notDirectlyQuestioned).toBeGreaterThan(0);
  expect(tasks.readingPlan.remainingUnitIds).toEqual(plan.units.filter(u=>!u.questionId).map(u=>u.id));expect(tasks.nextBatch.readingUnitId).toBe(tasks.readingPlan.remainingUnitIds[0]);
 });
 it('追加后仍能导出、导入和恢复之前的成绩、指纹及位置',()=>{
  const a=q('q-c09-056'),s=emptyState();s.readingLayoutVersion=2;s.readingUnitId=a.readingUnitId;s.attempts=[grade(a,a.answer,s,1200)];s.session={questionId:a.id,attemptId:s.attempts[0].id,selected:a.answer,startedAt:1,elapsedBefore:0};
  const restored=restoreReadingState(parseBackup(exportBackup(s)),qs,plan);expect(restored).toEqual(s);expect(restored.attempts[0].fingerprint).toBe(baseline['q-c09-056']);expect(statistics(restored).correct).toBe(1);
 });
 it('守住实验过程解释、心情与丰富、比赛预期和文学条件的边界',()=>{
  expect(q('q-c09-062').passage).toContain('Perhaps');expect(q('q-c09-062').analyses.join(' ')).toContain('非已测得');
  expect(q('q-c09-063').passage).toContain('as happy as');expect(q('q-c09-063').analyses.join(' ')).toContain('完全没有情绪');
  expect(q('q-c09-069').analyses.join(' ')).toContain('本句尚未给最终结果');
  expect(q('q-c09-071').passage).toContain('tied at 2 to 2');
  expect(q('q-c09-078').passage).toContain('under the right circumstances');
  expect(q('q-c09-079').analyses.join(' ')).toContain('不是天文学证据');expect(q('q-c09-081').analyses.join(' ')).toContain('真实穿越时间');
 });
});
