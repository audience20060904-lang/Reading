import {describe,it,expect} from 'vitest';
import 'fake-indexeddb/auto';
import {readFileSync} from 'node:fs';
import {emptyState,grade,newSession,statistics} from '../src/core';
import {database,loadStudy,localCheckpoints,saveState} from '../src/db';
import {chapterPosition} from '../src/chapterProgress';
import type {Question,ReadingPlan} from '../src/types';
const plan=JSON.parse(readFileSync('public/data/reading-plan.json','utf8')) as ReadingPlan;
const qs=JSON.parse(readFileSync('public/data/questions.json','utf8')) as Question[];
const submitted=()=>{const s=emptyState(),a=grade(qs[0],qs[0].answer,s,1234);s.attempts=[a];s.readingUnitId=qs[0].readingUnitId;s.session={...newSession(qs[0]),attemptId:a.id,selected:a.selected};return s;};
describe('本章阅读位置',()=>{
 it('按本章短段而非全书计算，第2段不是2/1056',()=>{const u=plan.units[1],p=chapterPosition(plan,u);expect(p.position).toBe(2);expect(p.total).toBe(plan.units.filter(v=>v.chapterId===u.chapterId).length);expect(p.percent).toBe(2/p.total*100);});
 it('跨章后按新章重置，上一章末段为100%',()=>{const i=plan.units.findIndex(u=>u.chapterId!==plan.units[0].chapterId);expect(chapterPosition(plan,plan.units[i]).position).toBe(1);expect(chapterPosition(plan,plan.units[i-1]).percent).toBe(100);});
 it('任意跳转只计算位置，不伪造已读或成绩',()=>{const s=emptyState(),before=structuredClone(s);chapterPosition(plan,plan.units.at(-1)!);expect(s).toEqual(before);expect(statistics(s).total).toBe(0);expect(chapterPosition(plan,{...plan.units[0],id:'missing'}).percent).toBe(0);});
});
describe('本机事务与恢复',()=>{
 it('兼容原v1数据库，原状态key和历史快照不变',async()=>{const name=crypto.randomUUID(),db=await database(name),s=submitted();await db.put('study',s,'state');db.close();const loaded=await loadStudy(name);expect(loaded.state).toEqual(s);expect(loaded.revision).toBe(0);expect(await saveState(s,name,0)).toBe(1);expect((await loadStudy(name)).state.attempts).toEqual(s.attempts);});
 it('保留三个旧状态，计时保存不会挤掉恢复点',async()=>{const name=crypto.randomUUID();let s=emptyState();s.session=newSession(qs[0]);await saveState(s,name);for(let i=0;i<5;i++){s={...s,fontSize:21+i};await saveState(s,name);}const before=await localCheckpoints(name);expect(before).toHaveLength(3);expect(before.map(p=>p.state.fontSize)).toEqual([24,23,22]);await saveState({...s,updatedAt:new Date().toISOString(),session:{...s.session!,elapsedBefore:5000}},name);expect(await localCheckpoints(name)).toEqual(before);});
 it('主记录损坏时找有效恢复点，恢复时不改变历史成绩',async()=>{const name=crypto.randomUUID(),s=submitted();await saveState(s,name);await saveState({...s,fontSize:22},name);const db=await database(name);await db.put('study',{broken:true},'state');db.close();const recovered=await loadStudy(name);expect(recovered.recovered).toBe(true);expect(recovered.state).toEqual(s);await saveState(recovered.state,name,recovered.revision);expect((await loadStudy(name)).state.attempts).toEqual(s.attempts);});
 it('全部损坏时拒绝偷偷清空记录',async()=>{const name=crypto.randomUUID(),db=await database(name);await db.put('study',{broken:true},'state');db.close();await expect(loadStudy(name)).rejects.toThrow('损坏');const again=await database(name);expect(await again.get('study','state')).toEqual({broken:true});again.close();});
 it('同源两个标签页竞争时旧版本事务不能覆盖新答案',async()=>{const name=crypto.randomUUID(),a=await loadStudy(name),b=await loadStudy(name),saved=submitted();await saveState(saved,name,a.revision);await expect(saveState({...b.state,theme:'dark'},name,b.revision)).rejects.toThrow('另一标签页');expect((await loadStudy(name)).state).toEqual(saved);});
 it('无效导入不覆盖原记录或增加恢复点',async()=>{const name=crypto.randomUUID(),s=submitted();await saveState(s,name);await expect(saveState({...s,attempts:[{...s.attempts[0],correct:!s.attempts[0].correct}]},name)).rejects.toThrow();expect((await loadStudy(name)).state).toEqual(s);expect(await localCheckpoints(name)).toEqual([]);});
});
