"""25 individually authored exercises for frozen targets, PDF pages 81-85.
Preserve printed English, source positions and all previously published questions.
"""
from pathlib import Path
import json,hashlib
ROOT=Path(__file__).resolve().parents[2]
load=lambda p:json.loads((ROOT/p).read_text(encoding='utf8'))
b=load('public/data/book.json');plan=load('public/data/reading-plan.json');targets=load('source/short-questions/batch021-targets.json')['targets']
ss={s['id']:s for s in b['sentences']};pp={p['id']:p for p in b['paragraphs']};out=[]
def add(i,kind,prompt,options,answer,prompt_zh,options_zh,analyses,quotes,word,meaning,context,example,collocations,translation,support='explicit'):
 t=targets[i-1];u=next(u for u in plan['units'] if u['id']==t['readingUnitId']);group=[ss[sid] for sid in u['sentenceIds']];p=pp[u['paragraphId']];text=p['text'][group[0]['start']:group[-1]['end']]
 assert hashlib.sha256(text.encode()).hexdigest()==t['passageSha256'];evidence=[]
 for quote in quotes:
  offset=text.find(quote);assert offset>=0,(i,quote);start=group[0]['start']+offset;end=start+len(quote);touching=[s for s in group if s['start']<end and s['end']>start]
  evidence.append(dict(quote=quote,sentenceIds=[s['id'] for s in touching],sources=list({(r['pdfPage'],r['block']):r for s in touching for r in s['sources']}.values())))
 assert word.lower() in text.lower(),(i,word)
 out.append(dict(id=t['questionId'],version=1,readingUnitId=u['id'],chapterId=u['chapterId'],sectionId=u['sectionId'],paragraphId=u['paragraphId'],sentenceIds=u['sentenceIds'],passage=text,prompt=prompt,options=options,answer=answer,type=kind,promptZh=prompt_zh,optionsZh=options_zh,analyses=analyses,evidence=evidence,vocabulary=[dict(word=word,meaning=meaning,context=context,example=example,collocations=collocations)],translation=translation,support=support,editorialStatus='PDF 第 81–85 页逐题原页核对；固定原句与来源；保留理论推测、调查相关、自报、团队分组、假想工作预测及行为指标的边界；原文连续无重复'))







add(1,'细节','What imbalance does Marx fear in the development of a person?',
 ['Every faculty develops equally through specialization.','One faculty develops at the cost of the others.','Economic skills decline while all other faculties grow.','Specialization affects economic life but leaves other spheres untouched.'],1,
 'Marx 担心人的能力发展出现什么失衡？',['所有能力都通过专门化得到同等发展。','一种能力的发展以其他能力为代价。','经济技能下降，而其他能力全部增长。','专门化影响经济生活，却不涉及其他领域。'],
 ['A one single faculty 与 all other faculties 的代价关系不是均衡发展。','B at the expense of 明确指出发展单一能力会牺牲其他能力，这是 Marx 的担忧。','C 颠倒了受益与受损对象，也把 faculty 武断缩成经济技能。','D not only the economic, but every other sphere 扩展了涉及领域，非仅限经济。此处引述理论担忧，不是实验结论。'],
 ['that development in a man of one single faculty at the expense of all other faculties.'],
 'at the expense of','以……为代价','一种能力的发展挤占其他能力的发展，不是指财务费用','She improved her speed at the expense of accuracy.',['at the expense of other faculties','develop one skill at the expense of another'],
 '例如，他担心劳动分工会使人变得单向度：“劳动分工不仅支配经济领域，也支配社会其他每一个领域，并到处奠定那种无所不包的、使人专门化和分类的制度的基础，即以其他一切能力为代价来发展人的某一种能力。”')

add(2,'作者意图','How does the quoted Marx passage qualify the increase in productive power?',
 ['It benefits laborers by developing all their faculties.','It reduces social output while enriching individual workers.','It benefits capitalists without affecting individual laborers.','It benefits capitalists while damaging individual laborers.'],3,
 '引述的 Marx 论述怎样限定生产力的提高？',['通过发展全部能力而使劳动者受益。','降低社会产出，同时丰富个体劳动者。','使资本家受益，却不影响个体劳动者。','使资本家受益，同时损害个体劳动者。'],
 ['A instead of for...the labourer 否定了这里把劳动者当作主要受益者的读法。','B It increases 明说提高生产力；不能把个体受损改成社会产出下降。','C by crippling 表明提高生产力伴随个体受损，不是毫无影响。','D for the benefit of the capitalist 与 crippling the individual labourers 同时支持此项。mortifies...ruins 是 Marx 的批判性措辞，不是本段测得的普遍医学结果。'],
 ['for the benefit of the capitalist instead of for that of the labourer','by crippling the individual labourers.'],
 'crippling','使受严重损害；使能力受限','引语中批评劳动者受到压抑，不能据此认定所有人出现同种身体损伤','The restrictions were crippling the group’s ability to respond.',['cripple individual labourers','cripple someone’s ability'],
 'Marx 进一步担心劳动分工会使劳动者变得愚钝：“它提高劳动的社会生产力，不是为了劳动者，而是为了资本家的利益；而它又是通过使个体劳动者残缺受损来做到这一点的。”Marx 认为，劳动分工“折磨肉体并摧毁心智”。')

add(3,'细节','Which two workplace features does Erikson identify as key sources of alienation?',
 ['Narrower specialties and restricted worker control.','Broader responsibilities and stronger worker control.','Lower quotas and less managerial monitoring.','More routine work and complete worker autonomy.'],0,
 'Erikson 把哪两项工作场所特征视为异化的主要来源？',['专业分工越来越窄，工人控制权受限。','职责更加广泛，工人控制权更强。','配额减少，管理监督减弱。','工作更例行化，而工人完全自主。'],
 ['A narrower and narrower specialties 与 limit...control 是并列的两项结构性来源。','B 把两者方向都反转了。','C quotas 和 constant monitoring 是后文例子，不是降低配额和监督。','D 第一部分接近例子，但 complete autonomy 与限制控制权矛盾。题目考观点定位，不意味着本段以实验确立唯一原因。'],
 ['subdivide labor into narrower and narrower specialties','limit the amount of control workers exercise over the work they do.'],
 'boil down to','归结为；主要在于','将异化的主要来源概括为两类工作结构','The disagreement boils down to who controls the schedule.',['boil down to two factors','sources boil down to'],
 '1985 年，在美国社会学协会的主席演讲中，Kai Erikson 讨论了 Marx 的异化理论如何仍适用于现代工作场所。具体来说，他认为异化的主要来源归结为“现代工作场所中把劳动细分为越来越狭窄专业的那些结构，以及第二类结构——限制工人对自己所做工作行使多少控制权的结构”。文职人员受到配额、例行程序和管理者持续监督的约束。')

add(4,'同义改写','Which paraphrase preserves Erikson’s qualification of the division of labor?',
 ['It necessarily makes every worker indifferent and cruel.','It protects workers from exhaustion in every workplace.','It may contribute to dehumanizing feelings and behavior.','It has been experimentally proved to cause each listed outcome.'],2,
 '哪种改写保留了 Erikson 对劳动分工的限定？',['它必定使每个工人冷漠、残酷。','它在每个工作场所都保护工人免于疲惫。','它可能促成非人化的感受与行为。','实验已证明它造成列出的每一种结果。'],
 ['A potential 不能改成必然，更不能扩为每位工人。','B agent of 指可能促成这些问题，而非保护人免受问题。','C may 保留 potential 的可能性，概括列举的冷漠、残暴、疲惫等。','D encouraged us to think 是观点提示，当前句没有给实验设计或证明。IELTS 改写要同时守住方向与确定程度。'],
 ['a potential agent of “human indifference, brutality, exhaustion, cruelty, [and] numbness.”'],
 'potential','潜在的；可能的','把劳动分工称为可能促成不良后果的因素，不表示必然发生','The review identified a potential source of confusion.',['a potential agent of','potential consequences'],
 'Erikson 鼓励我们把现代劳动分工看作“人的冷漠、残暴、疲惫、残酷以及麻木”的一种潜在促成因素。')

add(5,'细节','What did Kohn’s study examine in the survey sample?',
 ['Only productivity and wages among factory managers.','Three labor dimensions and four alienation aspects among 3,101 employed Americans.','Four labor dimensions and three alienation aspects among 3,101 students.','A randomized change of supervision among all American workers.'],1,
 'Kohn 的研究在调查样本中考察了什么？',['只考察工厂经理的产出与工资。','在 3,101 名就业美国人中考察三项劳动维度与四项异化方面。','在 3,101 名学生中考察四项劳动维度与三项异化方面。','随机改变全体美国工人的监督方式。'],
 ['A 列出的指标是监督、例行化、复杂性及异化，非仅工资产出，也没限定工厂经理。','B 三项劳动维度、四项异化方面与 3,101 Americans employed in civilian occupations 均匹配。','C 对调三和四，还把就业样本换成学生。','D survey data 不等于随机干预；样本不等于全体工人。some evidence 支持理论，不是彻底证明全部推测。'],
 ['survey data from 3,101 Americans employed in civilian occupations.','three dimensions of labor','four specific aspects of alienation'],
 'substantive complexity','实质复杂性','描述工作本身的内容是否复杂，是所测三项劳动维度之一','The study compared jobs with different levels of substantive complexity.',['substantive complexity of work','measure work complexity'],
 '社会学家 Melvin Kohn 找到了一些支持 Marx 推测的证据。例如，他研究了 3,101 名从事非军职工作的美国人的调查数据。他测量了劳动的三个维度：监督的严密程度、工作的例行化程度和工作的实质复杂性；还测量了异化的四个具体方面：无力感、自我疏离、失范和文化疏离。')

add(6,'有限推断','Which conclusion stays within the evidence stated about these respondents?',
 ['Those work characteristics were associated with more frequent reports of alienation.','Every closely supervised respondent reported all the listed feelings.','Respondents were randomly assigned to simpler jobs.','Alienation was shown to cause managers to increase supervision.'],0,
 '关于这些受访者，哪一结论没有越过本句证据？',['这些工作特征与更常报告异化感有关。','每位受严密监督者都报告了全部感受。','受访者被随机分配到较简单的工作。','研究证明异化使管理者加强监督。'],
 ['A more likely to report 支持报告概率更高的关联，不是人人如此。','B 将更可能扩大成每个人，并把多个感受变成人人全有。','C 本句没有随机分配工作的信息。','D 把描述的关联擅自反向写成因果；原文没有确立这种因果方向。定位 more likely 和 report，可同时避免绝对化与把自报当客观全知。'],
 ['Respondents with close supervision, routinized work, and lack of work complexity were more likely to report'],
 'powerless','无力的；感到没有掌控能力的','指受访者报告对生活缺乏控制的感受，不是测量肌肉力量','She felt powerless to change the rigid timetable.',['feel powerless','powerless to change'],
 '受到严密监督、工作例行化且缺乏复杂性的受访者，更可能报告以下感受：他们无法掌控自己的生活，感到无力；他们感到没有目标，与大多数人珍视的生活价值相疏离；他们也不在乎什么是对、什么是错。',support='limited-inference')

add(7,'逻辑关系','What qualification does the author make before introducing the new research interest?',
 ['Kagan and Marx describe exactly the same degree of alienation.','All specialized teamwork is as alienating as an assembly line.','Being part of a larger team can never be enjoyable.','Specialized teamwork may be less alienating, and participating in a larger effort can be fun.'],3,
 '引入新的研究兴趣前，作者作了什么限定？',['Kagan 与 Marx 描述的异化程度完全相同。','所有专业团队工作都与流水线一样令人异化。','参与更大的团队绝不可能有乐趣。','专业团队工作也许较少令人异化，参与更大的事业也可能有趣。'],
 ['A not exactly the same 和 much darker 表明二者有区别。','B perhaps not as alienating 保留程度差别，而非一概相等。','C can be fun 明确允许有趣。','D 同时保留 perhaps 的谨慎比较与 can 的可能性。作者在限定前述批评后提出研究兴趣，没有先宣布新研究的结果。'],
 ['perhaps not as alienating as working in a factory assembly line.','It can be fun to be part of something larger than yourself.'],
 'alienating','令人疏离的；使人产生异化感的','比较不同工作形式带来的疏离体验，原文用 perhaps 保留不确定性','The repetitive process felt alienating to some members of the team.',['an alienating task','not as alienating as'],
 'Kagan 所说的“情绪被稀释”与 Marx 的异化概念并不完全相同；Marx 的异化要阴暗得多。而且，作为大团队的一员，做数据分析这样的专门任务，也许不像在工厂流水线上工作那样令人异化。参与比自身更大的事业也可能很有趣。读了 Kohn 的研究后，我对劳动分工的心理后果产生了好奇，具体是它对幸福、意义和心理丰富性的影响。')

add(8,'作者意图','What role do the three questions play in this passage?',
 ['They report three established effects of specialization.','They instruct workers to abandon their jobs immediately.','They pose competing possibilities about efficiency and psychological experience.','They give participants the answers to the coming experiment.'],2,
 '这三个问句在片段中起什么作用？',['报告专门化的三项既定效果。','命令工人立即辞职。','提出效率与心理体验之间几种有待研究的可能。','向参与者提供接下来实验的答案。'],
 ['A 问句在提出问题，不是宣布已确立的三项结果。','B do your job 是最后一种设问，没有辞职指令。','C 前两问担心情绪范围缩小、丰富性下降与无聊，第三问提出相反可能，形成待检验的选择。','D 没有实验答案或给参与者的指示。IELTS 作者意图题要识别疑问形式，不把研究动机误读为研究发现。'],
 ['Does specialization reduce psychological richness and increase boredom? Or is everything fine if you just do your job?'],
 'in favor of','为了；偏向于','此处设问是否牺牲完整情绪体验以换取机器般的效率','The committee set aside variety in favor of consistency.',['in favor of efficiency','choose one approach in favor of another'],
 '劳动分工是否为了机器般的效率而夺走了完整范围的情绪体验？专门化是否降低心理丰富性并增加无聊？或者，只要把自己的工作做好，一切其实都没问题？')

add(9,'细节','How were participants introduced to the online motorcycle task?',
 ['They worked alone without meeting any team members.','Three participants joined each session and first created a team name together.','They chose their job condition before receiving the Zoom link.','They began by assembling physical motorcycles in a factory.'],1,
 '参与者怎样进入线上摩托车组装任务？',['他们独自工作，没有接触团队成员。','每场三人，先一起想出团队名称。','收到 Zoom 链接前先自行选择工作条件。','先在工厂组装实体摩托车。'],
 ['A three participants、as a team 和共同命名都表明团队安排。','B Each experimental session had three participants 与命名的团队建设活动直接对应。','C 本段未说自行选条件；后续安排也不能提前编成自主选择。','D online 明确为线上组装，不能改成实体工厂。'],
 ['Each experimental session had three participants','coming up with the name of their team as a team-building activity.'],
 'designated','指定的','预先安排参与者进入的 Zoom 链接，不是他们任意选择的地点','Please join the designated meeting room at noon.',['a designated Zoom link','a designated time'],
 '为回答这些问题，我和研究生 Youngjae Cha 设计了一项线上组装任务。参与者被邀请在预定时间进入指定的 Zoom 链接，由研究助理迎接。每场实验有三名参与者，他们被告知将在线上以团队形式组装摩托车。他们先花了一些时间一起为团队取名，作为团队建设活动。')

add(10,'细节','At what level was assignment to the two production conditions made?',
 ['Each motorcycle part was assigned a different condition.','Each participant independently selected a preferred condition.','The condition changed after every motorcycle within a session.','The team or session received one condition, with successive sessions using different conditions.'],3,
 '两种生产条件的分配在什么层级进行？',['每个摩托车零件分到不同条件。','每人独立选择偏好的条件。','一场之内每完成一辆就更换条件。','按团队或场次分条件，相邻场次采用不同条件。'],
 ['A one aspect 是分工条件内的任务安排，不是条件分配单位。','B been assigned 不是自行选择。','C once...another one 只说完成一辆再做下一辆，不说更换实验条件。','D at the team level 与 one session...the next 明确给出分组单位和场次安排。本段没有说条件随机分配，不能把后文等待时长的随机化移到这里。'],
 ['This assignment was done at the team level. So, one session was the division of labor condition and the next was the whole production condition.'],
 'condition','实验条件；实验情境','这里区分每人负责一道工序与每人独立完成整车两种任务安排','Participants completed the task under one of two conditions.',['the division of labor condition','the whole production condition'],
 '随后，他们被告知已被分配到以下两种安排之一：只负责组装的一个方面，即劳动分工条件；或独自完成整个生产过程，即每人组装摩托车全部零件，完成一辆后再做下一辆。分配在团队层面进行。因此，一场采用劳动分工条件，下一场采用整车生产条件。我们鼓励参与者尽可能多地生产摩托车。')

add(11,'细节','What output is reported for the whole-production condition?',
 ['Five motorcycles per person on average, giving fifteen for a three-person team.','Five motorcycles per three-person team, giving fifteen per person.','Fifteen motorcycles per person, giving forty-five per team.','Fifteen motorcycles per team in each of three different time periods.'],0,
 '独立完成整个生产过程的条件下，原文报告多少产量？',['平均每人五辆，三人团队共十五辆。','三人团队共五辆，每人十五辆。','每人十五辆，每队四十五辆。','每队在三个不同时间段各完成十五辆。'],
 ['A five...on average 指每位成员，three-person team...fifteen 给出团队换算。','B 对调个人与团队单位，算术关系也不符。','C 把团队总数当个人数再乘三。','D 原文未设置三个时间段；three-person 指三个人。数量题先标清每人与每队，不能混用实验后主观感受与产量指标。'],
 ['they were able to assemble only five motorcycles on average. For a three-person team, this meant an average of fifteen motorcycles.'],
 'on average','平均而言','报告该实验条件的平均产量，不保证每个个体恰好五辆','The participants solved eight problems on average.',['five motorcycles on average','an average of fifteen'],
 '实验结束时，我们询问他们有多快乐、觉得任务有多大意义，以及感觉有多心理丰富。在产出方面，分工条件的参与者比独立完成整个生产过程的参与者好得多。当每位成员独自完成整个生产过程时，平均每人只能组装五辆摩托车。对三人团队来说，这意味着平均十五辆。')

add(12,'逻辑关系','What feature makes the output contrast a rate comparison?',
 ['The division-of-labor team spent four times as long working.','The two conditions used different output measures.','The sixty-motorcycle output was achieved within the same amount of time.','The sixty motorcycles were produced separately by each worker.'],2,
 '什么条件使这里的产出对比能够比较生产速度？',['分工团队工作了四倍时间。','两条件使用不同产出指标。','六十辆的产出是在相同时间内达到的。','六十辆由每个工人各自独立生产。'],
 ['A within the same amount of time 明确否定工作时长四倍。','B 两者都比较摩托车产量，没有更换单位。','C 相同时间内完成六十辆使产出差异成为速度差异，而非单纯工作更久。','D team produced 是团队平均总产量，不能当每人六十辆。four times 保留原书表达；结合相邻上一段的三人团队十五辆，理解为六十为十五的四倍，非所有生产活动的保证值。'],
 ['the division of labor team produced, on average, sixty motorcycles within the same amount of time.'],
 'in contrast','相比之下；形成对照','引出分工团队的产量，与前一条件作比较','The first design was slow; in contrast, the second finished quickly.',['in contrast to','in contrast, the team'],
 '相比之下，分工团队在相同时间内平均生产六十辆摩托车。劳动分工使产量达到四倍！')

add(13,'细节','Which psychological costs are ruled out in this part of the report?',
 ['All possible psychological costs in every kind of workplace.','Lower happiness and lower meaning in the reported task comparison.','Lower psychological richness and greater boredom.','Any difference in the teams’ motorcycle output.'],1,
 '报告的这一部分排除了哪些心理代价？',['各种工作场所中一切可能的心理代价。','所报告任务比较中的幸福下降和意义下降。','心理丰富性下降和更加无聊。','团队摩托车产量的任何差异。'],
 ['A 这里只谈本次任务的幸福与意义，不能扩大到所有维度或工作场所。','B happiness, no 与 meaning...no cost either 直接对应，且 reported similar 是报告相似，不是证明精确相等。','C 本片段没有说丰富性无代价，不能借前两个维度推到第三个。','D 产量不是心理代价指标，前文也已有产量差异。'],
 ['Participants in both conditions reported similar levels of enjoyment and happiness. In terms of meaning, there was no cost either.'],
 'in terms of','就……而言；在……方面','把结论限定到幸福或意义这一具体维度','In terms of speed, the new method worked well.',['in terms of happiness','in terms of meaning'],
 '但劳动分工有没有带来心理代价？就幸福而言，没有。两种条件下的参与者报告了相似程度的享受与快乐。就意义而言，也没有代价。')

add(14,'逻辑关系','What contrast is introduced by “However” in this report?',
 ['Meaningfulness was similar, whereas psychological richness was lower under division of labor.','Meaningfulness was lower, whereas psychological richness was the same.','Division of labor made the task both richer and more interesting.','Whole production was more efficient but less psychologically rich.'],0,
 '报告中的 However 引出什么对比？',['意义感相似，但分工条件下心理丰富性较低。','意义感较低，但心理丰富性相同。','分工使任务既更丰富又更有趣。','独立完整生产效率更高，却较不丰富。'],
 ['A similar levels of meaningfulness 后转向 significantly lower...richness，构成不同维度的结果对比。','B 对调相似和较低所属的指标。','C more boring, monotonous, less interesting 与更有趣方向相反。','D not efficient 指完整组装效率不高，不能改成更高。这是该线上任务的报告，不能直接断言所有真实工作的长期心理结果。'],
 ['similar levels of meaningfulness','the participants in the division of labor condition reported significantly lower levels of psychological richness'],
 'monotonous','单调的；缺少变化的','与 more boring、less interesting 并列描述分工任务的体验','Repeating the same step soon became monotonous.',['a monotonous task','boring and monotonous'],
 '当被问及任务时，两种条件下的参与者报告了相似程度的意义感。然而，分工条件的参与者报告的心理丰富性显著低于独立完成整个生产过程的参与者。也就是说，分工使任务更无聊、更单调、更缺乏趣味。独自组装完整摩托车并不高效。')

add(15,'逻辑关系','What does “Even so” signal between the two statements?',
 ['The later statement corrects the earlier statement as false.','The later statement gives the cause of the earlier one.','The later statement repeats the earlier one without a contrast.','The positive assessment remains despite the preceding negative assessment.'],3,
 '这两个陈述之间的 Even so 表示什么？',['后句纠正前句，认定前句错误。','后句给出前句的原因。','后句没有对比地重复前句。','尽管先前有负面评价，后面的正面评价仍成立。'],
 ['A Even so 是让步，不是撤销上一判断。','B 不表示 because 式因果。','C quite the opposite 后仍说 far more interesting，转折让步明显。','D 即便如此，体验仍有趣，保留两项判断并存。本短段的 it、the opposite 承接前文；只凭这里不能新增精确产量、条件分配或长期工作结论。'],
 ['Even so, it was a far more interesting experience.'],
 'Even so','即便如此；尽管这样','承认前面的不利评价，同时保留“更有趣”的评价','The route was slow. Even so, we enjoyed the journey.',['even so, it was','even so, the experience'],
 '事实上，情况恰好相反。即便如此，这仍是一次有趣得多的体验。')

add(16,'细节','What work pattern is imagined in the first consulting scenario?',
 ['A lone generalist completing many unrelated projects.','A team whose members exchange specialties every day.','A member of a large collaborative project repeating tasks in one specialty.','An experienced consultant reporting what actually happened at work.'],2,
 '第一个咨询情境设想了什么工作模式？',['独自做许多不相干项目的通才。','每天互换专业的团队。','大合作项目中的一员，在同一专业内重复任务。','有经验的顾问报告实际工作经历。'],
 ['A 原文是 with many others，且只给一个大项目。','B specializing in one area 不等于每天换专业。','C big collaborative project、one area、repeating similar tasks 三点均对应。','D Imagine 明确为设想，不是实际职业调查。题目只要求识别情境，不能把情境本身当作已观察到的结果。'],
 ['specializing in one area and repeating similar tasks every day.'],
 'collaborative','合作的；协作的','说明项目由多人共同参与，与独立工作的另一情境形成对照','The students completed a collaborative project on local history.',['a collaborative project','collaborative work'],
 '想象你在一家咨询公司工作，被安排与许多人一起参与一个大型合作项目。在这个团队里，想象你专攻一个领域，每天重复类似任务。这样的工作会是什么感受？')

add(17,'语境词义','What does “generalist” mean in the independent consulting scenario?',
 ['A person doing many different tasks rather than one specialized part.','A person managing others while doing none of the project’s tasks.','A person repeating a single specialty as part of a large team.','A person who has already proved happier in a real consulting job.'],0,
 '在独立咨询情境中，generalist 是什么意思？',['承担多种不同任务，而非只做一个专业环节的人。','管理别人但不做项目任务的人。','在大团队中重复某一专业任务的人。','已在真实咨询工作中被证明更快乐的人。'],
 ['A 后置 doing many different tasks by yourself 直接解释 generalist。','B 自己完成多种任务，不是只管理不做。','C 将上一情境的 specialist 放到当前情境。','D 当前只有 Imagine，既没有真实从业测量，也未给幸福结果。词义题优先利用同句解释，不凭日常对职位的印象判断。'],
 ['you have to be a generalist, doing many different tasks by yourself.'],
 'generalist','通才；承担多种任务的人','在设想中独立处理一个大项目所需的不同任务，不等于事事精通','As a generalist, she handled research, design and testing.',['be a generalist','a generalist role'],
 '现在想象你在一家咨询公司独立工作。你被分配到一个需要多种任务的大项目。独立工作时，你必须成为通才，自己完成许多不同任务。这样的工作会是什么感受？')

add(18,'细节','Which pattern did the UVA students predict across the two imagined jobs?',
 ['Greater happiness and richness in the specialist job, with similar meaning.','Greater happiness in the specialist job, similar meaning, and greater richness in the generalist job.','Greater happiness and meaning in the generalist job, with similar richness.','Identical happiness, meaning and richness in both jobs.'],1,
 'UVA 学生对两种假想工作的预测呈现什么模式？',['专才工作更幸福且更丰富，意义相似。','专才工作更幸福，意义相似，通才工作更丰富。','通才工作更幸福且更有意义，丰富性相似。','两种工作的幸福、意义和丰富性完全相同。'],
 ['A rich 的方向错配，原文将较丰富归于 generalist。','B happier...specialized、similar meaning、richer...generalist 三项逐一对应。','C 幸福方向相反，意义也并非通才更高。','D 三项并不全相同；similar meaning 不能扩为所有指标完全相等。expected、predicted、thought 都是想象预测，并非真实任职后的长期体验。'],
 ['happier in the specialized job on a collaborative project','They predicted similar levels of meaning.','psychologically richer in the generalist job than in the specialist job.'],
 'predicted','预测；预期','学生想象未来感受，未实际从事这两种工作后再评价','The students predicted that the varied task would be engaging.',['predict similar levels','predict how one would feel'],
 '为检验这一点，我们让一组 UVA 学生样本中的一半想象第一个情境，另一半想象第二个情境。令我们意外的是，学生预期，在合作项目中担任专才会比在独立项目中担任通才更幸福。他们预测两者意义感相似。但最重要的是，学生认为，在通才工作中的生活会比在专才工作中更有心理丰富性。')

add(19,'作者意图','Which specific similarity does the author cite as a replication?',
 ['Both studies measured consultants’ long-term careers.','Both studies found every psychological outcome to be identical.','Both studies required participants to assemble real consulting teams.','The specialized condition was judged less interesting than the broader task condition.'],3,
 '作者具体把哪项相似之处称为结果复现？',['两研究都测量顾问的长期职业生涯。','两研究发现每个心理指标结果完全相同。','两研究都要求参与者组建真实咨询团队。','专门化条件被认为比承担较完整任务的条件更少趣味。'],
 ['A 一项线上组装、一项假想工作，均非长期从业跟踪。','B 原文在冒号后点明 less interesting，不能扩成全部结果完全相同。','C 没有组建真实咨询团队这一共同任务。','D like those... 与 less interesting...generalist 给出具体复现的趣味性方向。thought their job 表示预测，不是实际任职体验；不要用 replicated 一词抹平设计差别。'],
 ['participants in the specialized job thought their job would be less interesting than those in the generalist job.'],
 'replicated','复现；重复得到相似结果','这里具体指专门化较少趣味这一结果方向，不是所有测量都完全一致','The second task replicated the earlier pattern of responses.',['replicate the results','conceptually replicate a finding'],
 '通过这种方式，我们复现了线上组装实验的结果：与劳动分工条件下的人相似，专才工作条件的参与者认为自己的工作会比通才工作条件的参与者更少趣味。')

add(20,'逻辑关系','Why did the researchers introduce a trivia task in the next experiment?',
 ['To verify that participants had actually worked as consultants.','To replace the consulting setup with a factory production line.','To add a behavioral curiosity measure because imagined-life predictions may be inaccurate.','To ask the same feelings questions without changing the outcome measure.'],2,
 '研究者为什么在下一实验中引入常识问答任务？',['核实参与者确实做过咨询顾问。','把咨询设定换成工厂流水线。','因为假想生活预测可能不准，改用行为好奇心指标。','不改变结果指标，只重问相同感受问题。'],
 ['A 没有核实真实顾问工作经历。','B kept...setup...the same 保留咨询情境设定，不是改成工厂。','C predictions...not always correct 与 measuring behavioral curiosity 直接构成动机和方法。','D instead of asking...feel 说明更换测量，而非原样重问。行为指标可补充预测，但并不自动证明真实职业生活的长期结果。'],
 ['participants’ predictions about an imagined life are not always correct.','this time measuring behavioral curiosity.'],
 'account for','考虑到；应对；把……纳入考量','To account for this 指针对预测可能不准的问题作方法调整','The researchers changed the measure to account for possible reporting errors.',['account for this limitation','account for prediction errors'],
 '当然，参与者对假想生活的预测并不总是正确。为应对这一点，我们又做了一项实验，这次测量行为上的好奇心。研究的实验设定仍与咨询情境实验相同。不过，我们不再询问他们在设想咨询公司工作生活时会有何感受，而是让参与者完成常识问答任务。')

add(21,'细节','What happened when participants selected the skip button?',
 ['They moved to the next question without seeing the answer.','They saw the answer immediately and then moved on.','They waited before receiving the current answer.','They were returned to the consulting-scenario instructions.'],0,
 '参与者选择 skip 按钮时会发生什么？',['不看答案，直接进入下一题。','立即看到答案后再继续。','等待后得到当前答案。','回到咨询情境的说明。'],
 ['A answer was not shown 与 moved on to the next question 都明确。','B 把没有展示改成立即展示。','C 将 wait 按钮的机制错安给 skip。','D 没有返回情境说明的步骤。本段所举总统问题是实验题例，不需要用外部知识回答本题。'],
 ['If participants hit the skip button, then the answer was not shown and they moved on to the next question.'],
 'skip','跳过；略过','任务按钮的作用是放弃查看当前答案，继续下一道','You may skip a question and return to it later.',['hit the skip button','skip to the next question'],
 '任务包含这样的问题：哪位美国总统还持有一项发明专利？在这项任务中，每显示一道问题，就有两种回应选项：等待按钮和跳过按钮。如果参与者按跳过，答案不会显示，他们就进入下一题。')

add(22,'细节','How was curiosity operationalized in the fifteen-question task?',
 ['By the speed with which a person pressed skip.','By how many answers a person was willing to wait for.','By whether a person already knew the president’s name.','By the number of seconds participants chose for each delay.'],1,
 '十五题任务怎样把好奇心转化为可观察指标？',['按下跳过按钮的速度。','愿意等待多少个答案。','是否本来就知道总统姓名。','参与者为每次延迟自行选择多少秒。'],
 ['A 原文使用等待答案的数量，不是跳过速度。','B The more answers...the more curious 直接给出操作指标。','C Lincoln 是答案例子，预存知识不是文中计分规则。','D 等待时长由程序在十至十五秒之间随机确定，不是参与者挑选。本指标反映本任务的等待行为，不能当作个人永久性格的全能测量。'],
 ['The more answers someone waited for, the more curious they were.'],
 'willing','愿意的；乐意的','表示为获得答案而承受等待的意愿','She was willing to wait for a clearer explanation.',['be willing to wait','willing to know more'],
 '如果按等待，他们必须等一段时间才能得到答案，例如 Abraham Lincoln；精确等待时长在十至十五秒之间随机确定。通常，好奇的人想知道答案，所以愿意等待。我们的实验共有十五道题。一个人等待查看的答案越多，就被视为越好奇。')

add(23,'有限推断','Which conclusion matches the reported behavioral comparison?',
 ['All working specialists became uninterested in everything beyond their jobs.','Generalists already knew more trivia answers before the task.','The study directly measured years of real consulting work.','Participants imagining a generalist role waited for answers more readily than those imagining a specialist role.'],3,
 '哪项结论符合报告的行为比较？',['所有在职专才都对工作之外的一切失去兴趣。','任务开始前，通才已知道更多常识答案。','研究直接测量多年真实咨询工作。','想象通才角色者比想象专才角色者更愿意等待答案。'],
 ['A 从 imagining 的实验场景扩大到全体在职专才，并把 other seemingly irrelevant 扩成一切。','B 本片段没有报告事前知识差异。','C 任务测量等待行为，不是多年职业追踪。','D 更愿等待及比较对象均与首句一致。作者后两句概括角色影响，解释时仍应保留假想角色与本任务行为的证据范围。'],
 ['Participants imagining they were generalists proved behaviorally more curious and more willing to wait for answers than those who were imagining a specialist job'],
 'seemingly','看似；表面上','信息对当前专业似乎无关，不等于它客观上毫无价值','The seemingly unrelated examples helped her understand the problem.',['seemingly irrelevant matters','seemingly unrelated information'],
 '想象自己是通才的参与者，在行为上表现出更强的好奇心，比想象自己从事专才工作的人更愿意等待答案；这在概念上复现了心理丰富性的发现。换言之，当你被安排成为专才时，你会对其他看似无关的事失去兴趣；当你被安排成为通才时，你会对其他事情更好奇。',support='limited-inference')

add(24,'逻辑关系','What mechanism does the author propose for specialization’s selective focus?',
 ['Learning much about one specialty may require ignoring information outside it.','Developing deep knowledge requires attending equally to every topic.','Marketable skills remove the need to learn about one’s industry.','A healthcare consultant is shown to lack any knowledge of healthcare.'],0,
 '作者提出什么机制来解释专门化的选择性注意？',['深入学习一个专业可能需要忽略该领域以外的信息。','形成深厚知识需要同等注意每个话题。','可就业技能消除了学习本行业的需要。','医疗顾问被证明完全不懂医疗。'],
 ['A selectively attending、ignore irrelevant information 及 might need 给出可能的注意力取舍机制。','B ignore 与同等注意所有话题不符。','C 原文 need to learn so much 恰好强调学习需求。','D 医疗顾问是假设例子，强调行业知识多，不是无知证明。末句保留专业知识与技能的收益；不要把解释读成专门化毫无价值。'],
 ['you need to learn so much about the healthcare business that you might need to ignore information unrelated to that industry.'],
 'marketable','有市场需求的；有就业价值的','形容可在就业市场中发挥价值的专业技能','The course helped her develop marketable analytical skills.',['marketable skills','develop marketable expertise'],
 '但为什么会这样？当你专攻某件事时，你会选择性地关注与专业有关的信息，并努力忽略无关信息。例如，如果你是医疗咨询顾问，需要学习大量医疗行业知识，以至于可能不得不忽略与该行业无关的信息。专门化让你拥有某些领域的深厚知识，以及有就业价值的技能。')

add(25,'作者意图','What does the Louvre comparison illustrate?',
 ['A documented study showing the Mona Lisa is less valuable than other paintings.','A deliberate decision to avoid learning anything about one’s own specialty.','Narrow attention to one focus can cause other worthwhile experiences to be missed.','Evidence that every museum visitor ignores paintings on the same side.'],2,
 'Louvre 的比喻要说明什么？',['一项证明 Mona Lisa 比其他画价值低的研究。','有意决定不学习自己的专业。','注意力过于集中在一点，可能错过其他有价值的体验。','所有博物馆参观者都忽略同一侧画作的证据。'],
 ['A It’s like 引出比喻，没有艺术价值实验或排名。','B unintentionally 是无意后果，且讨论忽略专业之外领域。','C 只盯 Mona Lisa 而错过其他杰作，对应专门化后对生活其他领域少了兴趣。','D 比喻不是对所有游客实际行为的统计；right, left, back 也不是同一侧。作者意图题要说明类比映射，不把形象例子当实测证据。'],
 ['being so focused on the Mona Lisa that you forget to look to your right, left, and back and miss all the other masterpieces!'],
 'unintentionally','无意地；并非有意地','把对其他生活领域失去兴趣说成专门化的非预期代价','He unintentionally overlooked several useful suggestions.',['unintentionally miss something','an unintended consequence'],
 '但无意间，专门化会让你对生活其他领域不再感兴趣。这就像去 Louvre，太专注于 Mona Lisa，以至于忘记看看右边、左边和身后，错过了所有其他杰作！')

assert len(out)==25 and [q['id'] for q in out]==[t['questionId'] for t in targets]

def persist():
 path=ROOT/'source/short-questions/additional.json';existing=load('source/short-questions/additional.json');byid={q['id']:q for q in existing}
 for q in out:
  if q['id'] in byid:assert byid[q['id']]==q,('Refuse to overwrite changed authoring',q['id'])
  else:existing.append(q)
 path.write_text(json.dumps(existing,ensure_ascii=False,indent=2)+'\n',encoding='utf8',newline='\n')
 review=dict(batchId='batch-021',date='2026-10-22',pdfSha256=b['pdfSha256'],checkedPdfPages=list(range(81,86)),questionIds=[q['id'] for q in out],paragraphs=[dict(id=pid,textSha256=hashlib.sha256(pp[pid]['text'].encode()).hexdigest()) for pid in dict.fromkeys(q['paragraphId'] for q in out)],note='完整PDF81–85原页视觉对照，含Marx跨页引述、Erikson观点、Kohn调查、线上组装实验、假想咨询工作及等待答案任务。分别保留理论、相关、实验自报、想象预测与行为指标；不声称随机分配组装条件或真实从业效果；产量四倍按本书15对60的同人数团队基线理解。全段审阅不冒充所有候选句已配题。')
 (ROOT/'source/short-questions/review-chapter08-labor25.json').write_text(json.dumps(review,ensure_ascii=False,indent=2)+'\n',encoding='utf8',newline='\n')
 print('Saved',len(out),'of 25 individually authored exercises')

if __name__=='__main__':persist()
