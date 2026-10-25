import {exportBackup,parseBackup} from './core';
import type {StudyState} from './types';

export type CloudConfig={owner:string;repo:string;token:string;password:string};
export type RemoteSave={sha:string|null;branch:string;state:StudyState|null};
const PATH='reading/study.enc.json',MAX=12_000_000,ITERATIONS=310000;
const encode=(data:Uint8Array)=>{let text='';for(let i=0;i<data.length;i+=8192)text+=String.fromCharCode(...data.subarray(i,i+8192));return btoa(text);};
const decode=(text:string)=>Uint8Array.from(atob(text),c=>c.charCodeAt(0));
async function key(password:string,salt:Uint8Array,usage:KeyUsage[]){
 if(password.length<12)throw new Error('加密口令至少 12 个字符；请在手机和电脑使用相同口令。');
 const material=await crypto.subtle.importKey('raw',new TextEncoder().encode(password),'PBKDF2',false,['deriveKey']);
 return crypto.subtle.deriveKey({name:'PBKDF2',salt:salt as BufferSource,iterations:ITERATIONS,hash:'SHA-256'},material,{name:'AES-GCM',length:256},false,usage);
}
export async function encryptSave(state:StudyState,password:string){
 const plain=exportBackup(state);parseBackup(plain);
 if(new TextEncoder().encode(plain).length>8_000_000)throw new Error('在线存档目前支持 8MB 内的完整备份，请先下载 JSON 保管较大的记录。');
 const salt=crypto.getRandomValues(new Uint8Array(16)),iv=crypto.getRandomValues(new Uint8Array(12));
 const ciphertext=await crypto.subtle.encrypt({name:'AES-GCM',iv},await key(password,salt,['encrypt']),new TextEncoder().encode(plain));
 return JSON.stringify({format:'reading-encrypted-save',version:1,kdf:'PBKDF2-SHA256',iterations:ITERATIONS,salt:encode(salt),iv:encode(iv),data:encode(new Uint8Array(ciphertext))});
}
export async function decryptSave(text:string,password:string):Promise<StudyState>{
 if(text.length>MAX)throw new Error('在线存档超过大小限制');
 let root;try{root=JSON.parse(text);}catch{throw new Error('在线文件不是有效存档');}
 if(root?.format!=='reading-encrypted-save'||root.version!==1||root.kdf!=='PBKDF2-SHA256'||root.iterations!==ITERATIONS||!['salt','iv','data'].every(k=>typeof root[k]==='string'))throw new Error('在线存档格式或版本不匹配');
 let plain;try{
  const salt=decode(root.salt),iv=decode(root.iv),data=decode(root.data);
  if(salt.length!==16||iv.length!==12||data.length<16)throw new Error();
  plain=await crypto.subtle.decrypt({name:'AES-GCM',iv},await key(password,salt,['decrypt']),data);
 }catch{throw new Error('无法解密：请检查加密口令，或存档文件是否损坏。');}
 return parseBackup(new TextDecoder('utf-8',{fatal:true}).decode(plain));
}
function base(c:CloudConfig){
 if(!/^[a-z\d](?:[a-z\d-]{0,38})$/i.test(c.owner)||!/^[a-z\d_.-]{1,100}$/i.test(c.repo)||['.','..'].includes(c.repo))throw new Error('请填写有效的 GitHub 用户名和仓库名');
 if(!c.token.trim()||/[\r\n]/.test(c.token))throw new Error('请在本页填写仓库专用访问令牌');
 return `https://api.github.com/repos/${encodeURIComponent(c.owner)}/${encodeURIComponent(c.repo)}`;
}
async function request(c:CloudConfig,path:string,init:RequestInit={},missing=false){
 const url=base(c)+path;
 let res;try{res=await fetch(url,{...init,headers:{Accept:'application/vnd.github+json',Authorization:`Bearer ${c.token.trim()}`,'X-GitHub-Api-Version':'2026-03-10',...init.headers},cache:'no-store',credentials:'omit',redirect:'error',signal:AbortSignal.timeout(25000)});}catch{throw new Error('无法连接 GitHub，请检查网络；本机记录仍保留。');}
 if(missing&&res.status===404)return null;
 if(!res.ok)throw new Error(res.status===409||res.status===422?'在线存档有冲突或仓库分支不可写。请重新读取检查，勿覆盖另一设备的新进度。':res.status===401?'GitHub 令牌无效或已过期。':res.status===403?'GitHub 拒绝访问：请检查 Contents 读写权限、配额或组织限制。':res.status===404?'找不到仓库，或令牌无权访问。':`GitHub 请求失败（${res.status}），本机记录仍保留。`);
 return res;
}
async function privateRepo(c:CloudConfig){
 const r=await request(c,'');const repo=await r!.json();
 if(repo.private!==true||repo.visibility!=='private')throw new Error('在线存档只允许 Private 私有仓库；请勿使用公开的 Reading 网站仓库。');
 if(repo.archived||repo.disabled||!repo.default_branch)throw new Error('仓库不可写，请使用已初始化 README 的私有仓库。');
 return repo.default_branch as string;
}
export async function inspectCloud(c:CloudConfig):Promise<RemoteSave>{
 const branch=await privateRepo(c),r=await request(c,`/contents/${PATH}?ref=${encodeURIComponent(branch)}`,{},true);
 if(!r)return {sha:null,branch,state:null};
 const file=await r.json();
 if(file.type!=='file'||!/^[a-f\d]{40,64}$/i.test(file.sha)||!Number.isFinite(file.size)||file.size>MAX)throw new Error('在线存档不是有效文件，或超过大小限制');
 // Fetch immutable blob, so metadata, content and the conflict-check SHA always agree.
 const blob=await request(c,`/git/blobs/${file.sha}`,{headers:{Accept:'application/vnd.github.raw+json'}});
 return {sha:file.sha,branch,state:await decryptSave(await blob!.text(),c.password)};
}
export async function uploadCloud(c:CloudConfig,state:StudyState,expected:RemoteSave):Promise<RemoteSave>{
 const branch=await privateRepo(c);if(branch!==expected.branch)throw new Error('仓库默认分支已改变，请重新读取在线存档');
 const encrypted=await encryptSave(state,c.password);
 const r=await request(c,`/contents/${PATH}`,{method:'PUT',headers:{'Content-Type':'application/json'},body:JSON.stringify({message:'Update encrypted reading save',content:encode(new TextEncoder().encode(encrypted)),branch,...(expected.sha?{sha:expected.sha}:{})})});
 const result=await r!.json();if(!/^[a-f\d]{40,64}$/i.test(result.content?.sha))throw new Error('GitHub 未返回可验证的存档指纹，请重新读取检查');
 const uploaded={sha:result.content.sha,branch,state:structuredClone(state)};
 const verified=await inspectCloud(c);
 if(verified.sha!==uploaded.sha||JSON.stringify(verified.state)!==JSON.stringify(state))throw new Error('上传后校验不一致，请重新读取在线存档；本机记录仍保留。');
 return verified;
}
