import {describe,it,expect} from 'vitest';
import {readFileSync} from 'node:fs';
import {renderToStaticMarkup} from 'react-dom/server';
import type {Book,Question,ReadingPlan} from '../src/types';
import {emptyState,exportBackup,grade,parseBackup,restoreReadingState,restoreSession,statistics,studySummary} from '../src/core';
import AnswerExplanation from '../src/AnswerExplanation';
import {getQuestionTranslation} from '../src/questionTranslations';
const book=JSON.parse(readFileSync('public/data/book.json','utf8')) as Book;
const qs=JSON.parse(readFileSync('public/data/questions.json','utf8')) as Question[];
const plan=JSON.parse(readFileSync('public/data/reading-plan.json','utf8')) as ReadingPlan;
const legacy=JSON.parse(readFileSync('source/archive/questions-v1.json','utf8')) as Question[];
describe('全书连续短段',()=>{
 it('全书每个候选句恰好出现一次，顺序与来源完全一致',()=>{
  const ids=plan.units.flatMap(u=>u.sentenceIds);expect(ids).toEqual(book.sentences.map(s=>s.id));expect(new Set(ids).size).toBe(ids.length);
  expect(plan.coverage.missingSentenceIds).toEqual([]);expect(plan.coverage.duplicateSentenceIds).toEqual([]);
 });
 it('短段不改写英语、不截断原句，长度受限且可追溯到同一段落',()=>{
  for(const u of plan.units){const p=book.paragraphs.find(p=>p.id===u.paragraphId)!,ss=u.sentenceIds.map(id=>book.sentences.find(s=>s.id===id)!);expect(ss.every(s=>s.paragraphId===p.id)).toBe(true);const text=p.text.slice(ss[0].start,ss.at(-1)!.end);expect(text.trim().split(/\s+/).length).toBe(u.wordCount);expect(u.wordCount).toBeLessThanOrEqual(110);}
  expect(plan.coverage.over90Words.length).toBe(4);
 });
 it('前两题和所有当前题目的原句均无重叠',()=>{
  expect(qs[0].sentenceIds.some(id=>qs[1].sentenceIds.includes(id))).toBe(false);
  const ids=qs.flatMap(q=>q.sentenceIds);expect(new Set(ids).size).toBe(ids.length);
  for(const q of qs)expect(plan.units.find(u=>u.id===q.readingUnitId)?.sentenceIds).toEqual(q.sentenceIds);
 });
 it('开篇第一小节的每个短段都已配有题目和完整中文材料',()=>{
  const units=plan.units.filter(u=>u.sectionId==='c01-s01');expect(units.length).toBeGreaterThan(5);expect(units.every(u=>u.questionId)).toBe(true);
  for(const u of units){const q=qs.find(q=>q.id===u.questionId)!;expect(q.translation).toMatch(/[\u4e00-\u9fff]/);expect(getQuestionTranslation(q)).toBeDefined();}
 });
 it('导入短段与题目不一致的位置时，重置选择，防止给另一道题计分',()=>{
  const s=emptyState();s.readingLayoutVersion=2;s.readingUnitId=qs[1].readingUnitId;s.session={questionId:qs[0].id,attemptId:null,selected:1,startedAt:1,elapsedBefore:0};const fixed=restoreReadingState(s,qs,plan);expect(fixed.session?.questionId).toBe(qs[1].id);expect(fixed.session?.selected).toBeNull();
 });
 it('原文全包含与配题全完成分开，待补充片段不伪造成题目',()=>{
  expect(plan.coverage.allSentencesIncluded).toBe(true);expect(plan.coverage.allQuestionsPrepared).toBe(false);
  expect(plan.units.filter(u=>u.questionId).length).toBe(qs.length);expect(plan.units.filter(u=>!u.questionId).length).toBe(plan.coverage.unitsWithoutQuestions);
 });
 it('无题短段的位置可持久化与备份恢复，不产生或恢复虚假作答',()=>{
  const s=emptyState();s.readingUnitId=plan.units.find(u=>!u.questionId)!.id;s.session=null;
  expect(restoreSession(parseBackup(exportBackup(s)),qs)).toEqual(s);expect(statistics(s).total).toBe(0);
  expect(studySummary(s,book,qs,plan)).toContain(s.readingUnitId);expect(()=>parseBackup(exportBackup({...s,readingUnitId:44 as unknown as string}))).toThrow();
 });
 it('首次升级进入新版短段，不复用旧版答案；全部历史成绩保持原样',()=>{
  const s=emptyState(),old=legacy[0];s.attempts=[grade(old,old.answer,s,100)];s.session={questionId:old.id,attemptId:s.attempts[0].id,selected:old.answer,elapsedBefore:0,startedAt:1};const before=JSON.stringify(s.attempts);
  const migrated=restoreReadingState(s,qs,plan);expect(migrated.session?.attemptId).toBeNull();expect(migrated.session?.selected).toBeNull();expect(migrated.readingUnitId).toBe(qs[0].readingUnitId);expect(JSON.stringify(migrated.attempts)).toBe(before);
 });
 it('升级后主动回看旧解析并刷新，继续保留该历史会话',()=>{
  const s=emptyState(),old=legacy[0];s.attempts=[grade(old,old.answer,s,100)];s.readingLayoutVersion=2;s.readingUnitId=qs[0].readingUnitId;s.session={questionId:old.id,attemptId:s.attempts[0].id,selected:old.answer,elapsedBefore:0,startedAt:1};expect(restoreReadingState(s,qs,plan)).toEqual(s);
 });
 it('短段 v2 记录和旧 v1 快照独立，旧答案与版本完整保留',()=>{
  const s=emptyState(),old=legacy[0];s.attempts=[grade(old,old.answer,s,123)];s.session={questionId:old.id,attemptId:s.attempts[0].id,selected:old.answer,elapsedBefore:0,startedAt:1};
  const restored=restoreSession(parseBackup(exportBackup(s)),qs);expect(restored.attempts[0].snapshot).toEqual(old);expect(restored.attempts[0].version).toBe(1);expect(qs[0].version).toBe(2);expect(statistics(restored).correct).toBe(1);
 });
});
describe('只保留选项分析、词汇和整段译文',()=>{
 it('所有题目均有与英文和选项顺序完全匹配的中文译文',()=>{for(const q of qs){const t=getQuestionTranslation(q);expect(t?.prompt,q.id).toMatch(/[\u4e00-\u9fff]/);expect(t?.options).toHaveLength(4);expect(t?.options.every(v=>/[\u4e00-\u9fff]/.test(v))).toBe(true);}});
 it('未提交时不渲染任何中文题目、选项翻译或答案解析',()=>{expect(renderToStaticMarkup(<AnswerExplanation question={qs[0]} favorites={[]} onFavorite={()=>{}}/>)).toBe('');});
 it('提交后仅三类解析，包含问题和四项翻译，译文在最后',()=>{
  const q=qs[0],html=renderToStaticMarkup(<AnswerExplanation question={q} attempt={grade(q,q.answer,emptyState(),4)} favorites={[]} onFavorite={()=>{}}/>);
  expect([...html.matchAll(/<h3>(.*?)<\/h3>/g)].map(m=>m[1])).toEqual(['一、问题与选项分析','二、重点词汇','三、原文整段参考译文']);
  const t=getQuestionTranslation(q)!;expect(html).toContain(t.prompt);for(const v of t.options)expect(html).toContain(v);
  expect(html).not.toContain('语法解析');expect(html).not.toContain('IELTS 阅读技巧');expect(html).not.toContain('一、原文理解');expect(html.lastIndexOf('passage-translation')).toBeGreaterThan(html.lastIndexOf('vocab-grid'));
 });
 it('英文题目或选项变动后，不套用不匹配的旧译文',()=>{expect(getQuestionTranslation({...qs[0],prompt:'Changed'})).toBeUndefined();expect(getQuestionTranslation({...qs[0],options:[...qs[0].options].reverse() as Question['options']})).toBeUndefined();});
});
