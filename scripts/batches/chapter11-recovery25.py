"""25 individually authored exercises for frozen targets, PDF pages 126-130.
Preserve printed English, source positions and all previously published questions.
"""
from pathlib import Path
import json,hashlib
ROOT=Path(__file__).resolve().parents[2]
load=lambda p:json.loads((ROOT/p).read_text(encoding='utf8'))
b=load('public/data/book.json');plan=load('public/data/reading-plan.json');targets=load('source/short-questions/batch032-targets.json')['targets']
ss={s['id']:s for s in b['sentences']};pp={p['id']:p for p in b['paragraphs']};out=[]
def add(i,kind,prompt,options,answer,prompt_zh,options_zh,analyses,quotes,word,meaning,context,example,collocations,translation,support='explicit'):
 t=targets[i-1];u=next(u for u in plan['units'] if u['id']==t['readingUnitId']);group=[ss[sid] for sid in u['sentenceIds']];p=pp[u['paragraphId']];text=p['text'][group[0]['start']:group[-1]['end']]
 assert hashlib.sha256(text.encode()).hexdigest()==t['passageSha256'];evidence=[]
 for quote in quotes:
  offset=text.find(quote);assert offset>=0,(i,quote);start=group[0]['start']+offset;end=start+len(quote);touching=[s for s in group if s['start']<end and s['end']>start]
  evidence.append(dict(quote=quote,sentenceIds=[s['id'] for s in touching],sources=list({(r['pdfPage'],r['block']):r for s in touching for r in s['sources']}.values())))
 assert word.lower() in text.lower(),(i,word)
 out.append(dict(id=t['questionId'],version=1,readingUnitId=u['id'],chapterId=u['chapterId'],sectionId=u['sectionId'],paragraphId=u['paragraphId'],sentenceIds=u['sentenceIds'],passage=text,prompt=prompt,options=options,answer=answer,type=kind,promptZh=prompt_zh,optionsZh=options_zh,analyses=analyses,evidence=evidence,vocabulary=[dict(word=word,meaning=meaning,context=context,example=example,collocations=collocations)],translation=translation,support=support,editorialStatus='完整PDF126–130原页视觉核对及跨页拼接。Kobe物理修复和心理伤痕分开，调查波次与作者休假年分开，房损/失亲同时分析不作随机因果或变量全无关联。Solnit为引语/作者阐释，电视职业愿望为作者回忆。四川震前后为同校新组，as if/presumably保留，非研究者随机分配灾害；100供选/10获得/平均略逾1至约4为九岁结果，不补六岁或长期个体变化。市政申请按每职位且非实际就职，1989–2000与1995变化分开。COVID接触包括本人/家属/熟人，捐款奖金/加倍与结果分开，作者made价值解释不升级成随机感染因果或医学建议。承认长期损害，不强加受害者获益/感恩；不宣称逐句证据全覆盖。'))







add(1,'语境词义','What does “brought to light” mean here?',
 ['Revealed a human capacity for compassion.','Removed all physical destruction.','Installed lighting in every damaged home.','Proved disasters are desirable.'],0,
 '此处 brought to light 意思是什么？',['显露人的同情能力。','消除全部破坏。','为所有灾房装灯。','证明灾难值得追求。'],
 ['A 指显露人的力量，compassion明确命名。','B 本句没否认破坏，But承接前段。','C 习语非实体照明。','D 显现品质不等于灾难可欲。they需顺读前段理解，本题核心词义由本句支持。'],
 ['brought to light one of the greatest human strengths, compassion.'],
 'compassion','同情；关怀他人的苦难','作者指出灾难中显露的人的力量','The volunteers responded with compassion.',['show compassion','human compassion'],
 '但是，正如Nietzsche指出的，它们也显露了人类最伟大力量之一：同情。')

add(2,'细节','Which numerical statement matches the account of the earthquake?',
 ['The earthquake struck in 2001 with magnitude 1.42.','Exactly 100,000 people died.','More than 100,000 homes were completely destroyed.','Kobe had only 6,400 residents.'],2,
 '哪项数字与地震叙述一致？',['2001年发生，震级1.42。','恰好十万人死亡。','逾十万住宅彻底毁坏。','Kobe只有6400居民。'],
 ['A 1995年1月17日、7.3级；1.42百万是人口。','B 十万为住宅，死亡逾6400且不是恰好。','C 数量、对象、程度都准确。','D 6400为死亡人数阈值，非人口。war zone为外观比喻，不是战争史。'],
 ['Over 100,000 homes were completely destroyed and over 6,400 people died.'],
 'epicenter','震中','书中说靠近Kobe市中心，不等于全区域震度相同','The epicenter was close to the city center.',['earthquake epicenter','close to the epicenter'],
 '1995年1月17日，7.3级地震震动Kobe及周边，称Hanshin-Awaji地震。震中近市中心，Kobe人口142万。倒塌房屋、毁坏公路和火灾使它看似战区。逾十万住宅彻底毁坏，逾6400人死亡。')

add(3,'逻辑关系','Why does the author say residents were surprised?',
 ['Kobe was described as the most earthquake-prone area.','No damage occurred in Kobe.','Tokyo had experienced this same earthquake first.','Kobe and Kansai were not known for frequent earthquakes, unlike Tokyo and Tohoku.'],3,
 '作者为何说居民惊讶？',['Kobe被描写为最频繁地震区。','Kobe无损害。','Tokyo先经历同场地震。','不同于Tokyo和Tohoku，Kobe和Kansai不以频震闻名。'],
 ['A 与are not相反。','B devastated明确遭重创。','C 无同场先后事件。','D whereas...not 后So构成惊讶原因；不以频繁闻名不等于历史上从无地震。'],
 ['the Tokyo and Tohoku areas are known for frequent earthquakes, whereas the Kobe and Kansai areas are not.'],
 'whereas','而；然而','连接两个地区在频繁地震名声上的对比','One area was familiar with the risk, whereas the other was not.',['whereas...are not','contrast with whereas'],
 '在日本，Tokyo和Tohoku以地震频繁著称，Kobe及Kansai却不是。因此，这次地震令Kobe居民惊讶而深受创伤。')

add(4,'细节','Who classified the damaged homes into four categories?',
 ['Children selecting stickers.','Insurance companies examining the homes.','Applicants for municipal jobs.','The author during the 1995 earthquake itself.'],1,
 '谁将受损住宅分为四类？',['挑贴纸儿童。','检查住宅的保险公司。','市政岗位求职者。','作者在1995年地震现场。'],
 ['A 属后续不同研究。','B Insurance companies examined...classified明示。','C 不属损害分级。','D 作者2012–2013休假研究，非1995现场分级。调查年份2001/2003/2005/2011与作者分析时间分开。'],
 ['Insurance companies examined damaged homes and classified them into four categories'],
 'sabbatical','学术休假的','研究者在2012–2013驻Kobe，区别调查收集年份','She spent her sabbatical year studying recovery.',['sabbatical year','spend a sabbatical in'],
 '这些经历留下多深心理伤痕？为调查，我在Kobe度过2012–2013学术休假年，分析Hyogo Life Recovery Surveys。调查于2001、2003、2005、2011在Kobe及周边进行。保险公司检查住宅，分完全损坏、半损、部分损坏、无损四类。')

add(5,'推断','What comparison is supported for the time of the first survey?',
 ['Current living conditions were broadly similar despite different levels of damage in 1995.','All respondents had identical life histories.','Physical repairs proved psychological recovery was complete.','The first survey occurred immediately after the earthquake.'],0,
 '首次调查时支持怎样的比较？',['1995损害程度不同，但当时居住条件大致相似。','所有人生经历相同。','物理修复证明心理完全康复。','震后立即首次调查。'],
 ['A not substantially different指当前生活条件，不抹去过去损失。','B 生活条件相近非人生完全同一。','C 该句仅物理修复，未证明心理。','D first survey为2001，不是1995立即。all fully repaired按书保留，不冒充独立重查城市工程数据。'],
 ['current living conditions','were not substantially different'],
 'spared','幸免于；未遭受','住宅未被地震毁坏，非指所有人生都无损','Some homes had been spared by the earthquake.',['spared by an earthquake','homes that were spared'],
 '到2001年，Kobe及周边所有物理损坏已修复。这意味着首次调查时，1995年房子全毁者的当时居住条件，与住宅幸免者没有重大差别。')

add(6,'主旨','What central finding qualifies the idea that time heals everything?',
 ['All group differences disappeared by 2003.','Only physical rebuilding mattered to the study.','Those who lost homes continued to report worse well-being as late as 2011.','No participant reported any physical illness.'],2,
 '什么核心发现限定时间治愈一切的说法？',['2003组差全消失。','研究只关心物理重建。','失去住宅者到2011仍报告较差福祉。','无人报告身体病痛。'],
 ['A later results similar to2001而非消失。','B psychological scars为主题。','C 2001及后续比较持续，2011距震十六年。','D more physical illnesses相反。心理免疫系统是作者概念比喻，不是检验免疫细胞或诊断每个人。'],
 ['the results in 2003, 2005, and even 2011—sixteen years after the earthquake—were similar to those from 2001.'],
 'devastation','巨大破坏；重创','强调灾害严重损失及长期影响','Recovery from the devastation took many years.',['the devastation of an earthquake','psychological scars'],
 '但失去住宅者的心理伤痕仍可见。2001年，1995房全毁者比无损者生活满意度显著较低，并自报更多负面情绪与身体疾病。2003、2005，甚至2011——震后十六年——结果仍似2001，时间没治愈一切。心理免疫系统不足以抵御地震重创。')

add(7,'同义改写','Which restatement preserves the reported outcomes?',
 ['Victims reported higher satisfaction and fewer illnesses.','Every victim had an identical clinical diagnosis.','All health problems had disappeared.','Victims still reported lower satisfaction and more negative emotions and physical illnesses.'],3,
 '哪项改述保留结果？',['满意更高病更少。','每位受害者临床诊断完全相同。','一切健康问题消失。','仍自报满意较低、负面情绪与身体病痛更多。'],
 ['A 比较方向全反。','B 报告组间倾向不等于人人同诊断。','C illnesses仍较多。','D still与reported及三项指标均保留。当前句没给完整研究细节，不能加入新临床检验。'],
 ['still significantly less satisfied with their lives and reported more negative emotions and physical illnesses'],
 'significantly','显著地','研究所述比较差异，不提供此处未列效应大小','The groups differed significantly in reported satisfaction.',['significantly less satisfied','report negative emotions'],
 '多年之后，受害者的生活满意度仍显著较低，也报告更多负面情绪和身体疾病。')

add(8,'逻辑关系','Why examine housing damage and human loss simultaneously?',
 ['To assume the two forms of loss could never co-occur.','To consider each contribution to well-being while accounting for the other.','To prove that bereavement was harmless.','To replace survey reports with randomized disasters.'],1,
 '为何同时考察住宅与亲人损失？',['假定两者绝不共存。','考虑另一因素时分析各自对福祉的贡献。','证明失亲无害。','以随机灾害替代问卷。'],
 ['A 前面明说房损越多越可能失亲。','B 因两类损失相伴，simultaneously后分析各自独立作用；不是变量统计上完全无关。','C lingering negative effect相反。','D 共同分析不是随机分配损失，不能据此保证排除全部混杂。'],
 ['we examined housing damage simultaneously with human losses.','housing damage and human loss each had an independent effect on well-being'],
 'lingering','持续不去的；长期残留的','失亲负面影响可能长久残留','The loss had a lingering effect on well-being.',['lingering negative effect','lingering grief'],
 '调查还显示，房损越多，越可能失去亲人。失亲也可能长期损害福祉。因此我们同时分析房损与失亲。结果显示两者对福祉各有独立作用：损失越大，生活满意度越低，负面情绪和健康问题越多。')

add(9,'主旨','What conclusion does the author draw about the Kobe case?',
 ['Time did not completely heal the consequences.','Time cannot improve any aspect of any tragedy.','Every survivor recovered at exactly the same speed.','Physical reconstruction never occurred.'],0,
 '作者对Kobe案例得出什么概括？',['时间未完全治愈后果。','任何悲剧任何方面时间都不改善。','所有幸存者康复速度相同。','从无物理重建。'],
 ['A did not heal everything保留非全部的范围。','B 一个案例及everything的否定不能改成一切情境无改善。','C 没给同速结论。','D 结论针对悲剧延续影响，不否认物理重建。'],
 ['the Kobe earthquake was a tragic case where time did not heal everything.'],
 'tragic','悲剧性的；悲惨的','对该案例的概括，不淡化长期痛苦','The account described a tragic case of lasting loss.',['a tragic case','a tragic experience'],
 '简言之，Kobe地震是一个时间没有治愈一切的悲剧案例。')

add(10,'细节','What did Anna Holshouser do after the 1906 earthquake?',
 ['Conducted a randomized survey of all survivors.','Served only two people per week.','Started a temporary soup kitchen serving two to three hundred people a day.','Opened a permanent restaurant in every Oakland neighborhood.'],2,
 '1906地震后Anna做什么？',['对全部幸存者随机调查。','每周仅服务两人。','设临时施食处，日供二三百人。','在Oakland每街区开永久餐厅。'],
 ['A 书中记录善行，不是这项试验。','B 数量与单位错误。','C makeshift/evacuation camp及日供人数准确。','D Oakland为支援来源，不是遍地餐厅。'],
 ['Anna Holshouser started a makeshift soup kitchen in an evacuation camp.','she served two to three hundred people a day.'],
 'makeshift','临时凑合的；权宜的','应急营地中搭建的施食厨房','Volunteers opened a makeshift kitchen.',['a makeshift soup kitchen','a makeshift shelter'],
 'Rebecca Solnit在A Paradise Built in Hell记录灾民许多亲社会行动。例如1906 San Francisco地震后，Anna Holshouser在疏散营地设临时施食厨房。湾对岸Oakland支援下，她每天供食二三百人。')

add(11,'主旨','What possibility does Solnit emphasize in this quotation?',
 ['Disasters leave every person physically undamaged.','Disaster can disrupt old orders and call forth deep feelings and capacities.','All emergencies guarantee happiness.','Only directly injured people experience disruption.'],1,
 'Solnit引语强调什么可能性？',['每个人身体都无损。','灾难可打破旧秩序，唤起深层情感能力。','所有紧急状况保证幸福。','只有直接受伤者受扰乱。'],
 ['A wounded/killed/orphaned承认严重伤害。','B disruptive power/new possibilities和calling into play串联核心。','C can be rich不等于guarantee happiness。','D periphery...largely undamaged...profoundly disrupted指旁及人群。这里是著作引语的观点，不是实验概率估计。'],
 ['the ability of disasters to topple old orders and open new possibilities'],
 'topple','推翻；使倾覆','形容旧社会秩序被扰动的比喻','The crisis threatened to topple the old order.',['topple old orders','open new possibilities'],
 'Solnit总结：伤者、死者、失孤者周围，同城甚至同社区还有更多大体无损却深受扰动者。关键是灾难打破旧秩序、开启新可能的扰动力量。情感深度、触及存在核心、调动最强情绪和能力，即使在病榻、战争和紧急状况中，也可能丰富。')

add(12,'作者意图','What contrast is made between disaster and comfortable circumstances?',
 ['Comfort invariably produces the deepest experience.','Disaster victims should be blamed for their distress.','The author reports that no comfortable person ever feels bored.','Disaster may reveal depths, while apparent happiness can sometimes insulate people from them.'],3,
 '灾难与舒适情境形成什么对照？',['舒适总带来最深体验。','应责怪灾民痛苦。','舒适者从不无聊。','灾难可能显露深处，表面幸福有时隔绝它。'],
 ['A sometimes...insulation与总是最深不符。','B 无责怪受害者。','C ennui/angst正提无聊焦虑。','D seems to argue及sometimes保留可能性，不推广成所有苦难必有益。两层含作者对Solnit的解释与她的引语，不混作实验发现。'],
 ['Solnit seems to argue that a natural disaster reveals one’s true colors','sometimes is only insulation from the depths'],
 'insulation','隔绝；隔离保护','比喻舒适有时隔绝深层体验，并非建筑绝缘材料','Comfort can act as insulation from difficult questions.',['insulation from the depths','emotional insulation'],
 'Solnit似乎认为，自然灾难揭露真实本色，触及存在最深处，甚至帮助发现自身最好一面。相反，她指出，常被当作幸福环境的事物，有时只是与深处隔绝；舒适者的无聊与焦虑似乎提示这一点。')

add(13,'细节','What occupations did many interviewed surviving children mention?',
 ['Nurses, firefighters and doctors.','Only professional athletes.','Every municipal role listed elsewhere in the chapter.','Their parents’ jobs, without any examples.'],0,
 '许多受访幸存儿童提了哪些职业？',['护士、消防员、医生。','仅职业运动员。','本章别处所有市政职业。','父母职业且无例子。'],
 ['A 最后一句明列三项。','B 无运动员例子。','C 不应把后文社工幼教并入当前电视回忆。','D 有明确职业，但未称皆父母职业。作者记忆不是已量化的代表性职业追踪；silver linings为依Solnit推论。'],
 ['Many said nurses, firefighters, and doctors.'],
 'silver linings','困境中的积极一面','不取消灾害破坏的潜在亮点比喻','They looked for silver linings without denying the loss.',['some silver linings','a silver lining in adversity'],
 '依Solnit，即使1995 Hanshin-Awaji这样毁灭性地震，也应有些困境中的亮点。我记得看1995年电视访问幸存儿童，问他们长大想做什么，许多人说护士、消防员、医生。')

add(14,'作者意图','What does this question propose for investigation?',
 ['That children had intentionally caused the earthquake.','Whether children’s perspectives and prosocial tendencies may have changed.','That every child had already become a doctor.','That Fujimoto had conducted the children’s experiment.'],1,
 '此问提出调查什么？',['孩子故意造成地震。','孩子视角及亲社会倾向是否可能改变。','每个孩子已成医生。','Fujimoto开展儿童实验。'],
 ['A 无此意思。','B is it possible 明示假说，made them more prosocial为待检验问题。','C 职业愿望非已实现任职。','D Fujimoto仅作此前人物对比。疑问不能写成此段已验证人人改变。'],
 ['is it possible that the devastating earthquake changed these children’s perspectives on life and made them more prosocial?'],
 'prosocial','亲社会的；有益于他人的','指关心帮助他人的倾向，非外向程度本身','The task measured prosocial behavior through giving.',['prosocial behavior','become more prosocial'],
 '像Staten Island的Takashi Fujimoto一样，有没有可能，毁灭性地震改变了这些孩子的人生视角，使他们更亲社会？')

add(15,'细节','How was the post-earthquake group obtained?',
 ['By retesting exactly the same children a decade later.','By recruiting only adults from another province.','By selecting a new group of six- and nine-year-olds from the same schools.','By asking only children whose homes were destroyed.'],2,
 '震后样本怎样取得？',['十年后重测同一批孩子。','只招另一省成人。','从同样学校取新一批六和九岁儿童。','只问住宅全毁者。'],
 ['A new group不是同个体，且震后一月。','B Chinese children in Sichuan不是外省成人。','C 年龄、学校和新组均准确。','D 未限定住宅全毁。四月震前与五月十二地震、之后一月时间要分开。'],
 ['One month after the earthquake, the researchers collected data from a new group of six- and nine-year-olds from the same schools.'],
 'altruistic','利他的','通过给出自身资源帮助同学来考察','The study examined altruistic giving among children.',['altruistic giving','data on altruistic giving'],
 '最直接证据可见Jean Decety及同事研究。他们2008年4月收集Sichuan六岁九岁儿童的利他给予资料。一月后，5月12日，7.9级地震袭击Sichuan。震后一月，他们从相同学校新一组六岁九岁儿童再收集数据。')

add(16,'推断','What assumption underlies the natural-experiment interpretation?',
 ['The earthquake was deliberately randomly assigned.','Every child’s characteristics were proved identical.','The two groups consisted of the same individuals.','The groups were presumed comparable apart from experiencing the earthquake.'],3,
 '自然实验解释基于什么假定？',['地震被刻意随机分配。','每个孩子特征证明完全一致。','两组是同一批个体。','推定两组除经历地震外可比。'],
 ['A as if randomly不是研究者安排灾难。','B presumably是推定，非全部特征实证完全相同。','C 前段是new group。','D 括号具体解释可比性假定；保留sort of/as if限定，非无条件随机试验。'],
 ['were presumably no different from the children in the post-earthquake study in any other ways except for having experienced the major earthquake'],
 'presumably','推定地；大概','可比性的推定，不是假定已证明所有混杂不存在','The groups were presumably comparable before the event.',['presumably no different','chosen as if randomly'],
 '这构成某种自然实验，震前震后条件的参与者仿佛随机选择。也就是说，推定两批孩子除经历大地震外，其他方面没有差别。')

add(17,'细节','What donation opportunity did each child receive?',
 ['They could voluntarily give some of their chosen ten stickers.','They were required to donate all one hundred stickers.','They could donate only stickers they had not chosen.','They had to buy stickers with their own money.'],0,
 '每个孩子获什么捐赠机会？',['可自愿捐所选十张中的一些。','必须全捐一百张。','只能捐没选的贴纸。','须用自己的钱购买。'],
 ['A if they wanted...out of the ten 明示自主与资源范围。','B 一百是可挑总量，十张是获得量，无强制全捐。','C out of ten they received相反。','D 由任务提供，不是付钱买。没有把自愿捐赠改成服从要求。'],
 ['if they wanted to donate some stickers out of the ten they had received, they could.'],
 'donate','捐赠；给出以帮助他人','从自己的十张中自愿给没有获选的同学','The children could donate part of their stickers.',['donate some stickers','donate out of one’s own share'],
 '实验每次邀一名儿童到校内安静房间，由女性研究者接待，说可从一百张选十张给自己。选好最爱十张后，告知部分同学未获选玩游戏、不会得到贴纸。不过若愿意，可从获给的十张中捐一些。')

add(18,'细节','What change was reported for nine-year-olds’ average donations?',
 ['From four of one hundred to one of one hundred.','From ten stickers to no stickers.','From slightly over one of ten to about four of ten.','Exactly four stickers from every child before and after.'],2,
 '九岁儿童平均捐赠怎样变化？',['百张中四变一。','十变零。','十张中略多于一变约四。','每个孩子震前后都恰四张。'],
 ['A 分母十非一百，方向亦反。','B 没有从全捐到零。','C on average/slightly/about与前后时点均保留。','D 平均不是人人精确值；此段只给九岁结果，不能编造六岁结果或持久年限。计数是行为测量，不是自陈利他。'],
 ['nine-year-olds gave, on average, slightly more than one out of the ten stickers.','nine-year-olds gave, on average, about four out of the ten stickers.'],
 'anonymous','匿名的；未指明身份的','接收同学身份未透露，区别于研究者是否知道捐者','The stickers were intended for an anonymous classmate.',['an anonymous classmate','an anonymous recipient'],
 '他们拿空信封，装想捐给一名匿名同学的贴纸。结束后，研究者数捐出数量，作为利他给予的行为测量。震前九岁儿童平均捐十张中略多于一张；震后一月平均约四张。')

add(19,'细节','What evidence was examined in the Kobe–Tokyo comparison?',
 ['Only personal interviews with the same schoolchildren.','Municipal job-application trends from 1989 to 2000.','Applications to every private company worldwide.','Hospital records from the 1906 earthquake.'],1,
 'Kobe–Tokyo比较考察什么证据？',['只访问同一批小学生。','1989–2000市政职位申请趋势。','全球所有私企申请。','1906地震医院记录。'],
 ['A 是职业资料，与贴纸儿童研究不同。','B 时间、尺度明确；社工消防员幼教为市政招聘例子。','C 非全球私企。','D 不是1906事件。Kobe有大地震、Tokyo该期没有该大地震，是比较基础而非保证地区所有条件相同。'],
 ['trends in job applications at the municipality level from 1989 to 2000 in the Kobe and Tokyo areas'],
 'municipality','市镇；地方市政单位','日本这些岗位由地方政府层面招聘','The municipality advertised several public-service posts.',['municipality level','municipal jobs'],
 '灾难对价值和职业偏好的长期影响还有别的证据吗？我们看1989–2000 Kobe和Tokyo地方市政求职趋势，区别在于前者该期经历大地震而后者没有。考察社工、消防员、幼教申请人数，这些岗位在日本由市政层面招聘。')

add(20,'推断','What finding supports the author’s interpretation about prosocial jobs?',
 ['Applications fell equally in both areas.','Every Kobe resident became a firefighter.','There were no changes anywhere in 1995.','Applicants per position rose sharply in Kobe in 1995, unlike Tokyo.'],3,
 '什么发现支持作者对亲社会职业的解释？',['两地申请同样下降。','每个居民成消防员。','1995到处没变化。','Kobe1995每岗申请者剧增，Tokyo没同样现象。'],
 ['A soared是上升，非下降。','B 岗位申请非全体居民实际入职。','C Kobe明确变化。','D applicants per position保留分母；suggest是对趋势解释，不等于随机证明地震导致每个人职业转向。'],
 ['the number of applicants per position soared in 1995 in the Kobe area, but not in the Tokyo area.'],
 'soared','激增；迅速上升','每个职位申请人数上升，而非岗位本身数目必上升','The number of applicants per position soared.',['applications soared','soar in a particular year'],
 '我们发现，1995 Kobe每个岗位的申请者数剧增，Tokyo没有。发现提示地震使亲社会工作更具吸引力。')

add(21,'主旨','What warning accompanies the discussion of prosocial change?',
 ['Survivors’ losses can have lasting effects on well-being and ordinary life.','Every survivor necessarily forgets the tragedy within months.','Physical symptoms were absent sixteen years later.','The author recommends seeking disasters for happiness.'],0,
 '亲社会改变讨论同时带来什么提醒？',['幸存者损失会长期影响福祉与正常生活。','每人几月内必忘悲剧。','十六年后无身体症状。','作者建议为快乐追求灾难。'],
 ['A long-lasting/ingrained/rob them承认长期伤害。','B 记入身份人生故事，非全忘。','C more physical symptoms相反。','D No one wishes表明无人愿受，不给追求灾难建议。不能以亲社会可能性抵销损害。'],
 ['the negative effects of natural disasters on the well-being of survivors are long-lasting.'],
 'ingrained','深嵌的；根深蒂固的','悲剧进入身份与人生故事，不是短暂擦过','The memory became ingrained in the family’s story.',['ingrained in identities','ingrained in life stories'],
 '记住，十六年后，失去住宅的Kobe居民仍比无房损者满意较低、身体症状更多。灾难对幸存者福祉的负面影响长久。悲剧嵌入身份与人生故事，可夺走幸福和常态。没人想受这种悲剧。')

add(22,'语境词义','What does “a treasure amidst ruins” suggest in this argument?',
 ['All losses have been compensated financially.','There can be valuable perspective changes without denying devastation.','Ruined buildings literally contain hidden gold.','Every survivor must feel grateful for disaster.'],1,
 'treasure amidst ruins 在论证中暗示什么？',['一切损失已财务补足。','不否认破坏也可能有珍贵视角变化。','废墟字面藏金。','每位幸存者必须感激灾难。'],
 ['A 没有赔偿结论。','B could mean/more prosocial把潜在丰富比作珍宝，并不取消痛苦。','C 语境是心理变化，非考古宝藏。','D many/could不等于人人必须，不能强加受害者感恩义务。幸福不可能是even if条件，不是声明所有人永不快乐。'],
 ['The change of perspective experienced by earthquake survivors could mean that their lives are now psychologically richer than before.'],
 'antidotes','缓解或对抗某物的力量','对悲伤的比喻性应对，非临床药物处方','Community support can serve as an antidote to isolation.',['antidotes to grief','a treasure amidst ruins'],
 '然而，即使灾后无法幸福，幸存者仍能过好人生。艰难时人性一些最好品质可对抗悲伤，许多人更亲社会。视角改变可能意味着人生比从前心理更丰富。他们发现“废墟中的珍宝”。')

add(23,'细节','How is exposure to COVID-19 defined in the study described?',
 ['Only the respondent’s own confirmed infection.','Anyone who had heard about the pandemic.','Diagnosis or death involving the respondent, a family member or an acquaintance.','Only employment in a hospital.'],2,
 '该研究怎样界定接触COVID-19？',['仅本人确认感染。','任何听说疫情的人。','本人、家人或熟人获诊断或死亡的经历。','只限医院工作。'],
 ['A 明列family member/acquaintance，范围更广。','B hearing不是所给操作定义。','C 括号准确界定，不能统一改成全体本人患病。','D 无职业限定。研究比较既有接触与未接触，未说随机感染分组。'],
 ['respondents themselves, a family member, or an acquaintance diagnosed with or died from COVID-19'],
 'acquaintance','熟人；认识的人','比家属更广的认识对象，非必为亲密好友','An acquaintance shared news of the experience.',['a family member or an acquaintance','an acquaintance diagnosed with'],
 'COVID-19扰乱生活工作。它改变世界观了吗？增加心理丰富了吗？一项研究考察疫情早期接触过COVID-19者，即本人、家人或熟人确诊或死于COVID-19，是否比未接触者表现更多亲社会行为。')

add(24,'细节','Which donation arrangement is accurately described?',
 ['Every participant received both $5 and €4.','Only international charities were permitted.','The researchers kept half of each donation.','Participants could donate part of a country-specific bonus, and donations would be doubled.'],3,
 '哪项准确描述捐款安排？',['每人同时拿五美元四欧元。','只许国际慈善。','研究者留下一半捐款。','可捐所在国对应奖金一部分，捐款获加倍。'],
 ['A 美国五美元、意大利四欧元，不是同人两份。','B 地方、全国、国际均可。','C doubled是加倍非抽一半。','D 金额安排、选择和匹配准确；更多人愿捐与捐得更多是两个结果。疫情接触非随机操纵，不由此保证感染改善道德。'],
 ['the amount they donated would be doubled by the researcher.'],
 'monetary','金钱的；货币形式的','意外奖金作为可捐资源，非健康改善奖赏','Participants received an unexpected monetary bonus.',['monetary bonus','donate some of the money'],
 '参与者获意外奖金，美国五美元，意大利四欧元，再问是否捐一部分给所在地慈善、全国慈善或国际慈善。研究者告知捐额会加倍。两国接触过COVID-19者，不只比未接触者更可能捐，也捐得更多。')

add(25,'作者意图','What interpretation does the author draw from the preceding findings?',
 ['Personal COVID-19 experience shifted values in a prosocial direction.','Every victim became equally generous forever.','The study randomly infected participants to improve values.','The findings establish a treatment recommendation.'],0,
 '作者从前述结果作什么解释？',['个人COVID-19经历使价值趋于亲社会。','每位受害者永远同等慷慨。','研究随机感染参与者改善价值。','确立治疗建议。'],
 ['A 这是作者用made表达的解释；当前单句未提供独立因果识别，不能把既有接触比较升级为感染随机试验。','B 无人人同等及永远的支持。','C 没有随机感染设计。','D 价值方向论述不是医学治疗或鼓励感染。'],
 ['personal experience with COVID-19 made the victims change their values in a prosocial direction.'],
 'indicate','表明；提示','引出作者从结果作出的解释，不自动等于严密因果证明','The findings indicate a possible shift in priorities.',['findings indicate that','a prosocial direction'],
 '这些发现表明，COVID-19的个人经历使受害者的价值观朝亲社会方向改变。')

assert len(out)==25 and [q['id'] for q in out]==[t['questionId'] for t in targets]

def persist():
 path=ROOT/'source/short-questions/additional.json';existing=load('source/short-questions/additional.json');byid={q['id']:q for q in existing}
 for q in out:
  if q['id'] in byid:assert byid[q['id']]==q,('Refuse to overwrite changed authoring',q['id'])
  else:existing.append(q)
 path.write_text(json.dumps(existing,ensure_ascii=False,indent=2)+'\n',encoding='utf8',newline='\n')
 review=dict(batchId='batch-032',date='2026-10-23',pdfSha256=b['pdfSha256'],checkedPdfPages=list(range(126,131)),questionIds=[q['id'] for q in out],paragraphs=[dict(id=pid,textSha256=hashlib.sha256(pp[pid]['text'].encode()).hexdigest()) for pid in dict.fromkeys(q['paragraphId'] for q in out)],note='完整PDF126–130原页视觉核对及跨页拼接。Kobe物理修复和心理伤痕分开，调查波次与作者休假年分开，房损/失亲同时分析不作随机因果或变量全无关联。Solnit为引语/作者阐释，电视职业愿望为作者回忆。四川震前后为同校新组，as if/presumably保留，非研究者随机分配灾害；100供选/10获得/平均略逾1至约4为九岁结果，不补六岁或长期个体变化。市政申请按每职位且非实际就职，1989–2000与1995变化分开。COVID接触包括本人/家属/熟人，捐款奖金/加倍与结果分开，作者made价值解释不升级成随机感染因果或医学建议。承认长期损害，不强加受害者获益/感恩；不宣称逐句证据全覆盖。')
 (ROOT/'source/short-questions/review-chapter11-recovery25.json').write_text(json.dumps(review,ensure_ascii=False,indent=2)+'\n',encoding='utf8',newline='\n')
 print('Saved',len(out),'of 25 individually authored exercises')

if __name__=='__main__':persist()
