import catalog from './data/question-revision-catalog.json';
import type {Question} from './types';

// Versioned, prewritten editorial corrections. Submitted attempts use their own
// snapshots; only the current question bank receives these replacements.
export function applyQuestionRevisions(questions:Question[],pdfSha256:string){
 if(pdfSha256!==catalog.pdfSha256)throw new Error('题目校对与书籍来源不匹配');
 const replacements=new Map((catalog.questions as unknown as Question[]).map(q=>[q.id,q]));
 return questions.map(q=>{
  const revised=replacements.get(q.id);if(!revised)return q;
  if(q.fingerprint!==(catalog.baselineFingerprints as Record<string,string>)[q.id])throw new Error('题目校对与原题版本不匹配，请更新离线缓存后重试。');
  return revised;
 });
}
