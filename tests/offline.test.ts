import {describe,it,expect} from 'vitest';
import {readFileSync,existsSync} from 'node:fs';
describe('离线构建合同',()=>{
 it('离线构建脚本使用相对地址、隔离缓存、限定本地作用域',()=>{const text=readFileSync('scripts/build-offline.mjs','utf8');expect(text).toContain("'three-dimensions:'+SCOPE+':'");expect(text).toContain('url.origin!==self.location.origin');expect(text).toContain('c.addAll(requests)');expect(text).toContain("cache:'reload'");expect(text).toContain('readFile(new URL(import.meta.url))');expect(text).toContain('k.startsWith(PREFIX)');expect(text).toContain("new URL('./index.html',self.registration.scope)");});
 it('manifest 的启动入口、scope、图标均为相对路径',()=>{const m=JSON.parse(readFileSync('public/manifest.webmanifest','utf8'));expect(m.start_url).toBe('./');expect(m.scope).toBe('./');expect(m.icons[0].src).not.toMatch(/^\//);});
 it('运行时不接入 AI API、远程字体或学习数据库',()=>{const files=['src/App.tsx','src/core.ts','src/db.ts','src/style.css'].map(p=>readFileSync(p,'utf8')).join('\n');expect(files).not.toMatch(/api\.openai|api\.anthropic|generativelanguage|fonts\.googleapis|firebase|supabase/);expect(readFileSync('package.json','utf8')).not.toMatch(/openai|anthropic/);});
 it('生产离线清单若存在则覆盖正文、题库、HTML 和 JS/CSS',()=>{if(existsSync('dist/offline-manifest.json')){const m=JSON.parse(readFileSync('dist/offline-manifest.json','utf8'));expect(m.files).toContain('./index.html');expect(m.files).toContain('./data/book.json');expect(m.files).toContain('./data/questions.json');expect(m.files.some((p:string)=>p.endsWith('.js'))).toBe(true);expect(m.files.some((p:string)=>p.endsWith('.css'))).toBe(true);}});
});
