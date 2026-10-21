import {Bookmark,Check,X} from 'lucide-react';
import type {Attempt,Question,Vocabulary} from './types';
import {letters} from './core';
import {getQuestionTranslation} from './questionTranslations';
import PassageTranslation from './PassageTranslation';
export default function AnswerExplanation({question:q,attempt,favorites,onFavorite}:{question:Question;attempt?:Attempt;favorites:Vocabulary[];onFavorite:(v:Vocabulary)=>void}){
 if(!attempt)return null;
 const translated=getQuestionTranslation(q);
 return <section className="explanation" aria-label="详细中文解析">
  <div className={`result ${attempt.correct?'good':'bad'}`} role="status"><span className="result-icon">{attempt.correct?<Check/>:<X/>}</span><div><h2>{attempt.correct?'回答正确，继续保持。':'这道题值得再读一次。'}</h2><p>答案回顾：我的答案 <b>{letters[attempt.selected]}</b> · 正确答案 <b>{letters[attempt.correctAnswer]}</b> · {attempt.correct?'正确':'错误'}</p></div></div>
  <div className="explain-body">
   <h3>一、问题与选项分析</h3>
   <div className="question-translation"><p lang="en">{q.prompt}</p><p lang="zh-CN">{translated?.prompt??'此历史版本的问题译文尚未整理。'}</p></div>
   {q.analyses.map((a,i)=><div className={`analysis ${i===q.answer?'correct-analysis':''}`} key={i}><b>{letters[i]} {i===q.answer?'✓':''}</b><div className="option-analysis-copy"><p lang="en">{q.options[i]}</p><p className="option-translation" lang="zh-CN">{translated?.options[i]??'此历史版本的选项译文尚未整理。'}</p><p className="option-reason">{a.replace(/^[A-D]\s*/, '')}</p></div></div>)}
   <h3>二、重点词汇</h3><p className="muted small">英文例句为学习者编写，不是书中引文。</p>
   <div className="vocab-grid">{q.vocabulary.map(v=><article className="vocab" key={v.word}><button className={`bookmark ${favorites.some(x=>x.word===v.word)?'saved':''}`} onClick={()=>onFavorite(v)} aria-label={`收藏 ${v.word}`}><Bookmark size={17}/></button><h4 lang="en">{v.word}</h4><p>{v.meaning}</p><p className="muted">本句语境：{v.context}</p><p lang="en" className="example">{v.example}</p><p className="small">常见搭配：{v.collocations.join(' · ')}</p></article>)}</div>
   <PassageTranslation question={q} submitted/>
  </div>
 </section>;
}
