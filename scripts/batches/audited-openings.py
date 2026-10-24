"""3 individually authored exercises for frozen targets, PDF pages 144 and 160.
Preserve printed English, source positions and all previously published questions.
"""
from pathlib import Path
import json,hashlib
ROOT=Path(__file__).resolve().parents[2]
load=lambda p:json.loads((ROOT/p).read_text(encoding='utf8'))
b=load('public/data/book.json');plan=load('public/data/reading-plan.json');targets=load('source/short-questions/batch043-targets.json')['targets']
ss={s['id']:s for s in b['sentences']};pp={p['id']:p for p in b['paragraphs']};out=[]
def add(i,kind,prompt,options,answer,prompt_zh,options_zh,analyses,quotes,word,meaning,context,example,collocations,translation,support='explicit'):
 t=targets[i-1];u=next(u for u in plan['units'] if u['id']==t['readingUnitId']);group=[ss[sid] for sid in u['sentenceIds']];p=pp[u['paragraphId']];text=p['text'][group[0]['start']:group[-1]['end']]
 assert hashlib.sha256(text.encode()).hexdigest()==t['passageSha256'];evidence=[]
 for quote in quotes:
  offset=text.find(quote);assert offset>=0,(i,quote);start=group[0]['start']+offset;end=start+len(quote);touching=[s for s in group if s['start']<end and s['end']>start]
  evidence.append(dict(quote=quote,sentenceIds=[s['id'] for s in touching],sources=list({(r['pdfPage'],r['block']):r for s in touching for r in s['sources']}.values())))
 assert word.lower() in text.lower(),(i,word)
 out.append(dict(id=t['questionId'],version=1,readingUnitId=u['id'],chapterId=u['chapterId'],sectionId=u['sectionId'],paragraphId=u['paragraphId'],sentenceIds=u['sentenceIds'],passage=text,prompt=prompt,options=options,answer=answer,type=kind,promptZh=prompt_zh,optionsZh=options_zh,analyses=analyses,evidence=evidence,vocabulary=[dict(word=word,meaning=meaning,context=context,example=example,collocations=collocations)],translation=translation,support=support,editorialStatus='PDF144与160原页逐字核对新增章首作者正文；只增加缺失来源，不改写1053已发布题目。'))

add(1,'细节','What question does the author acknowledge sharing with the reader?',
 ['Whether exploration has no possible value.','Whether psychological richness can become excessive.','Whether happiness has already replaced every other ideal.','Whether the book has avoided discussing curiosity.'],1,
 '作者承认自己与读者共有的疑问是什么？',['探索是否完全没有价值。','心理丰富是否也可能过多。','快乐是否已经取代其他所有理想。','本书是否一直没谈好奇心。'],
 ['A I hope…there is a point说明希望读者认可价值，不是否认任何价值。','B too much psychological richness后接I do, too，直接承认自己也有这疑问。','C 未称快乐取代其他理想。','D exploration/curiosity/richness正是这里回顾的主题。'],
 ['But, first, you might be wondering if there is such a thing as too much psychological richness? I do, too.'],
 'touch on','简要谈及；涉及','为结论前要讨论的两个问题作引介','The introduction touches on two unresolved questions.',['touch on a question','reach a conclusion'],
 '在到达本书结论之前，我想谈谈剩下的两个问题。希望到现在你已认同，探索、好奇与心理丰富的人生有其价值。但首先，你也许会想：心理丰富是否也可能过多？我也有这个疑问。')

add(2,'逻辑关系','What possibility is raised in contrast to the earlier emphasis on “go”?',
 ['Familiar people must be left behind before a life can become rich.','Moving is guaranteed to produce more richness than staying.','Psychological richness might also come from staying and familiar people or things.','Every earlier facilitator has required moving to another country.'],2,
 '与先前偏向“走”的强调相比，作者提出什么可能？',['必须离开熟人才可能丰富。','迁移保证比留下更丰富。','留下以及熟悉的人或物，也可能带来心理丰富。','每种先前促进因素都要求移居国外。'],
 ['A Can we…from familiar objects and people恰是在探讨相反可能。','B 此处是问题，没有保证比较结果。','C Can we also…by staying与familiar objects and people构成对照，保留疑问而非既定结论。','D most不能改为every；go也不等于必须跨国迁移。'],
 ['Can we also gain psychological richness by staying, or from familiar objects and people?'],
 'facilitators','促进因素','指前文讨论的促进心理丰富的因素，不一定是组织活动的主持人','Curiosity can be a facilitator of learning.',['facilitators of exploration','gain richness from'],
 '其次，目前讨论过的多数心理丰富促进因素偏向“走”而非“留”。我们也能通过留下，或从熟悉的物品和人身上，获得心理丰富吗？')

add(3,'主旨','How does the author position a psychologically rich life in this opening?',
 ['As an additional path alongside happiness and meaning.','As a concept that makes happy and meaningful lives impossible.','As a scientific replacement for all earlier ideas of a good life.','As an instruction that all readers must change countries.'],0,
 '这段章首如何定位心理丰富的人生？',['作为快乐与意义之外的另一条道路，与两者并列。','使快乐和有意义的人生不可能存在的概念。','科学地取代所有先前好人生观念。','要求所有读者改变居住国家的指令。'],
 ['A adding to the two better-known paths支持增添、并列而非取代。','B 再次并列三种人生的ingredients，没有使其中两种不可能。','C adding不能替换成replacement/all earlier。','D seeing the world through a new lens是看世界的视角比喻，并非必须搬迁。'],
 ['adding to the two better-known paths to a good life: a happy life and a meaningful life.'],
 'lens','镜头；看待事物的视角','new lens比喻通过三维框架重新看世界','The book offered a new lens through which to view ordinary experiences.',['through a new lens','paths to a good life'],
 '本书引入了心理丰富人生这一新概念，在两条较为人熟知的好人生道路——快乐人生与有意义的人生——之外增加了一条。既然你已了解这三种人生的构成，让我们看看，你能否开始用新的视角看世界：三维的人生。')

def persist():
 existing=load('source/short-questions/additional.json');byid={q['id']:q for q in existing}
 for q in out:
  if q['id'] in byid:assert byid[q['id']]==q
  else:existing.append(q)
 (ROOT/'source/short-questions/additional.json').write_text(json.dumps(existing,ensure_ascii=False,indent=2)+'\n',encoding='utf8')
 record=dict(batchId='batch-043',date='2026-10-24',pdfSha256=b['pdfSha256'],checkedPdfPages=[144,160],questionIds=[q['id'] for q in out],paragraphs=[dict(id=pid,textSha256=hashlib.sha256(pp[pid]['text'].encode()).hexdigest()) for pid in dict.fromkeys(q['paragraphId'] for q in out)],note='两段实际章首作者正文，逐字核对后按原页顺序补入；第13章6句分两段，第14章2句一段。旧题对象及来源ID保留。')
 (ROOT/'source/short-questions/review-audited-openings.json').write_text(json.dumps(record,ensure_ascii=False,indent=2)+'\n',encoding='utf8')
 print('Saved',len(out),'audited opening exercises')

if __name__=='__main__':persist()
