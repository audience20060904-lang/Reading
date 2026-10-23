"""25 individually authored exercises for frozen targets, PDF pages 122-126.
Preserve printed English, source positions and all previously published questions.
"""
from pathlib import Path
import json,hashlib
ROOT=Path(__file__).resolve().parents[2]
load=lambda p:json.loads((ROOT/p).read_text(encoding='utf8'))
b=load('public/data/book.json');plan=load('public/data/reading-plan.json');targets=load('source/short-questions/batch031-targets.json')['targets']
ss={s['id']:s for s in b['sentences']};pp={p['id']:p for p in b['paragraphs']};out=[]
def add(i,kind,prompt,options,answer,prompt_zh,options_zh,analyses,quotes,word,meaning,context,example,collocations,translation,support='explicit'):
 t=targets[i-1];u=next(u for u in plan['units'] if u['id']==t['readingUnitId']);group=[ss[sid] for sid in u['sentenceIds']];p=pp[u['paragraphId']];text=p['text'][group[0]['start']:group[-1]['end']]
 assert hashlib.sha256(text.encode()).hexdigest()==t['passageSha256'];evidence=[]
 for quote in quotes:
  offset=text.find(quote);assert offset>=0,(i,quote);start=group[0]['start']+offset;end=start+len(quote);touching=[s for s in group if s['start']<end and s['end']>start]
  evidence.append(dict(quote=quote,sentenceIds=[s['id'] for s in touching],sources=list({(r['pdfPage'],r['block']):r for s in touching for r in s['sources']}.values())))
 assert word.lower() in text.lower(),(i,word)
 out.append(dict(id=t['questionId'],version=1,readingUnitId=u['id'],chapterId=u['chapterId'],sectionId=u['sectionId'],paragraphId=u['paragraphId'],sentenceIds=u['sentenceIds'],passage=text,prompt=prompt,options=options,answer=answer,type=kind,promptZh=prompt_zh,optionsZh=options_zh,analyses=analyses,evidence=evidence,vocabulary=[dict(word=word,meaning=meaning,context=context,example=example,collocations=collocations)],translation=translation,support=support,editorialStatus='完整PDF122–126原页视觉核对与跨页拼接。Nietzsche病痛回忆为个人归因且保留potential，非医疗试验；Kahneman论文4851为书载2022单年引用非今日累计，SS遭遇为其回忆不臆测照片身份或士兵内心、不美化纳粹迫害。严格区分本人interesting与作者psychologically rich；有意义/幸福非全称。Sandy触电按幸存者叙事译触电不误作死亡；37天住院/36年独立/500美元用途分开。Katrina迁移及2006返回与2018回顾分开，bomb/veil是比喻；幸存者纽带反思与灾难伤害并存，不作人人净获益保证。保留引语跨单元和原句指纹，不宣称逐句直接证据全覆盖。'))







add(1,'细节','To what did Nietzsche attribute his insights here?',
 ['His illness.','A new collection of survey data.','His appointment to every university.','The number of essays sold.'],0,
 'Nietzsche 在此将洞见归于什么？',['自己的疾病。','新调查资料。','受聘所有大学。','文章销量。'],
 ['A credited his illness 直接支持，是本人归因。','B 未报告调查。','C 没有所有大学任职。','D 标题为幽默例子，未提销量。不能把个人归因当疾病普遍有益的实验证明。'],
 ['Nietzsche credited his illness.'],
 'credited','将……归功于','表示 Nietzsche 对洞见来源的解释','She credited the experience with changing her perspective.',['credit an experience','credit illness as a source'],
 'Nietzsche 给文章取了幽默标题：《我为何如此智慧》《我为何如此聪明》《我为何写出如此好书》。他很有趣。为何有这么多洞见？Nietzsche 归功于自己的疾病。')

add(2,'逻辑关系','What opportunity did the prolonged illness provide in this account?',
 ['It made him accept an appointment in 1876.','It prevented every change in routine.','It allowed a complete change of habits and distance from conventions.','It proved that philology was unrelated to languages.'],2,
 '长期疾病在叙述中提供什么机会？',['使他于1876年接受任命。','阻止一切习惯变化。','让他彻底改变习惯、脱离惯常规范。','证明语文学不研究语言。'],
 ['A 任命是1869年，1876年因病请假。','B gave...change habits 与此相反。','C 末两句直接支持；个人传记不作所有患者因果保证。','D 括号明确语文学研究语言历史。'],
 ['This prolonged illness gave him a chance to change his habits completely. It helped him detach himself from typical conventions.'],
 'prolonged','持续很久的；长期的','修饰疾病持续状态，而非病情严重程度的量化','The prolonged interruption changed his routine.',['prolonged illness','a prolonged period'],
 '1869年，二十四岁的他获任 Basel University 古典语文学（研究语言历史）教席，是该职位最年轻任职者。1876年疾病迫使他请假。长久患病给他彻底改变习惯的机会，帮助他脱离惯常规范。')

add(3,'同义改写','What change in activity does Nietzsche’s recollection describe?',
 ['He increased reading while giving up reflection.','He conducted a clinical trial on happiness.','He resumed teaching without any rest.','He stopped reading and made room for thinking.'],3,
 'Nietzsche 回忆描述什么活动变化？',['增读而不思考。','开展幸福临床试验。','不休息就复教。','停止阅读，为思考留空间。'],
 ['A 原文 stopped reading and started thinking 正相反。','B 回忆与个人感受，不是试验。','C lying still/leisure/waiting 都强调静养。','D 活动变化有明文支持；自称痛苦时期最满意自己，不能外推患者幸福规律。'],
 ['In his sickness, he stopped reading and started thinking.'],
 'bestowed','给予；赋予','他以较庄重措辞说疾病带来静养的必要性','The pause bestowed an unexpected chance for reflection.',['bestow on someone','bestow a necessity'],
 '他后来回忆，疾病允许、命令他忘却，赋予他静卧、闲暇、等待与耐心的必要，而这意味着思考。病中他停止阅读，开始思考。回望人生，他说自己从未比在最病痛时期更满意自己。')

add(4,'推断','How does the author qualify the link between adversity and richness?',
 ['Adversity guarantees wisdom for everyone.','Adversity has the potential to produce psychological richness.','Only illness can ever change perspectives.','Nietzsche’s account is presented as a controlled experiment.'],1,
 '作者怎样限定逆境与丰富的联系？',['保证人人智慧。','有潜力产生心理丰富。','只有疾病能变视角。','当作受控实验。'],
 ['A potential 是潜力，不是保证。','B 最后 suggesting...potential 精确保留限定。','C 个人来源不能改成唯一途径。','D 是个人引用及作者阐释，不是试验。正反视角切换不表示否认痛苦。'],
 ['adversity has the potential to generate psychological richness.'],
 'conversely','反过来；相反地','从病者看健康，也反过来从充盈人生看衰颓','He considered the problem and, conversely, its opposite perspective.',['and conversely','reverse perspectives'],
 '病中，他觉得回到自然的自我。他描述从病者视角看较健康的概念与价值，又反过来从丰富人生的充盈自信看衰颓本能的隐秘运作，终于知道如何颠倒视角。他将疾病视为视角变化和智慧来源，提示逆境有产生心理丰富的潜力。')

add(5,'主旨','How is the influence of Kahneman’s work characterized?',
 ['It changed thinking in both psychology and economics.','It affected only his own autobiography.','It removed rationality from every economic model.','It was limited to papers published in 2002.'],0,
 '怎样概括 Kahneman 研究的影响？',['改变心理学和经济学的思考。','只影响个人自传。','从所有经济模型移除理性。','只限2002年论文。'],
 ['A not just...but also 指认知与经济理性两领域。','B 本段讨论学术贡献。','C changed how...think 不等于所有模型一律删除。','D 2002是获奖年，论文系列在1970和1980年代。'],
 ['changed not just how psychologists think about human cognition, but also how economists think about rationality'],
 'foundational','基础性的；奠基性的','理性被说成现代经济学许多理论的基础假设','The paper challenged a foundational assumption.',['foundational assumption','foundational contributions'],
 'Daniel Kahneman 获2002年诺贝尔经济学奖。他与 Amos Tversky 在1970和1980年代发表系列有影响论文，成为世界最杰出心理学家之一。论文不只改变心理学家对认知的思考，也改变经济学家对理性的思考，理性是许多现代经济学的基础假设。')

add(6,'细节','What does the figure 4,851 refer to?',
 ['The number of heuristics identified in 1974.','All citations accumulated only before 1980.','Papers published in 2022 that cited the 1974 Science paper.','The participants in the original 1974 experiment.'],2,
 '4,851 这个数字指什么？',['1974发现的启发式数量。','1980前全部引文。','2022年发表且引用1974年Science论文的文献数。','原实验被试数。'],
 ['A 启发式列三种。','B in 2022 alone 限定单年而非此前累计。','C 括号明确数字、年份和被引论文。','D 是文献数非受试人数；不更新为今日实时引用量。'],
 ['This 1974 Science paper was cited by 4,851 papers published in 2022 alone'],
 'enduring','持久的；长久存在的','后来的引用说明学术影响延续','The review highlighted the theory’s enduring influence.',['enduring influence','an enduring contribution'],
 '例如，在广被引用的1974年论文中，两人描述代表性、可得性、锚定与调整三种启发式，各激发数千后续论文。仅2022年发表的文献中，就有4,851篇引用这篇1974年Science论文，表明其持久影响。')

add(7,'作者意图','What shift does “not just a Nobel laureate” introduce?',
 ['A rejection of his academic work.','A claim that he never experienced danger.','A complete account of the quoted incident within this short passage.','A move from scholarly honors to an extraordinary personal history.'],3,
 'not just a Nobel laureate 引入什么转向？',['否定学术工作。','称从没危险经历。','当前短段已完整讲完事件。','从学术荣誉转向非凡个人经历。'],
 ['A not just 是补充维度，不是否定。','B 逃离纳粹占领及scary表明危险。','C 回忆在引语日期处中断，后续短段继续。','D personal story 明确引向童年回忆；书中给出死亡年份年龄，保留来源不假装新查资料。'],
 ['was not just a Nobel laureate. He had an extraordinary personal story.'],
 'laureate','获奖者','Nobel laureate 指诺贝尔奖得主','The laureate also described a difficult childhood.',['Nobel laureate','a distinguished laureate'],
 '但2024年九十岁去世的 Kahneman 不只是诺奖得主。他有非凡个人故事，七岁时逃离纳粹占领的Paris。诺奖传记中他回忆一段惊险事件：“应该是1941年底或1942年初。（引语续后段）')

add(8,'细节','What circumstances made the walk home precarious?',
 ['He was returning before the curfew with official permission.','He had stayed out late under rules requiring a star and a 6 p.m. curfew.','He had forgotten which city he lived in.','He was required to stay with his friend all night.'],1,
 '什么使回家路上处境危险？',['宵禁前获准返回。','在被迫戴星标且六点宵禁下玩得太晚。','忘记所住城市。','被要求整夜留朋友家。'],
 ['A stayed too late 不支持按时获准。','B 两项强制规则加逗留过晚构成背景。','C 无遗忘城市。','D 没有这项要求。inside out 是翻到反面；本段未明说动机，后段才提内侧星标，不把推测冒充此句明示。'],
 ['Jews were required to wear the Star of David and to obey a 6 p.m. curfew.','had stayed too late.'],
 'curfew','宵禁','这里是纳粹占领时期针对犹太人的强制限制','The memoir describes a strictly enforced curfew.',['obey a curfew','a 6 p.m. curfew'],
 '“犹太人被要求佩戴大卫之星，并遵守下午六点宵禁。我去和一位基督徒朋友玩，逗留太晚。我把棕色毛衣翻面，走几个街区回家。”')

add(9,'细节','Which action follows the soldier’s intense look in the recollection?',
 ['He beckoned the child over, picked him up and hugged him.','He immediately inspected every garment.','He gave directions and walked away without contact.','He invited the entire family to his home.'],0,
 '回忆中士兵注视之后做什么？',['招孩子过来，抱起并拥抱。','立即检查全部衣物。','指路后无接触离开。','邀请全家去家里。'],
 ['A Then...beckoned...picked...hugged 顺序直接支持。','B 原文没有检查行为。','C 有身体接触。','D 没有家属邀请。黑色SS制服解释孩子恐惧，不由单个遭遇粉饰纳粹迫害或臆测士兵内心。'],
 ['Then he beckoned me over, picked me up, and hugged me.'],
 'beckoned','招手示意','示意孩子靠近，非挥手让离开','The visitor beckoned the child over.',['beckon someone over','look intently'],
 '“走在空街上时，我看见一名德国士兵走来。他穿着我被告知最该害怕的黑制服——特招SS士兵的制服。我想快走，靠近时发现他紧盯着我。然后他招我过去，抱起我并拥抱。”')

add(10,'语境词义','What does “a close call” suggest about the episode?',
 ['An ordinary telephone conversation.','A meeting that was planned in advance.','A narrowly avoided danger.','An event without any perceived risk.'],2,
 'a close call 在此暗示什么？',['普通电话。','提前计划会面。','险些出事的遭遇。','没有任何感知风险。'],
 ['A 不是电话含义。','B 事件非预先安排。','C terrified...notice star 后能离开，作者以险情概括。','D 明说terrified。男孩照片和给钱是所述动作，未说明照片中男孩身份，也未说明士兵看见星标。'],
 ['I was terrified that he would notice the star inside my sweater.','It was a close call.'],
 'close call','险些发生危险的事；侥幸脱险','指担心身份被发现的惊险经历，不是通话','The memoir describes the escape as a close call.',['a close call','have a close call'],
 '“我吓坏了，怕他发现毛衣内侧的星标。他用德语激动地讲话。把我放下时，他打开钱包，给我看男孩照片，并给一些钱。”这是一次险些出事的遭遇。')

add(11,'细节','Whom did Kahneman credit with inspiring his career?',
 ['The soldier’s son, whose identity is established here.','His mother.','The author of this book.','A teacher who organized the encounter.'],1,
 'Kahneman 将职业启发归于谁？',['本段已确定身份的士兵儿子。','母亲。','本书作者。','安排遭遇的教师。'],
 ['A 照片男孩身份未证实，此段没这种归因。','B He credited his mother 明示。','C 不是作者。','D 无教师安排。人的复杂有趣是本人回忆结论，不能由此美化迫害环境。'],
 ['He credited his mother for inspiring him to become a psychologist.'],
 'inspiring','启发；激励','母亲对他理解人及职业选择的影响','Her questions were inspiring to the young researcher.',['inspire someone to become','inspire curiosity'],
 'Kahneman 继续说：“回家时，我比以往更确信母亲对了：人无穷地复杂且有趣。”他将成为心理学家的启发归功于母亲。')

add(12,'细节','Why was Kahneman’s father released from Drancy in this account?',
 ['The whole family had already moved to Palestine.','His father had completed a university degree.','The war had ended before his detention.','His employer intervened.'],3,
 '叙述中父亲为何获释离开Drancy？',['全家已迁Palestine。','已拿大学学位。','关押前战争已结束。','雇主出面干预。'],
 ['A 迁Palestine在战后且父亲已去世。','B 没有相关学位原因。','C 当时战争和逃亡仍在继续。','D However...employer intervened...released 明示原因；原定送灭绝营不等于实际已送到。'],
 ['his employer intervened, and he was released.'],
 'intervened','介入；干预','雇主出面改变拘禁结果，不补写未知具体手段','The employer intervened on the worker’s behalf.',['intervene on behalf of','an employer intervened'],
 'Kahneman 父亲被拘禁Drancy，原定送往灭绝营。但雇主干预，使他获释。全家逃到Vichy，德国人到来后再逃法国中部。父亲1944年去世；战后家人迁到Palestine。')

add(13,'主旨','What does the list of subjects emphasize about Kahneman?',
 ['He pursued a wide range of intellectual interests before the famous collaboration.','He studied only cognitive biases throughout his life.','Every listed subject was a military assignment.','He began graduate work before serving in the army.'],0,
 '学科清单强调什么？',['著名合作之前已广泛涉猎。','毕生只研究认知偏误。','所列全部是军队任务。','军队服役前已开始研究生工作。'],
 ['A Many different...eclectic mix 加合作前诸领域显示广泛兴趣。','B 忽略多个主题。','C 服役与学术兴趣不是全等。','D before starting graduate work 明确先后相反。'],
 ['Many different subjects interested him, so he studied an eclectic mix of topics'],
 'eclectic','兼收并蓄的；多元选取的','研究主题跨感知、人格与哲学等领域','The course offered an eclectic mix of topics.',['an eclectic mix','eclectic interests'],
 '他毕业于Hebrew University，在以军先任排长一年，再于国防军心理部门任军官一年，之后去UC Berkeley读研。兴趣广泛，涉猎潜意识知觉、光学平台、人格评估、Wittgenstein与科学哲学。与Tversky开始认知偏误著名合作前，他已研究精神分析、记忆、视觉和动机。')

add(14,'细节','What research sequence followed the collaboration with Tversky?',
 ['He abandoned all scholarship immediately.','Life satisfaction came before any work on pleasure and pain.','He studied pleasure and pain, followed by happiness and life satisfaction.','He returned exclusively to classical philology.'],2,
 '与Tversky合作之后的研究顺序是什么？',['立刻放弃学术。','满意度先于快乐痛苦。','先快乐痛苦，再幸福与生活满意度。','只回到古典语文学。'],
 ['A made foundational contributions 表示继续贡献。','B then 给出相反先后。','C 单句直接支持顺序。','D 古典语文学是前文Nietzsche领域，不应错配人物。'],
 ['study pleasure and pain, then happiness and life satisfaction'],
 'foundational','奠基性的','对后续领域发展有基础作用的贡献','The project made a foundational contribution to the field.',['foundational contributions','at each stop'],
 '与Tversky的合作结束后，Kahneman 接着研究快乐和痛苦，再研究幸福与生活满意度，在每一站都作出奠基性贡献。')

add(15,'作者意图','What expectation does “Wrong” overturn?',
 ['That Kahneman had never contributed to society.','That he would describe his own life as extremely meaningful because of his contributions.','That the interview occurred in 2018.','That Seligman had ever discussed meaning with him.'],1,
 'Wrong 推翻什么预期？',['从未贡献社会。','贡献多，所以本人会称人生极有意义。','访谈发生于2018。','从未与Seligman讨论意义。'],
 ['A 开头承认diverse contributions。','B you might expect 后的自我评价被否定，不能用外部荣誉代替本人体验。','C 无否定访谈年份。','D 引语正回忆该谈话。当前句引语未完，下段继续本人坚持的措辞。'],
 ['you might expect Kahneman to think his life was extremely meaningful, right? Wrong.'],
 'characterize','将……描述为；刻画','本人用何种词描述人生，不等于客观判定人生无价值','She did not characterize the period as wholly happy.',['characterize a life as','didn’t characterize'],
 '他作为军队领导者、教师、学者对社会贡献多样，你也许以为他会觉得人生极有意义吧？错了。他并不把人生描述为有意义。2018访谈中他说，曾与积极心理学创始人Martin Seligman谈话，对方试图说服他人生有意义。（引语续后段）')

add(16,'细节','Which description did Kahneman insist on for his life?',
 ['Meaningful in exactly Seligman’s sense.','Entirely miserable without interest.','Uninteresting but financially secure.','Interesting.'],3,
 'Kahneman 坚持怎样形容自己人生？',['完全按Seligman所说的有意义。','全然悲惨毫无趣味。','无趣但经济安全。','有趣。'],
 ['A 他对Meaningful称不理解，并非接受。','B 本句强调interesting。','C 无经济安全对比。','D insisted...interesting 直接支持。不能把不理解一个标签改成自认毫无价值。'],
 ['I had an interesting life.'],
 'insisted','坚持说；坚持主张','坚持自己的用词，而不是接受他人替代标签','He insisted that interesting was the better description.',['insist that','insist on a description'],
 '“我坚持说，而且今天仍这么想：我的人生有趣。‘有意义’不是我理解的东西。”')

add(17,'细节','What example undermines the idea that his life was wholly happy?',
 ['He described four years of writing alone as terrible and miserable.','He said every stage of research was pleasant.','He never experienced any ups and downs.','Winning the Nobel Prize prevented all suffering.'],0,
 '什么例子否定人生全然幸福的说法？',['独自写书四年被形容糟糕痛苦。','每个研究阶段都愉快。','没任何起伏。','诺奖阻止全部苦难。'],
 ['A 引语four years...terrible...miserable 明示。','B 没说每阶段愉快。','C many ups and downs 正相反。','D 荣誉与痛苦并存，非免疫痛苦。非wholly happy也不等于从未快乐。'],
 ['There were four years when I worked alone on a book. That was terrible, and I was miserable.'],
 'wholly','完全地；全然地','否定全然幸福，保留人生好坏起伏','The experience was not wholly pleasant.',['wholly happy','not wholly'],
 'Kahneman 也不觉得人生全然幸福。同次访谈他说：“有四年我独自写一本书，糟透了，我很痛苦。”他逃离纳粹占领的Paris，二战中逃亡三四年，后来又获诺奖，人生起伏很多。')

add(18,'细节','Who applies the label “psychologically rich” in this sentence?',
 ['Kahneman quotes Seligman’s exact diagnosis.','The author, interpreting Kahneman’s description of an interesting life.','The soldier in the childhood account.','An unnamed clinical committee.'],1,
 '此句由谁使用心理丰富标签？',['Kahneman逐字引用Seligman诊断。','作者解释Kahneman所说的有趣人生。','童年故事的士兵。','无名临床委员会。'],
 ['A 既非诊断也未说逐字引用。','B He said...interesting 与 I would call... 清楚区分本人用词和作者归类。','C 该士兵无此表述。','D 无委员会。不能误写为Kahneman自称心理丰富。'],
 ['He said his life was best described as “interesting”; I would call it psychologically rich.'],
 'described','描述的；形容的','两个说话者选用不同描述词，关注归属','The author described the life as rich in experience.',['best described as','call it psychologically rich'],
 '他说，人生最好用“有趣”描述；我会称之为心理丰富。')

add(19,'细节','What was Fujimoto trying to do when he was injured?',
 ['Repair the roof after leaving his apartment.','Buy a winter jacket at a store.','Unplug cords as water entered the apartment.','Call the ambulance for his landlord.'],2,
 'Fujimoto受伤时正试图做什么？',['离公寓后修屋顶。','去店买冬装。','水进入公寓时拔电线。','替房东叫救护车。'],
 ['A 无屋顶维修。','B 冬装援助为后续，不是受伤动作。','C tried to unplug...electrocuted 明示；此处译触电，不武断译当场死亡。','D 救护车由房东次日呼叫，当前短段尚未述此结果。'],
 ['When he tried to unplug the cords, he was electrocuted.'],
 'gush','涌出；猛冲入','洪水大量进入地下公寓','Water began to gush into the room.',['gush into an apartment','water began to gush'],
 '2012年10月29日Hurricane Sandy袭击New York City。六十四岁的Takashi Fujimoto独居Staten Island地下公寓。正用摄影灯光设备时，水猛涌入房。他试图拔掉电线时触电。')

add(20,'细节','Which sequence matches the rescue account?',
 ['An ambulance found him before the storm began.','His landlord hospitalized him for three days.','He rescued his landlord and immediately recovered.','His landlord found him the next morning, and he spent thirty-seven days in hospital.'],3,
 '哪项顺序符合救援叙述？',['风暴前救护车找到他。','房东令他住院三天。','他救房东后立刻痊愈。','次晨房东发现，之后住院三十七天。'],
 ['A 是风暴水淹后次晨。','B thirty-seven 非three，房东负责呼叫救护车不是治疗。','C 主客体反转且无即刻恢复。','D 时间、人物和住院长度均匹配；不添加医学处置细节。'],
 ['The next morning, his landlord found him','hospitalized for the next thirty-seven days'],
 'consciousness','意识；清醒状态','时而清醒时而昏迷，不是整夜持续清醒','He drifted in and out of consciousness.',['in and out of consciousness','regain consciousness'],
 '他整夜在淹水公寓中时而清醒、时而昏迷。次晨房东在积水里发现他，叫救护车。他因中风与烧伤住院三十七天。多数财物损毁。')

add(21,'细节','What assistance is explicitly described?',
 ['A $500 grant for winter clothing and shoes.','A new apartment purchased for him.','A promise that all future medical costs would be covered.','Replacement of every damaged possession.'],0,
 '明确描述了什么援助？',['五百美元补助买冬装鞋子。','买下一间新公寓。','承诺所有未来医疗费。','替换全部损坏物品。'],
 ['A grant/500/winter jacket/clothes/shoes 都有明文。','B 没有赠公寓。','C 没有医疗费保证。','D 具体补助不能扩大成全财物赔偿。后面是报纸转述的本人感受，不能作全体受灾者统计。'],
 ['Catholic Charities provided him with a $500 grant to buy a winter jacket, clothes, and shoes.'],
 'misty-eyed','泪眼朦胧的；眼眶湿润的','谈帮助恢复的人时动情的描述','He became misty-eyed while thanking the volunteers.',['become misty-eyed','talk about those who helped'],
 '但Catholic Charities给他五百美元补助，买冬夹克、衣服和鞋。按The New York Times转述，谈到灾后帮助他恢复的人时，他泪眼朦胧，说这改变了他整个人生的视角。')

add(22,'逻辑关系','How does the passage characterize Fujimoto’s changed outlook?',
 ['He had intentionally planned the near-death experience.','He concluded that community had no value.','A terrible involuntary experience reaffirmed his belief in community.','He denied that anything about him had changed.'],2,
 '片段怎样描述他改变的看法？',['主动计划濒死遭遇。','得出社区没价值。','可怕且非主动的遭遇重新坚定社区信念。','否认自己有变化。'],
 ['A far from intentional 明确非主动。','B reaffirmed 不是否定。','C terrible 与社区信念并列，不抹去伤害。','D changed him 明说改变。仍住同公寓是此人行为，非建议其他灾民重复危险处境。'],
 ['It was terrible, but it reaffirmed his belief in community'],
 'reaffirmed','再次确认；重新坚定','经历支持他对社区的信念，而不意味伤害不重要','The support reaffirmed her belief in community.',['reaffirm a belief','reaffirm belief in community'],
 '他经历Sandy远非主动选择。虽为此前独立生活三十六年自豪，濒死经历仍改变了他。这很可怕，却重新坚定社区信念，以至后来仍留同一地下公寓，与原房东和邻居为伴。')

add(23,'细节','Which relocation sequence is described for Joe and Jordan?',
 ['New Orleans, then directly back from Atlanta in 2018.','Atlanta, then Washington D.C., then New Orleans in January 2006.','Washington D.C., then Atlanta, with no return.','They remained in New Orleans throughout.'],1,
 'Joe和Jordan经历什么迁移顺序？',['Atlanta直接于2018返城。','先Atlanta，再Washington D.C.，2006年1月回New Orleans。','先D.C.再Atlanta，没返城。','始终留原城。'],
 ['A 2018是十三年后回顾，不是返回年份。','B first/then/January2006 精确对应。','C 顺序相反且漏返回。','D evacuated 明说离开。开头两城恢复速度是作者比较，非据此断言所有居民恢复等快。'],
 ['They evacuated to Atlanta first, then to Washington D.C. In January 2006, they returned to New Orleans.'],
 'evacuated','撤离；疏散','因灾暂时离开原城市，不等于决定永不返回','The family evacuated to another city.',['evacuate to','return after evacuation'],
 'New York City从Sandy恢复较快，而New Orleans在Katrina后苦撑多年。2018年，Joe Bridges与儿子Jordan回顾十三年前飓风影响。他们先撤到Atlanta，再到Washington D.C.，2006年1月回New Orleans。Joe说，原住一切漂亮的D.C.，回来让他有些无所适从。（引语续后段）')

add(24,'逻辑关系','What contrast is introduced by “Despite the long-lasting damage”?',
 ['Jordan said every abandoned home had been repaired.','Joe preferred destruction to the beauty of D.C.','The storm’s impact had disappeared by 2018.','Persistent visible damage coexisted with Jordan’s positive judgment of the city.'],3,
 'Despite long-lasting damage 引入什么对照？',['Jordan说所有废屋已修复。','Joe偏好破坏胜过D.C.美景。','2018年影响已消失。','可见长期损害与Jordan对城市的积极评价并存。'],
 ['A still see abandoned homes 相反。','B Joe描述冲击，未说偏好破坏。','C veil仍覆盖城市，非消失。','D Despite连接损害和I think...better city，后者是Jordan看法，非全城客观净收益测量。bomb是比喻，不改成真实轰炸事件。'],
 ['Despite the long-lasting damage, Jordan said, “I think we’re a better city because of it.'],
 'veil','面纱；笼罩的阴影','Jordan以比喻形容风暴影响持续笼罩城市','The memory cast a veil over the neighborhood.',['a veil covering a city','long-lasting damage'],
 '“那里很好。回到New Orleans，却像炸弹炸过。”2018年Jordan仍看见Katrina留下的废屋，称风暴是一层仍罩城市的面纱。尽管损害长久，他说：“我觉得因为它，我们城市更好了。（引语续后段）')

add(25,'推断','What should be preserved when interpreting the claim of stronger bonds?',
 ['It is a survivor’s account of closeness alongside explicit acknowledgment of widespread devastation.','It proves the hurricanes benefited every resident overall.','The author denies any destruction occurred.','It establishes that all relationships last forever as a measured fact.'],0,
 '理解纽带更强时应保留什么？',['幸存者讲亲近，同时明确承认广泛毁坏。','证明飓风使每人总体受益。','作者否认破坏。','实测确立所有关系永存。'],
 ['A 引语说关系长久，随后作者强调destroyed many lives，两面都须保留。','B 个体反思不能推广为人人净获益。','C 最后一句明确毁坏。','D gonna last forever 是受访者感情表达，不是长期测量定律。本段开头延续Jordan引语。'],
 ['Those bonds, you know, those are the things that are gonna last forever.”','Hurricanes Katrina and Sandy destroyed many people’s lives.'],
 'closer knit','关系更紧密的','受访者感受到亲友群体纽带增强，不代表所有居民','The volunteers became a closer knit group.',['a closer knit community','closer knit bonds'],
 '“更坚强，联系更紧密。与亲友经历Katrina这样重大的事，那些纽带，你知道，会永远延续。”Katrina和Sandy摧毁了许多人的生活。')

assert len(out)==25 and [q['id'] for q in out]==[t['questionId'] for t in targets]

def persist():
 path=ROOT/'source/short-questions/additional.json';existing=load('source/short-questions/additional.json');byid={q['id']:q for q in existing}
 for q in out:
  if q['id'] in byid:assert byid[q['id']]==q,('Refuse to overwrite changed authoring',q['id'])
  else:existing.append(q)
 path.write_text(json.dumps(existing,ensure_ascii=False,indent=2)+'\n',encoding='utf8',newline='\n')
 review=dict(batchId='batch-031',date='2026-10-23',pdfSha256=b['pdfSha256'],checkedPdfPages=list(range(122,127)),questionIds=[q['id'] for q in out],paragraphs=[dict(id=pid,textSha256=hashlib.sha256(pp[pid]['text'].encode()).hexdigest()) for pid in dict.fromkeys(q['paragraphId'] for q in out)],note='完整PDF122–126原页视觉核对与跨页拼接。Nietzsche病痛回忆为个人归因且保留potential，非医疗试验；Kahneman论文4851为书载2022单年引用非今日累计，SS遭遇为其回忆不臆测照片身份或士兵内心、不美化纳粹迫害。严格区分本人interesting与作者psychologically rich；有意义/幸福非全称。Sandy触电按幸存者叙事译触电不误作死亡；37天住院/36年独立/500美元用途分开。Katrina迁移及2006返回与2018回顾分开，bomb/veil是比喻；幸存者纽带反思与灾难伤害并存，不作人人净获益保证。保留引语跨单元和原句指纹，不宣称逐句直接证据全覆盖。')
 (ROOT/'source/short-questions/review-chapter11-adversity25.json').write_text(json.dumps(review,ensure_ascii=False,indent=2)+'\n',encoding='utf8',newline='\n')
 print('Saved',len(out),'of 25 individually authored exercises')

if __name__=='__main__':persist()
