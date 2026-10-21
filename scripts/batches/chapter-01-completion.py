"""37 individually authored exercises complete Chapter 1's existing short units.
Read-only source: uploaded PDF pages 9-16, visually checked 2026-10-21.
Merge by stable ID; never overwrite unrelated or modified published exercises.
"""
from pathlib import Path
import json
ROOT=Path(__file__).resolve().parents[2]
b=json.loads((ROOT/'public/data/book.json').read_text(encoding='utf8'))
plan=json.loads((ROOT/'public/data/reading-plan.json').read_text(encoding='utf8'))
ss={s['id']:s for s in b['sentences']};pp={p['id']:p for p in b['paragraphs']};out=[]
def add(number,unit_id,kind,prompt,options,answer,prompt_zh,options_zh,analyses,quotes,word,meaning,context,example,collocations,translation,support='explicit'):
 u=next(u for u in plan['units'] if u['id']==unit_id);group=[ss[i] for i in u['sentenceIds']];p=pp[u['paragraphId']];text=p['text'][group[0]['start']:group[-1]['end']];evidence=[]
 for quote in quotes:
  offset=text.find(quote);assert offset>=0,(number,quote);start=group[0]['start']+offset;end=start+len(quote);sentences=[s for s in group if s['start']<end and s['end']>start]
  sources=list({(r['pdfPage'],r['block']):r for s in sentences for r in s['sources']}.values())
  evidence.append(dict(quote=quote,sentenceIds=[s['id'] for s in sentences],sources=sources))
 assert word.lower() in text.lower(),(number,word)
 assert len(options)==len(options_zh)==len(analyses)==4
 out.append(dict(id=f'q-c01-{number:03}',version=1,readingUnitId=u['id'],chapterId=u['chapterId'],sectionId=u['sectionId'],paragraphId=u['paragraphId'],sentenceIds=u['sentenceIds'],passage=text,prompt=prompt,options=options,answer=answer,type=kind,promptZh=prompt_zh,optionsZh=options_zh,analyses=analyses,evidence=evidence,vocabulary=[dict(word=word,meaning=meaning,context=context,example=example,collocations=collocations)],translation=translation,support=support,editorialStatus='按第 1 章 PDF 第 9–16 页具体原文编写；保持已发布短段边界；区分叙事、研究概括、比喻与引文'))

add(41,'c01-s02-p009-00982-r001-004','逻辑关系','How has the author’s response to the choice between staying and going changed?',
 ['He now finds leaving easier than he did at graduation.','He has always found the choice equally difficult.','A once straightforward choice has become increasingly difficult.','He now rejects leaving because The Clash advised him to stay.'],2,
 '作者对留下还是离开的抉择，反应发生了什么变化？',['如今离开比毕业时更容易。','他一直觉得这个抉择同样困难。','曾经简单的选择变得越来越困难。','如今他拒绝离开，因为 The Clash 劝他留下。'],
 ['A more and more difficult 表示越来越难，方向相反。','B It was easy, then 与后来的困难构成变化，并非一直如此。','C 当年 Just go 很干脆，随着年龄增长却 increasingly difficult，准确概括转折。','D 歌词只是为问题措辞；没有乐队给作者建议或作者拒绝离开的信息。'],
 ['It was easy, then. Just go. As I get older, though, it has become more and more difficult.'],
 'framed','表述；以某种方式提出','用一段歌词来表述毕业时面临的选择','The debate was framed as a choice between cost and quality.',['frame a question','be framed in terms of'],
 '我想起高中即将毕业的时候，当时面临的选择可用 The Clash 那句不朽的歌词来表达：“我该留下，还是该离开？”那时很容易：走就是了。但随着年龄增长，这个选择变得越来越困难。')

add(42,'c01-s02-p009-00982-r005-008','细节','Which priorities distinguish the two kinds of people described here?',
 ['Some favour stability, while others welcome adventure.','Some value academic research, while others reject it.','Some preserve old friendships, while others avoid friendship.','Some ask the question once, while others never ask it.'],0,
 '这里描述的两类人，在优先考虑的事情上有何不同？',['一些人倾向稳定，另一些人欢迎冒险。','一些人重视学术研究，另一些人排斥研究。','一些人维系老朋友，另一些人回避友谊。','一些人只问过一次这个问题，另一些人从未问过。'],
 ['A prioritizing a stable life 与 embracing an adventurous life 直接形成对照。','B 学术研究属于作者的经历，原文没有按是否接受研究划分两类人。','C loyal 不能扩大为另一类人拒绝所有友谊；本段未讨论交友取舍。','D many times over 强调反复思考，并非一次与从不的对比。'],
 ['Some of you might be like my father: loyal, prudent, and nostalgic, prioritizing a stable life.','Others may be more like me: impressionable, whimsical, and risk-taking, embracing an adventurous life.'],
 'prudent','审慎的；谨慎的','与忠诚、怀旧一起描述偏好稳定生活的人','A prudent traveller keeps a copy of important documents.',['a prudent decision','prudent planning'],
 '几十年来，这个问题一直处于我的个人生活和学术研究的中心。我想，你们大多数人也曾问过自己同样的问题，而且不止一两次，而是反复多次。有些人可能像父亲一样，忠诚、审慎而念旧，把稳定生活放在首位。另一些人也许更像我，易受触动、随性而愿意冒险，拥抱充满冒险的生活。')

add(43,'c01-s02-p009-03518-r002-002','作者意图','What does “first” indicate about the question “What is a good life?”?',
 ['It has already been answered conclusively.','It will replace every later question in the book.','It should be postponed until the end of the discussion.','It is a starting point the discussion needs to address.'],3,
 '“first”说明“什么是美好生活”这个问题在讨论中处于什么位置？',['这个问题已有定论。','它将取代书中所有后续问题。','应该把它推迟到讨论结束。','它是讨论首先需要处理的起点。'],
 ['A need to start with the question 是提出问题，不是宣布结论。','B start 不支持取代所有后续问题，范围被扩大。','C first 与 postponed until the end 顺序相反。','D need to start with 明确把它设为起点。'],
 ['But first we need to start with the question: What is a good life?'],
 'start with','从……开始','标明作者讨论问题的先后顺序','We should start with the most urgent task.',['start with a question','start with the basics'],
 '但首先，我们需要从这个问题开始：什么是美好的生活？')

add(44,'c01-s02-p009-05468-r001-004','作者意图','Why does the author ask about freedom and career goals?',
 ['To prove that freedom and career success are identical.','To invite consideration of possible sources of personal happiness.','To announce the measured results of a career survey.','To conclude that career goals necessarily prevent happiness.'],1,
 '作者为什么询问自由和职业目标？',['证明自由与事业成功完全相同。','邀请读者思考个人幸福可能来自哪里。','公布一项职业调查测得的结果。','断定职业目标必然妨碍幸福。'],
 ['A 两个候选例子并不表示两者完全相同。','B What makes you happy? 后面接自由和实现目标，用问题引导探索幸福来源。','C 本段没有样本、测量或调查结果，只是一组设问。','D 问句没有给出妨碍幸福的必然因果结论。'],
 ['What makes you happy? Freedom to do whatever you want to do? Pursuing and accomplishing your career goals?'],
 'accomplishing','完成；实现','与 pursuing 并列，指追求并实现职业目标','She is proud of accomplishing a difficult task.',['accomplish a goal','accomplish a task'],
 '首先，什么是个人幸福？什么使你快乐？是想做什么就做什么的自由吗？是追求并实现自己的职业目标吗？','inference')

add(45,'c01-s02-p009-05468-r005-006','细节','What example does the author give of a decision he calls selfish?',
 ['Taking his sons out of university to travel.','Refusing a job because it involved moving.','Moving to New York City for a prestigious university job.','Sending his sons to a beach resort without him.'],2,
 '作者举了哪个自称自私的决定作为例子？',['让儿子们退大学去旅行。','因为需要搬家而拒绝工作。','为了名校的一份工作搬到纽约市。','让儿子们独自去海滨度假村。'],
 ['A 儿子当时在中学阶段，原文没有退大学或旅行的事。','B 作者实际选择搬家接受工作，不是拒绝。','C including moving...to take a job 明确列举了这一决定。','D beach or spa 是前面的幸福设问，不能移作儿子的实际经历。'],
 ['I have made many selfish decisions in life, including moving to New York City to take a job at a prestigious university while my sons were still in middle and high school.'],
 'prestigious','享有声望的','描述作者接受工作的大学，未给出具体排名','She received an award from a prestigious institution.',['a prestigious university','a prestigious award'],
 '是去海滩或水疗中心一趟吗？我一生中做过许多自私的决定，其中包括在儿子们还分别读初中和高中的时候，为了到一所享有声望的大学任职而搬到纽约市。')

add(46,'c01-s02-p009-05468-r009-010','推断','Which statement preserves the author’s degree of certainty about his father’s decision?',
 ['He suggests, rather than establishes, that his father stayed to please others.','He proves that his father moved solely to earn more money.','He states that his father was unable to find work elsewhere.','He confirms that his mother ordered his father to remain.'],0,
 '哪一说法保留了作者谈论父亲决定时的确定程度？',['他提出父亲可能为了让别人幸福而留下，并未把动机确定下来。','他证明父亲搬家完全为了多赚钱。','他断言父亲无法在其他地方找到工作。','他证实母亲命令父亲留下。'],
 ['A perhaps 限定对父亲动机的解释；只能说可能，不能说已证实。','B 父亲决定留下，赚更多钱只是假设搬去城市的可能结果。','C could have made far more money 不支持找不到其他工作的说法。','D 原文没有命令或强迫的信息，把家庭考虑扩大成强制。'],
 ['My father, on the other hand, decided to stay in his hometown, perhaps to make my mother and others happy at the expense of his own happiness.','He could have made far more money if he had moved to a booming city in the same prefecture.'],
 'at the expense of','以牺牲……为代价','作者推测父亲可能为他人幸福牺牲个人幸福','We should not save time at the expense of accuracy.',['at the expense of health','at the expense of quality'],
 '另一方面，父亲决定留在家乡，也许是想以牺牲自身幸福为代价，让母亲及其他人幸福。如果搬到同一县的一座蓬勃发展的城市，他本可以赚到多得多的钱。','inference')

add(47,'c01-s02-p009-05468-r011-012','同义改写','Which paraphrase best matches the passage’s comparison of happiness-seeking strategies?',
 ['Trying to make oneself happy never succeeds.','Helping others guarantees permanent happiness for every individual.','The passage attributes happiness only to earning more money.','Seeking others’ happiness can benefit oneself, while a self-focused pursuit can fail.'],3,
 '哪一改写最符合本段对追求幸福方式的比较？',['设法让自己幸福从来不会成功。','帮助别人保证每个人永久幸福。','本段把幸福完全归因于赚更多的钱。','追求他人的幸福可以使自己受益，而只求自己幸福有时会失败。'],
 ['A sometimes fails 不能改为 never succeeds；频率被绝对化。','B permanent 和 every individual 超出了研究概括，没有终身个体保证。','C 本段列出亲社会支出、感恩信和知足心态，不是唯金钱论。','D 保留了对他人的关注能使自身受益，以及自我导向追求有时失败的对比。'],
 ['psychological research shows that trying to make others happy will make you happy, while trying to make yourself happy sometimes fails to do so.'],
 'satisficer','知足者；接受足够好结果的人','作者用 happy with good enough 解释这种心态','A satisficer may choose a suitable option without comparing every alternative.',['a satisficer mindset','a satisficer rather than a maximizer'],
 '具有讽刺意味的是，多年后，父亲似乎比我更满意自己的决定。这听起来像是中国谚语的素材，却说明了一个更普遍的道理：心理学研究显示，努力让别人幸福也会使自己幸福，而努力让自己幸福有时反而做不到。的确，心理学家发现，亲社会支出、写感恩信，以及知足者心态，也就是对足够好的结果感到满意，都能促进幸福。')

add(48,'c01-s02-p010-02895-r001-002','作者意图','What issue does the question about “a life without regrets” open up?',
 ['Whether the father has abandoned his family tradition.','Whether self-sacrifice and virtue necessarily prevent regret.','Whether the mother earned more than the father.','Whether all meaningful lives are financially successful.'],1,
 '关于“没有遗憾的人生”的设问，引出了什么问题？',['父亲是否放弃了家庭传统。','自我牺牲和美德是否一定能避免遗憾。','母亲是否比父亲挣得更多。','所有有意义的人生是否都在经济上成功。'],
 ['A 作者说把家庭传统放在自身需要之上，没有说放弃。','B But 引出疑问，检视有意义的人生是否就没有遗憾，而非直接断定。','C 本段没有比较父母收入。','D meaningful 与财务成功没有在此建立必然联系。'],
 ['But is a life of self-sacrifice and virtue—which we might call a “meaningful life”—a life without regrets?'],
 'self-sacrifice','自我牺牲','把他人的需要置于个人需要之上','Caring for the family sometimes involved self-sacrifice.',['a life of self-sacrifice','an act of self-sacrifice'],
 '也许，父亲美好生活的关键在于，他决定把别人的需要——母亲以及家庭传统——放在自身需要之上。但一种充满自我牺牲和美德、我们或许称为“有意义”的人生，就是没有遗憾的人生吗？','inference')

add(49,'c01-s02-p010-02895-r005-005','逻辑关系','What possible cost of self-sacrifice is identified in this sentence?',
 ['Missed opportunities may later become sources of regret.','Virtue invariably makes people financially poorer.','Every sacrifice leads to immediate public criticism.','Regret disappears once a person gives up opportunities.'],0,
 '这句话指出自我牺牲可能付出什么代价？',['错过的机会日后可能成为遗憾的来源。','美德必然使人更贫穷。','每次牺牲都会立刻招致公开批评。','一旦放弃机会，遗憾就会消失。'],
 ['A forgo opportunities 与 ultimately...more regrets 直接建立潜在代价的联系，may 保留可能性。','B 没有谈收入，invariably 也把可能性改成必然。','C public criticism 不在原文中，且每次、立刻都无依据。','D 原文说可能带来更多遗憾，并非消除遗憾。'],
 ['Some people may lead a life of self-sacrifice and virtue but forgo opportunities that ultimately lead to more regrets and “what ifs.”'],
 'forgo','放弃；舍弃','主动或因选择而放弃潜在机会','He chose to forgo a promotion to remain near his family.',['forgo an opportunity','forgo a benefit'],
 '有些人或许过着自我牺牲、充满美德的生活，却放弃了机会，最终因此多了遗憾和“要是当初……”的追问。')

add(50,'c01-s02-p010-02895-r007-008','细节','How is Nel Wright’s choice used to illustrate the idea in this passage?',
 ['She rejects family expectations to pursue childhood adventures.','Her life provides experimental proof that marriage causes regret.','She sets aside adventurous dreams to meet expectations of being a wife and mother.','She persuades Sartre to change his definition of authenticity.'],2,
 '本段怎样通过 Nel Wright 的选择来举例？',['她拒绝家庭期待，追逐儿时冒险梦想。','她的人生提供了婚姻导致遗憾的实验依据。','她搁置冒险梦想，去符合妻子和母亲角色的期待。','她说服萨特改变真实生活的定义。'],
 ['A 她 puts aside 梦想并遵从家人期待，方向正好相反。','B Sula 是小说；人物例子不能改写为婚姻因果实验。','C puts aside...to seek perfection...just as her family expects 明确支持。','D 没有两人交流或哲学家改定义的信息。'],
 ['An example is found in Toni Morrison’s novel Sula, where Nel Wright puts aside her childhood dreams of adventure to seek perfection in her role as a wife and mother, just as her family expects of her.'],
 'puts aside','搁置；放在一边','Nel 暂置或放弃冒险梦想以履行家庭角色','She put aside her travel plans while caring for a relative.',['put aside a dream','put aside personal ambitions'],
 '法国哲学家让-保罗·萨特会把这种人生称为“自欺”的人生。托妮·莫里森的小说《秀拉》里有一个例子：Nel Wright 搁置了儿时冒险的梦想，转而追求在妻子和母亲的角色上做到完美，正如家人对她的期待。')

add(51,'c01-s03-p011-01650-r001-004','主旨','Why does Sacks’s life present a “quandary” for the author?',
 ['It was entirely free of emotional struggle.','It was admirable only because of financial success.','It shows that exploration necessarily cures depression.','Its admirable qualities are not fully captured by happiness or self-sacrifice.'],3,
 '为什么 Sacks 的人生使作者感到现有概念难以解释？',['他完全没有情绪困扰。','他的人生只因财务成功而值得钦佩。','它说明探索必定能治愈抑郁。','幸福或自我牺牲都不能完整概括其中令人钦佩的品质。'],
 ['A 原文明确有 depression 和 long period of inner struggle。','B 本段没有以金钱解释他的人生价值。','C 有抑郁仍探索不等于探索治愈抑郁，不能倒置为医疗因果。','D Neither...nor...fully capture 是核心判断；苦难与探索并存，使现有两类概念不足。'],
 ['He had depression and a long period of inner struggle, yet he kept exploring new frontiers.','Neither personal happiness and contentment nor self-sacrifice and virtue fully capture what was so admirable about Sacks’s life.'],
 'quandary','难题；困惑的处境','指如何用现有美好生活概念解释 Sacks 的人生','The unexpected result left the team in a quandary.',['be in a quandary','present a quandary'],
 'Oliver Sacks 的故事提出了一个难题。他患有抑郁，也经历了长期内心挣扎，却一直探索新的领域。他在 2015 年出版的自传恰如其分地题为《On the Move: A Life》。个人幸福与满足，或自我牺牲与美德，都无法充分概括 Sacks 的人生何以如此令人钦佩。')

add(52,'c01-s03-p011-01650-r005-005','细节','Who does the sentence credit with choosing the term “a psychologically rich life”?',
 ['Oliver Sacks and his publisher.','The author and his students.','The author’s father and neighbours.','An unnamed group of philosophers.'],1,
 '这句话把“心理丰富的人生”这一术语的选定归于谁？',['Oliver Sacks 和他的出版商。','作者及其学生。','作者的父亲和邻居。','一群未具名的哲学家。'],
 ['A 本句没有给 Sacks 或出版商归属。','B my students and I 明确指作者与自己的学生。','C 父亲和邻居没有出现在这句话中。','D my students 不能换成未具名哲学家。'],
 ['We need a new term, one my students and I have decided to call a psychologically rich life.'],
 'term','术语；名称','此处为一种人生维度取名，不指学期或期限','The researchers introduced a term for the new pattern.',['introduce a term','use the term'],
 '我们需要一个新术语，我和学生决定把它称为心理丰富的人生。')

add(53,'c01-s03-p011-03795-r008-009','同义改写','What does the phrase “a distinct multitude of flavors” suggest here?',
 ['A life containing a varied collection of experiences.','A diet made up mainly of different chocolates.','A life defined by repeatedly having one pleasant feeling.','A method of measuring food preferences over time.'],0,
 '“a distinct multitude of flavors”在这里暗示什么？',['一种由多样经历构成的人生。','一种主要由不同巧克力构成的饮食。','一种由反复体验单一愉快感受定义的人生。','一种长期测量食物偏好的方法。'],
 ['A 后句明确 rich in terms of life experiences，flavors 借指不同经历的丰富滋味。','B 把比喻中的风味当成实际饮食，偏离 life experiences。','C multitude 表示多种，不能缩减为单一感受的重复。','D 本段没有测量食物偏好的研究方法。'],
 ['Over time, the accumulation of psychologically rich experiences makes for a psychologically rich life, one with a distinct multitude of flavors.','A psychologically rich life is, well, rich in terms of life experiences.'],
 'accumulation','积累；累积','经历随着时间增多，共同构成人生的丰富性','The accumulation of small discoveries changed her perspective.',['the accumulation of experiences','gradual accumulation'],
 '随着时间推移，心理丰富的经历不断累积，造就了一种心理丰富的人生，其中有着独特而多样的滋味。所谓心理丰富的人生，丰富的正是人生经历。','inference')

add(54,'c01-s03-p011-05745-r001-002','作者意图','Why does the author introduce a detour into research history?',
 ['To abandon the question of why a new term is needed.','To argue that research on the good life has ended.','To explain the need for the new term through three research phases.','To rank three phases by the happiness of their researchers.'],2,
 '作者为什么转向回顾研究史？',['放弃解释为什么需要新术语。','宣称关于美好生活的研究已经结束。','通过三个研究阶段解释为什么需要新术语。','按研究者的幸福程度给三个阶段排名。'],
 ['A To explain why 直接说明仍在回答原问题。','B 历史回顾不表示研究终结。','C To explain why 与 three phases 给出目的及组织框架。','D phases 是历史划分，不是按研究者幸福程度排序。'],
 ['But why do we need this new term? To explain why, let’s take a slight detour into the history of psychological research on the good life, which I think of as having three phases.'],
 'detour','绕行；暂时转向旁支话题','暂时回顾研究史以帮助解释当前概念','The lecture took a brief detour into the history of the problem.',['take a detour','a brief detour into'],
 '但为什么需要这个新术语呢？为了解释这一点，让我们稍稍绕个弯，回顾心理学关于美好生活的研究史；在我看来，这段历史可以分为三个阶段。')

add(55,'c01-s03-p011-06802-r001-002','细节','Which detail about Ed Diener is explicitly stated?',
 ['He coined the term psychological richness in 1984.','He was the author’s graduate advisor and published “Subjective Well-Being” in 1984.','He was the only researcher who had ever studied happiness.','He supervised the author’s high-school studies.'],1,
 '关于 Ed Diener，哪项细节在原文中明确出现？',['他在 1984 年创造了心理丰富这一术语。','他是作者的研究生导师，并于 1984 年发表《Subjective Well-Being》。','他是唯一研究过幸福的人。','他指导作者的高中学习。'],
 ['A 1984 年对应论文发表时间，不是创造心理丰富术语的时间。','B graduate school advisor 以及论文名与年份都直接吻合。','C one of the first 不等于唯一一位，范围被缩小成排他断言。','D graduate school 是研究生阶段，不是高中。'],
 ['Ed Diener, my graduate school advisor, was one of the first researchers to study happiness.','He published a paper entitled “Subjective Well-Being” in 1984.'],
 'entitled','题为；名为','说明论文标题，不是在谈享有某种权利','She wrote an article entitled “Learning through Travel.”',['a paper entitled','a book entitled'],
 '我的研究生导师 Ed Diener 是最早研究幸福的学者之一。他在 1984 年发表了一篇题为《Subjective Well-Being》的论文。')

add(56,'c01-s03-p011-06802-r004-004','细节','What was positive psychology based on, according to this sentence?',
 ['Happiness research alone, excluding all related topics.','The study of material wealth rather than psychological states.','Only the study of psychological illness and its treatment.','The study of happiness together with topics such as hope, optimism, and flow.'],3,
 '根据这句话，积极心理学建立在什么研究基础上？',['只有幸福研究，排除一切相关主题。','物质财富研究，而非心理状态研究。','只有心理疾病及其治疗研究。','幸福研究，以及希望、乐观、心流等相关主题的研究。'],
 ['A as well as 明确把其他相关主题纳入，不能删除。','B 本句列的是心理主题，没有以财富取代它们。','C 疾病治疗没有出现在列举中，only 也缺乏支持。','D 完整对应 happiness as well as...hope, optimism, and flow。'],
 ['Martin Seligman and Mihaly Csikszentmihalyi then built and popularized positive psychology based on the study of happiness as well as other related topics like hope, optimism, and flow.'],
 'popularized','使普及；推广','指把积极心理学传播给更广泛的人群','Her articles popularized a complex scientific idea.',['popularize an idea','popularize a field'],
 '随后，Martin Seligman 和 Mihaly Csikszentmihalyi 以幸福以及希望、乐观、心流等相关主题的研究为基础，建立并推广了积极心理学。')

add(57,'c01-s03-p012-02392-r001-001','细节','Which combination belongs to Carol Ryff’s alternative model described here?',
 ['Autonomy, purpose, and personal growth.','Income, fame, and physical comfort.','Obedience, competition, and career status.','Pleasure, entertainment, and freedom from all duties.'],0,
 '哪组要素属于这里描述的 Carol Ryff 的替代模型？',['自主性、目标感和个人成长。','收入、名气和身体舒适。','服从、竞争和职业地位。','愉悦、娱乐和免除所有责任。'],
 ['A 三项均出现在六项清单中，是 autonomy、purpose、personal growth。','B 清单没有收入、名气或身体舒适。','C 服从不能替代自主性，竞争与地位也不在清单中。','D 把模型改成娱乐和免除责任，与原文六项不符。'],
 ['an alternative model of a good life that focused on autonomy, self-acceptance, purpose, positive relations, environmental mastery, and personal growth.'],
 'autonomy','自主性；自我决定能力','Ryff 模型列出的一个维度，并非免除全部责任','The course gives learners greater autonomy over their schedules.',['personal autonomy','develop autonomy'],
 '随后在 1989 年，Carol Ryff 发表了题为《Happiness Is Everything, or Is It?》的论文，提出一种关于美好生活的替代模型，关注自主性、自我接纳、目标感、积极关系、环境掌控和个人成长。')

add(58,'c01-s03-p012-04612-r001-004','逻辑关系','What distinction is illustrated by the comparison between work and a break?',
 ['Workers are less engaged during work and happier during work.','Having an easy life necessarily makes life meaningful.','Greater happiness during breaks can coexist with greater engagement during work.','Work and breaks have identical effects on happiness and engagement.'],2,
 '工作与休息的比较说明了什么区别？',['工作时投入更少，而且更幸福。','生活轻松必然使人生有意义。','休息时更幸福可以与工作时更投入同时存在。','工作和休息对幸福与投入的作用完全相同。'],
 ['A 两项都与原文方向不符：休息时更幸福，工作时更投入。','B don’t necessarily say...meaningful 明确否定这种必然推导。','C 分别保留 happier during a break 与 more engaged during the work，不混同两个指标。','D 原文用 However 区分二者，不是作用相同。'],
 ['Workers are happier during a break than during work. However, they feel more engaged during the work than during the break.'],
 'engaged','投入的；专注参与的','这里指在工作活动中的投入，不等同于幸福感','The discussion kept the students deeply engaged.',['feel engaged','engaged in an activity'],
 '过去二十年里，幸福研究者一直在争论享乐式幸福与实现式幸福的相对重要性。例如，说自己生活轻松的人，往往也说自己幸福，却不一定说人生有意义。工作者在休息时比工作时更幸福。然而，他们在工作时比休息时感觉更投入。')

add(59,'c01-s04-p013-00982-r001-001','细节','What has been disputed among the researchers described in this sentence?',
 ['Whether either happiness or meaning can ever be studied.','Which matters more: happiness or meaning.','Whether all people define happiness identically.','Which research method measures wealth most accurately.'],1,
 '这句话中的研究者在争论什么？',['幸福或意义究竟能否被研究。','幸福和意义，哪一个更重要。','所有人对幸福的定义是否完全一样。','哪种研究方法能最准确地测量财富。'],
 ['A 原文说研究者争论相对重要性，没有否定研究本身的可能。','B relative importance 与 one is more important than the other 明确指向重要性比较。','C 没有讨论所有人的定义是否一致。','D 既没有财富测量，也没有比较研究方法。'],
 ['Well-being researchers have debated the relative importance of happiness vs. meaning, arguing that one is more important than the other.'],
 'relative importance','相对重要性','比较幸福和意义彼此的分量，而非各自的绝对数值','The report considers the relative importance of cost and reliability.',['assess relative importance','the relative importance of two factors'],
 '幸福研究者一直在争论幸福与意义的相对重要性，主张其中一个比另一个更重要。')

add(60,'c01-s04-p013-00982-r008-008','细节','Which belief is singled out as relevant to predicting intelligence and performance?',
 ['The belief that intelligence is determined entirely by income.','The belief that all people have already reached their potential.','The belief that performance cannot be studied scientifically.','The belief that intelligence can be improved.'],3,
 '哪种观念被特别指出与预测智力和表现有关？',['智力完全由收入决定。','所有人都已经达到自己的潜能上限。','人的表现无法得到科学研究。','智力可以得到提高。'],
 ['A 原文没有提到收入，更没有收入完全决定智力的结论。','B 原文关注能否提高，而非人人都已达到上限。','C 句子实际讨论预测智力和表现，并不否定科学研究。','D whether we believe that intelligence can be improved 直接限定所谈观念。'],
 ['whether we believe that intelligence can be improved—is also important in predicting intelligence and human performance'],
 'predicting','预测','此处说观念对预测表现有重要性，不等于独自决定表现','Past practice can be useful in predicting future performance.',['predict performance','predict an outcome'],
 '她指出，我们如何看待自己的智力——具体说，是否相信智力可以提高——对于预测智力和人的表现也很重要。')

add(61,'c01-s04-p013-03322-r001-004','细节','Why did the author initially suggest hiring someone to repair the window?',
 ['He regarded himself as unskilled at practical repairs.','His son had already repaired every window in the house.','His wife wanted to replace the entire Victorian house.','The windows had never used sash cords.'],0,
 '作者最初为什么建议请人修窗户？',['他认为自己不擅长动手维修。','儿子已经修好了房子里的每扇窗。','妻子想更换整座维多利亚式房子。','窗户从未使用过窗绳。'],
 ['A I’m not handy 是作者紧接雇人建议给出的理由，指不善于动手。','B 本段没有儿子已完成维修的经历。','C 妻子要求修坏掉的窗绳，不是更换房子。','D still operated with sash cords 明确说这些窗仍使用窗绳。'],
 ['I answered, “We should just hire someone. I’m not handy.”'],
 'handy','善于动手的；擅长维修的','作者否定自己具备修窗这类实际技能','My neighbour is handy with tools and repaired the shelf.',['be handy with tools','a handy person'],
 '有一天吃晚饭时，妻子问我能否修好客厅里坏掉的窗绳；我们那座十九世纪末的维多利亚式住宅仍保留原装的上下推拉窗，靠窗绳操作。我回答：“直接请人来吧。我不擅长动手。”当时读初中的二儿子立刻回应：“爸爸，那是固定型思维！')

add(62,'c01-s04-p013-03322-r005-006','同义改写','What idea is expressed by “You can get better!”?',
 ['Improvement is possible only outside school.','A person’s present skill level can never change.','A person can develop abilities rather than remain at the current level.','Learning about a mindset guarantees immediate expert performance.'],2,
 '“You can get better!”表达了什么想法？',['只有在校外才可能进步。','一个人当前的技能水平永远不能改变。','人的能力可以发展，并非只能停留在当前水平。','学到一种思维模式便保证立刻成为专家。'],
 ['A 后句明说在学校学到成长型思维，且没有 only outside school 的限制。','B can get better 与永不能改变相反。','C 保留 can 的可能性，准确改写能力可发展的意思。','D can 不是保证，get better 也不是立刻成为专家。'],
 ['You can get better!” It turned out he had just learned about Dweck’s growth mindset in school.'],
 'turned out','结果发现；原来','作者解释儿子鼓励背后的学习来源','It turned out that she had already studied the topic.',['it turned out that','turn out to be'],
 '你能做得更好！”原来，他刚在学校里学到了 Dweck 的成长型思维。')

add(63,'c01-s04-p013-03322-r008-008','作者意图','How does the author use the analogy with the growth mindset?',
 ['To claim that psychological richness has already replaced intelligence research.','To express hope that psychological richness will expand the idea of a good life.','To show that growth mindset and psychological richness are identical measures.','To prove that every new concept immediately improves everyone’s life.'],1,
 '作者怎样运用与成长型思维的类比？',['断言心理丰富已取代智力研究。','表达心理丰富有望拓展美好生活概念的期待。','说明成长型思维和心理丰富是同一个指标。','证明每个新概念都会立刻改善所有人的生活。'],
 ['A 没有替代智力研究的说法，只是在两种概念作用之间作类比。','B I hope 明确表明期待，reveal a new dimension 指拓展对美好生活的理解。','C 类比功能不等于两个概念或测量完全相同。','D I hope 不能改成已证明；every、immediately、everyone 均超出原句。'],
 ['Just as the growth mindset revealed a new dimension of human intelligence and ability, I hope that psychological richness can reveal a new dimension of a good life.'],
 'dimension','维度；方面','指理解美好生活时新增的方面，而非空间尺寸','The interview added a new dimension to the discussion.',['a new dimension','reveal another dimension'],
 '正如成长型思维揭示了人类智力和能力的一个新维度，我希望心理丰富也能揭示美好生活的一个新维度。')

add(64,'c01-s04-p013-05662-r001-004','主旨','Which feature of happiness is introduced by the balloon comparison?',
 ['It grows permanently whenever a person has a new experience.','It measures the social impact of a person’s work.','It can be assessed only by observing physical balloons.','It is a subjective feeling that rises and falls.'],3,
 '气球的比较首先引出了幸福的哪种特征？',['每有新经历就会永久增长。','它衡量一个人工作的社会影响。','只有观察真实气球才能评估它。','它是一种会起伏的主观感受。'],
 ['A 原文明确 rises and falls，不是只增不减的永久累积。','B 本段定义的是主观感受，没有将其定义为工作影响。','C 气球是比喻，不是实际测量工具。','D subjective feeling 与 rises and falls 是文中的直接定义。'],
 ['happiness is a subjective feeling that rises and falls to indicate where one’s life stands. It is a bit like a balloon.'],
 'subjective','主观的','幸福被描述为个人感受到的状态，而非客观财富总数','Comfort is partly a subjective judgement.',['a subjective feeling','subjective well-being'],
 '那么，心理丰富与幸福和意义有什么不同？本书主体会详细回答这个问题，表 1 则提供简要总结。不过，简而言之，幸福是一种会上下起伏、反映人生当前处境的主观感受。它有点像气球。')

add(65,'c01-s04-p013-05662-r005-008','逻辑关系','What change is marked by “But” in the balloon image?',
 ['The balloon becomes unaffected by its surroundings.','Bad weather is presented as the cause of smooth sailing.','Favourable conditions keep it high, whereas bad weather makes it deflate.','The passage shifts from a metaphor to results of a weather experiment.'],2,
 '气球意象中的“But”标记了什么变化？',['气球不再受周围环境影响。','坏天气被说成是一帆风顺的原因。','有利条件使它高高飘起，而坏天气使它瘪下来。','从比喻转为报告天气实验结果。'],
 ['A 天气改变状态，说明仍受环境影响。','B Smooth sailing 位于好条件下，把因果方向与条件对错了。','C right wind and air pressure 与 bad weather 对照，floats high 转为 deflates。','D 全段仍在展开气球意象，没有实验数据或方法。'],
 ['With the right wind and air pressure, it floats high. Smooth sailing. Life is going well. But when the weather is bad, it deflates.'],
 'deflates','泄气；瘪下来','气球意象中由高涨转为低落的状态变化','The balloon slowly deflates when air escapes.',['a balloon deflates','deflate a balloon'],
 '在合适的风和气压下，它会高高飘起。一帆风顺，生活进展良好。但天气不好时，它就瘪了下来。')

add(66,'c01-s04-p013-05662-r009-010','语境词义','In these short statements, what does “Grounded and stuck” convey?',
 ['A state of being held down and unable to progress.','A feeling of rapid and effortless progress.','A successful arrival at a planned destination.','A decision to begin a new research project.'],0,
 '在这两句短句中，“Grounded and stuck”表达什么状态？',['被困住、难以前进的状态。','迅速而轻松地向前发展的感受。','成功抵达预定目的地。','决定开始一个新的研究项目。'],
 ['A 与后句 Life is not going well 相呼应，grounded、stuck 共同表达受阻。','B 与 stuck 及 not going well 相反。','C 到达目的地的成功结果并未出现。','D 没有研究计划或新决定，属于无依据添加。'],
 ['Grounded and stuck. Life is not going well.'],
 'stuck','困住的；停滞不前的','与 grounded 并列，形容生活受阻的感受','She felt stuck and unsure how to move forward.',['feel stuck','get stuck'],
 '落在地上，动弹不得。生活并不顺利。')

add(67,'c01-s04-p014-03090-r002-005','逻辑关系','When does the passage say it becomes harder to see the point of one’s life?',
 ['Whenever a person begins to care about the world.','When one’s efforts do not seem to make a clear difference.','Only after every long-term goal has been achieved.','As soon as one sees the fruits of one’s labour.'],1,
 '本段说，什么时候会更难看清人生的意义所在？',['只要开始关心世界时。','当自己的努力似乎没有带来明确改变时。','只有在所有长期目标都达成以后。','一看到劳动成果时。'],
 ['A devoted to making a difference 对应人生有意义，而非看不清意义。','B when your efforts are not making a clear difference 是后句明确给出的条件。','C 原文没有所有目标达成这一前提，only 也无支持。','D fruits of your labor 出现在能看到意义的一侧，方向相反。'],
 ['But when your efforts are not making a clear difference, it is harder to see the point of your life.'],
 'fruits of your labor','劳动成果；努力的收获','这里指看得见的贡献与遗产，不是字面水果','After years of training, she could see the fruits of her labor.',['see the fruits of your labor','enjoy the fruits of your labor'],
 '当你致力于为世界带来改变时，你的人生当然有其意义。你看得到自己的劳动成果、留下的影响。你的存在有了理由。但当努力没有带来明确改变时，人生的意义就更难看清了。')

add(68,'c01-s04-p014-03090-r006-008','作者意图','What role does the imagined breakup play in this passage?',
 ['It reports a verified event in the singer’s biography.','It proves that romantic love always leads to failure.','It describes the results of a controlled relationship study.','It illustrates hypothetically how relationship-based meaning could feel lost.'],3,
 '本段设想的分手起到什么作用？',['报告歌手生平中已经核实的事件。','证明爱情总是导致失败。','描述一项受控关系研究的结果。','以假设说明，依托一段关系的意义可能怎样失落。'],
 ['A Imagine 明确要求想象，不能当作已核实传记事实。','B 一种假设情境不能推出所有爱情都会失败。','C 歌曲与想象的例子不是对照实验。','D Imagine 加 would 标记假设，用于展示关系破裂时意义感可能受损。'],
 ['Imagine that he broke up with this woman. His dedication would be wasted, and his life would feel pointless.'],
 'pointless','无意义的；徒劳的','描述在设想情境中失去关系寄托后的主观感受','Without a clear purpose, the exercise seemed pointless to him.',['feel pointless','a pointless task'],
 '苏格兰创作歌手 Lewis Capaldi 在《Pointless》中唱道：“在我追逐的所有梦想中……没有你，一切都毫无意义。”设想他与这名女子分手：他的投入就会付诸东流，他的人生也会感觉失去了意义。','inference')

add(69,'c01-s04-p014-04650-r005-006','语境词义','What does “precariousness” most nearly mean in this closing phrase?',
 ['The mathematical precision of meaning.','The unchangeable permanence of meaning.','The instability or vulnerability of meaning.','The complete absence of meaning in every life.'],2,
 '结尾短语中的“precariousness”最接近什么意思？',['意义的数学精确性。','意义永不改变的持久性。','意义的不稳定性或脆弱性。','每个人的人生都完全没有意义。'],
 ['A precariousness 不表示精确，短语也不涉及数学度量。','B 不稳定与永久不变相反。','C 词义指缺乏稳固保障、可能动摇或失落。','D 脆弱不等于完全不存在，every life 也扩大了范围。'],
 ['So it goes. The precariousness of meaning.'],
 'precariousness','不稳定性；脆弱性','强调意义感可能摇动，而非宣称所有意义都不存在','The incident exposed the precariousness of their financial position.',['the precariousness of meaning','the precariousness of a situation'],
 '事情就是如此。这便是意义的脆弱性。')

add(70,'c01-s05-p015-01260-r001-003','主旨','What distinguishes psychological richness in this passage?',
 ['It concerns accumulated experiences rather than an overall feeling or life’s point.','It is measured only by the amount of money a person earns.','It requires all experiences to produce the same pleasant feeling.','It is defined as having a single unchanging purpose throughout life.'],0,
 '本段用什么特征区分心理丰富？',['它关注积累的经历，而非总体感受或人生目的。','它只用一个人挣多少钱来衡量。','它要求一切经历都带来同一种愉悦感受。','它被定义为终身拥有一个不变的目标。'],
 ['A not about...but about...the accumulation of experiences 明确给出区分标准。','B 钱用于类比物质丰富，心理丰富对应的是经历，不是收入。','C interesting experiences and stories 没有限制为同一种愉悦。','D 作者正把它与 what the point of your life is 区分，不能重新定义为单一目标。'],
 ['it is not about an overall feeling of where life is going or what the point of your life is, but about an experience, or more precisely the accumulation of experiences over time.','The more interesting experiences and stories you have, the more psychologically rich you are.'],
 'quantified','量化；以数量表示','作者把经历与金钱作类比，说明丰富可以累积，并未在此提供统一计分公式','The benefits cannot always be quantified in a single number.',['be quantified by','quantify an effect'],
 '心理丰富不同于幸福和意义：它关注的不是人生走向的总体感受，也不是人生的目的，而是经历，更准确地说，是随着时间累积的经历。正如物质丰富可以用金钱量化——钱越多，物质上越富有——心理丰富也可以用经历来量化。有趣的经历和故事越多，心理上就越丰富。')

add(71,'c01-s05-p015-01260-r004-004','逻辑关系','What relationship does the sentence establish between wealth and experiences?',
 ['Wealth is required before experiences can accumulate.','Both can accumulate, contributing to different kinds of richness.','Experiences can replace money in every financial transaction.','Accumulating wealth prevents psychological richness.'],1,
 '这句话在财富与经历之间建立了什么关系？',['必须先有财富，经历才能积累。','二者都可以积累，分别形成不同的丰富。','经历能在所有金融交易中取代金钱。','积累财富会阻止心理丰富。'],
 ['A 类比两种积累方式，没有先决财富条件。','B Just as...you can... 把财富累积与经历累积并列，分别对应物质和心理丰富。','C 这是类比，不是把经历当成实际货币。','D 句子没有两者互斥或阻碍的因果关系。'],
 ['Just as you can accumulate wealth and become materially rich, you can accumulate experiences and become psychologically rich.'],
 'accumulate','积累；逐渐增多','这里分别用于财富和经历，强调随时间增加','Travellers accumulate memories from the places they visit.',['accumulate wealth','accumulate experiences'],
 '正如你可以积累财富而变得物质富有，你也可以积累经历而变得心理丰富。')

add(72,'c01-s05-p015-04972-r001-002','细节','Who is described as better suited to a psychologically rich life?',
 ['Everyone, equally and without exception.','Only people who have accumulated great wealth.','People who are satisfied with never exploring anything new.','Curious people, more than people who are already content.'],3,
 '原文说，什么人更适合心理丰富的人生？',['每个人都完全一样，毫无例外。','只有积累了巨额财富的人。','满足于永远不探索新事物的人。','比起已感到满足的人，更适合好奇的人。'],
 ['A not for everyone 否定了无差别适合所有人的断言。','B 没有财富门槛或 only 限制。','C 把 content 一侧反说成了更适合。','D suits the curious more than the content 是原句的直接比较。'],
 ['A psychologically rich life is not for everyone. It suits the curious more than the content.'],
 'content','满足的；满意的','the content 指感到满足的一类人，此处不是“内容”这个名词','He felt content with a quiet evening at home.',['feel content','be content with'],
 '心理丰富的人生并不适合每个人。比起已感满足的人，它更适合充满好奇的人。')

add(73,'c01-s05-p015-04972-r004-004','逻辑关系','What paradox does the sentence identify?',
 ['Happiness and meaning necessarily eliminate every regret.','Unanswered questions always lead immediately to happiness.','The complacency encouraged by happiness and meaning can leave life incomplete.','Meaning is possible only when a person rejects happiness altogether.'],2,
 '这句话指出了什么悖论？',['幸福和意义必然消除所有遗憾。','未解问题总会立刻带来幸福。','幸福和意义促生的自满，可能使人生仍不完整。','只有彻底拒绝幸福才可能有意义。'],
 ['A 原文说 can...major regrets，与消除所有遗憾相反。','B 未解问题是这种不完整生活的表现，不是必然立刻幸福的原因。','C 保留 can 的可能性，并准确连接 complacency 与 incomplete life。','D 没有二者必须互斥或彻底拒绝幸福的条件。'],
 ['Yet the paradox of happiness and meaning is that the complacency they foster can make for an incomplete life with major regrets, doubts, and unanswered questions.'],
 'complacency','自满；安于现状','这里指可能减少探索、使遗憾和疑问留下的满足状态','Early success can lead to complacency if a team stops learning.',['lead to complacency','avoid complacency'],
 '然而，幸福与意义的悖论在于，它们所滋生的自满可能造成人生的不完整，留下重大的遗憾、怀疑和未解的问题。')

add(74,'c01-s05-p015-04972-r006-007','推断','Which conclusion stays within the passage’s claims about seeking new experiences?',
 ['It may help reduce regrets, but a regret-free life is expressed as a hope.','It guarantees that no reader will ever regret a decision.','It matters only after a person has reached every destination.','It requires abandoning the search for new knowledge.'],0,
 '关于寻求新经历，哪个结论没有超出本段的说法？',['它可能有助于减少遗憾，但完全没有遗憾仍是一种期待。','它保证所有读者永远不后悔任何决定。','只有达成所有目的地以后，它才重要。','它要求放弃探索新知识。'],
 ['A hopefully 和 or at least fewer regrets 保留期待和较弱结果，没有保证。','B guarantees、no reader、ever 把期待夸大成无例外的终身保证。','C not just the destination but also the journey 表明过程也重要，并非达成后才重要。','D 原文同时鼓励 new experiences 和 new knowledge，不能删去后者。'],
 ['By reminding ourselves that what counts is not just the destination but also the journey, we learn to find value in seeking new experiences and new knowledge, hopefully leading to a life without regrets, or at least fewer regrets.'],
 'what counts','真正重要的事','强调人生的过程与目的地同样值得关注','What counts is whether we learn from the experience.',['what really counts','what counts most'],
 '因此，任何人都可以从心理丰富研究的启示中受益。提醒自己重要的不只是目的地，还有旅程本身，我们便能学着在寻求新经历和新知识中发现价值，希望由此过上没有遗憾的人生，或者至少少一些遗憾。','inference')

add(75,'c01-s05-p016-01140-r001-001','细节','What alternatives does this question explicitly present?',
 ['Becoming wealthy or remaining poor.','Staying or going.','Studying alone or joining a research team.','Choosing happiness or rejecting all meaning.'],1,
 '这个问句明确提出了哪两个选择？',['变富或保持贫穷。','留下或离开。','独自学习或加入研究团队。','选择幸福或拒绝一切意义。'],
 ['A 问句没有财富两极的选择。','B stay 与 go 是仅有的两个明确选项。','C 没有学习或研究团队的信息。','D 没有把留下或离开直接等同于幸福与拒绝意义。'],
 ['So, should you stay or should you go?'],
 'should','应该；是否应当','此处询问选择是否合适，不是表示过去发生过的事实','Should we remain here or continue the journey?',['should I stay','should we go'],
 '那么，你该留下，还是该离开？')

add(76,'c01-s05-p016-01140-r003-003','同义改写','Which paraphrase preserves the meaning of “on the path toward psychological richness”?',
 ['They have already completed every stage of psychological development.','They can become psychologically rich only by travelling continuously.','They have proved that staying can never offer psychological richness.','They are already moving in the direction of psychological richness.'],3,
 '哪个改写保留了“on the path toward psychological richness”的意思？',['他们已经完成心理发展的所有阶段。','他们只有不停旅行才能变得心理丰富。','他们已经证明留下永远不能带来心理丰富。','他们已经在朝心理丰富的方向前进。'],
 ['A on the path toward 是过程和方向，不是所有阶段已完成。','B 句子没有持续旅行或唯一途径的限制。','C 对离开者的描述不能反推出留下者永远没有可能。','D moving in the direction of 准确对应 on the path toward，保留 already。'],
 ['And those who go are already on the path toward psychological richness.'],
 'on the path toward','在通往……的道路上','表达朝某目标发展的过程，而非已经完全实现','Regular practice puts learners on the path toward fluency.',['on the path toward success','on the path toward recovery'],
 '而那些选择离开的人，已经走在通向心理丰富的道路上了。')

add(77,'c01-s05-p016-01725-r001-003','作者意图','What do these three questions invite the reader to consider?',
 ['Which city has the highest average income.','Why happiness research must be abandoned completely.','The ingredients, examples, and distinctiveness of a psychologically rich life.','How all people can follow one identical life plan.'],2,
 '这三个问题邀请读者思考什么？',['哪座城市的平均收入最高。','为什么必须完全放弃幸福研究。','心理丰富人生的要素、人物例子及其独特之处。','如何让所有人遵循完全相同的人生计划。'],
 ['A 没有城市收入排名的问题。','B 比较不同人生维度不等于宣布放弃幸福研究。','C ingredients、Who else、How...different 分别对应构成、人物与区别。','D 问题旨在探索，并未规定人人相同的计划。'],
 ['What are the other ingredients of a psychologically rich life? Who else has led a psychologically rich life? How is a psychologically rich life different from a happy life or a meaningful one?'],
 'ingredients','构成要素；成分','借用配料含义，询问这种人生由哪些因素构成','Trust is one of the ingredients of a strong partnership.',['the ingredients of success','a key ingredient'],
 '心理丰富的人生还有哪些构成要素？还有谁过着这样的人生？心理丰富的人生与幸福的人生或有意义的人生有何不同？')

assert len(out)==37 and [q['id'] for q in out]==[f'q-c01-{n:03}' for n in range(41,78)]
path=ROOT/'source/short-questions/additional.json'
existing=json.loads(path.read_text(encoding='utf8'))
byid={q['id']:q for q in existing}
for q in out:
 if q['id'] in byid:assert byid[q['id']]==q,('Refuse to overwrite changed authoring',q['id'])
 else:existing.append(q)
path.write_text(json.dumps(existing,ensure_ascii=False,indent=2)+'\n',encoding='utf8',newline='\n')
print('Merged 37 specifically written exercises; existing seven opening exercises preserved.')
