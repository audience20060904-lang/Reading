import {readdir,readFile,writeFile} from 'node:fs/promises';
import {createHash} from 'node:crypto';
import {join,relative} from 'node:path';
const root='dist';
async function files(dir){return (await Promise.all((await readdir(dir,{withFileTypes:true})).map(e=>e.isDirectory()?files(join(dir,e.name)):[join(dir,e.name)]))).flat();}
const paths=(await files(root)).filter(p=>!p.endsWith('sw.js'));
const hash=createHash('sha256');for(const p of paths.sort())hash.update(await readFile(p));
const version=hash.digest('hex').slice(0,16),urls=paths.map(p=>'./'+relative(root,p).replaceAll('\\','/'));
// Scoped cache identity prevents / and /repo/ installations from deleting one another.
const worker=`const SCOPE=new URL(self.registration.scope).pathname;
const PREFIX='three-dimensions:'+SCOPE+':';
const CACHE=PREFIX+${JSON.stringify(version)};
const FILES=${JSON.stringify(urls)};
self.addEventListener('install',event=>event.waitUntil((async()=>{const c=await caches.open(CACHE);await c.addAll(FILES);await self.skipWaiting();})()));
self.addEventListener('activate',event=>event.waitUntil((async()=>{for(const k of await caches.keys())if(k.startsWith(PREFIX)&&k!==CACHE)await caches.delete(k);await self.clients.claim();})()));
self.addEventListener('fetch',event=>{const url=new URL(event.request.url);if(event.request.method!=='GET'||url.origin!==self.location.origin||!url.pathname.startsWith(SCOPE))return;
event.respondWith((async()=>{const cache=await caches.open(CACHE);const hit=await cache.match(event.request,{ignoreSearch:true});if(hit)return hit;
if(event.request.mode==='navigate'){const shell=await cache.match(new URL('./index.html',self.registration.scope));if(shell)return shell;}
return fetch(event.request);})());});
self.addEventListener('message',event=>{if(event.data==='VERSION')event.ports[0]?.postMessage({version:${JSON.stringify(version)},cache:CACHE});});
`;
await writeFile(join(root,'sw.js'),worker);
await writeFile(join(root,'offline-manifest.json'),JSON.stringify({version,files:urls,scope:'relative',notice:'首次完整缓存后离线可用。缓存随构建内容指纹更新，学习记录位于独立 IndexedDB。'},null,2));
console.log(`Offline cache ${version}: ${urls.length} assets, relative scope.`);
