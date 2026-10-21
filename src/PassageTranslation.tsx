import catalog from './data/passage-translations.json';
import type {Question} from './types';

type TranslationEntry = {questionId:string;passage:string;sourceFingerprint:string;translation:string};
const entries = catalog.entries as TranslationEntry[];
const translationsByPassage = new Map(entries.map(entry=>[entry.questionId+'\0'+entry.passage,entry]));

// Match the original passage exactly, so older attempt snapshots can display the
// translation without changing their answer, version, fingerprint, or score.
export function getPassageTranslation(question:Pick<Question,'id'|'passage'>):string|undefined {
 return translationsByPassage.get(question.id+'\0'+question.passage)?.translation;
}

export default function PassageTranslation({question,submitted}:{question:Question;submitted:boolean}) {
 if(!submitted)return null;
 const translation=getPassageTranslation(question);
 if(!translation)return null;
 return <section className="passage-translation" aria-label="原文整段参考译文">
  <h3>三、原文整段参考译文</h3>
  <p className="muted small">对应本题上方的完整英文片段，供学习参考。</p>
  <p className="translated-passage" lang="zh-CN">{translation}</p>
 </section>;
}
