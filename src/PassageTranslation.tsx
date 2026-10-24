import catalog from './data/passage-translations.json';
import type {ReactNode} from 'react';
import type {Question} from './types';

type TranslationEntry = {questionId:string;passage:string;sourceFingerprint:string;translation:string};
const entries = catalog.entries as TranslationEntry[];
const translationsByPassage = new Map(entries.map(entry=>[entry.questionId+'\0'+entry.passage,entry]));

// Match the original passage exactly, so older attempt snapshots can display the
// translation without changing their answer, version, fingerprint, or score.
export function getPassageTranslation(question:Pick<Question,'id'|'passage'>):string|undefined {
 return translationsByPassage.get(question.id+'\0'+question.passage)?.translation;
}

export default function PassageTranslation({question,submitted,original}:{question:Question;submitted:boolean;original?:ReactNode}) {
 if(!submitted)return null;
 const translation=getPassageTranslation(question);
 return <section className="passage-translation" aria-label="原文整段参考译文">
  <h3>三、原文整段参考译文</h3>
  {original??<div className="passage" lang="en">{question.passage}</div>}
  <p className="translated-passage" lang="zh-CN">{translation??'此历史版本的整段译文尚未整理。'}</p>
 </section>;
}
