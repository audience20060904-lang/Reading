import {readFileSync,existsSync} from 'node:fs';
import {createHash} from 'node:crypto';
import {describe,it,expect} from 'vitest';
const read=(p:string)=>JSON.parse(readFileSync(p,'utf8')),catalog=read('src/data/question-revision-catalog.json');
const q=(id:string)=>catalog.questions.find((v:any)=>v.id===id);
const canonical=(v:any):string=>Array.isArray(v)?'['+v.map(canonical).join(',')+']':v&&typeof v==='object'?'{'+Object.keys(v).sort().map(k=>JSON.stringify(k)+':'+canonical(v[k])).join(',')+'}':JSON.stringify(v);
describe('第十八批：类比当前证据与释义修订历史',()=>{
 it('累积总数对照变化平均数，不依赖未显示的经历定义',()=>{
  const v=q('q-c01-029');expect(v.options[v.answer]).toContain('cumulative');expect(v.options[v.answer]).toContain('changing average');expect(v.translation).toContain('打击率');expect(v.analyses[0]).not.toContain('物质财富');
 });
 it('often限定保留，解释不借前后原句',()=>{
  expect(q('q-c01-030').analyses[0]).not.toContain('suits the curious');expect(q('q-c01-030').analyses[1]).not.toContain('some people');expect(q('q-c01-032').analyses[2]).not.toContain('前文');
 });
 it('已发布的查词修订记录有不可变指纹，后续新增不覆盖旧记录',()=>{
  const lexical=read('src/data/word-lookup-revisions.json'),manifest=read('source/question-revisions/manifest.json');let count=0;
  for(const batch of manifest.batches){if(!existsSync(batch.receipt))continue;const receipt=read(batch.receipt);for(const saved of receipt.lookupRevisionFingerprints??[]){const matches=lexical.updates.filter((r:any)=>r.revisionId===saved.revisionId&&r.occurrenceId===saved.occurrenceId);expect(matches).toHaveLength(1);expect(createHash('sha256').update(canonical(matches[0])).digest('hex')).toBe(saved.sha256);count++;}}
  expect(count).toBeGreaterThanOrEqual(3);
 });
});
