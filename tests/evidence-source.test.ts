import {describe,it,expect} from 'vitest';
import {readFileSync} from 'node:fs';
import {matchEvidence,assertPlannedEvidence} from '../scripts/evidence-source.mjs';
import {activeReading} from '../src/activeReading';
const read=(p:string)=>JSON.parse(readFileSync(p,'utf8'));
const book=read('public/data/book.json'),active=activeReading(read('public/data/questions.json'),read('public/data/reading-plan.json'));
describe('包含上下文的逐字证据来源映射',()=>{
 it('拒绝用扩展引文吞掉下一批尚未设题的句子',()=>{const q=active.questions.find(q=>q.id==='q-c01-034')!,[first,next]=q.sentenceIds;const evidence=[{sentenceIds:[first,next]}];expect(()=>assertPlannedEvidence([{evidence}],new Set(),[first])).toThrow(/unassigned gap/);});
 it('允许已经配题的必要语境以及本批分别设题的原句',()=>{const q=active.questions.find(q=>q.id==='q-c01-034')!,[first,next]=q.sentenceIds;const questions=[{evidence:[{sentenceIds:[first,next]}]}];expect(()=>assertPlannedEvidence(questions,new Set([first]),[next])).not.toThrow();expect(()=>assertPlannedEvidence(questions,new Set(),[first,next])).not.toThrow();});
 it('普通句引用精确绑定目标来源，扩展完整上下文时如实包含两个源ID',()=>{const q=active.questions.find(q=>q.id==='q-c01-034')!,s=book.sentences.find((s:any)=>s.id===q.sentenceIds[0]),next=book.sentences.find((s:any)=>s.id===q.sentenceIds[1]);expect(matchEvidence(book,q,s.id,s.text).sentenceIds).toEqual([s.id]);const quote=q.passage.slice(q.passage.indexOf(s.text),q.passage.indexOf(next.text)+next.text.length);expect(matchEvidence(book,q,s.id,quote).sentenceIds).toEqual([s.id,next.id]);});
 it('断行字符不能伪装完整证据，真实完整跨块谚语映射两个候选ID',()=>{const q=active.questions.find(q=>q.id==='q-c11-062')!;const e=matchEvidence(book,q,q.sentenceIds[1],q.passage);expect(e.sentenceIds).toEqual(q.sentenceIds);expect(e.quote).toContain('七転八起');expect(e.sources.length).toBeGreaterThan(1);});
 it('引用不覆盖目标或添加不存在的词时拒绝编译',()=>{const q=active.questions.find(q=>q.id==='q-c01-034')!;expect(()=>matchEvidence(book,q,q.sentenceIds[1],book.sentences.find((s:any)=>s.id===q.sentenceIds[0]).text)).toThrow();expect(()=>matchEvidence(book,q,q.sentenceIds[0],'Invented source words.')).toThrow();});
});
