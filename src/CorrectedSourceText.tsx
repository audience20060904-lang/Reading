import {Fragment} from 'react';
import WordText from './WordLookup';
import type {Book,ReadingUnit,StudyState} from './types';
export default function CorrectedSourceText({book,unit,state,jumpId,evidenceIds,onMark}:{book:Book;unit:ReadingUnit;state:StudyState;jumpId:string;evidenceIds:Set<string>;onMark:(id:string)=>void}){
 const ss=unit.sentenceIds.map(id=>book.sentences.find(s=>s.id===id)!);
 return <>{ss.map((s,i)=>{const previous=ss[i-1],p=book.paragraphs.find(p=>p.id===s.paragraphId)!;const gap=!previous?'':previous.paragraphId===s.paragraphId?p.text.slice(previous.end,s.start):unit.sourceSegments!.find(x=>x.paragraphId===s.paragraphId)!.separator;return <Fragment key={s.id}>{gap}<span id={s.id} className={`sentence ${jumpId===s.id?'jump-highlight':''} ${evidenceIds.has(s.id)?'evidence-highlight':''}`}><WordText paragraphId={s.paragraphId} text={s.text} start={s.start}/></span></Fragment>;})}<small className="cross-source-marks">跨来源断句已核对 · 候选句已读：{ss.map((s,i)=>{const read=state.readSentences.includes(s.id)||state.readSections.includes(s.sectionId);return <button className={`sentence-mark ${read?'marked':''}`} key={s.id} aria-label={`${read?'取消已读':'标记已读'} ${s.id}`} title={s.id} onClick={()=>onMark(s.id)}>{read?'●':'○'} {i+1}</button>;})}</small></>;
}
