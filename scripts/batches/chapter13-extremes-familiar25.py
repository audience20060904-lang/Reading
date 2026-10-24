"""25 individually authored exercises for frozen targets, PDF pages 147-151.
Preserve printed English, source positions and all previously published questions.
"""
from pathlib import Path
import json,hashlib
ROOT=Path(__file__).resolve().parents[2]
load=lambda p:json.loads((ROOT/p).read_text(encoding='utf8'))
b=load('public/data/book.json');plan=load('public/data/reading-plan.json');targets=load('source/short-questions/batch037-targets.json')['targets']
ss={s['id']:s for s in b['sentences']};pp={p['id']:p for p in b['paragraphs']};out=[]
def add(i,kind,prompt,options,answer,prompt_zh,options_zh,analyses,quotes,word,meaning,context,example,collocations,translation,support='explicit'):
 t=targets[i-1];u=next(u for u in plan['units'] if u['id']==t['readingUnitId']);group=[ss[sid] for sid in u['sentenceIds']];p=pp[u['paragraphId']];text=p['text'][group[0]['start']:group[-1]['end']]
 assert hashlib.sha256(text.encode()).hexdigest()==t['passageSha256'];evidence=[]
 for quote in quotes:
  offset=text.find(quote);assert offset>=0,(i,quote);start=group[0]['start']+offset;end=start+len(quote);touching=[s for s in group if s['start']<end and s['end']>start]
  evidence.append(dict(quote=quote,sentenceIds=[s['id'] for s in touching],sources=list({(r['pdfPage'],r['block']):r for s in touching for r in s['sources']}.values())))
 assert word.lower() in text.lower(),(i,word)
 out.append(dict(id=t['questionId'],version=1,readingUnitId=u['id'],chapterId=u['chapterId'],sectionId=u['sectionId'],paragraphId=u['paragraphId'],sentenceIds=u['sentenceIds'],passage=text,prompt=prompt,options=options,answer=answer,type=kind,promptZh=prompt_zh,optionsZh=options_zh,analyses=analyses,evidence=evidence,vocabulary=[dict(word=word,meaning=meaning,context=context,example=example,collocations=collocations)],translation=translation,support=support,editorialStatus='完整PDF147–151原页视觉核对。D.J.来信续句与不同人过量阈值按原文，不设统一次数。Taylor Mac连续24小时现场非录音/24场；Morris/Needham为评论个人体验，非控制实验。舞台扮演偏见不等于认同偏见；imaginary bus非真实出行自传，seismic/roof为修辞，7am还有5小时。q-c13-032承接闭引号原字保留。作者肯定丰富又犹豫，健康风险might及occasionally、might consider不扩为人人持续冒险；Polley是作品例子非疗效试验或文档行动指令。A/B哲学人物立场分清、presumably保留。妻子1991相识/1999结婚/约2010挂画，作者must be happy为观察推测非诊断；此前焦虑与画作欢快可以并存。boy是感叹，most非全部；B内在感恩为归属明确的哲学宗教主张，不提前援引下一段实验当本段证据。原有额外正文审计待办仍开放，候选池无漏ID不等于全书正文无遗漏。'))







add(1,'逻辑关系','What contrast does the speaker draw between himself and his Colorado friend?',
 ['Both would have found staying in one place intolerable.','The friend wanted to move, whereas the speaker refused.','Both had already tried and rejected the same lifestyle.','Staying would have distressed the speaker, while moving would have been unthinkable for his friend.'],3,
 '说话者怎样对比自己与科罗拉多朋友？',['两人都无法忍受留在同地。','朋友想搬，说话者拒绝。','两人都已试过并拒绝同一生活方式。','说话者难忍留守，朋友则无法想象搬迁。'],
 ['A for him...moving不是朋友也讨厌留守。','B 把两个人的取向对换。','C would have been是反事实判断，非说双方都做过同一试验。','D for me/for him及staying/moving形成对应对照；torture是来信者强调难受的比喻，不是这里发生了实际酷刑。'],
 ['For me staying in one place would have been torture, for him [his Colorado friend] moving would be unthinkable.'],
 'unthinkable','难以想象的；不可考虑的','表示朋友对搬迁生活的强烈不愿，非逻辑上无法发生','For her, leaving the village was unthinkable.',['would be unthinkable','stay in one place'],
 '“对我来说，一直待在同个地方会是折磨；对他〔我那位科罗拉多朋友〕来说，搬家则无法想象。”（承接上一单元的来信引文。）')

add(2,'主旨','What conclusion follows from the contrasting reactions to repeated moves?',
 ['A single numerical limit determines how much richness is acceptable for everyone.','Whether richness is excessive depends partly on the person and the context.','The number of moves is irrelevant to every person’s experience.','The five distressed readers had all moved more often than D.J.'],1,
 '反复搬迁引起不同反应，由此得出什么结论？',['所有人有同一个可接受次数上限。','丰富是否过量，部分取决于个人和情境。','搬迁次数与每个人的经历都毫无关系。','五位困扰读者全比D.J.搬得多。'],
 ['A personality/family/context反对统一阈值。','B 末句明确个性、家庭及其他情境的重要作用。','C 不能从非统一阈值推成次数对所有人全无关。','D 八至十三次与D.J.前述更多次不相符。比较的是不同来信反应，不是随机试验得出每个人的安全搬迁次数。'],
 ['one’s personality, family situation, and many other contextual factors clearly play an important role.'],
 'contextual factors','情境因素','家庭背景等条件会改变同类经历对人的意义','The researchers considered several contextual factors.',['contextual factors','in contrast'],
 '以D.J.经历的那么多次搬迁而言，对他来说并不存在搬得太多或丰富过量的问题。相反，对Mary、Liz、Gus、Peggy和Jim来说，八到十三次就确实太多了。问丰富能否过量时，一个人的人格、家庭处境及许多其他情境因素，显然十分重要。')

add(3,'细节','What made Taylor Mac’s performance unusual in the account?',
 ['It was a live performance lasting continuously from Saturday noon to Sunday noon.','It was a recording that could be played at any time.','It consisted of twenty-four short concerts on separate weekends.','It began at midnight and ended at noon on the same day.'],0,
 '叙述中Taylor Mac演出有何特别？',['现场连续演出，从周六中午到周日中午。','任何时间都可播放的录音。','分开多个周末的24场短演出。','午夜开始，当日中午结束。'],
 ['A live、twenty-four hours straight及两个noon给出形式、持续性和时段。','B 作者先明确not a recorded concert。','C twenty-four是连续小时，不是场次。','D 两个noon相隔一天，不是午夜到同日中午。题名24-Decade也不等于演了24年。'],
 ['singing and dancing for twenty-four hours straight, from noon on Saturday to noon on Sunday.'],
 'straight','连续地；不间断地','此处修饰24小时唱跳的持续时间，非直线方向','The musicians played for three hours straight.',['hours straight','a live concert'],
 '说到极端，你听说过24小时音乐会吗？不是那种可随时收听的录制音乐会，而是24小时现场演出！Taylor Mac于2016年在布鲁克林St. Ann’s Warehouse表演《A 24-Decade History of Popular Music》，从周六中午到周日中午，连续唱跳24小时。')

add(4,'作者意图','What does Morris emphasize beyond the physical feat?',
 ['The audience’s ability to recall every lyric.','The superior comfort of the venue’s seating.','Mac’s expressive versatility across lyrics, styles, tempos, and vocal registers.','The claim that the show succeeded mainly because it was prerecorded.'],2,
 'Morris除体能壮举外还强调什么？',['观众记住全部歌词的能力。','场地座椅格外舒适。','Mac在歌词、风格、速度、音域上的多样表现。','演出主要因预录而成功。'],
 ['A remembered的主体是Mac，不是观众。','B 本段没有座椅赞美，不能添加场地结论。','C wasn’t simply之后列出记词及丰富表达，protean点出多变。','D sang/performance没有预录成功说法。此处是评论家赞誉，非实验测得的普遍心理效应。'],
 ['It wasn’t simply the physical feat','he sang them—in every imaginable style, at every tempo, with every possible facial expression and every register of his handsome, protean voice.'],
 'protean','多变的；变化多端的','赞美歌声能呈现多样风格音域，不是固定单一音色','The actor’s protean voice suited many different roles.',['a protean voice','a physical feat'],
 '评论家Wesley Morris在《New York Times》赞扬演出：“Mac先生给了我人生中最伟大的经历之一……不只是体能壮举……他记住了所有歌词……用一切可想象的风格、各种速度、各种表情，以及他那优美多变嗓音的各个音域，把它们唱出来。”')

add(5,'逻辑关系','What contrast structures this passage?',
 ['All ticket buyers rejected the show, while Morris stayed home.','The author attended eagerly, whereas Morris found it pointless.','The author’s initial skepticism is set against Morris’s transformative response.','A scientific finding is contrasted with a different controlled experiment.'],2,
 '本段由什么对照组织？',['所有购票者拒演出，Morris留在家。','作者热切参加，Morris觉得无意义。','作者起初怀疑，与Morris受到转变的反应对照。','一项科学发现对照另一控制实验。'],
 ['A 850人付费在场，非全拒绝，没说Morris未去。','B ridiculous是作者初印象，transformational则属Morris，人物评价错配。','C first impression/ridiculous与uniquely transformational明确对照。','D 评论引述不等于控制实验。末尾Yankee Doodle解读归属Morris所述演出，不擅自写成作者独立证实的歌曲历史。'],
 ['My first impression was that this was a ridiculous idea.','And this was a uniquely transformational experience for Morris:'],
 'deprive themselves of','使自己缺少；剥夺自己的','自愿少睡的反问，体现作者对长时参与的怀疑','They would not willingly deprive themselves of rest.',['deprive oneself of sleep','a transformational experience'],
 '我最初觉得这是荒谬主意。谁会自愿不睡觉，还在不舒服的椅子上坐一整天？得知竟有850人付钱到场，我很惊讶。可对Morris，这是一种独特的转变经历：“开场不久，他有力地论述了《Yankee Doodle》中英国的恐同意味，并让你觉得，它成为美国常见曲目的地位，是美国重新挪用文化的早期例子。')

add(6,'作者意图','What is the stated purpose of the audience’s disturbing role-play?',
 ['To make participants feel hatred in order to engage with unfamiliar emotions.','To endorse racism and homophobia as the author’s preferred values.','To establish that every audience member held those views outside the performance.','To replace the concert with an actual historical war.'],0,
 '观众令人不适的角色扮演，所述目的是什么？',['让参与者感受仇恨，以接触陌生情绪。','认可种族主义和恐同是作者偏好价值。','确立每位观众在场外都持这些观点。','把音乐会换成实际历史战争。'],
 ['A to feel what hate actually feels like明确目的；后文love/empathy说明所述情绪体验。','B act like是演出参与情境，不等于赞同被扮演的偏见。','C 角色行为不是对每位观众日常信念的诊断。','D war scene是场景演绎，不是真战。首句对歌曲看法变化是Morris的引述，不能变为全体人同一反应。'],
 ['act like racists and homophobes to feel what hate actually feels like.'],
 'empathy','共情；理解他人感受的能力','与爱及羞耻消解并列，是叙述中的情绪反应','The story encouraged empathy for people with different experiences.',['feel empathy','actively participate'],
 '“总之，我以后再听这首歌，感受再也不会一样了。”观众被邀请主动参与战争等场景，扮演种族主义者和恐同者，以体会仇恨实际是什么感觉。他们感受到爱、共情，以及Morris所说的“羞耻被撕碎”。')

add(7,'细节','What change does Needham describe in response to Mac’s version of the song?',
 ['A song he had always strongly disliked became technically easier to sing.','A song that had not moved him much suddenly brought him to tears.','He stopped responding emotionally to all performances.','He remembered riding a real bus to the 1963 march himself.'],1,
 'Needham描述Mac的歌曲版本引起什么变化？',['一首一直厌恶的歌变得技术上易唱。','此前没强烈感受的歌突然令他落泪。','他从此对所有表演无情绪。','他记起自己亲乘真实巴士参加1963游行。'],
 ['A never had strong feelings不等于强烈厌恶，也没评价演唱难度。','B never...strong feelings与brings sudden tears形成反差。','C 眼泪说明被触动，非情绪消失。','D imaginary bus是演出想象情境，不能当评论家真实乘车回忆。这是个人艺术体验自述。'],
 ['I’ve never had strong feelings about ‘You Keep Me Hangin’ On’','brings sudden tears to my eyes'],
 'imaginary','想象中的；虚构的','表演所设想的巴士情境，不是实际交通记录','The performance followed an imaginary journey through the city.',['an imaginary bus','bring tears to one’s eyes'],
 'Morris并非唯一如此的人。同日，艺术编辑Alex Needham在《Guardian》写道：“熬这么久，会让人的心境出现奇特变化。我对Supremes的《You Keep Me Hangin’ On》从没有强烈感受，可Mac这个版本，由一辆想象中的巴士上、前往支持1963年华盛顿民权游行的同性恋者唱出，突然使我热泪盈眶……')

add(8,'语境词义','How should “all but tears the roof off” be understood?',
 ['As a building inspection reporting a collapsed roof.','As evidence that the drums caused a measured earthquake.','As a statement that the concert ended immediately at 7am.','As a vivid exaggeration of the performance’s power and audience excitement.'],3,
 '应怎样理解all but tears the roof off？',['建筑检查报告屋顶塌了。','鼓声造成测得地震的证据。','演出早7点立即结束。','夸张形容演出力量与观众激动。'],
 ['A roof意象不是结构损坏报告。','B seismic也是震撼感修辞，非地震测量。','C We still have five hours说明尚未结束。','D sound/spectacle/roars构成强烈氛围，撕屋顶是评论中的夸张表达。about five minutes也保留评论者主观估计。'],
 ['This combination of sound, spectacle and a spirit of joyful activism against injustice is so powerful it all but tears the roof off'],
 'spectacle','壮观场面；令人注目的景象','与声音和抗争精神并列，描述舞台体验','The parade was a colorful spectacle.',['sound and spectacle','a spirit of activism'],
 '“早上7点，Brooklyn United Marching Band——一队戴粉红帽的黑人男孩——列队上台，猛烈击鼓，为Curtis Mayfield赞颂非裔美国人自豪与自主的《Move on Up》奏出震撼结尾……声音、场面与以欢乐抗争不公的精神结合，强大得几乎掀翻屋顶。观众似乎欢呼了约五分钟，Mac笑说：‘我们还有五小时。’')

add(9,'同义改写','Which statement best preserves the author’s summary?',
 ['Unusual participation and unfamiliar feelings led concertgoers to see things differently.','Every concertgoer was clinically tested and found permanently transformed.','Only observing familiar routines caused no change in anyone’s perspective.','The concert changed the historical events portrayed on stage.'],0,
 '哪项最保留作者总结？',['不寻常参与和陌生感受使观众换了视角。','逐个临床测试证实每人永久转变。','只观察熟悉日常，没有人视角变化。','音乐会改变了舞台所述历史事件本身。'],
 ['A did unusual things/felt unfamiliar emotions/changes in perspective逐项对应。','B 段中未报告临床测量、每人或永久性。','C 把unusual、unfamiliar及changes全部反写。','D 变化的是人的视角，不是过去事实。原单元首有承接引文的闭引号，保留而不擅删英文。'],
 ['Concertgoers at Taylor Mac’s concert did unusual things and felt unfamiliar emotions, which resulted in changes in perspective.'],
 'perspective','视角；看问题的方式','人对事物的理解角度变化，不是历史事件本身被改变','The discussion changed her perspective on the experience.',['changes in perspective','unfamiliar emotions'],
 '”在Taylor Mac的音乐会上，观众做了不寻常的事，感受陌生情绪，由此改变了看问题的视角。（开头闭引号承接上一单元的评论引文。）')

add(10,'逻辑关系','What tension does the author express about the concert?',
 ['He denies that it was rich because he personally dislikes all music.','He promises to attend every future performance of the same length.','He recognizes its richness while remaining hesitant to commit an entire night.','He believes ordinary concerts are too short to produce any value.'],2,
 '作者对音乐会表达什么张力？',['因自己讨厌所有音乐而否认丰富。','保证参加今后每场同样长的演出。','承认丰富，却仍犹豫是否投入整夜。','认为普通音乐会太短，毫无价值。'],
 ['A prime example明确承认丰富，未说厌恶所有音乐。','B hesitate与保证参加相反。','C all for...but even I刻画价值认同和参与意愿的区别。','D good reasons for a few hours肯定常规时长合理性，非全无价值。'],
 ['I am all for psychological richness, but even I would still hesitate to sign up for this concert.'],
 'sign up for','报名参加；登记加入','把认可一种体验与亲自承诺参加区分开','She hesitated to sign up for the overnight event.',['sign up for a concert','hesitate to'],
 '这是心理丰富经历的绝佳例子。但谁愿意为此熬一整夜？我完全赞成心理丰富，可连我也仍会犹豫是否报名参加这场音乐会。一般音乐会只持续几个小时，是有充分理由的。')

add(11,'推断','What does the contrast between the reviewers and others suggest?',
 ['The same length of experience is equally beneficial for all audiences.','An intensely rich experience may suit some people while exceeding others’ limits.','The reviewers’ responses prove that no health cost is possible.','People who avoid this concert cannot lead rich lives.'],1,
 '评论家与其他人的对照提示什么？',['相同时长对所有观众同等有益。','高度丰富的体验可能适合某些人，却超过他人限度。','评论家反应证明不可能有健康代价。','不去音乐会就不可能人生丰富。'],
 ['A For others...might be too much直接否定统一适宜。','B for people like与For others对照，might保留可能性。','C even dangerous to their health保留不利可能，非无成本证明。','D 段中没有把单次极端演出当丰富人生的必要条件。它也没给量化健康试验结果。'],
 ['For others, however, this might be too much, even dangerous to their health.'],
 'supersized','超大份的；规模特大的','借用份量比喻强度很大的丰富体验，不等于人人最优','The festival offered a supersized version of the usual show.',['a supersized experience','too much for someone'],
 '再次说，对Wesley Morris和Alex Needham这样的人，这是一份超大号的丰富体验。但对其他人，它可能过量，甚至危及健康。',support='limited-inference')

add(12,'主旨','What balance does the author advocate in this passage?',
 ['Recognize the protective instinct but occasionally move beyond one’s comfort zone.','Avoid every unfamiliar experience regardless of its risks.','Reject the survival value of caution altogether.','Replace occasional challenges with constant exposure to danger.'],0,
 '本段作者主张什么平衡？',['承认保护本能，同时偶尔走出舒适区。','不论风险如何，避免每种陌生经历。','全盘否定谨慎对生存的价值。','用持续置身危险代替偶尔挑战。'],
 ['A helps us survive承认回避的保护作用，every once in a while限定为偶尔挑战。','B too much running away批评过度回避。','C 原文明确本能有助生存。','D occasionally的限定不能强化为持续冒险；这是作者论述，不把它改成本站要求执行的危险行为。'],
 ['We have an instinct to run away from risks, which helps us survive.','We need to push ourselves beyond our comfort zones every once in a while.'],
 'timid','胆怯的；畏缩的','指作者担忧过度回避带来的生活态度，非临床诊断','He felt too timid to try the unfamiliar activity.',['beyond our comfort zones','every once in a while'],
 '不过，归根结底，不尝试就难知道什么对自己过量。我们有逃离风险的本能，它帮助我们生存。但逃避过度，会让我们胆怯得无法真正生活。我们需要偶尔推动自己走出舒适区。')

add(13,'作者意图','How is Polley’s book used in the argument?',
 ['As a controlled study proving that danger benefits everyone.','As a report that the author had personally faced Polley’s exact tragedies.','As a command contained in the document that readers must obey literally.','As an example leading into a tentative invitation to face challenges.'],3,
 'Polley的书在论证中怎样被使用？',['证明危险人人受益的控制研究。','说作者亲历Polley完全相同的悲剧。','文档中必须逐字服从的命令。','作为例子，引出考虑面对挑战的邀请式建议。'],
 ['A 描述经历的书不是对所有人的受控实验。','B she experienced属于Polley，不是Oishi亲历同样事件。','C 阅读材料中的建议是待理解的作者观点，不是必须执行的命令。','D might consider保留建议与考虑，书名引向挑战主题；不扩写成无条件拥抱任何现实危险的保证。'],
 ['Sarah Polley published a book entitled Run Towards the Danger, describing a series of tragedies and dangerous situations she experienced.','you might consider challenging yourself'],
 'entitled','题为；名叫','引出作品名称，不是有权获得某物的意思','She published a memoir entitled A Different Journey.',['a book entitled','consider challenging yourself'],
 '电影导演兼作家Sarah Polley出版了《Run Towards the Danger》，描述她经历的一系列悲剧和危险处境。下次遇到危险时，你也许可以考虑挑战自己，朝它迎去。（此处呈现原书作者的建议措辞，非网站的行动指令。）')

add(14,'细节','Which contrast in Either/Or is described here?',
 ['Author A promotes commitment, while B promotes only novelty.','Author A promotes beauty and adventure, while B promotes commitment.','Both authors reject planning as well as spontaneity.','The two figures are presented as identical in age and occupation.'],1,
 '这里描述《Either/Or》的哪种对照？',['A倡导承诺，B只倡导新奇。','A倡导美与冒险，B倡导承诺。','两人都反对计划和自发。','两人年龄职业完全相同。'],
 ['A 把A/B主张倒置。','B aesthetic...beauty and adventure与life of commitment分别归属A/B。','C 列conflicts不是说双方都否定所有成分。','D presumably young/retired judge是不同人物设定且带推定语气。哲学角色主张不能当现代实验结论。'],
 ['“A” promotes an aesthetic life, or a life of beauty and adventure, whereas “B” promotes a life of commitment.'],
 'juxtaposes','并置；并列对照','把两人物及其人生观放在一起形成对比','The essay juxtaposes two approaches to a good life.',['juxtapose A with B','a life of commitment'],
 '剩下的问题是，能否不只从陌生，也从熟悉中找到丰富。Søren Kierkegaard于1843年写的《Either/Or》，讨论稳定与不稳定、无聊与刺激、长期与短期、理性与激情、计划与自发的冲突。如前所述，它把作者A（推测是一名青年）与作者B（推测是那位退休法官）并置。“A”倡导审美的人生，亦即美与冒险的人生；“B”倡导承诺的人生。')

add(15,'主旨','What possibility is opened by the final question?',
 ['Novelty can be obtained only by continuously replacing relationships.','The author has proved that learning stops in familiar settings.','Deep attention to one familiar person or object might also bring richness.','Author B’s perspective has already been rejected as entirely worthless.'],2,
 '最后的提问开启什么可能？',['新奇只能靠不断更换关系获得。','作者已证明熟悉环境里学习停止。','深入关注熟悉的人或物，也可能带来丰富。','B的视角已被全盘否定。'],
 ['A only path正被质疑，不能作肯定结论。','B 此处询问另一可能途径，非宣布学习停止。','C digging deep into one person or object对应深化熟悉对象；问题语气还不是实验验证。','D Is it also possible邀读者考虑B，并非先否定其全部价值。'],
 ['Is it also possible to gain psychological richness from B’s perspective, by digging deep into one person or object?'],
 'going with the flow','顺势而行；随兴应变','此处列为A式新奇、自发取向的一部分','On holiday she preferred going with the flow to following a strict plan.',['go with the flow','dig deep into'],
 '到目前为止，我一直主张接纳A的优先选择：新奇、激情、自发、顺势而行。的确，不断尝试新事物，会让人持续学习成长。但那是通向心理丰富的唯一路径吗？能否也从B的视角出发，通过深入了解一个人或一件事物，获得心理丰富呢？')

add(16,'推断','What does the account of meeting and marrying his wife illustrate?',
 ['Spending years together need not exhaust what there is to discover about a person.','Marriage erased every memory of the years before 1999.','The author met his wife for the first time after their wedding.','Knowing someone longer inevitably prevents any new discovery.'],0,
 '相识与结婚的叙述说明什么？',['多年相处也未必穷尽对一个人的发现。','婚姻抹掉了1999年前所有记忆。','作者婚后才初次见妻子。','认识久了必然不能有新发现。'],
 ['A before marriage...Even so...until after说明虽相处多仍能后来知道新面向。','B 没有记忆被抹去的情节。','C met1991、married1999，清楚相识在前。','D 与many things...didn’t know直到婚后相反。单个个人例子支持有限可能，不代表所有婚姻必有同样结果。'],
 ['I spent a lot of time with her before marriage. Even so, there were many things that I didn’t know about her until after we were married.'],
 'Even so','即便如此；尽管如此','承接婚前相处很多，转出仍有未知面向','They had talked for years. Even so, there was more to learn.',['even so','a familiar person'],
 '人生中有些最丰富的体验，是在熟悉的人、物或地方发现新东西。我于1991年遇见妻子，1999年结婚。婚前已与她相处很久。即便如此，仍有许多事直到结婚后我才知道。',support='limited-inference')

add(17,'细节','What prompted the question “What should I buy?”?',
 ['The decision to sell all the paintings already covering the house.','A request to buy a house immediately after meeting his wife.','A wish, around 2010, to put paintings on the living room wall.','A plan to begin a formal art collection in 1991.'],2,
 '“我该买什么？”由什么情境引起？',['决定卖掉已挂满房屋的画。','初识妻子后立刻买房的请求。','约2010年想在客厅墙上挂画。','1991年开始正式艺术收藏的计划。'],
 ['A walls empty说明此前多空着，未说卖满屋画。','B buy宾语在挂画语境，非买房，也非初识当下。','C wanted to hang...living room及around2010直接支持。','D nearly twenty years after first met不是1991立刻收藏，且无正式收藏计划。'],
 ['I finally wanted to hang some paintings on the living room wall. This was around 2010'],
 'nearly','将近；差不多','nearly twenty years为约略时长，不等于精确满二十年','They had known each other for nearly twenty years.',['nearly twenty years','hang paintings'],
 '比如，多年来家中大多数墙一直空着，后来我终于想在客厅墙上挂几幅画。那大约是2010年，距初次遇见她已将近20年。“我该买什么？”我问。')

add(18,'语境词义','What does “And boy could she paint” convey?',
 ['A boy, rather than his wife, made the paintings.','The author was impressed by his wife’s painting ability.','The author doubted that his wife had any ability to paint.','The wife could paint only when she was a child.'],1,
 'And boy could she paint表达什么？',['画是一个男孩而非妻子画的。','作者惊叹妻子的绘画能力。','作者怀疑妻子完全不会画。','妻子仅童年能画。'],
 ['A boy是感叹用语，不是新人物。','B 这里倒装加强惊叹，前面的What/I did not know显示意外发现。','C could she paint的肯定感叹不是否定。','D could在此描述能力，并无only childhood限制。不能把感叹式错当普通疑问句。'],
 ['And boy could she paint.'],
 'boy','哇；哎呀〔感叹用语〕','此处表强烈惊讶与赞赏，不指男孩','Boy, that performance was impressive!',['boy, could she paint','an exclamation of surprise'],
 '妻子回答：“我会画。”“什么？”我不知道她会画。哇，她画得可真好。')

add(19,'细节','What has happened to most of the walls?',
 ['They remain completely empty.','They display only paintings bought from a gallery.','They have been removed to make space for a studio.','They are decorated with the wife’s numerous paintings.'],3,
 '大多数墙如今怎样了？',['仍完全空着。','只陈列画廊购画。','被拆掉给画室腾地方。','装饰着妻子创作的许多画。'],
 ['A now graced by与空白相反。','B her paintings由She has painted连接，非只购入的作品。','C 文中未拆墙。','D so much that说明创作多，结果多数墙有她的画；most不能扩大为每一面墙。'],
 ['most of our walls are now graced by her paintings.'],
 'graced by','因……而增色；由……装点','画作为墙面增添美感，非授予正式称号','The hallway was graced by family photographs.',['be graced by paintings','most of our walls'],
 '她画了那么多画，如今家里大多数墙都由她的作品装点。')

add(20,'细节','Which example supports the description of her as meticulous?',
 ['She sometimes spends over half an hour composing a simple email reply.','She always finishes every task in less than a minute.','She never worries about things going wrong.','She writes complex letters only for professional artists.'],0,
 '哪个例子支持她做事细致的描述？',['有时回一封简单邮件就花超过半小时。','每项任务总在一分钟内完成。','从不担心出错。','只给专业艺术家写复杂信件。'],
 ['A more than thirty minutes/simple reply具体化methodically and slowly。','B slowly与总极快相反。','C worries about many things直接否定从不担心。','D 没有限定收信职业，simple不是complex。sometimes不等于每封邮件都固定耗时。'],
 ['She sometimes spends more than thirty minutes writing a simple reply to an email.'],
 'meticulous','一丝不苟的；极细致的','作者以做事有条理而慢、回复邮件耗时为例说明，不作临床诊断','She was meticulous when checking the details.',['a meticulous person','very methodically'],
 '妻子是个友善但很容易焦虑的人。她担忧生活中许多可能出问题的事。她也非常细致，做任何事都有条不紊、慢慢来。有时，回复一封简单邮件，她会花超过30分钟。')

add(21,'逻辑关系','How did her actual paintings differ from the author’s expectations?',
 ['He expected bright, quick work but saw dark paintings produced slowly.','He expected dark, slow work but saw cheerful colors created quickly.','He expected no art but found that every painting copied the same pear exactly.','His expectations were fully confirmed in both mood and speed.'],1,
 '实际作品与作者预期有什么差别？',['本以为明亮且快，实见暗沉且慢。','本以为暗沉且慢，实见欢快色彩且画得快。','以为无艺术，却见每画精确复制同个梨。','情绪基调和速度都完全符合预期。'],
 ['A 把预期与实际全反过来。','B expected...dark/take a while与pink/sky blue/pastel/quickly对应对照。','C pears例子不等于所有画都同一个梨，且作者确实有预期作品。','D surprised与完全符合相反。Mondrian-style说明风格，不等于画是Mondrian本人所作。'],
 ['I expected her paintings to be rather dark and to take a while to finish.','all very, very quickly. Her paintings were so happy.'],
 'pastel colors','柔和的浅色；粉彩色调','描写作品浅淡柔和的配色，与作者预期暗色形成对照','She chose pastel colors for the new design.',['in pastel colors','Mondrian-style canvases'],
 '她就是那样的人。所以我以为她的画会相当暗沉，画完也要很久。可她把梨画成粉红和天蓝，还以粉彩色调创作Mondrian风格画布，而且全都非常、非常快，令我意外。她的画那么欢快。')

add(22,'推断','Which claim is most carefully supported by this passage?',
 ['A scientific test proved that she never experiences anxiety.','Twenty years together guarantees complete knowledge of a partner.','The author deliberately arranged an experiment to diagnose her personality.','The painting episode led him to discover a new aspect of his long-known partner.'],3,
 '哪项是本段最谨慎支持的说法？',['科学测试证实她从不焦虑。','相处20年保证完全了解伴侣。','作者故意安排实验诊断人格。','绘画事件让他发现熟悉伴侣的新面向。'],
 ['A must be a very happy person是作者据观察所作推测，不是科学检测，也没取消先前焦虑描述。','B 叙述恰显示多年后仍有新发现。','C if I had never wanted是反事实回想，不是受控诊断安排。','D 末两句直接连接挂画需求、发现人格面向和双方的丰富体验，保留个案范围。'],
 ['I might have never discovered this aspect of my wife’s personality.','Learning something new about my wife, two decades into our relationship, was enriching for both of us.'],
 'decisively','果断地；坚定利落地','描述她画画时的行动方式，与平时慢而细致的印象形成反差','She acted decisively once she had chosen a direction.',['paint decisively','deep down'],
 '她创作时如此果断。在内心深处，她想必是个很快乐的人。然而，若我从没想为客厅墙找一幅画，也许就永远不会发现妻子人格的这一面。在相处20年后，仍能了解妻子新的一面，对我们两人都是丰富的体验。',support='limited-inference')

add(23,'主旨','What does the sentence emphasize?',
 ['Long acquaintance guarantees knowledge of everything about a person.','New acquaintances are incapable of teaching us anything.','Some understanding becomes possible only through knowing someone over time.','The author recommends ending relationships once they become familiar.'],2,
 '本句强调什么？',['认识久保证了解一个人的一切。','新朋友什么也不能让人学到。','有些理解要经过长期相识才能得到。','作者建议熟悉后就结束关系。'],
 ['A some things不能扩大成everything，only learn from不等于自动保证都学会。','B 肯定长期才学到某些事，不是否定新相识所有价值。','C some与for a long time共同限定内容和时间条件。','D 没有结束关系建议。句子关注深度相识的可能价值，不给精确最低年限。'],
 ['There are some things you only learn from knowing one person for a long time.'],
 'for a long time','很长一段时间','强调理解的时间深度，没规定统一年数','They had known each other for a long time.',['know someone for a long time','learn from knowing someone'],
 '有些东西，只有长期认识同一个人，才会了解。')

add(24,'作者意图','How does B describe the renewal of first love?',
 ['As an ongoing activity, rather than merely looking back sadly or remembering poetically.','As abandoning marriage whenever its first excitement fades.','As a scientific claim already tested within this quotation.','As proof that novelty and commitment cannot coexist.'],0,
 'B怎样描述初恋的更新？',['是持续活动，而非只伤感回望或诗意追忆。','最初刺激减弱就抛弃婚姻。','此引文本身已做科学检验的论断。','证明新奇与承诺无法共存。'],
 ['A continual rejuvenation与not just...This is an activity清楚区分更新与被动回望。','B within...marriage强调婚姻中延续，非离开。','C 这段是Either/Or中B的主张，不是实验结果。','D sustained within marriage主张可以共存，非不能。最终问句尚待下段回答，不在此段补入实验解释。'],
 ['This rejuvenation…is not just a sad backward glance, or the poetic memory of an experience…. This is an activity.'],
 'rejuvenation','更新；恢复活力','指初恋感受在婚姻中的持续再生，不是生理返老还童','Shared reflection brought a sense of rejuvenation to the relationship.',['continual rejuvenation','a backward glance'],
 '《Either/Or》里的“B”认为，新奇、激情、自发，甚至冒险感都能在婚姻制度内保持。他说：“对我而言，这关系到我们初恋的不断更新……这种更新……不只是一次伤感的回望，或对经历的诗意记忆……这是一种活动。”那么，这种活动是什么呢？')

add(25,'细节','According to B, what kind of action helps sustain love?',
 ['Publicly displaying gratitude without any internal reflection.','Replacing all reflection with travel to unfamiliar places.','Recollecting first love only as an external historical record.','Internal grateful reflection, including gratitude to God.'],3,
 '按照B的主张，哪种活动有助于维持爱？',['只公开展示感激而不内省。','以陌生旅行取代全部反思。','仅把初恋当外部历史档案回忆。','内在的感恩反思，包括感激上帝。'],
 ['A not external but internal明确内在意义，非只外在展示。','B internal action/reflection不能替成旅行。','C 本段说want to hold on及grateful reflection，非仅档案记录。','D 第一句及According to B明确行动和观点归属；宗教情境中的主张不扩成所有人须信教的指令，后文研究不能提前拿来作本段证据。'],
 ['The answer is an internal action, or reflection, including gratitude to God.','According to B, grateful reflection in the context of religion helps you maintain your love toward your partner.'],
 'hold on to','保有；坚持；不放开','此处指想珍惜延续初恋，而非抓住实体物件','They wanted to hold on to the affection they had shared.',['hold on to first love','grateful reflection'],
 '答案是一种内在活动，也就是反思，其中包括对上帝的感激。“这样的感恩，像一切祈祷一样，都结合着行动因素；不是外在、而是内在意义上的行动，在此就是想保有这份初恋。”按照B的看法，在宗教情境中怀着感激反思，有助于维持对伴侣的爱。')

assert len(out)==25 and [q['id'] for q in out]==[t['questionId'] for t in targets]

def persist():
 path=ROOT/'source/short-questions/additional.json';existing=load('source/short-questions/additional.json');byid={q['id']:q for q in existing}
 for q in out:
  if q['id'] in byid:assert byid[q['id']]==q,('Refuse to overwrite changed authoring',q['id'])
  else:existing.append(q)
 path.write_text(json.dumps(existing,ensure_ascii=False,indent=2)+'\n',encoding='utf8',newline='\n')
 review=dict(batchId='batch-037',date='2026-10-24',pdfSha256=b['pdfSha256'],checkedPdfPages=list(range(147,152)),questionIds=[q['id'] for q in out],paragraphs=[dict(id=pid,textSha256=hashlib.sha256(pp[pid]['text'].encode()).hexdigest()) for pid in dict.fromkeys(q['paragraphId'] for q in out)],note='完整PDF147–151原页视觉核对。D.J.来信续句与不同人过量阈值按原文，不设统一次数。Taylor Mac连续24小时现场非录音/24场；Morris/Needham为评论个人体验，非控制实验。舞台扮演偏见不等于认同偏见；imaginary bus非真实出行自传，seismic/roof为修辞，7am还有5小时。q-c13-032承接闭引号原字保留。作者肯定丰富又犹豫，健康风险might及occasionally、might consider不扩为人人持续冒险；Polley是作品例子非疗效试验或文档行动指令。A/B哲学人物立场分清、presumably保留。妻子1991相识/1999结婚/约2010挂画，作者must be happy为观察推测非诊断；此前焦虑与画作欢快可以并存。boy是感叹，most非全部；B内在感恩为归属明确的哲学宗教主张，不提前援引下一段实验当本段证据。原有额外正文审计待办仍开放，候选池无漏ID不等于全书正文无遗漏。')
 (ROOT/'source/short-questions/review-chapter13-extremes-familiar25.json').write_text(json.dumps(review,ensure_ascii=False,indent=2)+'\n',encoding='utf8',newline='\n')
 print('Saved',len(out),'of 25 individually authored exercises')

if __name__=='__main__':persist()
