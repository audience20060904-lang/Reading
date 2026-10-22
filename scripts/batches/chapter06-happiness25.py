"""25 individually authored exercises for frozen targets, PDF pages 62-65.
Preserve printed English, source positions and all previously published questions.
"""
from pathlib import Path
import json,hashlib
ROOT=Path(__file__).resolve().parents[2]
load=lambda p:json.loads((ROOT/p).read_text(encoding='utf8'))
b=load('public/data/book.json');plan=load('public/data/reading-plan.json');targets=load('source/short-questions/batch016-targets.json')['targets']
ss={s['id']:s for s in b['sentences']};pp={p['id']:p for p in b['paragraphs']};out=[]
def add(i,kind,prompt,options,answer,prompt_zh,options_zh,analyses,quotes,word,meaning,context,example,collocations,translation,support='explicit'):
 t=targets[i-1];u=next(u for u in plan['units'] if u['id']==t['readingUnitId']);group=[ss[sid] for sid in u['sentenceIds']];p=pp[u['paragraphId']];text=p['text'][group[0]['start']:group[-1]['end']]
 assert hashlib.sha256(text.encode()).hexdigest()==t['passageSha256'];evidence=[]
 for quote in quotes:
  offset=text.find(quote);assert offset>=0,(i,quote);start=group[0]['start']+offset;end=start+len(quote);touching=[s for s in group if s['start']<end and s['end']>start]
  evidence.append(dict(quote=quote,sentenceIds=[s['id'] for s in touching],sources=list({(r['pdfPage'],r['block']):r for s in touching for r in s['sources']}.values())))
 assert word.lower() in text.lower(),(i,word)
 out.append(dict(id=t['questionId'],version=1,readingUnitId=u['id'],chapterId=u['chapterId'],sectionId=u['sectionId'],paragraphId=u['paragraphId'],sentenceIds=u['sentenceIds'],passage=text,prompt=prompt,options=options,answer=answer,type=kind,promptZh=prompt_zh,optionsZh=options_zh,analyses=analyses,evidence=evidence,vocabulary=[dict(word=word,meaning=meaning,context=context,example=example,collocations=collocations)],translation=translation,support=support,editorialStatus='PDF 第 62–65 页逐题原页核对；保留固定原句、概率和 potential/probably 限定；区分作者解释、电视人物、历史叙述与政治人物引语归属'))



add(1,'同义改写','Which wording best preserves the meaning of “is linked to” in this sentence?',
 ['Is associated with.','Is completely identical to.','Is the only possible cause of.','Is incompatible with.'],0,
 '哪种表达最能保留本句 is linked to 的含义？',['与……相关联。','与……完全相同。','是……唯一可能的原因。','与……无法并存。'],
 ['A linked to 表示有关联，保留原句强度。','B 关联不等于两个概念完全相同。','C 既没有唯一，也没有仅凭本句确定因果的依据。','D 原句表示联系，而非不相容；This 指前文，但本题只考查当前句中明确出现的关系措辞。'],
 ['extraversion is linked to a psychologically rich life.'],
 'linked to','与……有关联','指外向性与心理丰富人生之间的联系，不能扩写为单一决定原因','Regular practice is linked to improved performance in this survey.',['be linked to','closely linked to'],
 '这是外向性与心理丰富人生发生联系的一种方式。')

add(2,'细节','Which factor is offered to explain why extraverts explore the social world more?',
 ['Their certainty that no conversation can ever go badly.','Their wish to avoid every unfamiliar person.','Their confidence and self-assurance.','Their fear of losing all existing friendships.'],2,
 '作者提出什么因素，解释外向者更多探索社交世界？',['确信没有任何谈话会出问题。','希望避开所有不熟悉的人。','自信与自我确信。','害怕失去全部现有友谊。'],
 ['A not threatening 是主观感受，不是所有谈话必成功的客观保证。','B 与 explore the social world 及 meeting a new person 的方向相反。','C One factor 后直接给出 confidence and self-assurance，不能漏掉 one 所保留的非唯一性。','D 本段没有失去老朋友的担忧；反问 What is there to lose 强化较少畏惧的态度。'],
 ['One factor is their confidence and self-assurance.'],
 'self-assurance','自信；对自己的确信','与 confidence 并列，解释结识陌生人时较少感到威胁','Her self-assurance helped her begin the conversation.',['confidence and self-assurance','a sense of self-assurance'],
 '从基本层面说，外向者为什么更多探索社交世界？一个因素是他们的自信与自我确信。自信时，结识新朋友并不令人感到威胁。有什么可失去的呢？')

add(3,'逻辑关系','How does the passage connect confidence with starting a conversation?',
 ['Confidence makes people focus more on every possible negative judgment.','Greater confidence makes entering a new conversation more likely.','Confidence removes any need to learn from other people.','Confidence guarantees that every story told will be interesting.'],1,
 '本段怎样把自信与开始谈话联系起来？',['自信使人更关注每一种可能的负面评价。','越自信，越可能加入新的谈话。','自信消除了向别人学习的需要。','自信保证每个讲出的故事都很有趣。'],
 ['A 原文转而关注 benefits，而不是更担心负面评价。','B The more...the more likely...明确表达概率随自信增加的关系。','C learning something new 恰是列出的收益之一。','D more likely 不是保证，interesting stories 也不代表每个故事必有趣。'],
 ['The more confident you are, the more likely you are to enter a new conversation.'],
 'positive spiral','正向循环；积极的螺旋','本段用来描写较少畏惧、关注收益与更愿谈话相联的过程，不是无限上升定律','A small success can begin a positive spiral of effort and confidence.',['a positive spiral','create a positive spiral'],
 '你不担心对方负面评价自己，或给人留下坏印象。相反，你想到的是收益：结识新人、学到新东西、分享有趣的故事。这里也存在一种正向循环。你越自信，就越可能加入新的谈话。')

add(4,'逻辑关系','Which sequence best reflects the passage’s account of parties?',
 ['A rich party experience makes another party impossible.','Fewer conversations always produce a richer party experience.','Attending one party proves that someone will attend every later party.','More conversations enrich the experience, which may encourage another visit.'],3,
 '哪一顺序最符合本段对聚会经历的解释？',['一次丰富的聚会经历使参加下一次成为不可能。','谈话越少，聚会总是越丰富。','参加一次聚会证明以后每次都会去。','更多谈话丰富经历，而这种经历可能鼓励再次参加。'],
 ['A 原文 more likely to go，不是无法再去。','B 将 more new conversations 的方向倒置，还添加 always。','C 可能性不能换成每次都去的保证。','D 前句谈话增加丰富性，后句说丰富经历提高再参加的可能；这是作者的解释，不是本段提供了每一次聚会的实验结果。'],
 ['The more new conversations you enter, the psychologically richer the party becomes for you.','is more likely to go to another party.'],
 'enriching','使丰富的；增进体验的','psychologically enriching 指为心理经历增加内容，不单指愉快或物质收益','The exchange was an enriching experience for both students.',['an enriching experience','psychologically enriching'],
 '你加入的新谈话越多，这场聚会对你而言就越心理丰富。在一次聚会上获得使心理更丰富的经历的人，更可能参加另一场聚会。')

add(5,'细节','What did the cited study report about extraverts in college?',
 ['They participated in more college activities than introverts.','They all joined every campus organisation.','They took part only in athletic activities.','They had less energy than introverts but more free time.'],0,
 '所引研究报告了大学外向者的什么情况？',['他们比内向者参与更多大学活动。','他们全都加入每个校园组织。','他们只参加体育活动。','他们精力比内向者少，但空闲时间更多。'],
 ['A found that...more college activities...than introverts 直接给出比较。','B 更多不是每个人参与所有组织。','C 原例还包括校园社团、服务和志愿者组织。','D 精力方向相反，也没有空闲时间数据；研究中的参与差异不能单凭本段变成精力导致结果的确定证明。'],
 ['extraverts were involved with more college activities, such as intramural athletics, campus clubs, and service and volunteer clubs, than introverts.'],
 'intramural','校内的；机构内部的','intramural athletics 指校内体育活动，不是校际竞赛','The university organises intramural athletics each term.',['intramural athletics','intramural sports'],
 '外向性中另一个可能与心理丰富性相关的方面是精力。外向者往往比内向者更有精力。一个人精力越多，就能参与越多活动。例如，一项研究发现，外向者比内向者参与更多大学活动，包括校内体育、校园社团，以及服务和志愿者组织。')

add(6,'细节','Which comparison is actually made about Joy Ryan?',
 ['She has visited more parks than every younger traveller.','She is more energetic than every other person her age.','She is full of energy compared with other people in their nineties.','She is unable to reach remote parks despite her energy.'],2,
 '本段实际对 Joy Ryan 作了哪种比较？',['她比每位年轻旅行者游览的公园都多。','她比其他所有同龄人都有精力。','与其他九十多岁的人相比，她精力充沛。','尽管有精力，她仍无法到达偏远公园。'],
 ['A 比较对象不是年轻旅行者，也没给公园数量排名。','B 与其他人比较不能扩大为超越所有同龄人。','C Compared to other ninety-somethings 明确比较范围。','D can visit 正好说明能去；这是个人示例，不是对所有九十岁人群的实验结论。'],
 ['Compared to other ninety-somethings, she is full of energy.'],
 'remote','偏远的；远离中心地区的','形容她可前往的国家公园，不是遥控或远程办公','The path leads to a remote village in the mountains.',['remote national parks','a remote area'],
 'Joy Ryan 在这里又是一个很好的例子。与其他九十多岁的人相比，她精力充沛。正因如此，她能游览偏远的国家公园，享受不同寻常、心理丰富的经历。')

add(7,'细节','How is Mr. Rogers introduced as an example of a happy person?',
 ['As a participant whose mood was measured after a laboratory task.','As a governor discussing social policy.','As a traveller who avoids singing and dancing.','As a cheerful, friendly neighbour in a television show.'],3,
 'Mr. Rogers 被怎样引入，作为幸福人物的例子？',['完成实验任务后接受情绪测量的参与者。','讨论社会政策的州长。','回避歌舞的旅行者。','电视节目中面带愉快笑容的友善邻居。'],
 ['A 本段是电视节目人物描述，不是实验参与者报告。','B 当前段落没有州长或政策讨论。','C singing、dancing 都是节目的内容，不是他所回避的事。','D In this show、friendly neighbor、cheerful smile 分别对应场景和特征。'],
 ['In this show, he is a friendly neighbor with a cheerful smile.'],
 'cheerful','愉快的；开朗的','描述节目里邻居的笑容，不是对其全部现实生活的测量','A cheerful greeting made the room feel welcoming.',['a cheerful smile','a cheerful greeting'],
 '幸福的人与心理丰富的人是否不同？Mister Rogers’ Neighborhood 中的 Mr. Rogers，是一个“幸福”人物的例子。在这档节目里，他是面带愉快笑容的友善邻居。节目包括许多歌唱、舞蹈和木偶戏。')

add(8,'作者意图','What is the effect of the question “Who wouldn’t want to hang out with a guy” here?',
 ['It reports a survey in which nobody liked the character.','It enthusiastically suggests that the character is appealing company.','It asks the reader to calculate how many people avoid television.','It establishes that every viewer has personally met the character.'],1,
 '这里 Who wouldn’t want to hang out with a guy 这一问法有什么作用？',['报告一项没有人喜欢该角色的调查。','热情暗示这个角色是令人愿意相伴的人。','要求读者计算有多少人回避电视。','确立每位观众都亲自见过该角色。'],
 ['A 修辞性问句不是调查结果，且语气相反。','B 前句 lot of fun 加上反问，表达欣赏与亲近感。','C 没有数字、样本或计算任务。','D 想相处不等于实际见面，也不能把反问视为所有观众偏好的实测。'],
 ['That’s a lot of fun! Who wouldn’t want to hang out with a guy who sings,'],
 'hang out with','与……相处；一起消磨时光','口语表达一起待着，不是正式工作或实际见面记录','We often hang out with friends after class.',['hang out with friends','want to hang out'],
 '这可真有趣！谁不想和一个唱着“请问，你愿意做我的邻居吗？”的人一起相处呢？')

add(9,'细节','Which trait is excluded from the happy-life pattern reported in the meta-analysis?',
 ['Emotional stability.','Conscientiousness.','Openness to experiences.','Agreeableness.'],2,
 '这项元分析所报告的幸福人生模式，没有把哪个特质包括在内？',['情绪稳定性。','尽责性。','经验开放性。','宜人性。'],
 ['A emotional stability 明列于模式中。','B conscientiousness 明列于模式中。','C but not by openness to experiences 明确排除它作为该模式的特征；不是说开放的人一定不幸福。','D agreeableness 明列其中。元分析的相关模式与电视人物引例作用不同，不能把后者当作实验。'],
 ['a happy life is characterized by emotional stability, extraversion, conscientiousness, and agreeableness, but not by openness to experiences.'],
 'meta-analysis','元分析；荟萃分析','文中引用 Anglim 及同事综合研究的分析，不是只凭一个节目角色下结论','The meta-analysis combined findings from several studies.',['a meta-analysis of studies','conduct a meta-analysis'],
 'Mr. Rogers 展现了幸福者的核心特征：外向、情绪稳定（较少神经质）、尽责、宜人。心理丰富性的相关模式，与幸福的模式相当不同。据 Anglim 及同事的元分析，幸福人生以情绪稳定、外向、尽责和宜人为特征，却不以经验开放性为特征。')

add(10,'逻辑关系','Why does the author say the two strongest predictors of happiness “make sense”?',
 ['Their affective meanings align with a definition emphasising positive over negative emotions.','They prove that happy people never experience negative emotion.','They show that openness is the same thing as emotional stability.','Their names demonstrate that personality never changes.'],0,
 '作者为什么说幸福的两项最强预测因素“合乎道理”？',['它们的情感含义与积极情绪占优势、消极情绪相对较少的定义一致。','它们证明幸福者从不体验消极情绪。','它们说明开放性与情绪稳定性是同一概念。','它们的名称证明人格永不改变。'],
 ['A some scholars 对外向性与神经质的概念化，和幸福的情绪定义相衔接，形成文中的理由。','B relative lack 是相对较少，不是绝对没有。','C 没有将开放性等同情绪稳定性。','D 本段讨论概念和关联，不讨论人格是否永不变化。'],
 ['by definition a happy life is the preponderance of positive emotions and relative lack of negative emotions'],
 'preponderance','占优势；占较大比重','表示积极情绪较多，不代表消极情绪完全不存在','The report noted a preponderance of positive responses.',['a preponderance of','the preponderance of positive emotions'],
 '幸福人生的两项最强人格预测因素是情绪稳定性与外向性。一些人格学者把外向性理解为积极情感倾向（好心情），把神经质理解为消极情感倾向（坏心情）。按定义，幸福人生是积极情绪占优势、消极情绪相对较少；因此，外向与情绪稳定最能体现幸福人生，是合乎道理的。')

add(11,'推断','What limited conclusion is supported by the two travel-related examples?',
 ['All people who travel have exactly the same level of happiness.','Being open to experience prevents a person from being happy.','Rick Steves and Anthony Bourdain were measured in a laboratory experiment here.','Openness can coexist with different levels of happiness.'],3,
 '两个与旅行有关的人物例子支持什么有限结论？',['所有旅行者的幸福水平完全一样。','对经验开放会阻止一个人幸福。','Rick Steves 与 Anthony Bourdain 在这里接受了实验室测量。','开放性可以与不同的幸福水平并存。'],
 ['A 原文恰恰对照 happy 与 less happy，不能扩大为所有旅行者。','B 文中有 happy and open 的组合。','C 没有报告两人的实验测量；他们是作者的说明性例子。','D 作者并列幸福且开放、较不幸福但开放两种组合，支持这个有限结论；almost as many 也不能据本段编成精确人数或比例。'],
 ['are happy and open to experience','are less happy but open to experience.'],
 'not necessarily','不一定；未必','否定必然性：幸福者未必开放，但不排除幸福又开放者','A longer answer is not necessarily a better answer.',['not necessarily true','not necessarily the case'],
 '总体而言，幸福人格与心理丰富人格的关键区别是：幸福者不一定对经验开放，而心理丰富者相当开放。作者说，这意味着，像旅行作家 Rick Steves 一样既幸福又开放的人，与像厨师兼旅行纪录片制作者 Anthony Bourdain 一样较不幸福但开放的人，数量几乎相当。','inference')

add(12,'逻辑关系','What main link is proposed between the listed personality traits and happiness?',
 ['The traits remove all need for social relationships.','The traits are connected with good relationships, whose quality predicts happiness.','Happiness depends only on being popular with strangers.','The traits ensure that every relationship is free from disagreement.'],1,
 '作者在人格特质与幸福之间提出什么主要联系？',['这些特质消除了社交关系的所有需要。','这些特质与良好关系相联，而关系质量能预测幸福。','幸福只取决于受陌生人欢迎。','这些特质确保每段关系都没有分歧。'],
 ['A quality of social relationships 正是作者的重点。','B Primarily because 给出关系质量这一解释环节，再用 friendly、stable、reliable、kind 作说明。','C quality 不是只看陌生人的好感，only 也无依据。','D 没有无分歧的保证；predictor 也不能自行改成唯一确定原因。'],
 ['Primarily because the quality of social relationships is a big predictor of happiness.'],
 'reliable','可靠的；值得信赖的','形容有助于良好人际关系的人格表现，不是量表信度的术语用法','A reliable colleague follows through on agreed tasks.',['a reliable person','reliable and kind'],
 '为什么情绪稳定、外向、尽责与宜人有利于幸福人生？主要因为社交关系的质量是幸福的重要预测因素。谁拥有良好的社交关系？像 Mr. Rogers 这样的人：友善、稳定、可靠而善良。')

add(13,'语境词义','What does “emotionally volatile” mean in this description?',
 ['Prone to rapid or unpredictable emotional changes.','Consistently calm with little emotional fluctuation.','Skilled at recalling every past feeling accurately.','Unable to experience any emotion at all.'],0,
 '这里 emotionally volatile 是什么意思？',['容易出现快速或难以预测的情绪变化。','始终平静，情绪几乎不波动。','善于准确回忆过去每种感受。','完全无法体验任何情绪。'],
 ['A volatile 指不稳定、易变化，修饰情绪。','B 与 volatile 相反。','C 不涉及情绪记忆能力。','D 情绪易变不等于毫无情绪。整句把多个特征并列作概括，不能单抽 introverted 就断言每个内向者都交不到朋友。'],
 ['emotionally volatile'],
 'volatile','易变的；不稳定的','emotionally volatile 指情绪起伏不定，不是物质易挥发或完全无情绪','His mood was volatile during the stressful week.',['emotionally volatile','a volatile mood'],
 '一个情绪起伏不定、内向、不可靠且爱争辩的人，不容易赢得很多朋友。')

add(14,'作者意图','Why mention deadlines and family birthdays in this passage?',
 ['To argue that remembering dates removes every financial problem.','To show that family occasions are the only basis of happiness.','To illustrate the practical effort involved in maintaining stability.','To suggest avoiding any task that feels unpleasant.'],2,
 '这里为什么提到截止日期与家人的生日？',['论证记住日期能消除所有财务问题。','说明家庭场合是幸福的唯一基础。','举例说明维持稳定需要付出的实际努力。','建议回避任何令人不愉快的任务。'],
 ['A 记忆日期只是付出的一部分，不是解决所有财务问题的保证。','B 本段同时谈 financial 与 relationship stability，没有唯一基础的说法。','C work hard 后列举记日期和做不想做的事，具体化维持稳定的责任。','D 最后一句恰是需要做某些不想做的事。'],
 ['In order to achieve these, we must work hard on our finances and our relationships.','We need to remember the deadlines of various tasks and the birthdays of children and in-laws.'],
 'in-laws','姻亲；因婚姻形成的亲属','与 children 并列，指需要维系关系并记住生日的家人','They spent the holiday visiting their in-laws.',['visit the in-laws','children and in-laws'],
 '第二，财务稳定与关系稳定对幸福人生很重要。为了做到这些，我们必须在财务和人际关系上付出努力。我们需要记住各种任务的截止日期，以及孩子和姻亲的生日。我们也需要做一些自己不想做的事情。')

add(15,'推断','Which conclusion about a boss’s liking is justified by the wording?',
 ['It guarantees both a raise and a promotion.','It is associated here with a greater chance of a raise or promotion.','It makes work relationships irrelevant to a career.','It proves that every well-liked employee works harder.'],1,
 '关于上司的喜欢，本段措辞支持哪项结论？',['保证同时加薪和晋升。','在此被描述为与更高的加薪或晋升机会相联。','它使工作关系与职业毫无关系。','证明每位受欢迎的员工都更努力。'],
 ['A more likely 不是保证，or 也不是必须同时发生。','B 对应条件句中的概率比较，不改成必然结果。','C 前文刚说宜人性改善工作与家庭关系。','D 本段未测量所有受喜欢员工的努力程度，不能推导该事实。'],
 ['If your boss likes you, you are more likely to receive a raise or a promotion than if they don’t like you.'],
 'conscientiousness','尽责性；认真负责的倾向','本段承接维持稳定所需的责任与努力，和宜人性分工说明','Conscientiousness can be reflected in careful planning and follow-through.',['high conscientiousness','conscientiousness and agreeableness'],
 '因此，尽责性确实有帮助。宜人性既能改善工作关系，也能改善家庭关系。如果上司喜欢你，你得到加薪或晋升的可能性，比上司不喜欢你时更高。','inference')

add(16,'语境词义','What does “a boon” mean in this account of coping with bad events?',
 ['A guarantee that bad events will never happen.','A permanent cause of difficult circumstances.','A requirement to suppress every negative feeling.','A helpful benefit or advantage.'],3,
 '在应对坏事的叙述中，a boon 是什么意思？',['坏事永不发生的保证。','困难处境的永久原因。','压抑所有负面感受的要求。','一种有帮助的益处或优势。'],
 ['A Bad things happen 明说仍会遇到坏事。','B 上下文讨论帮助恢复，不是造成困难。','C 没有要求压抑所有负面情绪。','D positivity、help...recover、there to help 都指向助益；心理免疫系统在这里是作者的心理恢复类比，并非医疗处方。'],
 ['extraversion and emotional stability are a boon'],
 'boon','益处；有帮助的东西','形容困难出现时外向性和情绪稳定性带来的助益，而非免除困难','The extra time was a boon to the small team.',['a boon to someone','a real boon'],
 '第三，外向性所关联的积极性，有助于应对困难处境。情绪稳定性帮助我们更快从坏消息中恢复。好人也会遇到坏事。但坏事发生时，外向性与情绪稳定性是一种助益（无论如何，我们的心理免疫系统也会提供帮助）。')

add(17,'推断','How should the proposed explanation involving exploration be interpreted?',
 ['As one possible reason, since exploration can have different kinds of outcomes.','As proof that trying a new restaurant always increases happiness.','As evidence that open people never have unpleasant experiences.','As a claim that every exploration necessarily reduces happiness.'],0,
 '涉及探索的解释，应怎样理解？',['一种可能原因，因为探索可能带来不同结果。','证明尝试新餐厅总会增加幸福。','证明开放者从不遇到不愉快的经历。','声称每次探索都必定减少幸福。'],
 ['A potential reason 保留不确定性，后面同时讨论正面与负面结果。','B when...positive outcome 是条件，不是每次都正面。','C 负面探索经历明列于最后一句。','D 正面结果与更高幸福相联，不能说所有探索都减少幸福；uncorrelated 也不等于对每个人都毫无关系。'],
 ['One potential reason is the greater motivation to explore among open people.','But when the exploration results in a negative experience, it is not.'],
 'potential','可能的；潜在的','限定 reason，表示作者提出可能解释，尚非由本段确立的唯一原因','The report discusses one potential explanation for the pattern.',['a potential reason','a potential explanation'],
 '最后，为什么经验开放性与幸福人生不相关？一个可能原因是开放者更有探索动机。当探索（例如尝试一家新餐厅）带来正面结果时，它与更高幸福水平相联。但探索带来负面经历时，则并非如此。','inference')

add(18,'语境词义','What relationship does “antithetical to” express here?',
 ['A necessary precondition for.','In opposition to.','An exact synonym for.','A numerical measure of.'],1,
 '这里 antithetical to 表达什么关系？',['是……必要的先决条件。','与……相对立。','是……完全同义的表达。','是……的数值测量。'],
 ['A 表达对立，非必要前提。','B 对应作者将探索与作为幸福基础的稳定相对照。','C 对立不是同义。','D 不是数量或量表关系；本句是作者的概括，不能扩大成每次探索都会破坏幸福的实验结论。'],
 ['antithetical to the stability'],
 'antithetical to','与……相对立；与……不相容','在作者论述中将探索与稳定放在相对的一面，不是统计系数用语','The proposed restriction was antithetical to the group’s stated principles.',['antithetical to stability','antithetical to a principle'],
 '探索也与稳定相对立，而稳定是幸福人生的基础。')

add(19,'作者意图','Why introduce Thunberg and Huckabee as being at opposite political ends?',
 ['To establish that they support the same policies.','To show that meaningful lives require one particular party membership.','To report a controlled experiment comparing their personalities.','To ask what personalities may share despite different political positions.'],3,
 '为什么指出 Thunberg 与 Huckabee 位于政治光谱的两端？',['确立他们支持相同政策。','说明有意义人生要求加入某个特定政党。','报告比较两人人格的对照实验。','询问政治立场不同的人，其人格可能有什么共同之处。'],
 ['A opposite end 与政策相同不是同一意思。','B 作者跨立场举例，没有指定政党资格。','C 这是引入人物的论述，不是两人参加的实验报告。','D 先设政治差异，再以 What...in common 提出人格共同点的问题；本段并未直接给出共同点的完整答案。'],
 ['At the opposite end of the political spectrum','What do their personalities have in common?'],
 'political spectrum','政治光谱；政治立场的范围','表示不同政治立场，不是人物品德或研究评分的高低轴','The debate included speakers from across the political spectrum.',['the political spectrum','opposite ends of the spectrum'],
 '现在来想想过着有意义人生的人是什么样。瑞典环保活动者 Greta Thunberg 令人想到。在政治光谱的另一端，Mike Huckabee 也令人想到。他们的人格有什么共同之处？')

add(20,'细节','Which account matches the start of Greta’s protest as narrated in the book?',
 ['At nineteen, she protested daily inside the Swedish parliament.','At fifteen, she protested every Friday outside a university.','At fifteen, she protested every Friday in front of the Swedish parliament.','At fifteen, she began a campaign against all school education.'],2,
 '哪项符合书中叙述的 Greta 抗议起点？',['十九岁时，每天在瑞典议会内部抗议。','十五岁时，每周五在一所大学外抗议。','十五岁时，每周五在瑞典议会前抗议。','十五岁时开始反对一切学校教育的运动。'],
 ['A 年龄、频率和地点均错配。','B 地点是 parliament，不是 university。','C at age fifteen、every Friday、in front of the Swedish parliament 三处均对应。','D 标语强调 for Climate，不能改成反对一切教育；to date 的时间基准是原书叙述时，不冒充今天的实时状态。'],
 ['At age fifteen, Greta began protesting in front of the Swedish parliament every Friday'],
 'catalyzed','促成；推动；起催化作用','作者用来描述她对青年气候行动的推动，并非声称每一场行动都由她单独造成','The meeting catalyzed a wider discussion about transport.',['catalyze change','catalyze activism'],
 '十五岁时，Greta 开始每周五站在瑞典议会前抗议，举着写有“为气候罢课”的牌子。她的运动被称为“Fridays for Future”，传播到世界各地。她推动了大量青年气候行动；截至原书叙述时，她仍倡导减少碳排放、提高可持续性。Greta 始终投入自己的工作。')

add(21,'作者意图','What do the school break and relentless work illustrate in the author’s description?',
 ['The priority and sustained effort she gives to her activism.','The end of her interest in environmental issues.','A requirement that every meaningful life must abandon school.','An equal division of all her commitments in 2019.'],0,
 '作者描述的暂时离校与不懈工作，说明什么？',['她把行动工作放在优先位置，并持续付出努力。','她不再对环境议题感兴趣。','每种有意义人生都必须离开学校。','她在 2019 年平均分配所有事务。'],
 ['A dedicate all her energy、prioritizes、relentlessly 一起突出投入与优先顺序。','B 与持续工作相反。','C 人物例子不能变成所有人的教育建议或必要条件。','D prioritizes...over 明确并非平均分配。'],
 ['She prioritizes her environmental activism work over other commitments and works relentlessly.'],
 'conviction','坚定信念；确信','A woman of conviction 概括作者所描述的坚持，不是法律上的定罪','She spoke with conviction about the project’s purpose.',['a woman of conviction','act with conviction'],
 '2019 年，她甚至暂时离校，把全部精力投入行动。她把环保行动工作置于其他事务之上，不懈努力。一个拥有坚定信念的女人。')

add(22,'逻辑关系','What is given as the connection between Huckabee’s pastoral work and his move into politics?',
 ['His college required every religion student to become a governor.','He stopped listening to people once he became a pastor.','His work for a televangelist prevented any later public role.','Hearing policy-related personal struggles led him toward politics.'],3,
 '本段怎样联系 Huckabee 的牧师工作与从政？',['大学要求每位宗教学生都成为州长。','当牧师后，他停止听别人倾诉。','电视布道者的工作阻止他此后担任任何公共职务。','听到与政策有关的个人困境，使他转向政治。'],
 ['A 原文没有大学的此类要求。','B listened to so many 正相反。','C 文中叙述他后来成为州长。','D so many...policy-related that...turned to politics 给出作者所述的转向原因，不要把履历先后单独误认成普遍因果定律。'],
 ['he listened to so many personal stories of struggles that were policy-related that he turned to politics'],
 'pastor','牧师','指他在 Texarkana 的宗教工作角色，不是州长或政策分析师的同义词','The pastor listened to concerns raised by local families.',['serve as a pastor','a local pastor'],
 'Mike Huckabee 出生于 Arkansas。他在大学学习宗教，之后成为电视布道者 James Robison 的工作人员，随后在 Texarkana 当牧师。做牧师时，他听到太多与政策有关的个人困境故事，因此转向政治，后来成为 Arkansas 州长。')

add(23,'作者意图','What does the food example illustrate about Huckabee’s presentation of policy views?',
 ['He cites a scientific estimate of the actual danger posed by refugees.','He uses a food analogy while framing policy through his beliefs.','He gives nutritional advice unrelated to any policy issue.','He argues that every policy should be decided by laboratory food tests.'],1,
 '食物例子说明 Huckabee 怎样表达政策观点？',['他引用科学估计，说明难民实际带来的危险。','他从自身信念出发讨论政策，并使用食物类比。','他给出与政策无关的营养建议。','他主张每项政策都应由食品实验决定。'],
 ['A 花生数量属于他所说的假设类比，不是关于难民风险的科学样本、事实或比例。','B 宗教信念的 perspective 与 food metaphors 均由作者明确指出。','C 括号明示问题是美国是否接受叙利亚难民，非营养咨询。','D 文中没有这种决策规则。引语观点归于 Huckabee，不等于作者、网站或研究证据对难民的判断；不得把食物比喻当成真实群体的风险证据。'],
 ['from the perspective of his religious beliefs','he uses food metaphors frequently'],
 'clemencies','赦免；宽恕处置','指政策层面给予宽赦的处理，与前文信仰中的 forgiveness 相接，不是接受难民的同义词','The report discussed the procedures used to consider clemencies.',['a policy regarding clemencies','grant clemency'],
 '他从宗教信念的视角思考政策议题（例如，他信奉宽恕，因此支持较宽松的赦免政策），而且经常使用食物比喻（例如，谈到美国是否应接受叙利亚难民，他说：“如果你买了一袋五磅的花生，知道袋中约十颗有致命毒性，你会拿给孩子吃吗？答案是不会。”）。注：这是书中归于 Huckabee 的假设类比，不是关于难民实际风险的研究数据或网站立场。')

add(24,'推断','What does “probably” signal about the explanation of Huckabee’s sense of meaning?',
 ['The book reports his exact answer to a meaning questionnaire.','The author has proved that all religious people share the same motivation.','The author offers an interpretation rather than a directly verified inner report.','Huckabee is described as having no clear guiding principles.'],2,
 '解释 Huckabee 的意义感时，probably 表示什么？',['书中报告了他在意义感问卷上的确切回答。','作者已证明所有宗教人士的动机相同。','作者给出解释性推测，而非直接核实的内心自报。','书中说他没有明确的指导原则。'],
 ['A 当前片段没有问卷题项、作答或测量记录。','B 单个人物的推测不能推出全体相同动机。','C He probably thinks 明确限制作者对其内心想法的确定程度。','D guided by clear principles 恰说明有明确原则。'],
 ['He probably thinks his life is meaningful because'],
 'dedicated','投入；致力于','has dedicated his life to 描述作者据以解释其意义感的长期投入，不能据此冒充本人直接测量','She has dedicated many years to community work.',['dedicate one’s life to','be dedicated to a cause'],
 '他大概认为自己的人生有意义，因为他一生投入宗教事业，对他人的生活产生了影响，而且人生由明确原则指引。一个拥有坚定信念的男人。','inference')

add(25,'细节','Which trait is ranked first, and which least, in the pattern described for meaningful lives?',
 ['Conscientiousness first; openness to experience least.','Openness to experience first; conscientiousness least.','Extraversion first; emotional stability least.','Agreeableness first; extraversion least.'],0,
 '本句给出的有意义人生特征中，哪个排第一，哪个最弱？',['尽责性第一，经验开放性最弱。','经验开放性第一，尽责性最弱。','外向性第一，情绪稳定性最弱。','宜人性第一，外向性最弱。'],
 ['A first by conscientiousness 与 least by openness 直接给出两端。','B 把顺序颠倒。','C 情绪稳定性紧随尽责性，不是最弱。','D 宜人性不是第一，外向性也不是最弱；least 表示所述模式中的相对次序，不等于开放者绝不可能有人生意义。'],
 ['first by conscientiousness, followed by emotional stability, extraversion, agreeableness, and, as with happy people, least by openness to experience.'],
 'characterized','以……为特征','概括研究所述的人格模式，不是给每个人设定必须同时满足的入场标准','The neighbourhood is characterized by narrow streets and small shops.',['be characterized by','characterized first by'],
 '通往有意义人生的道路很多，但人格研究显示，过着有意义人生的人，首先以尽责性为特征，其后依次是情绪稳定性、外向性、宜人性；与幸福者一样，最不以经验开放性为特征。')

assert len(out)==25 and [q['id'] for q in out]==[t['questionId'] for t in targets]

def persist():
 path=ROOT/'source/short-questions/additional.json';existing=load('source/short-questions/additional.json');byid={q['id']:q for q in existing}
 for q in out:
  if q['id'] in byid:assert byid[q['id']]==q,('Refuse to overwrite changed authoring',q['id'])
  else:existing.append(q)
 path.write_text(json.dumps(existing,ensure_ascii=False,indent=2)+'\n',encoding='utf8',newline='\n')
 review=dict(batchId='batch-016',date='2026-10-22',pdfSha256=b['pdfSha256'],checkedPdfPages=list(range(61,66)),questionIds=[q['id'] for q in out],paragraphs=[dict(id=pid,textSha256=hashlib.sha256(pp[pid]['text'].encode()).hexdigest()) for pid in dict.fromkeys(q['paragraphId'] for q in out)],note='完整 PDF 61–65 页视觉核对，含上一批已审阅叙事段落、跨页元分析说明和花生引语。保留英文、原数字、potential/probably 与 more likely 等限定；区分节目引例、相关、作者推测和人物引语；花生是假设政治类比，不作难民实际风险证据。候选句界不是人工最终分句。')
 (ROOT/'source/short-questions/review-chapter06-happiness25.json').write_text(json.dumps(review,ensure_ascii=False,indent=2)+'\n',encoding='utf8',newline='\n')
 print('Saved',len(out),'of 25 individually authored exercises')

if __name__=='__main__':persist()
