"""25 individually authored exercises for frozen targets, PDF pages 155-158.
Preserve printed English, source positions and all previously published questions.
"""
from pathlib import Path
import json,hashlib
ROOT=Path(__file__).resolve().parents[2]
load=lambda p:json.loads((ROOT/p).read_text(encoding='utf8'))
b=load('public/data/book.json');plan=load('public/data/reading-plan.json');targets=load('source/short-questions/batch039-targets.json')['targets']
ss={s['id']:s for s in b['sentences']};pp={p['id']:p for p in b['paragraphs']};out=[]
def add(i,kind,prompt,options,answer,prompt_zh,options_zh,analyses,quotes,word,meaning,context,example,collocations,translation,support='explicit'):
 t=targets[i-1];u=next(u for u in plan['units'] if u['id']==t['readingUnitId']);group=[ss[sid] for sid in u['sentenceIds']];p=pp[u['paragraphId']];text=p['text'][group[0]['start']:group[-1]['end']]
 assert hashlib.sha256(text.encode()).hexdigest()==t['passageSha256'];evidence=[]
 for quote in quotes:
  offset=text.find(quote);assert offset>=0,(i,quote);start=group[0]['start']+offset;end=start+len(quote);touching=[s for s in group if s['start']<end and s['end']>start]
  evidence.append(dict(quote=quote,sentenceIds=[s['id'] for s in touching],sources=list({(r['pdfPage'],r['block']):r for s in touching for r in s['sources']}.values())))
 assert word.lower() in text.lower(),(i,word)
 out.append(dict(id=t['questionId'],version=1,readingUnitId=u['id'],chapterId=u['chapterId'],sectionId=u['sectionId'],paragraphId=u['paragraphId'],sentenceIds=u['sentenceIds'],passage=text,prompt=prompt,options=options,answer=answer,type=kind,promptZh=prompt_zh,optionsZh=options_zh,analyses=analyses,evidence=evidence,vocabulary=[dict(word=word,meaning=meaning,context=context,example=example,collocations=collocations)],translation=translation,support=support,editorialStatus='完整PDF155–158原页视觉核对。Jiro有竞争者但未同等被紧盯比较，不改成毫无竞争；toes为警醒习语，反刍解释非普遍临床因果，童年玩心出自同学访谈。职业路径provided that深度足够才可探索，one way非唯一。Spotify11,861,427/30,561,926为as of this writing快照非实时；大学生偏好为作者观察，音乐多样性One possible explanation与Pet Sounds反事实不作已证因果，承认Beach Boys作品也多样，作曲者比较仅归本段。Yesterday情节为电影非现实，哭泣为作者歌词共鸣不补歌词或全家反应。怀旧有联系/意义等益处，熟悉对象中新发现区别于纯怀旧。Offill重读人物Septimus/Clarissa/Peter按阶段，不混小说人物与现实作者，fifty-second year保留原措辞不擅算已满52。Peter/Sally/Richard角色与话语分清；brain/heart为文学比喻，Not a word为人物答话，and laughed续接旧边界不当独立最终句。吸引原因mystery不补造；文学例证非实验。额外正文审计待办保持开放，不以候选池完整代替全书正文完整。'))







add(1,'逻辑关系','Which contrast does the author draw between elite athletes and Jiro?',
 ['Jiro has no competitors, whereas every athlete works privately.','Athletes never have their defeats recorded.','Athletes’ defeats become public, while Jiro’s work was not watched as closely against rivals.','Disappearing fish made every sushi chef abandon the profession.'],2,
 '作者怎样对照顶尖运动员与Jiro？',['Jiro毫无竞争者，运动员全私下工作。','运动员的失败从不记录。','运动员失败公开，而Jiro不被同样紧盯着与对手比较。','鱼类消失令所有寿司师傅离职。'],
 ['A has had many competitors明确有竞争者；区别在关注比较方式，不在有无竞争。','B objectively recorded and becomes public直接否定。','C every defeat/public与not closely watched...against形成对照，不能强化为Jiro完全没被评价。','D had to adjust type of sushi是调整供应，不是所有人离职。'],
 ['every defeat is objectively recorded and becomes public.','Jiro’s performance was not closely watched against the performances of others.'],
 'adjust','调整；适应改变','鱼类供应变化使菜单种类调整，非彻底停止做寿司','The chef adjusted the menu when an ingredient became unavailable.',['adjust the type of sushi','unexpected challenges'],
 '顶尖运动员的艰难之处，是每次失败都被客观记录并公开。Jiro虽有过许多竞争者，他的表现却没有那么紧密地被拿来与别人比较。第二，像日本的寿司师傅一样，他随时间面对多样、意外的挑战。东京湾某些常见寿司鱼类消失，他不得不逐年调整所供应的寿司种类。')

add(2,'语境词义','What does “keep him on his toes” mean here?',
 ['Keep him alert and occupied with changing practical demands.','Force him to stand literally on tiptoe while cooking.','Prevent him from ever making any mistake.','Make him focus exclusively on public rankings.'],0,
 'keep him on his toes在这里是什么意思？',['让他警醒忙碌，应对变化的实际要求。','迫使他踮脚做菜。','使他永不犯错。','使他只盯公开排名。'],
 ['A 环境与经济挑战带来daily decisions and demands，说明保持投入应变。','B 这是习语，不是在规定站姿。','C I assume...makes mistakes还承认大师可能失误。','D 此处强调日常决策，不是公开竞技名次。作者说没有多少时间反刍，是解释性叙述，非证明忙碌必治疗所有人的反刍。'],
 ['These challenges as well as economic challenges keep him on his toes.','Jiro has been preoccupied with various daily decisions and demands.'],
 'ruminate','反复思量；纠结反刍','这里指在表现与错误上反复打转的思维，非动物反刍食物','He tried not to ruminate on every small mistake.',['ruminate on mistakes','keep someone on their toes'],
 '这些环境变化迫使他改变制作菜单的方式。它们连同经济挑战，让他一直保持警醒。部分顶尖运动员倾向反复琢磨表现，并要每天激励自己苦练；Jiro却忙于各种日常决策和要求。因为这些挑战，他没时间真正反刍错误（我想，连大师也会偶尔犯错）。')

add(3,'细节','What continuity in Jiro’s character is described?',
 ['He stopped joking once he became a professional.','The documentary directly observed him as an elementary-school child.','His playfulness began only after his eightieth birthday.','A mischievous childhood spirit continued as lighthearted joking in later life.'],3,
 '本段描述Jiro性格什么延续？',['成为专业人士后不再开玩笑。','纪录片直接拍到他当小学生。','80岁生日后才开始顽皮。','童年的淘气延续为晚年轻松地开玩笑。'],
 ['A still joking与停止相反。','B childhood信息来自小学朋友访谈，不是直接观察当年童年影像的声明。','C carried...well into说明延续，非才开始。','D mischievous boy及lightheartedness...eighties连接前后。年龄与纪录片叙述时点相连，不作其今日年龄断言。'],
 ['He was a very mischievous boy, according to an interview with his elementary school friends in the documentary.','still joking around with his customers.'],
 'lightheartedness','轻松愉快；不沉重的心态','指与顾客玩笑互动的态度，不等于工作不认真','Her lightheartedness made the conversation enjoyable.',['a sense of lightheartedness','joke around with customers'],
 '第三，回到第7章主题，Jiro很有玩心。纪录片中小学朋友受访说，他小时候是个很淘气的男孩。他把这种轻松愉快带到80多岁，仍与顾客说笑。')

add(4,'主旨','What enables continued discovery within Jiro’s long-established craft?',
 ['A rule against changing any part of the existing menu.','Creative possibilities and his belief that he can still improve.','A need to change professions whenever he feels bored.','The claim that opening a restaurant ends all further learning.'],1,
 '什么使Jiro在长期从事的手艺中仍可发现新东西？',['禁止改现有菜单的规则。','创作可能与他相信还能进步。','一无聊就必须换职业。','开店即结束学习的说法。'],
 ['A new nigiri/new way to cook eel明确可改。','B creative art与can still improve构成继续探索的基础。','C 本段说在原手艺内创新，不要求换职业。','D 1965开店是时间背景，不是学习终点。if ever gets bored为条件，不能写成已永久厌倦。'],
 ['sushi is a creative art.','He thinks that he can still improve as a sushi chef.'],
 'extant','现存的；现有的','形容目前已有菜单，区别于未来可创造的新做法','The artist reconsidered the extant design before trying another version.',['the extant menu','come up with new ways'],
 '毕竟，寿司是创造性的艺术。若他对现有菜单感到无聊，就能想出各种方法，创作新握寿司或烹调鳗鱼的新方式。他觉得自己做寿司仍能改进。Jiro于1965年开了Sukiyabashi Jiro。')

add(5,'推断','What possibility does the final sentence support?',
 ['Long-term repetition can coexist with regularly finding new things to try.','Decades at one location necessarily eliminate curiosity.','Disliking holidays proves everyone should avoid taking breaks.','A person must switch careers to keep looking forward to work.'],0,
 '末句支持哪种可能？',['长期重复与经常发现新尝试可以共存。','数十年同地必然消除好奇。','不喜欢放假证明所有人都应不休息。','必须换职业才可期待工作。'],
 ['A Even if...can still把重复与新尝试并置，保留可能性而非人人保证。','B 与结论相反。','C hates holidays是书述Jiro个人体验，不是给所有人的休息规则。','D same restaurant/same location说明不必靠换职业才出现新奇。'],
 ['Even if you do the same things every day for many decades, you can still find something new to try regularly.'],
 'looks forward to','期待；盼望','后接动名词working，描述仍有工作期待的个人状态','She looks forward to learning a new technique.',['look forward to working','find something new'],
 '在同一地点同一家餐厅长期任主厨，确实很久。可这么多年以后，每逢必须关店放假，他仍不喜欢。他总期待回餐厅工作。即便几十年里每天做同样的事，也仍能经常找到新尝试。',support='limited-inference')

add(6,'逻辑关系','What condition qualifies devotion to one career as a path to richness?',
 ['The career must remain unchanged in technique and perspective.','Every amateur must first become a restaurant owner.','The career must be deep enough to support lifelong exploration.','The worker must avoid acquiring any new skills.'],2,
 '专注一项职业成为丰富途径，有什么条件？',['技法视角都必须不变。','每位业余者先当餐厅老板。','职业须有足够深度，支持终身探索。','从业者必须避免新技能。'],
 ['A changes over time与不变相反。','B amateur是对照，不是所有人必须开店的规定。','C provided that引入必要限定，不能删为任何职业只要坚持就必丰富。','D acquires new techniques明确学习新技能。one way也不是唯一道路。'],
 ['devotion to one career, provided that the chosen career is deep enough for lifelong exploration.'],
 'provided that','条件是；只要满足……','把职业的深度与探索空间作为前提，限制结论范围','The plan can work, provided that enough time is available.',['provided that','lifetime devotion'],
 'Jiro这样的shokunin，其工作与业余爱好者不同，因为它要求终身投入。随着习得新技法和视角，工作也会变化。他设法不断更新自己最初对寿司的热爱。通向心理丰富的一条路，是沿他的道路专注一项职业——前提是，这项职业足够深，能让人探索终身。')

add(7,'细节','How should the Spotify figures be interpreted within this passage?',
 ['They measure lifetime concert attendance for the two bands.','They compare monthly listeners at the author’s time of writing.','They show that the Beach Boys had the larger listener count.','They establish the exact number of current listeners today.'],1,
 '本段Spotify数字应怎样理解？',['测两乐队终生演唱会人次。','比较作者写作时的月听众数。','显示Beach Boys听众更多。','确立今天此刻精确听众数。'],
 ['A monthly listeners非终生入场人次。','B as of this writing明确时点；11,861,427对30,561,926是当时引用数字。','C Beatles较大，方向不能反。','D 书载历史快照不是实时查询结果。almost three times是作者约略比较，不是精确三倍。'],
 ['monthly listeners, as of this writing.','30,561,926 monthly listeners, almost three times that of the Beach Boys.'],
 'as of this writing','截至写作时；写下这些文字时','限制数字时效，防止把书中快照当实时数据','The project had twenty members as of this writing.',['monthly listeners','as of this writing'],
 '为什么Beatles比Beach Boys受欢迎得多？看Spotify，截至写作时，Beach Boys月听众高达11,861,427；Beatles则达惊人的30,561,926，几乎是前者三倍。两个乐队在1960年代都曾极受全球欢迎。')

add(8,'作者意图','Why mention similar active periods and comparable album numbers?',
 ['To prove the bands had identical musical styles.','To establish that every college student prefers the Beatles.','To report a randomized listening experiment.','To show that these similarities do not by themselves resolve the observed popularity difference.'],3,
 '为何提活跃时期及专辑数量相近？',['证明音乐风格完全相同。','确立每个大学生都偏爱Beatles。','报告随机听歌实验。','说明这些相似点本身不能解释所观察到的人气差异。'],
 ['A 时期与数量不等于风格。','B I see more是作者个人观察，不是所有人偏好。','C 本段没有分组实验。','D Yet和Why在相近产出与不同观察之间设问，为后文解释开路。comparable不是每张专辑或每年活动都精确相等。'],
 ['The two bands were active for similar periods and released comparable numbers of albums. Yet today I see more college students listening to the Beatles than the Beach Boys.'],
 'comparable','相近而可比较的','此处指专辑数量大体相当，不要求完全一模一样','The two groups produced comparable amounts of work.',['comparable numbers','similar periods'],
 '两乐队活跃时期相近，发行专辑数量也相当。然而，如今我看到听Beatles的大学生多于Beach Boys。为什么？')

add(9,'主旨','What possible explanation does the author propose?',
 ['The Beatles released only songs with a single emotional tone.','The Beatles’ popularity was experimentally caused by nostalgia alone.','Their songs and artistic phases offered substantial variety.','Rebellion replaced every other theme from the beginning.'],2,
 '作者提出什么可能解释？',['Beatles只出单一情绪歌曲。','实验证明其流行只由怀旧造成。','歌曲与艺术阶段具有显著多样性。','最初起反叛便取代所有其他主题。'],
 ['A 从简单情歌到怀旧、哲学、反叛等列举否定单一。','B One possible explanation不是实验确证，也不只怀旧。','C very diverse及不同phase支持多样性这一假说。','D initial goody-goody后才列其他阶段，不是从始至终只反叛。歌名是例子，不从名称编造新歌词。'],
 ['One possible explanation is that the Beatles’ popular songs are very diverse','a countercultural phase, a spiritual phase, and a discontentment phase.'],
 'ranging from','范围从……到……','引出并列音乐主题和情绪类型，体现多样性','Their interests ranged from simple melodies to experimental music.',['ranging from A to B','a countercultural phase'],
 '一种可能解释，是Beatles流行歌曲很多样：从《All You Need Is Love》《I Want to Hold Your Hand》这样的简单情歌，到《Yesterday》《Hey Jude》这样怀旧温柔的歌；从《Let It Be》《Nowhere Man》《Across the Universe》这样哲学性、灵性浓厚的歌，到《Revolution》《Come Together》这样反叛的歌。他们最初有乖男孩乐队阶段，之后经历反主流文化、灵性和不满的阶段。')

add(10,'推断','What does the counterfactual about Pet Sounds suggest in the author’s account?',
 ['Exposure to a different part of a band’s work might change the interest it attracts.','The Beach Boys never produced diverse music.','Changing radio play has already been experimentally proved to equalize both bands’ popularity.','Every casual listener has studied the Beach Boys’ entire catalogue.'],0,
 '作者关于Pet Sounds的反事实提出什么可能？',['接触乐队作品的不同部分，可能改变人们兴趣。','Beach Boys从未有多样作品。','已实验证明改变播放可使两乐队人气相等。','每位普通听众都研究其全部作品。'],
 ['A If...had been played...might have been interested保留对接触方式的假设。','B did produce diverse songs明确承认其多样性。','C 反事实不是已实施随机试验，也没equalize结论。','D often equated with某首名曲说明熟悉面可能狭窄，不是全面研究。三位/一位作曲者是本段作者所作对比，不据此扩写全部创作史。'],
 ['If the Beach Boys’ Pet Sounds had been played more often than Surfin’ U.S.A., more people might have been interested in the Beach Boys.'],
 'equated with','被等同于；被视作同一回事','普通听众可能把整个乐队简化为一首代表曲','The writer was often equated with a single famous novel.',['be equated with','a casual music lover'],
 '他们有John、Paul和George三名成员作曲；按本段叙述，相比Brian Wilson一人作曲的Beach Boys，这给了他们更多多样性。Wilson以创新、实验闻名，所以Beach Boys确实也有多样歌曲。但普通乐迷常把他们等同《Surfin’ U.S.A.》：“大家都冲浪去了，冲浪去，美国。”如果《Pet Sounds》比《Surfin’ U.S.A.》更常播放，也许会有更多人对Beach Boys感兴趣。',support='limited-inference')

add(11,'细节','What did the author describe feeling in the summer of 2020?',
 ['Complete freedom to travel and meet his parents whenever he wished.','A sense of being trapped, with ordinary outings and family visits uncertain.','Confidence that the pandemic would end immediately.','No interest in watching films during the lockdown.'],1,
 '作者描述2020年夏天有什么感受？',['随时旅行见父母的完全自由。','被困住，日常外出和探亲都不确定。','确信疫情立即结束。','封闭时对电影毫无兴趣。'],
 ['A 何时返日见父母的疑问表明受限，非随时自由。','B no way out/stuckness及两个When问题共同支持。','C increasingly clear...here to stay与立即结束相反。','D watched a lot of movies明确看许多电影。这里是个人回忆，不据其感受诊断所有隔离者。'],
 ['I felt as though there was no way out, a sense of stuckness','When could I go back to Japan and see my aging parents?'],
 'stuckness','受困感；停滞感','作者觉得无路可走、难以恢复日常的主观感受','The long interruption left her with a sense of stuckness.',['a sense of stuckness','here to stay'],
 '2020年夏天，越来越清楚疫情不会很快消失，我觉得像无路可走，陷于停滞，整天关在屋里。什么时候才能外食、与人相聚？什么时候能回日本见渐老的父母？封闭在家，我们看了许多电影。')

add(12,'逻辑关系','How does the author distinguish the film’s premise from why it stayed with him?',
 ['He says he became the only real person who remembered the Beatles.','He attributes all its value to an exceptionally good plot.','He rejects the film as completely forgettable in every respect.','He outlines the fictional premise but says its memorability came from something beyond the plot.'],3,
 '作者怎样区分电影设定与它令人难忘的原因？',['说自己成了现实中唯一记得Beatles的人。','把全部价值归于格外精彩的情节。','认为电影各方面完全不值得记。','概述虚构设定，但说难忘之处在情节之外。'],
 ['A only person是电影主人公设定，非作者现实身份。','B movie was OK是较平的评价，completely different reason other than plot排除主要因情节难忘。','C memorable明确仍难忘。','D Still把一般情节评价与另一难忘原因区分，具体原因留给后段，不擅补新情节。'],
 ['The movie was OK. Still, it was memorable for a completely different reason other than the plot.'],
 'protagonist','主人公；主角','电影叙事里的歌手，须与看电影的作者分清','The protagonist discovers a world that has forgotten the songs.',['a struggling protagonist','other than the plot'],
 '其中一部是2019年电影《Yesterday》。主人公是个艰难谋生的歌手，发现只有自己还记得Beatles，于是开始唱他们的歌并出名。电影还可以。不过，它令人难忘，完全是由于情节以外的另一个原因。')

add(13,'细节','Why did the song affect the author so strongly?',
 ['Its lyrics expressed how he felt during COVID.','He had written it with the film’s lead actor.','The plot proved his family had forgotten the band.','It was the first song he had ever heard.'],0,
 '这首歌为何强烈触动作者？',['歌词表达了疫情期间的感受。','他与男主角合写了歌。','情节证明家人忘记了乐队。','那是他生平第一次听歌。'],
 ['A captured how I felt给出直接原因。','B 无作者作词或与演员合作信息。','C 电影设定不能移给现实家人。','D 没说第一次听任何歌。妻子和两个青少年孩子在旁，使他觉得哭泣尴尬，不代表他们也同哭或嘲笑他。'],
 ['But its lyrics captured how I felt during COVID.'],
 'captured','准确表达；抓住','歌词契合主观处境，不是物理捕获','The poem captured her feeling of being far from home.',['capture how someone feels','could not stop crying'],
 '主角唱《The Long and Winding Road》时，我止不住哭。我与妻子、两个青少年孩子一起看，所以很尴尬。但歌词准确表达了我在COVID期间的感受。')

add(14,'主旨','What distinction does the passage introduce?',
 ['The Beatles have no substantial body of work to revisit.','Repeated listening always increases psychological richness regardless of attention.','Returning to familiar comfort through nostalgia differs from discovering something new.','Nostalgia is defined as an inability to remember anything.'],2,
 '本段引入什么区分？',['Beatles没有可重访的丰富作品。','不论如何注意，重复听都必增加心理丰富。','怀旧地回到熟悉舒适，与发现新东西不同。','怀旧就是完全无法记事。'],
 ['A abundant/diverse bodies直接相反。','B important to distinguish反对把单纯重复等同新丰富。','C reenactment of past/comfort zone说明怀旧活动，而开头go deep/find new提示另一种重访方式。','D reenactment是重现过去，不是失忆。本段并没说怀旧没有任何好处。'],
 ['it is important to distinguish between nostalgia and psychological richness.','returning to the same familiar comfort zone.'],
 'bodies of work','作品总集；一系列作品','body在这里是艺术家积累的作品，不是人体','The archive preserves several diverse bodies of work.',['abundant bodies of work','reenactment of the past'],
 '对Beatles、Bob Dylan和Aretha Franklin，你能不断深入、发现新东西，因为他们留下丰厚而多样的作品。不过，区分怀旧与心理丰富很重要。许多人不断听同些乐队，是因为怀旧。这里主要活动是重演过去，回到同一个熟悉舒适区。')

add(15,'逻辑关系','What makes listening to the same band psychologically rich in the author’s distinction?',
 ['Avoiding every connection between past and present.','Continuing to notice previously unnoticed aspects.','The mere fact that the band is familiar.','Feeling nostalgia while noticing nothing new.'],1,
 '按作者区分，持续听同一乐队何以构成心理丰富？',['避免过去现在任何连接。','继续注意到以前没注意的方面。','仅仅因为乐队熟悉。','仅怀旧而无任何新发现。'],
 ['A 作者承认怀旧能连接过去现在，没要求消除。','B noticing something...didn’t notice before给出关键。','C 熟悉本身不足，重访时有新发现才是此处所说丰富。','D for sake of nostalgia does not increase明确区分；但怀旧仍有联系、社交、意义等益处，不把不同益处判成毫无价值。'],
 ['if you keep listening to the same band because you keep noticing something you didn’t notice before, that is a psychologically rich experience'],
 'for the sake of','为了；出于……目的','限制纯为怀旧而听的目的，与带着新注意的重听对照','They returned to the song for the sake of nostalgia.',['for the sake of nostalgia','social connectedness'],
 '说清楚些，怀旧——对自己过去的感伤向往——有许多好处：连接过去与现在、加强社会联结、帮助找到人生意义。但纯为怀旧听同一乐队，不会增加心理丰富。相反，若你不断听是因为总发现以前没注意的新东西，那就是心理丰富的体验，是在熟悉对象中发现丰富。')

add(16,'作者意图','Why is Offill’s essay introduced?',
 ['To report that readers must abandon familiar novels after one reading.','To show that Woolf has fans only in one generation.','To replace the topic of new discoveries with a ranking of magazine sales.','To illustrate how repeated readings of one novel can reveal new things.'],3,
 '为何引入Offill的文章？',['要求读者读一次后就弃旧小说。','说明Woolf仅有一代粉丝。','把新发现主题换成杂志销量排名。','说明反复读同一本小说仍可发现新东西。'],
 ['A many times与只读一次相反。','B across generations明确跨代。','C 无销量数据或排名。','D discover many new things on each read承接熟悉作品中的丰富。十七八岁是她初读年龄，不是人物或作者Oishi的年龄。'],
 ['it’s possible to read Mrs. Dalloway many times and discover many new things on each read.'],
 'across generations','跨越不同世代','描述作品长期被不同年龄世代读者喜爱','The novel attracted readers across generations.',['fans across generations','on each read'],
 '像Beatles一样，Virginia Woolf跨世代都有热情读者。小说家Jenny Offill为《New Yorker》写了一篇题为《A Lifetime of Lessons in Mrs. Dalloway》的文章。她概括了为什么能一再读《Mrs. Dalloway》，每读一次都发现新东西。初读时，她十七八岁。')

add(17,'细节','Which character captures the reader’s attention in this passage?',
 ['A carefree child without any experience of war.','Richard, whose profession is described in detail here.','Septimus Warren Smith, a war veteran with deep trauma.','The real novelist Woolf serving as an officer in the war.'],2,
 '本段中，哪位人物吸引这位读者？',['无战争经历的无忧儿童。','本段详述职业的Richard。','受深创伤的退伍军人Septimus Warren Smith。','作为真实军官参战的小说家Woolf。'],
 ['A war veteran/deep trauma都与选项相反。','B 此段未介绍Richard职业。','C captivated by直接连接人物和退伍创伤背景。','D Woolf是介绍人物的小说作者，不能把人物背景归给作者。这是文学人物和读者认同，不是临床诊断样本。'],
 ['She was captivated by Septimus Warren Smith, the war veteran with a deep trauma.'],
 'captivated','被深深吸引；着迷','指读者被小说人物吸引，而非人物被实际囚禁','She was captivated by the character’s inner life.',['be captivated by','a war veteran'],
 '她被Septimus Warren Smith吸引，他是一名有深刻创伤的退伍军人。Woolf这样介绍他：“大约30岁，脸苍白，鹰钩鼻”，又写：“世界举起了鞭子；它将落在何处？”Offill想：“对，就是这个。完全就是。”')

add(18,'细节','How does Offill’s focus shift across the later readings described?',
 ['In her thirties she notices Clarissa; at a later reading closer to Clarissa’s age, Peter moves her.','She focuses only on Septimus in every reading.','Peter interests her in her thirties, but Clarissa appears only in her childhood reading.','The focus changes because the novelist rewrote the characters between her readings.'],0,
 'Offill后来的重读，注意对象怎样变化？',['30多岁关注Clarissa；后来接近其年龄时被Peter打动。','每读都只关注Septimus。','30多岁关注Peter，童年才见Clarissa。','小说家在她每次读之间重写人物，故对象变。'],
 ['A thirties/intrigued Clarissa与Finally/moved Peter对应。','B 明确列出新的吸引对象，非始终仅一人。','C 人物与阶段错配，也把初读改为童年。','D 原文呈现读者阶段变化，没有作品被重写信息。“进入第52年”原措辞保留，不算作已满52岁的精确年龄证明。'],
 ['This time she was intrigued by Clarissa Dalloway','This time, she was moved by Peter Walsh, Clarissa’s old flame'],
 'old flame','旧情人；昔日恋人','指人物过去的恋爱关系，非实际火焰','He met an old flame after many years.',['an old flame','find relief in self-distancing'],
 '到了30多岁，她再读一次。这次，她对Clarissa Dalloway着迷，后者会注意到“笑着带那荒唐的毛茸茸小狗去跑步的女孩”。最后，Offill到了与Mrs. Dalloway相仿的年纪——“刚进入生命的第52年”——又读一次。这次打动她的是Clarissa的旧情人Peter Walsh；他在自我抽离中找到宽慰，一切不再那么与自身纠缠。')

add(19,'逻辑关系','What made identification with Clarissa and Peter easier for Oishi?',
 ['He had personally written both fictional characters.','He had been their childhood classmate.','He had already carried out a clinical study of them.','He was at a similar life stage, recognizing everyday obligations and preoccupation with the past.'],3,
 '什么使Oishi更易认同Clarissa和Peter？',['他亲自写了这两人物。','他是两人的童年同学。','他已对其做临床研究。','处于相仿人生阶段，认出日常义务与对往事的执念。'],
 ['A 小说作者是Woolf，不是Oishi。','B 虚构人物不是作者现实同学。','C 个人读书感受不是临床研究。','D was...age后接That made it easy，列义务、倦怠、往事等共鸣。Peter后面自述失败不能当作作者本人政治身份。'],
 ['I was Clarissa Dalloway and Peter Walsh’s age. That made it easy to identify with those characters'],
 'ennui','倦怠；无聊厌倦感','人生琐事中的厌倦情绪，非这里正式诊断的疾病','The routine sometimes filled him with ennui.',['daily obligations and ennui','identify with characters'],
 '我读《Mrs. Dalloway》时，年纪与Clarissa Dalloway、Peter Walsh相仿。这使我容易认同他们：日常生活的责任、倦怠、昔日的执念，以及对过去本身的执念。Peter谈自己的失败，说：“他曾是社会主义者，从某种意义上说是个失败者——没错。')

add(20,'细节','Which change in Sally’s appraisal of Richard is described?',
 ['She once praised his intellect but now says he has declined.','She once mocked his intelligence but now says he has improved.','She says Peter has improved and plans to marry him.','She never knew Richard before the party.'],1,
 '本段描述Sally对Richard评价有什么变化？',['曾夸聪明，如今说退步。','曾嘲他不够聪明，如今说他进步了。','说Peter进步并计划嫁他。','派对前从不认识Richard。'],
 ['A deride...not smart enough与过去称赞相反；improved非退步。','B used to deride和Richard has improved对照直接支持。','C Richard不是Peter，也没有婚嫁计划；Richard是Clarissa丈夫。','D used to deride说明此前已评价他。开头仍承接Peter关于年轻人的内心话，不应把这段全部归给Sally。'],
 ['who used to deride Richard, Clarissa’s husband, as not smart enough','Richard has improved. You are right. I shall go and talk to him.'],
 'deride','嘲笑；讥讽','Sally过去对Richard智力的轻视，与此时改观对照','She no longer derided the ideas she once dismissed.',['deride someone as','has improved'],
 '“但他想，文明的未来仍在那样的青年手里；在30年前像他那样的青年手里：热爱抽象原则，让书从伦敦一路送到喜马拉雅山顶，读科学、读哲学。”派对结束时，Clarissa少年时的好友Sally——过去嫌Clarissa的丈夫Richard不够聪明——说：“Richard进步了。你说得对。我去和他说说话。')

add(21,'作者意图','What does the comparison of “brain” and “heart” foreground in the quoted speech?',
 ['A medical claim that the brain is physiologically unnecessary.','A demand to replace all emotion with abstract reasoning.','The relative value of human feeling rather than intellect alone.','Proof that Peter has permanently stopped feeling excitement.'],2,
 '引文中brain与heart的比较突出什么？',['大脑生理上不必要的医学主张。','要求以抽象推理替换全部情感。','相较只看智力，更关注人的感情价值。','证明Peter永久不再激动。'],
 ['A 小说对白比喻智力与心性，不是医学实验。','B 问What does brain matter...compared with heart是质疑只看聪明，非排除情感。','C 延续人物重新评价他人的语境，突出心性/感情的重要。','D 后半Peter问terror/ecstasy/excitement，恰有强烈情绪。其疑问在此尚未答，不补成确定诊断。'],
 ['What does the brain matter…compared with the heart?'],
 'ecstasy','狂喜；强烈喜悦','Peter追问的强烈情绪之一，此处非药物名称','He felt a sudden sense of ecstasy at the reunion.',['terror and ecstasy','extraordinary excitement'],
 '“我去道晚安。比起心，大脑又算什么呢？”最后，年长的Peter自问：“这是什么恐惧？这是什么狂喜？……是什么让我如此激动？”')

add(22,'细节','Who is named as the answer in this sentence?',
 ['Clarissa, described as his former love.','Sally, described as the novelist.','Richard, described as his old teacher.','Septimus, described as a childhood friend.'],0,
 '本句把谁点明为答案？',['Clarissa，被称为他的昔日恋人。','Sally，被称为小说家。','Richard，被称为旧老师。','Septimus，被称为童年朋友。'],
 ['A Clarissa与old flame都是本句明示。','B 人名和身份都无此句支持。','C 不能把别的人物关系补成师生。','D 本句没有Septimus或童年同学关系。句中His承接前段Peter，短句不重复前段提问原文。'],
 ['His answer was Clarissa, his old flame.'],
 'answer','答案；回应','对前文情绪追问所给的人物指向，非客观实验变量','Her answer was the person she had known for years.',['his answer was','his old flame'],
 '他的答案是Clarissa，他的旧情人。')

add(23,'逻辑关系','What discrepancy about Peter is emphasized?',
 ['He lacked any education but published several novels.','He had fulfilled every youthful ambition before fifty-two.','He never expressed any interest in becoming a writer.','Despite education, travel, and a youthful writing ambition, he says he has written nothing.'],3,
 '本段强调Peter什么落差？',['无教育却出版多部小说。','52岁前实现所有青年抱负。','从未想过当作家。','受过教育、旅行多、年轻想写作，却说一字未写。'],
 ['A well-educated与缺乏教育相反；Not a word也不支持已出版。','B truly clueless及未写字与全部实现相反。','C thought he would be a writer直接否定。','D 资历、抱负与实际自述之间的反差明确；这是对小说人物的讨论，不是说本书作者未写过字。'],
 ['When he was young, he thought he would be a writer.','Peter replied, at age fifty-two, “Not a word!”'],
 'clueless','茫然的；毫无头绪的','这里指不知道自己人生想要什么，不等于没受教育','Despite his experience, he remained clueless about what he wanted next.',['clueless as to','a youthful ambition'],
 'Peter受过良好教育，也游历甚广，却对自己人生想要什么十分茫然。年轻时，他以为会成为作家。Sally问：“你写了吗？”52岁的Peter答：“一字没写！”')

add(24,'推断','What can be inferred about Peter’s attention to Clarissa?',
 ['Love in India erased all memories of Clarissa.','His attachment to Clarissa persists despite another love in India.','He remembers Clarissa only as a stranger at the party.','The author has already explained exactly why she attracts him.'],1,
 '关于Peter对Clarissa的关注，能推什么？',['在印度的爱抹掉所有Clarissa记忆。','虽在印度另有爱情，对Clarissa的牵挂仍在。','只把她记作派对陌生人。','作者已精确解释她为何吸引他。'],
 ['A Throughout the novel...thinks about明显不是抹去。','B Although...found love in India...could not keep eyes off her支持牵挂仍存，不据此补写具体关系行为。','C childhood/adolescence/adulthood均被回想，不是仅陌生人。','D 末句还在问吸引原因。开头and laughed承接上一单元回答，保留旧边界，非独立叙事人物新增。'],
 ['Although he found love in India, he could not keep his eyes off her.'],
 'could not keep his eyes off','无法把目光从……移开','这里表示持续被吸引，不是眼睛受伤的字面症状','He could not keep his eyes off the familiar face.',['keep one’s eyes off','throughout the novel'],
 '并笑了。整部小说里，Peter都想着Clarissa，童年、少年、成年时的她。虽然在印度找到了爱情，他仍无法把目光从她身上移开。Clarissa究竟有什么吸引力？（首句动作承接上一单元。）',support='limited-inference')

add(25,'主旨','How does the author connect Peter’s attraction with Offill’s reading?',
 ['Both demonstrate that familiarity must lead to boredom.','Both prove a single psychological cause through an experiment.','Both repeatedly find appeal in something familiar, even as the exact cause of attraction remains partly mysterious.','Both require replacing the familiar person or book with a new one.'],2,
 '作者怎样连接Peter的吸引与Offill的阅读？',['两者都说明熟悉必无聊。','两者用实验证明单一心理原因。','都在熟悉对象中反复发现吸引，尽管具体原因仍有谜。','都须用新人新书替掉熟悉对象。'],
 ['A No boredom here直接否定必然无聊。','B largely a mystery承认未知；文学比较也非实验因果证明。','C As...Offill...Peter...并列持续发现书/人的新旧魅力。','D one woman及同一本Mrs. Dalloway强调深入熟悉对象，不是不断更换。'],
 ['That is largely a mystery to me.','As Offill finds a lifetime of lessons from Mrs. Dalloway, Peter keeps finding old and new appeal in Clarissa.'],
 'appeal','吸引力；魅力','指人物对Peter的新旧吸引，不是向法院上诉','The familiar story retained its appeal while revealing new details.',['old and new appeal','a lifetime of lessons'],
 '这对我而言大体仍是谜。但这里有个52岁的男人，依然疯狂地爱着旧女友。这里没有无聊，而是对同一个女人纯粹、真切、无尽的好奇。正如Offill从《Mrs. Dalloway》发现一生的启示，Peter也不断在Clarissa身上发现旧与新的吸引力。')

assert len(out)==25 and [q['id'] for q in out]==[t['questionId'] for t in targets]

def persist():
 path=ROOT/'source/short-questions/additional.json';existing=load('source/short-questions/additional.json');byid={q['id']:q for q in existing}
 for q in out:
  if q['id'] in byid:assert byid[q['id']]==q,('Refuse to overwrite changed authoring',q['id'])
  else:existing.append(q)
 path.write_text(json.dumps(existing,ensure_ascii=False,indent=2)+'\n',encoding='utf8',newline='\n')
 review=dict(batchId='batch-039',date='2026-10-24',pdfSha256=b['pdfSha256'],checkedPdfPages=list(range(155,159)),questionIds=[q['id'] for q in out],paragraphs=[dict(id=pid,textSha256=hashlib.sha256(pp[pid]['text'].encode()).hexdigest()) for pid in dict.fromkeys(q['paragraphId'] for q in out)],note='完整PDF155–158原页视觉核对。Jiro有竞争者但未同等被紧盯比较，不改成毫无竞争；toes为警醒习语，反刍解释非普遍临床因果，童年玩心出自同学访谈。职业路径provided that深度足够才可探索，one way非唯一。Spotify11,861,427/30,561,926为as of this writing快照非实时；大学生偏好为作者观察，音乐多样性One possible explanation与Pet Sounds反事实不作已证因果，承认Beach Boys作品也多样，作曲者比较仅归本段。Yesterday情节为电影非现实，哭泣为作者歌词共鸣不补歌词或全家反应。怀旧有联系/意义等益处，熟悉对象中新发现区别于纯怀旧。Offill重读人物Septimus/Clarissa/Peter按阶段，不混小说人物与现实作者，fifty-second year保留原措辞不擅算已满52。Peter/Sally/Richard角色与话语分清；brain/heart为文学比喻，Not a word为人物答话，and laughed续接旧边界不当独立最终句。吸引原因mystery不补造；文学例证非实验。额外正文审计待办保持开放，不以候选池完整代替全书正文完整。')
 (ROOT/'source/short-questions/review-chapter13-devotion-art25.json').write_text(json.dumps(review,ensure_ascii=False,indent=2)+'\n',encoding='utf8',newline='\n')
 print('Saved',len(out),'of 25 individually authored exercises')

if __name__=='__main__':persist()
