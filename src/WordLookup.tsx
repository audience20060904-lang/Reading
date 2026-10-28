import {createContext,Fragment,useContext,useLayoutEffect,useRef,useState} from 'react';
import type {ReactNode} from 'react';
import {createPortal} from 'react-dom';
import {X} from 'lucide-react';
import {getWordLookups} from './wordLookups';
import type {WordSelection} from './wordLookups';
import type {TextHighlight} from './evidenceHighlights';

type Active={word:WordSelection;anchor:HTMLButtonElement};
const LookupContext=createContext<{activeId?:string;open:(word:WordSelection,anchor:HTMLButtonElement)=>void}|null>(null);

function WordCard({active,onDismiss}:{active:Active;onDismiss:()=>void}){
 const ref=useRef<HTMLDialogElement>(null),{word}=active;
 useLayoutEffect(()=>{
  const dialog=ref.current!;dialog.showModal();
  const previousOverflow=document.body.style.overflow;document.body.style.overflow='hidden';
  const position=()=>{
   if(innerWidth<=600){dialog.style.left='';dialog.style.top='';return;}
   const rect=active.anchor.getBoundingClientRect(),box=dialog.getBoundingClientRect();
   dialog.style.left=Math.max(12,Math.min(rect.left,innerWidth-box.width-12))+'px';
   const below=rect.bottom+10;
   dialog.style.top=Math.max(12,Math.min(below+box.height<=innerHeight-12?below:rect.top-box.height-10,innerHeight-box.height-12))+'px';
  };
  position();window.addEventListener('resize',position);window.visualViewport?.addEventListener('resize',position);
  return()=>{window.removeEventListener('resize',position);window.visualViewport?.removeEventListener('resize',position);document.body.style.overflow=previousOverflow;if(dialog.open)dialog.close();};
 },[active]);
 return <dialog ref={ref} className="word-card" lang="zh-CN" aria-label={`查词：${word.text}`} onCancel={e=>{e.preventDefault();onDismiss();}} onClose={e=>{if(!e.currentTarget.open)onDismiss();}} onKeyDown={e=>{if(e.key!=='Tab')return;const nodes=e.currentTarget.querySelectorAll<HTMLElement>('button:not([disabled]),a[href],input:not([disabled]),[tabindex="0"]'),first=nodes[0],last=nodes[nodes.length-1];if(first&&((e.shiftKey&&document.activeElement===first)||(!e.shiftKey&&document.activeElement===last))){e.preventDefault();(e.shiftKey?last:first).focus();}}} onClick={e=>{if(e.target!==e.currentTarget)return;const r=e.currentTarget.getBoundingClientRect();if(e.clientX<r.left||e.clientX>r.right||e.clientY<r.top||e.clientY>r.bottom)onDismiss();}}>
  <button className="word-card-close" aria-label="关闭查词" onClick={onDismiss} autoFocus><X size={18}/></button>
  <span className="word-kind">{word.entry.kind==='shifted'?'熟词偏义':'难词'}</span>
  <h2 lang="en">{word.entry.headword}</h2>
  {word.text.toLowerCase()!==word.entry.headword.toLowerCase()&&<p className="word-form">文中词形：<span lang="en">{word.text}</span></p>}
  <h3>本段中的意思</h3><p className="word-context">{word.contextMeaning}</p>
  <h3>其他常见意思</h3>
  {word.entry.otherMeanings.length?<ul>{word.entry.otherMeanings.map(m=><li key={m}>{m}</li>)}</ul>:<p className="word-single-sense">通常没有其他独立的常见义项。</p>}
 </dialog>;
}

export function WordLookupProvider({children}:{children:ReactNode}){
 const [active,setActive]=useState<Active|null>(null);
 const dismiss=()=>{if(!active)return;const anchor=active.anchor;setActive(null);requestAnimationFrame(()=>{if(anchor.isConnected)anchor.focus({preventScroll:true});});};
 return <LookupContext.Provider value={{activeId:active?.word.id,open:(word,anchor)=>setActive({word,anchor})}}>{children}{active&&createPortal(<WordCard key={active.word.id} active={active} onDismiss={dismiss}/>,document.body)}</LookupContext.Provider>;
}

function markedText(text:string,offset:number,ranges:TextHighlight[]){
 if(!ranges.length)return text;const nodes:ReactNode[]=[];let cursor=0;
 for(const r of ranges){const from=Math.max(0,r.start-offset),to=Math.min(text.length,r.end-offset);if(to<=from)continue;if(from>cursor)nodes.push(text.slice(cursor,from));nodes.push(<mark className="evidence-highlight" key={offset+from}>{text.slice(from,to)}</mark>);cursor=to;}
 if(cursor<text.length)nodes.push(text.slice(cursor));return nodes;
}
export default function WordText({paragraphId,text,start,highlights=[]}:{paragraphId:string;text:string;start:number;highlights?:TextHighlight[]}){
 const lookup=useContext(LookupContext),words=getWordLookups(paragraphId,text,start);
 if(!words.length)return <>{markedText(text,0,highlights)}</>;
 let cursor=0;
 return <>{words.map(word=>{const from=word.start-start,to=word.end-start,before=markedText(text.slice(cursor,from),cursor,highlights);cursor=to;return <Fragment key={word.id}>{before}<button type="button" className={`lookup-word ${lookup?.activeId===word.id?'lookup-active':''}`} data-word-id={word.id} aria-label={`查词 ${word.text}`} aria-haspopup="dialog" onClick={e=>lookup?.open(word,e.currentTarget)}>{markedText(text.slice(from,to),from,highlights)}</button></Fragment>;})}{markedText(text.slice(cursor),cursor,highlights)}</>;
}
