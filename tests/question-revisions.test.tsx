import {describe,it,expect} from 'vitest';
import {readFileSync} from 'node:fs';
import {createHash} from 'node:crypto';
import {renderToStaticMarkup} from 'react-dom/server';
import {activeReading} from '../src/activeReading';
import {applyQuestionRevisions} from '../src/questionRevisions';
import {emptyState,exportBackup,grade,newSession,orderedQuestions,parseBackup,restoreReadingState,statistics} from '../src/core';
import {getPassageTranslation} from '../src/PassageTranslation';
import {getQuestionTranslation} from '../src/questionTranslations';
import AnswerExplanation from '../src/AnswerExplanation';
import type {Book,Question,ReadingPlan} from '../src/types';
const read=(p:string)=>JSON.parse(readFileSync(p,'utf8'));
const book=read('public/data/book.json') as Book,base=read('public/data/questions.json') as Question[],extras=read('public/data/evidence-questions.json') as Question[],originalPlan=read('public/data/reading-plan.json') as ReadingPlan,repair=read('src/data/sentence-repair-catalog.json'),catalog=read('src/data/question-revision-catalog.json'),frozen=read('source/question-revisions/review-001-baseline.json');
const before=[...base.map(q=>repair.questions.find((r:Question)=>r.id===q.id)??q),...extras] as Question[],active=activeReading(base,originalPlan,extras),qs=active.questions;
const canonical=(v:any):string=>Array.isArray(v)?'['+v.map(canonical).join(',')+']':v&&typeof v==='object'?'{'+Object.keys(v).sort().map(k=>JSON.stringify(k)+':'+canonical(v[k])).join(',')+'}':JSON.stringify(v);

describe('有版本记录的题目校对',()=>{
 it('12题升级版本，其余2697题及全部阅读单元和来源完全保留',()=>{
  expect(catalog.questions).toHaveLength(12);expect(qs).toHaveLength(2709);expect(new Set(qs.map(q=>q.id)).size).toBe(2709);
  for(const old of before){const q=qs.find(q=>q.id===old.id)!;if(!q.contentRevision){expect(q).toEqual(old);continue;}expect(old).toEqual(frozen.questions.find((x:Question)=>x.id===old.id));expect(q.version).toBe(old.version+1);expect(q.fingerprint).not.toBe(old.fingerprint);expect(q.answer).toBe(old.answer);expect(q.passage).toBe(old.passage);expect(q.evidence.map(e=>e.sentenceIds)).toEqual(old.evidence.map(e=>e.sentenceIds));for(const [i,e] of q.evidence.entries()){expect(q.passage).toContain(e.quote);expect(e.quote).toContain(old.evidence[i].quote);expect(e.sources).toEqual(old.evidence[i].sources);}expect(q.sentenceIds).toEqual(old.sentenceIds);expect(q.readingUnitId).toBe(old.readingUnitId);const {fingerprint,...content}=q;expect(createHash('sha256').update(canonical(content)).digest('hex')).toBe(fingerprint);}
  expect(orderedQuestions(qs,book).map(q=>q.id)).toEqual(orderedQuestions(before,book).map(q=>q.id));expect(active.plan.units.map(u=>u.id)).toEqual(originalPlan.units.map(u=>u.id));
 });
 it('修窗的新译文保留行动意向，旧快照仍呈现旧译文与旧选项',()=>{
  const old=before.find(q=>q.id==='q-c01-024')!,q=qs.find(q=>q.id===old.id)!;
  expect(getPassageTranslation(q)).toContain('激励我去修窗户');expect(getPassageTranslation(q)).not.toContain('修好了');expect(getPassageTranslation(old)).toContain('修好了');expect(getQuestionTranslation(q)?.options).toEqual(q.optionsZh);expect(getQuestionTranslation(old)?.options).not.toEqual(q.optionsZh);const tolstoy=qs.find(q=>q.id==='q-c01-028')!;expect(tolstoy.evidence[1].quote).toContain('a good wife who loved me');
 });
 it('已提交记录按旧快照恢复，统计不重算；重新练习才生成新版本记录',()=>{
  const old=before.find(q=>q.id==='q-c01-024')!,q=qs.find(q=>q.id===old.id)!,s=emptyState(),a=grade(old,0,s,1234);s.attempts=[a];s.readingLayoutVersion=2;s.readingUnitId=old.readingUnitId;s.session={...newSession(old),attemptId:a.id,selected:a.selected};
  const restored=restoreReadingState(parseBackup(exportBackup(s)),qs,active.plan);expect(restored.attempts).toEqual(s.attempts);expect(restored.session).toEqual(s.session);expect(statistics(restored)).toEqual(statistics(s));
  const retry=grade(q,q.answer,restored,2345);expect(retry.version).toBe(q.version);expect(retry.snapshot.options).toEqual(q.options);expect(a.snapshot.options).toEqual(old.options);expect(retry.attemptNumber).toBe(2);expect(retry.correct).toBe(true);
 });
 it('未提交的旧选择不误套新选项，同版的选择可刷新恢复',()=>{
  const old=before.find(q=>q.id==='q-c01-024')!,q=qs.find(q=>q.id===old.id)!,s=emptyState();s.readingLayoutVersion=2;s.readingUnitId=old.readingUnitId;s.session={...newSession(old),selected:2};
  const restored=restoreReadingState(s,qs,active.plan);expect(restored.session?.selected).toBeNull();expect(restored.session?.fingerprint).toBe(q.fingerprint);restored.session!.selected=1;expect(restoreReadingState(restored,qs,active.plan).session?.selected).toBe(1);expect(restored.attempts).toEqual([]);
 });
 it('提交前不显示新译文和解析；提交后显示匹配版本并去掉过期编校话语',()=>{
  for(const q of catalog.questions as Question[]){const props={question:q,favorites:[],onFavorite:()=>{}};expect(renderToStaticMarkup(<AnswerExplanation {...props}/>)).toBe('');const attempt=grade(q,q.answer,emptyState(),1234),html=renderToStaticMarkup(<AnswerExplanation {...props} attempt={attempt}/>);expect(html).toContain(q.promptZh);expect(html).not.toContain('下一批');expect(html).not.toContain('此历史版本的问题译文尚未整理');expect(html).not.toContain('此历史版本的选项译文尚未整理');for(const z of q.optionsZh!)expect(html).toContain(z);}
 });
 it('错误PDF或变化的基线拒绝套用校对，未知题目不被覆盖',()=>{
  expect(()=>applyQuestionRevisions(before,'wrong')).toThrow('来源');expect(()=>applyQuestionRevisions(before.map(q=>q.id==='q-c01-024'?{...q,fingerprint:'changed'}:q),book.pdfSha256)).toThrow('版本');const unknown={...base[0],id:'unknown'};expect(applyQuestionRevisions([unknown],book.pdfSha256)).toEqual([unknown]);
 });
});
