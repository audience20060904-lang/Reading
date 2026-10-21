import catalog from './data/question-translations.json';
import type {Question} from './types';
export function getQuestionTranslation(q:Pick<Question,'id'|'prompt'|'options'>){
 const entry=catalog.entries.find(e=>e.questionId===q.id&&e.prompt===q.prompt&&e.options.every((o,i)=>o===q.options[i]));
 return entry?{prompt:entry.promptZh,options:entry.optionsZh}:undefined;
}
