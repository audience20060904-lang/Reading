import catalog from './data/sentence-repair-catalog.json';
import type {Question,ReadingPlan} from './types';
import {applyQuestionRevisions} from './questionRevisions';

// These are precompiled local records, not generated questions. Original published
// records remain intact for source audit and immutable historical snapshots.
export function activeReading(questions:Question[],plan:ReadingPlan,evidenceQuestions:Question[]=[]){
 if(plan.pdfSha256!==catalog.pdfSha256)throw new Error('断句修复与书籍来源不匹配');
 const replacements=new Map((catalog.questions as unknown as Question[]).map(q=>[q.id,q]));
 const units=new Map(catalog.units.map(u=>[u.id,u]));
 const active=questions.map(q=>{
  const replacement=replacements.get(q.id);if(!replacement)return q;
  if(q.fingerprint!==(catalog.baselineFingerprints as Record<string,string>)[q.id])throw new Error('断句修复与原题版本不匹配，请更新离线缓存后重试。');
  return replacement;
 });
 const ids=new Set(active.map(q=>q.id));
 for(const q of evidenceQuestions){if(q.family!=='sentence-evidence'||ids.has(q.id)||!active.some(p=>p.id===q.parentQuestionId&&p.readingUnitId===q.readingUnitId))throw new Error('逐句补题数据不匹配，请更新缓存后重试');ids.add(q.id);}
 const combined=applyQuestionRevisions([...active,...evidenceQuestions],plan.pdfSha256);
 return {questions:combined,plan:{...plan,rule:plan.rule+' '+catalog.rule,coverage:catalog.coverage,units:plan.units.map(original=>{const u=units.get(original.id)??original;const additional=evidenceQuestions.filter(q=>q.readingUnitId===u.id);return additional.length?{...u,questionIds:[u.questionId!,...additional.map(q=>q.id)]}:u;})} as ReadingPlan};
}
