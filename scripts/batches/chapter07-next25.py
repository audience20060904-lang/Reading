"""25 individually authored exercises for frozen targets, PDF pages 69-73.
Preserve printed English, source positions and all previously published questions.
"""
from pathlib import Path
import json,hashlib
ROOT=Path(__file__).resolve().parents[2]
load=lambda p:json.loads((ROOT/p).read_text(encoding='utf8'))
b=load('public/data/book.json');plan=load('public/data/reading-plan.json');targets=load('source/short-questions/batch018-targets.json')['targets']
ss={s['id']:s for s in b['sentences']};pp={p['id']:p for p in b['paragraphs']};out=[]
def add(i,kind,prompt,options,answer,prompt_zh,options_zh,analyses,quotes,word,meaning,context,example,collocations,translation,support='explicit'):
 t=targets[i-1];u=next(u for u in plan['units'] if u['id']==t['readingUnitId']);group=[ss[sid] for sid in u['sentenceIds']];p=pp[u['paragraphId']];text=p['text'][group[0]['start']:group[-1]['end']]
 assert hashlib.sha256(text.encode()).hexdigest()==t['passageSha256'];evidence=[]
 for quote in quotes:
  offset=text.find(quote);assert offset>=0,(i,quote);start=group[0]['start']+offset;end=start+len(quote);touching=[s for s in group if s['start']<end and s['end']>start]
  evidence.append(dict(quote=quote,sentenceIds=[s['id'] for s in touching],sources=list({(r['pdfPage'],r['block']):r for s in touching for r in s['sources']}.values())))
 assert word.lower() in text.lower(),(i,word)
 out.append(dict(id=t['questionId'],version=1,readingUnitId=u['id'],chapterId=u['chapterId'],sectionId=u['sectionId'],paragraphId=u['paragraphId'],sentenceIds=u['sentenceIds'],passage=text,prompt=prompt,options=options,answer=answer,type=kind,promptZh=prompt_zh,optionsZh=options_zh,analyses=analyses,evidence=evidence,vocabulary=[dict(word=word,meaning=meaning,context=context,example=example,collocations=collocations)],translation=translation,support=support,editorialStatus='PDF 第 69–73 页逐题原页核对；固定原句与来源；区分关联、比较、作者建议、文学引语和反事实；保留原书叙述时点、might/appears 等限定'))





add(1,'逻辑关系','What contrast is introduced by “Yet” in this passage?',
 ['Adult athletes and children are said to have identical daily schedules.','Elite sport leaves little room for play, although play matters for child development.','Gopnik argues that children should specialise immediately.','Repetition is described as irrelevant to elite sport.'],1,
 'Yet 在本段引出什么对照？',['成年运动员与儿童的日程完全一样。','精英体育很少留出玩乐空间，但玩乐对儿童发展重要。','Gopnik 主张儿童应立即专攻。','反复训练被说成与精英体育无关。'],
 ['A 本段没有相同日程的比较。','B not much space 后接 critical for healthy child development，形成对照。','C 她强调长期童年可先尝试许多事，再在成年专攻。','D practice...is the name of the game 正强调反复训练的主导地位。'],
 ['There is not much space for playfulness. Yet play and playfulness are critical for healthy child development.'],
 'specialize','专攻；专门从事','指在众多探索之后集中于某一领域，不等同最初接触任何活动','After exploring several subjects, she chose to specialize in ecology.',['specialize in one area','specialize in a sport'],
 '在精英运动员的世界里，训练、训练、再训练才是核心，几乎没有多少玩心的空间。然而，玩耍与玩心对儿童健康发展至关重要。Alison Gopnik 认为，人类拥有格外漫长的童年，可以先尝试许多事，之后才在成年时被迫专攻一个领域。')

add(2,'细节','What is this prolonged period of play said to help children learn?',
 ['Only the rules of one professional sport.','A fixed occupation before exploring any alternatives.','Formal examination answers without social interaction.','Social norms and varied skills in informal settings.'],3,
 '这段延长的玩乐期，被说成帮助儿童学习什么？',['只学习一种职业运动的规则。','尚未探索其他可能，就选定固定职业。','在没有社交互动时掌握正式考试答案。','在非正式环境中学习社会规范与多样技能。'],
 ['A diverse skills 不只是一种运动。','B exploration 不是回避替代可能。','C informal settings 与正式考试不同，也无排除互动之意。','D learning social norms and diverse skills in informal settings 直接对应。'],
 ['learning social norms and diverse skills in informal settings.'],
 'social norms','社会规范','在日常玩耍等非正式情境中学习的交往规则，不是单项赛事规则的同义词','Children learn social norms through everyday interaction.',['learn social norms','social norms and skills'],
 '这段延长的探索期，是玩耍的时期；它对在非正式环境中学习社会规范和多样技能至关重要。')

add(3,'主旨','What comparison did the study examine?',
 ['Dedicating oneself early to one sport versus playing several before specialising.','Competing in science awards versus competing in the Olympics.','Playing only informal games versus never engaging in any sport.','Winning as a child versus avoiding every adult competition.'],0,
 '这项研究考察了什么比较？',['早早专注一项运动，与先玩多项再专攻相比。','科学奖项比赛与奥运比赛相比。','只玩非正式游戏，与从不运动相比。','童年获胜，与回避所有成年比赛相比。'],
 ['A one main sport 与 multiple sports before specializing 是明列的两条路径。','B 当前句只讨论运动，不涉及科学奖。','C 比较双方都参与运动，非运动与完全不运动。','D 本句提出表现路径问题，不是回避成年赛事；examined whether 只是研究问题，尚未给出结果或随机分派程序。'],
 ['single-minded dedication to one main sport or playing multiple sports before specializing in one sport.'],
 'single-minded dedication','专心一意的投入','在此指集中于一项主运动的路径，与先参与多项运动区分','The project required single-minded dedication during its final week.',['single-minded dedication to','dedication to one sport'],
 '一项近期研究考察，更高表现究竟来自专心投入一项主运动，还是先参与多项运动、之后再专攻一种。这里的“近期”依原书叙述时点理解。')

add(4,'细节','Which account accurately describes the meta-analysis and its top-performer group?',
 ['Fifty-five athletes in 6,096 studies, including 772 national champions.','Fifty-five studies of 6,096 athletes, with all athletes in the world’s top ten.','Fifty-five studies of 6,096 athletes, including 772 top-ten international performers.','772 studies of fifty-five athletes, including 6,096 local competitors.'],2,
 '哪项准确描述这项元分析及其最高水平组？',['6,096 项研究中有五十五名运动员，包括 772 名全国冠军。','五十五项研究共 6,096 名运动员，全部都属世界前十。','五十五项研究共 6,096 名运动员，其中 772 名属国际赛事前十水平。','772 项研究共五十五名运动员，包括 6,096 名地方选手。'],
 ['A 颠倒研究数与人数，并误写最高水平定义。','B 6,096 是各层级总数，并非全为国际前十。','C fifty-five、6,096、772 与括号中 top ten...international competition 一一对应。','D 数字角色全部错配。其余组为全国级 3,028、区域级 1,706、地方级 590；研究数不能当参与人数。'],
 ['meta-analyzed fifty-five studies that included 6,096 athletes, including 772 of the world’s top performers (defined as top ten performers in an international competition'],
 'national class','全国级；国家级别','本段依国家选拔队或全国锦标赛前十界定这一层级，须与世界级和区域级区分','The report compared national class performers with local competitors.',['national class performers','national selection team'],
 '这项研究对五十五项研究作元分析，共含 6,096 名运动员：772 名世界顶级选手（定义为奥运、世界田径锦标赛或泛美运动会等国际比赛前十名）、3,028 名全国级选手（国家选拔队成员，或全国锦标赛前十）、1,706 名区域级选手（棒球小联盟、NCAA 一级），以及 590 名地方或县级运动员。')

add(5,'推断','Which conclusion best preserves the reported comparison?',
 ['Early specialists never succeed as adults.','Playing several sports guarantees that an athlete cannot burn out.','Every successful athlete followed exactly the same sporting path.','Later specialisation was linked with less burnout and greater adult competitive success.'],3,
 '哪项结论最保留研究报告的比较强度？',['早期专攻者成年后从不成功。','参与多项运动保证绝不倦怠。','所有成功选手走完全相同的运动路径。','较晚专攻与较少倦怠、较高成年比赛成功可能相联。'],
 ['A less likely、more likely 不是早期专攻者永不成功。','B 相对较少倦怠不能改成不会倦怠的保证。','C 后面以不同路径的人物说明并非唯一模式。','D 保留两项相对比较，不从本段自行推出对每个人的确定因果或训练处方。'],
 ['were less likely to burn out and more likely to succeed in national and international competitions in adulthood'],
 'burn out','倦怠；因长期消耗而耗尽热情','描述长期投入中的耗竭风险，不是字面燃烧，也不是本网站作医学诊断','The demanding schedule made him worry that he would burn out.',['burn out early','risk of burnout'],
 '研究者发现，相较于职业生涯很早便专攻的精英选手，较晚之前仍参与多项运动的选手，更少倦怠，也更可能在成年全国及国际比赛成功。每有像 Michael Phelps 和 Simone Biles 的选手，也有像 Michael Jordan 和 Alex Morgan 的选手。Jordan 高中时除了篮球，还打棒球和美式橄榄球。','inference')

add(6,'细节','What timing is reported for Alex Morgan’s club-team participation?',
 ['She joined a club team before trying any other sport.','She did not play in a club team until age fourteen.','She began club soccer at the same age as Jordan’s basketball break.','She played only volleyball and never played soccer in high school.'],1,
 '本段怎样描述 Alex Morgan 参加俱乐部队的时间？',['尚未尝试其他运动就加入俱乐部队。','直到十四岁才参加俱乐部队。','她开始俱乐部足球的年龄等同 Jordan 暂离篮球时的年龄。','高中只打排球，从未踢足球。'],
 ['A grew up playing multiple sports，不能增加“先于所有其他运动”的条件。','B didn’t...until age fourteen 明确给出时间。','C 片段没有这种年龄对应，Jordan 的 two years 是离开时长。','D volleyball、track、soccer 三者均列出。直到十四岁入俱乐部不等于十四岁才首次接触足球。'],
 ['Alex Morgan grew up playing multiple sports and didn’t play in a club team until age fourteen.'],
 'sabbatical','暂时休离；休假期','本段指 Jordan 在巅峰期暂离篮球去打棒球，不是终身退役的同义词','She took a sabbatical from teaching to complete a book.',['take a sabbatical from','a two-year sabbatical'],
 '哀悼父亲期间，Jordan 在巅峰期暂离篮球两年，改打棒球。Alex Morgan 从小参与多项运动，直到十四岁才参加俱乐部队。高中时，她除了踢足球，还打排球、参加田径。')

add(7,'逻辑关系','How does the reported starting-age pattern differ between junior and adult competition?',
 ['Later starting predicts more success at both levels.','Earlier starting predicts more success at both levels.','Earlier starting predicts junior success, whereas later starting predicts adult success.','Starting age has no reported relationship with success at either level.'],2,
 '所报告的开始年龄模式，在青少年与成年比赛之间有何差别？',['两个层级都是较晚开始预测更多成功。','两个层级都是较早开始预测更多成功。','较早开始预测青少年成功，较晚开始预测成年成功。','两个层级均未报告开始年龄与成功有关系。'],
 ['A 青少年层级的方向相反。','B 成年层级的方向相反。','C earlier...junior 与 later...adult 构成 whereas 对照，须分清比赛阶段。','D 两类预测关联都被明确报告。开始一项运动与只专攻该运动不是可随意互换的概念，不能据此要求所有人延后开始运动。'],
 ['the success rate at the junior competition level is predicted by the earlier start age','the success rate at the adult competition level is predicted by the later start age.'],
 'whereas','而；然而','连接青少年与成年比赛中方向不同的开始年龄模式','The first group improved quickly, whereas the second improved more gradually.',['whereas the other group','whereas in adulthood'],
 '研究另一个关键发现是：青少年比赛的成功率由较早开始年龄预测（越早越成功），而成年比赛的成功率由较晚开始年龄预测。也就是说，在成年精英比赛中，较晚开始该运动的选手，比早开始者更成功。')

add(8,'细节','What comparison is made about reaching a major milestone?',
 ['World-class athletes reached it later than national-class athletes.','National-class athletes always reached it later than world-class athletes.','All athletes reached it at exactly the same age.','Only local athletes were considered capable of reaching it.'],0,
 '关于达到重要里程碑，本句作了什么比较？',['世界级选手比全国级选手更晚达到。','全国级选手总比世界级更晚达到。','所有选手都在完全相同年龄达到。','只有地方级选手被认为能达到。'],
 ['A significantly later than...national-class counterparts 明确比较方向。','B 方向倒置且添加 always。','C 原句报告时间差异，不是同龄。','D 本句比较世界级与全国级，没有地方级独占资格。例子是首次全国锦标赛或首次入选队伍，不必然指首次开始该运动。'],
 ['world-class athletes reached a major milestone','significantly later than did their national-class counterparts.'],
 'milestone','里程碑；重要阶段','指首次全国赛事或首次入选队伍等阶段，不是最初开始运动的同义词','Her first published paper was an important milestone.',['reach a milestone','a major milestone'],
 '与此相关，世界级选手达到重要里程碑（例如首次参加全国锦标赛、首次入选选拔队伍）的时间，显著晚于全国级的对应选手。')

add(9,'推断','Which interpretation keeps the scope and direction of the practice-hours finding?',
 ['Every extra hour of practice causes lower performance in all athletes.','The study found that no training of any kind is useful.','More coach-led practice guaranteed higher performance among world-class adults.','More main-sport practice hours were associated with lower performance among world-class adults.'],3,
 '哪种解释保留训练时数发现的范围与方向？',['所有选手每多练一小时，表现就必然更低。','研究发现任何训练都无用。','更多教练主导训练保证世界级成年选手表现更高。','世界级成年选手中，更多主项训练时数与较低表现相关。'],
 ['A 关联不能改成每小时确定因果，也不能扩展到所有年龄与水平。','B 原文没有全面否定训练。','C lower 被改成 higher，且保证不受支持。','D 保留 main-sport、world-class adult、associated with 和 lower 四个限定。其他运动中的青少年自主玩耍，与较高成年表现的关联是另一项发现。'],
 ['a high number of main-sport practice hours was associated with lower performance among the world-class adult athletes.'],
 'pickup games','临时自发组织的比赛','作为 youth-led play 的例子，与固定教练主导训练形成区别','Friends organised pickup games in the park after school.',['play pickup games','youth-led play'],
 '短期内，专攻会转化为成功；但长期看，并不总有回报。研究发现，在主运动之外，更多青少年自主玩耍（如临时自组比赛）与较高成年表现相关。令人意外的是，世界级成年运动员中，大量主项训练时数反而与较低表现相关。','inference')

add(10,'作者意图','What recommendation does the author draw from these findings for elite athletes?',
 ['Stop every kind of sporting activity immediately.','Increase playful involvement in other sports and reduce coach-led main-sport practice.','Replace other sports with even more coach-led main-sport practice.','Apply the same fixed training reduction to every child and adult.'],1,
 '作者据这些发现，给精英运动员提出什么建议？',['立即停止所有运动。','增加其他运动中的玩乐参与，减少教练主导的主项练习。','用更多教练主导的主项练习取代其他运动。','对每个儿童与成年人采用相同的固定减量。'],
 ['A reduce 不等于停止所有运动。','B increase...other sports 与 reduce...main sport 两部分均对应。','C 把建议方向完全倒置。','D if you are an elite athlete 限定人群，原句也没有固定减量数值。这是作者基于所述发现提出的建议，不能当成每位运动员都适用的个体训练方案或独立随机实验结论。'],
 ['increase playful engagement in other sports and reduce coach-led practice time for your main sport.'],
 'engagement','参与；投入','playful engagement 强调以玩乐心态参与其他运动，而非仅观看比赛','The programme encouraged active engagement in local activities.',['playful engagement','engagement in other sports'],
 '这些发现与其他运动中青少年自主玩耍的发现结合，提示作者：如果你是精英运动员，增加其他运动中的玩乐参与、减少主运动的教练主导训练，可能更好。')

add(11,'细节','Which finding is reported about the forty-eight German Nobel laureates?',
 ['Forty-two had multidisciplinary study or work experience.','All forty-eight won the Leibniz Prize before the Nobel Prize.','Only six had ever studied or worked in any field.','Forty-two specialised earlier because they had no other interests.'],0,
 '本段关于四十八位德国诺贝尔奖得主，报告了什么发现？',['其中四十二位有跨学科学习或工作经历。','四十八位全都先获 Leibniz 奖再获诺奖。','只有六位曾在任何领域学习或工作。','四十二位因没有其他兴趣而更早专攻。'],
 ['A Forty-two of the forty-eight 与 multidisciplinary...experiences 直接对应。','B 本段比较奖项获奖者群体，没有说四十八人全获两奖。','C 把四十八减四十二的差值错解为从未学习或工作者。','D 原句说 suggesting a later specialization，方向相反。这是专业经历比较，不能改成随机安排学科路径。'],
 ['Forty-two of the forty-eight Nobel laureates had engaged in multidisciplinary study or work experiences'],
 'multidisciplinary','跨学科的；涉及多个学科的','描述学习或工作经历范围，不等同于从未深入任何领域','The project brought together a multidisciplinary research team.',['multidisciplinary study','multidisciplinary work experiences'],
 '有趣的是，早期专攻效应在完全不同的专业领域——科学——也得到重复观察。另一项研究，把物理、化学、经济学及医学／生理学领域的四十八位德国诺贝尔奖得主，与德国最高国家科学奖 Leibniz 奖得主比较。四十八位中四十二位有跨学科学习或工作经历，提示较晚专攻。未获诺奖的 Leibniz 得主，早期成功来得比后来获诺奖者更早。')

add(12,'细节','Which career-timing result does the author highlight?',
 ['Nobel winners earned full professorships faster in every case.','Leibniz winners were less likely than Nobel winners to have student scholarships.','Eventual Nobel winners took longer to become full professors than Leibniz winners.','Neither group had reached a full professorship.'],2,
 '作者特别强调了什么职业时间结果？',['每位诺奖得主都更快成为正教授。','Leibniz 得主比诺奖得主更少获得学生奖学金。','后来获诺奖者成为正教授，比 Leibniz 得主用时更长。','两组均无人任正教授。'],
 ['A longer 不是 faster，也没有每个个案都如此的说明。','B more likely 被倒置成更少。','C took significantly longer...full professorships 直接对应。','D 原句比较晋升时间，不能推成两组都没晋升。研究比较中的较慢进展不等于能力低，也不证明故意推迟晋升就能获诺奖。'],
 ['it took significantly longer for the eventual Nobel winners to earn full professorships than the Leibniz winners.'],
 'eventual','最终的；后来成为的','eventual Nobel winners 是后来获奖的人，需与较早职业阶段区分','The eventual winner had not led during the first round.',['the eventual winner','eventual success'],
 '例如，Leibniz 得主比诺奖得主更可能在学生时代获得奖学金。我最喜欢的发现是：后来获诺奖者成为正教授的时间，显著长于 Leibniz 得主。因此，作者概括，诺奖得主探索更多学科、进展较慢，却最终到达顶峰而未耗尽热情。')

add(13,'主旨','What difficulty does Nietzsche criticise in the quoted passage?',
 ['Receiving too many awards before entering adulthood.','Choosing vocations too early and becoming trapped under their burden.','Having so much freedom that no one ever chooses a vocation.','Taking too long to learn the rules of competitive sport.'],1,
 'Nietzsche 的这段引语批评什么困难？',['成年前获奖过多。','太早选职业，之后受其负担困住。','自由太多，以致从无人选职业。','学习竞技规则用时太久。'],
 ['A 引语没有谈获奖数量。','B choose vocations too early 与难以甩掉的 burden 直接对应。','C condemned to choose 是被迫太早选择，不是没有人选择。','D 没有谈竞技规则；这里是 Nietzsche 的历史性批评引语，不能当成对所有现代德国青年的实验结论。'],
 ['condemned to choose vocations too early, and then to waste away under a burden they can no longer shake off.'],
 'vocations','职业；人生所从事的事业','引语批评过早选定并难以卸下的职业负担，不是体育项目名称','She explored several vocations before settling on teaching.',['choose a vocation','a vocational choice'],
 '在 Ecce Homo 中题为“Human, All Too Human”的文章里，Friedrich Nietzsche 谈德国的专攻现象：“我发现，许多年轻人经历着同样的苦恼：一个违背自然的步骤，几乎迫使他们走向第二步。在德国，在这个帝国里——说得明确些——太多人注定过早选择职业，之后在再也甩不掉的负担下衰耗。”这是文学／哲学引语，不是实验结果。')

add(14,'语境词义','What does “opium” suggest in this literary quotation?',
 ['A measured medical treatment prescribed by the study’s researchers.','A literal substance added to the performers’ food.','Proof that music permanently removes every vocational problem.','A metaphor for temporary escape or self-forgetting.'],3,
 '这段文学引语中的 opium 暗示什么？',['研究者处方中经过测量的医疗治疗。','实际加进表演者食物的物质。','证明音乐永久消除一切职业问题。','暂时逃离或忘却自我的比喻。'],
 ['A 这不是医疗实验或处方。','B 上下文 they forget themselves 指精神上的暂时逃离，无食物添加行为。','C for a moment、five or six hours 都不支持永久消除问题。','D 引语把 Wagner 比作“鸦片”，借此写暂时忘却自身，不提供药理或用药结论。'],
 ['they forget themselves, they are rid of themselves for a moment'],
 'rid of','摆脱；暂时从……解脱','这里与忘却自我相连，是引语中的比喻，不是永久治愈证明','For a moment, she felt rid of her everyday worries.',['be rid of worries','get rid of a burden'],
 '“这些人需要 Wagner 作为一种鸦片：他们忘了自己，一时摆脱自己——我在说什么？是五六个小时！”这里的“鸦片”是引语中的比喻，表现暂时忘我。')

add(15,'细节','Which pairing of Sidis’s ages and events matches the passage?',
 ['At eight he lectured at Harvard; at eleven he first sat the two exams.','At eight he earned a medical degree; at eleven he entered MIT.','At eight he passed the named exams; at eleven he lectured on astrophysics at Harvard.','At eleven he passed the exams and stopped studying astrophysics.'],2,
 '哪组 Sidis 的年龄与事件对应原文？',['八岁在 Harvard 演讲，十一岁才参加两项考试。','八岁取得医学学位，十一岁入读 MIT。','八岁通过所列考试，十一岁在 Harvard 讲天体物理。','十一岁通过考试后停止学习天体物理。'],
 ['A 把两个年龄对应事件颠倒。','B passing an exam 不等于取得学位或实际入学。','C at age eight 后列解剖学与 MIT 入学考试，eleven 后列 Harvard 演讲。','D 片段没有停止学习的说法。often considered 是所述声誉，不是网站独立测定“史上最聪明”的排名。'],
 ['At age eight, he passed the Harvard Medical School’s anatomy exam, as well as the entrance exam to MIT.','When Sidis was eleven years old, he gave a lecture on astrophysics at Harvard.'],
 'cautionary tale','警示故事；引人警惕的事例','作者用来提示早期成就可能伴随风险，不是具有普遍代表性的实验样本','The failed project became a cautionary tale about rushing decisions.',['a cautionary tale','present a cautionary tale'],
 'William James Sidis 的故事又是一个警示事例。他常被认为是史上最聪明的人。八岁时，他通过 Harvard Medical School 的解剖学考试，也通过 MIT 入学考试。十一岁时，他在 Harvard 作天体物理讲座。')

add(16,'推断','How should “might” and “could” affect the interpretation of the final claim?',
 ['They present possible risks rather than a guaranteed outcome for every early specialist.','They prove that early specialisation was Sidis’s only cause of burnout.','They establish that the professor’s prediction was correct.','They show that no early specialist can retain other interests.'],0,
 'might 与 could 应怎样影响对结尾论断的理解？',['它们提出可能风险，而非每位早期专攻者必然遭遇的结果。','它们证明早期专攻是 Sidis 倦怠的唯一原因。','它们确立那位教授的预测正确。','它们表明早期专攻者都无法保有其他兴趣。'],
 ['A 两个情态动词都限制确定程度；人物故事不能替代普遍因果实验。','B 片段没有排除其他原因或证明唯一原因。','C 原文明说 prediction was wrong。','D might dispel 不等于对每个人都必然剥夺兴趣。'],
 ['Early specialization might dispel interest in other activities in life and could lead to early burnout.'],
 'dispel','消散；驱散；使消退','此处说其他活动的兴趣可能消退，须保留 might 限定','The new evidence helped dispel the misunderstanding.',['dispel interest','dispel a doubt'],
 '在场的一位 MIT 物理教授说，Sidis 将成为伟大的天文数学家与科学领袖。但教授的预测错了。Sidis 耗尽了热情。过早专攻，可能使人对生活中其他活动的兴趣消退，也可能导致早期倦怠。','inference')

add(17,'作者意图','What does the author do with the phrase “makes me wonder if”?',
 ['Announce that persistence has no value in any profession.','Raise the possibility that single-minded grit should be accompanied by playfulness.','Report a completed trial proving a treatment for depression.','Conclude that every elite athlete and academic is depressed.'],1,
 '作者用 makes me wonder if 做什么？',['宣布坚持对任何职业都无价值。','提出单一目标的坚毅是否应与玩心相伴这一可能。','报告已完成的试验，证明一种抑郁治疗。','断定每位精英运动员与学者都抑郁。'],
 ['A paired with 不是把坚毅完全取消。','B wonder if 提出思考与问题，不是宣布已验证的必然规律。','C 句中无试验、治疗程序或疗效证明。','D high prevalence 不能改成每个人，也没有给出可自行编成精确比例的数据。'],
 ['makes me wonder if a singular grit needs to be paired with playfulness.'],
 'paired with','与……配合；与……相伴','把坚毅与玩心并置，保留努力的价值，而非二者只能取一','Focused work can be paired with time for exploration.',['be paired with','pair persistence with playfulness'],
 '精英运动员与学者中，倦怠与抑郁较为常见，这让我思考：只盯单一目标的坚毅，是否需要与玩心相伴？')

add(18,'细节','What qualification applies to the twenty-two postseason games mentioned here?',
 ['Every team is guaranteed to play exactly twenty-two.','They replace the 162 regular-season games.','They are an upper limit, expressed as “up to”.','They refer to twenty-two training hours each week.'],2,
 '这里提到二十二场季后赛，有什么限定？',['每支球队都保证恰好打二十二场。','它们取代 162 场常规赛。','它们是 up to 所表达的上限。','它们指每周二十二小时训练。'],
 ['A up to 不等于每支球队固定保证场数。','B 33、162、至多 22 是所列阶段，并非替换常规赛。','C up to 明示最多，不能漏掉这一限定。','D games 是场数，不是训练小时。书中赛程及人物球队、投打频率依其叙述时点保留，不冒充当前赛季核验。'],
 ['up to 22 postseason games'],
 'grueling','极累人的；艰苦的','描述书中所列长赛季的消耗，不是人物已经确诊某种疾病','The team completed a grueling series of away matches.',['a grueling schedule','a grueling season'],
 '原书描述，MLB 赛季漫长而艰苦，包括 33 场春训赛、162 场常规赛，以及最多 22 场季后赛——所列上限合计 217 场！这安排对 Dodgers 的 Shohei Ohtani 尤其吃力，书中说他多数比赛打击，至少每周投球一次。他有坚毅与自信，也有玩心。')

add(19,'作者意图','How is Ohtani’s action with his bat used in the passage?',
 ['As evidence that a bat needed medical treatment to function.','As proof that humour always causes elite performance.','As a report that he stopped caring about his sport completely.','As an example of a joking response to difficulty that appears to help him relax.'],3,
 '作者怎样使用 Ohtani 对球棒所做的动作？',['证明球棒需要医疗处理才可使用。','证明幽默总能导致顶级表现。','报告他已彻底不在意运动。','作为面对困难时开玩笑、似乎有助放松的例子。'],
 ['A jokingly 明确是幽默动作，非真的给球棒治病。','B appears to help 不等于已证明、总能或单一确定因果。','C 没有彻底失去兴趣的说法。','D 再次未安打后假装给球棒做 CPR，说明困难中的幽默态度。might...feel depressed 也不能直接充当对球员的新临床诊断。'],
 ['Ohtani jokingly gave his bat CPR.','appears to help Ohtani relax'],
 'dugout','球员休息区；球员席','指他未击出安打后走回的棒球场休息区，不是家中地下室','The player returned to the dugout after his turn at bat.',['return to the dugout','make one’s way to the dugout'],
 'Ohtani 在 2022 赛季打击开局糟糕，24 次中有 3 次安打（.125）。这样的数据可能使球员沮丧。但某场比赛中，他又未击出安打、走回球员席时，开玩笑地给球棒做了 CPR。他面对困难的幽默感，似乎有助放松并持续保持顶级表现。')

add(20,'语境词义','What does the chess-game comparison suggest about baseball here?',
 ['It is becoming more analytical and logical, with playfulness restoring some fun.','Baseball has literally replaced its balls and bats with chess pieces.','Data analysis is said to have made every game more spontaneous and silly.','The author argues that humour has no place in professional work.'],0,
 '这里把棒球比作棋局，意在暗示什么？',['比赛越来越重分析和逻辑，而轻松态度可恢复一些趣味。','棒球实际已用棋子取代球棒和球。','数据分析使每场比赛都更即兴、更胡闹。','作者认为职业工作不应有幽默。'],
 ['A data analytics、logical 与棋局相连，末句把 lightheartedness 与打破单调相连。','B 这是比喻，不是规则实际更换。','C 方向与 logical 的描述不符，且 every 过度概括。','D puts fun back into work 正支持给工作增添趣味。'],
 ['it is turning into more of a chess game','Lightheartedness punctures the monotony and puts fun back into work.'],
 'monotony','单调；一成不变的乏味','指过度逻辑化氛围中作者所感到的乏味，并非比赛实际上毫无变化','A short creative activity broke the monotony of the afternoon.',['break the monotony','puncture the monotony'],
 '随着 MLB 越来越由数据分析主导，比赛变得越来越逻辑化；它愈发像棋局，而不像“国民消遣”。轻松态度打破单调，把趣味重新带回工作。')

add(21,'细节','Whom does Shaq praise as exceptionally hard-working in the interview quotation?',
 ['Patrick Bet-David.','Shohei Ohtani.','Kobe Bryant.','Every player on the team without distinction.'],2,
 '访谈引语中，Shaq 赞扬谁格外勤奋？',['帕特里克·贝特-戴维（Patrick Bet-David）。','大谷翔平（Shohei Ohtani）。','科比·布莱恩特（Kobe Bryant）。','全队每个人，不作区别。'],
 ['A 他是采访者，非这句话所赞扬对象。','B 这段访谈引语点名的是 Kobe。','C Kobe was a beast, nobody works harder than him 明确归属。','D 引语突出一个人，并非全队同等比较。这是 Shaq 访谈中的评价，不是本段对所有球员工时的客观实验测量。'],
 ['“Kobe was a beast, nobody works harder than him'],
 'work ethic','敬业精神；工作投入的态度','描述 Kobe 对艰苦训练的投入，不是正式工作时数的同义词','Her strong work ethic was evident in the care she took over each task.',['a strong work ethic','a grueling work ethic'],
 'Shaquille O’Neal 是另一位顶级运动员，作为球员既令人敬畏，也受人喜爱。与以艰苦训练精神著称的队友 Kobe Bryant 不同，Shaq 被认为没那么刻苦。在 Patrick Bet-David 的采访中，他说：“Kobe 太猛了，没有人比他更努力……那时 Kobe 刚结婚、开始进入家庭生活，而我已是四个孩子的父亲。”')

add(22,'作者意图','What does Shaq’s account of life after training help illustrate?',
 ['He had no responsibilities outside basketball.','His work coexisted with family and business roles, supporting the idea of different paths to success.','He claimed that two to three hours of work guarantees success for everyone.','He had abandoned both parenthood and business to train constantly.'],1,
 'Shaq 对训练后生活的叙述，有助于说明什么？',['篮球之外他没有责任。','工作与家庭、商业角色并存，呼应成功可有不同道路。','他声称任何人只工作二三小时都保证成功。','他为不断训练而放弃父亲角色与商业事务。'],
 ['A Daddy、husband、business 明列其他角色。','B 角色切换与 find success in many ways 相连，说明多种成功方式的论点。','C 这是自述，不是对所有人的时数处方或成功保证。','D 引语明确说训练后要履行这些角色，不是放弃它们。'],
 ['now I have to be Daddy, now I have to be husband, now I have to take care of business.','“I think you can find success in many ways.”'],
 'whimsical','随兴的；富有奇趣的','作者与 relaxed、lighthearted 并列描述 Shaq，不等于没有责任或从不工作','The display included a whimsical drawing of the city.',['a whimsical style','relaxed and whimsical'],
 '“所以，完成两到三小时的工作后，我还要当爸爸、当丈夫，还要处理商业事务。”在许多方面，Shaq 更放松、轻松而随兴。他在采访中接着说：“我认为成功可以有很多方式。”Shohei 和 Shaq 都相当成功。')

add(23,'推断','What does the counterfactual about Shaq’s work ethic allow the reader to conclude?',
 ['More achievement and earlier burnout are both presented as possibilities, not established outcomes.','Kobe’s work ethic definitely would have prevented any burnout in Shaq.','Shaq actually adopted Kobe’s exact work routine and was experimentally tested.','The passage proves that Shaq won no major awards.'],0,
 '关于 Shaq 敬业精神的反事实，允许读者得出什么？',['更多成就与更早倦怠都作为可能提出，并非已确立结果。','Kobe 的投入方式肯定会使 Shaq 永无倦怠。','Shaq 实际照搬 Kobe 作息并接受实验测量。','本段证明 Shaq 未获任何大奖。'],
 ['A If...had 与两个 might have 描述未实际验证的另一种过去，不可选定某一结果为事实。','B 第二个可能恰是 might have burned out early。','C 条件反事实不是实际发生或随机实验。','D 本段列出年度新人、MVP 和四次 NBA 冠军。人物荣誉按原书所列年份保留，不补写之后赛季。'],
 ['If Shaq had Kobe’s work ethic, Shaq might have accomplished even more as a basketball player. But he also might have burned out early in his career.'],
 'accomplished','取得成就；完成','might have accomplished 是对未实现过去的可能推测，不是新增真实成绩','With more time, the team might have accomplished more.',['accomplish more','might have accomplished'],
 '原书列出，Ohtani 是 2018 年美联年度新人、2021 与 2023 年 MVP；Shaq 是 1993 年年度新人、2000 年 MVP，赢得四次 NBA 冠军。如果 Shaq 有 Kobe 的敬业精神，他可能在篮球上取得更多成就。但他也可能在生涯更早阶段就倦怠。','inference')

add(24,'逻辑关系','What does “Even so” add to the acknowledgement of work ethic?',
 ['Work ethic is irrelevant to success.','Playfulness has already been proved to replace all practice.','Only carefree people can enter competitive professions.','Playfulness may also contribute to long-term success despite the importance of effort.'],3,
 '承认敬业精神重要后，Even so 补充什么？',['敬业精神与成功无关。','已证明玩心可取代全部练习。','只有无忧无虑的人才可进入竞争职业。','即使努力重要，玩心也可能有助长期成功。'],
 ['A 第一行 critical 明确认可其重要。','B might 不是已证明，contributor 也不是全部替代。','C 没有这种资格排除。','D 让步后增加可能被低估的因素，保留 both effort 与 playfulness 的空间。'],
 ['Even so, playfulness might be an underrated contributor to long-term success.'],
 'underrated','被低估的；未得到足够重视的','修饰玩心作为长期成功可能因素的评价，不等于它已被证明是唯一因素','The quiet colleague was an underrated contributor to the project.',['an underrated contributor','an underrated factor'],
 '众所周知，敬业精神对在职业体育及竞争性职业中上升至关重要。即便如此，玩心可能是一个被低估的长期成功因素。')

add(25,'细节','Which personality pattern is attributed to playfulness in this excerpt?',
 ['High conscientiousness with no openness or extraversion.','A complete absence of every personality trait.','Openness and extraversion combined with relatively less conscientiousness and neuroticism.','Neuroticism alone, with no other trait involved.'],2,
 '本片段把玩心归于什么人格组合？',['高尽责性，没有开放性或外向性。','所有人格特质都完全不存在。','开放性与外向性，并相对较少尽责性和神经质。','只有神经质，不涉及任何其他特质。'],
 ['A 原文明列 openness 和 extraversion，并说 relative lack of conscientiousness。','B relative lack 不是所有特质完全消失。','C 四项方向和 relative 的相对限定均对应。','D 不只一个特质，且神经质方向为相对较少。所引定义中的“愿意显得有点傻”不等于缺乏智力，relatively less 也不是完全没有责任感；本段并未证明玩心导致成功的确定因果。'],
 ['playfulness is a blend of openness to experience and extraversion, and a relative lack of conscientiousness and neuroticism.'],
 'ambiguity','模糊性；多重解释的空间','所引定义把模糊与双重含义视作智慧与乐趣的来源，不是样本数据不清的说法','The ambiguity of the joke allowed several interpretations.',['find ambiguity in','ambiguity and double edges'],
 '有没有经验证据表明玩心确实有益？瑞士心理学家 René Proyer 对成人玩心的研究，比我认识的其他人都深入。他发现，玩心是经验开放性、外向性，以及相对较少尽责性与神经质的结合。文中把它描述为“愿意显得有点傻的开放态度”，包含不那么担心表现能力、不自视过高、不把规范当成神圣，以及从模糊和双重意味中发现智慧与乐趣。')

assert len(out)==25 and [q['id'] for q in out]==[t['questionId'] for t in targets]

def persist():
 path=ROOT/'source/short-questions/additional.json';existing=load('source/short-questions/additional.json');byid={q['id']:q for q in existing}
 for q in out:
  if q['id'] in byid:assert byid[q['id']]==q,('Refuse to overwrite changed authoring',q['id'])
  else:existing.append(q)
 path.write_text(json.dumps(existing,ensure_ascii=False,indent=2)+'\n',encoding='utf8',newline='\n')
 review=dict(batchId='batch-018',date='2026-10-22',pdfSha256=b['pdfSha256'],checkedPdfPages=list(range(69,74)),questionIds=[q['id'] for q in out],paragraphs=[dict(id=pid,textSha256=hashlib.sha256(pp[pid]['text'].encode()).hexdigest()) for pid in dict.fromkeys(q['paragraphId'] for q in out)],note='完整 PDF 69–73 页视觉核对，含跨页运动研究、Sidis 叙事和 Shaq 引语。保留55项/6096人与各层级、起始年龄和专攻年龄区别、关联与建议、文学比喻、原书赛程上限与历史年份、appears/might及反事实；末段完整审阅多于本批题目上下文，候选句界不作人工最终分句。')
 (ROOT/'source/short-questions/review-chapter07-next25.json').write_text(json.dumps(review,ensure_ascii=False,indent=2)+'\n',encoding='utf8',newline='\n')
 print('Saved',len(out),'of 25 individually authored exercises')

if __name__=='__main__':persist()
