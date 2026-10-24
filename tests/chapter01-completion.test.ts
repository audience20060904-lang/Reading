import {describe,it,expect} from 'vitest';
import {readFileSync} from 'node:fs';
import {createHash} from 'node:crypto';
import baseline from './fixtures/batch004-fingerprints.json';
import type {Book,Question,ReadingPlan} from '../src/types';
import {getQuestionTranslation} from '../src/questionTranslations';
const b=JSON.parse(readFileSync('public/data/book.json','utf8')) as Book;
const qs=JSON.parse(readFileSync('public/data/questions.json','utf8')) as Question[];
const plan=JSON.parse(readFileSync('public/data/reading-plan.json','utf8')) as ReadingPlan;
const added=qs.filter(q=>q.chapterId==='c01'&&Number(q.id.slice(-3))>=41);
describe('第 1 章补齐与已发布内容保护',()=>{
 it('已发布 67 道题内容指纹不变，不用更新题库篡改旧成绩',()=>{
  expect(Object.keys(baseline)).toHaveLength(67);
  for(const [id,fingerprint] of Object.entries(baseline))expect(qs.find(q=>q.id===id)?.fingerprint,id).toBe(fingerprint);
 });
 it('第 1 章 177 个候选句按顺序进入 77 个已配题短段，五小节均完整',()=>{
  const units=plan.units.filter(u=>u.chapterId==='c01');expect(units).toHaveLength(77);
  expect(units.flatMap(u=>u.sentenceIds)).toEqual(b.sentences.filter(s=>s.chapterId==='c01').map(s=>s.id));
  expect(units.flatMap(u=>u.sentenceIds)).toHaveLength(177);expect(units.every(u=>u.questionId)).toBe(true);
  for(const u of units){const q=qs.find(q=>q.id===u.questionId)!;expect(q.translation).toMatch(/[\u4e00-\u9fff]/);expect(getQuestionTranslation(q)?.options).toHaveLength(4);}
 });
 it('37 道新增题证据准确覆盖引用触及的句子，审阅记录绑定实际文本',()=>{
  expect(added).toHaveLength(37);
  const reviews=JSON.parse(readFileSync('source/short-questions/review-chapter-01.json','utf8'));
  for(const q of added){
   const p=b.paragraphs.find(p=>p.id===q.paragraphId)!;
   expect(reviews.paragraphs.find((r:any)=>r.id===p.id)?.textSha256).toBe(createHash('sha256').update(p.text).digest('hex'));
   for(const e of q.evidence){const start=p.text.indexOf(q.passage)+q.passage.indexOf(e.quote),end=start+e.quote.length;expect(e.sentenceIds).toEqual(q.sentenceIds.filter(id=>{const s=b.sentences.find(s=>s.id===id)!;return s.start<end&&s.end>start;}));}
  }
 });
 it('文学引例、假设和不确定程度不被包装成实验或个体保证',()=>{
  const get=(id:string)=>qs.find(q=>q.id===id)!;
  expect(get('q-c01-068').support).toBe('inference');expect(get('q-c01-068').analyses[0]).toContain('Imagine');
  expect(get('q-c01-050').analyses[1]).toContain('小说');expect(get('q-c01-074').analyses[0]).toContain('hopefully');
  expect(get('q-c01-046').analyses[0]).toContain('perhaps');
  const tasks=JSON.parse(readFileSync('source/content-tasks.json','utf8'));
  expect(tasks.chapters.find((c:any)=>c.id==='c01').remainingReadingUnitIds).toEqual([]);
  expect(tasks.chapters.find((c:any)=>c.id==='c01').remainingEvidenceIds.length).toBeGreaterThan(0);
  expect(tasks.nextBatch.chapterId).toBe(plan.units.find(u=>!u.questionId)?.chapterId);expect(plan.coverage.allQuestionsPrepared).toBe(plan.units.every(u=>u.questionId));
 });
});
