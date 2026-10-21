"""Seven individually written exercises fill every short unit in Chapter 1 Section 1."""
from pathlib import Path
import json
ROOT=Path(__file__).resolve().parents[2]
b=json.loads((ROOT/'public/data/book.json').read_text(encoding='utf8'))
plan=json.loads((ROOT/'public/data/reading-plan.json').read_text(encoding='utf8'))
ss={s['id']:s for s in b['sentences']};pp={p['id']:p for p in b['paragraphs']};out=[]
def add(number,unit_id,kind,prompt,options,answer,prompt_zh,options_zh,analyses,quotes,word,meaning,context,example,collocations,translation):
 u=next(u for u in plan['units'] if u['id']==unit_id);group=[ss[i] for i in u['sentenceIds']];p=pp[u['paragraphId']];text=p['text'][group[0]['start']:group[-1]['end']];evidence=[]
 for quote in quotes:
  start=p['text'].find(quote);assert quote in text and start>=0;end=start+len(quote);sentences=[s for s in group if s['start']<end and s['end']>start]
  sources=list({(r['pdfPage'],r['block']):r for s in sentences for r in s['sources']}.values())
  evidence.append(dict(quote=quote,sentenceIds=[s['id'] for s in sentences],sources=sources))
 assert word.lower() in text.lower()
 out.append(dict(id=f'q-c01-{number:03}',version=1,readingUnitId=u['id'],chapterId=u['chapterId'],sectionId=u['sectionId'],paragraphId=u['paragraphId'],sentenceIds=u['sentenceIds'],passage=text,prompt=prompt,options=options,answer=answer,type=kind,promptZh=prompt_zh,optionsZh=options_zh,analyses=analyses,evidence=evidence,vocabulary=[dict(word=word,meaning=meaning,context=context,example=example,collocations=collocations)],translation=translation,support='explicit',editorialStatus='按具体原文逐题编写；补齐第 1 章第 1 小节短段；无重复原句'))
add(34,'c01-s01-p007-03458-r004-006','细节','What does the passage explicitly say about Yoshi’s close friends?',
 ['They are mainly people he met through his wife.','They are the same friends he has known since elementary school.','They returned to his town only after he turned fifty.','They organise professional softball tours for him.'],1,
 '片段明确说，Yoshi 的亲密朋友有什么特点？',['他们主要是他通过妻子认识的人。','他们仍是他从小学起就认识的同一批朋友。','他们直到他年过五十才回到他的小镇。','他们为他组织职业垒球巡回比赛。'],
 ['A 原文没有说这些朋友通过妻子认识；妻子的来源与朋友认识时间不能混同。','B the same close friends...since elementary school 直接说明交友的长期延续。','C into his fifties 修饰打垒球的时间，不是朋友返回小镇的时间。','D neighborhood league 是邻里联赛；协会组织的是温泉旅行，不是职业巡回赛。'],
 ['He still lives in the same town; he still has the same wife; and he still has the same close friends he has known since elementary school.'],
 'into his fifties','一直到五十多岁时','说明 Yoshi 五十多岁时仍参加邻里垒球活动','She continued running races into her fifties.',['continue into one’s fifties','work into one’s sixties'],
 '二十七岁时，Yoshi 娶了一位邻镇女子，并有了三个孩子。他五十多岁时仍参加邻里垒球联赛，也喜欢每年随邻里协会前往各处温泉旅行。他仍住在同一个小镇，仍与同一位妻子相伴，也仍拥有从小学起就认识的同一批亲密朋友。')
add(35,'c01-s01-p007-05992-r001-002','细节','How soon after his eighteenth birthday did the narrator leave for college?',
 ['On the day of his eighteenth birthday.','Eighteen months after his birthday.','Exactly eighteen days after his birthday.','After spending eighteen years in Tokyo.'],2,
 '叙述者在十八岁生日多久后离开家乡上大学？',['在十八岁生日当天。','生日后十八个月。','生日后恰好十八天。','在东京度过十八年之后。'],
 ['A after...eighteen days 表示生日过后，并非生日当天。','B 将 days 错换成 months，时间单位不符。','C exactly eighteen days 逐字给出了准确间隔。','D Tokyo 是离乡上大学的目的地，不是此前住了十八年的地方。'],
 ['After my eighteenth birthday, it took me exactly eighteen days to leave our small town for college in Tokyo.'],
 'a world away','相距遥远；仿佛处在另一个世界','作者以此描述自己与父亲所处位置或生活的距离','After moving abroad, her old routine felt a world away.',['feel a world away','a world away from'],
 'Yoshi 是我的父亲，而我这个儿子却身在遥远的另一方。十八岁生日后，过了恰好十八天，我就离开我们的小镇，去东京上大学。')
add(36,'c01-s01-p007-05992-r004-005','逻辑关系','Which event occurred before the author began the programme in Maine?',
 ['He attended a summer English programme in New York City.','He reunited with his girlfriend in Tokyo.','He completed a year of graduate study in Boston.','He decided to stop learning English.'],0,
 '在开始缅因州的课程之前，作者经历了什么？',['他在纽约市参加了暑期英语课程。','他与东京的女友复合。','他在波士顿完成了一年研究生学习。','他决定停止学习英语。'],
 ['A Before I started...先交代缅因州课程之前，后接 Staten Island in New York City 的暑期课程。','B had just broken up 表示刚分手，与复合相反。','C 该片段没有报告在波士顿完成研究生学习。','D 参加英语课程并不支持停止学习的说法。'],
 ['Before I started the program in Maine, I attended a summer English program on Staten Island in New York City.'],
 'broken up with','与……分手','说明作者当时刚结束与东京女友的恋爱关系','She had broken up with her partner before moving.',['break up with a partner','have just broken up'],
 '开始缅因州的课程之前，我在纽约市的斯塔滕岛参加了一个暑期英语课程。我刚与东京的女友分手，也厌倦了处于恋爱关系之中。')
add(37,'c01-s01-p007-05992-r008-011','细节','Why did the author take a bus to Boston every weekend?',
 ['To attend his own graduate classes there.','To return to Tokyo at the end of each week.','To begin his year in Lewiston.','To visit the woman who was starting graduate school there.'],3,
 '作者为什么每个周末都乘巴士去波士顿？',['去那里参加自己的研究生课程。','每周末返回东京。','开始在刘易斯顿的一年生活。','看望将在那里开始研究生学习的那位女子。'],
 ['A 在波士顿开始研究生学习的是 she，不能把主语换成作者。','B 去东京是在五月，不是每个周末；巴士目的地也是波士顿。','C 作者将在缅因州的刘易斯顿开始一年生活，周末巴士则用于去波士顿。','D to see her 直接给出出行目的，her 回指在波士顿读研究生的女子。'],
 ['During the 1991–1992 academic year, I took a Greyhound bus to Boston to see her every weekend.'],
 'was about to','即将；正要','两人当时各自即将开始的学习安排','The train was about to leave when we arrived.',['be about to start','be about to leave'],
 '她即将在波士顿开始研究生学习。我则即将在缅因州刘易斯顿开始一年的生活。在 1991—1992 学年，我每个周末都乘灰狗巴士去波士顿看她。五月，我不得不回到东京。')
add(38,'c01-s01-p007-05992-r012-012','逻辑关系','What contrast is introduced by “Though” in the passage?',
 ['He always planned to study in the U.S., but eventually refused to return.','His earlier plans excluded U.S. graduate study, but he later wanted to return.','He intended to work in Tokyo and therefore never changed his plans.','His original goal was to work for the U.S. Ministry of Education.'],1,
 '片段中的“Though”引出了什么对照？',['他一直计划赴美读研，最终却拒绝回去。','较早的计划没有赴美读研，但后来他决心返回。','他打算在东京工作，因此从未改变计划。','他原先的目标是在美国教育部工作。'],
 ['A hadn’t had any intention 否定了早期赴美读研的意愿；结尾却是 determined to come back。','B 对齐原先在日本文部省工作且无意赴美读研，与后来决心返回的反差。','C 用 therefore 抹去了 Though 引出的转折；never 与决心改变不符。','D 原文是 Ministry of Education in Japan，地点被错换成美国。'],
 ['Though my career plan before studying abroad was to work for the Ministry of Education in Japan, and I hadn’t had any intention of attending graduate school in the U.S., by then I was determined to come back.'],
 'determined','下定决心的；坚定的','与此前无意赴美读研形成转折，表明后来返回的意愿','She was determined to finish the course.',['be determined to return','determined to do something'],
 '虽然留学前，我的职业计划是在日本文部省工作，而且此前从未打算赴美读研究生，但到那时，我已经下定决心要回来。')
add(39,'c01-s01-p007-05992-r014-016','细节','What is explicitly stated about the author’s two children?',
 ['They were both born on Staten Island.','They were born to different mothers.','They were born in two different cities.','They were born before he met the Korean woman.'],2,
 '片段明确说，作者的两个孩子有什么情况？',['他们都出生于斯塔滕岛。','他们的母亲不是同一个人。','他们出生于两座不同的城市。','他们出生在作者遇到那位韩国女子之前。'],
 ['A born in two different cities 与“都在斯塔滕岛”矛盾。','B 作者说与同一位韩国女子结婚并有两个孩子，不能把不同城市错配成不同母亲。','C born in two different cities 直接支持。','D Along the way, I married...and we had two children 不支持孩子出生在相遇之前。'],
 ['Along the way, I married the Korean woman I met on Staten Island and we had two children, born in two different cities.'],
 'varying lengths','不同的时长','说明作者在各座城市停留的时间长短不一','The students submitted essays of varying lengths.',['stays of varying lengths','periods of varying lengths'],
 '接下来，我在纽约市、伊利诺伊州香槟市、明尼苏达州明尼阿波利斯市和弗吉尼亚州夏洛茨维尔市先后停留，时长不一，然后继续迁往芝加哥。在这一路上，我与在斯塔滕岛认识的韩国女子结婚，有了两个孩子，他们分别出生于两座不同的城市。我已经多年没见过任何小学朋友了。')
add(40,'c01-s01-p008-04260-r001-004','主旨','How does “on the other hand” organise the comparison?',
 ['It contrasts the father’s predictable comforts with the author’s more stressful life.','It shows that father and son share the same annual routine.','It attributes the father’s comfort to the author’s professional success.','It describes the father changing from a comfortable life to a stressful one.'],0,
 '“on the other hand”怎样组织这段比较？',['对照父亲可预期的安稳舒适与作者更有压力的生活。','说明父子拥有相同的年度生活安排。','把父亲的舒适归因于作者的职业成功。','描述父亲从舒适生活变得压力重重。'],
 ['A 前半写父亲的稳定和四季活动，后半用 My life 转向作者的不稳定、期限压力与拒绝。','B 活动清单修饰父亲的生活，并非父子的共同安排。','C 原文没有建立父亲舒适由儿子职业成功造成的因果关系。','D 压力重重的是 My life，主语由父亲换为作者，不是父亲自身的阶段变化。'],
 ['My father’s life has been stable, familiar, and comfortable.','My life, on the other hand, has been far less stable, far less familiar, and far more stressful with constant deadlines for lecturing, grading, and writing mixed with countless rejections (e.g., grants, papers, book proposals, job applications).'],
 'on the other hand','另一方面；与此相对','标记从父亲的安稳转向作者的压力生活','The flat is small; on the other hand, it is close to work.',['on the one hand ... on the other hand','on the other hand, ...'],
 '父亲的生活一直稳定、熟悉而舒适。春天是每年的赏樱聚会，夏天是盂兰盆舞节，秋天是赏叶之旅，冬天则泡温泉。这是一种温馨的生活，一种美好生活。相比之下，我的人生远没有那么稳定和熟悉，压力却大得多：讲课、评分和写作的截止期限不断，还夹杂着无数次拒绝，例如资助、论文、图书提案和求职申请遭拒。')
path=ROOT/'source/short-questions/additional.json';path.parent.mkdir(parents=True,exist_ok=True);path.write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n',encoding='utf8',newline='\n')
print('Saved',len(out),'specific opening-section exercises')
