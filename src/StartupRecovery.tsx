import {useState} from 'react';
import CloudArchive from './CloudArchive';
import {database,saveState} from './db';
import {emptyState,parseBackup} from './core';
import type {StudyState} from './types';

export default function StartupRecovery(){
 const [error,setError]=useState(''),[busy,setBusy]=useState(false);
 async function recover(state:StudyState){
  try{
   const db=await database();const revision=(await db.get('study','revision'))??0;db.close();
   if(!window.confirm(`恢复会替换本机学习数据，使用备份中的 ${state.attempts.length} 次作答与学习位置。确定恢复？`))return;
   setBusy(true);await saveState(state,undefined,revision);location.reload();
  }catch(e){setError((e as Error).message);setBusy(false);}
 }
 return <section className="startup-recovery"><h2>从备份恢复</h2><p>加载失败不会自动清空本机记录。可先重试加载，或在确认后使用完整备份替换。</p><label className="button">选择 JSON 备份<input aria-label="启动恢复 JSON 备份" type="file" accept=".json,application/json" hidden disabled={busy} onChange={async e=>{try{const file=e.target.files?.[0];if(file){if(file.size>50_000_000)throw new Error('备份超过50MB');await recover(parseBackup(await file.text()));}}catch(err){setError((err as Error).message);}e.target.value='';}}/></label>{error&&<p role="alert">{error}</p>}<CloudArchive restoreOnly state={emptyState()} disabled={busy} onRestore={recover}/></section>;
}
