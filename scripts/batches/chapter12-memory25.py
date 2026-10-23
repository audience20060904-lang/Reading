"""25 individually authored exercises for frozen targets, PDF pages 139-142.
Preserve printed English, source positions and all previously published questions.
"""
from pathlib import Path
import json,hashlib
ROOT=Path(__file__).resolve().parents[2]
load=lambda p:json.loads((ROOT/p).read_text(encoding='utf8'))
b=load('public/data/book.json');plan=load('public/data/reading-plan.json');targets=load('source/short-questions/batch035-targets.json')['targets']
ss={s['id']:s for s in b['sentences']};pp={p['id']:p for p in b['paragraphs']};out=[]
def add(i,kind,prompt,options,answer,prompt_zh,options_zh,analyses,quotes,word,meaning,context,example,collocations,translation,support='explicit'):
 t=targets[i-1];u=next(u for u in plan['units'] if u['id']==t['readingUnitId']);group=[ss[sid] for sid in u['sentenceIds']];p=pp[u['paragraphId']];text=p['text'][group[0]['start']:group[-1]['end']]
 assert hashlib.sha256(text.encode()).hexdigest()==t['passageSha256'];evidence=[]
 for quote in quotes:
  offset=text.find(quote);assert offset>=0,(i,quote);start=group[0]['start']+offset;end=start+len(quote);touching=[s for s in group if s['start']<end and s['end']>start]
  evidence.append(dict(quote=quote,sentenceIds=[s['id'] for s in touching],sources=list({(r['pdfPage'],r['block']):r for s in touching for r in s['sources']}.values())))
 assert word.lower() in text.lower(),(i,word)
 out.append(dict(id=t['questionId'],version=1,readingUnitId=u['id'],chapterId=u['chapterId'],sectionId=u['sectionId'],paragraphId=u['paragraphId'],sentenceIds=u['sentenceIds'],passage=text,prompt=prompt,options=options,answer=answer,type=kind,promptZh=prompt_zh,optionsZh=options_zh,analyses=analyses,evidence=evidence,vocabulary=[dict(word=word,meaning=meaning,context=context,example=example,collocations=collocations)],translation=translation,support=support,editorialStatus='完整PDF139–142原页视觉核对。叙事人格关联、自报和tend不作因果；英雄提示研究与作者most likely心理丰富推测分开，不补随机化。感觉寻求者记忆任务为组间比较，反思不足为可能解释，不声称新奇导致损伤；百万富翁为心理积累比喻。馆藏对话保留跨单元引号、时间线索与试探确认，不重复或补句；af Klint创作先后及死后公开愿望依原书，不把无直接先锋联系扩大为无一切影响。复述帮助记忆但不保证准确。Beloved中Sixo为文学人物，She gather等人物用语原样保留，不改作标准语法或实验；电影角色与演员分开。海明威1930存箱、1956重得、后来回忆录，未补出版年；moveable feast为比喻。Pennebaker为书中写作益处概述，can不扩成人人立即治愈。保留旧ID范围与短句单元；候选句、原页审阅、上下文、直接证据分别计数。'))







add(1,'细节','How long does the interview typically take?',
 ['Exactly one hour.','Several days.','A few hours.','Less than a minute.'],2,
 '这项访谈通常要多久？',['恰好一小时。','好几天。','几个小时。','不到一分钟。'],
 ['A 没有exactly或one的限定。','B hours不是days。','C a few hours直接对应；typically表示通常而非每次固定时长。','D 与几个小时相差很大，不能把简短的问题当作整个访谈时长。'],
 ['this interview typically takes a few hours.'],
 'typically','通常；一般而言','描述常见访谈时长，不作每次的硬性规定','The discussion typically takes two hours.',['typically takes','a few hours'],
 '正如你可以想象的，这项访谈通常要花几个小时。')

add(2,'逻辑关系','What distinguishes the redemption narrative described here from contamination?',
 ['It reaches a happy ending after a decline and a turning point.','It starts badly and never changes direction.','It excludes setbacks from the account.','It begins well but deteriorates after a certain point.'],0,
 '这里的救赎叙事与污染叙事有何不同？',['先衰落再转折，最终有快乐结局。','开头坏，之后从不改向。','完全不讲挫折。','开头好，某节点后变坏。'],
 ['A good to bad、turning point、happy ending构成救赎叙事的变化线。','B 段中救赎包含转折，不是持续变坏。','C goes from good to bad包含不顺，非把挫折删掉。','D 这是contamination narrative的说明，误把另一类型当答案。Bush只是叙事例子，不是对其全部历史行为的客观判定。'],
 ['a typical redemption narrative that goes from good to bad before it hits a turning point and concludes with a happy ending.'],
 'goes south','变糟；走下坡路','污染叙事在某节点后由好转坏的习语，非地理向南','The plan went south after the funding was withdrawn.',['a redemption narrative','a contamination narrative'],
 '叙事有许多分类方式，但两个主要类型是救赎叙事和污染叙事。George W. Bush的故事是典型的救赎叙事：先由好转坏，之后遇到转折，最后以快乐结局收尾。G.W.的故事太典型了，McAdams甚至写了一本题为《George W. Bush and the Redemptive Dream》的书。另一种原型是污染叙事：人们讲的故事一开始很好，但在某个节点之后变糟。')

add(3,'细节','Which association does the passage report?',
 ['Greater openness is linked to less complex life stories.','A redemptive story proves that personality has permanently changed.','Narrative tone is unrelated to agreeableness.','Greater openness tends to accompany more complex life stories.'],3,
 '本段报告哪种关联？',['更高开放性与更不复杂的故事相联。','救赎叙事证明人格已永久改变。','叙事情绪基调与宜人性无关。','更高开放性往往伴随更复杂的人生故事。'],
 ['A more complex的方向被倒置。','B associated/tend表关联与倾向，没证明讲故事导致永久人格变化。','C 中间一句明确宜人、尽责及低神经质者叙事更积极。','D high in openness...more complex与原文对应，保留tend的概率限定。救赎叙事者的特征也是自报，不等于客观诊断。'],
 ['Individuals high in openness to experience tend to tell more complex stories than those low in openness.'],
 'conscientious','尽责的；认真负责的','此处是人格特质，与叙事的情绪基调相关','A conscientious student checks her work carefully.',['conscientious people','openness to experience'],
 '叙事认同，也就是我们如何讲述自己的人生故事，与多种人格特质有关。例如，讲救赎故事的人自报比不这样讲的人更尽责、更宜人、更外向，也较少神经质。宜人、尽责、低神经质的人，其人生叙事情绪基调，比不宜人、不尽责、高神经质的人更积极。对经验开放性较高的人，也倾向于比开放性低的人讲更复杂的故事。')

add(4,'语境词义','What does “colors” mean in this sentence?',
 ['Illustrates a story with visible pigments.','Influences how a life story is told.','Assigns a fixed score to each life event.','Ensures that the story is completely accurate.'],1,
 '本句colors是什么意思？',['给故事涂上可见颜料。','影响人生故事的讲述方式。','给每件人生事件固定评分。','确保故事完全准确。'],
 ['A colors为比喻动词，非画画。','B personality作为主语，影响how they tell的方式。','C 没有评分尺度。','D 影响叙述方式不等于保证记忆准确。So标志对前面人格与叙事关系的概括，不凭此建立因果实验结论。'],
 ['one’s personality colors how they tell their life story.'],
 'colors','影响；使带上某种色彩','人格让人生叙述带上个人倾向，非字面上色','Her experience colored her interpretation of the event.',['color an interpretation','tell a life story'],
 '因此，一个人的人格会影响其讲述人生故事的方式。')

add(5,'作者意图','What do the quoted questions encourage participants to connect?',
 ['The costs of their home and work arrangements.','Their present identity with experiences, changes, and goals.','Their personality scores with other participants’ scores.','The exact publication dates of novels they have read.'],1,
 '这些引述问题鼓励参与者把什么联系起来？',['住家和工作的开支。','现在的自我与经历、环境变化、目标。','自己与他人的人格分数。','所读小说的精确出版日期。'],
 ['A work/home的平常问题在另一条件，本段没问成本。','B makes you you、change...prompted、overall goal聚焦成为今天自己的历程。','C 段中没问人格测评分数。','D novel experience指新奇经历，不能把novel误作这里问的小说。没有从半数分组补写随机化。'],
 ['What change of setting or novel experience prompted your journey to become who you are today?','What overall goal were you striving for that led to who you are today?'],
 'striving for','努力争取；追求','指塑造今天自我的历程中所追求的整体目标','She was striving for a better understanding of herself.',['strive for a goal','a novel experience'],
 '近期研究还表明，人生故事的视角会改变人们讲述它的方式。例如，Benjamin Rogers及同事向一组参与者中的一半提出一系列问题，诸如：“什么使你成为你？”“什么环境变化或新奇经历，开启了使你成为今天自己的历程？”“你为之努力的什么整体目标，使你成为今天的自己？”')

add(6,'作者意图','What framing are these prompts presumed to encourage?',
 ['A detached inventory of household features.','A judgment that rivals never affect a life.','A demand that the participant invent an enemy.','Viewing oneself as the hero of a journey involving obstacles and growth.'],3,
 '这些提示被认为会鼓励什么叙事框架？',['疏离地罗列家庭特征。','认定对手从不影响人生。','要求参与者编造敌人。','把自己视为经历障碍与成长的旅程主角。'],
 ['A mundane日常罗列是对照条件。','B obstacles含rival的例子，不是否认影响。','C such as举例可遇障碍，非强迫编敌人。','D 最后一句明确hero of their story；presumably保留作者对提示作用的判断。legacy也不只指钱财遗产。'],
 ['These are the prompts that presumably lead a person to think of themselves as the hero of their story.'],
 'legacy','留给后人的影响；遗产','问题询问人生旅程留下何种影响，不限财产','Her teaching left a lasting legacy in the community.',['leave a legacy','overcome obstacles'],
 '“什么挑战或障碍，比如宿敌、竞争者或负面事件，挡在你的旅程上？”“在成为今天自己的旅程中，你个人如何成长？”“你的旅程以哪些方式留下了影响？”这些提示，想必会引导一个人把自己看成故事里的英雄。')

add(7,'细节','What difference did telling a story as a hero make, according to this passage?',
 ['People felt their lives were more meaningful and flourishing.','People were asked only to list work and home features.','People objectively became wealthier after the questions.','People lost interest in interpreting their life stories.'],0,
 '根据本段，作为英雄讲故事带来什么差别？',['人们觉得生活更有意义、更蓬勃。','人们只被问工作与住家特征。','问题后客观上变得更有钱。','人们不再想解释人生故事。'],
 ['A made people feel对应所报告的感受变化；未补写客观财富或永久人格改变。','B 那是另一半的平常问题，非英雄叙事的结果。','C meaningful/flourishing不等于测得收入增长。','D 本段报告更积极感受，没有兴趣消失结果。'],
 ['Telling their stories as a hero made people feel that their lives were more meaningful and flourishing.'],
 'mundane','平常的；日常的','描述工作住家等普通生活特征的问题，区别于英雄旅程提示','The interview began with mundane questions about daily routines.',['mundane questions','feel more meaningful'],
 '另一半参与者被问了一系列平常问题，例如：“告诉我们你生活的各种特征……比如你的工作和住家。”把自己的故事作为英雄故事来讲，使人觉得人生更有意义、更蓬勃。')

add(8,'推断','Which conclusion preserves the author’s qualification?',
 ['The heroic role guarantees objectively richer experiences.','An observer can never tell a satisfying story.','One’s perceived role affects the account, with greater psychological richness described as likely.','Changing one’s role changes every event that actually occurred.'],2,
 '哪项结论保留作者的限定？',['英雄角色保证客观经历更丰富。','旁观者永远讲不出满意故事。','自认为的角色影响讲述，心理更丰富被说成很可能。','换角色会改变已发生的每件事。'],
 ['A sounds及most likely没有给客观保证。','B whether...hero...observer是视角对照，非永远不可能的绝对结论。','C 保留叙述与听起来的感受层面，以及most likely的推测强度。','D 编辑叙述视角并非改变过去事件。单句是作者综合判断，不能把心理丰富部分说成此处直接实验测量。'],
 ['whether your life sounds more satisfying, more meaningful, and, most likely, psychologically richer.'],
 'observer','观察者；旁观者','对照人生故事主角的自我角色视角','He described the scene as an observer rather than a participant.',['as an observer','most likely'],
 '归根结底，你怎样看待自己在自己人生中的角色——把自己看作故事的英雄，还是一个旁观者——确实会影响故事怎样讲述，也会影响人生听起来是否更令人满意、更有意义，以及很可能在心理上更丰富。',support='limited-inference')

add(9,'主旨','Why is memory important to the portfolio described here?',
 ['It converts every forgotten event into financial wealth.','It removes any need to think about past experiences.','It guarantees that every recollection is factually exact.','It allows past experiences to remain part of psychological wealth.'],3,
 '为什么记忆对这里的“组合”重要？',['将所有遗忘事件变为金钱财富。','免除思考过去经历的需要。','保证每次回忆事实精确。','让过去经历仍能成为心理财富的一部分。'],
 ['A portfolio和wealth是心理积累比喻，不是理财收益。','B deep processing等说明需要加工，非无需思考。','C 本段谈记住与遗忘，没有保证逐字准确。','D 忘记事件就错过把它纳入心理财富的机会，因此记忆是保留经历的关键。'],
 ['If we forget a past event, we miss out on the chance to add that experience to our portfolio of psychological wealth.'],
 'consolidation','巩固','认知科学语境中的记忆巩固，与深加工和复习并列','Rest and review can support memory consolidation.',['memory consolidation','deep processing'],
 '记忆是心理丰富人生的关键。如果我们忘记一件过去的事，就错过了把那次经历加入心理财富组合的机会。但我们怎样记住呢？从认知科学来看，深度加工、复习和巩固显然是关键。')

add(10,'同义改写','Which practice best matches this sentence?',
 ['Notice an event, revisit it often, and develop its details.','Ignore an event until someone supplies an exact record.','Seek novelty once and avoid thinking about it again.','Focus only on whether other people remember the event.'],0,
 '哪种做法最符合本句？',['注意事件、经常回想、展开细想。','忽略事件直到有人提供精确记录。','只追求一次新鲜，之后不再想。','只关心别人是否记得。'],
 ['A pay attention、think...frequently、elaborate三项逐一对应。','B 忽略与注意相反，原文没说依赖精确记录才开始。','C 避免回想与frequently相反。','D 主语we强调自己加工经历，非只测别人。in order to说明记忆是目的，不是保证永不遗忘。'],
 ['pay attention to what is happening, think about an event frequently, and elaborate on it in order to remember it.'],
 'elaborate on','详细展开；深入阐述','对事件作更丰富加工，非编造原来没有的事实','She elaborated on the experience in her journal.',['elaborate on an event','pay attention to'],
 '换言之，为了记住一件事，我们需要注意正在发生什么，经常思考那件事，并对它作更详细的展开。')

add(11,'逻辑关系','How does the memory study relate to the discussion of sensation-seekers?',
 ['It proves that seeking novelty directly destroys memory.','It shows that sensation-seekers had fewer novel experiences.','It reports weaker memory-task performance alongside a possible explanation involving reflection.','It finds that nightly reflection makes all personality differences disappear.'],2,
 '记忆研究与感觉寻求者的讨论是什么关系？',['证明追求新奇直接破坏记忆。','显示感觉寻求者新奇经历更少。','报告较弱记忆任务表现，并伴随反思不足的可能解释。','发现每夜反思消除所有人格差异。'],
 ['A 一项组间任务表现不能独自证实追求新奇造成记忆损害。','B despite说明他们寻求更多多样新奇经历。','C might not及One of the reasons限定心理丰富的解释；研究明确仅报告短期/工作记忆任务相对表现。','D much more likely非所有差异归零，段中无此实验。'],
 ['One of the reasons why sensation-seekers might not lead a far more psychologically rich life','In one study, sensation-seekers did poorly in short-term memory and working memory tasks, relative to non-sensation-seekers.'],
 'reflective','善于反思的；常回顾思考的','指回想经历的倾向，不是镜面反射','A reflective learner reviews what happened each day.',['reflect upon experiences','working memory tasks'],
 '有些人天生更善于反思。如果你每晚反思当天的事情，就比不这样做的人更可能记住那些事。感觉寻求者虽然比不寻求刺激者追求更多多样、新奇的经历，却未必拥有丰富得多的人生；其中一个原因是他们不反思自己的经历。一项研究中，与不寻求刺激者相比，感觉寻求者在短期记忆和工作记忆任务中表现较差。')

add(12,'作者意图','What is the purpose of comparing sensation-seekers to partying millionaires?',
 ['To report participants’ verified bank balances.','To illustrate consuming experiences without accumulating their psychological value.','To establish that travel spending causes poor memory.','To suggest that all wealthy people lack interesting experiences.'],1,
 '把感觉寻求者比作开派对的百万富翁，有什么作用？',['报告已核实的参与者银行余额。','比喻消耗经历却没有积累其心理价值。','确立旅行花费导致记忆差。','说所有富人都缺乏有趣经历。'],
 ['A are like明确比喻，非财产调查。','B momentary thrill与not accumulating对照，强调无反思就短暂兴奋后又需新刺激。','C 比喻不提供旅行消费与记忆的因果实验。','D millionaires为类比对象，不能扩大到所有富人的人生判定。'],
 ['Without reflection, experience serves as a momentary thrill.','they are wasting their adventures and not accumulating psychologically rich experiences.'],
 'momentary','短暂的；片刻的','刺激只维持一时，没变为长久心理积累','The news brought a momentary thrill.',['a momentary thrill','accumulate experiences'],
 '没有反思，经历就只是一时的兴奋。过一阵子，这些人又需要更多刺激。感觉寻求者就像办派对、把赚来的钱全花光的百万富翁：他们浪费自己的冒险，没有积累心理丰富的经历。')

add(13,'作者意图','What does the wife’s question illustrate?',
 ['A formal test of the artist’s nationality.','The need to remember every museum visit without help.','A claim that only naturally introspective people can remember art.','An everyday prompt that can help someone recall an experience.'],3,
 '妻子的提问用来说明什么？',['对艺术家国籍的正式测试。','必须不借助帮助记住每次博物馆参观。','只有天生内省者能记住艺术。','可帮助人回想经历的日常提示。'],
 ['A nationality只是记忆线索，不是此处实验目的。','B Having someone...正说明可借他人提问。','C If you are not...what can you do为不天生内省者提供方式。','D 先提出日常测记忆，再用妻子问展览作例证。尚未给艺术家姓名，不能从此段推出完整身份。'],
 ['Having someone test your memory in everyday life is one way.','Shige, do you remember that exhibition at the Guggenheim?'],
 'introspective','内省的；善于自我省察的','愿意向内回顾思考经历的倾向','She became more introspective after the long journey.',['inclined to be introspective','test your memory'],
 '不过，如果你不是天生就倾向内省的人，能怎么办呢？让别人在日常生活中测试你的记忆，是一种方法。比如，我妻子曾问：“Shige，你还记得古根海姆那次展览吗？一位瑞典女性……她叫什么来着？”')

add(14,'细节','What timing clues are supplied in this exchange?',
 ['The last year abroad, during summer.','The first year in New York, during winter.','The first year in Paris, during winter.','A precisely dated day in New York.'],1,
 '这段对话提供了什么时间线索？',['国外最后一年，夏季。','在纽约的第一年，冬季。','在巴黎的第一年，冬季。','纽约某个精确到日的日期。'],
 ['A first和winter都被改了。','B First year in New York及In winter逐项对应。','C 城市是New York，不能混入后面的巴黎。','D 没有年月日；一个阶段和季节不等于精确日期。开头I have no idea显示起初没想起来，非已准确回忆。'],
 ['First year in New York. In winter.'],
 'have no idea','不知道；毫无头绪','对方最初无法辨认所谈经历，之后才接受线索','I have no idea when we last visited that gallery.',['have no idea','in winter'],
 '“我完全不知道你在说什么。我们什么时候去的？”“在纽约的第一年。冬天。')

add(15,'推断','What does the final “Yes, Hilma!” indicate within this exchange?',
 ['A correction that the paintings were not abstract.','A decision to visit the exhibition for the first time.','Confirmation of the tentative identification just offered.','Proof that every detail of the visit has been recovered.'],2,
 '这段对话最后“Yes, Hilma!”说明什么？',['纠正画并非抽象。','决定首次去看展。','确认刚刚试探提出的身份辨认。','证明参观的所有细节都已恢复。'],
 ['A Super abstract没被否定。','B 对话在辨认记忆，没有首次出行计划。','C Af Klint or something带试探，Yes与Hilma接着确认这一辨认。','D 一次姓名确认不能推出所有参观细节都准确回忆。huge/pink是线索，不宜变成关于其全部作品的定义。'],
 ['Af Klint or something?” “Yes, Hilma!”'],
 'abstract','抽象的','描述这次回忆中的画作风格，非缺乏具体生活经历','The gallery displayed a large abstract painting.',['abstract paintings','a tentative identification'],
 '非常抽象。”“呃……巨大、粉红色的画？Af Klint之类的？”“对，Hilma！”',support='limited-inference')

add(16,'细节','Which statement matches the account of af Klint?',
 ['She made abstract works before Mondrian and Kandinsky and wanted posthumous public display.','She developed abstract works only after direct collaboration with Kandinsky.','She wanted to display all her work publicly during her lifetime.','She refused any eventual public viewing of her work.'],0,
 '哪项符合本段对af Klint的叙述？',['早于Mondrian和Kandinsky创作抽象作品，希望死后才公开。','仅在与Kandinsky直接合作后才创作抽象作品。','希望生前公开全部作品。','拒绝作品将来任何形式的公开。'],
 ['A before给创作先后，until after her death给公开时间限制。','B without any direct association否定此处直接联系；不能说由Kandinsky带动。','C 把not...until after改成生前。','D 不愿生前展示不等于永不公开；也没说她与世上所有艺术家绝无任何联系。'],
 ['created her amazing, abstract pieces before Piet Mondrian and Wassily Kandinsky','af Klint did not want the public to see her work until after her death.'],
 'avant-garde','先锋的；前卫的','指主要前卫艺术家，限定原文所说没有直接联系的对象','The exhibition featured avant-garde artists.',['avant-garde artists','direct association'],
 '然后，我们就能提醒自己：Hilma af Klint在Piet Mondrian和Wassily Kandinsky之前，已经创作了令人惊叹的抽象作品，而且与任何主要前卫艺术家都没有直接联系。与大多数艺术家不同，她不想让公众在自己去世前看到作品。')

add(17,'作者意图','Why does the author mention his wife, children, and students?',
 ['To show that they painted the works he recalled.','To identify people who prompt recollection and also listen.','To claim that only family members can support memory.','To report a controlled experiment comparing their memory scores.'],1,
 '作者为何提妻子、孩子和学生？',['说明他们画了所忆作品。','指出提醒他回忆、也愿意倾听的人。','声称只有家人可支持记忆。','报告比较他们记忆分数的对照实验。'],
 ['A 他们是提问者和听众，不是画家。','B fulfilled that role回指ask...questions，末句再补good listeners。','C students已超家人，且作者没有only限制。','D 这是个人反事实回顾，不是给这些人分组做实验。would not have thought是作者自己的判断。'],
 ['having people ask you questions about your past experiences is really helpful.','My wife, children, and students have fulfilled that role for me. They are also good listeners.'],
 'let alone','更不用说','在否定中递进：若未被提醒，连展览也没想到，更谈不上画作','He could not recall the visit, let alone the exact date.',['let alone remember','fulfil a role'],
 '没有妻子问这些问题，我就不会想起Klint的展览，更不用说记起她的画。因此，让人问起你的过去经历，确实很有帮助。妻子、孩子和学生对我都起了这个作用。他们也是好听众。')

add(18,'推断','What limitation does the parenthesis place on retelling?',
 ['It can help only if the listener verifies every detail.','It inevitably replaces all genuine memories with false ones.','It is useful only for events that happened that same day.','It may aid remembering without guaranteeing exact accuracy.'],3,
 '括号对复述的作用作了什么限定？',['只有听众逐项核实才有帮助。','必然把全部真实记忆变假。','只对当天的事有帮助。','可能帮助记忆，但不保证完全精确。'],
 ['A 没有核实每项的前提。','B not accurate不等于每段记忆必全假，更无必然替换。','C 每日讲述是情境，不是only限制。','D even if明确：帮助记得与回忆是否完全忠实可以分开；不要把复述流畅当作事实准确证明。'],
 ['Retelling, in turn, helps you remember what happened (even if the stories themselves are not accurate recollections of exactly what happened).'],
 'captive audience','不能轻易离开的听众；固定听众','此处指身边可持续听你叙述的人，并非真的被囚禁','The family provided a captive audience for his travel stories.',['a captive audience','accurate recollections'],
 '如果身边有固定听众，你就更可能告诉他们每天发生了什么。反过来，复述有助于记住发生的事，即使故事本身未必是对事情实际经过的精确回忆。',support='limited-inference')

add(19,'作者意图','Why is the character Sixo quoted?',
 ['To illustrate how a listener can help give shape to scattered parts of a person’s story.','To present a clinical trial of walking thirty miles.','To prove that every good listener must be a romantic partner.','To prescribe a standard grammar rule from the character’s speech.'],0,
 '为什么引用Sixo这个人物的话？',['说明倾听者可帮人把零散人生故事整理成形。','呈现步行30英里的临床试验。','证明好听众必须是恋人。','从人物话语规定标准语法。'],
 ['A 开头craft a story/see the point与引文pieces...right order相呼应，是文学例证。','B character in Toni Morrison’s Beloved明确小说人物，不是实验受试。','C 一个伴侣例子不能推成必须浪漫关系。','D 原文保留人物语言如She gather，题目不擅改为标准英语，也不把它教作通用标准。'],
 ['A good listener not only asks the right questions and listens, but also helps you craft a story and see the point of your story.','The pieces I am, she gather them and give them back to me in all the right order.'],
 'craft','精心构建；打磨','在叙事语境把经历组织成能表达意义的故事，非编造事实','She helped him craft a clear account of the journey.',['craft a story','see the point'],
 '好听众不只问恰当的问题并倾听，还帮你构建故事，看出故事的意义。例如，Toni Morrison小说《Beloved》中的人物Sixo解释自己为何走30英里去见他的女人：“她是我心灵的朋友。她把我聚拢起来，伙计。我那些零碎的部分，她收起来，再按恰当的顺序还给我。')

add(20,'语境词义','What does “accrue your experiences” suggest in this context?',
 ['Sell descriptions of the past for money.','Ensure that every event can be recalled verbatim.','Build up experiences as a lasting psychological resource.','Replace talking with a single professional diagnosis.'],2,
 '这里accrue your experiences意味着什么？',['把过去描述卖钱。','确保每事能逐字回忆。','把经历积累为较持久的心理资源。','以一次专业诊断取代交谈。'],
 ['A accrue借积累作比喻，没有卖故事情节。','B remember不保证逐字不差，前段也有限定。','C 与digest、remember并列，指通过定期交谈消化并积累经历。','D 文中先谈好治疗师，再一般谈someone与on a regular basis，没有一次诊断替代交谈。引文承接小说，不能当实验结论。'],
 ['Finding someone with whom you can talk about your past experiences on a regular basis helps you digest, remember, and accrue your experiences.'],
 'accrue','积累；逐渐增加','把经历消化记住并保留其心理价值，不是经济利息','The benefits accrued over several years of reflection.',['accrue experiences','on a regular basis'],
 '“有个心灵的朋友那样的女人，真好，你知道。”好的治疗师也能帮助把令人困惑的碎片拼在一起。找到一个能让你经常谈论过去经历的人，有助于你消化、记住并积累这些经历。')

add(21,'作者意图','Why does the author introduce keeping a journal here?',
 ['To require every reader to imitate Daniel Plainview’s attitude.','To offer a way of preserving experiences for people who prefer solitude.','To argue that company always damages memory.','To claim that Hemingway never talked to anyone in Paris.'],1,
 '作者为什么在这里提出写日记？',['要求每位读者模仿Daniel Plainview态度。','给偏好独处者提供保存经历的方法。','论证陪伴总会损害记忆。','声称海明威在巴黎从不与人说话。'],
 ['A 电影人物只是Some people are like的说明，非行为指令。','B If you prefer a solitary solution明确提供另一选择；要写也要重读。','C 先前谈交谈的益处，本段并未改成陪伴有害。','D kept detailed journals不能推出完全不社交。Daniel为角色、Daniel Day Lewis为演员，不能混为真实作者自白。'],
 ['If you prefer a solitary solution, keeping a journal and rereading it is an excellent way to keep track of your experiences.'],
 'solitary','独处的；独自的','提供不依赖交谈听众的记忆方式，不是孤独程度诊断','She preferred a solitary walk before writing.',['a solitary solution','keep track of experiences'],
 '你们有些人也许不喜欢与人相伴。毕竟，有些人就像电影《There Will Be Blood》里由Daniel Day Lewis饰演的Daniel Plainview，他说：“我总看到人最坏的一面……我想赚足够的钱，好远离所有人。”如果偏好独自解决，写日记并重读，是追踪经历的极好方式。Ernest Hemingway二十多岁时在巴黎生活，并写了详细日记。')

add(22,'逻辑关系','Which sequence matches the account of Hemingway’s journals?',
 ['They were stored before he left Paris, rediscovered in 1956, and later used in writing about Paris.','They were written in 1956, then taken to Paris for the first time in 1930.','The manager wrote the journals and published them before meeting Hemingway.','Hemingway published the memoir in 1930, then began recording the 1920s.'],0,
 '哪项顺序符合海明威日记的叙述？',['离开巴黎前存放，1956重见，后来用于写巴黎。','1956写，然后1930首次带去巴黎。','经理写日记，见海明威前就出版。','1930出版回忆录，随后开始记录1920年代。'],
 ['A before...1930存箱，1956经理提醒，取回读后later写回忆录，次序准确。','B 颠倒日期，也混淆日记创作与发现。','C 经理只告知箱子仍在，没有代写出版。','D 本段没给回忆录出版年，不能把1930离开时间偷换为出版时间。'],
 ['Before he left Paris in 1930, he put them in a trunk','In 1956, he was having lunch with the manager of the Ritz','He read and wrote about his experiences in Paris later in his memoir, A Moveable Feast.'],
 'retrieved','取回；找回','从酒店地下室取回早年存放的箱子','She retrieved her notebook from the drawer.',['retrieve a trunk','store in a basement'],
 '1930年离开巴黎前，他把日记放进一个箱子，存到Ritz酒店地下室。1956年，他与酒店经理吃午饭，经理告诉他，箱子还在地下室！于是海明威去地下室取回箱子，在里面发现自己1920年代的日记。他读了这些日记，后来在回忆录《A Moveable Feast》中写下巴黎经历。')

add(23,'作者意图','What does the author emphasize through the “moveable feasts” image?',
 ['Paris must remain a person’s permanent physical home.','War is the only experience worth recording.','Recorded experiences can remain with a person and be cherished later.','Travel alone guarantees perfect factual recollection.'],2,
 '作者用“流动盛宴”的意象强调什么？',['巴黎必须成为永久实际住处。','只有战争值得记录。','记录过的经历能相伴长久，供日后珍惜。','单靠旅行就保证完美回忆。'],
 ['A wherever you go说明可离开而记忆仍在。','B ranging from...举海明威经历，不把战争限定为唯一值得记录的事。','C stays with you与recordkeeping helped...remember and cherish共同说明可携带的心理财富。','D journalistic habits强调记录，且没保证记忆绝对准确；文学比喻非实验结果。'],
 ['His journalistic habits of recordkeeping helped him remember and cherish those unique experiences for years to come.'],
 'cherish','珍惜；珍藏于心','多年后仍珍视那些独特经历的价值','She cherished the memory of their conversations.',['remember and cherish','for years to come'],
 '在书名下面，他写道：“如果你足够幸运，年轻时在巴黎生活过，那么此后无论去哪里，它都会伴随你，因为巴黎是一场流动的盛宴。”海明威有许多不同寻常的人生经历，从第一次世界大战到第二次世界大战，再到西班牙内战。他作为记者养成的记录习惯，帮助他在往后多年记住并珍惜那些独特经历。因此，他收集了许多场流动的盛宴。')

add(24,'主旨','What additional benefit of writing does this passage describe?',
 ['It makes recording experiences unnecessary.','It guarantees immediate recovery from every traumatic event.','It prevents a person from asking why events happened.','It can organize thoughts and help make sense of difficult events.'],3,
 '本段描述写作的哪项额外益处？',['让记录经历变得不必要。','保证立刻从每次创伤恢复。','阻止人追问事件原因。','能整理思想，帮助理解艰难事件。'],
 ['A diaries...building blocks正肯定记录。','B can没有immediate/every保证；段落未给治疗方案或普遍治愈数据。','C see why与阻止追问相反。','D However从记忆转向组织想法、理解行为和事件意义，是书中对Pennebaker发现的概述，不补具体研究设计。'],
 ['the benefits of journal keeping are not limited to memory.','by writing you can organize your thoughts and overcome a traumatic event.','You can start to see why you did this, or why that happened, and what it all means.'],
 'building blocks','构成基础；基础材料','日记为将来心理丰富提供可回顾的经历材料','These notes became the building blocks of her later memoir.',['building blocks of','organize your thoughts'],
 '我自己懒得这样做，但日记和日志是你未来心理丰富的基础材料。不过，写日志的益处不限于记忆。James Pennebaker发现，通过写作，你可以整理思想，克服一件创伤事件。你能开始理解：自己为何那样做，或事情为何发生，以及这一切意味着什么。')

add(25,'语境词义','What does “refresh your memory” mean here?',
 ['Revive recollection by looking at old photographs.','Replace earlier memories with newly invented events.','Prove that every old photograph is accurate.','Stop recording events once a photograph exists.'],0,
 '这里refresh your memory是什么意思？',['看旧照片以唤起回忆。','用新编事件替换旧记忆。','证明每张旧照都准确。','有照片后就停止记录。'],
 ['A look at old photo albums给具体唤起回忆的方法。','B refresh是唤回，不是造新事实。','C 单句没讨论照片真实性，不能当核验结果。','D Likewise补充一种方式，并非禁止其他记录。can保留可采用的建议，非人人必须如此。'],
 ['you can look at old photo albums to refresh your memory.'],
 'refresh your memory','唤起回忆；使重新记起','借旧相册重新想起过去，不保证全部细节精确','The photographs helped refresh her memory of the trip.',['refresh your memory','old photo albums'],
 '同样，你可以翻看旧相册来唤起回忆。')

assert len(out)==25 and [q['id'] for q in out]==[t['questionId'] for t in targets]

def persist():
 path=ROOT/'source/short-questions/additional.json';existing=load('source/short-questions/additional.json');byid={q['id']:q for q in existing}
 for q in out:
  if q['id'] in byid:assert byid[q['id']]==q,('Refuse to overwrite changed authoring',q['id'])
  else:existing.append(q)
 path.write_text(json.dumps(existing,ensure_ascii=False,indent=2)+'\n',encoding='utf8',newline='\n')
 review=dict(batchId='batch-035',date='2026-10-23',pdfSha256=b['pdfSha256'],checkedPdfPages=list(range(139,143)),questionIds=[q['id'] for q in out],paragraphs=[dict(id=pid,textSha256=hashlib.sha256(pp[pid]['text'].encode()).hexdigest()) for pid in dict.fromkeys(q['paragraphId'] for q in out)],note='完整PDF139–142原页视觉核对。叙事人格关联、自报和tend不作因果；英雄提示研究与作者most likely心理丰富推测分开，不补随机化。感觉寻求者记忆任务为组间比较，反思不足为可能解释，不声称新奇导致损伤；百万富翁为心理积累比喻。馆藏对话保留跨单元引号、时间线索与试探确认，不重复或补句；af Klint创作先后及死后公开愿望依原书，不把无直接先锋联系扩大为无一切影响。复述帮助记忆但不保证准确。Beloved中Sixo为文学人物，She gather等人物用语原样保留，不改作标准语法或实验；电影角色与演员分开。海明威1930存箱、1956重得、后来回忆录，未补出版年；moveable feast为比喻。Pennebaker为书中写作益处概述，can不扩成人人立即治愈。保留旧ID范围与短句单元；候选句、原页审阅、上下文、直接证据分别计数。')
 (ROOT/'source/short-questions/review-chapter12-memory25.json').write_text(json.dumps(review,ensure_ascii=False,indent=2)+'\n',encoding='utf8',newline='\n')
 print('Saved',len(out),'of 25 individually authored exercises')

if __name__=='__main__':persist()
