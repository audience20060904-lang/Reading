import {describe,it,expect} from 'vitest';
import {readFileSync} from 'node:fs';
import {renderToStaticMarkup} from 'react-dom/server';
import {activeReading} from '../src/activeReading';
import {evidenceHighlights,sliceHighlights} from '../src/evidenceHighlights';
import {groupedQuestionTypes} from '../src/questionTypes';
import {emptyState,grade,newSession,statistics} from '../src/core';
import ReadingPractice from '../src/ReadingPractice';
import WordText from '../src/WordLookup';
import type {Book,Question,ReadingPlan} from '../src/types';
const read=(p:string)=>JSON.parse(readFileSync(p,'utf8'));
const book=read('public/data/book.json') as Book,base=read('public/data/questions.json') as Question[],active=activeReading(base,read('public/data/reading-plan.json') as ReadingPlan,read('public/data/evidence-questions.json'));
const text=(html:string)=>html.replace(/<[^>]*>/g,'').replace(/&amp;/g,'&').replace(/&quot;/g,'"').replace(/&#x27;/g,"'").replace(/&lt;/g,'<').replace(/&gt;/g,'>');
describe('提交后证据定位与清晰统计',()=>{
 it('证据只在提交后标记，整段译文仍在最后且原文只有一份',()=>{
  const q=active.questions[0],s=emptyState();s.readingUnitId=q.readingUnitId;s.session=newSession(q);const props={book,questions:active.questions,plan:active.plan,state:s,question:q,busy:false,onUnit:()=>{},onSelect:()=>{},onSubmit:()=>{},onChat:()=>{},onSource:()=>{},onFavorite:()=>{},onMark:()=>{},onRetry:()=>{}};
  const before=renderToStaticMarkup(<ReadingPractice {...props}/>);expect(before).not.toContain('evidence-highlight');expect(before).not.toContain('金色标记');
  const after=renderToStaticMarkup(<ReadingPractice {...props} attempt={grade(q,q.answer,s,1234)}/>);expect(after).toContain('evidence-highlight');expect(after).toContain('金色标记');expect([...after.matchAll(/class="passage"/g)]).toHaveLength(1);expect(after.indexOf('二、重点词汇')).toBeLessThan(after.indexOf('三、原文整段参考译文'));
 });
 it('标记原文不影响可查词按钮及任何字符，支持部分词内高亮',()=>{
  const p=book.paragraphs[0],q=active.questions[0],ranges=evidenceHighlights(q,book);expect(ranges).toEqual([{start:0,end:q.passage.length}]);
  for(const marked of [ranges,[{start:105,end:108}]]){const html=renderToStaticMarkup(<WordText paragraphId={p.id} text={q.passage} start={0} highlights={marked}/>);expect(text(html)).toBe(q.passage);expect([...html.matchAll(/aria-label="查词 clementines"/g)]).toHaveLength(1);expect(html).toContain('evidence-highlight');}
 });
 it('所有题的高亮范围非空、连续合法且不互相重叠',()=>{
  for(const q of active.questions){const ranges=evidenceHighlights(q,book);for(const [i,r] of ranges.entries()){expect(r.start,q.id).toBeGreaterThanOrEqual(0);expect(r.end,q.id).toBeLessThanOrEqual(q.passage.length);expect(r.end,q.id).toBeGreaterThan(r.start);if(i)expect(r.start,q.id).toBeGreaterThan(ranges[i-1].end);}}
 });
 it('跨源片段高亮裁切后不重复字符，合并重叠证据',()=>{
  const q=active.questions.find(q=>q.id==='q-c11-062')!,ranges=evidenceHighlights({...q,evidence:[...q.evidence,...q.evidence]},book);let offset=0,joined='';for(const s of q.sourceSegments!){offset+=s.separator.length;const marked=sliceHighlights(ranges,offset,s.text.length),html=renderToStaticMarkup(<WordText paragraphId={s.paragraphId} text={s.text} start={s.start} highlights={marked}/>);joined+=s.separator+text(html);offset+=s.text.length;}expect(joined).toBe(q.passage);
 });
 it('重复片段按来源句定位；同一句内部仍有歧义时不猜位置',()=>{
  const q={...base[0],paragraphId:'p',sentenceIds:['s1','s2'],passage:'same same',evidence:[{...base[0].evidence[0],quote:'same',sentenceIds:['s2']}]} as Question,b={...book,paragraphs:[{...book.paragraphs[0],id:'p',text:q.passage}],sentences:[{...book.sentences[0],id:'s1',paragraphId:'p',start:0,end:4},{...book.sentences[0],id:'s2',paragraphId:'p',start:5,end:9}]} as Book;
  expect(evidenceHighlights(q,b)).toEqual([{start:5,end:9}]);expect(evidenceHighlights({...q,evidence:[{...q.evidence[0],sentenceIds:['s1','s2']}]},b)).toEqual([]);
 });
 it('题型归组用次数加权，不平均两个正确率且不改原标签',()=>{
  const raw={'语境词义':{total:2,correct:1,rate:.5},'语境含义':{total:8,correct:2,rate:.25},'未知新题型':{total:1,correct:1,rate:1}},before=JSON.stringify(raw),group=groupedQuestionTypes(raw);expect(group['语境词义']).toEqual({total:10,correct:3,rate:.3});expect(group['未知新题型']).toEqual(raw['未知新题型']);expect(JSON.stringify(raw)).toBe(before);
 });
 it('全库现有36个题型归为8组，统计次数与原始历史一致',()=>{
  const raw:Record<string,{total:number;correct:number;rate:number}>={};for(const q of active.questions){const v=raw[q.type]??={total:0,correct:0,rate:0};v.total++;}expect(Object.keys(raw)).toHaveLength(36);const groups=groupedQuestionTypes(raw);expect(Object.keys(groups)).toHaveLength(8);expect(Object.values(groups).reduce((n,v)=>n+v.total,0)).toBe(2709);
  const state=emptyState(),q=active.questions.find(q=>q.type==='语境词义')!;state.attempts=[grade(q,q.answer,state,1234)];const saved=JSON.stringify(state),stats=statistics(state);groupedQuestionTypes(stats.byType);expect(JSON.stringify(state)).toBe(saved);expect(Object.keys(stats.byType)).toEqual([q.type]);
 });
});
