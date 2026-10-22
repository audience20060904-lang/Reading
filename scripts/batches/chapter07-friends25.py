"""25 individually authored exercises for frozen targets, PDF pages 73-77.
Preserve printed English, source positions and all previously published questions.
"""
from pathlib import Path
import json,hashlib
ROOT=Path(__file__).resolve().parents[2]
load=lambda p:json.loads((ROOT/p).read_text(encoding='utf8'))
b=load('public/data/book.json');plan=load('public/data/reading-plan.json');targets=load('source/short-questions/batch019-targets.json')['targets']
ss={s['id']:s for s in b['sentences']};pp={p['id']:p for p in b['paragraphs']};out=[]
def add(i,kind,prompt,options,answer,prompt_zh,options_zh,analyses,quotes,word,meaning,context,example,collocations,translation,support='explicit'):
 t=targets[i-1];u=next(u for u in plan['units'] if u['id']==t['readingUnitId']);group=[ss[sid] for sid in u['sentenceIds']];p=pp[u['paragraphId']];text=p['text'][group[0]['start']:group[-1]['end']]
 assert hashlib.sha256(text.encode()).hexdigest()==t['passageSha256'];evidence=[]
 for quote in quotes:
  offset=text.find(quote);assert offset>=0,(i,quote);start=group[0]['start']+offset;end=start+len(quote);touching=[s for s in group if s['start']<end and s['end']>start]
  evidence.append(dict(quote=quote,sentenceIds=[s['id'] for s in touching],sources=list({(r['pdfPage'],r['block']):r for s in touching for r in s['sources']}.values())))
 assert word.lower() in text.lower(),(i,word)
 out.append(dict(id=t['questionId'],version=1,readingUnitId=u['id'],chapterId=u['chapterId'],sectionId=u['sectionId'],paragraphId=u['paragraphId'],sentenceIds=u['sentenceIds'],passage=text,prompt=prompt,options=options,answer=answer,type=kind,promptZh=prompt_zh,optionsZh=options_zh,analyses=analyses,evidence=evidence,vocabulary=[dict(word=word,meaning=meaning,context=context,example=example,collocations=collocations)],translation=translation,support=support,editorialStatus='PDF 第 73–77 页逐题原页核对；固定原句和来源；区分随机干预的实测、自报、未测推测、团队调查、私人叙事、假设情境和电影引例'))






add(1,'同义改写','Which statement best preserves the description of playful people?',
 ['They never treat any situation seriously.','They avoid every responsibility regardless of context.','They always worry about presenting themselves as important.','They do not overvalue their own seriousness and seem able to adjust to the situation.'],3,
 '哪项最保留这句对有玩心者的描述？',['他们对任何情况都不认真。','他们不论情境都回避所有责任。','他们总担心怎样显得重要。','他们不过度严肃地看待自己，似乎能按情况调整态度。'],
 ['A when to be serious 明确保留认真时刻。','B 没有回避所有责任的说法。','C 与 do not take themselves too seriously 相反。','D 保留不自视过重和何时轻松、何时认真两方面；seem 也不能改成每次必然判断正确。'],
 ['they seem to know when to take it easy and when to be serious.'],
 'take it easy','放轻松；不绷得太紧','与 be serious 对照，强调按情境调整，不是永远不努力','After finishing the report, she decided to take it easy for an hour.',['take it easy','know when to take it easy'],
 '总体而言，有玩心的人不过分严肃地看待自己，而且似乎知道什么时候该放轻松，什么时候该认真。')

add(2,'细节','What did the randomly assigned counting group do in the recent study?',
 ['Receive a fixed programme requiring more outdoor vacations.','Count their own playful activities each day for one week.','Measure the personality of every person they met for a year.','Avoid noticing anything playful until the study ended.'],1,
 '近期研究中，被随机分到记录组的参与者做什么？',['接受要求增加户外假期的固定安排。','连续一周每天清点自己做过的有玩心的事。','全年测量遇到每个人的人格。','研究结束前避免注意任何好玩的事。'],
 ['A nature 和 vacation 属于前文 2013 年比较，不是该干预的分派任务。','B count...every day for one week 明确任务与时长，对照组没收到清点指令。','C 没有全年或评别人性格的任务。','D 恰恰要求注意和清点有玩心的事，非回避。随机分派的是清点任务，不能改写成强制所有人增加同样多玩耍。'],
 ['randomly assigned some participants to count the playful things they did every day for one week'],
 'communing with nature','亲近自然；沉浸于自然','出现在另一项偏好比较中，须与后句的随机清点任务区分','She enjoys communing with nature during quiet walks.',['commune with nature','enjoy communing with nature'],
 '在 2013 年论文中，Proyer 发现，有玩心者比玩心较少者对生活略更满意。他还发现，幸福者享受亲近自然，有玩心者则不然。反过来，幸福者并非特别喜欢度假，有玩心者却喜欢。另一项近期研究把一些参与者随机分派为连续一周每天清点自己做过的有玩心的事；其他人则未收到清点指令。“近期”依原书叙述时点。')

add(3,'推断','Which distinction between evidence and speculation is explicit in this passage?',
 ['Satisfaction and depression were reported outcomes; greater psychological richness is the author’s unmeasured expectation.','Psychological richness was measured, but satisfaction was not.','The intervention proved equal improvements in every dimension for every participant.','The authors measured only meaning and ignored all other outcomes.'],0,
 '本段明确区分了哪种证据与推测？',['满意度与抑郁是所报告的结果；心理丰富性提升是作者对未测维度的预期。','心理丰富性测了，满意度没测。','干预证明每人在每个维度都同等改善。','研究者只测意义，忽略其他结果。'],
 ['A 第一行是参与者报告的生活满意与抑郁差异，下一句明确未测 meaning 或 richness，I suspect 转为本书作者推测。','B 恰好颠倒测量范围。','C 没有每人、每维度同等改善的证据。','D did not measure meaning 与选项相反。up to three months 是所报告随访范围，不能写成终身持续或确定临床治疗。'],
 ['reported more life satisfaction and less depression than those in the control group','The authors did not measure meaning or psychological richness, but I suspect'],
 'intervention','干预；研究中安排的任务','此处指前述玩心记录任务，其已测结果与作者对未测维度的推测必须分开','The intervention asked participants to record one daily experience.',['after the intervention','an intervention group'],
 '记录玩心经历的人，比对照组报告更多生活满意和更少抑郁，不仅在干预刚结束时如此，最长随访到三个月后也如此。研究者没有测量意义或心理丰富性，但我猜，这种玩心干预对增进心理丰富性可能特别有效，因为玩心很可能带来新奇、有趣的经历。','inference')

add(4,'作者意图','Why are the sitcoms and Samantha mentioned?',
 ['To establish a survey of how all real friends manage appointments.','To show that friendship requires living inside a television studio.','To illustrate an appealing image of spontaneity and how friends may encourage it.','To argue that planned interactions cannot be enjoyable.'],2,
 '为什么提到情景喜剧和 Samantha？',['确立所有现实朋友如何约时间的调查结果。','说明友谊必须发生在电视摄影棚。','描绘自发性的吸引人形象，以及朋友可能带来的带动作用。','论证计划好的互动都不可能愉快。'],
 ['A 原文称 fantasy world，是虚构引例而非总体调查。','B fictional apartment 不等于现实交友的必要地点。','C 随意串门、每天做未计划之事，以及类似 Samantha 的朋友，共同说明自发性。','D 没有否定所有计划活动的乐趣。'],
 ['they portray a fantasy world where you can pop in and out of a friend’s apartment anytime you want','can bring playfulness and spontaneity to your life.'],
 'spontaneity','自发性；随兴而为','强调未经预先安排的活动，而非保证每次都适合所有人','Their free afternoon left room for spontaneity.',['bring spontaneity to life','playfulness and spontaneity'],
 '像玩心一样，自发性也能丰富人生。Friends 和 Seinfeld 等情景喜剧持续受欢迎，一个原因是它们描绘幻想世界：随时进出朋友公寓，无须预约，每天都可做没计划的事。如果你天性不随兴，结交像 Sex and the City 中 Samantha 那样的朋友，可能把玩心与自发性带进生活。')

add(5,'细节','When did the author describe almost daily informal coffee with someone?',
 ['Only after he stopped seeing all his graduate-school friends.','During graduate school, when many friends were nearby at school.','After every colleague had scheduled a meeting two weeks ahead.','Only during planned annual outings with his wife.'],1,
 '作者何时几乎每天都与人随意喝咖啡？',['仅在不再见研究生朋友之后。','研究生时期，许多朋友都在学校附近时。','每位同事都提前两周预约之后。','仅在与妻子计划好的年度出游中。'],
 ['A 文中正是在朋友都在校时发生，不是停止往来之后。','B In graduate school 后接串门、过街喝咖啡及 almost every day。','C 当前片段没有同事两周预约的安排。','D coffee with someone 不限妻子，也非每年一次。自述不能推广为所有研究生或教师的日程。'],
 ['In graduate school, when most of my friends were at school','Almost every day, I had coffee with someone.'],
 'stop by','顺便拜访；临时过去看看','形容未预先安排的办公室探访，不是停止工作永久离开','I may stop by your office after class.',['stop by an office','stop by for coffee'],
 '一个难题来了：你上次与人随兴外出是什么时候？有机会时，我仍会和妻子随兴出门，但与朋友这样做已经多年没有了。读研究生时，大多数朋友都在学校，我会顺便去实验室伙伴的办公室，一起过街到 Espresso Royale 喝咖啡。几乎每天，我都和人喝咖啡。')

add(6,'语境词义','What does “unplanned” indicate about the lunches?',
 ['They never happened despite being scheduled.','They were always eaten alone.','They happened exactly once, at a formal appointment.','They were not arranged in advance.'],3,
 'unplanned 说明这些午餐怎样？',['虽已排程却从未发生。','总是独自吃。','只发生一次，且正式预约。','事先没有安排好。'],
 ['A unplanned 不是已预约又取消。','B with someone 明说与他人一起。','C Almost every day 与只一次相反，unplanned 也不等于正式预约。','D 表示非预先安排的相聚，不要求每次都与同一个人。'],
 ['Almost every day, I ate lunch with someone unplanned.'],
 'unplanned','未经计划的；事先未安排的','修饰午餐相聚的自发性质，不是没有吃成或没有同伴','An unplanned conversation led to a useful idea.',['an unplanned lunch','unplanned interactions'],
 '几乎每天，我也会未经预先安排地与人一起吃午饭。')

add(7,'细节','What happened when the author first invited the nearby assistant professor for coffee?',
 ['The colleague immediately accepted and left his office.','The author sent a formal invitation before taking the faculty job.','The author dropped by and invited him, but the colleague said he could not.','The colleague invited the author to a laboratory across town.'],2,
 '作者最初邀请附近助理教授喝咖啡时，发生什么？',['对方立即接受并离开办公室。','作者取得教职前先寄正式邀请。','作者顺路敲门邀请，对方却说不行。','对方邀请作者到城另一头的实验室。'],
 ['A Nope. I can’t. 与立即接受相反。','B When I got a faculty position 才发生，且是敲门开口。','C dropped by、knocked、邀请及否定回答均直接对应。','D 没有跨城实验室邀请的信息。本片段的拒绝不能推成对方永不愿见面。'],
 ['I knocked on the door and said, “Hi, Bob, do you want to grab coffee?” He said, “Nope. I can’t.'],
 'grab coffee','一起喝杯咖啡','口语式随意邀请，不必是正式排程会议','We could grab coffee after the seminar.',['grab coffee with someone','want to grab coffee'],
 '我在 University of Minnesota 得到教职时，希望也这样，便顺路去附近一位助理教授的办公室。我敲门说：“嗨，Bob，要不要喝杯咖啡？”他说：“不行。我不能。”')

add(8,'推断','What aspect of the reply appears to stun the author?',
 ['A casual coffee invitation turned into a calendar check and a proposal for two weeks later.','The colleague had forgotten that coffee existed.','The PDA proved the colleague had no responsibilities.','The colleague refused any contact for the rest of his life.'],0,
 '回答的什么方面似乎使作者惊讶？',['随意喝咖啡的邀请变成查日程、约两周后。','同事忘记咖啡的存在。','PDA 证明同事毫无责任。','同事拒绝此后终身任何联系。'],
 ['A right now 没空，接着查日程说两周后；作者由此对照教授与研究生生活。','B 没有失忆内容。','C 查时间表体现安排，不证明没有责任。','D What about in two weeks 是另提时间，不是终身拒绝。此处是作者个人反应，不是所有教授的统计结论。'],
 ['looked at his schedule carefully, and said, “What about in two weeks?” I was stunned.'],
 'stunned','震惊的；惊讶得愣住的','描述作者对日程安排方式的反应，不是身体被击昏','She was stunned by the unexpected reply.',['be stunned by','a stunned reaction'],
 '“我现在没有时间。”然后他翻口袋，掏出 PDA（那是 2000 年 9 月），仔细看日程说：“两周后怎么样？”我愣住了。我心想，原来这就是教授与研究生的不同。','inference')

add(9,'语境词义','What does the advice to be “stingy with my time” mean?',
 ['Spend all available time with every visitor.','Refuse to pay money for coffee.','Work without ever considering productivity.','Be sparing about giving time away, to protect productivity.'],3,
 'be stingy with my time 这条建议是什么意思？',['把所有时间都给每位访客。','拒绝付咖啡钱。','工作时完全不考虑产出。','谨慎分配给别人的时间，以保护工作产出。'],
 ['A 与 highly protective、stingy 方向相反。','B with my time 明确是时间，不是钱。','C Otherwise, I wouldn’t be productive 给出产出理由。','D 表示不轻易给出时间；建议归于一位资深教授，不应错当普遍实验定律或网站要求。'],
 ['A senior professor later advised me to be stingy with my time. Otherwise, I wouldn’t be productive.'],
 'stingy with','舍不得给出；对……吝惜','这里指严格保留时间，不是关于金钱的原义场景','He was stingy with the time he allowed for interruptions.',['stingy with one’s time','be protective of one’s time'],
 '教授不只是忙，也高度保护自己的时间。后来，一位资深教授劝我要吝惜时间，否则便不会有工作产出。')

add(10,'主旨','What comparison did Hinds want to investigate?',
 ['Whether all online meetings should be replaced by coffee breaks.','Whether teams at multiple sites collaborate and innovate at the same rate as teams at one site.','Whether professors drink more coffee than graduate students.','Whether the pandemic made all workers equally spontaneous.'],1,
 'Hinds 想研究什么比较？',['所有线上会议是否都应被咖啡休息取代。','多地点团队与单地点团队的协作和创新速度是否相同。','教授喝咖啡是否比研究生多。','疫情是否使所有工作者同样自发。'],
 ['A 当前片段未提出全面替换会议的政策。','B multiple sites 与 single site 是明确比较组，关注 collaborate and innovate。','C 前面咖啡故事不是这里的研究问题。','D 没有所有人同样的命题；wondered if 仍是提出问题，不是已经给出因果结果。'],
 ['wondered if work teams consisting of people at multiple sites collaborate and innovate at the same rate as work teams where everyone is at a single site.'],
 'collaborate','协作；合作','与 innovate 并列，指团队共同工作，而非测量个人咖啡偏好','Researchers at the two campuses collaborate on the project.',['collaborate with a team','collaborate and innovate'],
 '我们生活在高度排程的时代，日历排得满满，几乎不留随兴活动机会。疫情时期转向远程工作，更限制了自发互动。Stanford Business School 研究工作团队、协作与创新的教授 Pamela Hinds 想知道，多地点团队是否能像所有人同处一地的团队，以相同速度协作和创新。')

add(11,'细节','What pattern was reported for the geographically distributed teams in the survey?',
 ['More spontaneous communication, more shared identity and less task conflict.','No difference in communication or conflict from concentrated teams.','Less spontaneous communication, less shared identity and more task conflict.','The same shared identity, with all conflict permanently removed.'],2,
 '调查中的地理分散团队呈现什么模式？',['更多自发沟通、更多共同认同、更少任务冲突。','与集中团队的沟通及冲突都没差别。','较少自发沟通、较少共同认同、更多任务冲突。','共同认同不变，所有冲突永久消失。'],
 ['A 三个比较方向都倒置。','B 结果明确报告差别。','C less、less、more 与原句逐一对应。','D 没有共同认同不变或永久消除冲突的证据。样本是单一跨国公司研发部门的49个团队，survey 不是把所有公司随机分派，研究者的机制解释不能直接推广成普遍确定因果。'],
 ['geographically distributed teams had far less spontaneous communication, less shared identity, and far more task conflict'],
 'escalate','升级；变得更严重','指研究者所说冲突可能逐渐加剧，不是冲突必定消失','The team discussed the disagreement before it could escalate.',['conflicts escalate','before they escalate'],
 'Hinds 与 Mark Mortensen 合作，调查单一跨国公司研发部门的四十九个团队。结果显示，地理分散团队比集中团队少得多自发沟通、共同认同较少，任务冲突更多。两人总结：“自发沟通有助共同认同、共享情境的形成，也帮助分散团队在冲突升级前识别并解决冲突。”')

add(12,'语境词义','What does “initiate” mean in the sentence?',
 ['Start or set in motion.','Cancel permanently after completion.','Record as a formal meeting minute.','Prove impossible under every circumstance.'],0,
 '本句 initiate 是什么意思？',['开始；发起。','完成后永久取消。','记入正式会议纪要。','证明在所有情形都不可能。'],
 ['A initiate spontaneous interactions 指发起自发互动。','B 不是完成后的取消。','C 不指会议记录。','D harder and harder 表示更困难，非绝对不可能。'],
 ['initiate spontaneous interactions with others.'],
 'initiate','发起；开始','指主动开启与他人的自发互动，不是使之终结','A simple question can initiate a conversation.',['initiate interactions','initiate a conversation'],
 '随着工作会议越来越多通过 Zoom 等线上形式进行，主动发起与他人的自发互动，变得越来越难。')

add(13,'细节','What conditions are linked to college friendships in the passage?',
 ['Living far apart and meeting only through appointments.','Close proximity with repeated, unplanned interactions.','Sharing exactly the same career for life.','Having no contact outside formal classes.'],1,
 '本段把大学友谊与什么条件相连？',['住得很远，只在预约时见面。','彼此住得近，反复发生未经安排的互动。','一生从事完全相同的职业。','正式上课之外没有联系。'],
 ['A close proximity 与远隔相反，unplanned 也不是仅预约。','B 居住接近与 repeated and unplanned interactions 都是明列条件。','C 没有同一终身职业的要求。','D 可能甚至同宿舍，不能限于课堂。毕业后朋友 might 是可能的同事或孩子朋友的父母，不是排他清单。'],
 ['College friends are the friends you lived in close proximity to','with whom you had repeated and unplanned interactions.'],
 'proximity','接近；邻近','指地理和居住位置靠近，有利于反复碰面，不是亲密感本身的同义词','Living in close proximity made informal visits easier.',['in close proximity to','close proximity'],
 '成年交新朋友时，自发性带来另一项挑战。大学朋友与毕业后朋友有什么不同？大学朋友是与你住得近、可能甚至同宿舍、与你反复发生未经计划互动的人。毕业后的朋友，可能是同事，或孩子朋友的父母。')

add(14,'推断','How should “I would be surprised if” be understood here?',
 ['As a measured rule that no adult can ever make a close friend.','As proof that the reader has never had any college friends.','As a claim that every post-college friendship is equally close.','As the author’s expectation that matching college-level closeness is difficult, not impossible.'],3,
 'I would be surprised if 在这里应怎样理解？',['测量证实任何成年人都不能再交密友。','证明读者从未有大学朋友。','宣称毕业后每段友谊都同等亲密。','作者预期达到大学密友那样的亲密较难，而非不可能。'],
 ['A 主观预期不是所有人的测量定律。','B 问句没有证实读者个人经历。','C as close as 是比较门槛，不是每段同样亲密。','D would be surprised 表达作者的怀疑或低预期，不能把条件句改成绝对禁止。'],
 ['I would be surprised if you were able to make new friends as close as your best friends from college.'],
 'as close as','和……一样亲密','比较友谊的亲密程度，不是地理距离的比较用法','The new colleagues gradually became as close as old classmates.',['as close as a best friend','become close with someone'],
 '你和他们有多亲近？如果你能交到像大学里最好的朋友那样亲密的新朋友，我会感到惊讶。','inference')

add(15,'语境词义','What are “K.O.F.’s” in Williams’s quotation?',
 ['Friends guaranteed to remain best friends forever.','A formal experimental category based on a measured age threshold.','“Kind of friends”: situational friends, at least for now.','Only people who share the same dormitory room.'],2,
 'Williams 引语中的 K.O.F.’s 指什么？',['保证永远最好的朋友。','基于测定年龄阈值的正式实验类别。','某种程度的朋友：至少暂时是情境性朋友。','仅限同一宿舍房间的人。'],
 ['A 与 situational、for now 的暂时性不符。','B 记者引语不是测出三十岁绝对界线的实验。','C 括号 kind of friends 直接释义，和前文 situational 相接。','D 当前引语讲成年工作情境，没有限定宿舍。fatalism can creep in 是可能出现的感受，不能改成注定无法交密友的事实。'],
 ['situational friends: K.O.F.’s (kind of friends)—for now.'],
 'fatalism','宿命感；认为事情已注定的心态','指对成年交密友可能生出的感受，不是作者测得的必然命运','A sense of fatalism made it harder for him to try again.',['a sense of fatalism','fatalism can creep in'],
 '在“Why Is It Hard to Make Friends Over 30?”一文中，New York Times 记者 Alex Williams 总结：“不管结交多少朋友，宿命感可能悄悄出现：像青少年或二十岁出头那样交 B.F.F. 的时期，差不多过去了。该接受情境性朋友了：K.O.F.（某种程度的朋友）——至少暂时如此。”工作中，你可能因同一项目而与某人亲近。')

add(16,'逻辑关系','What explains the difficulty maintaining closeness after the pilot ended?',
 ['The loss of constant day-to-day interaction that had sustained the friendship.','A confirmed argument that made both women refuse any later contact.','A rule banning television writers from becoming friends.','The fact that both women had never worked together.'],0,
 '试播集结束后，为什么难以维持亲密？',['支撑友谊的持续日常互动消失。','已证实争吵使两人拒绝此后任何联系。','规定禁止电视编剧交朋友。','两人从未一起工作。'],
 ['A without that constant day-to-day interaction 明确指出互动条件不再存在。','B 文中没说争吵或永久拒联。','C 没有行业禁令。','D 她们正是在同一团队工作而亲近。这个记者转述个案说明情境变化，不证明项目结束的友谊必然都消失。'],
 ['it was hard to be as close without that constant day-to-day interaction'],
 'pilot','试播集；试播节目','在 NBC series 的语境中指电视试播集，不是飞机驾驶员','The network ordered a pilot for the new comedy.',['a pilot episode','after the pilot was over'],
 '但除非再次与此人共事同一项目，否则很难保持联系。Williams 写到 NBC 剧集 Up All Night 的一位编剧，她与团队另一位女性变得亲密：“但试播集一结束，没有持续日复一日的互动，就很难同样亲近；再没有那种长下午，自然延伸到傍晚，在海滩闲逛后再去酒吧。”')

add(17,'推断','Which limited conclusion does the passage support about adult friendship?',
 ['Having a partner proves that every new friend will be rejected.','Parents are permanently incapable of friendship.','Distance no longer matters once someone has children.','Family commitments can make frequent, nearby, spontaneous meetings harder to arrange.'],3,
 '关于成年友谊，本段支持什么有限结论？',['有伴侣就证明每个新朋友都会被拒绝。','父母永久无法拥有友谊。','有孩子后距离完全无关紧要。','家庭责任可能让频繁、邻近而随兴的见面更难安排。'],
 ['A partner must like... 不等于所有人都拒绝。','B can feel nearly impossible 是感受和困难，不是能力永远消失。','C 最后一句仍强调 lives close by。','D 伴侣、孩子与每天碰面条件共同形成安排难度；不能把“难”提升为普遍绝对不可能。'],
 ['making friends later in life can feel nearly impossible.','find someone who lives close by, with whom you can meet up every day and have spontaneous outings.'],
 'into the equation','纳入考虑；加入这些因素','把孩子也纳入生活安排的考虑，不是要进行某个实际数学计算','Travel time must also be added into the equation.',['add something into the equation','bring something into the equation'],
 '如果有伴侣，伴侣也得喜欢任何新朋友，这又更难。再把一两个孩子纳入考虑，成年后交朋友可能让人觉得几乎不可能。换句话说，毕业后，要找到一个住得近、能每天见面并随兴出游的人，确实很有挑战。','inference')

add(18,'细节','What is Moritz’s status in the account introduced here?',
 ['A randomly assigned participant in a train experiment.','A hypothetical person used by a philosopher to discuss planned and unplanned action.','The author’s colleague whose exact behaviour was observed in Minnesota.','A railway official collecting data on all passengers.'],1,
 '本段引入的 Moritz 是什么性质的人物？',['火车实验中随机分派的参与者。','哲学家用来讨论计划与非计划行为的假设人物。','作者在 Minnesota 实际观察到的同事。','统计所有乘客的铁路官员。'],
 ['A hypothetical 与随机实测参与者不同。','B He considers a hypothetical person named Moritz 明确例子性质。','C 本段没有 Minnesota 实测记录。','D 他是拿车票赴约的假设旅客，不是官员。'],
 ['He considers a hypothetical person named Moritz as an example.'],
 'hypothetical','假设的；用于思考情境的','说明 Moritz 故事是哲学情境，不应充当实际调查数据','The tutor used a hypothetical case to explain the principle.',['a hypothetical person','a hypothetical scenario'],
 '当然，我们也可以独自随兴行动。哲学家 Jason D’Cruz 用“volatile reason”一词讨论计划与非计划行为。他以一位名叫 Moritz 的假设人物为例。情境中，Moritz 有一张从 Berlin 去 Dresden 与朋友见面的火车票。')

add(19,'细节','How does Moritz justify staying on the train?',
 ['He reasons that he could call his friends to cancel and apologise.','He has already received proof that the dinner was cancelled by his friends.','He knows the concert tickets have never existed.','He was instructed by his friends to avoid Dresden.'],0,
 'Moritz 怎样为继续留在火车上找理由？',['他想，可以打电话向朋友取消安排并道歉。','他已拿到朋友取消晚餐的证明。','他知道音乐会票从未存在。','朋友指示他避开 Dresden。'],
 ['A reasoning that he could just call...cancel...apologize 明确是他所想的处理方式。','B could call 不是朋友已经取消或同意。','C 片段明确有音乐会票和原定责任。','D 路线改变来自他临时看到 Zittau 的可能，不是朋友指示。'],
 ['reasoning that he could just call his friends to cancel their plans and apologize.'],
 'reasoning','推想；给自己的理由','指角色对如何处理赴约责任的想法，不是已经完成通话的记录','She stayed a little longer, reasoning that the next train would still be available.',['reasoning that','a line of reasoning'],
 '朋友正准备晚餐，Moritz 也有当晚和朋友听音乐会的票；换句话说，他有计划和责任。然而在火车上，他看到时刻表，意识到若坐过 Dresden，就能前往陌生的 Zittau。列车到 Dresden 时，他临时决定不下车、去 Zittau，心想只要打电话取消约定并道歉即可。')

add(20,'作者意图','What interpretation of Moritz’s action is attributed to D’Cruz?',
 ['It was fully planned long before the journey.','It was an experiment proving that every cancelled commitment brings happiness.','It was unpremeditated but served a deeper desire for an interesting life.','It showed that all responsibilities should always be abandoned.'],2,
 '作者把 D’Cruz 对 Moritz 行为的什么解释呈现出来？',['旅行很久以前就已完整计划。','这是证明每次取消约定都会幸福的实验。','虽非预先深思，却满足对有趣人生的深层愿望。','所有责任都应永远抛弃。'],
 ['A not a well-premeditated deliberate action 否定预先深思。','B 仍是假设情境，没有实际实验或每次都如此的证据。','C but nonetheless 后保留自发行为与深层愿望相合的解释。','D once in a while 限定偶尔，不能改成永远一概弃责。euphoria 是角色在假设故事中的感受，不是测得的总体效果。'],
 ['not a well-premeditated deliberate action','served to fulfill Moritz’s deep desire to lead an interesting life.'],
 'nonetheless','尽管如此；然而仍然','在不是预谋行动与仍满足愿望之间构成让步','The task was difficult; nonetheless, she completed it.',['but nonetheless','nonetheless served to'],
 '火车刚离开 Dresden，Moritz 便感到强烈欣喜和自由。D’Cruz 认为，这不是预先周密考虑的刻意行动，但自发行动仍满足了 Moritz 想过有趣人生的深层愿望。自发性暂时胜过责任。作者说，我们偶尔也可以、也应该像 Moritz 那样。')

add(21,'细节','What does the author say keeping professional expertise current requires?',
 ['Only occasional laughter, with no attention to research.','Careful attention, a commitment of time and dedication.','Avoiding new literature and data visualisation.','Letting all knowledge remain unchanged after graduation.'],1,
 '作者说，更新职业知识需要什么？',['只需偶尔大笑，不必关注研究。','细心关注、时间投入与努力奉献。','回避新文献和数据可视化。','毕业后让所有知识保持不变。'],
 ['A serious business 后明列具体投入。','B careful attention、time commitment、dedication 三项均对应。','C 作者说 try to stay up to date，方向相反。','D 文中强调持续更新，不是毕业后冻结知识。I 指书中作者自己的研究工作。'],
 ['It requires careful attention, time commitment, and dedication.'],
 'stay up to date','跟进最新进展；保持知识更新','指书中作者追踪本专业文献与方法，不是声称网站已核验今天所有研究','She reads journals to stay up to date in her field.',['stay up to date on','up-to-date knowledge'],
 '我们大多数人都努力把谋生的工作做得更好。作为研究者，我努力跟进最新文献、统计、数据可视化等。这都是严肃工作，需要细心关注、时间投入和奉献。')

add(22,'逻辑关系','How is the proposed link between intense focus and burnout qualified?',
 ['It is presented as possibly one reason, rather than the sole proven explanation.','It is established as the only cause of every athlete’s difficulties.','It means talent and determination prevent every loss of enjoyment.','It shows that sport can never become a livelihood.'],0,
 '高度专注与倦怠的联系，在本段怎样被限定？',['它被提出为一种可能原因，而非唯一且已证明的解释。','它被确立为每位选手困难的唯一原因。','它表示天赋和决心避免每一种乐趣流失。','它说明运动永不可能成为生计。'],
 ['A might be one of the reasons 同时限定可能性和非唯一性。','B one of 不能改成唯一，might 不能改成确定证明。','C Nevertheless 后说明有天赋、坚毅，仍可能失去乐趣。','D 原文明说 became their jobs and livelihoods。人物例子不能作为网站新增临床诊断。'],
 ['That might be one of the reasons','the sports they loved became their jobs and livelihoods, sucking the fun out of the whole thing.'],
 'livelihoods','生计；谋生方式','与 jobs 并列，指运动变成谋生工作后的负担情境，不单指爱好','Many families depend on fishing for their livelihoods.',['jobs and livelihoods','earn a livelihood'],
 '如此专注，很容易让大量时间过去，却没有趣味或笑声。这可能是 Michael Phelps、Simone Biles、Naomi Osaka 等世界顶尖选手发生倦怠的原因之一。他们有天赋、决心和大量坚毅。尽管如此，某一刻，他们热爱的运动变成了工作与生计，使整件事失去趣味。')

add(23,'作者意图','Why does the author mention other important factors at this point?',
 ['To withdraw the claim that athletes need hard training.','To establish that all athletes have identical personal histories.','To replace every account of difficulty with one single universal cause.','To prevent seriousness and dedication from being treated as the only explanation.'],3,
 '作者在这里为什么提到其他重要因素？',['撤回运动员需要刻苦训练的说法。','确立所有运动员的私人经历相同。','用一个普遍单一原因替代所有困难解释。','避免把严肃和投入当成唯一解释。'],
 ['A 最后一句仍说 They must train hard。','B 举出不同人物的不同经历，并非全体相同。','C other factors 恰恰增加解释因素。','D not just seriousness and dedication 明确限定前一解释。父母离异与性虐待是原书归于人物经历的重要因素，本题不据此独立诊断或解释所有人的心理健康。'],
 ['it is not just seriousness and dedication that brought about their burnout and depression.'],
 'To be sure','确实；诚然；须明确承认','在此引入必要限定，承认还有其他因素，非抹去前后文','To be sure, the plan has limits that need attention.',['to be sure','not just one factor'],
 '当然，原书还列出引发他们心理健康问题的其他重要因素，例如 Phelps 的父母离异，或 Biles 经历的性虐待。必须明确，并非只有严肃与投入带来了他们的倦怠和抑郁。然而，核心是精英运动员的生活艰难。他们必须刻苦训练。')

add(24,'语境词义','What does “lackluster” describe in this sporting context?',
 ['A performance that is guaranteed to break a world record.','An event that is never shown to any audience.','An unimpressive or disappointing performance.','A game played entirely without official rules.'],2,
 '这个体育语境中，lackluster 描述什么？',['保证破世界纪录的表现。','从不向任何观众展示的赛事。','不出彩或令人失望的表现。','完全没有正式规则的比赛。'],
 ['A 与 lackluster 的负向评价相反。','B recorded and broadcast 明说会记录、播出。','C 指表现平淡、不出彩，与持续竞赛及公开评价的压力相连。','D 词义不是没有规则。原句 could lose their appeal 保留可能，不是宣布所有选手都必定失去兴趣。'],
 ['Any rare, lackluster performance is recorded and broadcast.'],
 'lackluster','平淡的；不出彩的','修饰某次运动表现，而非永久否定人物能力','The team recovered after a lackluster first half.',['a lackluster performance','a lackluster start'],
 '他们必须持续参赛、表现。任何少见的不出彩表现都会被记录、播出。难怪那些他们如此热爱、如此擅长的运动，也可能失去吸引力。')

add(25,'主旨','Which balance does the author advocate in this passage?',
 ['Reject skill development because professionalism has no value.','Value specialisation while using playfulness to enjoy the journey beyond winning alone.','Treat the fictional film as experimental proof about every professional.','Measure a life only by whether it wins every competition.'],1,
 '本段作者主张什么平衡？',['专业化没有价值，因此拒绝技能发展。','肯定专攻的价值，同时用玩心享受过程，不只盯获胜。','把虚构电影当作关于所有专业人士的实验证明。','只用能否赢每次比赛衡量人生。'],
 ['A 首句明确肯定技能习得与提高。','B 肯定 specialization 后转向 all winning 的沉重，再用 journey, not just outcome 提出平衡。','C Jack 是 The Shining 的电影角色，不能当临床或因果实验结论。','D winning becomes everything 正是作者所质疑的状态。can help 不等于对所有心理困难的治疗保证。'],
 ['specialization and professionalism are great for skill acquisition and improvement.','enjoy the journey, not just the outcome.'],
 'skill acquisition','技能习得；获得技能的过程','作者明确承认专业化的益处，不能因后面的玩心论述而删去','Consistent practice supports skill acquisition over time.',['skill acquisition and improvement','support skill acquisition'],
 '说清楚，专攻与专业化很有利于技能习得和提高。但想想 Stanley Kubrick 电影 The Shining 中 Jack（Jack Nicholson 饰）的命运：只工作不玩耍，不仅让 Jack 无趣，最后也让他失去理智。当获胜成了一切，生活便过于沉重。游戏般轻松的心态，能帮助心理上卡住的人走过低谷，享受旅程，而不只是结果。')

assert len(out)==25 and [q['id'] for q in out]==[t['questionId'] for t in targets]

def persist():
 path=ROOT/'source/short-questions/additional.json';existing=load('source/short-questions/additional.json');byid={q['id']:q for q in existing}
 for q in out:
  if q['id'] in byid:assert byid[q['id']]==q,('Refuse to overwrite changed authoring',q['id'])
  else:existing.append(q)
 path.write_text(json.dumps(existing,ensure_ascii=False,indent=2)+'\n',encoding='utf8',newline='\n')
 review=dict(batchId='batch-019',date='2026-10-22',pdfSha256=b['pdfSha256'],checkedPdfPages=list(range(73,78)),questionIds=[q['id'] for q in out],paragraphs=[dict(id=pid,textSha256=hashlib.sha256(pp[pid]['text'].encode()).hexdigest()) for pid in dict.fromkeys(q['paragraphId'] for q in out)],note='完整 PDF73–77 页视觉核对，含干预结果跨页、教授对话、49团队调查、Williams引语、Moritz假设与电影例子。区分已测自报与未测心理丰富性推测、随机任务与调查关联、个人及记者叙述与总体、角色假设与实测、原书多因素说明与新增诊断。整段审阅多于本批上下文，候选句界不作人工最终分句。')
 (ROOT/'source/short-questions/review-chapter07-friends25.json').write_text(json.dumps(review,ensure_ascii=False,indent=2)+'\n',encoding='utf8',newline='\n')
 print('Saved',len(out),'of 25 individually authored exercises')

if __name__=='__main__':persist()
