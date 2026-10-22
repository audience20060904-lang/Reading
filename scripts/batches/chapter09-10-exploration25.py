"""25 individually authored exercises for frozen targets, PDF pages 102-107.
Preserve printed English, source positions and all previously published questions.
"""
from pathlib import Path
import json,hashlib
ROOT=Path(__file__).resolve().parents[2]
load=lambda p:json.loads((ROOT/p).read_text(encoding='utf8'))
b=load('public/data/book.json');plan=load('public/data/reading-plan.json');targets=load('source/short-questions/batch026-targets.json')['targets']
ss={s['id']:s for s in b['sentences']};pp={p['id']:p for p in b['paragraphs']};out=[]
def add(i,kind,prompt,options,answer,prompt_zh,options_zh,analyses,quotes,word,meaning,context,example,collocations,translation,support='explicit'):
 t=targets[i-1];u=next(u for u in plan['units'] if u['id']==t['readingUnitId']);group=[ss[sid] for sid in u['sentenceIds']];p=pp[u['paragraphId']];text=p['text'][group[0]['start']:group[-1]['end']]
 assert hashlib.sha256(text.encode()).hexdigest()==t['passageSha256'];evidence=[]
 for quote in quotes:
  offset=text.find(quote);assert offset>=0,(i,quote);start=group[0]['start']+offset;end=start+len(quote);touching=[s for s in group if s['start']<end and s['end']>start]
  evidence.append(dict(quote=quote,sentenceIds=[s['id'] for s in touching],sources=list({(r['pdfPage'],r['block']):r for s in touching for r in s['sources']}.values())))
 assert word.lower() in text.lower(),(i,word)
 out.append(dict(id=t['questionId'],version=1,readingUnitId=u['id'],chapterId=u['chapterId'],sectionId=u['sectionId'],paragraphId=u['paragraphId'],sentenceIds=u['sentenceIds'],passage=text,prompt=prompt,options=options,answer=answer,type=kind,promptZh=prompt_zh,optionsZh=options_zh,analyses=analyses,evidence=evidence,vocabulary=[dict(word=word,meaning=meaning,context=context,example=example,collocations=collocations)],translation=translation,support=support,editorialStatus='PDF第102–107页原页核对；引述/设问/调查偏好/模拟/历史叙事分开；百分比与跳跃次数保持单位，37%模型不当现实保证；Very few保留省略回答原样，图4辅助材料不冒充已结构化'))







add(1,'细节','Which qualification does Ebert make about what films can reveal?',
 ['Every film is remembered equally well.','Reviews reveal only a critic’s travel history.','At least good films can reveal people’s hidden desires and fears.','All films necessarily reveal every viewer’s secrets.'],2,
 'Ebert 对电影能揭示什么作了怎样的限定？',['每部电影都同样记得清楚。','影评只揭示评论家的旅行史。','至少好电影能揭示人隐秘的欲望和恐惧。','每部电影必定揭示所有观众的秘密。'],
 ['A forgot...most 与记得同样清楚相反。','B 引语谈 desire and fear，不是旅行履历。','C At least, the good ones will 保留 good 的范围，且 if you pay attention 给注意条件。','D 把限定的好电影扩大为所有电影及所有人。over 10,000 与 over 6,000 分别是观影和评论数量，不互换；这里是评论家引述，不是实验。'],
 ['what people desire and fear in their deepest secrets. At least, the good ones will.'],
 'deemed','认为；视为','Ebert 选择记住自己认为值得记忆的影片，不等于记住全部','She kept the notes she deemed useful.',['deem worth remembering','deem something valuable'],
 '影评人 Roger Ebert 看过一万多部电影，写过六千多篇影评。多数电影最终忘掉了，但他记住了自己认为值得记住的。Ebert 解释：“如果留心看电影，它们会告诉你人们最隐秘的欲望与恐惧。至少，好电影会。（引语续下段）')

add(2,'主旨','What contrast does the author draw in describing Ebert’s life?',
 ['Limited geographical exploration can coexist with extensive aesthetic and intellectual exploration.','Living in Chicago prevents every form of exploration.','Only people who move between countries can have rich inner lives.','Ebert’s film viewing was primarily a record of physical expeditions.'],0,
 '作者描述 Ebert 人生时作了什么对比？',['地理探索有限，仍可有广泛审美与智性探索。','住在 Chicago 阻止一切探索。','只有跨国迁居者才有丰富内心。','Ebert 看电影主要是在记录实体探险。'],
 ['A might not...physical, geographical 与 certainly...aesthetic and intellectual 构成核心对照。','B but 后明确有另一类探索。','C 否认间接探索，与例子意图相反。','D 引语谈被电影触动，不是实地探险记录。人物生平按原书呈现，不把 might not 改成此人从未离开城市的绝对事实。'],
 ['might not have led a life of physical, geographical exploration, but he certainly led a life of aesthetic and intellectual exploration.'],
 'intellectual','智性的；思想层面的','与 aesthetic 并列，区别于地理移动','The conversation offered an intellectual adventure.',['intellectual exploration','aesthetic and intellectual'],
 '“所以我们去看，盼望那些隐秘之处被触动。”被触动越深，内心越心理丰富。Ebert 生于 Urbana，毕业于 University of Illinois at Urbana-Champaign，成年生活在 Chicago；他或许没有过实体地理探索的人生，却确实过着审美与思想探索的人生。')

add(3,'逻辑关系','What possible effect of immersion is described?',
 ['It guarantees a new life perspective every time.','It can sometimes reveal unforeseen possibilities and a new perspective.','It eliminates all thoughts and emotions.','It requires that the sports outcome have a fixed script.'],1,
 '沉浸可能带来什么作用？',['每次保证新人生视角。','有时让人瞥见未料的可能性与新视角。','消除全部思想情绪。','要求体育结果有固定剧本。'],
 ['A sometimes 不等于每次保证。','B sometimes gives...glimpse...unforeseen possibility 直接支持。','C produces a different set 不是思想情绪归零。','D unscripted world of sports 恰无剧本。作者总结体验特征，不是在当前片段报告新实验效果量。'],
 ['sometimes gives us a glimpse of an unforeseen possibility and a new perspective on life.'],
 'transcending','超越日常的','描述暂时超出惯常体验的感受，不是实体超自然旅行','The performance felt like a transcending experience.',['a transcending experience','transcend typical experience'],
 '沉浸于复杂叙事世界或无剧本的体育世界时，我们被带入，也被改变。这是超越日常的体验，带来不同思想情绪，有时使我们瞥见未料的可能性与人生新视角。简言之，是心理丰富体验。')

add(4,'作者意图','What role do the WWE, park and film examples play?',
 ['They report three randomized experimental conditions.','They rank the activities by their measured benefits.','They establish that all viewers react identically.','They introduce experiences associated with interest, awe or strong emotion.'],3,
 'WWE、公园与电影的例子起什么作用？',['报告三个随机实验条件。','按测得益处排序。','确立所有观众反应一致。','引入可能带来兴趣、敬畏或强烈情绪的体验。'],
 ['A 没有实验设计或随机分组。','B 没有收益排序或量化测量。','C could、might 的例子不能扩大为人人相同。','D 三种体验分别关联有趣、敬畏和感动，随后引出 So what 的追问。最后的疑问不等于这里已证明收益。'],
 ['A WWE match could be an interesting weekend outing.','A visit to a national park might evoke awe and wonder'],
 'outing','外出活动；短途出游','形容周末去看比赛，不是移居或长期探险','The museum visit made a pleasant weekend outing.',['a weekend outing','an interesting outing'],
 '看一场 WWE 比赛可能是有趣的周末外出。去国家公园，也许唤起平常少有的敬畏与惊叹。Schindler’s List 会让你哭个不停。“那又怎样？”')

add(5,'主旨','What doubt is raised about exploration?',
 ['Whether every activity has already been shown to be harmful.','Whether Pascal personally attended all these events.','Whether these experiences offer benefits beyond filling time and avoiding boredom.','Whether people can ever feel bored at all.'],2,
 '这里对探索提出什么疑问？',['每种活动是否已被证明有害。','Pascal 是否亲自参加过这些活动。','这些体验除了打发时间、避免无聊，还有没有益处。','人是否可能无聊。'],
 ['A genuine benefits 是追问，不是已证明有害。','B would have called 是作者设想的哲学归类，不是 Pascal 的行程。','C Other than filling...genuine benefits 与 point of exploration 概括质疑。','D avoid boredom 已承认无聊这一可能。设问提出研究动机，不能把怀疑读成作者已宣布全部无益。'],
 ['Other than filling people’s time to avoid boredom, do these activities have any genuine benefits?'],
 'diversions','消遣；转移注意的活动','片段借哲学家的概念质疑是否只是打发时间','The games offered diversions during the long journey.',['mere diversions','activities as diversions'],
 '你也许会这样问，尽管刚读完上一章。这些活动不都是哲学家 Blaise Pascal 可能称作“消遣”的东西吗？除了填满时间、避免无聊，它们有什么真正益处？换句话说，探索有什么意义？')

add(6,'细节','What did Krebs and colleagues test in the great tits?',
 ['Whether the birds could identify every species of plant.','Whether the birds would know where to forage when two vegetation patches differed in food availability.','Whether the birds preferred cities to all vegetation.','Whether all birds in four regions had identical body lengths.'],1,
 'Krebs 及同事在大山雀中测试什么？',['是否能识别所有植物种类。','两片植被食物供应不同时，是否会知道在哪里觅食。','是否喜欢城市胜过所有植被。','四地区全部鸟的体长是否相同。'],
 ['A 研究问题是 forage，不是植物分类能力。','B two patches...differ...availability of food 直接描述任务。','C 没有城市选择条件。','D about five inches 是物种背景，并非测所有个体一样长。know 的引号也不证明鸟具有与人完全相同的主观认知。'],
 ['tested whether the great tits will “know” where to forage when two patches of vegetation differ in terms of availability of food.'],
 'forage','觅食','鸟在不同食物供应的植被区域寻找食物','The birds forage near the edge of the wood.',['forage for food','know where to forage'],
 '大自然也许有答案。大山雀 Parus major 属山雀科，约五英寸长，常见于欧洲、北非、中东和中亚。英国动物学家 John Richard Krebs 及同事测试，当两片植被的食物供应不同，大山雀是否会“知道”去哪里觅食。')

add(7,'细节','How did exploration differ when the food gap was smaller?',
 ['The birds explored more, averaging over forty hops before settling.','They always stopped after exactly ten hops.','They explored less because the better patch was obvious.','Forty percent of the birds refused to choose any patch.'],0,
 '食物供应差距较小时，探索怎样不同？',['探索更多，定下来前平均跳四十多次。','总在恰好十跳停止。','因为优势明显而探索更少。','百分之四十的鸟拒绝选择。'],
 ['A small...10 percent difference 对应 over forty hops on average。','B about ten 是差距大时，about 也不是精确十次。','C 差距小反而 a lot more。','D forty 是跳跃次数，不是鸟的百分比。50%与10%是食物供应差异，不能和行为次数或样本比例互换。'],
 ['When the difference in food availability was small','they explored a lot more (over forty hops on average)'],
 'exploited','利用；持续使用已发现的资源','这里是找到较优觅食点后留在那里利用，不是道德意义的剥削','After testing several routes, the team exploited the most reliable one.',['explore then exploit','exploit a better food patch'],
 '当一片明显优于另一片，例如食物供应差50%，大山雀只探索少许，约十跳，就找出更好的一片并留在那里“利用”它。差距较小时，例如10%，它们探索多得多，平均四十多跳，才定在稍好的一片。')

add(8,'同义改写','Which summary preserves the comparison with computer simulations?',
 ['The birds followed the simulated ideal perfectly in every observation.','The simulations showed that exploration never depends on food availability.','The scientists replaced actual observations with imaginary birds only.','The observed choices closely matched the ideal simulation, with exploration adjusted to the circumstances.'],3,
 '哪种概括保留了与计算机模拟的比较？',['每个观察中鸟都完美符合模拟。','模拟表明探索绝不随食物供应变。','研究只用想象的鸟取代实际观察。','观察选择非常接近理想模拟，探索程度按处境调整。'],
 ['A almost identical 不等于完全无例外。','B adjusted...depending on...availability 明确会调整。','C compared...actual experimental data 同时有真实数据。','D closely matched 保留 almost，且保留策略随资源差异变动。这里是鸟类任务，不证明所有人的选择都最优。'],
 ['the great tits’ choices were almost identical to the ideal simulated behaviors.','adjusted the degree of exploration depending on the levels of food availability'],
 'instinctively','本能地','作者描述鸟采用策略的方式，不是鸟理解概率公式的证据','The animal instinctively searched for shelter.',['instinctively use a strategy','respond instinctively'],
 '科学家还运行计算机模拟，把模拟最优结果与大山雀实际实验数据比较。令人惊讶的是，鸟的选择几乎与理想模拟行为相同。也就是说，大山雀本能地采用理想的先探索后利用觅食策略，并按不同区域食物供应调整探索程度。')

add(9,'细节','What varied among the 585 UVA students surveyed in fall 2019?',
 ['Whether every student had actually completed four years of follow-up.','Their experimentally assigned financial resources.','Preference for a psychologically rich college life according to year of college.','The number of bird-feeding patches allocated to them.'],2,
 '2019年秋调查的585名 UVA 学生中，什么随年级不同？',['是否人人完成四年追踪。','随机分配的财务资源。','对心理丰富大学生活的偏好。','分配给他们的鸟类觅食区数量。'],
 ['A 本段是同一时期不同年级比较，没有四年追踪。','B 没有财务干预。','C degree...chose...rich life...differed by...year 直接对应。','D 鸟是类比，不是学生任务的实体食物区。would like 问理想偏好，不是测实际生活已多丰富。'],
 ['we asked 585 UVA students what kind of college life they would like to have','differed by what year of college they were in.'],
 'leans toward','倾向于','按定义，丰富人生偏向探索；不是完全排斥利用','Her approach leans toward experimentation.',['lean toward exploration','lean toward a strategy'],
 '按定义，心理丰富人生偏向“探索”而非“利用”策略。像大山雀，人似乎也按处境改变策略。2019年秋，我们问585名 UVA 学生想过什么大学生活，发现对心理丰富人生的选择程度随年级明显不同。')

add(10,'细节','What ranking is reported for first-year students?',
 ['Meaning first, happiness second, richness last.','Richness first, happiness second, meaning last.','Happiness first, meaning second, richness last.','All three were exactly equal for first-year students.'],1,
 '大一学生的偏好顺序是什么？',['意义第一、幸福第二、丰富最后。','丰富第一、幸福第二、意义最后。','幸福第一、意义第二、丰富最后。','大一三者完全相等。'],
 ['A 将大四最偏意义的方向移给大一。','B first-year...rich most popular...happy second...meaningful last 逐项对应。','C happy top 属大二，不是大一。','D 大一有明确顺序。正文对大三“同样吸引”是概括；原页图4为33.9%、33.9%、32.1%，不能解释成三项精确相等或据此编精确相等题。'],
 ['Among first-year students, a psychologically rich college life was the most popular option, a happy life second, and a meaningful life last.'],
 'sophomores','大学二年级学生','与first-year、juniors、seniors组成不同年级的比较','The seminar included freshmen and sophomores.',['among sophomores','college sophomores'],
 '大一最偏好心理丰富大学生活，幸福第二，意义最后。大二最偏幸福，其次心理丰富。大三三种选择吸引力相近。大四最偏意义，幸福紧随其后。')

add(11,'作者意图','How does the author interpret the changing student priorities?',
 ['As proof that all people should explore forever without commitment.','As evidence that no students ever seek meaning.','As a tendency to explore first and later commit to meaningful goals.','As proof that the same students were experimentally tracked for four years.'],2,
 '作者怎样解读学生重点的变化？',['证明所有人都应永远探索不投入。','证明没有学生追求意义。','倾向先探索，之后投入有意义目标。','证明同一批学生被实验追踪四年。'],
 ['A once they figure out...dedicating themselves 包含后续投入。','B achieving a meaningful life 明确包括意义。','C 此项概括作者的 explore-then-exploit 解读。','D 段落没有同人四年追踪；这里仍是对年级偏好差异的解释。seem、tend 保留倾向，不能当每个人必遵循的阶段定律。'],
 ['their priorities seem to shift toward dedicating themselves to achieving a meaningful life.','tend, like the great tits, to use the explore-then-exploit strategy.'],
 'priorities','优先事项；重视的目标','指学生较重视哪类人生，不等于已经达到目标','Her priorities shifted after she discovered a new interest.',['priorities shift toward','changing priorities'],
 '早期许多大学生偏好探索。不过，像大山雀，一旦弄清想做什么，他们的重心似乎会转向投入有意义人生。我们发现，UVA 学生往往像大山雀，采用先探索后利用策略。')

add(12,'作者意图','Why does the author turn to Todd and Miller?',
 ['They specialize in optimal exploration-exploitation strategies across decision situations.','They have already proved every UVA student follows an optimal rule.','They deny that choices can ever be studied scientifically.','They personally arranged all of Kepler’s interviews.'],0,
 '作者为什么转向 Todd 与 Miller？',['他们专门研究多种决策中的最优探索利用策略。','已证明每个 UVA 学生都遵循最优规则。','否认选择可科学研究。','亲自安排 Kepler 的全部访谈。'],
 ['A as they are the experts...various decision-making situations 说明求助专业知识的理由。','B 前两句正在问是否最优，尚非确认。','C 研究专家身份与否认研究相反。','D 文章讲述历史故事，不是两人亲历安排。better position 表示相对更有资格回答，不是地理位置更近。'],
 ['they are the experts on the optimal explore-exploit strategy in various decision-making situations.'],
 'in a better position','更有条件；更有资格','此处指专业知识使两人更能回答，而非实体座位','The specialist is in a better position to assess the evidence.',['in a better position to answer','be well positioned to explain'],
 '但 UVA 学生采取的是最优策略吗？一般人会用最优探索利用策略吗？认知心理学家 Peter Todd 与 Geoffrey Miller 比我更有资格回答，因为他们是各种决策中最优探索利用策略的专家。他们写过一篇有趣、信息丰富的文章 From Pride and Prejudice to Persuasion: Satisficing in Mate Search。')

add(13,'细节','How is Kepler’s search for a second wife described?',
 ['He immediately chose the first person without speaking to others.','He interviewed eleven women over eleven years.','He courted and interviewed eleven women methodically over two years.','He conducted a randomized experiment on the women’s mathematical ability.'],2,
 '原文怎样描述 Kepler 寻找第二任妻子？',['立即选第一个人，从未接触其他人。','用十一年访谈十一人。','用两年有系统地追求、访谈十一人。','随机实验测试她们数学能力。'],
 ['A methodical search 与多位访谈否定立即停下。','B two-year period，不是十一年。','C eleven women 与两年、系统搜索完全吻合。','D 历史择偶叙事不是数学能力随机试验。第一任婚姻与死因均按本书叙述，不作独立传记核实。'],
 ['He thoroughly courted and interviewed eleven women over a two-year period.'],
 'methodical','有系统的；有条理的','形容寻找伴侣的步骤和投入，不等于无感情的实验','She used a methodical approach to compare the options.',['a methodical search','a methodical approach'],
 '该章以德国天文学家、数学家 Johannes Kepler 的故事开始。第一任妻子1611年死于霍乱；本书说，因为第一段婚姻不幸福，他并未过度哀悼。很快他有系统地寻找新妻，两年中仔细追求、访谈十一名女性。')

add(14,'细节','Why did Kepler not marry the fourth candidate in this account?',
 ['His friends opposed her lack of status.','She rejected him after he made her wait too long.','He had already married her before meeting the fifth candidate.','She lacked the education he demanded in an experiment.'],1,
 '按这段叙述，Kepler 为什么没娶第四位？',['朋友反对她地位低。','他让她等太久，她拒绝了求婚。','见第五位之前已娶第四位。','她缺少他在实验中要求的教育。'],
 ['A friends urged...high status 说明朋友赞成且她地位高。','B rejected...because...wait too long 直接给出原因。','C 原文说转而选个人最喜欢的第五位，并非先娶第四位。','D well educated 描述第五位，且没有教育实验。is thought to have provided 是历史评价的保留语，不是确立婚姻导致四部作品的实验因果。'],
 ['she rejected his proposal because he made her wait too long.'],
 'dowry','嫁妆','描述朋友看重第四位的经济条件，并非 Kepler 最终决定的唯一依据','The historical account described a large dowry.',['a large dowry','status and dowry'],
 '朋友劝他选第四位，她地位高、嫁妆多。但因他让她等太久，她拒绝求婚。他转而选自己最喜欢的第五位。她虽非最富家庭出身，却教育良好；人们认为她提供了有利家庭条件，使 Kepler 又完成四部重要著作。')

add(15,'主旨','How does the author summarize the outcome of Kepler’s search?',
 ['A wide and energetic search ended in a choice the author describes as successful.','Kepler refused every candidate and remained unmarried.','The search conclusively proved the 37 percent rule in all relationships.','The search was described as hurried and entirely joyless.'],0,
 '作者怎样总结 Kepler 搜索的结果？',['广泛且积极的寻找，以作者称成功的选择结束。','拒绝所有候选人，终身未再婚。','确凿证明所有关系适用37%规则。','搜索仓促且毫无乐趣。'],
 ['A took his time、explored widely、vigor 与 chose...well、happily married 一致。','B 与 happily married 相反。','C 单个人物叙事未检验普遍模型。','D brought excitement and vigor 与仓促无乐趣相反。这里保持作者评价，不推断所有广泛搜索必定幸福。'],
 ['Kepler took his time, explored widely, brought excitement and vigor to the search, and chose his second wife well. He was happily married.'],
 'vigor','活力；精力','与 excitement 并列描述投入搜索的状态','She approached the new project with vigor.',['excitement and vigor','bring vigor to a task'],
 'Kepler 不慌不忙，广泛探索，带着兴奋与活力寻找，也妥善选择第二任妻子。他婚后幸福。')

add(16,'细节','What decision is the secretary problem designed to model here?',
 ['How to hire every person in a candidate pool.','How to choose a spouse by measuring physical height only.','How to calculate the exact number of works Kepler would write.','How to select the best hire through a sequence of interviews.'],3,
 '这里的秘书问题模拟什么决策？',['如何雇用候选池每个人。','只量身高选择配偶。','算 Kepler 将写几部作品。','通过连续面试选出最佳雇员。'],
 ['A a particular individual，不是每人都雇。','B 没有身高测量。','C 作品数属上一叙事，不是模型目标。','D best possible hiring decision...series of interviews 明示。Kepler probably 懂概率是作者推测，不证明他实际按某条规则行事。'],
 ['make the best possible hiring decision based on a series of interviews.'],
 'pool','候选集合；候选池','指有限的一组候选人，不是游泳池','The committee interviewed candidates from a large pool.',['a set pool of candidates','a candidate pool'],
 'Kepler 是当时领先的数学家，所以他大概很懂概率定理。统计学有个著名的“秘书问题”：通过一系列面试作最佳聘用决定。研究者测量，从既定候选池中面试多少人之后，人会决定聘某一位。')

add(17,'细节','What happens during the first 37 percent of interviews under the stated rule?',
 ['All of these candidates are hired immediately.','They are rejected, forming a benchmark for judging later candidates.','Interviewers may hire earlier rejected candidates at any later time.','Exactly 37 percent of participants are required to follow the rule.'],1,
 '按这里的规则，前37%面试期间发生什么？',['所有这些候选人立即被雇。','拒绝这些人，并以其中最佳者作为后续比较基准。','可随时回头聘已拒绝者。','恰好37%的参与者被要求遵循规则。'],
 ['A saying no to all 正相反。','B first37...no...better than best of first37，支持先建立基准。','C cannot go back 明确不可召回。','D 37%是候选序列截点，不是参与者遵循率。模型有不可回头、二元决定等条件，不能当所有真实择偶情境的通用保证。'],
 ['interview the first 37 percent of candidates (i.e., saying no to all of them)','better than the best of the first 37 percent.'],
 'binary','二元的；只有两种结果的','这里每一步只能yes或no，不是多种中间聘用决定','The task required a binary yes-or-no response.',['binary decisions','a binary choice'],
 '你不能回到先前面试者，必须不断作是或否的二元决定，直到一次“是”，即聘用。计算机模拟显示，这里的最优策略是先面试前37%候选人、全部拒绝；之后再判断新候选人是否比前37%中的最佳者更好。这叫“37%规则”。有多少人实际遵循呢？')

add(18,'语境词义','What quantity does “Very few” express?',
 ['Every member of a group.','Exactly zero, with no exceptions.','A very small number, not necessarily zero.','A majority of the group.'],2,
 'Very few 表示怎样的数量？',['群体每一位。','精确为零，毫无例外。','数量极少，但不一定为零。','群体大多数。'],
 ['A few 不是全体。','B few 不等于 none，不能擅自改成零。','C very 加强“少”的程度，保留可能存在少数。','D 与大多数相反。本片段是承接上一问句的省略回答；保留既有短段与ID，不冒充独立完整句，也不在这两个词里编出精确百分比。'],
 ['Very few.'],
 'few','很少的；几乎没有多少','省略回答描述人数很少，不能据此算具体比例','Very few participants selected that option.',['very few people','only a few'],
 '极少数。（承接上一短段问句的省略回答。）')

add(19,'细节','Why might the hypothetical dating search be unattractive?',
 ['It has financial and psychological costs, and the preferred person may reject the proposal.','It involves no cost and guarantees mutual acceptance.','It allows every previous candidate to be recalled with certainty.','It guarantees that all 100 people will agree to marry.'],0,
 '为什么假设中的择偶搜索可能不吸引人？',['有金钱和心理成本，最中意者也可能拒绝。','毫无成本且保证相互接受。','保证可召回每个之前候选人。','保证100人都愿意结婚。'],
 ['A not only financially but also psychologically 与 might say no 对应两类限制。','B costly、might say no 均否定这种保证。','C 原文没保证别人可召回。','D potential mates 不是全部已同意的人。100/37是设想，不能当真实实验人数或婚恋建议的精确处方。'],
 ['dating so many people is costly, not only financially but also psychologically.','that person might say no to your proposal.'],
 'costly','代价高的','不仅花钱，还包括情绪和时间投入，不只商品价格','A long search can be costly in time and effort.',['financially and psychologically costly','a costly search'],
 '假设有100个潜在对象，你会至少分别约会其中37人一次，再按37%规则找最佳可选者吗？大概不会。因为约会这么多人不只财务代价高，心理代价也高。即使终于觉得找到“那个人”，对方也可能拒绝求婚。')

add(20,'主旨','What selection criterion does the author suggest in this practical contrast?',
 ['The highest ranking regardless of the other person’s feelings.','Any person chosen before mutual interest is known.','A guarantee of finding the mathematically best individual.','Someone one likes sufficiently who also returns that liking.'],3,
 '在这个现实对比中，作者提出什么选择标准？',['不论对方感受，只取最高排名。','未知道相互兴趣就随便选人。','保证找到数学意义的最佳个体。','自己足够喜欢、对方也喜欢自己的人。'],
 ['A likes you back 明确保留对方意愿。','B 相互喜欢不是完全未知就随便选。','C well enough 是足够好，不是保证全局最优。','D like well enough who likes you back 概括双方条件。Then...would be wasted 承接被拒绝的假设，不是每次广泛搜索都无价值。'],
 ['the first person you like well enough who likes you back.'],
 'settle on','选定；作出选择','在搜索后选择足够合适且相互喜欢的人，不等于安家定居的字面动作','After comparing the options, they settled on a workable plan.',['settle on a choice','settle on the first suitable option'],
 '那样，广泛搜索就会白费。因此，选定第一个你足够喜欢、也喜欢你的人，显得更有道理。')

add(21,'逻辑关系','What does the low-cost laboratory evidence add to the discussion?',
 ['It shows all participants use the optimum when costs are small.','It proves financial costs are the only cause of early choice.','Even when extra search costs are minimized, only some use the optimal strategy.','It eliminates every difference between laboratory choices and real dating.'],2,
 '低成本实验室证据补充说明什么？',['只要成本低，所有人就用最优策略。','证明财务成本是过早选择的唯一原因。','额外搜索成本尽量降低时，也只有部分人用最优策略。','消除实验选择与真实约会的一切差异。'],
 ['A only a fraction 不是全体。','B 低成本下仍偏离，不能把成本定为唯一原因。','C minimize...Even...little...fraction 的让步关系完整。','D artificial lab 与约会的成本形式仍有区别，不能完全等同。翻卡片只是降低搜索成本的例子，不是现实关系实验。'],
 ['Even in an artificial lab experiment where the search cost is little, only a fraction of people use the optimal search strategy.'],
 'minimize','尽量减少；使降至最低','减小额外搜索成本，不是证明所有成本绝对为零','The design aimed to minimize the effort needed for another choice.',['minimize search costs','minimize additional costs'],
 '不过，心理学家确实做过许多秘书问题实验，尽量减少额外搜索成本，比如只需再翻一张卡，而不必安排约会时间地点。即使在搜索成本很小的人造实验室任务中，也只有一部分人使用最优搜索策略。')

add(22,'细节','What deviation did humans and pigeons share across the experiments?',
 ['They selected too soon, before considering the ideal number of options.','They consistently waited beyond the optimal point.','Pigeons followed the rule more often than students.','Exactly 37 percent of each species followed the rule.'],0,
 '这些实验中，人和鸽子共有怎样的偏离？',['尚未考虑理想数量就过早选择。','一贯等到超过最优时点才选。','鸽子比学生更常遵循规则。','两个物种都恰有37%遵循。'],
 ['A They made selections too soon...before...ideal number 明示共同方向。','B too soon 与等太久相反。','C 学生30%，鸽子17%，不是鸽子更高。','D 37%是规则中的候选截点；30%和17%才是本段遵循率。跨三次实验的共同偏离不等于两物种全部认知能力相同。'],
 ['They made selections too soon, before considering the ideal number of options.'],
 'consistently','一贯地；稳定地','failed to consistently use 不等于没有任何个体曾用过最优解','The group did not consistently choose the same strategy.',['consistently use a strategy','fail to consistently apply'],
 '例如，实验条件下只有30%大学生遵循37%规则，不过略好于鸽子的17%。Herbranson 及同事总结：“三次实验中，鸽子与人都没能稳定采用秘书问题的最优解。更重要的是，两物种以同样方式偏离：还没考虑理想数量的选项，就过早作选择。”')

add(23,'作者意图','What argument does the author make about real mate selection?',
 ['Laboratory results guarantee the best partner for every individual.','Early selection may be even more likely when real searches involve high costs and possible rejection.','More exploration is said to harm everyone’s choices.','The passage reports a new randomized marriage trial.'],1,
 '作者对真实择偶提出什么论证？',['实验结果保证每人选到最佳伴侣。','现实搜索成本高、可能被拒，过早选择也许更易发生。','更多探索被说成损害所有人选择。','片段报告新的随机婚姻试验。'],
 ['A 没有对每个人的保证。','B If...little cost...then...real...high cost and rejection probability 是作者外推论证。','C For most...better choices 与所有人受害相反；most 也不等于全部。','D 这里是论证和经济学家观点，非新增随机婚姻干预。不能把论述改写为针对个人的无限约会处方。'],
 ['far more likely to make a selection too early in a real mating task with high search cost and rejection probability.'],
 'suboptimal','次优的；非最优的','指按所讨论目标未达最优，不是婚姻必失败的标签','The rushed process produced a suboptimal choice.',['suboptimal choices','a suboptimal strategy'],
 '如果搜索成本很小的任务里人都过早选择，那么成本高又可能被拒的真实择偶中，就更可能太早选择。经济学家确实认为，探索不足会使择偶不够理想。对多数人而言，探索越多，选择越好。')

add(24,'细节','In the explore-exploit terminology, how is the first group characterized?',
 ['They exploit before doing any exploration at all.','They search for fewer people over less time than the second group.','They are experimentally assigned to divorce quickly.','They explore for longer before committing to a choice.'],3,
 '按探索利用术语，第一组有什么特征？',['完全没探索就先利用。','比第二组花更少时间接触更少人。','被随机分配迅速离婚。','投入选择前先探索较久。'],
 ['A explored...before exploiting 明示先后。','B first group...long time...several，与短时少人组相反。','C analyzed data 是数据分析，不是随机分配离婚。','D 长期接触多人后结婚，对应 long exploration。当前片段还未报告后续婚姻稳定结果，不能提前写入证据。'],
 ['the first group explored for a long time before exploiting'],
 'trade-off','权衡；取舍','继续探索与投入既定选择之间的取舍，不表示二者永远不能先后结合','The team considered the trade-off between searching longer and acting now.',['exploration-exploitation trade-off','a trade-off in decisions'],
 '心理学家 Samantha Cohen 与 Peter Todd 分析 CDC 收集的全国代表性数据，了解真实婚姻决策中的探索利用取舍。他们发现，有人长期与多人约会才结婚，有人短期接触少数人就安定。按探索利用术语，第一组探索较久再利用，第二组探索较短再利用。')

add(25,'逻辑关系','Why does the passage argue for more exploration in the real mating context?',
 ['Many potential partners differ only slightly, unlike a case with one obviously superior choice.','One partner is assumed to be overwhelmingly better in every real situation.','Computer simulations are said to prove all marriages have identical outcomes.','Exploration is claimed to have no cost under any circumstances.'],0,
 '为什么片段主张现实择偶中多探索？',['许多潜在对象差别较小，不像一个选项明显最优的情形。','假设每个真实情境都有一人压倒性更好。','模拟证明所有婚姻结果一致。','探索在任何情况下都无成本。'],
 ['A if one...far better 的例外，与 But...many...slight differences 的现实描述形成论证。','B 把反事实条件例外当成所有现实。','C 模型错误率不等于所有婚姻结果一致。','D 前文已讨论成本，本片段没有否认成本。当前是模型与动物文献引出的推论，不把尚未在本片段出现的CDC结果倒灌成因果证明。'],
 ['there are many potential mates with only slight differences in overall value.'],
 'insufficient','不足的；不充分的','指未探索够多选项，与永远越多越好的无限要求不同','Insufficient information made the comparison difficult.',['insufficient exploration','insufficient information'],
 '动物行为文献与计算机模拟都提示，探索不足会带来更多错误。当然，若一个对象远优于其余，就无需探索，选择很明显。但真实择偶中，许多潜在对象的总体差别不大。这意味着，安定选择某一人之前，较多探索会更好。')

assert len(out)==25 and [q['id'] for q in out]==[t['questionId'] for t in targets]

def persist():
 path=ROOT/'source/short-questions/additional.json';existing=load('source/short-questions/additional.json');byid={q['id']:q for q in existing}
 for q in out:
  if q['id'] in byid:assert byid[q['id']]==q,('Refuse to overwrite changed authoring',q['id'])
  else:existing.append(q)
 path.write_text(json.dumps(existing,ensure_ascii=False,indent=2)+'\n',encoding='utf8',newline='\n')
 review=dict(batchId='batch-026',date='2026-10-22',pdfSha256=b['pdfSha256'],checkedPdfPages=list(range(102,108)),questionIds=[q['id'] for q in out],paragraphs=[dict(id=pid,textSha256=hashlib.sha256(pp[pid]['text'].encode()).hexdigest()) for pid in dict.fromkeys(q['paragraphId'] for q in out)],note='完整PDF102–107原页视觉核对，含图4和跨页文字。Ebert为引语/作者阐释，探索收益先作设问；鸟类数据与模拟比较保留almost，UVA585人为2019不同年级偏好调查非四年追踪；图4大三33.9/33.9/32.1与正文等吸引不作精确相等。Kepler按本书叙述，probably/is thought限定保留，37/30/17%含义分开，Very few是既有省略短段。统计与模型不当现实关系保证，末段完整审阅含尚未配题CDC后续结果。')
 (ROOT/'source/short-questions/review-chapter09-10-exploration25.json').write_text(json.dumps(review,ensure_ascii=False,indent=2)+'\n',encoding='utf8',newline='\n')
 print('Saved',len(out),'of 25 individually authored exercises')

if __name__=='__main__':persist()
