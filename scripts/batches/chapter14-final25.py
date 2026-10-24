"""25 individually authored exercises for frozen targets, PDF pages 166-169.
Preserve printed English, source positions and all previously published questions.
"""
from pathlib import Path
import json,hashlib
ROOT=Path(__file__).resolve().parents[2]
load=lambda p:json.loads((ROOT/p).read_text(encoding='utf8'))
b=load('public/data/book.json');plan=load('public/data/reading-plan.json');targets=load('source/short-questions/batch042-targets.json')['targets']
ss={s['id']:s for s in b['sentences']};pp={p['id']:p for p in b['paragraphs']};out=[]
def add(i,kind,prompt,options,answer,prompt_zh,options_zh,analyses,quotes,word,meaning,context,example,collocations,translation,support='explicit'):
 t=targets[i-1];u=next(u for u in plan['units'] if u['id']==t['readingUnitId']);group=[ss[sid] for sid in u['sentenceIds']];p=pp[u['paragraphId']];text=p['text'][group[0]['start']:group[-1]['end']]
 assert hashlib.sha256(text.encode()).hexdigest()==t['passageSha256'];evidence=[]
 for quote in quotes:
  offset=text.find(quote);assert offset>=0,(i,quote);start=group[0]['start']+offset;end=start+len(quote);touching=[s for s in group if s['start']<end and s['end']>start]
  evidence.append(dict(quote=quote,sentenceIds=[s['id'] for s in touching],sources=list({(r['pdfPage'],r['block']):r for s in touching for r in s['sources']}.values())))
 assert word.lower() in text.lower(),(i,word)
 out.append(dict(id=t['questionId'],version=1,readingUnitId=u['id'],chapterId=u['chapterId'],sectionId=u['sectionId'],paragraphId=u['paragraphId'],sentenceIds=u['sentenceIds'],passage=text,prompt=prompt,options=options,answer=answer,type=kind,promptZh=prompt_zh,optionsZh=options_zh,analyses=analyses,evidence=evidence,vocabulary=[dict(word=word,meaning=meaning,context=context,example=example,collocations=collocations)],translation=translation,support=support,editorialStatus='PDF166–169原页核对；书末建议与文学例子不改为实证因果，保留旧跨页候选分段并另记边界限制。'))

add(1,'同义改写','Which description best matches the psychologically rich life outlined here?',
 ['A predictable life built around a single unchanging plan.','A life whose value depends only on being constantly happy.','A varied, eventful journey that includes changes of direction.','A life that excludes familiar people and requires a television career.'],2,
 '哪项最符合本段描述的心理丰富人生？',['按单一不变计划过可预测的生活。','价值只取决于时时快乐的人生。','多样且多事、包含方向转折的旅程。','排除熟人并必须从事电视业的人生。'],
 ['A twists/detours与固定计划相反。','B 本段强调丰富、多样，并非只用快乐衡量。','C varied/eventful/changes of direction对应complexity、eventful、turning points。','D 喜欢Letterman是作者个人经历，非人人应从业；对比熟悉安逸也不等于禁止熟人。'],
 ['a life with twists and turns, stops, detours, and turning points'],
 'detours','绕路；偏离原路线的经历','以旅途绕路比喻人生不按直线发展','A chance meeting led to an unexpected detour in her career.',['take a detour','an unexpected detour'],
 '心理丰富的人生有曲折、停顿、绕路和转折；它多事而富有戏剧性，而非熟悉安逸；它复杂且多元；重在expeditus，即自发行动，而非deliberatio，即仔细斟酌；它像漫长蜿蜒的旅程，而非简单直路。Jon Stewart的《The Daily Show》之前，有David Letterman的《Late Show》。我喜欢他古怪的幽默，最喜欢他的十大榜单。')

add(2,'作者意图','Why does the author introduce his own Top Ten list?',
 ['To end the book in a playful way.','To rank ten experiments by their statistical reliability.','To replace every account given earlier in the book.','To claim that Appendix 3 contains the same television jokes.'],0,
 '作者为什么引入自己的十大榜单？',['以带有玩心的方式结束本书。','按统计可靠性排列十项实验。','取代全书前文的所有叙述。','宣称附录3收录相同电视笑话。'],
 ['A in the spirit of playfulness直接说明用意。','B list不是实验可靠性排名。','C end my book表示收尾，不是推翻前文。','D 附录是另一种总结，未称相同笑话。'],
 ['in the spirit of playfulness, I end my book with my own Top Ten list'],
 'in the spirit of','本着……精神','以玩心为基调安排总结','In the spirit of curiosity, we tried a different route.',['in the spirit of cooperation','a spirit of playfulness'],
 '所以，本着玩心，我用自己的心理丰富十大榜单为本书收尾（另一种总结见附录3）。')

add(3,'细节','What question does the author suggest asking when deciding whether to stay or go?',
 ['Will staying remove every possible future regret?','Would I regret staying when I look back in ten years?','Did everyone who moved to Boston become successful?','Which option is certain to be easier tomorrow?'],1,
 '面对留下还是离开，作者建议自问什么？',['留下能否消除未来全部后悔？','十年后回看，我会不会后悔当初留下？','搬去波士顿的人是否都成功？','哪种选择明天肯定更轻松？'],
 ['A 原文让人考虑可能的后悔，不保证消除全部。','B in ten years与if I stayed准确对应。','C 波士顿是未做之事的例子，没有成功统计。','D 关注十年后的回望，非明天难易。'],
 ['“In ten years, would I regret if I stayed?”'],
 'inaction','不行动','用理由为没有采取行动开脱','Fear can sometimes lead to inaction.',['an excuse for inaction','a period of inaction'],
 '10. 不留遗憾的人生：到了晚年，人们往往后悔本可做却没做的事：未接受工作机会、有机会却没搬去波士顿、没有重返学校。为不行动找借口很容易；但面对“该留下还是离开？”，问问自己：“十年后，我会后悔留下吗？”')

add(4,'逻辑关系','What contrast does the passage draw between short-term and long-term regret?',
 ['People regret only inaction at every stage of life.','Actions become impossible to regret after a few years.','Short-term regret is always larger than long-term regret.','Actions may cause short-term regret, while major long-term regrets concern inaction.'],3,
 '本段怎样对比短期与长期后悔？',['人在任何阶段都只后悔没做的事。','几年后采取过的行动就不可能令人后悔。','短期后悔总比长期大。','行动短期可能令人后悔，长期最大的遗憾来自没做的事。'],
 ['A may regret what we do承认行动也会后悔。','B 没有规定几年后绝不后悔行动。','C 比较的是对象和时间，不是短期程度一定更大。','D may、short run、biggest、long run均保留原文范围。'],
 ['we may regret what we do in the short run, but in the long run, our biggest regrets come from what we didn’t do.'],
 'in the long run','从长远看','与眼前的后悔形成时间对比','The extra practice may help in the long run.',['in the short run','a long-term regret'],
 '记住，短期里我们可能后悔做过的事，但从长远看，最大的遗憾来自我们没做的事。')

add(5,'细节','Which choice is given as an example of Calhoun following her parents’ advice?',
 ['Taking a job mainly because it provided extensive benefits.','Choosing work with greater freedom despite lacking job benefits for years.','Refusing to have a child until childcare was fully arranged.','Telling every reader that financial planning is unnecessary.'],1,
 '哪项是Calhoun遵循父母建议的例子？',['主要为丰厚福利选工作。','选择更自由的工作，尽管多年没有工作福利。','拒绝生孩子直到托育全安排好。','告诉每位读者财务计划毫无必要。'],
 ['A 原文是尽管缺少福利仍选自由。','B more freedom和hasn’t had job benefits in years直接支持。','C 她没有托育计划仍选择生孩子。','D 回忆个人选择，不等于所有人都无需规划。'],
 ['she chose a job that allowed her more freedom, even though she hasn’t had job benefits in years'],
 'boiled down to','归结为；简化为','父母将多数选择概括为安全或自由','The disagreement boiled down to different priorities.',['boil down to a choice','job benefits'],
 '9. 自由优于安全：诗人Ada Calhoun在《纽约时报杂志》的一篇文章里回忆，成长中父母常说，多数选择可归结为安全或自由，选择自由总更好。她听从建议：选了更自由的工作，尽管多年没有工作福利；也在没有托育计划的情况下选择生孩子。')

add(6,'语境词义','In “being out on the right limb,” what does “limb” most plausibly suggest?',
 ['A body part that has fully recovered from an injury.','A completely risk-free position with no difficult choices.','A personally fitting but exposed or risky course of action.','A branch of a company offering guaranteed benefits.'],2,
 '“being out on the right limb”中的limb最可能表示什么？',['伤后完全恢复的肢体。','没有困难选择、毫无风险的位置。','适合自己但较暴露或有风险的行动道路。','保证提供福利的公司分部。'],
 ['A 这里讨论自由、安全与选择，没有伤病。','B out on a limb的比喻与冒险有关，非无风险。','C right和right voice强调对自己合适，out on a limb含处于风险中的意味；属语境有限解释。','D 未提公司分部，job benefits不能移接成词义。'],
 ['there is no greater security than being out on the right limb, with the right voice in your head.'],
 'limb','树枝；在此处的比喻中指冒险的位置','Calhoun用out on the right limb表达选择合适自己的自由道路所带来的内在安全感','She went out on a limb to support an unpopular proposal.',['go out on a limb','choose freedom over security'],
 '她如今觉得：“没有比置身合适的险境、内心响着合适的声音更大的安全感了。”最终，能够选择自由而非安全、可能性而非责任、挑战而非安逸，是心理丰富人生的关键。','limited-inference')

add(7,'逻辑关系','How does the author qualify his discussion of specialization?',
 ['He recognizes professional benefits but warns against an excessively narrow view.','He claims that specialization never helps anyone professionally.','He treats every division of labor as a direct cause of failure.','He argues that only forest workers should become generalists.'],0,
 '作者怎样限定对专业化的讨论？',['承认职业上的益处，但警惕过于狭窄的视野。','宣称专业化从不帮助职业发展。','将所有劳动分工视为失败的直接原因。','只要求林业工人成为通才。'],
 ['A often leads to success与But too much…may相配，体现有条件的转折。','B 与often leads to success矛盾。','C meticulous division是背景，未称所有分工必然导致失败。','D forest/tree是只见树木不见森林的比喻，非职业限定。'],
 ['Professionally, specialization often leads to success. But too much specialization may lead us to miss the beauty of the forest for a tree.'],
 'specialization','专业化','专精职业有益，但过度专精可能缩窄视野','Her specialization is useful, but she also studies other fields.',['professional specialization','division of labor'],
 '8. 别只做专才，要做通才：我们多数人生活在高度专业化、劳动分工精细的世界。职业上，专业化往往带来成功。但过度专精可能让我们为了一棵树，错过整片森林的美。')

add(8,'同义改写','Which paraphrase best preserves the advice in this short passage?',
 ['Always do every skilled job yourself.','Abandon curiosity once you have a broad education.','Choose one subject and avoid practical tasks forever.','Remain curious, develop breadth, and occasionally try doing something yourself.'],3,
 '哪种改写最保留本段建议？',['永远自己做所有专业工作。','接受广泛教育后就放弃好奇。','只选一科、永不尝试实作。','保持好奇、拓展广度，偶尔自己动手。'],
 ['A maybe/once in a while不能改成always/every。','B Stay curious要求持续好奇。','C generalist强调广度，且允许自己尝试。','D 保留保持好奇、通才和偶尔动手三层意思。'],
 ['Stay curious in life, be a generalist, maybe even do it yourself once in a while!'],
 'once in a while','偶尔；间或','限制自己动手的频率，不是凡事亲力亲为','Once in a while, I repair a small item myself.',['once in a while','be a generalist'],
 '在生活中保持好奇，做个通才，甚至也许偶尔自己动手试试！')

add(9,'主旨','What obstacle to exploration is identified in this excerpt?',
 ['The powerful attraction of familiar routines.','The complete disappearance of familiar restaurants.','An inability to distinguish pigeons from humans.','A requirement to change snacks on every journey.'],0,
 '这段指出探索的什么障碍？',['熟悉惯例具有强大吸引力。','熟悉餐厅完全消失。','无法分辨鸽子与人。','每趟旅程都必须换零食。'],
 ['A comfort of familiarity…powerfully attractive为核心解释。','B going to the same chain恰说明重复光顾。','C pigeons/humans是并列比较，不是识别障碍。','D eating the same snack是习惯例子，未颁布每趟换食物的规则。本段sitting后跨页，下一短段quietly续接，不当作独立完整句。'],
 ['The comfort of familiarity is so powerfully attractive that we forget the joy of exploration'],
 'familiarity','熟悉；熟悉感','熟悉带来的舒适吸引人重复既有选择','Familiarity can make a place feel comfortable.',['the comfort of familiarity','the joy of exploration'],
 '7. “先试十二个”：鸽子和人都探索得不够。熟悉感带来的舒适如此有吸引力，让我们忘了探索的乐趣，吃同样的零食、去同一家连锁店，并坐着')

add(10,'细节','What does the “take a dozen” heuristic recommend before making a choice?',
 ['Choosing the first familiar option to avoid effort.','Comparing exactly twelve countries on every trip.','Exploring at least twelve possibilities before selecting one.','Keeping twelve apartments at the same time.'],2,
 '“先试十二个”的启发式建议在选择前做什么？',['为省事选第一个熟悉选项。','每趟旅行恰好比较十二国。','选定之前探索至少十二种可能。','同时保留十二套公寓。'],
 ['A 与explore before take our pick相反。','B at least不是exactly；对象例举伴侣、公寓、餐厅等，非只限国家。','C at least twelve与before take our pick直接支持。','D explore潜在选择不等于同时占有全部。句首quietly承接上段sitting，中文按跨页续文保留。'],
 ['explore at least twelve potential mates, apartments, restaurants, etc., before we take our pick.'],
 'heuristic','启发式；经验性决策方法','作者以至少探索十二种可能的经验规则提醒人克服熟悉偏好，非保证每次最优','A simple heuristic can guide an initial search.',['a decision heuristic','take our pick'],
 '安静地通勤。但承认这种偏向，我们便能克服它；“先试十二个”的启发式提醒我们，选定之前至少探索十二个潜在伴侣、公寓、餐厅等。探索更多，我们就能做出更好的决定。')

add(11,'推断','What can reasonably be inferred about the author’s view of familiar things?',
 ['They prevent all changes in perspective.','They can offer fresh discoveries when revisited.','They are useful only to film characters.','They must be replaced whenever they become comfortable.'],1,
 '关于熟悉的事物，可以合理推断作者持何看法？',['它们阻止所有视角改变。','重访时可以带来新发现。','只对电影角色有用。','一旦舒适就必须换掉。'],
 ['A discover new in the old与阻止所有变化不符。','B find richness/revisit/discover new支持熟悉也能带来发现。','C Plainview/Levy是例子，建议还列乐队、作者、书、影片、人。','D 无须一律替换；作者恰提供从熟悉中获得丰富的途径。'],
 ['Revisit a favorite band, author, book, film, or person, and you will discover new in the old.'],
 'revisit','重访；重新接触','再次接触熟悉喜爱的事物，发现新意','I revisited the novel and noticed a different theme.',['revisit a favorite book','find richness in the familiar'],
 '6. 在熟悉中发现丰富：但如果你像Daniel Plainview（“我想赚够钱，好远离所有人”）或Eugene Levy（“我真的很喜欢熟悉感”），也能在熟悉事物中找到丰富。重新接触喜欢的乐队、作者、书、电影或人，你会在旧中发现新。','inference')

add(12,'细节','Which behavior is associated with the “happiness trap” here?',
 ['Accepting that undesirable events sometimes happen.','Recording interesting experiences in writing.','Seeking novelty without judging one’s emotions.','Trying to avoid negative events at all costs and blaming oneself for discontent.'],3,
 '这里“快乐陷阱”与哪种行为有关？',['接受不如意之事有时会发生。','写下有趣经历。','寻找新奇且不评判自身情绪。','不惜一切代价避开负面事件，并因不满责怪自己。'],
 ['A 是后文bad things happen的承认，非陷阱的表现。','B 本段未以写作为陷阱。','C 不评判情绪不是blame ourselves。','D fear/avoid at all costs/blame逐一对应。'],
 ['We fear negative events, try to avoid them at all costs, and blame ourselves for our discontent.'],
 'at all costs','不惜一切代价','描述对负面经历竭力回避的倾向','They tried to prevent delays at all costs.',['avoid something at all costs','blame oneself for'],
 '5. 不要害怕负面事件：许多人掉进快乐陷阱。我们怕负面事件，不惜一切代价回避，又为自己的不满责怪自己。但生活事实就是：坏事会发生。')

add(13,'作者意图','What is the main purpose of the references to Nietzsche and Joyce?',
 ['To report the results of a controlled experiment on failure.','To promise that every hardship will immediately produce success.','To encourage readers to see difficulty as part of a life story and possible growth.','To argue that negative emotions should never be expressed.'],2,
 '提到Nietzsche与Joyce的主要意图是什么？',['报告关于失败的控制实验。','保证每次困难都立即带来成功。','鼓励读者把困难看作人生故事与可能成长的一部分。','论证绝不应表达负面情绪。'],
 ['A 哲学与文学呼应不是实验结果。','B 原文劝勉没有every/immediately的保证。','C OK to fail/feel negative与part of your story共同构成鼓励。','D It’s OK to feel negative emotions明确接纳负面感受。'],
 ['It’s OK to fail; it’s OK to feel negative emotions.','This is all part of your story.'],
 'hardship','艰难；困苦','拉丁语引句中的艰难，用于劝勉，不是必然成功的实证定律','She wrote about the hardships of moving abroad.',['through hardship','face hardship'],
 '失败没关系，有负面情绪也没关系。记住Nietzsche：这些挑战会让你更有智慧。记住James Joyce：Per aspera ad astra——穿过艰难，走向群星。这都是你故事的一部分。')

add(14,'语境词义','What does “kick in” mean in this sentence?',
 ['Begin to operate or take effect.','Physically strike something with a foot.','Stop working permanently.','Remove all memories of an experience.'],0,
 '本句kick in是什么意思？',['开始运作或产生作用。','用脚踢某物。','永久停止工作。','删除经历的全部记忆。'],
 ['A psychological immune system是心理适应的比喻，kick in意为开始发挥作用。','B 此处无实际踢的动作。','C let…kick in是让其起作用，非停止。','D 未说抹去全部记忆。'],
 ['let your psychological immune system kick in.'],
 'kick in','开始生效；开始起作用','让心理适应系统发挥作用，非身体免疫检测或医学处方','After a few minutes, her training kicked in.',['let something kick in','a psychological immune system'],
 '拥抱它带来的丰富，让你的心理免疫系统开始发挥作用。')

add(15,'细节','Why are writing and storytelling recommended?',
 ['They make interesting experiences unnecessary.','They prevent stories from ever changing.','They guarantee the accuracy of every remembered detail.','They help people remember their interesting stories.'],3,
 '为什么建议写作与讲故事？',['使有趣经历变得不必要。','让故事永远不能修改。','保证记忆每个细节准确。','帮助人记住自己有趣的故事。'],
 ['A richness是故事积累，写作帮助记住而非免除经历。','B 未禁止修改，下段还会谈编辑故事。','C excellent way记忆不等于every detail保证。','D remember them和way to remember是明示理由。'],
 ['It’s important to remember them, and writing is an excellent way to do it. Telling a story is also a great way to remember.'],
 'accumulation','积累；累积','心理丰富被描述为有趣故事逐渐累积','The archive is an accumulation of many small discoveries.',['the accumulation of stories','remember an experience'],
 '4. 写下来、讲出来：丰富是有趣故事的积累。记住它们很重要，写作是很好的办法；讲故事也是记忆的好方式。')

add(16,'逻辑关系','What comparison is made between wealth and stories?',
 ['Both must remain private within one generation.','Both can be passed on to enrich a later generation in different ways.','Both guarantee that descendants will avoid hardship.','Both have exactly the same financial value.'],1,
 '财富与故事之间作了什么比较？',['两者都必须只留在一代人中。','两者都能传给后代，以不同方式使其丰富。','两者保证后代免于艰难。','两者经济价值完全相等。'],
 ['A transferred across generations与封闭保存相反。','B wealth→materially rich、stories→psychologically rich，保留对应关系。','C 未许诺没有艰难，反而保留bad stuff作为成长跳板。','D 类比传承价值，不是金融等价。'],
 ['Just as wealth can be transferred across generations and help the next generation become materially rich, your stories can be transferred to the next generation and help them become psychologically rich.'],
 'springboard','跳板；起点','把不好的经历用于成长，不是删除它们','That first project became a springboard for further learning.',['a springboard for growth','transfer across generations'],
 '写与讲时，可以编辑自己的故事。保留不好的部分，却把它用作成长的跳板。记住Hemingway的流动盛宴，找到属于自己的。财富可以代际传递，帮助下一代物质富裕；同样，你的故事也可以传给下一代，帮助他们心理丰富。')

add(17,'细节','What simple response to boredom does the author suggest?',
 ['Make every social meeting require a formal appointment.','Avoid contacting friends unless a detailed plan already exists.','Text friends to find out whether they are available.','Wait until all friends have identical schedules.'],2,
 '作者建议无聊时做哪件简单的事？',['使每次社交都须正式预约。','没有细密计划就不联系朋友。','给朋友发消息看看他们是否有空。','等所有朋友日程完全相同。'],
 ['A scheduled/appointment是现状背景，并非新建议。','B 与text your friends直接相反。','C 明示text…see if they are free。','D if they are free是询问当下是否有空，不要求全体同一日程。'],
 ['Next time you are bored, text your friends to see if they are free.'],
 'hang out','相聚；闲逛','非正式地与朋友共度时间','We sometimes hang out after class.',['hang out with friends','make an appointment'],
 '3. 自发一些：我们生活在日程安排密集的时代。多数人连和朋友聚聚都需要预约。下次无聊时，发消息问问朋友有没有空。')

add(18,'作者意图','What is the purpose of the reference to Alice in Wonderland?',
 ['To encourage occasional departures from routine and curiosity about the unknown.','To require readers to imitate every action of a fictional character.','To say that real-life routines are always harmful.','To provide evidence from an experiment on reading speed.'],0,
 '提到《爱丽丝梦游仙境》的意图是什么？',['鼓励偶尔离开惯例、好奇未知。','要求逐一模仿虚构人物所有行为。','宣称现实中的惯例总有害。','提供阅读速度实验的证据。'],
 ['A from time to time和Seek the unknown为比喻提供定位。','B Be Alice是文学式鼓励，不是逐项行为命令。','C 偶尔偏离不等于总有害。','D 文学角色不构成实验。末尾Stop by a跨页接下段gallery，来源边界另记。'],
 ['Deviate from routines from time to time. Be Alice in Alice in Wonderland! Seek the unknown.'],
 'deviate from','偏离','偶尔改变惯例，保留from time to time的频率限制','We deviated from our usual route on Saturday.',['deviate from a routine','from time to time'],
 '时不时偏离惯例。像《爱丽丝梦游仙境》中的Alice那样！去寻找未知。顺路去一家')

add(19,'推断','What attitude is conveyed by “You never know what you will find”?',
 ['Confidence that every visit will produce a valuable purchase.','A warning that galleries contain the same things as shops.','A demand to avoid places without a fixed shopping list.','Openness to unexpected discoveries.'],3,
 '“You never know what you will find”表达什么态度？',['确信每次造访都会买到值钱东西。','警告画廊和商店物品相同。','要求没固定购物清单就别去。','对意外发现保持开放。'],
 ['A 未知发现不是保证购买获利。','B 场所并列不表示内容相同。','C 与never know所含开放性不符。','D 可合理读为愿意遇见没预先计划的发现；句首续上段Stop by a。'],
 ['You never know what you will find.'],
 'used bookstore','旧书店；二手书店','作者列举可顺路探访的场所之一','I found an old travel journal in a used bookstore.',['browse a used bookstore','stop by a gallery'],
 '画廊、旧书店或Goodwill店。你永远不知道会发现什么。','limited-inference')

add(20,'逻辑关系','Why might reading a novel appear to be a waste of time, according to the passage?',
 ['Because the author establishes that novels have no value.','Because novels are listed as a legal obligation.','Because an intense focus on completing obligations can make enjoyable activities seem unproductive.','Because people no longer have taxes or household tasks.'],2,
 '按本段，读小说为什么可能显得浪费时间？',['作者证明小说没有价值。','小说被列为法律义务。','过于专注完成责任，会让愉快活动显得不事生产。','人们已无税务与家务。'],
 ['A appear to be是某种视角下的表象，非作者判定无价值。','B washing/taxes才是责任例子，小说是享受例子。','C When…so focused on getting things done给出这种观感的条件。','D lots of obligations与没有责任相反。'],
 ['When we are so focused on getting things done, many things—especially enjoyable experiences, like reading a novel—appear to be a waste of time.'],
 'obligations','责任；必须履行的事','洗碗、报税等需要完成的事务','She balanced her obligations with time for reading.',['fulfil obligations','household obligations'],
 '2. 有玩心！我们都有很多责任，从洗碗到报税。过于专注把事情做完时，许多事情——尤其读小说之类愉快的体验——看起来像在浪费时间。')

add(21,'同义改写','Which statement best preserves the claim about playful moments?',
 ['Playfulness guarantees that social and economic responsibilities disappear.','Playful breaks may lead to unexpected learning and insights about our goals.','New insights can occur only during paid vacations.','Acting foolishly always prevents meaningful discovery.'],1,
 '哪项最保留关于玩心时刻的论点？',['玩心保证社会经济责任消失。','带玩心的休息可能带来意外学习与目标洞见。','只有带薪休假时才能有新洞见。','像傻瓜一样总会妨碍发现。'],
 ['A on vacation是暂离现实压力的比喻，不是责任消失保证。','B may对应可能，discover/learn/insight与原文匹配。','C 未说only或paid，别将比喻当假期规定。','D Be open to be a fool是允许探索中的笨拙，非必然阻止发现。'],
 ['we may discover something unexpected, learn something new, and gain new insight into our goals.'],
 'insight','洞见；深入认识','玩心时刻可能使人重新理解自己的目标','The conversation gave her new insight into her priorities.',['gain insight into','a playful moment'],
 '然而，正是在带玩心的时刻、在你“暂时从社会与经济现实中休假”时，我们可能发现意外、学到新东西，并对自己的目标产生新认识。“也愿意做个傻瓜吧！”')

add(22,'主旨','What scope does the author give a mindset of psychological richness?',
 ['It can guide small everyday choices as well as important life decisions.','It applies exclusively to permanent moves abroad.','It removes the need to make any difficult choices.','It concerns exhibitions but never other daily activities.'],0,
 '作者认为心理丰富的思维可用于什么范围？',['既能帮助重大人生决定，也能帮助日常小选择。','只适用于永久移民。','免去一切困难选择。','只关乎展览而非其他日常活动。'],
 ['A Beyond important…small, everyday直接说明适用范围。','B 未限定永久迁移。','C help make不等于不再选择。','D 新展览是举例，不能缩成唯一范围。'],
 ['Beyond important life decisions, a mindset of psychological richness can help us make small, everyday decisions, too.'],
 'mindset','思维方式；心态','将心理丰富作为看待日常选择的角度','A curious mindset helped her notice ordinary details.',['a mindset of curiosity','everyday decisions'],
 '1. 就去做！除了重大人生决定，心理丰富的思维也能帮助我们做日常小决定。去新展览，还是待在家里？')

add(23,'逻辑关系','How should the statement about days with new experiences be read?',
 ['As proof that every new activity causes lasting happiness for everyone.','As a finding about Doreen’s feelings in a controlled experiment.','As a claim that novelty and a sense of meaning cannot coexist.','As an association between doing something new and feeling the day richer, happier, and more meaningful.'],3,
 '应怎样理解做新事情那一天的描述？',['证明每种新活动都让每个人终身快乐。','关于控制实验中Doreen感受的发现。','声称新奇与意义感不可共存。','将做新事与当天觉得更丰富、更快乐、更有意义联系起来。'],
 ['A days/feel不能扩大为every/lasting/因果保证。','B Doreen属于随后引入的诗歌角色，非研究参与者。','C as well as明确三种感受可共同出现。','D 保留当天感受与新活动的关系，不擅加严格因果设计。'],
 ['On days when people do something new, they feel that the day is psychologically richer, as well as happier and more meaningful.'],
 'comfort zone','舒适区','倾向待在熟悉安心范围的生活方式','Trying a new class took him outside his comfort zone.',['stay within a comfort zone','try something new'],
 '去徒步吗？如果你喜欢待在舒适区，我建议你冒个小险，尝试新事——就去做！做新事情的日子，人们觉得当天心理上更丰富，也更快乐、更有意义。在《Ed》一诗中，Louis Simpson介绍了同名人物Ed：一个爱上女服务员Doreen的年轻人。')

add(24,'细节','What sequence of events is described for Ed?',
 ['His family approves, he marries Doreen, and she stays with him.','His family and friends disapprove, he marries someone else, and he later regrets not marrying Doreen.','Doreen leaves him after they marry, so he blames her family.','His friends choose Doreen’s husband after his wife returns.'],1,
 '本段描述Ed经历了什么顺序？',['家人赞成，娶Doreen，她一直留下。','亲友反对，他娶别人，后来后悔没娶Doreen。','娶Doreen后她离开，他责怪她家人。','妻子返回后朋友替Doreen选丈夫。'],
 ['A do not approve与another woman都不支持。','B not approve→instead marries another→wife leaves→should have married Doreen逐项匹配。','C His wife指娶的另一个女人，非Doreen。','D 没有妻子返回或替人选丈夫。诗歌叙事不是观察样本。'],
 ['So, instead he marries another woman. Years later, his wife leaves Ed. Ed complains to his friends and family that he should have married Doreen.'],
 'should have','本应；早该','对过去未作的选择表示遗憾，非现在必须已发生的事实','I should have asked for advice earlier.',['should have done','approve of a choice'],
 '他的家人和朋友不赞同。于是他娶了另一个女人。多年后，妻子离开Ed。他向亲友抱怨，当初本该娶Doreen。')

add(25,'作者意图','What shift occurs when the author changes “why didn’t you?” to “why don’t you?”',
 ['A change from a present invitation to a completed experiment.','A denial that Ed ever faced a choice.','A move from questioning a past omission to encouraging the reader to act now.','A claim that every reader must make Ed’s exact romantic choice.'],2,
 '作者把why didn’t you改成why don’t you，实现了什么转变？',['从当下邀请转为已完成实验。','否认Ed面对过选择。','从追问过去未做之事，转向鼓励读者现在行动。','要求每位读者作出和Ed完全相同的爱情选择。'],
 ['A didn’t指过去，don’t转向对读者当下的鼓励；无实验。','B why追问没做的选择，并未否认选择。','C my last words to you与时态转换共同支持此修辞用意。','D 借诗人话语劝勉行动，不要求重复角色具体婚姻决定。'],
 ['His family and friends reply, “Well, why didn’t you?”','So I borrow from Simpson to give my last words to you: “Well, why don’t you?”'],
 'borrow from','借用；取用某人的表达','借用Simpson诗中问句并转向读者','The speech borrowed an image from a familiar story.',['borrow from a writer','give one’s last words'],
 '他的家人朋友答道：“那你当时为什么没那么做？”于是，我借Simpson的话，把最后一句留给你：“那么，你为什么不去做呢？”','limited-inference')

def persist():
 path=ROOT/'source/short-questions/additional.json';existing=load('source/short-questions/additional.json');byid={q['id']:q for q in existing}
 for q in out:
  if q['id'] in byid:assert byid[q['id']]==q,('Refuse to overwrite changed authoring',q['id'])
  else:existing.append(q)
 path.write_text(json.dumps(existing,ensure_ascii=False,indent=2)+'\n',encoding='utf8',newline='\n')
 review=dict(batchId='batch-042',date='2026-10-24',pdfSha256=b['pdfSha256'],checkedPdfPages=[166,167,168,169],questionIds=[q['id'] for q in out],paragraphs=[dict(id=pid,textSha256=hashlib.sha256(pp[pid]['text'].encode()).hexdigest()) for pid in dict.fromkeys(q['paragraphId'] for q in out)],note='完整PDF166–169原页视觉核对。Top Ten是玩心式总结，非实验排行；Calhoun回忆与作者建议不作普遍安全承诺。often/may/once in a while/at least范围保留；文学比喻、Ed诗歌与当天感受关联区分，不改成实证因果。既有PDF167→168的sitting/quietly和168→169的Stop by a/gallery边界为跨页续文，固定原句及ID不重复补字，详见batch042-source-notes.json。既有池配题完成仍有章首正文/辅助材料源文审计待办。')
 (ROOT/'source/short-questions/review-chapter14-final25.json').write_text(json.dumps(review,ensure_ascii=False,indent=2)+'\n',encoding='utf8',newline='\n')
 print('Saved',len(out),'of 25 individually authored exercises')

if __name__=='__main__':persist()
