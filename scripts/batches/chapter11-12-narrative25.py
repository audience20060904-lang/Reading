"""25 individually authored exercises for frozen targets, PDF pages 130-136.
Preserve printed English, source positions and all previously published questions.
"""
from pathlib import Path
import json,hashlib
ROOT=Path(__file__).resolve().parents[2]
load=lambda p:json.loads((ROOT/p).read_text(encoding='utf8'))
b=load('public/data/book.json');plan=load('public/data/reading-plan.json');targets=load('source/short-questions/batch033-targets.json')['targets']
ss={s['id']:s for s in b['sentences']};pp={p['id']:p for p in b['paragraphs']};out=[]
def add(i,kind,prompt,options,answer,prompt_zh,options_zh,analyses,quotes,word,meaning,context,example,collocations,translation,support='explicit'):
 t=targets[i-1];u=next(u for u in plan['units'] if u['id']==t['readingUnitId']);group=[ss[sid] for sid in u['sentenceIds']];p=pp[u['paragraphId']];text=p['text'][group[0]['start']:group[-1]['end']]
 assert hashlib.sha256(text.encode()).hexdigest()==t['passageSha256'];evidence=[]
 for quote in quotes:
  offset=text.find(quote);assert offset>=0,(i,quote);start=group[0]['start']+offset;end=start+len(quote);touching=[s for s in group if s['start']<end and s['end']>start]
  evidence.append(dict(quote=quote,sentenceIds=[s['id'] for s in touching],sources=list({(r['pdfPage'],r['block']):r for s in touching for r in s['sources']}.values())))
 assert word.lower() in text.lower(),(i,word)
 out.append(dict(id=t['questionId'],version=1,readingUnitId=u['id'],chapterId=u['chapterId'],sectionId=u['sectionId'],paragraphId=u['paragraphId'],sentenceIds=u['sentenceIds'],passage=text,prompt=prompt,options=options,answer=answer,type=kind,promptZh=prompt_zh,optionsZh=options_zh,analyses=analyses,evidence=evidence,vocabulary=[dict(word=word,meaning=meaning,context=context,example=example,collocations=collocations)],translation=translation,support=support,editorialStatus='完整PDF130–136原页视觉核对含章末132与章首133。瑞典2021两次调查为自报比较，保留反向因果；谣言不作事实、暴力明确谴责，韧性most/common不作人人无创伤。既有单元q-c11-062原文仅起).，为131页七転八起括号因换行提取的末字续片，保留既有ID/范围并编来源续接辨识题，明确非独立英文段或最终人工句界，不补造英文或新主张；词汇特记日语末字。James画作是哲学比喻，保留不幸受约束。Bush为作者可选叙述示范，probably/could不作客观证实；Tim Wilson区别Anne Wilson。父母回顾多年龄评分非几十年追踪；本科纵向6.35原九月/6.05当下十一月/5.74回忆九月分开，实际记录指原自评不是客观能力。末段整段审阅含后续未配题材料，不宣称逐句直接证据全覆盖。'))







add(1,'细节','What did the April 2021 Swedish questionnaire find?',
 ['Participants were randomly assigned to infection.','Those previously infected reported greater psychological richness.','All respondents reported identical richness.','Only hospital records were collected.'],1,
 '2021年4月瑞典问卷发现什么？',['随机分配感染。','既往感染者自报心理丰富更高。','所有人丰富度相同。','只收医院档案。'],
 ['A 是匿名问卷，非随机感染。','B reported more...than 明示自报组间差异。','C more 比较方向清楚。','D 问卷问感染状态与主观人生感受，非只档案。973是受访人数，不证明感染导致丰富。'],
 ['those who had had COVID-19 reported more psychological richness than those who had not been infected.'],
 'anonymously','匿名地','不具名填写问卷，不等于研究随机分组','The respondents completed the questionnaire anonymously.',['fill out anonymously','an anonymous questionnaire'],
 'COVID-19这种异常经历增加心理丰富吗？Micael Dahlen与Helge Thorbjørnsen直接检验此问。2021年4月第二周，973名瑞典人匿名问卷，报告COVID状态与是否觉得人生心理丰富。曾患病者比未感染者自报更多心理丰富。')

add(2,'同义改写','Which statement preserves the comparison about erasing pandemic time?',
 ['Previously infected respondents were less inclined to erase that period.','Every infected person wanted to erase the period.','The groups expressed equal regret.','Less regret proves there was no suffering.'],0,
 '哪项保留抹去疫情时段的比较？',['曾感染者更不倾向抹掉该时期。','每位感染者都想抹掉。','两组后悔一样。','较少后悔证明从无痛苦。'],
 ['A less likely...erase 对应较低倾向。','B 把群体较少变每人都要，且方向相反。','C regretted less 不是相等。','D 后悔与痛苦不同，不能推为没有伤害。'],
 ['less likely to say that they would like to erase the pandemic time period from their life'],
 'erase','抹去；删除','假设从人生中除去一段时光的反事实偏好','She would not erase the difficult period from her life.',['erase a time period','erase from one’s life'],
 '曾患COVID-19的受访者，也比未患者更少说想从人生抹掉疫情时期。换言之，患过者比未患者后悔更少。')

add(3,'细节','What additional result did the June survey report?',
 ['It measured no psychological outcomes.','Every respondent had ceased fearing death completely.','Only uninfected respondents were included.','Previously infected respondents reported lower death anxiety.'],3,
 '六月调查另报告什么结果？',['没测心理结果。','每人完全不怕死。','仅含未感染者。','曾感染者自报死亡焦虑较低。'],
 ['A 同时报告心理丰富与死亡焦虑。','B lower levels不是全部归零；作者live without fear为解释。','C 比较曾感染与未患病者。','D Furthermore 后明示结果，保持自报和代表性样本范围。两次调查复现不自动确立因果。'],
 ['the COVID-19 respondents reported lower levels of death anxiety than those who had not had the illness.'],
 'representative','有代表性的','第二次从瑞典代表性样本调查，不等于每名瑞典人都参加','The researchers surveyed a representative sample.',['a representative sample','reported lower levels'],
 '两研究者于2021年6月再调查一组代表性瑞典样本。复现首次结果：曾患COVID-19者自报人生比未患者更丰富，也自报更低死亡焦虑。因此看来患病经历使他们较不怕死、较能无惧生活。（下一短段保留反向因果限定。）')

add(4,'逻辑关系','What alternative direction of causation does the author acknowledge?',
 ['Infection must have been deliberately assigned.','No variables could be related.','Lower prior death anxiety and greater activity may have preceded both richness and infection.','Psychological richness prevents every infection.'],2,
 '作者承认什么相反因果方向？',['感染一定刻意分配。','变量不可能有关。','原先较少死亡焦虑且常出门，可能先于丰富及感染。','丰富阻止每次感染。'],
 ['A 无随机感染。','B possible alternative不是无关联。','C get out and about...more likely to get COVID 明示既有倾向解释。','D more likely而非绝对预防。作者说possible，不把另一解释当已证实唯一原因。'],
 ['people who were getting out and about without death anxiety had more psychologically rich lives and were also more likely to get COVID.'],
 'reverse causality','反向因果','结果可能由原有心理与行为倾向造成，而非感染单向带来','The survey could not rule out reverse causality.',['reverse causality is possible','consider reverse causality'],
 '当然，这里也可能是反向因果：原本没什么死亡焦虑、常出去活动的人，人生更心理丰富，也更可能感染COVID。')

add(5,'作者意图','Why does the author mention the 1923 massacre?',
 ['To demonstrate harms that rule out calling tragedies simply positive.','To endorse the rumor as verified fact.','To claim all disaster effects are beneficial.','To attribute the killings to the earthquake’s physical shaking alone.'],0,
 '作者为何提1923屠杀？',['展示灾难更坏后果，拒绝简单称正面。','认可谣言为事实。','声称灾难影响全有益。','说仅由物理震动直接杀害。'],
 ['A not arguing...positive 与worse consequences构成论证。','B rumor明说传言，不能当韩国人实际抢劫证据。','C 开头明确否认。','D panic及massacre是社会暴力后果，不等于房屋震塌死亡。at least6000为书载数字，非本工具外部核验。'],
 ['I am not arguing that tragic events like war and pandemics are positive.','some disasters trigger even worse consequences'],
 'rumor','谣言；未经证实的传闻','在此是引发恐慌的指控，非可靠事实','A rumor spread rapidly through the frightened crowd.',['a rumor spread','a panic ensued'],
 '显然，我不是说战争和疫情这样的悲剧是正面的。事件之外，有些灾难引发更糟后果，如屠杀或大规模暴力。1923 Great Kanto地震次日，韩国人抢掠暴乱的谣言迅速传播，恐慌随之而来，大Tokyo地区至少6000名韩国人被杀。')

add(6,'细节','How is “elite panic” explained here?',
 ['A measured lack of fear in all survivors.','Excessive fear of social disorder.','A formally proven increase in community safety.','A justification the author endorses for violence.'],1,
 '此处elite panic怎样解释？',['所有幸存者完全无惧。','对社会失序的过度恐惧。','正式证明社区安全增加。','作者认可暴力的理由。'],
 ['A excessive fear与无惧相反。','B or后给出定义。','C 未给安全效益测量。','D should not have happened明确谴责；unprovoked violence不是合理正当防卫。末句承认长期创伤及悲惨结局，不强加人人复原。'],
 ['an “elite panic,” or excessive fear of social disorder.'],
 'unprovoked','无端的；未受挑衅的','描写针对Black居民的暴力，非认可它','The account condemned unprovoked violence.',['unprovoked violence','inflict violence on'],
 '同样，Katrina后出现elite panic，即过分害怕社会失序。自警团体成立，对Black居民施加无端暴力。这类事件不该发生。有人长期创伤，有人灾后选择结束生命。')

add(7,'主旨','What earlier image of resilient children does Masten describe?',
 ['They had no capacity to adapt.','They recovered only because every danger vanished.','They were often portrayed as extraordinary or invulnerable individuals.','Every scholar had always viewed resilience as ordinary.'],2,
 'Masten描述早期怎样看待韧性儿童？',['完全不能适应。','只因危险全部消失才复原。','常被描写为非凡或刀枪不入的个体。','学者从来都视韧性为普通。'],
 ['A exceptional strength不是无能力。','B 未说外部危险全消失。','C early images/invulnerable/invincible 是早期形象，不能错作作者无条件认可。','D lingered表明特殊英雄观长期存在。most不是人人，下一段才给研究惊喜。'],
 ['often described by words such as invulnerable, or invincible'],
 'resilient','有复原力的；能适应逆境的','不等于从不受伤或人人免于长期创伤','Many people are resilient after difficult changes.',['psychologically resilient','resilient children'],
 '然而研究表明，多数人韧性惊人，多数确实继续生活。心理韧性专家Ann Masten总结数十年研究：早期学术和媒体把这些儿童描写得非凡特殊，常用不受伤害、不可战胜等词。这种认为韧性儿童有超凡力量的想法，甚至在学术中也延续。（引语续下段）')

add(8,'主旨','What is the surprising conclusion about resilience?',
 ['It commonly emerges from basic human adaptation rather than rare invincibility.','It is always a property possessed by only one exceptional child.','It guarantees that no survivor feels pain.','It requires falling exactly seven times in a literal test.'],0,
 '关于韧性的惊人结论是什么？',['常来自基本适应系统，而非罕见无敌。','永远只属一名特殊儿童。','保证幸存者无痛。','必须真实测试恰跌七次。'],
 ['A ordinariness/common/basic adaptational systems共同支持。','B common与only相反。','C 韧性不是无痛保证。','D 谚语是比喻，非实验跌倒次数。原书括号日语在候选段落间断开，下一单元只是其结尾，不冒充独立英文句。'],
 ['Resilience appears to be a common phenomenon that results in most cases from the operation of basic human adaptational systems.'],
 'ordinariness','普通性；普遍性','与把韧性视为超人特质的旧印象对照','The review emphasized the ordinariness of resilience.',['ordinariness of a phenomenon','basic adaptational systems'],
 '韧性研究最大惊喜是现象的普通性。韧性看来很常见，多数源自人类基本适应系统的运作。研究为日本谚语“跌倒七次，第八次站起来”提供实证支持（括号日语七転八的末字续在下一单元）。')

add(9,'逻辑关系','How does this printed continuation function in its paragraph?',
 ['It starts a new result about COVID-19.','It is a complete new section heading.','It gives a numerical estimate of resilience.','It closes the parenthetical Japanese proverb begun in the preceding excerpt.'],3,
 '此印刷续片在原段落中起什么作用？',['开始新的COVID结果。','完整新小节标题。','给出韧性数值估计。','结束上一短段开始的括号内日语谚语。'],
 ['A 起).不含新的研究结果。','B 版面显示它接在七転八之后，而非独立标题。','C 无百分比或样本数。','D PDF131页同一谚语因排版换行被原提取器拆成两个候选段。本题是具体来源续接辨识，保留现有ID与三个字符；不是独立英文阅读段，也不把自动候选句计数当最终人工句界。'],
 ['起).'],
 '起','起身；站起来（日语谚语的末字）','此处不是英文单词，专用于说明原书日语七転八起的断行续接','The proverb describes getting up after repeated falls.',['七転八起','stand up again'],
 '“起）。”这是上一短段括号内七転八起的最后一个字及结束标点，含义承接“跌倒七次，第八次站起”；本片本身没有额外英文命题。')

add(10,'主旨','What possibility does the author offer when happiness seems unavailable?',
 ['Other values may frame a difficult life, including richness without happiness.','Every unfortunate event must be pleasant.','People should arrange disasters for themselves.','The painting proves a universal experimental result.'],0,
 '幸福遥不可及时，作者提出什么可能？',['可用其他价值理解人生，丰富未必快乐。','每个不幸事件必须愉快。','应安排自己遭灾。','画作证明普世实验结果。'],
 ['A other values/might enrich/far from happy保留可能与区别。','B far from happy相反。','C 没鼓励主动受难。','D 画是作者例子，非实验数据。'],
 ['it might unintentionally enrich our lives, even when the “enriching” experience is far from a happy one.'],
 'frame','理解；赋予解释框架','用其他价值看艰难人生，不是伪造事件','She used a different value to frame the experience.',['frame our lives','frame an unfortunate event'],
 '困难时幸福遥不可及，还有其他价值可用来理解人生。一种看待不幸的方式是，它也许无意丰富人生，即使“丰富”的体验远不快乐。Guido Reni一幅画描绘St. Michael踩住Satan脖颈。')

add(11,'逻辑关系','What condition qualifies the coexistence of richness and misfortune?',
 ['Misfortune must be allowed to grow without limit.','The misfortune must be kept in check.','Richness requires all suffering to be called happiness.','Every viewer must believe the painting literally predicts the future.'],1,
 '丰富与不幸并存有什么条件？',['不幸须无限扩大。','不幸须得到约束。','须把所有痛苦称幸福。','须相信画字面预测未来。'],
 ['A kept in check与无限扩张相反。','B so long as两次限定，不能省略。','C coexist不是同义，前段区分快乐。','D William James评论为哲学艺术比喻，不是因果实验或预言。'],
 ['Psychological richness and misfortune can coexist, so long as the misfortune is kept in check.'],
 'kept in check','受约束；得到控制','限定不幸不能失控，非对所有受害者保证能控制遭遇','The danger had to be kept in check.',['keep misfortune in check','so long as'],
 'William James评论此画：只要仍把脚踩在魔鬼脖颈上，世界因有魔鬼而更丰富。只要不幸得到约束，心理丰富与不幸能够共存。')

add(12,'作者意图','What focus does the new chapter announce?',
 ['Measuring earthquake magnitude again.','Treating all disasters as identical stories.','Exploring how storytelling shapes psychological richness.','Proving every survivor’s narrative is uplifting.'],2,
 '新章宣布什么重点？',['再量地震震级。','把灾难当完全相同故事。','探索讲故事怎样塑造心理丰富。','证明每个叙述都振奋。'],
 ['A 无重新测量。','B 有dramatic与hopeless不同故事。','C 最后一句明示故事在心理丰富中的作用。','D some/others区分多种走向。此前灾难影响是作者回顾，不能扩成人人必获益。'],
 ['the role of storytelling in psychological richness.'],
 'uplifting','鼓舞的；振奋人心的','与hopeless/depressing/dark故事走向对比','The account was memorable and ultimately uplifting.',['an uplifting story','ultimately uplifting'],
 '上一章我展示自然灾难经历往往令受害者更关心他人福祉并获新视角。不过体验是否真丰富人生，取决于人给自己讲的故事。有些戏剧性、难忘且最终鼓舞人，有些绝望、压抑、阴暗。本章探讨讲故事在心理丰富中的作用。')

add(13,'主旨','What complication accompanies the link between richness and life stories?',
 ['A life story never changes after it is first told.','Story quality has no role in richness.','Only the number of pages matters.','People narrate their own lives differently at different times.'],3,
 '丰富与人生故事联系中有什么复杂之处？',['第一次讲后永不改变。','故事质量没作用。','只看页数。','人在不同时间会不同地叙述自己人生。'],
 ['A differently at different times相反。','B quantity and quality都提到。','C 无页数指标。','D But引入Barnes所指出的叙述变化，不能把一次自述当永远固定的事实版本。'],
 ['we tell our own life story differently at different times.'],
 'intertwined','交织的；紧密相连的','心理丰富与故事数量质量相互关联的作者论述','Experience and narrative are closely intertwined.',['inherently intertwined with','quantity and quality'],
 '心理丰富本来就与故事数量质量交织。有趣故事越多，人生越心理丰富。但如Julian Barnes指出，我们不同时间讲人生会不同。你怎样讲自己的人生故事？')

add(14,'作者意图','Why introduce one possible narrative of George W. Bush?',
 ['To illustrate that the same life can be framed through different narrative structures.','To prove family background determines all behavior.','To announce a new study of all political families.','To claim that there is no alternative way to tell his story.'],0,
 '为何引入George W. Bush的一种叙述？',['说明同一人生可用不同故事结构呈现。','证明家庭决定一切行为。','宣布所有政治家族新研究。','声称没有另一讲法。'],
 ['A story structure设问后could be told/Alternatively展示框架选择。','B 不作决定论结论。','C 只是人物叙述例，非统计研究。','D Alternatively明确还有另一讲法。家庭叙述是作者示范，不当作新政治史核查。'],
 ['a story of George W. Bush could be told in terms of his illustrious family line','Alternatively, you can tell G.W.’s story in a different way.'],
 'illustrious','显赫的；卓著的','修饰家族背景，是一种叙述强调点','The biography emphasized an illustrious family line.',['an illustrious family line','follow in someone’s footsteps'],
 '更一般说，讲故事能力对心理丰富有多重要？故事结构多重要？如George W. Bush可被讲成出身显赫家族、循父祖足迹、显要政治家族听话的长子。也可以不同方式讲G.W.故事。')

add(15,'主旨','What does the alternative Bush narrative emphasize?',
 ['A life without any personal change.','A transformation from rebellious youth to a different adult identity.','A controlled comparison of all politicians.','The impossibility of making any life sound richer.'],1,
 '另一种Bush叙述强调什么？',['人生完全无变化。','从叛逆青年转为另一成年身份。','所有政客的受控比较。','不可能把任何人生讲丰富。'],
 ['A turning into是变化。','B 由受宠富家孩子转向作者所列成年特征，形成成长弧线。','C 叙述例非实验。','D 末句是Can we设问，未否定可能性。could add保留示范性质，不替作者政治评价作额外事实背书。'],
 ['the narrative of a rich, spoiled kid turning into a Bible-loving, sober, compassionate, conservative politician.'],
 'rebellious','叛逆的','可加入故事的早年经历，与成年变化对照','The memoir described rebellious years before a later change.',['rebellious years','a rebellious youth'],
 '你可加入叛逆岁月，以及父亲George H. W. Bush未寄厚望：一个受宠富家孩子变成爱圣经、戒酒、怀同情心的保守政客。我的问题是：能否让人生听起来更心理丰富？')

add(16,'细节','How is “story editing” defined?',
 ['Deleting every difficult experience from public records.','Replacing all evidence with fiction.','Techniques that redirect narratives about oneself and the social world.','A method for grading only literary manuscripts.'],2,
 'story editing怎样定义？',['从公共档案删全部困难经历。','以虚构替代所有证据。','重新引导对自我及社会世界的叙述技巧。','只批文学手稿的方法。'],
 ['A 例子反是highlight challenges。','B 定义是重导叙述，不授权捏造事实。','C 引语定义精确。','D 非只文学手稿，谈人对自身和社会的理解。Tim Wilson为Redirect作者，不与后文Anne Wilson混同。'],
 ['a set of techniques designed to redirect people’s narratives about themselves and the social world.'],
 'redirect','重新引导；改变走向','调整叙述焦点及解释方向，而非倒改实际事件','The exercise helped redirect the narrative toward growth.',['redirect narratives','story editing'],
 '著名心理学家Tim Wilson在Redirect讨论这一过程，称故事编辑：一套重新引导人们对自身和社会世界叙述的技巧。例如，可突出人生面对过的挑战。')

add(17,'推断','What reframing of the Yale years does the author propose?',
 ['They prove the student never engaged in counterproductive behavior.','They were a literal preface written for a book.','They establish that every legacy student faced identical hardships.','They could be told as a prelude to later maturity.'],3,
 '作者提议怎样重述Yale岁月？',['证明从无适得其反行为。','是书面序言。','所有校友子弟困难完全相同。','可讲成后来成熟的前奏。'],
 ['A drinking/partying被称counterproductive。','B prelude为人生阶段比喻。','C probably/could不能扩大成所有人确证经历。','D could reframe...prelude直接支持，是作者示范而非本人已给证词。1964–1968保留原排版空格，不擅改。'],
 ['He could reframe his Yale years as a prelude to becoming a mature man in his thirties.'],
 'counterproductive','适得其反的','试图证明价值却靠过度喝酒派对，反不达目标','The defensive response proved counterproductive.',['a counterproductive way','counterproductive behavior'],
 'G.W.作为数代Yale校友后人，可能未遭很大挑战，却可以说1964–1968大学时学校剧变，反体制情绪增长，校友子弟首次被鄙视。他须证明价值，却靠过度饮酒派对适得其反。可把Yale时期重述为三十多岁成熟的前奏。')

add(18,'逻辑关系','How could emphasizing a worse earlier self affect the narrative?',
 ['It could make later improvements stand out.','It would erase every objective record.','It proves no improvement occurred.','It would require claiming an ideal adolescence.'],0,
 '强调更差的早年自我怎样影响叙述？',['让后来改善更突出。','抹去所有客观记录。','证明毫无改善。','要求声称青春完美。'],
 ['A By emphasizing...could highlight improvements给出对比作用。','B 无档案删除。','C highlight不是否认。','D terrible与完美相反。could保留可能，不等于实际能力改善已客观证实。'],
 ['By emphasizing how terrible he was in his teens and twenties, he could also highlight his improvements.'],
 'highlight','突出；强调','通过早晚反差呈现成长，不等于制造资料','The story highlighted the change over time.',['highlight improvements','emphasize the past'],
 '通过强调十几岁和二十多岁时有多糟，他也可突出自己的改善。')

add(19,'细节','What was the reference point for the parents’ trait ratings?',
 ['Their children’s grades alone.','Other people of the same age.','Their scores on a mathematics examination.','The researchers’ personal opinion of them.'],1,
 '父母特质评分以什么为参照？',['只看孩子成绩。','其他同龄人。','数学考试分数。','研究者个人意见。'],
 ['A 研究父母自评，不是孩子学分。','B relative to...same age 明示比较参照。','C 宽容、自信、社交技能非数学测试。','D 自评不是专家打分。11点含0至10，中点5代表与大多数相同；Anne Wilson与Michael Ross是本研究作者。'],
 ['relative to other people of the same age on an 11-point scale'],
 'broadminded','宽容的；思想开阔的','列举的自评可取特质之一，非客观智商量度','The questionnaire asked how broadminded they considered themselves.',['broadminded and self-confident','desirable traits'],
 '这是相当健康的自我看法。Anne Wilson与Michael Ross研究让心理学导论学生的父母报告，与同龄人比，自己多宽容、自信、有社交技巧等；用11点量表，0远少于多数、5与多数相同、10远多于多数。')

add(20,'细节','How were earlier-life ratings obtained from the parents?',
 ['By following the parents continuously from age sixteen.','By testing only their actual children.','By asking them now to judge themselves at several earlier ages as well as currently.','By using school records from every year.'],2,
 '父母早年评分怎样获得？',['从十六岁持续追踪。','只测试他们孩子。','现在回评多个早年年龄并评当前自我。','用每年学校档案。'],
 ['A 问的是现在回顾，非跨几十年实时追踪。','B 对自己作答，非对子女测量。','C right now/then...applying...when 明示回顾设计。','D 无档案来源。49、20、35为所述平均年龄，16为固定回评年龄。'],
 ['answer these questions about themselves right now','applying them to when they were sixteen years old'],
 'midpoint','中点','父母与子女年龄之间的中间年龄，此处平均35岁','The survey included a rating for the midpoint between two ages.',['at the midpoint','average age'],
 '父母先答当下自己（平均49岁），再答十六岁、与孩子同龄时（平均20岁）、自己与子女年龄中点时（平均35岁）的自己。')

add(21,'细节','Which ordering correctly represents the parents’ reported ratings?',
 ['7.47 at sixteen, then falling to 5.87 now.','The same 5.00 at every age.','6.67 at thirty-five and 7.21 at twenty.','5.87 at sixteen, 6.67 around twenty, 7.21 around thirty-five, and 7.47 now.'],3,
 '哪项正确排列父母自报评分？',['十六7.47降至现在5.87。','每年龄同为5。','35岁6.67、20岁7.21。','十六5.87、约二十6.67、约三十五7.21、现在7.47。'],
 ['A 颠倒早晚。','B 各值不同且都高于中点5。','C 二十与三十五数值错配。','D 保留年龄与数值对应；这些是现在对不同阶段的平均评价，不是当年客观实际能力或实时评分。'],
 ['from 5.87 when they were sixteen','to 6.67 when they were their children’s age','to 7.21 when they were roughly thirty-five years old, to 7.47 now'],
 'steadily','稳步地；持续地','随所回顾年龄逐步升高的评分模式','The reported ratings increased steadily across the recalled ages.',['steadily increased','parents’ average ratings'],
 '宽容、自信、社交技能等可取特质，父母平均回评分从十六岁5.87（略高平均），到子女同龄约20岁6.67、约35岁7.21、当下约49岁7.47稳步上升；自认为比普通49岁者开阔、自信、善社交得多。')

add(22,'推断','What qualification limits the above-average tendency described?',
 ['It applies to many desirable traits, with concrete abilities such as music and mathematics excepted.','Every American considers every ability above average.','The parents’ objective youthful skills were certainly measured.','The passage says parents overestimate how skilled they were when young.'],0,
 '哪项限定文中高于平均倾向？',['许多可取特质有此倾向，但音乐数学等具体能力例外。','每个美国人每种能力都自认超平均。','确实测过父母年轻时客观技能。','父母高估年轻技能。'],
 ['A most/many与though not保留范围。','B 将most/many扩大every/every。','C 父母回顾非年轻实测。','D seem to underestimate是似乎低估，不是高估；可能借此感觉改善更大，尚需后续更强证据。'],
 ['though not on concrete ability traits such as musical skills and math abilities','parents seem to underestimate their skills as young people'],
 'concrete','具体的；较可明确检验的','与宽泛社会性特质对照的技能类别','The study distinguished broad traits from concrete abilities.',['concrete ability traits','musical skills and math abilities'],
 '多数美国人觉得领导、社交等许多可取特质高于平均，但音乐和数学等具体能力并非如此。本研究更有趣的是，父母似乎低估年轻技能，借此感觉自己改善很多。')

add(23,'作者意图','Why did Wilson and Ross conduct a longitudinal study?',
 ['To prove the parents had lied intentionally.','To examine the issue beyond uncertain retrospective judgments.','To replace all self-ratings with intelligence tests.','To follow the same parents from birth.'],1,
 '为何开展纵向研究？',['证明父母故意说谎。','超越不确定回顾评价，更深入考察。','用智商测试替全部自评。','从出生追同一父母。'],
 ['A 记忆偏差不等于故意欺骗。','B might indeed/ no way know for sure后为更多认识转纵向。','C 仍问独立、自信、社交相对同龄人的自评。','D 新研究是本科生，首测九月而非父母出生。当前只述首测，未给后测结果。'],
 ['There’s no way to know for sure. To gain more insight into this phenomenon, Wilson and Ross ran a longitudinal study.'],
 'longitudinal','纵向的；追踪的','多个时间点评同一组，与一次回顾区分','The longitudinal study compared ratings across two months.',['a longitudinal study','undergraduate participants'],
 '不过，父母年轻时也可能确实较不善社交、缺自信，无法确定。为多了解，Wilson与Ross做纵向研究。九月学年开始，请本科生评当下相对同龄同学有多独立、自信、善社交。')

add(24,'逻辑关系','What comparison did the November retrospective ratings make possible?',
 ['A comparison between two unrelated groups of parents.','A comparison of actual performance on different exams.','A comparison of remembered September selves with ratings actually recorded in September.','A comparison of careers before and after retirement.'],2,
 '十一月回顾评分使什么比较成为可能？',['两批不相关父母。','不同考试实际成绩。','记忆中的九月自我与九月实际记录的自评分。','退休前后职业。'],
 ['A 此研究同组学生两个时间点。','B actual ratings是当时记录的自评，不是客观技能考试。','C compare recollections...actual ratings two months earlier直接支持。','D 没退休变量。十一月同时评现在和回忆九月，不能把回忆当九月原记录。'],
 ['compare their recollections with their actual ratings two months earlier.'],
 'recollections','回忆；记忆内容','后测时对过去自我的记忆性评分','Their recollections differed from the earlier ratings.',['compare recollections','actual earlier ratings'],
 '约两月后十一月，再让学生评当下独立、自信、社交相对同龄人的程度；同时回想学期开始时的自己。评现在与记忆过去，使研究者可将回忆与两个月前实际自评记录比较。')

add(25,'推断','What discrepancy do the three ratings reveal?',
 ['Actual self-ratings rose from 5.74 in September to 6.35 in November.','The remembered September score exactly matched the original.','Objective social skill improved by the same amount in everyone.','Original September ratings exceeded November ratings, but recalled September ratings were lower than November’s.'],3,
 '三个评分揭示什么不一致？',['实际从九月5.74升至十一月6.35。','回忆九月与原始精确相同。','每人客观社交等量提升。','原始九月高于十一月，但回忆九月低于十一月。'],
 ['A 原始九月6.35、十一月6.05，5.74是十一月回想九月。','B 6.35不等于5.74。','C 是自评记忆模式，不是客观技能或人人变化。','D 实际记录方向下降，回忆却显得成长，三值时点归属准确。'],
 ['In September, they rated their desirable traits as 6.35','In November, they rated themselves on the desirable traits as 6.05','the remembered September self-rating was 5.74!'],
 'remembered','被回忆起的；记忆中的','十一月重建的九月自我，区别九月原始自评','The remembered score was lower than the original self-rating.',['remembered September self-rating','original self-rating'],
 '九月他们在同一11点量表评自己6.35，高于平均；十一月当下评分6.05。九月原始自评显著高于十一月。然而十一月回想九月时，竟觉得过去比现在显著更差：回忆九月评分只有5.74！')

assert len(out)==25 and [q['id'] for q in out]==[t['questionId'] for t in targets]

def persist():
 path=ROOT/'source/short-questions/additional.json';existing=load('source/short-questions/additional.json');byid={q['id']:q for q in existing}
 for q in out:
  if q['id'] in byid:assert byid[q['id']]==q,('Refuse to overwrite changed authoring',q['id'])
  else:existing.append(q)
 path.write_text(json.dumps(existing,ensure_ascii=False,indent=2)+'\n',encoding='utf8',newline='\n')
 review=dict(batchId='batch-033',date='2026-10-23',pdfSha256=b['pdfSha256'],checkedPdfPages=list(range(130,137)),questionIds=[q['id'] for q in out],paragraphs=[dict(id=pid,textSha256=hashlib.sha256(pp[pid]['text'].encode()).hexdigest()) for pid in dict.fromkeys(q['paragraphId'] for q in out)],note='完整PDF130–136原页视觉核对含章末132与章首133。瑞典2021两次调查为自报比较，保留反向因果；谣言不作事实、暴力明确谴责，韧性most/common不作人人无创伤。既有单元q-c11-062原文仅起).，为131页七転八起括号因换行提取的末字续片，保留既有ID/范围并编来源续接辨识题，明确非独立英文段或最终人工句界，不补造英文或新主张；词汇特记日语末字。James画作是哲学比喻，保留不幸受约束。Bush为作者可选叙述示范，probably/could不作客观证实；Tim Wilson区别Anne Wilson。父母回顾多年龄评分非几十年追踪；本科纵向6.35原九月/6.05当下十一月/5.74回忆九月分开，实际记录指原自评不是客观能力。末段整段审阅含后续未配题材料，不宣称逐句直接证据全覆盖。')
 (ROOT/'source/short-questions/review-chapter11-12-narrative25.json').write_text(json.dumps(review,ensure_ascii=False,indent=2)+'\n',encoding='utf8',newline='\n')
 print('Saved',len(out),'of 25 individually authored exercises')

if __name__=='__main__':persist()
