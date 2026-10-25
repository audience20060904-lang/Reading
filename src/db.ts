import {openDB} from 'idb';
import {emptyState,parseBackup} from './core';
import type {StudyState} from './types';
export const database=(name='life-three-dimensions-study-v1')=>openDB(name,1,{upgrade(db){db.createObjectStore('study');}});
export type LocalCheckpoint={savedAt:string;state:StudyState};
const validate=(state:StudyState)=>parseBackup(JSON.stringify({format:'three-dimensions-study',version:1,state}));
const meaningful=(s:StudyState)=>JSON.stringify({...s,updatedAt:'',session:s.session?{...s.session,elapsedBefore:0,startedAt:0}:null});
export async function loadStudy(name?:string){
 const db=await database(name);
 try{
  const tx=db.transaction('study'),store=tx.objectStore('study');
  const [raw,backups,revision]=await Promise.all([store.get('state'),store.get('checkpoints'),store.get('revision')]);
  if(raw!==undefined){try{return {state:validate(raw),revision:revision??0,recovered:false};}catch{/* Try an intact checkpoint. */}}
  for(const item of (Array.isArray(backups)?backups:[])){try{return {state:validate(item.state),revision:revision??0,recovered:true};}catch{/* Try the older point. */}}
  if(raw!==undefined)throw new Error('本机存档损坏，且没有可用恢复点。请从备份恢复；原始数据未删除。');
  return {state:emptyState(),revision:revision??0,recovered:false};
 }finally{db.close();}
}
export async function loadState(name?:string):Promise<StudyState>{return (await loadStudy(name)).state;}
export async function localCheckpoints(name?:string):Promise<LocalCheckpoint[]>{
 const db=await database(name);try{const points=await db.get('study','checkpoints');return (Array.isArray(points)?points:[]).flatMap(p=>{try{return [{savedAt:p.savedAt,state:validate(p.state)}];}catch{return [];}});}finally{db.close();}
}
export async function saveState(state:StudyState,name?:string,expectedRevision?:number):Promise<number>{
 const next=validate(state),db=await database(name);
 try{
  const tx=db.transaction('study','readwrite'),store=tx.objectStore('study');
  const [old,revision,backups]=await Promise.all([store.get('state'),store.get('revision'),store.get('checkpoints')]);
  if(expectedRevision!==undefined&&expectedRevision!==(revision??0)){tx.abort();await tx.done.catch(()=>{});throw new Error('另一标签页已更新存档。请刷新本页再继续，避免覆盖较新的记录。');}
  let previous:StudyState|undefined;try{if(old!==undefined)previous=validate(old);}catch{/* Keep intact recovery points. */}
  if(previous&&meaningful(previous)!==meaningful(next))await store.put([{savedAt:new Date().toISOString(),state:previous},...(Array.isArray(backups)?backups:[])].slice(0,3),'checkpoints');
  await store.put(next,'state');await store.put((revision??0)+1,'revision');await tx.done;
  return (revision??0)+1;
 }finally{db.close();}
}
