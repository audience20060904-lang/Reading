import {describe,it,expect} from 'vitest';
import {mkdtempSync,mkdirSync,writeFileSync,readFileSync,rmSync,realpathSync} from 'node:fs';
import {tmpdir} from 'node:os';
import {join,resolve,dirname,basename} from 'node:path';
import {execFileSync} from 'node:child_process';
const build=resolve('scripts/build-offline.mjs'),pages=resolve('scripts/prepare-github-pages.mjs');
function fixture(run:(dir:string)=>void){
 const parent=realpathSync(tmpdir()),dir=mkdtempSync(join(parent,'reading-offline-'));
 try{
  mkdirSync(join(dir,'dist','assets'),{recursive:true});mkdirSync(join(dir,'dist','data'));
  writeFileSync(join(dir,'dist','index.html'),'<html><head><link rel="stylesheet" href="./assets/style.css"></head><body><script type="module" src="./assets/index-jw90lmsw.js"></script></body></html>');
  writeFileSync(join(dir,'dist','assets','index-jw90lmsw.js'),'globalThis.readingFixture=true;');writeFileSync(join(dir,'dist','assets','style.css'),'body{color:black}');
  writeFileSync(join(dir,'dist','sw.js'),'old worker');writeFileSync(join(dir,'dist','data','book.json'),'{}');writeFileSync(join(dir,'dist','data','questions.json'),'[]');
  writeFileSync(join(dir,'dist','manifest.webmanifest'),JSON.stringify({scope:'./',start_url:'./'}));
  run(dir);
 }finally{
  const target=realpathSync(dir);if(dirname(target)!==parent||!basename(target).startsWith('reading-offline-'))throw Error('Unexpected fixture cleanup target');rmSync(target,{recursive:true,force:true});
 }
}
describe('离线发布的启动资源完整性',()=>{
 it('散列名以sw.js结尾的应用脚本仍被缓存，只排除根Service Worker',()=>fixture(dir=>{
  execFileSync(process.execPath,[build],{cwd:dir});const m=JSON.parse(readFileSync(join(dir,'dist','offline-manifest.json'),'utf8'));
  expect(m.files).toContain('./assets/index-jw90lmsw.js');expect(m.files).not.toContain('./sw.js');expect(readFileSync(join(dir,'dist','sw.js'),'utf8')).toContain('./assets/index-jw90lmsw.js');
 }));
 it('资源虽存在但启动脚本不在离线清单时拒绝发布',()=>fixture(dir=>{
  execFileSync(process.execPath,[build],{cwd:dir});const p=join(dir,'dist','offline-manifest.json'),m=JSON.parse(readFileSync(p,'utf8'));m.files=m.files.filter((v:string)=>!v.endsWith('index-jw90lmsw.js'));writeFileSync(p,JSON.stringify(m));
  expect(()=>execFileSync(process.execPath,[pages],{cwd:dir,stdio:'pipe'})).toThrow();
 }));
});
