"""Two individually authored exercises, visually verified against PDF pages 17-18.
Stable existing reading boundaries; merge without rewriting published questions.
"""
from pathlib import Path
import json,hashlib
ROOT=Path(__file__).resolve().parents[2]
load=lambda p:json.loads((ROOT/p).read_text(encoding='utf8'))
b=load('public/data/book.json');plan=load('public/data/reading-plan.json');ss={s['id']:s for s in b['sentences']};pp={p['id']:p for p in b['paragraphs']};out=[]
def add(number,unit_id,kind,prompt,options,answer,prompt_zh,options_zh,analyses,quotes,vocabulary,translation):
 u=next(u for u in plan['units'] if u['id']==unit_id);group=[ss[sid] for sid in u['sentenceIds']];p=pp[u['paragraphId']];text=p['text'][group[0]['start']:group[-1]['end']];evidence=[]
 for quote in quotes:
  offset=text.find(quote);assert offset>=0;start=group[0]['start']+offset;end=start+len(quote);touching=[s for s in group if s['start']<end and s['end']>start]
  evidence.append(dict(quote=quote,sentenceIds=[s['id'] for s in touching],sources=list({(r['pdfPage'],r['block']):r for s in touching for r in s['sources']}.values())))
 assert all(v['word'].lower() in text.lower() for v in vocabulary)
 out.append(dict(id=f'q-c02-{number:03}',version=1,readingUnitId=u['id'],chapterId=u['chapterId'],sectionId=u['sectionId'],paragraphId=u['paragraphId'],sentenceIds=u['sentenceIds'],passage=text,prompt=prompt,options=options,answer=answer,type=kind,promptZh=prompt_zh,optionsZh=options_zh,analyses=analyses,evidence=evidence,vocabulary=vocabulary,translation=translation,support='explicit',editorialStatus='PDF 第 17–18 页原页视觉核对；逐题编写；区分社交媒体表象、本人感受与客观判断，不从个案臆断因果'))
def v(word,meaning,context,example,*collocations):return dict(word=word,meaning=meaning,context=context,example=example,collocations=list(collocations))

add(30,'c02-s01-p017-05558-r003-006','逻辑关系',
 'What contrast does the passage draw about Madison Holleran?',
 ['Her party photographs documented an entirely secure private life.','Her cheerful online image contrasted with a more uncertain reality.','Her unhappy online posts matched her troubled private life.','Her private life was secure although her posts suggested unhappiness.'],1,
 '本段呈现了 Madison Holleran 的什么反差？',
 ['她的聚会照片记录了完全安稳的私人生活。','她在网上的快乐形象与更不安稳的现实形成反差。','她网上的不快乐帖文与困扰重重的私人生活一致。','她的私人生活很安稳，尽管帖文显示她不快乐。'],
 ['A 照片呈现快乐，但 Yet her reality was more tenuous 明确转向不那么安稳的现实；不能把照片当作私人生活完全安稳的证明。','B epitomized happiness 与 Yet...more tenuous 构成直接对照：线上看似幸福，现实却更不稳固。','C 原文写 smiling、sunshine 和 kicking back，帖文并非呈现不快乐；也不能把反差改成一致。','D 这个选项把反差方向颠倒：原文是线上快乐、现实不那么安稳，而非线上不快、私下安稳。'],
 ['According to The New York Times, she “posted images that show her smiling, dappled in sunshine or kicking back at a party.” Her social media epitomized happiness. Yet her reality was more tenuous.'],
 [v('epitomized','成为……的典型体现；集中表现','描述她的社交媒体呈现出典型的快乐形象，不证明实际生活状态','The small cottage epitomized the quiet life he wanted.','epitomize happiness','epitomize an ideal'),v('tenuous','不稳固的；脆弱的','这里描述她的现实状态相较网上形象更不稳固，不是在说照片不清晰','Their agreement remained tenuous after the meeting.','a tenuous relationship','a tenuous connection')],
 '以 Madison Holleran 为例，她是宾夕法尼亚大学一名“受欢迎、外表出众且才华横溢”的一年级学生。据《纽约时报》报道，她“发布的照片中，自己或面带笑容，或沐浴在斑驳阳光里，或在聚会上放松休闲”。她的社交媒体俨然是幸福的典型写照。然而，她的现实生活却没有那么稳固。')

add(31,'c02-s01-p017-05558-r007-008','细节',
 'What did Madison reveal to her sister about her social life?',
 ['She thought her friends had fewer social opportunities than she did.','She told her sister that her friends envied her social life.','She said her sister had a better social life than her friends.','She felt her social life compared unfavourably with her friends’.'],3,
 'Madison 向姐妹透露了自己对社交生活的什么感受？',
 ['她认为朋友们的社交机会比自己少。','她告诉姐妹，朋友们羡慕自己的社交生活。','她说姐妹的社交生活比朋友们更好。','她觉得自己的社交生活比不上朋友们。'],
 ['A 原文是她觉得自己不如朋友，选项把比较方向颠倒，并将 social life 擅自缩窄为机会数量。','B feeling 的主体是 Madison；原文没有报告朋友们羡慕她，把她的感受换成朋友的看法缺乏依据。','C her sister 是倾诉对象，不是社交生活的比较对象；that of her friends 中 that 回指 social life。','D feeling that her social life was inferior to that of her friends 直接说明她觉得自己比不上朋友。这是她的自我感受，不是客观排名；相邻的事件叙述也不能单独证实某种死亡原因。'],
 ['To her sister, she revealed feeling that her social life was inferior to that of her friends.'],
 [v('inferior to','比……差；不如……','描述她对自身社交生活的比较感受，而非书中证实的客观等级','This fabric is inferior to the sample we ordered.','feel inferior to others','be inferior to'),v('revealed','透露；说出此前未公开的事','指她向姐妹说出自己的私人感受，不表示公布研究发现','He revealed his concerns during a private conversation.','reveal a feeling','reveal something to someone')],
 '她向姐妹透露，觉得自己的社交生活不如朋友们。2014 年 1 月 17 日，Madison 从一座停车楼的顶部跳下，结束了自己的生命。')

path=ROOT/'source/short-questions/additional.json';existing=load('source/short-questions/additional.json');byid={q['id']:q for q in existing}
for q in out:
 if q['id'] in byid:assert byid[q['id']]==q,('Refuse to overwrite changed exercise',q['id'])
 else:existing.append(q)
path.write_text(json.dumps(existing,ensure_ascii=False,indent=2)+'\n',encoding='utf8',newline='\n')
p=pp[out[0]['paragraphId']]
review=dict(batchId='batch-007',date='2026-10-22',pdfSha256=b['pdfSha256'],checkedPdfPages=[17,18],paragraphId=p['id'],paragraphTextSha256=hashlib.sha256(p['text'].encode()).hexdigest(),questionIds=[q['id'] for q in out],note='完整原页 PNG 视觉复核，包括跨页 friends 及其后原句。固定现有短段边界，不重复原句；不将主观比较当成客观排名或单一因果解释。')
(ROOT/'source/short-questions/review-chapter-02-madison.json').write_text(json.dumps(review,ensure_ascii=False,indent=2)+'\n',encoding='utf8',newline='\n')
print('Merged two page-17–18 exercises; existing published content preserved.')
