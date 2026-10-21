// Regression: a new SW must not copy an old, still-fresh HTTP response into its cache.
import {createServer} from 'node:http';
import {readFile,writeFile,mkdir} from 'node:fs/promises';
import {resolve,extname,join,sep} from 'node:path';
import {pathToFileURL} from 'node:url';
import assert from 'node:assert/strict';
let chromium;
try{({chromium}=await import('playwright'));}catch{({chromium}=await import(pathToFileURL(join(process.env.USERPROFILE||'','.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules/playwright/index.mjs')).href));}
const root=resolve('dist'),bank=JSON.parse(await readFile(join(root,'data/questions.json'),'utf8'));
const baseline=JSON.parse(await readFile('tests/fixtures/batch002-fingerprints.json','utf8'));
const legacy=JSON.stringify(bank.filter(q=>baseline[q.id]));
const worker=await readFile(join(root,'sw.js'),'utf8'),version=JSON.parse(await readFile(join(root,'offline-manifest.json'),'utf8')).version;
const oldWorker=worker.replace('await c.addAll(requests)','await c.addAll(FILES)');
assert.notEqual(worker,oldWorker,'Regression needs the current install code');
let phase=0,questionFetches=0;
const mime={'.html':'text/html','.js':'text/javascript','.css':'text/css','.json':'application/json','.svg':'image/svg+xml','.webmanifest':'application/manifest+json'};
const server=createServer(async(req,res)=>{try{
 let path=decodeURIComponent(new URL(req.url,'http://localhost').pathname);
 if(!path.startsWith('/Reading/'))throw Error('wrong scope');path=path.slice('/Reading'.length);if(path==='/')path='/index.html';
 const file=resolve(root,'.'+path);if(!file.startsWith(root+sep))throw Error('path denied');
 let data;
 if(path==='/sw.js')data=phase===2?worker:oldWorker.replaceAll(version,(phase===0?'old-':'stale-')+version);
 else if(path==='/data/questions.json'){questionFetches++;data=phase===0?legacy:JSON.stringify(bank);}
 else data=await readFile(file);
 res.writeHead(200,{'Content-Type':mime[extname(path)]||'application/octet-stream','Cache-Control':path==='/sw.js'?'no-cache':'public, max-age=3600'});res.end(data);
}catch{res.writeHead(404);res.end('Not found');}});
await new Promise(r=>server.listen(4188,'127.0.0.1',r));
const browser=await chromium.launch({headless:true,...(process.platform==='win32'?{executablePath:process.env.BROWSER_PATH||'C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe'}:{})});
const page=await browser.newPage({viewport:{width:390,height:844}}),result={checks:[],passed:false};
const check=s=>{result.checks.push(s);console.log('PASS '+s);};
async function waitVersion(expected){
 for(let i=0;i<100;i++){
  const actual=await page.evaluate(()=>new Promise(resolve=>{const c=navigator.serviceWorker.controller;if(!c){resolve(null);return;}const ch=new MessageChannel(),t=setTimeout(()=>resolve(null),500);ch.port1.onmessage=e=>{clearTimeout(t);resolve(e.data.version);};c.postMessage('VERSION',[ch.port2]);}));
  if(actual===expected)return;
  await new Promise(r=>setTimeout(r,200));
 }
 throw new Error('Worker did not activate version '+expected);
}
const state=()=>page.evaluate(()=>new Promise((resolve,reject)=>{const r=indexedDB.open('life-three-dimensions-study-v1',1);r.onsuccess=()=>{const db=r.result,q=db.transaction('study').objectStore('study').get('state');q.onsuccess=()=>{db.close();resolve(q.result);};q.onerror=reject;};r.onerror=reject;}));
try{
 await page.goto('http://127.0.0.1:4188/Reading/');await page.locator('.question-prompt').waitFor();assert((await page.locator('.session-count').innerText()).includes('/ 45'));
 await page.getByRole('radio').nth(0).click();await page.getByRole('button',{name:'提交答案',exact:true}).click();await page.locator('.explanation').waitFor();await waitVersion('old-'+version);
 const before=await state();assert.equal(before.attempts.length,1);
 phase=1;await page.evaluate(async()=>{await (await navigator.serviceWorker.getRegistration()).update();});await waitVersion('stale-'+version);await page.reload();await page.locator('.explanation').waitFor();
 assert((await page.locator('.session-count').innerText()).includes('/ 45'));check('复现旧策略将仍有效的 45 题 HTTP 缓存复制进新 SW 缓存');
 const hits=questionFetches;
 phase=2;await page.evaluate(async()=>{await (await navigator.serviceWorker.getRegistration()).update();});await waitVersion(version);await page.reload();await page.locator('.explanation').waitFor();
 assert((await page.locator('.session-count').innerText()).includes('/ 60'));assert(questionFetches>hits,'New install must refresh questions from server');assert.deepEqual((await state()).attempts,before.attempts);assert.equal((await state()).session.attemptId,before.session.attemptId);
 assert((await page.locator('.passage-translation').innerText()).includes('种植水稻和茶叶'));check('修复后安装强制刷新正文题库至 60 题，并保留旧成绩、位置与译文');result.passed=true;
}catch(e){result.error=String(e);console.error(e);process.exitCode=1;await page.screenshot({path:'qa/cache-update-failure.png',fullPage:true}).catch(()=>{});}
finally{await mkdir('qa',{recursive:true});await writeFile('qa/cache-update-results.json',JSON.stringify(result,null,2));await browser.close();await new Promise(r=>server.close(r));}
