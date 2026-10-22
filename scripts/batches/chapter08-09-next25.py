"""25 individually authored exercises for frozen targets, PDF pages 85-90.
Preserve printed English, source positions and all previously published questions.
"""
from pathlib import Path
import json,hashlib
ROOT=Path(__file__).resolve().parents[2]
load=lambda p:json.loads((ROOT/p).read_text(encoding='utf8'))
b=load('public/data/book.json');plan=load('public/data/reading-plan.json');targets=load('source/short-questions/batch022-targets.json')['targets']
ss={s['id']:s for s in b['sentences']};pp={p['id']:p for p in b['paragraphs']};out=[]
def add(i,kind,prompt,options,answer,prompt_zh,options_zh,analyses,quotes,word,meaning,context,example,collocations,translation,support='explicit'):
 t=targets[i-1];u=next(u for u in plan['units'] if u['id']==t['readingUnitId']);group=[ss[sid] for sid in u['sentenceIds']];p=pp[u['paragraphId']];text=p['text'][group[0]['start']:group[-1]['end']]
 assert hashlib.sha256(text.encode()).hexdigest()==t['passageSha256'];evidence=[]
 for quote in quotes:
  offset=text.find(quote);assert offset>=0,(i,quote);start=group[0]['start']+offset;end=start+len(quote);touching=[s for s in group if s['start']<end and s['end']>start]
  evidence.append(dict(quote=quote,sentenceIds=[s['id'] for s in touching],sources=list({(r['pdfPage'],r['block']):r for s in touching for r in s['sources']}.values())))
 assert word.lower() in text.lower(),(i,word)
 out.append(dict(id=t['questionId'],version=1,readingUnitId=u['id'],chapterId=u['chapterId'],sectionId=u['sectionId'],paragraphId=u['paragraphId'],sentenceIds=u['sentenceIds'],passage=text,prompt=prompt,options=options,answer=answer,type=kind,promptZh=prompt_zh,optionsZh=options_zh,analyses=analyses,evidence=evidence,vocabulary=[dict(word=word,meaning=meaning,context=context,example=example,collocations=collocations)],translation=translation,support=support,editorialStatus='PDF 第 85–90 页逐题原页核对；固定原句与来源；保留外包调查与实验、自报、未实证推测、DIY回忆和反事实、文学引述及原书时点；原文连续无重复'))







add(1,'细节','What is the primary aim of outsourcing in the examples given?',
 ['To learn the professional’s specialist skills.','To make routine household work take longer.','To gain time by paying someone else to do the work.','To reduce the number of household tasks that exist.'],2,
 '这些例子中，外包的首要目的是什么？',['学习专业人士的专门技能。','让例行家务花更长时间。','付钱请别人做工作，以腾出时间。','减少家务本身的种类或数量。'],
 ['A 这里说请专业人士完成任务，没有说付费上课。','B more quickly 和 gain time 指节省时间，不是延长家务。','C primary goal...gain time 直接给出目的，清洁房屋只是例子。','D 任务由别人完成，不等于家务不再存在。$200 是举例价格，不是网站服务收费或普遍市场报价。'],
 ['The primary goal of outsourcing in this context is to gain time.'],
 'outsourcing','外包；请他人代做','把清洁等任务交给付费专业人士，以换取自己的时间','The family considered outsourcing the weekly cleaning.',['outsource household tasks','outsourcing routine work'],
 '外包是让现代生活更高效的一种方式。专业人士割草、清理排水沟，通常比个人做得更好、更快。在这里，外包的首要目的是获得时间。例如，你付二百美元请人清洁房屋。')

add(2,'有限推断','What does the reported survey pattern support?',
 ['Time-saving spending was linked with greater happiness and lower time stress in the respondents.','All respondents became happier after being randomly given cleaning services.','Material purchases were experimentally shown to cause time stress in all 4,469 respondents.','Time stress completely explained every difference in life satisfaction.'],0,
 '这里报告的调查模式支持什么？',['在受访者中，节省时间的支出与更幸福、较少时间压力相关。','所有受访者都被随机赠送清洁服务后变得更幸福。','实验表明实物购买使全部 4,469 人产生时间压力。','时间压力完全解释生活满意度的每一项差异。'],
 ['A were happier 与 less stressed 描述样本中的联系，适合用 linked with 表述。','B respondents 不代表随机赠送服务；也没有 all 均改善的结果。','C 当前是调查，未给实物购买的实验比较。','D in part 明确只是部分解释，不能写成完全解释。presumably 与 survey 不能合并成已证明普遍因果。'],
 ['across 4,469 respondents, those who spent some money every month to save free time were happier than those who didn’t.','This was in part explained by time stress'],
 'pressed for time','时间紧迫的；赶时间的','问卷提示语测量当天主观时间压力，不是测量实际工作分钟数','I felt pressed for time before the deadline.',['feel pressed for time','be pressed for time today'],
 '你省下几小时空闲时间，这想来会转化为更多幸福。Ashley Whillans 及同事发现，在 4,469 名受访者中，每月花一些钱来腾出空闲时间的人，比不这样做的人更幸福。这部分可以用时间压力解释；时间压力由“我今天觉得时间紧迫”这样的提示语测量。也就是说，花钱购买省时服务的人时间压力较小，而一个人越少为时间发愁，对整体生活就越满意。',support='limited-inference')

add(3,'细节','How was spending compared in the experiment?',
 ['Two groups each spent $80 on the same weekend.','Participants freely chose whether to spend all $80 on services.','Each participant spent $40 on services and materials together in one purchase.','Participants spent $40 on a time-saving service one weekend and $40 on a material purchase another weekend.'],3,
 '实验怎样比较两种支出？',['两组各在同一周末花八十美元。','参与者自由选择是否把八十美元全用于服务。','每人一次购买把四十美元同时用于服务和实物。','参与者一个周末用四十美元购买省时服务，另一周末用四十美元买实物。'],
 ['A 原文不是两组各花八十，也不是同一周末。','B told them to spend 给定两种用途，不是自由把全部钱用于服务。','C 拆为两个周末、各四十美元，非同一次混合购买。','D 两种消费由参与者在不同周末分别完成，联系发生在花钱当天。此处是为检验因果所做的实验，但本段没说周末顺序如何随机化，不能擅自补充。'],
 ['spend $40 on a time-saving service one weekend and spend the other $40 on a material purchase another weekend.'],
 'material purchase','实物购买；购买物质商品','与付钱节省时间的服务相比较的消费类别','She compared a material purchase with paying for a useful service.',['make a material purchase','a time-saving service versus a material purchase'],
 '随后，Whillans 及同事进行了实验，以检验省时支出的因果作用。他们给参与者八十美元，要求一个周末花四十美元购买省时服务，另一个周末把其余四十美元用于实物购买。研究者在参与者花这四十美元的当天联系他们。与买实物后相比，参与者报告在购买省时服务后有更多积极情绪、更少消极情绪。')

add(4,'逻辑关系','What relationship is reported between time pressure and happiness?',
 ['Greater time pressure was associated with greater happiness.','Lower time pressure went with higher reported happiness.','Time pressure stayed identical after both kinds of spending.','Lower time pressure eliminated every negative feeling.'],1,
 '原文报告时间压力与幸福有什么关系？',['时间压力越大，幸福越高。','时间压力越低，报告的幸福越高。','两种支出后的时间压力完全相同。','较低时间压力消除了每一种消极情绪。'],
 ['A 颠倒 the less...the more 的方向。','B less time pressure 与 more happiness 相对应，且幸福是 reported。','C felt less...after the time-saving service 表示时间压力较低，不是两者完全相同。','D less 不等于所有负面感受归零。本句的关系不能单独证明时间压力是幸福的唯一机制。'],
 ['the less time pressure they felt, the more happiness they reported.'],
 'time pressure','时间压力；时间紧迫感','参与者主观感到的赶时间程度，与报告的幸福相联系','A flexible schedule reduced her sense of time pressure.',['feel time pressure','less time pressure'],
 '同样，参与者在购买省时服务后感到较少时间压力；他们感到的时间压力越小，报告的幸福越多。')

add(5,'作者意图','Whose perspective qualifies the claim about repetitive tasks and working conditions?',
 ['Only the professional hired to perform the task.','Every person involved in the outsourcing arrangement.','At least the person paying for the service.','Only workers on a factory assembly line.'],2,
 '关于重复劳动和工作条件的陈述，原文限定在哪一方的视角？',['只限被雇来做事的专业人士。','外包安排中的每一个人。','至少指付钱购买服务的人。','只限工厂流水线工人。'],
 ['A 括号中说 paying，不是执行工作的受雇者。','B at least not for the person paying 不能扩大成所有参与者的条件都相同。','C 括号明确承认论述至少适用于付费者。','D division of labor 是对照，非括号限定的服务购买者。should 的幸福预期与末尾丰富性设问也应分开，不能把后者当已测结果。'],
 ['at least not for the person paying'],
 'detract from','减损；降低……的价值或程度','此处设问外包是否会减少心理丰富性，尚未给实证答案','The delay did not detract from our enjoyment of the visit.',['detract from psychological richness','detract from an experience'],
 '与劳动分工不同，外包不涉及重复任务和不人道的工作条件——至少对付钱的人而言如此。它的核心是腾出时间。只要你花钱让人做自己不想做的任务，并因此获得空闲时间，它应该会增加幸福。但外包是否也会像专门化和劳动分工那样，减损心理丰富性？')

add(6,'同义改写','Which statement preserves the evidence status of this claim?',
 ['A reduction in richness is possible, but the authors have not tested it empirically.','The authors’ experiment conclusively proved that outsourcing reduces richness.','The authors have ruled out any effect on psychological richness.','The authors have tested only workers and confirmed the effect for purchasers.'],0,
 '哪一陈述保留了这项主张的证据状态？',['丰富性可能减少，但作者尚未做实证检验。','作者的实验已确凿证明外包降低丰富性。','作者已排除外包对丰富性的任何影响。','作者只检验了工人，却确认了购买者的效果。'],
 ['A not empirically tested 与 possibility...could 同时保留。','B 把明确未检验改成已证实。','C 可能降低不等于排除任何影响。','D 没有工人样本或购买者确认的资料。IELTS 判断证据强度时，应把未实证的可能性与前面的幸福实验结果分开。'],
 ['We have not empirically tested this, but there is a possibility that outsourcing could reduce psychological richness.'],
 'empirically','以实证方式；通过实际观察或数据检验','作者明确承认尚未用实证数据测试外包对丰富性的这个判断','The hypothesis still needs to be tested empirically.',['empirically test a claim','not empirically tested'],
 '我们还没有对这一点进行实证检验，但外包有可能会减少心理丰富性。')

add(7,'细节','What made the couple consider doing the patio work themselves?',
 ['A contractor guaranteed they would finish for $4,000.','They had already earned $9,000 by selling the bricks.','They had confirmed the final project would save exactly $5,000.','The lowest quote was $9,000 while materials were about $4,000.'],3,
 '什么让夫妇考虑亲自动手修露台？',['承包商保证四千美元全部完工。','他们已通过卖砖赚了九千美元。','他们已确认最终恰好节省五千美元。','最低报价九千美元，而材料约四千美元。'],
 ['A 四千是材料成本，不是承包商全包保证。','B 原文只提估价与成本，没有卖砖收入。','C thought...couldn’t we 是当时的预计，不是完工后已确认的实际节省。','D 两个估计的差额让他们想到自己承担挖掘与劳动。这是个人项目价格，不是普遍施工报价或确保收益。'],
 ['the lowest price we found was $9,000. We checked the material cost, which was about $4,000.'],
 'estimates','估价；报价','雇人修露台前得到的费用预估，并非最终实际开销','We requested several estimates before choosing a builder.',['get a few estimates','the lowest estimate'],
 '一段时间以前，我和妻子考虑把杂乱的侧院改成砖砌露台。询了几个价，找到的最低报价是九千美元。我们查了材料成本，约四千美元。我们想，如果能省下至少五千美元，难道不能自己完成所有挖掘和劳动吗？')

add(8,'逻辑关系','How did the couple’s later experience compare with their initial impression?',
 ['The videos made the work seem impossible, but it proved effortless.','The work seemed manageable at first but required much more effort than expected.','They hired the video makers to complete all of the work.','They had anticipated the full workload before deciding to begin.'],1,
 '实际经历与夫妇最初的印象有什么差异？',['视频使工程看似不可能，实际却毫不费力。','起初看似可行，实际劳动远超预期。','他们雇视频制作者完成全部工作。','决定开工前，他们已完全预料工作量。'],
 ['A seemed doable 与 more work 把这个方向反转。','B doable 是起初判断，more...than...anticipated 是后来落差。','C decided to do it ourselves 是自己干，不是聘视频作者。','D more...than anticipated 明确表明低估。动机 Being cheap 是作者对自己的描述，不是实验对所有DIY者的结论。'],
 ['it seemed doable.','It was a lot more work than we had ever anticipated.'],
 'doable','可行的；做得到的','看视频后觉得可亲手完成，语气 seemed 并非客观保证容易','The repair seemed doable with the tools we had.',['seem doable','a doable project'],
 '我们看了几个 YouTube 视频，感觉可行。为了省钱，我们决定自己做。接下来就是典型的 DIY 故事了。工作量比我们原先预想的多得多。')

add(9,'语境词义','What does “taxing” mean in the description of preparing the ground?',
 ['Requiring payment of a government charge.','Increasing the value of the house automatically.','Physically demanding and tiring.','Reducing the number of bricks needed.'],2,
 '在准备地面的描述中，taxing 是什么意思？',['需要缴纳政府税费。','自动提高房屋价值。','费体力、令人疲惫的。','减少所需砖块数量。'],
 ['A tax 可指税，但这里形容夯实地面的劳动，不是税务。','B 没有房屋估值信息。','C hard、insanely difficult、backbreaking 构成费力语境，支持 demanding。','D 任务目的是形成平整牢固底座，未说减少砖数。这里报告艰难体力经历；不能仅凭 backbreaking 一词给出骨折诊断。'],
 ['Tamping down the ground to create a firm and level base for bricks was taxing.'],
 'taxing','费力的；使人劳累的','这里指夯实地基费体力，不是征税','Carrying heavy boxes upstairs was a taxing task.',['a taxing task','physically taxing'],
 '在二十乘二十四英尺、倾斜、布满树根且黏土硬如石头的院子里挖下九英寸，很不容易。把地面夯实，为砖块做出牢固平整的底座，也很费力。房子在山坡顶，工地又在车道另一侧，用独轮车搬三百袋碎石和沙子，极其困难。更别提搬两千块砖了——真让人腰背累垮。')

add(10,'细节','What reaction to the DIY decision is reported during the project?',
 ['They consistently felt certain they had made the best choice.','They blamed only the contractor who had done the work.','They regretted spending the project’s entire budget on hired labor.','They repeatedly questioned the choice and regretted not hiring help.'],3,
 '项目进行时，他们对 DIY 决定有什么反应？',['始终确信自己作了最佳选择。','只责怪完成工程的承包商。','后悔把全部预算花在雇人上。','反复质疑选择，后悔没请人来做。'],
 ['A questioned...many times 与始终确信相反。','B blamed each other 是互相埋怨，没有已雇的承包商。','C regretted not hiring 指没雇人，而非雇工超支。','D 疼痛、质疑、互责和后悔没雇人是此时的经历。这里有很多早晨无法起床的自述，不宜改成三个月每一天都无法活动。'],
 ['We questioned our decision many times. We blamed each other many times. We regretted not hiring someone else to do it instead.'],
 'regretted','后悔；感到遗憾','regretted not hiring 表示后悔当初没有请人，不是后悔请了人','They regretted not asking for advice earlier.',['regret not doing something','regret a decision'],
 '有许多个早晨，我因为背痛起不来。我们多次质疑自己的决定，多次互相埋怨，后悔没有请别人来做这件事。')

add(11,'有限推断','What uncertainty remains in the author’s assessment after completion?',
 ['Whether much money was really saved once their time was considered.','Whether they had completed the patio at all.','Whether the hired contractor actually took three months.','Whether their result was better than professional work.'],0,
 '完工后的评价中，作者仍不确定什么？',['考虑投入时间后，究竟有没有省下很多钱。','是否真的完成了露台。','已雇承包商是否实际做了三个月。','他们的成果是否胜过专业施工。'],
 ['A Given how many hours...weren’t sure 明确对实际节省存疑。','B took...to complete 表明已完成。','C 三个月是自己施工；三至四天是作者设想九千美元专业施工可达到的比较，不是已经雇人后实测。','D clearly not as good 已给评价，并非仍不确定成果是否更好。个人工时价值未给出，不能编造最终准确盈亏。'],
 ['Given how many hours we spent on the project, we weren’t sure if we’d saved much money in the end, either.'],
 'accomplished','完成；实现','would have accomplished 指作者设想专业施工本可达到的效果，不是已发生的第二次工程','The team accomplished the repair in two days.',['accomplish a project','what the payment would have accomplished'],
 '工程花了我们将近三个月才完成。最终效果相当不错，但显然不如花九千美元本可在三至四天实现的效果！考虑到投入了那么多小时，我们也不确定最后是否真的省了很多钱。',support='limited-inference')

add(12,'逻辑关系','What contrast is introduced by “And yet” at the start?',
 ['The author no longer remembers anything about the project.','The project remained memorable years later despite the earlier difficulties.','Seeing a snake made the author an experienced bricklayer immediately.','The family had outsourced the entire project before the snake appeared.'],1,
 '开头的 And yet 引出什么对比？',['作者已不记得工程的任何事情。','尽管先前很艰难，多年后项目仍留下可谈的记忆。','见到蛇使作者立即成为熟练砌砖工。','蛇出现前，全家已把整个工程外包。'],
 ['A still talk about memories 正好相反。','B And yet 转向 years later 的持续记忆；后面给挖到蛇的具体故事。','C 见蛇与技能没有这种即时因果；末句只说此前从未砌过砖。','D While digging 指作者参与挖掘，不是全部外包。garden snake 的描述是事件叙述，不能由惊叫推出蛇造成实际袭击。'],
 ['And yet, years later, we still talk about memories from our patio project.'],
 'hibernation','冬眠','被发现的花园蛇处于冬眠状态，解释场景，不是人进入休眠','The animal emerged from hibernation in spring.',['in hibernation','a snake in hibernation'],
 '然而，多年以后，我们仍会谈起露台工程的回忆。一天挖土时，我看到一条蛇，尖叫起来！我怕蛇，所以跳了起来，尽管那只是一条正在冬眠的花园蛇。做这个项目之前，我从未砌过砖。')

add(13,'细节','What new ability does the author say he discovered?',
 ['He was already an expert at every kind of repair.','He could safely remove every kind of snake.','He was reasonably good at brick edging.','He could finish any patio faster than a professional.'],2,
 '作者说自己发现了什么新能力？',['自己本来就是各种维修的专家。','能安全处理各种蛇。','自己在砌砖收边方面还不错。','能比专业人士更快完成任何露台。'],
 ['A not very handy 及 pretty low 的自评不支持原本全面精通。','B 这里发现的是砖边技能，没有处理各种蛇的能力证据。','C not half bad at brick edging 是“在砌砖收边上挺不错”的自我发现。','D 没有速度胜过专业人士，不能从某技能扩大成任何露台。If we had hired...would...Probably not 是未实际发生的反事实猜想，不是对照实验。'],
 ['I discovered that I’m not half bad at brick edging—a new discovery about myself.'],
 'not half bad','还不错；颇可以','一种委婉肯定，表示砖砌收边做得比自己原先预期好','For a first attempt, the result was not half bad.',['not half bad at something','be not half bad'],
 '总体上，我不太擅长动手，所以对自己动手能力的自信很低。但经过这番努力，我发现自己砌砖收边还挺不错——这是对自己的新发现。假如请人包办一切，我现在还会谈起它吗？大概不会，因为我就不会发现冬眠的蛇，也不会发现自己未曾知道的砌砖收边技能。')

add(14,'逻辑关系','How does the author distinguish short-run and long-run consequences?',
 ['Hiring help might have brought more short-run happiness, while doing it themselves left a richer store of stories and emotions.','Doing it themselves produced no negative feelings at the time and no later memories.','Hiring help actually gave them all the same stories while removing every cost.','The project guaranteed permanent happiness and erased memories of pain.'],0,
 '作者怎样区分短期与长期后果？',['雇人本可能增加短期幸福，亲手做则留下更多故事与情绪记忆。','亲手做当时毫无负面感受，后来也无记忆。','雇人实际上既给了相同故事又去除所有成本。','工程保证永久幸福，并抹去痛苦记忆。'],
 ['A would have 是外包的反事实判断；In the long run 则转向如今真实拥有的故事、骄傲与苦痛记忆。','B 明说 stress、pain、unhappiness，且现在有故事可讲。','C 没有实际采取外包，也没观察到“全部同样故事”。','D memories of agony and pain 并未消失，丰富性也不等于永久幸福。不能把痛苦本身概括成总是值得或必然有益。'],
 ['Outsourcing would have increased happiness in the short run.','In the long run, however, we now have far more stories'],
 'undiluted','未经稀释的；强烈而完整的','形容亲历后保留的原初骄傲，不是液体浓度','She felt undiluted pride in the work she had completed herself.',['undiluted raw emotion','undiluted pride'],
 '确实，露台项目在那三个月里带来许多压力、身体疼痛和不快乐。外包本会增加短期幸福。不过从长远看，我们如今有更多故事可讲给朋友，还有未被稀释的原初骄傲、成就感，以及煎熬与痛苦的记忆。')

add(15,'主旨','What distinction does the author draw between routine cleaning and building a patio?',
 ['Both are said to offer exactly the same stories and learning.','Outsourcing any routine task is presented as a serious mistake.','Patio building is described as easier than cleaning the house.','Outsourcing an unusual project may forgo richer experiences, whereas routine cleaning is portrayed as offering few stories.'],3,
 '作者在例行清洁与建露台之间作了什么区分？',['两者提供完全相同的故事和学习。','把任何日常任务外包都是严重错误。','建露台比打扫房屋容易。','外包特别项目可能错过丰富体验，而日常清洁被描写为较少产生故事。'],
 ['A In contrast 表示不同，不是完全等同。','B routine cleaning would have no opportunity cost 是作者对清洁的判断，并非所有外包都错。','C 这里比较故事与机会成本，不比较施工难度。','D 同时保留少故事的清洁与 might、could 限定下的露台机会成本。这是作者论证，非本段新增实验，也不能推广成任何人的日常清洁都绝无意义。'],
 ['cleaning your house by yourself might not generate many interesting stories.','outsourcing a project like building a brick patio might be a mistake'],
 'opportunity cost','机会成本；为某选择放弃的其他机会价值','这里指外包后失去亲历有趣项目的可能，不只是现金支出','Choosing the faster route had an opportunity cost: we missed the village.',['opportunity cost for psychological richness','consider the opportunity cost'],
 '就心理丰富性而言，把例行清洁外包不会有机会成本。毕竟，自己清洁房屋可能不会产生多少有趣故事。除了省些钱，这样做还有什么意义呢？相比之下，把建砖露台这样的项目外包可能是个错误，因为它可能带来心理丰富性方面的机会成本。')

add(16,'同义改写','Which paraphrase best matches the warning about hiring someone?',
 ['Hiring someone deliberately removes every source of happiness.','Paying for the work may unintentionally mean missing a potentially enriching experience.','Every hired worker prevents the employer from learning any skill.','An interesting life story can only come from unpaid manual work.'],1,
 '哪种改写最符合关于雇人代做的提醒？',['雇人会有意消除每个幸福来源。','付费请人做可能无意间让自己错过一段潜在的丰富体验。','每个雇工都阻止雇主学习任何技能。','有趣人生故事只能来自无薪体力劳动。'],
 ['A inadvertently 是无意，不是故意；richness 也不能换成所有幸福。','B may、unintentionally、potentially 分别守住 might、inadvertently、could。','C 原文没把受雇者说成蓄意阻止学习的人，也没有 every。','D an opportunity 不是唯一来源，不能加入 only。同义改写题除了保留内容，还要保留可能性和行为意图。'],
 ['might inadvertently rob you of an opportunity to have an interesting experience that could add richness to your life story.'],
 'inadvertently','无意间；不经意地','雇人本为省事，却可能并非有意地失去体验机会','She inadvertently missed a chance to meet the visiting writer.',['inadvertently rob someone of an opportunity','inadvertently miss a chance'],
 '雇人完成工作，可能会无意间剥夺你一次有趣体验的机会，而这次体验原本可能为你的人生故事增添丰富性。')

add(17,'主旨','What shared point is illustrated by the motorcycle, patio and generalist examples?',
 ['Richer engagement may require taking on a harder or broader task rather than the easiest route.','Specialization always demands broader perspectives than generalist work.','Building a patio is presented as less demanding than hiring someone.','Efficiency and psychological richness are defined as exactly the same thing.'],0,
 '摩托车、露台和通才的例子共同说明什么？',['更丰富的投入可能要求承担更难或更广的任务，而非最省事的路。','专才工作总比通才工作要求更广视角。','建露台被说成比雇人更轻松。','效率与心理丰富性被定义为同一回事。'],
 ['A lean into...challenging 与三项完整、困难或广泛参与的例子相呼应。','B generalist requires broader perspectives 比较方向相反。','C much harder 才是原文。','D 三例强调额外付出与丰富性的可能联系，不是概念相等。首句是本书作者的建议，不是网站要求用户执行危险行为或对所有挑战保证收益。'],
 ['we must lean into the unfamiliar, the risky, and the challenging.','Being a generalist requires broader perspectives than being a specialist.'],
 'lean into','主动投入；迎向','作者鼓励接近不熟悉和有挑战的体验，不是身体倾斜的字面动作','She decided to lean into the unfamiliar task and learn as she went.',['lean into a challenge','lean into the unfamiliar'],
 '为培养生活中的心理丰富性，我们必须主动迎向不熟悉、有风险和有挑战的事。组装整辆摩托车，比只组装其中一个部件困难、费时得多。建砖露台比请人代做难得多。成为通才比成为专才需要更广的视角。')

add(18,'逻辑关系','What trade-off should the two self-directed questions help a reader consider?',
 ['Whether every familiar activity guarantees lifelong richness.','Whether all negative emotions should be eliminated before starting any task.','Whether doing a challenging job oneself could yield a story despite short-run discomfort.','Whether hiring someone always produces more stories than doing it oneself.'],2,
 '这两个向自己提的问题，帮助读者考虑什么取舍？',['每项熟悉活动是否保证终身丰富。','开始任务前是否必须消除所有负面情绪。','尽管短期可能不舒服，亲手完成挑战是否能留下故事。','雇人是否总比亲手做产生更多故事。'],
 ['A familiar...doesn’t generate much richness 不支持这种保证。','B can produce negative emotions 并非先清零负面体验。','C Could I do it myself 与 Would I have an interesting story 把可行性、故事价值放进短长期权衡。','D 问的是自己做能否有故事，不是断言雇人总更多。can...also add 保留可能性，不能把挑战必然丰富化。'],
 ['a challenging project can produce a lot of negative emotions in the short run, it can also add psychological richness in the long run.'],
 'in the long run','从长远来看','与 short run 对照，指经历过后可能积累的丰富性，不保证立即开心','In the long run, learning the process gave her more confidence.',['in the long run','in the short run'],
 '熟悉的事物带来可靠的幸福，但不产生多少丰富性。相比之下，尽管有挑战的项目短期内可能引起许多负面情绪，长期也能增添心理丰富性。请人做事之前，问问自己：我能自己做吗？如果自己做，我会有一个有趣故事可讲吗？')

add(19,'作者意图','What change does the closing invitation recommend?',
 ['Never paying attention to productivity in any area of life.','Replacing all paid work permanently with bread making.','Finding the fastest available method for every everyday activity.','Occasionally choosing a slower hands-on way to add variety to life.'],3,
 '结尾的邀请建议作什么改变？',['生活任何领域都永不考虑生产力。','永久把所有有偿工作换成烤面包。','为每项日常活动寻找最快方法。','偶尔选较慢、亲手做的方式，为生活增添变化。'],
 ['A once in a while 限定为偶尔，不是永不考虑。','B bake...hand-grind 是生活例子，不是永久改职业。','C slower way 与一律最快相反。','D 偶尔离开效率优先、用DIY增添 spice 的意思完整。spice 是比喻性的趣味变化，不要求实际给咖啡或面包加某种香料。'],
 ['Escape the productivity trap once in a while.','Think of a slower way to do the same thing'],
 'once in a while','偶尔；有时','限定离开生产力陷阱的频率，不是彻底放弃效率','Once in a while, we cook a meal entirely from scratch.',['once in a while','escape the routine once in a while'],
 '效率就是一切吗？偶尔逃离生产力陷阱吧。想一种较慢的方式来做同一件事——自己烤面包，亲手研磨咖啡豆……自己动手，为生活增添一点趣味。')

add(20,'作者意图','What question opens the discussion of aesthetic experience?',
 ['Whether direct experiences have ever been discussed before.','Whether reading novels can offer richness comparable to direct experiences.','Whether building a patio is a form of publishing a novel.','Whether study abroad is the only possible source of richness.'],1,
 '关于审美体验的讨论以什么问题开头？',['此前是否曾讨论直接体验。','读小说能否提供与直接体验相似的心理丰富性。','建露台是否是一种出版小说的行为。','留学是否是心理丰富性的唯一来源。'],
 ['A I have discussed so far 承认此前已有讨论。','B 把 firsthand 的例子与 aesthetic experiences such as reading novels 联系起来，正是章节设问。','C 两类体验在比较，不是说建造就是出版。','D like...and... 提供多个例子，没有 only。Can 是引出主题的设问，此处还不是新实验发现。'],
 ['Can aesthetic experiences such as reading novels produce the same kind of psychological richness?'],
 'firsthand','亲身的；直接经历的','留学、建露台属于自己参与的体验，与通过小说的体验相对照','The report included firsthand accounts from local residents.',['firsthand experience','firsthand accounts'],
 '到目前为止，我讨论的大多数心理丰富体验都是亲身、直接的体验，例如留学和建露台。读小说这样的审美体验，能产生同样的心理丰富性吗？')

add(21,'细节','What purpose is given for Aziz’s becoming a fisherman?',
 ['To make a living and try to realize his dream of finishing high school.','To finance a bookstore he already owned at age six.','To avoid ever returning to education because he disliked books.','To retire from bookselling after a completed university degree.'],0,
 '原文说 Aziz 为什么成为渔夫？',['谋生，并努力实现高中毕业的梦想。','为六岁时已拥有的书店筹款。','因讨厌书而永不再上学。','大学毕业后从卖书退休。'],
 ['A make a living 与 dream of graduating high school 是两个明示目的；try 表示努力，不等于已毕业。','B 六岁时发生的是失去父母，不是已有书店。','C 本片段给出求学梦想，没有厌书或放弃一切教育的动机。','D 没有大学学位或退休信息。seventy-two-year-old 是书中人物叙述的年龄，不能直接当作现在年龄。'],
 ['He became a fisherman to try to make a living and achieve his dream of graduating high school.'],
 'orphaned','成为孤儿的；失去父母的','说明 Aziz 六岁时的处境，不是六岁开始经营书店','The story follows a child orphaned at an early age.',['be orphaned at age six','an orphaned child'],
 'Mohammed Aziz 肯定会回答“能”。Aziz 是 Morocco 的 Rabat Medina 一位七十二岁的书商。他六岁时成了孤儿。他做渔夫，试图维持生计，并实现高中毕业的梦想。')

add(22,'细节','What forced Aziz to leave school at fifteen?',
 ['His lack of interest in reading novels.','The cost of maintaining a bookstore he already owned.','The high price of textbooks.','A requirement to spend eight hours a day selling books.'],2,
 '什么迫使 Aziz 十五岁时退学？',['他对读小说毫无兴趣。','维持已拥有书店的费用。','教材价格高昂。','每天必须卖书八小时的规定。'],
 ['A high cost 是财务原因，不是缺乏读书兴趣。','B 原因是教材费用，开卖书事业发生在挫折之后。','C the high cost of textbooks 直接对应。','D six to eight hours 是书中所述每天阅读时间，不是当年卖书的规定。末尾引语在既有短段边界处续到下一段，保留原英文省略号，不补造引文。Now 指书中叙述时点。'],
 ['at age fifteen, the high cost of textbooks forced him to drop out.'],
 'channeled','把……转向；将情绪投入某方向','把退学挫折转化为卖书事业的动力，而非情绪消失的测量','She channeled her frustration into learning a new skill.',['channel frustration into a career','channel energy into something'],
 '然而，十五岁时，高昂的教材费用迫使他退学。他把这种挫折转向卖书的事业，起初只有一张地毯和九本书，摆在树荫下。如今他拥有一家书店，每天花六至八小时阅读。在访谈中他说：“我的生活围绕阅读展开……（引语续下段）')

add(23,'语境词义','What is meant by Aziz’s statement about living more than 4,000 lives?',
 ['He has held more than 4,000 paid jobs during his lifetime.','Reading many books has let him imaginatively experience many lives.','He has taken more than 4,000 separate vacations.','The passage reports a scientific count of literal reincarnations.'],1,
 'Aziz 所说活过四千多种人生是什么意思？',['一生做过四千多份有薪工作。','阅读许多书，让他在想象中体验许多人生。','他已度过四千多次独立假期。','片段报告对真实轮回次数的科学计数。'],
 ['A lives 由 books 的阅读经验引出，不是职业数量。','B read...books, so...lives 将阅读与想象中的人生体验联系，是比喻。','C rarely takes vacations 恰好表明很少休假。','D 这是人物引语与作者阐释，没有转世实验。十二小时工作与心理丰富并列，不能把长工时本身当成丰富性的确定原因。'],
 ['I’ve read more than 4,000 books, so I’ve lived more than 4,000 lives.'],
 'All the same','尽管如此；仍然','在工作时间长、很少休假后，转向仍通过阅读积累丰富体验','The journey was tiring. All the same, we were glad we went.',['all the same, he has','all the same, the experience'],
 '“我读过四千多本书，所以我活过四千多种人生。”Aziz 每天工作十二小时，很少休假。尽管如此，通过四千本书活过四千种人生，他积累了大量心理丰富的体验。')

add(24,'细节','Where did the dramatic events filling Proust’s afternoons take place?',
 ['In journeys he physically made during every afternoon.','In experiments comparing readers with nonreaders.','In meetings with the novelist at his house.','In the book he was reading.'],3,
 '填满 Proust 下午时光的戏剧性事件发生在哪里？',['他每个下午亲身进行的旅行中。','比较读者与不读书者的实验中。','他家中与小说家的会面中。','他正在阅读的书中。'],
 ['A events taking place in the book 明确是书中事件，不是每次实际旅行。','B 此处文学反思，不是实验设计。','C 没有会见小说家的场景。','D 第二句引语直接说明事件发生位置。whole lifetime 是对阅读强度的文学比较，不是实际统计每个读者人生事件数量。'],
 ['These were the events taking place in the book I was reading.'],
 'crammed with','挤满；充满','形容阅读的下午密集经历戏剧性事件，不是屋里挤满实体人物','The short visit was crammed with unexpected discoveries.',['be crammed with events','afternoons crammed with drama'],
 '在其杰作 In Search of Lost Time 的开篇卷 Swann’s Way 中，Marcel Proust 回顾自己的阅读体验：“那些下午充满了戏剧性事件，其数量往往超过一生中发生的事件。那些都是发生在我正在阅读的书里的事件。”')

add(25,'主旨','What conclusion does the author draw from the novelist’s power described here?',
 ['Books can make a psychologically rich life possible through access to many emotions.','Only direct travel can reveal emotions to a reader.','Every reader is guaranteed to feel all emotions within exactly one hour.','Reading removes the need for any firsthand experience in every life.'],0,
 '作者从这里描述的小说家力量得出什么结论？',['书能让人接触多种情绪，从而使心理丰富人生成为可能。','只有亲自旅行能让读者认识情绪。','每位读者都保证在恰好一小时内体验全部情绪。','阅读使每个人都不再需要任何亲身体验。'],
 ['A 最后 possible...via books 明示可能性，前面的 joys and sorrows 提供文学说明。','B 小说家的作用就是让人接触原本需要多年或不会亲历的情绪，不限旅行。','C 文学引语的 hour 不是给所有人的实测时限与保证。','D possible via books 不是阅读排除或替代全部直接体验。应区分作者结论与作为支持例子的 Proust 文学引述。'],
 ['it is possible to lead a psychologically rich life via books.'],
 'wield','运用；施展','形容小说家运用文字使读者感受情绪的文学力量，不是挥舞实物','The writer wields language with unusual precision.',['wield magic','wield the power of words'],
 '他接着描述小说家施展的魔力，说“在一个小时里，他［小说家］在我们内心释放世间全部喜悦与悲伤；其中仅仅少数，就需我们花真实人生中的多年才能认识，而最强烈的一些原本永远不会向我们显露”。因此，确实有可能通过书籍过一种心理丰富的人生。')

assert len(out)==25 and [q['id'] for q in out]==[t['questionId'] for t in targets]

def persist():
 path=ROOT/'source/short-questions/additional.json';existing=load('source/short-questions/additional.json');byid={q['id']:q for q in existing}
 for q in out:
  if q['id'] in byid:assert byid[q['id']]==q,('Refuse to overwrite changed authoring',q['id'])
  else:existing.append(q)
 path.write_text(json.dumps(existing,ensure_ascii=False,indent=2)+'\n',encoding='utf8',newline='\n')
 review=dict(batchId='batch-022',date='2026-10-22',pdfSha256=b['pdfSha256'],checkedPdfPages=list(range(85,91)),questionIds=[q['id'] for q in out],paragraphs=[dict(id=pid,textSha256=hashlib.sha256(pp[pid]['text'].encode()).hexdigest()) for pid in dict.fromkeys(q['paragraphId'] for q in out)],note='完整PDF85–90原页视觉核对；外包4469人调查与80美元实验分开，未实证的丰富性损失不作结果；DIY为个人回忆，专业价格/工期与外包体验属反事实比较；Aziz的年龄与现在按书中时点，4000人生为阅读比喻，Proust为文学反思。引语跨短段处不增删英文引号或省略号，全句ID仍为候选。')
 (ROOT/'source/short-questions/review-chapter08-09-next25.json').write_text(json.dumps(review,ensure_ascii=False,indent=2)+'\n',encoding='utf8',newline='\n')
 print('Saved',len(out),'of 25 individually authored exercises')

if __name__=='__main__':persist()
