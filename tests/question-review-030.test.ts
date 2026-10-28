import {readFileSync} from 'node:fs';
import {describe,it,expect} from 'vitest';
const read=(p:string)=>JSON.parse(readFileSync(p,'utf8')),catalog=read('src/data/question-revision-catalog.json');
const q=(id:string)=>catalog.questions.find((v:any)=>v.id===id);
describe('第三十批：计数单位、代词和鼓励语气',()=>{
 it('6000计数保持婴儿数量而非分娩事件，over和历史时间范围不丢',()=>{
  const v=q('qe-c03-0019');expect(v.answer).toBe(1);expect(v.options[v.answer]).toContain('over 6,000 babies');expect(v.options[v.answer]).toContain('twenty-year period described');expect(v.options[v.answer]).not.toContain('deliveries');expect(v.evidence[0].quote).toContain('over 6,000 babies');
 });
 it('职业段代词和主张归属保留，不擅换成职业存在',()=>{
  const ids=['q-c03-009','qe-c03-0012','qe-c03-0013'];for(const id of ids)expect(q(id).translation).toBe(q(ids[0]).translation);expect(q(ids[0]).translation).toContain('他声称，多数公司律师');expect(q(ids[0]).translation).toContain('若没有他们');expect(q(ids[0]).translation).not.toContain('自己这类职业不存在');
 });
 it('祈使是号召听众行动，不是已完成、由演讲者包办或全员保证',()=>{
  const v=q('qe-c03-0017');expect(v.answer).toBe(2);expect(v.options[3]).toContain('unconditional promise');expect(v.options[v.answer]).toContain('urges the listeners');expect(v.analyses[1]).toContain('行动者');
 });
 it('联想不添first，产品解析不塞保存拼写记录或未显示未来段落',()=>{
  const v=q('qe-c03-0020');expect(v.options[v.answer]).toBe('We may think of people who have done great things.');expect(q('qe-c03-0018').passage).toContain('Michele Obama');expect(q('qe-c03-0018').analyses.join(' ')).not.toContain('保留原书');expect(q('qe-c03-0021').analyses[3]).not.toContain('后面还');expect(q('qe-c03-0022').analyses[0]).toContain('本段开头');
 });
});
