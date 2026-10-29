import {readFileSync} from 'node:fs';
import {describe,it,expect} from 'vitest';
const read=(p:string)=>JSON.parse(readFileSync(p,'utf8')),catalog=read('src/data/question-revision-catalog.json');
const q=(id:string)=>catalog.questions.find((v:any)=>v.id===id);
describe('第四十四批：研究比较基准与范围',()=>{
 it('情绪的丰富日子比较明确以typical day为基准',()=>{
  const v=q('q-c05-029');expect(v.options[v.answer]).toContain('than a typical day');expect(v.optionsZh[v.answer]).toContain('比平常日子');expect(v.analyses[v.answer]).toContain('不能把后者基准换成幸福日子');expect(v.evidence[1].quote).toContain('than on a typical day');
 });
 it('三题结果译文保留多数学生报告与日子单位，不加入编辑说明',()=>{
  const ids=['q-c05-026','qe-c05-0045','qe-c05-0046'];for(const id of ids){expect(q(id).translation).toBe(q(ids[0]).translation);expect(q(id).translation).toContain('多数学生报告');expect(q(id).translation).toContain('那一天');expect(q(id).translation).not.toContain('这是原书');}expect(q(ids[0]).passage).toContain('enhanced');
 });
 it('well-being三方面不混成只有幸福，清单保留视频游戏类型',()=>{
  expect(q('qe-c05-0043').promptZh).toContain('幸福、意义和心理丰富');expect(q('qe-c05-0045').optionsZh[3]).toContain('幸福、意义和心理丰富');expect(q('q-c05-025').options[2]).toContain('video games');expect(q('qe-c05-0046').analyses[0]).toContain('not only psychological richness but also happiness and meaning');
 });
 it('排名是条件强推断，额外49页仅记为来源段上下文',()=>{
  const v=q('qe-c05-0052');expect(v.passage.startsWith('If novelty')).toBe(true);expect(v.translation).toContain('想必');expect(v.translation).not.toContain('留学必然');const r=read('source/question-revisions/review-044-report.json');expect(r.manual.pdfPagesForQuestionEvidence).toEqual([47,48]);expect(r.manual.additionalParagraphContextPages).toEqual([49]);expect(r.fullQuestionBankHumanReview).toBe(false);
 });
});
