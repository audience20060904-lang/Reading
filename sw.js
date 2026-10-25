const SCOPE=new URL(self.registration.scope).pathname;
const PREFIX='three-dimensions:'+SCOPE+':';
const CACHE=PREFIX+"bde5ee43f045dc95";
const FILES=["./assets/index-Bi_fhekW.css","./assets/index-U50cF4UG.js","./data/book.json","./data/coverage.json","./data/evidence-questions.json","./data/questions.json","./data/reading-plan.json","./figures/figure-1.png","./figures/figure-2.png","./figures/figure-3.png","./icon.svg","./index.html","./manifest.webmanifest"];
self.addEventListener('install',event=>event.waitUntil((async()=>{const c=await caches.open(CACHE);const requests=FILES.map(path=>new Request(new URL(path,self.registration.scope),{cache:'reload'}));await c.addAll(requests);await self.skipWaiting();})()));
self.addEventListener('activate',event=>event.waitUntil((async()=>{for(const k of await caches.keys())if(k.startsWith(PREFIX)&&k!==CACHE)await caches.delete(k);await self.clients.claim();})()));
self.addEventListener('fetch',event=>{const url=new URL(event.request.url);if(event.request.method!=='GET'||url.origin!==self.location.origin||!url.pathname.startsWith(SCOPE))return;
event.respondWith((async()=>{const cache=await caches.open(CACHE);const hit=await cache.match(event.request,{ignoreSearch:true});if(hit)return hit;
if(event.request.mode==='navigate'){const shell=await cache.match(new URL('./index.html',self.registration.scope));if(shell)return shell;}
return fetch(event.request);})());});
self.addEventListener('message',event=>{if(event.data==='VERSION')event.ports[0]?.postMessage({version:"bde5ee43f045dc95",cache:CACHE});});
