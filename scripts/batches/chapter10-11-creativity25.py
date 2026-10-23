"""25 individually authored exercises for frozen targets, PDF pages 118-122.
Preserve printed English, source positions and all previously published questions.
"""
from pathlib import Path
import json,hashlib
ROOT=Path(__file__).resolve().parents[2]
load=lambda p:json.loads((ROOT/p).read_text(encoding='utf8'))
b=load('public/data/book.json');plan=load('public/data/reading-plan.json');targets=load('source/short-questions/batch030-targets.json')['targets']
ss={s['id']:s for s in b['sentences']};pp={p['id']:p for p in b['paragraphs']};out=[]
def add(i,kind,prompt,options,answer,prompt_zh,options_zh,analyses,quotes,word,meaning,context,example,collocations,translation,support='explicit'):
 t=targets[i-1];u=next(u for u in plan['units'] if u['id']==t['readingUnitId']);group=[ss[sid] for sid in u['sentenceIds']];p=pp[u['paragraphId']];text=p['text'][group[0]['start']:group[-1]['end']]
 assert hashlib.sha256(text.encode()).hexdigest()==t['passageSha256'];evidence=[]
 for quote in quotes:
  offset=text.find(quote);assert offset>=0,(i,quote);start=group[0]['start']+offset;end=start+len(quote);touching=[s for s in group if s['start']<end and s['end']>start]
  evidence.append(dict(quote=quote,sentenceIds=[s['id'] for s in touching],sources=list({(r['pdfPage'],r['block']):r for s in touching for r in s['sources']}.values())))
 assert word.lower() in text.lower(),(i,word)
 out.append(dict(id=t['questionId'],version=1,readingUnitId=u['id'],chapterId=u['chapterId'],sectionId=u['sectionId'],paragraphId=u['paragraphId'],sentenceIds=u['sentenceIds'],passage=text,prompt=prompt,options=options,answer=answer,type=kind,promptZh=prompt_zh,optionsZh=options_zh,analyses=analyses,evidence=evidence,vocabulary=[dict(word=word,meaning=meaning,context=context,example=example,collocations=collocations)],translation=translation,support=support,editorialStatus='完整PDF118–122原页视觉核对和跨页拼接。列车118接触/97回收/另105想象者分开，随机分组结果是自报愉快不作长期普适保证。Jobs自我归因与作者传记叙述非实验；海外生活MBA比较不擅加随机性；多文化机制保留speculate/seem、综述不冒充全部因果。DIY及微笑为作者个人文化经验，不推广为全体日本人规范；道德相对主义和作弊保留correlated，不诊断个体。Jobs艺术引语不当实证，奖励保留might。第11章逆境先设问，Nietzsche地震是哲学隐喻并承认破坏，非受害者必然成长或医学处方。不宣称逐句直接证据全覆盖。'))







add(1,'作者意图','What possibility introduces the “interesting twist”?',
 ['We may misjudge what we will enjoy.','Familiarity has no empirical support.','Every stranger is unpleasant.','Psychological richness has already disappeared.'],0,
 '什么可能性引出有趣的转折？',['可能误判自己会享受什么。','熟悉效应无实证支持。','每个陌生人都令人不快。','心理丰富已消失。'],
 ['A We may not know what we want 转向偏好预测可能有误。','B 首句明确 evidence 很多。','C think...won’t be fun 是预期，不是对所有陌生人的事实判决。','D seems to spell doom 表面担忧，后有转折，非已消失结论。'],
 ['We may not know what we want.'],
 'twist','转折；出人意料的发展','从熟悉压制探索转向预测可能失准','The result added an unexpected twist to the argument.',['an interesting twist','a surprising twist'],
 '单纯曝光效应及熟悉、确定性的力量有无数实证和现实证据，似乎让心理丰富前景黯淡。同时，这里有个有趣转折：我们可能不知道自己想要什么。我们倾向认为与陌生人交谈不好玩。')

add(2,'主旨','What mismatch motivates the commuter experiment?',
 ['Commuters always predict exactly what they experience.','People expect greater enjoyment than any stranger can provide.','People may enjoy unfamiliar interaction more than they anticipate.','All travellers dislike the same stations.'],2,
 '什么不一致促成通勤实验？',['预测总与体验精确相同。','总高估陌生人能提供的快乐。','可能比预期更享受陌生互动。','所有旅客都讨厌相同车站。'],
 ['A underestimate 明说预测有偏差。','B 方向反转，原文是低估。','C actual...far more than we think 概括主题。','D 地点是实验招募背景，非车站喜好比较。118 是接触的通勤者数，不是后续回收数。'],
 ['we tend to underestimate how enjoyable doing something unfamiliar, like talking to a stranger, is.'],
 'underestimate','低估','对陌生互动愉悦程度的预测偏低','We sometimes underestimate how enjoyable a new conversation will be.',['underestimate enjoyment','underestimate how enjoyable'],
 '但实际与陌生人互动时，我们往往比想象中享受得多。也就是说，我们倾向低估做陌生事情的乐趣，例如与陌生人聊天。社会心理学家 Nick Epley 和 Juliana Schroeder 在通勤列车做实地实验，检验这种乐趣。研究助理在 Homewood Metra 站接触 118 名通勤者；该站是通向 Chicago 市中心 Millennium 站快线前几站之一。')

add(3,'细节','What instruction did the control group receive?',
 ['Talk to as many strangers as possible.','Avoid every normal commuting habit.','Remain silent regardless of their usual routine.','Make no changes to their normal commute.'],3,
 '控制组收到什么指示？',['尽量与多人聊天。','避开所有正常通勤习惯。','无论平时如何都保持沉默。','不改变正常通勤方式。'],
 ['A 主动聊天是第一组，且非越多人越好。','B 明确是不作改变。','C 不干涉惯常行为不等于强制沉默；独处另有一组。','D last third...not...any changes 准确。三分之一为分组描述，不据118强编每组整数人数。'],
 ['The last third were told not to make “any changes to your normal commute.”'],
 'solitude','独处','单独享受车程的条件，与不改常规控制条件不同','Some commuters enjoy solitude during a train ride.',['enjoy solitude','the solitude condition'],
 '三分之一被要求今天在火车上与新认识的人交谈，尝试建立联系，了解对方有趣之处。三分之一被要求独自待着，享受今日车程的独处。最后三分之一被要求不改变正常通勤方式。')

add(4,'细节','Which result was reported for the randomly assigned conversation group?',
 ['All 118 returned happier reports.','They reported happier, more pleasant commutes than the solitude and control groups.','They mailed their surveys before riding.','They reported less pleasure than every other group.'],1,
 '随机分到聊天条件者报告什么结果？',['118 人全回报更快乐。','车程比独处及控制组更快乐愉快。','乘车前就寄出问卷。','比其他每组更不愉快。'],
 ['A 97 人回收，不是118人全回；也未说人人个体改善。','B happier and more pleasant 是受试者自报组间结果。','C 车程结束填写并邮寄。','D 比较方向相反。随机分配与自报结果均保留，不能扩大成所有通勤者长期健康保证。'],
 ['The commuters randomly assigned to talk to a stranger reported that their commutes were significantly happier and more pleasant'],
 'randomly assigned','随机分配','研究设计分组方式，不是受试者按喜好自选','Participants were randomly assigned to one of three conditions.',['randomly assigned to','random assignment'],
 '每个人都拿到装问卷的信封，被要求车程结束填写，并用有邮票的回邮信封寄回。118 人中，97 人回寄。随机分到与陌生人聊天组的人报告，车程比独处组或控制组显著更快乐、更愉快。')

add(5,'逻辑关系','How did the second group’s predictions differ from the actual participants’ experiences?',
 ['They predicted conversation would be less pleasant, contrary to the actual experience pattern.','They rode the same train again and obtained identical outcomes.','They predicted no difference across conditions.','They predicted conversation would be the happiest condition.'],0,
 '第二批预测与实际参与者体验怎样不同？',['预期聊天较不愉快，与真实体验模式相反。','再乘同列车得到相同结果。','预期各条件无差异。','预期聊天最快乐。'],
 ['A Contrary...less happy and less pleasant 明示反向预期。','B another 105 且 simply imagine，不是重复乘车组。','C significantly less 不等于无差异。','D 方向相反。105 是另一批想象者，不能合并为原实验回收人数。'],
 ['those in the imagined experiment predicted that they would report feeling significantly less happy and less pleasant when talking to a stranger'],
 'Contrary to','与……相反','连接预测与实际体验的差异','Contrary to expectations, the conversation was enjoyable.',['contrary to expectations','contrary to the actual experience'],
 '有趣的是，两研究者又在 Homewood Metra 招募 105 名通勤者，仅请他们想象，处于聊天、独处、控制条件时会感觉怎样。与实际参与者相反，想象实验者预测，聊天条件比另两条件显著更不快乐、更不愉快。')

add(6,'作者意图','What action does the author advocate after discussing the commute findings?',
 ['Always choose the first candidate without exploration.','Keep every social routine unchanged.','Overcome familiarity bias to explore unfamiliar possibilities.','Treat every commute as a guaranteed benefit.'],2,
 '讨论通勤结果后，作者提倡什么？',['总不探索就选首位候选。','保持每个社交常规不变。','克服熟悉偏误，探索陌生可能。','把每次通勤当保证获益。'],
 ['A before exploring enough 是被批评的倾向。','B 当前鼓励新联系。','C 最后一句直接表明主张。','D 没有每次保证，作者把结果延伸至候选与择偶，是应用论证而非这些领域新实验。'],
 ['We need to overcome this familiarity bias in order to explore the new and unknown.'],
 'overcome','克服','指减少偏误对探索的限制','She tried to overcome her preference for familiar options.',['overcome a bias','overcome familiarity bias'],
 '认为不改变通勤、独自待着比与同路人聊天好，显然会有误判。我们觉得惯常车程优于新社交联系，这是明显的熟悉偏误。我们探索不足就选工作候选或潜在伴侣。为探索新的未知，我们需要克服这种偏误。')

add(7,'细节','What benefit did Jobs later attribute to his Indian experiences?',
 ['Immunity to illness for the rest of his life.','Confidence to trust his intuition.','A decision style based on rationality alone.','An absence of any questionable decisions.'],1,
 'Jobs 后来把什么益处归于印度经历？',['终身免疫疾病。','更有信心信任直觉。','只靠理性的决策风格。','从未作可疑决定。'],
 ['A 旅行中反而生病且消瘦。','B he credits 是 Jobs 的归因，不是实验确立印度之旅因果。','C balanced rationality and intuition 同时包含两者。','D some questionable ones 明说也有可疑选择。'],
 ['he credits his experiences in India for giving him confidence to trust his intuition.'],
 'intuition','直觉','与理性平衡的决策因素，而非保证正确的能力','He balanced analysis with intuition.',['trust one’s intuition','rationality and intuition'],
 'Steve Jobs 没有受熟悉偏误束缚，十九岁就渴望探索未知的印度。不幸的是，他生病、瘦了很多。但多年后，他把信任直觉的信心归功于印度经历。他独特、平衡理性与直觉的风格，带来许多出色选择，也有一些可疑选择。')

add(8,'作者意图','Why ask whether anything from Jobs’s experience is generalizable?',
 ['To prove a single biography represents everyone.','To reject all research on creativity.','To claim India was the only multicultural setting studied.','To move from an unusual individual toward broader evidence.'],3,
 '为何追问 Jobs 经历能否推广？',['证明一人生平代表所有人。','拒绝全部创造力研究。','称印度是唯一所研究多文化场景。','从独特个人转向更广泛证据。'],
 ['A idiosyncratic/one and only 正提出推广疑问。','B 后面引入研究证据。','C 没限定唯一国家。','D 从 specific only to him 到 amassed evidence 构成论述桥梁；seem 需保留，不能单一传记直接推广。'],
 ['Is there anything generalizable from his experience in India?','multicultural experiences seem to increase creativity.'],
 'generalizable','可推广的','能否超出一个独特人物，适用于更广范围','A single case may not be generalizable.',['generalizable findings','generalizable from an experience'],
 'Steve Jobs 独特，真正独一无二。他印度经历有什么可推广之处吗？还是只适用于他？社会心理学家 Angela Ka-yee Leung、William Maddux、Adam Galinsky、Chi-yue Chiu 已积累证据，显示多文化经历似乎增加创造力。')

add(9,'细节','What must a solution to the candle task achieve?',
 ['Fix the candle to a wall so it burns properly without dripping wax on the table or floor.','Extinguish the candle before any wax melts.','Use a candle without matches or tacks.','Place the candle directly on the floor.'],0,
 '蜡烛任务的解法须达到什么目标？',['固定墙上正常燃烧且不滴蜡到桌地。','融蜡前熄灭。','不使用火柴图钉。','直接放地上。'],
 ['A 两个条件 burn properly 与 won’t drip 都保留。','B 要能正常烧，不是立即熄灭。','C 材料包含火柴和盒装图钉，未禁止使用。','D 位置须墙上。当前只述问题，答案指向尾注；不编入未核对尾注解法。'],
 ['attach a candle to a wall so that the candle will burn properly and won’t drip wax on the table or floor?'],
 'tacks','图钉','任务提供的盒装材料之一','The box contained a handful of tacks.',['a box of tacks','a pack of matches'],
 '例如，参与者被要求解 Duncker 蜡烛问题：你有一支蜡烛、一包火柴和一盒图钉。能把蜡烛固定墙上，让它正常燃烧又不把蜡滴到桌子或地板吗？答案见尾注。')

add(10,'推断','Which conclusion is supported by the MBA comparison?',
 ['Every student who lived abroad solved the task.','Foreign experience was randomly assigned in this comparison.','More experience living abroad was associated with a higher likelihood of solving the task.','The finding applied only to a single creativity task.'],2,
 'MBA 比较支持什么结论？',['所有海外生活者都解出。','比较中随机分配海外经验。','海外生活更多与解出概率较高相关。','发现只限一个创造力任务。'],
 ['A more likely 是概率比较，不是全部成功。','B 没说随机安排出国。','C more...more likely 忠实保留比较；单凭这里不能定因果。','D different types...replicated 明说其他任务也重现。'],
 ['those with more experience living abroad were more likely to solve the Duncker candle problem than those with less foreign experience.'],
 'replicated','复现；重复验证','用不同创造力任务得到相似模式','The result was replicated using another task.',['replicate findings','different types of tasks'],
 '这是广泛用于测试创造力的任务。MBA 学生中，海外生活经验更多者，比海外经验较少者更可能解出 Duncker 蜡烛问题。用不同创造力任务也复现了这些发现。')

add(11,'逻辑关系','What mechanism do Leung and colleagues speculate about here?',
 ['Exposure prevents people from learning any new concepts.','Multicultural experience introduces novel ideas and concepts.','Every American builds a house personally.','All creativity arises from house renovation alone.'],1,
 'Leung 及同事在此推测什么机制？',['接触阻止学习新概念。','多文化经历带来新想法和概念。','每个美国人亲手造房。','所有创造力只来自装修。'],
 ['A acquire novel 与阻止相反。','B speculate 明确机制推测；建房是作者个人例子。','C ordinary idea 不等于人人实际亲自做。','D 一个例子不能限缩为唯一来源。'],
 ['people acquire novel ideas and concepts from multicultural experiences.'],
 'speculate','推测；提出可能解释','机制尚以推测表达，不改成该段独立实验证明','The researchers speculate that new concepts support flexibility.',['speculate that','speculate about a mechanism'],
 '为何多文化经历应与创造力关联？Leung 及同事推测，人从中获得新想法和概念。我到美国后新学的概念之一，是自己建造或翻新房子的可能性。对美国读者，这是普通想法。')

add(12,'细节','What was new to the author about DIY?',
 ['DIY was entirely absent from Japan.','Japanese DIY always involved constructing whole houses.','Only licensed professionals could ever make shelves.','Nonprofessionals might renovate or build an entire house themselves.'],3,
 'DIY 的什么对作者新鲜？',['日本完全无 DIY。','日本 DIY 总是整屋建造。','只有持证专业者能做架子。','非专业人士也可能自己翻新或建整屋。'],
 ['A 明确 DIY does exist。','B typically small projects，而非总整屋。','C 没有资格限制陈述。','D had never imagined...whole house 对应新观念，非全日本人的统一经历。'],
 ['I had never imagined that nonprofessionals would try to renovate or build a whole house by themselves.'],
 'nonprofessionals','非专业人士','不以此为专业的普通人尝试整屋工程','The workshop introduced simple repairs to nonprofessionals.',['nonprofessionals would try','build a whole house'],
 '对我却是激进想法。说清楚，日本确实有 DIY，但通常是架子、书柜等小工程。我从没想过，非专业人士会试着亲自翻新或造整所房。那种志向、开拓精神，对我都是新的。')

add(13,'推断','What change in the author’s outlook is described?',
 ['Previously unconventional concepts now seem normal to him.','His friends had already helped him build a house.','He had proved that every Tokyo friend opposed DIY.','Balloon framing made construction more difficult.'],0,
 '作者描述什么观念变化？',['原先跳出常规的概念如今显得正常。','朋友已帮他造房。','已证明每位东京朋友都反对 DIY。','轻木框架令建造更难。'],
 ['A totally out-of-box...but now...normal 明确前后变化。','B if I decided 是假设，不是已建成。','C I bet 是猜想朋友反应，非调查全部友人。','D makes...easier 明说更容易。'],
 ['These concepts were totally out-of-box thinking to me, but now seem quite normal.'],
 'out-of-box','跳出框架的；不循常规的','相对于作者原有经验的新颖思路','The approach encouraged out-of-box thinking.',['out-of-box thinking','seem quite normal'],
 '美国的 balloon framing 轻木框架是一项巧妙发明，让造房更容易。这些概念对我曾完全跳出框架，如今却很正常。我打赌，若决定自己造房，Tokyo 的大学朋友会觉得我疯了。')

add(14,'主旨','What does the smile example illustrate?',
 ['Smiling has exactly the same meaning everywhere.','Multicultural experience erases all cultural interpretation.','The same behavior can carry different meanings in different settings.','The author was never told to change his behavior.'],2,
 '微笑例子说明什么？',['到处含义完全相同。','多文化经历消除全部文化解释。','同一行为在不同环境可有不同含义。','作者从未被要求改行为。'],
 ['A same behavior...different meanings 正相反。','B 是认识多种意义，非消除解释。','C 作者成长中与到美国后的礼貌反馈对照。','D 被告知 smile more。这是个人文化经历与研究者推测，不把日本所有情境都简化成禁止微笑。'],
 ['the same behavior can have different meanings.'],
 'come across as','给人……印象','微笑在作者成长规范下可能被认为不礼貌','A brief reply can come across as impolite.',['come across as impolite','come across as friendly'],
 'Leung 及同事还推测，多文化经历教我们认识，同一行为会有不同意义。微笑是好例子。我从小受教在人前别微笑，因为可能显得不礼貌。但到美国，人人叫我多笑，说这样更礼貌！')

add(15,'细节','What did the author notice in the Ginza elevator?',
 ['The other passengers invited him to speak.','Their faces froze and he perceived them as scared.','Everyone left before he entered.','He had consciously avoided looking at them.'],1,
 'Ginza 电梯里作者注意到什么？',['乘客请他讲话。','他看到别人表情僵住，觉得他们害怕。','他进入前所有人已走。','他刻意避免看别人。'],
 ['A 没有人邀请交谈。','B noticed...faces froze 与 they were scared 是作者叙述及解读，不是测量恐惧。','C 已在电梯里的人仍在。','D looked at the others 明说看过去。'],
 ['I noticed that their faces froze; they were scared of me.'],
 'consciously','有意识地；刻意地','回日本时需刻意调整笑容，而非全自动行为','He consciously adjusted his greeting to the setting.',['consciously try','consciously adjust'],
 '如今回日本，我得刻意试着别微笑。例如有次去 Tokyo 的 Ginza 一家高档百货。我进电梯，看着里面的人，发现他们表情僵住；他们在怕我。')

add(16,'逻辑关系','What realization follows the author’s initial surprise?',
 ['He had entered the wrong country.','Everyone knew him personally.','His friendliness was objectively universal.','His eye contact and smile might violate the local expectations he describes.'],3,
 '最初惊讶后，作者意识到什么？',['进错国家。','人人私下认识他。','友善的含义客观普世。','目光接触与微笑可能违背其所述当地期待。'],
 ['A 没有地点弄错。','B 没人被说成认识他。','C 前后转折恰说明自己的友好理解不总适用。','D suddenly hit me 后认出自己的目光和微笑，how rude 是自嘲；不把轶事改为全体居民心理定律。'],
 ['it suddenly hit me that I was making eye contact and smiling at them—how rude!'],
 'hit me','我突然意识到','习语表示领悟而非受到实体击打','It suddenly hit me that I had misread the greeting.',['it suddenly hit me that','a realization hit me'],
 '他们为什么怕我？我是个友好的日本人呀！但一瞬后，我忽然意识到自己正在与他们目光接触、对他们微笑——多没礼貌！在日本按这里描述，你该这样做：进入电梯。')

add(17,'逻辑关系','How do Leung and colleagues connect cultural interpretation with creativity?',
 ['Recognizing multiple meanings may help generate multiple uses for a tool or idea.','Avoiding eye contact directly guarantees every invention.','Every behavior has only one correct meaning.','Cultural interpretation prevents alternative uses of tools.'],0,
 '研究者怎样联系文化解释与创造力？',['认识多种意义可能帮助想到工具或想法的多种用途。','不目光接触直接保证发明。','每种行为只有唯一含义。','文化解释阻止想到替代用途。'],
 ['A multiple meanings...in turn...multiple uses 是所提出机制。','B 把电梯例直接当发明保证，跳过论证。','C 与 multiple 相反。','D 方向反转。这是 argue 的机制解释，当前未给新实验步骤。'],
 ['understand multiple meanings of the same form of behavior, which in turn helps us think of multiple uses for one tool or idea.'],
 'in turn','进而；继而','连接理解多义到发散用途的论证链','New perspectives can in turn suggest new uses.',['which in turn helps','in turn leads to'],
 '不要直视别人。不要目光接触。低头，不打扰人。Leung 及同事认为，这类经历帮助理解同一种行为的多重意义，进而帮助想到同一工具或想法的多种用途。')

add(18,'主旨','Which benefit beyond creativity is summarized in the review?',
 ['A guarantee of perfect self-knowledge for every traveller.','Complete elimination of all intergroup prejudice.','Greater self-clarity and more positive relations with others.','Less ability to understand people from other groups.'],2,
 '综述概括创造力之外哪些益处？',['保证每位旅客完美自知。','完全消除一切群际偏见。','更清楚自我，与他人关系更积极。','更不能理解其他群体。'],
 ['A clearer 是相对更清楚，非完美保证。','B fewer/less 是较少，不是零。','C 自我、信任、理解和较少偏见歧视都支持。','D better able 方向相反。这里是综述概述，不能凭该段断言所有底层研究皆随机因果。'],
 ['gain a clearer sense of who they are and the lives they want to pursue.','trust others more and are better able to understand and relate to others.'],
 'outgroup','外群体的','不属于自身群体的成员，描述群际态度','The survey examined attitudes toward outgroup members.',['outgroup members','discriminate against outgroup members'],
 '近期研究综述还显示，多文化经历益处超出创造力。例如，海外生活时间也帮助个人更清楚自己是谁、想过什么生活。海外经历更多者更信任他人，更能理解和与他人建立联系。探索过世界者倾向有较少负面刻板印象与偏见，对外群体成员的歧视也比未探索者少。')

add(19,'细节','How is moral relativism defined here?',
 ['Morality is absolute and identical in all contexts.','What is good or bad is relative rather than absolute.','Every cross-cultural traveller cheats on every task.','Creativity itself is morally wrong.'],1,
 '此处怎样定义道德相对主义？',['道德绝对且各情境一致。','善恶相对而非绝对。','每个跨文化旅客每次都作弊。','创造力本身不道德。'],
 ['A 正好反义。','B the idea that...not absolute, but relative 直接定义。','C more likely/cheated more 不是每个人每次，且开头 correlated 限定证据。','D 当前报告可能不良关联，不评创造力本身错误。不能把相关改为出国必致作弊。'],
 ['morality, or what is good or bad, is not absolute, but relative.'],
 'correlated','相关的','不良结果与多文化经历相伴，不独自证明因果','The variables were correlated in the sample.',['correlated with','undesirable outcomes correlated with'],
 '应注意，多文化经历也与某些不理想结果相关。例如，经历更多者更可能相信道德相对主义，即道德或善恶不是绝对而是相对的。此外，绩效任务有作弊机会时，跨文化经历多者比少者作弊更多。')

add(20,'作者意图','What contrast does the author draw about Jobs?',
 ['Creative achievements prove all his conduct was moral.','His parking habits caused the invention of the iPhone.','He was neither creative nor controversial.','The conduct described as morally questionable coexisted with creativity.'],3,
 '作者对 Jobs 作什么对照？',['创意成就证明一切行为有德。','停车习惯导致发明 iPhone。','既无创造力也无争议。','被描写为道德可疑的行为与创造力并存。'],
 ['A But...also creative 没给不当行为开脱。','B 没有停车与发明因果。','C 反而两面都列出。','D 前三句负面叙述与 But 后创造力并置，属于作者对人物的描述，不当新实验样本证据。'],
 ['He showed signs of moral relativism. But Jobs was also creative.'],
 'launches','发布会；推出活动','product launches 指介绍设备的活动，不是火箭发射','The company demonstrated its device at product launches.',['product launches','particular device functions'],
 '毕竟，按作者叙述，Steve Jobs 曾在几场产品发布会上对特定设备功能向观众说谎，也经常在 Whole Foods 的残障专用区停车。他显出道德相对主义迹象。但 Jobs 也有创造力。')

add(21,'主旨','What principle does Jobs express through the musicians’ example?',
 ['Continue evolving and refining one’s work.','Copy every musical style without change.','Stop developing after one successful product.','Treat artistic change as proof of experimental causation.'],0,
 'Jobs 借音乐人表达什么原则？',['持续发展并打磨作品。','不变地复制所有音乐风格。','一件产品成功后停止发展。','将艺术变化当实验证据。'],
 ['A evolving/moving/refining 与 keep moving 表明不断发展。','B refining 是变化和打磨，不是不动。','C Otherwise 后警示停滞，方向相反。','D 引述是人物表达和艺术比喻，不是实验结论。帮助设计产品也不等于一人独力完成。'],
 ['They kept evolving, moving, refining their art.'],
 'refining','改进；打磨','持续精进艺术表达，不是物理炼制','The team kept refining the design.',['refine one’s art','keep evolving'],
 '他帮助设计 Mac、iPod、iPad、iPhone。谈到喜爱的 Bob Dylan 和 Beatles，Jobs 说，他们持续演变、前进、打磨艺术；他也一直努力前进，否则如 Dylan 所言，不忙着新生，就忙着死去。')

add(22,'推断','How should the possible “prizes” of exploration be understood?',
 ['A guarantee that every explorer finds the best possible partner.','A payment promised by the researchers.','Potential rewards, not assured outcomes for every person.','Evidence that psychological biases have already disappeared.'],2,
 '应怎样理解探索可能获得的奖励？',['保证每人找到唯一最佳伴侣。','研究者承诺付款。','可能收益，不是人人保证结果。','证明心理偏误已消失。'],
 ['A might/top 10 percent 都不支持保证唯一最佳。','B prize 是对潜在收获的比喻，非报酬安排。','C might 保留可能性，创造力、经验智慧、好伴侣是作者鼓励性的总结。','D despite...holding you back 承认阻力仍在。'],
 ['You might earn a prize or two: creativity, experiential wisdom—and a top 10 percent mate.'],
 'despite','尽管；即使有','鼓励在心理偏误阻力下仍探索','She explored the new subject despite her initial hesitation.',['despite psychological biases','despite obstacles'],
 '所以，继续前进。尽管心理偏误阻挡，也继续探索。你也许能赢得一两份奖赏：创造力、经验智慧——以及位居前 10% 的伴侣。')

add(23,'作者意图','What shift does the final question introduce?',
 ['From all experiences being accidental to denying choice.','From chosen rich experiences to experiences people did not choose.','From reading literature to banning films.','From intentional action to proving adversity is always beneficial.'],1,
 '最后问句引入什么转向？',['从一切偶然转向否认选择。','从主动选择的丰富体验转向非自愿体验。','从文学转向禁电影。','从主动行为转向证明逆境总有益。'],
 ['A Most intentional 并非一切偶然。','B choices 连列留学、阅读、电影、DIY 后用 But 转向 unintentional。','C 列举活动，无禁止。','D 问句未得逆境收益结论。Most/usually 不改成全称。'],
 ['But what about unintentional experiences?'],
 'intentional','有意的；主动选择的','与非意愿遭遇对照，不等于每种丰富体验皆自选','The visit was an intentional choice to try something new.',['intentional experiences','make the choice to'],
 '多数心理丰富体验是有意选择的。人通常主动决定留学。选择读 Marcel Proust，选择看 Agnès Varda 电影，选择动手做 DIY。但非自愿的体验呢？')

add(24,'主旨','What question does the passage raise about adverse experiences?',
 ['Which medicine cures every illness immediately?','How can every disaster be intentionally arranged?','Why do all victims benefit equally?','Whether unexpected adversity can add psychological richness.'],3,
 '本段对不利体验提出什么问题？',['何种药立刻治所有病。','如何主动安排所有灾难。','为何所有受害者等量获益。','意外逆境能否增加心理丰富。'],
 ['A 未谈治疗。','B unintentional/unexpected 强调非主动安排。','C typically/new perspectives 不等于每人必然等量获益。','D So...add psychological richness 是中心追问；未在这里证实所有逆境有益。'],
 ['do unintentional, adverse experiences add psychological richness to our lives?'],
 'adverse','不利的；逆境中的','指灾害或疾病等困难遭遇，不淡化损害','The study examined responses to adverse experiences.',['adverse experiences','unexpected and challenging'],
 '地震、飓风或疾病这类自然灾害或患病，是意外且充满挑战的体验。这些经历通常为遭遇者带来新视角。那么，非自愿的不利体验会增加人生的心理丰富吗？')

add(25,'作者意图','What does Nietzsche’s earthquake image emphasize as presented here?',
 ['Crisis can reveal inner powers and a will to live and re-create.','Every earthquake leaves all victims stronger.','The passage reports a controlled disaster experiment.','Earthquakes have no destructive consequences.'],0,
 '按此处呈现，Nietzsche 的地震意象强调什么？',['危机可能显露内在力量及生存重建意志。','每次地震使所有受害者更强。','报告受控灾害实验。','地震无破坏后果。'],
 ['A bring to light...inner powers 与 will to live...re-create 支持哲学阐释。','B often 不能改成人人必然，思想引语也非灾后获益保证。','C 哲学观点与古希腊解读，不是实验。','D bury wells/leave languishing 同时承认破坏与痛苦，不可删去。'],
 ['they also bring to light inner powers and secrets.','the will to live and to re-create.'],
 'catharsis','净化；宣泄','Nietzsche 对危机的哲学理解，而非医学诊疗结论','The critic interpreted the scene as a form of catharsis.',['a sort of catharsis','experience catharsis'],
 '哲学家 Friedrich Nietzsche 把地震视为某种净化，称地震掩埋许多水井、使许多人困苦，却也揭露内在力量和秘密。他精通古典哲学，了解古代世界。在古希腊人身上，他看到危机中最强的人性力量：活下去并重新创造的意志。最糟条件中常会显出人性最好的一面。')

assert len(out)==25 and [q['id'] for q in out]==[t['questionId'] for t in targets]

def persist():
 path=ROOT/'source/short-questions/additional.json';existing=load('source/short-questions/additional.json');byid={q['id']:q for q in existing}
 for q in out:
  if q['id'] in byid:assert byid[q['id']]==q,('Refuse to overwrite changed authoring',q['id'])
  else:existing.append(q)
 path.write_text(json.dumps(existing,ensure_ascii=False,indent=2)+'\n',encoding='utf8',newline='\n')
 review=dict(batchId='batch-030',date='2026-10-23',pdfSha256=b['pdfSha256'],checkedPdfPages=list(range(118,123)),questionIds=[q['id'] for q in out],paragraphs=[dict(id=pid,textSha256=hashlib.sha256(pp[pid]['text'].encode()).hexdigest()) for pid in dict.fromkeys(q['paragraphId'] for q in out)],note='完整PDF118–122原页视觉核对和跨页拼接。列车118接触/97回收/另105想象者分开，随机分组结果是自报愉快不作长期普适保证。Jobs自我归因与作者传记叙述非实验；海外生活MBA比较不擅加随机性；多文化机制保留speculate/seem、综述不冒充全部因果。DIY及微笑为作者个人文化经验，不推广为全体日本人规范；道德相对主义和作弊保留correlated，不诊断个体。Jobs艺术引语不当实证，奖励保留might。第11章逆境先设问，Nietzsche地震是哲学隐喻并承认破坏，非受害者必然成长或医学处方。不宣称逐句直接证据全覆盖。')
 (ROOT/'source/short-questions/review-chapter10-11-creativity25.json').write_text(json.dumps(review,ensure_ascii=False,indent=2)+'\n',encoding='utf8',newline='\n')
 print('Saved',len(out),'of 25 individually authored exercises')

if __name__=='__main__':persist()
