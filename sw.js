const SCOPE=new URL(self.registration.scope).pathname;
const PREFIX='three-dimensions:'+SCOPE+':';
const CACHE=PREFIX+"f458ec333a9dc261";
const FILES=["./assets/index-BGwPKRvu.js","./assets/index-okYbXdP-.css","./data/book.json","./data/coverage.json","./data/questions.json","./icon.svg","./index.html","./manifest.webmanifest"];
self.addEventListener('install',event=>event.waitUntil((async()=>{const c=await caches.open(CACHE);await c.addAll(FILES);await self.skipWaiting();})()));
self.addEventListener('activate',event=>event.waitUntil((async()=>{for(const k of await caches.keys())if(k.startsWith(PREFIX)&&k!==CACHE)await caches.delete(k);await self.clients.claim();})()));
self.addEventListener('fetch',event=>{const url=new URL(event.request.url);if(event.request.method!=='GET'||url.origin!==self.location.origin||!url.pathname.startsWith(SCOPE))return;
event.respondWith((async()=>{const cache=await caches.open(CACHE);const hit=await cache.match(event.request,{ignoreSearch:true});if(hit)return hit;
if(event.request.mode==='navigate'){const shell=await cache.match(new URL('./index.html',self.registration.scope));if(shell)return shell;}
return fetch(event.request);})());});
self.addEventListener('message',event=>{if(event.data==='VERSION')event.ports[0]?.postMessage({version:"f458ec333a9dc261",cache:CACHE});});
