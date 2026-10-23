"""25 individually authored exercises for frozen targets, PDF pages 111-115.
Preserve printed English, source positions and all previously published questions.
"""
from pathlib import Path
import json,hashlib
ROOT=Path(__file__).resolve().parents[2]
load=lambda p:json.loads((ROOT/p).read_text(encoding='utf8'))
b=load('public/data/book.json');plan=load('public/data/reading-plan.json');targets=load('source/short-questions/batch028-targets.json')['targets']
ss={s['id']:s for s in b['sentences']};pp={p['id']:p for p in b['paragraphs']};out=[]
def add(i,kind,prompt,options,answer,prompt_zh,options_zh,analyses,quotes,word,meaning,context,example,collocations,translation,support='explicit'):
 t=targets[i-1];u=next(u for u in plan['units'] if u['id']==t['readingUnitId']);group=[ss[sid] for sid in u['sentenceIds']];p=pp[u['paragraphId']];text=p['text'][group[0]['start']:group[-1]['end']]
 assert hashlib.sha256(text.encode()).hexdigest()==t['passageSha256'];evidence=[]
 for quote in quotes:
  offset=text.find(quote);assert offset>=0,(i,quote);start=group[0]['start']+offset;end=start+len(quote);touching=[s for s in group if s['start']<end and s['end']>start]
  evidence.append(dict(quote=quote,sentenceIds=[s['id'] for s in touching],sources=list({(r['pdfPage'],r['block']):r for s in touching for r in s['sources']}.values())))
 assert word.lower() in text.lower(),(i,word)
 out.append(dict(id=t['questionId'],version=1,readingUnitId=u['id'],chapterId=u['chapterId'],sectionId=u['sectionId'],paragraphId=u['paragraphId'],sentenceIds=u['sentenceIds'],passage=text,prompt=prompt,options=options,answer=answer,type=kind,promptZh=prompt_zh,optionsZh=options_zh,analyses=analyses,evidence=evidence,vocabulary=[dict(word=word,meaning=meaning,context=context,example=example,collocations=collocations)],translation=translation,support=support,editorialStatus='完整PDF111–115原页视觉核对及跨页拼接。词频观察与无意义词、汉字、人像和课堂曝光实验分开；假称Turkish不作真实语言事实；课堂评分量表、出席次数和主观熟悉/明确认识分开，linearly保留作者措辞但不编精确等差。机制实验不把早前观察婚配研究改成随机试验。购物/旅行属个人轶事；普查流动性是代理指标、统计控制非因果保证；成长经历观察与想象工作心态实验分开，every other year译隔年。and almost为既有跨单元句片，保留ID与连续阅读。末段完整审阅含尚未配题结果，不提前倒灌证据，不宣称逐句直接证据全覆盖。'))







add(1,'逻辑关系','Why might “good” be rated more desirable than “better” in the reported task?',
 ['It has a more positive dictionary meaning.','It is encountered more frequently in use.','It was the only word participants knew.','It had fewer printed appearances.'],1,
 '为什么所报任务中 good 可能比 better 更讨喜？',['字典意义更积极。','使用中出现得更频繁。','参与者只认识这一个词。','印刷出现次数更少。'],
 ['A 作者先承认通常意义上 better 更好，结果与这一预期形成反差。','B far more often 提供熟悉程度的解释；报告的是被试评价。','C 没说被试不认识 better。','D 与频率比较方向相反。此片段的频率与喜欢关系不能独自确立因果。'],
 ['the word “good” is used far more often than the word “better.”'],
 'desirability','讨喜程度；吸引力','词给人的正面感受，不等于字典中比较级的逻辑顺序','The survey measured the desirability of each design.',['the desirability of a word','increase desirability'],
 '大家都同意 good 是好的，但不如 better 那么好。不过就词频而言，good 的使用频率远高于 better。因此，如果经常遇见会增加一个词的讨喜程度，good 就应该比 better 更讨喜。果然，心理实验参与者报告，good 比 better 更讨喜！')

add(2,'作者意图','Why did Zajonc move from word-frequency findings to a new experiment?',
 ['Earlier findings proved that frequency had no effect.','The earlier words were all genuinely Turkish.','A correlation alone could not establish a causal effect.','Pronunciation had already explained every rating.'],2,
 'Zajonc 为什么从词频发现转向新实验？',['早期发现证明频率无效。','早期词全部是真土耳其语。','仅有相关不能确立因果效应。','发音已解释全部评分。'],
 ['A 不能推断因果不等于证明无效。','B they weren’t 明确否定所称语言身份。','C still correlational 后明确 cannot infer a causal effect，是新实验动机。','D 未报告发音解释了全部评分。无意义词被称作土耳其语是实验说明，不是真实语言知识。'],
 ['we cannot infer a causal effect between frequency and liking a word.'],
 'correlational','相关性的','两个变量共同变化的发现，不自动证明原因','The correlational evidence prompted a controlled experiment.',['correlational findings','infer a causal effect'],
 '这些词频研究发现很有趣，但仍属相关性结果。也就是说，我们不能据此推断频率与喜欢某词之间的因果效应。因此 Zajonc 设计实验，向参与者呈现 iktitaf、afworbu、saricik 等无意义词。实验者称其为“土耳其语”词（其实不是），并教他们各词的发音。')

add(3,'细节','How was familiarity manipulated in this task?',
 ['By presenting different words different numbers of times.','By teaching participants accurate Turkish translations.','By showing every word exactly twelve times.','By letting participants choose their own exposure frequency.'],0,
 '任务怎样操纵熟悉度？',['使不同词出现不同次数。','教准确土耳其语翻译。','每词恰好呈现十二次。','让参与者自选呈现次数。'],
 ['A once or twice 与 ten or twenty-five 对照，末句直接说明操纵。','B 参与者是猜好坏含义，没有教授准确译义。','C 十二是后续材料数量，当前呈现次数有多档。','D 没说参与者自行安排频率。'],
 ['Some words were presented only once or twice, while others were presented ten or twenty-five times.'],
 'manipulated','操纵；系统改变','实验者改变呈现频率以操作熟悉度，不是贬义欺骗的泛指','The experiment manipulated the number of repetitions.',['manipulate familiarity','manipulate a variable'],
 '随后参与者被要求读出每个词。之后，他们要从好或坏的角度猜测各“土耳其语”词的意思。一些词只呈现一两次，另一些呈现十次或二十五次。Zajonc 就这样操纵熟悉度。')

add(4,'主旨','What pattern was replicated across the materials described?',
 ['Chinese characters were always preferred to photographs.','All photographs received identical ratings.','Only real words benefited from repetition.','More frequent presentation increased positive evaluations of the same stimuli.'],3,
 '不同材料中重复出现什么结果模式？',['汉字总比照片受欢迎。','所有照片评分相同。','只有真实词重复后才受益。','同一刺激呈现更频繁时，正面评价更高。'],
 ['A 没有汉字与照片之间的偏好排名。','B same photos 是相同照片在不同频率条件下比较，不是评分全相等。','C nonsense words 也有结果。','D 十二无意义词、汉字、毕业生照片都重现更频繁呈现与更积极评价的模式；不等于每种现实关系都必定获益。'],
 ['all twelve nonsense words were rated higher on goodness when presented more frequently','those same photos were better liked when presented more frequently'],
 'replicated','重复验证；复现','用不同材料重现原先结果模式','The team replicated the finding with a new set of images.',['replicate a finding','replicate an experiment'],
 '他发现，全部十二个无意义词在呈现较频繁时，好的程度评分都高于呈现较少时。随后他用汉字重复验证这一初步发现。接着，他使用 Michigan State University 应届毕业生的照片，再次发现同样的照片在向参与者呈现更频繁时，比呈现较少时更受喜欢。')

add(5,'细节','Which feature distinguished the four women’s participation in the classroom experiment?',
 ['They attended different subjects at different universities.','They attended the same course with different frequencies.','They were selected to differ greatly in attractiveness.','Each attended all lectures throughout the semester.'],1,
 '四名女性在课堂实验中的参与有什么差别？',['在不同大学上不同科目。','同一课程的出席频率不同。','专门挑选外貌吸引力差很多的人。','每个人整个学期全勤。'],
 ['A 是同一心理学导论课程的实地实验。','B 从零、五、十到十五次，改变课堂曝光频率。','C rated as equally attractive 表示最初评定吸引力相同。','D 有人一次也没来，非全勤。四人是研究助理，不是四组全部被试人数。'],
 ['four female research assistants who were rated as equally attractive','never attended the lecture, the second woman attended five times, the third woman attended ten times, and the fourth one attended fifteen times'],
 'field experiment','实地实验','在真实大学课堂实施，区别于仅在实验室呈现词语','The researchers conducted a field experiment in a classroom.',['run a field experiment','a real college classroom'],
 '单纯曝光效应的故事不止于此。Richard Moreland 和 Bob Zajonc 在真实大学课堂开展实地实验。他们挑选四名被评为吸引力相同的女性研究助理，以不同频率参加心理学导论课。一人从不来，第二人来五次，第三人来十次，第四人在学期中来十五次。')

add(6,'逻辑关系','Why were the assistants instructed to use the same staircases and seating area?',
 ['To ensure that they never became visible.','To test differences in formal clothing.','To make them visible to most students in a similar way.','To require them to talk to every student.'],2,
 '为何要求助理走相同楼梯、坐同一区域？',['确保始终不可见。','测试正装差异。','让大多数学生以相似方式看见她们。','要求与每位学生谈话。'],
 ['A so that most students could see 正相反。','B casually dressed 是便装，未设正装比较。','C so that 直接给安排的目的。','D 当前只规定进入、路线、座位和着装，没有规定与每人交谈。'],
 ['walk the same staircases, and sit in the same area, so that most students could see them.'],
 'casual','随意的；非正式的','指助理统一采用便装风格，而非频率随机的意思','The participants wore casual clothing.',['casual fashion','casual clothing'],
 '她们被要求走进讲堂，走相同楼梯，坐在同一区域，好让大多数学生能看见她们。她们都穿便装。')

add(7,'细节','Which dimension were students asked to rate at the semester’s end?',
 ['How similar each woman seemed to themselves.','The women’s examination results.','How many lectures the students themselves missed.','Each assistant’s actual family background.'],0,
 '学期末要求学生评哪个维度？',['每名女性看起来与自己有多相似。','女性的考试成绩。','学生自己缺课次数。','每位助理的实际家庭背景。'],
 ['A perceived similarities (to the rater) 明确是与评分者的主观相似感。','B 没测考试成绩。','C 这里让学生评四人照片，不是报自己的出勤。','D perceived 不是实际背景调查。另两维度为吸引力和熟悉度。'],
 ['attractiveness, familiarity, and perceived similarities (to the rater).'],
 'perceived','感知到的；认为的','相似感是评分者主观判断，不自动等于客观一致','Perceived similarity may differ from measured similarity.',['perceived similarities','perceived attractiveness'],
 '学期末，班里学生被要求根据四名女性的照片，对吸引力、熟悉度以及感到她们与自己有多相似进行评分。')

add(8,'细节','Which pairing of attendance and attractiveness rating is correct?',
 ['No attendance: 4.38.','Five attendances: 4.25.','Ten attendances: 3.62.','Fifteen attendances: 4.38.'],3,
 '哪组出席次数和吸引力评分对应正确？',['零次：4.38。','五次：4.25。','十次：3.62。','十五次：4.38。'],
 ['A 零次为 3.62。','B 五次为 3.88。','C 十次为 4.25。','D 十五次对应 4.38，量表为 1–7。作者称 linearly increased；这些四舍五入值的相邻差并不完全相等，不据此编造精确等差公式或逐人必然变化。'],
 ['4.38 for the woman who showed up fifteen times.'],
 'scale','量表；评分尺度','1–7 是评分范围，不是出席次数范围','Participants rated the images on a seven-point scale.',['a 1 to 7 point scale','attractiveness ratings'],
 '结果与早期实验室实验十分相似：本实地实验中，吸引力评分（1 至 7 分量表）随着曝光增加而呈线性上升趋势：从未出席者为 3.62，出席五次者为 3.88，十次者为 4.25，十五次者为 4.38。')

add(9,'推断','What distinction does the passage draw about awareness?',
 ['Everyone explicitly recognized all four women.','Positive exposure effects may appear without much explicit recognition.','Nobody had ever seen any of the women.','Students rated objective similarity instead of perceived similarity.'],1,
 '片段对意识作出什么区分？',['所有人明确认出四人。','曝光影响可能在缺乏明确认出的情况下出现。','没有人曾看过任何一人。','学生评客观相似性而非主观感受。'],
 ['A nobody said yes 与此相反。','B seems...without much awareness 与显式询问的结果支持；保留 seems 限定。','C Very few 不是零，看见过与认识也不同。','D perceived similarities 明说主观相似感。不可把没人说认识扩大成没人见过。'],
 ['the mere exposure effect seems to happen without much awareness.','Very few people said they had seen them before.'],
 'awareness','意识；觉察','对是否认识或见过这些人的明确觉察','A preference can develop without full awareness.',['without much awareness','explicit awareness'],
 '同样，曝光更多也与更强的相似感相关。有趣的是，单纯曝光效应似乎不需要多少有意识的觉察。例如，明确问学生是否认识这四名女性时，没有人说认识。极少有人说以前见过她们。')

add(10,'细节','Which women received higher familiarity ratings in this comparison?',
 ['Those who attended five times rather than fifteen.','Only the woman who never attended.','Those who attended ten or fifteen times.','All four received the same ratings.'],2,
 '比较中哪些女性的熟悉度评分更高？',['五次比十五次者高。','只有从没来者高。','出席十次或十五次者。','四人评分相同。'],
 ['A 方向颠倒。','B 未出席者属于较低熟悉度比较组。','C ten and fifteen 与 did not...or...five 对照。','D more familiar 明确有差异。这里是熟悉度评分，不是在说十次与十五次之间谁更高。'],
 ['rated the women who attended the lecture ten and fifteen times more familiar than those who did not attend or attended only five times.'],
 'familiar','熟悉的','熟悉度量表判断，不必等于能明确说出认识对方','The repeated image began to look familiar.',['more familiar than','rate as familiar'],
 '然而，在熟悉度方面，他们给出席十次和十五次者的评分，比未出席或只出席五次者更熟悉。')

add(11,'主旨','How does the author connect the experiments to the earlier geographical studies?',
 ['The experiments offer a causal mechanism involving familiarity, similarity and favorability.','The geographical studies had randomly assigned every marriage.','Repeated exposure reduces all perceived similarity.','The experiments prove that proximity guarantees marriage.'],0,
 '作者怎样将实验与此前地理研究联系起来？',['实验提供涉及熟悉感、相似感和好感的因果机制解释。','地理研究随机分配了每段婚姻。','重复曝光降低所有相似感。','实验证明近距离保证结婚。'],
 ['A 作者从 repeated exposure 到 familiarity/similarity/favorability，再解释先前观察研究。','B 早前婚姻与同居资料并非随机分配。','C amplifies 与降低方向相反。','D 实验支持机制的因果论证，不把整体观察资料变成随机试验，也不保证任何特定婚姻。'],
 ['repeated exposure amplifies not only familiarity, but also perceived similarity (to the rater) and favorability.','providing a compelling causal claim for the Philadelphia marriage study and the Dutch cohabitation study.'],
 'amplifies','增强；放大','描述重复曝光对熟悉、主观相似及好感的作用','Repetition amplifies the sense of familiarity.',['amplify familiarity','amplify favorability'],
 '在这一系列实验中，Zajonc 及同事表明，反复曝光不只增强熟悉感，也增强与评分者的主观相似感和好感。此前研究已令人信服地表明，主观相似会带来吸引。新实验表明，居住邻近增加熟悉感与主观相似感，从而提升周围人的人际吸引力。这些精巧实验表明单纯曝光增加好感，为费城婚姻研究和荷兰同居研究提供了有力的因果论证。')

add(12,'同义改写','Which statement preserves the qualification in this sentence?',
 ['Every repeated meeting inevitably leads to romance.','Chance meetings eliminate attraction over time.','Only romantic partners ever meet by chance.','Repeated chance meetings can strengthen attraction and occasionally develop into romance.'],3,
 '哪项保留此句的限定？',['每次重复相遇必成恋情。','偶遇逐渐消除吸引。','只有恋人才会偶遇。','反复偶遇能增强吸引，有时发展成恋情。'],
 ['A sometimes 不等于每次必然。','B magnify 表示增强，不是消除。','C 没把偶遇范围限为已有情侣。','D 保留增强吸引与有时形成恋情两层含义。'],
 ['Repeated chance meetings do magnify attraction between people, sometimes resulting in a romantic relationship.'],
 'magnify','增强；放大','强化吸引，但不保证形成浪漫关系','Shared experiences can magnify an initial interest.',['magnify attraction','magnify an effect'],
 '反复偶遇确实会增强人与人之间的吸引，有时会由此形成浪漫关系。')

add(13,'作者意图','Why does the author introduce his visits to two shopping malls?',
 ['To report a randomized comparison of store sizes.','To open a new question about exposure effects beyond interpersonal relationships.','To establish that smaller malls contain more stores.','To prove that all American cities are objectively identical.'],1,
 '作者为何引入逛两个商场的经历？',['报告商场大小随机比较。','引出人际关系之外曝光效应的新问题。','确立小商场商店更多。','证明美国所有城市客观相同。'],
 ['A first-person 经历不是随机实验。','B other aspects of our lives 后举商场经验，将主题延伸到城市与消费。','C 只说第一次惊叹规模，没给数量比较结论。','D look alike 为疑问与感受，不是所有城市客观同一的证明。'],
 ['These mere exposure effects may influence other aspects of our lives, too.'],
 'puzzled','困惑的；不解的','第二次商场体验引出疑问，与第一次惊叹不同','She was puzzled by the similarity of the two buildings.',['feel puzzled','be puzzled by'],
 '这些单纯曝光效应也可能影响生活其他方面。例如，你想过美国城市和郊区为什么看着相似吗？我第一次去纽约 Staten Island 的大型商场时，对其规模和店铺数量印象深刻。后来去缅因州 Portland 郊区的一处中型商场时，我困惑了。')

add(14,'细节','What puzzled the author about the two malls?',
 ['They were both in Staten Island.','Neither contained any familiar stores.','They looked alike and contained many of the same stores.','They had exactly the same measured floor area.'],2,
 '两个商场的什么让作者困惑？',['两者都在 Staten Island。','都没有熟悉店铺。','看着相同，许多店铺也相同。','实测面积完全一样。'],
 ['A 问句明确对比 Staten Island 与 Portland。','B 反而是先前见过的店。','C look exactly the same 与 so many...also 两个问句直接支持。','D look 相似不是测量面积相等。'],
 ['Why did these two malls look exactly the same?','also in Portland’s mall?'],
 'malls','大型购物中心','作者对比两地购物中心，外观和店铺相似而非实测面积相同','The two malls featured several familiar shops.',['shopping malls','two malls'],
 '为什么这两个商场看起来一模一样？为什么我在 Staten Island 商场见过的那么多店，也出现在 Portland 的商场里？')

add(15,'语境词义','What does “cookie-cutter” suggest about the housing developments?',
 ['They look standardized and much like one another.','They are designed mainly for professional bakers.','They are unique to each conference attendee.','They are located inside airport terminals.'],0,
 'cookie-cutter 暗示住宅开发区什么特点？',['标准化、彼此很像。','主要为烘焙师设计。','每位参会者各有独特版本。','位于机场航站楼内。'],
 ['A 从高速沿途重复景观到城市为何相似，强调千篇一律。','B 字面误读，非烘焙用途。','C 与统一化景观相反。','D 是出租车沿途经过，不是航站楼内部。作者讲惯常旅途印象，没有量化全部城市。'],
 ['passing cookie-cutter housing developments, box stores, and shopping malls'],
 'cookie-cutter','千篇一律的；套模板式的','形容沿途住宅开发区缺乏差异','The suburb contained rows of cookie-cutter houses.',['cookie-cutter housing developments','cookie-cutter design'],
 '读研时，我开始去美国各城市参加心理学会议，也有类似感受。我会飞抵大机场，机场通常在大城市远郊。然后出租车走宽阔多车道公路，经过千篇一律的住宅开发区、大型卖场和商场，最后到达会议通常举办的市中心。这些城市为什么都看着相似？')

add(16,'逻辑关系','What contrast does the author draw between Japan and American suburbs?',
 ['Tokyo and Osaka have no large buildings or stations.','All Japanese stores belong to American chains.','American suburbs contain no restaurants.','Japanese cities can feel distinct despite shared urban features, unlike the repeated chains he describes in U.S. suburbs.'],3,
 '作者对日本与美国郊区作什么对比？',['东京大阪没有大楼车站。','日本商店全属美国连锁。','美国郊区没有餐厅。','日本城市虽有共同大都市设施仍感觉不同，而所述美国郊区反复出现连锁店。'],
 ['A both...many high-rise...large train stations 正相反。','B 解释提及 local stores，不是全为美国连锁。','C 原文明列两家餐饮连锁。','D Yet 引出设施相近但感受不同，随后对比美国郊区的相同店铺。perhaps 是推测本地店铺的作用，非确定因果结论。'],
 ['Yet they have very different feels, perhaps due to the overwhelming number of local stores, restaurants, and cafés.'],
 'perhaps','也许；可能','限定对本地店铺为何带来不同感觉的解释','The difference was perhaps due to the local businesses.',['perhaps due to','perhaps because of'],
 '日本并非如此：东京与大阪都是大城市，有许多高楼和大型车站，却给人很不一样的感觉，也许是因为大量本地商店、餐馆和咖啡馆。在美国郊区，不论纽约还是洛杉矶附近，你都能预期看到 Target、Whole Foods 等相同店铺，以及 Cheesecake Factory、Panera 等相同餐馆。')

add(17,'细节','How did the author’s responses change when he travelled?',
 ['He avoided Starbucks both at home and away.','He welcomed familiar stores and people more warmly away from home.','He greeted the student more curtly in Las Vegas.','He visited Starbucks every day in Charlottesville.'],1,
 '旅行时作者的反应怎样变化？',['在家出门都避开 Starbucks。','出门时更热情地欢迎熟悉店铺和熟人。','在 Las Vegas 更冷淡招呼学生。','在 Charlottesville 天天去 Starbucks。'],
 ['A traveling 时突然喜欢去，与此相反。','B 咖啡店偏好和对同一学生的招呼都随地点变化。','C curt hey 是校内，旅行见面更热情。','D 在当地去 local coffee shop，never went to Starbucks。这里是个人轶事，不是群体实验结果。'],
 ['when I was traveling, I would realize that all of a sudden I loved going to Starbucks.','Hey, Gary, so nice to see you!'],
 'curt','简短而冷淡的','描述校园内随意冷淡的 hey，与外地热情招呼形成对比','He answered with a curt greeting.',['a curt greeting','a curt “hey”'],
 '在 Charlottesville，我天天去本地咖啡店，从不去 Starbucks。但旅行时，我忽然发现自己爱去 Starbucks。在 Charlottesville 的心理学楼 Gilmer Hall 看到研究生经过，我会很简短地说声 hey。在 Las Vegas 的会议看到同一名学生，我会说：“嘿，Gary，见到你真高兴！”')

add(18,'推断','What tentative explanation follows the author’s near-hug?',
 ['He habitually hugged Gary in Gilmer Hall.','Strangers become less noticeable in familiar places.','Familiar people or stores may seem especially attractive amid unfamiliar surroundings.','Every traveller always embraces familiar students.'],2,
 '差点拥抱之后，作者提出什么初步解释？',['在 Gilmer Hall 习惯拥抱 Gary。','熟悉地方让陌生人较不显眼。','陌生环境中，熟人或熟悉店铺可能格外有吸引力。','每位旅客总会拥抱熟悉学生。'],
 ['A No chance 否定在校内拥抱。','B 不是当前解释的内容。','C seems...particularly...away...strangers 是作者的暂时概括，不能去掉限定。','D almost 是差点，且个人例子不扩大为所有旅客。开头 and 承接前段，保留既有连续分段。'],
 ['a familiar person or store seems to be particularly attractive when you are away from familiar places and surrounded by strangers.'],
 'surrounded','被围绕；身处……之中','身处陌生人中时熟悉者的吸引可能更突出','She felt reassured by a familiar face when surrounded by strangers.',['surrounded by strangers','away from familiar places'],
 '而且差点拥抱他。我会在 Gilmer Hall 拥抱他吗？绝不可能。因此，当你远离熟悉地点、身处陌生人之中时，一个熟人或熟悉店铺似乎会格外有吸引力。')

add(19,'作者意图','What does this question propose for investigation?',
 ['Whether unfamiliar settings strengthen the mere exposure effect.','Whether familiarity disappears in every new place.','Whether all exposure experiments have been disproved.','Whether people can recognize any familiar face at all.'],0,
 '此问提出要研究什么？',['陌生环境是否增强单纯曝光效应。','熟悉感是否在每个新地点消失。','所有曝光实验是否均被推翻。','人究竟能否认出任何熟悉面孔。'],
 ['A even stronger...unfamiliar setting 是核心比较。','B 更强不等于消失。','C 没质疑此前所有实验真伪。','D 研究强度如何随情境改变，不是基础识别能力。疑问句尚未给结果。'],
 ['the mere exposure effect is even stronger when you’re in an unfamiliar setting?'],
 'setting','环境；情境','指陌生场景这一可能改变效应强弱的条件','The same task may feel different in an unfamiliar setting.',['an unfamiliar setting','a familiar setting'],
 '有没有可能，身处陌生环境时，单纯曝光效应甚至更强？')

add(20,'细节','How did the researchers approximate encounters with strangers?',
 ['By counting conversations directly in every city.','By experimentally moving all census respondents.','By recording every traveller’s greeting.','By using census residential mobility as an indirect indicator.'],3,
 '研究者怎样近似估计遇见陌生人的频率？',['逐城直接计数所有对话。','实验性搬迁所有普查对象。','记录每位旅客的招呼。','用普查居住流动性作间接指标。'],
 ['A approximate 不等于直接观察所有相遇。','B 使用已有普查资料，不是安排搬迁。','C 没普遍记录旅行招呼。','D 推理是迁入迁出多的城市更可能被陌生人围绕，属于代理指标而非精确计数。'],
 ['use residential mobility data from the U.S. census to approximate how often people meet strangers'],
 'approximate','近似估计','用居住流动性间接衡量相遇频率，非直接逐次测量','The team used survey data to approximate daily contact.',['approximate a frequency','use data to approximate'],
 '为找答案，我和学生决定用美国人口普查的居住流动性数据，近似估计人们遇到陌生人的频率。理由是，在很多人搬迁的城市，身处陌生人之中的机会，比人们不怎么搬迁的城市高得多。')

add(21,'逻辑关系','Why were national chains predicted to be more popular in mobile states?',
 ['They were assumed to sell only local products.','Their familiarity might offer newcomers psychological comfort.','They were proven to have lower prices in every state.','They prevented all residents from moving again.'],1,
 '为何预期全国连锁在高流动州更受欢迎？',['假设只卖当地产品。','熟悉感可能给新来者心理安慰。','已证明各州价格总更低。','能阻止所有居民再搬家。'],
 ['A local stores 是比较对象，不是连锁仅售本地产品。','B more familiar...offer psychological comfort 是提出预测的机制设想。','C 没比较价格。','D 没声称店铺阻止搬迁。If so 标记假说推演，当前短段还未报告检验结果。'],
 ['national chain stores are more familiar than local stores in a new town and offer psychological comfort.'],
 'newcomers','新来者','新迁入一州或城镇的人，不等于所有居民','Newcomers often recognize national store names.',['a lot of newcomers','offer newcomers comfort'],
 '我们检验，Nevada、Florida 等高流动州是否比 Pennsylvania、West Virginia 等稳定州有更多 Chili’s、Whole Foods、Payless Shoes 这样的全国连锁店。想法是，在新城镇，全国连锁比本地店更熟悉，能提供心理安慰。如果如此，连锁应在 Nevada、Florida 这类新来者很多的州更受欢迎。')

add(22,'推断','What does the statistical adjustment establish in the reported comparison?',
 ['Income and population explain the entire association.','All possible confounders have been removed.','The chain-store difference persists after accounting for median income and population.','The analysis randomly assigned states to mobility conditions.'],2,
 '所报统计调整说明什么？',['收入人口解释全部关联。','所有潜在混杂都已消除。','考虑收入中位数和人口后，连锁数量差异仍在。','随机把州分配到流动条件。'],
 ['A true even when controlling 表明考虑两因素后结果仍在。','B 只列两项控制，不能推成全部混杂排除。','C 保留结果与控制变量的准确范围。','D 统计控制不是随机分组，也不能单独证明搬迁导致连锁增长。'],
 ['This is true even when controlling for median income and the total population'],
 'controlling for','控制；统计上考虑','分析中考虑收入和人口差异，不是实验操纵两者','The association remained after controlling for income.',['control for median income','control for population'],
 '果然，高流动州比稳定州有更多全国连锁店。即使控制收入中位数和总人口，结果仍如此，因为较富、人口较多的州也会吸引更多商家。')

add(23,'细节','Which students reported greater liking for national chain stores?',
 ['UVA students who had moved more frequently while growing up.','Only students who had never left Virginia.','Students experimentally forced to move each year.','All students who had grown up in one place.'],0,
 '哪些学生更喜欢全国连锁？',['成长中搬迁更频繁的 UVA 学生。','只有从未离开 Virginia 的学生。','被实验强迫每年搬迁的学生。','所有在同一地长大的学生。'],
 ['A grew up moving more frequently 与 grew up in one place 是明示比较。','B 没按是否离开州界分组。','C 这里记录成长经历，不是实验安排搬家。','D 方向相反，且不应把组间趋势变成所有个体。单句发现不独立证明因果。'],
 ['students who grew up moving more frequently liked national chain stores more than UVA students who grew up in one place.'],
 'frequently','频繁地','描述成长经历的搬迁次数多，不是近期一天的旅行频率','The family moved frequently during her childhood.',['move frequently','more frequently than'],
 '我们还发现，成长过程中搬迁更频繁的 University of Virginia 学生，比在同一个地方长大的 UVA 学生更喜欢全国连锁店。')

add(24,'细节','What distinguished the experimental conditions?',
 ['Actual assignment to jobs in three different cities.','A requirement that every student move annually.','A comparison of ten years of real employment records.','Imagining repeated moves, long-term stability, or a typical day.'],3,
 '实验条件之间有什么不同？',['真实分配至三座城市工作。','要求每个学生每年搬家。','比较十年实际就业记录。','想象反复搬迁、长期稳定或普通一天。'],
 ['A asking...think 是想象工作情境，没有真实岗位分配。','B every other year 是隔年，且仅一个想象条件。','C 至少十年是设想岗位要求，不是已经追踪十年。','D 三种心态诱导准确对应；普通一天是控制组。'],
 ['we manipulated the mindset of residential mobility','move to a new city every other year','live in the same city for at least ten years','a typical day in their own lives (the control group).'],
 'mindset','心态；思维状态','通过想象未来工作来诱导，不是真让人完成多年搬家','The task encouraged a mindset of stability.',['manipulate a mindset','a mobility mindset'],
 '在最后一系列实验中，我们操纵居住流动心态：让一些参与者想象 UVA 毕业后立刻从事一份要求每隔一年搬到新城市的工作；另一些想象毕业后立刻从事一份要求在同一城市至少住十年的工作；其余人想象自己生活中普通的一天，作为控制组。')

add(25,'细节','Which materials were used in the modified exposure tasks?',
 ['Marriage licenses and store receipts.','Chinese characters and portrait photographs.','Only Turkish vocabulary tests.','Road maps and apartment floor plans.'],1,
 '改编曝光任务用了什么材料？',['结婚许可和购物小票。','汉字和人像照片。','仅土耳其语词汇测验。','道路地图和公寓平面图。'],
 ['A 是其他研究可能涉及的资料，不在此任务描述。','B one with Chinese characters...other with portrait photos 明确列出。','C 不是土耳其语知识测验，也不限一种材料。','D 没用地图或户型图。当前单句只述材料，还没报告哪组效应更强。'],
 ['one with Chinese characters and the other with portrait photos.'],
 'modified','改编的；经过调整的','沿用先前曝光任务并改变版本，不表示原任务无效','The researchers used a modified version of the task.',['a modified version','a modified task'],
 '随后，我们给出改编版 Zajonc 单纯曝光任务：一种用汉字，另一种用人像照片。')

assert len(out)==25 and [q['id'] for q in out]==[t['questionId'] for t in targets]

def persist():
 path=ROOT/'source/short-questions/additional.json';existing=load('source/short-questions/additional.json');byid={q['id']:q for q in existing}
 for q in out:
  if q['id'] in byid:assert byid[q['id']]==q,('Refuse to overwrite changed authoring',q['id'])
  else:existing.append(q)
 path.write_text(json.dumps(existing,ensure_ascii=False,indent=2)+'\n',encoding='utf8',newline='\n')
 review=dict(batchId='batch-028',date='2026-10-23',pdfSha256=b['pdfSha256'],checkedPdfPages=list(range(111,116)),questionIds=[q['id'] for q in out],paragraphs=[dict(id=pid,textSha256=hashlib.sha256(pp[pid]['text'].encode()).hexdigest()) for pid in dict.fromkeys(q['paragraphId'] for q in out)],note='完整PDF111–115原页视觉核对及跨页拼接。词频观察与无意义词、汉字、人像和课堂曝光实验分开；假称Turkish不作真实语言事实；课堂评分量表、出席次数和主观熟悉/明确认识分开，linearly保留作者措辞但不编精确等差。机制实验不把早前观察婚配研究改成随机试验。购物/旅行属个人轶事；普查流动性是代理指标、统计控制非因果保证；成长经历观察与想象工作心态实验分开，every other year译隔年。and almost为既有跨单元句片，保留ID与连续阅读。末段完整审阅含尚未配题结果，不提前倒灌证据，不宣称逐句直接证据全覆盖。')
 (ROOT/'source/short-questions/review-chapter10-exposure25.json').write_text(json.dumps(review,ensure_ascii=False,indent=2)+'\n',encoding='utf8',newline='\n')
 print('Saved',len(out),'of 25 individually authored exercises')

if __name__=='__main__':persist()
