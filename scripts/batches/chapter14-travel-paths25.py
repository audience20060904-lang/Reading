"""25 individually authored exercises for frozen targets, PDF pages 163-166.
Preserve printed English, source positions and all previously published questions.
"""
from pathlib import Path
import json,hashlib
ROOT=Path(__file__).resolve().parents[2]
load=lambda p:json.loads((ROOT/p).read_text(encoding='utf8'))
b=load('public/data/book.json');plan=load('public/data/reading-plan.json');targets=load('source/short-questions/batch041-targets.json')['targets']
ss={s['id']:s for s in b['sentences']};pp={p['id']:p for p in b['paragraphs']};out=[]
def add(i,kind,prompt,options,answer,prompt_zh,options_zh,analyses,quotes,word,meaning,context,example,collocations,translation,support='explicit'):
 t=targets[i-1];u=next(u for u in plan['units'] if u['id']==t['readingUnitId']);group=[ss[sid] for sid in u['sentenceIds']];p=pp[u['paragraphId']];text=p['text'][group[0]['start']:group[-1]['end']]
 assert hashlib.sha256(text.encode()).hexdigest()==t['passageSha256'];evidence=[]
 for quote in quotes:
  offset=text.find(quote);assert offset>=0,(i,quote);start=group[0]['start']+offset;end=start+len(quote);touching=[s for s in group if s['start']<end and s['end']>start]
  evidence.append(dict(quote=quote,sentenceIds=[s['id'] for s in touching],sources=list({(r['pdfPage'],r['block']):r for s in touching for r in s['sources']}.values())))
 assert word.lower() in text.lower(),(i,word)
 out.append(dict(id=t['questionId'],version=1,readingUnitId=u['id'],chapterId=u['chapterId'],sectionId=u['sectionId'],paragraphId=u['paragraphId'],sentenceIds=u['sentenceIds'],passage=text,prompt=prompt,options=options,answer=answer,type=kind,promptZh=prompt_zh,optionsZh=options_zh,analyses=analyses,evidence=evidence,vocabulary=[dict(word=word,meaning=meaning,context=context,example=example,collocations=collocations)],translation=translation,support=support,editorialStatus='完整PDF163–166原页视觉核对。游轮/背包为比喻非旅游产品推荐；九国受访中many Americans非全体，一名UVA学生非九国统一答案。700机票/250三十日通票为作者昔日回忆非当前报价；1988市中心描述不扩为今日城市安全结论。末程三天约70小时、20美元被骗等于日预算非全程旅费。男子承诺与实际消失分段区分，骑警经历个人叙述不推广群体。Chicago聚会后才知Wisconsin，不补路线/绑架；饮酒和接受邀请为回忆非给读者行动要求。Foer同名主人公为小说例证，heritage/coherence/significance关联意义不强制人生路径。志愿项目只作书中例子非质量认证；朋友/地点示例非互斥类型。歌曲为艺术引述非实证城市承诺。作者明确not best/not always better/one way，三维可共存，Sacks seemed与Linda seems保留；1980年代in earnest不否认古代哲思；未来第四维might/文化差异likely非已发现。既有候选池与两段额外开章正文/辅助材料审计仍区分，不宣称全书完成。'))







add(1,'作者意图','What aspect of a happy life does the cruise metaphor emphasize?',
 ['Constant uncertainty about where to sleep.','The need to plan every detail independently.','A requirement that everyone must travel to the Caribbean.','Comfort and having practical needs arranged for oneself.'],3,
 '游轮比喻强调快乐人生的什么方面？',['总不知道睡哪里。','必须独立规划全部细节。','要求每人必须去加勒比。','舒适，实际需求由别人安排照料。'],
 ['A Everything planned与住宿不确定相反。','B taken care of表示安排好，非都独自做。','C like是人生比喻，不是实际旅行命令。','D planned/get fed/taken care of共同突出安稳受照料。播客两位作者借旅行作比，非此段比较游轮乘客的实验。'],
 ['A happy life is like a Caribbean cruise. Everything is planned. You get fed, and everything is taken care of.'],
 'taken care of','被照顾；得到安排','食物和其他需求已有安排，体现比喻的轻松一面','All the practical details were taken care of.',['be taken care of','a trip metaphor'],
 '在播客《Two Psychologists Four Beers》中，Yoel Inbar与Alexa Tullett用这些旅行比喻，描述快乐人生与心理丰富人生。快乐人生像加勒比游轮旅行：一切规划好，有人提供吃的，所有事都有人照料。')

add(2,'细节','What does the quoted student’s ideal emphasize?',
 ['An obligation to work harder during every vacation.','Financial comfort, family happiness, and freedom from work worries.','A desire to visit all nine countries in the study.','A claim that every American described the same ideal.'],1,
 '这位学生引述中的理想强调什么？',['每次度假都必须更努力工作。','经济舒适、家庭幸福、不再担忧工作。','想游遍调查九国。','声称每位美国人理想相同。'],
 ['A not want to worry about working与加班义务相反。','B beach/money/happy family/no need work是该个案的明确内容。','C nine countries是招募范围，非学生计划。','D many Americans不是all，且这只是一位18岁UVA学生举例，不能当九国所有人的统一回答。'],
 ['On a beach with lots of money and a happy family.','I would not want to worry about working'],
 'rejuvenation','恢复活力；休整','此处休假放松的恢复，不等于前文关系更新的具体机制','The quiet holiday offered time for rest and rejuvenation.',['relaxation and rejuvenation','an ideal life'],
 '我们请九国参与者描述理想人生时，许多美国人写得像豪华游轮生活。比如，一位18岁UVA学生写：“在海滩，有许多钱和幸福家庭。我不想担忧工作，因为已经足够成功，不再需要工作。”对许多人，假期和理想人生是放松、恢复活力，被服务和娱乐。')

add(3,'逻辑关系','Which combination defines the backpacking analogy here?',
 ['Personal choice alongside responsibility and uncertainty.','Complete advance planning by a company with no personal choices.','A guarantee that nothing unpleasant will happen.','A claim that a rich experience must always feel comfortable.'],0,
 '这里背包游类比由哪组特点组成？',['自主选择，同时承担责任与未知。','公司提前安排一切，个人无选择。','保证无不快。','声称丰富体验总须舒适。'],
 ['A plan...by yourself/choose与never know/might bad一起给出自主和不确定。','B 与自己规划相反。','C might encounter bad明确保留不利可能。','D 本段恰容纳可能不舒适，未把心理丰富等同一直快乐。类比不是背包旅游必定丰富的实验保证。'],
 ['You have to plan it all by yourself. You can choose what you want to do.','you never know what to expect, and you might encounter something bad.'],
 'at the same time','与此同时；同时又','并列自主选择的好处和未知风险，不是在说只有好处','She valued the freedom. At the same time, she recognized the uncertainty.',['at the same time','choose what to do'],
 '心理丰富的旅程像背包游。你得自己规划全部，也能选择做什么。同时，你不知道会遇到什么，也可能碰上坏事。')

add(4,'细节','Which purchase is correctly described?',
 ['A thirty-day airline pass costing about $250.','A $700 daily bus ticket bought in Los Angeles.','Flights from Tokyo to LA for about $700 and a thirty-day Greyhound pass for about $250.','Prepaid accommodation for thirty days costing $700.'],2,
 '哪项正确描述了购买项目？',['约250美元30日航空通票。','在洛杉矶买700美元每日巴士票。','东京到LA约700美元机票，另250美元30日灰狗通票。','预付30日住宿700美元。'],
 ['A 250对应Greyhound巴士通票，不是航空。','B 700为Tokyo到LA机票，非每日巴士。','C 两金额、交通方式与30日期限逐项对应。','D 本段未买住宿。about为约数，且都是作者昔日旅行回忆，非可购买的今日报价。'],
 ['Malaysia Airlines for about $700','a thirty-day Greyhound pass, which was about $250.'],
 'available','当时可买到的；可获得的','cheapest tickets available指那次购买时的可选机票，不是今天市场最便宜','They chose the least expensive tickets available at the time.',['the cheapest tickets available','a thirty-day pass'],
 '我在东京读大一时，与朋友去美国背包旅行。我们买当时能找到的最便宜机票，从东京到LA，搭Malaysia Airlines约700美元；另买30日Greyhound通票，约250美元。')

add(5,'逻辑关系','Why did the final stretch become an almost nonstop bus ride?',
 ['They had decided to visit no city before Washington.','The original pass allowed travel for only seventy hours.','Their friend had booked a new flight from Washington.','They realized in Washington that little time remained to get back to LA.'],3,
 '为什么最后变成几乎不停的长途巴士？',['到华盛顿前决定不访任何城市。','原通票只准70小时。','朋友已订华盛顿新机票。','到华盛顿时发现返LA所余时间很少。'],
 ['A 前面已列多城市，非全跳过。','B pass30日，70小时是末段乘车时间，不能互换。','C 没有新订航班。','D almost out of time→so final three days解释时间压力。almost nonstop非一秒也未停车，not exactly fun也是不太愉快的委婉表达。'],
 ['we realized we were almost out of time, so the final three days were an almost nonstop bus ride from D.C. to LA.'],
 'almost out of time','时间几乎用完；所剩无几','说明行程规划使返程紧迫，不是预算已经用完','They were almost out of time and had to return directly.',['almost out of time','an almost nonstop ride'],
 '我们用30天从LA乘灰狗到旧金山、西雅图、南达科他州拉什莫尔山、芝加哥、尼亚加拉瀑布、纽约，再到华盛顿D.C.。到D.C.才发现时间几乎用完，所以最后三天几乎不停乘巴士返LA。70小时车程……可不怎么好玩。')

add(6,'细节','Which conditions contributed to the frightening moments in this account?',
 ['No advance bookings, a limited budget, little English, and the station locations described for 1988.','A luxury hotel booking that removed every uncertainty.','Fluent English and unlimited accommodation funds.','A current safety assessment of every American downtown.'],0,
 '这段叙述中，哪些条件伴随令人害怕的时刻？',['未预订、预算有限、英语少，以及所述1988年车站位置。','豪华酒店预订排除一切未知。','英语流利且住宿经费无限。','对今日所有美国市中心的安全评估。'],
 ['A 首句临到找住宿，末句预算/英语限制，中间车站位置和back in1988提供叙述背景。','B didn’t have reservations且只付得起hostels，非豪华预订。','C limited/minimal都与之相反。','D 过去个人经历不是今日所有街区风险指南；almost always也非每一个车站。'],
 ['We didn’t have any reservations for hotels in advance','With our limited budget and minimal English, we encountered many scary moments.'],
 'in advance','提前；事先','订房原本可在抵达前完成，但作者说未如此做','They had not booked accommodation in advance.',['reservations in advance','a limited budget'],
 '我们未提前订酒店，到洛杉矶、旧金山、西雅图后才找住处。只负担得起青年旅舍。灰狗站几乎总在市中心，1988年那些地方不算最安全。预算少、英语又很有限，我们遇到许多惊险时刻。')

add(7,'细节','What did the man promise when asking to borrow $20?',
 ['To buy the author a permanent bank account.','To obtain cash at the nearby bank and repay him.','To pay for a thirty-day Greyhound pass.','To guide him to a hotel in Wisconsin.'],1,
 '男子借20美元时许诺什么？',['给作者买永久银行账户。','到附近银行取现金并还他。','付30日灰狗通票。','带他到威斯康星酒店。'],
 ['A nearby bank不等于替人开账户。','B go to bank/get cash/pay me back是男子的承诺；此段尚未给实际兑现结果。','C 通票是前面作者行程，非男子许诺。','D 混入后文不同旅行事件与地点。说了会还，不等于有证据已经归还。'],
 ['He said he would just go to the bank, get cash, and pay me back.'],
 'pay me back','还钱给我；偿还','转述陌生人的承诺，不能误读成钱已退回','He promised to pay me back the next day.',['borrow money','pay someone back'],
 '纽约时，我们在42街青年旅舍外，一名男子靠近我，问能否借20美元。旁边就有Citibank。他说去银行取现金便还我。“跟我来。”他说。')

add(8,'推断','What made the $20 loss especially significant to the narrator?',
 ['It represented the total cost of his flights.','It was the price of the full month’s bus pass.','It was money he had already recovered at the bank.','It equaled his daily budget.'],3,
 '20美元损失为什么对叙述者特别重要？',['是全部机票费。','是整月巴士通票价。','是已从银行取回的钱。','相当于一天预算。'],
 ['A 机票金额来自别段，非20美元。','B 日预算不同于月通票。','C disappeared/scammed没有已追回证据。','D which was my daily budget给出金额对个人处境的重要性。不能据此说整趟旅费全被骗。'],
 ['scammed out of $20 in Times Square, which was my daily budget!'],
 'scammed out of','被骗走〔钱财〕','作者回顾钱被拿走、对方消失的事件，不是成功借贷','He was scammed out of the money he had lent.',['be scammed out of money','a daily budget'],
 '于是我跟他到银行排队。过一阵子，他不见了。就这样，我在时代广场被骗20美元——那可是我一天的预算！',support='limited-inference')

add(9,'逻辑关系','What contrast does “Yet that same day” introduce?',
 ['They were expelled from the park but later toured inside the White House.','They never reached Washington despite leaving New York.','Police officers invited them to sleep longer on the bench.','The White House tour happened before their bus left New York.'],0,
 'Yet that same day引入什么反差？',['被赶离公园，却同日进入白宫参观。','虽离开纽约但没到华盛顿。','警察请他们在长椅多睡。','离开纽约前已参观白宫。'],
 ['A kicked us out与go inside White House同日形成遭遇反差。','B arrived Washington明确到达。','C 作者描述thought homeless/physically kicked out，非邀请。','D early-morning arrival后that same day不支持此前参观。这里只复述其个人经历，不推广所有警察或今日参观政策。'],
 ['They thought we were homeless and literally and physically kicked us out. Yet that same day, we were able to go inside the White House on a tour.'],
 'ended up','最终；结果到了……境地','表示抵达后睡在长椅上的结果，不必是提前计划','They ended up resting on a bench after the overnight journey.',['end up falling asleep','that same day'],
 '从纽约的巴士清早到华盛顿D.C.，我们后来在白宫附近的公园长椅睡着。不久，一群骑警出现，把我们当成无家者，真的动脚把我们赶走。可就在同一天，我们又能进白宫参加参观。')

add(10,'细节','What additional activity is stated?',
 ['A paid tour of every government building.','A free Capitol Hill tour.','A permanent job on Capitol Hill.','A private meeting with the president.'],1,
 '本句另说参加了什么？',['付费游遍所有政府大楼。','免费Capitol Hill参观。','国会山永久工作。','与总统私下会面。'],
 ['A for free非付费，也没every building。','B 地点活动与免费直接对应。','C tour不是受雇。','D 没有总统会面信息。过去参加免费行程，不是对今日价格与准入的实时承诺。'],
 ['We also went on the Capitol Hill tour for free.'],
 'for free','免费地；不收费','修饰那次参观的费用，非所有当地消费都免费','They attended the exhibition for free.',['go on a tour for free','also went on'],
 '我们还免费参加了Capitol Hill的参观。')

add(11,'细节','How did the encounter with the three young people begin?',
 ['His friend introduced them at the White Sox game.','They invited him to Wisconsin before speaking to him.','They asked him for a picture at a festival he attended alone.','He had booked a guided meeting with them in advance.'],2,
 '与三位年轻人的相遇怎样开始？',['朋友在White Sox球赛介绍。','没交谈就邀他去威斯康星。','他独自逛节庆时，他们请他拍照。','他事先预约导览会面。'],
 ['A friend去球赛，作者自己去festival，不能把两处相遇合并。','B 这里先拍照，邀请在后文，地点也没给。','C went alone/met three/asked picture逐项支持。','D ended up meeting表偶遇，非预约。'],
 ['So I went alone and ended up meeting three other young people there. They asked me to take a picture of them, so I did.'],
 'ended up meeting','后来偶然遇见；结果结识','与朋友分开行动后出现非预定相遇，不是事前安排的活动','She ended up meeting new people at the festival.',['take a picture of someone','go alone'],
 '到芝加哥时，Grant Park有盛大节庆。朋友去看White Sox球赛，我却想逛节庆。于是独自去了，后来结识三位年轻人。他们请我帮拍照，我便拍了。')

add(12,'逻辑关系','What does “but I said yes” contrast with?',
 ['His full knowledge of the address and packed luggage.','His decision to avoid talking to anyone.','A promise to return immediately to his friend’s baseball game.','His lack of knowledge about the house’s location and lack of spare clothes.'],3,
 'but I said yes与什么形成反差？',['对地址完全了解且行李齐全。','决定不和任何人交谈。','保证立刻回朋友球赛。','不知房子位置，也没带换洗衣服。'],
 ['A didn’t have a clue/nor change clothes正相反。','B already started talking，非避免交谈。','C 本段没有球赛承诺。','D 两项准备不足与仍答应邀请形成转折。only time had alcohol是旅程中的一次自述，不扩成读者应仿效饮酒或接受陌生人邀约的建议。'],
 ['I didn’t have a clue where the house was, nor did I have a change of clothes with me, but I said yes.'],
 'didn’t have a clue','毫无头绪；一点不知道','不知道聚会房子在哪里，而不是房子已经被证实危险','I did not have a clue where the station was.',['have a clue where','a change of clothes'],
 '接着我们聊起来。没多久，他们亲切地邀我去其中一人家里聚会。我不知道房子在哪里，也没带换衣，还是答应。这是那趟旅程中我唯一一次喝酒。')

add(13,'细节','What did the author discover about the party location afterward?',
 ['He had spent the night somewhere in Wisconsin.','The party had taken place inside the YMCA.','The house was beside the Times Square bank.','He had never actually left his hostel room.'],0,
 '事后，作者发现聚会地点有什么意外？',['那晚竟在威斯康星某处。','聚会就在YMCA里面。','房子在时代广场银行旁。','其实从没离开旅舍房间。'],
 ['A It turned out...Wisconsin给出之后才知的地点。','B gave a ride back YMCA说明YMCA是返回住处，不是聚会屋。','C 混入纽约被骗的不同事件。','D fell asleep party house与未离房相反。不能从惊讶补写绑架、距离或具体交通路线。'],
 ['It turned out I had been somewhere in Wisconsin that night!'],
 'turned out','后来发现；结果原来','标记事后获知的信息，不是当初已掌握位置','It turned out that the house was much farther away than he thought.',['it turned out that','give someone a ride back'],
 '我在聚会屋睡着。第二天早晨，一位新认识的人开车送我回市中心所住的YMCA。原来那晚我竟在威斯康星某处！我简直不敢相信。')

add(14,'主旨','How does the author assess the bus journey overall?',
 ['As the ideal method that everyone should copy.','As entirely worthless because it was physically uncomfortable.','As uncomfortable, yet memorable and revealing of many sides of the country.','As an experience that was comfortable at every moment.'],2,
 '作者总体怎样评价巴士旅程？',['所有人都应复制的理想方式。','因身体不适而毫无价值。','不舒服，却难忘并看到美国多面。','每刻都舒适。'],
 ['A can’t say...the way没有普遍推荐。','B But...memorable/chance see肯定其价值。','C 疼痛与获得难忘经历并存，区别不舒服与无丰富价值。','D hours sitting造成疼痛，非全程舒适。个人反思并不是现今交通方式评测。'],
 ['My butt certainly hurt from hours of sitting. But I came away from it with a memorable thirty days and the chance to see many sides of the U.S.'],
 'came away from it with','经历后收获；从中带走','指带走回忆和见识，非只携物理行李离开','She came away from the trip with a new perspective.',['come away with memories','a memorable thirty days'],
 '当然，我不能说Greyhound就是横穿美国的最佳办法。长时间坐着，我屁股确实疼。但这趟留下难忘30天，也让我有机会看到美国的许多面。')

add(15,'作者意图','What does the journey in Everything Is Illuminated illustrate?',
 ['A fictional travel example centered on family heritage and self-understanding.','A claim that every vacation must involve finding a wartime rescuer.','Proof that the novelist and protagonist are necessarily the same real person.','A luxury tour designed entirely for passive comfort.'],0,
 '《Everything Is Illuminated》中的旅程说明什么？',['以家族传承和自我理解为中心的虚构旅行例子。','每次度假都必须找战时救助者。','证明小说家与同名主角必是同一真实人。','只为被动舒适设计的豪华游。'],
 ['A 小说情节用于说明意义型旅行，通过家族历史认识自己。','B some vacations不是所有人必须同样寻人。','C also named仅说明同名，不能自动当作作者真实自传。','D 主目的heritage，不是服务娱乐。Augustine是救主角祖父的女人，不是作者Oishi的亲属信息。'],
 ['The main purpose of such a trip is to learn more about your family’s heritage','By learning about your family’s heritage, you learn about yourself.'],
 'heritage','传承；历史渊源','家族在哪里怎样生活、经历何事，不限于金钱继承','The journey helped her understand her family’s heritage.',['family heritage','learn about yourself'],
 '有些假期更关乎意义。Jonathan Safran Foer的《Everything Is Illuminated》中，同名主人公去乌克兰，寻找二战中救过祖父的女人Augustine。这类旅程主要为了解家族传承：家人在哪里、怎样生活，一生发生过什么。了解家族传承，也会了解自己。')

add(16,'细节','Which two components of meaning are named?',
 ['Comfort and entertainment.','Coherence and significance.','Salary and occupational prestige.','Uncertainty and physical danger.'],1,
 '本句点明意义的哪两个构成？',['舒适与娱乐。','连贯感与重要感。','工资与职业声望。','未知与身体危险。'],
 ['A 属前文不同假期目标，非此句所列。','B coherence/significance明确对应。','C 无薪资或声望。','D 本句谈理解传承带来的意义，非风险指标。two key components不等于所有人的意义只准来自家族。'],
 ['a sense of coherence and significance: two key components of meaning in life.'],
 'coherence','连贯性；一致而可理解的整体感','让自身经历和家族背景形成可理解联系的感受','The narrative gave her experiences a sense of coherence.',['coherence and significance','a sense of heritage'],
 '清楚理解自己的传承，也带来连贯感与重要感：这是人生意义的两个关键组成部分。')

add(17,'主旨','What general conclusion follows the volunteer-tourism examples?',
 ['Every volunteer trip has the same measured outcome.','Beach trips are the only legitimate vacations.','Vacations can be shaped around different good-life aims.','A meaningful vacation must exclude any happiness.'],2,
 '志愿旅行例子之后得出什么一般结论？',['每次志愿旅程测得同样结果。','海滩游才是唯一正当假期。','假期可按不同好人生目标设计。','有意义假期必须没有快乐。'],
 ['A 列例子不等于逐个测同样效果，也未作项目质量背书。','B Instead of beach...volunteer正提供其他选择。','C Just like job...happiness/meaning/richness总结多维规划可能。','D 三目标不必互斥。医疗志愿等是书中例子，不能把它当读者应报名的现实项目推荐。'],
 ['Just like a job, vacation can be catered toward increasing happiness, meaning, or psychological richness.'],
 'catered toward','按……需要安排；朝……目标设计','假期可有不同侧重，不限一种统一形式','The course was catered toward learners’ interests.',['catered toward increasing meaning','volunteer tourism'],
 '另一些人选择志愿旅游，如到尼泊尔支持女性教育、到危地马拉做医疗志愿、到肯尼亚保护野生动物。有些大学生春假不去海滩，而为Habitat for Humanity做志愿者。像工作一样，假期也可朝增加快乐、意义或心理丰富来安排。')

add(18,'主旨','What is the scope of the framework in this passage?',
 ['It applies only to paid employment.','It requires all friends to provide exactly the same benefit.','It excludes academic courses from evaluation.','It can be used broadly, including for courses and friendships.'],3,
 '本段框架适用范围怎样？',['只适用有薪工作。','要求所有朋友提供同样好处。','不允许评价课程。','可广泛使用，包括课程与友谊。'],
 ['A pretty much anything超出工作。','B Some...Other说明朋友可有不同价值。','C academic courses明确举课程。','D 开头概括后列课程和朋友，显示跨领域应用；不把fun和helpful固定为互斥人格类别。'],
 ['you can evaluate pretty much anything in terms of happiness, meaning, and psychological richness.','Academic courses can be happy, meaningful, or psychologically rich courses.'],
 'in terms of','从……方面；按……维度','强调评价视角，不是说事物只能有一个维度','They discussed the experience in terms of learning and enjoyment.',['in terms of happiness','evaluate experiences'],
 '总之，几乎任何东西都可从快乐、意义、心理丰富评价。课程可以令人快乐、有意义或心理丰富。有些朋友相处开心；另一些朋友有用、会帮助你。')

add(19,'细节','What role do Jerusalem and Rome play in the examples?',
 ['They illustrate places associated with remembering the past and considering meaning.','They are said to make every visitor forget all troubles instantly.','They prove that exploration is impossible in familiar cities.','They are the only places where people can ever find happiness.'],0,
 '例子中Jerusalem与Rome起什么作用？',['说明可唤起往事和人生意义思考的地方。','让每位访客立刻忘掉所有烦恼。','证明熟悉城市不能探索。','人只能在两地找到快乐。'],
 ['A remember past/think meaning直接给其例证功能。','B 忘烦恼快乐是Disneyland的例子，且不是每人保证。','C 没有否定熟悉城市探索。','D such as是举例，不是only地点限制。同一地点可能有多面价值，不能把这些示例当排他分类。'],
 ['Some places, such as Jerusalem and Rome, help us remember the past and think about the meaning of life.'],
 'expand your horizons','开阔视野；拓展理解范围','指朋友帮助接触新观点经历，非地平线的物理移动','The conversation helped expand her horizons.',['expand your horizons','think about meaning'],
 '另一些朋友帮你开阔眼界。有些地方如Disneyland，让我们忘却烦恼而快乐；有些如Jerusalem和Rome，让我们记起过去、思考人生意义；其他地方鼓励探索，获得心理丰富。')

add(20,'逻辑关系','How does knowing one’s preferred dimension guide action?',
 ['It guarantees that a particular city can provide every possible experience.','It makes all future planning unnecessary.','It helps one select and arrange experiences aligned with one’s goals.','It proves that song lyrics are experimental evidence about city life.'],2,
 '明确自己优先维度，怎样引导行动？',['保证某城提供所有可能经历。','此后无需任何规划。','帮助选择安排与目标一致的经历。','证明歌词是城市生活实验证据。'],
 ['A 歌词意象不能作城市能力的字面保证。','B structuring/curating正涉及主动安排。','C know maximize→start structuring/curating→align goals构成主张。','D according to歌曲明确艺术引述，非实验。快乐、意义、丰富是可选择侧重，不强制人人优先同一维。'],
 ['When you know what you want to maximize (happiness, meaning, or richness), you can start structuring your life and curating experiences that align your goals.'],
 'curating','精心挑选并组织','像策展一样主动选择经历，不是网站在运行时自动生成内容','She began curating experiences that matched her interests.',['curate experiences','align with goals'],
 '例如，按Jay-Z与Alicia Keys在《Empire State of Mind》中所唱，纽约是“没有什么你做不到……街道让你焕然一新，灯光给予灵感”的地方。当你知道想优先增加快乐、意义还是丰富，就能开始安排生活，精心挑选与目标相合的经历。')

add(21,'主旨','Which claim does the author explicitly make?',
 ['A rich life is always better than every happy or meaningful life.','Prioritizing psychological richness is one way to lead a good life.','Happiness and meaning have been disproved as paths to a good life.','Every person must choose the richest possible life.'],1,
 '作者明确主张哪一项？',['丰富人生总胜过一切快乐或意义人生。','优先心理丰富是好人生的一种途径。','快乐意义已被证伪。','每人必须追求最高丰富。'],
 ['A I am not arguing...always better明确否认。','B Rather后直接给one way，保留多元性。','C 否定丰富必最好，不是否定另外两路。','D one way非人人must的唯一规定。此声明是理解全书立场的限定，不可因题名强调丰富就删掉。'],
 ['I am not arguing that a psychologically rich life is the best life','prioritizing psychological richness is one way to lead a good life.'],
 'prioritizing','优先考虑；赋予较高优先级','在多种价值间侧重丰富，并不宣布其他价值无效','She was prioritizing exploration at that stage of her life.',['prioritize psychological richness','one way to lead a good life'],
 '本书展示了一条新的好人生道路：心理丰富。要说清楚，我并不是主张心理丰富的人生最好，或总优于快乐、有意义的人生。我主张的是：优先心理丰富，是过好人生的一种方式。')

add(22,'作者意图','Why is Oliver Sacks used as an example here?',
 ['To show that people can benefit from more than one form of a good life.','To prove happiness prevents meaning and interesting experiences.','To treat Goldmund as a participant in a clinical trial.','To claim that all patients and caretakers had identical lives.'],0,
 '为什么这里以Oliver Sacks为例？',['说明人可同时受益于不止一种好人生。','证明快乐阻止意义与有趣经历。','把Goldmund当临床试验受试者。','声称所有患者照护者人生相同。'],
 ['A possible...more than one后举seemed happy/meaningful/many stories，说明多维可共存。','B 同时列这些价值，非互相排斥。','C Goldmund是小说人物，不能升格成实验样本。','D touched lives说明影响，不是说受影响的人经历全相同。seemed保留作者对Sacks晚年快乐的判断语气。'],
 ['it is possible to benefit from more than one type of good life.','His life was also meaningful, since he touched and changed many patients’ and caretakers’ lives'],
 'perspective-changing','改变看法的；带来新视角的','形容可使人重新看事物的经历，非保证每次都快乐','The conversation was a perspective-changing experience.',['perspective-changing experiences','benefit from more than one type'],
 '像《Narcissus and Goldmund》的Goldmund，即使不快乐，也不觉得有意义，只要人生充满多样、有趣、改变视角的经历，仍能是好人生。我们也见过，人可以同时受益于多种好人生。例如，Oliver Sacks晚年似乎很快乐；他也有意义，因为触动并改变许多患者与照护者的人生，而且当然有许多故事可讲。')

add(23,'推断','What does Linda’s example add to the discussion?',
 ['It proves that retirement erases every earlier experience.','It shows that meaning and unusual experiences must exclude enjoyment.','It suggests that enjoyment, contribution, and unusual experiences can coexist in one life.','It establishes that all taxi drivers share the same life pattern.'],2,
 'Linda的例子补充什么？',['证明退休抹掉所有旧经历。','说明意义、特殊经历必排斥享受。','提示享受、贡献与特殊经历可同在一个人生。','确立所有出租车司机人生相同。'],
 ['A over span life filled...仍联系过去，非抹去。','B enjoying retirement与made difference/many unusual并存。','C all three及三个描述支持多维共存的个案，seems保留判断限度。','D 一个司机例子不能扩为职业全体模式。Sacks也有三维是前文总结，不把Linda误写成Sacks照护者。'],
 ['Linda, the taxi driver we met in Chapter 4, seems to have had it all, too.','She is enjoying her retirement, having made a difference in the world over the span of a life filled with many unusual experiences.'],
 'made a difference','产生积极影响；有所贡献','指她人生对世界的影响，区别于单纯经历很不同','Her work made a difference in the community.',['make a difference in the world','enjoy retirement'],
 'Sacks毕竟拥有三种好人生。第4章认识的出租车司机Linda，似乎也都拥有。她享受退休；在充满不寻常经历的一生里，她也给世界带来过改变。',support='limited-inference')

add(24,'细节','What sequence of research developments does the author describe?',
 ['Three dimensions were fixed permanently before the 1980s.','Empirical research began in ancient Greece and immediately found four dimensions.','Psychological richness appeared before any discussion of happiness or meaning.','Research intensified in the 1980s, first yielded happiness and meaning, and later added richness.'],3,
 '作者描述研究发展怎样的顺序？',['1980年代前永久定好三维。','古希腊开始实证研究，立刻发现四维。','丰富先于任何快乐意义讨论。','1980年代实证投入加深，先有快乐意义，后来增丰富。'],
 ['A 文字说1980年代才in earnest、后来第三维，不是此前永久定论。','B 此处经验研究史不同于人类早期哲学思考，没写立即四维。','C first thirty years two，Now third方向明确。','D 保留作者对该领域发展线索的概述，不把started in earnest改成人类此前从未想过好人生。'],
 ['empirical research into the question of a good life started in earnest only in the 1980s.','The first thirty years of the endeavor produced two viable dimensions of a good life: happiness and meaning.'],
 'in earnest','认真投入地；正式而深入地','强调研究开展程度，不是否认此前所有相关思想存在','The investigation began in earnest after the initial discussion.',['start in earnest','empirical research'],
 '因此，问“还有其他好人生道路吗”很合理。记得，对好人生问题的实证研究，到1980年代才真正大力展开。最初30年产生两种可行维度：快乐和意义。如今，我们又发现第三维：心理丰富。')

add(25,'逻辑关系','What stance toward future models does the closing passage take?',
 ['Openness to further paths and cultural variation, guided by personal values.','Certainty that a fourth path has already been established.','A rule that every culture must pursue the same single ideal.','The claim that existing dimensions are now useless.'],0,
 '结尾对未来模型持什么态度？',['对更多路径与文化差异开放，并以个人价值引导。','确信第四路已确立。','规定所有文化追同一个理想。','声称现有维度已无用。'],
 ['A might/likely/diverse与knowing who/value共同给出开放性和价值导向。','B might soon reveal是未来可能，非已经发现。','C cultural differences否定单一统一规则。','D 有更多可能不等于否认已有路径价值。right one指适合自身追求，不是文本给出的全人类唯一排名。'],
 ['There might be other paths to a good life','Future research is likely to find cultural differences','Knowing who you are and what you value will guide you in pursuing the right one.'],
 'pursuing','追求；努力走向','按自我理解与价值选择人生道路，而非被模型强制统一','She was pursuing a path that reflected her values.',['pursue the right path','what you value'],
 '好人生也许还有其他路径，新研究可能很快揭示第四种甚至更多。未来研究很可能发现通向好人生的文化差异。归根结底，这是多种好人生道路的故事。知道自己是谁、重视什么，会引导你追求适合的一条。')

assert len(out)==25 and [q['id'] for q in out]==[t['questionId'] for t in targets]

def persist():
 path=ROOT/'source/short-questions/additional.json';existing=load('source/short-questions/additional.json');byid={q['id']:q for q in existing}
 for q in out:
  if q['id'] in byid:assert byid[q['id']]==q,('Refuse to overwrite changed authoring',q['id'])
  else:existing.append(q)
 path.write_text(json.dumps(existing,ensure_ascii=False,indent=2)+'\n',encoding='utf8',newline='\n')
 review=dict(batchId='batch-041',date='2026-10-24',pdfSha256=b['pdfSha256'],checkedPdfPages=list(range(163,167)),questionIds=[q['id'] for q in out],paragraphs=[dict(id=pid,textSha256=hashlib.sha256(pp[pid]['text'].encode()).hexdigest()) for pid in dict.fromkeys(q['paragraphId'] for q in out)],note='完整PDF163–166原页视觉核对。游轮/背包为比喻非旅游产品推荐；九国受访中many Americans非全体，一名UVA学生非九国统一答案。700机票/250三十日通票为作者昔日回忆非当前报价；1988市中心描述不扩为今日城市安全结论。末程三天约70小时、20美元被骗等于日预算非全程旅费。男子承诺与实际消失分段区分，骑警经历个人叙述不推广群体。Chicago聚会后才知Wisconsin，不补路线/绑架；饮酒和接受邀请为回忆非给读者行动要求。Foer同名主人公为小说例证，heritage/coherence/significance关联意义不强制人生路径。志愿项目只作书中例子非质量认证；朋友/地点示例非互斥类型。歌曲为艺术引述非实证城市承诺。作者明确not best/not always better/one way，三维可共存，Sacks seemed与Linda seems保留；1980年代in earnest不否认古代哲思；未来第四维might/文化差异likely非已发现。既有候选池与两段额外开章正文/辅助材料审计仍区分，不宣称全书完成。')
 (ROOT/'source/short-questions/review-chapter14-travel-paths25.json').write_text(json.dumps(review,ensure_ascii=False,indent=2)+'\n',encoding='utf8',newline='\n')
 print('Saved',len(out),'of 25 individually authored exercises')

if __name__=='__main__':persist()
