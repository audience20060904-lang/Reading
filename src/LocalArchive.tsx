import {useEffect,useState} from 'react';
import {localCheckpoints} from './db';
import type {LocalCheckpoint} from './db';
import type {StudyState} from './types';
export default function LocalArchive({state,onRestore}:{state:StudyState;onRestore:(s:StudyState)=>void}){
 const [points,setPoints]=useState<LocalCheckpoint[]>([]),[notice,setNotice]=useState('');
 useEffect(()=>{let live=true;localCheckpoints().then(p=>{if(live)setPoints(p);}).catch(()=>{if(live)setNotice('恢复点暂时不可用，请下载 JSON 备份');});return()=>{live=false;};},[state.updatedAt]);
 return <section className="panel"><h2>自动保存与恢复点</h2><p className="muted">选择、提交、位置和阅读偏好即时保存；未提交题目的用时每 5 秒保存。最近 3 次不同状态在同一事务内保留恢复点，单纯计时不挤掉恢复点。恢复前仍需确认。</p><div className="setting-row"><span>减少浏览器自动清理 <small>{notice||'可申请持久存储，不能替代备份'}</small></span><button onClick={async()=>{try{setNotice(await navigator.storage?.persist?.()?'已获得持久存储；主动清除数据仍会删除记录':'浏览器未授予持久存储，请定期备份');}catch{setNotice('此浏览器暂不支持申请，请定期备份');}}}>保护本机存档</button></div>{points.map((p,i)=><div className="setting-row" key={i}><span>{new Date(p.savedAt).toLocaleString('zh-CN')}<small>{p.state.attempts.length} 次作答 · {p.state.readingUnitId||'尚未开始'}</small></span><button onClick={()=>onRestore(p.state)}>恢复此记录</button></div>)}{!points.length&&<p className="muted small">还没有恢复点。下一次改变学习状态后会自动保留。</p>}</section>;
}
