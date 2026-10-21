import {ArrowUpRight,Check,ChevronLeft,ChevronRight,Leaf,MessageCircle,X} from 'lucide-react';
import type {Attempt,Book,Question,ReadingPlan,ReadingUnit,StudyState,Vocabulary} from './types';
import {letters} from './core';
import AnswerExplanation from './AnswerExplanation';
type Props={book:Book;questions:Question[];plan:ReadingPlan;state:StudyState;question:Question;attempt?:Attempt;busy:boolean;onUnit:(u:ReadingUnit,fresh?:boolean)=>void;onSelect:(i:number)=>void;onSubmit:()=>void;onChat:()=>void;onSource:(id:string)=>void;onFavorite:(v:Vocabulary)=>void;onMark:(u:ReadingUnit)=>void;onRetry:()=>void};
export default function ReadingPractice({book,questions,plan,state,question,attempt,busy,onUnit,onSelect,onSubmit,onChat,onSource,onFavorite,onMark,onRetry}:Props){
 const unit=plan.units.find(u=>u.id===state.readingUnitId)??plan.units.find(u=>u.questionId===question.id)??plan.units[0];
 const index=plan.units.indexOf(unit),prepared=questions.find(q=>q.id===unit.questionId),q=prepared&&state.session?.questionId===prepared.id?question:prepared;
 const answered=q&&attempt?.questionId===q.id?attempt:undefined,legacy=!!(answered&&prepared&&answered.fingerprint!==prepared.fingerprint);
 const paragraph=book.paragraphs.find(p=>p.id===unit.paragraphId)!,sentences=unit.sentenceIds.map(id=>book.sentences.find(s=>s.id===id)!);
 const shownIds=legacy?q!.sentenceIds:unit.sentenceIds,shownWords=legacy?q!.passage.trim().split(/\s+/).length:unit.wordCount;
 const passage=legacy?q!.passage:paragraph.text.slice(sentences[0].start,sentences.at(-1)!.end);
 const chapter=book.chapters.find(c=>c.id===unit.chapterId)!,section=book.sections.find(s=>s.id===unit.sectionId)!;
 const read=unit.sentenceIds.every(id=>state.readSentences.includes(id)||state.readSections.includes(unit.sectionId));
 return <>
  <div className="page-heading"><div><div className="eyebrow"><span className="tiny-line"/>READ IN ORDER</div><h1>读一小段，向前一点。</h1><p>全书原句连续排列，每句只出现一次。</p></div><div className="session-count"><span>{String(index+1).padStart(2,'0')}</span> / {plan.units.length}<small>短段 · 已备 {questions.length} 题</small></div></div>
  <div className="reading-path"><span>Chapter {String(chapter.number).padStart(2,'0')}</span><ChevronRight size={14}/><span lang="en">{section.title}</span><button className="text-button" onClick={()=>onSource(unit.sentenceIds[0])}>查看章节 <ArrowUpRight size={14}/></button></div>
  {legacy&&<div className="notice">正在回看改版前的作答快照，原答案和成绩保留。<button className="text-button" onClick={()=>onUnit(unit,true)}>使用新版短段练习</button></div>}
  <div className={`practice-grid ${q?'':'reading-only-grid'}`}>
   <article className="passage-card"><div className="card-top"><span className="eyebrow">READ THE PASSAGE</span><span className="page-tag">PDF {unit.pdfPages.join('–')} · {shownWords} 词</span></div><h2 lang="en">{section.title.replace(/^\d+\. /,'')}</h2><div className="passage" lang="en" style={{fontSize:state.fontSize}}>{passage}</div><div className="passage-footer"><Leaf size={15}/><span>{legacy?'历史快照原文 · 未改写旧作答':'保留原句 · 本段不与其他短段重叠'}</span><button className="text-button" onClick={()=>onSource(unit.sentenceIds[0])}>查看来源</button></div><details className="source-details"><summary>来源、句子 ID 与排版规则</summary><p>{unit.paragraphId}</p><p>{shownIds.join(' / ')}</p><p>{book.normalization}</p><p>这里的句子数量为自动候选分句。短段保持原文顺序，不等于全部句界已经人工定稿。</p></details></article>
   {q?<section className="question-card"><div className="card-top"><span className="eyebrow">ONE QUESTION</span><span className="type-tag">{q.type}</span></div><h2 lang="en" className="question-prompt">{q.prompt}</h2><p className="muted small">选择并提交后，查看中文问题、选项翻译和解析。</p><div className="options" role="radiogroup" aria-label="答案选项">{q.options.map((o,i)=>{const cls=answered?(i===q.answer?'correct':i===answered.selected?'incorrect':''):state.session?.selected===i?'chosen':'';return <button role="radio" aria-checked={state.session?.selected===i} disabled={!!answered||busy} key={i} className={`option ${cls}`} onClick={()=>onSelect(i)}><span className="option-letter">{letters[i]}</span><span lang="en">{o}</span>{answered&&i===q.answer&&<Check size={17}/ >}{answered&&i===answered.selected&&i!==q.answer&&<X size={17}/>}</button>;})}</div>
   {!answered?<button className="primary submit" disabled={state.session?.selected==null||busy} onClick={onSubmit}>{busy?'正在保存…':'提交答案'}<ChevronRight size={18}/></button>:<div className={`submitted ${answered.correct?'success':'failure'}`}>{answered.correct?<Check size={17}/>:<X size={17}/>}已提交 · 正确答案 {letters[q.answer]}<span>{Math.round(answered.elapsedMs/1000)} 秒</span></div>}
   <button className="ask-button" onClick={onChat}><MessageCircle size={17}/>Ask ChatGPT<ArrowUpRight size={15}/></button><p className="micro muted">复制问题，在 ChatGPT 新标签页手动讨论。</p></section>:<aside className="reading-unprepared"><h2>这段原文已完整保留</h2><p>本段题目与中文学习材料尚未编写。可以继续阅读；这里没有占位题，也不会增加作答次数。</p><p className="muted small">全书 {plan.units.length} 个短段，已有 {plan.coverage.unitsWithQuestions} 段配题，还有 {plan.coverage.unitsWithoutQuestions} 段待补充。</p></aside>}
  </div>
  {q&&<AnswerExplanation question={q} attempt={answered} favorites={state.favorites} onFavorite={onFavorite}/>}
  <div className="reading-unit-actions"><button className={read?'read-mark active':'read-mark'} disabled={read} onClick={()=>onMark(unit)}><Check size={14}/>{read?'本段已读':'手动标记本段已读'}</button><span className="muted small">已读只记录阅读进度，不产生答题成绩。</span></div>
  <div className="question-navigation"><button disabled={index===0} onClick={()=>onUnit(plan.units[index-1])}><ChevronLeft size={17}/>上一段</button><span>{q&&!answered?'先提交答案，再继续下一段。':answered?'读完解析，再按自己的节奏继续。':'按原书顺序继续阅读。'}</span><button className="primary" disabled={index===plan.units.length-1||!!(q&&!answered)} onClick={()=>onUnit(plan.units[index+1])}>下一段<ChevronRight size={17}/></button></div>
  {answered&&<button className="text-button retry-current" onClick={onRetry}>重新练习本题（新增一次记录）</button>}
 </>;
}
