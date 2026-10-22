"""50 individually authored exercises for frozen targets, PDF pages 41-49.
Preserve printed English, source positions and all previously published questions.
"""
from pathlib import Path
import json,hashlib
ROOT=Path(__file__).resolve().parents[2]
load=lambda p:json.loads((ROOT/p).read_text(encoding='utf8'))
b=load('public/data/book.json');plan=load('public/data/reading-plan.json');targets=load('source/short-questions/batch012-targets.json')['targets']
ss={s['id']:s for s in b['sentences']};pp={p['id']:p for p in b['paragraphs']};out=[]
def add(i,kind,prompt,options,answer,prompt_zh,options_zh,analyses,quotes,word,meaning,context,example,collocations,translation,support='explicit'):
 t=targets[i-1];u=next(u for u in plan['units'] if u['id']==t['readingUnitId']);group=[ss[sid] for sid in u['sentenceIds']];p=pp[u['paragraphId']];text=p['text'][group[0]['start']:group[-1]['end']]
 assert hashlib.sha256(text.encode()).hexdigest()==t['passageSha256'];evidence=[]
 for quote in quotes:
  offset=text.find(quote);assert offset>=0,(i,quote);start=group[0]['start']+offset;end=start+len(quote);touching=[s for s in group if s['start']<end and s['end']>start]
  evidence.append(dict(quote=quote,sentenceIds=[s['id'] for s in touching],sources=list({(r['pdfPage'],r['block']):r for s in touching for r in s['sources']}.values())))
 assert word.lower() in text.lower(),(i,word)
 out.append(dict(id=t['questionId'],version=1,readingUnitId=u['id'],chapterId=u['chapterId'],sectionId=u['sectionId'],paragraphId=u['paragraphId'],sentenceIds=u['sentenceIds'],passage=text,prompt=prompt,options=options,answer=answer,type=kind,promptZh=prompt_zh,optionsZh=options_zh,analyses=analyses,evidence=evidence,vocabulary=[dict(word=word,meaning=meaning,context=context,example=example,collocations=collocations)],translation=translation,support=support,editorialStatus='PDF 第 41–49 页逐题核对；固定连续原句；区分个案、焦点小组自述和诗歌引例，不扩大研究范围或因果'))

add(1,'推断','What lasting value does the speaker find in these experiences?',
 ['They will provide memories and stories to share later in life.','They make every difficult experience impossible.','They remove any need to communicate with other people.','They are valuable only if repeated in precisely the same way.'],0,
 '说话者从这些经历中看到什么长久价值？',['它们留下日后可以分享的回忆和故事。','它们使一切艰难经历都不可能发生。','它们消除与他人交谈的需要。','只有一模一样地重复才有价值。'],
 ['A something...I can sit and talk about 把体验与日后讲述连接起来。','B enjoyed every minute 是个人感受，不保证所有困难消失。','C talk about 恰恰保留交流价值。','D 原句赞叹外面的发现，没有必须精确重复的条件。'],
 ['It gave me something when I get older, I can sit and talk about.'],
 'miraculous','奇妙的；令人惊叹的','表达说话者对所见所历的赞叹，不是在提出超自然证据','The transformation of the neglected garden seemed miraculous.',['a miraculous change','seem miraculous'],
 '“实在难以想象，外面能遇到那么多美丽、奇妙的事物……简直令人惊叹。而且我享受其中每一分钟……它给了我一些东西，等我更老时，可以坐下来谈一谈。”','inference')

add(2,'语境词义','What does the clarification “psychologically rich” indicate?',
 ['Joy’s wealth is measured by the value of her home.','The richness concerns her experiences and stories rather than stated financial assets.','Joy has stopped telling stories because she is ninety-four.','Financial success is described as the only source of a rich life.'],1,
 'psychologically rich 这一补充说明表示什么？',['Joy 的丰富程度用房产价值衡量。','这里的丰富指经历与故事，而不是列明的财产。','Joy 因九十四岁而不再讲故事。','财务成功被说成丰富生活的唯一来源。'],
 ['A 本句没有房产或财产计量。','B 破折号中的 psychologically 明确丰富的维度，many stories 是相关内容。','C many stories to tell 与不再讲故事相反。','D 没有 only，且解释强调心理维度。'],
 ['many stories to tell about her incredibly rich—psychologically rich—life.'],
 'incredibly','极其；令人难以置信地','修饰 rich，强化丰富程度，而非表示故事不可信','The small exhibition was incredibly varied.',['incredibly rich','incredibly varied'],
 '如今九十四岁的 Joy，有许多故事可以讲述，关于她极其丰富——心理丰富——的人生。年龄按原书当时的叙述保留。')

add(3,'细节','Why was Linda driving a taxi part-time?',
 ['To meet a condition for keeping her county-government job.','To replace a full-time university teaching position.','To stay occupied and earn additional money after retirement.','To transport only passengers who were visiting UC Riverside.'],2,
 'Linda 为什么兼职开出租车？',['满足保留县政府工作的条件。','代替大学全职教职。','退休后让自己有事做，并赚些额外收入。','只接送访问 UC Riverside 的乘客。'],
 ['A retired years before 说明此前已退休，没有保留职位条件。','B 大学教授是乘客的身份，不能移给司机。','C keep herself busy 与 make extra money 是两个直接目的。','D 本段没有限定接客对象。'],
 ['She was driving part-time to keep herself busy and make extra money.'],
 'part-time','兼职地；非全日制地','修饰 driving，说明她退休后的工作安排','He works part-time at the library.',['work part-time','a part-time job'],
 '2022 年 3 月 11 日，我从加州 Riverside 的酒店乘出租车去机场。司机——我就叫她 Linda 吧——向我讲起她的人生故事，真是精彩。她曾在县政府工作，多年前已退休。她兼职开车，让自己有事可做，也赚些额外收入。')

add(4,'细节','Which statement correctly assigns the family details in the conversation?',
 ['The narrator had seven grandchildren and Linda had two children.','Linda had two children, both professors at UVA.','The narrator’s youngest daughter had just become the taxi driver.','The narrator had two children, while Linda had four children and seven grandchildren.'],3,
 '哪项正确对应了谈话中的家庭信息？',['叙述者有七个孙辈，Linda 有两个孩子。','Linda 有两个孩子，都是 UVA 教授。','叙述者最小的女儿刚成为出租车司机。','叙述者有两个孩子，Linda 有四个孩子和七个孙辈。'],
 ['A 把 answer: yes, two kids 和她的家庭数据错配。','B four kids 不是两个；教授是叙述者自己的工作。','C youngest daughter 属于 Linda，刚搬到 Riverside，不是成为司机。','D 人称、孩子与孙辈数量均与原句对应。'],
 ['answer: yes, two kids','she had four kids and seven grandchildren, two of whom she had given birth to.'],
 'grandchildren','孙辈；孙子女与外孙子女','表示 children 的下一代，不能把四个孩子与七个孙辈加成同一代','Her grandchildren visit during the school holidays.',['children and grandchildren','seven grandchildren'],
 '她问我为什么来 Riverside（回答：访问 UC Riverside），以及做什么工作（回答：当时在弗吉尼亚大学当教授）。这使她谈起刚搬到 Riverside 的小女儿，以及其他孩子，其中一个住在华盛顿特区。她问我有没有家庭（回答：有，两个孩子），又说自己有四个孩子和七个孙辈，其中两个是她亲自生下的。')

add(5,'逻辑关系','What reason does Linda give for carrying her daughter’s children?',
 ['Her daughter had medical conditions that made pregnancy and delivery life-threatening.','Her daughter wanted Linda to become the children’s genetic mother.','The narrator had recommended that every grandmother do the same.','Linda wanted to increase the number of her own children from four to seven.'],0,
 'Linda 为什么替女儿孕育孩子？',['女儿的疾病使怀孕与分娩危及生命。','女儿想让 Linda 成为孩子的遗传学母亲。','叙述者建议每位祖母都这样做。','Linda 想把自己的孩子从四个增加到七个。'],
 ['A She did so because 后直接给出这个个案的原因。','B 原文给的是女儿的卵子和女婿的精子，不能换成 Linda 的卵子。','C 作者表示惊讶并听解释，没有对所有祖母作建议。','D 七个是孙辈总数，不是她自己孩子的目标数。'],
 ['She did so because her daughter had medical conditions that made pregnancy and delivery life-threatening.'],
 'gestational carrier','妊娠代孕者；孕育胚胎者','是文中 Linda 所述角色；理解她代为妊娠与配子来源的区别，不延伸为医疗建议','The article explains the term gestational carrier.',['a gestational carrier','serve as a gestational carrier'],
 '等等，她怀过自己的孙辈？我简直不敢相信。于是她继续解释：她分别在五十二岁和五十五岁时，为女儿和女婿做了妊娠代孕者，通过体外受精，使用女婿的精子和女儿的卵子妊娠。她这样做，是因为女儿的疾病使怀孕和分娩有生命危险。')

add(6,'细节','How does Linda distinguish her bond with the grandchildren she carried?',
 ['She says none of the other grandchildren matter to her.','She values all seven but feels a particular bond with the two she carried.','She says she carried all seven and feels exactly the same toward each.','She denies having any emotional response when telling the story.'],1,
 'Linda 怎样描述与自己孕育的孙辈的感情？',['她说其他孙辈对自己都不重要。','七个都特别，但与自己孕育的两个有特殊联系。','她说七个全由自己孕育，对每个感受完全相同。','她否认讲故事时有任何情绪。'],
 ['A while all seven grandkids are special 明确保留对所有孙辈的珍视。','B all seven special 与 special bond with the two 两层都被保留。','C 原文只说 two she carried，不是全部七个。','D almost crying 是强烈情绪表现，与否认情绪相反。'],
 ['while all seven grandkids are special, she shared a special bond with the two she carried.'],
 'bond','纽带；亲密联系','指人际情感关系，不是血缘或遗传来源的证明','The shared project created a strong bond between them.',['a special bond','a close bond with'],
 'Linda 讲这个故事时几乎哭了。两个孙辈出生时她都做了剖宫产，也分别喂过母乳。我问她是否觉得他们像自己的孩子，她坦言：七个孙辈都很特别，但自己与亲自孕育的那两个，有一种特殊纽带。')

add(7,'逻辑关系','Why does Linda’s answer remind the author of Marsh’s research?',
 ['It shows that Linda was a participant in Marsh’s experiment.','It establishes that all organ donors have identical motives.','She presents an exceptional good deed as simply the right thing to do.','She argues that helping relatives can never count as altruism.'],2,
 'Linda 的回答为什么让作者想到 Marsh 的研究？',['这证明 Linda 参加过 Marsh 的实验。','这确认所有器官捐献者的动机完全相同。','她把非凡善举说成只是应该做的事。','她主张帮助亲属绝不算利他。'],
 ['A reminded me of 是联想，不是确认参加研究。','B tend to downplay 不是所有捐献者动机一致的定论。','C 她淡化自我称赞，与研究中利他者淡化善举的倾向相呼应。','D 没有关于所有亲属帮助的排除性定义。'],
 ['it was simply the right thing to do.','extraordinary altruists, who, she found, tend to downplay their good deeds.'],
 'downplay','淡化；轻描淡写','指降低对自己善举的强调，不等于善举没有发生','She tends to downplay her contribution to the project.',['downplay an achievement','downplay one’s role'],
 '接下来，她的故事愈发有趣。她提到曾把自己的一个肾捐给前夫。我说她一定格外无私，她却回答：不是，那只是应该做的事。她的回答让我想到 Abigail Marsh 对非凡利他者的研究；Marsh 发现，这些人往往会淡化自己的善举。','inference')

add(8,'细节','What reason does Linda give for seeing the kidney donation as right?',
 ['Her ex-husband had raised all four children before she met him.','She believed that her children’s success removed any obligation to others.','She had received a kidney from him when she was eighteen.','She credits the stability he provided with helping her raise four successful children.'],3,
 'Linda 为什么认为向前夫捐肾是应该做的事？',['她与前夫相识前，四个孩子都由他抚养。','她认为孩子成功就消除了对他人的一切责任。','她十八岁时曾接受他捐的肾。','她认为他提供的稳定生活帮助自己养育了四个成功的孩子。'],
 ['A before they met 描述她十八岁生双胞胎，不是前夫已抚养四人。','B 原文是感念支持而捐赠，并非成功后无责任。','C 十八岁对应生育，不是接受器官捐献。','D without having the stability...provided 是她说明的关键理由。'],
 ['she could never have raised four kids who all turned out to be very successful without having the stability that her (now ex) husband had provided.'],
 'turned out','结果成为；最终发展为','turned out to be 说明孩子后来成长的结果','The difficult task turned out to be a useful lesson.',['turn out to be','turn out well'],
 'Linda 解释，没有后来成为前夫的丈夫提供的稳定生活，自己绝不可能把四个孩子都养育得很成功。四人中的两个是双胞胎，是她十八岁、尚未与他相识时生下的。把一个肾捐给他，是应该做的事。')

add(9,'主旨','What principle best explains Linda’s approach to retirement?',
 ['Work should take priority over all travel and family activities.','Once she had enough, she wanted work to support a life arranged on her own terms.','Retirement meant refusing any further paid work.','She valued travel only when it involved returning to the same country every year.'],1,
 '什么原则最能解释 Linda 的退休安排？',['工作应优先于所有旅行和家庭活动。','有了足够条件后，她希望工作服务于自己安排的生活。','退休意味着拒绝此后任何有酬工作。','她只珍视每年回同一个国家的旅行。'],
 ['A she worked to live 明确把生活而非工作放在目的位置。','B enough、enjoy her life、structure her life...wanted 共同说明自主安排。','C work here and there 保留偶尔工作的可能。','D France 与 Vietnam、Cambodia、Thailand 展示多地旅行，没有每年同国限制。'],
 ['she didn’t live to work; she worked to live.','structure her life in the way she wanted.'],
 'sing the praises of','赞美；称赞','她赞美加州的自然环境，是习语，不一定指唱歌','Visitors often sing the praises of the town’s quiet parks.',['sing the praises of a place','sing someone’s praises'],
 '她接着赞美加州的山、沙漠与海洋，说自己喜欢退休生活，每年能旅行两三个月。她刚在法国待了三个月，前一年又花两个月游历越南、柬埔寨和泰国。她提早退休，因为她不是为工作而活，而是为生活而工作。具备足够条件后，她只想享受人生：偶尔工作，按自己想要的方式安排生活。')

add(10,'细节','Which pattern of family contact is explicitly described?',
 ['She spoke to one child daily but never saw the others.','They visited daily but spoke only on holidays.','She spoke to all four adult children every day, and they visited regularly.','The four children contacted one another without speaking to her.'],2,
 '这句话明确描述了怎样的家庭联系？',['她每天只与一个孩子说话，其他人从不见面。','他们每天见面，但只在节日交谈。','她每天与四个成年子女都交谈，也经常互访。','四个子女彼此联系，却不与她交谈。'],
 ['A all four 不是仅一人，regularly 也不是从不见。','B daily 修饰交谈，regularly 修饰互访，不能对调。','C 两种频率及对象范围都与原句一致。','D 主句主语 She 明确参与交谈。'],
 ['She talked to all four adult children daily, and they visited each other regularly.'],
 'regularly','定期地；经常地','描述互访保持一定频率，不必等于每天','The neighbours meet regularly to discuss local projects.',['visit regularly','meet regularly'],
 '她每天都与四个成年子女交谈，他们也经常互相探望。')

add(11,'推断','What does the author’s assessment of Linda suggest about the three dimensions?',
 ['Financial wealth is required before any other dimension is possible.','A difficult early life rules out later happiness or meaning.','Psychological richness must replace happiness rather than coexist with it.','Psychological richness can coexist with happiness and meaning without stated financial wealth.'],3,
 '作者对 Linda 的评价说明这三个维度可能是什么关系？',['必须先有财富，其他维度才可能出现。','早年生活艰难会排除日后的幸福或意义。','心理丰富必须取代幸福，不能并存。','即使没有被描述为财务富有，心理丰富仍可与幸福和意义并存。'],
 ['A might not be financially rich 仍接肯定心理丰富，非财富先决条件。','B Despite...early on 转折说明早年困难没有排除现在的生活。','C all three dimensions 表明作者认为可以并存。','D 保留 might、I think 和 seems 的评价性质，不把个案扩成所有人的保证。'],
 ['Linda might not be financially rich, but she is psychologically and experientially rich.','she now seems to live her life in all three dimensions.'],
 'experientially','从经历而言；在亲历层面上','与 psychologically 并列，区分经历丰厚与金钱富有','The exchange programme was experientially rich for the students.',['experientially rich','experientially grounded'],
 '多么有趣的人生，我想。Linda 财务上也许不富有，但她在心理和经历上很丰富。我想，也可以说她幸福，并且过着有意义的生活。尽管早年作为单亲母亲经历困难，如今她似乎在三个维度上都活得充实。','inference')

add(12,'作者意图','What is the purpose of these opening questions?',
 ['To investigate which experiences contribute to psychological richness and which do not.','To announce that exploration has no connection with psychological richness.','To prove that every unusual experience has the same psychological value.','To replace the question of experience with a ranking of national wealth.'],0,
 '这些开头问题的作用是什么？',['探究哪些经历有助于心理丰富，哪些没有。','宣布探索与心理丰富毫无联系。','证明每种不寻常经历的心理价值相同。','把经历问题换成国家财富排名。'],
 ['A ingredients、contribute 和 impoverished 从正反两面提出探究范围。','B If...tends to lead 保留探索与丰富的倾向联系，没有否定联系。','C 连续问句尚在探究成分，未证明所有经历价值相同。','D 没有国家财富排名。'],
 ['what exactly are the ingredients of psychological richness?','What kinds of experiences are psychologically impoverished?'],
 'impoverished','贫乏的；缺少丰富性的','psychologically impoverished 指心理体验贫乏，不是单指经济贫困','The account felt emotionally impoverished without the personal details.',['psychologically impoverished','an impoverished experience'],
 '如果探索的生活往往通向心理丰富的生活，那么心理丰富究竟由什么构成？什么样的经历有助于心理丰富？什么样的经历在心理上是贫乏的？')

add(13,'细节','Who took part in the two focus groups described?',
 ['Randomly selected residents from two different countries.','Undergraduate research assistants in one group, and graduate students and postdocs in the other.','Only two undergraduate students, each observed alone.','Professors in one group and their family members in the other.'],1,
 '这里的两个焦点小组由哪些人组成？',['从两个国家随机抽取的居民。','一组本科研究助理，另一组研究生和博士后。','仅两名本科生，每人单独接受观察。','一组教授，另一组教授家属。'],
 ['A 原文是作者的学生与研究人员，没有随机跨国抽样。','B consisted of 后分别给出两组成员。','C two 是小组会议数，非只有两名被试，且另组包括研究生和博士后。','D 教授家属不在名单中。'],
 ['One group consisted of my undergraduate research assistants, and the other consisted of my graduate students and postdocs at UVA.'],
 'focus group','焦点小组；专题讨论组','这里通过回顾和讨论周末经历收集回答，不是随机干预实验','The researchers held a focus group to discuss commuting experiences.',['hold a focus group','focus group discussions'],
 '为弄清这些问题，我在 2015 年九月组织了两次焦点小组会议。一组是我的本科研究助理，另一组是我在 UVA 的研究生和博士后。首先，我请他们回想周末做过什么。然后问，哪件事让他们最幸福。')

add(14,'细节','Which pairing accurately reflects the majority responses?',
 ['Happiest: volunteering; most meaningful: going out with friends.','Happiest: religious services; most meaningful: an event not yet described.','Happiest: outings with friends or family; most meaningful: helping, religious services, or volunteering.','Happiest: working alone; most meaningful: avoiding commitments.'],2,
 '哪一项准确配对了多数人的回答？',['最幸福：志愿服务；最有意义：与朋友外出。','最幸福：宗教活动；最有意义：尚未描述的事件。','最幸福：与亲友外出；最有意义：助人、宗教活动或志愿服务。','最幸福：独自工作；最有意义：回避承诺。'],
 ['A 把两类主要回答对调。','B 宗教活动属于 meaningful 的回答，不是本段 happiest 的多数回答。','C 两项 majority 各自对应的内容均正确。','D 两类活动均非本段报告的多数回答；不能自行添加。'],
 ['going out with friends or family was their happiest event.','The majority of answers involved helping someone, attending a religious service, or volunteering.'],
 'majority','多数；大部分','只报告这两组回答中的多数，不代表所有人或全体人口','The majority of respondents preferred the earlier start time.',['the majority of answers','a majority of respondents'],
 '多数人回答，与朋友或家人外出，是最让他们幸福的事。接着，我问哪件事最有意义。多数回答涉及帮助他人、参加宗教活动或做志愿服务。最后，我问哪件事最具心理丰富性。')

add(15,'同义改写','Which paraphrase best preserves the description of the event?',
 ['An event counts only if it excludes both happiness and meaning.','An ordinary event becomes unusual merely by being repeated.','Happiness and meaning alone are stated to be sufficient for the description.','The event is unusual and interesting, rather than merely happy or meaningful in itself.'],3,
 '哪种改写最忠实于这里对事件的描述？',['只有完全排除幸福和意义才算。','普通事件只要被重复就自动变得不寻常。','幸福和意义本身被说成已足以符合描述。','事件不寻常而有趣，不只是本身令人幸福或有意义。'],
 ['A not just 不等于 must exclude；可以兼具幸福或意义。','B 原文没有重复造成新奇的因果。','C unusual and interesting 是额外强调，不能只剩幸福或意义。','D 同时保留两个形容词与 not just、per se 的范围。'],
 ['an event that was unusual and interesting, not just happy or meaningful per se.'],
 'per se','本身；就其本身而言','限定 happy or meaningful，不表示心理丰富必须排斥这两者','The delay was not a problem per se; the lack of information was.',['not harmful per se','valuable per se'],
 '我把它解释为一种不寻常、有趣的事件，而不只是本身让人幸福或有意义的事件。')

add(16,'逻辑关系','How did Grace’s view of professional wrestling change in this account?',
 ['She expected fake violence and cheap drama, but discovered a possible positive role for children.','She expected children’s charity work, but discovered there were no charities involved.','She had attended many matches and found the experience entirely predictable.','She went to study a scientific theory but left rejecting all role models.'],0,
 '在这段叙述中，Grace 对职业摔角的看法怎样变化？',['原以为是虚假暴力和廉价戏剧，后来看到对儿童可能有积极作用。','原以为有儿童慈善，后来发现完全没有。','她此前看过许多场比赛，觉得完全可预测。','她为研究科学理论而去，后来拒绝所有榜样。'],
 ['A expecting 对照 To her surprise, she left with the discovery，方向正确。','B 慈善是她后来注意到的内容，不是被否定的原先预期。','C first professional wrestling event 明确是第一次。','D 原文没有科学理论研究或拒绝所有榜样。'],
 ['She went in expecting stereotypical fake violence and cheesy drama.','professional wrestlers can be inspiring role models for children'],
 'cheesy','俗气的；廉价煽情的','cheesy drama 是 Grace 入场前的预期评价，不是作者已经确认的事实','The scene felt cheesy because every reaction was exaggerated.',['cheesy drama','a cheesy line'],
 'Grace 和 Rachel 的回答最令人难忘。Grace 是来自华盛顿特区郊区的大二学生。周末，她第一次与朋友去看职业摔角。入场时，她以为会看到刻板印象里的假暴力和廉价戏剧。出乎意料，她离场时发现，职业摔角手可以成为激励儿童的榜样，因为 WWE 大力投入儿童慈善事业。')

add(17,'细节','Beyond attending for the first time, what made Grace’s experience richer than a typical outing?',
 ['The absence of any painful or angry emotions.','Her unexpected change in perspective.','The certainty that her initial expectations were entirely correct.','Her decision to avoid cheering with the audience.'],1,
 '除了第一次参加，什么让 Grace 的经历比普通外出更丰富？',['没有任何痛苦或愤怒情绪。','她的视角发生意料之外的变化。','她确定最初的预期全都正确。','她决定避免与观众一起欢呼。'],
 ['A felt outraged and pained 明确包含不愉快感受。','B In addition to novelty 后明确点出 unexpected change in perspective。','C change 表示视角发生变化，不是原先印象毫无改变。','D cheered 是发生过的反应，不是刻意避免。'],
 ['her unexpected change in perspective made this experience much richer than a typical outing.'],
 'novelty','新奇性；首次体验带来的新鲜感','与视角变化并列，说明新奇不是这里唯一的丰富来源','The novelty of the new route made the walk engaging.',['the novelty of an experience','a sense of novelty'],
 '她笑、欢呼，也感到愤怒和痛苦，最终被这次体验深深打动。除了首次观看摔角比赛的新奇，她意料之外的视角变化，也让这次经历比普通外出丰富得多。')

add(18,'细节','What makes the encounter in Rachel’s apartment lounge unusual?',
 ['The young man is writing on a laptop without a shirt.','The young man is giving a formal lecture to residents.','Rachel has already met him at a wrestling match.','The lounge has been converted into a private bedroom.'],0,
 'Rachel 在公寓休息室遇到的情景有什么不寻常？',['年轻男子没穿上衣，正在笔记本电脑上写东西。','年轻男子正在给住户作正式演讲。','Rachel 已在摔角赛上见过他。','休息室已被改造成私人卧室。'],
 ['A writing...laptop 与 shirtless 是片段明确给出的组合。','B 没有演讲或听众。','C 摔角是另一人的经历，本段没有先前相识。','D lounge 是楼内公共休息空间，未说改成卧室。'],
 ['A young man (most likely another UVA student) was writing something on his laptop. What was strange was that he was shirtless.'],
 'lounge','休息室；公共起居空间','指公寓楼供住户使用的公共空间，不是她自己的房间','Residents gathered in the lounge after dinner.',['an apartment lounge','a common lounge'],
 'Rachel 也是 UVA 的大二学生，来自弗吉尼亚中部。同一个周末，她去了公寓楼的休息室，遇到不寻常的事。一名年轻男子（很可能也是 UVA 学生）正在笔记本电脑上写东西。奇怪的是，他没穿上衣。')

add(19,'推断','What can be concluded about why the man was shirtless?',
 ['Rachel confirmed that he was responding to extreme heat.','He explained that he wanted to display his physique.','Rachel remained puzzled, without a confirmed explanation.','The narrator established a medical reason for his behaviour.'],2,
 '对于男子为何不穿上衣，可以得出什么结论？',['Rachel 确认他因酷热脱衣。','他解释自己想展示体形。','Rachel 仍感到困惑，没有确认解释。','叙述者确定了其行为的医学原因。'],
 ['A It was not warm 排除将酷热当成本段已确认解释。','B didn’t seem to be showing off 不能变成他亲口确认炫耀。','C could not quite figure out 明确表示原因仍未弄清。','D 片段没有医学原因或诊断。'],
 ['This puzzled Rachel. She could not quite figure out why he was working shirtless in a common area.'],
 'figure out','弄清；理解','此处是否定形式，表示没有得出原因，不是已经发现真相','We need more information to figure out what happened.',['figure out why','figure out a problem'],
 '休息室里并不暖和。他看起来也不像在炫耀上身，因为体格并不特别健壮。这让 Rachel 困惑。她实在弄不明白，他为什么在公共区域光着上身工作。','inference')

add(20,'细节','Which feature does the author explicitly attribute to both experiences?',
 ['A lasting change in perspective.','An element of novelty and unexpectedness.','Participation in children’s charity work.','An identical range of intense emotions.'],1,
 '作者明确说两种经历都具有什么特征？',['持久的视角变化。','新奇与出乎意料的成分。','参与儿童慈善工作。','完全相同的一系列强烈情绪。'],
 ['A 本段尚未说两者都改变视角。','B Both...novelty and unexpectedness 直接对应。','C WWE 慈善不是 Rachel 遭遇的共同内容。','D 本段没有证明两者情绪种类和强度完全相同。'],
 ['Both Grace’s and Rachel’s experiences have an element of novelty and unexpectedness.'],
 'unexpectedness','意外性；不可预料性','是两种经历的共同点，不能据此自动认定丰富程度相同','The unexpectedness of the encounter made it memorable.',['an element of unexpectedness','novelty and unexpectedness'],
 '你觉得哪种经历心理上更丰富：Grace 的 WWE 之行，还是 Rachel 遇到的没穿上衣的男子？两人的经历都有新奇与意外成分。Grace 从未看过职业摔角，Rachel 也从没在公寓公共区域见过普通男子光着上身打字。两种经历当然都有趣。')

add(21,'逻辑关系','Why is Grace’s experience described as more emotionally complex?',
 ['Rachel experienced no emotion at all.','Grace felt only joy while Rachel felt many intense emotions.','Their experiences were equal because both involved surprise.','Grace felt many intense emotions, while Rachel felt mild surprise and apprehension.'],3,
 '为什么说 Grace 的经历在情绪上更复杂？',['Rachel 完全没有情绪。','Grace 只有快乐，Rachel 才有许多强烈情绪。','两者都惊讶，所以情绪复杂性相同。','Grace 有许多强烈情绪，Rachel 则只有轻度惊讶与不安。'],
 ['A mild surprise and apprehension 仍是情绪，不是没有。','B 颠倒两人的情绪范围和强度。','C 共有惊讶不等于整体情绪复杂性相同。','D lots of different, intense emotions 对比 only mild...，直接解释复杂性判断。'],
 ['whereas Grace experienced a lot of different, intense emotions, such as excitement, joy, fear, anger, and surprise, Rachel experienced only mild surprise and apprehension.'],
 'apprehension','担忧；不安','在此与 mild surprise 一起描述 Rachel 的较轻情绪反应','She felt some apprehension before entering the unfamiliar room.',['mild apprehension','a sense of apprehension'],
 '但它们丰富吗？首先，Grace 经历了兴奋、喜悦、恐惧、愤怒、惊讶等许多不同的强烈情绪，Rachel 却只感到轻度惊讶和不安。因此，Grace 的 WWE 经历在情绪上复杂得多。其次，Grace 入场前对 WWE 已有一些预设，回来时视角却不同了，例如了解到 WWE 支持反霸凌活动，许多孩子也崇拜摔角手。')

add(22,'主旨','What conclusion does the author draw from the two focus-group sessions?',
 ['Rich experiences involve novelty together with intensity, complexity, and perspective change.','Any unusual event is equally rich regardless of its effect.','Rich experiences must exclude negative emotions.','Rachel’s experience changed her perspective more than Grace’s did.'],0,
 '作者从两场焦点小组讨论得出什么概括？',['丰富经历包含新奇，也包含强度、复杂性和视角变化。','所有不寻常事件无论影响如何都同样丰富。','丰富经历必须排除负面情绪。','Rachel 的视角变化比 Grace 更大。'],
 ['A not only...but also 后列出的要素完整对应。','B 新奇不是唯一条件，不能推出同等丰富。','C 原句没规定排除负面情绪。','D Rachel...did not change 与此相反；这仍是讨论所得概括，不是普遍因果实验。'],
 ['psychologically rich experiences involve not only novelty but also intensity, complexity, and a change in perspective.'],
 'intensity','强度；强烈程度','与复杂性、新奇和视角变化并列，不只表示快乐强度','The intensity of the discussion surprised the visitors.',['emotional intensity','the intensity of an experience'],
 '也就是说，Grace 在事件后改变了视角。相比之下，Rachel 的经历新奇而不寻常，却完全没有改变她的看法。总体而言，两场焦点小组讨论显示，心理丰富的经历不仅涉及新奇，也涉及强度、复杂性和视角变化。')

add(23,'作者意图','What change in focus do these questions introduce?',
 ['From daily life to a ranking of weekend destinations.','From psychological richness to the exclusion of happiness and meaning.','From a rich weekend outing to the qualities of an entire day.','From student experiences to a confirmed causal theory.'],2,
 '这些问题引入什么关注点变化？',['从日常生活转向周末目的地排名。','从心理丰富转为排除幸福和意义。','从丰富的周末外出转向一整天的性质。','从学生经历转向已证实的因果理论。'],
 ['A 片段没有目的地排名，方向也相反。','B 最后一句仍询问 happy or meaningful，没有排除。','C weekend outing 对比 day，扩大考察单位。','D 连续问句提出问题，不是宣布已验证因果。'],
 ['what makes a weekend outing psychologically rich, what about a psychologically rich day?'],
 'relatedly','相关地；与此相联系地','连接心理丰富的一天与幸福、有意义的一天的相关提问','The report discusses cost and, relatedly, access.',['relatedly ask','and, relatedly,'],
 '既然已经弄清什么使周末外出心理丰富，那么心理丰富的一天又如何？什么让一天心理丰富或不丰富？相关地，什么让一天幸福或有意义？')

add(24,'细节','What ordinary scene is described in the account of Carver’s poem?',
 ['Friends discussing ambition beside a newspaper stand.','A newspaper boy and his friend walking up the driveway, smiling.','A visitor delivering coffee inside the poet’s study.','A crowd debating the meaning of happiness in the street.'],1,
 '对 Carver 诗歌的介绍描写了什么日常场景？',['朋友在报摊旁讨论抱负。','报童与朋友微笑着沿车道走来。','访客把咖啡送进诗人的书房。','人群在街上讨论幸福含义。'],
 ['A 本段没有抱负讨论或报摊。','B newspaper boy with his friend、driveway 和 smiling 都在原句中。','C 咖啡在观察者手边，没有访客送进房间的动作。','D 场景是两人微笑走来，不是人群辩论；诗歌不是实验记录。'],
 ['He sees the newspaper boy with his friend walking up to his driveway, just smiling'],
 'driveway','通向住宅的车道','指道路与住宅之间的进出通道，不能误译为室内走廊','A bicycle stood at the end of the driveway.',['walk up a driveway','a private driveway'],
 'Raymond Carver 在《幸福》一诗中描写清晨的日常。他端着咖啡坐在窗边向外看，见报童和朋友沿着通往自家的车道走来，只是微笑着：“幸福。它不期而至。')

add(25,'逻辑关系','What tension does “Yet” highlight?',
 ['The scene is extraordinary because it can never recur.','The scene is predictable, so each moment of happiness lasts permanently.','The author rejects any possibility of happiness in daily routines.','An ordinary repeatable scene can contain a sudden, fleeting happy moment.'],3,
 'Yet 强调了什么张力？',['场景因永不重现而非同寻常。','场景可预测，所以幸福时刻会永久持续。','作者否定日常生活中出现幸福的可能。','普通可重复的场景，也能包含突然、短暂的幸福时刻。'],
 ['A predictable, repeatable 不是永不重现。','B ephemeral 明确短暂，不是永久。','C Carver finds happiness in this mundane scene 肯定日常幸福。','D Yet 把场景的常见可重复，与瞬间的突然易逝并置。'],
 ['This is a predictable, repeatable scene. Yet it is also sudden and ephemeral.'],
 'ephemeral','短暂的；转瞬即逝的','与 predictable、repeatable 对照，形容当下幸福体验易逝','The evening light created an ephemeral glow on the water.',['an ephemeral moment','ephemeral beauty'],
 '“而且说真的，它超出了清晨任何关于它的谈论。”Carver 在这平凡场景中找到幸福。这是可预料、可重复的场景，却也突然且短暂。')

add(26,'细节','What is presented as part of a happy day in this account?',
 ['Noticing heartwarming things and laughing with friends.','Ignoring pleasant moments in order to analyse ambition continuously.','Avoiding all contact with friends and family.','Treating deep reflection as the sole necessary source of happiness.'],0,
 '这里把什么列为幸福的一天的组成部分？',['留意暖心事物，与朋友畅快大笑。','为持续分析抱负而忽略愉快时刻。','避免与亲友的一切接触。','把深思视为幸福唯一必需来源。'],
 ['A noticing something heartwarming 与 good laugh with friends 直接出现。','B don’t pay attention...miss it 警示错过，而非建议忽略。','C with friends 与回避一切接触相反。','D according to Carver 的文学解读不是普遍、唯一必要条件。'],
 ['noticing something heartwarming, having a good laugh with friends'],
 'heartwarming','暖心的；令人感动愉快的','形容值得留意的温暖日常，不要求重大成就','The neighbours shared a heartwarming story of kindness.',['a heartwarming moment','a heartwarming story'],
 '如果不留意，你可能就会错过。幸福的一天来自注意到暖心事物、与朋友畅快大笑，以及按照 Carver 的说法，不去思索死亡、抱负、爱情或太深奥的事。')

add(27,'作者意图','Why does the author turn to the idea of a meaningless day?',
 ['To show that meaningful and meaningless are identical.','To claim that every day without paid work is pointless.','To make the question easier by approaching it from the opposite direction.','To abandon the question of meaning altogether.'],2,
 '作者为什么转而讨论无意义的一天？',['说明有意义与无意义完全相同。','断言没做有酬工作的日子都无意义。','从反面入手，使问题更容易回答。','彻底放弃对意义的讨论。'],
 ['A flip 表示换为相反问题，不是两者相同。','B wasted 与 pointless 不是本段对有酬工作作定义。','C becomes much easier to answer 直接说明翻转提问的作用。','D 仍借反面推进原问题，并未放弃。'],
 ['When you flip the question to ask what a meaningless day is, all of sudden it becomes much easier to answer.'],
 'flip','翻转；换个相反角度','flip the question 把“有意义”换成“无意义”来思考','Try to flip the question and examine the opposite case.',['flip the question','flip the perspective'],
 '什么是有意义的一天？这个问题更难回答一点。可当你把问题翻过来，问什么是无意义的一天时，它突然容易回答多了。无意义的一天就是被浪费、全然没有价值的一天。')

add(28,'同义改写','Which statement best captures the contrast in the passage?',
 ['Familiar lectures are the only possible source of meaning.','A meaningless day adds little, whereas a meaningful day has a point and an accomplishment.','Every lecture necessarily makes the listener’s day meaningless.','A day has meaning only when it includes previously unknown information.'],1,
 '哪一项最准确概括这里的对比？',['熟悉内容的讲座是意义的唯一来源。','无意义的一天贡献很少，有意义的一天则有价值并有所完成。','任何讲座都必然使听众的一天无意义。','只有包含从未知道的信息，一天才有意义。'],
 ['A 讲座是对“没有增添太多”的类比，不是唯一来源。','B does not add much 与 opposite、point、accomplished 共同支持。','C material you already know well 有限定，不能扩为所有讲座。','D 示例不能改成只有新知识才有意义的排他条件。'],
 ['a meaningless day does not add much to your life. A meaningful day is the opposite. There is a point to that day. You’ve accomplished something.'],
 'accomplished','完成；达成','强调当天做成某件事，不限定必须重大或获奖','She accomplished the small task before lunch.',['accomplish something','accomplish a task'],
 '就像听一场内容早已熟悉的讲座，无意义的一天没给生活增添多少东西。有意义的一天则相反。这一天有其价值，你完成了某件事。')

add(29,'推断','What do the examples imply about accomplishment?',
 ['Only a publicly recognised achievement counts.','Helping someone counts only if it is paid work.','Laundry and exercise are excluded from worthwhile activity.','Ordinary completed activities can keep a day from feeling entirely wasted.'],3,
 '这些例子说明“完成事情”可以怎样理解？',['只有获公众认可的成就才算。','帮助别人只有收报酬才算。','洗衣与锻炼被排除在有价值活动之外。','日常小事的完成也可以让一天不至于全被浪费。'],
 ['A 写信、洗衣等并不要求公众认可。','B helped someone 没有有酬前提。','C 原文恰把 laundry 和 exercised 列作例子。','D 这些普通行动后接 not totally wasted，支持有限概括。'],
 ['You did laundry or exercised. You got something done, and the day was not totally wasted.'],
 'laundry','洗衣；待洗衣物','do laundry 在这里指做洗衣这项家务','He did the laundry before going out.',['do laundry','a load of laundry'],
 '比如，你也许写了一封信，帮助了某个人，洗了衣服或做了运动。你完成了某件事，这一天便没有完全浪费。','inference')

add(30,'逻辑关系','How does the reference to rest extend the account of meaning?',
 ['It allows needed rest that prepares for later work to have value even without much immediate output.','It says rest makes all future work unnecessary.','It limits meaningful days to days of maximum productivity.','It treats every inactive day as automatically meaningful.'],0,
 '提到休息怎样扩展了对意义的说明？',['即使当下产出不多，为后续工作恢复体力的必要休息也有价值。','说明休息会使一切未来工作都不必要。','把有意义的一天限制为产出最高的日子。','把每个没有活动的日子都自动算作有意义。'],
 ['A Even if...much-needed rest...prepare 保留产出少也可能有价值的情形。','B prepare...another day of hard work 仍指向未来工作。','C didn’t get much done 直接允许并非高产。','D maybe 和 much-needed 限定，不能变成所有不活动都有意义。'],
 ['Even if you didn’t get much done, maybe you got some much-needed rest to prepare you for another day of hard work.'],
 'much-needed','急需的；非常必要的','修饰休息，指出其恢复与准备作用，而非任意闲置都等价','The weekend provided a much-needed break.',['much-needed rest','a much-needed break'],
 '即使没完成多少事，也许你得到了急需的休息，为另一天的辛劳做好准备。让一天有意义的方式有很多。')

add(31,'语境词义','What do the “counterfactuals” concern in this account of Kenyon’s poem?',
 ['A confirmed report that none of her routines occurred.','A prediction of the exact date her routines will change.','Alternative possibilities in which she could not carry out ordinary routines.','A comparison proving that her breakfast was unusual.'],2,
 '这里的 counterfactuals 涉及什么？',['确认她一项日常活动都没发生的报告。','精确预测日常活动会在哪天变化。','她本可能无法完成平常活动的另一种可能。','证明早餐异常的比较。'],
 ['A She gets out...eats... 描述做到了，不是全没发生。','B might have been unable 不是精确日期预测。','C 与实际日常相对的“本可能无法做到”，正是反事实可能。','D Nothing special 不支持早餐异常。'],
 ['she might have been unable to get out of bed, unable to do all the routines. There are many counterfactuals in “Otherwise.”'],
 'counterfactuals','反事实设想','想象与已发生情形不同的可能，不是宣布事实记录造假','The essay uses counterfactuals to explore how events might have differed.',['consider counterfactuals','counterfactual thinking'],
 '像 Raymond Carver 一样，Jane Kenyon 在《Otherwise》中写日常生活：起床、吃早饭、吃午饭、午睡、吃晚饭、睡觉。没什么特别，除了她本可能无法起床、无法完成这些日常活动。《Otherwise》中有许多这样的反事实设想。')

add(32,'主旨','What makes an ordinary day precious in this interpretation?',
 ['It is valuable only if it produces a measurable gain.','It is appreciated partly because life could be worse or different.','It can never change in the future.','It removes the need to cherish daily life.'],1,
 '这一解读中，普通的一天为什么珍贵？',['只有产生可测量收益才有价值。','部分因为生活本可能更糟或不同，所以更值得珍惜。','未来永远不会改变。','它使珍视日常生活变得不必要。'],
 ['A not just...explicit gains 明确超出显性收益。','B could have been a lot worse 和 will be otherwise 支持通过可能差异珍视当下。','C will be otherwise 表示总有一天不同，并非永远不变。','D cherishes her mundane life 正是肯定珍视。'],
 ['It could have been a lot worse, which makes this typical day precious.','A meaningful day is not just a day with explicit gains.'],
 'cherishes','珍惜；珍视','指因意识到可能失去或变化而看重平常生活','She cherishes the quiet conversations with her family.',['cherish daily life','cherish a memory'],
 '事情本可能糟得多，这使寻常的一天变得珍贵。她显然珍惜平凡的生活。有意义的一天不只是有明确收获的一天，也可以是让你心怀感激的一天，因为“有一天，我知道，一切会变成别样”。')

add(33,'作者意图','How is Oliver’s poem used in the discussion of a rich day?',
 ['To establish that despair must be eliminated before exploration is possible.','To prove that only exceptionally virtuous people can imagine new possibilities.','To report an experiment involving the movements of wild geese.','To invite imaginative engagement with a world that can be harsh as well as exciting.'],3,
 'Oliver 的诗在丰富的一天的讨论中起什么作用？',['确立必须先消除绝望才能探索。','证明只有格外有德的人才能想象新可能。','报告关于野雁运动的实验。','邀请人以想象力接触既严酷又令人兴奋的世界。'],
 ['A despair is a part of life 承认绝望，不是消除前提。','B don’t have to be extraordinarily good or virtuous 否定这种门槛。','C 诗歌引例不是野雁实验。','D imagination 与 harsh and exciting 同时保留开放和复杂感受。'],
 ['the world offers itself to your imagination.','harsh and exciting.'],
 'despair','绝望','诗歌解读中被承认为人生的一部分，不是研究者对读者的诊断','The character moves between hope and despair.',['a sense of despair','hope and despair'],
 '那么，心理丰富的一天呢？Mary Oliver 在《Wild Geese》中告诉我们：不必格外善良或有德，绝望是生活的一部分，渺小也是存在的一部分。即便如此，她鼓励我们像野雁：“世界向你的想象力敞开自己。”世界有如此多可提供、可探索的东西：“严酷而令人兴奋。”')

add(34,'细节','Which combination describes a psychologically rich day here?',
 ['Unfamiliar experience, varied emotions, and a new perspective.','A familiar routine, one pleasant emotion, and unchanged beliefs.','Material success, public recognition, and freedom from uncertainty.','Avoidance of unusual events, emotional restraint, and complete predictability.'],0,
 '这里哪组特征描述心理丰富的一天？',['陌生经历、多样情绪和新视角。','熟悉常规、单一愉悦情绪和不变看法。','物质成功、公众认可和没有不确定性。','回避异常事件、压制情绪和完全可预测。'],
 ['A 三项分别对应 unfamiliar、wide range、new perspective。','B 将陌生改为熟悉、多样改单一、变化改不变。','C 原句没有财富、认可或零不确定性的要求。','D 与原句三项描述方向相反。'],
 ['experience something unfamiliar, feel a wide range of emotions, and gain a new perspective on life.'],
 'unfamiliar','陌生的；不熟悉的','指超出已有熟悉经验的事物，不一定危险或不愉快','The path led through an unfamiliar part of town.',['something unfamiliar','an unfamiliar experience'],
 '心理丰富的一天，是你经历陌生事物、感受广泛情绪，并获得新的人生视角的一天。')

add(35,'细节','Which statement correctly distinguishes participants from reports in the diary study?',
 ['There were more than 2,600 students, each reporting for two days.','More than 200 students reported for fourteen days, producing over 2,600 daily reports.','Exactly fourteen students produced 200 reports in total.','The researchers assigned 2,600 different experiences to each student.'],1,
 '哪项正确区分了日记研究中的参与人数与报告数量？',['超过 2,600 名学生，每人报告两天。','超过 200 名学生记录十四天，形成超过 2,600 份每日报告。','恰好十四名学生总共写了 200 份报告。','研究者给每位学生分配 2,600 种经历。'],
 ['A 把报告数误作人数，并改动记录天数。','B 人数、十四天与总报告数分别准确对应。','C fourteen 是天数，two hundred 是人数，不能调换。','D keep daily records 是记录行为感受，不是操控分配经历。'],
 ['more than two hundred college students to keep daily records of what they did and how they felt for fourteen days, resulting in over 2,600 daily reports.'],
 'respectively','分别地；各自对应地','把三类因素与幸福、有意义、心理丰富三种日子按顺序对应','The two groups met on Monday and Tuesday, respectively.',['correspond respectively to','A and B, respectively'],
 '我想知道，依据上述诗歌归纳出的幸福、有意义和心理丰富的一天的关键因素，是否也分别让普通大学生的一天幸福、有意义或心理丰富。Hyewon Choi 和我请两百多名大学生连续十四天记录做了什么、感受如何，最终得到超过 2,600 份每日报告。')

add(36,'细节','What did the activity checklist ask about?',
 ['Only students’ grades and family income.','The researcher’s judgement of which activity students should choose.','Whether students had volunteered, attended concerts, hiked, played games, and similar activities.','Only whether the day had been happy, with no questions about behaviour.'],2,
 '活动清单询问了什么？',['只问成绩与家庭收入。','研究者判断学生应该选哪项活动。','是否志愿服务、听音乐会、徒步、玩电子游戏等。','只问当天是否幸福，完全不问行为。'],
 ['A 这些项目没有出现在本段清单。','B asked whether 是询问已做的事，不是分配应做的事。','C 对应清单明确列出的活动例子。','D In addition to 说明除感受外还问常规、新事物和具体活动。'],
 ['an activity checklist that asked them whether they volunteered, went to a concert, hiked, played a video game, and so on.'],
 'checklist','核对清单；项目表','在研究中列出活动供参与者报告，不是活动指令','The organiser used a checklist to record completed tasks.',['an activity checklist','complete a checklist'],
 '除幸福、意义和心理丰富感外，我们还问每天典型还是不典型、参加多少常规活动、有多少空闲，以及是否做了新事、遇见新人或吃了新食物。我们还提供活动清单，询问是否做志愿服务、听音乐会、徒步、玩电子游戏等。这些每日报告让我们较清楚地看到学生怎样度过一天。')

add(37,'推断','Which conclusion stays closest to the reported finding?',
 ['Every person becomes happier whenever they try any new food.','Novelty affected psychological richness but never meaning or happiness.','The study randomly assigned novelty and established a universal causal law.','Most students reported all three qualities more positively on days involving something new.'],3,
 '哪项结论最贴近报告的发现？',['每个人每次尝试任何新食物都更幸福。','新奇只影响心理丰富，绝不涉及意义或幸福。','研究随机分配新奇经历，确立普遍因果规律。','多数学生在包含新事物的日子，对三个维度都报告得更积极。'],
 ['A most students 与 every person、whenever 的范围不同。','B not only...but also 明确涉及三个维度。','C 片段说 associated 和 reported，没有随机操控的说明。','D 保留多数、日子比较和自报性质，不额外保证因果。'],
 ['most students reported that their day was happier, more meaningful, and richer on a day when they did something new, ate something new, or met someone new.'],
 'associated with','与……相关联','指观察到的共同变化，不能自动读成随机试验确证因果','The survey found that participation was associated with higher satisfaction.',['be associated with','factors associated with well-being'],
 '首先，我们发现一些与幸福、意义和心理丰富这三个方面都相关的共同因素。做新事、吃新食物或遇见新人，不仅增强心理丰富，也增强幸福与意义。也就是说，多数学生报告，在做新事、吃新食物或遇见新人的日子，他们更幸福、更有意义，也更丰富。这是原书对日记报告结果的表述，不额外改写为随机实验结论。','inference')

add(38,'细节','Which comparison is actually reported?',
 ['Atypical days were richer but not happier; freer days were richer but not more meaningful.','Atypical days were happier but less rich; free time always reduced meaning.','Atypical and typical days were identical on all measures.','More free time made days more meaningful but never psychologically richer.'],0,
 '片段实际报告了哪组比较？',['不典型日子更丰富却不更幸福；更空闲的日子更丰富却不更有意义。','不典型日子更幸福但较不丰富；空闲总使意义下降。','典型与不典型日子所有指标都相同。','空闲更多使日子更有意义，却从不更丰富。'],
 ['A 分别保留 atypical 的丰富/幸福比较，以及 free time 的丰富/意义比较。','B 前半倒置；no more meaningful 不是必然降低意义。','C 原文明确给出丰富程度差异。','D 将空闲与丰富、意义的比较方向读反。'],
 ['an atypical day was psychologically richer than a typical day, but an atypical day was not happier than a typical day.','a free day was no more meaningful than a less free day.'],
 'atypical','非典型的；不同寻常的','与 typical 对比，不能自动等同于更快乐','An atypical schedule gave her time to explore a new route.',['an atypical day','an atypical experience'],
 '其次，我们发现心理丰富的一天有一些独特预测因素。例如，不典型的一天比典型日子心理上更丰富，却并不更幸福。空闲更多的一天比空闲少的日子心理上更丰富。相反，更空闲的一天并不比不那么空闲的一天更有意义。')

add(39,'逻辑关系','What distinction does the author draw between accomplishment and unusual activity?',
 ['Only unusual activity is linked to happiness and meaning.','Getting things done is linked to happier, more meaningful days, while unusual activity is linked to richness.','Required work and unusual activity are described as identical in every effect.','Routine activity is said to be the only route to psychological richness.'],1,
 '作者怎样区分完成事务与不同寻常的活动？',['只有异常活动与幸福及意义相关。','完成事务对应更幸福、有意义，不同寻常活动对应心理丰富。','必须做的工作与不寻常活动在所有作用上都相同。','常规活动是心理丰富的唯一路径。'],
 ['A 前两句把较多 required work 与幸福、意义相连。','B whereas 构成两种活动与不同维度的对照；不据此保证个人因果。','C 对照正强调不同侧重，并非全部效果相同。','D 最后强调 don’t usually do，非唯一常规路径。'],
 ['getting things done made the day happier and more meaningful, whereas doing something unusual made the day psychologically richer.'],
 'vineyard','葡萄园','作为短途外出的例子，不要求旅行昂贵或遥远','The walking route passes a small vineyard.',['visit a vineyard','a trip to a vineyard'],
 '最后，必须完成的工作更多的一天，比这类工作较少的一天更幸福、更有意义。也就是说，完成事务让一天更幸福、更有意义，而做不寻常的事让一天心理上更丰富。无论短途去葡萄园、走进城里陌生街区、看棒球赛，还是给小学老友打电话，做平时不常做的事，都比每天重复的事更有趣、更具心理丰富性。以上保留原书对报告结果的概括。')

add(40,'主旨','How are the emotional patterns of happy and psychologically rich days contrasted?',
 ['Happy days contain more negative emotions than rich days by definition.','Rich days are defined by the complete absence of negative feelings.','Happy days involve much positive and little negative feeling; rich days involve more of both.','Both kinds of day require watching news that agrees with one’s views.'],2,
 '幸福与心理丰富的日子在情绪模式上怎样对比？',['按定义，幸福日子的负面情绪比丰富日子更多。','丰富日子被定义为完全没有负面感受。','幸福日子正面多、负面少；丰富日子则两类情绪都更多。','两者都要求观看与自己观点一致的新闻。'],
 ['A 本段不是这种负面情绪比较，幸福日子是 not many negative。','B both positive and negative 明确保留负面。','C 对应前两句对两种日子的分析。','D Fox/CNN 是作者关于可能兴趣与不悦的例子，不是所有人的必要条件。'],
 ['a happy day was one in which participants experienced a lot of positive emotions and did not feel many negative emotions.','they felt more emotions—both positive and negative—than on a typical day.'],
 'subsequent','后续的；接下来的','修饰 analyses，表示前述报告之后进一步分析','Subsequent discussions clarified the proposal.',['subsequent analyses','subsequent research'],
 '后续分析还显示，幸福的一天是参与者有许多正面情绪、却没有多少负面情绪的一天。相比之下，心理丰富的一天，是他们比平常感到更多情绪的一天——既有正面，也有负面。例如，如果你是自由派，观看 Fox News 也许会不悦，却可能比观看 CNN 或其他更契合自己观点的频道更有趣。')

add(41,'逻辑关系','Why is study abroad proposed as a particularly rich experience?',
 ['It guarantees comfort by keeping all customs familiar.','It removes the need to encounter different norms.','It is ranked solely by the price of travel.','It places people in unfamiliar cultures that are exciting and challenging.'],3,
 '为什么作者认为留学可能是尤其丰富的经历？',['它让习俗保持熟悉，因而保证舒适。','它消除接触不同规范的需要。','排名只依据旅行价格。','它让人进入陌生文化，同时感到兴奋与挑战。'],
 ['A unfamiliar 和 challenging 与保证熟悉舒适相反。','B different...norms 正是所列要素。','C 论据是新奇、复杂与视角变化，不是价格排名。','D 陌生景观、习俗和规范解释了兴奋与多层挑战。'],
 ['an unfamiliar culture with different landscapes, customs, and norms','It’s exciting but also challenging at many levels.'],
 'norms','规范；群体惯例','指文化中的行为期待，不只是书面法律','Visitors gradually learned the community’s social norms.',['social norms','cultural norms'],
 '如果新奇、复杂性和视角变化是心理丰富的关键成分，那么留学必然在心理丰富事件中名列前茅。毕竟，留学让自己进入陌生文化，面对不同景观、习俗和规范——全新的生活方式。这令人兴奋，却也在许多层面充满挑战。')

add(42,'细节','What does the reported fall of nearly 96 percent refer to?',
 ['Americans studying abroad, comparing 2018–2019 with 2020–2021.','The worldwide population of university students in a single year.','A reduction in the cost of studying abroad after 2021.','The share of all Americans who had never travelled domestically.'],0,
 '这里接近 96% 的下降指什么？',['比较 2018–2019 与 2020–2021 学年美国留学人数。','某一年度全球大学生总人口。','2021 年后留学费用下降。','所有美国人中从未国内旅行的比例。'],
 ['A 344,099 到 14,549 的是 Americans studied abroad，两个学年明确给出。','B 人群不是全球全部大学生。','C 这是人数变化，不是费用。','D 留学人数不能换成国内旅行经历比例；数据按原书年份理解。'],
 ['344,099 Americans studied abroad during the 2018–2019 academic year.','during the 2020–2021 academic year the total number of Americans who studied abroad decreased by nearly 96 percent, to 14,549'],
 'deprived of','被剥夺；无法享有','指疫情时期失去探索机会，不是学生主动选择全部拒绝','The closure deprived residents of a place to gather.',['be deprived of opportunities','deprive someone of access'],
 '根据国际教育协会的数据，2018–2019 学年有 344,099 名美国人出国留学。由于全球疫情，2020–2021 学年美国留学人数下降近 96%，至 14,549 人，显示疫情时期有多少大学生失去了探索机会。这是书中给定年份的历史比较。')

add(43,'细节','Which expense is explicitly listed?',
 ['A salary for a private research assistant.','Room and board.','A permanent home purchase.','A compulsory professional licence.'],1,
 '这里明确列出了哪项支出？',['私人研究助理的薪资。','食宿。','购买永久住宅。','强制职业执照。'],
 ['A 片段未列研究助理费用。','B Room and board 直接出现，指食宿。','C 房屋购买不是 room and board 的含义。','D 原文没有执照支出。'],
 ['Studying abroad is expensive. Airplane tickets. Room and board. New clothes.'],
 'room and board','食宿','是费用搭配，board 在此不是木板或董事会','The programme fee includes room and board.',['pay for room and board','include room and board'],
 '留学很昂贵。机票。食宿。新衣服。')

add(44,'逻辑关系','What role did the scholarship play in the author’s account?',
 ['It required him to pay every expense without support.','It proved that students of all incomes had equal access.','It made participation possible by covering extensive costs.','It directed him to three universities in France.'],2,
 '奖学金在作者这段叙述中起什么作用？',['要求他无资助地承担全部费用。','证明各收入学生的机会完全相同。','承担广泛费用，使他有可能参加留学。','指定他去法国三所大学。'],
 ['A paid for full tuition... 与完全无资助相反。','B harder for lower socioeconomic status 明确指出门槛差异。','C couldn’t have done...if...hadn’t gotten 说明资助的关键作用。','D Maine 是推荐所在地，非 France，推荐来自导师。'],
 ['I couldn’t have done it myself if I hadn’t gotten the Rotary International scholarship'],
 'socioeconomic','社会经济的','描述家庭社会与经济条件，不单指个人学术能力','The study considered differences in socioeconomic background.',['socioeconomic status','socioeconomic background'],
 '因此，社会经济地位较低的学生更难参加。如果没获得 Rotary International 奖学金，我自己也做不到；它支付了全部学费、食宿、教材、往返机票，甚至一个月的暑期英语课！获得奖学金后，我问本科导师 Hara 教授该去哪里。他很推崇文理学院，推荐了缅因州的三所。')

add(45,'细节','Which sequence matches the author’s travel account?',
 ['Tokyo to Maine in July, followed by an August return to Tokyo.','Portland to Staten Island, then an English course in Tokyo.','A month at Wagner College before leaving Japan.','Tokyo to New York in July, a month studying English, then Portland in August.'],3,
 '哪组顺序符合作者的旅行叙述？',['七月东京赴缅因州，八月返东京。','Portland 到 Staten Island，然后在东京上英语课。','离开日本前先在 Wagner College 待一个月。','七月东京赴纽约，学一个月英语，八月赴 Portland。'],
 ['A 七月目的地是 New York City，不是缅因州；未说八月返日。','B 地点顺序和课程地点都被改动。','C Wagner College 在 Staten Island，是离开东京之后。','D 三个阶段的时间与地点都正确。'],
 ['In July 1991, I left Tokyo for New York City. I spent one month at Wagner College on Staten Island studying English. Then I flew to Portland, Maine, in August.'],
 'assumption','假定；设想','导师关于英语学习环境的判断，并非已验证每位留学生的最优方案','The plan rested on an assumption about travel time.',['an assumption that','make an assumption'],
 '他的设想是，我在那里不会遇到其他日本学生，能最好地学英语。1991 年七月，我离开东京前往纽约，在 Staten Island 的 Wagner College 学了一个月英语。然后八月飞往缅因州 Portland。')

add(46,'细节','What does the author remember more than thirty years later?',
 ['A conversation in the car after Dean Reese picked him up at the airport.','A formal music examination in Tokyo before departure.','A conversation in which he drove Dean Reese to the airport.','A lecture given before he enrolled at Wagner College.'],0,
 '三十多年后，作者仍记得什么？',['Reese 院长到机场接他之后的一段车中谈话。','出发前在东京的正式音乐考试。','由他开车送 Reese 去机场时的谈话。','入读 Wagner College 之前的一堂课。'],
 ['A picked me up 与 conversation in the car 直接对应。','B 没有考试，问题只是车中询问音乐偏好。','C picked me up 的接送主体被倒置。','D 本段是赴 Bates College 的接机经历，不是此前课程。'],
 ['Thirty-plus years later, I still remember our conversation in the car on that warm afternoon.'],
 'picked me up','来接我','这里指到机场接人，不是捡起物品','My friend picked me up at the station.',['pick someone up at the airport','pick someone up from school'],
 'James Reese 院长到机场接我，开车带我们去 Lewiston 的 Bates College。三十多年后，我仍记得那个暖和下午的车中谈话。“你最喜欢什么音乐？”Reese 院长问。')

add(47,'推断','What does “escaped me” mean in the context of the conversation?',
 ['The musicians physically left the car.','The author refused to listen to jazz.','The familiar names temporarily failed to come to mind.','Dean Reese had never heard of the musicians.'],2,
 '这里 escaped me 是什么意思？',['音乐家亲自离开了车。','作者拒绝听爵士乐。','熟悉的名字一时想不起来。','Reese 从未听过那些音乐家。'],
 ['A names 作主语，不是音乐家从车里逃离。','B 作者明确回答 Jazz，非拒绝听。','C at that moment 与 well-known names 表明暂时记忆提取失败。','D 没有关于 Reese 不认识这些人的说明。'],
 ['the most well-known names, like Charlie Parker and Miles Davis, escaped me at that moment.'],
 'escaped me','让我一时想不起','表示未能回忆起信息，不是信息主动逃跑','Her name escaped me for a moment.',['a name escapes someone','the answer escaped me'],
 '“爵士乐。”我说。身为黑人的 Reese 院长回答：“我也爱爵士！”接着问：“你最喜欢哪位音乐家？”不知怎么，那一刻连 Charlie Parker、Miles Davis 这样最出名的名字，我都想不起来。','inference')

add(48,'细节','How did the author initially interpret Dean Reese’s words?',
 ['As a request to turn up the music.','As an instruction to leave the car immediately.','As a confirmed invitation to perform jazz.','As a statement that Bill Evans was waiting outside.'],1,
 '作者最初怎样理解 Reese 院长的话？',['要求把音乐开大。','命令自己立刻下车。','确认邀请自己演奏爵士。','说 Bill Evans 正在外面等。'],
 ['A 没有调节音乐音量的动作。','B I thought 明确交代作者当时以为应该立刻离开车。','C 未提演出邀请。','D 未说音乐家在场；只可确定作者的初始理解，不能据此认定 Reese 真在赶人。'],
 ['I thought he meant that I should get out of the car right that moment.'],
 'pause','停顿','long pause 指回答前较长沉默，不是旅程暂停','After a brief pause, she answered the question.',['a long pause','after a pause'],
 '长长停顿之后，我说：“Bill Evans。”Reese 院长立刻说：“Get out of here!” 我吓坏了，以为他要我当场下车。')

add(49,'细节','What coincidence does Dean Reese explain?',
 ['Bill Evans had also studied at Bates College.','Every Japanese student preferred the same musician.','The author and Reese had both been taught by Bill Evans.','Another former Japanese student had also named Bill Evans as a favourite.'],3,
 'Reese 院长解释了什么巧合？',['Bill Evans 也在 Bates College 读过书。','所有日本学生都喜欢同一音乐家。','作者与 Reese 都受过 Bill Evans 教导。','另一位以前的日本学生也最喜欢 Bill Evans。'],
 ['A 本句没有音乐家的就读履历。','B another former Japanese student 仅另一个人，非所有人。','C 没有师生关系的信息。','D another、also 与 Bill Evans 清楚说明共同偏好。'],
 ['another former Japanese student’s favorite musician was also Bill Evans!'],
 'former','以前的；先前的','修饰 student，指以前的学生，不是国籍已发生变化','A former student returned to visit the department.',['a former student','a former colleague'],
 '随后他解释，另一位以前的日本学生，最喜欢的音乐家也是 Bill Evans！')

add(50,'主旨','What memory contrast introduces the dorm-room example?',
 ['Many study-abroad events remain vivid, unlike numerous conversations from the same period in Tokyo.','The author remembers every Tokyo conversation but nothing from abroad.','Only conversations about music are remembered from either country.','All memories of his roommate Mike have disappeared.'],0,
 '宿舍例子前，作者先作了什么记忆对比？',['许多留学事件仍清晰，而同期在东京的许多谈话已记不清。','东京每次谈话都记得，国外一件事也不记得。','两个国家都只记得音乐谈话。','与室友 Mike 有关的记忆全部消失。'],
 ['A don’t remember many 对照 still vivid，正是例子引出的对比。','B 把两地的记忆状态倒置，并扩大为每次与全无。','C 本段没有 only music，下一例是接电话。','D 作者正举出与 Mike 同住和接电话的清晰记忆。'],
 ['I don’t remember many conversations I had in Tokyo','many things that happened during my study abroad are still vivid in my memory.'],
 'vivid','鲜明的；清晰如在眼前的','形容多年后留学记忆的鲜明程度，不保证每个细节绝对准确','She has vivid memories of her first day in the city.',['a vivid memory','remain vivid'],
 '那段时期，在东京与教授、院长甚至朋友的许多谈话，我都记不清了。但留学期间发生的许多事情，仍在记忆中鲜明如昨。例如，我与一位叫 Mike 的学生同住宿舍。我常接起电话，听到：“Mike 在吗？”')

assert len(out)==50 and [q['id'] for q in out]==[t['questionId'] for t in targets]

def persist():
 path=ROOT/'source/short-questions/additional.json';existing=load('source/short-questions/additional.json');byid={q['id']:q for q in existing}
 for q in out:
  if q['id'] in byid:assert byid[q['id']]==q,('Refuse to overwrite changed authoring',q['id'])
  else:existing.append(q)
 path.write_text(json.dumps(existing,ensure_ascii=False,indent=2)+'\n',encoding='utf8',newline='\n')
 review=dict(batchId='batch-012',date='2026-10-22',pdfSha256=b['pdfSha256'],checkedPdfPages=list(range(41,50)),questionIds=[q['id'] for q in out],paragraphs=[dict(id=pid,textSha256=hashlib.sha256(pp[pid]['text'].encode()).hexdigest()) for pid in dict.fromkeys(q['paragraphId'] for q in out)],note='完整 PDF 原页视觉复核，包括跨页引语；个案、焦点小组、日记自报与诗歌引例分别说明，候选句界不冒充人工最终分句。')
 (ROOT/'source/short-questions/review-chapter04-05-next50.json').write_text(json.dumps(review,ensure_ascii=False,indent=2)+'\n',encoding='utf8',newline='\n')
 print('Saved',len(out),'of 50 individually authored exercises')

if __name__=='__main__':persist()
