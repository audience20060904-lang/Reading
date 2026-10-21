"""Batch 003: individually authored questions after PDF 17-26 visual comparison.
Executed only by the offline content-authoring script, never by the website.
The new IDs append to chapter 2; final reading order is sorted independently.
"""
V.update({
 'takeheart':vocab('take to heart','认真看待；深受影响','人们把先假装成功再取得成功的说法当真','She took the advice to heart and practised daily.','take advice to heart','take a remark to heart'),
 'assume':vocab('assume','认为；假定','最后的问句推测人们可能持有的信念，未确认事实','We should not assume that silence means agreement.','assume that','assume responsibility'),
 'intervention':vocab('intervention','干预','实验要求参与者表现得外向这一操作','The intervention involved a short conversation.','an experimental intervention','the effect of an intervention'),
 'anticipated':vocab('anticipated','预期；预料','与陌生人交谈后的幸福感超过事前预计','The journey took longer than we had anticipated.','anticipate a change','as anticipated'),
 'alienating':vocab('alienating','使疏离的；让人感到格格不入的','快乐压力使负面感受显得不被接纳','The formal language can be alienating to new readers.','an alienating experience','feel alienated from'),
 'thrown':vocab('thrown off','被弄糊涂；感到意外','作者因对方反过来感谢他而一时困惑','The unexpected question threw me off.','be thrown off by','throw someone off balance'),
 'assumed':vocab('assumed','以为；假定','年轻女子误以为作者是给她送餐的人','I assumed the bag belonged to my neighbour.','assume someone is','a widely assumed connection'),
 'cocky':vocab('cocky','自负的；过分自信的','故事中 Kahneman 与导师讨论的一种性格','The player sounded confident without being cocky.','a cocky attitude','sound cocky'),
 'while':vocab('while','而；然而','对照作者没有获得面试与同门获得面试','Mia chose the train, while Leo drove.','while others','while in contrast'),
 'impulsive':vocab('impulsive','冲动的','不健康情绪应对中的冲动购物','An impulsive purchase can disrupt a budget.','impulsive shopping','impulsive behaviour'),
 'defects':vocab('defects','缺点；缺陷','小说中对 soma 的宣称，不是实验确认的药效','The inspection revealed several defects in the design.','a design defect','identify defects'),
 'reinterpret':vocab('reinterpret','重新解释','改变对同一事件的理解方式','She reinterpreted the delay as time to prepare.','reinterpret an event','reinterpret something as'),
 'dampen':vocab('dampen','减弱；抑制','从另一视角看事件可能减轻负面反应','The rain did not dampen their enthusiasm.','dampen a reaction','dampen enthusiasm'),
 'linger':vocab('linger','持续逗留；迟迟不消失','让负面心情短暂存在，而不立即强行修复','The scent lingered in the room.','linger for a while','a lingering doubt'),
 'underestimate':vocab('underestimate','低估','人们低估自然恢复情绪的能力','Do not underestimate the time needed for revision.','underestimate the power of','seriously underestimate'),
 'satisfactory':vocab('satisfactory','令人满意的；达到要求的','满足者选择达到要求的方案，而不穷尽最佳方案','The team found a satisfactory solution.','a satisfactory choice','satisfactory results'),
 'maximizer':vocab('maximizer','最大化追求者；力求最优者','择校例子中努力寻求能进入的最佳学校的人','A maximizer may compare every available option.','a maximizer mindset','maximizers and satisficers'),
 'upward':vocab('upward social comparison','向上社会比较','把自己与更成功或更富有的人相比','Upward social comparison can shift a person’s goals.','engage in upward social comparison','avoid upward social comparison'),
 'obsessed':vocab('obsessed','着迷的；过度执着的','研究结尾所描述的过度关注社会比较者','He became obsessed with checking the results.','be obsessed with','obsessed with comparison'),
 'curated':vocab('curated','精心挑选、编排的','社交媒体图像经过选择，并非他人生活全貌','The museum displayed a carefully curated collection.','carefully curated images','a curated collection'),
 'inferior':vocab('inferior','较差的；低人一等的','看到别人炫耀时产生的自我评价','She felt inferior despite her strong performance.','feel inferior to','an inferior product'),
 'coziness':vocab('coziness','舒适温馨感','作者对 hygge 的解释之一','The warm lighting added coziness to the room.','a sense of coziness','coziness and comfort'),
 'contentment':vocab('contentment','满足；知足','丹麦段落强调对现有生活感到满足','He found contentment in a simple routine.','a life of contentment','a sense of contentment'),
 'gratify':vocab('gratify','使满意；取悦','尼采引述中为避免受伤而迎合众人的行为','The result will gratify the supporters.','please and gratify','gratify a desire'),
 'virtue':vocab('virtue','美德；德行','引述质疑被称作美德的怯懦与迎合','Patience is a virtue worth practising.','a moral virtue','be called a virtue'),
 'seductive':vocab('seductive','诱人的；有吸引力的','小幸福与意义吸引人选择安稳惯常生活','The promise of instant success can be seductive.','a seductive idea','a seductive promise'),
 'convention':vocab('convention','惯例；传统规范','使人趋于和谐、避免冲突的常规生活方式','The artist chose to challenge convention.','be drawn to convention','challenge convention'),
 'richness':vocab('richness','丰富性','悲伤等感受可为内心生活增添的层次','The novel captures the richness of ordinary life.','the richness of experience','add richness to'),
 'reflect':vocab('reflect on','认真思考；反思','作者请已经幸福的读者审视自己的满足心态','Take a moment to reflect on your priorities.','reflect on a decision','time to reflect on')
})

add(34,'作者意图','What is the function of the final question beginning with “Likewise”?',
 ['It establishes that pretending to be happy reliably improves mood.','It raises a possible belief by analogy with accounts of apparent success.','It reports participants’ answers to a study of American happiness.','It concludes that successful people no longer need to pretend.'],1,
 '作者从两则关于先假装成功的叙述转向一个疑问：人们是否也会以为装快乐能变快乐？might 和问号保留不确定性。这些职业、产品故事没有证明情绪干预的效果。',
 ['A 把推测性问句改成可靠的效果结论；该段并未进行幸福干预实验。','B Likewise 建立类比，might many Americans assume 提出可能存在的信念。','C 问句来自作者，没有报告美国参与者回答或样本。','D 前文叙事没有推出成功者从此无需假装这一结论。'],
 ['Likewise, might many Americans assume that, if they pretend to be happy, they will eventually become happy?'],['takeheart','assume'],
 '主干是 might many Americans assume...?：情态动词 might 前置构成一般疑问句。assume 后接 that 宾语从句，其中 if they pretend... 是条件从句，主句为 they will eventually become happy。might 表推测，不是已经观察到的事实。',
 '作者意图题要区分类比、提出问题和证明结论。Likewise 提示从前面事例迁移到新话题；情态词和问号限制论证强度，不能选确证因果的选项。',ctx='all',
 translation='那么，人们为什么要假装幸福呢？当然，有句俗话叫“先装成那样，直到真正做到”。许多人把这样的信念放在心上：如果一直假装自己成功，最终就会成功。昆汀·塔伦蒂诺后来编剧并执导了《低俗小说》等标志性电影；当时他还在加利福尼亚曼哈顿海滩的一家录像店当店员。为了得到在好莱坞担任制片助理的第一份工作，他谎称自己有电影行业的工作经历。史蒂夫·乔布斯也曾先假装做到，后来才真正做到。第一代 iPhone 有内存问题，无法同时运行多个程序。在第一代 iPhone 的产品发布会上，乔布斯用了多部手机；旧手机演示崩溃后，就换成一部新的。它还有带宽问题。因此，当台上的 iPhone 连接不佳时，他们作了假，始终显示五格信号。后来，苹果修复了内存问题。同样地，许多美国人是否也会以为，只要假装幸福，最终就会真的幸福呢？')

add(36,'同义改写','Which statement best preserves the reported result of the extraversion experiments?',
 ['Only people who were already extraverts reported greater happiness.','The studies established that fake smiling works as reliably as social interaction.','Acting more extravertedly increased reported happiness, even among natural introverts.','Talking to strangers produced the amount of happiness participants had expected.'],2,
 '片段说明被要求表现外向者事后报告更幸福，这种干预对天性内向者也有效；与陌生人交谈的结果还比事先预期更好。结论有 does tend to 的倾向性限制，不等于永久改变性格。',
 ['A only 排除了原文明示的 natural introverts。','B 末句把表现外向与假笑区分开，不能把两类证据合并成同等可靠。','C 保留行为干预、报告结果及内向者也受益三个信息。','D 原文是 far happier than they had anticipated，不是符合原先预期。'],
 ['Afterward, they reported more happiness than those who were asked to behave normally.','Surprisingly, the intervention worked even for natural introverts.'],['intervention','anticipated'],
 'those who were asked... 中 who 引导定语从句，were asked to behave 是被动结构。even for natural introverts 中 even 强调超出预期的适用人群。末句 does tend to 用 does 强调谓语，但 tend to 仍表示倾向。',
 '改写题同时核对比较对象和适用人群：more...than 比较两种行为条件，even 扩展到内向者。干预结果不能改成固定性格分类，更不能套用到另一项假笑研究。',ctx='all',
 translation='还有许多实验要求参与者表现得像外向者。事后，他们报告的幸福感比被要求正常表现的人更高。令人惊讶的是，这种干预甚至对天性内向者也有效。同样，当人们被要求与陌生人交谈，也就是表现得像外向者时，他们感到的幸福远远超过自己事先的预期。这些发现已被重复验证。因此，即使假笑未必能让人更幸福，表现得像外向者的确往往能使人更幸福。')

add(39,'逻辑关系','Why does the author place “And yet” before the statement about negative emotions?',
 ['To deny that pressure changes how people view sadness.','To show that unavoidable feelings conflict with the demand to be happy.','To explain that criticism is less upsetting than missing a train.','To introduce the second face of the happiness trap in full.'],1,
 '前面说快乐压力让悲伤、愤怒等显得不可取且令人疏离；And yet 转向现实限制：负面情绪无法完全避免，遭遇不顺时难受是自然的。段首说有两面，不代表后面已完整介绍第二面。',
 ['A yet 不是否定前面压力的影响，而是指出这种要求与情绪现实的冲突。','B 对应 not possible to avoid 与前句 undesirable and alienating 的反差。','C 火车、批评、孩子不感恩是并列事例，没有程度排名。','D 此段标出 First 并继续解释第一面；第二面尚未在此完整展开。'],
 ['First, there is the pressure to be happy, which makes feeling sadness, anger, and anguish seem undesirable and alienating.','And yet it is not possible to avoid negative emotions.'],['alienating'],
 'which 引导非限制性定语从句，修饰 the pressure to be happy；makes 后接 feeling... 作宾语、seem... 作补足语。it is not possible to avoid... 中 it 是形式主语，不定式是真正主语。三个 when 从句并列，主句为 you feel bad。',
 '逻辑题先确定连接词两侧的命题。这里是规范压力与不可避免的现实之间的让步转折，不是事例之间的因果或程度比较。',ctx='all',
 translation='幸福陷阱有两面。首先，是必须幸福的压力，它使悲伤、愤怒和痛苦等感受显得不受欢迎，并让人感到格格不入。然而，负面情绪不可能完全避免。当你错过火车、有人批评你，或孩子对你所做的一切毫无感激之意时，你会感到难受。这再自然不过了。')

add(40,'语境词义','In the doorway anecdote, “completely thrown off” most nearly means that the author was:',
 ['physically prevented from entering his building.','pleased to be recognised by a neighbour.','uncertain whether he had ordered the correct food.','confused by an unexpected response.'],3,
 '女子反过来说 Thank YOU 使作者一时困惑，接着 Then I realized 才揭示她误以为他在给她送餐。thrown off 在这里不是身体上被推开或赶走。',
 ['A 把短语作字面动作理解；女子实际上给作者开了门。','B 她把作者误认成送餐员，而非认出邻居；作者后来感到受辱。','C 没有怀疑自己点错餐的内容，误会涉及身份和食物去向。','D 对应出乎意料的回应以及随后才明白误会的时间顺序。'],
 ['When she replied, “Thank YOU!” I was completely thrown off.','Then I realized: she assumed I was the Chinese deliveryman bringing her food.'],['thrown','assumed'],
 'When she replied... 为时间状语从句，主句 I was completely thrown off 使用被动形式的习语。she assumed 后省略 that；bringing her food 是现在分词短语，后置修饰 deliveryman，不能修饰年轻女子。',
 '短语词义要用前后事件验证。Then I realized 提供认知变化线索；注意 her food 是女子以为送给她的食物，不是作者实际送货的事实。',ctx='all',
 translation='例如，我在纽约生活时就多次遇到过这样一件事。我住的楼没有门卫。一天，我从附近的中餐馆买了外卖回到楼前，一位年轻女子替我开了门。我说：“谢谢！”她却回答：“该谢谢你！”这让我完全摸不着头脑。随后我才明白，她以为我是给她送餐的中国外卖员。我读研究生时发生过这种事，当上正教授后也遇到过。我觉得受到了侮辱。不过，生活中总会有这种事，对吧？')

add(41,'细节','What outcome does the author explicitly report one week after the conversation?',
 ['His lab mate received an interview that he himself did not receive.','His advisor withdrew his application before Princeton considered it.','His lab mate accepted the Princeton job instead of him.','Kahneman interviewed him but rejected him after the meeting.'],0,
 '明确结果是作者没得到面试，而那位被称为 cocky 的同门得到了。原文没有交代最终聘任，也没有说导师撤回申请；故事不能被扩写成招聘全过程。',
 ['A 对应 did not get the job interview 与 lab mate did 的对照。','B 导师谈及另一位学生，不等于正式撤回作者申请。','C 面试机会不等于录用或接受职位，结果范围被扩大。','D 作者没有获得面试；不存在该段所说的面试后拒绝。'],
 ['A week later, I found out that I did not get the job interview at Princeton, while my “cocky” lab mate did!'],['cocky','while'],
 'found out 后接 that 宾语从句。while 连接对照分句；my lab mate did 中 did 代替 got the job interview，避免重复，不是 got the job。引号中的 cocky 沿用故事里对性格的称呼。',
 '细节题严格区分申请、面试、录用、接受职位四个阶段。把 interview 省略后误补成 job，是常见的结果扩大干扰；助动词 did 要回指最近的完整谓语。',ctx='all',
 translation='说到研究生院，我读博士五年级时，导师告诉我这样一个故事。普林斯顿的著名心理学家丹尼尔·卡尼曼给我的导师埃德·迪纳打电话，向他打听我。当时，我申请了普林斯顿的一个助理教授职位。他们聊了一会儿后，卡尼曼问导师：“Shige 自负吗？”导师回答：“不，他不自负。”卡尼曼说：“嗯，要在普林斯顿生存下去，就得有些自负。”然后，我想，导师做了一个好导师会做的事：“我还有另一个学生，他很自负。”一周后，我得知自己没有获得普林斯顿的面试机会，而那位“自负”的同门却得到了！世界并不总是公平的，不是吗？')

add(43,'作者意图','How should the description of “soma” be read in this passage?',
 ['As the author’s prescribed method for recovering from a low mood.','As a result showing that every mood-repair method is unhealthy.','As a fictional illustration within a discussion of responses to low mood.','As evidence from a clinical comparison of pills and exercise.'],2,
 'soma 出现在 In Brave New World, Aldous Huxley writes 引导的小说引述中，用来穿插说明人们如何应对心情低落。引号中的优势宣称属于作品文本，不是作者推荐或临床研究结果。',
 ['A personally 后作者说的是听歌、交谈、午睡，没有推荐服用 soma。','B 段落明确同时列出 healthy 与 unhealthy 做法，不能一概视为有害。','C 引述来源及上下文都支持“文学例子”这一性质。','D 没有临床样本、比较设计或实验药效数据；把小说设定当证据。'],
 ['In Brave New World, Aldous Huxley writes, “What you need is a gramme of soma,” a pill that has “all the advantages of Christianity and alcohol; none of their defects.”'],['impulsive','defects'],
 'Some people...while others... 用 while 并列对照不同应对方式。a pill that has... 是 soma 的同位说明，that 从句修饰 pill；has 的内容仍处在小说引用框架内。Personally 标记转入作者自己的事例。',
 '先识别证据类型和观点归属。作品名、writes 和引号说明是文学引述；不能凭引语中的 all / none 就认为作者给出了医学或实验结论。',ctx='all',
 translation='感到必须快乐的人几乎会尝试一切办法来修复心情。有些人做很健康的事，例如锻炼和徒步；另一些人则做很不健康的事，例如过量饮酒或冲动购物。在《美丽新世界》中，奥尔德斯·赫胥黎写道：“你需要的是一克 soma。”这种药丸据称具备“基督教与酒精的一切好处，却没有它们的任何缺点”。就我个人而言，心情低落时会听最喜欢的歌，有时还会跟着唱。其他时候，我会与妻子交谈。她不在身边时，我就打个盹。')

add(44,'主旨','What do the approaches in the paragraph mainly have in common?',
 ['They remove the original event from the person’s memory.','They change the perspective through which an upsetting event is viewed.','They require the other person to agree to reverse the event.','They treat future distress as certain to be worse than present distress.'],1,
 '正面重释事件、从另一个人的视角看、从未来自己的视角看，都改变理解事件的角度，而非抹去事件或控制他人。末尾说未来可能只像小颠簸，保留 might。',
 ['A 视角变化不等于失去或删除记忆。','B 可统摄 reinterpret、other person’s perspective 和 future self 三种做法。','C 父亲、前妻和未来自己是说明视角的例子，没有要求他人撤销离婚。','D 与未来或许只像小颠簸的例子相反，还把可能性改成必然。'],
 ['For instance, people can try to positively reinterpret the event.','Others try to see themselves from the perspective of their future self.'],['reinterpret','dampen'],
 'try to reinterpret / try to distance / try to see 都是不定式作 try 的宾语；start seeing 用动名词。which could dampen... 的 which 对前面的换位看法作补充，could 仅表可能作用；will I be suffering 使用将来进行时设想未来感受。',
 '主旨题寻找多个例子的共同机制，而非选某个离婚细节。视角改变是共同上位概念；记忆删除、改变他人和情绪必然恶化均超出片段。',ctx='all',
 translation='应对持续的负面心情，还有更精细的方法。情绪调节研究者把它们分为几个主要类别。例如，人们可以尝试正面地重新解释事件。一个有两个年幼孩子的离异父亲，可能把离婚重新理解为天赐的机会：前妻照看孩子时，自己可以有更多时间从事爱好。另一些人可能尝试与离婚事件拉开距离，从另一个人的角度看同一件事，这可能减弱他们对触发事件的负面反应。还有些人尝试从未来自己的视角看待现在的自己。五年后，我还会同样痛苦吗？到了未来，这件事可能只像人生道路上的一次小颠簸。')

add(46,'逻辑关系','Which sequence of ideas best matches the author’s argument?',
 ['Mood-repair habits strengthen the immune system, which creates pressure to be happy.','All negative moods result from shopping, so shopping must stop before recovery.','Natural recovery is underestimated, while pressure can encourage reliance on unhealthy coping.','Emotional acceptance removes every need for active emotion regulation.'],2,
 '段首说低估心理免疫系统，并转而严重依赖自制的情绪修复办法；条件句设想减少快乐压力、让心情暂时存在后自然恢复机制发挥作用。末句警告可能走向不健康应对。potentially 不能改成必然，讨论的是原文论证而非个体诊疗规则。',
 ['A 把压力与应对方式的论证方向倒置，原文没有说这些习惯增强免疫系统。','B 购物被列为可能的应对方式，非所有负面心情的起因。','C 同时保留 underestimate、pressure 与 potentially destructive coping 的关系。','D 片段没有 every；不能把自然恢复改成彻底否定一切主动调节。'],
 ['What is surprising is how much people underestimate the power of their psychological immune system and instead rely heavily on their homemade remedies for mood repair, from alcohol to sweets to shopping.','This element of the happiness trap leads us down a potentially destructive path of unhealthy coping.'],['linger','underestimate'],
 'What is surprising 是 what 引导的主语从句，is 后为 how much 引导的表语从句。If we didn’t feel...and simply let... 中两个动词并列；主句 would kick in, attack...and remove... 使用假设条件结构，不是一次已经发生的实验记录。',
 '逻辑关系题用箭头复原作者的方向，并保留 potentially。识别虚拟条件句，可避免把作者解释性假设误写成已完成的随机实验结论或放之四海的建议。',ctx='all',
 translation='令人惊讶的是，人们如此低估自身心理免疫系统的力量，反而严重依赖自己想出的心情修复办法，从酒精、甜食到购物。如果我们没有感到那么大的快乐压力，只是让负面心情暂时停留一会儿，自身的心理免疫系统就会开始起作用，攻击不幸福这一“心理病毒”，并把它清除。幸福陷阱的这一方面，把我们引向一条可能具有破坏性的不健康应对道路。')

add(47,'细节','What distinguishes the satisficer in the college-choice example?',
 ['The student chooses a satisfactory option that meets stated needs.','The student lacks the grades required to consider elite universities.','The student applies to every school before choosing the cheapest offer.','The student treats the highest possible prestige as the only requirement.'],0,
 '满足者并非能力不足；原文说其很可能也能进入常春藤或杜克等学校，但认为 UVA 满足所需且可享州内学费，所以只申请那里。good enough 指达到自身要求。',
 ['A 对应 satisfactory choice 与 UVA has everything I want。','B 原文明确说 could probably get into...elite schools，不能把满足者定义为成绩不够。','C 只申请 UVA，不是先穷尽学校；也没有把最低学费作为唯一标准。','D best possible college 是最大化追求者的思路，观点归属错配。'],
 ['If you are the type of person who often accepts “good enough,” also known as a “satisficer”—one who sacrifices the best choice for a satisfactory choice—you are much more likely to be happy with your decisions.','You apply only to UVA and get in.'],['satisfactory','maximizer'],
 'one who sacrifices... 是 satisficer 的同位解释，who 引导定语从句。If you are... 主句为 you are much more likely...；be likely to do 表可能性，much 修饰比较级 more likely。only 的位置限定申请学校数量。',
 '定义题先找同位解释，再用事例验证。不要把“主动接受足够好”误读成“因条件不足被迫接受”，也不要把一个学费理由扩大成唯一标准。',ctx='all',
 translation='幸福陷阱的第二个方面是：如果你不要求得到过多的幸福，反而更容易获得幸福。社会心理学家巴里·施瓦茨发现了“足够好”的力量。如果你常常接受“足够好”，也就是所谓“满足者”——放弃最佳选择而接受令人满意选择的人——你就更可能对自己的决定感到满意。假设你是高中毕业班学生，GPA 几乎完美，SAT 分数很高，还参加过许多课外活动。你想去哪所大学？你可能想去自己有能力进入的最好的大学，于是申请了十所学校。如果你是这样的人，你就是最大化追求者。现在假设你是满足者：你很可能也能进入常春藤盟校，或杜克之类的顶尖学校。但你却说：“我觉得弗吉尼亚大学具备我想要的一切，而且我能享受州内学费。”你只申请 UVA，并且被录取了。')

add(49,'作者意图','What does Jim Clark’s sequence of wealth targets chiefly illustrate?',
 ['Financial success guarantees satisfaction once a fixed target is reached.','Every successful entrepreneur measures happiness in exactly the same way.','Comparing fortunes proves that wealth is unrelated to any life outcome.','Repeated success need not end dissatisfaction when comparison targets keep moving.'],3,
 '目标从一千万变成一亿、十亿，后来又变成比 Larry Ellison 更富。该事例说明成功后参照点仍可不断抬高，不能单凭达到目标就保证知足。作者对 Clark 是否满足用 I wonder 发问，并未测定其内心状态。',
 ['A 一再更换目标正好削弱固定财富门槛能保证满足的想法。','B 只有一个人的叙述，不能推广到 every entrepreneur。','C 该段讨论向上比较与幸福，不支持财富与所有人生结果毫无关联。','D need not 保留有限结论，moving targets 概括目标逐次变化。'],
 ['He now thought he would be happy if he made $100 million.','Now he said, “I want…more money than Larry Ellison. Then I will stop.”'],['upward','obsessed'],
 'who cofounded Netscape 为非限制性定语从句。thought 后 would be happy 是过去视角下的将来；if he made... 为条件从句。despite 后接名词短语 his enormous success，表示成就与满足疑问的反差。',
 '例证意图题概括变化规律，而非盯住某个金额。区分人物故事、作者疑问和结尾研究的相关结果；不能把人物例子升级为所有富人的确定因果规律。',ctx='all',support='inference',
 translation='与最大化心态密切相关，向上社会比较也是不幸福的另一个来源。网景联合创始人吉姆·克拉克作为硅谷企业家取得了一连串成功。他向记者迈克尔·刘易斯回忆，起初曾觉得只要赚到一千万美元就会幸福。但后来网景大获成功，他又觉得赚到一亿美元才会幸福。再一次巨大成功后，他觉得赚到十亿美元才会真正幸福。后来他确实赚到了十亿美元。现在他却说：“我想要……比拉里·埃里森更多的钱。然后我就停下来。”据《福布斯》，2023 年克拉克的净资产为 38 亿美元，而埃里森为 1580 亿美元。尽管克拉克极其成功，我仍不知道他是否曾真正感到满足。关于这一点，研究发现很清楚。索尼娅·柳博米尔斯基和李·罗斯发现，不进行向上社会比较的人，比痴迷于社会比较的人更幸福。')

add(50,'作者意图','Why does the author recall the story about trash bags and suitcases?',
 ['To show that social comparisons can be resisted by accepting difference.','To establish that suitcases cause students to feel inferior.','To prove that carefully curated images reveal complete lives.','To suggest that matching others’ possessions resolves social comparison.'],0,
 '故事中父亲用“与众不同没有关系”回应行李箱差异；末尾又把这句话用于社交媒体上感到自卑的读者。它支持接纳差异、抵抗向上比较，并非证明某类行李造成情绪。',
 ['A 把中间故事与段尾对读者的提醒连接起来。','B 故事里出现物品差异，不是行李箱导致自卑的因果实验。','C carefully curated 指精心挑选，不能当成完整生活；也非该故事的功能。','D 父亲没有让孩子买同款行李箱，重点是无需模仿别人。'],
 ['When you feel inferior to others who are showing off on social media, remember Mr. Johnson’s dad. It is OK to be different.'],['curated','inferior'],
 'With social media 是背景介词短语；we are bombarded 使用被动结构。who are showing off... 修饰 others；When you feel inferior... 是时间或条件性质的状语从句，主句 remember 为祈使句。',
 '作者意图题留意故事之后的回扣句，特别是从人物回到 you 的位置。可将事例概括为接纳差异，但不能编造实验因果或反向推出必须购买同类物品。',ctx='all',
 translation='有了社交媒体，我们不断受到他人精心挑选的图像轰炸。其他人似乎都过得无比精彩！避免向上社会比较很难，但并非不可能。我记得夏洛茨维尔布福德中学校长约翰逊先生，曾向我们这些家长和学生讲过他在 UVA 读大学时的故事。搬入学校那天，这位来自田纳西州的非裔美国人用一堆黑色垃圾袋装着自己的东西。他注意到其他 UVA 学生都用行李箱，于是问当房屋油漆工的父亲：“我们为什么没有行李箱？”父亲怎么回答？“孩子，与众不同没有关系。”当你看到别人在社交媒体上炫耀而自觉不如别人时，请记住约翰逊先生父亲的话：与众不同没有关系。')

add(51,'语境词义','How does the passage explain “hygge”?',
 ['Competitive ambition directed at Denmark’s national ranking.','Comfort and modest everyday pleasures associated with contentment.','A rule requiring everyone to avoid long-term expectations.','The BBC’s method for calculating international happiness scores.'],1,
 'hygge 后面的 the coziness and small joys of life 是直接解释，随后连接知足的生活。它不是幸福排名的计算方法，也不是强制所有人放弃计划的规则。',
 ['A 排名解释 BBC 为何采访，不是 hygge 的词义。','B 对应同位解释及 a life of contentment。','C 受访者说对人生期待不多，不能扩大成 everyone 必须遵守的规范。','D BBC 在此寻找幸福秘诀，没有说明其统计方法。'],
 ['Like my father, many Danes cherish hygge, the coziness and small joys of life, along with the idea of a life of contentment.'],['coziness','contentment'],
 'Like my father 是前置比较短语，主语仍为 many Danes。the coziness and small joys of life 是 hygge 的同位语；along with 连接另外珍视的观念，不改变主谓关系。',
 '陌生词后紧接逗号加释义名词短语时，优先识别同位解释。分清引入采访的背景、被解释的词和受访者的看法，避免把范围扩大成普遍规则。',ctx='all',
 translation='由于丹麦经常跻身世界最幸福国家之列，BBC 前往采访丹麦人，寻找幸福的关键。秘诀是什么？许多丹麦人说，他们对人生没有太多期待。降低期待，对自己已有的东西感到满足，这是丹麦人的智慧。和我的父亲一样，许多丹麦人珍视 hygge，也就是生活的温馨舒适与小小乐趣，同时珍视一种知足的生活理念。')

add(53,'有限推断','In the quoted passage, why is pleasing everybody criticised?',
 ['It demonstrates that the speakers have attained the highest possible virtue.','It prevents anyone from enjoying even a small amount of contentment.','It is portrayed as an attempt to avoid being hurt, even when called virtue.','It is shown by an experiment to reduce all forms of happiness.'],2,
 '引述先说这些人最想要无人伤害自己，接着用 Thus 引出取悦所有人的做法，再评价这是怯懦，即使名为美德。这个推断仅限引述中的评价，不是实验发现或所有礼貌行为的定义。',
 ['A 引述质疑被称作美德的行为，没有赞为最高德行。','B 这些人恰恰追求小幸福与知足，非完全失去满足。','C 串联 nobody should hurt them、Thus 与 even if it be called virtue，保留观点归属。','D 文学哲学引述没有实验设计，all forms 也扩大范围。'],
 ['At bottom, these simpletons want a single thing most of all: that nobody should hurt them. Thus they try to please and gratify everybody. This, however, is cowardice, even if it be called virtue.'],['gratify','virtue'],
 '冒号后 that nobody should hurt them 解释 a single thing 的内容。Thus 标记在引述内部的因果推进。even if it be called virtue 是带让步意义的表达，be 为较正式的虚拟形式；被称为美德不改变引述中的批评。',
 '推断题优先连接原文已经给出的动机和结果，不引入一般心理定律。题干 In the quoted passage 限定观点来源，不能把尼采引述归给临床实验。',ctx='all',support='inference',
 translation='弗里德里希·尼采想必会赞同约翰的宣言。他认为，大多数人受了蒙蔽，才去追求幸福和美德。在《查拉图斯特拉如是说》中，他这样描绘过一种幸福而有德行生活的诱惑：“他们会赞美我，引诱我进入一种小小的美德；他们会劝我的脚步跟随小幸福的滴答节奏。我走在人群中，睁着双眼：他们变小了，而且还在越来越小；但这源于他们关于幸福和美德的教义。他们在美德上也很谦抑——因为他们想要知足。而只有一种谦抑的美德，才能同知足相容……谦抑地拥抱一点小幸福——他们把这叫作‘听天由命’——然后又谦抑地眯眼寻找下一点小幸福。归根结底，这些愚人最渴望的只有一件事：没有人伤害他们。因此，他们试着讨好、取悦所有人。然而这就是怯懦，即使它被称作美德。”')

add(54,'逻辑关系','Why are “small happiness and meaning” described as dangerous here?',
 ['They can attract people into a conventional life that avoids conflict.','They require everyone to become literal mountain climbers.','They make people consciously choose the greatest physical danger.','They are rejected because a comfortable life cannot contain any meaning.'],0,
 'because 后说明其危险在于诱惑性；随后说人们几乎不自觉地被惯例吸引，以求和谐、无冲突。这里是在阐释 Zarathustra 的人生评价，不是要求所有人实际登山，也没有说舒适生活绝无意义。',
 ['A 把 seductive、drawn to convention 与 conflict-free life 连起来，符合该段逻辑。','B wanderer / mountain climber 出现在哲学引述中，不能当成对所有人的字面指令。','C 原文说 almost unconsciously，且追求的是避免冲突，方向相反。','D 片段讨论这种生活的吸引与代价，没有否定任何意义存在的可能。'],
 ['Small happiness and meaning are dangerous because they are so seductive. Almost unconsciously, most people are drawn to convention, so that they can live a harmonious, conflict-free life.'],['seductive','convention'],
 'because 引导原因从句，they 回指 small happiness and meaning。are drawn to convention 为被动形式；so that they can live... 表目的。末句 For Zarathustra 明确标记评价视角，it 回指这种惯常安稳生活。',
 '因果题用 because 和 so that 分别定位原因与目的，不把它们对调。抽象哲学引述应按当前段落的阐释理解；保留 For Zarathustra 的观点限定。',ctx='all',
 translation='尼采没有倡导一种惯常、简单而舒适的生活，而是倡导漫游者的人生。查拉图斯特拉对自己说：“我是一个漫游者，也是一个登山者……你现在才踏上通往伟大的道路！顶峰与深渊——它们如今连在一起。你正走向伟大：过去对你而言最大的危险，如今成了最大的庇护。”查拉图斯特拉是“所有远行者、所有不愿脱离危险而生活之人的朋友……对你们这些勇敢的寻觅者、探索者，以及所有扬起机巧船帆驶入可怕海洋的人——你们陶醉于谜题，欣喜于暮色，灵魂被笛声诱往每个漩涡，因为你们不愿用怯懦的手沿着威胁摸索；在能够猜测的地方，你们不愿推演——我只对你们讲述我所见的谜，那最孤独者的幻象。”小小的幸福与意义之所以危险，是因为它们太诱人了。大多数人几乎不自觉地被惯例吸引，以便过上和谐、没有冲突的生活。对查拉图斯特拉而言，那不是值得过的人生。（译文保留本 PDF 引述中 threat 一词的“威胁”含义，不擅自改成其他版本措辞。）')

add(55,'主旨','Which statement best captures the balance of the chapter’s closing advice?',
 ['Negative feelings should replace happiness as the only aim of life.','A happy person should abandon all sources of comfort and small joy.','Only people who are currently unhappy can live a good life.','Accept occasional negative feelings and consider possibilities beyond contentment.'],3,
 '作者一方面允许偶尔悲伤、愤怒或害怕，另一方面肯定已经幸福的人；同时请读者反思满足心态，考虑舒适和小乐趣之外是否还有可能。幸福是美好生活的一条道路，但不是唯一道路。',
 ['A 把反对唯一幸福标准误读成树立唯一负面情绪标准。','B 原文有 at least once in a while，没有要求放弃一切舒适。','C 作者说已经幸福的人 doing great，没有排斥他们过好生活。','D 同时概括情绪接纳与超越安稳满足的开放反思，保留偶尔的限度。'],
 ['If you feel pressure to feel happy all the time, remember that it is OK to be sad, angry, or fearful every now and then.','Perhaps there could be more to life than coziness and small joys, at least once in a while.','Happiness is not the only way to lead a good life, as we shall see.'],['richness','reflect'],
 'If you feel... 为条件从句，主句 remember that... 为祈使句并接宾语从句。there could be... 使用 there be 存在结构和情态动词，Perhaps 再次限制确定性；to lead a good life 后置修饰 way。',
 '章末主旨题同时读取让步、肯定和建议。every now and then、Perhaps、at least once in a while 都防止走向极端；not the only 只是否定唯一性，不等于全面否定幸福。',ctx='all',
 translation='如果你感到必须时时快乐的压力，请记住：偶尔悲伤、愤怒或害怕是可以的。这些情绪会为你的内心生活增添复杂性与丰富性。如果你已经对自己的人生感到幸福，你也做得很好。不过，花一点时间反思一下自己的满足者心态。人生或许不只有温馨舒适和小小乐趣，至少偶尔可以如此。正如我们接下来会看到的，幸福不是过上美好生活的唯一方式。')
