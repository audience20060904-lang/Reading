"""25 individually authored exercises for frozen targets, PDF pages 90-93.
Preserve printed English, source positions and all previously published questions.
"""
from pathlib import Path
import json,hashlib
ROOT=Path(__file__).resolve().parents[2]
load=lambda p:json.loads((ROOT/p).read_text(encoding='utf8'))
b=load('public/data/book.json');plan=load('public/data/reading-plan.json');targets=load('source/short-questions/batch023-targets.json')['targets']
ss={s['id']:s for s in b['sentences']};pp={p['id']:p for p in b['paragraphs']};out=[]
def add(i,kind,prompt,options,answer,prompt_zh,options_zh,analyses,quotes,word,meaning,context,example,collocations,translation,support='explicit'):
 t=targets[i-1];u=next(u for u in plan['units'] if u['id']==t['readingUnitId']);group=[ss[sid] for sid in u['sentenceIds']];p=pp[u['paragraphId']];text=p['text'][group[0]['start']:group[-1]['end']]
 assert hashlib.sha256(text.encode()).hexdigest()==t['passageSha256'];evidence=[]
 for quote in quotes:
  offset=text.find(quote);assert offset>=0,(i,quote);start=group[0]['start']+offset;end=start+len(quote);touching=[s for s in group if s['start']<end and s['end']>start]
  evidence.append(dict(quote=quote,sentenceIds=[s['id'] for s in touching],sources=list({(r['pdfPage'],r['block']):r for s in touching for r in s['sources']}.values())))
 assert word.lower() in text.lower(),(i,word)
 out.append(dict(id=t['questionId'],version=1,readingUnitId=u['id'],chapterId=u['chapterId'],sectionId=u['sectionId'],paragraphId=u['paragraphId'],sentenceIds=u['sentenceIds'],passage=text,prompt=prompt,options=options,answer=answer,type=kind,promptZh=prompt_zh,optionsZh=options_zh,analyses=analyses,evidence=evidence,vocabulary=[dict(word=word,meaning=meaning,context=context,example=example,collocations=collocations)],translation=translation,support=support,editorialStatus='PDF第90–93页逐题核对；人物引语、个人反思、假设、比喻和哲学论述分别归属；跨短段引号按原书保留'))







add(1,'主旨','What does the author see in The Remains of the Day beyond an engaging story?',
 ['A practical manual for managing a household.','An exploration of moral dilemmas and life’s meaning.','A statistical history of every British butler.','A film review concerned only with the actors.'],1,
 '作者认为 The Remains of the Day 除了引人入胜的故事，还探讨什么？',['管理家务的实用手册。','道德困境与人生意义。','所有英国管家的统计史。','只关注演员的影评。'],
 ['A 管家职责是故事背景，不是本段所说的额外主题。','B not just...also about moral dilemmas and the meaning of life 直接定位主题。','C in the novel 限定虚构人物，非全体管家统计。','D 电影演员是括号补充，不能覆盖小说主题。'],
 ['it is also about moral dilemmas and the meaning of life.'],
 'engrossing','引人入胜的','形容小说吸引注意力，与它还有道德主题并不矛盾','The engrossing story kept her reading until midnight.',['an engrossing novel','an engrossing story'],
 '对我而言，Kazuo Ishiguro 的 The Remains of the Day 不仅是一部引人入胜的小说，讲述英国管家 Stevens 为贵族 Darlington 服务直到二战结束，也讨论道德困境与人生意义。小说中，Stevens——电影版由 Anthony Hopkins 饰演——尽力侍奉 Darlington。在事业巅峰，他管理二十八名员工，而 Darlington 在二战期间主持许多重要会议。')

add(2,'细节','What changed for Stevens after the Hall was sold?',
 ['He became the American owner of the estate.','His staff expanded and he abandoned all holidays.','He continued managing twenty-eight people without interruption.','He managed only four staff and received his first real professional vacation.'],3,
 '庄园售出后，Stevens 的处境发生什么变化？',['成为庄园的美国主人。','员工增加，并放弃一切假期。','一直管理二十八人，没有变化。','只管理四名员工，并得到职业生涯首次真正假期。'],
 ['A 美国买主是 Farraday，不是 Stevens。','B reduced...only four 表示减少，且有假期。','C 沿用上一阶段人数，忽略 however 后的变化。','D four 与 first time...real vacation 都明示。这是小说情节，不作真实人物履历核实。'],
 ['Mr. Stevens was reduced to managing a staff of only four.','Mr. Stevens is given a real vacation'],
 'execute','执行；完成','指妥善完成家务职责，不是处刑的词义','She planned the event carefully and executed each task well.',['execute duties','carefully plan and execute'],
 '他最自豪的是自己的专业素养，以及周密计划、完美执行家中一切职责的能力。然而战后，Darlington 家族世代持有的庄园最终卖给美国商人 Farraday，Stevens 管理的员工减至四人。他职业生涯首次获得真正的假期，决定去英格兰西部旅行。')

add(3,'细节','What does Stevens now have time to reflect upon?',
 ['His life so far and his service to Lord Darlington.','Only the future profits from selling the Hall.','The film actor’s career rather than his own life.','A new career he has already begun abroad.'],0,
 'Stevens 此时有时间反思什么？',['此前的人生及为 Darlington 服务的岁月。','只反思出售庄园的未来利润。','电影演员的生涯，而非自己。','已经开始的海外新职业。'],
 ['A life up to that point 与 time serving Lord Darlington 对应两个对象。','B 没有利润资料，only 也缩小了范围。','C he 指 Stevens，非演员。','D 没有已开始新职业的信息。reflect upon 表示回顾思考，不保证他已得出确定答案。'],
 ['reflect upon his life up to that point and his time serving Lord Darlington.'],
 'reflect upon','反思；仔细回顾','对自己的过去和服务经历作思考','The journey gave her time to reflect upon her choices.',['reflect upon one’s life','reflect upon past experience'],
 '他第一次有时间反思截至那时的人生，以及侍奉 Darlington 的那些岁月。')

add(4,'作者意图','What moral question does the passage raise about Stevens’s dedication?',
 ['Whether a clear purpose necessarily proves that its cause is good.','Whether Darlington’s actions were harmless to England.','Whether dedication retains value when the cause served proves morally compromised.','Whether Stevens secretly opposed Darlington throughout the war.'],2,
 '片段就 Stevens 的奉献提出什么道德问题？',['目标明确是否必能证明目标善良。','Darlington 的行为是否对英国无害。','所服务事业道德有问题时，奉献本身是否仍有价值。','Stevens 是否整个战争中都暗中反对主人。'],
 ['A 接近主题，但末尾具体问的是人生是否白费、奉献有无自身价值，并未直接作这个一般断言。','B harmed England 已给小说中的判断。','C complete waste or...worth something on its own 准确概括开放设问。','D 没有暗中反对的证据，不能补造动机。设问不等于作者已经裁定人生全部无价值。'],
 ['Did this render Mr. Stevens’s life a complete waste, or was his dedication worth something on its own?'],
 'render','使成为；使处于某状态','render...a complete waste 在设问中指是否使人生完全白费','The missing evidence rendered the conclusion uncertain.',['render something worthless','render a life a waste'],
 'Stevens 把整个人生奉献给 Darlington 和庄园。他有生活目标，也有意义——直到战争结束，Darlington 被揭示为纳粹同情者和天真的业余外交活动者，其行为最终损害英国。这是否使 Stevens 的一生彻底白费，还是他的奉献本身也有某种价值？')

add(5,'细节','Which view is expressed by Stevens in this quotation?',
 ['Darlington chose the correct path and caused no harm.','Darlington chose his own path, even though it proved misguided.','Darlington never made any choices for himself.','The author has experimentally established Darlington’s courage.'],1,
 '这段引语中，Stevens 表达什么看法？',['Darlington 道路正确且未造成伤害。','Darlington 至少自行选过道路，尽管后来证明误入歧途。','Darlington 从未自行选择。','作者通过实验证明其勇气。'],
 ['A proved...misguided 否定道路正确。','B chose...misguided...at least 三处共同支持。','C 与 he chose it 相反。','D 这是小说人物的辩解和评价，不是作者实验或认可其道德。引语在下一短段续接，不能把没出现的结尾补入当前原文。'],
 ['He chose a certain path in life, it proved to be a misguided one'],
 'misguided','被误导的；方向错误的','人物承认所选择道路出错，并非正确路线的同义词','The plan was based on a misguided assumption.',['a misguided path','a misguided decision'],
 '小说结尾，Stevens 说：“Darlington 不是坏人。他一点也不坏……阁下是个勇敢的人。他在人生中选择了一条路，后来证明那是错路，但他毕竟作了选择，至少他还能这样说。（引语续下段）')

add(6,'主旨','What does Stevens emphasize about his own service?',
 ['He relied on his lord’s wisdom and believed his work was worthwhile.','He had independently designed every political action.','He had known all along that his work was pointless.','He had never trusted Darlington at any time.'],0,
 'Stevens 强调自己服务经历中的什么？',['依赖主人的智慧，相信自己在做值得的事。','每个政治行动都由他独立设计。','一直明知工作毫无价值。','从未信任过主人。'],
 ['A 重复 trusted 并以 worthwhile 说明当时的信念。','B 依赖判断不等于独立设计所有政治行动。','C 当时相信有价值，不是明知无意义。','D trusted 的反复出现直接反驳。信念是人物自述，不能由此证明其工作事实上有益。'],
 ['I trusted in his lordship’s wisdom.','I trusted I was doing something worthwhile.'],
 'worthwhile','值得的；有价值的','人物相信自己的服务有意义，不是作者已证实其结果有益','She wanted to spend her time on something worthwhile.',['do something worthwhile','a worthwhile task'],
 '“至于我自己，我连这一点都不能声称。你看，我信任过。我信任阁下的智慧。那些年侍奉他，我一直相信自己在做值得的事情。”')

add(7,'作者意图','What new concern did reading the novel prompt in the author?',
 ['Whether the novel was a literal record of his own travels.','Whether every act of dedication necessarily benefits humanity.','Whether he should become a British butler immediately.','Whether his own dedication could be misguided and do more harm than good.'],3,
 '读小说使作者产生什么新忧虑？',['小说是否真实记录了自己的旅行。','每种奉献是否必然有益人类。','是否应立即成为英国管家。','自己的奉献是否也可能方向错误，害处大于益处。'],
 ['A mentally transported 是想象进入故事，不是亲自去过的记录。','B 将 could 的个人疑问改成普遍必然，还偏离具体自我反省。','C 没有改行决定。','D could my dedication...harm...more than help 直接对应。他也开始考虑支持掌权者的工作人员的道德处境，并非替伤害开脱。'],
 ['could my dedication to something turn out to be completely misguided and harm humanity more than help?'],
 'mentally transported','在想象中被带入','读者注意和想象进入小说时代与场所，不是身体移动','The vivid account mentally transported her to the old harbour.',['be mentally transported to','transport a reader into a story'],
 '读这部小说时，我仿佛在想象中来到 Darlington 庄园，以及二十世纪三十年代和四十年代初的事件之中。我第一次想：自己的奉献会不会也完全误入歧途，对人类伤害多于帮助？作为日本人，我一直认为帝国日本的上校和政客纯属邪恶，但此前从未考虑那些为他们工作、把一生用于支持他们的人的道德问题。')

add(8,'逻辑关系','How did the unsettling thought affect the reading experience?',
 ['It made the author happy by proving all historical actions justified.','It left his view of history completely unchanged.','It was unhappy but made the experience deeper and richer.','It proved that he had actually served as a wartime colonel.'],2,
 '这个令人不安的想法怎样影响阅读体验？',['证明历史行为都正当，令作者幸福。','完全未改变历史看法。','想法不快乐，却让体验更深、更丰富。','证明他确实曾任战时上校。'],
 ['A not a happy thought，且 falsely 保留错误信念，不是正当化。','B certainly changed 明说看法改变。','C nevertheless 把不快乐与更丰富连接，说明二者不等同。','D might have been...in their situations 是假设，不是履历。对处境的反思不等于否认伤害或免除责任。'],
 ['This was not a happy thought, but nevertheless made the reading experience deeper and richer.'],
 'entertained','曾考虑；曾在脑中容纳','entertain a possibility 指考虑可能性，不是娱乐某人','She had never entertained the possibility of being mistaken.',['entertain a possibility','entertain a thought'],
 'The Remains of the Day 挑战了我对二战中某些日本上校和其他处于道德困境者的看法：他们可能只是做自己的工作，错误地相信在服务更大的善。这本书确实改变了我看日本历史的方式。处于他们的境地，我也可能成为邪恶的上校，这是我从未考虑过的可能。这个想法不令人快乐，却使阅读更深、更丰富。')

add(9,'语境词义','What does “transportation” mean in the psychological description?',
 ['Physical travel to the location where a film was shot.','Deep immersion in a narrative through attention, imagery and feeling.','Moving a book from one room to another.','The claim that every reading experience is enriching.'],1,
 '心理学描述中的 transportation 是什么意思？',['实际去电影拍摄地旅行。','注意、想象与情感深深融入叙事。','把书搬到另一房间。','每次阅读都能丰富人生的主张。'],
 ['A 这里进入 narrative world，不是出行。','B melding of attention, imagery, and feeling 就是文中定义。','C 房间变化只是外界干扰的例子。','D not all 明确否认任何阅读都丰富。词义定位要看紧邻定义，而非日常交通义。'],
 ['a complete melding of attention, imagery, and feeling that psychologists call “transportation.”'],
 'immersed','沉浸的；全神贯注的','深入故事世界，以至于没注意身旁小变化','She was so immersed in the novel that she missed the announcement.',['be immersed in a narrative','deeply immersed'],
 '如上述例子，确有可能通过书、电影和艺术间接获得心理丰富性。但并非所有阅读或观看都丰富。那么丰富的审美体验关键是什么？首先，读或看时，人会如此沉浸在故事世界，以至于不注意外界的小变化，例如有人进房间：注意、想象与情感完全融合，心理学家称为“叙事沉浸”。')

add(10,'细节','What requirement is added beyond immersion?',
 ['The experience must involve actual travel.','The plot must be forgotten within a few days.','The story must contain no emotional events.','The experience must also be memorable.'],3,
 '除了沉浸，还增加什么要求？',['必须实际旅行。','必须几天内忘记情节。','故事不能有情绪事件。','体验还必须让人记得。'],
 ['A as if 是如同亲历，不是必须出行。','B 忘记情节作为反例，不是条件。','C 没有排除情绪。','D It also has to be memorable 直接给出新增要求；不是一沉浸就充分丰富。'],
 ['not every immersive experience is psychologically rich. It also has to be memorable.'],
 'memorable','值得记住的；留下鲜明记忆的','与数日就忘剧情的观看作对照','The unexpected conversation made the evening memorable.',['a memorable experience','remain memorable'],
 '人必须被带入叙事世界，体验故事事件，仿佛自己就在其中。其次，正如实际体验，并非每次沉浸都有心理丰富性；它还必须令人记得。我有很多次周末看完电影，几天后就忘记情节。')

add(11,'逻辑关系','How is retaining an experience related to richness here?',
 ['Retention is presented as necessary for the experience to enrich one’s life.','Retention alone is said to guarantee every form of richness.','Forgetting is presented as the key to enrichment.','Vivid memories are said to prevent indirect experiences.'],0,
 '这里保留体验记忆与丰富性有什么关系？',['保留记忆被视为体验丰富人生的必要条件。','只要记住，就保证所有丰富性。','遗忘被视为丰富人生的关键。','鲜明记忆会阻止间接体验。'],
 ['A unless...retained...not enriching 支持必要条件。','B 必要不等于充分，不能加 alone guarantee。','C not enriching 与遗忘有益相反。','D 这里谈阅读观看，未排除间接体验。IELTS 逻辑题注意 unless 表示条件，而非把条件倒转。'],
 ['unless these experiences are retained in your mind, they are not enriching your life.'],
 'retained','被保留；被记住','经验留存在心中，而非保留实体票据','Details of the journey were retained in her memory.',['be retained in memory','retain an experience'],
 '要让阅读或观看体验丰富，它必须在记忆中保持鲜明。换句话说，除非这些体验保留在心里，否则它们没有在丰富你的人生。')

add(12,'作者意图','What does the comparison with high earners illustrate?',
 ['Frequent travel always produces a satisfying life.','Psychological richness requires literally earning more money.','Having many experiences need not build lasting richness if they do not accumulate.','All sensation-seekers have low incomes.'],2,
 '与高收入者的比较说明什么？',['频繁旅行总会带来满意人生。','丰富性要求真的赚更多钱。','若体验未积累，经历很多也未必形成持续丰富性。','所有寻刺激者收入都低。'],
 ['A some...do not seem...satisfying 正是反例。','B money 是类比，不是心理丰富的字面门槛。','C 经历不断发生却不积累，类比赚得多却花光；保留 some 的范围。','D 没有寻刺激者收入调查。类比帮助说明观点，不是实验验证所有旅行者。'],
 ['psychological richness requires the accumulation of interesting experiences','They are like high-income individuals who spend all the money they earn.'],
 'accumulation','积累','强调体验留存成整体，而不只是不断追新','The archive grew through the accumulation of small discoveries.',['the accumulation of experiences','gradual accumulation'],
 '如同物质财富需要积累金钱，心理丰富也需要积累直接或间接的有趣体验。有些寻刺激者走遍世界，却发现这些多样经历似乎没合成令人满意的人生。他们不断需要新体验，就像把收入全花光的高收入者。')

add(13,'同义改写','What corresponds to saving money in the psychological-richness analogy?',
 ['Constantly replacing one experience with another.','Remembering and cherishing one’s experiences.','Avoiding all new experiences.','Turning each memory into a financial asset.'],1,
 '心理丰富性的类比中，什么对应于存钱？',['不断用新体验替换旧体验。','记住并珍惜自己的经历。','避开全部新体验。','把每个记忆变成金融资产。'],
 ['A 对应不断消费，不是保留。','B remember and cherish 是明确对应。','C 保留旧经历不等于不尝试新事物。','D 没有把记忆交易变现的要求。类比映射“保存”，不是把两类财富混成同一东西。'],
 ['the psychologically rich need to remember and cherish their experiences.'],
 'cherish','珍惜；珍爱','珍视经历，让它们在记忆中积累','They cherish the memories of their first journey together.',['cherish an experience','cherish memories'],
 '如同高收入者需存钱才会物质富有，心理丰富的人也需要记住、珍惜经历。记忆至关重要。')

add(14,'细节','Why did the author not find Home Alone particularly rich?',
 ['It lacked much complexity and did not change his perspective.','It was neither immersive nor fun.','He could not remember anything about it.','It prevented every viewer from reflecting on life.'],0,
 '作者为什么不觉得 Home Alone 特别丰富？',['不够复杂，也未改变他的视角。','既不沉浸也无趣。','他完全记不起电影。','它阻止所有观众反思人生。'],
 ['A mainly because 后直接说明两个原因。','B immersive, fun 正好相反。','C even memorable 承认记得。','D my perspective 是个人评价，不能扩大成所有观众。好玩、沉浸、记得并不在作者论述中自动充分。'],
 ['it did not have much complexity and did not change my perspective in life.'],
 'perspective','视角；看问题的方式','作品改变看人生的方式，不只是更换观看位置','The story changed her perspective on ambition.',['change one’s perspective','a new perspective on life'],
 '最后，要让阅读观看丰富，它还须有一定复杂性，并最终改变视角。Home Alone 很沉浸、好玩，甚至令人记得，但对我而言并不特别心理丰富，主要因为不够复杂，也未改变我看人生的方式。')

add(15,'细节','What narrative feature of Rashomon is described?',
 ['Four unrelated crimes are solved by one consistent witness.','The audience receives one account that nobody disputes.','The final version is identified here as objectively proven true.','Four characters give conflicting but convincing accounts of one event.'],3,
 '这里描述 Rashomon 的什么叙事特点？',['四件无关案件由同一证人解决。','只有一个无人争议的版本。','本段指出最终版本已客观证实。','四个人对同一事件给出冲突却可信的叙述。'],
 ['A single event 而非四件案。','B completely different 与 contradict 表示多版本冲突。','C 片段没判定哪个客观为真。','D 四个角色、同一事件、相互推翻却同样有说服力都吻合。这是电影结构，不是四份现实证词的研究。'],
 ['the four main characters each provide completely different accounts of what happened.'],
 'accounts','叙述；说法','对同一事件的版本，不是银行账户','The witnesses gave different accounts of the meeting.',['conflicting accounts','an account of what happened'],
 '你看过哪些心理丰富电影？对我而言，Akira Kurosawa 的 1950 年电影 Rashomon 属于此类。影片围绕武士被杀这一事件，但四个主要角色各说出完全不同的经过。每人让观众相信自己的版本是真相，下一版本却又同样令人信服地反驳前一版本。')

add(16,'逻辑关系','How did the final event change the author’s response to Rashomon?',
 ['It confirmed that human goodness could never exist.','It made the film less memorable by removing all emotion.','It shifted a bleak view toward hope through an unexpected example of goodness.','It proved that human memory is always accurate.'],2,
 '最终事件怎样改变作者对 Rashomon 的反应？',['确认人不可能善良。','移除所有情绪，使电影不再难忘。','意外善举使灰暗看法转向希望。','证明人类记忆总准确。'],
 ['A human goodness emerges 与否定善相反。','B 作者仍说 deep, interesting, rich。','C depressing note 到 hopeful place 直接呈现转向。','D fallibility 指会出错，善举没有把记忆变成总准确。改变的是作者自己的观看回应，不保证每个观众一样。'],
 ['a final event epitomizing human goodness emerges out of nowhere.','the film made me believe that the world is a hopeful place instead.'],
 'fallibility','易错性；可能出错','描述人类记忆并非永远可靠','The discussion highlighted the fallibility of memory.',['human fallibility','the fallibility of memory'],
 '最后，正当影片似乎要以人性残酷和记忆易错的灰暗基调结束，一件体现人性善的事件突然出现。我当时把世界看成糟糕地方，影片却让我相信世界有希望。我觉得 Rashomon 深刻、有趣且心理丰富。')

add(17,'细节','Which memorable contrast in The Matrix is mentioned?',
 ['The choice between red and blue pills and confusion about reality and virtual reality.','A choice between two different books about Japan.','A demonstrated absence of any confusion about reality.','A comparison of the acting in Rashomon and Home Alone.'],0,
 '这里提到 The Matrix 哪个令人记得的对照？',['红蓝药丸的选择，以及现实与虚拟现实的混淆。','两本日本题材书的选择。','证明现实从不让人困惑。','比较 Rashomon 与 Home Alone 的演技。'],
 ['A 两项均列在 memorable in many ways 后。','B pills 不是书。','C confusion 与不存在混淆相反。','D 片段没有演技比较。Morpheus 的台词属于电影世界，不是现实世界的事实声明。'],
 ['the iconic choice between the red pill and blue pill; the confusion between reality and virtual reality.'],
 'iconic','标志性的；广为辨认的','指影片中典型的红蓝药丸选择场景','The scene became an iconic moment in the film.',['an iconic choice','an iconic scene'],
 '若你太年轻，没看过 Rashomon，就看看 The Matrix（1999）。它在很多方面令人难忘：标志性的红蓝药丸选择，现实与虚拟现实的混淆。Morpheus 说：“Matrix 无处不在，就在我们四周。（台词续下段）')

add(18,'语境词义','What does “blind you from the truth” suggest in the quoted dialogue?',
 ['A medical diagnosis of permanent physical blindness.','A deceptive world preventing someone from recognizing the truth.','A request to close the window before watching a film.','A scientific finding about every person in the real world.'],1,
 '引述台词中的 blind you from the truth 暗示什么？',['永久失明的医学诊断。','一个欺骗性世界使人看不到真相。','看电影前关窗的请求。','关于现实每个人的科学发现。'],
 ['A eyes 与 blind 在这里构成蒙蔽比喻，并非诊断。','B pulled over your eyes 与 from the truth 支持遮蔽认知。','C look out your window 是台词场景，不是操作要求。','D 电影台词不当成现实实验结果；末尾 What truth 是另一角色的提问。'],
 ['the world that has been pulled over your eyes to blind you from the truth.'],
 'blind','蒙蔽；使看不见','此处指认知上不知真相，不是实际眼疾','His confidence blinded him to the weakness in his plan.',['blind someone to the truth','be blinded by an assumption'],
 '“甚至此时此刻，在这间屋子里。望向窗外时你也能看见……它是蒙在你眼前、让你看不见真相的世界。”“什么真相？”')

add(19,'细节','How does Morpheus describe the prison in this fragment?',
 ['As a place Neo has already escaped by physical force.','As an ordinary room that can be explored with all the senses.','As a prison whose existence has been scientifically proved outside the film.','As something a person cannot taste, see or touch.'],3,
 'Morpheus 在当前片段中怎样描述监狱？',['Neo 已用武力逃出的地方。','可用所有感官探索的普通房间。','电影以外已科学证明存在的监狱。','人不能尝、看或触碰的东西。'],
 ['A 没有已逃出的行动。','B cannot taste or see or touch 正相反。','C 这是片中人物对 Neo 的说法。','D 三个感官否定直接支持。Into a prison 是既有台词的片段，保留原样，不擅自补成书外引语。'],
 ['a prison that you cannot taste or see or touch.'],
 'bondage','奴役；束缚','电影台词中的受控制状态，不是研究对真实读者的诊断','The novel explores freedom and bondage through its characters.',['be born into bondage','escape from bondage'],
 'Neo 问道。Morpheus 回答：“你是奴隶，Neo。像所有其他人一样，你生来就在束缚中，置身一座不能尝、不能看、不能触碰的监狱。（台词续下段）')

add(20,'有限推断','What does “Gradually” indicate about understanding the characters’ situation?',
 ['Understanding arrives fully before the story begins.','The characters’ situation never becomes clearer.','Recognition develops over time rather than all at once.','Only a physical prison can explain the story.'],2,
 'Gradually 表明对角色处境的理解怎样形成？',['故事开始前已完全了解。','处境永不会更清楚。','认识逐步发展，而非一次全部出现。','只有实体监狱能解释故事。'],
 ['A start to notice 与逐步形成不支持事前全知。','B 开始察觉表示更清楚，不是永远不知。','C Gradually 的时间过程义直接支持。','D prison for your mind 是台词比喻，不能限定实体监狱。本短段没有给出后续具体剧情，不补造解答。'],
 ['Gradually, you start to notice what is really happening to all the characters.'],
 'Gradually','逐渐地','观影理解随着叙事推进而形成','Gradually, the pattern became clear to the reader.',['gradually notice','gradually become aware'],
 '“一座禁锢你心智的监狱。”逐渐地，你开始察觉所有角色究竟经历着什么。',support='limited-inference')

add(21,'逻辑关系','How do the Kim children challenge the stereotype described?',
 ['They are portrayed as smart and stylish despite stereotypes of the poor as incompetent.','They are wealthy children whom the film portrays as incapable.','They prove that every poor person has the same abilities.','They never interact with the wealthy family.'],0,
 'Kim 家孩子怎样挑战所述刻板印象？',['贫者常被视为无能，他们却聪明、时髦。','他们是被说成无能的富家孩子。','证明所有贫者能力都相同。','从不接触富裕家庭。'],
 ['A Contrary to...poor...incompetent 与 smart, stylish, cunning 构成反差。','B the poor Kims，家庭身份错置。','C 两个虚构人物不证明所有穷人同质。','D Kim 全家为 Park 家工作，明确接触。cunning 还带机巧狡黠，不要把角色写成毫无道德复杂性。'],
 ['Contrary to stereotypes that cast the poor as hopeless and incompetent, the two Kim children are smart, stylish, and cunning.'],
 'cunning','机巧的；狡黠的','与聪明时髦并列，保留角色的谋略和道德复杂性','The character used a cunning plan to enter the household.',['a cunning plan','smart and cunning'],
 '如果没看过 The Matrix，那 Parasite（2019）呢？它讲贫穷的 Kim 家与富裕的 Park 家，两家各有一儿一女。不知怎的，Kim 家四人都为 Park 家工作，并发现富人生活。与把穷人视为无望、无能的刻板印象相反，Kim 家两个孩子聪明、时髦且狡黠。')

add(22,'细节','How do the claimed identities match the tutoring jobs?',
 ['Elite student for art tutoring; artist for English tutoring.','Artist for art tutoring; elite student for English tutoring.','Both claim to be artists to teach English.','Both truthfully report completed elite university degrees.'],1,
 '声称的身份与家教职位怎样对应？',['名校学生教艺术，艺术家教英语。','艺术家教艺术，名校学生教英语。','两人都称艺术家来教英语。','两人都如实报告已获名校学位。'],
 ['A 颠倒 respectively 的对应顺序。','B artist/elite college student 对 art tutor/English tutor 按顺序对应。','C 将两身份合为一个。','D lie 与 claim 表明编造，且 student 不是毕业学位。Park 家的 nice and naive 是影片描写，不推广为所有富人性格。'],
 ['an artist and elite college student in order to be hired as an art tutor and an English tutor, respectively.'],
 'respectively','分别；各自对应地','将两个身份按次序对应两种家教工作','Mia and Leo teach art and English, respectively.',['A and B, respectively','correspond respectively to'],
 '他们骗 Park 家，分别自称艺术家和名校学生，以应聘艺术家教和英语家教。另一方面，与把富人描绘成精明算计的刻板印象相反，Park 夫妇友善而天真。一幕里，Kim 先生说：“她很有钱，但仍然善良。”Kim 太太回答：“不是‘有钱但仍善良’。（台词续下段）')

add(23,'作者意图','What is the function of Ms. Kim’s explanation?',
 ['It establishes experimentally that wealth always causes kindness.','It says poverty makes kindness impossible for every person.','It rejects any link between circumstances and behavior.','It invites reconsideration of kindness in relation to economic circumstances.'],3,
 'Kim 太太的解释起什么作用？',['实验确立财富总能导致善良。','认定贫穷使每个人都不可能善良。','否认处境与行为的任何联系。','引导重新考虑善良与经济处境的关系。'],
 ['A 角色说 because 不等于实验因果证据。','B if I had...I’d... 是人物反事实，不是全体穷人的定律。','C 台词恰在把钱与行为关联起来。','D 后句 new way of thinking 指向对机会、公平和道德的重想；不自动代表作者认可台词为普遍真理。'],
 ['The film gives us a new way of thinking about the rich and the poor, abilities and opportunities, fairness and morality.'],
 'morality','道德；行为的善恶评价','与能力、机会、公平并列，是影片引发思考的主题','The discussion considered morality as well as opportunity.',['fairness and morality','questions of morality'],
 '“她善良是因为她有钱。要是我有这么多钱，我也会善良！”影片让我们以新方式思考富人与穷人、能力与机会、公平与道德。')

add(24,'细节','How does Kant characterize pleasant arts in the quoted passage?',
 ['As directed merely toward enjoyment and making time pass unnoticed.','As necessarily changing every person’s moral beliefs.','As devoid of any capacity to please people together.','As a scientific test of the psychological effects of games.'],0,
 'Kant 的引语怎样界定 pleasant arts？',['仅以享受、让时间不知不觉流逝为方向。','必定改变每个人的道德信念。','完全不能使聚在一起的人愉悦。','检验游戏心理效果的科学实验。'],
 ['A merely to enjoyment 与 time pass imperceptibly 直接支持。','B no further interest 不能加上必定改变信念。','C gratify a company at table 指让同桌人愉悦。','D 这是哲学分类引述，不是实验。仅在此分类中解释 pleasant，不推成所有游戏绝无其他价值。'],
 ['those that are directed merely to enjoyment.','making the time pass imperceptibly.'],
 'imperceptibly','不知不觉地；难以察觉地','形容愉快消遣中时间流逝未被注意','The afternoon passed imperceptibly as they talked.',['pass imperceptibly','time passes imperceptibly'],
 '在 Critique of Judgment 中，Immanuel Kant 区分美的艺术与悦人的艺术。他把悦人的艺术描述为“仅仅指向享受的艺术。其中包括所有能让同桌人愉悦的迷人艺术……也包括那些除了让时间不知不觉流逝之外、没有更进一步旨趣的游戏”。')

add(25,'主旨','What distinguishes reflective judgment from mere sensation here?',
 ['It excludes any mental representation of an object.','It is simply the same as passing time pleasantly.','It involves a gap between sensation and reality and a new mental understanding.','It guarantees that all viewers perceive an object identically.'],2,
 '这里的反思判断与单纯感觉有什么区别？',['排除对对象的任何心理表征。','仅等同于愉快打发时间。','涉及感觉与现实的差距，以及新的心理理解。','保证所有观众理解完全一致。'],
 ['A a new mental representation 明确保留表征。','B greater than...mere sensation 表示不止消遣。','C gap...new mental representation and understanding 是末尾解释。','D 没有人人一致的保证。purposive 与 devoid of definite purpose 并列是哲学限定，不擅自删括号或改成无任何意义。'],
 ['“reflective judgment,” which involves some gap between sensation and reality and a new mental representation and understanding of an object.'],
 'reflective judgment','反思判断','在本书对 Kant 的阐释中，指不止感官愉悦、会重新理解对象的判断','The artwork encouraged reflective judgment rather than a quick reaction.',['reflective judgment','the exercise of reflective judgment'],
 '相比之下，“美的艺术是一种以自身为合目的性的表象方式，虽然没有［明确］目的，却能促进与社会沟通相关的心智能力的培养”。这里，Kant 把审美体验界定为超越单纯感觉享受、转而享受所谓“反思判断”的东西；后者涉及感觉与现实之间的某种差距，以及对对象新的心理表征和理解。')

assert len(out)==25 and [q['id'] for q in out]==[t['questionId'] for t in targets]

def persist():
 path=ROOT/'source/short-questions/additional.json';existing=load('source/short-questions/additional.json');byid={q['id']:q for q in existing}
 for q in out:
  if q['id'] in byid:assert byid[q['id']]==q,('Refuse to overwrite changed authoring',q['id'])
  else:existing.append(q)
 path.write_text(json.dumps(existing,ensure_ascii=False,indent=2)+'\n',encoding='utf8',newline='\n')
 review=dict(batchId='batch-023',date='2026-10-22',pdfSha256=b['pdfSha256'],checkedPdfPages=list(range(90,94)),questionIds=[q['id'] for q in out],paragraphs=[dict(id=pid,textSha256=hashlib.sha256(pp[pid]['text'].encode()).hexdigest()) for pid in dict.fromkeys(q['paragraphId'] for q in out)],note='完整PDF90–93原页视觉核对；小说角色、电影台词不当作事实或作者赞同；日本历史反思为作者的道德设问，不将可能性改为开脱罪行。记忆与复杂性为本书论述，Home Alone/Rashomon为个人评价，Kant为哲学引述。保留引用片段既有边界、引号与省略号，不重复原句。')
 (ROOT/'source/short-questions/review-chapter09-aesthetics25.json').write_text(json.dumps(review,ensure_ascii=False,indent=2)+'\n',encoding='utf8',newline='\n')
 print('Saved',len(out),'of 25 individually authored exercises')

if __name__=='__main__':persist()
