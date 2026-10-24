"""25 individually authored exercises for frozen targets, PDF pages 159-163.
Preserve printed English, source positions and all previously published questions.
"""
from pathlib import Path
import json,hashlib
ROOT=Path(__file__).resolve().parents[2]
load=lambda p:json.loads((ROOT/p).read_text(encoding='utf8'))
b=load('public/data/book.json');plan=load('public/data/reading-plan.json');targets=load('source/short-questions/batch040-targets.json')['targets']
ss={s['id']:s for s in b['sentences']};pp={p['id']:p for p in b['paragraphs']};out=[]
def add(i,kind,prompt,options,answer,prompt_zh,options_zh,analyses,quotes,word,meaning,context,example,collocations,translation,support='explicit'):
 t=targets[i-1];u=next(u for u in plan['units'] if u['id']==t['readingUnitId']);group=[ss[sid] for sid in u['sentenceIds']];p=pp[u['paragraphId']];text=p['text'][group[0]['start']:group[-1]['end']]
 assert hashlib.sha256(text.encode()).hexdigest()==t['passageSha256'];evidence=[]
 for quote in quotes:
  offset=text.find(quote);assert offset>=0,(i,quote);start=group[0]['start']+offset;end=start+len(quote);touching=[s for s in group if s['start']<end and s['end']>start]
  evidence.append(dict(quote=quote,sentenceIds=[s['id'] for s in touching],sources=list({(r['pdfPage'],r['block']):r for s in touching for r in s['sources']}.values())))
 assert word.lower() in text.lower(),(i,word)
 out.append(dict(id=t['questionId'],version=1,readingUnitId=u['id'],chapterId=u['chapterId'],sectionId=u['sectionId'],paragraphId=u['paragraphId'],sentenceIds=u['sentenceIds'],passage=text,prompt=prompt,options=options,answer=answer,type=kind,promptZh=prompt_zh,optionsZh=options_zh,analyses=analyses,evidence=evidence,vocabulary=[dict(word=word,meaning=meaning,context=context,example=example,collocations=collocations)],translation=translation,support=support,editorialStatus='完整PDF159–163原页视觉核对。温故知新是谚语非加热操作，B/Aron/Jiro证据类型分开；Jazz人物对话为能动性例子非控制世界的科学保证。James公式pretentions保留原拼写并依段释aspirations，happiness模型To simplify to extreme非精密诊断，文化emphasis非每位国民。Payscale超过两百万人502职业为问卷，满意和意义数字按职业/指标匹配；median薪资与average满意是职业聚合相关，不改成个人加薪因果。社工/警察工资解释might/perhaps保留，艺术职业丰富为My guess，Payscale未测该维，不把作者创造力对照扩成各职业所有个人绝无创造。旅行情境比较非实际旅游推荐，could great/disaster保持不确定。新确认160页块5作者开章正文误归引文，追加audit-c14-opening-p160-b005；连同144页开章正文待补入，现有候选池不代表全书正文完整。'))







add(1,'主旨','What idea does the proverb illustrate in this paragraph?',
 ['New knowledge requires abandoning everything old.','Studying familiar or old material can reveal something new.','Objects must be physically heated before they can be understood.','Only recent works can provide psychologically rich experiences.'],1,
 '这段谚语说明什么？',['新知识须抛弃一切旧物。','研习熟悉或古老材料也能发现新知。','物品必须先实际加热才可理解。','只有新作品才能带来心理丰富。'],
 ['A learn from studying something very old与全弃旧相反。','B 最后一句直接解释温故知新，旧材料与新发现可相连。','C warm old是谚语解读，不是加热操作或物理实验。','D often learn new from old不支持only recent。popular in Japan是本段对使用背景的说法，不据此编造谚语起源。'],
 ['We often learn something new from studying something very old.'],
 'proverb','谚语；格言','作为概括性智慧引入，而非测量数据或实验定律','The proverb reminds readers to revisit familiar ideas.',['a popular proverb','learn something new'],
 '日本有一句常用谚语：温故知新。第一个字是“温”，第二个“旧”，第三个“知识”，最后一个“新”。温习旧的，就会学到新的。我们经常能通过研习很古老的东西，学到新知。')

add(2,'作者意图','What common theme links B, Aron, and Jiro in this summary?',
 ['Each claims that recognition ends the need for further exploration.','Each recommends abandoning every long-term commitment.','Each provides the same kind of randomized experimental evidence.','Familiar commitments can be renewed through gratitude, novelty, or continued refinement.'],3,
 '总结中B、Aron与Jiro由什么共同主题连接？',['都说获认可便不必探索。','都建议抛弃所有长期承诺。','都给出相同随机实验证据。','熟悉承诺可通过感恩、新奇或持续精进更新。'],
 ['A even after三星仍完善反对此项。','B 婚姻与长期职业都说明留在熟悉对象内继续学习。','C B为哲学角色，Aron为研究，Jiro为个案，证据类型不能混同。','D 感恩心态、偶尔注入新奇与六十年完善技艺共同展示更新可能。作者说key是概述，不扩成所有关系唯一原因。'],
 ['with the right mindset of gratitude, we could all learn more about ourselves and our partner.','an occasional infusion of novelty in a long-term romantic relationship','even after getting a three-star rating from Michelin.'],
 'infusion','注入；添加','把适量新奇带入已有长期关系，而非必须更换伴侣','A small infusion of novelty changed their familiar routine.',['an infusion of novelty','relationship longevity'],
 '《Either/Or》的B相信婚姻神圣；抱持恰当的感恩心态，我们能更了解自己与伴侣。Art Aron的研究显示，偶尔向长期恋爱关系注入新奇，是关系长久的关键。Jiro Ono六十年来忙于完善寿司手艺，连获米其林三星后也如此。')

add(3,'主旨','What does the author suggest if someone does not want entirely new material?',
 ['Revisit old favorites and explore them more deeply.','Conclude that psychological richness is no longer possible.','Repeat the old experience while deliberately ignoring every difference.','Replace all artistic interests with one fixed interpretation.'],0,
 '不想接触全新材料时，作者建议什么？',['重访旧爱，深入探索。','认定再无心理丰富可能。','重复旧经历并刻意忽略差异。','以唯一固定解释取代全部艺术兴趣。'],
 ['A old favorites...haven’t engaged with...digging deeper给出具体替代途径。','B might discover something new and rich仍保留可能。','C noticing新东西的主题不是刻意忽略。','D 各艺术家experiment/evolved说明变化与多样，非只准固定解释。might是建议可能，不承诺每次重访必有发现。'],
 ['you might try old favorites that you haven’t engaged with for a long time. You might discover something new and rich.'],
 'engaged with','投入接触；认真欣赏研究','这里指再次阅读、聆听或研究旧爱作品，不是订婚','She engaged with the familiar novel more deeply on a second reading.',['engage with old favorites','dig deeper into work'],
 'Beatles、Bob Dylan、Aretha Franklin、Miles Davis、Picasso、Yayoi Kusama、Hilma af Klint、Kara Walker，都拥抱实验、尝试新风格，随时间演变。长期不断深入其作品，你能从每位艺术家学到新东西。若不想读、听或研究新材料，也许可以试试许久未接触的旧爱。你可能发现新的丰富之处。')

add(4,'细节','What surprises Violet in the recalled conversation?',
 ['Her hairdresser has forgotten the title of the novel.','She has already planned every change in the world.','The suggestion that she could imagine the world as she wants it.','A scientific claim that every external event is controllable.'],2,
 '回忆中的谈话，什么令Violet惊讶？',['理发师忘了小说名。','她早已规划世界一切变化。','她可以按自己希望的样子想象世界这一提议。','所有外部事件皆可控制的科学主张。'],
 ['A 没有忘记书名情节。','B thought had never crossed her mind与早已规划相反。','C hairdresser问make it up...want，引发她从未考虑的想法。','D 小说对话是能动性启发，不是证明人能控制所有客观事件的实验。末尾What’s the point的答话续后段，不补造结局。'],
 ['Violet is surprised by the question; the thought had never crossed her mind.'],
 'crossed her mind','进入她的脑海；被她想到','表示以前未考虑过这种可能，不是忘掉既有完整计划','The possibility had never crossed her mind.',['never crossed one’s mind','recall a conversation'],
 'Toni Morrison的《Jazz》近结尾时，主人公Violet回忆与理发师的一次谈话。理发师说：“如果你不能按自己想要的样子想象世界，那这世界对你有什么用？”Violet很惊讶，从没这样想过。“有什么意义呢？')

add(5,'逻辑关系','What tension is expressed in this continuation?',
 ['Both speakers agree that the life belongs to someone else.','An inability to change things is met with an insistence on owning one’s life.','The hairdresser promises that all external barriers have already disappeared.','The speakers abandon the topic of life for a discussion of money.'],1,
 '这段续文表达什么张力？',['两人都同意人生属于别人。','无力改变的看法，遇到坚持人生属于自己的回应。','理发师保证外部障碍已全消失。','两人转而谈钱。'],
 ['A mine/My life明确主张归属自己。','B I can’t change it与hairdresser insists...mine构成对照。','C 归属感不等于所有障碍已经消失。','D 本句无金钱议题。引文是小说人物话语，不能当网站对读者下达的强制命令。'],
 ['I can’t change it.','The hairdresser insists, “That’s the point…[I] forgot it was mine. My life.”'],
 'insists','坚持说；强调','理发师对人生主体性的回应，而非已测得的客观因果结论','She insists that the choice deserves careful thought.',['insist that','my life'],
 '“我改变不了它。”理发师坚持说：“问题就在这里……〔我〕忘了它本来是我的。我的人生。”')

add(6,'作者意图','Why does the author recommend reflection after milestones?',
 ['To encourage reviewing life along the way rather than waiting until its end.','To require everyone to judge life only by happiness.','To say that every desired change is fully under personal control.','To prohibit reflecting before finishing high school.'],0,
 '作者为什么建议里程碑后反思？',['鼓励沿途回顾，而非一直等到生命终点。','要求只用快乐评判人生。','声称所有想要的改变完全可控。','禁止高中毕业前反思。'],
 ['A Instead of waiting...deathbed/after each milestone直接说明时机对照。','B 列happiness/meaning/richness三个方向，不是only。','C 反思愿望不构成完全控制外界的保证。','D 高中例子不是反思的最低年龄限制。perhaps try保留建议语气，非强制执行指令。'],
 ['Instead of waiting until you’ve reached your deathbed, perhaps try to reflect after each milestone:'],
 'milestone','重要节点；里程碑','如高中结束等可回顾某阶段生活的节点','Finishing the project was a useful milestone for reflection.',['after each milestone','reflect on a life stage'],
 '若不按自己希望的样子思考世界，就会忘记这是自己的人生。所以别忘了，人生属于我们，我们想要比现状更多的东西：也许更多快乐、意义或心理丰富。与其等到临终，不如尝试在每个重要节点后反思：高中结束时，你会怎样评价自己的高中生活？')

add(7,'细节','What three dimensions does the model provide for evaluation?',
 ['Wealth, fame, and educational rank.','Work, marriage, and parenting as the only acceptable life paths.','Youth, middle age, and old age.','Happiness, meaning, and psychological richness.'],3,
 '模型提供哪三个评价维度？',['财富、名气、学历排名。','工作婚育三种唯一可接受道路。','青年、中年、老年。','快乐、意义、心理丰富。'],
 ['A 三项均不是这里给的模型名称。','B 工作、大学、育儿是阶段例子，不是模型三维，也非唯一路径。','C 不是按年龄段定义三维。','D 破折号内happiness/meaning/psychological richness直接列明。三个维度可用于不同经历，不要求每人有同样里程碑。'],
 ['The triad model of a good life—happiness, meaning, and psychological richness—gives you three dimensions'],
 'triad','三元组；三个相联部分','在这里指好人生模型的三个评价面向','The framework uses a triad of complementary ideas.',['a triad model','evaluate experiences'],
 '大学结束时，你会怎样看大学生活？第一份工作结束时呢？孩子高中毕业时，你又怎样看自己的育儿经历？好人生的三元模型——快乐、意义、心理丰富——提供三个可用来评价经历的维度。')

add(8,'语境词义','What does “pretentions” mean in James’s equation as explained here?',
 ['Achievements already completed.','Other people’s judgments of one’s intelligence.','A person’s aspirations.','The total number of years a person has worked.'],2,
 '本段解释中，James公式的pretentions是什么意思？',['已完成成就。','别人对自己智力的判断。','个人抱负或期望。','工作总年数。'],
 ['A success是分子，aspirations为这里解释的分母，不能互换。','B 作者明确定义，非他人智力评价。','C By pretentions...aspirations直接释义；保留PDF拼写pretentions，不擅改原文。','D 没有工作年限变量。公式是此段历史理论表述，不是对所有心理状况的精密诊断工具。'],
 ['By pretentions, James meant one’s aspirations.'],
 'aspirations','抱负；所期望达成的目标','公式中用以衡量成功相对程度的期望，不是已经获得的成果','Her aspirations changed as she gained experience.',['fulfil aspirations','success divided by aspirations'],
 '1890年，William James在《The Principles of Psychology》中提出自尊公式：“self-esteem = success/pretentions”。他用pretentions指个人抱负。因此，达成大多数抱负时自尊高，没达成时低。按这公式，有两种提升自尊的方法。')

add(9,'逻辑关系','Within the author’s deliberately simplified analogy, which two changes could increase happiness?',
 ['More success or lower aspirations.','Less success or higher aspirations.','More success only, with aspirations irrelevant.','Changing the definition of interpersonal success to exclude other people.'],0,
 '在作者刻意简化的类比中，哪两种改变可能提高快乐？',['增加成功，或降低抱负。','减少成功，或提高抱负。','只能增成功，抱负无关。','重新定义人际成功以排除他人。'],
 ['A increase...success/reduce aspiration直接对应分子和分母两种变化。','B 将两个变化方向都倒置。','C other way明确第二路，非only。','D personal/interpersonal/societal是成功的层面，不是排除人际关系。could及simplify to extreme限定为简化框架，不升级成人人通用精确幸福计算。'],
 ['One is to increase the amount of success. The other way is to reduce aspiration.','To simplify to the extreme'],
 'to simplify to the extreme','极度简化地说','作者主动承认模型简化，不能删掉这一限定','To simplify to the extreme, the model compares outcomes with expectations.',['reduce aspiration','a simplified function'],
 '一种是增加成功量，另一种是降低抱负。James的自尊公式也可以用于快乐。若极度简化，可以把快乐写成两因素的函数：成功（个人、人际或社会层面）除以抱负。')

add(10,'细节','How does the author contrast the cultural emphases?',
 ['Americans minimize aspirations, while Danes focus only on harder work.','American emphasis is on increasing success; Danish emphasis is on minimizing aspirations.','Both cultures are said to prohibit changing aspirations.','Every individual in each country is proved to follow the same strategy.'],1,
 '作者怎样概括两种文化侧重？',['美国人降期望，丹麦只强调更努力。','美国侧重增加成功，丹麦侧重降低抱负。','两文化都禁止调整期望。','已证明每个个体策略完全相同。'],
 ['A 将国家与策略互换。','B enhancing success与minimizing aspirations分别对应作者概括。','C 前句明确可以reducing aspirations，非禁止。','D cultural emphasis不是每位国民都如此的实验结论，也没有确证所有人的幸福变化。'],
 ['The American cultural emphasis is on enhancing the amount of success by working harder, whereas the Danish cultural emphasis, for instance, is on minimizing aspirations.'],
 'emphasis','侧重；强调点','文化概括层面的倾向，不能抹去个体差异','The two approaches differ in emphasis.',['cultural emphasis','whereas'],
 '人可以通过增加成功或降低抱负来提高快乐。美国文化侧重努力工作、扩大成功；丹麦文化则比如更侧重降低抱负。')

add(11,'作者意图','What role does the reference to Freud play?',
 ['It provides a detailed comparison of all possible forms of success.','It reports a new controlled experiment involving work and love.','It shows that the chapter will no longer discuss work.','It introduces work and love before narrowing attention to success at work.'],3,
 '提Freud起什么作用？',['详细比较所有成功形式。','报告新的工作爱情控制实验。','说明本章不再谈工作。','先引入工作与爱，再缩焦到工作成功。'],
 ['A two main tasks是引述的概括，不是穷尽所有成功形式的细比较。','B said不是开展新实验。','C So let’s look...work明确接着谈工作。','D questions about kinds of success→Freud work/love→success at work形成过渡。likely不是工作爱情顺利必然囊括每人的全部人生价值。'],
 ['the two main tasks of humans are to work and to love.','So let’s look at success at work.'],
 'likely','可能；很有可能','限定成功于工作和爱情与人生成功的关系，不是绝对保证','A useful framework is likely to raise further questions.',['have likely succeeded','success at work'],
 '不过，我们谈的是什么成功？Sigmund Freud说，人类两个主要任务是工作与爱。如果工作和爱情都成功，你很可能在人生中成功了。那么，来看工作上的成功。')

add(12,'细节','What is one way of defining success at work in this passage?',
 ['Counting only how many job categories exist.','Assigning workers to jobs randomly.','Asking workers how satisfied they are with their jobs.','Ignoring workers’ own judgments and using salary alone.'],2,
 '本段提出怎样一种定义工作成功的方法？',['只数职业类别。','随机分配工作。','问劳动者对工作多满意。','忽略本人判断，只看工资。'],
 ['A 502是调查职业类别数，不是个体成功判据。','B 分析问卷未说随机安排职业。','C one way...ask...satisfied直接支持；many ways说明非唯一。','D 本段采用主观满意度，并非只以薪水替代。two million是超过两百万人，不能改成502位受访者。'],
 ['one way is to ask workers how satisfied they are with their jobs.','Payscale’s survey of over two million people in 502 job categories.'],
 'survey','调查；问卷资料','作者分析的大样本工作问卷，不是职业随机实验','The survey asked workers about job satisfaction.',['analyze a survey','job categories'],
 '定义工作成功的方法很多，其中一种是问劳动者多满意自己的工作。说满意的人，就被视为在工作中成功。我分析了Payscale对超过两百万人、502类职业的调查。按这些资料，什么能预测工作满意度？')

add(13,'同义改写','What does the question ask more specifically?',
 ['Which kinds of workers show job satisfaction above the average.','Which individual worker has the highest salary in the world.','Why every worker must enjoy the same job.','How many people refuse all forms of employment.'],0,
 '这个问题更具体地问什么？',['哪些类别劳动者的工作满意度高于平均。','世界上哪位个人工资最高。','为什么每人必须喜欢同样工作。','多少人拒绝所有工作。'],
 ['A kinds of workers与higher-than-average逐项对应，保留群体和比较基准。','B job satisfaction非工资，above average也非全球第一。','C 原文问差异，不是规定都喜欢同职。','D 没问失业或拒绝就业人数。问句本身没有给哪类最高的结果。'],
 ['what kinds of workers have higher-than-average job satisfaction?'],
 'higher-than-average','高于平均水平的','用平均满意度作比较基准，不等于人人都满意','The group reported higher-than-average satisfaction.',['higher-than-average satisfaction','more precisely'],
 '更准确地说，哪些类型的劳动者，其工作满意度高于平均水平？')

add(14,'细节','Which pair of satisfaction rates matches the passage?',
 ['Actuaries 59%; social workers 80%.','Police officers 78%; computer scientists 65%.','Actuaries 80%; social workers 59%.','All four occupational groups 80%.'],2,
 '哪组满意比例与本段一致？',['精算师59%，社工80%。','警察78%，计算机科学家65%。','精算师80%，社工59%。','四组全80%。'],
 ['A 把精算师与社工比例倒置。','B 78属于计算机及信息科学家，65属于警察，错配。','C 两数字与群体直接对应；另外两组78与65不同。','D 比例明确不同，更不是每个人都满意。数据是作者引用调查，非本网站更新的今日职业排名。'],
 ['80 percent of actuaries are satisfied with their jobs.','Social workers were even worse, at only 59 percent satisfied.'],
 'actuaries','精算师','此处职业类别，比例描述该调查组满意度，不是人人人生幸福','The survey compared actuaries with other occupational groups.',['actuaries’ job satisfaction','percent satisfied'],
 '例如，80%的精算师满意工作。类似地，78%的计算机与信息科学家满意。相比之下，警察只有65%满意。社工更低，只有59%。')

add(15,'推断','How is pay presented as an explanation of the differences?',
 ['As the only cause already proved by random assignment.','As one possible reason, with perceived unfair compensation suggested.','As completely unrelated to what workers do.','As a finding that all four groups receive identical salaries.'],1,
 '工资被怎样用来解释差别？',['随机分配已证实的唯一原因。','一个可能原因，并猜想报酬不公平感。','与工作内容完全无关。','发现四组工资完全相等。'],
 ['A might be one reason与Perhaps都保留可能性，非随机因果或唯一原因。','B 文本用困难工作与报酬不高推测感到补偿不公。','C Given the difficult jobs正联系工作要求与报酬。','D 没有报四组薪水相同的数据。题目理解的是作者解释强度，不提供个人职业收入建议。'],
 ['Pay might be one reason.','Perhaps they feel they are not fairly compensated for what they do.'],
 'compensated','得到报酬；获得补偿','指劳动付出与工资是否相称的感受，不是已确认的法律赔偿','They felt fairly compensated for the demanding work.',['fairly compensated','might be one reason'],
 '为什么精算师和计算机科学家，比社工和警察更满意工作？工资可能是一个原因。考虑到社工和警察每天做的困难工作，他们薪水并不高。也许，他们觉得自己的付出没有得到公平报酬。',support='limited-inference')

add(16,'逻辑关系','Which conclusion stays within the association reported here?',
 ['Raising any individual’s salary will certainly increase satisfaction by the same amount.','Salary was unrelated to satisfaction across the categories.','Every high-paid individual was more satisfied than every low-paid individual.','Across 502 job categories, median salary and average satisfaction were strongly related.'],3,
 '哪项结论不超出本句的关联？',['每个人加薪都必等幅提高满意。','各类别薪资与满意无关。','每位高薪者都比每位低薪者满意。','502职业类别间，中位工资与平均满意度强相关。'],
 ['A correlated不能单独确证个体加薪因果，更无相同效果大小。','B strongly correlated与无关相反。','C 群体汇总关联不保证任意两个个体排序。','D 保留across502jobs的聚合层级，median salary与average satisfaction的指标也未混换。'],
 ['across 502 jobs, median salary was strongly correlated with average job satisfaction.'],
 'correlated with','与……相关联','统计共同变化，区别于单向因果证明','Across the categories, income was correlated with reported satisfaction.',['strongly correlated with','median salary'],
 '确实，在502类职业之间，中位工资与平均工作满意度强相关。')

add(17,'主旨','Why does the author turn from job satisfaction to meaning?',
 ['To show that satisfaction is only one dimension of work success.','To claim that the survey had never asked about meaning.','To say that satisfied workers must also find work highly meaningful.','To replace every occupational comparison with salary rankings.'],0,
 '作者为何从工作满意转向意义？',['说明满意只是工作成功的一个维度。','声称调查从没问意义。','声称满意者必高度感到工作有意义。','用薪水排名取代所有职业比较。'],
 ['A not the only way连接好人生不只快乐，提出另一个工作评价维度。','B Payscale measured this明确测了意义。','C satisfied yet many not very meaningful显示可能分离。','D 此处扩展评价，不是仅薪水。'],
 ['job satisfaction is not the only way to define success at work.','many of them do not find their jobs to be very meaningful.'],
 'meaningful','有意义的；有价值感的','区别于对工作是否满意，两个主观评价可不一致','The work was difficult but meaningful to her.',['find work meaningful','define success'],
 '正如快乐不是好人生的唯一道路，工作满意也不是工作成功的唯一定义。那么，工作中的意义呢？有趣的是，Payscale测了它。虽然绝大多数精算师与计算机科学家满意工作，其中许多人并不觉得工作很有意义。')

add(18,'细节','Which comparison of meaning rates is correct?',
 ['Actuaries 81%; law enforcement officers 36%.','Social workers 73%; law enforcement officers 81%.','Computer and information scientists 73%; social workers 45%.','All groups had the same meaning and satisfaction rates.'],1,
 '哪项工作意义比例比较正确？',['精算师81%，执法人员36%。','社工73%，执法人员81%。','计算机信息科学家73%，社工45%。','各组意义与满意比例全相同。'],
 ['A 36属于精算师，81属于执法人员，位置颠倒。','B 最后一句直接给73/81；精算师36、计算机与信息科学家45。','C 职业与数字交换。','D 作者正展示满意与意义两维有别，不是都相同。不能由两个比例相减断定具体哪些个人同时满足两项。'],
 ['73 percent of social workers and 81 percent of law enforcement officers find their jobs to be meaningful.'],
 'In contrast','相比之下；与此相反','转换到另一组职业，以对比意义与满意的不同模式','The first group reported comfort. In contrast, the second emphasized purpose.',['in contrast','find meaning in work'],
 '例如，只有36%的精算师觉得工作有意义，计算机与信息科学家也只有45%。相较之下，社工与警察虽然不特别满意工作，却觉得有意义。确实，73%的社工与81%的执法人员觉得自己的工作有意义。')

add(19,'细节','Which figures belong to art directors in this passage?',
 ['65% satisfied and 42% finding meaning.','35% satisfied and 67% finding meaning.','67% satisfied and 35% finding meaning.','42% satisfied and 65% finding meaning.'],2,
 '本段哪些数字属于艺术总监？',['65%满意，42%有意义。','35%满意，67%有意义。','67%满意，35%有意义。','42%满意，65%有意义。'],
 ['A 这两数属于编辑，不是艺术总监。','B 把艺术总监的两个评价维度对换。','C Similarly后明确67满意、35意义。','D 不仅错用编辑数字，还交换指标。低于其他职业不等于所有从业者都不喜欢工作。'],
 ['67 percent of art directors are satisfied with their jobs, but only 35 percent find their work meaningful.'],
 'pattern','模式；呈现出的规律','资料中不同职业满意与意义比例形成的分布，不是统计因果证明','The data showed a pattern across occupations.',['an interesting pattern','job satisfaction'],
 '不过，有没有工作虽然满意度或意义不高，仍是好工作？Payscale资料显示一个有趣模式：65%的编辑觉得工作令人满意，只有42%觉得有意义。类似地，67%的艺术总监满意工作，只有35%觉得有意义。')

add(20,'逻辑关系','Why are funeral directors an interesting comparison group?',
 ['They have exactly the same meaning rate as writers.','They report much lower satisfaction and meaning in both measures.','They are the only group asked about creativity in the survey.','Their satisfaction rate is similar to writers’, but their meaning rate is much higher.'],3,
 '为何把殡葬主管作为有趣对照？',['与作家意义率完全同。','两指标都低得多。','是调查唯一被问创造力的组。','满意率与作家相近，意义率高得多。'],
 ['A 作家30%，殡葬主管87%，并不相同。','B 68满意略高于67，87意义远高于30。','C 本段没问创造力；后段还明确调查未问。','D similar...satisfaction与However...meaning构成所述对照。similar非精确相同，也不是给个人换职的指令。'],
 ['67 percent in satisfaction and 30 percent in meaning.','68 percent of funeral directors are satisfied with their jobs. However, 87 percent of them find their jobs to be meaningful.'],
 'comparison group','比较组；对照对象','这里是调查中另一职业群体，非必然随机实验控制组','The researchers used another occupation as a comparison group.',['an interesting comparison group','in terms of satisfaction'],
 '作家和作者与艺术总监很相似：满意67%，意义30%。殡葬主管是有趣的比较组。他们工作满意度相近，68%满意；但87%觉得工作有意义。')

add(21,'作者意图','Why does the author resist recommending a switch based only on satisfaction and meaning?',
 ['Those two measures omit qualities such as creativity, which the survey did not assess.','The survey proved that all creative jobs are highly psychologically rich.','The occupational groups were identical on every unmeasured characteristic.','The author believes salary is the only legitimate work metric.'],0,
 '作者为何不愿只凭满意和意义建议转职？',['这两指标遗漏创造力等特质，调查也没测。','调查已证明所有创意工作心理丰富很高。','各组所有未测特征都相同。','作者认为工资是唯一合法指标。'],
 ['A self-expression/creativity加did not ask指出评价框架和测量缺口。','B 未问心理丰富相关问题，不能把猜想说成已测结果。','C 没有未测特征完全一样的证据。','D 作者正主张多维，不是只薪水。对殡葬主管的创造力对照属于作者这里的论述，不能扩成任何该职业者都无创造性的普遍事实。'],
 ['Payscale did not ask survey respondents how interesting their jobs were, how much creativity mattered in their jobs, or other questions pertaining to psychological richness.'],
 'pertaining to','关于；涉及','明确哪些心理丰富相关内容没有被该问卷覆盖','The questionnaire omitted items pertaining to creativity.',['pertaining to psychological richness','self-expression and creativity'],
 '如果满意与意义是好工作的唯一指标，我们也许会建议艺术总监、编辑和作家考虑做殡葬主管。实际我们不会，因为知道前几类有殡葬主管所没有的东西：自我表达和创造力。Payscale没有问工作多有趣、创造力多重要，或其他心理丰富相关问题。（职业对照保留作者表述，不作该职业全体个人能力断言。）')

add(22,'推断','How should the claim about creative jobs’ richness be classified?',
 ['A directly measured result from the Payscale richness scale.','A guarantee that every worker in these professions should remain there.','The author’s hypothesis, used to illustrate the three-dimensional framework.','A finding that happiness and meaning never matter at work.'],2,
 '关于创意职业心理丰富的说法应怎样分类？',['Payscale丰富量表直接测得。','保证每位该职业者都应留下。','作者假说，用于说明三维框架。','发现快乐意义对工作从不重要。'],
 ['A My guess/would与先前未测丰富的限定否定直接量表发现。','B many/may非every或职业处方。','C 猜想某些职业虽不高快乐或意义仍可能丰富，体现框架解释价值。','D 把补充第三维偷换成删除前两维。could still be good保留可能，而非职业价值普遍排名。'],
 ['My guess is that many art directors, editors, and writers would say that their jobs are interesting, creative, and psychologically rich.','This may be a reason why people continue in such professions.'],
 'professional sphere','职业领域','把好人生三维框架应用到工作，而非另一个社会数据库','The discussion applied the idea to the professional sphere.',['the professional sphere','my guess is that'],
 '我猜，许多艺术总监、编辑和作家会说，工作有趣、有创意、心理丰富。这可能是人们继续从事这些职业的一个原因。用三维框架定义好人生的益处，是它也可用于职业领域，解释为何某些快乐或意义不高的工作，仍可能是好工作——心理丰富的工作。',support='limited-inference')

add(23,'细节','How is the all-inclusive tour initially characterized?',
 ['Travelers must invent every part of the itinerary themselves.','Travelers pay and arrive, while the company supplies a plan.','It necessarily costs less than every backpacking trip.','The company guarantees that travelers will discover nothing unfamiliar.'],1,
 '本段首先怎样描述全包旅行？',['游客须自行设计全部行程。','游客付款到场，公司提供计划。','必比每次背包游便宜。','公司保证毫无陌生发现。'],
 ['A 有公司plan，非游客安排每件事。','B pay/show up及company has a plan直接支持。','C luxury不提供相对于所有背包行程的价格数据。','D 没有关于绝无新奇的保证。本段是比较情境，不是为读者推荐或预订实际旅游产品。'],
 ['All you have to do is pay and show up. The tour company has a plan.'],
 'all-inclusive','全包式的；主要项目统一安排的','指旅行情境里由公司计划安排，非这里对某商品合同的核验','They chose an all-inclusive tour with a planned itinerary.',['an all-inclusive tour','pay and show up'],
 '下次假期，你想参加全包豪华旅行，还是朴素背包游？全包旅行很轻松：只需付钱并到场，旅行公司已有计划。')

add(24,'逻辑关系','What contrast is made between the two travel arrangements?',
 ['Backpacking removes all uncertainty about accommodation.','Both arrangements require exactly the same amount of personal planning.','The organized tour requires more independent planning than backpacking.','The organized tour provides entertainment, while backpackers face uncertain accommodation and self-planning.'],3,
 '两种旅行安排形成什么对照？',['背包游消除住宿全部不确定。','两者个人规划工作完全同。','团队游比背包游需更多自主规划。','组织游提供娱乐，背包游面对住宿未知并自做规划。'],
 ['A don’t know what kind of accommodations明确不确定。','B pretty much everything by yourself突出背包规划负担。','C 把两边安排与自主负担颠倒。','D morning-to-night entertainment对照住宿未知/自行规划。harder不必然等于毫无价值，段中也没给最终体验结果。'],
 ['They’ll entertain you from morning to night','You don’t know what kind of accommodations you’ll end up with. You have to plan pretty much everything by yourself.'],
 'accommodations','住宿；住处安排','背包情境中最终能住什么样地方尚不确定','They were unsure what accommodations they would find.',['find accommodations','plan by yourself'],
 '他们从早到晚安排娱乐，你只管坐着享受。背包游却难得多：你不知道最终会住到怎样的地方，几乎一切都得自己规划。')

add(25,'语境词义','What does “It’s all on you” mean in this context?',
 ['You bear responsibility for the arrangements and their uncertain outcome.','Every successful trip is funded by someone else.','The trip has already been proved to be a disaster.','There is no possibility of a good experience.'],0,
 '这里It’s all on you是什么意思？',['安排及不确定结果的责任由你承担。','每次成功旅行都由别人资助。','已经证明行程灾难。','绝无良好体验可能。'],
 ['A all on you承接自主规划，could great/could disaster同时保留两端可能。','B on you是责任，不是在说他人付款。','C could also不是已经发生。','D could be great明确仍可能很好。不要把不确定性误写成失败已定。'],
 ['It’s all on you: it could be great, but it could also be a disaster.'],
 'on you','由你负责；责任在你','此处承接背包旅程的自主安排，不是东西物理压在身上','The final decision is on you.',['it is all on you','could be great'],
 '一切都由你负责：它可能很棒，也可能成为一场灾难。')

assert len(out)==25 and [q['id'] for q in out]==[t['questionId'] for t in targets]

def persist():
 path=ROOT/'source/short-questions/additional.json';existing=load('source/short-questions/additional.json');byid={q['id']:q for q in existing}
 for q in out:
  if q['id'] in byid:assert byid[q['id']]==q,('Refuse to overwrite changed authoring',q['id'])
  else:existing.append(q)
 path.write_text(json.dumps(existing,ensure_ascii=False,indent=2)+'\n',encoding='utf8',newline='\n')
 review=dict(batchId='batch-040',date='2026-10-24',pdfSha256=b['pdfSha256'],checkedPdfPages=list(range(159,164)),questionIds=[q['id'] for q in out],paragraphs=[dict(id=pid,textSha256=hashlib.sha256(pp[pid]['text'].encode()).hexdigest()) for pid in dict.fromkeys(q['paragraphId'] for q in out)],note='完整PDF159–163原页视觉核对。温故知新是谚语非加热操作，B/Aron/Jiro证据类型分开；Jazz人物对话为能动性例子非控制世界的科学保证。James公式pretentions保留原拼写并依段释aspirations，happiness模型To simplify to extreme非精密诊断，文化emphasis非每位国民。Payscale超过两百万人502职业为问卷，满意和意义数字按职业/指标匹配；median薪资与average满意是职业聚合相关，不改成个人加薪因果。社工/警察工资解释might/perhaps保留，艺术职业丰富为My guess，Payscale未测该维，不把作者创造力对照扩成各职业所有个人绝无创造。旅行情境比较非实际旅游推荐，could great/disaster保持不确定。新确认160页块5作者开章正文误归引文，追加audit-c14-opening-p160-b005；连同144页开章正文待补入，现有候选池不代表全书正文完整。')
 (ROOT/'source/short-questions/review-chapter13-14-evaluation25.json').write_text(json.dumps(review,ensure_ascii=False,indent=2)+'\n',encoding='utf8',newline='\n')
 print('Saved',len(out),'of 25 individually authored exercises')

if __name__=='__main__':persist()
