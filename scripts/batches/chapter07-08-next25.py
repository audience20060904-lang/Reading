"""25 individually authored exercises for frozen targets, PDF pages 77-82.
Preserve printed English, source positions and all previously published questions.
"""
from pathlib import Path
import json,hashlib
ROOT=Path(__file__).resolve().parents[2]
load=lambda p:json.loads((ROOT/p).read_text(encoding='utf8'))
b=load('public/data/book.json');plan=load('public/data/reading-plan.json');targets=load('source/short-questions/batch020-targets.json')['targets']
ss={s['id']:s for s in b['sentences']};pp={p['id']:p for p in b['paragraphs']};out=[]
def add(i,kind,prompt,options,answer,prompt_zh,options_zh,analyses,quotes,word,meaning,context,example,collocations,translation,support='explicit'):
 t=targets[i-1];u=next(u for u in plan['units'] if u['id']==t['readingUnitId']);group=[ss[sid] for sid in u['sentenceIds']];p=pp[u['paragraphId']];text=p['text'][group[0]['start']:group[-1]['end']]
 assert hashlib.sha256(text.encode()).hexdigest()==t['passageSha256'];evidence=[]
 for quote in quotes:
  offset=text.find(quote);assert offset>=0,(i,quote);start=group[0]['start']+offset;end=start+len(quote);touching=[s for s in group if s['start']<end and s['end']>start]
  evidence.append(dict(quote=quote,sentenceIds=[s['id'] for s in touching],sources=list({(r['pdfPage'],r['block']):r for s in touching for r in s['sources']}.values())))
 assert word.lower() in text.lower(),(i,word)
 out.append(dict(id=t['questionId'],version=1,readingUnitId=u['id'],chapterId=u['chapterId'],sectionId=u['sectionId'],paragraphId=u['paragraphId'],sentenceIds=u['sentenceIds'],passage=text,prompt=prompt,options=options,answer=answer,type=kind,promptZh=prompt_zh,optionsZh=options_zh,analyses=analyses,evidence=evidence,vocabulary=[dict(word=word,meaning=meaning,context=context,example=example,collocations=collocations)],translation=translation,support=support,editorialStatus='PDF 第 77–82 页逐题原页核对；固定原句与来源；保留可能、反事实、近似转述、假设估算、eventually和观点归属；书中AI或建议均不触发程序操作'))







add(1,'细节','What prompted the author to suggest visiting Annapolis?',
 ['Seeing a road sign while driving his family between two other cities.','A previously booked cruise that required an Annapolis stop.','A formal invitation received before leaving Baltimore.','A plan to move his family permanently to Annapolis.'],0,
 '什么促使作者提议去 Annapolis？',['开车带家人往另两城途中，看到一块路牌。','早已预订的游船要求停靠 Annapolis。','离开 Baltimore 前收到正式邀请。','计划把全家永久搬到 Annapolis。'],
 ['A driving...when I saw a sign 给出临时起意的触发。','B 本片段没有预订游船的安排。','C 没有正式邀请，作者是看到路牌后询问家人。','D 去游玩不等于永久迁居。could、often 也不能变成所有临时行动必有丰富结果。'],
 ['I was driving my family from Baltimore to Charlottesville one day when I saw a sign for Annapolis.'],
 'on a whim','临时起意；一时兴起','与 without prior planning 相连，描述未提前安排的经历','On a whim, they visited a small museum on the way home.',['do something on a whim','go somewhere on a whim'],
 '自发行动可能让我们体验未经预先计划的生活。我们最有趣的一些经历，往往是一时兴起做的事。就我而言，有一天我带家人从 Baltimore 开车去 Charlottesville，看到 Annapolis 的路牌，便问妻子和两个孩子：“有人想去 Annapolis 吗？”')

add(2,'细节','Which sequence is described after the family’s reply?',
 ['They rejected the suggestion and drove straight home.','They moved to Annapolis and gave up travelling.','They visited without planning, wandered around and took a cruise.','They cancelled a cruise that had been booked months earlier.'],2,
 '家人回答后，发生了哪一顺序？',['他们拒绝建议，直接回家。','搬到 Annapolis 后放弃旅行。','未经计划前往、在城里闲逛，又乘游船。','取消几个月前订好的游船。'],
 ['A everyone said Why not 是接受，非拒绝。','B went to 不等于迁居。','C totally unplanned、wandered、hopped on a cruise 依次对应。','D 原文说实际乘船，没给提前订票或取消的信息；儿子仍提起此事是个人记忆叙事，不是对所有家庭的实验。'],
 ['So we went to Annapolis, totally unplanned. We wandered around town and hopped on a cruise'],
 'hopped on','登上；顺势上了','在这里轻松描述乘上游船，不一定指真的跳跃上船','We hopped on a bus to explore the old town.',['hop on a cruise','hop on a bus'],
 '出乎我意料，每个人都说：“为什么不呢！”于是我们完全没计划地去了 Annapolis。我们在城里闲逛，还乘了一次游船，儿子至今仍会说起。')

add(3,'主旨','What central point about personality and richness opens the summary?',
 ['Personality traits permanently fix everyone’s capacity for a rich life.','Personality alone does not determine richness; playfulness and spontaneity can be learned.','Only already-extraverted people may try new experiences.','Meaning requires avoiding every difficult task for other people.'],1,
 '总结开头关于人格与丰富性的核心是什么？',['人格永久固定每个人丰富人生的能力。','人格本身不完全决定丰富性，人可学习玩心与自发性。','只有原本外向者才可尝试新经历。','意义要求回避一切为他人做的困难任务。'],
 ['A alone do not determine 否定这种决定论。','B 首句直接把非完全决定与可学习的路径连接。','C we can all learn 不限原本外向者。','D 文中说为重要事业付出、常为他人利益做困难任务，方向相反；作者在比较人生取向，不是把三者定为绝对互斥。'],
 ['personality traits alone do not determine our capacity for psychological richness: we can all learn to foster psychological richness through playfulness and spontaneity.'],
 'foster','促进；培养','指通过玩心与自发性培养丰富性，不是由既有人格自动保证结果','The workshop aims to foster curiosity through simple experiments.',['foster psychological richness','foster curiosity'],
 '总之，人格特质本身并不决定我们心理丰富的能力：我们都能学习通过玩心与自发性培养心理丰富。在这方面，心理丰富人生又与更优先严肃活动的幸福、有意义人生形成对照。为了获得意义，你需要投身重要事业，花时间做常常困难、对他人有益的任务。幸福也很严肃。')

add(4,'逻辑关系','How does the author qualify the admirable goals mentioned here?',
 ['They are declared worthless in every situation.','They require no effort or sustained attention.','Every person must pursue them on every day.','They can require sustained effort and are not for everyone or every day.'],3,
 '作者怎样限定这里提到的可敬目标？',['在所有情况都毫无价值。','不需要努力或持续注意。','每个人每天都必须追求。','它们可能需持续努力，并非适合每个人或每一天。'],
 ['A admirable 明确保留价值。','B requires sustained attention 与无需努力相反。','C not for everyone, nor for every day 正好否定一概而论。','D 同时保留努力成本与适用范围；Shaq 是说明不同偏好的例子，不证明某个偏好必然优于其他。'],
 ['being gritty or mindful requires sustained attention and is not always easy.','Such endeavors are not for everyone, nor for every day.'],
 'endeavors','努力；所追求的活动','承接坚持、善良、社交、正念等目标，不是贬低这些目标','Their creative endeavors required time and patience.',['such endeavors','sustained endeavors'],
 '心理学家报告，坚毅、善良、善社交和正念，有助于幸福。这些目标都值得赞赏，但坚毅或正念需要持续注意，并不总容易。这样的努力不适合每个人，也不适合每一天。像 Shaq 一样，有些人更偏好玩心而非正念，更偏好顽皮而非严肃。')

add(5,'逻辑关系','Which balance is expressed by the opening contrast about grit?',
 ['Grit makes achieving goals impossible.','Single-mindedness always guarantees a fun and rich life.','Grit can support goals, while single-mindedness can drain fun and richness.','The Biles example establishes the same recovery process for every athlete.'],2,
 '开头对坚毅的对照表达什么平衡？',['坚毅使实现目标不可能。','一心一意总保证人生有趣丰富。','坚毅可帮助目标，但过分盯单一目标也可能耗掉乐趣与丰富性。','Biles 例子确立了每位选手完全相同的恢复过程。'],
 ['A 原句 help...achieve their goals 正相反。','B suck the fun...out 表达可能代价，不是保证丰富。','C but 把益处与可能代价相连，保留 can。','D 一个人物叙事不等于每个选手的相同结果，也不提供临床处理方案。'],
 ['Grit can clearly help a person achieve their goals, but being single-minded can suck the fun and richness out of life.'],
 'rejuvenated','恢复活力的；焕发精神的','书中用于描述 Biles 休息后归来的状态，不是对所有人的疗效保证','After the break, the team returned feeling rejuvenated.',['strong and rejuvenated','feel rejuvenated'],
 '坚毅显然能帮助人实现目标，但只盯一个目标，也可能把人生中的乐趣与丰富性吸走。书中叙述，Simone Biles 退出东京奥运比赛，恐惧与焦虑使她不堪重负；休息一段时间后，她坚强归来，重获活力。')

add(6,'语境词义','What does “antidote” mean in this discussion?',
 ['A metaphorical counterbalance to excessive seriousness.','A specific medicine tested for a diagnosed illness.','Proof that duties must be permanently abolished.','A guarantee that all committed effort is harmful.'],0,
 '这里 antidote 是什么意思？',['对过度严肃的一种比喻性调节或解药。','针对确诊疾病测试的具体药物。','必须永久取消一切责任的证明。','所有投入努力都有害的保证。'],
 ['A to too much seriousness 限定对象是“过度”，后面列举与之相对的轻松态度。','B 文中是比喻，不是药物试验。','C 短语对照不是永久弃责的规则。','D too much 不等于任何程度的努力都坏。'],
 ['As an antidote to too much seriousness, we need playfulness and spontaneity.'],
 'antidote','解药；对抗某种不良状态的方法','此处为过度严肃提供平衡的比喻，不是医学处方','A walk was a welcome antidote to a long afternoon indoors.',['an antidote to','an antidote to seriousness'],
 '作为过度严肃的解药，我们需要玩心与自发性。让爱好暂胜职责，让娱乐暂胜承诺，让放松暂胜投入。')

add(7,'细节','Which action is among the author’s concrete suggestions?',
 ['Keep every journey identical and avoid making anyone laugh.','Try being playful daily and make someone close to you laugh.','Replace every work task with a permanent holiday.','Wait for a formal invitation before trying any playful action.'],1,
 '哪项属于作者给出的具体建议？',['每次路线完全一样，避免逗任何人笑。','试着每天有玩心，并逗身边的人笑。','用永久假期取代每项工作。','任何玩乐行动前都等待正式邀请。'],
 ['A 原文含 make...laugh 和 take a detour，方向相反。','B at least once a day 与 partner, friend, or coworker 对应。','C 没有永久放弃工作。','D 没有正式邀请这个前提；祈使句是书中建议，不是研究已经测得每项动作的确定效果。'],
 ['Try to be playful at work or at home at least once a day. Try to make your partner, friend, or coworker laugh.'],
 'detour','绕路；改变通常路线','作为回家时偶尔偏离惯例的例子，不是迷路的同义词','We took a short detour to see the river.',['take a detour','on your way home'],
 '试着在工作或家里每天至少有一次玩心。试着逗伴侣、朋友或同事笑。回家时绕个路。跳进一个水坑。')

add(8,'作者意图','What attitude do the suggestions in this excerpt encourage?',
 ['Being unable to act seriously in any setting.','Treating all outcomes as scientifically guaranteed.','Avoiding every physical or sensory experience.','Occasionally embracing childlike, spontaneous experiences.'],3,
 '这些建议鼓励什么态度？',['在任何情境都不能认真。','把所有结果当成科学保证。','回避所有身体或感官经历。','偶尔接纳孩子般、自发的体验。'],
 ['A once in a while 不是时时不能认真。','B 结尾是作者对丰富而难忘人生的倡议，不是本段给出随机实验。','C swim、wet、dirty 都是接触体验的例子。','D little kid 与 spontaneous 呼应偶尔轻松体验；不必把所有动作读成人人必须完成的清单。'],
 ['Be like a little kid once in a while. When you do something spontaneous, you’ll make life rich and memorable.'],
 'memorable','难忘的；值得记住的','指作者期待自发体验留下鲜明记忆，不是逐个行为的实测评分','The unexpected visit became a memorable part of the trip.',['a memorable experience','rich and memorable'],
 '去游泳。让自己湿一湿、脏一脏。偶尔像个小孩子。当你做些自发的事，就会让人生丰富而难忘。')

add(9,'主旨','What problem and counterforce does the new chapter introduce?',
 ['A lack of coffee and the need for a new advertising campaign.','A rejection of all earlier discussion of playfulness.','An obsession with productivity and a possible counterforce in DIY.','A plan to make every person specialise as early as possible.'],2,
 '新章引出什么问题及其对抗力量？',['咖啡不足与新广告的需要。','否定前面所有玩心讨论。','对生产力的迷恋，以及 DIY 这一可能的对抗力量。','让所有人尽早专攻的计划。'],
 ['A 当前片段的焦点不是咖啡广告。','B 先回顾前文，并把新问题与过早专攻潜在危害相连。','C obsession with productivity 与 counterforce...Do-It-Yourself 明确成对。','D 本句承接 potential harm，不是倡导所有人更早专攻。could 保留可能性，不是唯一确定机制。'],
 ['the obsession with productivity','the counterforce that could fill your life with psychological richness: Do-It-Yourself.'],
 'counterforce','反作用力量；对抗力量','指作者引入的 DIY 对生产力迷恋的可能平衡作用','Curiosity can act as a counterforce to rigid routine.',['a counterforce to','a potential counterforce'],
 '此前，我谈了促进心理丰富人生的因素，如玩心，以及 expeditus（“随时准备出发”）的态度。与上章过早专攻的潜在危害紧密相关，我现在要谈另一种可能吸走人生丰富性的力量：对生产力的迷恋；也要谈可能把心理丰富性带回来的一股对抗力量：自己动手做。')

add(10,'作者意图','What does the question “but at what cost?” do here?',
 ['It requests the exact price of a cup of coffee.','It shifts from praising productivity to considering possible psychological costs.','It establishes that productive people achieve nothing.','It proves the advertisement measured psychological richness.'],1,
 'but at what cost? 在这里起什么作用？',['询问一杯咖啡的准确售价。','从肯定生产力转向思考可能的心理代价。','确立高产者什么都没完成。','证明广告测量了心理丰富性。'],
 ['A cost 在这里是代价，而非咖啡价格询问。','B Productivity gain is great 先认可益处，再提出代价问题。','C get things done 明确承认完成任务的形象。','D 广告只是文化引例，没有心理丰富性的测量报告。in part 也不等于唯一广告成功原因。'],
 ['Productivity gain is great, but at what cost?'],
 'prolific','高产的；成果丰富的','指文化所赞赏的产出量，不等于人的体验一定丰富','The prolific writer published essays in several fields.',['a prolific writer','prolific individuals'],
 '许多人看着待办清单、靠咖啡因提神，开始一天。“America Runs on Dunkin’”广告成功，部分因为它把 Dunkin’ Donuts 定位为帮助你启动工作的一家公司。我们生活在崇拜高产、有条理、能把事情做完者的文化中。生产力提升很好，但代价是什么？')

add(11,'主旨','What question is raised about the pursuit of efficiency?',
 ['What unintended psychological effects might an obsession with efficiency have?','Which factory has already removed every psychological difficulty?','How can every task be completed with no possible trade-off?','Why is efficiency proved to be harmful in every circumstance?'],0,
 '本句对追求效率提出什么问题？',['迷恋效率可能带来什么非预期心理影响？','哪家工厂已消除所有心理困难？','如何让每项任务都没有任何取舍？','为什么已证明效率在任何情形都坏？'],
 ['A might、unintended、psychological consequences 三个限定均保留。','B 没有工厂或已消除困难的结论。','C 原句恰在追问潜在代价，而非声称可以没有取舍。','D 问句并未给出普遍有害的证明。'],
 ['What might be the unintended psychological consequences of our obsession with efficiency?'],
 'unintended','非故意的；未预期的','限定心理后果不是追求效率时本来想达到的结果，不表示结果已全部证实','The change had an unintended effect on daily routines.',['unintended consequences','an unintended effect'],
 '我们对效率的迷恋，可能产生什么非预期的心理后果？')

add(12,'推断','How should the introduction’s comment attributed to Krueger be treated?',
 ['As a verbatim transcript certified by an experiment.','As a criticism that economics has no foundational book.','As proof that Smith’s book contains no stories.','As the author’s approximate recollection of a comment praising its storytelling.'],3,
 '应怎样理解归于 Krueger 的导言评论？',['经实验证明的逐字记录。','批评经济学没有奠基著作。','证明 Smith 的书没有故事。','作者对赞扬该书叙事能力的一段评论作近似回忆。'],
 ['A something along the lines 明确不是逐字认证，也没有实验。','B 评论说 foundational book，并非没有。','C great storyteller 是肯定叙事。','D 保留作者喜欢这本书及对导言大意的转述；I totally agree 是本书作者态度，不能错归于 Krueger 的另一句直接引语。'],
 ['he says something along the lines of this','the foundational book on modern economics was written by a great storyteller.'],
 'along the lines of','大致类似于；意思大约是','提示下面是评论的大意，不能伪装成独立核实的逐字引文','She offered a suggestion along the lines of a shared study group.',['something along the lines of','a comment along these lines'],
 '我很喜欢 Adam Smith 的 The Wealth of Nations。我买的版本有一篇精彩导言，由杰出经济学家 Alan Krueger 撰写。他的大意是：经济学学生很幸运，因为现代经济学的奠基著作出自一位伟大的讲故事者。我完全同意。The Wealth of Nations 意外地引人入胜。','inference')

add(13,'推断','What does the counterfactual about the order of reading mean?',
 ['The author actually changed his profession after reading the two books.','A different reading order might have led him toward economics, but this is not an actual switch.','Every reader must choose economics rather than psychology.','The author says he never wrote a book in English.'],1,
 '关于阅读顺序的反事实是什么意思？',['作者实际读两书后已经转行。','若阅读顺序不同，可能转向经济学，但这不是实际转行记录。','每位读者都必须选经济学，不选心理学。','作者说自己从未写英文书。'],
 ['A If I had read...might have chosen 描写未实现的另一种过去，不能当成已转行。','B 保留条件与可能性。','C 是作者个人反思，不是所有读者的职业指令。','D 下一句明确说首部英文著作及其题名。'],
 ['If I had read it before William James’s Principles of Psychology, I might have chosen economics over psychology.'],
 'might have chosen','原本可能会选择','与 if...had read 构成对不同过去的推测，不是实际选择的新闻','With a different timetable, she might have chosen another course.',['might have chosen','choose one field over another'],
 '假如我在 William James 的 Principles of Psychology 之前读这本书，我可能会选择经济学而非心理学。我甚至把自己首部英文书命名为 The Psychological Wealth of Nations。','inference')

add(14,'细节','What is the initial pin-factory scenario used as a comparison?',
 ['Ten workers already dividing every task could each make 48,000 pins.','One worker needs no operations to make a pin.','Each worker does all operations, producing perhaps one pin per day independently.','Ten workers perform no work until an assembly line is built in 1913.'],2,
 '最初的针厂情境用什么作为比较基线？',['十人已分好全部工序，每人生产 48,000 枚。','一名工人无需任何工序就能做针。','每人独自做所有工序，每天或许做一枚针。','十人直到 1913 年造流水线才工作。'],
 ['A 初始情境尚未分工，也没出现该每人产量。','B all the operations 明说有完整工序。','C If...all operations 与 maybe one pin a day 给出假设及近似产量。','D 将后文另一段历史年份混入当前假设；Imagine 是思想情境，不是随机分派工人的实测报告。'],
 ['If one worker did all the operations necessary to produce a single pin, this worker could produce maybe one pin a day.'],
 'independently','独立地；各自完成地','在初始比较中指每人自行做完整生产流程，非专门负责一道工序','The two groups worked independently before comparing their notes.',['work independently','produce independently'],
 '像任何好书一样，The Wealth of Nations 以精彩观察开篇。想象一家针厂。如果一名工人独自做完一枚针所需的所有工序，他一天或许只能生产一枚。这意味着，十名工人各自独立工作，一天仅生产十枚。')

add(15,'细节','Which output does Smith estimate for ten workers dividing the operations?',
 ['4,800 pins for the whole group and 48,000 per worker each day.','Ten pins for the whole group and one per worker each day.','48,000 pins per worker, with no group total stated.','48,000 pins for the group, or 4,800 per worker each day.'],3,
 'Smith 估计十名分工工人的产量是多少？',['全组 4,800，每人每天 48,000 枚。','全组十枚，每人每天一枚。','每人 48,000 枚，没有全组产量。','全组每天 48,000 枚，平均每人 4,800 枚。'],
 ['A 颠倒全组与人均，且无法与十人相合。','B 这是前一未分工基线，不是本段分工估算。','C 48,000 是十人合计，不是每人。','D ten workers、48,000、4,800 per worker 对应；相比前段每人或许一枚，文中称 4,800 倍，不是 48,000 倍。estimated 保留估算性质，不是所有工厂保证值。'],
 ['Adam Smith estimated that, this way, these ten workers could produce 48,000 pins a day, or 4,800 per worker.'],
 'division of labor','劳动分工','把生产过程分给各自负责一两道工序的人，不是简单增加人数','The division of labor gave each member a different task.',['the division of labor','a simple division of labor'],
 '但如果十人各自专门负责一两道工序呢？例如一人拉金属丝，一人拉直，一人切断，一人磨尖针头，等等。Adam Smith 估计，这样十人一天能生产 48,000 枚，即每人 4,800 枚。因此，简单分工就会让生产力提升 4,800 倍！')

add(16,'同义改写','Which wording best preserves “is often equated with” in this sentence?',
 ['Is frequently treated as closely identified with.','Is always proved mathematically identical to.','Is described as having no relationship with.','Is rarely mentioned alongside.'],0,
 '哪项最保留本句 is often equated with 的意思？',['常被看作与……紧密相联或等同。','总被数学证明完全相同。','被描述为与……毫无关系。','很少与……一同提起。'],
 ['A 保留 often 的频率和社会理解中的“等同看待”。','B often 不是总是，也非数学证明。','C 与 equated with 相反。','D often 不是很少；No wonder 是承接前述估算的评论，不是新实验。'],
 ['modernization is often equated with specialization and the division of labor.'],
 'equated with','被等同于；被看作一回事','描写人们如何理解现代化，不保证概念在每种定义下完全一致','Speed is sometimes equated with efficiency, though they are not identical.',['be equated with','often equated with'],
 '难怪现代化常被等同于专业化和劳动分工。')

add(17,'细节','Which timeline preserves the qualification in the account of Ford’s factory?',
 ['The factory produced over 10,000 per day before it started making the Model T.','The assembly line was introduced in 1908 after maximum output had already been reached.','After the assembly line was introduced in 1913, output eventually exceeded 10,000 per day.','The text says output exceeded 10,000 on the exact first day of the 1913 change.'],2,
 '哪一时间线保留 Ford 工厂叙述中的限定？',['开始造 Model T 前，日产已超过一万。','1908 年在达到最高产量后才引入流水线。','1913 年引入流水线后，产量最终超过每天一万。','文字说 1913 年改变的第一天就日产超过一万。'],
 ['A At first...only a few，不能将后期产量挪到开工前。','B 1908 是开始造 Model T，1913 才是引入流水线。','C after...in 1913 与 eventually 保留先后及逐步达到的限定。','D eventually 不等于改变的精确第一天。本段其他历史概括按原书保留，不冒充独立史实或当前产量核验。'],
 ['after Ford introduced the assembly line—a far more efficient division of labor—in 1913, his factory was eventually able to produce over 10,000 per day.'],
 'assembly line','流水线；装配线','作为更高效率分工的历史例子，不是本段针厂估算的同一事件','The factory reorganised its assembly line to reduce delays.',['introduce an assembly line','assembly-line production'],
 'The Wealth of Nations 出版于 1776 年，也就是美国宣布独立的一年。原书概述，当时美国主要是农业社会，没有工厂。1908 年，Henry Ford 开始生产受欢迎的 Model T。起初工厂一天仅能生产几辆；1913 年引入流水线这种高效分工后，最终能日产超过一万辆。')

add(18,'逻辑关系','What does “Yet” challenge in this passage?',
 ['The claim that companies have never considered efficiency.','The assumption that productivity has already reached its maximum.','The fact that inventory can be tracked in real time.','The idea that assembly lines existed more than a century ago.'],1,
 'Yet 在本段挑战什么？',['公司从未考虑效率的说法。','生产力已经达到最大值的假定。','库存可以实时跟踪这一事实。','流水线已存在一百多年的想法。'],
 ['A 前面没有说公司从未考虑效率。','B you might think...maximum 后用企业继续寻找改进作反差。','C real-time inventory 是改进的例子，不是被否定的对象。','D 文中承接百余年背景，没有否定它。constantly looking 是作者描述，不是今天逐家公司实时核验。'],
 ['you might think we’ve reached maximum productivity.','Yet companies like Amazon and Target are constantly looking for more ways to improve efficiency'],
 'inventory','库存；存货','real-time inventory 指持续更新的存货信息，是效率措施例子','The shop updated its inventory after every delivery.',['real-time inventory','inventory management'],
 '这项发明已过去一百多年，你或许会以为生产力达到最大值了。毕竟，每道工序还能分得多细？然而，Amazon 和 Target 等公司仍不断找提升效率的方法，从人员调整到实时库存管理。')

add(19,'主旨','What change in the reach of division of labor is described?',
 ['Outsourcing has become reserved exclusively for wealthy corporations.','Domestic appliances eliminated every household responsibility immediately.','The division of labor disappeared from workplaces after the 1990s.','Economising and outsourcing have spread beyond workplaces into everyday life.'],3,
 '本段描述劳动分工的范围发生什么变化？',['外包变得只允许富有公司使用。','家电立即消除了所有家庭责任。','1990 年代后分工从工作场所消失。','节约效率与外包从工作场所扩展到日常生活。'],
 ['A no longer...reserved only 明确否定仅限富有者。','B easier and less time-consuming 不等于彻底消失。','C 原文是进一步分工，不是工作场所停止分工。','D 从 past mostly workplaces 到 economizing habits...our life，说明范围扩展。last two decades 以原书叙述为基准，不直接当作今日统计。'],
 ['economizing habits have thoroughly penetrated our life, resulting in further division of labor.','Outsourcing is no longer a term reserved only for multinational corporations or the rich.'],
 'outsourcing','外包；交给外部提供者完成','从公司语境扩展到家务服务，不等于所有家务都已完全外包','The firm considered outsourcing part of its cleaning work.',['outsource home cleaning','outsourcing services'],
 '过去，分工主要限于工厂、农场、餐厅等工作场所。到 1990 年代，家中多数人仍自己做饭、清洁、洗衣，尽管微波炉、洗衣机、洗碗机已使家务更轻松省时。然而原书所说的过去二十年，节约效率的习惯已深入生活，带来进一步分工。外包已不再只是跨国公司或富人的用语。')

add(20,'细节','Which services are explicitly described as outsourced by middle-class households?',
 ['Home cleaning, lawn care and even grocery shopping.','Only university experiments and scientific interpretation.','All family relationships and every financial decision.','Only tasks carried out inside multinational factories.'],0,
 '中产家庭外包的服务，原文明列哪些？',['家庭清洁、草坪维护，甚至买杂货。','只有大学实验和科学解释。','全部家庭关系与每个财务决定。','只有跨国工厂内部任务。'],
 ['A 三项服务在第一句逐一列出。','B 当前家庭例子不是大学科研分工。','C 所列服务不能扩展到全部关系；后句忙碌专业人士的 AI 使用也不是每个家庭的一切决策。','D 当前例子已从工厂进入家庭。本题只是理解原书描述，不是建议投资或为网站接入 AI。'],
 ['outsource home cleaning, lawn care, and even grocery shopping.'],
 'lawn care','草坪维护；草地养护','列为家庭可交给服务方的一项工作，不是 grocery shopping 的同义词','The neighbours hired a local service for lawn care.',['outsource lawn care','lawn care services'],
 '许多中产家庭把居家清洁、草坪维护，甚至杂货购物外包。忙碌的专业人士使用 AI 来排程、规划，甚至进行金融投资。这是原书描述的现象，不是本网站的运行功能。')

add(21,'细节','How does the passage describe big-team social psychology work?',
 ['One person always performs every operation without collaborators.','Different people handle materials, study execution, data work and interpretation.','No team member has a distinct role.','The team stops after preparing materials and never assembles a paper.'],1,
 '本段怎样描述大型团队社会心理学工作？',['总由一人独自完成全部操作。','不同人分别处理材料、执行研究、数据与解释。','没有任何成员有不同分工。','准备材料后就停止，从不组装论文。'],
 ['A 多个 someone else 明确不同人接手。','B materials、run、clean/analyze、interpret 依次列出任务。','C each...their part 表示各有分工。','D 后面明确 assemble...parts 然后进入下一篇；本段描述流程，不直接判定每篇质量或体验好坏。'],
 ['someone has to prepare experimental materials, someone else has to run the study','someone else has to interpret it'],
 'interpret','解释；阐释意义','这里是解释研究数据或结果，与清理和统计分析分列，不宜混为一项','The team discussed how to interpret the results.',['interpret results','interpret the data'],
 '学术界，大团队科学正取代传统小实验室科学，需要高度分工。在大团队社会心理学中，有人备实验材料，有人执行研究，有人清数据，有人分析，有人解释，等等。每位成员做自己的部分，团队再快速组装，转向下一篇论文。')

add(22,'细节','What output rate is stated in this sentence?',
 ['Exactly twelve papers from every scientist each month.','No papers until all collaboration ends.','Dozens of papers each year.','A single paper across the team’s entire history.'],2,
 '本句给出什么论文产出频率？',['每位科学家每月恰好十二篇。','合作全部结束前没有论文。','每年数十篇。','团队整个历史仅一篇。'],
 ['A dozens 不是精确十二，也非每月或每位个人。','B produce 明说已有产出。','C dozens...every year 给出数量级与时间单位。','D 与每年数十篇相反；这句话只说明数量，不自动证明论文质量、心理丰富性或所有团队均如此。'],
 ['they produce dozens of papers every year.'],
 'dozens of','数十；几十个','表示大约若干个“十二”的数量级，不是恰好十二这个固定数','The archive contains dozens of letters from that period.',['dozens of papers','produce dozens of'],
 '这样，他们每年能产出数十篇论文。')

add(23,'主旨','What feature of the earlier scientific work does Kagan emphasise?',
 ['A small pair performed the whole process and closely shared the emotions of success or failure.','Hundreds of separate experts each completed one isolated step.','Every experiment had guaranteed success and abundant funding.','Graduate students were never involved in producing papers.'],0,
 'Kagan 强调早期科研的什么特点？',['一小对人完成整个过程，密切共享成败情绪。','几百位分开的专家各做一道孤立步骤。','每次实验必成功且资金充足。','研究生从未参与论文。'],
 ['A two minds and four hands...all the work 与成败情绪 restricted to a pair 对应。','B 这是他之后对大团队的对照，不是 earlier work 的描述。','C often with no outside funds，且明确允许失败。','D help of a graduate student 明确有参与。引语是 Kagan 对其研究生年代的回顾，不是对所有年代每项科研的普遍测量。'],
 ['two minds and four hands, often with no outside funds, performed all the work.','was restricted to a pair of agents.'],
 'savored','细细体会；享受','指成功时体验到的骄傲，不是品尝食物的字面场景','She savored the satisfaction of finishing the difficult repair.',['savor pride','savor a success'],
 '已故 Harvard 心理学家 Jerome Kagan 感叹这种趋势：“我读研究生的年代，典型科学家到大学楼的地下室，带着一位研究生，一遍遍写报告有趣结果的论文……两个头脑、四只手，常没有外部经费，完成所有工作。在这样的条件下，实验成功时享受的自豪，或失败时挫折与悲伤的混合，只由这两个人共同体会。”')

add(24,'语境词义','What does “diluted” mean in Kagan’s comparison?',
 ['Mixed with a measured volume of water.','Proved entirely absent from every team member.','Turned into a larger number of published papers.','Less concentrated or personally intense when spread across many contributors.'],3,
 'Kagan 的比较中 diluted 是什么意思？',['加入测定体积的水。','证明每位成员完全没有情绪。','转变成更多已发表论文。','分散到许多贡献者后，不那么集中、切身强烈。'],
 ['A 情绪稀释是比喻，不是化学加水实验。','B seriously diluted 不等于所有人毫无情绪。','C 当前句谈情绪，非把情绪直接计为论文数。','D 承接上段一对人共享成败，再对照数百专家及执行团队。不能把 Kagan 的评价冒充测量了每位大团队成员的情绪。'],
 ['These emotions are seriously diluted when hundreds of experts design experiments to be executed by teams.'],
 'diluted','被稀释的；强度被分散的','比喻成果与过程分散到多人后，个体情绪体验没那么集中','The personal impact of the achievement felt diluted across the huge organisation.',['diluted emotions','seriously diluted'],
 '“当数百位专家设计实验，再由团队执行时，这些情绪就被严重稀释了。”')

add(25,'作者意图','What misunderstanding does the author explicitly correct about Kagan?',
 ['That Kagan believed every team produced no papers.','That his concern was about output quantity rather than the psychological experience of science.','That Kagan had ever worked with a graduate student.','That Marx’s speculation was an experiment measuring team productivity.'],1,
 '作者明确纠正关于 Kagan 的什么误解？',['Kagan 认为所有团队都不写论文。','他的关切只是产出数量，而非做科研的心理体验。','Kagan 曾与研究生合作。','Marx 的推测是测量团队产出的实验。'],
 ['A 原文没有归给 Kagan “团队零产出”的观点。','B not complaining about productivity 后用 Instead 转向 psychological and experiential aspects，正是在纠正这一误解。','C 本段没有撤回研究生合作的回顾。','D speculated 表示理论性推测，不是实验；第三句引出 Marx，不能把前面 Kagan 的体验批评全改归 Marx。'],
 ['Kagan was not complaining about the productivity of team scientists. Instead, he was lamenting the psychological and experiential aspects of doing science today.'],
 'experiential','体验的；亲历方面的','区别于产出数量，指做科研过程中的亲身感受','The course included an experiential component in the workshop.',['experiential aspects','psychological and experiential'],
 '说清楚，Kagan 并不是抱怨团队科学家的生产力，而是在惋惜当今做科学的心理与体验层面。Karl Marx 则曾就劳动分工的多种负面后果作过著名推测。')

assert len(out)==25 and [q['id'] for q in out]==[t['questionId'] for t in targets]

def persist():
 path=ROOT/'source/short-questions/additional.json';existing=load('source/short-questions/additional.json');byid={q['id']:q for q in existing}
 for q in out:
  if q['id'] in byid:assert byid[q['id']]==q,('Refuse to overwrite changed authoring',q['id'])
  else:existing.append(q)
 path.write_text(json.dumps(existing,ensure_ascii=False,indent=2)+'\n',encoding='utf8',newline='\n')
 review=dict(batchId='batch-020',date='2026-10-22',pdfSha256=b['pdfSha256'],checkedPdfPages=list(range(77,83)),questionIds=[q['id'] for q in out],paragraphs=[dict(id=pid,textSha256=hashlib.sha256(pp[pid]['text'].encode()).hexdigest()) for pid in dict.fromkeys(q['paragraphId'] for q in out)],note='完整PDF77–82原页视觉对照，含第7章结尾与第8章开篇、跨页导言和Kagan/Marx段落。保留近似转述、个人反事实、针厂假设估算与基线、Ford的eventually、原书历史/相对时点及心理体验观点归属；书中AI描述不作为网站功能。全段审阅不冒充所有候选句已配题。')
 (ROOT/'source/short-questions/review-chapter07-08-next25.json').write_text(json.dumps(review,ensure_ascii=False,indent=2)+'\n',encoding='utf8',newline='\n')
 print('Saved',len(out),'of 25 individually authored exercises')

if __name__=='__main__':persist()
