"""45 individually authored exercises for the next 45 frozen reading units.
PDF pages 18-25 visually checked on 2026-10-22. No runtime question generation.
"""
from pathlib import Path
import json,hashlib
ROOT=Path(__file__).resolve().parents[2]
load=lambda p:json.loads((ROOT/p).read_text(encoding='utf8'))
b=load('public/data/book.json');plan=load('public/data/reading-plan.json');targets=load('source/short-questions/batch008-targets.json')['targets']
ss={s['id']:s for s in b['sentences']};pp={p['id']:p for p in b['paragraphs']};out=[]
def add(n,kind,prompt,options,answer,prompt_zh,options_zh,analyses,quotes,word,meaning,context,example,collocations,translation,support='explicit'):
 target=targets[n-32];assert target['questionId']==f'q-c02-{n:03}'
 u=next(u for u in plan['units'] if u['id']==target['readingUnitId']);group=[ss[i] for i in u['sentenceIds']];p=pp[u['paragraphId']];text=p['text'][group[0]['start']:group[-1]['end']]
 assert hashlib.sha256(text.encode()).hexdigest()==target['passageSha256']
 evidence=[]
 for quote in quotes:
  offset=text.find(quote);assert offset>=0,(n,quote);start=group[0]['start']+offset;end=start+len(quote);touching=[s for s in group if s['start']<end and s['end']>start]
  evidence.append(dict(quote=quote,sentenceIds=[s['id'] for s in touching],sources=list({(r['pdfPage'],r['block']):r for s in touching for r in s['sources']}.values())))
 assert word.lower() in text.lower(),(n,word)
 out.append(dict(id=f'q-c02-{n:03}',version=1,readingUnitId=u['id'],chapterId=u['chapterId'],sectionId=u['sectionId'],paragraphId=u['paragraphId'],sentenceIds=u['sentenceIds'],passage=text,prompt=prompt,options=options,answer=answer,type=kind,promptZh=prompt_zh,optionsZh=options_zh,analyses=analyses,evidence=evidence,vocabulary=[dict(word=word,meaning=meaning,context=context,example=example,collocations=collocations)],translation=translation,support=support,editorialStatus='PDF 第 18–25 页具体原文逐题编写并视觉核对；保留限定、统计年份、观点归属及类比性质；固定无重复短段'))

add(32,'主旨','What does the author stress when discussing Madison’s death?',
 ['Social comparison alone fully explains it.','A cheerful appearance rules out serious inner difficulties.','Its complexity cannot be reduced to one feeling of inferiority.','Her private feelings were objectively identical to her friends’.'],2,
 '作者讨论 Madison 的死亡时强调什么？',['仅凭社会比较就能完整解释。','快乐的外表能排除严重内心困扰。','其复杂性不能简化为一种自卑感。','她的私人感受客观上与朋友完全相同。'],
 ['A not just...but also...明确拒绝单一因素解释。','B 原文恰好对照快乐表象与深刻内心挣扎。','C extremely complex 与 many other things 支持多因素、非单一解释。','D 没有对朋友感受作客观测量或等同判断。'],
 ['Suicide is an extremely complex behavior. Madison’s suicide must have been driven not just from feeling inferior to her friends’ social lives, but also from many other things.'],
 'profound','深刻的；强烈的','修饰内心挣扎，强调表象未呈现的深度','The journey had a profound effect on her outlook.',['profound inner struggles','a profound effect'],
 '自杀是一种极其复杂的行为。Madison 的自杀，驱动因素一定不只是觉得自己的社交生活不如朋友，还包括许多其他事情。令人震惊的是，她如此善于在公众面前装作快乐；一个看上去适应良好、很幸福的人，也有深刻的内心挣扎，最终走向悲剧。她是例外，还是普遍情形？')

add(33,'细节','What does “14 out of 100,000” describe in the passage?',
 ['The rate of Americans dying by suicide in 2018.','The percentage increase from 2000 to 2018.','The number of adults reporting suicidal thoughts in 2020.','The proportion of all deaths attributed to suicide in 2018.'],0,
 '“每十万人中有十四人”在本段指什么？',['2018 年美国人死于自杀的比率。','2000 至 2018 年的百分比增幅。','2020 年报告自杀想法的成年人数量。','2018 年所有死亡中自杀所占的比例。'],
 ['A 原句明确限定 2018 年、美国人及 dying by suicide。','B 增幅对应 38 percent，不是 14/100,000。','C 本段该数字不指思想，也不属于 2020 年。','D 分母是美国人口，不是所有死亡人数。'],
 ['In the peak year of 2018, the rate of Americans dying by suicide reached 14 out of 100,000'],
 'rate','比率；发生率','这里以每十万人为分母，须与百分比增幅区分','The report gives the accident rate per 100,000 residents.',['a mortality rate','a rate per 100,000'],
 '根据美国疾病控制中心（CDC）的人口动态统计，2000 至 2018 年间，美国人的自杀情况增加了 38%。自杀仍相对少见。在达到高点的 2018 年，美国人死于自杀的比率为每十万人中十四人，这个数字可能让 Madison 的个案看起来像例外。然而，自杀意念却并非如此少见。')

add(34,'细节','Which interpretation matches the passage’s 2020 figures?',
 ['1.2 million adults seriously considered suicide and 12.2 million attempted it.','Roughly one in twenty adults died by suicide that year.','The two figures count the same event in identical populations.','12.2 million adults seriously considered suicide, distinct from 1.2 million attempts.'],3,
 '哪项解释符合本段的 2020 年数字？',['120 万成年人认真考虑自杀，1,220 万次为尝试。','当年约每二十名成年人中就有一人死于自杀。','两个数字统计的是相同人群中的同一种事件。','1,220 万成年人认真考虑自杀，有别于 120 万次自杀尝试。'],
 ['A 把想法人数与尝试次数的数字对调了。','B one in 20 指认真想过，不是死亡。','C 原文区分 attempts 与 adults who thought，不能等同。','D 正确保留两类统计对象；没有假定二者互不重叠或完全相同。'],
 ['According to the CDC, in 2020 there were 1.2 million suicide attempts and 12.2 million American adults who “seriously” thought about suicide.'],
 'roughly','大约；粗略地','one in 20 是近似概括，不是精确个体预测','Roughly half the participants arrived early.',['roughly one in twenty','roughly half'],
 '根据 CDC 的数据，2020 年发生了 120 万次自杀尝试，另有 1,220 万美国成年人“认真”想过自杀。这意味着当年约每二十名美国成年人中，就有一人认真想过以自杀方式死亡。这个数字很大。因此，若看自杀想法的出现频率，Madison 的个案似乎就没那么罕见了。')

add(35,'作者意图','What issue does the question shift attention toward?',
 ['How to calculate an exact mortality rate.','Why someone experiencing suicidal thoughts felt pressure to appear happy.','Whether Madison ever experienced unhappiness.','Which public appearance proves an absence of inner struggle.'],1,
 '这个问题把注意力转向什么？',['如何计算精确死亡率。','为什么有自杀想法的人仍感到必须表现快乐的压力。','Madison 是否曾经不快乐。','哪种公众表象能证明没有内心挣扎。'],
 ['A 问句没有要求计算统计比率。','B Why...pressure...despite...直接呈现这一待解释的反差。','C despite having 已承认内心困扰，并非怀疑其存在。','D 问句探讨反差，不能用表象证明内心无困扰。'],
 ['Why did she feel so much pressure to put on a happy face, despite having suicidal thoughts?'],
 'despite','尽管；虽然有','引出内心想法与表现快乐压力之间的反差','Despite the rain, the match continued.',['despite difficulties','despite having doubts'],
 '于是，下一个问题是：为什么她尽管有自杀想法，仍感到那么大的压力，要摆出一副快乐面孔？','inference')

add(36,'主旨','What view of happiness is illustrated by the students’ responses?',
 ['Happiness is entirely unrelated to individual effort.','Happiness is an unavoidable outcome of chance alone.','Happiness is something achieved through effort and success.','Happiness is defined only by the absence of anger.'],2,
 '学生的回答体现了怎样的幸福观？',['幸福与个人努力完全无关。','幸福只是运气必然带来的结果。','幸福可以通过努力和成功获得。','幸福只被定义为没有愤怒。'],
 ['A reward for hard work 明确联系努力。','B 本段强调 achievable 与 succeeding，不是纯粹运气。','C reward、succeeding、victory 共同体现成就导向的文化理解。','D 回答没有把幸福限定为排除愤怒。'],
 ['Many wrote something like, “Happiness is a reward for all the hard work you employ” and “Happiness is the feeling of succeeding.” One student wrote simply that happiness is a “victory”!'],
 'achievable','可达到的；可实现的','描述文化把幸福看成可以达成的目标','The team agreed on a challenging but achievable target.',['an achievable goal','an achievable target'],
 '必须快乐的压力，其核心是美国文化将幸福建构为一种可以实现的东西。在一项研究中，美国大学生被要求写下想到“幸福”时浮现的任何内容。许多人写道，幸福是所有辛勤努力的回报，或幸福是成功时的感受。一名学生干脆把幸福称为一场“胜利”！')

add(37,'细节','What were college students asked to write about in the other study?',
 ['Aspects, features, or effects of happiness or unhappiness.','Only occasions when they won a competition.','Their predicted salary after graduation.','Reasons for ranking happiness above health.'],0,
 '另一项研究要求大学生写什么？',['幸福或不幸福的方面、特征或影响。','仅写赢得比赛的场合。','毕业后预计能获得的薪水。','把幸福排在健康之前的理由。'],
 ['A 逐项对应 different aspects, features, or effects 及 either...or...。','B 把开放主题缩窄成仅有竞赛胜利。','C 本段未要求收入预测。','D 没有让学生比较幸福与健康的排名。'],
 ['Another study asked college students to write about “different aspects, features, or effects of either happiness or unhappiness.”'],
 'association','联系；关联','这里概括幸福与成功的概念联系，不是自动证明因果','The study examined the association between sleep and concentration.',['an association between','a strong association'],
 '也就是说，幸福与成功之间有很强的联系。另一项研究要求大学生写下“幸福或不幸福的不同方面、特征或影响”。')

add(38,'逻辑关系','Which conditional reasoning is described as common among many people?',
 ['Failure always produces success before happiness.','Happiness and success are treated as unrelated concepts.','Success is possible only when a person feels unhappy.','Not being happy is taken to imply not being successful.'],3,
 '本段说，许多人采用怎样的条件推理？',['失败总会先带来成功，再带来幸福。','幸福与成功被看作无关。','只有不幸福时才可能成功。','不幸福被理解为不成功。'],
 ['A 原文是 Failure begets unhappiness，没有失败必获成功。','B pursuit...equated 明确把两者相联。','C only when unhappy 与原文对成功带来幸福的描述不符。','D To many...if you are not happy, you are not successful 明确给出这种观念，非作者证明的普遍定律。'],
 ['To many, if you are not happy, you are not successful.'],
 'equated','被等同；被视为一样','描述将追求幸福与追求胜利等同的思路','A high price should not automatically be equated with quality.',['be equated with','equate one thing with another'],
 '如果幸福就是胜利，追求幸福就被等同于追求胜利。成功带来幸福，失败产生不幸福。对许多人来说，如果你不幸福，你就是不成功。')

add(39,'作者意图','How is Steinberg’s magazine cover used here?',
 ['As experimental proof that prosperity guarantees happiness.','As an illustration of a cultural story linking happiness with success.','As evidence that the author endorses calling unhappy people losers.','As a record of who won a real happiness competition.'],1,
 'Steinberg 的杂志封面在这里起什么作用？',['作为富裕保证幸福的实验证据。','展示把幸福与成功相联的文化叙事。','证明作者赞同把不幸福者称为失败者。','记录一场真实幸福比赛的获胜者。'],
 ['A 封面是文化例证，不是因果实验。','B cultural narrative 与封面上 Prosperity 获胜的形象呼应。','C 文段在说明压力来源，不能把被描述的标签当成作者赞同。','D 把象征性封面误读成实际比赛记录。'],
 ['The pressure to be happy might come from this cultural narrative of happiness as a sign of success.','In Saul Steinberg’s iconic 1959 New Yorker cover, Prosperity wins the contest of the Pursuit of Happiness, suggesting that it takes success and prosperity to be happy.'],
 'narrative','叙事；解释框架','指文化中幸福象征成功的故事或理解方式','The film challenges a familiar narrative about success.',['a cultural narrative','a dominant narrative'],
 '如果你不幸福，你就是个失败者。必须幸福的压力，也许来自这种把幸福看作成功标志的文化叙事。Saul Steinberg 那幅具有代表性的 1959 年《纽约客》封面上，“富裕”赢得“追求幸福”的竞赛，暗示必须成功而富裕才能幸福。','inference')

add(40,'细节','What qualification does the passage make about happiness after a major accomplishment?',
 ['Its effect seems to fade within about six months.','Its effect is guaranteed to last for life.','Every accomplishment immediately reduces happiness.','Promotions affect happiness only after six months have passed.'],0,
 '本段怎样限定重大成就带来的幸福？',['其影响似乎会在六个月内消退。','其影响保证持续一生。','每项成就都会立刻降低幸福。','晋升只有过了六个月才影响幸福。'],
 ['A seems to disappear within six months 支持，并保留 seems 的限定。','B rarely...everlasting 与终身保证相反。','C 影响不持久不等于立刻降低幸福。','D within 指消退的时间范围，不是开始生效的时间。'],
 ['The effect of a major accomplishment like a promotion on happiness seems to disappear within six months.'],
 'everlasting','永久的；永恒的','本段否定胜利通常会带来永久幸福的期待','The characters hoped for everlasting peace.',['everlasting happiness','everlasting peace'],
 '幸福研究者的发现与成就导向的幸福观很不一样：一次胜利很少带来永久的，甚至长期的幸福。像晋升这样的重大成就对幸福的影响，似乎会在六个月内消失。')

add(41,'细节','How did the tenure study distinguish expectations from experienced outcomes?',
 ['It asked only tenured professors to predict other people’s careers.','It randomly granted tenure to every participant.','It asked current assistant professors for predictions, then interviewed people with actual tenure outcomes.','It treated the assistants’ predictions as the final measured outcomes.'],2,
 '终身教职研究怎样区分预期与实际经历？',['只让已获终身教职者预测别人的职业。','随机给予每位参与者终身教职。','先询问现任助理教授的预测，再访谈已实际经历结果的人。','把助理教授的预测直接当成最终实际结果。'],
 ['A 最初被问的是 untenured assistant professors，不是已获教职者。','B 研究者询问和访谈，没有随机授予职位。','C asked...how...would feel 与 Next...former...did get...did not get 对应两个阶段。','D 忽略了后续对实际经历者的访谈，混同预测与结果。'],
 ['Dan Gilbert and colleagues asked untenured assistant professors how happy they would feel if they got tenure, as well as how unhappy they would feel if they were denied tenure.','Next, the researchers interviewed former assistant professors who did get tenure and others who did not get tenure.'],
 'tenure','终身教职；长期职位保障','此处指大学职业评审的结果，不是一般任期长度','She applied for tenure after several years of teaching.',['get tenure','be denied tenure'],
 '在一项研究中，Dan Gilbert 和同事询问尚未获得终身教职的助理教授：如果获得，会有多幸福；如果遭拒，又会有多不幸福。这听起来像个答案明显的问题。确实，他们都说，获得会欣喜，遭拒会受到沉重打击。接着，研究者访谈了以前的助理教授，其中一些获得了终身教职，另一些没有。')

add(42,'逻辑关系','What comparison does this sentence make?',
 ['Tenured professors were less happy than every rejected applicant.','Actual happiness after tenure was lower than current assistants had imagined.','Current assistants were unhappy because they had already lost tenure.','Receiving tenure was shown to make all recipients unhappy.'],1,
 '这句话作了什么比较？',['获终身教职者比每位遭拒者都不幸福。','获得教职后的实际幸福低于现任助理教授的想象。','现任助理教授因已经失去教职而不幸福。','获得教职被证明让所有获得者都不幸福。'],
 ['A 比较对象是 current assistant professors 的想象，不是每位遭拒者。','B not as happy as...imagined 准确给出实际与预期的差距。','C 当前助理教授在此是预测者，原句没有已失去教职。','D 低于预期不等于绝对不幸福，all 也无依据。'],
 ['those who got tenure were not as happy as the current assistant professors imagined.'],
 'imagined','想象；预想','修饰预测的幸福程度，区别实际经历','The course was more demanding than she had imagined.',['as imagined','imagine an outcome'],
 '那么，坏消息是，获得终身教职的人，并没有现任助理教授想象的那么幸福。')

add(43,'主旨','What does the passage identify as building long-term happiness?',
 ['A single major victory that removes the need for daily contact.','The permanent excitement of every promotion.','Having a first child rather than maintaining friendships.','Small recurring experiences such as daily coffee with a close friend.'],3,
 '本段认为什么能积累长期幸福？',['一次重大胜利，使日常交往不再必要。','每次晋升带来的永久兴奋。','生第一个孩子，而非维持友谊。','日常反复的小经历，例如每天和挚友喝咖啡。'],
 ['A It is not a big win 排除单次大胜的解释。','B short-lived 与永久兴奋相反。','C first child 被列为喜悦相对短暂的例子，不能替换后面的要点。','D Rather 后以 small things 和每天喝咖啡直接说明长期幸福的来源。'],
 ['Rather, it’s the small things in life, like having a coffee with your best friend every day, that build long-term happiness.'],
 'short-lived','短暂的；持续不久的','修饰重大事件带来的喜悦，而非事件本身的持续时间','The excitement after the announcement was short-lived.',['short-lived joy','a short-lived effect'],
 '幸福科学的第一个启示是，人们高估了成功在自身幸福中的作用。重大晋升、结婚或第一个孩子出生的喜悦，都相对短暂。带来幸福的不是一次大胜。相反，生活中的小事，比如每天和最好的朋友喝杯咖啡，才会积累长期幸福。')

add(44,'细节','What belief is conveyed by “Fake it till you make it” as explained here?',
 ['Continuing to act successful may eventually lead to success.','Pretending and succeeding are always unrelated.','Everyone who appears successful has already achieved every goal.','The saying advises people to abandon any appearance of success.'],0,
 '本段怎样解释“Fake it till you make it”所传达的信念？',['持续装作成功，最终可能真正成功。','假装与成功总是无关。','看起来成功的人都已实现所有目标。','这句话建议放弃任何成功的表象。'],
 ['A if you continue to pretend...eventually succeed 是文中对这种信念的解释；不是实验证明人人必定成功。','B 原文描述的信念正是两者相联。','C 把假装的状态误当成已经完成目标。','D 与 continue to pretend 的方向相反。'],
 ['Many people take to heart the belief that if you continue to pretend you are successful, you will eventually succeed.'],
 'take to heart','认真接受；铭记于心','描述人们相信并采纳这种说法','She took the teacher’s advice to heart.',['take advice to heart','take a belief to heart'],
 '那么，人们为什么假装幸福？当然，有句俗话叫“先装得像，直到真的做到”。许多人深信，如果持续装作成功，最终就会成功。')

add(45,'细节','Which limitation is explicitly attributed to the first iPhone?',
 ['It had no stored programmes of any kind.','It could not run even a single programme.','It could not run multiple programmes at the same time.','Its memory problem occurred only when switched off.'],2,
 '原文明示第一代 iPhone 有什么限制？',['完全没有任何已存储程序。','连一个程序也无法运行。','无法同时运行多个程序。','内存问题只在关机时发生。'],
 ['A memory problem 不等于没有任何程序。','B multiple 被偷换成 single，限制范围被扩大。','C could not run multiple programs simultaneously 直接支持。','D 没有把问题限定在关机状态。'],
 ['The first iPhone had a memory problem. It could not run multiple programs simultaneously.'],
 'simultaneously','同时地','限定不能同时运行多个程序，不是否定全部运行能力','The two teams worked simultaneously on different tasks.',['run simultaneously','occur simultaneously'],
 'Quentin Tarantino 后来编剧并执导了《低俗小说》等知名电影；当时他在加利福尼亚州曼哈顿海滩一家录像店做店员。为了获得第一份好莱坞制片助理工作，他谎称曾在电影业工作。Steve Jobs 也是先装得像，直到真正做到。第一代 iPhone 有内存问题，无法同时运行多个程序。')

add(46,'细节','How did Jobs respond when a phone crashed during the launch demonstration?',
 ['He increased that phone’s bandwidth without switching devices.','He continued using the same phone throughout every crash.','He permanently repaired the memory before continuing.','He switched to a new iPhone during the demonstration.'],3,
 '发布演示中一部手机崩溃时，Jobs 怎样应对？',['不更换设备，直接增加该机带宽。','每次崩溃后仍始终使用同一部手机。','先永久修好内存再继续。','在演示中换用一部新的 iPhone。'],
 ['A bandwidth 是另一个问题，未说换机增加带宽。','B switching to a new one 与始终同机相反。','C 演示中的换机不能改成已永久修复。','D as soon as the old one crashed 明确给出换机时机。'],
 ['Steve Jobs used multiple iPhones, switching to a new one as soon as the old one crashed during the demonstration.'],
 'bandwidth','带宽','与演示中的崩溃换机并列，属于另一个技术问题','Video calls require sufficient bandwidth.',['a bandwidth problem','limited bandwidth'],
 '第一代 iPhone 的发布会上，Steve Jobs 使用了多部 iPhone；演示中旧的一部一崩溃，他就换上一部新的。它还有带宽问题。')

add(47,'细节','What did participants evaluate after holding a pen in their mouth?',
 ['How successfully they had become popular.','How funny several cartoons were.','How often most Americans pretended to smile.','Whether their own happiness beliefs were correct.'],1,
 '参与者嘴里叼笔之后，评价了什么？',['自己变得多受欢迎。','几幅漫画有多好笑。','多数美国人多久假笑一次。','自己的幸福观是否正确。'],
 ['A 实验没有评价受欢迎程度。','B They then saw several cartoons and rated how funny they were 直接说明。','C 开头明确说对多数美国人的假设尚无定论，不能当成该实验测量。','D 实验评价漫画，不是要求判断个人幸福观正误。'],
 ['They then saw several cartoons and rated how funny they were.'],
 'mimic','模仿；模拟','用叼笔动作形成类似微笑或不微笑的表情','The exercise asks learners to mimic a speaker’s rhythm.',['mimic a smile','mimic a movement'],
 '我们并不能确定，多数美国人是否认为假装幸福就会使自己幸福。即便如此，有一个著名实验，让参与者嘴里叼着笔，以模拟微笑或不微笑。随后，他们观看几幅漫画，并评价其好笑程度。研究者的发现相当惊人。')

add(48,'细节','Which result is reported for the pen experiment in this excerpt?',
 ['The smile group received different and objectively funnier cartoons.','The non-smile group rated the same cartoons as funnier.','The smile group rated the same cartoons as funnier than the non-smile group.','The experiment compared naturally extraverted and introverted people.'],2,
 '此片段报告叼笔实验的哪个结果？',['微笑组看了不同且客观更好笑的漫画。','不微笑组认为同样的漫画更好笑。','微笑组比不微笑组认为同样的漫画更好笑。','实验比较天生外向者和内向者。'],
 ['A same cartoons 排除了材料不同的解释。','B 把两组评分方向倒置了。','C 正确保留组别、同样材料及比较方向；这是此处报告的实验结果。','D 分组根据表情条件，不是天生性格类型。'],
 ['Those in the “smile” condition rated the same cartoons as funnier than those in the non-smile condition!'],
 'condition','实验条件；实验组情境','这里指微笑条件，不是疾病或身体状况','Participants were assigned to a quiet condition or a noisy condition.',['an experimental condition','the control condition'],
 '处于“微笑”条件的参与者，认为同样的漫画比不微笑条件的参与者认为的更好笑！仅仅移动面部肌肉，使自己看起来面带笑容，就让他们更喜欢这些漫画。')

add(49,'同义改写','Which statement preserves the qualification in the passage’s conclusion?',
 ['Acting more extraverted tends to increase happiness, even if fake smiling does not.','Fake smiling and acting extraverted always have identical effects.','Every introvert becomes permanently happier after one social interaction.','Replicated findings show that all attempts to change behaviour fail.'],0,
 '哪一说法保留了本段结论的限定？',['表现得更外向通常会提升幸福，即使假笑没有这种作用。','假笑与外向行为总有完全相同的效果。','每个内向者只社交一次就永久更幸福。','重复验证证明所有改变行为的尝试都会失败。'],
 ['A tend to 保留倾向性，even if 保留与假笑的区分。','B even if...does not 不支持效果完全相同。','C every、permanently、one 都超出原句。','D 本段对外向行为给出正向倾向，不是所有尝试失败。'],
 ['So, acting like an extravert does tend to make people happier, even if fake smiling does not.'],
 'replicated','被重复验证；被重复研究得到','描述研究发现的再现，不等于每位个体都有同一效果','The finding was replicated in a second study.',['replicate a finding','replicate an experiment'],
 '这些发现已经得到重复验证。因此，表现得像个外向者，确实倾向于让人更幸福，即使假笑并不会。')

add(50,'主旨','How does the passage frame sadness, anger, and anxiety?',
 ['They invariably show that a person has failed.','They should never arise in ordinary situations.','They disappear whenever anagrams are used in experiments.','They are natural in some situations, rather than proof of failure.'],3,
 '本段怎样看待悲伤、愤怒和焦虑？',['它们无一例外说明一个人失败了。','它们不应在日常情境中出现。','只要实验采用字母重排题，它们就会消失。','它们在某些情境下很自然，并非失败的证明。'],
 ['A 作者将把不幸福视为失败称作 misconception。','B only natural 与 never arise 相反。','C 字母重排题是后文实验设置，没有消除情绪的结论。','D 前两句明确肯定这些情绪的自然性，反对失败标签。'],
 ['The key takeaway here is that it is only natural that we feel sad, angry, and anxious in some situations. Too much emphasis on happiness has led to a dangerous misconception that unhappiness is a sign of failure.'],
 'misconception','误解；错误观念','指把不幸福等同于失败的看法','It is a misconception that practice never involves mistakes.',['a common misconception','challenge a misconception'],
 '这里最重要的启示是，在某些情境中感到悲伤、愤怒和焦虑，是再自然不过的事。过分强调幸福，造成了一种危险的误解：不幸福就是失败的标志。在一项实验中，参与者被要求做字母重排题，有的承受必须快乐的压力，有的没有。')

add(51,'逻辑关系','What changes the emotional impact of the same failure?',
 ['An objectively more serious failure occurs.','Believing that one is supposed to be happy makes it feel worse.','The belief that happiness is expected removes all disappointment.','The failure becomes less important when happiness is required.'],1,
 '什么改变了同一次失败带来的情绪影响？',['失败本身客观上变得更严重。','相信自己理应快乐，会使失败感觉更糟。','认为理应幸福会消除一切失望。','要求快乐时，失败会变得更不重要。'],
 ['A same failure 明确保持失败本身相同。','B when you believe...supposed to be happy 是感觉更差的条件。','C feels worse 与消除失望相反。','D 原句说体验更糟，并非事件重要性降低。'],
 ['The same failure feels worse when you believe that you are supposed to be happy.'],
 'supposed to','被期待应当；理应','这里表示必须快乐的规范性期待','We are supposed to submit the form by Friday.',['be supposed to do','be supposed to feel'],
 '当你相信自己理应快乐时，同样的失败也会感觉更糟。')

add(52,'细节','What does the international study establish in this sentence?',
 ['Americans felt greater average pressure to be happy than the three other named groups.','Every American felt more pressure than every Japanese participant.','Germans were happier than Americans in every measured respect.','The comparison included Americans and Japanese participants only.'],0,
 '这句话中的国际研究说明了什么？',['美国人平均感到的快乐压力高于另外三个被列出的群体。','每个美国人的压力都高于每个日本参与者。','德国人在所有测量方面都比美国人幸福。','比较仅包括美国人和日本人。'],
 ['A on average 与 Japanese, Ukrainians, and Germans 明确给出平均比较及三个群体。','B 把群体平均差异扩大为每一个体的排序。','C 指标是快乐压力，不是所有方面的幸福程度。','D 遗漏了乌克兰人和德国人。'],
 ['A large international study found that Americans on average feel far more pressure to be happy than Japanese, Ukrainians, and Germans.'],
 'on average','平均而言','限定群体平均趋势，不断言每个人都如此','The journey takes forty minutes on average.',['on average','higher on average'],
 '一项大型国际研究发现，美国人平均感受到的必须快乐的压力，远高于日本人、乌克兰人和德国人。')

add(53,'细节','What additional pressure was associated with pressure to feel happy?',
 ['Pressure to feel sad and angry more frequently.','Pressure to avoid all social relationships.','Pressure not to experience sadness and anger.','Pressure to report happiness only in research settings.'],2,
 '感到必须幸福的人，还伴随着什么压力？',['更频繁地感到悲伤和愤怒的压力。','回避所有社会关系的压力。','不应体验悲伤和愤怒的压力。','只在研究场景中报告幸福的压力。'],
 ['A not to feel 将方向限定为避免这些情绪，不是增加。','B 原文没有把关系回避列为额外压力。','C also feel pressure not to feel sadness and anger 直接支持。','D 没有 only 或研究场景的限制。'],
 ['individuals who feel pressure to feel happy also feel pressure not to feel sadness and anger.'],
 'stuck','受困的；无法摆脱的','stuck in a happiness trap 比喻被快乐要求困住','The team felt stuck in an unproductive routine.',['be stuck in a trap','feel stuck'],
 '此外，这些研究者发现，感到必须幸福压力的人，也感到不应悲伤或愤怒的压力。简而言之，许多美国人被困在幸福陷阱中。')

add(54,'语境词义','In this sentence, “faces” most nearly means which of the following?',
 ['Stages.','Aspects.','Expressions.','Outcomes.'],1,
 '这句话中的“faces”最接近哪个意思？',['阶段。','方面。','表情。','结果。'],
 ['A faces 本身未表示先后阶段。','B two faces 在此比喻陷阱有两个方面。','C 不能因文中谈幸福就把抽象说法误读为面部表情。','D 原句是在划分陷阱的方面，不是在列出两个结果。'],
 ['The happiness trap has two faces.'],
 'faces','方面；面向','抽象事物的不同面向，不是字面的人脸','The report examines the two faces of urban development.',['two faces of an issue','the many faces of'],
 '幸福陷阱有两个方面。')

add(55,'主旨','How does the author characterise feeling bad after the listed events?',
 ['As proof that the person has failed at life.','As evidence that criticism is always justified.','As a feeling limited to parents and train passengers.','As a natural response to unpleasant experiences.'],3,
 '作者怎样看待列举事件后产生的难受？',['证明这个人的人生失败了。','证明批评总是合理的。','这种感受只限于父母和火车乘客。','这是对不愉快经历的自然反应。'],
 ['A It is only natural 不支持失败标签。','B 自然会难受不等于批评内容总正确。','C 举例不能变成仅有这些人会感受到。','D 后句直接用 natural 评价这些情绪反应。'],
 ['When you miss a train, when someone criticizes you, when your child shows no sign of gratitude for what you do, you feel bad. It is only natural.'],
 'gratitude','感激；感谢之情','描述孩子是否对父母所做之事表达感激','She expressed gratitude for her teacher’s patience.',['show gratitude','express gratitude'],
 '当你错过火车、被人批评，或孩子对你所做的一切毫无感激表示时，你会难受。这是再自然不过的事。')

add(56,'细节','What did the young woman do that prompted the author to thank her?',
 ['She brought him food from the Chinese restaurant.','She arranged for a door attendant to assist him.','She opened the building door for him.','She carried his meal upstairs to his flat.'],2,
 '那位年轻女子做了什么，使作者向她道谢？',['从中餐馆给他带来食物。','安排门房协助他。','为他打开楼门。','把他的饭菜送上楼。'],
 ['A 作者自己带着外卖回来，不能换成女子送餐。','B 楼内 without a door attendant，未说安排门房。','C opened the door for me 后紧接 So I said Thank you，直接对应。','D 没有替他上楼送餐的动作。'],
 ['a young woman opened the door for me. So I said, “Thank you!”'],
 'takeout','外卖食品；打包带走的饭菜','作者从餐馆带回的食物，不是女子递给他的','We ordered takeout after a long day.',['takeout food','order takeout'],
 '例如，我住在纽约市时曾多次遇到这样的经历。我住的大楼没有门房。有一天，我从附近中餐馆买了外卖回楼里，一位年轻女子为我打开门，于是我说：“谢谢！”')

add(57,'细节','At which stages of his career did the author say these experiences occurred?',
 ['Both as a graduate student and as a full professor.','Only before he began graduate school.','As a graduate student, but never as a professor.','Only after he retired from academic work.'],0,
 '作者说，这些经历发生在职业生涯的哪些阶段？',['研究生时期和正教授时期都有。','仅在开始研究生学习之前。','研究生时期有，成为教授后从未有。','仅在退出学术工作之后。'],
 ['A and...as well 明确连接两个阶段。','B when I was a graduate student 排除只在此前发生。','C 后半明确补充 full professor，不能删掉。','D 退休不在原文中。'],
 ['It happened when I was a graduate student and it happened when I was a full professor as well.'],
 'insulted','受辱的；感到被冒犯的','作者直接报告自己的感受，不是给出他人的心理诊断','She felt insulted by the dismissive remark.',['feel insulted','be insulted by'],
 '这在我读研究生时发生过，在我已成为正教授时也发生过。我感到受辱。但这种事就是会发生，对吧？')

add(58,'细节','What was the context of Kahneman’s inquiry about the author?',
 ['The author was applying to begin undergraduate study at Princeton.','Diener had applied to become a student of the author.','The author had already accepted a full professorship at Princeton.','The author had applied for an assistant professor position at Princeton.'],3,
 'Kahneman 打听作者的情况，背景是什么？',['作者正在申请普林斯顿的本科。','Diener 申请成为作者的学生。','作者已经接受普林斯顿的正教授职位。','作者申请了普林斯顿的助理教授职位。'],
 ['A fifth-year PhD student 与本科申请不符。','B Ed Diener 是作者导师，不是申请当其学生。','C had applied 不等于已接受；职位也是 assistant professor。','D At that time...assistant professor job...applied for 明确支持。'],
 ['At that time, there was an assistant professor job at Princeton that I had applied for.'],
 'advisor','导师；指导者','Ed Diener 是作者导师，Kahneman 致电向他了解作者','Her advisor helped her prepare for the interview.',['a graduate advisor','an academic advisor'],
 '说到研究生院，我读博士五年级时，导师给我讲了下面这个故事。普林斯顿的著名心理学家 Daniel Kahneman 打电话给我的导师 Ed Diener，向他打听我。当时，我申请了普林斯顿的一个助理教授职位。两人聊了一会儿后，Kahneman 问导师：“Shige 自负吗？”')

add(59,'细节','How did the advisor respond after Kahneman said survival at Princeton required being cocky?',
 ['He changed his description and called the author cocky.','He mentioned another student of his who was cocky.','He denied that Kahneman had made such a requirement.','He described Kahneman as his own cockiest student.'],1,
 'Kahneman 说在普林斯顿生存需要自负之后，导师怎样回应？',['改口说作者自负。','提到自己另一个自负的学生。','否认 Kahneman 提出过这一要求。','把 Kahneman 称为自己最自负的学生。'],
 ['A another student 不是重新评价作者本人。','B 引语 There is another student of mine who is cocky 直接支持。','C 导师没有否认对方的话，而是接着提出另一名学生。','D 混淆导师、致电者与学生的角色。'],
 ['“There is another student of mine who is cocky.”'],
 'cocky','自负的；过分自信的','对话中的人物评价，不是本段认定的录用标准真理','His cocky answer annoyed the interview panel.',['a cocky attitude','sound cocky'],
 '导师回答：“不，他不自负。”Kahneman 说：“嗯，要在普林斯顿生存，你得自负。”然后，我想，导师做了一个好导师会做的事：“我还有另一个学生，他很自负。”')

add(60,'同义改写','Which statement best preserves “not always fair”?',
 ['Every event in the world is fair.','No event in the world is ever fair.','Some events can be unfair.','Fairness can be assumed in every situation.'],2,
 '哪项改写最准确保留“not always fair”的意思？',['世界上的每件事都公平。','世界上从来没有任何公平的事。','有些事情可能不公平。','任何情境都可以假定公平。'],
 ['A always fair 与原句的否定相反。','B not always 不等于 never，不能全盘否定公平。','C 保留“并非总是”的有限否定，没有扩大成一概不公。','D every situation 抹去了原句指出的例外。'],
 ['The world is not always fair, is it?'],
 'fair','公平的；公正的','指待遇或结果的公正性，不是天气或外貌','A fair decision considers all the evidence.',['fair treatment','a fair decision'],
 '这个世界并不总是公平的，不是吗？')

add(61,'作者意图','What does the final question invite the reader to consider?',
 ['How people respond when they feel bad.','Why unfair events can never produce bad feelings.','Which country has the highest average income.','The measured success rate of one named therapy.'],0,
 '最后的问句邀请读者思考什么？',['人在难受时怎样应对。','为什么不公平事件绝不产生难受感。','哪个国家平均收入最高。','某项具名疗法测得的成功率。'],
 ['A what do you do 紧接 when you feel bad，转向应对方式。','B 第一句明确说遇到这类事件会难受。','C 本段没有国家或收入比较。','D 没有提供具名疗法或测得的比率。'],
 ['And when you feel bad, what do you do?'],
 'feel bad','感到难受；情绪不佳','这里指事件后的不愉快感受，不是道德品质差','I felt bad after the argument and took time to reflect.',['feel bad about something','feel bad after an event'],
 '当这类事件发生时，你会难受。而当你难受时，你会做什么呢？','inference')

add(62,'细节','How does the passage classify attempts to repair mood?',
 ['Exercise and hiking are described as unhealthy attempts.','Over-drinking and impulsive shopping are the healthy examples.','Everyone under pressure chooses an identical method.','People may use healthy or unhealthy methods to improve mood.'],3,
 '本段怎样区分修复心情的尝试？',['锻炼和徒步被说成不健康的尝试。','过量饮酒和冲动购物是健康例子。','每个承受压力的人都选择同样的方法。','人们可能采用健康或不健康的方法改善心情。'],
 ['A 原文将 exercise and hiking 列入 very healthy things。','B over-drinking 与 impulsive shopping 属于 very unhealthy things。','C Some...while others...明确存在不同选择。','D 同时保留两类应对，未把描述误写成推荐不健康行为。'],
 ['Some people do very healthy things, like exercise and hiking, while others do very unhealthy things, like over-drinking or impulsive shopping.'],
 'impulsive','冲动的；未经充分考虑的','修饰购物方式，不是购物一概不健康','She avoided impulsive purchases by using a list.',['impulsive shopping','an impulsive purchase'],
 '感到必须快乐压力的人，几乎什么都愿意试，以修复心情。有些人做很健康的事，例如锻炼和徒步；另一些人则做很不健康的事，例如过量饮酒或冲动购物。')

add(63,'细节','What does the author say he does if his wife is not around?',
 ['He waits for her return before doing anything.','He takes a nap.','He phones her to discuss every song.','He goes shopping instead of resting.'],1,
 '作者说，妻子不在身边时他会做什么？',['等她回来之后才采取任何行动。','小睡一会儿。','打电话和她讨论每首歌。','去购物而不是休息。'],
 ['A just take a nap 表明他会采取别的做法，不是只等待。','B If she’s not around, I just take a nap 直接回答条件对应的行为。','C 原文未提电话，也没有讨论每首歌。','D 作者在这里说的是小睡，不是购物。'],
 ['If she’s not around, I just take a nap.'],
 'sing along','跟着唱；随音乐唱','是作者自己有时采用的做法，不是实验处方','The audience began to sing along with the band.',['sing along with','sing along to a song'],
 '就我个人而言，心情低落时，我会听喜欢的歌曲。有时甚至跟着唱。有时，我会和妻子聊聊。如果她不在身边，我就小睡一会儿。')

add(64,'主旨','What does this excerpt introduce?',
 ['Categories of methods for addressing a persistent negative mood.','A claim that every negative mood lasts permanently.','The abandonment of research on emotion regulation.','One method guaranteed to work for every person.'],0,
 '这个片段引出了什么？',['处理持续负面心情的方法类别。','每种负面心情都永久持续的断言。','放弃情绪调节研究。','一个保证对每个人都有效的方法。'],
 ['A methods 与 classify...a few major categories 直接对应。','B persistent 表示持续，不等于永久，也没有 every。','C researchers classify 描述正在研究和分类，不是放弃。','D a few major categories 不是唯一方法，更没有个体保证。'],
 ['There are more sophisticated methods for dealing with a persistent, negative mood. Emotion regulation researchers classify them into a few major categories.'],
 'persistent','持续的；不易消退的','修饰负面心情，不表示永远不会改变','A persistent noise made concentration difficult.',['a persistent problem','a persistent mood'],
 '对于处理持续的负面心情，还有更精细的方法。情绪调节研究者把这些方法分成几个主要类别。')

add(65,'语境词义','What does “a tiny bump in the road” suggest about a possible future view of the event?',
 ['It will certainly feel just as painful forever.','It must literally have involved a road accident.','It might later seem like a minor obstacle.','Its importance will definitely increase over five years.'],2,
 '“道路上的一个小颠簸”暗示未来可能怎样看待这个事件？',['它一定永远同样痛苦。','事件字面上一定是交通事故。','以后它可能显得只是一个小障碍。','它的重要性在五年里必定增加。'],
 ['A might 保留可能性，也没有永远同样痛苦的断言。','B 把比喻误读为实际事故。','C tiny bump 比喻小挫折；might 保留不确定性。','D 既把程度方向颠倒，也将可能改为必定。'],
 ['In the future, this event might feel like a tiny bump in the road.'],
 'a tiny bump in the road','一个小障碍；轻微挫折','以路面颠簸比喻未来眼中或许不再重大的事件','The delayed delivery was only a tiny bump in the road for the project.',['a bump in the road','a minor bump in the road'],
 '五年之后，我还会同样痛苦吗？未来，这件事可能感觉只是道路上的一个小颠簸。','inference')

add(66,'主旨','What attitude is attributed to people who feel less pressure to be happy?',
 ['They believe negative moods never occur naturally.','They reject the possibility that time can help.','They insist on removing every bad feeling immediately.','They accept occasional bad feelings and do less to repair them.'],3,
 '本段描述，较少感到快乐压力的人持怎样的态度？',['认为负面心情绝不会自然发生。','拒绝时间可能有所帮助。','坚持立刻消除每一种难受。','接受偶尔难受，因此较少主动修复心情。'],
 ['A only natural 明确认可偶尔难受的自然性。','B They believe that time heals...与拒绝时间作用相反。','C would not do as much 与立刻消除每种情绪相反。','D think it is only natural 和 more emotional acceptance 共同支持。'],
 ['those who don’t feel pressure to feel happy would not do as much to repair a negative mood, as they think it is only natural to feel bad once in a while. Here there is more emotional acceptance.'],
 'acceptance','接纳；接受','情绪接纳指允许偶尔难受，不等于根本没有负面情绪','Acceptance of uncertainty helped her continue the task.',['emotional acceptance','acceptance of uncertainty'],
 '相比之下，不感到必须快乐压力的人，不会那么积极地修复负面心情，因为他们认为偶尔难受很自然。这里有更多情绪接纳。他们相信时间会治愈一切。而他们是对的。')

add(67,'细节','How is the psychological immune system described in the analogy?',
 ['As a biological virus produced by an unhappy thought.','As a system that activates automatically after an undesirable event.','As a deliberate technique requiring conscious practice every time.','As a system that prevents every undesirable event from happening.'],1,
 '这个类比怎样描述心理免疫系统？',['由不快乐想法产生的生物病毒。','不如意事件发生后自动启动的系统。','每次都需要有意识练习的刻意技巧。','阻止一切不如意事件发生的系统。'],
 ['A biological immune system 是类比对象，不能把情绪当实际病毒。','B automatically kicks in when...直接说明自动启动与触发条件。','C automatically 与每次必须刻意操作相反。','D after an event 的应对不能改成事前阻止所有事件。'],
 ['the psychological immune system automatically kicks in when an undesirable event happens.'],
 'kicks in','开始起作用；启动','此处指不如意事件后心理系统开始自动运作','The backup generator kicks in when the power fails.',['a system kicks in','a response kicks in'],
 '这就是 Dan Gilbert、Tim Wilson 和同事所说的“心理免疫系统”。正如病毒进入身体时生物免疫系统会启动，不如意事件发生时，心理免疫系统也会自动启动。')

add(68,'语境词义','What distinguishes a “satisficer” as defined in this passage?',
 ['Accepting any option regardless of whether it meets basic needs.','Refusing to make a choice until every alternative disappears.','Accepting a satisfactory option instead of insisting on the best.','Always choosing the option with the lowest objective quality.'],2,
 '按本段定义，“satisficer”的特点是什么？',['不管是否满足基本需要，都接受任何选项。','直到所有其他选项消失才肯选择。','接受令人满意的选项，而不坚持最优。','总选择客观质量最低的选项。'],
 ['A satisfactory 保留满足要求，不等于毫无标准地接受任何东西。','B 原文没有拖延至没有选项的条件。','C sacrifices the best choice for a satisfactory choice 是明确定义。','D 放弃追求最优不等于故意选择最差。'],
 ['a “satisficer”—one who sacrifices the best choice for a satisfactory choice'],
 'satisficer','满意即可的选择者；知足型决策者','接受符合要求的选择，而非不计代价寻找最好','A satisficer stops searching after finding a suitable flat.',['a satisficer mindset','a satisficer rather than a maximizer'],
 '幸福陷阱的第二个要素是，如果你不贪求太多幸福，它其实更容易获得。社会心理学家 Barry Schwartz 发现了“足够好”的力量。如果你经常接受“足够好”，也就是一个“满意即可者”——为令人满意的选择放弃最佳选择的人——你就更有可能满意自己的决定。假设你是高中毕业班学生。')

add(69,'细节','What decision is introduced in this hypothetical scenario?',
 ['Which college to choose.','Which high school to enter.','Which extracurricular activity to begin.','Which college course will provide the highest salary.'],0,
 '这个假设情境提出了什么决定？',['选择哪所大学。','进入哪所高中。','开始哪项课外活动。','哪门大学课程将带来最高薪水。'],
 ['A Which college do you want to go to 直接说明。','B 问的是 college，不是 high school。','C 课外活动是已做过的背景，不是问句的选择对象。','D 没有课程或薪水预测。'],
 ['Which college do you want to go to?'],
 'extracurricular','课外的','修饰课程之外的活动，不等于校外工作','She takes part in several extracurricular activities.',['extracurricular activities','an extracurricular programme'],
 '你的平均成绩几乎完美，SAT 分数很高，也参加了许多课外活动。你想去哪所大学？')

add(70,'细节','Why is the person in this example called a maximizer?',
 ['Applying to ten schools is presented as the sole universal test.','The person prefers any acceptable option over the best possible one.','The person has already been rejected by ten colleges.','The person seeks the best possible college and applies to ten schools.'],3,
 '例子中的人为什么被称为最大化选择者？',['申请十所学校被当作唯一且普遍的判定标准。','比起最好选择，此人更偏爱任何可接受选项。','此人已经被十所大学拒绝。','此人追求可能进入的最好大学，并申请十所学校。'],
 ['A 关键还包括 best possible 的目标，不能只抽取数量当普遍标准。','B 这与追求 best possible 相反。','C apply 是申请，不是已被拒绝。','D 把目标和具体申请行为一并保留，符合例子。'],
 ['You might want to go to the best possible college you could get into. So you apply to ten schools. If this is you, you are a maximizer.'],
 'maximizer','最大化选择者；追求最优的人','例子中以可进入的最好大学为目标，广泛申请','A maximizer may compare many alternatives before choosing.',['a maximizer mindset','a maximizer decision strategy'],
 '你也许想去自己可能进入的最好大学。因此，你申请了十所学校。如果这描述的就是你，你就是一个最大化选择者。')

add(71,'细节','What outcome is reported for the study featuring the college-choice scenario?',
 ['The Cornell maximizer was necessarily happier because of the school’s prestige.','The UVA satisficer was likely happier than the Cornell maximizer.','Every UVA student was happier than every Cornell student.','Decision style was absent from the comparison.'],1,
 '包含择校情境的研究报告了什么结果？',['康奈尔的最大化选择者因学校声望而必然更幸福。','弗吉尼亚大学的满意即可者可能比康奈尔的最大化选择者更幸福。','每位弗吉尼亚大学学生都比每位康奈尔学生幸福。','比较中没有涉及决策心态。'],
 ['A 将倾向改成必然，且颠倒了研究报告的方向。','B likely 保留倾向，并正确对应情境中的两类选择者。','C 情境研究不能扩大为两校所有学生的幸福排名。','D 开头明确区分 maximizer 与 satisficer。'],
 ['A study featuring a similar scenario found that the person who went to UVA was likely to be happier than the person who went to Cornell.'],
 'scenario','情境；设想的情况','研究使用类似择校情境，不是给所有学校作普遍排名','The workshop discussed a scenario involving two job offers.',['a similar scenario','a hypothetical scenario'],
 '假设一名最大化选择者进入康奈尔大学，而满意即可者去了弗吉尼亚大学。第一年结束时，谁更可能幸福？一项包含类似情境的研究发现，去了弗吉尼亚大学的人，可能比去了康奈尔大学的人更幸福。')

add(72,'逻辑关系','How do the two “If I...” statements function here?',
 ['They imagine alternative past conditions, contrasted with the satisficer’s lack of counterfactuals.','They report Yale and Princeton offers that were actually received.','They show that the UVA satisficer applied to more schools than anyone else.','They establish that no alternatives could ever be imagined.'],0,
 '两句“If I...”在这里起什么作用？',['设想不同的过去条件，与满意即可者没有反事实想法形成对照。','报告实际收到的耶鲁和普林斯顿录取。','说明弗吉尼亚大学的满意即可者比所有人申请得更多。','证明永远不可能想象其他选择。'],
 ['A If...might have 表示未发生的替代情境，后文 In contrast 转向 zero counterfactuals。','B might have gotten into 不能当成实际已录取。','C 原文说该人没有申请其他学校。','D 前两句就在想象替代情况，zero 仅修饰该例中的满意即可者。'],
 ['If I had scored 20 points higher on the SAT, I might have gotten into Yale. If I had one more extracurricular activity, I might have gotten into Princeton.','In contrast, the satisficer UVA student had zero counterfactuals'],
 'counterfactuals','反事实设想；关于另一种过去的假想','指“如果当初不同，结果可能怎样”的想法','She avoided dwelling on counterfactuals after making her choice.',['consider counterfactuals','dwell on counterfactuals'],
 '如果 SAT 再高二十分，我可能就进耶鲁了。如果再多一项课外活动，我可能就进普林斯顿了。相比之下，弗吉尼亚大学那名满意即可的学生没有反事实设想，因为此人找到了满足所有要求的学校，且没有申请其他任何学校。没有备选，没有反事实，也没有遗憾。')

add(73,'作者意图','Which approach does the author recommend in this passage?',
 ['Keep dwelling on rejection from the preferred school.','Avoid noticing positive features of the current school.','Adopt a good-enough mindset and notice what is good about the current school.','Treat entry to an elite school as a guarantee of happiness.'],2,
 '本段中，作者推荐哪种做法？',['持续想着被最想去的学校拒绝。','避免注意现在学校的优点。','采取足够好的心态，并发现当前学校的好处。','把进入名校当作幸福保证。'],
 ['A stop thinking about it 与持续反刍相反。','B start looking for what is good 正是鼓励注意优点。','C 同时保留 good-enough mindset 和对当前学校的积极关注。','D 这是 some Americans 的信念，作者随后提出不同看法。'],
 ['having a good-enough mindset is the more reliable route.','If you did not get into your top school, stop thinking about it and start looking for what is good about your current school.'],
 'Easier said than done','说起来容易，做起来难','承认建议执行有难度，不是否定建议','Changing a habit is easier said than done.',['be easier said than done','easier said than done, but'],
 '一些美国人深信，进入顶尖学校是通往幸福人生的道路；但实际上，拥有足够好的心态才是更可靠的路径。如果没有进入最想去的学校，就停止反复想着这件事，开始寻找现在学校的优点。说起来容易做起来难，但这会让你更幸福。')

add(74,'逻辑关系','How does the opening sentence connect upward social comparison with the discussion?',
 ['It says maximizing always protects people from comparing themselves with others.','It presents entrepreneurial success as making upward comparison impossible.','It treats Clark’s career as a series of business failures.','It links upward comparison to maximizing and calls it another source of unhappiness.'],3,
 '首句怎样把向上社会比较接入讨论？',['说最大化心态总能保护人不与别人比较。','把创业成功说成能使向上比较不可能发生。','把 Clark 的职业经历说成一连串商业失败。','将向上比较与最大化心态相联，称其为不幸福的另一个来源。'],
 ['A closely related 不是抵御比较。','B 原句没有说成功能消除比较。','C a series of successes 明确是成功经历。','D closely related to...another source 准确给出关联和论述作用。'],
 ['Closely related to the maximizer mindset, upward social comparison is another source of unhappiness.'],
 'upward social comparison','向上社会比较','与处于更有利位置的人相比，不是泛指所有社会互动','Upward social comparison can make an achievement feel less impressive.',['engage in upward social comparison','avoid upward social comparison'],
 '向上社会比较与最大化心态密切相关，是不幸福的另一个来源。共同创办 Netscape 的 Jim Clark，作为硅谷创业者，取得过一连串成功。')

add(75,'观点归属','Which claim is presented as a research finding rather than speculation about Clark?',
 ['Clark’s personal satisfaction was directly measured and confirmed.','People avoiding upward comparison were happier than those obsessed with comparison.','Clark was reported to be wealthier than Ellison in 2023.','Lyubomirsky and Ross studied only Clark and Ellison.'],1,
 '哪项被作为研究发现提出，而非对 Clark 的猜测？',['Clark 的个人满足感被直接测量并确认。','不做向上比较的人，比执着比较的人更幸福。','据报道，2023 年 Clark 比 Ellison 更富有。','Lyubomirsky 和 Ross 只研究了 Clark 与 Ellison。'],
 ['A I wonder 是作者的疑问，不是已测量确认。','B found that 引出这项研究发现。','C $3.8 billion 与 $158 billion 的大小方向被倒置，且数字是报道而非该研究的幸福结论。','D 研究中的 individuals 不能擅自缩成仅这两个人。'],
 ['Sonja Lyubomirsky and Lee Ross found that individuals who do not engage in upward social comparison are happier than those who are obsessed with social comparison.'],
 'net worth','净资产；资产减负债后的价值','文中财富数字属于引用的 2023 年报道，不是当前实时估值','Her net worth includes savings and property minus debts.',['an estimated net worth','increase one’s net worth'],
 '据《福布斯》报道，2023 年 Clark 的净资产是 38 亿美元，而 Larry Ellison 是 1,580 亿美元。我想知道，尽管取得巨大成功，Jim Clark 是否曾得到满足。在这一点上，研究发现非常明确。Sonja Lyubomirsky 和 Lee Ross 发现，不做向上社会比较的人，比沉迷社会比较的人更幸福。')

add(76,'主旨','What position does the passage take on avoiding upward comparison on social media?',
 ['It is difficult but possible.','It is impossible without any exception.','It is unnecessary because online images show everyone’s complete life.','It is easy because the images are randomly selected.'],0,
 '本段怎样看待在社交媒体上避免向上比较？',['困难，但可能做到。','绝无例外地不可能。','不必要，因为网上图像展示每个人的完整生活。','容易，因为这些图像随机选取。'],
 ['A It is difficult...But it is possible 同时保留难度与可能性。','B possible 明确排除绝对不可能。','C carefully curated 与完整记录不同，seems 也仅指表象。','D curated 是精心选择，不是随机；作者也没有说容易。'],
 ['It is difficult to avoid upward social comparison. But it is possible.'],
 'curated','精心挑选和编排的','描述呈现给我们的他人形象，不是未经选择的生活全貌','The exhibition contains a carefully curated selection of photographs.',['carefully curated images','a curated selection'],
 '有了社交媒体，我们不断被他人精心筛选呈现的图像轰炸。其他人似乎都正度过人生中最美好的时光！向上社会比较很难避免，但并非不可能。')

assert len(out)==45 and [q['id'] for q in out]==[f'q-c02-{n:03}' for n in range(32,77)]

def persist():
 path=ROOT/'source/short-questions/additional.json';existing=load('source/short-questions/additional.json');byid={q['id']:q for q in existing}
 for q in out:
  if q['id'] in byid:assert byid[q['id']]==q,('Refuse to overwrite changed authoring',q['id'])
  else:existing.append(q)
 path.write_text(json.dumps(existing,ensure_ascii=False,indent=2)+'\n',encoding='utf8',newline='\n')
 review=dict(batchId='batch-008',date='2026-10-22',pdfSha256=b['pdfSha256'],checkedPdfPages=list(range(18,26)),questionIds=[q['id'] for q in out],paragraphs=[dict(id=pid,textSha256=hashlib.sha256(pp[pid]['text'].encode()).hexdigest()) for pid in dict.fromkeys(q['paragraphId'] for q in out)],note='完整原页视觉复核；固定原句和短段。保留时间范围、条件及观点归属，不把文化说法当结论或群体研究当个体保证。')
 (ROOT/'source/short-questions/review-chapter-02-forty-five.json').write_text(json.dumps(review,ensure_ascii=False,indent=2)+'\n',encoding='utf8',newline='\n')
 print('Saved',len(out),'of 45 individually authored exercises')

if __name__=='__main__':persist()
