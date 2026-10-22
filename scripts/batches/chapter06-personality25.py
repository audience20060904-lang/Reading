"""25 individually authored exercises for frozen targets, PDF pages 58-62.
Preserve printed English, source positions and all previously published questions.
"""
from pathlib import Path
import json,hashlib
ROOT=Path(__file__).resolve().parents[2]
load=lambda p:json.loads((ROOT/p).read_text(encoding='utf8'))
b=load('public/data/book.json');plan=load('public/data/reading-plan.json');targets=load('source/short-questions/batch015-targets.json')['targets']
ss={s['id']:s for s in b['sentences']};pp={p['id']:p for p in b['paragraphs']};out=[]
def add(i,kind,prompt,options,answer,prompt_zh,options_zh,analyses,quotes,word,meaning,context,example,collocations,translation,support='explicit'):
 t=targets[i-1];u=next(u for u in plan['units'] if u['id']==t['readingUnitId']);group=[ss[sid] for sid in u['sentenceIds']];p=pp[u['paragraphId']];text=p['text'][group[0]['start']:group[-1]['end']]
 assert hashlib.sha256(text.encode()).hexdigest()==t['passageSha256'];evidence=[]
 for quote in quotes:
  offset=text.find(quote);assert offset>=0,(i,quote);start=group[0]['start']+offset;end=start+len(quote);touching=[s for s in group if s['start']<end and s['end']>start]
  evidence.append(dict(quote=quote,sentenceIds=[s['id'] for s in touching],sources=list({(r['pdfPage'],r['block']):r for s in touching for r in s['sources']}.values())))
 assert word.lower() in text.lower(),(i,word)
 out.append(dict(id=t['questionId'],version=1,readingUnitId=u['id'],chapterId=u['chapterId'],sectionId=u['sectionId'],paragraphId=u['paragraphId'],sentenceIds=u['sentenceIds'],passage=text,prompt=prompt,options=options,answer=answer,type=kind,promptZh=prompt_zh,optionsZh=options_zh,analyses=analyses,evidence=evidence,vocabulary=[dict(word=word,meaning=meaning,context=context,example=example,collocations=collocations)],translation=translation,support=support,editorialStatus='PDF 第 58–62 页逐题原页核对；固定原句和已有单元边界；区分相关、自报、作者推论与个人叙事；保留概率语气及短语尾段'))


add(1,'细节','How did the psychologists organise the personality terms into broader factors?',
 ['They asked raters to choose the five most familiar words without statistical analysis.','They collected self-ratings and used factor analysis to group the terms.','They treated the 187 students as 187 independent personality factors.','They replaced all self-ratings with observations of the students’ parents.'],1,
 '心理学家怎样把人格词汇整理为更宽泛的因子？',['让评分者不经统计分析选出最熟悉的五个词。','收集自我评分，再用因素分析把词汇归组。','把 187 名学生视为 187 个独立人格因子。','把所有自评换成对学生父母的观察。'],
 ['A 原文明确用了 factor analysis，非仅凭熟悉度选择。','B rate themselves 后接 applied...factor analysis，顺序与方法均对应。','C 187 是示例研究的学生人数，不是因子数；1,710 才是其评分词条数。','D themselves 表示自评，没有父母观察这一程序。'],
 ['rate themselves using many of the original Allport-Odbert terms, then applied the statistical technique of factor analysis'],
 'factor analysis','因素分析','把许多词条的评分整理为较大组的统计方法，不是按人数命名人格类型','The researchers used factor analysis to examine how the ratings clustered.',['apply factor analysis','a statistical technique'],
 '后来，心理学家让大量参与者用原来 Allport–Odbert 词表中的许多词自我评分，再运用因素分析这种统计方法，把词汇整理为较大的组，即“因子”。例如，Lew Goldberg 让 187 名大学生就 1,710 个词自评：“你一般有多快活？一般有多内敛？一般有多残虐？”')

add(2,'语境词义','What does the expression “and so on” indicate?',
 ['The sequence has reached its final item.','The next item contradicts every earlier example.','Further similar items could be added.','The examples must be repeated in reverse order.'],2,
 'and so on 这个表达表示什么？',['这一列举已到最后一项。','下一项将反驳之前所有例子。','还可继续列出类似项目。','必须把例子倒过来重复。'],
 ['A 省略后续类似项目，不是宣告没有其他项目。','B 不含转折或反驳关系。','C 是“等等、诸如此类”的意思，提示列举未穷尽。','D 不涉及倒序。本单元按既有固定边界保留为短语尾段；它不是一个独立完整句，也不补写缺失主语或上下文。'],
 ['and so on.'],
 'and so on','等等；诸如此类','表示同类项目还可继续列举；此处仅保留原页的列表收尾短语','The pack contains pencils, rulers, erasers, and so on.',['and so on','and so forth'],
 '等等。')

add(3,'作者意图','What does the comparison with continents help explain?',
 ['Many personality-describing words are organised into a few broad factors.','Each personality trait belongs to a particular geographical continent.','The five factors correspond to five named countries.','Psychologists count only traits associated with large cities.'],0,
 '把人格因子比作大陆，有助于说明什么？',['大量人格描述词被整理为少数宽泛因子。','每种人格特质都属于某个地理大陆。','五个因子分别对应五个具名国家。','心理学家只统计与大城市有关的特质。'],
 ['A words 对应城镇，five factors 对应大陆，突出归类层级。','B 比喻不能改成真实地理归属。','C 原文五因子是外向、神经质、尽责、宜人和经验开放性，没有五国配对。','D countless words 表示广泛词汇，并非只筛城市有关的特质。'],
 ['By classifying all these words into five factors, personality psychologists essentially organized them into “continents” on the map.'],
 'cluster','聚集；归成群','人格描述词按关联形成较大的组，并非地理迁移','The responses cluster around three broad themes.',['cluster into groups','cluster around a theme'],
 'Goldberg 的研究及类似研究发现，许多人格特质可以整齐归入五个因子：外向性（如快活、健谈、合群、活跃），神经质（如易怒、胆怯、自我批评），尽责性（如坚持、整洁、可靠），宜人性（如慷慨、友善、信任他人），以及经验开放性（如爱好文学、有洞见、感知敏锐）。从某种意义说，人格心理学家创造了一张地图。像世界各地的城镇一样，描述人格的词数不胜数。把这些词归为五个因子，就相当于把它们整理为地图上的“大陆”。')

add(4,'细节','When does the author locate the Big Five’s particularly influential discovery?',
 ['In 1936 and the early 1940s.','Throughout the entire nineteenth century.','Only after the early 2000s.','In the 1980s and early 1990s.'],3,
 '作者把大五人格这一特别有影响的发现定位于何时？',['1936 年及 1940 年代初。','整个十九世纪。','仅在 2000 年代初以后。','1980 年代及 1990 年代初。'],
 ['A 本句给出的不是早期词表整理年份。','B 与明确的年代不符。','C 将时间推后，且 only 没有依据。','D 直接对应 in the 1980s and early 1990s；这是作者对当时影响力的评价。'],
 ['the most influential discovery in personality psychology in the 1980s and early 1990s.'],
 'influential','有影响力的','形容这项发现在人格心理学中的影响，不表示它解释所有人格差异','The paper became influential in later discussions.',['an influential discovery','highly influential'],
 '这些因子被称为“大五人格”，是 1980 年代和 1990 年代初人格心理学中最有影响力的发现。')

add(5,'主旨','What research question do the examples of wrestling and studying abroad introduce?',
 ['Whether all activities appeal equally to every personality.','Whether studying abroad eliminates differences between people.','Which personality factors are associated with a psychologically rich life.','Which sporting activity guarantees a psychologically rich life.'],2,
 '摔角观赛和留学的例子引出了什么研究问题？',['所有活动是否对每种人格同样有吸引力。','留学是否消除了人与人的差异。','哪些人格因子与心理丰富的人生相关。','哪项体育活动能保证心理丰富的人生。'],
 ['A 开头恰恰提出不同人可能选择不同活动。','B 没有消除差异这一问题。','C 后两句直接从活动差异转向人格特质及大五因子的关联。','D associated with 不是保证；摔角仅用于引出差异，并非推荐的必然方法。'],
 ['which of the Big Five factors are associated with a psychologically rich life?'],
 'associated with','与……相关联','提出人格因子和丰富人生是否相关的研究问题，不等同确定因果','The survey asked which habits were associated with satisfaction.',['be associated with','closely associated with'],
 '周末去看职业摔角赛的人，可能与回避此类活动的人很不同。留学的人，也可能与不留学的人很不同。心理丰富的人是否具有独特的人格特质？如果有，哪些大五人格因子与心理丰富的人生相关？')

add(6,'细节','Which description matches the data collection reported here?',
 ['Exactly 5,000 people in one sample from the United States.','More than 5,000 respondents in seven samples across three countries.','Seven respondents in more than 5,000 separate samples.','More than 5,000 respondents drawn only from Korea and India.'],1,
 '哪项符合本句所报告的数据收集范围？',['美国一个样本中恰好 5,000 人。','三个国家的七个样本，共逾 5,000 名受访者。','逾 5,000 个独立样本中共七名受访者。','逾 5,000 名受访者全部只来自韩国和印度。'],
 ['A over 不是恰好，seven separate samples 不是一个。','B 人数、样本数及美国、韩国、印度三个国家均对应。','C 颠倒人数与样本数。','D 漏掉美国。本句没有说明随机抽样或对三个国家总体的代表性。'],
 ['over 5,000 respondents in seven separate samples across the U.S., Korea, and India.'],
 'respondents','受访者；作答者','提供调查数据的人，不是样本组的数量','Respondents could skip questions they did not wish to answer.',['survey respondents','collect data from respondents'],
 '为了回答这些问题，我们从美国、韩国和印度的七个独立样本中，收集了超过 5,000 名受访者的数据。')

add(7,'细节','Which set correctly matches each example to the life dimension being assessed?',
 ['Purpose—richness; interesting experiences—happiness; satisfaction—meaning.','Satisfaction—richness; purpose—happiness; interesting experiences—meaning.','Interesting experiences—meaning; satisfaction—happiness; purpose—richness.','Interesting experiences—richness; satisfaction—happiness; purpose—meaning.'],3,
 '哪组把示例与所评估的人生维度正确对应？',['目的—丰富；有趣经历—幸福；满意—意义。','满意—丰富；目的—幸福；有趣经历—意义。','有趣经历—意义；满意—幸福；目的—丰富。','有趣经历—丰富；满意—幸福；目的—意义。'],
 ['A 三组中目的、经历和满意度均错配。','B 把三类题项循环错置。','C 只有满意对应幸福正确，另两项颠倒。','D lot of interesting experiences、satisfied with my life、clear sense of purpose 分别属于三套自报题项；不是对参与者临终时实际行为的观察。'],
 ['a psychologically rich life (e.g., “I have had a lot of interesting experiences,”','a happy life (e.g., “I am satisfied with my life,”','a meaningful life (e.g., “I have a good sense of what makes my life meaningful,”'],
 'sense of purpose','目的感；目标感','有意义生活量表中的自我描述，不是研究者替参与者安排的目标','Volunteering gave her a stronger sense of purpose.',['a clear sense of purpose','develop a sense of purpose'],
 '我们向他们提出一系列关于心理丰富人生的问题，例如“我有过许多有趣的经历”“在临终时，我可能会说：我见识并学到了很多”（完整题目见附录 1，也可测测自己的心理丰富性分数）；一系列关于幸福人生的问题，例如“我对自己的人生感到满意”“到目前为止，我已经得到人生中想要的重要东西”；以及一系列关于有意义人生的问题，例如“我很清楚是什么使自己的人生有意义”“我的人生有明确的目的感”。')

add(8,'细节','What did the additional personality questions ask respondents to judge?',
 ['How well descriptive words characterised them in general.','How often they had met people called imaginative or tense.','Which word was most common in a dictionary.','How much their personality had changed since yesterday.'],0,
 '新增的人格问题要求受访者判断什么？',['描述词在多大程度上概括自己通常的样子。','遇到被称为有想象力或紧张的人的频率。','哪个词在词典中最常见。','自己的人格从昨天起变化了多少。'],
 ['A the degree to which each word described who they are in general 直接说明评分对象。','B 词描写的是本人，不是所遇他人。','C 不是词频或词典调查。','D in general 指通常特征，不是一天内的变化。'],
 ['the degree to which each word described who they are in general'],
 'sympathetic','有同情心的；体谅他人的','列为自评人格的描述词之一，不是感到自己值得同情','She was sympathetic to the students’ concerns.',['sympathetic to someone','a sympathetic listener'],
 '此外，我们询问受访者的人格：富于想象、做事有条理、健谈、有同情心、紧张等每个词，在多大程度上描述了他们通常的样子。')

add(9,'推断','What does the comparison with fathers’ and sons’ heights imply about the .47 correlation?',
 ['It predicts every individual’s psychological richness without error.','It reflects a fairly strong tendency with room for exceptions.','It means exactly 47 percent of open people have rich lives.','It proves that openness alone causes every rich experience.'],1,
 '父子身高的类比说明 .47 这一相关值意味着什么？',['能毫无误差地预测每个人的心理丰富性。','呈现相当强的倾向，但仍容许例外。','恰好 47% 的开放者人生丰富。','证明开放性单独造成每一种丰富经历。'],
 ['A far from absolute 排除无误差预测。','B quite strong, though far from absolute 既说明关联强度，也限制绝对化。','C 相关系数不是人数百分比。','D predictors 和 correlation 均不能仅凭本段改写为单一确定因果。'],
 ['which is quite strong, though far from absolute.','open people tend to lead a psychologically rich life'],
 'correlation','相关；相关系数','此处 .47 衡量开放性与心理丰富性的关联，不是 47% 的人数比例','A correlation does not by itself establish a causal direction.',['a correlation between','a positive correlation'],
 '心理丰富人生的两项主要人格预测因素是经验开放性与外向性（所有相关值见附录 2）。经验开放性与心理丰富性的 .47 相关，类似父亲与儿子身高之间的相关，相当强，但远非绝对。也就是说，开放的人倾向于过心理丰富的人生，就像父亲高的儿子往往也高。','inference')

add(10,'逻辑关系','How does this passage qualify the link between openness and richness?',
 ['Low openness rules out richness in every case.','High openness guarantees richness despite all other circumstances.','Only people high in openness can be exceptions.','There are exceptions in both directions.'],3,
 '本段怎样限定开放性与丰富性之间的联系？',['低开放性在每个个案中都排除丰富性。','高开放性不受其他条件影响，必定保证丰富性。','只有高开放性者可能成为例外。','两个方向都存在例外。'],
 ['A 原文有低开放但人生丰富者。','B 原文也有高开放但人生不丰富者。','C as well as 两侧分别列出两类例外。','D 两类相反组合同时出现，说明关联并非一一决定。'],
 ['people low in openness who lead psychologically rich lives as well as people who are high in openness who don’t lead psychologically rich lives.'],
 'exceptions','例外','不符合总体倾向的个体，不能因其存在就断言总体没有关联','Several exceptions prevented a simple rule from fitting every case.',['an exception to a rule','plenty of exceptions'],
 '但正如有些儿子的身高与父亲很不同，这里也有许多例外：有些开放性低的人过着心理丰富的人生，也有些开放性高的人并没有。现在，让我们先聚焦开放性与心理丰富性的联系。')

add(11,'细节','Which tendency is specifically reported for students high in openness?',
 ['They are less likely to pursue intellectual interests.','They prefer routine more than students low in openness.','They are more likely to study abroad than less open students.','They all choose the same artistic subject at university.'],2,
 '本段具体报告高开放性学生具有哪种倾向？',['较不愿追求知识兴趣。','比低开放性学生更偏好惯例。','比低开放性学生更可能留学。','大学里全部选择同一种艺术学科。'],
 ['A 原文说 open people 对知识和艺术有兴趣。','B preferring routine 修饰低开放性者。','C 最后一句明确比较留学可能性；more likely 不等于所有人。','D 没有统一选科的信息，也不能把倾向扩成全体。'],
 ['Students who are open to experience are more likely to study abroad'],
 'pursuits','追求；活动','intellectual and artistic pursuits 指知识与艺术方面的兴趣活动，不限于正式学位','She makes time for artistic pursuits after work.',['intellectual pursuits','artistic pursuits'],
 '为什么经验开放性高的人往往过着心理丰富的人生？开放的人富于想象、好奇，对知识和艺术活动有兴趣。开放性低的人则较传统、脚踏实地，偏好惯例，对知识或艺术活动较少兴趣。与开放性低的学生相比，开放的学生更可能留学；留学是一项已知能增进心理丰富性的活动。')

add(12,'逻辑关系','Which sequence best represents the reciprocal relationship the authors propose?',
 ['Openness encourages enriching activities, which can further increase openness.','Enriching activities eliminate openness, which then prevents later activities.','Personality fixes destiny, so activities cannot make any difference.','Studying abroad benefits only people who are already extraverts.'],0,
 '哪一顺序最符合作者提出的双向关系？',['开放性促成丰富活动，活动又可进一步提高开放性。','丰富活动消除开放性，进而阻止后续活动。','人格决定命运，所以活动毫无作用。','留学只使本来就外向的人获益。'],
 ['A increases one’s chance 与 in turn boosts 对应相互促进；这是作者据所述信息提出的解释，不是本段单独证明的普遍确定因果。','B boosts 是提高，不是消除。','C 原文明确说人格并非命运。','D 本段没有外向者独享留学收益的限制。'],
 ['openness to experience increases one’s chance of engaging in richness-enhancing activities, which in turn boosts one’s openness further.'],
 'reciprocal','相互的；双向的','说明作者所提出的开放性与丰富经历相互促进，而非单向宿命','The discussion focused on a reciprocal relationship between trust and cooperation.',['a reciprocal relationship','reciprocal influence'],
 '有趣的是，与没有留学的人相比，留学者随时间变得更开放。基于这些信息，我们认为经验开放性与心理丰富性存在双向关系：开放性增加参与增进丰富性活动的机会，而这些活动又进一步提高开放性。不过，人格不是命运；本书后面的章节会介绍每个人无论人格如何，都能采用、使人生更心理丰富的策略。')

add(13,'推断','What limitation does Joy Ryan’s example illustrate?',
 ['She had no openness until the author measured it at age ninety-four.','Being open ensures abundant travel opportunities from childhood.','Openness alone need not produce rich experiences when opportunities are limited.','The .47 correlation means opportunities have no role in richness.'],2,
 'Joy Ryan 的例子说明了什么限制？',['直到作者在她九十四岁测量前，她一直毫无开放性。','只要开放，从童年起就必有丰富旅行机会。','机会有限时，单有开放性不一定带来丰富经历。','.47 的相关意味着机会对丰富性毫无作用。'],
 ['A might have always been 保留可能性，文中没有声称作过这种测量。','B 她八十五岁前恰恰探索机会较少。','C 不保证的总论与机会受限的个人例子相连，支持有限推断。','D 机会在本例中正是关键条件，相关系数不能排除它。'],
 ['having an open personality doesn’t necessarily guarantee that you will lead a psychologically rich life.','until she turned eighty-five, she hadn’t had many opportunities to explore the world.'],
 'hooked','着迷的；被深深吸引的','指她接触国家公园后被吸引，并非这里在诊断药物成瘾','After the first lesson, she was hooked on pottery.',['be hooked on','get hooked'],
 '.47 的相关也意味着，拥有开放人格不一定保证过心理丰富的人生。我们在第 4 章见过的九十四岁国家公园爱好者 Joy Ryan，或许一直对经验开放。但是，直到八十五岁前，她都没有太多探索世界的机会。一旦接触 Smoky Mountain National Park，她便着迷了。','inference')

add(14,'主旨','Which combination does the author emphasise as opening the door to rich experiences?',
 ['An open personality with no need for opportunities or resources.','An open personality together with opportunities and resources.','Resources alone, regardless of any opportunity to use them.','A wish to travel as proof that all parks have already been visited.'],1,
 '作者强调什么组合能为丰富经历打开大门？',['开放人格，不需要机会或资源。','开放人格加上机会和资源。','只有资源，不论有没有使用机会。','想旅行就证明已游览全部公园。'],
 ['A plus 后的两个条件被遗漏。','B 概括末句三个要素的组合，不将其当作排他性的万能公式。','C 不符合原文列出的共同条件。','D wanted to visit 是意愿，不是完成经历。'],
 ['having an open personality plus opportunities and resources opens the door to psychologically rich experiences.'],
 'opens the door to','为……打开大门；创造可能','以开门比喻开放性、机会与资源促成接触丰富经历','The scholarship opened the door to further study.',['open the door to opportunities','open the door to new experiences'],
 '她对更多新经历变得开放，此后想去游览所有国家公园。换言之，开放的人格加上机会和资源，为心理丰富的经历打开了大门。')

add(15,'细节','Which account correctly preserves the timing of Simon Ramo’s patents?',
 ['He received all twenty-five patents at age one hundred.','He received his final patent before turning thirty.','He had sixty-two patents before he was thirty.','He had twenty-five patents before thirty and his last at one hundred.'],3,
 '哪项正确保留了 Simon Ramo 获专利的时间信息？',['全部二十五项专利都在一百岁取得。','最后一项专利在三十岁前取得。','三十岁前有六十二项专利。','三十岁前有二十五项，一百岁获得最后一项。'],
 ['A 把早年专利与晚年最后一项合并为同一时间。','B 原文最后一项在 age one hundred。','C sixty-two 指书的数量，不是专利数。','D twenty-five...before...thirty 与 final...one hundred 分别对应；这是个人事例，不证明所有高智力者必然如此。'],
 ['he had twenty-five patents before he was thirty, and earned his final patent at age one hundred.'],
 'patents','专利','指发明获得的专利；须与本段另一个数字“六十二本书”区分','The engineer holds several patents for medical devices.',['hold a patent','earn a patent'],
 '除了机会与资源，智力与艺术能力也是因素。Simon Ramo 是航天工程师，他在《纽约时报》的讣告被评为特别心理丰富。他在 California Institute of Technology 获得物理与工程博士学位，后来研制洲际弹道导弹，即 ICBM。他一生出版六十二本书，三十岁前已有二十五项专利，一百岁取得最后一项专利。')

add(16,'逻辑关系','What reason is given for Ramo’s move from large corporations to his own company?',
 ['He became tired of corporate bureaucracy.','He had stopped being interested in engineering.','He needed a company devoted only to tennis books.','His employer required him to become a barber.'],0,
 '本段给出 Ramo 离开大公司、创办自己公司的什么原因？',['他厌倦了公司官僚作风。','他不再对工程感兴趣。','他需要一家只写网球书的公司。','雇主要求他改当理发师。'],
 ['A got sick of the bureaucracy 后用 So 引出创办公司，原因明确。','B 创业后仍开发导弹初始原型。','C 网球是另一个兴趣，only 扩大并限制了业务范围。','D former barbershop 是创业场地，不能据此改写职业或雇主要求。'],
 ['got sick of the bureaucracy. So he started his own company in a former barbershop'],
 'bureaucracy','官僚体制；繁琐规章','指令他厌倦的大公司运作方式，不是字面疾病','The team reduced bureaucracy to speed up decisions.',['corporate bureaucracy','cut through bureaucracy'],
 '他于一百零三岁去世。Simon 最初在大公司工作，却厌倦官僚作风。因此他在一间原来的理发店创办自己的公司，在那里开发洲际弹道导弹的初始原型。他也对其他主题有兴趣，包括网球策略——后来他还为此写了一本书。')

add(17,'作者意图','How does the author use Ramo’s “registered opportunist” reply?',
 ['As evidence that he had formally registered a new political party.','To illustrate humor and interests not confined to one belief system.','To establish that he had no interest in the world around him.','As a definition of the only acceptable personality type.'],1,
 '作者怎样使用 Ramo 那句“登记在册的机会主义者”的回答？',['证明他正式登记成立了新政党。','表现幽默及不受单一信仰体系束缚的兴趣。','证明他对周遭世界毫无兴趣。','定义唯一可接受的人格类型。'],
 ['A 不能把玩笑字面化成政党登记事实。','B great sense of humor 引出回答，后文又强调多样兴趣与智力。','C fascination with the world 与此相反。','D 个人描述不是所有人必须遵循的规范。'],
 ['he had a great sense of humor.','Ramo’s fascination with the world could not be codified by a particular belief system.'],
 'codified','被编成体系；被系统归类','指他的世界兴趣难被某个特定信仰体系固定概括','The informal practices were later codified in a handbook.',['codify rules','be codified by a system'],
 '而且，他很有幽默感。被问到政治立场时，他回答：“我是登记在册的机会主义者。”Ramo 对世界的着迷，无法用某个特定信仰体系来归纳。他兴趣多样，智力非凡。')

add(18,'细节','What does the passage say Cha did NOT do after the 1955–1972 writing period?',
 ['Transfer to his newspaper’s Hong Kong office during that period.','Become known under the name Jin Yong.','Write any new novels after that period.','Write novels inspired by martial arts history during that period.'],2,
 '本段说，1955–1972 年创作期之后，Cha 没有再做什么？',['在该时期转到报纸香港办事处。','以 Jin Yong 这个名字为人所知。','在该时期之后再写新小说。','在该时期写受武术历史启发的小说。'],
 ['A 调职在 1950 年代，选项不是本段所说停止的创作行为。','B 别名是身份说明，没有改名停止之意。','C didn’t write any new novels after this period 直接对应。','D 此前确实创作这类小说，不能错配为之后未再写的时间范围。'],
 ['Despite his popularity, Cha didn’t write any new novels after this period.'],
 'Despite','尽管','把受欢迎与后来不再写新小说形成让步关系，不解释停止创作的原因','Despite the rain, the outdoor performance continued.',['despite his popularity','despite the difficulties'],
 '另一个心理丰富人生的例子是小说家 Louis Cha（亦即 Jin Yong、金庸），他的讣告刊于《海峡时报》。Cha 出生于中国，最初在上海当记者，1950 年代转到报纸的香港办事处。他在 1955 至 1972 年间，写了一系列受武术历史启发、极受欢迎的小说。尽管备受欢迎，这一时期之后他没有再写新小说。')

add(19,'细节','What did Cha continue doing instead of producing new novels?',
 ['Replacing every favorite character with a historical journalist.','Moving all his writing work back to Shanghai.','Revising only the newspaper articles of other writers.','Rereading and revising his own novels.'],3,
 'Cha 没有再写新小说，而是继续做什么？',['把所有喜爱的人物换成历史记者。','把全部写作工作搬回上海。','只修订其他作者的报纸文章。','重读并修订自己的小说。'],
 ['A 人物分手使他落泪，不是替换人物。','B 本段没有回迁上海的信息。','C own novels 明确是自己的小说。','D Instead 引出 reread...continued to revise，正面说明替代活动。后面的政治经历按作者叙述保留，不据此推出普遍结论。'],
 ['Instead, he reread his own novels and continued to revise them.'],
 'defiant','反抗的；不屈服的','作者用来加强 unconventional 的人物特征，后接政治写作经历','She remained defiant in the face of pressure to withdraw.',['a defiant attitude','remain defiant'],
 '他转而重读自己的小说，不断修订。在自己的小说里读到最喜爱人物的分手，他会落泪。他不循常规，甚至带有反抗精神。1960 年代末，他写了一系列反毛文章，原文叙述这使他被列入中国共产党的暗杀名单。')

add(20,'逻辑关系','What contrast does “Yet” introduce in the account of Cha’s life?',
 ['His life was turbulent and not worry-free, but still unique and interesting.','His escape guaranteed that he never faced any worries.','His life was uninteresting because he spent almost a year abroad.','His happiness is presented as the cause of his escape.'],0,
 'Yet 在 Cha 人生的叙述中引出什么对照？',['生活动荡、并非无忧，却仍独特有趣。','逃离保证他再无任何忧虑。','在外近一年使他的人生变得无趣。','他的幸福被说成逃离的原因。'],
 ['A hardly...happy or worry-free 与 unique, interesting 构成让步对照。','B 把避免暗杀的目的扩大成永无忧虑。','C interesting 与无趣相反，句中也没有这种因果。','D 逃离的目的明写 to avoid assassination，不是幸福导致。'],
 ['Cha’s tumultuous life can hardly be characterized as happy or worry-free. Yet he had a unique, interesting life.'],
 'tumultuous','动荡的；充满波折的','形容作者所述政治风险与逃离经历，不等同于幸福或无忧','The memoir describes a tumultuous period of change.',['a tumultuous life','a tumultuous period'],
 '他逃往新加坡，为避免暗杀在那里住了近一年。Cha 动荡的人生很难说是幸福或无忧无虑的。然而，他拥有独特而有趣的人生。')

add(21,'细节','Which distinction between the two subfactors is described?',
 ['Openness predicts only scientific work, while intellect excludes the arts.','Both subfactors are described as having no connection with creativity.','Openness is linked with creative arts, while intellect is linked with arts and sciences.','Intellect and openness are simply two names for the same subfactor.'],2,
 '本段怎样区分两个子因子？',['开放子因子只对应科学，智性排除艺术。','两个子因子都与创造无关。','开放子因子与艺术创造有关，智性与艺术和科学创造都有关。','智性与开放只是同一子因子的两个名称。'],
 ['A 将领域颠倒，还把智性涉及艺术这一点删去。','B 原文明确说 more creative accomplishments。','C 对应 arts 与 both in arts and sciences；tend to 表示倾向，不是所有人的决定性规则。','D 原文明确 two subfactors。作者把 Ramo 与 Cha 作示例属于人物解释，并未报告两人的直接量表测量。'],
 ['People high in openness tend to have more creative accomplishments in the arts, whereas people high in intellect tend to have more creative accomplishments both in arts and sciences.'],
 'subfactors','子因子','经验开放性这一较大因子之下的开放与智性两个分支，不是两个全新的大五因子','The model divides the broad category into two subfactors.',['two subfactors','classify into subfactors'],
 '人格心理学家把经验开放性分成两个子因子：开放与智性。开放子因子高的人往往有更多艺术创造成就，而智性高的人在艺术与科学两方面都往往有更多创造成就。作者推断，Simon Ramo 的经验开放性中，智性维度一定很高，因为他探索并创造性解决了各种工程问题；Louis Cha 的开放维度一定很高，因为他过着情感丰富、富于想象的人生。')

add(22,'同义改写','Which statement best paraphrases the author’s proposed distinction?',
 ['Openness and extraversion both concern only abstract ideas.','Openness explores sensory and abstract information; extraversion explores people.','Extraversion means avoiding interpersonal information.','Openness concerns social status, while extraversion concerns intelligence tests.'],1,
 '哪项最贴近作者提出的区分？',['开放性与外向性都只关乎抽象观念。','开放性探索感官与抽象信息；外向性探索他人。','外向性意味着回避人际信息。','开放性关乎社会地位，外向性关乎智力测试。'],
 ['A 把外向性所探索的人际信息删掉，only 也缩窄了开放性。','B 对应 sensory and abstract 与 interpersonal，以及 ideas 与 other people 的对照。','C exploring 与 avoiding 方向相反。','D social world 不等于社会地位，本段也没提智力测试。'],
 ['openness to experience is concerned with the exploration of sensory and abstract information, extraversion is concerned with the exploration of interpersonal information.'],
 'interpersonal','人际的；人与人之间的','指探索他人和社会互动中的信息，不是抽象知识的同义词','The course develops interpersonal communication skills.',['interpersonal information','interpersonal skills'],
 '经验开放性与心理丰富性的联系似乎显而易见，外向性在心理丰富人生中的作用却未必如此。理解这联系最容易的方式，是把外向性看作探索社会世界的兴趣。也就是说，如果经验开放性关乎探索感官与抽象信息，外向性就关乎探索人际信息。如果开放的人对观念好奇，外向的人就对其他人好奇。')

add(23,'逻辑关系','What reason does the sentence give for linking more interaction with richer experiences?',
 ['Every conversation is equally pleasant.','Meeting people removes all differences between them.','Rich experiences require talking only to existing friends.','People differ, so interacting with more people increases experiential variety.'],3,
 '本句给出什么理由，把更多互动与更丰富的经历联系起来？',['每次谈话都同样愉快。','结识他人会消除他们之间的一切差异。','丰富经历要求只和老朋友交谈。','人各有不同，因此更多互动增加经历的多样性。'],
 ['A diverse 不等于每次都愉快。','B Because people are different 把差异作为前提，而非被消除的结果。','C 原句没有 only 或老朋友限制。','D 前半句给出理由，两个 the more 连接互动数量、多样经历与丰富性；这是作者的论述，不是本句提供了随机实验或每次互动的效果保证。'],
 ['Because people are different, the more people you interact with, the more diverse experiences you will have'],
 'diverse','多样的；各不相同的','强调与不同人接触带来的经历差异，不单指数量多或总是快乐','The project brought together people with diverse backgrounds.',['diverse experiences','diverse backgrounds'],
 '由于人各有不同，你与越多人互动，便会有越多样的经历，人生也会变得越丰富。')

add(24,'细节','How does the author describe his own usual behaviour at a party?',
 ['He tends to stay with one or two familiar people for a deeper conversation.','He tries to meet every new person and avoids familiar faces.','He refuses to speak to anyone he already knows.','He describes his strategy as identical to an extravert’s.'],0,
 '作者怎样描述自己在聚会中通常的表现？',['倾向与一两位熟人待在一起，作较深入的交谈。','努力结识每位陌生人，回避熟面孔。','拒绝与任何已认识的人说话。','认为自己的策略与外向者完全相同。'],
 ['A already know、one or two people、deeper conversation 逐一对应。','B 把熟人换成陌生人，且 every 扩大范围。','C 与 gravitate toward someone I already know 相反。','D very different 明说有别。此处是作者自述，不是对所有内向者的统一测定。'],
 ['I usually stick with one or two people and try to have a deeper conversation.'],
 'gravitate toward','自然地趋向；被吸引到','指作者在聚会中习惯靠近熟人，是倾向而非不可改变的规则','At large events, I gravitate toward small discussion groups.',['gravitate toward someone','gravitate toward familiar surroundings'],
 '在聚会上，你会和谁交谈？我是内向的人，所以会自然走向自己已经认识的人。我通常和一两个人待在一起，试着作较深入的交谈。外向的人则有很不同的策略。')

add(25,'逻辑关系','Why might an extraverted friend expand someone’s social network more?',
 ['Extraverts have fewer friends, leaving more room in each network.','Extraverts tend to have more friends, offering links to a wider network.','A single friendship guarantees meeting every kind of person.','Extraverts learn new things only from introverted friends.'],1,
 '为什么一位外向朋友可能更能扩展一个人的社交网络？',['外向者朋友更少，网络因此有更多空位。','外向者通常朋友更多，可通向更广的关系网络。','一段友谊保证结识每种人。','外向者只能从内向朋友学到新东西。'],
 ['A fewer 与原文 more 相反。','B Since 引出朋友更多这一理由，is likely to 保留概率，而非必然。','C 将 more likely 扩成保证且扩大至每种人。','D 本段没有“只能”或这类学习来源限制。network extraversion bias 具体指外向者与其他外向者交友的现象，不能泛化为所有友谊都只发生在同类之间。'],
 ['Since extraverts have more friends than introverts, making an extraverted friend is likely to expand your social networks more than making an introverted friend.'],
 'network extraversion bias','社交网络外向性偏向','本段称外向者与其他外向者交友的现象，并非保证每位朋友都外向','The seminar discussed network extraversion bias in friendship patterns.',['network extraversion bias','expand social networks'],
 '他们会与许多新面孔交谈，交到更多朋友。外向者会与其他外向者成为朋友，这一现象称为“社交网络外向性偏向”。由于外向者比内向者朋友更多，与外向者交朋友，可能比与内向者交朋友更能扩展你的社交网络。因此从长远看，外向者比像我这样的内向者，更可能遇到不同类型的人，也更可能学到新东西。')

assert len(out)==25 and [q['id'] for q in out]==[t['questionId'] for t in targets]

def persist():
 path=ROOT/'source/short-questions/additional.json';existing=load('source/short-questions/additional.json');byid={q['id']:q for q in existing}
 for q in out:
  if q['id'] in byid:assert byid[q['id']]==q,('Refuse to overwrite changed authoring',q['id'])
  else:existing.append(q)
 path.write_text(json.dumps(existing,ensure_ascii=False,indent=2)+'\n',encoding='utf8',newline='\n')
 review=dict(batchId='batch-015',date='2026-10-22',pdfSha256=b['pdfSha256'],checkedPdfPages=list(range(58,63)),questionIds=[q['id'] for q in out],paragraphs=[dict(id=pid,textSha256=hashlib.sha256(pp[pid]['text'].encode()).hexdigest()) for pid in dict.fromkeys(q['paragraphId'] for q in out)],note='完整 PDF 58–62 原页视觉对照，包含跨页题项、Joy Ryan 和社交网络段落。保留 .47 的非决定性、自报范围、作者双向关系解释和人物归因；q-c06-032 保留既有固定单元的 and so on 短语尾段，不称为独立完整句。候选句界不冒充人工最终分句。')
 (ROOT/'source/short-questions/review-chapter06-personality25.json').write_text(json.dumps(review,ensure_ascii=False,indent=2)+'\n',encoding='utf8',newline='\n')
 print('Saved',len(out),'of 25 individually authored exercises')

if __name__=='__main__':persist()
