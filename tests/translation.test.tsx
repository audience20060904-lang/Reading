import {describe,it,expect} from 'vitest';
import {renderToStaticMarkup} from 'react-dom/server';
import {readFileSync} from 'node:fs';
import type {Question} from '../src/types';
import PassageTranslation,{getPassageTranslation} from '../src/PassageTranslation';
import catalog from '../src/data/passage-translations.json';
const questions=JSON.parse(readFileSync('public/data/questions.json','utf8')) as Question[];

describe('提交后的完整原文翻译',()=>{
 it('当前每一道题都有与完整英文片段精确对应的预先编写译文',()=>{
  expect(catalog.entries.length).toBeGreaterThanOrEqual(questions.length);
  for(const q of questions){const entry=catalog.entries.find(e=>e.questionId===q.id&&e.sourceFingerprint===q.fingerprint);expect(entry?.passage,q.id).toBe(q.passage);expect(getPassageTranslation(q),q.id).toMatch(/[\u4e00-\u9fff]/);}
 });
 it('只选择但未提交时不显示翻译，提交后才显示',()=>{
  const q=questions[0];expect(renderToStaticMarkup(<PassageTranslation question={q} submitted={false}/>)).toBe('');
  const html=renderToStaticMarkup(<PassageTranslation question={q} submitted/>);expect(html).toContain('三、原文整段参考译文');expect(html).toContain('绿茶和小柑橘');expect(html).not.toContain('种植水稻和茶叶');
 });
 it('旧作答快照也能显示匹配译文，不修改快照与历史成绩字段',()=>{
  const q=JSON.parse(readFileSync('source/archive/questions-v1.json','utf8'))[0],before=JSON.stringify(q);expect(getPassageTranslation(q)).toContain('种植水稻和茶叶');expect(JSON.stringify(q)).toBe(before);
 });
 it('原文不同的旧版本或未知题目不套用不匹配的译文',()=>{
  expect(getPassageTranslation({...questions[0],passage:questions[0].passage+' Different text.'})).toBeUndefined();expect(getPassageTranslation({...questions[0],id:'unknown'})).toBeUndefined();
 });
});
