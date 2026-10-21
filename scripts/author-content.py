"""Curated offline question batch. All quotations are checked against book.json.
Explanations, questions and learner examples are authored learning material.
No API, runtime generation, repeated fill-in templates, or invented book content.
"""
from pathlib import Path
import json, hashlib, random, re, runpy
ROOT=Path(__file__).resolve().parents[1]
b=json.loads((ROOT/'public/data/book.json').read_text(encoding='utf-8')); out=[]
def vocab(word,meaning,context,example,*collocations):return dict(word=word,meaning=meaning,context=context,example=example,collocations=list(collocations))
V={
'known':vocab('known for','因……闻名','说明该地点有名的物产，而非人物职业','The village is known for its pottery.','be known for its scenery','be widely known for'),
'cultivate':vocab('cultivating','耕作；种植（cultivate 的 -ing 形式）','种植水稻与茶叶，说明 Yoshi 的日常生活','The family earns a living by cultivating rice.','cultivate rice','cultivate the land'),
'ancestor':vocab('ancestor','祖先','父系世代延续的生活路径','Her ancestors lived in the valley.','a common ancestor','follow one’s ancestors'),
'drop':vocab('dropped out','退学；中途退出','读了一年农业高中后离校务农','He dropped out of the course to work full-time.','drop out of school','a school dropout'),
'laid':vocab('laid out','规划；安排','祖先已形成的生活道路','They laid out a plan for the garden.','lay out a plan','a path laid out by'),
'scholarship':vocab('scholarship','奖学金','帮助作者赴 Maine 留学的资助','She won a scholarship to study abroad.','win a scholarship','a scholarship to study'),
'yet':vocab('Yet','然而','把只想学英语与意外恋爱连接起来','I wanted a quiet trip. Yet I made many new friends.','and yet','yet another'),
'forgood':vocab('for good','永久地','作者毕业后离开日本，并非只是短暂旅行','They moved to the coast for good.','leave for good','close for good'),
'diverged':vocab('diverged','分岔；产生差异','父子人生路径发生很大分歧','Their interests diverged after college.','diverge from','diverging paths'),
'convivial':vocab('convivial','欢乐友好的；适于交际的','与老友、家人相处的亲切愉快生活','We enjoyed a convivial evening with our neighbours.','a convivial atmosphere','a convivial evening'),
'yearning':vocab('yearning','强烈渴望','作者想看外面世界的深切愿望','She felt a yearning to explore new places.','a yearning for','a yearning to do'),
'tradeoffs':vocab('trade-offs','权衡；取舍','稳定与流动等生活方式的利弊交换','Every design involves trade-offs.','trade-offs between','make a trade-off'),
'draw':vocab('draw from','从……汲取；利用','以心理科学研究为论证资料','The course draws from several disciplines.','draw from research','draw on evidence'),
'supplement':vocab('supplementing','补充','用文学、电影和哲学例子补充已有数据','She supplemented the report with interviews.','supplement data with','supplement an income'),
'expense':vocab('at the expense of','以……为代价','把他人幸福置于个人幸福之前时的代价','He built his career at the expense of his health.','at the expense of others','at one’s own expense'),
'perhaps':vocab('perhaps','也许','作者对父亲动机提出可能解释，非确定事实','Perhaps a smaller goal would be more useful.','perhaps because','perhaps the most'),
'cherish':vocab('cherish','珍爱；珍惜','父亲可能学会珍惜农场日常生活','We cherish the time we spend together.','cherish a memory','cherish everyday life'),
'inaction':vocab('inaction','不行动；未采取行动','长期遗憾常来自没说、没做的事情','The delay was caused by years of inaction.','regret inaction','a policy of inaction'),
'forgo':vocab('forgo','放弃；舍弃','为了自我牺牲而放弃机会','She chose to forgo the promotion.','forgo an opportunity','forgo a benefit'),
'authentic':vocab('authentic','真实的；忠于自我的','与自己的欲望和理想一致的人生','He wanted a life that felt authentic.','an authentic life','authentic experience'),
'quandary':vocab('quandary','困境；难以解决的问题','Sacks 人生的价值难以由既有两种维度概括','The result left the team in a quandary.','be in a quandary','a moral quandary'),
'perspective':vocab('perspective','视角；看法','有些经历会改变看待世界的方式','Travel gave her a new perspective on work.','change one’s perspective','a fresh perspective'),
'likewise':vocab('Likewise','同样地；类似地','把巧克力的复杂味道映射到丰富经历','The first group improved; likewise, the second group progressed.','and likewise','likewise for'),
'accumulation':vocab('accumulation','积累','经历随时间累加形成心理丰富性','The archive is an accumulation of many years of work.','the accumulation of experience','gradual accumulation'),
'legitimizing':vocab('legitimizing','使获得认可；使合法化','使幸福研究在心理学界获得科学地位','The new evidence helped legitimize the field.','legitimize a practice','legitimize a field'),
'autonomy':vocab('autonomy','自主性','Ryff 所列美好生活构成之一','The job gives employees considerable autonomy.','personal autonomy','autonomy in decision-making'),
'overlap':vocab('overlap','重叠；共同部分','幸福与意义的自我报告常有大量重合','There is some overlap between the two courses.','overlap between','a considerable overlap'),
'adequate':vocab('adequate','足够的；适当的','原有概念不足以描述 Sacks 式的人生','The room has adequate space for study.','adequate vocabulary','adequate for the task'),
'mindset':vocab('mindset','思维模式','关于能力是否可以提升的看法','Feedback can help students develop a growth mindset.','a growth mindset','a fixed mindset'),
'motivated':vocab('motivated','激励；促使','儿子的建议促使作者尝试修窗','The challenge motivated her to practise daily.','motivate someone to do','highly motivated'),
'frequency':vocab('frequency','频率','令人愉快的小互动出现的次数','The frequency of meetings has increased.','the frequency of events','high frequency'),
'snag':vocab('snag','障碍；意外问题','幸福随时间变化，因而不稳固','The plan hit a snag at the final stage.','hit a snag','a technical snag'),
'boils':vocab('boils down to','归结为','把意义的核心概括为人生有没有指向','The decision boils down to time and cost.','boil down to a choice','it all boils down to'),
'precariousness':vocab('precariousness','不稳定；脆弱性','意义感可能突然失去支撑','The storm exposed the precariousness of the bridge.','the precariousness of life','economic precariousness'),
'quantified':vocab('quantified','量化','作者借物质财富作类比描述经历的累积','The benefits cannot easily be quantified.','quantify the impact','be quantified by'),
'safetynet':vocab('safety net','安全网；保障','幸福或有意义生活的舒适与安全感','Savings can provide a financial safety net.','provide a safety net','a social safety net'),
'zerosum':vocab('zero-sum games','零和博弈','作者否定三种美好生活维度必须此消彼长','The two teams need not treat cooperation as a zero-sum game.','a zero-sum game','zero-sum thinking'),
'resilience':vocab('resilience','韧性；恢复能力','心理丰富性可能给留下的人增加的生活品质','The team showed resilience after the setback.','build resilience','emotional resilience'),
'vicarious':vocab('vicarious','间接体验的；通过他人获得的','本书将探讨是否必须亲身积累体验','Reading can offer vicarious experiences.','vicarious experience','vicarious pleasure'),
'ultimate':vocab('ultimate','最终的；根本的','在此是亚里士多德关于幸福目标的表述','Our ultimate goal is to understand the process.','the ultimate goal','ultimate responsibility'),
'undue':vocab('undue','过度的；不适当的','要求自己总快乐所施加的过分压力','The deadline placed undue pressure on the team.','undue pressure','undue emphasis'),
'equate':vocab('equate','等同；视为相同','研究中美国大学生把幸福与成就联系起来','We should not equate speed with quality.','equate A with B','be equated with'),
'overestimate':vocab('overestimate','高估','对成功和失败带来的情绪强度预测偏高','We often overestimate how much we can do in a day.','overestimate the impact','overestimate one’s ability'),
'tenure':vocab('tenure','终身教职；任期','助理教授预测获得或未获终身教职的情绪','She applied for tenure after several years.','get tenure','be denied tenure'),
'intensity':vocab('intensity','强度','与积极事件的发生频率形成对照','The intensity of the light changed slowly.','emotional intensity','the intensity of an experience'),
'replicate':vocab('replicate','重复验证；复现','模仿微笑的实验结果未获所有研究一致复现','Another team tried to replicate the experiment.','replicate findings','a replication study'),
'ruminated':vocab('ruminated','反复琢磨；反刍思考','反复想着解不开字谜的失败','He ruminated about the meeting for hours.','ruminate about a failure','ruminate on a problem'),
'associated':vocab('associated with','与……相关联','幸福与好运或成就的文化联系','This colour is often associated with spring.','be associated with','closely associated'),
'reappraisal':vocab('reappraisal','重新评价','重新解释事件以调节负面情绪','A reappraisal helped her see the event differently.','cognitive reappraisal','a positive reappraisal'),
'counterfactuals':vocab('counterfactuals','反事实设想','对未发生的录取路径进行如果式想象','He kept imagining counterfactuals about the choice.','counterfactual thinking','consider counterfactuals'),
'statusquo':vocab('status quo','现状','过度满足现状可能妨碍挑战与成长','The committee voted to maintain the status quo.','maintain the status quo','challenge the status quo')
}
def add(pnum,ptype,prompt,options,correct,explanation,analyses,quotes,vkeys,grammar,strategy,ctx='near',support='explicit',translation=None):
 p=b['paragraphs'][pnum]; ss=[s for s in b['sentences'] if s['paragraphId']==p['id']];evidence=[];ranges=[]
 for quote in quotes:
  start=p['text'].find(quote); assert start>=0,(p['id'],quote);end=start+len(quote);ev=[s for s in ss if s['start']<end and s['end']>start]; assert ev
  evidence.append(dict(quote=quote,sentenceIds=[s['id'] for s in ev],sources=list({(r['pdfPage'],r['block']):r for s in ev for r in s['sources']}.values())));ranges.extend([ss.index(s) for s in ev])
 lo=0 if ctx=='all' else max(0,min(ranges)-1);hi=len(ss)-1 if ctx=='all' else min(len(ss)-1,max(ranges)+1)
 context=ss[lo:hi+1];passage=p['text'][context[0]['start']:context[-1]['end']];voc=[V[k] for k in vkeys]
 for v in voc:assert v['word'].lower() in passage.lower(),(v['word'],passage)
 chapter=p['chapterId'];n=sum(q['chapterId']==chapter for q in out)+1
 q=dict(id=f'q-{chapter}-{n:03}',version=1,chapterId=chapter,sectionId=p['sectionId'],paragraphId=p['id'],sentenceIds=[s['id'] for s in context],passage=passage,prompt=prompt,options=options,answer=correct,type=ptype,explanation=explanation,analyses=analyses,evidence=evidence,vocabulary=voc,grammar=grammar,strategy=strategy,support=support,editorialStatus='逐题编写；引文与提取原文精确匹配，原页核对状态另计')
 if translation:q['translation']=translation
 # Fixed per-question permutation avoids a repeating answer-position sequence.
 if out:
  order=list(range(4)); random.Random(q['id']+'editorial-v1').shuffle(order)
  q['options']=[options[i] for i in order];q['analyses']=[re.sub(r'^[A-D]',chr(65+j),analyses[i]) for j,i in enumerate(order)];q['answer']=order.index(correct)
 def canonical_numbers(v):
  if isinstance(v,float) and v.is_integer(): return int(v)
  if isinstance(v,list):return [canonical_numbers(x) for x in v]
  if isinstance(v,dict):return {k:canonical_numbers(x) for k,x in v.items()}
  return v
 q=canonical_numbers(q)
 q['fingerprint']=hashlib.sha256(json.dumps(q,ensure_ascii=False,sort_keys=True,separators=(',',':')).encode()).hexdigest();out.append(q)
# Paragraph indexes are pinned to extraction-v1, checked by explicit source quotations.
add(0,'细节','What is Yoshi’s hometown known for?', ['Its rice exports and softball teams.','Its green tea and clementines.','Its agricultural high school.','Its annual cherry blossom parties.'],1,
'开头先介绍出生地点，再说明当地因绿茶和小柑橘闻名。务农、学校、活动出现在后文，但不是 known for 的内容。', ['A 把后文的水稻种植和垒球活动错配为城镇闻名的原因；片段也没有 rice exports。','B 直接对应 known for its green tea and clementines。','C 农业高中是 Yoshi 的经历，原文没有称该校使城镇闻名。','D 片段没有把赏樱聚会列为该镇闻名的原因。'],['Yoshi was born in a small mountain town on the island of Kyushu, Japan, known for its green tea and clementines.'],['known'],
'主句是 Yoshi was born，was born 为一般过去时被动形式，表示出生。in a small mountain town 交代地点；on the island of Kyushu 进一步定位。known for... 是过去分词短语，对前面所说的地点作补充说明；不是 Yoshi 自己种的东西使他个人出名。',
'细节定位题：先定位专有名词 Yoshi 和 known for，再核对修饰对象。不要因为后文出现 rice 或 school 就把人物经历当作地点特征。',translation='Yoshi 出生在日本九州岛的一个山间小镇，当地以绿茶和小柑橘闻名。')
add(0,'同义改写','Which statement best restates Yoshi’s connection with earlier generations?', ['He left farming to study family history.','He returned to the town after years overseas.','He followed a family pattern in both place and occupation.','He shared his ancestors’ birthplace but rejected their work.'],2,
'父辈、祖父及此前男性祖先都生活在当地；Yoshi 也一生住在那里种稻种茶。结尾还明确说他沿祖先铺设的道路生活。',['A 误把农业生活改为历史研究，且 left farming 与原文相反。','B 原文是 lived his entire life there，没有海外归来。','C 把地点延续与职业延续合并改写，受到首尾句支持。','D rejected their work 与 cultivating rice and tea 及 followed the path 相反。'],['Like his father, grandfather, and every male ancestor before him, Yoshi has lived his entire life there, cultivating rice and tea.','Yoshi followed the path laid out by his ancestors'],['cultivate','ancestor'],
'Like his father... 是前置比较短语，不是谓语。主句 has lived 使用现在完成时，表示从过去延续至今；cultivating rice and tea 是现在分词短语，补充与主语 Yoshi 相关的生活活动。',
'同义改写需同时保留范围和关系。family pattern 概括世代延续，place and occupation 概括地点与耕作；entire life 不能改成离开后返回。',ctx='all')
add(0,'细节','What did Yoshi do after about one year of agricultural high school?', ['He became a farmer.','He joined a softball league professionally.','He married a woman from his school.','He moved to a neighbouring town.'],0,
'He chose this path 后的 when 从句具体交代退学成为农民。婚姻在二十七岁，不能与高中退学时间混同。',['A become a farmer 是原文明示的去向。','B 原文是 neighborhood softball league，没有职业身份，也未置于退学后立即发生。','C 妻子来自邻镇，不等于同校同学，结婚时间也不同。','D 来自邻镇的是妻子，不能把修饰对象换为 Yoshi。'],['He chose this path after just a year of agricultural high school, when he dropped out to become a farmer.'],['drop'],
'He chose this path 是一般过去时主句。after just a year... 表时间；when he dropped out 补充这一阶段发生的事；to become a farmer 是不定式目的状语。',
'时间细节题要对齐事件与时间。防止把下一句的 married 与当前句的 after just a year 拼接成一个不存在的经历。')
add(0,'语境词义','In “the path laid out by his ancestors”, what does “path” refer to?', ['A road connecting farms and hot springs.','A sequence of trips organised by neighbours.','The physical route from Kyushu to Tokyo.','An established way of living passed through the family.'],3,
'path 是生活道路的隐喻。后面的 occupation, place, expectations, and way of life 说明延续的内容超出血缘。',['A 把隐喻误读成公路；没有连接农场与温泉的路线说明。','B 邻里旅行只是生活活动之一，不能概括祖先的职业与期待。','C 去东京是作者的经历，不是 Yoshi 沿袭的道路。','D 对应世代的生活方式，包括职业、地点与期待。'],['In making these choices, Yoshi followed the path laid out by his ancestors, connecting with them through common threads of not just blood, but occupation, place, expectations, and way of life.'],['laid','ancestor'],
'laid out by his ancestors 是被动含义的过去分词短语，后置修饰 path。connecting with them 是现在分词短语；not just blood, but... 用并列成分扩大共同纽带的范围。',
'词义题先读同句解释项。occupation、expectations、way of life 构成语义线索；看到 path 就选实际道路属于只认字面。')
add(1,'细节','What enabled the author to study abroad in Maine during college?', ['A job with Japan’s Ministry of Education.','A scholarship from Rotary International.','An invitation from his girlfriend in Boston.','A place on a neighbourhood association trip.'],1,
'大学四年级获得 Rotary International 奖学金，目的为到 Maine 留学；与后面改变职业计划、去 Boston 看恋人不同。',['A Ministry of Education 是留学前职业计划，不是资助来源。','B 与 scholarship from Rotary International 逐字对应。','C Boston 关系发生在后面，未说是出国留学的邀请来源。','D 邻里协会旅行是父亲的活动。'],['In my fourth year of college, I got a scholarship from Rotary International to study abroad in Maine.'],['scholarship'],
'时间状语 In my fourth year of college 位于句首；I got a scholarship 是一般过去时主句；from 表来源，to study abroad... 表示奖学金支持的学习目的。',
'定位 Maine 后回读动词与介词。from Rotary International 回答资助来源；不要用后文有吸引力的人生事件替换明示原因。')
add(1,'逻辑关系','What contrast is introduced by “Yet” in the account of the summer programme?', ['He wanted a relationship but decided to study instead.','He planned to stay in Tokyo but found a job in Maine.','He hoped only to improve his English but unexpectedly fell in love.','He disliked Boston but visited it for academic research.'],2,
'前文说厌倦恋爱，只想提高英语；Yet 引出结识韩国学生并恋爱的转折。',['A 把意愿与实际结果倒置。','B 没有在 Maine 找工作的情节。','C only 对应 simply，unexpectedly 对应 Yet 表示的意外转折。','D Boston 的出行目的是见她，不是学术研究；片段也没有 dislike。'],['I simply wanted to improve my English. Yet, I met a student from Korea and fell in love.'],['yet'],
'wanted to improve 中不定式作 wanted 的补足内容。Yet 作连接副词引出反预期；met 与 fell 是同一主语的并列过去时谓语。',
'逻辑题先圈出 simply 与 Yet：一个限制原先目的，一个引入实际转折。正确选项要同时保留两侧，不能只复述恋爱事件。')
add(1,'语境词义','What does “for good” mean in the author’s account of leaving Japan?', ['For the summer programme.','For a better-paid government job.','For the benefit of his hometown.','Permanently.'],3,
'for good 是固定短语，表示永久离开；后文列出各城市生活轨迹，与早期短期留学形成区别。',['A 暑期课程发生在更早的 Staten Island 经历，不是此处离开的期限。','B 原文没有说这次离开是为收入更高的政府职位。','C 把 good 误读成道德或利益判断。','D permanently 对应固定短语 for good。'],['In June 1993, after graduation, I left Japan for good.'],['forgood'],
'In June 1993 与 after graduation 都是时间状语。I left 是一般过去时；for good 整体作副词性成分，不能按 for + 好处逐词理解。',
'固定短语题要用后文核对。连续迁往美国城市支持 permanently，但不能凭此推断以后从未回日本探亲。')
add(2,'主旨','What chiefly occupies the author’s thoughts three decades after leaving home?', ['Why his life and his father’s took such different courses.','Whether his father should have changed his occupation.','How to persuade his children to return to Japan.','Which of his former cities was the most comfortable.'],0,
'两句都围绕父子路径差异：父亲有机会却未搬离，而自己搬过许多次。这里的疑问不是劝说别人或评选城市。',['A 直接概括 diverged from my father’s 与两种搬迁选择。','B 只抓职业，漏掉段落核心的迁移与生活分歧，也没有 should 的建议。','C 没有提到劝孩子返回。','D 没有在本段比较城市舒适度。'],['I often find myself wondering how my life could have diverged from my father’s to such an extraordinary extent.','I wonder why he didn’t move away when he had the chance, and why, in contrast, I have moved so many times.'],['diverged'],
'find myself wondering 是 find + 宾语 + 现在分词。how my life could have diverged... 为 wondering 的宾语从句；could have + 过去分词表示对已经发生差异的思索。',
'主旨题追踪重复的疑问结构 how / why，寻找共同对象。不能把其中一个细节放大为本段全部意图。',ctx='all')
add(3,'有限推断','Why does the author suggest he could not have lived exactly like his father?', ['He was certain a stable life would make everyone unhappy.','He had an especially strong desire to explore beyond home.','His father had asked him to leave the town.','He found all friendship with old classmates uninteresting.'],1,
'作者承认羡慕父亲某些生活，却认为探索外部世界的渴望太强，无法照走祖辈道路。有限推断是个人适配不同，而非否定稳定生活。',['A everyone 是范围扩大，原文还称父亲生活 good。','B 对应 intense yearning to see the outside world；属于有明确根据的概括。','C 原文没有父亲要求他离开。','D 作者反而希望能与老友喝酒回忆，并未否定所有旧友关系。'],['Though I love my job most days, I do envy my father’s simple, convivial life sometimes','I had an intense yearning to see the outside world, too intense to follow the well-trodden life path of my ancestors.'],['convivial','yearning'],
'Though 引导让步从句；do envy 用 do 强调羡慕确实存在。too intense to follow... 是 too + 形容词 + 不定式结构，表示渴望强烈到无法照原路径生活。',
'推断保持个体范围：I could not 不能替换成所有人都不应该。留意 though / but 表示的复杂态度，避免把作者立场简化成完全赞成或反对。',ctx='all',support='inference')
add(4,'逻辑关系','What is the function of the paired alternatives such as “stable” and “mobile”?', ['To rank all mobile lives as morally superior.','To show that the author has abandoned psychological research.','To establish choices whose trade-offs raise the question of a good life.','To demonstrate that all readers have already made the same choice.'],2,
'一组组相对生活方式之后用 But which one... 提出问题。列举的功能是铺垫取舍与核心研究问题，并非提前宣布唯一优胜者。',['A 没有道德高下排序。','B 研究问题正由此引出，不是被放弃。','C 对应 trade-offs 与结尾 good life 的提问。','D Some... Others... 明确承认读者选择不同。'],['There are, of course, trade-offs between a stable life and a mobile life, a simple life and a dramatic life, a comfortable life and a challenging life, a conventional life and an unconventional life.','But which one gets us closer to a good life?'],['tradeoffs'],
'There are 为存在句。between A and B 的并列结构连续列出四组权衡；But 引出转向总问题的疑问句。',
'逻辑功能题不能只看词义。联系列举后的问题，判断列举在论证链中的作用：提出取舍 → 引向美好生活的定义。',ctx='all')
add(5,'作者意图','How does the author plan to investigate what makes a good life?', ['By treating literary stories as controlled experiments.','By replacing psychological data with personal opinions.','By relying exclusively on philosophical definitions.','By using psychological research supplemented by cultural examples.'],3,
'draw from decades of research 是研究基础，supplementing ... with examples 表示补充关系。文学电影哲学例子不是实验数据。',['A 将例子误当实验，改变证据性质。','B replacing 与 supplementing 相反。','C exclusively 排除了原文明确的心理研究。','D 同时保留研究基础与补充例子的关系。'],['To answer this question, I will draw from decades of research in psychological science, supplementing the available data with examples from literature, film, and philosophy.'],['draw','supplement'],
'To answer this question 是目的状语；I will draw... 为主句。supplementing... 是现在分词短语，逻辑主语为 I；with examples 表补充材料。',
'作者意图题关注方法词 draw from、supplement。正确答案保留证据层级，不能把 literature 升格为 controlled experiments。',ctx='all')
add(6,'作者意图','Why is Donna Tartt’s question included?', ['To frame a tension between personal happiness and making others happy.','To report the results of an experiment about generosity.','To establish that writers reject all forms of happiness.','To prove that self-sacrifice prevents regret.'],0,
'引述提出两种幸福的取向，作者随后继续用 should 提问。它用于构建问题，不是实验证据或已获证明的结论。',['A 与引述及后续自问构成同一张力。','B 此处是小说作者的谈话，没有实验。','C 从疑问推成所有作家拒绝幸福，双重扩大。','D 后文还要质疑牺牲是否无悔，此处并未证明。'],['Should we strive to be happy? Or should we work for others’ happiness before thinking of our own?'],['expense'],
'Should we... 与 Or should we... 是并列选择式反问。before thinking... 中 thinking 为动名词，our own 省略与前文相同的 happiness。',
'观点归属题先辨引述者与作者的后续评论。疑问句用于展开议题，不能当作统计结论或已经成立的定理。',ctx='all')
add(7,'细节','What was the outcome of the author’s decision to maximise his own happiness by moving?', ['His sons immediately became happier at their new school.','He did not find himself happier in the end.','His father decided to move to the same city.','He concluded that career moves never benefit anyone.'],1,
'选择工作搬家后，作者明说 did not find myself any happier。这里只报道这次个人经历，不能扩大到所有职业搬迁。',['A 原文只说孩子原本不想离开朋友，未报告新学校立即更快乐。','B 是该句的准确改写。','C 父亲决定留下，不是同迁。','D never / anyone 是没有根据的普遍化。'],['Though my sons did not want to move away from their friends and their hometown, I chose to maximize my own personal happiness.','In the end, I did not find myself any happier.'],['expense'],
'Though 从句表示让步，主句 chose to maximize 说明选择。find myself + 形容词是宾语补足语结构；not ... any happier 表示没有比以前更幸福。',
'结果细节题区分动机和结果。chose to maximize 是目的，did not find 是结果；不能把想要的效果直接当成实际效果。',ctx='all')
add(7,'有限推断','How certain is the author about why his father has been happy?', ['He identifies the father’s income as the only proven cause.','He reports that his father was experimentally assigned to lower expectations.','He offers adjusted expectations as a possible explanation.','He says family tradition has no possible relevance.'],2,
'It is possible that 限定确定程度；调整期待、珍惜日常是作者提出的解释，未报告对父亲进行实验。',['A income 与 only proven cause 都没有文本支持。','B 把个人推测改成随机干预事实。','C possible explanation 对应 It is possible that。','D 文中未否定传统，反而多次提到。'],['It is possible that the main reason my father has been so happy is that he adjusted his expectations so that he came to cherish everyday life on the farm, enjoying smaller pleasures alongside his longtime spouse.'],['cherish'],
'It is possible that... 中 It 为形式主语。the main reason... is that... 是嵌入结构；so that 引导结果 / 目的相关说明，enjoying... 补充日常生活状态。',
'推断题要保留情态强度。possible 不能替换成 proven、only 或 certainly；个人解释不能升级为实验因果。',support='inference')
add(8,'逻辑关系','Which contrast about regret does the author make?', ['People regret inaction only when they are young.','Long-term regret is always caused by self-sacrifice.','Action and inaction cause identical regrets at every stage.','Action tends to be regretted in the short term, inaction in the long run.'],3,
'两句用 In the short term / In the long run 和 however 对照 action 与 inaction。后面虽讨论牺牲，却未声称全部长期后悔都由牺牲造成。',['A 文中没有 young 的年龄限制，混淆时间尺度与年龄。','B always 和单一成因超出文本。','C identical 抹除了明确对照。','D 同时保留时间与行为的正确配对。'],['In the short term, people regret action, like saying or doing something stupid.','In the long run, however, people regret inaction, like not saying “I love you” or not going back to school.'],['inaction'],
'In the short term 与 In the long run 是对应状语；like 后接 saying / doing / not saying 等动名词短语举例。however 作插入连接副词表达转折。',
'逻辑关系题建议画两列：短期—行动；长期—不行动。干扰项常交换配对或把倾向改为绝对因果。')
add(8,'同义改写','What risk of prioritising self-sacrifice is described?', ['People may lose contact with their own wishes and feel less authentic.','People necessarily become unwilling to help others.','People can no longer remember their childhood families.','People always gain clearer personal ideals.'],0,
'作者肯定牺牲值得赞赏，同时指出它可能使人忽略自身欲望和理想，直到生活不再真实。may / can 保留了风险而非必然。',['A lose contact with wishes 是 lose sight of desires 的同义改写，且保留 may。','B 并未说不愿帮助别人，反而牺牲正在服务别人。','C lose sight of 是忽略，不是失去记忆。','D always gain 与风险方向相反。'],['Self-sacrifice is admirable, to be sure, but prioritizing it can lead people to lose sight of their own desires and ideals until their lives no longer feel authentic.'],['authentic'],
'Self-sacrifice is admirable 是让步式肯定，but 引出限制；prioritizing it 是动名词主语；lead people to... 中不定式补足结果，until 从句表示发展的界限。',
'同义题保留 can 的可能性，且不要把 lose sight of 逐词解释成视力或记忆问题。')
add(9,'作者意图','What role does the account of Oliver Sacks play here?', ['It proves that depression is necessary for a valuable life.','It offers an example of an adventurous, experientially rich life despite hardship.','It shows that professional boundaries never matter.','It establishes that Sartre conducted research on Sacks.'],1,
'Sacks 的困难与仍然充满冒险好奇的人生并置，呈现另一种值得欣赏的生活。不是倡导抑郁，也不是报告 Sartre 的实验。',['A despite 不等于 necessary：逆境不是必要条件。','B 对应 Yet / even though 与 rich、adventure、curiosity。','C challenged boundaries 不等于所有边界无价值。','D would have approved 是作者假设的哲学评价，不是研究事实。'],['Yet, even though he had some tough years, his life was full of adventure and curiosity, challenged professional boundaries, and was deeply experientially and emotionally rich—it was an authentic life, the kind that Sartre would have approved of.'],['authentic'],
'even though 是让步从句；主语 his life 后有 was full、challenged、was rich 的并列。would have approved of 是对假想评价的过去虚拟表达，不能理解为真实发表的评论。',
'作者意图题看例子服务的概念。人物经历用于展现丰富性；不要把传记描述当作必要条件或临床建议。',ctx='all')
add(10,'主旨','Which feature is central to the author’s definition of a psychologically rich life?', ['Unchanging routines that remove every surprise.','A constant feeling of personal contentment.','Diverse and interesting experiences that change one’s perspective.','Self-sacrifice as the single measure of a good life.'],2,
'定义句的核心是 diverse, unusual, interesting experiences that change your perspective。后面的曲折、多样与复杂均围绕此展开。',['A 与 twists and turns、unusual 相反。','B 前文已说 happiness/contentment 不能充分概括。','C 准确概括定义句。','D 把被指出不足的单一维度变为唯一定义。'],['A psychologically rich life is a life filled with diverse, unusual, interesting experiences that change your perspective;'],['perspective'],
'主干是 A psychologically rich life is a life。filled with... 为过去分词短语修饰 life；that change your perspective 是定语从句，that 指向 experiences，故 change 为复数形式。',
'定义主旨题定位 X is...，然后检查定语从句，它常提供区分同类概念的关键限定。',ctx='all')
add(11,'作者意图','Why does the author compare psychological richness to dark chocolate?', ['To recommend replacing sweet food with bitter food.','To claim that unpleasant experiences are always preferable.','To show that richness is a measure of food quality alone.','To illustrate surprise, complexity and a mixture of qualities.'],3,
'黑巧克力同时可甜、苦、咸，产生意外与复杂深度；Likewise 将这些性质映射到经历，不是营养建议。',['A 把概念类比误当饮食建议。','B 原文是多种性质，而非越不愉快越好。','C 后文明确将 richness 用于人生经历。','D 与 surprise、intensity、complexity、depth 对应。'],['It is sweet but also bitter, or even salty.','It keeps you surprised, and it has heightened intensity, complexity, and depth.','Likewise, a psychologically rich experience is different from a typical experience; there is something unexpected and powerful.'],['likewise'],
'sweet but also bitter 用 but also 连接不同味觉；Likewise 是类比过渡词。there is something unexpected and powerful 是存在句，形容词后置修饰不定代词 something。',
'类比题区分用来说明的对象与说明的概念。巧克力味道是工具，复杂经历才是作者的论述目标。',ctx='all')
add(13,'细节','What contribution is attributed to Ed Diener and his students?', ['Helping establish happiness as a legitimate topic of scientific study.','Replacing all research on hope and optimism with autobiography.','Creating the eudaimonic approach in 1989.','Proving that psychological richness and happiness are identical.'],0,
'1980 年代的一系列 subjective well-being 论文，推动幸福研究在心理学内获得科学地位。后面的积极心理学与 Ryff 的模型需区分归属。',['A 对应 legitimizing the scientific study of happiness。','B 没有 replacing all，传记也不是此处方法。','C 1989 的替代模型归于 Carol Ryff，不是 Diener。','D 本段没有这一同一性结论。'],['Ed and his students, such as Randy Larsen and Bob Emmons, went on to publish a series of papers on subjective well-being throughout the 1980s, legitimizing the scientific study of happiness within psychology.'],['legitimizing'],
'Ed and his students 为并列主语；went on to publish 表示接着做；legitimizing... 为分词结果补充。such as 引入学生例子，不改变主干。',
'人名归属题建立人物—时间—贡献配对；不要把相邻段的 Ryff 1989 与 Diener 1984/1980s 交换。',ctx='all')
add(14,'同义改写','How does the passage distinguish the eudaimonic and hedonic approaches?', ['The former concerns money; the latter concerns social status.','The former is linked to a meaningful life; the latter to a happy life.','The former rejects personal growth; the latter requires self-sacrifice.','The former was developed by Diener; the latter by Ryff.'],1,
'原文用破折号给出简要解释：eudaimonic—meaningful；hedonic—happy。不是说两者完全没有重合。',['A 钱与地位不是此处两种方法的定义。','B 对应两个破折号后的概括。','C Ryff 模型包含 personal growth，而 self-sacrifice 非此句对 hedonic 的定义。','D 把人物归属颠倒。'],['the “eudaimonic approach”—a meaningful life, in short','the “hedonic approach”—a happy life.'],['autonomy'],
'has come to be called 使用现在完成时加被动不定式，描述逐渐形成的命名。in contrast to 引出对照；破折号后的名词短语解释术语。',
'术语题可优先看同位解释与破折号。保留两组映射，不要因同属 good life 就混同或倒置。',ctx='all')
add(15,'主旨','What is the best summary of the debate described in this paragraph?', ['Researchers unanimously deny that happiness and meaning overlap.','Every study shows that breaks are more meaningful than work.','Findings and interpretations differ about the distinction and overlap between happiness and meaning.','The debate has established epigenetic differences beyond dispute.'],2,
'段内先给两者不同的例子，再以 However 转到很强重叠与研究者不同立场。主旨应保留分歧，不能把某一派变成全体结论。',['A 后半段正强调 overlap，unanimously 与文本相反。','B 更快乐与更投入是不同维度，且 every study 过度绝对。','C 总结不同发现与解释，而不偏取一方。','D Some researchers even claimed 后还有对立发现，不是 beyond dispute。'],['However, other researchers found that almost all people who say they are happy tend to also say that their lives are meaningful, and vice versa.','The overlap between hedonic and eudaimonic well-being is so great that some researchers argue that they are virtually the same thing.','Others argue that both happiness and meaning in life are so important that there is no point debating which is more important.'],['overlap'],
'who say... 为修饰 people 的定语从句；so great that... 为程度—结果结构。some researchers / other researchers / Others 指不同观点群体，须逐一归属。',
'多观点主旨题跟踪 however、some、others 等路标。单项研究和研究者声称不能自动代表领域共识。',ctx='all')
add(16,'作者意图','What does the comparison with nature, nurture and growth mindset illustrate?', ['That genetic explanations of intelligence should replace all others.','That happiness is irrelevant once richness is considered.','That psychological richness determines intelligence.','That a third concept can broaden a discussion framed by two dimensions.'],3,
'作者认同幸福与意义都重要，类比自然与养育同样都重要，再用 growth mindset 示范第三概念如何扩展视野。不是声称心理丰富性决定智力。',['A 原文说 both nature and nurture are important。','B 作者明确两者都重要。','C 把类比两侧概念混合为不存在的因果命题。','D 抓住二元讨论引入第三维度的共同结构。'],['My own take is that happiness and meaning are both important.','In the end, both nature and nurture are important. Then Carol Dweck proposed and popularized a third idea: the growth mindset.'],['adequate','mindset'],
'My own take is that... 中 that 引导表语从句。whether we believe... 是嵌入的选择疑问内容。Then 表叙述推进，a third idea 与前面的两方对照。',
'类比推理应匹配关系而非混用变量：两种因素均重要—第三概念拓宽讨论；不能推出心理丰富性导致智力提升。',ctx='all')
add(17,'细节','What effect did the son’s comment have on the author?', ['It encouraged him to repair the window and improve his practical skills.','It persuaded him that only professionals can learn new skills.','It made him abandon the idea that mindsets can change.','It caused his wife to hire a different handyman.'],0,
'My son’s suggestion motivated me to fix the window and become a better handyman 明示建议后的行动与改善。',['A 对应 fix the window / become a better handyman。','B 与 You can get better 及作者亲自尝试相反。','C 这是概念扩展思考的例子，不是放弃。','D 原文未报告妻子另请工人。'],['My son’s suggestion motivated me to fix the window and become a better handyman'],['motivated','mindset'],
'My son’s suggestion 是名词所有格主语，motivated 是过去时谓语。motivate somebody to do 中两个并列不定式共享 to：fix... and become...。',
'细节题分开初始反应与最终行为。We should just hire someone 是起初想法；问题询问 comment 的 effect，须读到 motivated。',ctx='all')
add(18,'同义改写','What does the batting-average comparison suggest about happiness?', ['Only rare, spectacular achievements have lasting value.','Frequent small positive interactions can matter more than occasional major successes.','The size of each pleasant event is the only important factor.','Happiness remains constant once a major goal is reached.'],1,
'作者用安打频率作比，随后 In other words 明确解释：频繁的小型愉快社交比偶尔的大晋升更快累积长期幸福。',['A 与 frequent small 相反。','B 准确保留频率与重大但偶发事件的对照。','C only size 偷换 frequency 为强度。','D rises and falls / changes 与 constant 相反。'],['In other words, frequent small, pleasant social interactions add up to long-term happiness more quickly than occasional big promotions.'],['frequency'],
'frequent small, pleasant social interactions 是复数主语，add up to 为谓语短语。more quickly than 构成速度比较，不是在否定大晋升有任何价值。',
'同义改写优先定位 In other words。比较级只表示相对差异，不能扩大为 only、never 或零作用。',ctx='all')
add(19,'语境词义','What is “the snag” in the discussion of happiness?', ['Success is impossible in a prosperous life.','Sporting results cannot be measured.','Happiness fluctuates and therefore offers insecure support.','William James rejects all pleasant experiences.'],2,
'snag 后立即解释 changes over time，并用季节不同表现说明波动，后引 James 谈不稳固的锚定。',['A impossible 无依据，原文说健康繁荣的人生仍夹杂危险。','B 棒球是类比，未否定测量。','C 对应 changes over time 与 insecure anchorage。','D 引文用于说明不稳定，不等于拒绝一切愉悦。'],['The snag is that happiness—like the batting average—changes over time; one season you hit well; another season not so well.'],['snag'],
'The snag is that... 中 that 引导表语从句。like the batting average 是破折号隔开的插入比较；分号后的两组 season 状语具体说明变化。',
'语境词义题用紧接的解释，而不是字典中所有可能义项。snag 在此是概念的障碍或局限，并非钩住东西的物理动作。',ctx='all')
add(20,'语境词义','In the phrase “boils down to”, what is the author doing?', ['Describing a process for removing negative emotions.','Explaining how a song was produced.','Claiming that every effort produces a clear legacy.','Reducing a complex idea to its central question.'],3,
'boils down to whether... 把人生意义这个复杂问题概括为生活有没有一个 point。后文提供奉献、影响与失去指向的例子。',['A 没有烹煮或移除情绪的过程。','B 歌曲是后面的例子，不是该短语含义。','C when efforts are not making a clear difference 明确允许看不到影响。','D 对应把意义归结到一个核心问题。'],['Meaning in life, on the other hand, boils down to whether your life has a “point.”'],['boils'],
'Meaning in life 是主语；boils down to 为固定动词短语，to 是介词；whether your life has a point 为介词后的名词性从句。',
'短语题注意搭配整体。to 在这里并非不定式标记，其后是 whether 从句；后续例子帮助锁定“归结为”。',ctx='all')
add(21,'有限推断','What does Tolstoy’s example suggest within this discussion?', ['External success and a loving family do not necessarily secure a sense of meaning.','Only people with financial losses question their lives.','Praise always prevents an existential crisis.','Tolstoy’s crisis was experimentally caused by writing novels.'],0,
'作者先陈述幸福、有产出与没有明显损失，再以 Yet 描写意义危机。由此可有限推断外在成功不必然保障意义感。',['A 保留 do not necessarily 的适当强度。','B without any obvious loss 直接反驳这一必要条件。','C 引述说 loaded with praise 仍无法赋予意义。','D 传记引文不是实验，写小说也未被证明是原因。'],['Tolstoy was happy and productive.','Yet, without any obvious loss, he had a sudden existential crisis at about the age of fifty','And yet I could give no reasonable meaning to any actions of my life.'],['precariousness'],
'without any obvious loss 是介词短语，排除显而易见损失的伴随条件。Yet 与 And yet 强调反预期；could give no... 表示当时无法赋予合理意义。',
'例证推断不做因果升级。成功与危机并存足以反驳“成功必有意义”，却不足以证明成功导致危机。',ctx='all',support='inference')
add(22,'主旨','How is psychological richness contrasted with happiness in the career-home-runs analogy?', ['Richness depends on winning every single game.','Richness accumulates through experiences rather than tracking a changing overall feeling.','Richness can be measured only in financial earnings.','Richness erases all earlier experiences after each new event.'],1,
'幸福比作随每场比赛变化的打击率；丰富性比作职业生涯全垒打总数，关键在 adds up 与经历的累积。',['A every game 是幸福类比的变化单位，不是丰富性必须全胜。','B 保留累积与当前波动指标的区别。','C 金钱是物质财富的类比，不是心理丰富性的唯一计量。','D 与累积相反。'],['Psychological richness is different from happiness and meaning in the sense that it is not about an overall feeling of where life is going or what the point of your life is, but about an experience, or more precisely the accumulation of experiences over time.','If happiness is like the batting average that changes with every game, psychological richness is more like the total number of career home runs: it adds up.'],['accumulation','quantified'],
'not about... but about... 是同层次对照。If 从句建立类比前提；that changes with every game 修饰 batting average；冒号后 it adds up 点出比喻对应特性。',
'类比主旨题抓统计指标性质：比率随时变动，总数累积。不要额外推出所有经历等价或任何痛苦都有益。',ctx='all')
add(23,'细节','What does the author acknowledge about a psychologically rich life?', ['It guarantees more security than any other life.','It is suitable only for people who are already happy.','It often lacks the comfort and security found in a happy or meaningful life.','It requires giving up every form of meaning.'],2,
'安全网一句承认丰富人生的未知可能缺少另两种生活的舒适安全。作者同时说三种维度可以共存。',['A guarantees more 与 often lacks 相反。','B suits the curious 不等于 only already happy。','C 是 safety net 句的准确概括，保留 often。','D 与后面 some people 三者兼有相反。'],['The comfort and security of a happy or meaningful life provide a safety net that a psychologically rich life, with all its unknowns, often lacks.'],['safetynet'],
'The comfort and security 是复数主语，provide 作谓语。that...often lacks 为修饰 safety net 的定语从句，其中 that 作 lacks 的宾语；with all its unknowns 为插入补充。',
'细节题把长定语从句还原：a rich life often lacks the safety net。保留 often，不能把作者的承认放大为必然危险或无法幸福。')
add(23,'同义改写','What does “our lives are not zero-sum games” imply in this passage?', ['A good life must choose richness instead of happiness.','The three dimensions are always identical.','Meaning is possible only after all curiosity disappears.','Happiness, meaning and richness can coexist in a person’s life.'],3,
'not zero-sum 之后直接说 some people lead happy, meaningful, and psychologically rich lives。三者可以共存，而非必须只选其一。',['A 原文明说不必 choose a single path。','B 可以共存不等于概念相同。','C 没有意义以好奇心消失为条件。','D 对应 some people 同时拥有三种品质。'],['Thankfully, our lives are not zero-sum games in which we must choose a single path to a good life; some people lead happy, meaningful, and psychologically rich lives.'],['zerosum'],
'in which 引导修饰 games 的定语从句。分号把否定单一路径与具体共存例子连接；happy, meaningful, and psychologically rich 为三个并列形容词。',
'抽象短语题读分号后的解释。not zero-sum 表可兼有，不等于人人已经兼有，也不等于三种维度没有差异。')
add(24,'有限推断','What can be inferred about people who choose to stay?', ['They may still gain interest and resilience through psychological richness.','They cannot experience psychological richness without moving away.','They must adopt the author’s pattern of repeated migration.','They are guaranteed a completely regret-free life.'],0,
'作者直接说对 stay 的人，丰富性会增加兴趣与韧性。因此不能把丰富性等同迁居，也不能保证无遗憾。',['A 是本段对留下者的积极可能性，范围有限。','B 与 For those who stay...add 相反。','C 没有必须迁移的要求。','D 此处没有 guaranteed，前文也保留 at least fewer regrets 的限制。'],['For those who stay, psychological richness will add a new dimension of interest and resilience to life.'],['resilience'],
'For those who stay 是介词短语，who stay 修饰 those。主句 psychological richness will add...；a new dimension 后 of interest and resilience 具体说明维度内容。',
'推断检查必要条件：作者明确谈 stay，便不能附加“必须离开家乡”。把文中承诺升级到 completely regret-free 也无依据。',ctx='all',support='inference')
add(25,'作者意图','What is the purpose of the questions at the end of this chapter?', ['To claim that indirect experiences have already been ruled out.','To preview issues that the rest of the book will explore.','To replace the earlier definition with a financial one.','To demonstrate that no research on richness exists.'],1,
'问题串涵盖人物、概念区别、亲历与间接体验、益处与方法，最后 This book will venture deeply into these questions 表明预告后文。',['A 是否间接体验算数是待探讨问题，不是已排除。','B 由最后一句直接支持。','C 未将概念改成财富定义。','D 提问不表示没有研究，作者已介绍研究方向。'],['Do you need to accumulate experiences firsthand, or do vicarious experiences count as well?','This book will venture deeply into these questions.'],['vicarious'],
'Do you need... or do... 是选择问句，两侧各自保留助动词。will venture 是将来时，指本书后续论述；these questions 回指整组问题。',
'段末功能题用最后一句锁定作用。问题形式不等于否定答案，尤其不能把 or 的一端当作作者已下定论。',ctx='all')
# Batch 2: additional Chapter 2 source-specific questions, not placeholders for other chapters.
add(26,'观点归属','Who is explicitly associated with the idea that happiness is “the ultimate goal of goals”?', ['William James.','Ed Diener.','Aristotle.','The survey respondents.'],2,
'according to Aristotle 清楚标出这句话的观点来源；随后 James 的问题、Diener 的调查是其他材料。',['A James 出现在下一句，不是这句 ultimate goal 的归属。','B Diener 与后面的国际调查相关。','C according to Aristotle 明示归属。','D 调查对象提供重视程度，不是该表述的署名来源。'],['Happiness is the ultimate goal of goals, according to Aristotle.'],['ultimate'],
'Happiness is... 为系表结构；according to Aristotle 是观点来源状语。保留 according to 有助于避免把哲学主张转述为研究结果。',
'观点归属先定位 according to，而非选最近出现的研究者。哲学判断与后续样本调查属于不同证据类型。')
add(27,'主旨','What irony introduces the discussion of the happiness trap?', ['Happy people never help others.','Public happiness always reflects inner experience.','No one sees happiness as a worthwhile goal.','Pursuing happiness blindly can sometimes produce unhappiness.'],3,
'The irony is that... 直接点题；作者没有否认幸福有价值，而是质疑盲目追求和持续表现快乐的压力。',['A 与前文 more prosocial 相反，且 never 绝对化。','B 后面 precisely 区分外在表现与内在感受。','C 先前称 worthy goal，并非所有人否定。','D 保留 blind pursuit 与 sometimes 的限定。'],['The irony is that our blind pursuit of happiness sometimes leads to unhappiness.'],['undue'],
'The irony is that... 中 that 为表语从句；our blind pursuit 是单数主语，leads 作谓语；sometimes 限定发生频率，不能删去后读成普遍必然。',
'段首主题句常提供答案。确认频率副词 sometimes，避免选项里的 always、never 对原文做绝对化改写。')
add(30,'细节','What association was found in the American college students’ responses?', ['Happiness was often connected with personal achievement.','Happiness was defined exclusively as inherited wealth.','Happiness was viewed as unrelated to success.','Students agreed that sadness was a medical diagnosis.'],0,
'段落两项研究的回应把 happiness 与 reward、succeeding、victory 联系起来，最后用 equate happiness with personal achievement 概括。',['A 与结句一致，保留样本范围为美国大学生。','B exclusively 与 inherited wealth 均未出现。','C 与 strong association 相反。','D 没有诊断调查，不可把文化概念变成医学结论。'],['The earlier findings were replicated: American college students tend to equate happiness with personal achievement.'],['equate'],
'冒号后进一步解释 replicated 的发现；tend to equate 表倾向，equate A with B 为固定搭配，不是所有人绝对一致。',
'调查细节题保留样本与倾向范围。American college students 不等于所有国家所有年龄群体。',ctx='all')
add(32,'同义改写','What is the affective forecasting error described in the passage?', ['Underestimating the value of every possible promotion.','Predicting both success-related joy and failure-related distress as greater than they turn out to be.','Accurately predicting lasting happiness from every success.','Expecting failure to make people happier than success.'],1,
'作者说我们高估成功带来的幸福，也高估失败带来的不幸福。两侧都是情绪影响的高估，不是预测失败会胜过成功。',['A underestimating 把方向颠倒，every 扩大范围。','B 同时保留成功和失败两侧的预测偏高。','C 文中重点正是预测不准确。','D 高估失败的痛苦不等于预计失败比成功更快乐。'],['Decades of research on the “affective forecasting error” suggest that we tend to overestimate the happiness that our success will bring about, while also overestimating the unhappiness that our failure will generate.'],['overestimate'],
'research suggest 后接 that 宾语从句；that our success will bring about 修饰 happiness，that our failure will generate 修饰 unhappiness。while also overestimating 表同时存在的另一面。',
'双向效应题检查方向：success—happiness 高估；failure—unhappiness 高估。干扰项可能只反转一个动词或一侧情绪。')
add(32,'细节','How did former assistant professors who were denied tenure compare with current professors’ expectations?', ['They were exactly as devastated as predicted.','They refused to discuss their happiness.','They were happier than the current professors had imagined.','They were guaranteed to become happier than all tenured professors.'],2,
'结句说被拒绝终身教职的人比现任助理教授想象的快乐得多。比较对象是预测值，不是得到终身教职者。',['A 与 far happier than imagined 相反。','B 研究者已经访谈他们，没有拒绝交流之说。','C 正确保留 happier 的比较基准。','D 偷换比较对象为所有获得终身教职者，还添加 guaranteed。'],['The good news is that those who were denied tenure were far happier than the current assistant professors imagined.'],['tenure'],
'those who were denied tenure 中 who 从句限定群体。were denied 是被动；far 修饰比较级 happier，than 后省略了重复的情绪程度内容。',
'比较题先划基准：than ... imagined，比较实际感受与预期，不能改为拒绝与通过两组之间的排名。',ctx='all')
add(33,'主旨','Which pattern is emphasised as a source of long-term happiness?', ['One sufficiently intense personal achievement.','Avoiding every form of social interaction.','Frequent public recognition of individual success.','Repeated small positive events and close relationships.'],3,
'作者明确 frequency, not intensity，并把关系成功与个人成功对照。选择应兼顾频繁小事与亲密关系。',['A 正是段落反驳的 big win 观念。','B 与 coffee with your best friend、close relationships 相反。','C 虽有 frequent，但把亲密关系换成公众认可。','D 准确概括小型积极事件、频率和关系。'],['Happiness is the frequency, not the intensity, of positive events.','Relatedly, studies show that happiness is the product of close relationships rather than personal accomplishments.'],['intensity'],
'not the intensity 为对照插入，of positive events 同时限定 frequency / intensity；rather than 连接两种来源，突出作者强调的关系侧。',
'主旨不能只匹配一个同词 frequent；还要核对事件类型。公众成就不等于亲密关系里的小型积极互动。',ctx='all')
add(35,'细节','What does the passage report about replications of the pen-in-the-mouth experiment?', ['Some attempts failed to replicate it, while others succeeded.','All attempts confirmed it without exception.','No researchers ever tried to repeat it.','The author says replication is irrelevant to interpretation.'],0,
'Some failed... though others were able... 清楚表明重复验证结果混合。不能把最初显著结果说成所有后续一致。',['A 同时保留失败和成功复现。','B all / without exception 与 Some failed 冲突。','C 明确有重复研究。','D 段落提及复现限制，未说不相关。'],['Some failed to replicate the original findings, though others were able to replicate them.'],['replicate'],
'Some / others 指不同研究尝试者；though 引导让步 / 对照，were able to replicate 表成功做到。them 回指 findings。',
'科学证据题区分原始实验与复现。保留混合结果，避免用 all、none 强化为文中没有的共识。',ctx='all')
add(37,'逻辑关系','Why is the impossible-anagram experiment discussed?', ['To prove that everyone lacks language ability.','To show that pressure to be happy can worsen reactions to the same failure.','To establish that the control group solved all the anagrams.','To recommend failure as the only route to happiness.'],1,
'everyone failed 使失败结果相同；压力组对失败反刍更多，用于说明应该快乐的信念可能让同样失败更糟。',['A impossible 的任务设计不能推断所有人语言能力不足。','B 对应 pressured 组更多 ruminated 与末句 same failure。','C control 组也失败，并未解开所有字谜。','D 实验关注压力和反应，不是建议追求失败。'],['The anagrams were impossible to solve, and everyone failed.','The participants who were pressured to be happy ruminated about the failure more than the participants in the control condition, where there was no pressure to be happy.'],['ruminated'],
'who were pressured... 修饰 participants；where... 修饰 control condition。more than 对比反刍程度，任务结果 everyone failed 是两组共同背景。',
'实验逻辑先区分自变量（快乐压力）与共同条件（均失败），再看因变量（反刍）。不可把设计为不可能完成的任务解释成能力差异。',ctx='all')
add(38,'有限推断','Which conclusion stays within the evidence of the international comparison?', ['Every American feels more pressure than every Japanese person.','Belief in luck has been proved to remove all sadness.','Countries associating happiness more with luck appeared to show less pressure to be happy.','Cultural associations were experimentally assigned to entire nations.'],2,
'on average、appears、associated 限定结论：这是平均与文化联系的比较，不是每个人的排序或国家随机实验。',['A every 偷换平均层次。','B remove all sadness 与相关比较完全不同。','C 保留 countries、association 和 appeared 的谨慎程度。','D 片段没有国家层面的随机分配。'],['Interestingly, in the countries where happiness is more strongly associated with good luck and fortune than personal accomplishments (e.g., Japan and Germany), there appears to be less pressure to be happy.'],['associated'],
'where... 修饰 countries；more strongly...than 比较文化联系强度。there appears to be 表谨慎观察，不能改成 there must always be。',
'推断题保留聚合层级与证据强度。国家平均差异不是任意两个人的确定比较，相关关系也不能直接改写成因果。',support='inference')
add(45,'同义改写','What does the “psychological immune system” analogy highlight?', ['That active coping methods are always ineffective.','That negative moods should never be discussed.','That biological viruses directly cause all unhappiness.','That people have a natural capacity to recover from negative emotional states.'],3,
'作者先承认主动策略有效，再指出人类还有自然恢复能力。免疫系统是类比，不是把所有不快乐诊断为病毒感染。',['A Although...effective 明确承认主动策略。','B 片段未禁止讨论情绪。','C 把类比当成生物病因。','D 与 natural ability to heal and recover 对应。'],['Although active emotion regulation strategies such as reappraisal and self-distancing are effective, humans do have a natural ability to heal and recover from negative mood states.'],['reappraisal'],
'Although 引导让步；humans do have 用 do 强调拥有自然能力；to heal and recover 为修饰 ability 的并列不定式。',
'类比题先识别对应属性：自动恢复能力。不要把类比对象的全部生物性质搬到心理概念中，也不要忽视 Although 的让步。',ctx='all')
add(48,'作者意图','What explains the UVA–Cornell example in the passage?', ['The number of imagined alternative outcomes, rather than a claim that one university is inherently better.','A controlled demonstration that tuition alone determines happiness.','A rule that all students should apply to ten schools.','Evidence that every Cornell student regrets enrolling.'],0,
'作者明确排除院校自身高下，强调备选带来的反事实。情境例子用于讨论决策方式，并非给两所大学永久排名。',['A 对应 nothing to do with UVA vs. Cornell 与 alternative options。','B tuition 在前段例子出现，但不是此处解释，更非 alone 因果。','C 十校是 maximizer 情境，不是给所有人的规则。','D every Cornell student 严重扩大了情境研究范围。'],['It has nothing to do with UVA vs. Cornell, but rather with the notion of alternative options.','The Cornell student applied to ten schools, which means they had nine counterfactuals.'],['counterfactuals'],
'nothing to do with A, but rather with B 表排除一种解释、转向另一种。which means... 为补充说明从句；they 回指情境中的学生，不能泛化成整个学校。',
'作者意图题优先看作者明确的排除与解释。院校专名可作定位，但不能因专名抢眼就把思维方式研究误当择校榜单。',ctx='all')
add(52,'有限推断','What limitation of the satisficer mindset does the author identify?', ['It can never be useful in everyday decisions.','Contentment with the status quo can discourage necessary challenges and growth.','It necessarily makes all people financially poorer.','It always creates more counterfactuals than maximising.'],1,
'作者承认日常使用 satisficer，但指出满足现状可能阻碍必要挑战与个人成长。此处是条件性的不足，不是否定全部价值。',['A 文中说 I actively use it，never 相反。','B 对应 content with status quo → discourages...growth，保留 can。','C 原文没有财富必然下降。','D 与前面例子的反事实数量方向相反，也没有 always。'],['But this mindset can have a dark side as well.','For instance, it makes you content with the status quo, which in turn discourages you from embracing necessary challenges and personal growth.'],['statusquo'],
'which in turn... 为非限制性定语从句，对前面的满足现状状态作结果补充；discourage somebody from doing 中 from 后用动名词 embracing。',
'立场题同时保留肯定与限制。can have a dark side 不能扩大成从无价值，也不能缩成只有好处。',ctx='all',support='inference')
# Append separately saved editorial batches without renumbering existing questions.
runpy.run_path(str(ROOT/'scripts/batches/chapter02-expansion.py'),init_globals=globals())
sentence_order={s['id']:i for i,s in enumerate(b['sentences'])}
out.sort(key=lambda q:min(sentence_order[sid] for e in q['evidence'] for sid in e['sentenceIds']))
# Reviews record actual visual comparison, independently of question coverage.
reviews=json.loads((ROOT/'source/reviews.json').read_text(encoding='utf-8')) if (ROOT/'source/reviews.json').exists() else []
reviewed={r['paragraphId'] for r in reviews if r['status']=='visual-proofread'}
for r in reviews:
 if r.get('reviewedTextSha256'):
  p=next(p for p in b['paragraphs'] if p['id']==r['paragraphId'])
  assert hashlib.sha256(p['text'].encode()).hexdigest()==r['reviewedTextSha256'], ('Stale visual review',p['id'])
for s in b['sentences']:s['review']='visual-proofread' if s['paragraphId'] in reviewed else 'candidate'
(ROOT/'public/data/book.json').write_text(json.dumps(b,ensure_ascii=False,indent=2),encoding='utf-8')
(ROOT/'public/data/questions.json').write_text(json.dumps(out,ensure_ascii=False,indent=2),encoding='utf-8')
catalog_path=ROOT/'src/data/passage-translations.json'
catalog=json.loads(catalog_path.read_text(encoding='utf-8'))
previous={(e['questionId'],e['passage']):e for e in catalog['entries']}
for q in out:
 key=(q['id'],q['passage'])
 if key in previous:
  assert previous[key]['passage']==q['passage'], ('Review translation after content change',q['id'])
 else:
  assert q.get('translation'), ('Missing full-passage translation',q['id'])
  catalog['entries'].append(dict(questionId=q['id'],passage=q['passage'],sourceFingerprint=q['fingerprint'],translation=q['translation']))
catalog_path.write_text(json.dumps(catalog,ensure_ascii=False,indent=2),encoding='utf-8')
legacy_path=ROOT/'source/archive/questions-v1.json'
legacy=json.loads(legacy_path.read_text(encoding='utf8'))
assert {q['id']:q['fingerprint'] for q in out}=={q['id']:q['fingerprint'] for q in legacy}, 'Preserve legacy revisions; author new short-unit revisions explicitly'
runpy.run_path(str(ROOT/'scripts/prepare-short-reading.py'),run_name='__main__')
print(f'Wrote {len(out)} legacy-compatible short questions. No full coverage claim.')
