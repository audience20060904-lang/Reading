"""Two individually authored exercises, verified against PDF page 17 on 2026-10-22.
Merge with existing prepared content; no rewriting of published units or questions.
"""
from pathlib import Path
import json,hashlib
ROOT=Path(__file__).resolve().parents[2]
load=lambda p:json.loads((ROOT/p).read_text(encoding='utf8'))
b=load('public/data/book.json');plan=load('public/data/reading-plan.json');ss={s['id']:s for s in b['sentences']};pp={p['id']:p for p in b['paragraphs']};out=[]
def add(number,unit_id,prompt,options,answer,prompt_zh,options_zh,analyses,quotes,vocabulary,translation):
 u=next(u for u in plan['units'] if u['id']==unit_id);group=[ss[sid] for sid in u['sentenceIds']];p=pp[u['paragraphId']];text=p['text'][group[0]['start']:group[-1]['end']];evidence=[]
 for quote in quotes:
  offset=text.find(quote);assert offset>=0;start=group[0]['start']+offset;end=start+len(quote);touching=[s for s in group if s['start']<end and s['end']>start]
  evidence.append(dict(quote=quote,sentenceIds=[s['id'] for s in touching],sources=list({(r['pdfPage'],r['block']):r for s in touching for r in s['sources']}.values())))
 assert all(v['word'].lower() in text.lower() for v in vocabulary)
 out.append(dict(id=f'q-c02-{number:03}',version=1,readingUnitId=u['id'],chapterId=u['chapterId'],sectionId=u['sectionId'],paragraphId=u['paragraphId'],sentenceIds=u['sentenceIds'],passage=text,prompt=prompt,options=options,answer=answer,type='细节',promptZh=prompt_zh,optionsZh=options_zh,analyses=analyses,evidence=evidence,vocabulary=vocabulary,translation=translation,support='explicit',editorialStatus='PDF 第 17 页原页视觉核对；逐题编写；区分哲学引述、调查评分与研究关联，不夸大为确定因果'))
def v(word,meaning,context,example,*collocations):return dict(word=word,meaning=meaning,context=context,example=example,collocations=list(collocations))

add(28,'c02-s01-p017-03608-r002-004',
 'According to the William James quotation, what drives much of human action and endurance?',
 ['The pursuit, preservation, and recovery of happiness.','The avoidance of every form of discomfort.','The aim of gaining money rather than happiness.','The wish to rank happiness below other concerns.'],0,
 '根据 William James 的引述，什么推动着人们的许多行动和忍耐？',
 ['追求、保持和重获幸福。','避免任何形式的不适。','追求金钱而不是幸福。','希望把幸福排在其他关切之后。'],
 ['A gain、keep、recover happiness 分别对应追求、保持、重获幸福；原文将其称为多数人行动与忍耐背后的隐秘动机。','B willing to endure 说明为了幸福，人们可能愿意忍受困难；不能改成回避一切不适。','C 这段引述围绕 happiness，没有把金钱确立为取代幸福的动机。','D James 将幸福称为 chief concern，并非把它放在其他关切之后。这是被引用的观点，不是本段报告的实验结论。'],
 ['When William James asked himself, “What is human life’s chief concern?” his answer was: “It is happiness. How to gain, how to keep, how to recover happiness, is in fact for most men at all times the secret motive of all they do, and of all they are willing to endure.”'],
 [v('chief concern','首要关切；最重要的关注点','James 用这个短语提问人生最关心什么；chief 在此表示主要的','Safety is the chief concern when planning the trip.','a chief concern','the chief concern of'),v('endure','忍受；承受','描述人们为了幸福愿意承受的困难，不表示必须回避所有不适','The hikers endured a long night in the cold.','endure hardship','endure discomfort')],
 '当 William James 问自己“人生最主要的关切是什么”时，他的回答是：“是幸福。如何获得、如何保持、如何重获幸福，事实上，对大多数人来说，无论何时，都是他们所做的一切，以及他们愿意忍受的一切背后的隐秘动机。”')

add(29,'c02-s01-p017-03608-r005-007',
 'What does the figure 69 percent refer to in Diener’s study?',
 ['Respondents who rated money as extremely important.','People whose health improved because they became happy.','Respondents who gave happiness the highest importance rating.','Respondents who ranked love and health above happiness.'],2,
 'Diener 的研究中，69% 这个数字指什么？',
 ['认为金钱极其重要的受访者。','因为变得幸福而改善健康的人。','给幸福的重要性打出最高分的受访者。','认为爱情和健康比幸福更重要的受访者。'],
 ['A 69% 对应给幸福评分的人，不是给金钱评分的人；money 是随后比较的项目。','B 健康和亲社会行为出现在后面的研究概括中，不是 69% 的统计对象；本段也没有以实验说明变幸福必然导致健康改善。','C rated happiness as extremely important 与 a perfect 7 on a 1 to 7 point scale 共同说明，这些受访者给幸福的重要性打了最高分。','D ahead of money, love, and health 说明幸福的重要性居于这些项目之前；选项把比较方向倒置了。'],
 ['It is a goal shared by many across the globe; in a large international study conducted by Ed Diener, 69 percent of respondents rated happiness as extremely important (a perfect 7 on a 1 to 7 point scale), ahead of money, love, and health.'],
 [v('respondents','受访者；作答者','指参加这项国际研究并给重要性评分的人，不是世界人口的全部成员','Most respondents completed the questionnaire online.','survey respondents','respondents to a questionnaire'),v('prosocial','亲社会的；有益于他人的','描述研究概括中幸福者更倾向于表现出的助人等行为，不能当成该调查 69% 的定义','Sharing supplies is an example of prosocial behaviour.','prosocial behaviour','prosocial actions')],
 '这是全球许多人共同追求的目标。在 Ed Diener 主持的一项大型国际研究中，69% 的受访者认为幸福极其重要，在 1 至 7 分的量表上给出满分 7 分，其重要性排在金钱、爱情和健康之前。这是一个值得追求的目标，因为研究表明，幸福的人更健康，也更具亲社会倾向。他们在工作中表现更好，寿命也比不幸福的人更长。')

path=ROOT/'source/short-questions/additional.json';existing=load('source/short-questions/additional.json');byid={q['id']:q for q in existing}
for q in out:
 if q['id'] in byid:assert byid[q['id']]==q,('Refuse to overwrite changed exercise',q['id'])
 else:existing.append(q)
path.write_text(json.dumps(existing,ensure_ascii=False,indent=2)+'\n',encoding='utf8',newline='\n')
p=pp[out[0]['paragraphId']]
review=dict(batchId='batch-006',date='2026-10-22',pdfSha256=b['pdfSha256'],checkedPdfPages=[17],paragraphId=p['id'],paragraphTextSha256=hashlib.sha256(p['text'].encode()).hexdigest(),questionIds=[q['id'] for q in out],note='原页 PNG 视觉复核，固定当前短段边界；哲学引述不是实验，调查比例不是健康因果比例。候选句界不是人工定稿。')
(ROOT/'source/short-questions/review-chapter-02-next-two.json').write_text(json.dumps(review,ensure_ascii=False,indent=2)+'\n',encoding='utf8',newline='\n')
print('Merged two page-17 exercises; preserved all existing exercises.')
