"""25 individually authored exercises for frozen targets, PDF pages 38-41.
Preserve printed English, source positions and all previously published questions.
"""
from pathlib import Path
import json,hashlib
ROOT=Path(__file__).resolve().parents[2]
load=lambda p:json.loads((ROOT/p).read_text(encoding='utf8'))
b=load('public/data/book.json');plan=load('public/data/reading-plan.json');targets=load('source/short-questions/batch011-targets.json')['targets']
ss={s['id']:s for s in b['sentences']};pp={p['id']:p for p in b['paragraphs']};out=[]
def add(i,kind,prompt,options,answer,prompt_zh,options_zh,analyses,quotes,word,meaning,context,example,collocations,translation,support='explicit'):
 t=targets[i-1];u=next(u for u in plan['units'] if u['id']==t['readingUnitId']);group=[ss[sid] for sid in u['sentenceIds']];p=pp[u['paragraphId']];text=p['text'][group[0]['start']:group[-1]['end']]
 assert hashlib.sha256(text.encode()).hexdigest()==t['passageSha256'];evidence=[]
 for quote in quotes:
  offset=text.find(quote);assert offset>=0,(i,quote);start=group[0]['start']+offset;end=start+len(quote);touching=[s for s in group if s['start']<end and s['end']>start]
  evidence.append(dict(quote=quote,sentenceIds=[s['id'] for s in touching],sources=list({(r['pdfPage'],r['block']):r for s in touching for r in s['sources']}.values())))
 assert word.lower() in text.lower(),(i,word)
 out.append(dict(id=t['questionId'],version=1,readingUnitId=u['id'],chapterId=u['chapterId'],sectionId=u['sectionId'],paragraphId=u['paragraphId'],sentenceIds=u['sentenceIds'],passage=text,prompt=prompt,options=options,answer=answer,type=kind,promptZh=prompt_zh,optionsZh=options_zh,analyses=analyses,evidence=evidence,vocabulary=[dict(word=word,meaning=meaning,context=context,example=example,collocations=collocations)],translation=translation,support=support,editorialStatus='PDF 第 38–41 页逐题核对；固定连续原句；保留个案、引述与原书历史措辞，不把叙事当作普遍因果或医疗建议'))

add(1,'细节','What did Mossner’s biography establish in Gopnik’s investigation?',
 ['Desideri wrote Hume’s Treatise at the Royal College.','Hume had met Gopnik during her visit to France.','Hume lived in La Flèche while working on his Treatise.','The Jesuit Royal College was located in Rome rather than La Flèche.'],2,
 'Mossner 的传记在 Gopnik 的调查中提供了哪条信息？',['Desideri 在皇家学院写了 Hume 的《人性论》。','Hume 在 Gopnik 访法时见过她。','Hume 写《人性论》时住在 La Flèche。','耶稣会皇家学院位于罗马而非 La Flèche。'],
 ['A 该书作者是 Hume，原句未把写作归于 Desideri。','B 片段是她查阅历史传记，没有两人会面。','C found that 后直接说明地点与写作同时发生。','D She also learned 指 La Flèche 有该学院，D 将地点换掉。'],
 ['Gopnik consulted Ernest Mossner’s biography of Hume and found that Hume lived in La Flèche, France, while working on his Treatise.'],
 'grappling with','努力应对；认真钻研','这里指投入处理难解的历史问题，而非身体搏斗','The team is grappling with a difficult design problem.',['grapple with a question','grapple with uncertainty'],
 'Gopnik 查阅 Ernest Mossner 写的 Hume 传记，发现 Hume 写《人性论》时住在法国 La Flèche。她还得知那里有耶稣会皇家学院。Ippolito Desideri 当时是否也住过那所学院？开始钻研这个问题时，她发现，自从那次抑郁发作以来，自己第一次开始期待明天。')

add(2,'逻辑关系','Why did Gopnik go to the Jesuit archives in Rome?',
 ['An expert told her that the Jesuits kept extensive records.','Mossner’s biography had answered every question about Desideri.','She had been appointed director of the Royal College.','An expert said that no Jesuit records had survived anywhere.'],0,
 'Gopnik 为什么前往罗马的耶稣会档案馆？',['一位专家告诉她，耶稣会详尽记录了各种事情。','Mossner 的传记已回答关于 Desideri 的每个问题。','她被任命为皇家学院院长。','专家说各地都没有留下任何耶稣会记录。'],
 ['A Based on this tip 回指专家说 documented everything，解释行动依据。','B Desideri 的问题更难回答，不是已经全部解决。','C 没有任职信息，Caltech 是学术休假期间的停留地。','D 与 documented everything 的线索方向相反。'],
 ['The expert told her that the Jesuits documented everything. Based on this tip, Gopnik went to the Jesuit archives in Rome.'],
 'archives','档案馆；档案资料','指保存历史记录、供她寻找线索的机构或资料集合','The historian spent a week searching the university archives.',['consult the archives','historical archives'],
 'Ippolito Desideri 的生平颇为神秘，Gopnik 有关他的问题，比有关 Hume 的问题难回答得多。2007 年，她利用学术休假到 Caltech，遇到一位研究十七、十八世纪耶稣会历史的专家。专家告诉她，耶稣会把一切都记了下来。根据这条线索，她去了罗马的耶稣会档案馆。')

add(3,'细节','Which discovery concerning Dolu is reported as an additional link?',
 ['He completed Hume’s Treatise in Rome in 1738.','He accompanied Gopnik to the Royal College in 2007.','He became ambassador to France after retiring from La Flèche.','He had served in Buddhist Siam and retired to La Flèche in 1723.'],3,
 '关于 Dolu，哪一发现被报告为另一条联系？',['他在 1738 年于罗马完成 Hume 的《人性论》。','他在 2007 年陪 Gopnik 前往皇家学院。','他离开 La Flèche 退休后出任驻法大使。','他曾出使信奉佛教的暹罗，1723 年退居 La Flèche。'],
 ['A 写作主体和地点都被替换，原文没有 Dolu 写《人性论》。','B Dolu 是十七、十八世纪线索中的人物，不是她现代旅行的同行者。','C French ambassador to Buddhist Siam 是法国派驻暹罗的大使，非驻法大使。','D 身份、暹罗经历与退居时间地点均对应原句；这是本书所叙研究线索。'],
 ['Dolu, a French ambassador to Buddhist Siam in the 1680s, retired to La Flèche in 1723.'],
 'uncovered','发现；揭示','指在历史调查中找出另一条联系，不表示每种影响机制已被直接观察','The search uncovered a letter in the local archives.',['uncover a link','uncover evidence'],
 '在罗马的最后一天，她得知 Desideri 在 David Hume 身处皇家学院时曾再次造访那里。此外，Gopnik 又发现一条联系：Dolu 在十七世纪八十年代曾任法国驻佛教暹罗的大使，1723 年退居 La Flèche。她的问题得到了回答：David Hume 一定在 La Flèche 读过有关佛教的材料。她把东方哲学与西方启蒙运动联系了起来。')

add(4,'主旨','What broadens Gopnik’s account beyond simply becoming happy again?',
 ['She concludes that curiosity has no place in recovery.','She values varied experiences and the ability to move through sadness as well as joy.','She states that history must replace science in everyone’s life.','She says that solitude and sadness can never be part of a valued life.'],1,
 '什么让 Gopnik 的叙述超出“重新幸福”本身？',['她认为好奇心与恢复无关。','她珍视多样经历，以及穿越悲伤与欢乐的能力。','她说每个人都必须用历史取代科学。','她说孤独和悲伤绝不能属于值得珍视的生活。'],
 ['A 结尾正把 endless curiosity 视为拯救自己的来源。','B as well as、not just happiness 与 endless variety 展示经历和能力的扩展。','C history as well as science 是两者兼容，且属个人叙述，不是所有人的规定。','D make my way through sadness and solitude 承认并能经历它们，非排除。'],
 ['I could make my way through sadness and solitude, not just happiness','the sheer endless variety of human experience.'],
 'solitude','独处；孤独状态','与 sadness 并列，是她说自己能够穿越的经历，不意味着普遍治疗方法','She used a quiet hour of solitude to reflect.',['in solitude','a period of solitude'],
 'Gopnik 在《大西洋月刊》文章结尾说：“我再一次成了格外幸运、幸福的女人，充满不理性的兴奋和日常喜悦。但我不只如此。我发现自己既能爱女性也能爱男性，既能爱历史也能爱科学；我能穿越悲伤与孤独，而不只是幸福……我在人类心灵无穷无尽的好奇，以及人类经验无穷无尽的多样性中，找到了自己的救赎。”')

add(5,'逻辑关系','How does the passage develop after acknowledging Gopnik’s crisis?',
 ['It says that her outlook remained entirely unchanged.','It claims that every crisis necessarily produces wisdom.','It describes changing perspectives that opened new passions and intellectual horizons.','It concludes that the losses prevented all further learning.'],2,
 '承认 Gopnik 的危机之后，片段怎样展开？',['说她的看法完全不变。','声称每场危机必然产生智慧。','描述视角变化，并带出新的热情和知识视野。','认定那些损失阻止了此后所有学习。'],
 ['A continually shifted her perspective 明确有变化。','B 讲的是她的经历，没有 every crisis 的普遍保证。','C 从 loss 经 But 转折，走向新热情、知识视野和智慧。','D discovered new... 与停止所有学习相反。'],
 ['Dramatic life changes brought ups and downs that continually shifted her perspective. The result was that, at midlife, she discovered new passion, fresh intellectual horizons, and wisdom.'],
 'horizons','视野；眼界','intellectual horizons 指能接触与探索的知识范围','Learning a language can broaden intellectual horizons.',['broaden one’s horizons','intellectual horizons'],
 '危机期间，Gopnik 经历了幸福和意义的失落。但并非一切都失去了。剧烈的人生变化带来起伏，不断改变她的视角。结果是，到了中年，她发现了新的热情、新的知识视野和智慧。')

add(6,'细节','What does Gopnik value about the life described in this sentence?',
 ['Its seemingly endless variety.','Its complete absence of change.','Its dependence on professional awards.','Its guarantee of permanent happiness.'],0,
 '这句话说 Gopnik 珍视这种生活的什么？',['仿佛无穷无尽的多样性。','完全没有变化。','依赖职业奖项。','保证永久幸福。'],
 ['A values for its 后直接接 sheer endless variety。','B variety 与无变化相反。','C 本句没有奖项条件。','D psychologically rich 不等于永久幸福保证。'],
 ['a psychologically rich life she values for its “sheer endless variety.”'],
 'variety','多样性；丰富变化','是她珍视心理丰富生活的具体原因，而非某一成就的数量','The course offers a variety of reading experiences.',['endless variety','a variety of experiences'],
 '如今，她过着心理丰富的生活，珍视其中“纯然无尽的多样性”。')

add(7,'细节','Which pairing correctly distinguishes Jobs’s birth and adoptive parents?',
 ['Paul and Clara were his birth parents; Jandali and Schieble adopted him.','His birth parents are not named, but his father’s employer is.','Jandali and Clara were his birth parents; Paul and Schieble adopted him.','Jandali and Schieble were his birth parents; Paul and Clara adopted him.'],3,
 '哪一项正确区分了 Jobs 的亲生父母与养父母？',['Paul 和 Clara 是亲生父母；Jandali 和 Schieble 收养他。','没有给亲生父母姓名，但给了父亲雇主。','Jandali 和 Clara 是亲生父母；Paul 和 Schieble 收养他。','Jandali 和 Schieble 是亲生父母；Paul 和 Clara 收养他。'],
 ['A 颠倒了 Born to 与 adopted by 的两组人。','B 两组父母均被具名，没有父亲雇主信息。','C 把两组中的姓名交叉错配。','D 出生与收养的动词短语分别限定这两组人。'],
 ['Born to Abdulfattah Jandali and Joanne Schieble, he was adopted by Paul and Clara Jobs.'],
 'adopted','被收养','这里指家庭中的收养关系，不是采用某种做法','They adopted a child several years later.',['be adopted by','adopt a child'],
 'Steve Jobs 是另一个选择探索生活的例子。他的亲生父母是 Abdulfattah Jandali 和 Joanne Schieble，后来被 Paul 与 Clara Jobs 收养。他聪明，却讨厌上学。他喜欢和父亲一起待在车库里，修修做做各种东西。')

add(8,'语境词义','What does “threw parties” mean in this sentence?',
 ['Cancelled parties after damaging the lighting.','Hosted parties featuring elaborate electronic light displays.','Threw electronic equipment during school lessons.','Organised formal lectures about stage lighting.'],1,
 '这句话中的 threw parties 是什么意思？',['损坏灯光后取消聚会。','举办配有精心设计电子灯光表演的聚会。','在课堂上扔电子设备。','组织有关舞台灯光的正式讲座。'],
 ['A threw parties 是举办派对，没有取消或损坏。','B throw a party 的固定搭配与 with 后的灯光细节都对应。','C 把 throw 的搭配误读成字面扔东西。','D parties 不是正式讲座，原文也没说授课。'],
 ['he played pranks and threw parties with elaborate electronic light shows.'],
 'elaborate','精心设计的；复杂的','形容电子灯光表演，强调布置或设计细致','The theatre used an elaborate lighting system.',['an elaborate display','an elaborate design'],
 '高中时，他搞恶作剧，还举办配有精心设计的电子灯光表演的聚会。')

add(9,'逻辑关系','What contrast is introduced by “Instead” in the account of the India trip?',
 ['Jobs sought enlightenment but experienced serious illness instead.','Jobs planned to work in an orchard but enrolled in college instead.','Jobs intended to stay a week but remained for forty years.','Jobs abandoned an interest in spirituality before the trip began.'],0,
 '印度之行叙述中的 Instead 引入了什么对比？',['Jobs 寻求开悟，结果却经历严重疾病。','Jobs 打算在果园工作，却上了大学。','Jobs 原计划待一周，却留了四十年。','旅行开始前，Jobs 已放弃精神探索兴趣。'],
 ['A in search of...enlightenment 与 unable to find、got dysentery 构成期望与实际的反差。','B dropping out of college 后在果园工作，不是为去印度而重新入学。','C seven months 是旅行时长，forty pounds 是体重变化，不能错配为四十年。','D became deeply interested 与此相反。'],
 ['He was unable to find enlightenment in India. Instead, he got dysentery and lost forty pounds in a week.'],
 'enlightenment','开悟；精神上的觉悟','此处指旅行所追求的精神体验，不是下一章的历史启蒙运动名称','The memoir describes a search for spiritual enlightenment.',['spiritual enlightenment','seek enlightenment'],
 '大学辍学后，Jobs 在苹果园工作，对东方灵性和 LSD 产生浓厚兴趣。十九岁时，他前往印度，用七个月寻找导师与精神开悟。他在印度没能找到开悟，反而患了痢疾，一周内瘦了四十磅。')

add(10,'观点归属','How should the comparison of intellect and intuition be read here?',
 ['As the narrator’s controlled comparison of every country.','As proof that Jobs abandoned thinking altogether.','As a statement that all forms of intuition are equally valuable.','As Jobs’s later reflection on the perspective he gained from travel.'],3,
 '这里对智力与直觉的比较应怎样理解？',['叙述者对所有国家的对照试验。','Jobs 完全放弃思考的证明。','所有直觉都同样有价值的断言。','Jobs 后来对旅行所获视角的回顾。'],
 ['A Decades later he reflected 引入个人回顾，不是跨国对照实验。','B 对直觉的重视不等于放弃全部思考，本段也无这种声明。','C in some ways...but in other ways is not 明确保留不同价值方面。','D 观点属于引语中的 Jobs，不能扩大成人群能力的实验定论。'],
 ['Decades later he reflected','which is in some ways just as valuable but in other ways is not.'],
 'intuition','直觉','是 Jobs 在个人回顾中与 intellect 对比的认识方式，不是对整个人群的客观测量','Her intuition suggested a solution that she later checked carefully.',['trust one’s intuition','an intuitive judgement'],
 '不过，他确实在旅途中获得新视角。几十年后，他回忆：“对我来说，返回美国比前往印度更让我感到文化冲击。印度乡村的人不像我们这样使用智力，他们更多使用直觉，而且他们的直觉比世界其他地方发展得更充分……在印度的村庄里……他们学到了别的东西，在某些方面同样有价值，在另一些方面却未必。”')

add(11,'语境词义','What does “experiential wisdom” most directly refer to?',
 ['Knowledge derived exclusively from formal academic qualifications.','Understanding gained through experience.','A guarantee that every intuitive judgement is correct.','A rejection of any knowledge acquired through living.'],1,
 'experiential wisdom 最直接指什么？',['完全来自正式学历的知识。','通过经历获得的理解和智慧。','保证每个直觉判断都正确。','拒绝一切从生活中得到的知识。'],
 ['A experiential 指向经历，并未限定学历。','B experience 与 wisdom 的组合就是从经历积累的理解。','C power 是价值评价，不提供 every judgement 的准确保证。','D 将 experiential 的来源方向读反。'],
 ['the power of intuition and experiential wisdom.'],
 'experiential','经验性的；通过亲历获得的','修饰 wisdom，突出智慧来自经历，而非只凭抽象规则','The workshop combines reading with experiential learning.',['experiential wisdom','experiential learning'],
 '“这就是直觉与经验智慧的力量。”')

add(12,'主旨','How does the passage characterise Jobs’s career by age thirty?',
 ['It consisted entirely of setbacks with no major success.','It was uninterrupted progress after he gave up intuition.','It combined major achievement with a severe professional setback.','It ended permanently when the Macintosh was launched.'],2,
 '片段怎样概括 Jobs 三十岁前后的事业？',['只有挫折，没有重大成功。','放弃直觉后一路顺利。','既有重大成就，也有严重职业挫折。','Macintosh 发布时就永久结束了。'],
 ['A smashing success 明确存在成就。','B both his intellect and his intuition 与放弃直觉不符，not always smooth sailing 也否定一路顺利。','C Macintosh 的成功与 1985 年被自己创办的公司解雇形成对比。','D 没有说事业永久结束，只说被解雇。'],
 ['his career was not always smooth sailing.','he had a smashing success with the launch of the Macintosh computer. But in 1985, he got fired from the company he had established.'],
 'smooth sailing','一帆风顺','这里比喻事业顺利，不是航海经历','The project was not all smooth sailing after the first month.',['not all smooth sailing','expect smooth sailing'],
 'Jobs 最终掌握了同时运用智力与直觉的方法。当然，他的事业并非总是一帆风顺。到三十岁时，Macintosh 电脑的发布让他大获成功。但在 1985 年，他被自己创办的公司解雇了。')

add(13,'细节','According to the excerpt, what contrast is made between NeXT and the graphics venture?',
 ['NeXT’s sales disappointed, while the graphics division’s first feature became a major success after years of work.','NeXT immediately released Toy Story, while the graphics division sold computers poorly.','Both ventures are said to have succeeded immediately in January 1986.','The graphics division was bought only after Jobs returned to Apple in 1997.'],0,
 '根据片段，NeXT 与图形业务之间有什么对比？',['NeXT 销售不佳，而图形部门的首部长片在多年后大获成功。','NeXT 立即发布《玩具总动员》，图形部门卖电脑不佳。','两个项目都在 1986 年一月立即成功。','Jobs 1997 年回到 Apple 之后才收购图形部门。'],
 ['A disappointing 对比 huge success，且 nearly ten years 保留漫长过程。','B 将两项业务和作品归属错配。','C 1986 年一月是收购时间，非两个项目即时成功。','D 原书给出收购在 1986 年，重返 Apple 在 1997 年，先后被颠倒。'],
 ['NeXT, but sales were disappointing.','Toy Story (1995), was a huge success, but it took him nearly ten years to get there.'],
 'division','部门；分部','这里指 Lucasfilm 的计算机图形业务部门，而非数学除法','The company created a separate graphics division.',['a graphics division','a company division'],
 '于是他创办自己的电脑公司 NeXT，但销售令人失望。与此同时，他在 1986 年一月买下 Lucasfilm 的计算机图形部门。其首部长片《玩具总动员》（1995）大获成功，但走到这一步用了近十年。1997 年，Jobs 重返 Apple，接着经历传奇般的发展，原书依次写到 2001 年的 iPod、2002 年的 iMac、2007 年的 iPhone 和 2010 年的 iPad。这里保留书中的年份表述。')

add(14,'细节','How old was Jobs when the finding described here was made?',
 ['Thirty, in 1985.','Forty-eight, in 1997.','Fifty-eight, in 2003.','Forty-eight, in 2003.'],3,
 '这句话所述发现发生时，Jobs 多大？',['三十岁，1985 年。','四十八岁，1997 年。','五十八岁，2003 年。','四十八岁，2003 年。'],
 ['A 本句给的是 2003 年、四十八岁，不是此前事业转折的年份年龄。','B 年龄对应，但年份不是 1997。','C 年份对应，年龄却把 forty-eight 错读为五十八。','D In 2003 与 when he was forty-eight 两处直接匹配。'],
 ['In 2003, when he was forty-eight, his doctor found a tumor in his pancreas.'],
 'pancreas','胰腺','此处只用于交代个案中的发现部位，不提供诊断或治疗建议','The textbook includes a diagram of the pancreas.',['the pancreas','a diagram of the pancreas'],
 '2003 年，Jobs 四十八岁时，医生在他的胰腺发现了一个肿瘤。')

add(15,'推断','What mixed assessment does Bowers give of the young Jobs?',
 ['He was consistently patient but lacked any persuasive vision.','He could be impulsive and difficult, yet his vision was compelling.','His vision was compelling because he never disagreed with anyone.','His professional role was to direct human resources in the early 1980s.'],1,
 'Bowers 对年轻时的 Jobs 作了什么有褒有贬的评价？',['他始终耐心，但没有任何有说服力的愿景。','他可能冲动难相处，但愿景很有感召力。','愿景有感召力，因为他从不与人争执。','他在八十年代初的职责是人力资源管理。'],
 ['A impetuous 与 patient 相反，compelling 也否定缺乏有说服力愿景。','B very impetuous and very difficult 与 But your vision was compelling 形成混合评价。','C 原文未说愿景感染力源于从不争执；difficult 还削弱这种读法。','D 人力资源职务是来访者 Ann Bower 的背景，不能归给 Jobs。'],
 ['You were very impetuous and very difficult. But your vision was compelling.'],
 'impetuous','冲动的；急躁行事的','属于 Bowers 对年轻 Jobs 的性格回顾，不是临床诊断','His impetuous decision surprised the rest of the team.',['an impetuous decision','an impetuous person'],
 '临近生命尽头，Steve Jobs 邀请八十年代初曾任 Apple 人力资源主管的 Ann Bower 来到病床旁。他问她：“告诉我，年轻时我是什么样的人？”Bowers 回答：“你非常冲动，也很难相处。但你的愿景很有感召力。”（英文姓名形式按原页保留。）','inference')

add(16,'作者意图','How does Jobs’s response relate to “The journey is the reward”?',
 ['He argues that only the final financial result has value.','He denies that the journey taught him anything.','He acknowledges learning along the way, reinforcing the value of the journey.','He promises that every future journey will avoid difficulty.'],2,
 'Jobs 的回应与“旅程就是回报”有什么联系？',['他主张只有最终财务结果有价值。','他否认旅程教会自己任何东西。','他承认一路学到东西，呼应旅程本身的价值。','他承诺未来每次旅程都没有困难。'],
 ['A 这段谈途中学习，不是只有财务结果。','B did learn 的重复强调确实学到了，而非否认。','C Bowers 的话与 Jobs 对学习的回应相互呼应。','D 没有对未来旅程作零困难保证。'],
 ['The journey is the reward.','I did learn some things along the way'],
 'along the way','在过程中；一路上','把学习放在旅程过程之中，而非仅在终点','We changed our plan and learned new skills along the way.',['learn along the way','discover along the way'],
 '“你告诉过我们：‘旅程就是回报。’后来证明，那是真的。”Jobs 回应：“我确实在一路上学到了一些东西……我确实学到了一些东西。我真的学到了。”','inference')

add(17,'观点归属','What can be established from Jobs’s statement to Isaacson?',
 ['Jobs described his own life as fortunate and felt he had done all he could.','Isaacson independently proved that Jobs had never made a mistake.','Jobs claimed his career had contained no setbacks.','The quotation says everyone who achieves fame will feel fulfilled.'],0,
 '从 Jobs 对 Isaacson 的话中能确定什么？',['Jobs 形容自己人生幸运，并觉得已尽自己所能。','Isaacson 独立证明 Jobs 从未犯错。','Jobs 声称事业没有经历任何挫折。','引语说所有成名者都会感到满足。'],
 ['A I’ve had 和 I’ve done 明确是他自己的回顾。','B told...biographer 是引语来源，不是传记作者独立证明完美。','C lucky 不等于没有 setback，句中也没说 no setbacks。','D 从个人 I 不能扩为所有成名者。'],
 ['I’ve had a very lucky career, a very lucky life. I’ve done all that I can do.'],
 'biographer','传记作者','指记录他人生的 Walter Isaacson，不能把人物的自述误当作者验证结果','The biographer compared interviews with archived letters.',['a biographer of','an authorised biographer'],
 'Jobs 对传记作者 Walter Isaacson 说：“我的事业很幸运，我的人生很幸运。我已经做了自己能做的一切。”')

add(18,'推断','Which interpretation preserves the qualification in this passage?',
 ['Jobs’s inner state is established with complete certainty.','Every psychologically rich life is guaranteed to contain no regret.','Jobs is presented as regretting every earlier decision.','Jobs appeared to have no regrets, which the author links to psychological richness.'],3,
 '哪种理解保留了片段的限定？',['Jobs 的内心状态被完全确定地证实。','每一种心理丰富生活都保证没有遗憾。','Jobs 被描述为后悔此前每个决定。','Jobs 看上去没有遗憾，作者把这与心理丰富联系起来。'],
 ['A seemed to 是观察性判断，不能删成确定证明。','B a defining characteristic 是作者概括，不是每个人都零遗憾的保证。','C no regrets 与后悔每个决定相反。','D 保留 seemed 的不确定性，以及下一句作者建立的联系。'],
 ['Steve Jobs seemed to have no regrets. That is a defining characteristic of a psychologically rich life.'],
 'seemed','似乎；看上去','限制对内心状态判断的确定性，不可无声改成已证实','She seemed satisfied with the revised draft.',['seem to have','seem satisfied'],
 '临终时，Steve Jobs 似乎没有遗憾。这是心理丰富生活的一项标志性特征。','inference')

add(19,'作者意图','What shift does the question introduce?',
 ['From everyday people to an exclusive focus on celebrities.','From outwardly exceptional people to people encountered in ordinary life.','From accomplished people to an argument that ordinary lives cannot be rich.','From personal stories to a controlled experiment already described in this excerpt.'],1,
 '这个问题引入什么转向？',['从普通人转为只关注名人。','从外表看来非凡的人，转向日常生活中常遇到的人。','从有成就者转为论证普通人生不可能丰富。','从个人故事转向本片段已介绍的对照实验。'],
 ['A extraordinary 是前面故事，every day 是将要转向的对象，方向被颠倒。','B What about...every day 把关注范围扩大到普通人。','C 这是开放提问，未否定普通人生的丰富性。','D 片段没有实验设计或实验结果。'],
 ['What about the story of the type of person we all encounter every day?'],
 'outwardly','从外表看；表面上','修饰 extraordinary，指从可见成就观察到的非凡，而非完整内在评价','The building looked outwardly unchanged after the renovation.',['outwardly successful','outwardly calm'],
 '那些是从外表看来非凡、成就突出的人物故事。那么，我们每天都会遇到的那类普通人，又有什么故事呢？')

add(20,'主旨','Which summary best fits Joy’s life before the change described later?',
 ['She frequently moved between towns and enjoyed improving family relations.','Her retirement immediately restored both health and close family ties.','She remained in one home while suffering bereavements, growing distance from family, and declining health.','She left Ohio in 1949 and stopped working when her children were young.'],2,
 '哪项最贴合 Joy 在后来转变之前的生活？',['她频繁搬家，家庭关系日益改善。','退休立即让她恢复健康并与家人亲近。','她长期住在同一住宅，经历丧亲、家庭疏远和健康下降。','她 1949 年离开俄亥俄，孩子年幼时就停止工作。'],
 ['A same house 与频繁搬家相反，drifted apart 也不是关系改善。','B 原文写工作至八十多岁，没有退休立即恢复的情况。','C 住宅稳定与多次失去亲人、家庭距离和健康变化均被涵盖。','D 1949 是结婚年份，there 表示在当地养育孩子；停止工作的年龄也被换掉。'],
 ['Joy Ryan has lived in the same house','she drifted apart from her family and her health declined.'],
 'toiled away','辛苦持续工作','描述她高龄时仍在杂货店劳作，不是悠闲消磨时光','They toiled away in the workshop until evening.',['toil away at a job','toil away for hours'],
 '过去六十七年，Joy Ryan 一直住在俄亥俄州 Duncan Falls 这座只有两个红绿灯的小镇的同一所房子里。她 1949 年结婚，在那里养育三个孩子。她简单的生活中有许多悲剧：丈夫 1994 年死于癌症，十年后她又失去两个成年子女。直到八十多岁，她仍在杂货店辛苦工作，与家人渐渐疏远，健康也在下降。这些相对时间按原书叙述保留。')

add(21,'细节','What interrupts Joy’s monotonous life in this sentence?',
 ['A call from a grandson with whom she had become estranged.','A message from an employer asking her to return to work.','A reunion arranged by a grandson who had always remained close.','A phone call announcing that she had already completed a world tour.'],0,
 '这句话中，什么打断了 Joy 单调的生活？',['一位与她关系疏远的孙子打来的电话。','雇主要求她回去工作的消息。','一直与她亲近的孙子安排的团聚。','告知她已完成环球旅行的电话。'],
 ['A phone call 与 estranged grandson 直接对应事件和来电者关系。','B 没有雇主或返工请求。','C estranged 不是一直亲近，且句中事件是来电。','D 没有已完成环球旅行的信息。'],
 ['a phone call from an estranged grandson interrupted her monotonous life.'],
 'estranged','疏远的；关系隔阂的','形容孙子与她此前的关系，不等于地理上住得远','She hoped to reconnect with an estranged relative.',['an estranged relative','be estranged from'],
 '但后来，一位与她疏远的孙子的来电，打断了她单调的生活。')

add(22,'细节','Why did Brad phone his grandmother, according to the passage?',
 ['To ask her to pay for a new veterinary clinic.','To end a decade in which they had spoken every day.','To teach her how to make banana bread for a classmate.','To seek advice while struggling emotionally after a classmate’s death.'],3,
 '根据片段，Brad 为什么给祖母打电话？',['请她出资开一家新的兽医诊所。','结束双方每天通话的十年。','教她为同学做香蕉面包。','在同学去世后情绪艰难时寻求建议。'],
 ['A veterinary school student 是学生身份，没有筹款或开诊所。','B ten-year stretch of estrangement 是十年疏远，不是天天通话。','C 做香蕉面包是来电时的活动，不是打电话的目的。','D struggling...mental health、shaken 和 for some advice 支持该目的。'],
 ['he had been shaken by the recent suicide of a classmate.','he phoned his grandma for some advice.'],
 'stretch','一段持续的时间','ten-year stretch 指十年这一段持续的疏远时期','After a long stretch abroad, she returned to her hometown.',['a ten-year stretch','a long stretch of time'],
 'Brad Ryan 当时三十四岁。作为一名正在经历心理困扰的兽医专业学生，一位同学最近的自杀让他深受震动。因此有一天，做香蕉面包做到一半时，他给祖母打电话寻求建议。经历长达十年的疏远后，他也是直到不久前才重新开始与她交谈。')

add(23,'逻辑关系','What development followed the discovery made during the phone call?',
 ['Joy’s extensive earlier travels made Brad abandon the mountain trip.','Learning how little Joy had seen inspired a mountain trip that grew into a wider journey of reconciliation.','A completed national-park tour caused the first phone call between them.','They learned that family conflict had ended before they began travelling.'],1,
 '电话中的发现之后，发生了什么发展？',['Joy 先前丰富的旅行经历让 Brad 放弃山区之行。','得知 Joy 未曾见过多少风景，激发了山区旅行，并发展为更广泛的和解之旅。','已经完成的国家公园游览促成双方第一次通话。','他们发现所有家庭冲突在出发前就结束了。'],
 ['A never seen...mountain or ocean 说明见识有限，且确实启程。','B revelation 促发 take a trip，随后从二十八天露营扩大为全国公园和解旅程。','C 原文是电话促发旅行，不能因果倒置。','D wasn’t always pleasant 和 divorce...rift 保留未解决冲突。'],
 ['It inspired them to take a trip to the mountains','became a journey of reconciliation through every national park in the U.S.'],
 'reconciliation','和解；修复关系','这里指祖孙在旅行中修复隔阂，不只是行程规划','A long conversation opened the way to reconciliation.',['a journey of reconciliation','family reconciliation'],
 '这通电话让 Brad 惊讶地发现：Joy 八十五年的人生里，从没见过山或海，更不用说冰川、沙漠、野牛或鲸了。这促使他们出发去山区；起初是在 Smoky Mountains 露营二十八天，后来却成了走遍美国各个国家公园的和解之旅。旅程并非总是愉快：Brad 父母之间难看的离婚，曾造成他与 Joy 的隔阂。')

add(24,'细节','Which experience is matched with the correct location?',
 ['Watching a humpback whale leap in front of their boat in Yellowstone.','Helicoptering over glaciers in the Channel Islands.','Becoming trapped among bison in Yellowstone.','Ziplining in New River Gorge National Park in Alaska.'],2,
 '哪一项把经历与地点匹配正确？',['在 Yellowstone 看座头鲸从船前跃起。','在 Channel Islands 乘直升机越过冰川。','在 Yellowstone 被困在野牛群中。','在阿拉斯加的 New River Gorge 国家公园玩滑索。'],
 ['A 座头鲸对应加州近海 Channel Islands，不是 Yellowstone。','B 冰川直升机对应 Alaska，地点被替换。','C getting trapped in a herd of bison in Yellowstone 逐项匹配。','D New River Gorge 原文在 West Virginia，不在 Alaska。'],
 ['getting trapped in a herd of bison in Yellowstone'],
 'herd','兽群；一群大型动物','a herd of bison 指野牛群，区别于单只动物','A herd of deer crossed the distant hillside.',['a herd of bison','a herd of cattle'],
 '但他们一起在路上度过数小时、化解过去冲突的同时，也共享了非凡经历：在 Yellowstone 陷入野牛群；在加州近海 Channel Islands 看到座头鲸就在船前跃出水面；乘直升机飞越阿拉斯加冰川。Joy 还成为在西弗吉尼亚州 New River Gorge 国家公园玩滑索的最年长者。这一纪录表述按原书当时的叙述保留。')

add(25,'逻辑关系','What contrast does the author draw before introducing Joy’s own words?',
 ['Her visible wonder during the interview contrasts with her earlier plain and disconnected life.','Her earlier life is described as richer in experience than the expedition.','The interview establishes that Joy had remained close to Brad throughout the previous nine years.','The author contrasts Brad’s enthusiasm with Joy’s complete lack of interest.'],0,
 '引入 Joy 自己的话之前，作者作了什么对比？',['访谈中的惊叹神采，与此前平淡而疏远的生活形成对比。','此前的生活被描写成比远征更富经历。','访谈确认 Joy 在此前九年始终与 Brad 亲近。','作者将 Brad 的热情与 Joy 完全没兴趣对比。'],
 ['A sparkle of wonder 对照 plain life、distanced 和 far from...rich。','B far from a psychologically rich one 描述从前，方向被倒置。','C distanced from Brad 明确是疏远，而非始终亲近。','D their eyes 同时包括两人，没有说 Joy 完全没兴趣。'],
 ['the sparkle of wonder in their eyes','Just nine years ago Joy was living a plain life, distanced from Brad and battling depression.'],
 'expedition','远征；考察旅程','指两人描述的长途探索旅行，不限定科学或军事任务','The expedition crossed several remote valleys.',['describe an expedition','set out on an expedition'],
 '看 Brad 与 Joy 接受 PBS《新闻时刻》采访时，人不由得注意到，他们描述远征经历时，眼里闪着惊奇的光。就在九年前，Joy 还过着平淡生活，与 Brad 疏远，并与抑郁抗争。她那时的人生远称不上心理丰富。用她自己的话说：')

assert len(out)==25 and [q['id'] for q in out]==[t['questionId'] for t in targets]

def persist():
 path=ROOT/'source/short-questions/additional.json';existing=load('source/short-questions/additional.json');byid={q['id']:q for q in existing}
 for q in out:
  if q['id'] in byid:assert byid[q['id']]==q,('Refuse to overwrite changed authoring',q['id'])
  else:existing.append(q)
 path.write_text(json.dumps(existing,ensure_ascii=False,indent=2)+'\n',encoding='utf8',newline='\n')
 review=dict(batchId='batch-011',date='2026-10-22',pdfSha256=b['pdfSha256'],checkedPdfPages=list(range(38,42)),questionIds=[q['id'] for q in out],paragraphs=[dict(id=pid,textSha256=hashlib.sha256(pp[pid]['text'].encode()).hexdigest()) for pid in dict.fromkeys(q['paragraphId'] for q in out)],note='完整 PDF 原页视觉复核，包括跨页引语；个案叙事、人物回顾和原书历史措辞分别说明，候选句界不冒充人工最终分句。')
 (ROOT/'source/short-questions/review-chapter04-next25.json').write_text(json.dumps(review,ensure_ascii=False,indent=2)+'\n',encoding='utf8',newline='\n')
 print('Saved',len(out),'of 25 individually authored exercises')

if __name__=='__main__':persist()
