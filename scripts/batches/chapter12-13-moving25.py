"""25 individually authored exercises for frozen targets, PDF pages 142-147.
Preserve printed English, source positions and all previously published questions.
"""
from pathlib import Path
import json,hashlib
ROOT=Path(__file__).resolve().parents[2]
load=lambda p:json.loads((ROOT/p).read_text(encoding='utf8'))
b=load('public/data/book.json');plan=load('public/data/reading-plan.json');targets=load('source/short-questions/batch036-targets.json')['targets']
ss={s['id']:s for s in b['sentences']};pp={p['id']:p for p in b['paragraphs']};out=[]
def add(i,kind,prompt,options,answer,prompt_zh,options_zh,analyses,quotes,word,meaning,context,example,collocations,translation,support='explicit'):
 t=targets[i-1];u=next(u for u in plan['units'] if u['id']==t['readingUnitId']);group=[ss[sid] for sid in u['sentenceIds']];p=pp[u['paragraphId']];text=p['text'][group[0]['start']:group[-1]['end']]
 assert hashlib.sha256(text.encode()).hexdigest()==t['passageSha256'];evidence=[]
 for quote in quotes:
  offset=text.find(quote);assert offset>=0,(i,quote);start=group[0]['start']+offset;end=start+len(quote);touching=[s for s in group if s['start']<end and s['end']>start]
  evidence.append(dict(quote=quote,sentenceIds=[s['id'] for s in touching],sources=list({(r['pdfPage'],r['block']):r for s in touching for r in s['sources']}.values())))
 assert word.lower() in text.lower(),(i,word)
 out.append(dict(id=t['questionId'],version=1,readingUnitId=u['id'],chapterId=u['chapterId'],sectionId=u['sectionId'],paragraphId=u['paragraphId'],sentenceIds=u['sentenceIds'],passage=text,prompt=prompt,options=options,answer=answer,type=kind,promptZh=prompt_zh,optionsZh=options_zh,analyses=analyses,evidence=evidence,vocabulary=[dict(word=word,meaning=meaning,context=context,example=example,collocations=collocations)],translation=translation,support=support,editorialStatus='完整PDF142–147原页视觉核对含12章末143与13章首144。文学例证非实验；MIDUS1995/2005为既有数据关联分析，不补随机搬迁。内向者could/tend限定不扩为人人必然；当时尚未明确心理丰富概念，所以未测其效果。读者邮件与自报不作总体诊断/因果，Mary的real trauma为自我比较不认可贬低痛苦；作者not a clinical psychologist和hope/might原样保留。父母决定搬迁、树根为比喻、个案可兼具代价与收益。Tom跨页Once we / actually lived两单元保留来源ID与字符，标注非独立最终句界，不补句不重复。D.J.45次为一生、11校为12年；最后引文未闭合续后段。发现13章首144页block5实为作者导语却被旧规则列为epigraph-or-subtitle，另存正文补入审计待办，现有1053单元不得当全书完整分段。'))







add(1,'作者意图','Why is Gopnik’s story mentioned in this summary?',
 ['To show that only invented crises make narratives interesting.','To illustrate a crisis giving an account a journey-like structure.','To prove that every crisis produces the same intellectual outcome.','To replace reflection with a list of places visited.'],1,
 '此总结为什么提到Gopnik的故事？',['说明只有编造危机才让故事有趣。','说明危机能让叙述形成旅程式结构。','证明每次危机都产生相同智识结果。','用地点清单代替反思。'],
 ['A same series of events强调重新组织已有事件，非编造危机。','B sudden crisis...prompts...journey是前文强调挣扎与转折的具体例证。','C 一则故事不构成每次危机的统一结果，unexpected还强调意外性。','D 本段谈危机、应对与结构，非地点罗列。Alison的文章是举例，非此处开展实验。'],
 ['Alison Gopnik’s Atlantic story in Chapter 4 is fascinating because it starts with a sudden crisis that prompts a long, unexpected intellectual journey.'],
 'related','讲述；叙述','此处被动式be related表示事件怎样被讲出，不是彼此相关','The same incident can be related from different viewpoints.',['relate a series of events','an intellectual journey'],
 '总之，同一系列事件可以用不同方式讲述，通过故事编辑变得更有意思。强调挣扎与挑战，可以让叙事获得结构并发生转变。聚焦危机及你如何克服它们，会让同一故事更像英雄旅程。第4章里Alison Gopnik的《Atlantic》文章之所以精彩，是因为它以一场突然的危机开头，开启了一段漫长、意外的智识旅程。')

add(2,'主旨','What does the author ultimately prioritize over storytelling technique alone?',
 ['Readers knowing every family mystery before the character does.','Having a nickname that makes a character memorable.','Removing uncertainty from the beginning of every story.','Having experiences, reflecting on them, and retaining them psychologically.'],3,
 '作者最终把什么看得比单纯讲述技巧更重要？',['读者先于角色知道所有家族谜团。','有一个让人物好记的绰号。','删除每个故事开头的不确定。','真正经历、加以反思，并在心理上保存。'],
 ['A alongside him是与人物一起渐知，非提前全知道。','B Milkman只是人物绰号，不是结论。','C totally clueless说明起初不知反能形成吸引力。','D bottom line后列出实际经历、反思、保存三项；not...per se是并非只靠怎样讲。文学例子不变成实证研究。'],
 ['what kinds of experiences you actually have, whether you reflect on them, and whether you can keep them in your psychological memorabilia box.'],
 'per se','本身；单就其本身而言','限制所否定的是单纯叙述方式，而非否定反思或好叙事的作用','A long journey is not valuable per se; attention also matters.',['not valuable per se','a memorabilia box'],
 'Toni Morrison的《Song of Solomon》精彩之处，在于主人公Macon Dead III，绰号“Milkman”，起初全然懵懂；读者与他一起，慢慢弄清家族谜团及“Song of Solomon”的真正含义。关键并不只是你怎样讲故事本身，而是你实际有怎样的经历、是否反思，以及是否能把它们保存在心理纪念物盒子里。')

add(3,'主旨','What question is the author now raising about psychological richness?',
 ['Whether it can become excessive despite the earlier preference for moving.','Whether material wealth and psychological richness are exactly identical.','Whether the cited song scientifically demonstrates the benefits of moving.','Whether staying has already been proved better in all circumstances.'],0,
 '作者现在对心理丰富提出什么问题？',['尽管先前偏向迁移，它是否也会过量。','物质财富与心理丰富是否完全相同。','引用歌曲是否科学证明搬家的好处。','留在原地是否已证明在所有情况下更好。'],
 ['A But can...too psychologically rich引出对前面迁移更丰富的假设进行再问。','B 第一项物质财富是类比起点，不是两者相同的定义。','C 歌曲是书的开场线索，不是科学证据。','D assumed说明此前假设，不是已证实一切情况下留守更优。'],
 ['But can your life be too psychologically rich?','Here I assumed that moving is a more psychologically enriching experience than staying.'],
 'assumed','假定；设想','作者回顾先前使用的出发假设，区别于已经证实的普遍结论','The model assumed that everyone had the same resources.',['assume that','material wealth'],
 '谈到物质财富，大多数人同意钱再多也不嫌多。但人生在心理上能否太丰富？我以The Clash的《Should I Stay or Should I Go?》开篇，当时假定搬迁比留在原地更能丰富心理经历。')

add(4,'作者意图','What possibility does this question introduce?',
 ['A recommendation that all children should move at least ten times.','A report that the person moved exactly ten times after childhood.','A case of unusually frequent childhood relocation.','A comparison of adult incomes in ten different cities.'],2,
 '这个问题引入什么可能情形？',['建议所有孩子至少搬十次。','报告此人成年后恰好搬十次。','童年异常频繁搬迁的情形。','十城成人收入比较。'],
 ['A what if是设问，不是行动建议。','B more than ten不是exactly ten；childhood非成年。','C over the course of childhood限定阶段，more than ten凸显频繁。','D 没有收入或十座城市信息。单句仍是假设情形，非某样本测得结果。'],
 ['But what if someone moves more than ten times over the course of their childhood?'],
 'over the course of','在……期间；在……历程中','限定十余次搬迁累积于童年阶段','The family moved twice over the course of a year.',['over the course of childhood','more than ten times'],
 '但如果一个人在整个童年期间搬家超过十次，又会怎样呢？')

add(5,'细节','What relationship did the authors examine using MIDUS data?',
 ['Whether changing adult jobs causes childhood moves.','Whether moving was randomly assigned in 1995.','Whether psychological richness was measured after each school change.','Whether frequent childhood moves were associated with adult unhappiness.'],3,
 '作者用MIDUS数据考察什么关系？',['成年换工作是否导致童年搬家。','1995年是否随机分配搬迁。','每次换校后是否测心理丰富。','童年频繁搬迁是否与成年不幸福有关。'],
 ['A 颠倒人生阶段，也加入未提的工作变量。','B analyzed data不是随机安排家庭搬家；两次收集年份不能充当随机实验。','C 本段说well-being indicators，未说每次转校都测心理丰富。','D 最后一句would be associated with明确研究问题，范围是过多童年迁移与成年不幸福。'],
 ['We wondered if excessive childhood moves would be associated with unhappiness in adulthood.'],
 'indicators','指标','研究中的多种幸福相关衡量信息，不等于一项完整诊断','The survey included several indicators of well-being.',['indicators of well-being','associated with'],
 'Uli Schimmack和我分析了“美国中年研究”（MIDUS）在1995年及2005年收集的数据。这项由知名幸福感研究者Carol Ryff组织的研究，含有多种幸福指标，以及参与者童年搬迁次数的信息。我们想知道，过多童年搬迁是否与成年不幸福有关。')

add(6,'同义改写','Which statement preserves the population and qualification of the takeaway?',
 ['All adults who move once inevitably lose every close relationship.','Excessive childhood moves may have lasting well-being costs for introverts who struggle to form connections.','Introverts always find new social ties easier than extraverts.','Adult unhappiness was proved to be the cause of childhood moves.'],1,
 '哪项保留了论文要点的人群与限定？',['所有搬过一次家的成人必失去每段亲密关系。','过多童年搬迁可能给难建社交的内向者带来持久幸福代价。','内向者总比外向者更易建立新联系。','已证明成年不幸福导致童年搬家。'],
 ['A excessive不是一次，among introverts不是所有人，could不是必然。','B 保留could的可能性、内向者范围、建立联系困难的解释。','C harder time而非更易；本句也未直接比较两类型全体。','D 既颠倒时间，又把解释强化为已证因果。虽原书用effect措辞，不能补称随机因果实验。'],
 ['excessive childhood moves could have a lingering negative effect on subjective well-being in adulthood among introverts','they tend to have a harder time making social connections in new places'],
 'lingering','持续不散的；长久残留的','指童年经历的影响可能延续到成年，并非只影响搬迁当天','The dispute had a lingering effect on their friendship.',['a lingering negative effect','subjective well-being'],
 '论文的主要启示是：过多童年搬迁可能对内向者成年后的主观幸福感产生持久负面影响，因为他们往往更难在新地方建立社交联系，最终在成年时只有很少的亲密关系。')

add(7,'细节','Which chronology matches the account?',
 ['The newspaper report preceded the paper by a year.','Reader emails arrived before any report was published.','The paper appeared in June 2010 and the Times report followed on July 9.','Psychological richness had already been fully articulated before both publications.'],2,
 '哪项时间顺序符合叙述？',['报纸比论文早一年。','任何报道发布前就收到读者来信。','论文2010年6月发表，《Times》7月9日报道。','两次发表前已完整提出心理丰富概念。'],
 ['A June到July是论文先、报道后。','B In response承接报道，非在报道前。','C 两个日期直接对应；不从后文Mary说的7月11版本擅改作者所述7月9日期。','D had not articulated明确尚未提出该概念。'],
 ['Our paper was published in June 2010. On July 9, 2010, The New York Times reported on our paper.'],
 'articulated','明确表达；清楚提出','指当时尚未清晰提出心理丰富这个概念','The team had not yet articulated its central idea.',['articulate a concept','in response'],
 '我们的论文发表于2010年6月。《New York Times》于2010年7月9日报道了它。作为回应，我收到许多《Times》读者及其他人的电子邮件。在那个时候，我们还没有明确提出心理丰富这个概念。')

add(8,'逻辑关系','How does the author qualify the evidence at this point?',
 ['Psychological richness was not tested, while readers’ accounts informed the discussion of happiness.','Reader emails established a measured richness increase for every participant.','The study had tested richness but omitted happiness entirely.','Personal accounts removed the need for any distinction between happiness and richness.'],0,
 '作者此时怎样限定证据？',['没检验心理丰富，但读者经历帮助理解幸福。','邮件确立每位参与者丰富度测得提高。','研究测了丰富，完全没涉及幸福。','个人叙述使幸福与丰富不必区分。'],
 ['A unable to test...richness与informative...happiness形成明确区分。','B 邮件是个人经历，不是每位样本统一测量，更非人人丰富度提高。','C 两者颠倒。','D 作者恰恰划清这两个讨论对象，不能因来信就合并概念。'],
 ['we were unable to test whether excessive childhood moves might affect psychological richness.','personal experiences shared by readers were highly informative in regard to happiness.'],
 'in regard to','关于；就……而言','限定来信帮助理解的是幸福，而非已检验心理丰富','The letters were informative in regard to family life.',['in regard to happiness','personal experiences'],
 '所以，我们无法检验过多童年搬迁是否可能影响心理丰富。不过，就幸福而言，读者分享的个人经历很有启发。许多童年常搬家的人报告，成年后仍持续面对困难。例如，下面是一封Mary的邮件。')

add(9,'细节','What childhood pattern does Mary repeatedly return to in therapy?',
 ['Changing schools once after finishing twelfth grade.','Moving twelve times only during adulthood.','Remaining at one school for twelve years.','Moving and changing schools twelve times across grades one to twelve.'],3,
 'Mary在治疗中反复回到哪种童年经历？',['十二年级毕业后换校一次。','成年后才搬十二次。','同一学校读十二年。','一至十二年级间搬家换校十二次。'],
 ['A 不是毕业后一次，1st to12th限定整个中小学阶段。','B 把童年时期改成成年。','C 与moved and changed schools相反。','D 12 times in12 years及年级范围直接支持。她感到内疚和影响深是个人自述，不能据邮件推出所有人的临床结果。'],
 ['I moved and changed schools 12 times in 12 years—from 1st grade to 12th grade.'],
 'bringing it up','提起这件事','指Mary因谈论频繁搬迁及其影响而偶感内疚，不是搬起物体','She felt uneasy about bringing it up again.',['feel guilty bringing it up','in and out of therapy'],
 '我很感兴趣地读了7月11日星期日版《New York Times》的文章。它令我着迷，因为多年来我断断续续接受治疗，却似乎总回到同一点：从一年级到十二年级，我在十二年里搬家换校十二次。如此一件事会这样影响我的人生，一直让我觉得出乎意料；有时连提起它，我都会内疚。')

add(10,'推断','What does Mary’s closing comment suggest?',
 ['She is announcing that the problem has completely disappeared.','She asks the author to move her family again.','She minimizes the experience yet still struggles with it and appreciates acknowledgment.','She is formally diagnosing every other frequent mover.'],2,
 'Mary结尾的话透露什么？',['她宣布问题已完全消失。','她请求作者让家人再搬。','她觉得经历不算严重，却仍放不下，并感谢认可。','她正式诊断所有频繁搬迁者。'],
 ['A cannot let it go与已解决相反。','B 无再次搬家的请求。','C hardly compares...yet...cannot说明自我轻视与持续困扰的张力；thanks for validation表达感谢被理解。','D 这是个人来信而非诊断。real trauma是Mary自我比较的措辞，不代表题库认定其痛苦不真实。'],
 ['It hardly compares to real trauma and yet I cannot let it go. Many thanks for a bit of validation and understanding.'],
 'validation','认可；对感受的承认','让来信者感到经历和困扰被认真对待，非数据格式校验','She appreciated the validation of her difficult experience.',['validation and understanding','let it go'],
 '它几乎无法与真正的创伤相比，可我就是放不下。非常感谢这份认可与理解。Mary。（“真正的创伤”是来信者自己的比较用语。）',support='limited-inference')

add(11,'细节','What continuing difficulty does the account attribute to Liz?',
 ['An inability to settle down and find contentment.','A refusal to attend any school during childhood.','A confirmed diagnosis reported by the psychiatrists.','A childhood spent in one country and one school.'],0,
 '叙述说Liz持续面临什么困难？',['无法安定下来并找到满足。','童年拒绝上任何学校。','精神科医生报告已确诊。','童年一直同一国同一校。'],
 ['A settle down、put down roots、contentment三项直接描述不安定。','B went to eleven schools说明上了多校，非从未上学。','C 原文说医生未发现问题，不可补造诊断；这里只复述书中的来信转述。','D multiple countries与eleven schools都否定。'],
 ['She could not settle down, put down roots, and find any sort of contentment.'],
 'put down roots','扎根；建立稳定生活联系','由植物扎根比喻建立持续关系与归属','After years of moving, they hoped to put down roots.',['put down roots','find contentment'],
 '许多人表达了相似的挣扎。像Mary一样，Liz在多个国家读过十一所学校，自称“就是那样的孩子之一……不断地搬、搬、搬”。她也进出过精神科病房，但精神科医生没有找到什么问题。她无法安定、扎根，或找到任何满足感。')

add(12,'主旨','Which pattern is illustrated by Gus’s brief account?',
 ['Repeated school changes were followed by many enduring close friendships.','Frequent new-school experiences accompanied a lack of close relationships.','One late school transfer resolved his earlier loneliness.','He studied at one school from kindergarten through eighth grade.'],1,
 'Gus的简短经历说明什么模式？',['反复转校后有很多长久密友。','常在新学校就读，同时缺乏亲近关系。','一次晚期转校解决孤独。','幼儿园到八年级一直同校。'],
 ['A never close to anyone与很多密友相反。','B 每年不同校、从未与谁亲近、feel so lost共同体现此个人经历的模式。','C 段中没说孤独被解决。','D a different school every year否定同一学校。个人来信不是代表所有搬迁者的统计样本。'],
 ['From kindergarten to eighth grade, he was a new kid at a different school every year. He was never close to anyone.'],
 'lost','迷茫的；无所归属的','I feel so lost指情感困惑，不是地图上迷路','After another school change, he felt lost and alone.',['feel lost','be close to someone'],
 '20岁的Gus面对类似问题。从幼儿园到八年级，他每年都在不同学校当新生。他从没与任何人亲近。邮件结尾他写道：“我觉得如此迷茫。”')

add(13,'细节','Which distinction between Peggy and Jim is accurate?',
 ['Both reported exactly thirteen childhood moves.','Peggy stated a proven cause, while Jim reported no social difficulties.','Peggy wondered about instability; Jim reported few friends and trouble forming attachments.','Jim was the sixty-three-year-old mother of three children.'],2,
 '哪项正确区分Peggy与Jim？',['两人都报告童年恰好搬十三次。','Peggy给出已证原因，Jim没有社交困难。','Peggy猜想不稳定的影响；Jim报告朋友少、难以依恋。','Jim是63岁三个孩子的母亲。'],
 ['A thirteen childhood moves属于Peggy，Jim报告的是8所小学和3所高中，指标不能互换。','B wondered是疑问而非已证实，Jim也明确有关系困难。','C 保留Peggy推测语气和Jim自述范围。','D 把Peggy身份移给61岁Jim。drugs/fights/jail为后者叙述，不能说已证明由搬家单独造成。'],
 ['she wondered if her inability to fit in was caused by this lack of stability.','he has very few friends and has a “problem with getting attached to people”'],
 'getting attached to','形成依恋；产生亲近感','Jim自述难以与人建立情感联系，不是物体黏接','She worried about getting attached to people she might soon leave.',['get attached to people','fit in'],
 'Peggy是63岁、三个孩子的母亲，童年搬过十三次家。她想知道，自己难以融入是否由这种缺乏稳定造成。最后，61岁的Jim读过八所小学和三所高中。他告诉我，自己朋友很少，“与人形成依恋有困难”，还有毒品、打架、坐牢的问题。')

add(14,'语境词义','What does Jim mean by wishing to “get past being angry”?',
 ['He wants to erase all evidence of where he lived.','He says other people have already solved the same problem.','He plans to recreate the missed childhood experiences exactly.','He wants to move beyond resentment about moving and missing childhood experiences.'],3,
 'Jim说希望get past being angry，是什么意思？',['想抹掉所有居住证据。','说别人都已解决同一问题。','计划精确重造错过的童年。','希望走出对搬迁和错失童年的怨愤。'],
 ['A get past指情绪上走过，不是销毁资料。','B others...like me仅表示相信有人相似，没说已经解决。','C wish并未说精确再造过去。','D angry about...moving and missing指出愤怒的对象，get past表示希望摆脱持续困扰。'],
 ['I wish I could get past being angry about all the moving and missing all the things you are supposed to do as a kid growing up.'],
 'get past','走过；克服；不再受困于','在本句指摆脱持续愤怒，而非物理经过一个地点','It took time to get past her resentment.',['get past being angry','miss childhood experiences'],
 'Jim说：“我希望自己能不再因不停搬迁、错过成长中孩子本该做的那些事而愤怒。我知道，还有别的人和我一样。”')

add(15,'作者意图','What does the repeatedly transplanted tree image emphasize?',
 ['Repeated disruption of relationships without the children choosing the moves.','The children’s independent choice to avoid all familiar places.','A formal clinical diagnosis established for every reader.','The claim that everyone who moves has the same inevitable outcome.'],0,
 '反复移植的树这个意象强调什么？',['孩子未选择搬迁，却反复遭遇关系中断。','孩子自主选择避开所有熟悉地方。','为每名读者建立正式临床诊断。','每个搬迁者都有相同必然结果。'],
 ['A parents initiated、did not get to decide与forming relationships相联，树比喻反复失根。','B 决定权在父母，非孩子。','C 这是作者根据来信的说明，不能冒充本网站重新做诊断。','D in part、seems、most保留有限范围和解释性语气，不是人人必然。'],
 ['They did not get to decide whether to stay or go, yet they had to suffer the consequences of the moves.','They are like trees transplanted too many times.'],
 'transplanted','被移植的','树的迁移比喻孩子被动离开既有关系网络','The young tree was transplanted to a new garden.',['trees transplanted','form relationships'],
 '他们的困难，部分是因为搬迁由父母发起。他们无权决定留下或离开，却必须承受后果。正如Mary和Liz提到的，他们没有什么特定、可诊断的心理病理问题；相反，难以与人建立关系，似乎是这些读者大多数问题的核心。他们像被移植太多次的树。（这里保留作者对来信的表述，不是网站作出的诊断。）')

add(16,'逻辑关系','What contrast does “Yet” introduce?',
 ['Moving is easy, and the readers correctly blame themselves.','Repeated uprooting is difficult, but the readers still blame themselves.','New soil always solves relationship difficulties immediately.','The readers blame their parents and feel no personal guilt.'],1,
 'Yet引入什么反差？',['搬迁很容易，所以他们正确责怪自己。','反复失根很难，他们却仍自责。','新土壤总会立刻解决关系难题。','他们只怪父母，毫无自责。'],
 ['A hard与easy相反，且原文没认可自责正当。','B 前句强调一次已难、反复更难，Yet后却是他们怪自己。','C let alone加强困难，非立即解决。','D blame themselves明确自责。树根继续是比喻，不是植物生理实验。'],
 ['It is hard to be uprooted from a familiar soil and then grow roots in a new soil once, let alone being uprooted again and again. Yet, they blame themselves for their struggle.'],
 'uprooted','被连根拔起；被迫离开熟悉环境','借树离土比喻人与熟悉生活及关系分离','The move left the family feeling uprooted.',['be uprooted from','again and again'],
 '从熟悉的土壤里被拔出，再到新土里扎根，一次都已很难，更不用说一次次被拔起。然而，他们却为自己的挣扎责怪自己。')

add(17,'细节','Which sequence of suggestions does the author give, with his stated caveat?',
 ['Diagnose a disorder first, then move to another country.','Assume the children chose the moves, then avoid anyone with similar experiences.','Treat the advice as guaranteed therapy, then suppress childhood memories.','Recognize that it was not their fault, then seek someone who understands.'],3,
 '保留作者自我限定时，他给出什么建议顺序？',['先诊断，再移居他国。','先认定孩子自选搬迁，再避开相似经历者。','当作保证有效治疗，再压下童年记忆。','先承认不是自己的错，再找理解处境的人。'],
 ['A 原文未建议诊断或再搬迁。','B 与not their fault和someone...similar困难均相反。','C 作者先说不是临床心理学家、建议可能不准，不能强化成治疗保证。','D first/second明确顺序；siblings等只是可能理解者的例子，不是唯一资格。此题阅读作者观点，不把其建议升级为本站临床方案。'],
 ['I am not a clinical psychologist, so my suggestions might be off target.','A first step is to embrace the fact that this is fundamentally not their fault.','A second step is to find someone who can understand their predicament'],
 'predicament','困境；难处','指童年不稳定及后续挣扎带来的处境','A friend who had moved often understood her predicament.',['understand a predicament','off target'],
 '我不是临床心理学家，所以建议可能不得要领。不过，还是给受童年不稳定困扰的人几条建议。第一步是接受这样一个事实：从根本上说，这不是他们的错。第二步是找能理解处境的人，也许是早年有过类似困难的人，比如同样多次搬家的兄弟姐妹，或军人、外交官家庭长大的成年子女。')

add(18,'推断','How strong is the claim about finding positive aspects?',
 ['It is a guaranteed result for everyone who speaks to a sibling.','It denies that childhood difficulties ever mattered.','It is a hope that understanding and validation may enable a different focus.','It is a measured finding that all participants’ symptoms disappeared.'],2,
 '关于看到积极方面的说法有多强？',['保证每个与手足交谈者都做到。','否定童年困难曾有影响。','希望理解和认可可能帮助转换关注点。','测得所有参与者症状消失。'],
 ['A hope、might不支持保证；也没限定只能手足。','B validate childhood difficulties恰恰先承认困难。','C once条件、hope愿望、might可能性共同限定推断，不把积极视角当作否认受苦。','D 没有干预测量或症状归零数据。'],
 ['My hope is that once they find someone who can understand and validate their childhood difficulties and subsequent struggles, they might be able to focus on some positive aspects'],
 'subsequent','后来的；随后的','童年困难之后持续出现的挣扎，不是另一项明确确诊','The move shaped several subsequent decisions.',['subsequent struggles','validate difficulties'],
 '我希望，一旦他们找到能理解并认可其童年困难及后来挣扎的人，就也许能关注曾生活在多样环境中的一些积极方面。',support='limited-inference')

add(19,'逻辑关系','What is being introduced as supporting material here?',
 ['A randomized comparison of all military children.','A particular email from Tom among the author’s correspondence.','A statistical estimate of how often every family moves.','A clinical finding that contradicts all the earlier emails.'],1,
 '这里引入什么作为支持材料？',['全部军人子女的随机比较。','作者收到的来信中Tom的一封。','每个家庭搬迁频率的统计估计。','推翻此前所有来信的临床发现。'],
 ['A emails不是随机实验，单句还未提Tom家庭背景。','B some emails及Here is an email限定为收到的个人来信。','C 单封邮件不等于总体频率估计。','D show just that承接说明，不是推翻所有苦难案例。简短引入句不补写未出现的邮件结果。'],
 ['Indeed, some emails I received show just that. Here is an email from Tom.'],
 'Indeed','确实；的确','在此连接作者前述想法与随后举出的来信，不使个案变为普遍规律','Indeed, one letter offered a useful example.',['Indeed, some emails','receive an email'],
 '确实，我收到的一些邮件正体现了这一点。下面是一封Tom的邮件。')

add(20,'细节','What background does the letter writer give for his interest in frequent childhood moves?',
 ['He grew up in a Navy family and moved every two to three years.','He organized the MIDUS data collection in 1995 and 2005.','He moved just once after reading the UVA Today article.','He had already proved that every military child benefits from moving.'],0,
 '写信者以什么背景解释对童年频繁搬迁的兴趣？',['海军家庭长大，每两三年搬一次。','组织1995和2005的MIDUS收集。','读报道后才搬过一次。','已经证明所有军人孩子都受益。'],
 ['A grew up...Navy family与every2–3years是个人经历的明确说明。','B 把MIDUS研究者角色移给来信者。','C childhood years不等于读报道后才搬一次。','D 一封自述没有普遍效益证明。原单元末尾Once we跨PDF页接到下一单元；保留原字，不把该残句冒称完整英文句。'],
 ['I grew up in a Navy family and moved, during my childhood years, every 2–3 years.'],
 'Navy','海军','指来信者成长家庭的军种背景，不自动说明全部搬迁原因','He grew up in a Navy family that moved frequently.',['a Navy family','every two to three years'],
 '今早我很感兴趣地读了《UVA Today》关于你近期研究经常搬家的孩子那篇论文的报道。我关注这个话题已很久，因为我在海军家庭长大，童年每两三年就搬一次。有一次，我们……（原页在此跨页，后续文字在下一单元。）')

add(21,'细节','What contrast is stated in this continuation of the letter?',
 ['Four moves occurred without any school change.','Three years in one school involved four house changes.','Four years in one house still included three school changes.','The writer changed neither home nor school during the period.'],2,
 '这段来信续文陈述什么反差？',['搬四次但没换校。','一校三年内换四次住处。','同一住处四年，仍换三次学校。','期间住处学校都没变。'],
 ['A lived in the same house不是搬四次。','B 把4years与3times及house/schools交叉错配。','C 同屋四年与期间三次换校由but相连，准确保留两种稳定性之别。','D 明确changed schools3times。单元从actually开始，承接上一页Once we；不是独立定稿句界。'],
 ['actually lived in the same house for 4 years, but I changed schools 3 times during that period'],
 'during that period','在那段期间','指同一住处居住的四年，不是全部童年','She changed classes twice during that period.',['during that period','change schools'],
 '……其实在同一所房子里住过四年，但那段期间我换了三次学校……（承接上一单元的“有一次，我们”。）')

add(22,'细节','How did the writer try to gain rapid peer respect?',
 ['By refusing to participate in classroom competition.','By remaining unnoticed until the school year ended.','By changing schools whenever he met a rival.','By excelling academically from the start of each school year.'],3,
 '写信者怎样争取迅速获得同伴尊重？',['拒绝参与课堂竞争。','一直不引人注意到学年末。','遇到竞争者就换校。','从每学年一开始就力争学业出色。'],
 ['A serious competition和top echelon肯定竞争，非回避。','B Start day one与等到年末相反。','C 没说遇对手主动转校，不能编选择动机。','D excel...head of the class加day one，说明以成绩争取认可的个人策略，不推出人人都应这样。'],
 ['I found the safest and best way for me was to excel in school—go to the head of the class.','Start day one each fall letting them know there was a new guy in town who was serious competition'],
 'excel','表现出色；胜过一般水平','以学业成绩突出获得同伴尊重的自述策略','She worked hard to excel in mathematics.',['excel in school','gain peer respect'],
 '成长时，我很清楚地发现，在每所新学校、每个新社区里，迅速获得某些同伴的尊重非常重要。我发现，对我来说最安全、最好的方式，是学业出色——成为班里的尖子。每年秋天从第一天就让他们知道，新来了一个强劲对手；毋庸怀疑，各校最拔尖的学生之间总有竞争……')

add(23,'主旨','What mixed assessment does Erin offer?',
 ['She regrets lacking close friends but values the varied, immersive experiences.','She rejects both friendship and any experience of other places.','She claims the letter proves that childhood moving has no costs.','She says she visited places only briefly and met no local people.'],0,
 'Erin给出什么兼具两面的评价？',['遗憾缺少密友，但珍惜多样而深入的经历。','拒绝友谊也拒绝各地经历。','说来信证明童年搬家没有代价。','说只短访且没遇当地人。'],
 ['A regret与but...thanked保留遗憾和感激两面，immersing区别走马观花。','B wide variety和close friends是看重而非双双拒绝。','C 个人评价不证明无代价，缺少密友本身就是遗憾。','D not just visiting与immersing明确反对只短访解读。开头Tom自己也称anecdotal，不能提升为总体因果证据。'],
 ['I moved a lot and I do regret not having close friends','a wide variety of experiences with people from different places','not just visiting but immersing myself in it.'],
 'anecdotal','基于个别经历的；轶事性的','Tom对自己提供的信息性质的自我限定，非系统总体证据','The letter provided anecdotal information rather than population statistics.',['anecdotal information','immerse oneself in'],
 '我不确定像我这样的个案信息对你多有价值，但随时愿意交流想法。类似地，Erin写道：“我搬过很多次，也确实遗憾没有亲密朋友。”但她也感谢父母，让她有机会“与来自不同地方的人有各式各样的经历”，并且“看见我们的国家，不只是游览，而是深入其中”。')

add(24,'细节','How does D.J. evaluate the two lifestyles in this passage?',
 ['Staying has advantages, but moving has no benefits at all.','Both moving and staying have drawbacks as well as benefits.','His friend moved more often than he did.','Both friends agree that staying in Colorado was a mistake.'],1,
 '本段中D.J.如何评价两种生活方式？',['留守有优点，迁移毫无好处。','迁移与留守都有缺点也有好处。','朋友比他搬得更频繁。','两人都同意留在科罗拉多是错误。'],
 ['A both sides...perks说明迁移也有优点。','B 最后一句同时承认双方drawbacks和perks。','C 朋友大部分时间留同一区域，仅参军离开数年；D.J.一生搬超45次。','D 他们各觉得对方选择奇怪，非共同判定留守错误。45次为一生，11校为12年，不能把次数范围混在一起。'],
 ['D.J. sees that both sides have their drawbacks and their perks.'],
 'perks','好处；额外益处','与drawbacks构成两种生活方式各有利弊的对照','The job had its drawbacks and its perks.',['drawbacks and perks','both sides'],
 '最后，D.J.一生搬家超过45次，12年里读了11所学校。他把自己的人生与科罗拉多三年级时一位朋友相比；那位朋友仍住同一区域，只曾去空军服役几年后回来。朋友觉得他搬那么多次很疯狂；D.J.则觉得朋友一直待同个地方很疯狂。D.J.看得出，双方都有缺点也有好处。')

add(25,'细节','Which advantages does D.J. describe for his own experience?',
 ['Using locations to date memories and having opportunities to change others’ perceptions of him.','Never having to adapt his identity or remember new places.','Proving that staying always prevents satisfaction.','Finding particular years harder to remember than his friend does.'],0,
 'D.J.描述自己经历有哪些好处？',['用居住地定位年份，并有机会改变别人对自己的看法。','从不需调整自我或记新地方。','证明留守总会阻止满足。','比朋友更难记住具体年份。'],
 ['A track years...where living与re-created...change perceived me共同支持，是D.J.的自述。','B re-created myself many times与从不调整相反。','C 他在本段开始总结时说两种生活都能有满足，不是证明留守无益。','D hard time属朋友，can easily属D.J.，人物归属错配。最后引文跨到下一单元，保留原有边界，不补写后续句。'],
 ['D.J. can easily track years based on where he was living at the time.','I have re-created myself so many times and had the opportunity to change how people perceived me.'],
 'perceived','看待；感知','别人对来信者的印象，不等于他已客观变成另一人','Moving changed how her new classmates perceived her.',['how people perceived me','track years'],
 '他的朋友很难记得具体年份或事情发生的时间。D.J.却能根据当时住在哪儿，很容易地追踪年份。他说：“我一次次重新塑造自己，也有机会改变别人对我的看法。”最能说明问题的是，他这样总结：“我认为，两种生活方式都能找到满足。')

assert len(out)==25 and [q['id'] for q in out]==[t['questionId'] for t in targets]

def persist():
 path=ROOT/'source/short-questions/additional.json';existing=load('source/short-questions/additional.json');byid={q['id']:q for q in existing}
 for q in out:
  if q['id'] in byid:assert byid[q['id']]==q,('Refuse to overwrite changed authoring',q['id'])
  else:existing.append(q)
 path.write_text(json.dumps(existing,ensure_ascii=False,indent=2)+'\n',encoding='utf8',newline='\n')
 review=dict(batchId='batch-036',date='2026-10-23',pdfSha256=b['pdfSha256'],checkedPdfPages=list(range(142,148)),questionIds=[q['id'] for q in out],paragraphs=[dict(id=pid,textSha256=hashlib.sha256(pp[pid]['text'].encode()).hexdigest()) for pid in dict.fromkeys(q['paragraphId'] for q in out)],note='完整PDF142–147原页视觉核对含12章末143与13章首144。文学例证非实验；MIDUS1995/2005为既有数据关联分析，不补随机搬迁。内向者could/tend限定不扩为人人必然；当时尚未明确心理丰富概念，所以未测其效果。读者邮件与自报不作总体诊断/因果，Mary的real trauma为自我比较不认可贬低痛苦；作者not a clinical psychologist和hope/might原样保留。父母决定搬迁、树根为比喻、个案可兼具代价与收益。Tom跨页Once we / actually lived两单元保留来源ID与字符，标注非独立最终句界，不补句不重复。D.J.45次为一生、11校为12年；最后引文未闭合续后段。发现13章首144页block5实为作者导语却被旧规则列为epigraph-or-subtitle，另存正文补入审计待办，现有1053单元不得当全书完整分段。')
 (ROOT/'source/short-questions/review-chapter12-13-moving25.json').write_text(json.dumps(review,ensure_ascii=False,indent=2)+'\n',encoding='utf8',newline='\n')
 print('Saved',len(out),'of 25 individually authored exercises')

if __name__=='__main__':persist()
