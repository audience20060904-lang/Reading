"""25 individually authored exercises for frozen targets, PDF pages 106-111.
Preserve printed English, source positions and all previously published questions.
"""
from pathlib import Path
import json,hashlib
ROOT=Path(__file__).resolve().parents[2]
load=lambda p:json.loads((ROOT/p).read_text(encoding='utf8'))
b=load('public/data/book.json');plan=load('public/data/reading-plan.json');targets=load('source/short-questions/batch027-targets.json')['targets']
ss={s['id']:s for s in b['sentences']};pp={p['id']:p for p in b['paragraphs']};out=[]
def add(i,kind,prompt,options,answer,prompt_zh,options_zh,analyses,quotes,word,meaning,context,example,collocations,translation,support='explicit'):
 t=targets[i-1];u=next(u for u in plan['units'] if u['id']==t['readingUnitId']);group=[ss[sid] for sid in u['sentenceIds']];p=pp[u['paragraphId']];text=p['text'][group[0]['start']:group[-1]['end']]
 assert hashlib.sha256(text.encode()).hexdigest()==t['passageSha256'];evidence=[]
 for quote in quotes:
  offset=text.find(quote);assert offset>=0,(i,quote);start=group[0]['start']+offset;end=start+len(quote);touching=[s for s in group if s['start']<end and s['end']>start]
  evidence.append(dict(quote=quote,sentenceIds=[s['id'] for s in touching],sources=list({(r['pdfPage'],r['block']):r for s in touching for r in s['sources']}.values())))
 assert word.lower() in text.lower(),(i,word)
 out.append(dict(id=t['questionId'],version=1,readingUnitId=u['id'],chapterId=u['chapterId'],sectionId=u['sectionId'],paragraphId=u['paragraphId'],sentenceIds=u['sentenceIds'],passage=text,prompt=prompt,options=options,answer=answer,type=kind,promptZh=prompt_zh,optionsZh=options_zh,analyses=analyses,evidence=evidence,vocabulary=[dict(word=word,meaning=meaning,context=context,example=example,collocations=collocations)],translation=translation,support=support,editorialStatus='完整PDF106–111原页视觉核对及跨页拼接；CDC关联不作因果保证；100/1000候选、14%/3%与前10%目标分开。费城许可证、荷兰个人筛选与MIT友谊提名单位分开，众数/中位数与测量时点不混用；Cupid为比喻；宿舍随机背景按作者概括保留，不冒充完整随机试验方案。功能距离研究与后续曝光机制实验分开。末段完整审阅含未配题词频比较，未声称全书逐句证据覆盖。'))







add(1,'推断','Which conclusion is supported by the CDC data as described?',
 ['Longer exploration guarantees that a marriage will last.','Shorter exploration is associated with a greater likelihood of divorce.','Divorce causes couples to shorten their premarital exploration.','Every long exploration ends in marriage.'],1,
 '按片段描述，CDC 数据支持哪项结论？',['探索久保证婚姻持续。','探索较短与更高离婚可能性相关。','离婚导致婚前探索缩短。','每次长期探索都以婚姻告终。'],
 ['A on average 是平均趋势，不能保证个体结果。','B more likely 明示两组离婚可能性的比较；观察性数据不能单独证明因果。','C 颠倒时间和论证方向，原文没有检验反向因果。','D 数据讨论已婚者的稳定性，没有追踪每次探索是否结婚。'],
 ['more likely to end their marriage in divorce than those who spend more time exploring before marriage.'],
 'marital stability','婚姻稳定性','指婚姻维持的平均趋势，不是个人必然结果','The survey examined marital stability over time.',['marital stability','greater marital stability'],
 'CDC 数据表明，花较少时间探索的人（开始认真交往后很快结婚的人），确实比婚前花更多时间探索的人更可能以离婚结束婚姻。因此，平均而言，探索越多，婚姻越稳定。')

add(2,'逻辑关系','Why do Todd and Miller question the 37 percent rule here?',
 ['CDC data directly contradict all search models.','Animals can always identify the single best mate.','Finding a top-tier mate may matter more than identifying the single best one.','The rule requires animals to choose the worst available mate.'],2,
 'Todd 和 Miller 在这里为何质疑 37% 规则？',['CDC 数据直接反驳全部搜索模型。','动物总能辨认唯一最优配偶。','找到优质对象可能比认出唯一最优者更重要。','规则要求动物选最差对象。'],
 ['A consistent with 明说数据与规则相符，不是矛盾。','B can’t really tell 恰表明难以区分。','C best possible 与 top 10 percent 的区别，以及 isn’t critical，支持改变最优目标的质疑。','D 文中没有最差对象这一要求。这里只列质疑理由，尚未给新搜索比例。'],
 ['animals can’t really tell the difference between the best possible mate and a top 10 percent mate.','for animals, finding the best mate isn’t critical.'],
 'take issue with','对……提出异议','对规则的适用理由提出质疑，不等于全盘否定数据','The reviewer took issue with the proposed criterion.',['take issue with a rule','take issue on several grounds'],
 'CDC 数据与 37% 规则相符。不过，Peter Todd 和 Geoffrey Miller 从几个方面质疑该规则。例如，动物实际上难以区分最好的配偶与位居前 10% 的配偶。而且，对动物来说，找到最好的配偶并非至关重要。')

add(3,'细节','Under what condition does examining the first 14 percent yield the highest success probability?',
 ['There are 100 potential mates and success means finding one of the best options.','There are 1,000 potential mates and success means finding the single best.','The goal remains the single best among 100 candidates.','The first 14 percent must all become partners.'],0,
 '在什么条件下，先看 14% 的成功概率最高？',['100 个候选，成功目标是优质选项之一。','1,000 个候选，目标是唯一最优者。','100 个候选，目标仍是唯一最优者。','前 14% 必须全成为伴侣。'],
 ['A change...one of the best 与 set to 100 同时限定结果。','B 候选数和成功标准都换了。','C 忽略从 best 到 one of the best 的关键变化。','D looking at 是考察，不是与所有人建立伴侣关系。模型概率不能当现实成功承诺。'],
 ['change the criterion from the best option to one of the best options?','looking at the first 14 percent instead of the first 37 percent','when the number of potential mates is set to 100.'],
 'cursory','简略的；较不深入的','相对于考察 37%，先考察的比例更小','A cursory search revealed several promising choices.',['a cursory search','a more cursory search'],
 '相反，重要的是能找到最佳选项中的一个（如前 10%）。如果把标准从唯一最佳改成最佳选项之一，会怎样？当潜在配偶数设为 100 时，更简略的搜索——先看 14% 而不是 37%——带来最高成功概率。')

add(4,'细节','What procedure is described for 100 potential mates?',
 ['Reject all candidates after examining the first 14.','Choose the best of the first 14 retrospectively.','Select exactly the fourteenth candidate regardless of quality.','Examine the first 14, then choose the next candidate who exceeds their best.'],3,
 '100 个潜在对象时，片段描述什么步骤？',['考察前 14 个后拒绝所有人。','回头选择前 14 个中最好的。','不论质量直接选第 14 个。','考察前 14 个，再选随后超过其中最佳者的对象。'],
 ['A then pick 明确还要选择。','B next mate 表示随后遇见者，不是回头挑。','C 14 是基准样本数，不是固定获选序号。','D better than the best one from the first 14 明示比较门槛。开头 3% 是 1,000 候选时的搜索比例，不是前 10% 的质量标准。'],
 ['look at the first 14 mates carefully and then pick the next mate that is better than the best one from the first 14.'],
 'potential','潜在的；可能的','尚未成为实际伴侣的候选对象','The list included a hundred potential applicants.',['potential mates','potential candidates'],
 '当潜在配偶数设为 1,000 时，只先搜索 3% 这一更简略的做法，找到前 10% 对象的概率最高。换句话说，若有 100 个潜在对象，你只需仔细考察前 14 个，再选随后遇到的、比前 14 个中最佳者更好的人。')

add(5,'同义改写','Which statement restates the rule for 1,000 potential mates?',
 ['Choose one of the first 30 without comparing later candidates.','Use the best of the first 30 as a benchmark for a subsequent choice.','Wait until all 1,000 have been considered before choosing.','Treat the first 30 as the only acceptable partners.'],1,
 '哪项准确改述 1,000 个候选时的规则？',['不比较后来对象，直接选前 30 个之一。','以前 30 个中最好者为基准，选择后来的对象。','看完全部 1,000 个才选择。','只有前 30 个才可接受。'],
 ['A next one 表示选择在基准组之后。','B better than the best of the first 30 保留基准与后续选择关系。','C 无需看遍全部的步骤。','D 前 30 个用于考察，不是唯一获选范围。末句是作者认为更合理的评价，不是保证每人幸福。'],
 ['look at 30 mates carefully and pick the next one that is better than the best of the first 30.'],
 'reasonable','合理的；切实的','评价比 37% 的搜索负担更可行','The revised target seemed more reasonable.',['more reasonable than','a reasonable search strategy'],
 '若有 1,000 个潜在对象，你需要仔细考察 30 个，再选接下来比前 30 个中最佳者更好的人。这比 37% 规则合理多了。')

add(6,'作者意图','Why does the author ask about twelve serious relationships?',
 ['To report that twelve relationships guarantee a successful marriage.','To show that apartments and partners have identical search costs.','To question whether a simpler heuristic can still be difficult in practice.','To claim that Todd and Miller require exactly twelve marriages.'],2,
 '作者为何追问怎样拥有十二段认真交往？',['报告十二段关系保证婚姻成功。','表明找房和择偶成本完全一样。','质疑较简单的经验规则在现实中仍可能很难。','称两研究者要求恰好十二次婚姻。'],
 ['A does a pretty good job 是启发式评价，不是保证。','B 两种寻找情境作例子，未比较成本相等。','C Though...easier...still pretty demanding 后的设问突出实践难度。','D serious relationships 是认真交往，既不是十二次婚姻，也不是精确必须十二。'],
 ['Though it is a lot easier than the 37 percent rule, the “take a dozen” heuristic is still pretty demanding.'],
 'heuristic','启发式方法；经验规则','简化搜索的参考方法，不是保证最优的定理','The team used a simple heuristic to narrow the list.',['a useful heuristic','the “take a dozen” heuristic'],
 '最终，Todd 和 Miller 认为，无论问题集合如何，“先考察一打”的经验规则在找到前 10% 选项方面表现相当不错。这意味着，下次找新伴侣或新公寓，最好至少考察一打再决定。尽管比 37% 规则容易得多，它仍很苛刻。人们怎么在结婚前拥有十二段认真的交往呢？')

add(7,'细节','How does Kepler’s search compare with the “take a dozen” heuristic?',
 ['His eleven candidates were close to the suggested dozen.','He considered twelve candidates every year.','He evaluated only two candidates over eleven years.','His search exactly matched twelve candidates in two months.'],0,
 'Kepler 的搜索与“考察一打”规则怎样比较？',['十一名候选接近建议的一打。','每年考察十二名。','十一年仅考察两名。','两个月恰好考察十二名。'],
 ['A eleven 与 dozen 接近，pretty close 明示并非精确相同。','B eleven...over two years 不支持每年十二。','C 颠倒了人数与时间。','D 人数与时间均不符。这里按书中历史叙事作比较，不是新实验。'],
 ['considering eleven candidates over two years—pretty close'],
 'thorough','周密的；细致的','形容两年考察十一名对象的做法','She made a thorough comparison before deciding.',['a thorough job','a thorough search'],
 'Kepler 两年间考察了十一名候选，做得相当周密——已经很接近 Todd 和 Miller 的“考察一打”经验规则。')

add(8,'主旨','What question organizes this short passage?',
 ['How to calculate a new exact search percentage.','Whether all decisions have already been experimentally solved.','Why rejection never affects real choices.','What besides cost and possible rejection may explain limited exploration.'],3,
 '本短段围绕什么问题？',['如何计算新的精确搜索比例。','是否所有决策都已被实验解决。','为何拒绝从不影响选择。','成本和拒绝风险之外，什么解释探索不足。'],
 ['A 没有新比例计算。','B If 是设问前提，不是全部问题已解决的结论。','C Aside from 承认已有这两因素，不是否认。','D why don’t we explore more 与 what else is key 概括中心，并连向心理丰富人生。'],
 ['Aside from search cost and rejection probability, what else is key?'],
 'Aside from','除了……之外','暂把已讨论的因素放一边，追问其他解释','Aside from time, access also affects exploration.',['aside from cost','aside from these factors'],
 '如果 Kepler 和上述统计学家已找出许多决策的最优解，我们为何不多探索？除了搜索成本与被拒概率，还有什么关键因素？它能告诉我们关于心理丰富人生的什么呢？')

add(9,'细节','What did Bossard examine in the marriage licenses?',
 ['How satisfied each couple was after fifty years.','Where each partner had lived when applying.','Whether online dating caused their marriage.','The number of rejected proposals per applicant.'],1,
 'Bossard 在结婚许可资料中考察什么？',['五十年后婚姻满意度。','双方提出申请时住在哪里。','网恋是否导致结婚。','每位申请者求婚被拒次数。'],
 ['A 未报告长期满意度追踪。','B examined where...at the time of application 明示住址与时点。','C 资料是 1931 年，当前片段也没网恋变量。','D 未记录求婚拒绝次数。5,000 是许可证数，不是每人的候选人数。'],
 ['obtained 5,000 marriage licenses submitted in Philadelphia and surrounding counties in 1931, and examined where the pairs had lived at the time of application.'],
 'licenses','许可证；执照','这里是结婚许可资料，提供配对和住址信息','The researcher examined historical marriage licenses.',['marriage licenses','submit a license application'],
 '答案也许在社会学和社会心理学中。宾夕法尼亚大学社会学家 James Bossard 获得 1931 年费城及周边各县提交的 5,000 份结婚许可，考察双方申请时的住址。为了解费城婚姻的地理分布，他想看人们决定结婚前相隔多远。如果单身男女广泛探索，许多人就会与住得很远的人结婚。')

add(10,'细节','Which numerical statement accurately describes the findings?',
 ['82.2 percent had lived together before marriage.','17.8 percent had both lived outside Philadelphia.','Over half had lived within twenty blocks of each other.','33.58 percent had lived more than twenty blocks apart.'],2,
 '哪项数字描述符合结果？',['82.2% 婚前已同居。','17.8% 双方均住市外。','超过一半婚前相距不超过二十个街区。','33.58% 相距超过二十个街区。'],
 ['A lived separately 是各自居住，并非同居。','B 17.8% 是一方市内、一方市外。','C over half...within twenty blocks 直接支持。','D 33.58% 对应五个街区或更近，不是二十个以上。各百分比描述的范围不能混用。'],
 ['over half of the couples had lived within twenty blocks of each other before marriage'],
 'separately','分开地；各自地','双方都在费城，但婚前各自居住','The two researchers worked separately before comparing notes.',['live separately','separately in the same city'],
 '结果表明，1930 年代费城人在附近找到伴侣。只有 890 对，即 17.8%，婚前一方住费城、一方住市外。其余 82.2% 婚前各自住在费城。最著名的结果是，超过一半的夫妻婚前彼此住在二十个街区内，33.58% 相距五个街区或更近！')

add(11,'作者意图','What does Bossard’s comment about Cupid’s wings illustrate?',
 ['Partners often came from a restricted local area despite many possible candidates.','The study measured the actual flight distance of birds.','Most couples deliberately compared every candidate in the city.','The city offered very few potential partners in total.'],0,
 'Bossard 关于丘比特翅膀的评论说明什么？',['虽有众多潜在人选，伴侣常来自有限的邻近区域。','研究测量鸟的实际飞行距离。','多数夫妇刻意比较过全市每个候选。','全市潜在伴侣总数极少。'],
 ['A hundreds of thousands 与 only...close 对照，翅膀比喻概括局部配对。','B Cupid 是引述中的比喻，不是鸟类实验。','C appeared to consider only 并非核实每人所有考察行为，更不支持全市比较。','D 城市候选数恰被说成非常多。'],
 ['the majority of them appeared to consider only those who lived close to them.'],
 'eligible','符合条件的；适宜的','eligible bachelors and bachelorettes 指适婚单身男女','The event welcomed eligible applicants from nearby towns.',['eligible bachelors','eligible candidates'],
 '虽然费城这样的大城市中，适婚单身男女确有数十万潜在伴侣，多数人似乎只考虑住得近的人。否则，怎么会有多数配对出现在二十个街区内？Bossard 回顾结果时评论：“丘比特也许有翅膀，但显然不适合长途飞行。”')

add(12,'推断','Why should proximity in 1931 Philadelphia not be treated as an isolated explanation?',
 ['Residents had been randomly allocated to all neighborhoods.','Distance was measured only after marriage.','Shared backgrounds were explicitly ruled out.','Nearby residence could also reflect shared backgrounds and more opportunities to interact.'],3,
 '为何不能把 1931 年费城的近距离当成孤立解释？',['居民已被随机分配至所有街区。','只在结婚后量距离。','共同背景被明确排除。','住得近也可能反映共同背景和更多接触机会。'],
 ['A 原文描述族裔和种族隔离，而非随机分配。','B 此处解释近邻可能意味着什么，未改测量时点。','C shared...backgrounds 明确列为可能因素。','D many factors 后列两类机制，不能由观察直接断定纯距离因果。'],
 ['Living nearby could indicate many factors.','proximity also meant shared cultural, linguistic, and religious backgrounds'],
 'segregated','隔离的；分隔居住的','描述当时按族裔和种族形成的居住格局','The historical map showed a segregated city.',['ethnically segregated','racially segregated'],
 '住得近可能意味着许多因素。首先，1931 年费城存在族裔与种族隔离。因此，近距离也意味着共同的文化、语言、宗教背景，这在当时尤其重要。近距离还意味着，人们比起远处的人，更可能与附近的人发生接触。')

add(13,'同义改写','Which statement best restates this sentence?',
 ['Nearby residents inevitably became close friends.','People living close together were much more likely to become acquainted.','Distant residents were more likely to meet by chance.','Acquaintanceship determined everyone’s exact address.'],1,
 '哪项最准确改述此句？',['近邻必定成为密友。','住得近的人相识的可能性大得多。','远处居民更可能偶遇。','相识决定每个人的具体住址。'],
 ['A chance 是可能性，acquaintanceship 只是相识，不保证密友。','B dramatically higher 准确对应 much more likely。','C 把近与远的比较方向颠倒。','D 条件句谈近距离下相识概率，不是相识决定住址。'],
 ['the chance of acquaintanceship was dramatically higher if they lived close by.'],
 'acquaintanceship','相识；认识的关系','从不认识到彼此认识，不自动等于深厚友谊','Their acquaintanceship began with a brief conversation.',['the chance of acquaintanceship','develop an acquaintanceship'],
 '也就是说，如果彼此住得近，相识的可能性就大得多。')

add(14,'作者意图','Why does the author introduce the objection that the study was conducted in 1931?',
 ['To invite consideration of whether findings transfer across changing social conditions.','To announce that the original licenses were fabricated.','To show that cross-religious marriage was then the norm.','To establish that where people live has remained unchanged.'],0,
 '作者为何引入“那可是 1931 年”的异议？',['引导考虑社会条件改变后结果是否仍适用。','宣布原许可系伪造。','说明当时跨宗教婚姻是常态。','确立居住方式从未变化。'],
 ['A A lot has changed 后列居住、相识和婚配变化，提出时代适用性问题。','B 没质疑资料真实性。','C rarely married 恰表明罕见。','D changed 明示变化。作者引入可能反驳，不代表此处已判定邻近效应消失。'],
 ['A lot has changed, including where people live, how they meet, and whom they marry.'],
 'rarely','很少；罕有','修饰当时白人中跨宗教婚配的频率，不能改成绝不发生','They rarely met outside their neighborhood.',['rarely marry','rarely encounter'],
 '你也许会说，费城研究不错，但那是 1931 年。许多事情已经改变，包括住在哪里、怎样相识、与谁结婚。1931 年，与不同种族的人结婚几乎不可能。即使白人内部，不同宗教的人也很少通婚。')

add(15,'逻辑关系','What is the function of the question about the residential proximity effect?',
 ['It confirms that online dating has eliminated proximity.','It denies any increase in the apparent pool of partners.','It asks whether an apparent expansion of choice has made proximity outdated.','It measures the exact rate of growth in online users.'],2,
 '关于居住邻近效应的问句起什么作用？',['确认网恋已消除邻近影响。','否认潜在对象看来有所增加。','追问选择范围似乎扩大后，邻近影响是否已过时。','测量网民增长的精确速率。'],
 ['A 问句不是肯定结论。','B seems...grown 表示看来增长。','C Now...online dating 后提出过去效应是否仍在的研究问题。','D exponentially 在此为作者描述，没有具体增长率或测量。'],
 ['the number of potential mates seems to have exponentially grown. Is the residential proximity effect a thing of the past?'],
 'a thing of the past','已经过时或不复存在的事物','问旧有邻近影响是否仍然存在','The editor asked whether paper-only forms were a thing of the past.',['be a thing of the past','become a thing of the past'],
 '如今，随着在线约会平台普及，潜在伴侣数量似乎呈指数式增长。居住邻近效应是否已经成为过去？')

add(16,'细节','Who was specifically selected for the Dutch study?',
 ['289,248 newly married couples from all European countries.','Every Dutch citizen regardless of relationship status or year.','Only people who met through online dating platforms.','289,248 individuals who began cohabiting as domestic partners during 2004.'],3,
 '荷兰研究具体选取了谁？',['欧洲各国 289,248 对新婚夫妻。','不论关系和年份的每位荷兰公民。','只选在线平台认识的人。','2004 年开始以伴侣身份同居的 289,248 名个人。'],
 ['A individuals 不是 couples，且范围是荷兰。','B entire population 描述总体统计资料，More specifically 后有实际筛选条件。','C 没按认识平台筛选。','D 人数、身份与全年起止日期准确。不能把个人数当夫妻对数。'],
 ['they selected 289,248 individuals who started cohabitation as domestic partners between January 1, 2004, and December 31, 2004.'],
 'cohabitation','同居','以伴侣身份开始共同居住，不等于办理婚姻','The study recorded addresses before cohabitation.',['start cohabitation','prior to cohabitation'],
 'Karen Haandrikman 及同事提出了同一问题，查看荷兰全体人口的人口动态统计。没错，你没看错：荷兰全体人口。更具体说，他们选取 2004 年 1 月 1 日至 12 月 31 日开始以伴侣身份同居的 289,248 名个人。')

add(17,'逻辑关系','Why did researchers also examine addresses roughly five years earlier?',
 ['Some applicants might already have been living together when submitting their application.','Earlier addresses were guaranteed to reveal each person’s birthplace.','The application records contained no residential information.','All partners had separated exactly five years before applying.'],0,
 '为何还考察约五年前的住址？',['部分申请者提出申请时可能已经同居。','早期住址保证等于出生地。','申请记录完全没有住址信息。','所有伴侣都在申请前恰好五年分开。'],
 ['A Because...chance...already been living together 给出补充测量的理由。','B 五年前地址不等于出生地。','C First...looked at where...lived 表明有住址资料。','D 没有分手时间信息，roughly 也非精确五年。两套数据的最常见距离是众数，不能称所有人都隔一公里。'],
 ['there was a chance that those who submitted the cohabitation application as partners during 2004 had already been living together'],
 'prior to','在……之前','标记测量相对于开始同居的时间','They compared the records prior to publication.',['prior to cohabitation','five years prior to'],
 '首先，研究者查看每个人开始同居前住在哪里。因为 2004 年以伴侣身份提交同居申请的人可能已经住在一起，研究者也查看双方在开始同居大约五年前的居住距离。两套数据都表明，同居前双方最常见的居住距离只有一公里，即 0.62 英里。')

add(18,'细节','Which statement correctly interprets the reported distances?',
 ['One kilometer was the median distance at birth.','The median distance at birth was 22.9 kilometers.','Thirteen percent had lived one kilometer apart five years earlier.','Every couple had lived less than fifteen miles apart before cohabitation.'],1,
 '哪项正确理解所报距离？',['出生地距离中位数是一公里。','出生地之间距离中位数为 22.9 公里。','五年前相距一公里者占 13%。','每对伴侣同居前都相距不到十五英里。'],
 ['A 一公里是前文最常见距离，此处出生地中位数为 22.9 公里。','B 22.9...at birth 精确对应。','C 13% 是即将同居前，五年前约 10.5%。','D half 与出生地关系不能变成所有人同居前住址。中位数 6.2/7.8/22.9 需分别对应三个时点。'],
 ['The median distance was 6.2 kilometers (3.85 miles) right before cohabitation, 7.8 kilometers (4.85 miles) five years before, and 22.9 kilometers (14.23 miles) at birth.'],
 'median','中位数的','按大小排序处于中间位置的距离，不是平均数或最常见值','The median distance was lower than the mean.',['median distance','median value'],
 '新同居伴侣中，约 13% 在开始同居前相距约一公里；约 10.5% 在开始同居五年前相距约一公里。同居前即刻的距离中位数为 6.2 公里（3.85 英里），五年前为 7.8 公里（4.85 英里），出生时为 22.9 公里（14.23 英里）。也就是说，2004 年开始同居的荷兰人中，一半选择的伴侣，其出生地离自己的出生地不到十五英里。')

add(19,'推断','What does the comparison with Cupid in Philadelphia suggest?',
 ['Every Dutch partner in 2004 had met online.','The Internet had proved incapable of forming any relationship.','Geographical closeness still characterized partnerships in the Dutch data.','The two studies measured exactly the same distance percentages.'],2,
 '与费城丘比特的比较提示什么？',['2004 年所有荷兰伴侣都在网上认识。','互联网被证明不能形成任何关系。','荷兰数据中的伴侣配对仍有地理邻近特征。','两研究测得完全相同的距离百分比。'],
 ['A online dating became popular 是时代背景，不是每人的相识渠道。','B 未实验检验互联网能否形成关系。','C Yet...no different...not adapted for long flights 比喻邻近现象仍在。','D 比较的是共同趋势，不是统计量完全相等。这些数据不能单独识别网恋的因果效果。'],
 ['Yet Cupid in the Netherlands in 2004 was no different from Cupid in Philadelphia in 1931—not adapted for long flights.'],
 'cosmopolitan','国际化的；文化多元的','强调即便在这样的国家，配对地理范围仍出人意料地小','The city is known for its cosmopolitan population.',['a cosmopolitan country','a cosmopolitan city'],
 '这些统计提示，即使对一个相当国际化的欧洲国家，世界也小得惊人。在线约会在 2000 年代初流行起来。然而，2004 年荷兰的丘比特与 1931 年费城的并无不同——不适合长途飞行。这告诉我们什么？')

add(20,'逻辑关系','Why was the selection effect minimized in the MIT setting?',
 ['Unlike Philadelphia, the complexes lacked ethnic enclaves that attracted particular groups.','Researchers required all residents to choose the same three friends.','The study excluded every resident born outside the city.','Every resident was allowed to select a neighborhood by religion.'],0,
 'MIT 场景为何使选择效应减小？',['不同于费城，公寓群没有吸引特定群体的族裔聚居区。','研究者要求大家选同样三个朋友。','排除了所有外地出生居民。','每人可按宗教自选社区。'],
 ['A no ethnic enclaves 后 so 给出减小居住自选效应的原因。','B 选择朋友的提问不等于指定朋友。','C 没有这类排除标准。','D 按背景自选正是要尽量减小的效应。minimum 是尽量少，不等于所有混杂因素均被完全消除。'],
 ['there were no ethnic enclaves','the selection effect (i.e., a resident choosing to live in a particular area) was kept to a minimum.'],
 'enclaves','聚居区；飞地','ethnic enclaves 指特定族裔集中居住的区域','The historian studied ethnic enclaves in the port city.',['ethnic enclaves','live in an enclave'],
 '1940 年代末，社会心理学家 Leon Festinger、Stan Schachter 和 Kurt Back 考察 MIT 的 Westgate 与 Westgate West 两处住宅群中的友谊形成，也关注距离与关系。不同于费城，这里没有族裔聚居区，例如吸引中国移民聚居的唐人街，因此选择效应（居民选择住在某个特定区域）被尽量减小。')

add(21,'细节','What does the figure of 112 out of 187 refer to?',
 ['Participants who had exactly three next-door friends.','Residents who lived four or more units away from everyone.','Couples who had applied for marriage licenses.','Friendship nominations involving someone next door or directly linked by stairs.'],3,
 '112/187 这个数字指什么？',['恰有三个隔壁朋友的参与者。','与所有人都相隔四个单元以上的居民。','申请结婚许可的夫妇。','被提名朋友住隔壁或在楼梯直接连通单元的提名。'],
 ['A 分母为 friendship nominations，不是满足某条件的人数。','B 四单元或以上只有七次提名。','C 当前是友谊研究，非结婚许可。','D 112...187...60 percent 对应紧邻或楼梯直连。提名次数不能自动当独立居民数。'],
 ['112 out of the possible 187 friendship nominations, or 60 percent, lived next door or in the unit connected directly through staircases.'],
 'nominations','提名；被指名的对象记录','受访者说出常社交的朋友产生的记录，不是随机分配','The survey collected friendship nominations from residents.',['friendship nominations','make a nomination'],
 'Festinger 及同事确切知道参与者住在哪里，并问一个简单问题：“你在 Westgate 或 Westgate West 社交见得最多的三个人是谁？”在大学宿舍这个小世界里，结果重现了费城与荷兰的发现：187 个可能的友谊提名中，112 个，即 60%，住在隔壁或楼梯直接连通的单元。只有七次提名指向相隔四个单元或更远的人。所以，物理距离显然重要。')

add(22,'同义改写','What does functional distance help explain here?',
 ['Why floor numbers alone perfectly predict every friendship.','Why everyone near stairs becomes friends immediately.','Why convenient routes can increase informal encounters and friendship opportunities.','Why physical distance ceases to matter near staircases.'],2,
 '这里的功能距离帮助解释什么？',['仅靠楼层号码便能完美预测每段友谊。','为何楼梯旁的人马上全成朋友。','方便的动线为何增加非正式相遇与交友机会。','为何楼梯附近物理距离就无关紧要。'],
 ['A 文中比较相遇机会，没有确定性预测。','B more likely 是概率而非必然，且没有立即的时限。','C 楼梯位置影响跨楼层接触，反复偶遇提高形成友谊可能性。','D physical and functional 表明两者都相关。这里是研究结果和机制解释，不是此片段中的随机曝光实验。'],
 ['Those who lived close to the staircases were far more likely to become friends with someone living on a different floor','the more frequently one meets someone informally, the more likely it is that a friendship emerges.'],
 'functional distance','功能距离','受楼梯等通行动线影响的实际接触便利程度','A shared entrance can reduce functional distance between neighbors.',['physical and functional distance','reduce functional distance'],
 '研究另一个有趣发现是，功能距离也重要。住楼梯旁的人比离楼梯远的人，更可能与不同楼层的人交朋友。这提示，物理距离与功能距离决定偶遇概率；非正式见某人越频繁，越可能产生友谊。')

add(23,'作者意图','What is the purpose of the final question?',
 ['To move from the pattern of chance encounters to a question about its mechanism.','To deny that geography has any power in dormitories.','To claim all residents share identical religious beliefs.','To introduce a measured effect of online dating platforms.'],0,
 '末尾问题有什么作用？',['从偶遇与关系的模式转向追问机制。','否认地理在宿舍中的影响。','声称所有居民宗教信仰相同。','引入网恋平台的实测效果。'],
 ['A But why...matter 追问已描述现象为何发生，尚未在当前段给机制答案。','B surprising power 明确强调影响。','C randomized 不能改成背景完全相同；此处按作者概括保留，不冒充详尽随机试验方案。','D 当前无平台测量。'],
 ['Festinger’s findings point to the surprising power of geography and repeated chance meetings. But why do chance encounters matter?'],
 'encounters','相遇；接触','chance encounters 指非预先安排的偶遇','Repeated encounters made the neighbors familiar to each other.',['chance encounters','repeated encounters'],
 '在大学宿舍这一背景中，文化、族裔、宗教背景是随机分布的；Festinger 的发现指向地理位置和反复偶遇的惊人力量。但偶遇为什么重要？')

add(24,'逻辑关系','What research sequence does the author describe?',
 ['Observe a correlation and immediately declare it causal.','Identify a real-world association, then test possible causal mechanisms.','Reject all field observations before examining any variables.','Treat familiarity as identical to residential distance.'],1,
 '作者描述了怎样的研究顺序？',['观察相关后马上宣布因果。','先识别现实关联，再检验可能的因果机制。','考察变量前拒绝全部实地观察。','把熟悉感等同居住距离。'],
 ['A then test 表明相关之后还需检验，不能直接宣称因果。','B identifying...association...then test causal mechanisms 对应研究顺序。','C 现实观察是出发点而非被全盘拒绝。','D 重复相遇增加熟悉感，不是熟悉感等于米数。Zajonc 实验被引入，但本段未给完整实验条件。'],
 ['identifying an association between two variables in the real world','then test causal mechanisms, or what accounts for the observed correlation.'],
 'zeroed in on','集中研究；把注意力对准','表示 Zajonc 聚焦熟悉感效应','The investigator zeroed in on a possible mechanism.',['zero in on a mechanism','zero in on an effect'],
 '社会心理学家做得最好时，会先识别现实中两个变量的关联（例如居住邻近与友谊），再检验因果机制，也就是解释所观察相关的因素。反复偶遇会增加熟悉感。Bob Zajonc 是最杰出的社会心理学家之一，他通过一系列实验聚焦熟悉感效应，或他所称的“单纯曝光效应”。')

add(25,'细节','How was word desirability determined in the earlier work?',
 ['By counting printed occurrences without asking any speakers.','By measuring how long words took to pronounce.','By checking whether words came from Turkish.','By combining English speakers’ ratings of English words.'],3,
 '早期研究如何确定词语的讨喜程度？',['不问说话者，只数印刷出现次数。','测量发音所需时间。','检查词是否来自土耳其语。','汇总英语使用者对英语词语的评分。'],
 ['A 印刷出现次数测 word frequency，不是 desirability。','B 没用发音时长定义好坏感受。','C 当前片段未涉及土耳其语；不能把后续实验材料提前当此处方法。','D aggregating...ratings 直接给出操作定义。这里介绍既有测量和改进背景，尚不能由此断定词频导致喜欢。'],
 ['Desirability was determined by aggregating English speakers’ ratings of various English words.'],
 'aggregating','汇总；合并','将多个英语使用者评分合并，区别于统计词出现次数','The analyst summarized the results by aggregating individual ratings.',['aggregate ratings','aggregate individual responses'],
 '甚至在做这一系列实验之前，Zajonc 就对以往词频及其与词语“讨喜程度”（即一个词听起来多好或多不好）关系的研究作了巧妙改进。词频按每个词在 1920 与 1930 年代出版的书籍和杂志中出现的次数测量，这是 Edward Thorndike 与 Irving Lorge 细致辛劳的成果。讨喜程度则通过汇总英语使用者对各种英语词的评分确定。')

assert len(out)==25 and [q['id'] for q in out]==[t['questionId'] for t in targets]

def persist():
 path=ROOT/'source/short-questions/additional.json';existing=load('source/short-questions/additional.json');byid={q['id']:q for q in existing}
 for q in out:
  if q['id'] in byid:assert byid[q['id']]==q,('Refuse to overwrite changed authoring',q['id'])
  else:existing.append(q)
 path.write_text(json.dumps(existing,ensure_ascii=False,indent=2)+'\n',encoding='utf8',newline='\n')
 review=dict(batchId='batch-027',date='2026-10-23',pdfSha256=b['pdfSha256'],checkedPdfPages=list(range(106,112)),questionIds=[q['id'] for q in out],paragraphs=[dict(id=pid,textSha256=hashlib.sha256(pp[pid]['text'].encode()).hexdigest()) for pid in dict.fromkeys(q['paragraphId'] for q in out)],note='完整PDF106–111原页视觉核对及跨页拼接；CDC关联不作因果保证；100/1000候选、14%/3%与前10%目标分开。费城许可证、荷兰个人筛选与MIT友谊提名单位分开，众数/中位数与测量时点不混用；Cupid为比喻；宿舍随机背景按作者概括保留，不冒充完整随机试验方案。功能距离研究与后续曝光机制实验分开。末段完整审阅含未配题词频比较，未声称全书逐句证据覆盖。')
 (ROOT/'source/short-questions/review-chapter10-proximity25.json').write_text(json.dumps(review,ensure_ascii=False,indent=2)+'\n',encoding='utf8',newline='\n')
 print('Saved',len(out),'of 25 individually authored exercises')

if __name__=='__main__':persist()
