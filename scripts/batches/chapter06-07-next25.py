"""25 individually authored exercises for frozen targets, PDF pages 65-69.
Preserve printed English, source positions and all previously published questions.
"""
from pathlib import Path
import json,hashlib
ROOT=Path(__file__).resolve().parents[2]
load=lambda p:json.loads((ROOT/p).read_text(encoding='utf8'))
b=load('public/data/book.json');plan=load('public/data/reading-plan.json');targets=load('source/short-questions/batch017-targets.json')['targets']
ss={s['id']:s for s in b['sentences']};pp={p['id']:p for p in b['paragraphs']};out=[]
def add(i,kind,prompt,options,answer,prompt_zh,options_zh,analyses,quotes,word,meaning,context,example,collocations,translation,support='explicit'):
 t=targets[i-1];u=next(u for u in plan['units'] if u['id']==t['readingUnitId']);group=[ss[sid] for sid in u['sentenceIds']];p=pp[u['paragraphId']];text=p['text'][group[0]['start']:group[-1]['end']]
 assert hashlib.sha256(text.encode()).hexdigest()==t['passageSha256'];evidence=[]
 for quote in quotes:
  offset=text.find(quote);assert offset>=0,(i,quote);start=group[0]['start']+offset;end=start+len(quote);touching=[s for s in group if s['start']<end and s['end']>start]
  evidence.append(dict(quote=quote,sentenceIds=[s['id'] for s in touching],sources=list({(r['pdfPage'],r['block']):r for s in touching for r in s['sources']}.values())))
 assert word.lower() in text.lower(),(i,word)
 out.append(dict(id=t['questionId'],version=1,readingUnitId=u['id'],chapterId=u['chapterId'],sectionId=u['sectionId'],paragraphId=u['paragraphId'],sentenceIds=u['sentenceIds'],passage=text,prompt=prompt,options=options,answer=answer,type=kind,promptZh=prompt_zh,optionsZh=options_zh,analyses=analyses,evidence=evidence,vocabulary=[dict(word=word,meaning=meaning,context=context,example=example,collocations=collocations)],translation=translation,support=support,editorialStatus='PDF 第 65–69 页逐题原页核对；固定原句与来源；保留非决定性、may/could 等限定；区分人物引例、句子补全研究、建议与竞技运动叙事'))




add(1,'细节','How are conscientious people described at the start of the passage?',
 ['As people who avoid setting goals so that they cannot fail.','As people whose plans change whenever they face a minor obstacle.','As organised, careful and thorough people who pursue clear goals diligently.','As people guaranteed to succeed without effort or setbacks.'],2,
 '片段开头怎样描述尽责的人？',['不设目标，以免失败。','一遇小障碍就改变计划。','有条理、细心、周密，并勤奋追求明确目标。','无需努力或经历挫折就必定成功。'],
 ['A clear goals 与不设目标相反。','B 作者强调不宜过于轻易灰心，未说遇小障碍就放弃。','C 两个开头句分别给出有条理等特征和勤奋追求目标。','D diligently 表示需要努力，全文没有免除挫折或保证成功。lower levels 是人格特质的相对描述，不是临床诊断。'],
 ['Conscientious people are well organized, careful, and thorough. They have clear goals and pursue them diligently.'],
 'diligently','勤奋地；认真而持续地','修饰追求明确目标的方式，不是轻松获得结果','She worked diligently to check each source.',['pursue goals diligently','work diligently'],
 '尽责的人有条理、细心而周密。他们有明确目标，并勤奋追求。因此，为成功追求目标，你不能过分担忧成功路上的种种障碍，也不能事情不顺时就轻易灰心。所以，较低的神经质水平（不过分担心）是有帮助的。')

add(2,'推断','Which reading best respects the caution in the author’s description of Thunberg?',
 ['The author suggests anxiety may fuel her work, without presenting a clinical diagnosis.','The author reports a medical test proving that anxiety always improves performance.','The passage says that a meaningful life requires overwhelming anxiety.','The passage establishes that she never worries about environmental problems.'],0,
 '哪种理解最保留作者描述 Thunberg 时的谨慎语气？',['作者认为焦虑可能推动她的工作，并未呈现临床诊断。','作者报告医学检测，证明焦虑总能提高表现。','有意义人生必须具有压倒性的焦虑。','书中确立她从不担忧环境问题。'],
 ['A appears、seems 均保留观察与解释的不确定性，本段没有临床测量。','B 没有医学检测，也无 always 的普遍保证。','C not overwhelming 才是最后一句的条件，不能删掉 not。','D worries intensely 明确相反；人格术语不应直接替换成对人物的疾病诊断。'],
 ['she seems to leverage her anxiety to fuel her work.','So long as one’s neuroticism is not overwhelming, a meaningful life is possible.'],
 'fuel','推动；为……提供动力','动词，比喻焦虑成为工作动力；作者使用 seems 保留推测','Her curiosity helped fuel a long research project.',['fuel her work','fuel an interest'],
 '值得注意的是，Thunberg 似乎比多数人更具神经质倾向。她强烈担忧环境灾难和气候变化。然而，她似乎把焦虑转化为工作的动力。只要神经质倾向没有强到令人无法承受，有意义的人生仍然可能。','inference')

add(3,'主旨','What common difficulty do the two political examples illustrate in the author’s argument?',
 ['Strong convictions ensure openness to every opposing opinion.','People at opposite political ends must have identical beliefs.','Immigration attitudes and climate opinions are measured here in a clinical experiment.','Strong commitments may make openness to conflicting positions difficult.'],3,
 '在作者论证中，两个政治人物例子说明什么共同困难？',['坚定信念确保接纳每种反对观点。','政治立场相反的人必须信念相同。','本段通过临床实验测量移民态度与气候观点。','强烈投入某种信念，可能使人难以开放接纳冲突立场。'],
 ['A 与 openness is difficult 的方向相反。','B 例子有共同模式，不等于观点内容相同。','C 没有实验方法或测量报告。','D 首句提出困难，后面分别说明作者所推断的不易开放之处。关于恐怖分子的措辞归于作者对 Huckabee 信念的描述，不是网站或研究对穆斯林群体作事实判断。'],
 ['openness is difficult for those who have strong convictions.'],
 'self-righteous','自以为正义的；自认立场正确的','作者提醒坚定事业信念可能伴随不愿审视其他立场，不是指信念本身必然错误','A self-righteous tone can make a discussion harder.',['become self-righteous','self-righteous about a cause'],
 '相比之下，信念坚定的人可能难以保持开放。人很容易对自己的事业自以为正义。作者认为，Huckabee 不太可能对来自穆斯林国家的移民开放，因为他坚信其中少数人可能是恐怖分子；Thunberg 不太可能接纳气候变化否认者的意见，因为她确信气候变化由人类活动驱动。这里保留作者的人物信念归属，不把前一说法当作关于实际群体风险的研究结论。')

add(4,'逻辑关系','What does the final sentence prevent the reader from concluding?',
 ['Openness and extraversion are associated with trying new things.','Personality traits determine with certainty who will have a rich life.','The author uses Goldmund as an illustration.','People may learn something new through experience.'],1,
 '最后一句防止读者得出什么结论？',['开放性和外向性与尝试新事物相关。','人格特质能确定无疑地决定谁的人生丰富。','作者用 Goldmund 作说明性例子。','人可通过经历学到新东西。'],
 ['A 该联系仍在，非决定性不等于毫无关联。','B not deterministic 正是否定这种必然决定。','C 文中明确引入小说人物，末句不否认引例。','D 文中保留 learn something new 的可能；Goldmund 是文学例子，不能视为实验参与者。'],
 ['These relationships are not deterministic, however.'],
 'deterministic','决定性的；必然决定结果的','not deterministic 限定人格与人生丰富性的关系，防止把概率当命运','The model describes a tendency rather than a deterministic rule.',['a deterministic relationship','not deterministic'],
 '那么，谁可能过心理丰富的人生？从人格特质看，经验开放且外向的人最可能如此。他们更可能做新事、遇见新人或学到新东西，像 Narcissus and Goldmund 中的 Goldmund。不过，这些关系并非决定性的。')

add(5,'推断','What possibility for introverts is supported by the examples?',
 ['They may find rich experiences through intellectual exploration or another person’s encouragement.','They must become extraverts before any intellectual journey is possible.','Their rich experiences are limited to visiting parks with Brad personally.','They are excluded from rich lives because they prefer fewer social contacts.'],0,
 '这些例子支持内向者的哪种可能性？',['可通过知识探索或他人带动获得丰富经历。','必须先变外向，才能有任何知识探索。','丰富经历只限于亲自和 Brad 游公园。','因偏好较少社交而被排除在人生丰富之外。'],
 ['A Gopnik 的知识旅程和有人引领的活动给出两条可能途径。','B 第一行明确有许多内向者人生丰富，无须先改变类型。','C someone like Brad 是类似引领者，非限定唯一人物。','D plenty of introverts 直接反对排除；might 保留可能，不是每次都会发生的保证。'],
 ['The type of intellectual journey that Alison Gopnik had is available to introverts who seek new intellectual knowledge.','Led by someone like Brad, introverted people might do something unusual.'],
 'intellectual journey','知识或思想探索的历程','不一定是地理旅行；可通过学习新知识获得丰富体验','Reading the letters began an intellectual journey for the student.',['an intellectual journey','seek new intellectual knowledge'],
 '有许多内向者过着心理丰富的人生。对寻求新知识的内向者，Alison Gopnik 那种思想探索之旅同样可行。同样，Joy Ryan 和孙子 Brad 去了许多国家公园。有像 Brad 那样的人引领，内向者也可能做不同寻常的事。','inference')

add(6,'细节','Which use of other personality traits does the author recommend?',
 ['Rejecting a partner’s suggestions to protect every existing routine.','Treating emotional stability as proof that new experiences are unnecessary.','Working conscientiously toward openness and accepting suggestions for adventure.','Waiting for all personality traits to become perfect before exploring anything.'],2,
 '作者建议怎样运用其他人格特质？',['拒绝伴侣建议以保护所有惯例。','把情绪稳定当成不必有新经历的证明。','认真努力地提高开放性，并乐于接受冒险建议。','等所有人格特质完美后才开始探索。'],
 ['A 原文 be agreeable to...suggestions 是接纳，不是拒绝。','B 第二层预测因素不排除新体验。','C conscientiously work 与 be agreeable 分别说明怎样利用尽责和宜人倾向。','D 没有先完美再行动的条件；作者强调 numerous ways 而非单一资格。'],
 ['conscientiously work on that goal','be agreeable to your friend’s and partner’s suggestions for a new adventure'],
 'expand your horizons','拓展眼界','指通过新冒险增加理解与经历，不是字面的地平线移动','Studying an unfamiliar art form can expand your horizons.',['expand your horizons','broaden your horizons'],
 '还应注意，尽责性、宜人性和情绪稳定性也是丰富人生的次要预测因素。这意味着，你可设定对新经历开放的目标，认真努力追求它，过心理丰富的人生。你也可以接纳朋友和伴侣提出的新冒险建议，拓展眼界。过心理丰富人生的方式确实很多。')

add(7,'逻辑关系','How strongly are the explanations for happiness presented here?',
 ['As the single proven cause of every happy life.','As partial explanations, with some explicitly qualified by “perhaps”.','As evidence that agreeable people never face disagreement.','As a denial that goal achievement has any relationship with happiness.'],1,
 '本段以多强的确定程度解释幸福？',['每种幸福人生唯一且已证实的原因。','部分解释，其中一些明确用 perhaps 限定。','证明宜人者从不遭遇任何分歧。','否认目标实现与幸福有任何联系。'],
 ['A tend、perhaps、in part 均避免唯一和必然。','B 两处 perhaps 和 in part 表明这是部分、带限定的机制解释。','C warm, conflict-free relationships 是作者描述的倾向，不是每个人永无冲突。','D 作者确实把目标实现作为尽责者可能更幸福的解释之一。'],
 ['perhaps in part because','perhaps because they tend to achieve their goals'],
 'in part','部分地；在一定程度上','限定解释范围，说明关系质量或积极态度不一定是全部原因','The delay was caused in part by bad weather.',['in part because','explain in part'],
 '谁幸福？外向且情绪稳定的人往往过幸福人生，或许部分因为他们往往拥有好关系，也能在多数处境中发现积极之处。尽责者也往往幸福，或许因为他们往往实现目标；宜人者往往幸福，部分因为他们与他人拥有温暖、少冲突的关系。')

add(8,'细节','What capacity is linked with meaning in this passage?',
 ['Changing causes whenever a minor worry appears.','Avoiding any lasting commitment to other people.','Eliminating every possible concern before taking action.','Devoting sustained effort to a few causes without excessive worry.'],3,
 '本段把哪种能力与意义感联系起来？',['一出现小担忧就换事业。','回避对他人的任何长期投入。','行动前消除每一种可能的担忧。','不过度担忧，长期投入少数几项事业。'],
 ['A extended period of time 表明持续，而非一遇担忧就转换。','B devote themselves 表示投入，非回避。','C without worrying too much 不是完全没有担忧。','D 对应 a few causes、extended period 和不过分担心；in part because 也不能扩大成唯一途径。'],
 ['devote themselves to a few causes for an extended period of time without worrying too much'],
 'devote themselves to','投身于；长期投入','指持续投入少数事业，不等于同时追逐所有目标','The volunteers devote themselves to preserving local history.',['devote oneself to a cause','devote time to a project'],
 '最后，谁过有意义的人生？尽责且情绪稳定的人往往如此，部分因为他们可以不过度担忧，长期投入少数几项事业，最终对世界产生影响。')

add(9,'主旨','Which contrast is central to the summary of personality correlates?',
 ['Openness is equally dominant in all three life dimensions.','Openness has no place in any good life.','Openness has a larger role in richness than in happiness or meaning.','Happiness and meaning are ruled out for anyone open to experience.'],2,
 '人格关联因素的总结，核心对比是什么？',['开放性在三个维度都同样占主导。','开放性在任何美好人生中都无作用。','开放性在丰富性中的作用，大于它在幸福或意义中的作用。','开放者不可能拥有幸福或意义。'],
 ['A 原文区分 minor 与 major。','B 文中明确说它对心理丰富性作用大。','C 第一、二句总结相对重要性的区别。','D relatively minor 不是绝对排除，也不是越开放就越不幸福的确定因果。'],
 ['openness to experience plays a relatively minor role in happiness and meaning, it plays a major role in a psychologically rich life.'],
 'correlates','相关因素；相关联的特征','personality correlates 指与人生维度相关的人格特征，不等同已证明的决定原因','The paper examined the correlates of life satisfaction.',['personality correlates','correlates of well-being'],
 '总之，在心理丰富人生与幸福、有意义人生的人格相关因素之间，经验开放性构成最显著的区别。它对幸福和意义的作用相对较小，对心理丰富人生却作用重大。关于心理丰富性的人格研究显示，接纳新经历是通往美好人生的一条道路。')

add(10,'作者意图','What practical use does the author propose for personality knowledge?',
 ['Use self-understanding and trait–life associations to develop strategies for a good life.','Use a personality score to assign every person a fixed destiny.','Take one test as a substitute for any later personal effort.','Choose the same life strategy regardless of any differences in personality.'],0,
 '作者建议怎样实际运用人格知识？',['利用自我认识及特质与人生维度的关联，制定美好人生策略。','用人格分数给每个人分配固定命运。','做一次测试就替代此后所有努力。','无论人格怎样不同，都采用完全相同策略。'],
 ['A know who you are 与 traits...associated 后，用 Harness...to develop strategies 明确用途。','B 不是定命运；本章前文已保留非决定性。','C 测试只是认识自己的一种提示，没有替代努力的承诺。','D 文中强调理解人格和不同人生维度，非抹掉差异。my website 归于书中作者，本网站不自动代做或跳转测试。'],
 ['Harness this understanding of our personality and the personality traits associated with psychological richness, happiness, and meaning to develop strategies for achieving the good life.'],
 'Harness','利用；把……用于某个目的','把人格理解转化为人生策略，不是控制或固定别人','The team hopes to harness local knowledge to improve the plan.',['harness understanding','harness knowledge'],
 '那么，人格心理学的一项启示是：了解自己是谁很重要（你可以在作者的网站上做大五人格测试）。了解哪些人格特质与美好人生的各维度相关，也同样重要。利用对自身人格以及与心理丰富、幸福、意义相关特质的理解，制定实现美好人生的策略。')

add(11,'作者意图','What is the purpose of the final encouragement to “Keep on reading”?',
 ['To insist that only people already high in openness can benefit.','To introduce practical tips while stressing that personality can change with effort.','To claim that reading alone instantly changes every personality trait.','To announce that the book has finished discussing psychological richness.'],1,
 '结尾鼓励 Keep on reading 的用意是什么？',['坚持只有原本高开放性者才能获益。','引出实际方法，并强调人格能随努力改变。','宣称只读文字就能立刻改变所有特质。','宣布全书已结束心理丰富性的讨论。'],
 ['A Even if 后列出相反特质，仍鼓励继续。','B following chapters give some tips 与 change with effort 共同说明继续读的理由。','C with effort 不等于只阅读即刻全部改变。','D following chapters 显示讨论仍将继续。书中祈使句是作者对读者的修辞内容，不是程序执行指令。'],
 ['The following chapters give some tips','personality can change with effort.'],
 'incorporate','纳入；融入','指把一点心理丰富性加入日常生活，不是彻底替换现有生活','She tried to incorporate short walks into her daily routine.',['incorporate something into','incorporate into everyday life'],
 '接下来的章节会给出一些方法，让我们都能把一点心理丰富性融入日常生活。即使你神经质倾向较高、不宜人、不尽责、内向、对新经历不开放，人格也可以随着努力而改变。不要放弃。继续读下去！')

add(12,'细节','What did McCrae and Costa’s 1980 study ask its 240 male participants to do?',
 ['Compete in an Olympic swimming event.','Practise household tasks for a fixed number of hours.','Become more open by taking a prescribed vacation.','Complete various unfinished sentences.'],3,
 'McCrae 与 Costa 的 1980 年研究要求 240 名男性参与者做什么？',['参加奥运游泳比赛。','按固定时数练习家务。','通过规定的度假提高开放性。','补全各种未完成的句子。'],
 ['A 竞技运动不是这项研究的任务。','B housework 出现在句子题干里，不表示研究要求实际做家务。','C 没有度假干预或指定人格改变任务。','D complete various sentences 明确程序；更开放者回答更俏皮属于所述比较，不能改成研究证明玩乐导致开放。'],
 ['asked 240 men to complete various sentences'],
 'playfulness','玩心；游戏般轻松的态度','在此通过句子补全回答中的俏皮程度体现，而非参与者实际从事某项运动','A little playfulness made the discussion more creative.',['embrace playfulness','a sense of playfulness'],
 '心理丰富人格的核心是经验开放性与外向性。但有人或许会问：缺少这些基本特质的我们，怎样变得更开放、更外向？一种回答是拥抱玩心。1980 年的一项研究中，Robert McCrae 与 Paul Costa 请 240 名男性补全“让我惹上麻烦的是……”和“当妻子请他做家务时……”等句子；开放男性的回答比不开放男性的回答俏皮得多。')

add(13,'推断','Which interpretation respects the contrasting housework responses?',
 ['They illustrate a playful twist, with the closed-minded contrast expressed conditionally.','They show that every open man actually refused all household work.','They prove that the researchers observed both men’s private homes.','They establish that reluctant housework makes all people closed-minded.'],0,
 '怎样理解家务回答的对比，才保留原文强度？',['它们说明俏皮的转折，而不开放者的对照用条件语气表达。','说明所有开放男性实际拒绝全部家务。','证明研究者观察了两人的私人家庭。','确立勉强做家务使所有人不开放。'],
 ['A invented an urgent excuse 带俏皮转折；would have responded 是条件性对照，不是所有人的实测原话。','B 句子补全回答不能直接当作实际家务行为，更不能扩大为每个人。','C 本段没有家庭观察程序。','D 没有这种确定因果方向。McCrae 与 Costa 的评论归于研究者，不必把每个比喻当字面事实。'],
 ['A closed-minded man would have responded','a playful, sometimes odd, sense of humor.'],
 'twist','出人意料的转折；意义上的变化','研究者说对句子含义稍作俏皮变化，不是身体扭转','The speaker gave the familiar story an unexpected twist.',['a slight twist','give a twist to a meaning'],
 '例如，一位高经验开放性的男性说：“当妻子请我做家务时，我编了个紧急借口。”不开放的男性则会这样回答：“当妻子请我做家务时，我勉强做了。”这里原文对后者使用条件语气。McCrae 与 Costa 观察道：“开放男性最后一个区分性特征，是俏皮、有时古怪的幽默感。他们可能稍稍扭转意思，也常对测试提出明显带玩笑性质的异议。”','inference')

add(14,'逻辑关系','What degree of certainty is conveyed by “may be central”?',
 ['Playfulness has been proved to be the sole cause of richness.','The three qualities have been ruled out as irrelevant.','The qualities are proposed as potentially important to both openness and richness.','Everyone must display all three qualities before having any rich experience.'],2,
 'may be central 表达什么确定程度？',['已证明玩心是丰富性的唯一原因。','已排除这三种特质，认定它们无关。','提出这些特质可能对开放性与丰富性都重要。','每个人必须先同时具备三者，才可能有任何丰富经历。'],
 ['A may 不等于已证明，central 也不等于唯一原因。','B may be central 不是排除。','C 保留可能性和 both 所涵盖的两个概念。','D 原句没有每个人必须满足的准入条件。'],
 ['may be central to both openness and psychological richness.'],
 'lightheartedness','轻松愉快；不沉重的态度','与玩心、古怪趣味并列的可能重要特征，不代表永不认真','The conversation had a welcome sense of lightheartedness.',['a sense of lightheartedness','playfulness and lightheartedness'],
 '因此，玩心、古怪趣味和轻松态度，可能对开放性与心理丰富性都很重要。')

add(15,'作者意图','What does Erikson’s “on vacation” expression suggest in context?',
 ['Adults must permanently give up economic responsibilities.','Playfulness offers a temporary release from ordinary adult demands.','Only a paid trip to another country can count as play.','Social and economic obligations are imaginary and do not exist.'],1,
 'Erikson 在这里说 on vacation，意在说明什么？',['成年人必须永久放弃经济责任。','玩心使人暂时从日常成年生活要求中抽离。','只有付费出国旅行才算玩。','社会与经济义务是不存在的幻想。'],
 ['A vacation 是暂时抽离的比喻，不是永久弃责。','B 后文承认成人确有许多责任，突出玩时的暂时解放感。','C 不是以付费或出国作为条件。','D All of us adults...responsibilities 明确认识现实责任。'],
 ['“on vacation from social and economic reality.”'],
 'on vacation','在休假；暂时抽离','这里是从社会经济现实的要求中暂时松开的比喻，不一定真实出游','During the game, she felt as if she were on vacation from everyday worries.',['on vacation from','go on vacation'],
 '但究竟什么叫有玩心？精神分析学家 Erik Erikson 的描述最贴切：有玩心时，你仿佛“从社会和经济现实中休假”。我们成年人都有许多社会与经济责任。这就是现实。')

add(16,'细节','Which pair of activities is actually suggested in this excerpt?',
 ['Abandoning every duty forever and becoming a full-time athlete.','Training with Steph Curry and being employed by Roger Ebert.','Replacing fantasy with financial planning at all times.','Imitating Curry while playing basketball and pretending to be Ebert while watching a film.'],3,
 '本片段实际建议了哪一对活动？',['永远放弃所有责任，并成为全职运动员。','与 Steph Curry 一起训练，并受雇于 Roger Ebert。','始终用财务规划取代想象。','打篮球时模仿 Curry，看电影时假装像 Ebert。'],
 ['A once in a while 限定偶尔，不是永远弃责。','B imitate 和 pretend 不等于真的与名人共事。','C fantasy and actuality 之间的活动并非排除想象。','D 两个祈使句分别给出运动模仿与观影扮演的例子。它们是书中学习文本，不会触发网站执行任何外部操作。'],
 ['Play basketball and imitate Steph Curry. Watch a movie and pretend to be like Roger Ebert.'],
 'actuality','现实；实际状态','与 fantasy 并列，描述偶尔在想象与实际之间游戏的空间','The design moved from an idea into actuality.',['fantasy and actuality','between fantasy and actuality'],
 '不过，Erikson 鼓励我们偶尔走到幻想与现实之间。让自己暂时从责任与义务中松开。打篮球时模仿 Steph Curry；看电影时假装自己像 Roger Ebert。')

add(17,'语境词义','What does “impersonate” mean in this suggestion?',
 ['Imitate someone’s manner or voice for a playful performance.','Become the legally appointed holder of someone’s office.','Write an official report on behalf of a government.','Prove that someone on the news is not real.'],0,
 '这个建议中的 impersonate 是什么意思？',['为玩乐表演而模仿某人的举止或声音。','依法就任对方的职务。','代表政府撰写正式报告。','证明新闻中的某人不存在。'],
 ['A 与同唱歌曲并列，语境是游戏式模仿。','B 模仿不等于取得总统职位。','C 本句没有官方授权或文书任务。','D 词义并非证明身份虚假；the president 保留书中一般称谓，不自行添入当前人物姓名。'],
 ['impersonate the president.'],
 'impersonate','模仿；扮演','此处指轻松模仿人物，不是本网站要求冒充身份或担任公职','The comedian can impersonate several familiar characters.',['impersonate a character','a playful impersonation'],
 '看晚间新闻时，模仿总统。跟着 Beyoncé 一起唱歌。')

add(18,'细节','Which detail is specifically reported about Phelps’s Olympic gold medals?',
 ['All thirteen were relay medals.','He won thirteen gold medals in individual Olympic events.','He won thirteen gold medals before he began training at eight.','He won every Olympic swimming event he entered.'],1,
 '关于 Phelps 的奥运金牌，本段具体报告什么？',['十三枚全部来自接力。','他在奥运个人项目中赢得十三枚金牌。','开始八岁训练前已赢得十三枚。','他参加的每个奥运游泳项目都夺冠。'],
 ['A individual events 与接力相反。','B thirteen、gold、individual 三项信息均对应。','C 把奖牌成就错误移到童年训练之前。','D widely considered one of the best 不等于每个项目必胜；本题定位原书叙述，不把数字扩写成个人与团体全部金牌总数。'],
 ['Michael Phelps won thirteen Olympic gold medals in individual events'],
 'at stake','有待争取；面临得失风险','表示大赛中得失重要，而不是某件物品立在木桩上','With the final contract at stake, the team checked every detail.',['a lot at stake','have something at stake'],
 '玩心的重要性，在得失重大的场合尤其明显，例如奥运会。Michael Phelps 在奥运个人项目中赢得十三枚金牌，广被认为是史上最优秀的游泳运动员之一。他八岁便已训练，打破各种年龄组纪录。')

add(19,'细节','Which training schedule is reported for Phelps?',
 ['Six days of training in total before an Olympic event.','Six hours a week spread across six months.','About six hours a day on six days each week.','One hour a day on every day of the year.'],2,
 '本段给出 Phelps 怎样的训练安排？',['奥运赛事前总共训练六天。','每周六小时，持续六个月。','每周六天，每天大约六小时。','一年每天都只练一小时。'],
 ['A per week 不是总共六天。','B 六小时是每日，不是每周，也无六个月限定。','C about six hours a day for six days a week 逐项对应，保留 about。','D 时数与频率均不符。这是人物训练叙事，不是对读者的训练处方。'],
 ['Phelps swam about six hours a day for six days a week.'],
 'soaked in','沉浸于；深处于','借游泳意象说明成长环境充满竞技游泳，不只是衣服被水浸湿','She grew up soaked in the language and stories of the region.',['be soaked in a world','grow up soaked in a culture'],
 'Phelps 从十一岁起继续在教练 Bob Bowman 指导下刻苦训练。姐姐 Hilary 也是奥运水平的游泳运动员。他在竞技游泳的世界中成长，深深浸润其中。他每周游六天，每天约六小时。')

add(20,'语境词义','What does “full of grit” emphasise about Phelps?',
 ['The amount of dirt present in his training pool.','A lack of any natural sporting talent.','An unwillingness to continue difficult training.','His determination and perseverance.'],3,
 'full of grit 突出 Phelps 的什么特点？',['训练池里泥沙很多。','完全没有运动天赋。','不愿继续困难训练。','他的决心与坚毅。'],
 ['A grit 此处是人格品质，不是泥沙。','B 原文明说 supremely talented。','C 坚毅与不愿坚持相反。','D 与举重、拉伸等努力相接，强调毅力；天赋与坚毅在句中并存，不需二选一。'],
 ['Michael Phelps is supremely talented and full of grit.'],
 'grit','坚毅；持久投入的韧性','指面对长期训练的坚持，不是物质颗粒','Finishing the long project required patience and grit.',['full of grit','show grit'],
 '他也举重和拉伸。Michael Phelps 天赋极高，而且充满坚毅。')

add(21,'细节','Which Rio 2016 events are named as Biles’s gold-medal events?',
 ['All-around, vault and floor.','Uneven bars, vault and swimming.','Only the team event, with no individual events named.','Floor, diving and the marathon.'],0,
 '本段点名 Biles 在 2016 里约奥运的哪些金牌项目？',['全能、跳马和自由体操。','高低杠、跳马和游泳。','只点名团体项目，没有个人项目。','自由体操、跳水和马拉松。'],
 ['A 对应 all-around、vault、floor。','B 原句没有点名高低杠，更无游泳。','C 文中列出三个具名项目，不能改成仅团体。','D 加入文中没有的其他运动。有关奖牌总排名的措辞依原书时点保留，不冒充最新赛事核验。'],
 ['gold medals in the all-around, vault, and floor events at 2016 Rio Olympics.'],
 'vault','跳马','在体操项目列表中指跳马，不是储藏室或撑竿跳','The gymnast practised her approach to the vault.',['the vault event','a vault routine'],
 'Simone Biles 是另一位非凡运动员。她在 2016 里约奥运的全能、跳马和自由体操项目赢得金牌。书中称，截至其叙述时，她赢得的奥运奖牌多于任何其他美国体操运动员。和 Phelps 一样，Biles 八岁开始认真训练。')

add(22,'逻辑关系','Why was Biles homeschooled, according to this passage?',
 ['Because she had given up gymnastics.','So that she could compete only once a year.','To make twenty to thirty-two hours of weekly training possible.','To avoid all forms of organised learning.'],2,
 '根据本段，Biles 为什么接受居家教育？',['因为已放弃体操。','为了每年只参赛一次。','以便每周能训练二十至三十二小时。','为了回避一切有组织的学习。'],
 ['A 与巨大投入相反。','B 文中无每年参赛次数。','C so that 明确说明安排教育方式的目的及训练时数。','D homeschooled 不等于没有教育，不能添加“回避一切学习”的动机。'],
 ['Simone was homeschooled so that she could train twenty to thirty-two hours per week.'],
 'unparalleled','无与伦比的；非凡的','作者强调她投入体操的程度，不是本段提供了量化比较所有人的实验','The small team showed unparalleled devotion to the archive.',['unparalleled devotion','unparalleled commitment'],
 '她天赋极高。Simone 接受居家教育，以便每周训练二十至三十二小时。她对体操展现了非凡的投入。')

add(23,'主旨','Why are swimming and gymnastics described as extremely high-pressure sports?',
 ['Because only the total number of training hours matters.','Because small mistakes are ignored once an athlete is talented.','Because swimmers and gymnasts face exactly the same scoring rules.','Because tiny timing or balance differences can seriously affect the result.'],3,
 '为什么作者把游泳与体操称为压力极大的运动？',['因为只看训练总时数。','因为只要有天赋，小失误都会被忽略。','因为两项运动的评分规则完全相同。','因为细微的时间或平衡差异，都能严重影响结果。'],
 ['A 本段强调训练以外的小细节同样关键。','B slightest loss...could ruin 表示小失误可能影响很大。','C 比较共同压力，不等于规则完全相同。','D 游泳胜负在瞬息之间，体操跌落或失衡会影响表现，两者共同支撑高压的概括。'],
 ['a win or loss is literally a matter of a split second.','the slightest loss of balance could ruin your performance.'],
 'split second','极短的一瞬；分秒之间','突出游泳胜负可能取决于极细微时间差，不给未写明的精确秒数','She changed direction in a split second.',['a split second','a matter of a split second'],
 '除了艰苦训练，很小的细节对游泳与体操都至关重要。游泳胜负确实取决于分秒之间。体操中，任何跌落或最轻微的失衡，都可能毁掉表现。换句话说，这些运动压力极大。')

add(24,'逻辑关系','What contrast is introduced by “Despite achieving spectacular success”?',
 ['Success prevented both athletes from ever feeling anxious.','Outstanding achievement coexisted with anxiety and depression in the account.','Their difficulties prove that every Olympian becomes depressed.','The passage gives a clinical experiment proving medals directly cause depression.'],1,
 'Despite achieving spectacular success 引出什么对照？',['成功使两人永远不会焦虑。','叙述中，非凡成就与焦虑、抑郁经历并存。','他们的困难证明每位奥运选手都会抑郁。','本段给出临床实验，证明奖牌直接导致抑郁。'],
 ['A despite 后的结果恰恰说明成功未排除困难。','B spectacular success 与 suffered from anxiety and depression 并列构成让步对照。','C 两个人物叙事不能推广为所有选手。','D 本段无临床实验、确定因果或网站对人物的新诊断；依原书报告保留经历，不提供医疗结论。'],
 ['Despite achieving spectacular success, both Michael Phelps and Simone Biles suffered from anxiety and depression.'],
 'dedication','投入；奉献；长期努力','a decade of dedication 突出赛前积累的努力与瞬间失误的反差','The restoration reflects years of dedication.',['a decade of dedication','dedication to a sport'],
 '一个小失误可能让你失去奖牌。而且，奥运会每四年举行一次，准备周期极长。一个瞬间就可能夺走梦想与十年的投入。尽管成就非凡，书中叙述 Michael Phelps 与 Simone Biles 都曾经历焦虑和抑郁。')

add(25,'逻辑关系','What qualification does the author add to the praise of single-minded dedication?',
 ['Too much single-mindedness could take away the simple joy of movement.','Any dedication is worthless and should be abandoned.','Winning medals guarantees lasting enjoyment of sport.','All athletes must choose between talent and happiness.'],0,
 '作者赞扬专注投入之后，增加了什么限定？',['过度专注可能夺走单纯运动的快乐。','任何投入都无价值，应全部放弃。','赢奖牌保证持续享受运动。','所有运动员必须在天赋与幸福之间二选一。'],
 ['A But、too much、could 三处共同限制过度投入可能带来的代价。','B surely admirable, even virtuous 明确认可投入本身。','C 开头说他们失去了对擅长运动的兴趣，不能认定奖牌保证乐趣。','D 文中没有所有运动员或天赋与幸福必然互斥的命题；这里是论述与人物例子，不是普遍因果实验。'],
 ['too much single-mindedness could rob you of the simple joy of just being able to jump, run, or swim.'],
 'single-mindedness','专心一意；只盯一个目标的倾向','本段区分可敬的专注与 too much 的过度专注，不是把努力一概否定','Her single-mindedness helped the project, but she also made time to rest.',['too much single-mindedness','single-minded dedication'],
 '他们对自己最擅长的运动失去了兴趣。专心一意地投入当然值得钦佩，甚至可称为美德。但是，过度专注可能夺走仅仅能够跳跃、奔跑或游泳的简单快乐。')

assert len(out)==25 and [q['id'] for q in out]==[t['questionId'] for t in targets]

def persist():
 path=ROOT/'source/short-questions/additional.json';existing=load('source/short-questions/additional.json');byid={q['id']:q for q in existing}
 for q in out:
  if q['id'] in byid:assert byid[q['id']]==q,('Refuse to overwrite changed authoring',q['id'])
  else:existing.append(q)
 path.write_text(json.dumps(existing,ensure_ascii=False,indent=2)+'\n',encoding='utf8',newline='\n')
 review=dict(batchId='batch-017',date='2026-10-22',pdfSha256=b['pdfSha256'],checkedPdfPages=list(range(65,70)),questionIds=[q['id'] for q in out],paragraphs=[dict(id=pid,textSha256=hashlib.sha256(pp[pid]['text'].encode()).hexdigest()) for pid in dict.fromkeys(q['paragraphId'] for q in out)],note='完整 PDF 65–69 页视觉核对，包括第6章结尾跨页内容与第7章开篇。保留非决定性、perhaps/may/could 和条件句；区分人物信念与事实、人格术语与临床诊断、句子补全回答与实际家务行为、假想对照与实测，以及竞技叙事与普遍因果。候选句界不是人工最终分句。')
 (ROOT/'source/short-questions/review-chapter06-07-next25.json').write_text(json.dumps(review,ensure_ascii=False,indent=2)+'\n',encoding='utf8',newline='\n')
 print('Saved',len(out),'of 25 individually authored exercises')

if __name__=='__main__':persist()
