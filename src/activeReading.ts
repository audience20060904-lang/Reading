import catalog from './data/sentence-repair-catalog.json';
import type {Question,ReadingPlan} from './types';

// These are precompiled local records, not generated questions. Original published
// records remain intact for source audit and immutable historical snapshots.
export function activeReading(questions:Question[],plan:ReadingPlan){
 if(plan.pdfSha256!==catalog.pdfSha256)throw new Error('断句修复与书籍来源不匹配');
 const replacements=new Map((catalog.questions as unknown as Question[]).map(q=>[q.id,q]));
 const units=new Map(catalog.units.map(u=>[u.id,u]));
 const active=questions.map(q=>{
  const replacement=replacements.get(q.id);if(!replacement)return q;
  if(q.fingerprint!==(catalog.baselineFingerprints as Record<string,string>)[q.id])throw new Error('断句修复与原题版本不匹配，请更新离线缓存后重试。');
  return replacement;
 });
 return {questions:active,plan:{...plan,rule:plan.rule+' '+catalog.rule,coverage:catalog.coverage,units:plan.units.map(u=>units.get(u.id)??u)} as ReadingPlan};
}
