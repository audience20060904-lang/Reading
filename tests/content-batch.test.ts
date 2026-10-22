import {describe,it,expect} from 'vitest';
import {readFileSync} from 'node:fs';
import {createHash} from 'node:crypto';
import type {Book,Question} from '../src/types';
import {emptyState,grade,newSession,restoreSession,neighbor} from '../src/core';
import baseline from './fixtures/batch002-fingerprints.json';
const book=JSON.parse(readFileSync('public/data/book.json','utf8')) as Book;
const qs=JSON.parse(readFileSync('public/data/questions.json','utf8')) as Question[];
const legacy=JSON.parse(readFileSync('source/archive/questions-v1.json','utf8')) as Question[];
const batch=qs.filter(q=>q.chapterId==='c02'&&Number(q.id.slice(-3))>=13&&Number(q.id.slice(-3))<=27);

describe('第三批内容和旧记录兼容',()=>{
 it('保留前两批每道题的 ID、内容与指纹',()=>{
  for(const [id,fingerprint] of Object.entries(baseline)){expect(legacy.find(q=>q.id===id)?.fingerprint,id).toBe(fingerprint);expect(qs.find(q=>q.id===id)?.version).toBeGreaterThan(1);}
 });
 it('新题按原书位置插入，旧会话按 ID 恢复，不按数组下标错位',()=>{
  const old=legacy.find(q=>q.id==='q-c02-007')!,state=emptyState(),attempt=grade(old,old.answer,state,2400);
  state.attempts=[attempt];state.session={...newSession(old),attemptId:attempt.id,selected:attempt.selected};
  const originalQuestions=qs.filter(q=>legacy.some(old=>old.id===q.id));
  expect(neighbor(originalQuestions,'q-c02-006',1)?.id).toBe('q-c02-013');
  expect(neighbor(qs,'q-c02-006',1)?.id).toBe('q-c02-044');
  expect(restoreSession(state,qs).session?.questionId).toBe(old.id);
  expect(restoreSession(state,qs).attempts[0].snapshot.fingerprint).toBe(baseline['q-c02-007']);
 });
 it('15 道新增题均有完整材料及经过原页核对的证据',()=>{
  expect(batch).toHaveLength(15);
  for(const q of batch){
   expect(q.translation,q.id).toMatch(/[\u4e00-\u9fff]/);
   expect(q.vocabulary.length,q.id).toBeGreaterThan(0);
   expect(q.analyses).toHaveLength(4);
   for(const e of q.evidence)for(const id of e.sentenceIds)expect(book.sentences.find(s=>s.id===id)?.review,q.id).toBe('visual-proofread');
  }
 });
 it('视觉核对记录锁定实际对照的段落文本，防止改文后沿用审校状态',()=>{
  const reviews=JSON.parse(readFileSync('source/reviews.json','utf8')).filter((r:any)=>r.batchId==='batch-003');
  expect(reviews).toHaveLength(30);
  for(const r of reviews){const p=book.paragraphs.find(p=>p.id===r.paragraphId)!;expect(createHash('sha256').update(p.text).digest('hex')).toBe(r.reviewedTextSha256);}
 });
});
