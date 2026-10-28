type Counts={total:number;correct:number;rate:number};
const groups:Record<string,string[]>={
 '细节与指代':['细节','比较','顺序','阅读顺序','指代'],
 '主旨与结构':['主旨','篇章结构','篇章联系'],
 '推断与证据':['推断','有限推断','证据判断','证据范围','研究结论','研究解释'],
 '作者意图与态度':['作者意图','观点归属','作者态度','作者观点','作者语气','修辞理解','比喻'],
 '语境词义':['语境词义','语境理解','语境含义'],
 '同义改写':['同义改写'],
 '逻辑与研究':['逻辑关系','指代与逻辑','研究设计','对话逻辑','研究逻辑','指代与概念','因果关系','语气与范围'],
 '语法理解':['语法与含义','语法与语境','语法']
};
const names=new Map(Object.entries(groups).flatMap(([group,labels])=>labels.map(label=>[label,group] as const)));
export function groupedQuestionTypes(raw:Record<string,Counts>):Record<string,Counts>{
 const result:Record<string,Counts>={};for(const [label,v] of Object.entries(raw)){const key=names.get(label)??label,group=result[key]??={total:0,correct:0,rate:0};group.total+=v.total;group.correct+=v.correct;group.rate=group.total?group.correct/group.total:0;}
 return Object.fromEntries([...Object.keys(groups),...Object.keys(result).filter(k=>!groups[k])].filter(k=>result[k]).map(k=>[k,result[k]]));
}
