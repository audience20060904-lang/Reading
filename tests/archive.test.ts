import {beforeEach,afterEach,describe,it,expect,vi} from 'vitest';
import 'fake-indexeddb/auto';
import {readFileSync} from 'node:fs';
import {emptyState,grade,newSession,statistics} from '../src/core';
import {database,loadStudy,localCheckpoints,saveState} from '../src/db';
import {chapterPosition} from '../src/chapterProgress';
import {decryptSave,encryptSave,inspectCloud,uploadCloud} from '../src/cloudSave';
import type {CloudConfig} from '../src/cloudSave';
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
describe('加密在线存档',()=>{
 const password='only-a-synthetic-passphrase';
 it('加密往返保留位置、已提交解析和快照，上传体不含明文原文',async()=>{const s=submitted(),text=await encryptSave(s,password);expect(text).not.toContain(qs[0].passage);expect(text).not.toContain('attempts');expect(await decryptSave(text,password)).toEqual(s);});
 it('每次使用随机盐与IV，同一内容密文不同',async()=>{const s=emptyState();expect(await encryptSave(s,password)).not.toBe(await encryptSave(s,password));});
 it('口令错误或密文被篡改时拒绝恢复',async()=>{const text=await encryptSave(submitted(),password);await expect(decryptSave(text,password+'wrong')).rejects.toThrow('无法解密');const root=JSON.parse(text);root.data='X'+root.data.slice(1);await expect(decryptSave(JSON.stringify(root),password)).rejects.toThrow('无法解密');});
 it('拒绝不匹配格式、超限以及过短口令',async()=>{await expect(decryptSave('{}',password)).rejects.toThrow('格式');await expect(encryptSave(emptyState(),'short')).rejects.toThrow('12');await expect(decryptSave('x'.repeat(12_000_001),password)).rejects.toThrow('大小');});
});
describe('GitHub私有仓库存档协议（模拟接口）',()=>{
 const c:CloudConfig={owner:'reader',repo:'private-saves',token:'synthetic-not-a-real-token',password:'synthetic-password-12345'};
 let body:string|null,sha:string,privateFlag:boolean,conflict:boolean,requests:{url:string;init:RequestInit}[];
 beforeEach(()=>{body=null;sha='a'.repeat(40);privateFlag=true;conflict=false;requests=[];vi.stubGlobal('fetch',vi.fn(async(url:string,init:RequestInit)=>{
  requests.push({url,init});const path=new URL(url).pathname;
  if(path.endsWith('/private-saves'))return Response.json({private:privateFlag,visibility:privateFlag?'private':'public',default_branch:'main'});
  if(init.method==='PUT'){
   if(conflict)return Response.json({}, {status:409});
   const sent=JSON.parse(init.body as string);if((body&&sent.sha!==sha)||(!body&&sent.sha))return Response.json({}, {status:409});
   body=new TextDecoder().decode(Uint8Array.from(atob(sent.content),c=>c.charCodeAt(0)));sha='b'.repeat(40);return Response.json({content:{sha}});
  }
  if(path.includes('/git/blobs/'))return new Response(body!);
  if(path.includes('/contents/'))return body?Response.json({type:'file',sha,size:body.length}):Response.json({}, {status:404});
  return Response.json({}, {status:404});
 }));});
 afterEach(()=>vi.unstubAllGlobals());
 it('新私有仓库可上传，重新下载解密校验全部记录',async()=>{const blank=await inspectCloud(c);expect(blank.sha).toBeNull();const s=submitted(),result=await uploadCloud(c,s,blank);expect(result.state).toEqual(s);expect((await inspectCloud(c)).state).toEqual(s);expect(body).not.toContain('Yoshi');expect(requests.every(r=>r.url.startsWith('https://api.github.com/repos/reader/private-saves'))).toBe(true);expect(requests.every(r=>r.init.cache==='no-store'&&r.init.credentials==='omit'&&r.init.redirect==='error')).toBe(true);});
 it('读取时元数据与原文使用同一个不可变blob指纹',async()=>{body=await encryptSave(submitted(),c.password);await inspectCloud(c);expect(requests.at(-1)?.url).toContain('/git/blobs/'+sha);});
 it('公开仓库即使令牌可写也拒绝上传',async()=>{privateFlag=false;await expect(inspectCloud(c)).rejects.toThrow('Private');await expect(uploadCloud(c,emptyState(),{sha:null,branch:'main',state:null})).rejects.toThrow('Private');expect(requests.some(r=>r.init.method==='PUT')).toBe(false);});
 it('另一设备修改后拒绝覆盖，不重试强制写入',async()=>{const expected=await inspectCloud(c);conflict=true;await expect(uploadCloud(c,submitted(),expected)).rejects.toThrow('冲突');expect(requests.filter(r=>r.init.method==='PUT')).toHaveLength(1);});
 it('网络、无权限、错误仓库名均不吞掉错误',async()=>{vi.stubGlobal('fetch',vi.fn().mockRejectedValue(new Error('token secret must not leak')));await expect(inspectCloud(c)).rejects.toThrow('无法连接');vi.stubGlobal('fetch',vi.fn().mockResolvedValue(Response.json({}, {status:401})));await expect(inspectCloud(c)).rejects.toThrow('过期');await expect(inspectCloud({...c,repo:'../public'})).rejects.toThrow('仓库名');});
 it('禁止读到未加密JSON后恢复，隐私配置不进入备份',async()=>{body=JSON.stringify({format:'three-dimensions-study'});await expect(inspectCloud(c)).rejects.toThrow('格式');expect(JSON.stringify(emptyState())).not.toContain(c.token);});
});
