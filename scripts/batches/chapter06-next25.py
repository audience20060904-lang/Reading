"""25 individually authored exercises for frozen targets, PDF pages 54-57.
Preserve printed English, source positions and all previously published questions.
"""
from pathlib import Path
import json,hashlib
ROOT=Path(__file__).resolve().parents[2]
load=lambda p:json.loads((ROOT/p).read_text(encoding='utf8'))
b=load('public/data/book.json');plan=load('public/data/reading-plan.json');targets=load('source/short-questions/batch014-targets.json')['targets']
ss={s['id']:s for s in b['sentences']};pp={p['id']:p for p in b['paragraphs']};out=[]
def add(i,kind,prompt,options,answer,prompt_zh,options_zh,analyses,quotes,word,meaning,context,example,collocations,translation,support='explicit'):
 t=targets[i-1];u=next(u for u in plan['units'] if u['id']==t['readingUnitId']);group=[ss[sid] for sid in u['sentenceIds']];p=pp[u['paragraphId']];text=p['text'][group[0]['start']:group[-1]['end']]
 assert hashlib.sha256(text.encode()).hexdigest()==t['passageSha256'];evidence=[]
 for quote in quotes:
  offset=text.find(quote);assert offset>=0,(i,quote);start=group[0]['start']+offset;end=start+len(quote);touching=[s for s in group if s['start']<end and s['end']>start]
  evidence.append(dict(quote=quote,sentenceIds=[s['id'] for s in touching],sources=list({(r['pdfPage'],r['block']):r for s in touching for r in s['sources']}.values())))
 assert word.lower() in text.lower(),(i,word)
 out.append(dict(id=t['questionId'],version=1,readingUnitId=u['id'],chapterId=u['chapterId'],sectionId=u['sectionId'],paragraphId=u['paragraphId'],sentenceIds=u['sentenceIds'],passage=text,prompt=prompt,options=options,answer=answer,type=kind,promptZh=prompt_zh,optionsZh=options_zh,analyses=analyses,evidence=evidence,vocabulary=[dict(word=word,meaning=meaning,context=context,example=example,collocations=collocations)],translation=translation,support=support,editorialStatus='PDF 第 54–57 页逐题核对；固定连续原句；保留讣告评分范围、原书数字和条件语气；区分词条与独立特质；不暗改数值不一致'))

add(1,'细节','What threshold did the study use to classify a life in one of the three dimensions?',
 ['At least 3.67 out of 5, averaged across four items and the raters.','A perfect score on every item from every rater.','At least 3.67 people out of every five obituaries.','A score below 3.67 on a four-point scale.'],0,
 '研究用什么门槛把人生归入三个维度之一？',['评分者对四项指标给出的平均分至少为五分中的 3.67。','每位评分者的每一项都必须满分。','每五份讣告中至少有 3.67 个人。','四分量表中低于 3.67 分。'],
 ['A at least、out of 5、average 和 four items 均对应原句。','B 高门槛不等于每项每人全满分。','C 把平均评分错作人数比例。','D 分值方向和量表上限都错；此处是所选讣告的评分分类，不是人口普查。'],
 ['an average score of at least 3.67 out of 5 across four items.'],
 'criterion','标准；判据','指把评分归入分类的门槛，不是每个人真实内心的直接测量','The team applied the same criterion to every application.',['a classification criterion','meet a criterion'],
 '首先，这些被介绍的人中，有多少过着幸福、有意义或心理丰富的生活？要归入其中一类，三位评分者需在四项指标上给出五分中至少 3.67 的平均分。这是相当高的门槛。依此标准，当月《纽约时报》刊登的 101 份讣告中，十五人的生活被归为心理丰富。')

add(2,'细节','Which counts does the passage report for happy and meaningful lives?',
 ['Fifteen happy lives and thirty-two meaningful lives.','Thirty-two happy lives and another thirty-two meaningful lives.','Sixty-four people whose lives met exactly one category.','Thirty-two happy lives and no meaningful lives.'],1,
 '片段报告幸福与有意义生活的人数各是多少？',['幸福十五人，有意义三十二人。','幸福三十二人，有意义另有三十二人。','六十四人且每人恰好只属于一类。','幸福三十二人，没有有意义的人。'],
 ['A 幸福人数在本句明确是 thirty-two。','B 两处 thirty-two 对应两个维度。','C 不能把类别人数相加并假定互不重叠。','D meaningful 同样明确为三十二，不是零。'],
 ['thirty-two people led a happy life, and another thirty-two people led a meaningful life'],
 'in contrast','相比之下；形成对比地','引出幸福、意义人数与前文丰富人数的比较，不表示类别互斥','In contrast, the second group preferred quiet rooms.',['in contrast to','in contrast with'],
 '相比之下，三十二人过着幸福生活，另有三十二人过着有意义生活（见图 1）。总体而言，幸福或有意义生活的人，比心理丰富生活的人更多。')

add(3,'细节','Who are named as meeting all three dimensions?',
 ['Nicholas Clinch alone.','All ten people in the rich-and-meaningful overlap.','Nicholas Clinch and Simon Ramo.','The three people in the rich-and-happy overlap only.'],2,
 '哪些人被点名为三个维度都达到的人？',['只有 Nicholas Clinch。','丰富与有意义交集中全部十人。','Nicholas Clinch 与 Simon Ramo。','只有丰富与幸福交集中的三人。'],
 ['A 原文 two，且列出两人。','B 两维交集不等于三维交集，不能把十人全算进来。','C There were two who did it all 后的两个人名直接对应。','D 三人的两维交集也不能代替三维的两人。'],
 ['There were two who did it all: Nicholas Clinch','and Simon Ramo (engineer, inventor, and author).'],
 'Venn diagram','维恩图；集合交叠图','用重叠显示类别交集，不能将不同交集人数当互斥组直接相加','A Venn diagram can show which characteristics overlap.',['draw a Venn diagram','the overlap in a Venn diagram'],
 '我们还考察，有多少人同时幸福、有意义、又心理丰富。有两人三个维度都具备：Nicholas Clinch（律师、登山家、曾任 Sierra Club 执行主管）和 Simon Ramo（工程师、发明家、作者）。如维恩图所示，十人既丰富又有意义，八人既幸福又有意义，三人既丰富又幸福。')

add(4,'推断','Why should the rating of forty-one people be interpreted cautiously?',
 ['The study confirmed that none of them had any relevant experience.','The raters were forbidden to read about their lives.','A rating automatically captures every unreported private experience.','The obituaries may have omitted events relevant to the classifications.'],3,
 '为什么应谨慎理解四十一人的评分结果？',['研究确认他们都没有任何相关经历。','评分者被禁止阅读人生材料。','评分自动涵盖所有未记载的私人经历。','讣告可能省略了与分类有关的事件。'],
 ['A might have failed to describe 表示材料可能不全，非人生确实没有。','B 本句没有禁读材料的说明。','C 未记录经历不能被评分自动补全。','D 括号里的保留直接指出信息缺漏的可能。'],
 ['their obituaries might have failed to describe relevant events'],
 'relevant','相关的；切题的','指对幸福、意义或丰富评级有用、却可能没写进讣告的事件','The reviewer asked for details relevant to the decision.',['relevant events','relevant to a classification'],
 '遗憾的是，四十一位研究对象被评为既不幸福、也无意义、也不心理丰富（当然，他们的讣告也许没有写出相关事件）。','inference')

add(5,'逻辑关系','Why did the researchers turn to The Daily Progress?',
 ['To examine local obituaries after recognising that New York Times profiles were not representative.','To prove that all local newspapers provide perfectly random samples.','To reuse the same three assistants and the same 101 articles without change.','To replace all rating criteria with the subjects’ financial assets.'],0,
 '研究者为什么转向 The Daily Progress？',['认识到《纽约时报》人物不具代表性后，进一步考察地方讣告。','证明所有地方报纸都提供完美随机样本。','原样重复同三名助理和同 101 篇文章。','把全部评分标准改为财产。'],
 ['A not representative 后接 So, next，明确说明后续材料选择的理由。','B 换地方报纸不自动保证随机或无偏代表性。','C three other assistants、116 和地方报纸均是不同材料配置。','D 没有财产替代评分标准的说明。'],
 ['their lives are not representative of the general population. So, next, we hired three other research assistants to code 116 obituaries found in The Daily Progress'],
 'representative','有代表性的','在此指能否代表一般人口，不能把名人样本直接推广到所有人','The small group was not representative of the whole town.',['representative of a population','a representative sample'],
 '话虽如此，《纽约时报》讣告往往报道 Muhammad Ali 那样的非凡人物，其生活显然不代表一般人口。因此，我们另外聘请三名助理，编码弗吉尼亚州 Charlottesville 地方报纸 The Daily Progress 在 2016 年六月、七月、八月的 116 份讣告。分析前同样确认评分可靠。')

add(6,'细节','Under the stated criterion, how many local obituaries qualified as psychologically rich?',
 ['Five of 101, with a threshold below 3.67.','Five of 116, or 4.3 percent, using the same threshold.','116 of five, using a newly invented scale.','All 116, provided they described travel.'],1,
 '按所述标准，多少份地方讣告达到心理丰富分类？',['101 中五份，门槛低于 3.67。','116 中五份，即 4.3%，使用相同门槛。','五份中的 116 份，使用新量表。','全部 116 份，只要提到旅行。'],
 ['A 分母应为 116，且门槛是 3.67 或以上。','B only five out of 116 和 same criterion 直接对应。','C 数量关系和“新量表”都不符。','D 并非全体，也未规定只要提旅行就达到。'],
 ['only five out of 116 (4.3 percent) qualified.'],
 'qualified','符合标准；达到资格','这里指达到特定评分门槛，不是证明其他人生活毫无价值','Only projects that met the criteria qualified for review.',['qualify under a criterion','qualify for a category'],
 '这些弗吉尼亚人中，有多少被认为过着心理丰富的生活？使用相同标准——一至五分量表平均 3.67 或以上——116 人中仅五人（4.3%）达标。The Daily Progress 的人物真的更不可能过心理丰富生活吗？也许他们的生活确实比《纽约时报》所写的见多识广者少些冒险。')

add(7,'细节','What alternative explanation is offered for lower richness ratings?',
 ['The local articles necessarily covered longer and more detailed lives.','All local subjects refused to disclose whether they were happy.','Shorter local obituaries may leave out interesting details.','Local raters were instructed to assign everyone the same score.'],2,
 '对较低的丰富评级，片段提出了什么替代解释？',['地方文章必然更长、更详细。','所有地方人物拒绝说明幸福。','较短的地方讣告可能省略有趣细节。','地方评分者被要求给所有人同分。'],
 ['A 原文是 shorter，不是更长。','B 没有所有人拒绝披露的说明，材料也不是直接采访自报。','C An alternative explanation 后明确是篇幅短、潜在细节遗漏。','D 没有统一固定分数的指令。'],
 ['the obituaries in The Daily Progress are shorter than those in The New York Times, leaving out potentially interesting details.'],
 'noteworthy','值得注意的','引出另外两个维度的评级情况，不等于已证明解释机制','The difference in response rates is noteworthy.',['it is noteworthy that','a noteworthy finding'],
 '另一种解释是，The Daily Progress 的讣告比《纽约时报》的短，省掉了可能有趣的细节。另一方面，值得注意的是，六十六人（56.9%）被评为生活幸福；同样，九十六人（82.8%）被评为生活有意义。')

add(8,'细节','How is Henry Saint Dahl described in this sentence?',
 ['As one of many people who failed all three categories.','As the researcher who designed the rating scale.','As the only person anywhere in the world with all three dimensions.','As the one person in this reported group rated as having all three dimensions.'],3,
 '这句话怎样描述 Henry Saint Dahl？',['未达到任何类别的许多人之一。','设计量表的研究者。','全世界唯一同时拥有三个维度的人。','所报告组中唯一被评为三个维度兼具的人。'],
 ['A happy, meaningful, AND psychologically rich 与未达到相反。','B 括号是人物生平，不是研究者身份。','C one person 的范围是当前报告样本，不是全世界。','D 保留 one、rated 和三个维度的限定。'],
 ['There was one person rated to have led a happy, meaningful, AND psychologically rich life: Henry Saint Dahl'],
 'native','某地出生者；本地人','Buenos Aires native 说明出生或籍贯背景，不是评分标准','A Lisbon native, she later moved to the countryside.',['a Buenos Aires native','a native of a city'],
 '有一人被评为同时幸福、有意义、且心理丰富：Henry Saint Dahl（生于 Buenos Aires，曾任 Inter-American Bar Association 秘书长，并编写西班牙语和法语法律词典）。')

add(9,'细节','What material did the researchers add to look beyond mainly American profiles?',
 ['111 obituaries from Singapore’s The Straits Times, coded by two other assistants.','116 New York Times profiles, coded by the same original team.','A nationwide random survey of every Singaporean household.','Forty newspaper titles from the United States.'],0,
 '为超出主要为美国人的人物材料，研究者增加了什么？',['新加坡《海峡时报》的 111 份讣告，由另外两名助理编码。','同一原团队编码的 116 份《纽约时报》人物材料。','对所有新加坡家庭的全国随机调查。','美国的四十种报纸。'],
 ['A two other assistants、111 obituaries 和 The Straits Times 对应原书印文。','B 报纸、数量和人员配置均错配。','C 仍是讣告编码，不是全国随机住户调查。','D Forty 是本段报出的丰富评级人数，不是报纸种数。'],
 ['two other research assistants code 111 obituaries in The Straits Times, a Singaporean newspaper.'],
 'mainly','主要地；大体上','说明前两份报纸的人物主要来自美国，不能改为全部美国人或全体人口','The collection consists mainly of local accounts.',['mainly feature','mainly consist of'],
 '这些发现虽有趣，但《纽约时报》和 The Daily Progress 主要报道美国人。我们想知道，美国之外的人是否过得更心理丰富。于是另外两名研究助理编码新加坡《海峡时报》的 111 份讣告。多少人被评为心理丰富？四十人！此处人数按原页保留。')

add(10,'细节','Which figure does this excerpt report as having all three dimensions?',
 ['Twenty-five people, all of whom were rated only happy.','Eight people, reported here as 6.9 percent.','Sixty-five people, reported here as 56.5 percent.','Every person included in the Straits Times profiles.'],1,
 '本片段报告多少人同时拥有三个维度？',['二十五人，他们都只被评为幸福。','八人，本文印为 6.9%。','六十五人，本文印为 56.5%。','《海峡时报》人物全部如此。'],
 ['A twenty-five 对应幸福人数，不是三维同时达到；也不能从幸福人数推断“只幸福”。','B Eight individuals 后接 have it all，人数与本段所印百分比均对应。','C sixty-five 对应 meaningful，不是三维交集。','D Eight 不是全体。原书前片段印 111 份、40 人，本片段却印 34.5%；40/111 约 36.0%，数值不一致。所有英文保留印文，本题只定位原句，不要求据此计算分母。'],
 ['Eight individuals (6.9 percent) were deemed to have it all: happy, meaningful, AND psychologically rich'],
 'deemed','被认为；被评定为','强调依据所述材料作出的评级，不等于直接读取人物内心','The proposal was deemed suitable after review.',['be deemed to have','be deemed suitable'],
 '也就是说，《海峡时报》讣告中 34.5% 的人物被评为心理丰富，远高于前两份报纸。同时，二十五人（21.6%）被评为幸福，六十五人（56.5%）被评为有意义。八人（6.9%）被认为三者兼具，包括建筑师 I. M. Pei 和妇科医生兼牧师 Tow Siang Hwa。注：此处百分比与前片段的“111 份、40 人”不能一致换算；按原页保留，不自行改数字或推定分母。')

add(11,'推断','What conclusion is actually stated in this sentence?',
 ['Everyone in the general population has a psychologically rich life.','The sentence supplies a p-value establishing statistical significance.','A substantial number of people lead psychologically rich lives.','Psychological richness is the only good form of life.'],2,
 '这句话实际作了什么结论？',['一般人口每个人都心理丰富。','句中提供 p 值证明统计显著。','相当数量的人过着心理丰富生活。','心理丰富是唯一好的生活形式。'],
 ['A a significant number 不是 everyone。','B 本句没给统计检验或 p 值，不能仅凭 significant 判断统计意义。','C 按普通语义保留“相当数量”，不扩大为全体或多数。','D 句子没有排除其他美好生活形式。'],
 ['a significant number of people lead a psychologically rich life.'],
 'significant','相当的；值得注意的','在 a significant number 中指数量可观，本句没有单独给统计显著性检验','A significant number of visitors returned for a second session.',['a significant number of','a significant amount of'],
 '我们的研究表明，相当数量的人过着心理丰富的生活。','inference')

add(12,'逻辑关系','What follows from the relative independence described by the author?',
 ['The three dimensions can never appear together.','A fictional example becomes an actual obituary participant.','Low happiness guarantees high richness in every life.','Psychological richness can occur without high happiness or meaning.'],3,
 '按作者所述，相对独立性支持什么？',['三个维度永不能并存。','小说例子因此成为实际讣告研究对象。','低幸福保证每种人生都高丰富。','心理丰富可以在没有幸福或意义时存在。'],
 ['A independence 不等于绝对互斥。','B Goldmund 是文学类比；probably rated 是推测，非研究中真实评分者。','C possible 不能改成所有人的必然保证。','D 最后一句明确说 it is possible...without happiness or meaning。'],
 ['The relative independence of the three forms of a good life evident in the obituary studies shows that it is possible to lead a psychologically rich life without happiness or meaning.'],
 'relative independence','相对独立性','指几个维度可区分、并非必须一起高，不表示彼此完全无关联','The analysis considered the relative independence of the two measures.',['relative independence of dimensions','relative independence from'],
 '这让我们回到大问题：没有幸福或意义，也能过美好生活吗？例如，Goldmund 的生活大概会被评为幸福与意义较低、心理丰富较高。讣告研究所见三种美好生活的相对独立性，表明没有幸福或意义，也可能过心理丰富的生活。')

add(13,'细节','What is the denominator for the four people mentioned here?',
 ['The fifteen New York Times individuals rated psychologically rich.','All obituaries ever published by the newspaper.','Four newspaper raters.','The entire population of New York City.'],0,
 '这里提到四人时，所对应的范围是什么？',['《纽约时报》中被评为心理丰富的十五人。','该报历史上所有讣告。','四名报纸评分者。','纽约市全部居民。'],
 ['A out of the fifteen individuals 明确限定这四人来自哪一组。','B 本句不是全部历史讣告。','C 四是人物数，不是评分者数。','D 讣告样本不能换成全市人口。'],
 ['out of the fifteen individuals who were rated to have led a psychologically rich life in the New York Times obituaries, we found four'],
 'out of','在……之中；从……范围内','在此限定子集与母组，不能把四人当整个人口比例','Out of the twenty applications, five met the requirements.',['four out of fifteen','out of the group'],
 '确实，《纽约时报》讣告中被评为心理丰富的十五人里，有四人过着心理丰富、但没有幸福或意义的生活。')

add(14,'作者意图','How is Steve Jobs used in this passage?',
 ['As a participant whose happiness was directly measured in this paragraph.','As a real-life illustration of an adventurous, learning-filled life that might not have been happy.','As proof that every inventor is unhappy.','As evidence that alienating others guarantees psychological richness.'],1,
 '这段怎样使用 Steve Jobs 的例子？',['作为本段直接测量了幸福的研究参与者。','作为充满冒险和学习、却未必幸福的真实人生例子。','证明所有发明家都不幸福。','证明疏远他人保证心理丰富。'],
 ['A 文中说 real-life example 和 might，未说这里直接测量他，也不能据此把他列入当月讣告样本。','B 保留例证身份、might not 与 adventures and learning。','C 个案不能推广为每位发明家。','D angry、alienated 是描述，不是产生丰富的充分因果。'],
 ['He might not have led a happy life, but it was an interesting one, full of adventures and learning.'],
 'alienated','使疏远；使产生隔阂','描述与周围人的关系，不应改写为获得丰富生活的建议','His dismissive remarks alienated several colleagues.',['alienate people','alienate those around someone'],
 '此外，我们在《纽约时报》讣告中找出八位被评为既丰富又有意义的人。Steve Jobs 是现实中的一个例子。他常生气，也疏远了周围许多人。他也许没过幸福生活，却过着有趣、充满冒险和学习的生活。这里的人物例证不等于将他认定为该月讣告样本中的一员。')

add(15,'推断','How should the rating pattern in this sentence be understood?',
 ['As a published set of numerical scores given by every rater.','As proof that the person had no meaningful experiences.','As a hypothetical assessment: low happiness, high meaning and richness.','As an assurance that all three dimensions were equally high.'],2,
 '应怎样理解本句的评级模式？',['每位评分者公布的一组数值。','证明此人没有有意义经历。','假设性的评价：幸福较低，意义与丰富较高。','保证三个维度同样高。'],
 ['A would have been rated 不是列出已公布实测分数。','B high in meaning 与此相反。','C 条件式评级语气与三个维度高低准确对应。','D low in happiness 不能被删去。'],
 ['would have been rated low in happiness but high in meaning and psychological richness.'],
 'would have been rated','本会被评为；若评分将被评为','是条件性、推测性表述，不能悄悄改成已实测','Under that rule, the entry would have been rated highly.',['would have been rated low','would have been rated highly'],
 '他的人生本会被评为幸福较低，但意义与心理丰富较高。','inference')

add(16,'作者意图','Why are Alison Gopnik and Linda mentioned?',
 ['To show that exploration must exclude meaning.','To replace research with a claim that every life is identical.','To establish that financial wealth is necessary for richness.','To illustrate that richness can coexist with happiness and meaning.'],3,
 '为什么提到 Alison Gopnik 与 Linda？',['说明探索必须排除意义。','用所有人生相同的主张取代研究。','确立财富是丰富的必要条件。','说明丰富可以与幸福和意义并存。'],
 ['A as well as 明确是兼具，不是排除。','B some people 与所有人相同不符。','C 本段没有财富必要条件。','D 两个例子紧接“有些人确实三者兼具”，用于说明共存可能。'],
 ['some people do lead a psychologically rich as well as a happy and meaningful life.','Alison Gopnik’s post–midlife crisis life is just that. So is the life of Linda, the taxi driver.'],
 'distinct','不同的；可区分的','distinct kind 指可作为单独维度讨论，不表示只能二选一','The two approaches are distinct but can be combined.',['a distinct kind of','distinct from'],
 '同样重要的是，有些人确实既心理丰富，又幸福、有意义。Alison Gopnik 中年危机之后的人生如此，出租车司机 Linda 也是。总之，我们的研究支持：探索生活是一种可区分的美好生活，即心理丰富的生活。')

add(17,'逻辑关系','What does “possible” establish about the dimensions?',
 ['Two or three dimensions may coexist, without guaranteeing this for everyone.','Every good life must score equally on all three.','No life can contain more than one dimension.','Exactly two dimensions are required and three are forbidden.'],0,
 'possible 对这些维度说明什么？',['两种或三种维度可以共存，但不保证所有人如此。','每种美好生活都必须三项同分。','任何人生最多只能有一种。','必须恰好两种，禁止三种。'],
 ['A possible 说明存在可能，two or three 明确可以兼具。','B 可能性不是所有人必须达到的要求。','C 与 two or three 相反。','D or three 明确保留三种。'],
 ['it is possible to have two or three of these dimensions of a good life.'],
 'dimensions','维度；方面','指美好生活的不同方面，能区分但不必互斥','The discussion considers several dimensions of the experience.',['dimensions of a good life','multiple dimensions'],
 '但它也表明，一个人可以同时拥有美好生活中的两种或三种维度。')

add(18,'作者意图','Why does the author introduce a short lecture on personality psychology?',
 ['To announce that personality differences have already been ruled out.','To prepare readers to examine whether personality distinguishes the different kinds of life.','To replace the book’s topic with a complete clinical diagnosis.','To claim that teaching experience proves all later hypotheses.'],1,
 '作者为什么引入简短的人格心理学讲解？',['宣布人格差异已被排除。','为考察人格能否区分不同生活方式提供基础。','把主题换成完整临床诊断。','声称授课经历证明所有后续假设。'],
 ['A 开头是在问 whether differentiate，不是已排除。','B To answer...need to know basics 直接解释基础讲解的用途。','C intro 和 five-minute 不是临床诊断。','D 以前教课说明讲解背景，不是研究假设真假的证明。'],
 ['To answer this question, we need to know the basics of personality psychology.'],
 'differentiate','区分；分辨差异','此处问人格特征能否区分几种生活，不代表已找到确定因果','The two examples help differentiate the concepts.',['differentiate between','differentiate one group from another'],
 '有没有人格特征，可以区分心理丰富生活者与幸福或有意义生活者？回答前，需要知道人格心理学的基础。我以前教过人格心理学导论，因此可以用五分钟讲解大五人格特质。')

add(19,'逻辑关系','Why were words for temporary states removed from the initial list?',
 ['The dictionary contained no words for personal behaviour.','Every temporary feeling was judged morally unacceptable.','The researchers were seeking characteristic patterns rather than temporary states.','All 400,000 entries were already pure personality traits.'],2,
 '为什么从初始名单移除描述暂时状态的词？',['词典没有任何描述个人行为的词。','每种暂时感受都被评为道德上不可接受。','研究者要找典型模式，而不是暂时状态。','全部四十万词条都已是纯人格特质。'],
 ['A 他们找到了 17,953 个个人描述词，非完全没有。','B 本段理由是定义与时间性质，不是道德评价。','C characteristic patterns 对比 temporary states，明确解释筛选。','D 四十万是词典总词条，不是最终特质数。'],
 ['Personality is often defined as characteristic patterns of thinking, feeling, and behavior, so the researchers removed all the words about temporary states'],
 'temporary','暂时的','与人格的典型思维、感受和行为模式对照，不把一时状态直接当稳定特征','The delay caused only a temporary change in the schedule.',['temporary states','a temporary condition'],
 '先说一点历史。1936 年，Gordon W. Allport 与 Henry S. Odbert 从 Webster 的 1925 年《新国际词典》中寻找描述人格或个人行为的全部词汇。该词典约四十万词条，其中有 17,953 个个人描述词，占记录词汇的 4.5%。人格通常定义为典型的思维、感受和行为模式，因此研究者删去 frantic、rejoicing 等描述暂时状态的词。')

add(20,'细节','Why did Allport and Odbert remove evaluative character terms?',
 ['To keep only explicitly moral praise.','To guarantee that all remaining words were equally familiar to everyone.','To eliminate every reference to behaviour.','To seek relatively neutral vocabulary and reduce bias in personality research.'],3,
 'Allport 与 Odbert 为什么移除评价品格的词？',['只保留明确的道德赞美。','保证剩余词汇每个人都同样熟悉。','消除一切行为描述。','寻找较中立的词汇，减少人格研究偏差。'],
 ['A judgment-free 与只留道德赞美相反。','B 本段没有保证词汇熟悉度相同。','C 目标仍是人格词汇，不是删去一切行为。','D neutral vocabulary to avoid biases 直接说明理由。'],
 ['they needed a judgment-free, relatively neutral vocabulary to avoid biases.'],
 'evaluative','评价性的；带价值判断的','指 excellent 等对人作褒贬的词，与相对中立描述区分','The reviewer separated descriptive statements from evaluative comments.',['evaluative terms','evaluative judgments'],
 'Allport 与 Odbert 也把人格与带道德评价的 character 区分。他们认为，要建立人格心理学的科学领域，需要不带判断、较中立的词汇以避免偏差。因此删去 excellent、acceptable、insignificant 等品格评价词。最终得到 4,504 个英语“纯”人格特质词。')

add(21,'推断','Which qualification should accompany the number 4,504?',
 ['It refers to dictionary-based ways of describing personality, not necessarily that many independent traits.','It counts all people who participated in a personality experiment.','It proves that no two listed words can be synonyms.','It represents the complete vocabulary of every language.'],0,
 '理解 4,504 这个数时，应保留什么限定？',['它是基于词典的人格描述方式数，不必然等于独立特质数。','它计算参加人格实验的全部人数。','它证明名单中的任何两词都不可能同义。','它代表每种语言的全部词汇。'],
 ['A based on the dictionary treatment 限定来源；ways to describe 不能自动等同独立维度。','B 这是描述词数量，不是受试者人数。','C 本句没有作无同义词的证明。','D someone’s personality 和特定 dictionary treatment 均非所有语言词汇总量。'],
 ['4,504 different ways to describe someone’s personality, based on the dictionary treatment.'],
 'based on','基于；以……为依据','限定这项描述数量来自词典处理，而非自然界独立特质的最终清单','The summary is based on the archived interviews.',['based on evidence','based on a dictionary'],
 '换句话说，按照这套词典处理方式，他们发现了 4,504 种描述一个人人格的方式。','inference')

add(22,'观点归属','What reasoning do Allport and Odbert give for studying trait words?',
 ['Repeated words cause the same personality in every speaker.','A trait’s lasting name in language is taken as evidence of a corresponding human pattern.','Only negative labels can describe personality.','Language contains no useful information about behaviour.'],1,
 'Allport 与 Odbert 为什么认为特质词值得研究？',['重复一个词会让每位说话者人格相同。','语言中长久存在的特质名称，被视为对应人类模式的依据。','只有负面标签能描述人格。','语言不含任何有关行为的有用信息。'],
 ['A 论证方向从人类模式到词的存在，不是词造成所有人同质。','B 引语中的 permanent place 与 name them 支持他们的词汇论证。','C egotistic 等只是例子，未说只可用负面词。','D 正是在为词汇作为线索辩护，不是否定其用处；这仍是他们的论证。'],
 ['If traits exist at all it is natural and proper to name them.','If there is a trait name, there must be some corresponding pattern of behavior, thinking, or feeling.'],
 'corresponding','相对应的','指词名与某种行为、思维或感受模式的关系，不表示每个词必是独立特质','Each symbol has a corresponding explanation in the guide.',['a corresponding pattern','corresponding to a label'],
 '但为什么靠词语说明内在品质？Allport 与 Odbert 认为：“如果许多人实际上并不自我中心、好斗或胆怯，这些称谓就不会在语言中占有永久位置。只要特质存在，给它们命名便自然且恰当。”如果有一个特质名称，就一定有相对应的行为、思维或感受模式。')

add(23,'逻辑关系','What problem do “adventurous” and “venturous” illustrate?',
 ['The list had excluded every word about adventure.','The words were both counts of participants.','Different words can overlap in meaning instead of representing distinct traits.','The research contained too few words to describe anybody.'],2,
 'adventurous 与 venturous 说明什么问题？',['名单排除了所有冒险相关词。','两个词都是参与者数量。','不同词可能同义重叠，而非各代表独立特质。','研究的词太少，无法描述任何人。'],
 ['A 名单明确 included both，非全排除。','B 两者是人格描述词，不是人数。','C too many synonyms 与 Not really 回应是否两种独立特质。','D 批评是同义词过多，不是词太少。'],
 ['claiming there were too many synonyms.','Are they two separate personality traits? (Not really.)'],
 'synonyms','同义词','强调不同词形可能表达近似内容，不应简单把词数当独立特质数','The editor replaced repeated terms with suitable synonyms.',['near synonyms','a list of synonyms'],
 '有人批评 Allport 与 Odbert 的研究，认为同义词太多。例如，“纯”人格词名单同时包括 adventurous 与 venturous。这真是两种独立人格特质吗？（并不真是。）')

add(24,'主旨','Which two vocabulary concerns are raised here?',
 ['There are no old words, and every person knows exactly the same vocabulary.','All uncommon words are morally positive and therefore unusable.','The list contains only foreign-language words rather than English.','Some words are archaic, and esoteric vocabulary may be understood unevenly across people.'],3,
 '这里提出了哪两项词汇方面的担忧？',['没有古词，每个人词汇完全相同。','所有少见词都是道德褒义，所以不可用。','名单只有外语词，没有英语。','有些词过时，而且人们对晦涩词的理解程度可能不同。'],
 ['A archaic 与 large individual differences 都和这项相反。','B 这里关注常用程度与理解差异，不是道德褒义。','C 没有仅含外语词的指控。','D 两条批评分别对应过时少用和词汇个体差异。'],
 ['many of the words, like “aery” and “breme,” were archaic and most people didn’t use them.','there were large individual differences in vocabulary and that esoteric terms should be removed.'],
 'esoteric','晦涩的；少数人熟悉的','修饰可能应从测量词表移除的词，避免不同词汇掌握造成混淆','The manual avoids esoteric terminology where a simple word will do.',['esoteric terms','esoteric vocabulary'],
 '另一些人认为，aery、breme 等许多词已经过时，多数人不用。（这些词的确不太有用。）还有人说，个人词汇量差异很大，应删去晦涩词语。（大概如此。）')

add(25,'逻辑关系','What does “Despite all the criticisms” highlight?',
 ['The early effort remained influential as the lexical approach even though it was criticised.','Every criticism was disproved and the original list was left unchanged forever.','The lexical approach was abandoned immediately.','Personality research stopped using language in any form.'],0,
 'Despite all the criticisms 强调什么？',['尽管受批评，早期工作仍以词汇取向延续并保持影响。','所有批评均被推翻，原名单永远不变。','词汇取向立即被抛弃。','人格研究停止使用任何语言材料。'],
 ['A despite 引出让步，has survived 表明方法传统延续。','B 延续不等于每条批评无效，也不保证原始词表不变。','C 与 has survived 相反。','D lexical approach 本身就是从词汇研究人格的取向。'],
 ['Allport and Odbert’s early effort to catalog personality trait words has survived as the “lexical approach” to personality.'],
 'lexical approach','词汇取向；词汇研究法','通过人格描述词研究特质的取向，不是把每个词都当作独立维度','The seminar introduced the lexical approach to personality.',['the lexical approach to personality','a lexical approach'],
 '尽管遭到这些批评，Allport 与 Odbert 早期整理人格特质词的努力，仍以人格研究的“词汇取向”延续下来。')

assert len(out)==25 and [q['id'] for q in out]==[t['questionId'] for t in targets]

def persist():
 path=ROOT/'source/short-questions/additional.json';existing=load('source/short-questions/additional.json');byid={q['id']:q for q in existing}
 for q in out:
  if q['id'] in byid:assert byid[q['id']]==q,('Refuse to overwrite changed authoring',q['id'])
  else:existing.append(q)
 path.write_text(json.dumps(existing,ensure_ascii=False,indent=2)+'\n',encoding='utf8',newline='\n')
 review=dict(batchId='batch-014',date='2026-10-22',pdfSha256=b['pdfSha256'],checkedPdfPages=list(range(54,58)),questionIds=[q['id'] for q in out],paragraphs=[dict(id=pid,textSha256=hashlib.sha256(pp[pid]['text'].encode()).hexdigest()) for pid in dict.fromkeys(q['paragraphId'] for q in out)],note='完整 PDF 原页视觉复核，包括跨页引语；讣告评分、原书数字不一致、文学假设与人格词汇史分别说明，候选句界不冒充人工最终分句。')
 (ROOT/'source/short-questions/review-chapter06-next25.json').write_text(json.dumps(review,ensure_ascii=False,indent=2)+'\n',encoding='utf8',newline='\n')
 print('Saved',len(out),'of 25 individually authored exercises')

if __name__=='__main__':persist()
