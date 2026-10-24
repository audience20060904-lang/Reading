"""25 individually authored exercises for frozen targets, PDF pages 151-155.
Preserve printed English, source positions and all previously published questions.
"""
from pathlib import Path
import json,hashlib
ROOT=Path(__file__).resolve().parents[2]
load=lambda p:json.loads((ROOT/p).read_text(encoding='utf8'))
b=load('public/data/book.json');plan=load('public/data/reading-plan.json');targets=load('source/short-questions/batch038-targets.json')['targets']
ss={s['id']:s for s in b['sentences']};pp={p['id']:p for p in b['paragraphs']};out=[]
def add(i,kind,prompt,options,answer,prompt_zh,options_zh,analyses,quotes,word,meaning,context,example,collocations,translation,support='explicit'):
 t=targets[i-1];u=next(u for u in plan['units'] if u['id']==t['readingUnitId']);group=[ss[sid] for sid in u['sentenceIds']];p=pp[u['paragraphId']];text=p['text'][group[0]['start']:group[-1]['end']]
 assert hashlib.sha256(text.encode()).hexdigest()==t['passageSha256'];evidence=[]
 for quote in quotes:
  offset=text.find(quote);assert offset>=0,(i,quote);start=group[0]['start']+offset;end=start+len(quote);touching=[s for s in group if s['start']<end and s['end']>start]
  evidence.append(dict(quote=quote,sentenceIds=[s['id'] for s in touching],sources=list({(r['pdfPage'],r['block']):r for s in touching for r in s['sources']}.values())))
 assert word.lower() in text.lower(),(i,word)
 out.append(dict(id=t['questionId'],version=1,readingUnitId=u['id'],chapterId=u['chapterId'],sectionId=u['sectionId'],paragraphId=u['paragraphId'],sentenceIds=u['sentenceIds'],passage=text,prompt=prompt,options=options,answer=answer,type=kind,promptZh=prompt_zh,optionsZh=options_zh,analyses=analyses,evidence=evidence,vocabulary=[dict(word=word,meaning=meaning,context=context,example=example,collocations=collocations)],translation=translation,support=support,editorialStatus='完整PDF151–155原页视觉核对。Fincham研究明确随机组、四周每天至少一次为伴侣祈祷，控制组回想当日活动，结果自报；less likely非零不忠，holy是felt非宗教真理证明。B历史/音乐比喻归哲学角色，育儿例子不作无子女无情谊。万圣节事故细节作者省略不补造。Aron新奇任务路线/枕头约束与轮流滚球控制分开；63对为复现新样本，后续讨论亲爱动作是行为结果。40%自报十年以上婚姻属另一研究线，不混63对或影像样本；21.4是平均年限，激活奖励相关脑区不等于直接测同量多巴胺。self-expansion为理论，due in part/could非唯一因果保证；夫妻旅行采访非随机研究。Jiro例子锚定2011纪录片当时年龄与书载星级，顾客seemed非盲法试吃；30至45分钟、九岁离家40岁开店、十年清洁/200次个案不推广硬规则。私人/公开竞技是作者解释比较，不当临床证明或人物今日健康断言。额外章首正文及辅助材料源文审计仍开放，不宣称全书完整覆盖。'))







add(1,'细节','Which feature of Fincham’s study is explicitly stated?',
 ['Participants in exclusive romantic relationships were recruited, and one group was randomly assigned to prayer.','Only people without a current partner were recruited.','All participants chose their own condition according to their beliefs.','The study compared married couples with people who had never dated.'],0,
 'Fincham研究明确写了哪项特征？',['招募正处排他恋爱关系者，一组随机分到祈祷条件。','只招没有现任伴侣的人。','所有人按信仰自选组别。','比较已婚者与从未约会者。'],
 ['A currently...exclusive及randomly assigned均有直接依据；不能进一步补写样本年龄或信仰限制。','B currently in...relationship否定无伴侣。','C randomly assigned不是人人自选。','D 段中没有这两个招募比较组。作者先问B的主张有何证据，再引入研究，不是把B引文本身当实验。'],
 ['participants who were currently in an exclusive romantic relationship were recruited.','One group of participants was randomly assigned into the prayer condition.'],
 'exclusive','排他的；专一的','这里限定当时的恋爱关系状态，不表示实验已保证之后无人不忠','They described their relationship as exclusive.',['an exclusive romantic relationship','randomly assigned'],
 '有没有证据支持B关于初恋不断更新的主张？Frank Fincham及同事做了一项恋爱关系中关于祈祷的有趣研究。其中一项招募了当时处于排他恋爱关系的参与者。一组参与者被随机分到祈祷条件。')

add(2,'逻辑关系','Which account correctly links the intervention, comparison, and reported result?',
 ['Both groups prayed daily, but only one group reported satisfaction.','The control group prayed, and the prayer group recalled daily activities.','Prayer for a partner was compared with daily reflection on one’s activities; the prayer group reported less infidelity.','The researchers observed every relationship continuously for four years.'],2,
 '哪项正确连接干预、对照与所报告结果？',['两组每日祈祷，仅一组报告满意度。','控制组祈祷，祈祷组回想每日活动。','为伴侣祈祷对比回想每日活动；祈祷组自报不忠较少。','研究者持续观察每段关系四年。'],
 ['A 只有祈祷条件被要求为伴侣祈祷，they all reported指两组都报告结果。','B 把条件任务互换。','C 保留四周干预、日常活动对照与reported测量性质；less likely不能改成无一人不忠。','D four weeks不是四年，reported不是研究者持续监视。文本说报告满意度，但此段不给两组满意度具体结果。'],
 ['pray at least once a day for the well-being of their partner for four weeks.','Four weeks later, they all reported whether they had engaged in infidelity','Those randomly assigned to the prayer condition were less likely to engage in infidelity than those in the control condition.'],
 'infidelity','伴侣关系中的不忠','研究四周后的自报结果之一，不是对所有现实伴侣的指控','The questionnaire asked about infidelity during the study period.',['engage in infidelity','at least once a day'],
 '在这一条件下，他们被要求连续四周，每天至少一次为伴侣的福祉祈祷。另一组则只需每天花些时间，想想自己当天做了什么。四周后，所有人报告是否有过不忠行为，以及关系满意度。被随机分到祈祷条件的人，比控制条件的人更少出现不忠行为。')

add(3,'细节','What additional difference was reported for the prayer condition?',
 ['Participants had all become members of the same religion.','Participants felt their relationship was more holy and sacred.','Participants had objectively better health than the control group.','Participants never experienced any further disagreement.'],1,
 '祈祷条件另报告什么差别？',['全部加入同一宗教。','觉得关系更神圣。','客观健康优于控制组。','之后从无争执。'],
 ['A 没有改宗或统一信仰的测量。','B felt...more holy and sacred直接支持，是对关系的感受比较。','C 本句没测健康。','D 神圣感受不等于未来零争执，也没任何never保证。不要把felt强化为客观宗教真理证明。'],
 ['those in the prayer condition felt that their romantic relationship was more holy and sacred than those in the control condition.'],
 'sacred','神圣的；被尊为不可轻慢的','描述参与者对关系的主观意义评价','They regarded the promise as sacred.',['holy and sacred','feel that a relationship is sacred'],
 '此外，相比控制条件，祈祷条件下的人更觉得自己的恋爱关系神圣。')

add(4,'主旨','According to B, what does marital love possess that first love lacks?',
 ['A complete absence of previous experience.','A prohibition on retelling shared stories.','A guarantee that no hardship will ever occur.','A history built from remembering and assimilating shared experiences.'],3,
 '按B的观点，婚姻之爱有什么是初恋所欠缺的？',['完全没有此前经历。','禁止复述共同故事。','保证永不受苦。','记忆和消化共同经历所形成的历史。'],
 ['A history/remembrance与没有经历相反。','B Couples often tell...same stories正肯定重复叙述。','C tested and purified的哲学表述没保证无苦难。','D element of history及assimilation说明共同经历不断被纳入爱之中。此处是人物B的论述，非已随机验证的结婚效果。'],
 ['the element of history, or the remembrance of shared experiences, is something that marital love has but first love lacks'],
 'assimilation','吸收；同化；融入','将经历吸收进关系的历史，而非生物消化的字面过程','Reflection supported the assimilation of a difficult experience.',['a process of assimilation','shared experiences'],
 '在《Either/Or》中，B还认为，历史这一因素，也就是对共同经历的回忆，是婚姻之爱具备而初恋欠缺的：“婚姻之爱的历史性，显现在它是一个吸收融合的过程；它在经历中试手，再把经历返照自身……爱在这一运动中经受考验、得到净化，并吸收那些经历。”伴侣常会向彼此反复讲同样的故事。')

add(5,'细节','Which division of work is described for the Halloween costume?',
 ['The son made the train, while both parents made a hat together.','The author made the cardboard train, and his wife made the hat.','His wife made the train costume, while he made a chimney-shaped hat.','The family bought both the train and the hat at the university event.'],2,
 '万圣节服装中，父母怎样分工？',['儿子做火车，父母合做帽子。','作者做纸火车，妻子做帽子。','妻子做火车装，作者做烟囱形帽子。','都在大学活动买来。'],
 ['A made的主体是妻子和作者，不是儿子。','B while前后人物任务对换。','C 妻子做纸板Thomas火车装，作者做chimney-shaped hat。','D made不等于购买，活动是穿好后带孩子去参加。three years old是儿子当时年龄，非父母制作服装的时长。'],
 ['My wife made a Thomas costume, a cardboard train decorated with blue felt fabric and yellow and red tape, while I made a chimney-shaped hat.'],
 'felt fabric','毛毡布料','装饰纸板火车的蓝色材料，felt在此非feel的过去式','She covered the cardboard with blue felt fabric.',['felt fabric','a chimney-shaped hat'],
 '妻子与我常复述一段万圣节故事：大儿子三岁时装扮成Thomas the Tank Engine。妻子做了Thomas服装，是一辆用蓝色毛毡及黄、红胶带装饰的纸板火车；我则做了烟囱形帽子。他可爱极了。我们带他参加UVA校园的大型万圣节不给糖就捣蛋活动。')

add(6,'推断','What can be concluded about the “little accident”?',
 ['It interrupted the fun, but its nature is not supplied.','It was definitely a serious injury requiring hospital treatment.','It happened before the family decided to attend the event.','It caused the author to describe every detail at length.'],0,
 '关于little accident能得出什么？',['它打断欢乐，但没给具体性质。','肯定是需住院的重伤。','在决定参加活动前发生。','使作者长篇说尽细节。'],
 ['A fun until指出转折，spare you the details明确省略细节，只能到此为止。','B little accident没有足够信息推出伤情与住院，不能补造。','C 本句延续活动中的fun，不提供此前决定的时间线。','D spare...details与长篇详述相反。'],
 ['It was fun until our son had a little accident—I’ll spare you the details.'],
 'spare you the details','不向你赘述细节','作者刻意不说具体经过，阅读推断不可越过这条证据边界','The meeting was awkward, but I will spare you the details.',['spare someone the details','a little accident'],
 '本来很开心，直到儿子出了点小状况——细节就不多说了。',support='limited-inference')

add(7,'主旨','How does the passage describe fellowship in marriage?',
 ['As passion without any shared history.','As a bond developing through repeated shared experiences, including adversity.','As a skill available only to couples who have children.','As an immediate result that needs no time together.'],1,
 '本段怎样描述婚姻中的情谊？',['只有激情，没有共同历史。','由反复共同经历、包括逆境逐渐形成的纽带。','仅有孩子的伴侣才能具备的技能。','不需相处时间便立即产生。'],
 ['A not just...but also明确加上共同逆境记忆。','B repeated shared experiences及extended period概括情谊的形成。','C who have children can举育儿中的连接可能，不是说无子女者不可能有情谊。','D extended period与瞬间结果相反。哲学论述并未规定所有婚姻必然如此。'],
 ['Fellowship emerges out of repeated shared experiences over an extended period of time.'],
 'adversity','逆境；困苦','关系中共同经历、之后共同回忆的困难','They supported each other through adversity.',['shared memory of adversity','develop fellowship'],
 'B在《Either/Or》中谈到情谊的发展。婚姻之爱不只是激情与兴奋，也包括对逆境的共同记忆。情谊从长时间里反复共同经历中产生。有孩子的伴侣，可以通过共同育儿建立纽带，并在养育过程中学到新东西。')

add(8,'作者意图','What does the school example illustrate?',
 ['Parents literally return to school as children of the same age.','All parents and children have identical school experiences.','A steady musical tempo was used as a clinical intervention at school.','Parents can revisit their own past from a new perspective through their children.'],3,
 '学校例子说明什么？',['父母真的变回同龄儿童上学。','父母孩子学校经历完全相同。','学校用稳定节奏作临床干预。','父母可通过孩子从新视角重看自己的过去。'],
 ['A reexperience是从parental perspective重新体会，非年龄倒退。','B similarities and differences同时保留异同。','C 后半是婚姻音乐比喻，不能当学校实验。','D 孩子入小学/中学让父母以家长眼光再体验自己的对应阶段。B的“整个人生重活”是哲学引语，非字面生理主张。'],
 ['you will reexperience your elementary school days from a parental perspective.'],
 'even tempo','均匀稳定的节奏','B借音乐稳定节奏说明婚姻可能的美，even非“甚至”在此的词义','The drummer maintained an even tempo throughout the piece.',['an even tempo','a parental perspective'],
 '正如B所说：“整个人生在孩子身上又活了一遍；只有到那时，人才能对自己的人生有所理解。”孩子上小学时，你会从家长视角重新体验自己的小学时光；上中学时，又会重新体会中学，注意到相似与不同。B以音乐的诗意再现比喻婚姻之爱：“在音乐中，均匀节奏可以有许多美感和巨大效果”——即使它单调。')

add(9,'同义改写','Which paraphrase preserves B’s musical analogy?',
 ['An apparently repetitive marriage can contain depth and beauty when lived well.','Every monotonous marriage is necessarily beautiful regardless of circumstances.','Marital love requires listening to the named works every day.','Surface variety is the only possible source of richness.'],0,
 '哪项保留B的音乐类比？',['看似重复的婚姻，经营得当也能有深度与美。','任何单调婚姻不论处境都必然美。','婚姻之爱要求每天听指定作品。','表面多样是丰富的唯一来源。'],
 ['A monotonic on the surface...rich...deep down及played properly共同支持有条件的可能性。','B might/can和played properly不能改成无条件必然。','C like是类比，不是播放曲目的行动规定。','D 段落恰讨论表面单调也可能深层丰富。音乐例子没有构成婚姻效果实验。'],
 ['monotony can be an even tempo that, played properly, produces beauty and great effect.','very monotonic on the surface but rich and beautiful deep down.'],
 'monotony','单调；重复感','此处不直接等同没有任何价值，作者借稳定节奏重解其可能性','She found unexpected beauty within the routine’s apparent monotony.',['suffer from monotony','on the surface'],
 '也就是说，婚姻之爱可能受单调困扰，但单调也可成为均匀的节奏；演奏得当，就能产生美与巨大效果。按照Kierkegaard的B，婚姻之爱可以像Maurice Ravel的《Boléro》和Philip Glass的《Metamorphosis》：表面很单调，深处却丰富而美。')

add(10,'作者意图','Why does the author introduce Aron’s experiment?',
 ['To show that B and A held exactly the same view of monotony.','To prove that prayer is the only way to sustain a relationship.','To explore another way of renewing long-term relationships when monotony becomes boring.','To replace the question of relationship renewal with a history of musical tempo.'],2,
 '作者为何引入Aron实验？',['说明B与A对单调完全同看法。','证明祈祷是维持关系的唯一方式。','探讨单调令人无聊时，更新长期关系的另一途径。','把关系更新问题换成音乐节奏史。'],
 ['A beautiful与boring是对照，非全同。','B beyond prayer明确问还有什么，不是only。','C How can...beyond prayer提出问题，experiment...answer承接寻找方法。','D 此处从哲学讨论过渡到关系实验，没转写音乐史。'],
 ['How can we continue to rejuvenate our long-term romantic relationships, beyond prayer?','Art Aron and colleagues conducted one of the most famous relationship experiments'],
 'rejuvenate','使恢复活力；更新','为长期恋爱关系重新带来活力，不是让年龄生理倒退','They wanted to rejuvenate their shared routine.',['rejuvenate a relationship','beyond prayer'],
 '如Kierkegaard的B所说，婚姻的单调可以美好。但对大多数像A的人，它也会无聊。除了祈祷，我们还能怎样不断更新长期恋爱关系？Art Aron及同事进行了一项最知名的关系实验，可以帮助回答这个问题。')

add(11,'细节','Which requirement belongs to the novel-arousing task?',
 ['Couples chose whichever condition they preferred.','The pillow could be carried using the participants’ teeth.','The task required standing upright throughout the route.','Couples moved on hands and knees and carried a pillow without hands, arms, or teeth.'],3,
 '哪项属于新奇唤起任务的要求？',['伴侣自选偏好条件。','可用牙齿携带枕头。','全程必须直立。','手膝着地移动，携枕头时不用手、臂或牙。'],
 ['A randomly assigned明确随机分组，非自选。','B without...teeth明确排除。','C remaining on hands and knees与直立相反。','D 结合移动姿势与枕头限制，越障时也需遵守。roughly30feet是往返路线描述，约3feet是卷垫高度，不能互换。这里复述实验条件，不是让读者执行。'],
 ['remaining on their hands and knees at all times','carry a pillow without using hands, arms, or teeth, even while going over the barrier.'],
 'barrier','障碍物','此处是返回起点处约三英尺高的卷起体操垫','The pair carefully crossed the barrier during the task.',['go over a barrier','a novel-arousing task'],
 '实验中，约会中和已婚伴侣被随机分到两个条件之一。分到“新奇唤起”任务的伴侣，被要求全程手膝着地，沿几块体操垫走到尽头再返回，路程约30英尺；回到起点时，要越过一卷约3英尺高的体操垫。此外，他们还要携带一个枕头，不能用手、手臂或牙齿，连越障时也一样。')

add(12,'细节','How did the control condition differ from the timed task?',
 ['Control couples completed the same barrier course six times.','Control couples simply took turns rolling a ball.','Control couples prayed for one minute before crossing the barrier.','Control couples carried the pillow three times in exactly three minutes.'],1,
 '控制条件与计时任务有什么不同？',['同样越障路线做六次。','只是轮流滚球。','越障前祈祷一分钟。','三分钟里携枕三次。'],
 ['A 控制组任务明确不同，非六次同路线。','B simply rolled a ball in turn直接支持。','C 混入前面的祈祷研究，本段不含此安排。','D under one minute属前面任务的三次要求，非控制组恰好三分钟。'],
 ['They were asked to do this three times in under one minute. In the control condition, couples simply rolled a ball in turn.'],
 'in turn','轮流；依次','滚球时两人交替，不是反过来改变因果方向','The players rolled the ball in turn.',['roll a ball in turn','in under one minute'],
 '他们被要求在不到一分钟内完成三次。控制条件下，伴侣只是轮流滚球。')

add(13,'逻辑关系','What did the final study add to the earlier self-report findings?',
 ['Discussion tasks in which the novel-task couples also showed more loving gestures afterward.','A finding that all couples remained equally satisfied for the rest of their lives.','A comparison with a group that never participated in any activity.','A replacement of all behavioral observations with a single brain scan.'],0,
 '最后研究在先前自报发现之外增加了什么？',['讨论任务中，新奇任务伴侣事后也表现更多亲爱动作。','所有伴侣终生同样满意的结果。','与完全未参加活动组的比较。','以一次脑扫描取代所有行为观察。'],
 ['A before/after discussion及exhibited loving gestures，给出自报以外的行为信息。','B after activity/later discussion没有终生追踪结论。','C 对照为mundane task而非无活动。','D 此段行为观察，不是后文另项神经影像研究。63对为新样本复现，不能自动当作每项研究总人数。'],
 ['the researchers added two discussion tasks before and after the activity.','also exhibited more loving gestures during the later discussion task than those in the mundane condition.'],
 'replicated','复现；用新样本重复得到','用63对已婚伴侣另作检验，不等于只重读原组答案','The team replicated the finding with a new sample.',['replicate findings','loving gestures'],
 '如Aron所预测，完成新奇唤起任务的伴侣，活动后自报的关系质量显著高于完成平常任务者。研究者又用63对已婚伴侣的新样本复现这些发现。最后一项研究在活动前后增加两个讨论任务。新奇任务条件的伴侣，不只自报关系质量更高，在后来的讨论中，也比平常条件者表现出更多亲爱的动作。')

add(14,'细节','What does the 40 percent figure refer to?',
 ['All participants assigned to the pillow task who had remained faithful.','The proportion of strangers whose images activated the brain.','People married over ten years who reported being very intensely in love.','Exactly forty of the sixty-three couples from the replication.'],2,
 '40%指什么？',['枕头任务中保持忠诚者占比。','陌生人图像激活脑的比例。','结婚超过十年者中，自报非常强烈恋爱感的人。','复现样本63对中恰好40对。'],
 ['A 混合新奇任务与另一祈祷研究的不忠结果。','B 百分比来自自报恋爱感，非脑图像激活比例。','C those married over ten years/reported/very intensely in love逐项限定。','D 40percent不是40对，且作者明确separate line of research，不能与63对复现样本混算。最后另提影像研究，也属不同研究。'],
 ['In a separate line of research, they also found that 40 percent of those married over ten years reported being “very intensely in love.”'],
 'rekindle','重新点燃；使复燃','用火焰比喻重唤爱与激情，could保留可能性','A shared discovery helped rekindle their enthusiasm.',['rekindle love','a separate line of research'],
 'Aron及同事发现，参与新奇而有挑战的活动，可能重燃爱，甚至激情。在另一条研究线上，他们还发现，结婚超过十年的人中，有40%自报“非常强烈地恋爱着”。看来，多年后仍让爱保持活力是可能的。另一项研究中，研究者用神经影像技术，向参与者展示伴侣、亲密朋友以及陌生人的面部图像。')

add(15,'细节','What comparison does the neuroimaging passage report?',
 ['Every participant had been married for exactly 21.4 years.','Partner images produced stronger reward-region activation than friend or stranger images.','Stranger images consistently produced the strongest reward response.','Dopamine levels were proved to increase by the same amount in every marriage.'],1,
 '神经影像段落报告什么比较？',['每人恰好结婚21.4年。','伴侣图像引起的奖励相关脑区激活强于朋友或陌生人图像。','陌生人图像始终引起最强反应。','证明每段婚姻多巴胺都等量增加。'],
 ['A average是均值，非人人恰好。','B when...partner...than...friend/stranger给出条件间方向。','C 方向相反。','D associated with dopamine-rich reward system不是直接测出每个人同量多巴胺增加，更不能推广全部婚姻。作者总结的是possible维持激情。'],
 ['they showed far stronger activation in the brain regions associated with the dopamine-rich reward system','when they saw their partner’s image than when they saw a close friend or a stranger.','it is possible to maintain passion over a long period of time.'],
 'activation','激活；活动增强','此处指影像观察到的相关脑区反应，不等于直接测量激素浓度','The scan showed stronger activation during the task.',['brain-region activation','an average of'],
 '参与者平均结婚21.4年，但看伴侣图像时，相比看亲密朋友或陌生人，他们在与富含多巴胺的奖励系统有关的脑区，如腹侧被盖区和背侧纹状体，激活强得多。Kierkegaard的B在这一点上是对的：长期保持激情是可能的。')

add(16,'主旨','What process does self-expansion theory propose?',
 ['Partners become less familiar as mutual disclosure increases.','A partner becomes part of the self only through physical travel.','Initial disclosure automatically creates unlimited later novelty.','Intense early disclosure incorporates the partner into the self, but later expansion opportunities diminish.'],3,
 '自我扩展理论提出什么过程？',['互相揭露越多，彼此越陌生。','只有实际旅行才会把伴侣纳入自我。','最初揭露自动带来无限后续新奇。','早期深入揭露使伴侣成为自我一部分，后来扩展机会减少。'],
 ['A partner becomes part of themselves不支持越来越陌生。','B 文中机制是交谈和self-disclosure，没only travel。','C opportunities...limited与无限相反。','D 前句初期扩展、However后机会受限，概括完整。posits表理论主张，非此两句直接报告新实验。'],
 ['their partner becomes part of themselves, essentially expanding the self.','after the initial phase of mutual self-disclosure, opportunities for further expansion are limited.'],
 'self-disclosure','自我揭露；向他人敞露内心','双方在深入交谈中分享个人感受经历，不等于泄露账号凭据','Mutual self-disclosure helped them understand each other.',['mutual self-disclosure','self-expansion theory'],
 'Aron著名的恋爱关系“自我扩展理论”提出：关系初期，两个人通过深入交谈进行大量自我揭露；随着时间，伴侣成为各自的一部分，本质上扩展了自我。但最初互相揭露的阶段之后，进一步扩展的机会就有限了。')

add(17,'逻辑关系','How does the theory explain the potential value of novel activities?',
 ['They eliminate every possible cause of marital dissatisfaction.','They prevent partners from learning anything unfamiliar.','They may provide new self-expansion opportunities where a partial cause of decline is their absence.','They prove that all marriages decline at exactly the same rate.'],2,
 '理论如何解释新奇活动的潜在价值？',['消除所有婚姻不满意原因。','阻止伴侣学习陌生事物。','缺少扩展机会是下降的部分原因，新活动可能补充机会。','证明所有婚姻以同样速度下降。'],
 ['A due in part不能扩成唯一病因或全部治愈。','B provide further opportunities与阻止学习相反。','C theorizes、in part、could保留理论解释、部分性及可能性。','D typical decline没给统一速度或人人必降。continuous rejuvenation是此解释下的表达，不保证不断升高。'],
 ['is due in part to this lack of new opportunities to expand the self','engagement in novel activities could provide further opportunities for self-expansion.'],
 'due in part to','部分归因于','防止把机会不足错当婚姻满意度下降的唯一原因','The change was due in part to new demands at work.',['due in part to','further opportunities'],
 'Aron推论，婚姻过程中满意度常见的下降，部分归因于缺少新的自我扩展机会；参加新活动，可能提供进一步扩展的机会。以这种方式，伴侣可以体验“持续更新”。')

add(18,'作者意图','Why mention Aron and Elaine’s activities?',
 ['To show that they applied their findings to their own shared life.','To report another randomized trial conducted across the listed countries.','To claim that only expensive international travel can renew love.','To establish that shared reflection is ineffective.'],0,
 '为何列举Aron与Elaine的活动？',['说明两人把研究发现用于自己的共同生活。','报告在列举国家做的另一随机试验。','声称只有昂贵跨国旅游才能更新爱。','确立共同反思无效。'],
 ['A took findings to heart后给徒步、互画、漂流等实践例子。','B In an interview是个人生活叙述，未给分组或跨国实验。','C painted pictures等不必跨国，文本没only/昂贵限制。','D as is shared reflection明确也肯定共同反思。不能把个人旅行记当作独立因果证据。'],
 ['he and his wife, Elaine, took their findings to heart','Novelty is effective for long-term romantic couples, as is shared reflection.'],
 'took their findings to heart','认真看待并付诸实践','不只口头认同研究，而把新活动带进夫妻生活','They took the advice to heart and tried a new routine together.',['take findings to heart','shared reflection'],
 '一次采访中，Art Aron说，他与妻子Elaine认真采纳自己的发现：他们到日本、意大利、塞尔维亚和新西兰徒步旅行。他们互相画像、看赛马、在大峡谷的科罗拉多河漂流，还去观鲸。新奇对长期恋爱伴侣有效，共同反思也一样。')

add(19,'细节','Which details illustrate Jiro’s continual attention to technique?',
 ['He avoids changing any preparation method once learned.','He chooses rice temperature solely to save cooking time.','He relies on the documentary’s title instead of assessing food.','He carefully controls rice temperature and massages octopus to improve tenderness.'],3,
 '哪些细节体现Jiro持续关注技艺？',['学会后不再改变任何方法。','只为节省时间选饭温。','靠纪录片名而不评价食物。','细控寿司饭温，并按摩章鱼改善嫩度。'],
 ['A constantly trying to improve与不改变相反。','B maximize taste是目的，非solely节省时间。','C documentary是介绍来源，不是质量判断方法。','D rice temperature及massage...tender两项对应。then85和2011都是书述纪录片时点，不冒称人物今日年龄或店铺现状。'],
 ['it must be the perfect temperature to maximize the taste of the fish.','He uses a massage technique to make his octopus more tender.'],
 'tender','嫩的；柔软易食的','此处形容章鱼口感，不是温柔的情绪或招标','The long preparation made the octopus tender.',['make octopus tender','sushi rice temperature'],
 '《Jiro Dreams of Sushi》是David Gelb于2011年拍摄的纪录片片名，主角是当时85岁、在东京做寿司的Jiro Ono。他痴迷寿司，不断改善技法。他对饭温讲究到极致：必须恰好，才能最大程度呈现鱼味。他还用按摩技法让章鱼更嫩。')

add(20,'作者意图','What does the increase from thirty to forty-five minutes illustrate?',
 ['He changed methods only because he had failed to earn recognition.','He continued seeking improvement despite already reaching a celebrated level.','Customers were randomly assigned in a blinded taste trial.','The longer preparation made him abandon sushi entirely.'],1,
 '从30分钟增至45分钟说明什么？',['只是因未获认可才改方法。','已获高度赞誉仍继续求进。','顾客被随机分配到双盲试吃。','更长准备使他彻底放弃寿司。'],
 ['A already earned three Michelin stars说明已有认可。','B Even though...could have been satisfied...Nonetheless构成不满足已有顶峰的对比。','C customers seemed to enjoy是观察性叙述，没随机或盲法设计。','D always...improve非放弃。星级是书中叙述背景，不作当前店铺状态声明。'],
 ['Even though Jiro had already earned three Michelin stars with the thirty-minute massage','Nonetheless, he always looks for ways to improve.'],
 'pinnacle','顶峰；最高成就','形容其既有烹饪艺术声誉，用以衬托仍精进','She kept experimenting after reaching the pinnacle of her profession.',['the pinnacle of culinary art','look for ways to improve'],
 '他最初把章鱼按摩30分钟；尝试更长时间后，顾客似乎更喜欢那寿司。尽管30分钟的做法已让他赢得米其林三星，如今他烹调前按摩45分钟。他本可以满足于那些已让他达到烹饪艺术巅峰的方法。可他总在寻找改进方式。')

add(21,'主旨','What common principle connects customer reactions and ingredient sourcing?',
 ['Daily scrutiny and precise choices support continuing refinement.','Recognition makes daily assessment unnecessary.','Ingredients are bought without regard to the merchant’s specialty.','Only the son’s age determines the restaurant’s quality.'],0,
 '顾客反应与食材采购由什么共同原则连接？',['每日细察与精确选择支持持续改善。','获认可后无需每日评估。','采购不考虑商家专长。','只由儿子年龄决定品质。'],
 ['A pays close...attention、meticulous、assessed every day、improved over time贯穿细节。','B 与每日评估相反。','C specialty merchants及trusted虾商/鳗商明确专门选择。','D fifty-something只是人物年龄描述，不是决定食物质量的唯一因素。没有说所有原料由同一个商家供应。'],
 ['Every aspect of the preparation and cooking is exact, assessed every day, and improved over time.'],
 'source','采购；寻找并取得','这里是动词，指从特定可靠商家取得食材，非网站源代码','The chef sourced fresh ingredients from trusted merchants.',['source ingredients','specialty merchants'],
 '每位顾客每吃一口后的表情，他都仔细、带着评判地观察。选鱼同样细致。他50多岁的儿子到筑地鱼市场，从专业商家采购全部食材：虾找固定信任的虾商，鳗找固定信任的鳗商，等等。准备和烹调的每个方面都精确，每天评估，日积月累地改善。')

add(22,'细节','How does the passage describe seating a left-handed customer?',
 ['Between two right-handed customers regardless of space.','Immediately to the right of another left-handed customer.','In a corner seat with nobody seated to their left.','At any available seat because handedness is ignored.'],2,
 '本段怎样描述左撇子顾客的座位？',['不论空间都夹在两位右手顾客间。','紧坐另一左撇子右侧。','坐角落，左边无人。','任意空位，因为不理惯用手。'],
 ['A 文中刻意避免左右惯用手相邻，不是随意夹坐。','B 不是描述必须两左撇子相邻的规则。','C corner seat、no one...left给出准确位置。','D even cares说明关注这点。可以理解为安排细致，但此句没给经测量的碰撞率下降，不能补因果数据。'],
 ['a left-handed person would sit in the corner seat, where no one sits on their left.'],
 'vice versa','反过来也一样','说明左右惯用手相邻的反向排列也一样避免，不是所有座位一律反转','The rule applies to the first group and vice versa.',['or vice versa','a corner seat'],
 'Jiro甚至在意顾客惯用右手还是左手，因此不会让右手顾客坐在左手顾客旁，反过来也一样；相反，左撇子会坐角落座位，左边没有其他人。')

add(23,'细节','Which sequence matches Jiro’s early career as described?',
 ['He opened his own restaurant at nine, then trained as an apprentice at forty.','He left home at nine, apprenticed for years, and opened his own restaurant at forty.','He began by training forty apprentices before ever working in a restaurant.','He avoided cleaning work until after receiving his own restaurant.'],1,
 '哪项符合Jiro早年职业顺序？',['九岁开店，40岁当学徒。','九岁离家，多年学徒，40岁开店。','没在餐厅工作前先带40名徒弟。','开店前一直不做清洁。'],
 ['A 年龄和阶段对调。','B left home...nine、apprenticeship...many years、own...forty顺序准确。','C 三到五名是开店后同时培训数量，非40名，40是年龄。','D 最后一句明确学徒从清洁洗碗开始，未支持免做清洁。战争贫困是书述离家背景，不据此补详细生平。'],
 ['Jiro left home at age nine.','finally opened up his own at age forty.'],
 'apprenticeship','学徒期；学徒训练','在寿司餐厅从基础杂务开始的长期学习过程','She completed an apprenticeship before opening her own workshop.',['do an apprenticeship','at any given time'],
 '因为战争与贫困，Jiro九岁离家。他在寿司餐厅做了多年学徒，终于在40岁时开了自己的店。那时起，他在任一时期同时培训三到五名学徒。学徒先从清扫餐厅和洗碗做起。')

add(24,'作者意图','What does the example of Nakazawa’s two hundred attempts emphasize?',
 ['A guarantee that every apprentice’s two-hundredth attempt is accepted.','Evidence that Jiro abandoned demanding standards after the first attempt.','The claim that apprentices never want to own restaurants.','The prolonged, exacting training described in this craft.'],3,
 'Nakazawa做200次的例子强调什么？',['保证每位学徒第200次必合格。','Jiro试一次后便放弃严标准。','学徒都不想自己开店。','这门手艺所述训练漫长而严格。'],
 ['A 个案次数不是所有人的合格公式，也没说每第200次统一过。','B deemed one usable是在大量尝试后，非取消标准。','C because...want to open up own restaurants正给出开店动机。','D ten years、two hundred、long and demanding一起支撑严苛学徒期。这里理解原书叙述，不把个案规范当各地餐饮从业的强制要求。'],
 ['made two hundred tamagoyakis as an apprentice before Jiro finally deemed one usable.','there has always been a long and demanding training period.'],
 'deemed','认为；判定','由师傅判断一份作品是否可用，不是学徒单方宣布毕业','The instructor deemed the final piece usable.',['deem one usable','a demanding training period'],
 '做了十年清洁后，Jiro才让学徒做tamago寿司，也就是蛋羹寿司。就连后来在纽约成名的Nakazawa，当学徒时也做了200份tamagoyaki，才终于有一份被Jiro认为可用。在sushi shokunin，即职业寿司师傅的世界，像日本其他手工艺职业一样，一直有漫长而苛刻的训练期。人们经历这种严酷学徒期，是因为最终想开自己的餐厅并取得成功。')

add(25,'逻辑关系','What initial contrast is offered to explain Jiro’s sustained engagement?',
 ['His pursuit of perfection was private and personal, unlike the athletes’ public competitive pursuit.','He had stopped pursuing improvement after sixty years.','The athletes’ performances were private while his were ranked in sporting competitions.','A clinical trial proved that private work prevents depression in everyone.'],0,
 '作者首先用什么对照解释Jiro长期投入？',['他的完美追求较私人个人化，运动员则公开竞技。','60年后他已不再求改进。','运动员表现私下进行，他却在体育比赛排名。','临床试验证明私下工作防止每人抑郁。'],
 ['A First...private and personal、whereas...public...competition是本段明确对照。','B quest for perfection不支持放弃。','C 两边条件对调且新增寿司体育排名。','D 这是作者解释性比较，不是关于抑郁的普遍临床因果证明。运动员经历是作者回顾第7章所述，不作其今日健康状态判断；arguably也不是确定无争议排名。'],
 ['Jiro’s quest for perfection is private and personal, whereas Phelps’s and Biles’s were public and in the context of competition with other athletes.'],
 'quest','追求；长期探求','对完善技艺持续投入，不是一次性找物','His quest for improvement continued for decades.',['a quest for perfection','burn out'],
 '第7章我谈过Michael Phelps与Simone Biles——或可说是史上最好的游泳和体操运动员——曾受抑郁困扰，也曾对擅长的运动失去兴趣。那么，Jiro为何每天做同件事超过60年，却没有同样倦怠？第一，他对完美的追求是私人和个人化的；Phelps与Biles则是在公开、与其他运动员竞争的环境中追求。')

assert len(out)==25 and [q['id'] for q in out]==[t['questionId'] for t in targets]

def persist():
 path=ROOT/'source/short-questions/additional.json';existing=load('source/short-questions/additional.json');byid={q['id']:q for q in existing}
 for q in out:
  if q['id'] in byid:assert byid[q['id']]==q,('Refuse to overwrite changed authoring',q['id'])
  else:existing.append(q)
 path.write_text(json.dumps(existing,ensure_ascii=False,indent=2)+'\n',encoding='utf8',newline='\n')
 review=dict(batchId='batch-038',date='2026-10-24',pdfSha256=b['pdfSha256'],checkedPdfPages=list(range(151,156)),questionIds=[q['id'] for q in out],paragraphs=[dict(id=pid,textSha256=hashlib.sha256(pp[pid]['text'].encode()).hexdigest()) for pid in dict.fromkeys(q['paragraphId'] for q in out)],note='完整PDF151–155原页视觉核对。Fincham研究明确随机组、四周每天至少一次为伴侣祈祷，控制组回想当日活动，结果自报；less likely非零不忠，holy是felt非宗教真理证明。B历史/音乐比喻归哲学角色，育儿例子不作无子女无情谊。万圣节事故细节作者省略不补造。Aron新奇任务路线/枕头约束与轮流滚球控制分开；63对为复现新样本，后续讨论亲爱动作是行为结果。40%自报十年以上婚姻属另一研究线，不混63对或影像样本；21.4是平均年限，激活奖励相关脑区不等于直接测同量多巴胺。self-expansion为理论，due in part/could非唯一因果保证；夫妻旅行采访非随机研究。Jiro例子锚定2011纪录片当时年龄与书载星级，顾客seemed非盲法试吃；30至45分钟、九岁离家40岁开店、十年清洁/200次个案不推广硬规则。私人/公开竞技是作者解释比较，不当临床证明或人物今日健康断言。额外章首正文及辅助材料源文审计仍开放，不宣称全书完整覆盖。')
 (ROOT/'source/short-questions/review-chapter13-love-craft25.json').write_text(json.dumps(review,ensure_ascii=False,indent=2)+'\n',encoding='utf8',newline='\n')
 print('Saved',len(out),'of 25 individually authored exercises')

if __name__=='__main__':persist()
