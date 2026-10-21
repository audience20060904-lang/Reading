import catalog from './data/passage-translations.json';
import type {Question} from './types';

type TranslationEntry = {questionId:string;passage:string;sourceFingerprint:string;translation:string};
const entries = catalog.entries as TranslationEntry[];
const translationsById = new Map(entries.map(entry=>[entry.questionId,entry]));

// Match the original passage exactly, so older attempt snapshots can display the
// translation without changing their answer, version, fingerprint, or score.
export function getPassageTranslation(question:Pick<Question,'id'|'passage'>):string|undefined {
 const entry=translationsById.get(question.id);
 return entry?.passage===question.passage?entry.translation:undefined;
}

export default function PassageTranslation({question,submitted}:{question:Question;submitted:boolean}) {
 if(!submitted)return null;
 const translation=getPassageTranslation(question);
 if(!translation)return null;
 return <section className="passage-translation" aria-label="原文整段参考译文">
  <h3>六、原文整段参考译文</h3>
  <p className="muted small">对应本题上方的完整英文片段，供学习参考。</p>
  <p className="translated-passage" lang="zh-CN">{translation}</p>
 </section>;
}
