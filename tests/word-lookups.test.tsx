import {describe,it,expect} from 'vitest';
import {readFileSync} from 'node:fs';
import {renderToStaticMarkup} from 'react-dom/server';
import type {Book,Question,ReadingPlan} from '../src/types';
import {emptyState,grade} from '../src/core';
import WordText from '../src/WordLookup';
import ReadingPractice from '../src/ReadingPractice';
import {getWordLookups} from '../src/wordLookups';
import catalog from '../src/data/word-lookups.json';
import baseline from './fixtures/word-lookups-v1.json';
import previous from './fixtures/word-lookups-v2.json';
import lastRelease from './fixtures/word-lookups-v3.json';
import expansion from '../source/b2-vocabulary/author-notes.json';
const read=(path:string)=>JSON.parse(readFileSync(path,'utf8'));
const book=read('public/data/book.json') as Book,qs=read('public/data/questions.json') as Question[],plan=read('public/data/reading-plan.json') as ReadingPlan;
const occurrences=Object.values(catalog.paragraphs).flat();
const textContent=(html:string)=>html.replace(/<[^>]*>/g,'').replace(/&amp;/g,'&').replace(/&quot;/g,'"').replace(/&#x27;/g,"'").replace(/&lt;/g,'<').replace(/&gt;/g,'>');

describe('针对具体原文的离线查词',()=>{
 it('每个标注都对应真实原文字符、稳定位置和所属句子',()=>{
  expect(occurrences).toHaveLength(4589);expect(new Set(occurrences.map(o=>o.id)).size).toBe(4589);
  for(const o of occurrences){const p=book.paragraphs.find(p=>p.id===o.paragraphId)!;expect(p.text.slice(o.start,o.end),o.id).toBe(o.text);expect(o.sentenceIds).toEqual(book.sentences.filter(s=>s.paragraphId===p.id&&s.start<o.end&&s.end>o.start).map(s=>s.id));}
 });
 it('仅预先选择的难词、熟词偏义或词组可查，普通词不泛化标蓝',()=>{
  expect(catalog.entries).toHaveLength(1874);for(const e of catalog.entries)expect(['difficult','shifted']).toContain(e.kind);
  const first=book.sentences[0];expect(getWordLookups(first.paragraphId,first.text,first.start).map(o=>o.text)).toEqual(['clementines']);
  expect(getWordLookups(first.paragraphId,'Yoshi',0)).toEqual([]);
 });
 it('所有正文的英文文本在加入按钮后逐字不变',()=>{
  for(const p of book.paragraphs){const html=renderToStaticMarkup(<WordText paragraphId={p.id} text={p.text} start={0}/>);expect(textContent(html),p.id).toBe(p.text);}
 });
 it('同段标注不重叠，不重复渲染任何字符',()=>{
  for(const list of Object.values(catalog.paragraphs)){for(let i=1;i<list.length;i++)expect(list[i].start).toBeGreaterThanOrEqual(list[i-1].end);}
 });
 it('只返回当前片段中的完整词，不把相邻段落的释义带进来',()=>{
  const o=occurrences[0];expect(getWordLookups(o.paragraphId,o.text,o.start)).toHaveLength(1);expect(getWordLookups(o.paragraphId,o.text.slice(1),o.start+1)).toEqual([]);
  expect(getWordLookups(o.paragraphId,'Different text',o.start)).toEqual([]);expect(getWordLookups('unknown',o.text,o.start)).toEqual([]);expect(getWordLookups(o.paragraphId,o.text,-1)).toEqual([]);
 });
 it('屈折词形可显示词典词头，语境义与常见义分开预存',()=>{
  const p=book.paragraphs.find(p=>p.text.includes('cultivating rice and tea'))!,word=getWordLookups(p.id,p.text,0).find(w=>w.text==='cultivating')!;
  expect(word.entry.headword).toBe('cultivate');expect(word.contextMeaning).toContain('种植');expect(word.entry.otherMeanings.join('')).toContain('培养');
 });
 it('熟词偏义保留本段解释，不使用同拼写的全局猜义',()=>{
  const p=book.paragraphs.find(p=>p.id===qs.find(q=>q.vocabulary.some(v=>v.word==='pool'))!.paragraphId)!;
  const word=getWordLookups(p.id,p.text,0).find(w=>w.text.toLowerCase()==='pool')!;expect(word.contextMeaning).toContain('候选');expect(word.entry.otherMeanings.join('')).toContain('游泳池');
 });
 it('单一常用义的词不编造第二义，全部语境义不包含答案标记',()=>{
  expect(catalog.entries.find(e=>e.id==='clementine')?.otherMeanings).toEqual([]);
  for(const o of occurrences)expect(o.contextMeaning).not.toMatch(/正确答案|选项|答案为/);
 });
 it('标注是可聚焦的真实按钮，未点击时不渲染词义弹窗',()=>{
  const p=book.paragraphs[0],html=renderToStaticMarkup(<WordText paragraphId={p.id} text={p.text} start={0}/>);expect(html).toContain('aria-haspopup="dialog"');expect(html).toContain('aria-label="查词 clementines"');expect(html).not.toContain('本段中的意思');expect(html).not.toContain('其他常见意思');
 });
 it('无法匹配原文位置的历史快照仍为纯原文，不错套当前释义',()=>{
  const q={...qs[0],passage:'Changed historical wording with clementines.',fingerprint:'historical-example'},state=emptyState();state.readingUnitId=q.readingUnitId;state.session={questionId:q.id,attemptId:null,selected:0,startedAt:1,elapsedBefore:0};
  const html=renderToStaticMarkup(<ReadingPractice book={book} questions={qs} plan={plan} state={state} question={q} attempt={grade(q,q.answer,state,100)} busy={false} onUnit={()=>{}} onSelect={()=>{}} onSubmit={()=>{}} onChat={()=>{}} onSource={()=>{}} onFavorite={()=>{}} onMark={()=>{}} onRetry={()=>{}}/>);
  expect(html).toContain(q.passage);expect(html).not.toContain('lookup-word');
 });
 it('扩充后保留首批全部词义和位置，并补足14章的实际语境标注',()=>{
  for(const e of baseline.entries)expect(catalog.entries.find(x=>x.id===e.id)).toEqual(e);
  for(const o of Object.values(baseline.paragraphs).flat())expect(occurrences.find(x=>x.id===o.id)).toEqual(o);
  const originalIds=new Set(Object.values(baseline.paragraphs).flat().map(o=>o.id)),added=occurrences.filter(o=>!originalIds.has(o.id));expect(added).toHaveLength(4384);
  for(const c of book.chapters)expect(added.some(o=>book.paragraphs.find(p=>p.id===o.paragraphId)?.chapterId===c.id),c.id).toBe(true);
  expect(catalog.entries.find(e=>e.id==='concrete')?.otherMeanings.join('')).toContain('混凝土');expect(catalog.entries.find(e=>e.id==='principal')?.otherMeanings.join('')).toContain('本金');
 });
 it('新增开篇词汇保留上一版全部词义与位置，并按本段语境解释',()=>{
  for(const e of previous.entries)expect(catalog.entries.find(x=>x.id===e.id)).toEqual(e);
  for(const o of Object.values(previous.paragraphs).flat())expect(occurrences.find(x=>x.id===o.id)).toEqual(o);
  const previousIds=new Set(Object.values(previous.paragraphs).flat().map(o=>o.id)),added=Object.values(lastRelease.paragraphs).flat().filter(o=>!previousIds.has(o.id));expect(added).toHaveLength(35);
  const world=added.find(o=>o.text==='a world away')!,maintain=added.find(o=>o.text==='maintain')!,reminiscing=added.find(o=>o.text==='reminiscing')!;
  expect(world.contextMeaning).toContain('相隔甚远');expect(maintain.contextMeaning).toContain('维系');expect(reminiscing.contextMeaning).toContain('追忆');
  expect(catalog.entries.find(e=>e.id===maintain.entryId)?.otherMeanings.join('')).toContain('主张');
 });
 it('B2扩充保留上一版全部词义和位置，新增记录逐项匹配预编写作者稿',()=>{
  for(const e of lastRelease.entries)expect(catalog.entries.find(x=>x.id===e.id)).toEqual(e);
  for(const o of Object.values(lastRelease.paragraphs).flat())expect(occurrences.find(x=>x.id===o.id)).toEqual(o);
  expect(expansion.additions).toHaveLength(3930);for(const row of expansion.additions)expect(occurrences.find(x=>x.id===row.occurrence.id)).toEqual(row.occurrence);
  for(const c of book.chapters)expect(expansion.additions.filter(row=>book.paragraphs.find(p=>p.id===row.occurrence.paragraphId)?.chapterId===c.id).length).toBeGreaterThan(150);
 });
 it('熟词偏义按具体语境区分，不把人名或实验术语当成普通义',()=>{
  const notes=expansion.additions.map(row=>row.occurrence);
  expect(notes.find(o=>o.text==='regulation'&&o.contextMeaning.includes('常规时间'))).toBeDefined();
  expect(notes.find(o=>o.text==='Blind'&&o.contextMeaning.includes('不知情'))).toBeDefined();
  expect(notes.find(o=>o.text==='scholarship'&&o.contextMeaning.includes('奖学金'))).toBeDefined();
  expect(notes.find(o=>o.text==='scholarship'&&o.contextMeaning.includes('学术研究'))).toBeDefined();
  expect(notes.filter(o=>['Joy','Grace','Angeles','Rockets'].includes(o.text))).toEqual([]);
  const report=read('source/b2-vocabulary/coverage.json');expect(report.pendingCandidateOccurrences).toEqual([]);expect(report.notice).toContain('not a full C2');
 });
});
