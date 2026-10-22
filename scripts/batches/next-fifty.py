"""50 individually authored exercises for frozen targets, PDF pages 25-32.
Preserve printed English, source positions and all previously published questions.
"""
from pathlib import Path
import json,hashlib
ROOT=Path(__file__).resolve().parents[2]
load=lambda p:json.loads((ROOT/p).read_text(encoding='utf8'))
b=load('public/data/book.json');plan=load('public/data/reading-plan.json');targets=load('source/short-questions/batch009-targets.json')['targets']
ss={s['id']:s for s in b['sentences']};pp={p['id']:p for p in b['paragraphs']};out=[]
def add(i,kind,prompt,options,answer,prompt_zh,options_zh,analyses,quotes,word,meaning,context,example,collocations,translation,support='explicit'):
 t=targets[i-1];u=next(u for u in plan['units'] if u['id']==t['readingUnitId']);group=[ss[sid] for sid in u['sentenceIds']];p=pp[u['paragraphId']];text=p['text'][group[0]['start']:group[-1]['end']]
 assert hashlib.sha256(text.encode()).hexdigest()==t['passageSha256'];evidence=[]
 for quote in quotes:
  offset=text.find(quote);assert offset>=0,(i,quote);start=group[0]['start']+offset;end=start+len(quote);touching=[s for s in group if s['start']<end and s['end']>start]
  evidence.append(dict(quote=quote,sentenceIds=[s['id'] for s in touching],sources=list({(r['pdfPage'],r['block']):r for s in touching for r in s['sources']}.values())))
 assert word.lower() in text.lower(),(i,word)
 out.append(dict(id=t['questionId'],version=1,readingUnitId=u['id'],chapterId=u['chapterId'],sectionId=u['sectionId'],paragraphId=u['paragraphId'],sentenceIds=u['sentenceIds'],passage=text,prompt=prompt,options=options,answer=answer,type=kind,promptZh=prompt_zh,optionsZh=options_zh,analyses=analyses,evidence=evidence,vocabulary=[dict(word=word,meaning=meaning,context=context,example=example,collocations=collocations)],translation=translation,support=support,editorialStatus='PDF 第 25–32 页逐题核对；固定连续原句；区分文学引述、自报、相关和假设，不扩大个体或因果结论'))

add(1,'细节','In what capacity does the narrator introduce Mr. Johnson?',
 ['A university admissions officer addressing applicants.','The narrator’s former professor at UVA.','A middle-school principal telling parents and students about his college years.','A journalist interviewing parents about school rankings.'],2,
 '叙述者以什么身份介绍 Johnson 先生？',['向申请者讲话的大学招生官。','叙述者在弗吉尼亚大学的前教授。','向家长和学生讲述大学往事的中学校长。','采访家长、讨论学校排名的记者。'],
 ['A principal of Buford Middle School 不是大学招生官。','B when he was a college student 描述 Johnson 自己的经历，不是担任作者教授。','C principal、parents and students、college student 三项均对应原句。','D 原文没有记者采访或学校排名。'],
 ['Mr. Johnson, the principal of Buford Middle School in Charlottesville, about when he was a college student at UVA.'],
 'principal','中小学校长','这里是职务名词，不是“主要的”这个形容词','The principal welcomed the new students.',['a school principal','the principal of a school'],
 '我记得夏洛茨维尔 Buford 中学的校长 Johnson 先生向我们这些家长和学生讲过一个故事，讲的是他在弗吉尼亚大学读书时的事。')

add(2,'逻辑关系','Why did the BBC seek the key to happiness among Danes, according to this excerpt?',
 ['Denmark often ranks among the world’s happiest countries.','Denmark was said to have no unhappy residents.','The BBC had already proved that national wealth alone creates happiness.','The Danes had asked the BBC to change a university ranking.'],0,
 '根据片段，BBC 为什么向丹麦人寻找幸福秘诀？',['丹麦经常位列世界最幸福国家之一。','据称丹麦没有不快乐的居民。','BBC 已证明只有国家财富创造幸福。','丹麦人要求 BBC 改大学排名。'],
 ['A Since 引出原因：常被列为最幸福国家之一。','B one of the happiest 不是所有居民都幸福。','C 没有财富的因果证明。','D 原句是幸福调查，不是大学排名请求。'],
 ['Since Denmark often ranks as one of the happiest countries in the world, the BBC went to the Danes in search of the key to happiness.'],
 'in search of','寻找；寻求','说明 BBC 此行要探究什么，不表示已得到因果证明','They travelled north in search of a quieter life.',['in search of answers','in search of the key'],
 '由于丹麦经常位列世界最幸福国家之一，BBC 前去向丹麦人寻找幸福的关键。秘诀是什么？')

add(3,'主旨','What stance does the author take toward the satisficer mindset here?',
 ['It should replace maximizing in every area of life.','It has no legitimate use in ordinary decisions.','It is useful only when a person stops planning.','It has an important place, without being universally preferred to maximizing.'],3,
 '作者在这里对满意即可心态持什么立场？',['应在生活所有方面取代最大化心态。','在日常决定中没有合理用途。','只有停止规划时才有用。','它有重要作用，但不因此应一概优先于最大化心态。'],
 ['A I don’t think so 回应前面的全面推崇提问，不能改成一律替代。','B important place 与主动采用它相矛盾。','C planning something 明确是用途之一。','D 同时保留作者的否定与对日常用途的肯定。'],
 ['Does this mean that we should promote the satisficer mindset over the maximizer mindset? I don’t think so. There is an important place in life for the satisficer mindset.'],
 'mindset','思维方式；心态','指作决定时采用的取向，而非固定身份标签','A flexible mindset can help when plans change.',['a satisficer mindset','adopt a mindset'],
 '这是否意味着应当把满意即可的心态推崇到最大化心态之上？我不这么认为。满意即可的心态在人生中有重要位置。我购物、做规划或进行日常决策时，都会主动采用它。')

add(4,'作者意图','How does the quotation from John support the warning?',
 ['It experimentally proves that unhappiness always improves health.','It voices rejection of a false happiness that can accompany settling for less.','It declares that all satisfaction is necessarily dishonest.','It shows that John recommends avoiding every challenge.'],1,
 'John 的引述怎样支持这里的警示？',['用实验证明不幸福总能改善健康。','表达对满足于较少所得时可能伴随的虚假幸福的拒绝。','宣称所有满足感必然不诚实。','说明 John 建议逃避一切挑战。'],
 ['A 小说人物的话不是健康实验。','B settling for less 与宁愿不快乐也不要 false happiness 相呼应。','C 警惕某种虚假幸福，不等于否定所有满足。','D 这段警示针对降低追求，并非鼓励回避挑战。'],
 ['settling for less than you can achieve.','I’d rather be unhappy than have the sort of false, lying happiness you were having here.'],
 'settling for','勉强接受；满足于','这里指接受低于自己能够实现的程度','She refused to settle for an inaccurate answer.',['settle for less','settle for second best'],
 '这就是幸福陷阱的第二部分：满足于低于自己所能达到的程度。听听《美丽新世界》中“野蛮人”John 的警告：“嗯，我宁愿不快乐，也不要你们这里那种虚假、骗人的幸福。”','inference')

add(5,'观点归属','Whose view is associated with people being deceived into happiness and virtue?',
 ['The BBC’s conclusion from a controlled trial.','The author’s claim about every survey respondent.','Nietzsche’s view, introduced through his writing.','A clinical diagnosis offered by John.'],2,
 '“人们被诱骗而幸福且有德”被归为谁的观点？',['BBC 的对照试验结论。','作者对每位调查受访者的断言。','通过其著作引入的 Nietzsche 的观点。','John 给出的临床诊断。'],
 ['A 此处没有 BBC 的实验。','B He believed 的 he 回指 Nietzsche，不是所有受访者的数据。','C Friedrich Nietzsche 后接 He believed，再引入其著作。','D 文学和哲学讨论不是临床诊断。'],
 ['Friedrich Nietzsche would have approved of John’s proclamation. He believed that most people are deceived to be happy and virtuous.'],
 'lure','诱使；引诱','引述中把人引向“小幸福”的吸引力','The advertisement tried to lure customers into the shop.',['lure someone into','lure someone away'],
 'Friedrich Nietzsche 会赞同 John 的宣言。他认为，多数人是受了蒙骗才变得幸福而有德。在《查拉图斯特拉如是说》中，他这样描述过幸福且有德生活的诱惑：“他们要以赞美把我诱入一种小小的美德；他们要劝我的脚踏着一种小幸福的滴答节奏。')

add(6,'主旨','What criticism does the quoted speaker make about seeking contentment?',
 ['It invariably produces the greatest possible virtue.','It prevents all forms of resignation.','It is presented as a scientific measure of physical size.','It can shrink aspiration into modest virtue and repeated small happinesses.'],3,
 '引述中的说话者怎样批评对满足的追求？',['它必然产生最大美德。','它能防止任何认命。','它是测量身体尺寸的科学方法。','它会让追求缩小为有限的美德和接连的小幸福。'],
 ['A only a modest virtue 与最大美德不符。','B 原文把拥抱小幸福称为 resignation。','C smaller 是哲学批评中的表达，不是身体测量。','D smaller、modest virtue、another small happiness 共同构成批评。'],
 ['For they are modest in virtue, too—because they want contentment. But only a modest virtue gets along with contentment….'],
 'resignation','认命；无奈接受','此处是引述中对安于小幸福的称呼，不是辞职','She accepted the delay with resignation.',['a sense of resignation','accept with resignation'],
 '“我走在这些人中，睁眼观察：他们变小了，还在越来越小；这是他们关于幸福与美德的教义造成的。他们在美德上也有限度，因为他们想要满足。但只有有限的美德能与满足相处……谦逊地拥抱一份小幸福，他们称之为‘认命’；接着又眯眼打量整体，寻找另一份小幸福。”')

add(7,'主旨','What kind of life does Nietzsche advocate in this excerpt?',
 ['A wandering life that embraces difficult heights and depths.','A comfortable life protected from every uncertainty.','A settled life based exclusively on public approval.','A life in which greatness removes all danger.'],0,
 'Nietzsche 在这段中提倡怎样的生活？',['漂泊探索、迎向艰难高峰与深渊的生活。','受到保护、不存在任何不确定性的舒适生活。','完全建立在公众认可之上的安定生活。','达到伟大便消除一切危险的生活。'],
 ['A wanderer、mountain climber 和 Peak and abyss 共同支持这一概括。','B comfortable life 是开头与所提倡生活相对的选择。','C 原文没有把公众认同设为生活依据。','D 高峰与深渊相连，不意味着危险全部消失。'],
 ['Nietzsche advocated for the life of a wanderer.','Peak and abyss—they are now joined together.'],
 'abyss','深渊','与 peak 并列，表达这段哲学引述中的极端处境','The path seemed to lead toward an abyss.',['a deep abyss','the edge of an abyss'],
 'Nietzsche 提倡的不是传统、简单、舒适的生活，而是漂泊者的生活。查拉图斯特拉对自己说：“我是漂泊者，也是登山者……你现在才开始走向伟大！高峰和深渊——如今它们连接在了一起。”')

add(8,'同义改写','Which statement best restates the reversal described in the quotation?',
 ['The traveller abandons greatness to avoid danger.','All faraway places are guaranteed to be safe.','What was once the greatest danger becomes the greatest refuge.','Refuge is available only to people who remain at home.'],2,
 '哪一项最准确地改写了引述中的转变？',['旅行者放弃伟大以躲避危险。','所有遥远地方都保证安全。','曾经最大的危险成了最大的庇护。','只有留在家里的人才能获得庇护。'],
 ['A 原句仍是 going your way to greatness，没有放弃。','B 引述中的反转不是旅行安全保证。','C hitherto 与 now 构成过去危险、如今庇护的反转。','D 后一句赞许远行且不愿没有危险的人。'],
 ['now that which has hitherto been your ultimate danger has become your ultimate refuge.'],
 'refuge','庇护；避难处','与 danger 构成引述中的反转，并非实用安全指南','The library became a refuge during a difficult month.',['seek refuge','a place of refuge'],
 '“你正在走向伟大：曾经是你最大危险的事物，如今成了你最大的庇护。”查拉图斯特拉是“一切远行者和不愿在没有危险的情况下生活之人的朋友……”。')

add(9,'作者意图','To whom does the quoted speaker address his riddle?',
 ['Readers who insist that every answer be supplied in advance.','Bold searchers willing to venture into uncertainty.','Officials responsible for guaranteeing safe sea travel.','People who reject every form of exploration.'],1,
 '引述中的说话者把谜题讲给谁？',['坚持所有答案必须预先给出的读者。','愿意冒险进入未知的勇敢探索者。','负责保证海上交通安全的官员。','拒绝一切探索的人。'],
 ['A drunk with riddles 描写乐于接触谜，而非要求现成答案。','B bold searchers、terrible seas 和 riddles 描写接受未知的对象。','C 航海意象用于哲学称呼，不是在分配官员职责。','D searchers 与 embarks 都指向探索，不能读成拒绝探索。'],
 ['To you, the bold searchers, researchers, and whoever embarks with cunning sails on terrible seas','to you alone I tell the riddle that I saw'],
 'embarks','登船；开始旅程','在这里与航海意象一起表现投身探索','She embarks on a new research project next month.',['embark on a journey','embark on research'],
 '“致你们，勇敢的探索者、研究者，以及所有驾着灵巧风帆驶入可怕海域的人——致你们这些沉醉于谜、欣然迎接暮色的人，你们的心灵被笛声引向每一个漩涡，因为你们不愿用胆怯的手沿着威胁摸索；能够猜测时，你们厌恶推演——我只向你们讲述我见到的谜、最孤独者的幻象。”原页此处印为 threat（威胁），英文据此保留，不擅改为其他词。')

add(10,'推断','What can be established from this sentence alone?',
 ['Every person agreed with Zarathustra’s judgement.','The sentence supplies experimental evidence about happiness.','Zarathustra regarded every possible life as worthless.','Zarathustra judged the life under discussion not worth living.'],3,
 '仅凭这句话，能确定什么？',['所有人都同意查拉图斯特拉的判断。','这句话提供了幸福实验的证据。','查拉图斯特拉认为所有可能的生活都无价值。','查拉图斯特拉认为当时讨论的那种生活不值得过。'],
 ['A For Zarathustra 限定观点所属，不代表共识。','B 这是价值判断，没有实验设计或结果。','C it 指特定讨论对象，不能扩成 every possible life。','D 保留观点归属和判断范围；单句没有完整交代 it 的具体前文。'],
 ['For Zarathustra, it was not a life worth living.'],
 'worth','值得的','worth living 表示值得过，评价对象受 it 的上下文限制','The exhibition is worth visiting.',['worth doing','worth the effort'],
 '在查拉图斯特拉看来，那不是一种值得过的生活。','inference')

add(11,'主旨','What do the quotations from Flaubert and Schwartz illustrate?',
 ['Happiness has critics who associate it with unattractive qualities.','Medical studies have established stupidity as necessary for happiness.','Everyone writing about happiness agrees that it is desirable.','The Stoics conducted the research cited by Schwartz.'],0,
 'Flaubert 和 Schwartz 的引述说明什么？',['幸福也有批评者，他们把它与并不讨喜的特征联系起来。','医学研究已确认愚蠢是幸福的必要条件。','所有谈幸福的作者都认为幸福值得追求。','斯多葛学派开展了 Schwartz 引用的研究。'],
 ['A doubters 后的两段尖刻引语具体展示批评态度。','B Flaubert 的书信措辞不是医学结论。','C many doubters 直接排除全体一致。','D 列举不同批评者，不代表他们共同开展研究。'],
 ['there are also many doubters','people are some of the dullest people I know.'],
 'doubters','怀疑者','指质疑幸福理想的人，并非被诊断的群体','The proposal had supporters as well as doubters.',['silence the doubters','convince the doubters'],
 '幸福有许多拥护者。但也有许多怀疑者，从斯多葛学派到 Gustave Flaubert 都在其中。Flaubert 写信给 Louise Colet 说：“愚蠢、自私和身体健康，是幸福的三个条件；不过，如果缺少愚蠢，一切就都完了。”Tony Schwartz 也抱着类似态度，在《哈佛商业评论》发表题为《幸福被高估了》的文章，说：“‘幸福’的人是我认识的人中最乏味的一些。”')

add(12,'作者意图','How does Silverstein’s closing remark function in this account of his poem?',
 ['It reports a measured decline in a country’s happiness.','It shows that no one in the imagined land is happy.','It punctures the appeal of a place where everything is happy and jolly.','It recommends that readers move to the land described.'],2,
 '这段介绍中，Silverstein 的结尾评论起什么作用？',['报告某国幸福度经测量下降。','表明想象中的地方没有一个人幸福。','削弱了那个人人幸福、处处欢乐之地的吸引力。','建议读者搬去所描写的地方。'],
 ['A 诗歌评论没有国家测量数据。','B 人人幸福是诗中设定，bore 评价其乏味，不是否认设定。','C 最后的 What a bore 对前面的全然欢乐形成讽刺转折。','D 结尾批评乏味，并非迁居建议。'],
 ['He describes the land of happy as a place where everyone is happy and everything is jolly. He ends his poem with: “What a bore.”'],
 'poignant','深刻动人的；尖锐的','此处强调作者认为这首诗的批评有力、令人感触','Her account offered a poignant reminder of the loss.',['a poignant critique','a poignant reminder'],
 'Shel Silverstein 的诗《幸福之地》也许是对幸福最尖锐动人的批评。他把幸福之地描述成一个人人幸福、事事欢乐的地方。诗的结尾却是：“真无聊。”','inference')

add(13,'逻辑关系','How does the spending example relate to the critique of happiness?',
 ['It confirms that happiness requires selfish spending.','It provides a counterexample to the claim that a happy life must be selfish.','It shows that spending on oneself and others has identical effects.','It establishes that money is the only source of happiness.'],1,
 '花钱的例子与对幸福的批评是什么关系？',['证实幸福必须靠自私消费。','反驳幸福生活必定自私这一说法。','表明为自己和别人花钱的效果完全相同。','确认金钱是幸福的唯一来源。'],
 ['A spending money on others 与必须自私相反。','B otherwise 引出反证，随后以为别人花钱增加幸福为例。','C as opposed to 强调两种花钱对象的对照。','D 一个例子不能推出唯一来源。'],
 ['One common critique is that a happy life might be a selfish one. In reality, there is lots of evidence that suggests otherwise.','spending money on others as opposed to on oneself increases happiness.'],
 'as opposed to','而不是；与……相对','在此对比消费的受益者：别人和自己','The session focuses on practice as opposed to theory.',['as opposed to oneself','practice as opposed to theory'],
 '为什么如此贬低幸福？一种常见批评认为，幸福的生活可能是自私的生活。实际上，有大量证据指向相反的情况。例如，把钱花在别人身上而不是自己身上，会增加幸福感。')

add(14,'作者意图','Why does the author temporarily assume the happiness-as-selfishness critique?',
 ['To withdraw the statement that happy people volunteer more.','To claim that volunteering makes everyone unhappy.','To prove that happiness never contributes to a good life.','To explore what could make a life good apart from happiness.'],3,
 '作者为什么暂时接受“幸福即自私”的批评作假定？',['撤回幸福的人志愿服务更多的说法。','断言志愿服务让所有人不幸福。','证明幸福从不有助于美好生活。','探索幸福之外还有什么能使生活美好。'],
 ['A for now, let’s assume 是讨论设定，不是撤回上一句。','B 没有这种因果断言，且对象与方向均被替换。','C if not happiness 的提问不构成永远无贡献的证明。','D proceed with a question 紧接提出幸福之外的好生活标准。'],
 ['for now, let’s assume the critique of happiness-as-selfishness and proceed with a question: What makes for a good life, if not happiness?'],
 'volunteer','自愿服务','这里为动词，比较志愿服务多寡，不是职业名称','I volunteer at the community garden on Saturdays.',['volunteer at a shelter','volunteer to help'],
 '幸福的人比不幸福的人做更多志愿服务。不过，目前先让我们接受“幸福就是自私”这一批评作为假定，接着问：如果不是幸福，什么能构成美好生活？')

add(15,'细节','How is significance first explained in this account of meaning in life?',
 ['A life matters to people beyond one’s family and friends.','A person receives public awards for every achievement.','A life has no obligations to strangers.','A person feels happy at every other person’s expense.'],0,
 '这里首先怎样解释生命意义中的重要性？',['一个人的生活对家人朋友之外的人也有分量。','一个人每项成就都获得公众奖项。','一个人的生活对陌生人没有责任。','一个人靠牺牲所有他人的利益来幸福。'],
 ['A not just...but also strangers 明确扩大生活所关涉的人群。','B matters 并未被定义为获奖。','C strangers 正是被纳入的对象。','D Tartt 所说是让别人幸福，即使牺牲自己的幸福；D 颠倒受益者。'],
 ['First, a meaningful life is a life that matters. It matters not just to one’s family members and friends, but also to strangers.'],
 'significance','重要性；意义','是此处意义感的一个维度：生活对他人有分量','The discovery has significance for local communities.',['personal significance','of great significance'],
 '小说家 Donna Tartt 提出，美好生活就是“让别人幸福，即使以牺牲自己的幸福为代价”——换言之，许多学者所说的“有意义的生活”。生命意义通常由重要性、目的和连贯性来界定。首先，有意义的生活是有分量的生活。它不仅对自己的家人朋友有分量，对陌生人也如此。')

add(16,'同义改写','What does knowing where one is going mean in this passage?',
 ['Remembering the route to every place one has visited.','Avoiding all changes in a daily timetable.','Having a clear purpose and a guiding sense of direction.','Making a difference only within one’s immediate family.'],2,
 '片段中“知道自己往哪里走”是什么意思？',['记得去过的每个地方的路线。','避免日程发生任何变化。','有明确目的和引导自己的方向感。','只对自己的直系亲属产生影响。'],
 ['A 在 clear purpose 的语境下是人生方向，不是导航记忆。','B 指导原则不等于日程绝不可变。','C clear purpose、sense of direction、guiding principle 互相解释。','D in the world 没有限定只有家人。'],
 ['Second, a meaningful life has a clear purpose. A person who leads a meaningful life knows where they’re going. There is a clear sense of direction and a guiding principle.'],
 'guiding principle','指导原则','指帮助人生保持方向的原则','Fairness is a guiding principle in her work.',['a clear guiding principle','follow a guiding principle'],
 '有意义的生活会在世界上产生影响。其次，有意义的生活有明确目的。过着有意义生活的人知道自己往哪里走。他们有清晰的方向感，也有指导原则。')

add(17,'细节','What makes the experiences described here form a meaningful whole?',
 ['They are identical in every respect.','They fit together under the person’s guiding principles.','They are kept separate from any personal principles.','They occur in a strictly unchanging order.'],1,
 '这里的经历怎样构成一个有意义的整体？',['每项经历在所有方面都相同。','在这个人自己的指导原则下彼此契合。','与任何个人原则保持分离。','按严格不变的顺序发生。'],
 ['A divergent 表明经历可以不同。','B fit together under...guiding principles 直接说明组织方式。','C under 表示由原则统合，非与原则分离。','D well organized 指连贯组织，没有规定发生顺序不可变。'],
 ['All of a person’s divergent experiences fit together under their own guiding principles.'],
 'divergent','不同的；分歧的','说明经历各不相同，但仍可被共同原则统合','The team brought together divergent perspectives.',['divergent experiences','divergent views'],
 '第三，有意义的生活组织有序。一个人种种不同的经历，都能在其自己的指导原则下相互契合。')

add(18,'语境词义','What distinguishes a “bullshit job” in Graeber’s definition here?',
 ['It requires strenuous physical labour.','It is any occupation held by millions of people.','It offers no opportunity to change employers.','Its holder cannot really justify why the job exists.'],3,
 '在 Graeber 这里的定义中，“bullshit job”的区别性特征是什么？',['需要繁重体力劳动。','任何有数百万人从事的职业。','没有换雇主的机会。','从业者自己无法真正说明这份工作存在的理由。'],
 ['A toiling away 描述辛劳耗日，并非这一定义的判据。','B millions 描述人数，不是职业类别的充分条件。','C 原文没有讨论换雇主机会。','D 定义明确落在从业者 can’t really justify the existence 上。'],
 ['He defines a bullshit job as a job that the person who is doing it can’t really justify the existence of that job.'],
 'justify','证明……有道理；为……提供充分理由','这里指说明一份工作为何有必要存在','The manager was asked to justify the extra cost.',['justify the existence of','justify a decision'],
 '相比之下，无意义的生活是对世界不产生任何影响的生活。人类学家 David Graeber 在《毫无意义的工作：一种理论》中认为，世界各地有数百万人正辛苦地把生命耗费在无意义的工作上。他把这种工作定义为：连从事它的人自己都无法真正说明其存在理由的工作。')

add(19,'逻辑关系','Why does the author say these occupations do not necessarily imply meaningless lives?',
 ['People can make a difference outside their jobs.','Graeber excludes all professional occupations from his argument.','The author claims that every corporate lawyer secretly enjoys the work.','A job’s repetitiveness guarantees a meaningful life.'],0,
 '作者为什么说这些职业并不必然意味着无意义的人生？',['人们也能在工作之外产生影响。','Graeber 将所有专业职业排除在论证之外。','作者断言每位公司律师都暗中喜欢这份工作。','工作的重复性保证人生有意义。'],
 ['A outside of their jobs 是最后结论的直接理由。','B 列出的 corporate lawyers 等恰恰属于论述范围。','C 原文归于 Graeber 的说法涉及职业存在，不是所有人喜欢工作。','D 重复性不是人生有意义的保证。'],
 ['Of course, people can make a difference in the world outside of their jobs. So this doesn’t mean corporate lawyers and public relations consultants lead meaningless lives.'],
 'clerical','文书事务的','修饰 jobs，指办公室文书工作，并非宗教职务','She gained experience in clerical work.',['clerical work','clerical duties'],
 '依 Graeber 之见，无意义的工作不只是重复性的工厂工作或文书工作，也包括公司律师、公关顾问、电话营销员和品牌经理。例如，他声称多数公司律师暗自认为，如果自己这类职业不存在，世界可能会更好。当然，人也可以在工作之外对世界产生影响。因此，这并不意味着公司律师和公关顾问就过着无意义的生活。')

add(20,'主旨','Which combination characterises the meaningless life described here?',
 ['Public recognition, a fixed destination, and emotional calm.','An ambitious career combined with frequent changes of employer.','A lack of positive impact, clear purpose, and a sense of wholeness.','Low income despite a strong sense of purpose.'],2,
 '哪组特征概括这里描述的无意义生活？',['公众认可、固定目的地与情绪平静。','有野心的事业与频繁换雇主。','缺少正面影响、明确目的和整体感。','虽很有目的感但收入低。'],
 ['A 片段没有把认可或情绪平静列为此类特征。','B 没有讨论换雇主，且 clear purpose 的缺失才是要点。','C not making any positive difference、no clear purpose、fragmented 对应三项。','D 收入没有出现，strong sense of purpose 还与原文相反。'],
 ['if you are not making any positive difference in the world, your life may feel pointless.','a meaningless life has no clear purpose.','a meaningless life feels torn and highly fragmented.'],
 'aimlessly','漫无目的地','描述缺乏清晰目标时生活的走向，不是空间上迷路','He spent the afternoon wandering aimlessly.',['wander aimlessly','drift aimlessly'],
 '但如果你没有给世界带来任何正面影响，你的人生可能会让你觉得毫无意义。同样，无意义的生活没有明确目的。没有明确目的的人往往漫无目标地度过人生。最后，无意义的生活让人感到撕裂、极为破碎。')

add(21,'同义改写','What does the sentence say about the roles a person plays?',
 ['They are too numerous for anyone to remember.','They fail to come together as an integrated whole.','They are necessarily limited to paid employment.','They all express one clearly unified purpose.'],1,
 '这句话对一个人承担的不同角色作了什么描述？',['角色太多，任何人都记不住。','它们无法相互整合为连贯整体。','它们必然只限于有报酬的工作。','它们都表达一个明确统一的目的。'],
 ['A different 不等于多到无法记忆。','B do not add up to a coherent whole 的核心是不能整合。','C roles 没有被限定为有酬职业。','D 把 do not 的否定读反了。'],
 ['The different roles one plays do not add up to a coherent whole.'],
 'coherent','连贯的；协调一致的','形容不同角色所未能组成的统一整体','The editor helped turn the notes into a coherent account.',['a coherent whole','a coherent account'],
 '一个人扮演的不同角色，无法汇成一个连贯的整体。')

add(22,'细节','Which statement accurately reflects the routes to a reason for living listed here?',
 ['A career is presented as the only acceptable route.','Social change is excluded because it involves others.','All people must make a scientific discovery before life can have meaning.','Several routes are offered, including career, religion, and social roles.'],3,
 '哪一项准确反映这里列举的人生理由的来源？',['事业是唯一可接受的途径。','社会变革因涉及他人而被排除。','所有人必须先有科学发现，人生才能有意义。','列出多条途径，包括事业、宗教和社会角色。'],
 ['A whether via 后面列出多个来源，并非唯一事业。','B social change 被明确列入。','C 科学发现只是列举的一种，不能改成所有人的门槛。','D 保留并列选择的范围，未把例子变成必要条件。'],
 ['whether via career, religion, social roles (e.g., parenthood), scientific discovery, or social change.'],
 'commencement','毕业典礼','commencement speakers 指毕业典礼演讲者，此处不是项目开工者','She was invited to give a commencement address.',['a commencement speech','a commencement speaker'],
 '不用说，有意义的生活听起来比无意义的生活更有吸引力。因此，人们说你应该找到活着的理由——可以通过事业、宗教、社会角色（如为人父母）、科学发现或社会变革来寻找。许多毕业典礼演讲者都作过类似劝勉，包括 Michelle Obama 在纽约市立大学 2016 届毕业典礼上的话：“成就伟大。为你们自己建立出色的人生……”')

add(23,'细节','What action is explicitly requested in this sentence?',
 ['Contribute to helping other people do the same.','Wait until other people have helped you first.','Take sole responsibility for every other person’s future.','Avoid helping others because success is entirely individual.'],0,
 '这句话明确要求采取什么行动？',['尽自己的一份力量帮助别人也做到同样的事。','先等其他人帮助自己。','独自承担所有其他人未来的全部责任。','因为成功完全是个人的事，所以不帮助别人。'],
 ['A do your part to help others 是直接请求，the same 的完整所指需结合前文。','B 没有“他人先帮助我”的前提。','C your part 是尽自己的份，不是承担全部责任。','D help others 与拒绝帮助相反。'],
 ['always, always do your part to help others do the same.'],
 'do your part','尽自己的责任；出一份力','强调个人对共同帮助行动的贡献','We can all do our part to keep the park clean.',['do your part to help','do your part in a team'],
 '“而且，请你们一定、一定尽自己的一份力，帮助别人也做到同样的事。”')

add(24,'逻辑关系','What event led Donna Adams-Pickett to decide to become an ob-gyn doctor?',
 ['Her father’s graduation from medical school.','A tobacco farm’s decision to close.','Learning that her grandmother and the baby had died during childbirth.','Hearing that her grandmother had become a doctor.'],2,
 '什么事件促使 Donna Adams-Pickett 决定成为妇产科医生？',['父亲从医学院毕业。','一家烟草农场决定关门。','得知祖母与婴儿都在分娩时去世。','听说祖母成为医生。'],
 ['A 父亲在文中是十二岁失去母亲，没有医学院经历。','B 农场是祖母的生活地点，没有关闭事件。','C After hearing this story 连接家族悲剧和职业决心。','D 祖母是分娩时去世的人，不是医生。'],
 ['her paternal grandmother, who lived on a tobacco farm, died while giving birth. The baby died as well','After hearing this story, she was determined to become an ob-gyn doctor.'],
 'paternal','父亲一方的','paternal grandmother 指父亲的母亲，即祖母','His paternal grandfather grew up near the coast.',['paternal grandmother','paternal relatives'],
 'Donna Adams-Pickett 医生确实践行了 Michele Obama 所提倡的事。小时候，她得知住在烟草农场的祖母在分娩时去世，婴儿也没能活下来，她父亲十二岁就失去了母亲。听到这个故事后，她下定决心成为妇产科医生。')

add(25,'细节','How does the author illustrate significance in Dr. Adams-Pickett’s life?',
 ['By saying that maternal care was already equally available everywhere.','By noting that some mothers and babies might have died without her care.','By proving that she personally eliminated every maternal death in Georgia.','By treating the number of television appearances as the measure of meaning.'],1,
 '作者怎样说明 Adams-Pickett 医生人生的重要性？',['说明孕产照护早已在各地同样普及。','指出没有她的照护，一些母亲与婴儿可能已经死亡。','证明她亲自消除了佐治亚州每一例产妇死亡。','把电视出镜次数作为人生意义的衡量标准。'],
 ['A maternity care desert 表示照护资源匮乏，非同等普及。','B significance 后括号中的 might have died 是直接说明。','C some 和 might 都有限定，不能扩大为消除全部死亡。','D PBS 是信息出处，不是衡量指标。'],
 ['significance (some mothers and babies might have died without her care).'],
 'maternity care desert','孕产照护资源匮乏地区','用 desert 比喻照护资源稀少的地区，并非气候沙漠','The report describes efforts to serve a maternity care desert.',['live in a maternity care desert','maternal care'],
 'Adams-Pickett 医生向 PBS《新闻时刻》分享说，过去二十年，她在佐治亚州奥古斯塔接生了六千多名婴儿；当地是孕产照护资源匮乏地区。她的人生无疑有意义：有明确目的——为佐治亚居民提供良好孕产照护，尤其关注分娩前后孕产死亡率远高于其他女性的黑人女性；也有重要性——如果没有她的照护，一些母亲与婴儿可能已经死亡。')

add(26,'语境词义','What does “coherence” refer to in this sentence?',
 ['Proof that every event in her life was planned in advance.','A guarantee that family tragedy always improves a career.','The absence of any changes in the course of her life.','A convincing connection running through the story of her life.'],3,
 '这句话里的 coherence 指什么？',['证明她所有人生事件都预先计划好了。','保证家族悲剧总能改善事业。','人生过程中从来没有任何变化。','贯穿她人生故事、令人信服的联系。'],
 ['A convincing narrative 不等于提前安排全部事件。','B 单个案例不能推出所有悲剧的必然益处。','C 连贯性允许变化，不是没有变化。','D narrative 与 course of her life 指事件间可理解的连接。'],
 ['Her family tragedy also gives a convincing narrative and coherence to the course of her life.'],
 'coherence','连贯性','指人生经历可串成可理解的故事，不代表必然因果或全由预设计划','The final chapter gives coherence to the whole account.',['narrative coherence','a sense of coherence'],
 '她的家族悲剧，也让其人生历程有了令人信服的叙事和连贯性。')

add(27,'逻辑关系','What limitation does “However” introduce after the description of heroes?',
 ['Their extraordinary accomplishments are too rare to feel readily attainable.','The named people never achieved anything important.','Graduation speeches prevent people from having meaningful lives.','Their achievements are common enough for everyone to reproduce easily.'],0,
 '描述英雄人物后，However 引入什么限制？',['那些非凡成就过于罕见，令人难以想象自己也能达到。','列举的人物从未成就重要的事。','毕业典礼演讲阻止人们过有意义的生活。','这些成就十分普遍，人人都容易复制。'],
 ['A so rare that...hard to imagine 明确表达难以企及。','B extraordinary achievements 肯定了成就，非否定。','C 演讲者只是所举英雄的典型，不构成阻碍的因果关系。','D rare 与 easily reproduce 相反。'],
 ['However, these accomplishments are so rare that it’s hard to imagine ever achieving such feats.'],
 'feats','非凡成就；功绩','指前文英雄人物完成的重大事情','Completing the expedition was an impressive feat.',['an extraordinary feat','achieve a feat'],
 '想到过着有意义生活的人，我们也许会想到做过大事的 Donna Adams-Pickett 医生、Michelle Obama 或 Barack Obama——就是那些在毕业典礼上演讲的人！这些都是非凡的成就，这些人都是英雄。然而，这样的成就非常罕见，让人难以想象自己也能完成这样的壮举。')

add(28,'细节','What is the first element of the meaning trap?',
 ['Meaningful lives necessarily require unhappiness.','People always choose goals that are too easy.','The accomplishment imagined is so grand that pursuing it sets people up for failure.','Failure proves that every part of a person’s life lacks meaning.'],2,
 '意义陷阱的第一个因素是什么？',['有意义的生活必然需要不幸福。','人们总是选择太容易的目标。','想象中与有意义生活相联的成就过于宏大，追求它会让人陷入失败。','失败证明一个人人生的每个部分都无意义。'],
 ['A 这段没有建立意义与不幸福的必要关系。','B so grand 指目标过大，不是太容易。','C 保留 grand accomplishment 到 aiming for it 的逻辑。','D 这段指出一种陷阱，没有把失败等同整个人生无意义。'],
 ['the type of accomplishment associated with a meaningful life is so grand that aiming for it will set us up for a failure.'],
 'set us up for','使我们容易遭遇；使我们陷入','这里指宏大标准使追求者容易落入失败，不是预订安排','Unrealistic deadlines can set a team up for failure.',['set someone up for failure','set someone up for success'],
 '就像幸福陷阱一样，也存在意义陷阱。意义陷阱的第一个因素是：人们把有意义的生活与过于宏大的成就联系起来，以至于追求那种成就会让自己陷入失败。')

add(29,'逻辑关系','What contrast does the author draw between popular belief and survey findings?',
 ['Most people reject meaning, while researchers say only heroes have it.','People imagine meaningful lives to be rare, but most respondents say their lives have meaning.','Survey data show that nearly everyone has achieved a heroic ambition.','Both popular belief and surveys say meaningful lives are limited to a tiny minority.'],1,
 '作者把大众想法与调查结果作了什么对比？',['多数人拒绝意义，而研究者说只有英雄才有意义。','人们想象有意义的生活很少见，但多数受访者说自己的人生有意义。','调查表明几乎人人都达成英雄式抱负。','大众与调查都说只有极少数人的生活有意义。'],
 ['A 颠倒观点归属，调查结果是多数人自报有意义。','B small 对比 most people say，且保留自报性质。','C 自报有意义不等于已实现英雄壮举。','D 两者形成反差，并非一致认定稀少。'],
 ['Although many people think that the number of people who lead a meaningful life is small, survey data show that, in fact, most people say they do have a meaningful life.'],
 'ambitions','抱负；志向','supersized ambitions 指公众想象中英雄的宏大追求','Her ambitions include improving local education.',['career ambitions','pursue an ambition'],
 '意义陷阱的第二个因素是，人们往往误解了所需条件。那些抱负超大的英雄形象，并不一定符合研究结果。虽然许多人认为过着有意义生活的人很少，但调查数据显示，实际上，多数人说自己确实有意义的生活。')

add(30,'细节','What does the reported 90 percent represent?',
 ['Americans who had received a national award.','All people worldwide who were independently certified as having meaningful lives.','Americans who strongly agreed on a five-point purpose scale.','Americans who said they had meaning in life in the cited Gallup data.'],3,
 '这里报告的 90% 代表什么？',['获得国家奖项的美国人。','全球经独立认证人生有意义的所有人。','在五点目的感量表上表示强烈同意的美国人。','所引 Gallup 数据中，说自己人生有意义的美国人。'],
 ['A 没有奖项指标。','B 原文是 Americans said，非全球客观认证。','C 此句没有五点量表或 strongly agreed。','D 准确保留人群、调查来源和自报内容。'],
 ['90 percent of Americans said they have meaning in life, according to the Gallup World Polls.'],
 'report','报告；转述研究结果','此处为动词，主语是论文作者，结果来自 Gallup 数据','The researchers report a difference between the two groups.',['report findings','report that'],
 'Samantha Heintzelman 和 Laura King 在题名巧妙的论文《人生颇有意义》中报告说，根据 Gallup 世界民意调查，90% 的美国人说自己人生有意义。')

add(31,'细节','What feature of the Gallup question is specified here?',
 ['It asks about important purpose or meaning and allows a yes-or-no answer.','It asks respondents to list independently verified achievements.','It requires a score from one to ten for happiness alone.','It offers separate numerical ratings for purpose and meaning.'],0,
 '这里指出 Gallup 提问具有什么特征？',['询问是否有重要目的或意义，采用是或否的回答形式。','让受访者列举经独立核实的成就。','要求只给幸福打一个一到十分的分数。','分别要求对目的与意义给出数值评分。'],
 ['A 引号内问题与 yes-or-no answer format 直接对应。','B 询问感受，不是核实成就清单。','C 不是十分量表，也不只问幸福。','D purpose or meaning 合在同一道是否题中，没有分别打分。'],
 ['“Do you feel your life has an important purpose or meaning?” with a yes-or-no answer format.'],
 'phrased','措辞；表述','说明调查问题如何问，可能影响回答的含义','The invitation was phrased as a question.',['carefully phrased','phrase a question'],
 '我们以为有意义的生活属于成就非凡的英雄，为什么大多数人却说自己的人生有意义？一个答案也许在于有关生命意义的问题是怎样问的。Gallup 的问题这样表述：“你是否觉得自己的人生有重要的目的或意义？”回答形式为“是”或“否”。')

add(32,'推断','Why might someone answer yes without finding life particularly meaningful?',
 ['The survey explicitly rewards every affirmative answer.','A yes answer certifies the respondent’s heroic accomplishments.','They may reject calling life utterly pointless even without a strong sense of meaning.','They are required to choose yes if they have ever felt unhappy.'],2,
 '为什么一个不觉得人生特别有意义的人仍可能回答“是”？',['调查明确奖励每个肯定回答。','回答“是”认证了其英雄式成就。','即使意义感不强，他们也可能不愿把人生说成全然无意义。','只要曾不幸福，就被要求选“是”。'],
 ['A 片段没有奖励或报酬。','B yes 表达自我感受，不认证成就。','C utterly pointless 的极端否定门槛解释了可能回答是的原因。','D 没有按幸福经历强制回答的规定。'],
 ['Those who did not feel like their lives were utterly pointless were likely to say yes to this question.','even if someone did not feel their life was particularly meaningful, they might have said yes.'],
 'utterly','完全地；彻底地','修饰 pointless，把否定选项理解成非常强的否定','The two accounts are utterly different.',['utterly pointless','utterly different'],
 '说“不，我的人生既无目的也无意义”，几乎等于说自己的人生毫无价值。那些不觉得自己的人生全然无意义的人，很可能会回答“是”。这意味着，即便某人并不觉得自己的人生特别有意义，也可能回答“是”。','inference')

add(33,'细节','How many respondents selected the strongest agreement category in the purpose survey?',
 ['9.1 percent, selecting 2 on the scale.','28.5 percent, selecting 5 on the scale.','1.1 percent, selecting 1 on the scale.','10.2 percent, selecting the combined disagreement categories.'],1,
 '在目的感调查中，多少受访者选择了最强的同意类别？',['9.1%，选择量表上的 2。','28.5%，选择量表上的 5。','1.1%，选择量表上的 1。','10.2%，选择合并后的不同意类别。'],
 ['A 9.1% 对应 2，即不同意，不是最强同意。','B 28.5% 对应 strongly agreed 和 5，三者一致。','C 1.1% 对应 strongly disagreed，方向相反。','D 合并不同意类别不是最高同意类别。'],
 ['28.5 percent of Americans “strongly” agreed (a 5 on a 1 to 5 point scale)'],
 'scale','量表；刻度','指用 1 至 5 的数字表示同意程度的测量形式','Participants rated the statement on a five-point scale.',['a five-point scale','on a scale of one to five'],
 '另一项聚焦目的感的 Gallup 调查使用“我的人生有真正的目的”这一表述，发现 28.5% 的美国人“强烈”同意（一至五分量表中的 5 分），1.1%“强烈”不同意（同一量表的 1 分），另有 9.1% 不同意（量表的 2 分）。')

add(34,'逻辑关系','What comparison is made between the two Gallup results?',
 ['The two percentages are exactly equal.','The 10 percent figure measures strong agreement in the later survey.','The 10.2 percent figure is larger because it includes all neutral responses.','The combined disagreement share is close to the earlier share answering no.'],3,
 '这里对两份 Gallup 结果作了什么比较？',['两个百分比完全相等。','10% 衡量后一次调查的强烈同意。','10.2% 更高是因为包含所有中立回答。','合并后的不同意比例，与较早回答“否”的比例接近。'],
 ['A quite well 表示很吻合，但 10 与 10.2 并非完全相等。','B 10% 对应 original data 中 said no。','C 这里明确是 strongly disagreed 或 disagreed，不含中立。','D 10% 与 10.2% 的比较对象和方向均准确。'],
 ['matches up quite well with the original Gallup data (10 percent said no vs. 10.2 percent disagreed).'],
 'matches up','相符；吻合','在此表示比例接近，不要求数值完全相等','The estimate matches up well with the final count.',['match up with','match up quite well'],
 '对“我的人生有真正的目的”表示强烈不同意或不同意的比例，与最初的 Gallup 数据相当吻合：原调查中 10% 回答“否”，而这里 10.2% 表示不同意。')

add(35,'作者意图','What question does the author raise before rejecting a simple self-reporting explanation?',
 ['Whether the high reported purpose reflects many heroes or an overly positive illusion.','Whether all Americans have achieved identical professional success.','Whether 54.9 percent strongly deny having any purpose.','Whether surveys should ask only about national awards.'],0,
 '作者在否定简单的自报解释前提出什么疑问？',['较高的目的感自报比例，是反映英雄很多，还是过度正面的幻觉。','所有美国人是否取得完全相同的职业成功。','是否有 54.9% 强烈否认任何目的。','调查是否应该只问国家奖项。'],
 ['A Are there so many heroic individuals 与 overly positive illusion 构成两种解释。','B 原文没说成就相同。','C 54.9% report having a more or less real purpose 是大致有目的，不是强烈否认。','D 没有提出只测奖项的建议。'],
 ['Are there so many heroic individuals making a difference in the U.S.? Or is this some kind of overly positive illusion?'],
 'self-reporting bias','自报偏差','指自己报告自身状况可能带来的偏差，此处作者随后说不能仅用它解释结果','The researchers considered possible self-reporting bias.',['reduce self-reporting bias','a potential bias'],
 '尽管如此，28.5% 的美国人报告人生有真正目的，另有 54.9% 报告多少有些真正目的，这仍令人印象深刻。美国真有这么多发挥影响的英雄人物吗？还是某种过度正面的幻觉？结果表明，这并不只是自报偏差。')

add(36,'逻辑关系','Which finding challenges the idea that reported meaning is only an illusion?',
 ['Participants and informants were never asked about the same person.','Friends and relatives assigned every participant an identical score.','Participants’ reports were correlated with reports from friends and family.','The researchers experimentally assigned participants to meaningful lives.'],2,
 '哪个发现挑战了“自报意义感只是幻觉”的解释？',['参与者与知情人从未评价同一个人。','朋友亲属给所有参与者完全相同的分数。','参与者自报与朋友家人的评价存在相关。','研究者用实验把参与者分配到有意义的人生。'],
 ['A 家人朋友报告的是该 participant 的生命意义。','B correlated 不等于全部相同或完全一致。','C 原文用有相关的结果对照“若只是幻觉则不会相关”的预测。','D asked...to report 是收集报告，不是操控分配人生。'],
 ['If the high percentage of self-reported meaning in life is only an illusion, informant reports would not correlate with self-reports.','self-reported meaning in life is correlated with informant-reported meaning in life.'],
 'informant','提供情况者；知情人','这里特指对参与者作评价的朋友和家人，不是警方线人','An informant who knew the participant completed the questionnaire.',['informant reports','informant-reported ratings'],
 '心理学家 Michael Steger 与同事请参与者报告自己觉得人生多有意义。此外，他还请参与者的朋友和家人评价这个人的生命意义。如果自报有意义的高比例只是一种幻觉，知情人的报告便不会与自报相关。他发现的却不同：自报的生命意义与知情人报告的生命意义存在相关。')

add(37,'推断','Which conclusion stays within the evidence described?',
 ['The reports have validity supported by agreement comparable to familiar trait measures.','Every individual self-report is perfectly accurate.','Personality traits have been proved to cause meaning in life.','Informants and participants always give exactly the same answers.'],0,
 '哪项结论没有超出所述证据？',['自报与知情人评价的相关程度可比于常见人格测量，为自报有效性提供支持。','每一份个人自报都完全准确。','人格特征已被证明造成生命意义。','知情人与参与者总是给出完全相同的回答。'],
 ['A similar to...personality traits 是作者判断 quite valid 的比较依据。','B quite valid 不是每个人、每次均完美准确的保证。','C 这里比较相关强度，不是证明人格造成意义。','D correlation 不要求每项回答完全一致。'],
 ['The self-informant correlation on meaning in life was similar to that in studies testing more familiar personality traits','self-reports of meaning in life are quite valid.'],
 'valid','有效的；有根据的','这里是测量有效性评价，不能扩成个体报告绝对无误','The team checked whether the measure was valid.',['a valid measure','valid evidence'],
 '生命意义上的自报与知情人评价之间的相关，与测量外向性、神经质（倾向于过度担忧）等更熟悉的人格特质的研究中的相关程度相似。因此，从科学角度看，生命意义的自报相当有效。','inference')

add(38,'细节','How are principles of faith described as helping religious people?',
 ['They prevent hurricanes from reaching residential areas.','They remove the need to interpret difficult situations.','They give a framework for interpreting difficult situations and gaining clarity.','They establish that all people with meaning follow the same religion.'],2,
 '这里怎样描述信仰原则对有宗教信仰者的帮助？',['阻止飓风到达居民区。','消除理解艰难处境的需要。','为理解艰难处境、获得清晰感提供框架。','证实所有有人生意义的人信奉同一宗教。'],
 ['A 心理解释框架不等于控制自然灾害。','B help them interpret 是帮助理解，不是无需理解。','C 原句 interpret difficult life situations 和 give them clarity 支持此项。','D tend to be religious 是倾向，不是所有人或同一宗教。'],
 ['Religious people follow certain principles of faith, which help them interpret difficult life situations accordingly and give them clarity.'],
 'clarity','清晰；明晰感','指对处境的理解更清楚，不是灾害的可预测性','Writing down her priorities gave her greater clarity.',['gain clarity','clarity of purpose'],
 '那么，自称人生有意义的这 28.5% 美国人是哪些人？首先，他们往往有宗教信仰。有宗教信仰的人遵循某些信仰原则，这些原则帮助他们据此理解人生的艰难处境，获得清晰感。2005 年，卡特里娜飓风卷走新奥尔良一些街区时，许多居民都难以理解为何会发生这样的事。')

add(39,'推断','What limited conclusion does the author draw about finding meaning?',
 ['Becoming a celebrated inventor is necessary for meaning.','A traditional religion is one possible route to meaning.','Religious belief guarantees that no one experiences psychological difficulty.','Every non-religious person lacks a meaningful life.'],1,
 '作者就寻找意义得出了哪一项有限结论？',['成为著名发明家是获得意义的必要条件。','传统宗教是寻找意义的一种可能途径。','宗教信仰保证所有人都不会心理受困。','所有无宗教信仰者的人生都没有意义。'],
 ['A don’t have to be 否定必须成为杰出发明家。','B One way 保留一种途径的范围，没有变成必选项。','C better able 是比较，不是零困难保证。','D 比较应对灾难的情况，不是宣布另一群体全部无意义。'],
 ['you don’t have to be a maverick inventor like Steve Jobs to feel like your life is meaningful. One way to find meaning is by following a traditional religion.'],
 'maverick','特立独行者；不拘常规的','修饰 inventor，指像 Steve Jobs 那类不同寻常的创新人物','The maverick designer challenged familiar conventions.',['a maverick inventor','a maverick thinker'],
 '有宗教信仰的人，比无宗教信仰的人更能从心理上应对这场灾难。所以，你不必成为 Steve Jobs 那样特立独行的发明家，才觉得人生有意义。遵循一种传统宗教，是寻找意义的一条途径。','inference')

add(40,'主旨','What do the contrasting examples suggest about meaning in life?',
 ['Public achievement guarantees that a person feels life is meaningful.','Only scientists can assess whether their lives have meaning.','Ordinary people lack any connection to a significant mission.','Subjective meaning does not necessarily follow external success or status.'],3,
 '这些对比案例说明生命意义有什么特点？',['公众成就保证一个人觉得人生有意义。','只有科学家能评估自己人生是否有意义。','普通人不可能与重要使命相联。','主观意义感不必然随外在成就或地位而来。'],
 ['A nonetheless 后说明受尊敬、获奖者也可能觉得无意义，否定保证。','B 没有限定只有科学家能判断。','C ordinary people 正被用来说明有人觉得自己与使命相联。','D subjective 加上两类人的反差，支持外在地位并非充分条件。'],
 ['Meaning in life is by nature very subjective.','In contrast, some ordinary people see their lives as linked to a significant mission.'],
 'self-esteem','自尊；自我价值感','属于研究所述与自报意义感相关的特征，并非因果保证','Supportive feedback can help a student’s self-esteem.',['high self-esteem','a sense of self-esteem'],
 'Steger 的研究还发现，说自己人生有意义的人，往往对未来乐观、外向、神经质程度低、友善、尽责，而且自尊较高。生命意义本质上非常主观。一些受尊敬、受欢迎、屡获奖项的科学家，仍觉得自己的人生毫无意义，并死于自杀。相比之下，一些普通人觉得自己的人生与重要使命相联。','inference')

add(41,'作者意图','What does the janitor’s reply illustrate within the story?',
 ['He links his own work to a larger shared mission.','He claims to be the astronaut who will walk on the moon.','He says that cleaning work prevents space exploration.','He provides a documented experimental result about all NASA staff.'],0,
 '在这个故事中，清洁工的回答说明什么？',['他把自己的工作与更大的共同使命相联系。','他声称自己就是将登月的宇航员。','他说清洁工作会阻止太空探索。','他提供了关于所有 NASA 职员的已记录实验结论。'],
 ['A helping put a man on the moon 把个人工作纳入共同任务。','B helping 不等于本人作为宇航员登月。','C 帮助实现使命，不是阻止它。','D famous folk legend 明确是流传故事，不是实验或已证实史料。'],
 ['In a famous folk legend','I’m helping put a man on the moon!'],
 'janitor','清洁工；楼宇管理员','故事中承担日常维护工作的人，与宇航员身份不同','The janitor opened the building before the staff arrived.',['a school janitor','work as a janitor'],
 '有个广为流传的民间故事：John F. Kennedy 一次访问 NASA 时，对一名清洁工说：“你好，我是 Jack Kennedy。你在做什么？”清洁工回答：“总统先生，我在帮助把人送上月球！”','inference')

add(42,'细节','Which link concerning conscientious people is stated here?',
 ['They worry more, so they abandon larger goals.','They achieve fewer goals but always rate their lives higher.','They achieve more goals and are more likely to feel they are moving toward a larger one.','They obtain meaning only through having high public status.'],2,
 '这里对尽责者作了哪项联系？',['他们担忧更多，因此放弃更大目标。','他们实现更少目标，却总把人生评价更高。','他们达成更多目标，也更可能觉得正朝人生更大目标前进。','他们只能通过较高公众地位获得意义。'],
 ['A non-neurotic 的担忧描述不能误归给所有尽责者。','B achieve more 与 fewer 相反，且 more likely 不是 always。','C 连续两句陈述实现更多目标与更可能感到朝大目标前进。','D 没有 only 或公众地位条件。'],
 ['Conscientious people achieve more of their goals than unconscientious people. Therefore, they are also more likely to feel that they are moving toward a larger goal in life'],
 'conscientious','认真尽责的','描述较能持续执行责任与目标的人格特质','A conscientious colleague checks the details carefully.',['a conscientious worker','conscientious about duties'],
 '其次，自尊较高的人比不喜欢自己的人更可能说自己的人生有分量。神经质程度低的人（不太担忧、也不容易感到压力的人），比神经质程度高的人更可能说自己的人生有明确目的和方向。尽责的人比不尽责的人能达成更多目标。因此，他们也更可能觉得，自己正在朝人生中的更大目标前进。')

add(43,'逻辑关系','What role does “To the extent that” play in the explanation?',
 ['It declares that every American shares all the listed traits.','It links widespread reported meaning to how widely the listed traits are present.','It reverses the claim that people can feel purpose in life.','It establishes that personality differences are impossible to measure.'],1,
 '解释中的 To the extent that 起什么作用？',['宣称每个美国人都具有全部列出的特征。','把意义感报告普遍这一现象，与这些特征的普遍程度联系起来。','推翻人能够感到人生有目的的说法。','证实人格差异不可能测量。'],
 ['A majority 和 a lot of 都不是每个人。','B 该结构表示在这些特征普遍的程度上，许多人自报有意义便可理解。','C likely to feel...purpose 是肯定倾向，不是否定。','D 没有讨论人格差异无法测量。'],
 ['To the extent that the majority of Americans have high self-esteem, are optimistic about their futures, and say they are extraverted, non-neurotic, agreeable, and conscientious, it makes sense that a lot of people say their lives have meaning.'],
 'to the extent that','在……的程度上；鉴于……达到的程度','引出解释所依赖的条件及程度，不能读成无条件全称断言','The plan is useful to the extent that it addresses local needs.',['to the extent that','to a large extent'],
 '他们很可能觉得自己的人生有方向、有目的、有意义。在多数美国人自尊较高、对未来乐观，并自称外向、神经质程度低、友善且尽责的程度上，许多人说自己的人生有意义，也就可以理解了。')

add(44,'主旨','What recurring pattern in finding meaning is described?',
 ['Constantly changing causes before making a commitment.','Avoiding work, family, and community as sources of meaning.','Trying to influence every area of life equally at once.','Sustained effort within a limited sphere often helps people achieve meaning.'],3,
 '这里描述了获得意义的什么常见模式？',['不断更换关注的事业，不作承诺。','避免从工作、家庭和社区获得意义。','同时在生活所有领域施加同等影响。','长期投入有限领域，常帮助人获得意义。'],
 ['A same location for an extended period 强调持续而非不断变换。','B work, family, and community 正被列为来源。','C one or two、well-defined、narrowness 指聚焦，不是面面俱到。','D 持续在特定领域作贡献，概括了本段例子与研究总结。'],
 ['volunteer in the same location for an extended period of time','successfully achieving a meaningful life often comes with focus and narrowness.'],
 'realm','领域；范围','指工作、家庭、社区等相对界定清晰的生活范围','The discussion moved into the realm of education.',['a realm of life','within the realm of'],
 '这些人格特质和态度会以可预期的方式表现出来。人们往往选择一两个格外关心的事业（如施粥所或教会），长期在同一地点做志愿服务，尝试在界定清楚的领域产生影响，从而获得意义。另一些人从工作、家庭和社区获得生命意义，同样是相对狭窄的生活领域。生命意义研究表明，成功获得有意义的生活，往往伴随专注和范围的狭窄。')

add(45,'细节','What is the strength of the claim made in this sentence?',
 ['It says there is usually no problem, while leaving room for exceptions.','It says a problem is impossible in every case.','It says problems occur in most cases.','It identifies the problem’s exact cause within this sentence.'],0,
 '这句话作出的断言强度是什么？',['说多数情况下没有问题，同时容许例外。','说任何情况下都不可能有问题。','说多数情况下都会出问题。','在本句内指出问题的精确原因。'],
 ['A In most cases 保留通常如此与存在例外的空间。','B most 不是 all，也不是不可能有问题。','C not a problem 的否定不能读反。','D this 的完整所指依赖前文，本句未交代具体原因。'],
 ['In most cases, this is not a problem.'],
 'in most cases','在大多数情况下','限制判断范围，避免把通常结论扩大为绝无例外','In most cases, the form can be completed online.',['in most cases','in some cases'],
 '在大多数情况下，这并不是问题。')

add(46,'观点归属','How is Mason introduced?',
 ['As a named participant whose real prison record was investigated.','As the researcher who designed a national survey.','As a hypothetical guard devoted to protecting Americans.','As an opponent of every form of national security work.'],2,
 'Mason 是怎样被引入的？',['调查了真实监狱档案的具名参与者。','设计全国调查的研究者。','一个致力于保护美国人的假设狱警。','反对一切国家安全工作的人。'],
 ['A hypothetical 明确不是已调查真实人物。','B 这里是案例中的狱警，不是调查研究者。','C hypothetical military prison guard 与 wants to devote...protection 均直接支持。','D cares about...dearly 与反对一切相关工作不符。'],
 ['Think of a hypothetical military prison guard, Mason.','Mason wants to devote his life to the protection of the American people.'],
 'hypothetical','假设的','明确案例的证据身份，不能当作真实受试者记录','Consider a hypothetical town with two schools.',['a hypothetical case','a hypothetical example'],
 '不过，这里存在一些令人不安的潜在影响。设想一位名叫 Mason 的假设军事监狱狱警。他十分关心美国国家安全。Mason 想把自己的一生投入保护美国人民的事业。')

add(47,'作者意图','Why does the passage end by asking whether Mason is leading a good life?',
 ['To endorse abuse as a necessary proof of purpose.','To question whether his felt meaning is enough to make his life good.','To establish that the prisoners have all been convicted of terrorism.','To show that Mason believes his own life has no meaning.'],1,
 '片段为什么以“Mason 这样算美好生活吗”结束？',['赞同虐待是目的感的必要证明。','质疑他感到有意义是否足以说明其生活是好的。','确认所有囚犯都已因恐怖主义定罪。','表明 Mason 认为自己的人生无意义。'],
 ['A 问句在质疑，不是赞同虐待。','B 自认保护人民而有意义，与 abuses 形成价值张力，引出追问。','C suspected 仅为涉嫌，不能改为全部定罪。','D Mason thinks...meaningful 明确是自认有意义。'],
 ['He abuses these suspected terrorists','Mason thinks he is leading a meaningful life','But is this a good life?'],
 'suspected','被怀疑的；涉嫌的','修饰 terrorists，表明怀疑状态，不等于司法定罪','The suspected leak is still being investigated.',['suspected of terrorism','a suspected offence'],
 '他被派往一座主要关押涉嫌恐怖主义者的监狱。他虐待这些嫌疑人，就像臭名昭著的阿布格莱布监狱虐囚事件那样。Mason 认为自己在保护美国人民、给世界带来影响，因此过着有意义的生活。但这算美好生活吗？','inference')

add(48,'逻辑关系','What distinction is made in this sentence?',
 ['Subjective meaning and objective goodness are guaranteed to coincide.','Objective goodness is irrelevant whenever a person feels purpose.','The case proves that every meaningful life is morally bad.','A life may feel meaningful to its holder while not being objectively good.'],3,
 '这句话作了什么区分？',['主观意义与客观上的好必然一致。','只要感到有目的，客观上的好就无关紧要。','这个案例证明所有有意义生活在道德上都坏。','一个人可能主观觉得有意义，生活却在客观上并不好。'],
 ['A but 表明两者在本例中可能分离。','B 原句仍以 objectively not so good 进行评价，并未取消其重要性。','C In this case 和 may 都限制范围，不能扩为所有生活。','D 正确保留主观与客观的对照，以及 may 的可能性。'],
 ['In this case, it may be subjectively meaningful, but objectively not so good.'],
 'subjectively','主观地','指当事人的感受角度，与 objectively 的评价角度对照','The task felt subjectively difficult despite a simple scoring system.',['subjectively meaningful','subjectively experienced'],
 '在这个案例中，这种生活可能主观上有意义，但客观上并不那么好。')

add(49,'细节','What relationship do the cited studies report?',
 ['Right-wing authoritarians reported more meaning than non-authoritarians.','An experiment proved that meaning causes authoritarianism in every person.','Mason’s actual biography was verified by the studies.','Authoritarianism was defined as critical resistance to all authority.'],0,
 '所引研究报告了什么关系？',['右翼威权主义者自报的生命意义高于非威权主义者。','实验证明意义感在每个人身上都会造成威权主义。','这些研究核实了 Mason 的真实生平。','威权主义被定义为批判地抗拒所有权威。'],
 ['A reported higher levels 与比较对象均直接对应。','B associated with 是相关，既无普遍因果也无实验操控。','C 首句再次强调 Mason merely hypothetical。','D 定义是 uncritical submission，D 将顺从读成抵抗。'],
 ['meaning in life is associated with right-wing authoritarianism','right-wing authoritarians reported higher levels of meaning in life than non-authoritarians.'],
 'adherence','遵守；坚持','strict adherence to conventional values 是作者所引定义的组成部分','The role requires adherence to clear safety rules.',['strict adherence to','adherence to rules'],
 '到目前为止，军事监狱警官 Mason 的例子仅仅是假设。对于这种生命意义错置的现象，有科学证据吗？近期研究发现，生命意义与右翼威权主义相关；这种信念体系被界定为：不加批判地服从权威、对违反社会规范者抱有攻击情绪，以及严格遵从传统价值观。也就是说，右翼威权主义者自报的生命意义水平高于非威权主义者。')

add(50,'推断','Which interpretation preserves the qualifications in this excerpt?',
 ['Civic work guarantees concern for all outsiders.','Every conservative is hostile to outsiders and every liberal is unhappy.','Civic involvement can coexist with narrow causes, and the studies report group differences.','The studies prove that changing political identity causes happiness and meaning.'],2,
 '哪一种理解保留了这段中的限定？',['公民事务工作保证关心所有外群体。','每个保守派都敌视外人，每个自由派都不幸福。','参与公民事务可以与狭窄目标并存，研究报告的是群体差异。','研究证明改变政治身份会造成幸福与意义。'],
 ['A But 转折指出 civic work 不保证目标广泛包容。','B might、potentially 和群体 reported higher 不能变为每个个体的绝对断言。','C 兼顾可能的狭窄与敌对，以及后文群体自报的比较。','D found...report higher 是研究关联，非身份干预的因果试验。'],
 ['their cause might be very narrow, and potentially antagonistic toward those they consider outsiders.','political conservatives','report higher levels of meaning in life as well as happiness than political liberals.'],
 'antagonistic','敌对的；对抗性的','potentially antagonistic 表示可能敌视，并非每人必然如此','The two groups adopted an antagonistic tone during the debate.',['antagonistic toward','an antagonistic relationship'],
 '他们也以自己的方式做不少公民事务工作。但他们的事业目标可能非常狭窄，并可能敌视那些被他们视为外人的人。同样，多项研究发现，政治保守派（通常被认为对内群体和外群体划界分明）自报的生命意义和幸福水平均高于政治自由派。','inference')

assert len(out)==50 and [q['id'] for q in out]==[t['questionId'] for t in targets]

def persist():
 path=ROOT/'source/short-questions/additional.json';existing=load('source/short-questions/additional.json');byid={q['id']:q for q in existing}
 for q in out:
  if q['id'] in byid:assert byid[q['id']]==q,('Refuse to overwrite changed authoring',q['id'])
  else:existing.append(q)
 path.write_text(json.dumps(existing,ensure_ascii=False,indent=2)+'\n',encoding='utf8',newline='\n')
 review=dict(batchId='batch-009',date='2026-10-22',pdfSha256=b['pdfSha256'],checkedPdfPages=list(range(25,33)),questionIds=[q['id'] for q in out],paragraphs=[dict(id=pid,textSha256=hashlib.sha256(pp[pid]['text'].encode()).hexdigest()) for pid in dict.fromkeys(q['paragraphId'] for q in out)],note='完整 PDF 原页视觉复核，包括跨页引语；保留印刷的 threat 等措辞，不暗改英文。区分文学、调查、相关及假设。候选句界不冒充人工最终分句。')
 (ROOT/'source/short-questions/review-next-fifty.json').write_text(json.dumps(review,ensure_ascii=False,indent=2)+'\n',encoding='utf8',newline='\n')
 print('Saved',len(out),'of 50 individually authored exercises')

if __name__=='__main__':persist()
