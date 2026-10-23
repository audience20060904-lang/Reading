"""25 individually authored exercises for frozen targets, PDF pages 115-118.
Preserve printed English, source positions and all previously published questions.
"""
from pathlib import Path
import json,hashlib
ROOT=Path(__file__).resolve().parents[2]
load=lambda p:json.loads((ROOT/p).read_text(encoding='utf8'))
b=load('public/data/book.json');plan=load('public/data/reading-plan.json');targets=load('source/short-questions/batch029-targets.json')['targets']
ss={s['id']:s for s in b['sentences']};pp={p['id']:p for p in b['paragraphs']};out=[]
def add(i,kind,prompt,options,answer,prompt_zh,options_zh,analyses,quotes,word,meaning,context,example,collocations,translation,support='explicit'):
 t=targets[i-1];u=next(u for u in plan['units'] if u['id']==t['readingUnitId']);group=[ss[sid] for sid in u['sentenceIds']];p=pp[u['paragraphId']];text=p['text'][group[0]['start']:group[-1]['end']]
 assert hashlib.sha256(text.encode()).hexdigest()==t['passageSha256'];evidence=[]
 for quote in quotes:
  offset=text.find(quote);assert offset>=0,(i,quote);start=group[0]['start']+offset;end=start+len(quote);touching=[s for s in group if s['start']<end and s['end']>start]
  evidence.append(dict(quote=quote,sentenceIds=[s['id'] for s in touching],sources=list({(r['pdfPage'],r['block']):r for s in touching for r in s['sources']}.values())))
 assert word.lower() in text.lower(),(i,word)
 out.append(dict(id=t['questionId'],version=1,readingUnitId=u['id'],chapterId=u['chapterId'],sectionId=u['sectionId'],paragraphId=u['paragraphId'],sentenceIds=u['sentenceIds'],passage=text,prompt=prompt,options=options,answer=answer,type=kind,promptZh=prompt_zh,optionsZh=options_zh,analyses=analyses,evidence=evidence,vocabulary=[dict(word=word,meaning=meaning,context=context,example=example,collocations=collocations)],translation=translation,support=support,editorialStatus='完整PDF115–118原页视觉核对与跨页拼接。搬迁心态实验区别真实迁居，焦虑用词相关不冒充独立随机中介操纵；Bates和购房经历为作者轶事，节目仅限作者观看且非盲评。杯子先设想后述实验典型结果，主观所有权估值非客观市价必升；零食计划与一次购买分开。英镑期望值非保证收益，原书称loss aversion但当前正向收益例不编损失条件、不视作独立证明；条件式舒适区论证不扩为无条件冒险。保留旧题和句界，不宣称逐句证据全覆盖。'))







add(1,'细节','Which condition produced a particularly strong familiarity-liking effect?',
 ['Imagining a typical day.','Imagining staying in one place.','Imagining frequent future moves.','Every condition produced an identical effect.'],2,
 '哪个条件下熟悉与喜欢的效应特别强？',['想象普通一天。','想象长期定居。','想象未来频繁搬迁。','各条件效应完全相同。'],
 ['A 是比较条件之一，非特别强者。','B 长期稳定条件比搬迁条件弱。','C thought about moving around frequently 与更喜欢熟悉刺激对应。','D all three 有效应不等于强度相同。实验操纵想象心态，不是让参与者真实多年搬家。'],
 ['in the residential mobility condition participants showed a particularly strong familiarity-liking effect.'],
 'particularly','尤其；特别','强调搬迁心态条件效应较强，不否认其他组也有','The effect was particularly strong in the new setting.',['particularly strong','particularly attractive'],
 '三个条件下都观察到单纯曝光效应，复现此前发现。不过最重要的是，居住流动条件下，参与者表现出特别强的熟悉—喜欢效应。也就是说，想象未来频繁搬迁时，比起想象长期留在一处或普通一天，他们更喜欢熟悉汉字或熟悉面孔。')

add(2,'细节','What relationship was reported between anxiety-related language and the effect?',
 ['More anxiety-related words accompanied a stronger familiarity-liking effect.','More anxiety words accompanied a weaker effect.','All conditions used the same number of anxiety words.','Anxiety words were independently assigned to each person.'],0,
 '焦虑相关用词与效应之间报告什么关系？',['焦虑词更多伴随更强熟悉偏好。','焦虑词更多伴随更弱效应。','各组焦虑词数量相同。','焦虑词被独立随机分配给各人。'],
 ['A the more...the stronger 明确同向关系。','B 方向反转。','C mobility condition 用词比另两组多。','D 用词是描述未来生活时观察到的，不是此处独立操纵的焦虑剂量。作者随后概括压力焦虑作用，不能将用词相关单独改成已随机验证的中介因果。'],
 ['the more anxiety-related words participants used, the stronger familiarity-liking effect they showed.'],
 'amplify','增强；放大','作者以此概括压力焦虑下熟悉偏好的增强','Uncertainty may amplify a preference for familiar routines.',['amplify a tendency','amplify an effect'],
 '结果，搬迁条件参与者描述未来流动生活时，比稳定组或控制组使用更多焦虑相关词；用这类词越多，熟悉—喜欢效应越强。换言之，压力与焦虑会增强我们喜欢熟悉事物的倾向。')

add(3,'作者意图','Why does the author return to the secretary problem?',
 ['To deny that exposure effects can be replicated.','To present a new marriage experiment here.','To claim familiarity always produces optimal decisions.','To critically examine what familiarity implies for exploring potential partners.'],3,
 '作者为何回到秘书问题？',['否认曝光效应可复现。','在此报告新婚姻实验。','声称熟悉总带来最优选择。','批判思考熟悉偏好对探索潜在伴侣的含义。'],
 ['A 开头明确 replicable。','B 当前是联系决策模型的讨论，非新试验。','C 应先探索陌生候选，恰提示熟悉偏好的局限。','D critically 与 partner 设问引出应用层面反思；模型建议不等于现实婚恋保证。'],
 ['But let’s think about its implications critically.','explore unfamiliar candidates before settling down'],
 'implications','含义；可能影响','研究现象对实际决策意味着什么','The team discussed the implications for everyday choices.',['practical implications','think about implications critically'],
 '单纯曝光效应可重复验证，读起来也有趣。但让我们批判地思考它的含义。秘书问题应用到寻找伴侣会如何？为作最优决定，你本应先探索陌生候选，再安定下来。')

add(4,'逻辑关系','What makes premature commitment more likely in the author’s account?',
 ['Enjoying extra effort and avoiding familiar objects.','Preference for familiarity and dislike of effort, worsened by stress.','Considering a dozen candidates guarantees failure.','Stress removes the preference for familiarity.'],1,
 '按作者论述，什么促使人过早定下来？',['喜欢额外努力、避开熟悉物。','偏好熟悉和厌恶费力，压力下更严重。','考察十二人保证失败。','压力消除熟悉偏好。'],
 ['A 两种倾向方向都颠倒。','B tendency...familiar 与 aversion...effort 共同促早定，under stress 加剧。','C 没有十二候选导致必败的结论。','D gets worse 不是消除。这里是作者综合应用，不编造个体婚姻预测。'],
 ['our tendency to like a familiar object and our aversion to extra effort makes us settle down prematurely.','gets worse when we are under stress.'],
 'prematurely','过早地；尚未充分准备地','探索不足时就定下来，不是按固定年龄划界','They committed prematurely before comparing alternatives.',['settle down prematurely','decide prematurely'],
 '如果想找很好的伴侣，你本应认真考虑一打潜在对象。这些过程令人有压力。心理研究表明，偏好熟悉事物和厌恶额外努力，使我们过早定下来。我们自己的研究进一步表明，压力下这种不良心理习惯更严重。')

add(5,'语境词义','What does “kicks in in full force” mean here?',
 ['Comes into operation strongly.','Permanently disappears.','Requires physical kicking.','Leads exclusively to political party membership.'],0,
 '此处 kicks in in full force 是什么意思？',['强烈地开始起作用。','永久消失。','需要实际踢击。','只导致加入政党。'],
 ['A 保守心态在新环境强力起作用，推动寻找熟悉。','B 相反，并非退出。','C kick in 为习语，非动作踢。','D conservative mindset 在此指求稳心理，无政党归属证据。Ironically 指新地点反而激起熟悉搜索。'],
 ['the conservative mindset kicks in in full force and makes you search for familiarity.'],
 'kicks in','开始起作用','心态被激活的比喻表达','The preference for familiar options kicks in under pressure.',['kick in','in full force'],
 '讽刺的是，身处新地方时，求稳的心态却全面启动，让你寻找熟悉。')

add(6,'作者意图','What does the Bates anecdote illustrate?',
 ['The author never met Japanese students abroad.','The author conducted a randomized study of his classmates.','Even a traveller may gravitate toward familiar cultural company.','Going abroad makes every social choice rational.'],2,
 'Bates 的经历说明什么？',['作者留学时没见过日本学生。','对同学做了随机实验。','即使出国也可能偏向熟悉文化同伴。','出国使每个社交选择都理性。'],
 ['A 有三位其他日本学生。','B 第一人称反思，不是随机试验。','C 从 Tokyo 到 Maine 却多与日本人来往，说明熟悉吸引。','D doesn’t make rational sense 与此相反；作者说心理上可理解。'],
 ['I hung out with those three Japanese students far more than I probably should have.'],
 'hung out','一起相处；常在一起','描述非正式社交，不是悬挂物件','They hung out with familiar classmates after lectures.',['hang out with friends','hang out together'],
 '我在 Bates 留学时，只有另外三名日本学生：Yoko、Kiyomi、Mariko。惭愧地说，我与他们相处的时间，大概远超本应花的时间。我为何从 Tokyo 千里迢迢到缅因州 Lewiston，还是与其他日本人来往？理性上说不通，心理上却说得通。')

add(7,'语境词义','What does the “psychological teddy bear” metaphor emphasize?',
 ['Familiarity makes people buy toys in every situation.','Familiarity eliminates the need for understanding.','Only childhood objects can be familiar.','Familiarity provides emotional comfort.'],3,
 '心理泰迪熊的比喻强调什么？',['熟悉总让人买玩具。','熟悉消除理解的需要。','只有童年物件能熟悉。','熟悉提供情绪安慰。'],
 ['A 比喻不是玩具销售结论。','B understand each other 正强调相互理解。','C 没限于童年物品。','D It gives us comfort 直接解释比喻。'],
 ['It gives us comfort. It’s a psychological teddy bear.'],
 'commiserate','同病相怜；相互慰藉','同伴互相理解并分享不易，而非只有理性计算','The students commiserated over the difficulties of moving abroad.',['commiserate with someone','commiserate over difficulties'],
 '我们能同病相怜、相互理解。熟悉是一股强大力量。它给我们安慰。它是一只心理上的泰迪熊。')

add(8,'逻辑关系','What is paradoxical in this sentence?',
 ['Comforting familiarity becomes least attractive during exploration.','Familiarity is most attractive precisely when exploration takes us into discomfort.','Exploration never creates uncomfortable situations.','The effect operates only when people remain at home.'],1,
 '这句话的悖论在哪里？',['探索时熟悉安慰最没吸引力。','恰在探索使人不适时，熟悉最具吸引力。','探索从不使人不适。','效应只在人留家中时起作用。'],
 ['A strongest/most 与最弱相反。','B 世界探索和不舒服情境恰让心理泰迪熊更吸引，形成张力。','C putting ourselves in uncomfortable situations 明示不适。','D 当前谈探索世界，并非只限家中。这里是作者的概括，不新增普遍最大效应量数据。'],
 ['when we are exploring the world and putting ourselves in uncomfortable situations.'],
 'paradoxically','看似矛盾地；悖论般地','探索陌生之时却格外渴望熟悉','Paradoxically, travel made the familiar cafe more appealing.',['paradoxically attractive','paradoxically and unfortunately'],
 '看似矛盾而又遗憾的是，恰在我们探索世界、让自己身处不舒服情境时，单纯曝光效应最强，心理泰迪熊也最有吸引力。')

add(9,'主旨','What idea does the proverb express as explained here?',
 ['Living somewhere can make even an initially undesirable place feel like the best city.','Every city eventually becomes a national capital.','House hunting requires moving to a capital city.','People always prefer places where they have never lived.'],0,
 '按此处解释，谚语表达什么？',['住下来后，起初不理想的地方也能感觉是最佳城市。','每个城市最后都成国家首都。','找房必须搬去首都。','人总偏好没住过的地方。'],
 ['A once you live...even an undesirable one...best city 直接支持。','B capital (best) 是谚语解释，不是政治变迁预测。','C 设问引入居住选择，无必须迁首都要求。','D 与住下来产生偏好相反。谚语不是实验定律。'],
 ['once you live somewhere, whatever city you land in (even an undesirable one) becomes your capital (best) city.'],
 'proverb','谚语','文化表达，用来引出住久生情的主题','The proverb captures a familiar experience.',['a Japanese proverb','quote a proverb'],
 '以找房为例。搬到新城市时，你最初在哪租房？如果最终在那里买房，又在哪买？日语谚语 Sumeba Miyako 说：一旦住在某地，无论落在哪座城，即使起初不理想，它也会成为你的都城，也就是最好的城市。')

add(10,'细节','How did the author initially assess downtown Saint Paul?',
 ['More convenient than Uptown in every respect.','The place most people recommended.','Less convenient than Uptown, but with a coffee shop they liked.','A neighborhood they immediately refused to rent in.'],2,
 '作者起初怎样评价 Saint Paul 市中心？',['各方面都比 Uptown 方便。','大多数人推荐的地方。','比 Uptown 不便，但找到喜欢的咖啡店。','立即拒绝租住的地方。'],
 ['A less convenient 方向相反。','B 大多数人推荐的是 Uptown Minneapolis。','C 评价及 But 后例子都吻合。','D 实际租住一年，并非拒租。个人经历不自动代表全体居民。'],
 ['at first we found downtown Saint Paul less convenient than Uptown. But we found a coffee shop we liked.'],
 'convenient','方便的','比较两个区域初住时的便利程度','The apartment was less convenient for commuting.',['less convenient than','a convenient location'],
 '初到 University of Minnesota 时，我们在 Saint Paul 市中心租了一年公寓。大多数人推荐 Uptown Minneapolis。起初，我们确实觉得 Saint Paul 市中心不如 Uptown 方便。但我们找到一家喜欢的咖啡店。')

add(11,'细节','Why had the first Charlottesville house become unsuitable after ten years?',
 ['It was in a different city from North Downtown.','It was too small for a family of four.','The family had never bought it.','The Japanese restaurant had closed.'],1,
 '十年后 Charlottesville 的第一所房子为何不合适？',['位于与 North Downtown 不同城市。','对四口之家太小。','一家人从未买过它。','日本餐厅关门。'],
 ['A North Downtown 正是该房所在街区。','B too small for a family of four 明示。','C immediately bought 表明已购买。','D 餐厅只是此前地点的喜好，没报告关闭。注意两城搬迁和十年时序。'],
 ['After ten years, the first house became too small for a family of four.'],
 'condo','公寓产权住宅','在 Saint Paul 寻找的购房类型，区别于先前租公寓','They searched for a condo near the cafe.',['look for a condo','buy a condo'],
 '我们还找到一家喜欢的日本餐厅。那年十月，我们已在 Saint Paul 市中心找产权公寓。后来搬到 Charlottesville，立即在 North Downtown 买了一所小房。十年后，对四口之家来说，第一所房子太小了。')

add(12,'细节','What move does this short passage describe?',
 ['To a smaller house in North Downtown.','To a larger house in Uptown.','No move to a different house.','To a larger house in North Downtown.'],3,
 '这个短段描述了怎样的搬家？',['搬到 North Downtown 更小的房子。','搬到 Uptown 更大的房子。','没有换房。','搬到 North Downtown 更大的房子。'],
 ['A larger 是更大，非更小。','B 回答是 North Downtown，不是 Uptown。','C moved 明示换房。','D 房屋大小与街区都由当前短段支持。与前段连读还能理解熟悉地区的主题，但本题不把上一段内容当当前证据。'],
 ['we moved to a larger house in what neighborhood? North Downtown!'],
 'neighborhood','街区；居住社区','换住房却保留原来居住区域','They bought a larger house in the same neighborhood.',['the same neighborhood','move to a neighborhood'],
 '所以，我们搬到了一所更大的房子，在哪个街区呢？North Downtown！')

add(13,'细节','What is David’s role in the program?',
 ['Finding three new houses matching the couple’s wish list.','Renovating the existing home as the designer.','Providing the couple with three new jobs.','Requiring the couple to remain in their old house.'],0,
 '节目中 David 的职责是什么？',['找三所符合夫妻愿望清单的新房。','作为设计师改造旧房。','提供三个新工作。','要求夫妻留旧房。'],
 ['A 房产经纪人帮找新社区新房并展示三所。','B 改造旧房是 Hilary 的职责。','C houses 不是 jobs。','D 当前只说明角色与选择，没有强制留住要求。节目设定不是随机实验。'],
 ['David shows three houses that meet the couple’s wish list.'],
 'renovations','翻新；改造工程','旧房需要大修，是节目两条选择线的起点','The house needed major renovations.',['major renovations','renovate a house'],
 'HGTV 热门节目 Love It or List It 中，出场夫妻的房子需要大规模翻新。主持人之一 Hilary 是设计师，帮助翻新。另一位 David 是房产经纪人，帮他们在新街区找新家。David 展示三所符合夫妻愿望清单的房子。')

add(14,'作者意图','Why does the author mention couples refusing to list their renovated home?',
 ['To prove that every episode has the same outcome.','To show that new houses were never attractive.','To illustrate familiarity bias through the episodes he watched.','To report a randomized trial of neighborhoods.'],2,
 '作者为何提夫妻拒绝挂牌卖房？',['证明每集结局都相同。','说明新房从没吸引力。','用自己看过的节目举例说明熟悉偏误。','报告社区随机试验。'],
 ['A every time I’ve watched 限于作者观看经历，不是统计所有集。','B 新房 typically appear 更吸引，形成 Yet 对比。','C 太爱原社区不愿走，被作者明确当 familiarity bias 例子。','D 节目观察不等于随机试验。Objectively speaking 是作者措辞，不能冒充客观盲评数据。'],
 ['they loved their neighborhood too much to leave.','This is a prime example of the familiarity bias'],
 'opted','选择了；决定了','opted not to list 表示决定不挂牌出售','They opted to keep their renovated home.',['opt not to list','opt to stay'],
 '客观地说，David 展示的房子通常看起来比翻新的旧房更吸引人。但每次我看这节目，夫妻都喜欢翻新结果，决定不挂牌换新房——他们太爱原社区，不愿离开。这正是此前讨论的熟悉偏误的典型例子。')

add(15,'逻辑关系','What is the purpose of the $5 mug scenario?',
 ['To report the author’s verified sale to the reader.','To set up a hypothetical comparison of purchase and resale valuation.','To establish that used mugs always appreciate in market price.','To explain why all mugs cost exactly $5.'],1,
 '五美元杯子的情境有什么作用？',['报告作者与读者已核实交易。','设想购买和转售估值的比较。','确立二手杯市场价格总升值。','说明所有杯子都恰好五美元。'],
 ['A Let’s say 是假设，非真实交易记录。','B 一周后买回需付多少，引出所有权估值。','C 逻辑预期是不应升值，甚至更低。','D 五美元只是设定金额，不是市场通价。当前还没给实验结果。'],
 ['Let’s say I was selling a coffee mug for $5','the value of the coffee mug should not have increased during that week'],
 'endowment effect','禀赋效应','为后续所有权提高主观估值的现象命名，此段先设情境','The example introduces the endowment effect.',['the endowment effect','psychology of ownership'],
 '行为经济学家 Richard Thaler 发现相关现象，称为禀赋效应。假设我以五美元卖杯子，你好心买下。一周后我问能否买回来，若可以，要付多少。按逻辑，杯子这周不该升值——若有什么变化，已经用过的杯子反该低于五美元。')

add(16,'细节','How did typical selling and buying valuations compare?',
 ['The minimum selling price was about half the maximum buying price.','Both prices were always exactly $5.','Participants refused every resale at any price.','The minimum selling price was twice the maximum buying price.'],3,
 '通常最低卖价与最高买价怎样比较？',['最低卖价约为最高买价一半。','两价总是恰好五美元。','任何价格都拒卖。','最低卖价为最高买价两倍。'],
 ['A 比例倒置。','B 例中五美元买却要别人付十美元。','C 愿意出售但要价更高，不是绝对拒售。','D lowest...twice...highest 直接支持；Typically/most 不等于所有个体和所有市场交易。'],
 ['the lowest price participants were willing to sell a possession of their own was twice as much as the highest price they were willing to pay to purchase that same object.'],
 'possession','拥有物；财物','已经属于自己的物品，所有权是比较关键','She valued the possession more once it belonged to her.',['a possession of one’s own','sell a possession'],
 '不过，这类实验发现，多数人想要远多于五美元！通常，参与者愿意出售自己拥有物品的最低价，是愿意购买同一物品的最高价的两倍。同一个五美元买的杯子，他们要别人付十美元。这是所有权心理，也就是禀赋效应。')

add(17,'推断','What kind of value increases after ownership in the author’s explanation?',
 ['The object’s value to its owner.','Its objectively verified market price in every case.','Its production cost after manufacture.','Its value equally to every observer.'],0,
 '作者解释中，拥有后增加的是哪种价值？',['对拥有者自身的价值。','每次都已客观核实的市场价。','制造后生产成本。','对每个旁观者同样增加的价值。'],
 ['A to you 限定主观估值。','B overestimate 表明可能高于他人认可，不是客观市场必升。','C 没谈制造成本变化。','D more valuable than most others would 正显示估值差异。房屋和节目行为是作者的应用解释。'],
 ['the value of that object increases to you.'],
 'overestimate','高估','认为自家房屋价值比别人认可的更高','Owners may overestimate what buyers will pay.',['overestimate value','overestimate how valuable'],
 '一旦拥有某物，它对你的价值就增加。这解释为什么多数人高估自家房价值。因为拥有且熟悉，他们喜欢它，并觉得它比多数别人认为的更值钱——这也是节目夫妻往往选择爱它而不是卖它的另一原因。')

add(18,'细节','Why did consumers plan three different snacks?',
 ['They were forbidden to repeat a snack.','They thought eating the same snack for three days would be boring.','They had already bought all three identical snacks.','They expected the study to last three years.'],1,
 '消费者为何计划三种不同零食？',['不许重复选择。','觉得连续三天同种会无聊。','已经买了三份相同零食。','以为研究持续三年。'],
 ['A 没有禁止重复规则。','B reasoning 直接说 same thing...too boring，想要变化。','C 当前是计划，不是实际购买结果。','D next three days 是三天。品牌清单为示例，非每个人必选菜单。'],
 ['they didn’t think they would want the same thing for three straight days; that would be too boring.'],
 'variety','多样性；变化','计划阶段想要多种零食，避免连续重复','The plan offered more variety than the final purchase.',['want variety','seek variety'],
 '熟悉的吸引力往往也强过多样性。研究让消费者计划未来三天每天吃什么零食，他们倾向选三种不同的，例如第一天抹茶 Kit-Kat，第二天 Reese’s Peanut Butter Cups，第三天 Hershey’s Milk Chocolate。他们觉得不会想连续三天吃同样东西，那太无聊。他们想要变化！')

add(19,'细节','What did consumers tend to buy when purchasing three days’ snacks at once?',
 ['Exactly the three different snacks they had imagined.','Only one snack for all three days.','Three portions of their favorite snack.','A different snack for every member of the research team.'],2,
 '一次买好三天零食时，消费者倾向买什么？',['恰是想象的三种不同零食。','三天只买一份。','三份最喜欢的同一种零食。','给每个研究人员买不同零食。'],
 ['A instead of three different 说明转向重复最爱。','B three 不是一份。','C three of their favorite snack 明示数量和重复。','D 未提给研究团队购买。in my case 是作者示例，不是全体被试同一品牌。'],
 ['they tended to buy three of their favorite snack'],
 'at once','一次性；同时','三天所需在同次购买，并非每天分别买','They bought the week’s supplies at once.',['buy at once','all at once'],
 '然而，令人惊讶的是，当消费者被要求一次买好未来三天零食时，他们倾向买三份最喜欢的同一种——以我为例，三份抹茶 Kit-Kat——而不是三种不同零食。')

add(20,'主旨','What contrast does the author summarize?',
 ['We always dislike imagining new experiences.','Actual choices contain more variety than plans in every case.','People never return to favorite restaurants.','We like variety in principle but often repeat familiar choices.'],3,
 '作者概括什么对比？',['总不喜欢想象新体验。','每次实际选择都比计划多样。','从不重返喜欢的餐厅。','理念上喜欢变化，实际却常重复熟悉选择。'],
 ['A Imagining...exciting 表示想象令人兴奋。','B 当前总结方向相反，tend 也不是每次。','C stick with...again and again 正相反。','D idea/planning 对照 in the end/actually，概括主题。'],
 ['we like the idea of variety, but in the end we tend to choose the same old products.'],
 'stick with','坚持选用；继续采用','实际用餐时反复选熟悉餐厅','They decided to stick with their favorite restaurant.',['stick with a favorite','stick with familiar products'],
 '这里的教训是，我们喜欢多样性的想法，最后却倾向选老产品。喜欢每周换家餐厅的想法，实际上却一次次去最爱的餐厅。在计划阶段，我们追求变化。想象不同零食令人兴奋！')

add(21,'逻辑关系','Why may implementation favor familiarity over novelty?',
 ['Practical costs become salient when an imagined plan turns into an actual choice.','Long flights disappear from consideration when acting.','Every unfamiliar product is proven to fail.','Actual choices involve no effort or uncertainty.'],0,
 '为何实施时可能偏向熟悉而非新奇？',['想象变为实际选择时，现实成本变得显眼。','行动时长途飞行不再需考虑。','每个陌生产品都被证明失败。','实际选择完全不涉及努力或不确定。'],
 ['A become aware...practical factors 给出原因，航程为例。','B long flight 恰进入考虑。','C risky 不是已证明失败。','D trying...too much work 强调费力。sure winner 的引号表示主观把握，不是市场收益保证。'],
 ['we tend to seek familiarity and ease, because we become aware of other practical factors'],
 'implementation','实施；执行','把计划落实成实际选择的阶段','Implementation brought practical costs into focus.',['implementation phase','planning and implementation'],
 '想象去 Alps 徒步令人兴奋！但实施时，我们倾向寻找熟悉与轻松，因为注意到其他现实因素，例如飞去 Switzerland 的长途航程。实际选择时，我们往往选稳妥的“赢家”，不选有风险的产品。我们会满足于熟悉的，因为尝试新东西太费力。')

add(22,'主旨','What tension is expressed between long-term and short-term preferences?',
 ['Both time horizons favor novelty exclusively.','Short-term security can pull us away from the novelty we want over time.','Long-term preferences always demand security alone.','Familiarity is described as emotionally cold.'],1,
 '长短期偏好之间有什么张力？',['两个时间尺度都只选新奇。','短期安全感可能使人远离长期想要的新奇。','长期总只求安全。','熟悉被描写得情绪冷漠。'],
 ['A long view 与 short term 偏好不同。','B want novelty 对照 want security，并指远离心理丰富。','C 颠倒长短期对应。','D warm and fuzzy 是温暖舒服。当前是作者概括，不是每个人每次必然选择。'],
 ['In the long view, we want novelty; in the short term, we want security.'],
 'novelty','新奇；新鲜体验','长期想要的变化，与短期求稳形成对照','Novelty appealed more strongly during planning.',['seek novelty','novelty and security'],
 '从长远看，我们想要新奇；短期内，我们想要安全。熟悉温暖而舒服，却对我们有惊人力量，把我们引离心理丰富。')

add(23,'细节','Which option has the higher expected monetary value in the example?',
 ['The certain £450, with an expected value of £1,000.','Both options have an expected value of £450.','The 50 percent chance of £1,000, with an expected value of £500.','The certain £450, with an expected value of £500.'],2,
 '例中哪项的货币期望值更高？',['确定四百五十镑，期望一千。','两项期望都四百五十镑。','一半概率得一千镑，期望五百。','确定四百五十镑，期望五百。'],
 ['A 确定四百五十的期望仍四百五十。','B 风险选项为 0.5×1000=500。','C 原文给出五百大于四百五十；期望不是保证拿到五百。','D 混淆两项数值。作者按期望值说逻辑上应选前者，不代表所有效用偏好都等价于货币期望最大化；这里只问计算。'],
 ['its expected value is £500, which is greater than the expected value of the latter, £450.'],
 'expected value','期望值','按概率加权的货币均值，不是保证收益','The expected value differs from the guaranteed payment.',['expected monetary value','calculate an expected value'],
 '这还关联更普遍的人类倾向：损失厌恶。Daniel Kahneman 和 Amos Tversky 问参与者：一半概率赢一千镑，与确定赢四百五十镑，喜欢哪个？按作者所说的逻辑，我们应选前者，因为期望五百镑，高于后者四百五十镑。尽管如此，多数人会选后者。')

add(24,'逻辑关系','Why is the certain gain attractive in the author’s description?',
 ['It necessarily exceeds the possible risky gain.','It requires no decision to be made.','It proves that anxiety never affects choices.','It feels pleasant and comfortable compared with a risky, anxiety-provoking possibility.'],3,
 '按作者描述，确定收益为何有吸引力？',['必定高于风险收益可能值。','完全无需作决定。','证明焦虑从不影响选择。','比起有风险且引发焦虑的可能收益，它令人愉快舒适。'],
 ['A even when...could be larger 说明风险项可能更大。','B 两项仍需选择。','C anxiety-provoking 明确提不适。','D sure win 与 hypothetical win 的情绪对比直接支持。作者称 loss aversion，这段只给正向收益的确定性比较；不编造损失条件或视为独自证明损失厌恶。'],
 ['A sure win is pleasant and comfortable. A hypothetical win is risky, anxiety-provoking, and uncomfortable.'],
 'anxiety-provoking','引发焦虑的','形容不确定获益带来的主观不适','An uncertain choice can be anxiety-provoking.',['an anxiety-provoking choice','risky and anxiety-provoking'],
 '我们想要确定收益而非假设可能获得的收益，即使后者可能更大。确定获胜令人愉快舒适。可能的获胜有风险，引人焦虑、不舒服。损失厌恶使我们在许多决策情境中趋于保守。')

add(25,'推断','What consequence follows from always choosing the sure bet in the author’s argument?',
 ['We would miss unexpected experiences by never leaving our comfort zone.','We would guarantee a psychologically rich life.','Unexpected experiences would become certain.','All risky choices would automatically become desirable.'],0,
 '按作者论证，总选稳妥选项会有什么后果？',['不离开舒适区，便错过意外体验。','保证心理丰富人生。','意外体验会变成确定事件。','所有风险选择自动值得做。'],
 ['A 两个 if 连成假设链：总求稳→不出舒适区→不遇意外。','B 与作者担心失去探索相反。','C unexpected 不是把意外确定化。','D 论述代价不等于劝做每种风险行为。保留 always 与条件句，不把有限论证扩大为无条件冒险要求。'],
 ['If we never ventured outside of our comfort zone, we would never encounter anything unexpected.'],
 'venture','冒险前往；大胆迈出','走出熟悉舒适范围，不必等于危险行动','They ventured beyond their usual routine.',['venture outside a comfort zone','venture into unfamiliar territory'],
 '但如果我们总选稳妥的一注，就永远不会走出舒适区。如果永远不走出舒适区，就永远遇不到任何意料之外的事。')

assert len(out)==25 and [q['id'] for q in out]==[t['questionId'] for t in targets]

def persist():
 path=ROOT/'source/short-questions/additional.json';existing=load('source/short-questions/additional.json');byid={q['id']:q for q in existing}
 for q in out:
  if q['id'] in byid:assert byid[q['id']]==q,('Refuse to overwrite changed authoring',q['id'])
  else:existing.append(q)
 path.write_text(json.dumps(existing,ensure_ascii=False,indent=2)+'\n',encoding='utf8',newline='\n')
 review=dict(batchId='batch-029',date='2026-10-23',pdfSha256=b['pdfSha256'],checkedPdfPages=list(range(115,119)),questionIds=[q['id'] for q in out],paragraphs=[dict(id=pid,textSha256=hashlib.sha256(pp[pid]['text'].encode()).hexdigest()) for pid in dict.fromkeys(q['paragraphId'] for q in out)],note='完整PDF115–118原页视觉核对与跨页拼接。搬迁心态实验区别真实迁居，焦虑用词相关不冒充独立随机中介操纵；Bates和购房经历为作者轶事，节目仅限作者观看且非盲评。杯子先设想后述实验典型结果，主观所有权估值非客观市价必升；零食计划与一次购买分开。英镑期望值非保证收益，原书称loss aversion但当前正向收益例不编损失条件、不视作独立证明；条件式舒适区论证不扩为无条件冒险。保留旧题和句界，不宣称逐句证据全覆盖。')
 (ROOT/'source/short-questions/review-chapter10-ownership25.json').write_text(json.dumps(review,ensure_ascii=False,indent=2)+'\n',encoding='utf8',newline='\n')
 print('Saved',len(out),'of 25 individually authored exercises')

if __name__=='__main__':persist()
