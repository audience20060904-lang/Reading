"""25 individually authored exercises for frozen targets, PDF pages 98-102.
Preserve printed English, source positions and all previously published questions.
"""
from pathlib import Path
import json,hashlib
ROOT=Path(__file__).resolve().parents[2]
load=lambda p:json.loads((ROOT/p).read_text(encoding='utf8'))
b=load('public/data/book.json');plan=load('public/data/reading-plan.json');targets=load('source/short-questions/batch025-targets.json')['targets']
ss={s['id']:s for s in b['sentences']};pp={p['id']:p for p in b['paragraphs']};out=[]
def add(i,kind,prompt,options,answer,prompt_zh,options_zh,analyses,quotes,word,meaning,context,example,collocations,translation,support='explicit'):
 t=targets[i-1];u=next(u for u in plan['units'] if u['id']==t['readingUnitId']);group=[ss[sid] for sid in u['sentenceIds']];p=pp[u['paragraphId']];text=p['text'][group[0]['start']:group[-1]['end']]
 assert hashlib.sha256(text.encode()).hexdigest()==t['passageSha256'];evidence=[]
 for quote in quotes:
  offset=text.find(quote);assert offset>=0,(i,quote);start=group[0]['start']+offset;end=start+len(quote);touching=[s for s in group if s['start']<end and s['end']>start]
  evidence.append(dict(quote=quote,sentenceIds=[s['id'] for s in touching],sources=list({(r['pdfPage'],r['block']):r for s in touching for r in s['sources']}.values())))
 assert word.lower() in text.lower(),(i,word)
 out.append(dict(id=t['questionId'],version=1,readingUnitId=u['id'],chapterId=u['chapterId'],sectionId=u['sectionId'],paragraphId=u['paragraphId'],sentenceIds=u['sentenceIds'],passage=text,prompt=prompt,options=options,answer=answer,type=kind,promptZh=prompt_zh,optionsZh=options_zh,analyses=analyses,evidence=evidence,vocabulary=[dict(word=word,meaning=meaning,context=context,example=example,collocations=collocations)],translation=translation,support=support,editorialStatus='PDF第98–102页原页核对；视觉丰富与心情分开，perhaps不改已测，体育为原书历史叙事，Proust是文学引述；题目文字证据独立于图像识别，保留所有旧题和原句'))







add(1,'细节','What did participants do after answering the first question about the drawing?',
 ['They received an explanation of the correct interpretation.','They immediately rated their happiness without seeing another question.','They drew a different beer glass from memory.','They moved to another page asking what else they could see.'],3,
 '回答关于画的第一个问题后，参与者做了什么？',['得到正确解释的说明。','不再看其他问题，立即评幸福。','凭记忆另画一杯啤酒。','到另一页回答还能看见什么。'],
 ['A 没有先给正确解读的步骤。','B moved on...new question 明示还有新问题；心情评价并非此时已给结果。','C wrote their answer 是写回答，不是重画。','D After...another page...Now, what else do you see 按序对应。本题依靠文字程序，不要求识别未在此片段显示的图像。'],
 ['After they wrote their answer, they moved on to another page with a new question: “Now, what else do you see?”'],
 'foam','泡沫','啤酒杯顶端泡沫的形状可形成另一种观看方式','Foam covered the top of the drink.',['foam on top','a layer of foam'],
 '看 Noma Bar 画的装满啤酒的细长杯子，即上方图2。顶部泡沫的形状，从某个角度看像张脸。一项实验中，我们在屏幕显示图像，问参与者：“你看见什么？”他们写完答案，进入另一页回答新问题：“现在，你还看见什么？”')

add(2,'细节','Which sequence of perceptions is described?',
 ['Everyone sees a face first and never sees a glass.','Most first see beer, and many later see a face.','Only the researchers see either object.','All participants report the same view at every stage.'],1,
 '原文描述怎样的观看顺序？',['所有人先见脸，永不见杯。','大多数先见啤酒，后来许多人见脸。','只有研究者能看见任一物体。','所有阶段人人看法相同。'],
 ['A first 是 beer，且 most/many 不是 everyone。','B Most...first 与 afterward, many 对应。','C 没有只有研究者的限定。','D Depending on your perspective 表示可有不同观看方式。不能把许多人转变改成每个人必转变。'],
 ['Most see a glass of beer first. But afterward, many see a face'],
 'afterward','随后；之后','标记第一次识别之后可能出现第二视图，不是同时或事前','She noticed the pattern only afterward.',['but afterward','notice something afterward'],
 '大多数人先看见一杯啤酒。随后，许多人看见一张脸——眼睛、鼻子和嘴。视角不同，你看见啤酒或脸。')

add(3,'细节','What was removed to make the altered image?',
 ['The entire beer glass.','All of the foam and the background.','The bubble that had functioned as an eye.','The question asking participants what they saw.'],2,
 '修改图像时移除了什么？',['整个啤酒杯。','全部泡沫与背景。','原先充当眼睛的气泡。','询问看见什么的问题。'],
 ['A altered image 仍是 glass filled with beer。','B 只说明 removed the bubble，不是全泡沫与背景。','C bubble...“eye” 直接给出改变。','D same two questions 保留程序。文字提供了可答证据，无需凭图猜测额外改动。'],
 ['I removed the bubble that was the “eye” in the first drawing.'],
 'altered','改动过的；修改后的','指图像细节变化，整体啤酒杯仍保留','The altered image retained most of the original design.',['an altered image','slightly altered drawings'],
 '另一组看的是修改过的啤酒杯图，即图3。一切相同，只是泡沫不再像脸，因为我移除了第一幅图中充当“眼睛”的气泡。也就是说，修改图只是装满啤酒的杯子。我们问同样两个问题：“你看见什么？”')

add(4,'细节','What was reported about seeing a face in the altered-image group?',
 ['None of them saw a face.','Most saw a face before noticing the beer.','Every participant reported both views.','They were explicitly instructed to draw faces.'],0,
 '修改图组关于看见脸的报告是什么？',['没有人看见脸。','大多数先见脸再见啤酒。','每个人都报告两种视图。','被明确要求画脸。'],
 ['A none of them saw a face 明示该组结果。','B most...glass of beer 指看啤酒，不是先看脸。','C 与 none 相反。','D write about what they saw 不是画脸指令。none 限定这组实验参与者，不应扩大为任何人在任何修改图上都不可能发现新物体。'],
 ['Again, most of them saw a glass of beer. But none of them saw a face.'],
 'one at a time','一次一个；逐个','第一组逐幅观看图底关系图，而非整组图同时呈现','The images appeared one at a time.',['show drawings one at a time','view one at a time'],
 '然后问：“你还看见什么？”同样，大多数看见一杯啤酒，但没人看见脸。第一组参与者一次看一幅图底关系图，并写下看见什么。')

add(5,'细节','What did all participants do after writing about the drawings?',
 ['They reported only their childhood reading habits.','They were told which group had won the experiment.','They altered the secondary objects themselves.','They evaluated the drawings and reported their current moods.'],3,
 '写完图像观察后，所有参与者做什么？',['只报告童年阅读习惯。','获知哪个组赢了实验。','自己修改次要物体。','评价图画并报告当前心情。'],
 ['A 将前文阅读调查的指标移入当前实验。','B 没有比赛胜负或获胜组。','C 第二组看已修改的图，不是自己修改。','D evaluate the drawings 与 report current moods 是后续两类测量。这里只列测量，尚未给结果，不能先断言哪组更幸福。'],
 ['Then all the participants were asked to evaluate the drawings and report their current moods.'],
 'secondary object','次要物体；第二种可识别对象','图中另一种视图被移除，非指另摆一件实体物品','Without the small detail, the secondary object was harder to recognize.',['lack the secondary object','identify a secondary object'],
 '第二组看略经修改的一系列图——基本与第一组相同，却缺少第二种物体——并写出看见什么。随后，所有参与者评价图画，报告当前心情。')

add(6,'主旨','What main experimental result is reported?',
 ['Clear single-view drawings were rated richer than figure-ground drawings.','Figure-ground drawings were experienced as richer and more interesting than clear-main-figure drawings.','Every participant reported identical visual experiences.','The researchers proved that initial puzzlement was the only cause of the ratings.'],1,
 '报告的主要实验结果是什么？',['单一清晰图比图底关系图更丰富。','图底关系图比主图明确的图更丰富、有趣。','所有人报告完全相同视觉体验。','证明最初困惑是评分的唯一原因。'],
 ['A 比较方向反了。','B psychologically richer 后以 interesting 等词解释，比较对象是 clear main figure。','C between the two groups 明说有差异。','D Perhaps they were puzzled 是作者对过程的可能解释，非已测得的唯一机制。不能把本段未报告的幸福差异补进结果。'],
 ['participants who saw the figure-ground drawings found them psychologically richer','than those who saw the drawings with a clear main figure.'],
 'clichéd','陈套的；缺乏新意的','less clichéd 指图像体验较不老套，不是说参与者人格有新意','The unexpected ending felt less clichéd than the usual formula.',['less clichéd','boring and clichéd'],
 '一系列实验中，看图底关系图的参与者觉得图更心理丰富，即更有趣、耐人寻味、清新，较少无聊与陈套；相比之下，另一组看的是主图明确的图。细微视觉差异带来两组很大心理差异。图底关系组在一幅图中看见多个东西。也许他们起初困惑，隐约觉得有点不同。')

add(7,'逻辑关系','What distinction between visual experience and mood is emphasized?',
 ['The control group was less happy in every experiment.','Both groups failed to identify anything in the images.','The figure-ground experience differed, but the groups were equally happy in the reported comparisons.','A clearer second view necessarily caused permanent happiness.'],2,
 '强调视觉体验与心情之间什么区别？',['控制组每次都更不幸福。','两组都没认出任何物体。','图底关系体验不同，但报告比较中两组一样快乐。','第二视图更清楚必定造成永久幸福。'],
 ['A as happy as 否定控制组更不幸福。','B secondary view 被识别，控制图也清楚。','C Notably...did not evoke different moods 与 as happy as 支持丰富性不等于幸福差异。','D 没有永久结果，更没有确定因果链。相似心情不能改成参与者完全没有情绪。'],
 ['the figure-ground drawings did not evoke different moods in any of the experiments. Participants in the control condition were as happy as those in the figure-ground condition.'],
 'unambiguous','没有歧义的；明确的','控制图的单一解读与多视图图画形成对照','The sign gave an unambiguous instruction.',['clear and unambiguous','an unambiguous figure'],
 '那种感觉随后变成对第二视图更确定的识别。相比之下，控制组看的是单一、清晰、无歧义的图。值得注意的是，在这些实验中，图底关系图没有引发不同心情；控制组与图底关系组同样快乐。')

add(8,'语境词义','What does “an aesthetic spice” mean here?',
 ['A small element of complexity adding richness to perception.','A literal ingredient added to the beer.','A method for making every image simpler.','A guarantee of greater happiness outside the task.'],0,
 '这里 aesthetic spice 是什么意思？',['少量复杂性为感知增添丰富性。','真正加入啤酒的调味料。','使每幅图更简单的方法。','任务之外更幸福的保证。'],
 ['A slight addition...enhanced...richness 构成调味般的比喻。','B as if 标记类比，不是真实配料。','C addition of complexity 并非变简单。','D 当前只谈 visual and perceptual richness，不给生活幸福保证。'],
 ['a slight addition of complexity and unexpectedness enhanced visual and perceptual richness'],
 'unexpectedness','意外性；出乎预期的性质','图像多一种解读带来的新鲜，而非危险事件','Unexpectedness made the simple demonstration engaging.',['complexity and unexpectedness','a touch of unexpectedness'],
 '即便如此，稍微增加复杂性与意外性，就增强视觉与感知丰富性，仿佛加入审美的调味。')

add(9,'细节','Why are sports described as a powerful source of drama?',
 ['All spectators interpret them in exactly the same way.','Their outcomes are fully scripted in advance.','They always end in victory for the favored team.','Their outcomes are not scripted and remain uncertain.'],3,
 '为什么体育被说成戏剧性的强大来源？',['所有观众解读相同。','结果事先完整写好。','总由被看好者获胜。','结果没有剧本，仍不确定。'],
 ['A For some...For others 承认不同体验。','B not scripted 直接否定。','C never really know 否认胜负保证。','D mainly because...not scripted 是明示解释。作者区分消遣与更丰富观看，不等于所有运动观看都产生同样效果。'],
 ['mainly because the outcome is not scripted. You never really know what will happen.'],
 'pastime','消遣；打发闲暇的活动','指部分人仅把体育当消遣，与更多戏剧意义对照','Watching the local team became a weekend pastime.',['a simple pastime','sports as a pastime'],
 '对一些人，体育只是消遣，是 Kant 所说“除了让时间不知不觉流逝，没有更进一步旨趣的游戏”。对另一些人，体育不止娱乐。它特别能产生戏剧性，主要因为结果没有剧本；你无法真正预知会发生什么。')

add(10,'作者意图','What do the missed groundball and unexpected basketball plays illustrate?',
 ['That high-level sport is free of mistakes and surprises.','That the passage independently verifies every historical detail.','That high-level sport can combine unpredictable drama and beauty.','That every spectacular play guarantees a championship.'],2,
 '漏接滚地球与意外篮球表现说明什么？',['高水平体育没有失误和惊喜。','本片段独立核实每项史实。','高水平体育能结合难料的戏剧性与美。','每次精彩表现都保证冠军。'],
 ['A 漏接和 least expected 强调意外，不是无失误。','B 题目按原书叙述理解，不声称另行核验赛程细节。','C 结尾 There is drama and beauty 概括这些例子。','D 比赛反转例子不保证每个精彩动作都夺冠。'],
 ['There is drama and beauty in high-level sports.'],
 'improbable','看似不可能的；发生概率很低的','形容出人意料的扣篮，不是断言物理上绝不可能','The player completed an improbable shot under pressure.',['improbable dunks','an improbable play'],
 '当你以为已赢下 World Series，明星一垒手却可能漏接普通滚地球，让球从双腿间穿过；转眼对手就赢了冠军——书中说这发生在1986年。还有 Magic Johnson 不可思议的传球，以及 Michael Jordan、LeBron James 在最意想不到时刻的惊人扣篮。高水平体育有戏剧性，也有美。')

add(11,'同义改写','Which paraphrase preserves the claim about watching sports?',
 ['Watching must replace every other aesthetic activity.','Watching can be interpreted as an aesthetic experience.','Only athletes who physically compete can experience aesthetics.','Every sporting event has been proved to enrich every viewer.'],1,
 '哪种改写保留了观看体育的主张？',['观看必须替代其他所有审美活动。','观看可以被理解为审美体验。','只有实际参赛者才有审美体验。','已证明每场比赛都丰富每位观众。'],
 ['A 没有替代一切的要求。','B could be construed as 对应 can be interpreted as，保留可能的解释。','C watching 指观看者，并非仅参赛者。','D could 不是所有人的实验保证。书名与年份给出处，不等于本句报告实验。'],
 ['watching sports could be construed as an aesthetic experience'],
 'construed','被理解；被解释为','将观看体育看作审美体验的一种概念解释','The gesture could be construed as an invitation.',['be construed as','could be construed as an experience'],
 '的确，观看体育可被理解为审美体验；哲学家 Stephen Mumford 在2012年 Watching Sport: Aesthetics, Ethics and Emotion 中对此有详细描述。')

add(12,'细节','What personal incentive for coming to the U.S. does the author mention?',
 ['The chance to watch NBA and MLB games.','A guarantee of joining the Rockets as a player.','The opportunity to coach Hakeem Olajuwon.','A promise that every season would end in a championship.'],0,
 '作者提到来美国的什么个人吸引因素？',['观看 NBA 和 MLB 的机会。','保证加入 Rockets 当球员。','执教 Hakeem Olajuwon 的机会。','每个赛季都夺冠的承诺。'],
 ['A one of...incentives...chance to see NBA and MLB 明示。','B see 是观看，不是加入球队。','C favorite player 不等于自己执教。','D 没有冠军承诺，且 one of 说明不是移居唯一动机。此处是个人叙事，不作为所有人的移居理由。'],
 ['one of the real incentives to come to the U.S. was a chance to see the National Basketball Association (NBA) and Major League Baseball (MLB).'],
 'incentives','吸引因素；激励','让作者想来美国的因素之一，不是雇佣奖金','Access to the library was one incentive for moving there.',['an incentive to come','one of the incentives'],
 '对我而言，来美国的真正吸引因素之一，是能看 NBA 和 MLB。下面是我最喜欢的 Houston Rockets 在1995年的戏剧性转折。他们由我最喜欢的 Hakeem Olajuwon 带领，在1993–1994赛季拿下队史首个 NBA 冠军。')

add(13,'有限推断','What did the opening nine-game winning streak lead people to expect?',
 ['An immediate end to the Rockets’ season.','Proof that the team could no longer lose a game.','That the previous championship had never happened.','Another championship season seemed likely.'],3,
 '开局九连胜让人们产生什么预期？',['赛季立即结束。','证明球队再也不会输。','此前冠军从未发生。','看起来又会是冠军赛季。'],
 ['A started out 与结束相反。','B looked...like 是印象，不是不能输的证明。','C another 承接已有冠军，并未否认。','D it looked...like another championship season 支持当时预期。本句尚未给最终结果，不能用后文夺冠倒灌成这里已确定。'],
 ['it looked to everyone like another championship season.'],
 'in a row','连续地；接连地','九场连胜，中间没有被本句说成夹着败局','The team won three matches in a row.',['win games in a row','nine games in a row'],
 '第二年，即1994–1995赛季，Rockets 开局连赢九场，大家都觉得这看起来又是一个冠军赛季。',support='limited-inference')

add(14,'细节','Which regular-season contrast is stated before the first playoff round?',
 ['Houston was third with 60–22; Utah was sixth with 47–35.','Both teams finished sixth with identical records.','Houston was sixth with 47–35; Utah was third with 60–22.','Houston had already been eliminated before facing Utah.'],2,
 '季后赛首轮前，常规赛表现有什么对照？',['Houston 第三、60胜22负；Utah 第六、47胜35负。','两队都第六且战绩相同。','Houston 第六、47胜35负；Utah 第三、60胜22负。','Houston 对 Utah 前已被淘汰。'],
 ['A 把球队与战绩、种子互换。','B 记录和种子均不同。','C Rockets...47-35...six 与 Jazz...three...60-22 精确对应。','D faced...first round 说明仍在赛中。常规赛记录不等于当前系列赛比分。'],
 ['a 47-35 record and were the number six seed','the number-three-seeded Utah Jazz, who ended the regular season with a 60-22 record'],
 'seed','种子排名','这里指季后赛排位，不是植物种子或胜场数','The sixth seed faced a higher-ranked team.',['the number six seed','a number-three-seeded team'],
 '但随后他们进攻挣扎。Rockets 最终以47胜35负结束常规赛，成为西部季后赛第六种子；这个收官令人失望。季后赛首轮对阵第三种子 Utah Jazz，对手常规赛60胜22负，阵容有 Karl Malone 和 John Stockton。')

add(15,'细节','How did game four change the first-round series?',
 ['Utah completed the series with its third win.','Houston won and tied the series at two games each.','Houston went ahead by three games to one.','Both teams were eliminated after a draw.'],1,
 '第四场怎样改变首轮系列赛？',['Utah 拿第三胜，结束系列赛。','Houston 获胜，把系列赛扳成2比2。','Houston 以3比1领先。','两队打平后都被淘汰。'],
 ['A one more win 是 Utah 原本的条件，however 后未实现。','B Houston won...tied at 2 to 2 直接说明。','C 把扳平错作3比1领先。','D tied 指系列赛各赢两场，不是单场平局或双淘汰。第五场回 Utah 只给地点，当前片段未给其结果。'],
 ['in game four Houston won: the series was now tied at 2 to 2.'],
 'tied','打平的；持平的','系列赛两队胜场相同，并非篮球单场无胜负','After four matches, the series was tied.',['a tied series','tied at two to two'],
 'Utah 起初在五场制系列赛以2比1领先，再赢一场就晋级。然而第四场 Houston 赢了，系列赛变为2比2。第五场，他们回到 Utah。')

add(16,'细节','What result answers the question about Utah’s home-court advantage?',
 ['Houston beat Utah 95 to 91.','Utah beat Houston 95 to 91.','The teams finished with identical scores.','The game was cancelled because Utah was at home.'],0,
 '关于 Utah 主场优势的设问，后文给出什么结果？',['Houston 以95比91击败 Utah。','Utah 以95比91击败 Houston。','两队得分相同。','因为 Utah 主场而取消比赛。'],
 ['A Nope 后明确 Houston beat Utah 95 to 91。','B 对调胜负双方。','C 95与91不相同。','D 没有取消的信息。该场主场方失利不能推广为主场优势从来无效。'],
 ['Houston beat Utah 95 to 91.'],
 'home court advantage','主场优势','设问指回到 Utah 主场是否使对方更有利，不保证胜利','Home court advantage did not guarantee a win.',['Utah’s home court advantage','have home court advantage'],
 'Utah 的主场优势会终结 Rockets 的赛季吗？没有，Houston 以95比91击败 Utah。')

add(17,'细节','What did Houston need to do after Phoenix took a 3–1 lead?',
 ['Win just one of the remaining three games.','Win three games in succession to take the series.','Lose one game and still advance automatically.','Return to the first-round five-game series.'],1,
 'Phoenix 以3比1领先后，Houston 需要怎样做？',['剩余三场只赢一场。','连赢三场才能拿下系列赛。','再输一场仍自动晋级。','回到首轮五场制系列赛。'],
 ['A 原文明说 three games in a row，不是一场。','B had to win...in order to win 直接给必要条件。','C one more loss...over 表示再输即结束。','D 当前second round seven-game series，不是回首轮。此时仍是必须完成的任务，不能提前写成已经三连胜。'],
 ['They had to win three games in a row in order to win the series.'],
 'in order to','为了；以便','连接必要的三连胜与赢下系列赛的目的','They needed another point in order to advance.',['in order to win','had to do something in order to'],
 '季后赛第二轮，Houston 面对第二种子 Phoenix Suns。Phoenix 在七场制系列赛3比1领先。再输一场，Houston 的赛季就结束。他们必须连赢三场，才能赢下系列赛。')

add(18,'细节','Which sequence follows the missed free throws in the account?',
 ['Houston lost game five and immediately left the playoffs.','Phoenix won games five, six and seven.','Houston won every remaining game in Phoenix, including game six.','Game five went to overtime; Houston won it in Phoenix, then won game six at home and game seven in Phoenix.'],3,
 '按这段叙述，罚球失手后发生哪一顺序？',['Houston 输第五场，立即离开季后赛。','Phoenix 连赢第五、第六、第七场。','Houston 剩余比赛都在 Phoenix 赢，第六场也在那里。','第五场加时，Houston 在 Phoenix 赢；第六场主场赢，第七场再在 Phoenix 赢。'],
 ['A Houston won game five 与输球相反。','B won 的主语是 Houston，不是 Phoenix。','C game six at home 明确区别场地。','D 加时、第五场结果及两场地点均按原文顺序对应。uncharacteristically 是反常失手，不是球员通常总罚失。'],
 ['Houston won game five in Phoenix','They won game six at home and game seven in Phoenix.'],
 'uncharacteristically','一反常态地；不符合平时表现地','限定 Barkley 此次两罚不中并非惯常状态','The normally accurate player uncharacteristically missed twice.',['uncharacteristically missed','act uncharacteristically'],
 'Phoenix 有机会赢第五场，但明星前锋 Charles Barkley 在常规时间接近结束时一反常态地两罚不中，比赛进入加时。最终 Houston 在 Phoenix 赢第五场，后来的一切便成为历史：第六场主场获胜，第七场在 Phoenix 获胜。西部决赛中，Houston 击败第一种子 San Antonio Spurs。')

add(19,'语境词义','What does “swept” imply about the finals series?',
 ['The teams alternated victories until the last game.','Houston was defeated without winning a game.','Houston won the series without losing a game.','The championship was postponed for a year.'],2,
 'swept 暗示总决赛系列赛怎样结束？',['两队轮流获胜直到最后。','Houston 一场未赢就败。','Houston 一场未输就赢下系列赛。','冠军延后一年才决出。'],
 ['A swept 的体育语境不是胜负交替。','B swept 的主语 they 是 Houston，且 won championship。','C 横扫指系列赛全胜，方向与夺冠一致。','D 没有延期的信息。consecutive 指连续夺冠，不代表整个赛季每场都赢。'],
 ['they swept the Orlando Magic in the finals and won their second consecutive NBA championship.'],
 'consecutive','连续的；接连的','指第二个连续 NBA 冠军，不是生涯所有比赛不败','The club won two consecutive titles.',['a second consecutive championship','consecutive titles'],
 '随后，他们在总决赛横扫 Orlando Magic，连续第二次赢得 NBA 冠军。')

add(20,'作者意图','Why does the author emphasize both comeback scores?',
 ['To stress how extraordinary the sixth seed’s route to the title seemed.','To prove that every sixth seed must win the championship.','To claim Houston was never at risk of elimination.','To describe two games played under an identical series format.'],0,
 '作者为何同时强调两次落后比分？',['突出第六种子夺冠路径有多非凡。','证明每个第六种子必夺冠。','声称 Houston 从未面临淘汰。','描述两个完全相同赛制下的单场比赛。'],
 ['A unbelievable、practically unheard of 与两种赛制逆转，共同突出罕见路径。','B 单一叙事不证明未来所有低种子必胜。','C many moments...thought it was over 承认多次危险。','D best of five 和 best of seven 是不同系列赛，不是两个同制单场。教练引语是鼓舞性表达，不是概率定律。'],
 ['coming back from 1-2 in a best of five series AND from 1-3 in a best of seven series is practically unheard of.'],
 'underestimate','低估','教练劝人别低估冠军的意志，不是说输赢已注定','Do not underestimate how difficult the final stage may be.',['underestimate the heart of a champion','never underestimate'],
 '第六种子赢下一切已经难以置信，又从五场制1比2和七场制1比3落后逆转，几乎闻所未闻。季后赛许多时刻，我以为结束了，但没有。主教练 Rudy Tomjanovich 的名言是：“永远别低估冠军的心！”')

add(21,'语境词义','What does “underdog” refer to in the author’s response?',
 ['The top seed expected to win easily.','A team that was guaranteed to lose every match.','A less-favored competitor whose victory broadens the sense of what is possible.','A team that had never won any game before 1995.'],2,
 '作者回应中的 underdog 指什么？',['被预计轻松获胜的第一种子。','保证每场必输的球队。','较不被看好的竞争者，其获胜拓展可能性的认识。','1995年前从未赢任何比赛的队。'],
 ['A 与 number one seed 的对照方向相反。','B 不被看好不等于注定输。','C underdog victory 与 expands...possible 结合低种子背景支持。','D 当前没有从未赢球的履历。richer than 是作者观赛评价，不证明所有观众必有相同体验。'],
 ['An underdog victory like this expands your view of what is possible.'],
 'underdog','不被看好的一方；弱势竞争者','在此指低种子且屡次濒临淘汰的球队，不是绝无胜算','The underdog surprised everyone by reaching the final.',['an underdog victory','support the underdog'],
 '1995年的季后赛感人、戏剧性十足，比看第一种子夺冠心理丰富得多。这样的不被看好者获胜，拓宽你对可能性的认识。')

add(22,'逻辑关系','How are aesthetic and firsthand experiences distinguished?',
 ['Aesthetic experiences can never feel real or immediate.','Aesthetic experiences involve interpretation, yet can still feel real and immediate under suitable circumstances.','Firsthand adventures require no personal involvement.','Every exposure to art automatically gives all viewers the same experience.'],1,
 '审美体验与亲身体验怎样区分？',['审美体验永不真实、直接。','审美涉及解释，但合适条件下仍可真实而直接。','亲身冒险不需本人参与。','每次接触艺术都自动使人人体验相同。'],
 ['A nonetheless 后明确 real, immediate。','B own interpretation 与 under the right circumstances 两部分都保留。','C firsthand personal adventures 指本人直接参与。','D own interpretation 和条件限定不支持人人自动相同。本书结论不能把每次看艺术都当成保证增益。'],
 ['It requires our own interpretation','we can still have very real, immediate experiences through arts and sports under the right circumstances.'],
 'Nonetheless','尽管如此；然而仍然','承认与亲历冒险不同，仍保留审美体验的真实性','The journey was indirect. Nonetheless, the encounter felt immediate.',['nonetheless, we can','nonetheless have an experience'],
 '因此，读诗或小说、看电影或艺术品、观看令人敬畏的运动表现，会增加心理丰富性。这需要我们自己解释诗人、小说家、电影人或艺术家的信念与表达，并认识运动员非凡行动中的美。从这意义说，它不同于个人冒险得到的亲身体验。尽管如此，合适条件下，我们仍能通过艺术和体育拥有非常真实、直接的体验。')

add(23,'主旨','What role does Proust assign to art in this quotation?',
 ['Enabling access to another person’s view beyond one’s own.','Providing scientific proof of inhabited landscapes on the moon.','Ensuring that all artists see an identical universe.','Replacing every other person’s viewpoint with our own.'],0,
 'Proust 在引语中赋予艺术什么作用？',['越出自身，接触他人的视角。','科学证明月球有有人居住的风景。','保证所有艺术家看同一宇宙。','用自身视角取代别人的。'],
 ['A emerge from ourselves 与 know what another person sees 概括核心。','B moon 是陌生程度的文学比较，不是天文学证据。','C not the same as our own 强调差异。','D 是认识他人，而非强迫别人同我。Through art alone 是 Proust 引语的文学论断，不当实验已排除所有其他途径。'],
 ['to emerge from ourselves, to know what another person sees of a universe which is not the same as our own'],
 'emerge from','从……走出；超越','比喻超出自我视野，非实际身体离开自身','The story helped him emerge from his narrow viewpoint.',['emerge from ourselves','emerge from a limited perspective'],
 '在 In Search of Lost Time 最后一卷 Time Regained 结尾，Proust 更广泛谈艺术作用：“唯有通过艺术，我们才能走出自我，知道别人所见的宇宙；那不同于我们的宇宙，没有艺术，其中风景对我们仍会像可能存在于月球上的风景一样陌生。（引语续下段）')

add(24,'作者意图','What is conveyed by the image of artists’ worlds still sending radiance centuries later?',
 ['Artists literally continue emitting physical light after death.','All artistic differences disappear over time.','Proust had traveled physically through infinite space.','Distinct artistic visions can remain accessible long after their creators’ time.'],3,
 '艺术家的世界数世纪后仍送来光辉，这个意象传达什么？',['艺术家死后真的持续发物理光。','艺术差异随时间全消失。','Proust 实际游历过无限太空。','独特艺术视野在创作者年代之后仍可被接触。'],
 ['A light、radiance 是艺术影响的比喻，非物理发光测量。','B worlds more different 强调独特性。','C 后句说他常病且少远行，没有太空旅行。','D centuries after...still...special radiance 表现跨时间仍能感受各自视野。不可把想象的多世界改成地理旅行统计。'],
 ['worlds which, centuries after the extinction of the fire from which their light first emanated','send us still each one its special radiance.'],
 'radiance','光辉；光彩','比喻不同艺术家视野持续给人的影响，而非实体星光','The painting retained a special radiance for later generations.',['special radiance','artistic radiance'],
 '“感谢艺术，我们不再只见自己那一个世界，而见世界增殖；有多少原创艺术家，便有多少世界供我们接触。这些世界彼此差异大于无限空间中旋转的世界；即使其光之源火熄灭数世纪，无论名为 Rembrandt 或 Vermeer，它们仍各送来特别光辉。”真实生活中，Proust 常生病，也避免走得太远。')

add(25,'逻辑关系','What contrast does “Even so” express in the statement about Proust?',
 ['Art prevented any experience across time or geography.','He became physically healthy because he traveled widely.','Art enabled access to multiple worlds despite the limitation being acknowledged.','The author retracts the claim that art can offer experience.'],2,
 '关于 Proust 的陈述中，Even so 表达什么对比？',['艺术阻止任何跨时空体验。','广泛旅行让他身体健康。','尽管承认前面的限制，艺术仍让他接触多个世界。','作者撤回艺术可提供体验的主张。'],
 ['A experienced multiple worlds 与阻止相反。','B 没有健康改善或广泛实体旅行的证据。','C Even so 保留限制与 thanks to art 的可能并存；上下文所述限制为常病、少远行。','D 这是加强艺术可提供体验，不是撤回。across time and geography 指艺术带来的体验，不能改成真实穿越时间。'],
 ['Even so, he experienced multiple worlds across time and geography thanks to art.'],
 'thanks to','由于；多亏','把多世界体验归于艺术，不是向人表达礼貌致谢','Thanks to the archive, she encountered voices from another century.',['thanks to art','experience worlds thanks to books'],
 '即便如此，多亏艺术，他仍体验了跨越时间与地域的多个世界。')

assert len(out)==25 and [q['id'] for q in out]==[t['questionId'] for t in targets]

def persist():
 path=ROOT/'source/short-questions/additional.json';existing=load('source/short-questions/additional.json');byid={q['id']:q for q in existing}
 for q in out:
  if q['id'] in byid:assert byid[q['id']]==q,('Refuse to overwrite changed authoring',q['id'])
  else:existing.append(q)
 path.write_text(json.dumps(existing,ensure_ascii=False,indent=2)+'\n',encoding='utf8',newline='\n')
 review=dict(batchId='batch-025',date='2026-10-22',pdfSha256=b['pdfSha256'],checkedPdfPages=list(range(98,103)),questionIds=[q['id'] for q in out],paragraphs=[dict(id=pid,textSha256=hashlib.sha256(pp[pid]['text'].encode()).hexdigest()) for pid in dict.fromkeys(q['paragraphId'] for q in out)],note='完整PDF98–102原页视觉核对，含图2、图3及跨页正文；本批仅考文字程序和结果，不宣称辅助图已结构化进入网页。丰富评分与心情区分，perhaps标记作者对过程的猜想，实验未给随机分配则不补造；1986/1995比赛按本书叙述设题，不作独立史实确认，不把冠军个案推成保证；Proust多世界是文学比喻，under the right circumstances等条件保留。')
 (ROOT/'source/short-questions/review-chapter09-figures-sports25.json').write_text(json.dumps(review,ensure_ascii=False,indent=2)+'\n',encoding='utf8',newline='\n')
 print('Saved',len(out),'of 25 individually authored exercises')

if __name__=='__main__':persist()
