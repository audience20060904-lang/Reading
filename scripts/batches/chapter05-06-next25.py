"""25 individually authored exercises for frozen targets, PDF pages 49-54.
Preserve printed English, source positions and all previously published questions.
"""
from pathlib import Path
import json,hashlib
ROOT=Path(__file__).resolve().parents[2]
load=lambda p:json.loads((ROOT/p).read_text(encoding='utf8'))
b=load('public/data/book.json');plan=load('public/data/reading-plan.json');targets=load('source/short-questions/batch013-targets.json')['targets']
ss={s['id']:s for s in b['sentences']};pp={p['id']:p for p in b['paragraphs']};out=[]
def add(i,kind,prompt,options,answer,prompt_zh,options_zh,analyses,quotes,word,meaning,context,example,collocations,translation,support='explicit'):
 t=targets[i-1];u=next(u for u in plan['units'] if u['id']==t['readingUnitId']);group=[ss[sid] for sid in u['sentenceIds']];p=pp[u['paragraphId']];text=p['text'][group[0]['start']:group[-1]['end']]
 assert hashlib.sha256(text.encode()).hexdigest()==t['passageSha256'];evidence=[]
 for quote in quotes:
  offset=text.find(quote);assert offset>=0,(i,quote);start=group[0]['start']+offset;end=start+len(quote);touching=[s for s in group if s['start']<end and s['end']>start]
  evidence.append(dict(quote=quote,sentenceIds=[s['id'] for s in touching],sources=list({(r['pdfPage'],r['block']):r for s in touching for r in s['sources']}.values())))
 assert word.lower() in text.lower(),(i,word)
 out.append(dict(id=t['questionId'],version=1,readingUnitId=u['id'],chapterId=u['chapterId'],sectionId=u['sectionId'],paragraphId=u['paragraphId'],sentenceIds=u['sentenceIds'],passage=text,prompt=prompt,options=options,answer=answer,type=kind,promptZh=prompt_zh,optionsZh=options_zh,analyses=analyses,evidence=evidence,vocabulary=[dict(word=word,meaning=meaning,context=context,example=example,collocations=collocations)],translation=translation,support=support,editorialStatus='PDF 第 49–54 页逐题核对；固定连续原句；区分个案、观察研究、写作实验和讣告评分，不扩大因果或样本范围'))

add(1,'逻辑关系','Why did the narrator ask callers to spell out their names?',
 ['He was testing whether callers could spell English words.','His limited English listening made their identities difficult to make out.','He wanted to prevent Mike from receiving messages.','Every caller refused to say whom they wanted to reach.'],1,
 '叙述者为什么要求来电者拼出姓名？',['测试来电者能否拼写英语。','英语听力有限，难以听清来电者身份。','阻止 Mike 收到留言。','每位来电者都拒绝说明找谁。'],
 ['A 目的是自己 write it down，没有考查来电者。','B Since I was still learning English 解释 make out 困难，so 引出拼写请求。','C Could you tell him 是传达留言，不是拦截。','D 片段并未说每个人拒绝说明对象。'],
 ['Since I was still learning English, I was never able to make out who this was','Could you please spell it out?'],
 'make out','辨认；听清','这里指从电话语音中辨认身份，不等于是否认识单词','I could barely make out the name over the noisy connection.',['make out a name','make out what someone says'],
 '我便回答：“不在。”电话另一头通常接着说：“能告诉他某某来过电话吗？”由于我还在学英语，总听不清对方是谁，就需要问：“能请你拼出来吗？”这样才能记下。')

add(2,'细节','What sequence of letters did the caller provide?',
 ['M-I-K-E.','H-I-S-M-O-T-H-E-R.','H-I-S-F-A-T-H-E-R.','F-I-R-S-T-N-A-M-E.'],2,
 '来电者提供了哪组字母？',['拼出 M-I-K-E。','拼出 H-I-S-M-O-T-H-E-R。','拼出 H-I-S-F-A-T-H-E-R。','拼出 F-I-R-S-T-N-A-M-E。'],
 ['A Mike 并非本句拼出的字母。','B 将 father 换成 mother。','C 与原句连字符拼写逐字一致；不要先假定它一定是人名。','D 原文没有拼出 first name。'],
 ['he spelled out, “H-I-S-F-A-T-H-E-R.”'],
 'spelled out','逐字母拼出','指来电者说出字母序列，不保证听者已理解整个短语','She spelled out her surname slowly.',['spell out a name','spell a word out'],
 '有一天，我接到电话，照同样的程序应对。询问来电者姓名时，他拼出：“H-I-S-F-A-T-H-E-R。”')

add(3,'细节','What does the narrator do after confirming the letter sequence?',
 ['He asks the caller to come to the dormitory immediately.','He tells Mike that his father is already at the door.','He refuses to end the conversation.','He thanks the caller and hangs up.'],3,
 '确认字母序列后，叙述者做了什么？',['请来电者立即到宿舍。','告诉 Mike 父亲已在门口。','拒绝结束谈话。','向来电者道谢，然后挂断。'],
 ['A 本段没有见面安排。','B 没有在门口或已告诉 Mike 的信息。','C I hung up 明确已结束通话。','D Great, thanks 后紧接 I hung up，顺序准确。'],
 ['“Great, thanks.” I hung up.'],
 'hung up','挂断电话','是 hang up 的过去式，不是把物品挂到墙上','He thanked the receptionist and hung up.',['hang up the phone','hang up after a call'],
 '我重复：“H-I-S-F-A-T-H-E-R？”“对。”“好的，谢谢。”我挂断了电话。')

add(4,'推断','What distinction does the narrator make about his difficulty?',
 ['He knew the individual words but failed to understand them over the phone at the time.','He had never learned either “his” or “father” in any form.','The caller had used words that did not exist in English.','He understood the caller’s identity before asking for spelling.'],0,
 '叙述者怎样区分自己的困难？',['认识单个词，却当时没能在电话中听懂。','此前从未以任何形式学过 his 或 father。','来电者用了不存在的英语词。','要求拼写之前已经理解身份。'],
 ['A knew the words 对比 could not understand...on the phone，体现词汇与听辨不同。','B I of course knew 明确否定从不认识。','C 两个词都存在，困难在听力理解。','D didn’t realize until...put down the phone 说明挂断后才明白。'],
 ['I of course knew the words “his” and “father.” I just could not understand the words on the phone.'],
 'comprehension','理解能力','listening comprehension 是理解听到的话，不等同于识字或拼写能力','The exercise tests listening comprehension with short conversations.',['listening comprehension','reading comprehension'],
 '直到放下电话，我才意识到原来是 Mike 的父亲！我当然认识 his 和 father 两个词，只是在电话里听不懂。当时我的英语听力理解能力很低。','inference')

add(5,'逻辑关系','What change in awareness follows the humiliating incident?',
 ['The narrator concludes that nobody else has similar difficulties.','He recognises similar humiliation among many immigrants and less fortunate people.','He decides that all immigrants have identical language ability.','He claims that embarrassment is necessary for every successful student.'],1,
 '这次令人羞愧的事之后，作者的认识怎样变化？',['认定其他人都没有类似困难。','意识到许多移民及处境较不利者也有类似屈辱感。','认定所有移民语言能力完全一致。','断言羞愧是每位成功学生的必要条件。'],
 ['A similar humiliation 明确涉及他人。','B But this incident made me realize 引出从自身经历到他人处境的认识。','C similar 不等于能力相同，many 也不是所有人。','D 个案的认识变化不能变成所有学生必须受辱的条件。'],
 ['this incident made me realize that many immigrants in the U.S. experience similar humiliation, as do many less fortunate people in Japan.'],
 'humiliation','羞辱感；屈辱感','是作者对自身经历及他人处境的体会，不是对人群能力的评价','The character describes the humiliation of being misunderstood in public.',['experience humiliation','a sense of humiliation'],
 '这太让我难堪了。事实上，我从未如此难堪。但这件事让我意识到，美国许多移民也有类似的屈辱感，日本许多处境较不利的人也是如此。')

add(6,'主旨','How does the narrator characterise the richness of studying abroad?',
 ['Only enjoyable sightseeing mattered, while difficult feelings added nothing.','It was rich because he avoided contact with any unfamiliar group.','Unexpected experiences and varied emotions brought lasting value and a changed identification with others.','Its value depended on never feeling embarrassed or confused.'],2,
 '作者怎样描述留学经历的丰富性？',['只有愉快观光有价值，困难感受毫无作用。','因避免接触陌生群体而丰富。','意外经历和多样情绪带来长远价值，也改变了对他人处境的认同。','只有从不难堪或困惑才有价值。'],
 ['A 同时包含 his father 事件和 awesome experiences，不能只保留愉快部分。','B 开头说此前未与移民认同，事件促成联系，不是回避。','C 认同变化、首次所见与 wide range...emotions 共同支撑。','D 困窘正是叙述的一部分，没有零困窘前提。'],
 ['Until then, I hadn’t identified myself with other immigrants at all.','This wide range of unexpected experiences and unusual emotions makes studying abroad extremely psychologically rich and rewarding in the long run.'],
 'identified myself with','认同；把自己与……的处境联系起来','此处是个人经历带来的认同变化，不等于所有群体经历完全一样','After hearing the story, she identified herself with the newcomer.',['identify with others','identify with someone’s experience'],
 '“his father”事件之前，我没想过交换生经历会与美国移民相似，也完全没把自己与其他移民联系起来。当然，留学时也有很多精彩体验，如去 Acadia 国家公园和 Martha’s Vineyard，第一次看到岩石海岸与灯塔。这样广泛的意外经历与不同寻常的情绪，让留学心理上极其丰富，并在长远中带来回报。')

add(7,'逻辑关系','What contrast is drawn between tourism and living abroad?',
 ['Tourism always includes deeper local relationships than living abroad.','Living abroad is said to eliminate every challenge.','Novelty alone is presented as sufficient for richness.','Living abroad is described as more challenging and emotionally varied, beyond tourism’s novelty.'],3,
 '旅游与在国外生活被怎样对比？',['旅游总比旅居带来更深本地关系。','在国外生活消除所有挑战。','仅新奇就足以构成丰富。','相较旅游的新奇，旅居被描述为挑战更多、情绪范围更广。'],
 ['A rarely...authentic interactions 与此相反，且原文不是 every tourist 的绝对判断。','B much more challenging 明确存在更多挑战。','C not just novelty 直接否定只看新奇。','D 保留比较和新奇之外的要素，不保证每个个体结果。'],
 ['Living abroad is much more challenging and evokes a wider range of emotions.','not just novelty but also challenges and perspective change.'],
 'evokes','唤起；引发','指旅居情境唤起更广情绪，不只正面情绪','The photograph evokes a mixture of affection and sadness.',['evoke emotions','evoke a response'],
 '以游客身份出国也新奇有趣，但游客很少与本地人有真实深入的互动。在国外生活更具挑战，也唤起更广泛的情绪。总之，心理丰富需要多种成分，不仅新奇，也有挑战和视角变化。')

add(8,'细节','How were the two groups described at the beginning of the semester?',
 ['They had similar levels of happiness, meaning, and psychological richness.','The abroad group was already richer on every measure.','The on-campus group had no interest in studying abroad.','They had been randomly assigned to identical travel destinations.'],0,
 '学期开始时，两组被怎样描述？',['幸福、生命意义和心理丰富水平相近。','国外组所有指标原本就更高。','留校组对留学完全没兴趣。','已被随机分配到相同旅行地点。'],
 ['A similar levels 后明确列出三个维度。','B 与 similar 相反。','C 留校组是 interested...but stayed on campus。','D recruited 是招募，未说明随机分配地点；不能凭相近起点宣称随机试验。'],
 ['At the beginning of the semester, study abroad students and on-campus students had similar levels of happiness, meaning in life, and psychological richness.'],
 'recruited','招募','此处招募已留学和留校学生，词本身不表示随机分组','The team recruited volunteers for a weekly survey.',['recruit participants','recruit students'],
 '考虑到这些，Jaime Kurtz 和我招募了留学一学期的学生，以及有留学兴趣却留在校园的学生。两组每周填写简短问卷，类似本章前述每日日记。学期初，留学与留校学生在幸福、生命意义和心理丰富上的水平相近。')

add(9,'细节','Which difference was reported thirteen weeks later?',
 ['The abroad group was happier and more meaningful but not richer.','The abroad group reported greater richness, without group differences in happiness or meaning.','The on-campus group reported no meaning in life at all.','The abroad group scored higher on every possible measure of well-being.'],1,
 '十三周后报告了什么差异？',['国外组更幸福、更有意义，却不更丰富。','国外组自报更丰富，幸福和意义方面则无组间差异。','留校组完全没有生命意义。','国外组在所有可能的幸福感指标上都更高。'],
 ['A 将唯一明确的丰富差异读反。','B reported more...though they didn’t differ 准确限定维度。','C 没有差异不等于某组为零。','D 三个维度已有两项未见差异，不能扩到所有指标。'],
 ['study abroad students reported more psychological richness than on-campus students, though they didn’t differ in terms of happiness or meaning in life.'],
 'in terms of','在……方面；就……而言','限定比较的是幸福和意义，不把局部比较扩为所有生活指标','The options differ in terms of time and cost.',['in terms of happiness','in terms of quality'],
 '然而十三周后，留学学生报告的心理丰富高于留校学生，但在幸福或生命意义方面，两组并无差异。')

add(10,'推断','Which interpretation keeps the activity finding within its reported scope?',
 ['Shopping was experimentally shown to cause richness in everyone.','Artistic activity was the only activity any abroad student ever did.','More artistic activity was associated with greater reported richness at semester’s end.','The researchers assigned every student to the same number of museum visits.'],2,
 '哪种理解保留了活动结果的实际范围？',['购物经实验证明让所有人丰富。','艺术活动是任何留学生唯一做过的活动。','更多艺术活动与学期末更高的自报丰富程度相联。','研究者给每人分配相同次数的博物馆参观。'],
 ['A 原文是 weekly reports，且最后分析聚焦艺术活动，不是普遍购物因果。','B 还列出购物、派对、短途旅行等。','C more...richer they reported 保留观察关联与自报性质。','D engaged in 不表示研究者操控次数。'],
 ['the more artistic activities they engaged in, the richer they reported their lives to be at the end of the semester.'],
 'engage in','参与；从事','表示学生实际参加的活动，不自动指研究者安排的干预','Participants engage in several community activities.',['engage in artistic activities','engage in volunteer work'],
 '为什么？深入分析周报发现，留学生更可能参加艺术活动（如音乐会、博物馆）、购物、派对和短途旅行；比留校学生更少参加社团会议、体育赛事、电子游戏或志愿活动。分析显示，艺术活动参加越多，学期末他们自报的人生越丰富。','inference')

add(11,'推断','What force does “Perhaps” give the explanation about artistic activities?',
 ['It establishes a proven mechanism for every student.','It says the other activities have no value for any purpose.','It changes a tentative explanation into a compulsory recommendation.','It offers a possible reason, without establishing it as a definite mechanism.'],3,
 'Perhaps 对艺术活动的解释赋予什么语气？',['确立适用于每位学生的已证实机制。','说明其他活动对任何目的都没价值。','把暂定解释变成必须遵从的建议。','提出一种可能理由，未把它确认为确定机制。'],
 ['A Perhaps 是可能性标记，不是已证实机制。','B not...associated with richness 只限该分析结果，不等于对任何目的无价值。','C 原文无强制建议，词义也不支持确定化。','D 艺术活动可能更挑战视角，是作者提出的解释而非已单独验证的机制。'],
 ['Perhaps artistic activities challenge you to expand your perspective more than shopping, partying, or taking a short trip.'],
 'ultimately','最终；归根结底','在这里限定最后分析所得关联，不代表所有时期所有人的绝对结论','The final review ultimately supported the revised proposal.',['ultimately associated with','ultimately depend on'],
 '其他活动最终并未与心理丰富相关联。也许艺术活动比购物、派对或短途旅行，更能挑战你去拓宽视角。','inference')

add(12,'观点归属','How does the author position his view alongside Susan Cain’s?',
 ['Both accounts give negative emotions a role, and the author links their combination with positive emotions to richness.','The author rejects Cain because he thinks only positive feelings matter.','Cain is described as having conducted the author’s final experiment.','Both claim that negative emotions guarantee happiness in every person.'],0,
 '作者怎样把自己的观点与 Susan Cain 的观点联系起来？',['两者都赋予负面情绪作用，作者把正负情绪的组合与丰富性相连。','作者认为只有正面情绪重要，所以否定 Cain。','Cain 被说成开展了作者最后的实验。','两者都断言负面情绪保证所有人幸福。'],
 ['A Similarly 引出与 Cain 相似的重视，同时明确 along with positive emotions。','B Similarly 是相呼应，并非否定或只保留正面。','C 本段引书与观点，没有实验执行者说明。','D richer 不是幸福保证，且 I think 和 argues 均标明观点归属。'],
 ['Similarly, I think that negative emotions such as sorrow and longing, along with positive emotions, make our lives psychologically richer.'],
 'longing','渴望；思念','与 sorrow 一起作为负面或苦甜情绪的例子，不等于疾病诊断','The letter expressed her longing for home.',['a longing for home','sorrow and longing'],
 'Susan Cain 在畅销书《Bittersweet》中主张：“明与暗、生与死——苦与甜——永远相伴”，悲伤、渴望等负面情绪“使我们完整”。她认为，负面情绪在情感生活中居核心位置，让人更有同理心，甚至更有创造力。类似地，我认为悲伤、渴望等负面情绪与正面情绪一起，让人生心理上更丰富。')

add(13,'细节','What similarity is reported between happy and meaningful lives in these studies?',
 ['Both were characterised by more negative than positive emotion.','Both involved more positive than negative emotions.','Both required never feeling sadness, anger, or fear.','Both were defined only by emotional complexity.'],1,
 '这些研究报告幸福生活与有意义生活有什么相似处？',['两者都是负面情绪多于正面。','两者正面情绪都多于负面。','两者都要求从不悲伤、愤怒或恐惧。','两者都仅以情绪复杂性定义。'],
 ['A 将 more positive...than negative 的方向读反。','B 最后一句直接说 meaningful 与 happy 在这一点相似。','C infrequently 不是 never，且没有“必须零负面”的门槛。','D 本段在报告情绪模式，不是只用复杂性定义两者。'],
 ['Those who were leading a meaningful life were quite similar to those leading a happy life in that they had more positive emotions than negative emotions.'],
 'infrequently','不经常地；很少地','限定负面情绪出现频率，不能替换成完全从不出现','The committee meets infrequently during the summer.',['occur infrequently','infrequently experienced'],
 '情绪复杂性在心理丰富中起什么作用？六项研究探索了正负情绪在幸福、意义与心理丰富中的作用。六项研究中，过幸福生活者有许多喜悦、满足和愉悦，却不常悲伤、愤怒或恐惧。有意义生活者与他们相似，正面情绪多于负面。')

add(14,'细节','Which emotional profile is described for a psychologically rich life?',
 ['Little positive emotion and no negative emotion.','Only fear and jealousy, with no positive emotion.','A lot of positive emotion together with a substantial amount of negative emotion.','The same single emotion throughout every day.'],2,
 '这里描述心理丰富生活有什么情绪特征？',['很少正面情绪，也没有负面情绪。','只有恐惧和嫉妒，没有正面情绪。','有许多正面情绪，也有相当多的负面情绪。','每天始终只有同一种情绪。'],
 ['A a lot of positive 与 quite a bit negative 都不符合。','B 原句包含许多正面情绪，不能删去。','C but also 连接正负两类，程度也准确。','D 原句是复数 emotions，并列两类，不是单一固定情绪。'],
 ['experienced a lot of positive emotions but also experienced negative emotions quite a bit.'],
 'quite a bit','相当多；颇多','在这里强调负面情绪并非完全缺席，不表示次数与正面必定相等','We learned quite a bit during the discussion.',['learn quite a bit','experience something quite a bit'],
 '有趣的是，过心理丰富生活的人，体验许多正面情绪，同时也相当多地体验负面情绪。')

add(15,'细节','How did the writing tasks differ between the participant groups?',
 ['One group wrote about the future, while the other described childhood.','One group wrote about the best and worst events, while the other wrote about the best and second-best.','One group was made to experience harm, while the other avoided all writing.','Both groups wrote only about their worst event of the year.'],1,
 '两组参与者的写作任务有什么不同？',['一组写未来，一组写童年。','一组写最好与最坏的事，另一组写最好与第二好的事。','一组被安排遭遇伤害，另一组完全不写作。','两组都只写一年中最坏的一件事。'],
 ['A 时间窗都是此前七天，并非未来与童年。','B 对应两组各自的事件组合。','C 操作是回顾写作，不是让人现实中遭遇坏事；两组都写。','D best、second-best 和 seven days 均被误换。'],
 ['Some participants wrote about the best event and the worst event they had experienced over the previous seven days, while other participants wrote about their best event and their second-best event.'],
 'evaluated','评价；评估','写作后评价过去一周及视角变化，不是观察未来结果','The students evaluated the course after the final session.',['evaluate an experience','evaluate one’s life'],
 '最后一个实验检验，能否让人觉得自己度过了更丰富的一周。有些参与者写此前七天最好和最坏的事，另一些写最好和第二好的事。写完后，他们评价过去一周，反思任务让自己对自身与世界的看法改变多少——也就是视角变化。')

add(16,'逻辑关系','What pattern of reports accompanies greater perspective change?',
 ['Less richness and more happiness.','More richness and more happiness in every individual.','No relationship with richness but a guaranteed rise in meaning.','Greater reported richness and lower reported happiness.'],3,
 '更多视角变化伴随怎样的报告模式？',['更少丰富，更多幸福。','每个人都更丰富且更幸福。','与丰富无关，却保证意义上升。','自报更丰富，同时自报幸福更少。'],
 ['A 把两个方向都读反。','B 最后一句是 less happiness，不是全体都更多幸福。','C 这里没有关于意义保证的结果。','D 两个 the more... 分别对应 richness 增和 happiness 减；报告间关联不能扩成所有人的必然因果。'],
 ['the more perspective changes they reported, the psychologically richer they reported their lives to be.','the more perspective change they reported, the less happiness they reported.'],
 'likelihood','可能性','increased the likelihood 描述更可能发生，不等于每个人必然发生','Clear instructions increased the likelihood of completing the task.',['the likelihood of change','increase the likelihood'],
 '相比写两件正面事件的人，写最好与最坏事件的人报告了更大程度的视角变化。简言之，写最坏事件提高了视角变化的可能性。最重要的是，报告的视角变化越多，他们自报的人生越心理丰富。有趣的是，视角变化报告越多，幸福报告越少。')

add(17,'作者意图','What function does the comparison with books and movies serve?',
 ['It illustrates how negative elements can add complexity and perspective change in the reported task.','It recommends deliberately causing bad events in real life.','It proves that every painful event always improves happiness.','It claims that fictional characters were the experiment’s participants.'],0,
 '与书籍和电影的比较起什么作用？',['说明负面成分可在所述任务中增添复杂性与视角变化。','建议故意在现实中制造坏事。','证明每件痛苦事件总会改善幸福。','声称虚构人物就是实验参与者。'],
 ['A Just as 引出类比，把作品戏剧性与此处视角变化连接。','B 这是回顾写作结果的解释，不是制造伤害的建议。','C richer 不能改为 always happier，单个任务也不是所有事件。','D 作品是比喻对象，不是参与者身份。'],
 ['Just as negative emotions such as fear and jealousy add drama to books and movies','the worst event had induced perspective change'],
 'induced','引起；促成','此处为作者对该任务结果的概括，不能扩成所有坏事都有益','The unfamiliar question induced a moment of reflection.',['induce a change','induce a response'],
 '正如恐惧、嫉妒等负面情绪给书籍和电影增添戏剧性，最坏的事件在这里引发视角变化，使参与者的人生在心理上更丰富。')

add(18,'细节','How is diversity distinguished from novelty here?',
 ['Diversity means doing the same thing without any emotional response.','Diversity is defined by wealth, while novelty is defined by income.','Novelty concerns difference from routine; diversity concerns a wide range of attention and emotion.','Novelty and diversity are both defined as memorising facts.'],2,
 '这里怎样区分多样性与新奇？',['多样性指无情绪地重复同一件事。','多样性由财富定义，新奇由收入定义。','新奇指不同于常规，多样性指广泛调动注意与情绪。','两者都被定义为记忆事实。'],
 ['A wide range 与单一重复、无情绪相反。','B 本段没有金钱定义。','C 两个标签后的解释各自准确对应。','D 原文定义不是背诵事实。'],
 ['Novelty: there’s something different from the same old, same old. Diversity: a wide range of attention and emotion is deployed.'],
 'deployed','调动；运用','指注意力和情绪被广泛调动，不是部署军队','Different skills were deployed to solve the problem.',['deploy attention','deploy a range of skills'],
 '那么，心理丰富由什么构成？本章从 Grace 的 WWE 之行、不典型的一天到一学期留学，这些例子有共同元素。新奇：有别于一成不变。多样：广泛的注意与情绪被调动。')

add(19,'细节','What is emphasised “Above all”?',
 ['Learning something new and gaining a new perspective.','Keeping every experience predictable and comfortable.','Ensuring that life is difficult without learning from it.','Memorising a vivid scene without any change in understanding.'],0,
 'Above all 特别强调什么？',['学到新东西，获得新视角。','让每种经历都可预测且舒适。','确保生活困难，却不从中学习。','只记住鲜明场景，不改变理解。'],
 ['A Above all 后直接接 learn something new，再接 gain perspective。','B more difficult and complex than usual 与保证舒适可预测不同。','C 挑战后明确强调学习，不能删去。','D vivid 是前面的 memorable，Above all 则进一步强调理解变化。'],
 ['Above all, you learn something new. You gain some new perspective.'],
 'memorable','值得记住的；令人难忘的','这里以 life is vivid 解释，随后仍加上学习与视角变化','The unexpected conversation made the visit memorable.',['a memorable experience','a memorable encounter'],
 '挑战：生活比平时更困难、更复杂。难忘：生活鲜明生动。最重要的是，你学到了新东西，获得了新视角。')

add(20,'主旨','Which mapping preserves the author’s concluding distinction?',
 ['Meaning: unusual experiences only; happiness: frustrating challenges only.','Richness: eliminating all unpleasantness; meaning: financial success only.','Happiness and meaning are both defined as avoiding other people.','Happiness: reliable positive experience; meaning: compassionate dedication; richness: unusual experience, challenge, and learning.'],3,
 '哪组对应保留作者结尾的区分？',['意义只靠异常经历；幸福只靠令人沮丧的挑战。','丰富就是消除所有不快；意义只靠财务成功。','幸福和意义都被定义为回避他人。','幸福侧重稳定正面体验；意义侧重慈悲投入；丰富侧重异常经历、挑战和学习。'],
 ['A 三个维度的重点被错配且添加 only。','B though...unpleasant 承认不快，意义也不是财务定义。','C Dedicating...to others 明确面向他人。','D 三句各自的侧重均保留，不把重点误作完全互斥类别。'],
 ['Simplifying one’s life so as to have reliably positive experiences, or contentment, is key to happiness.','Dedicating one’s life to others with compassion is key to meaning.','Experiencing the unusual, challenging oneself, and learning new things'],
 'compassion','同情与关怀；慈悲','修饰投入他人生活的态度，不是只追求个人成就','She responded to the newcomer’s difficulties with compassion.',['with compassion','show compassion for others'],
 '这些发现共同描绘了一幅清楚图景（也见第 1 章表 1）。简化生活，获得稳定的正面体验或满足，是幸福的关键。带着慈悲把生命投入他人，是意义的关键。经历不寻常之事、挑战自己、学习新东西——尽管有时令人挫败或不愉快——则是心理丰富的关键。')

add(21,'作者意图','Why does the lab seek to quantify psychological richness?',
 ['To establish that Joy and Linda are the only possible rich lives.','To find out how common psychologically rich lives are beyond exceptional stories.','To replace scientific evidence with a collection of favourite anecdotes.','To assume in advance that ordinary people cannot live richly.'],1,
 '实验室为什么要量化心理丰富？',['确认只有 Joy 和 Linda 可能有丰富人生。','了解非凡故事之外，心理丰富的生活有多普遍。','用喜欢的轶事取代科学证据。','预先假定普通人不可能丰富。'],
 ['A exceptional 引出进一步普遍性问题，不是断言只有两例。','B How common 与 determine how common 直接交代研究目标。','C Is there any scientific evidence 明确寻求证据。','D 开放提问不等于预设普通人不可能。'],
 ['Our lab set out to quantify psychological richness in people’s lives and determine how common it is.'],
 'quantify','量化；以数量衡量','把概念变成可分析的程度或数量，不等于测量已完美无误','The team tried to quantify changes in participation.',['quantify a difference','quantify psychological richness'],
 'Joy Ryan 和 Linda 的生活虽有趣，也显得非凡。普通人过心理丰富生活有多常见？有没有科学证据说明相当多的人确实如此？我们的实验室着手量化人们生活中的心理丰富，了解它有多普遍。')

add(22,'细节','Why are obituaries proposed as useful material?',
 ['They guarantee a random sample of every person in society.','They record private emotions with perfect accuracy.','They tell life stories that can be coded across a range of people.','They contain only the financial assets of CEOs.'],2,
 '为什么作者提出使用讣告作为材料？',['保证随机代表社会上每一个人。','完美记录私密情绪。','包含可编码分析、涉及多类人物的人生故事。','只含 CEO 的财产信息。'],
 ['A wide swath 不等于随机或无选择偏差。','B Perhaps...could 保留探索性，未保证内心记录完全准确。','C Every obituary tells a life story 与 coding、职业范围共同支持。','D from CEOs...to musicians and athletes 范围并非仅 CEO，且不是只查财产。'],
 ['Every obituary tells a life story.','By coding hundreds of obituaries for different life characteristics, we could cover a wide swath of people'],
 'obituaries','讣告；逝者生平纪述','作为第三方叙述的人生材料，不等同逝者本人的完整自报','The archive contains newspaper obituaries from several decades.',['newspaper obituaries','analyse obituaries'],
 '我们意识到，可以在生命结束时通过讣告评价人生，这是一项有价值的工具。每份讣告都讲述人生故事。也许分析内容，就能了解一个人的生活多幸福、有意义、心理丰富。给数百份讣告按不同人生特征编码，可涵盖从 CEO、政治人物到音乐家、运动员的广泛人群。')

add(23,'语境词义','What does “Blind to our hypotheses” mean here?',
 ['The assistants could not see the obituary text.','The assistants were unaware of the researchers’ hypotheses while rating.','The assistants had forgotten all twelve themes.','The researchers had no hypotheses of any kind.'],1,
 '这里 Blind to our hypotheses 是什么意思？',['助理看不到讣告文字。','评分时，助理不知道研究者的假设。','助理忘了全部十二个主题。','研究者完全没有假设。'],
 ['A 他们 read and rate，blind 的对象是 hypotheses，不是文字。','B blind to 指对特定信息不知情，准确限定评分者。','C 没有忘记主题的说明。','D our hypotheses 表明有假设，只是评分者不知。'],
 ['Blind to our hypotheses, they rated the happiness, meaningfulness, and psychological richness of the lives described in each obituary.'],
 'hypotheses','假设；待检验的解释','是研究者的预测或解释，不是已证实结果','The study compared two hypotheses about memory.',['test hypotheses','blind to the hypotheses'],
 '我们聘请三名研究助理，在 2016 年六月阅读并按十二个主题评分《纽约时报》的 101 份讣告。他们不知道我们的研究假设，评价每份讣告所述人生的幸福、意义与心理丰富。')

add(24,'细节','Which definition is used for psychological richness in the rating procedure?',
 ['A life consisting entirely of comfort, satisfaction, and joy.','A life measured solely by contributions to society.','A life with the highest income among those profiled.','A life involving many diverse and unusual experiences.'],3,
 '评分程序对心理丰富采用什么定义？',['完全由舒适、满足、喜悦组成的生活。','仅以社会贡献衡量的生活。','所述人物中收入最高的生活。','遭遇许多多样、不寻常经历的生活。'],
 ['A comfortable、satisfied、joyful 是这里 happy life 的定义，不能错配。','B contribution...difference 对应 meaningful life。','C 没有以最高收入定义心理丰富。','D diverse, unusual experiences 是该维度的原文定义。'],
 ['a psychologically rich life (a life in which a person encounters many diverse, unusual experiences).'],
 'on a scale of','以……的量表衡量','说明每个人生按一至五分评价，不能把分值当人物数量','Respondents rated the item on a scale of one to five.',['on a scale of 1 to 5','a rating scale'],
 '首先，我们给评分者明确的定义：幸福生活是舒适、满足、愉悦的生活；有意义生活是对社会作贡献、产生影响的生活；心理丰富生活是遇到许多多样、不寻常经历的生活。然后请他们用一至五分评分，回答“此人的生活多幸福？”“多充实？”“多有趣？”等问题。')

add(25,'推断','What check is described before data analysis?',
 ['The researchers checked agreement across the three assistants’ ratings.','They established that every obituary was a perfectly complete life record.','They proved that a rating of five was correct for every person.','They required the assistants to know the hypotheses before scoring.'],0,
 '数据分析之前进行了什么检查？',['检查三位助理的评分是否一致。','确立每份讣告都是完美完整的人生记录。','证明每个人都应评五分。','要求助理先知道假设才评分。'],
 ['A consistent across the three research assistants 指跨评分者的一致性。','B 一致性不是材料完整性的证明。','C 一致不等于每人分数相同或都应五分。','D 本句没有这种要求，也不能把一致性检查改成告知假设。'],
 ['We checked that ratings were consistent across the three research assistants before analyzing our data.'],
 'consistent','一致的；相互吻合的','这里指评分者之间的评分一致，不自动保证对每个人生判断绝对准确','The reviewers checked whether their ratings were consistent.',['consistent ratings','consistent across raters'],
 '分析数据之前，我们检查了三位研究助理的评分是否一致。','inference')

assert len(out)==25 and [q['id'] for q in out]==[t['questionId'] for t in targets]

def persist():
 path=ROOT/'source/short-questions/additional.json';existing=load('source/short-questions/additional.json');byid={q['id']:q for q in existing}
 for q in out:
  if q['id'] in byid:assert byid[q['id']]==q,('Refuse to overwrite changed authoring',q['id'])
  else:existing.append(q)
 path.write_text(json.dumps(existing,ensure_ascii=False,indent=2)+'\n',encoding='utf8',newline='\n')
 review=dict(batchId='batch-013',date='2026-10-22',pdfSha256=b['pdfSha256'],checkedPdfPages=list(range(49,55)),questionIds=[q['id'] for q in out],paragraphs=[dict(id=pid,textSha256=hashlib.sha256(pp[pid]['text'].encode()).hexdigest()) for pid in dict.fromkeys(q['paragraphId'] for q in out)],note='完整 PDF 原页视觉复核，包括跨页引语；个案、周报观察、写作实验与讣告评分分别说明，候选句界不冒充人工最终分句。')
 (ROOT/'source/short-questions/review-chapter05-06-next25.json').write_text(json.dumps(review,ensure_ascii=False,indent=2)+'\n',encoding='utf8',newline='\n')
 print('Saved',len(out),'of 25 individually authored exercises')

if __name__=='__main__':persist()
