import {createServer} from 'node:http';
import {readFile,mkdir,writeFile} from 'node:fs/promises';
import {resolve,sep,extname} from 'node:path';
import {createHash} from 'node:crypto';
import {pathToFileURL} from 'node:url';
import assert from 'node:assert/strict';
let chromium;try{({chromium}=await import('playwright'));}catch{({chromium}=await import(pathToFileURL(resolve(process.env.USERPROFILE||'','.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules/playwright/index.mjs')).href));}
const root=resolve('dist'),mime={'.html':'text/html','.js':'text/javascript','.css':'text/css','.json':'application/json','.svg':'image/svg+xml','.webmanifest':'application/manifest+json'};
let server;let base=process.env.READING_TEST_URL;
if(!base){server=createServer(async(req,res)=>{try{const p=new URL(req.url,'http://local').pathname.replace(/^\/Reading\//,'/'),file=resolve(root,'.'+(p==='/'?'/index.html':p));assert(file.startsWith(root+sep));const data=await readFile(file);res.writeHead(200,{'Content-Type':mime[extname(file)]||'application/octet-stream','Cache-Control':'no-store'});res.end(data);}catch{res.writeHead(404);res.end();}});await new Promise(r=>server.listen(4189,'127.0.0.1',r));base='http://127.0.0.1:4189/Reading/';}
const live=!!process.env.READING_TEST_URL,bank=JSON.parse(await readFile('public/data/questions.json','utf8')),book=JSON.parse(await readFile('public/data/book.json','utf8')),plan=JSON.parse(await readFile('public/data/reading-plan.json','utf8')),manifest=JSON.parse(await readFile('dist/offline-manifest.json','utf8'));
const report={url:base,checks:[],limits:['隔离 Edge 中合成作答；390px 视口不是实体手机；离线为浏览器模拟。']};
const check=s=>{report.checks.push(s);console.log('PASS '+s);};await mkdir('qa',{recursive:true});
const browser=await chromium.launch({headless:true,...(process.platform==='win32'?{executablePath:process.env.BROWSER_PATH||'C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe'}:{})});
const ctx=await browser.newContext({viewport:{width:390,height:844}}),page=await ctx.newPage();const errors=[];page.on('pageerror',e=>errors.push(String(e)));
const state=()=>page.evaluate(()=>new Promise((resolve,reject)=>{const r=indexedDB.open('life-three-dimensions-study-v1',1);r.onsuccess=()=>{const db=r.result,q=db.transaction('study').objectStore('study').get('state');q.onsuccess=()=>{db.close();resolve(q.result);};q.onerror=reject;};r.onerror=reject;}));
try{
 for(const p of [...manifest.files,'./sw.js']){const r=await page.request.get(new URL(p,base).href+'?verify='+manifest.version);assert.equal(r.status(),200,p);assert.equal(createHash('sha256').update(await r.body()).digest('hex'),createHash('sha256').update(await readFile(resolve(root,p))).digest('hex'),p);}
 check('线上或本地全部静态资源逐字节匹配已测构建');
 await page.goto(base);await page.locator('.question-prompt').waitFor();
 const units=plan.units.filter(u=>u.chapterId==='c01'),texts=[];let right=0;
 for(let i=0;i<units.length;i++){
  const q=bank.find(q=>q.id===units[i].questionId);await page.getByRole('heading',{name:q.prompt,exact:true}).waitFor();
  texts.push(await page.locator('.passage').innerText());assert.equal(texts.at(-1),q.passage);assert.equal(await page.locator('.explanation').count(),0);assert.equal(await page.getByRole('radio').count(),4);assert(await page.getByRole('button',{name:'下一段',exact:true}).isDisabled());
  const selected=i%7===0?(q.answer+1)%4:q.answer;if(selected===q.answer)right++;
  await page.getByRole('radio').nth(selected).click();await page.getByRole('button',{name:'提交答案',exact:true}).click();await page.locator('.explanation').waitFor();
  assert.equal(await page.locator('.passage').innerText(),q.passage);assert.deepEqual(await page.locator('.explain-body h3').allTextContents(),['一、问题与选项分析','二、重点词汇','三、原文整段参考译文']);assert.equal(await page.locator('.option-translation').count(),4);assert((await page.locator('.passage-translation').innerText()).includes(q.translation));assert(await page.evaluate(()=>document.documentElement.scrollWidth<=innerWidth));
  if(q.id==='q-c01-058')await page.locator('.explanation').screenshot({path:`qa/chapter01-${live?'live':'local'}-bilingual.png`,animations:'disabled'});
  if((i+1)%20===0)console.log(`Verified ${i+1}/77 reading units`);
  if(i<units.length-1)await page.getByRole('button',{name:'下一段',exact:true}).click();
 }
 assert.equal(texts.join(' '),book.paragraphs.filter(p=>p.chapterId==='c01').map(p=>p.text).join(' '));check('逐段走完第 1 章 77 段、177 候选句，无跳段、漏句或重复');check('全部新增题提交前隐藏、提交后三类双语解析及整段译文正确，手机无溢出');
 const completed=await state();assert.equal(completed.attempts.length,77);assert.equal(completed.attempts.filter(a=>a.correct).length,right);
 await page.reload();await page.locator('.explanation').waitFor();assert.deepEqual((await state()).attempts,completed.attempts);await page.getByRole('button',{name:'学习统计',exact:true}).click();assert.deepEqual(await page.locator('.stat-card strong').allTextContents(),['77','77',String(right),(right/77*100).toFixed(1)+'%']);
 await page.locator('.history-row').first().click();await page.locator('.explanation').waitFor();assert.equal(await page.locator('.passage').innerText(),completed.attempts.at(-1).snapshot.passage);assert.equal((await state()).attempts.length,77);check('77 次独立作答统计正确，刷新及回看最近历史均不重复计分');
 await page.evaluate(async()=>{await navigator.serviceWorker.ready;if(!navigator.serviceWorker.controller)await new Promise(r=>navigator.serviceWorker.addEventListener('controllerchange',r,{once:true}));});await ctx.setOffline(true);await page.reload();await page.locator('.explanation').waitFor();assert.equal((await state()).attempts.length,77);assert.equal(errors.length,0,errors.join('\n'));check('整章学习后模拟离线重载恢复历史解析，无运行时错误');report.passed=true;
}catch(e){report.passed=false;report.error=String(e);process.exitCode=1;console.error(e);await page.screenshot({path:`qa/chapter01-${live?'live':'local'}-failure.png`,fullPage:true,animations:'disabled'}).catch(()=>{});}
finally{await writeFile(`qa/chapter01-${live?'live':'local'}-results.json`,JSON.stringify(report,null,2));await browser.close();if(server)await new Promise(r=>server.close(r));}
