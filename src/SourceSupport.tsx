import type {Book,ReadingPlan,ReadingUnit,SupportMaterial} from './types';

export function sectionItems(book:Book,plan:ReadingPlan,sectionId:string) {
 const units=plan.units.filter(u=>u.sectionId===sectionId).map(unit=>({kind:'unit' as const,unit}));
 const support=(book.supportMaterials??[]).filter(m=>m.sectionId===sectionId).map(material=>({kind:'support' as const,material}));
 const source=(item:{kind:'unit';unit:ReadingUnit}|{kind:'support';material:SupportMaterial})=>item.kind==='support'?item.material.sources[0]:book.paragraphs.find(p=>p.id===item.unit.paragraphId)!.sources[0];
 return [...units,...support].sort((a,b)=>source(a).pdfPage-source(b).pdfPage||source(a).block-source(b).block);
}

export default function SourceSupport({material:m}:{material:SupportMaterial}) {
 return <aside className="source-support" data-support-id={m.id}>
  <p className="source-meta">PDF {m.sources[0].pdfPage} · {m.id} · 原页已核对 · 辅助材料</p>
  <h3 lang="en">{m.title}</h3>
  {m.image&&<img src={import.meta.env.BASE_URL+m.image} alt={m.title} loading="lazy"/>}
  {m.columns&&m.rows&&<div className="table-scroll"><table lang="en"><thead><tr>{m.columns.map((s,i)=><th key={i} scope="col">{s}</th>)}</tr></thead><tbody>{m.rows.map((row,i)=><tr key={i}>{row.map((s,j)=>j===0?<th key={j} scope="row">{s}</th>:<td key={j}>{s}</td>)}</tr>)}</tbody></table></div>}
  {m.columns&&<p className="source-table-hint">左右滑动查看完整表格</p>}
  <details><summary>原始提取与来源位置</summary>{m.sources.map(s=><div key={s.block}><small>PDF {s.pdfPage} · block {s.block} · bbox {s.bbox.join(', ')}</small><pre lang="en">{s.raw}</pre></div>)}</details>
  {m.kind!=='subheading'&&<p className="muted small">按原页恢复图表与说明，不计入叙事候选句子、配题数或学习成绩。</p>}
 </aside>;
}
