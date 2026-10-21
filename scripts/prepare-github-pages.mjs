import {readFile,writeFile,stat} from 'node:fs/promises';
import assert from 'node:assert/strict';
import {resolve,sep} from 'node:path';

// Run after the regular build. Relative URLs work at /Reading/ without a server rewrite.
const root=resolve('dist');
const base=new URL('https://audience20060904-lang.github.io/Reading/');
const html=await readFile(resolve(root,'index.html'),'utf8');
const cache=JSON.parse(await readFile(resolve(root,'offline-manifest.json'),'utf8'));
const manifest=JSON.parse(await readFile(resolve(root,'manifest.webmanifest'),'utf8'));
assert.equal(manifest.scope,'./');
assert.equal(manifest.start_url,'./');
const urls=[...cache.files,...[...html.matchAll(/(?:src|href)="([^"]+)"/g)].map(m=>m[1])];
for(const path of urls){
  const url=new URL(path,base);
  assert.equal(url.origin,base.origin,`External resource: ${path}`);
  assert(url.pathname.startsWith(base.pathname),`Resource escapes /Reading/: ${path}`);
  const file=resolve(root,decodeURIComponent(url.pathname.slice(base.pathname.length)));
  assert(file.startsWith(root+sep),`Invalid resource path: ${path}`);
  assert((await stat(file)).isFile(),`Missing resource: ${path}`);
}
assert(cache.files.includes('./data/book.json'));
assert(cache.files.includes('./data/questions.json'));
await stat(resolve(root,'sw.js'));
await writeFile(resolve(root,'.nojekyll'),'');
console.log(`GitHub Pages ready: dist/ (${cache.files.length} cached resources, /Reading/ validated).`);
console.log('Publish dist contents to gh-pages, then select gh-pages / (root) in Settings > Pages.');
