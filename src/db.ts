import {openDB} from 'idb';
import {emptyState} from './core';
import type {StudyState} from './types';
export const database=(name='life-three-dimensions-study-v1')=>openDB(name,1,{upgrade(db){db.createObjectStore('study');}});
export async function loadState(name?:string):Promise<StudyState>{const db=await database(name);try{return (await db.get('study','state'))??emptyState();}finally{db.close();}}
export async function saveState(state:StudyState,name?:string){const db=await database(name);try{await db.put('study',structuredClone(state),'state');}finally{db.close();}}
