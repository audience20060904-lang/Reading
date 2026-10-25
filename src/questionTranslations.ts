import catalog from './data/question-translations.json';
import type {Question} from './types';
export function getQuestionTranslation(q:Pick<Question,'id'|'prompt'|'options'|'family'|'promptZh'|'optionsZh'>){
 if(q.family==='sentence-evidence'&&q.promptZh&&q.optionsZh?.length===4)return {prompt:q.promptZh,options:q.optionsZh};
 const entry=catalog.entries.find(e=>e.questionId===q.id&&e.prompt===q.prompt&&e.options.every((o,i)=>o===q.options[i]));
 return entry?{prompt:entry.promptZh,options:entry.optionsZh}:undefined;
}
