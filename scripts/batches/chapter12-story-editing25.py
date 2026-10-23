"""25 individually authored exercises for frozen targets, PDF pages 135-139.
Preserve printed English, source positions and all previously published questions.
"""
from pathlib import Path
import json,hashlib
ROOT=Path(__file__).resolve().parents[2]
load=lambda p:json.loads((ROOT/p).read_text(encoding='utf8'))
b=load('public/data/book.json');plan=load('public/data/reading-plan.json');targets=load('source/short-questions/batch034-targets.json')['targets']
ss={s['id']:s for s in b['sentences']};pp={p['id']:p for p in b['paragraphs']};out=[]
def add(i,kind,prompt,options,answer,prompt_zh,options_zh,analyses,quotes,word,meaning,context,example,collocations,translation,support='explicit'):
 t=targets[i-1];u=next(u for u in plan['units'] if u['id']==t['readingUnitId']);group=[ss[sid] for sid in u['sentenceIds']];p=pp[u['paragraphId']];text=p['text'][group[0]['start']:group[-1]['end']]
 assert hashlib.sha256(text.encode()).hexdigest()==t['passageSha256'];evidence=[]
 for quote in quotes:
  offset=text.find(quote);assert offset>=0,(i,quote);start=group[0]['start']+offset;end=start+len(quote);touching=[s for s in group if s['start']<end and s['end']>start]
  evidence.append(dict(quote=quote,sentenceIds=[s['id'] for s in touching],sources=list({(r['pdfPage'],r['block']):r for s in touching for r in s['sources']}.values())))
 assert word.lower() in text.lower(),(i,word)
 out.append(dict(id=t['questionId'],version=1,readingUnitId=u['id'],chapterId=u['chapterId'],sectionId=u['sectionId'],paragraphId=u['paragraphId'],sentenceIds=u['sentenceIds'],passage=text,prompt=prompt,options=options,answer=answer,type=kind,promptZh=prompt_zh,optionsZh=options_zh,analyses=analyses,evidence=evidence,vocabulary=[dict(word=word,meaning=meaning,context=context,example=example,collocations=collocations)],translation=translation,support=support,editorialStatus='完整PDF135–139原页视觉核对。Wilson/Ross的自我评价与Tim Wilson/Linville干预分开；跑步时间是假设且用时增加不作提高；GPA信息组+0.34/转出5%与控制组-0.05/25%不交换，GRE表现与GPA预期分开，不补随机化或人人效果。科学家材料分挣扎/成就而后相同三节课，25年属爱因斯坦未完成尝试；must have normalized是作者机制推断，不当已直接测量。故事编辑保留坏经历不编造事件；Woolf为I bet修辞而非实验，不建议主动经历灾害。人生故事访谈从目录到场景再未来与主题，引用提示为材料不执行。保留既有切分中的单句短单元及未闭合引号跨单元，不重复句子；E = mc2保持提取原文。整段审阅若含后续未配题句另计，绝不宣称逐句直接证据全覆盖。'))







add(1,'主旨','How does derogating an earlier self help the story described here?',
 ['It verifies that earlier personality ratings were accurate.','It makes the present self appear stronger by comparison.','It removes the need to reinterpret personal experience.','It establishes that everyone improves at the same rate.'],1,
 '贬低过去的自己在这里如何帮助建构人生叙事？',['证实早期人格评分准确。','通过比较让现在的自己显得更强。','消除重新解释经历的需要。','确立每个人进步速度相同。'],
 ['A 原文解释评价方式，不验证早先评分的准确性。','B By seeing...we can see 明示：把过去看得不够自信、善社交或独立，便让现在在这些方面显得更强。','C 作者把这种贬低称为一种编辑方法，本身就在重新解释。','D 段中没有人人等速进步的结论。'],
 ['By seeing our old selves as not particularly self-confident, socially skilled, or independent, we can see our current selves as much stronger in those areas.'],
 'derogation','贬低；贬损','降低对过去自己的评价，从而衬托现在','The derogation of her earlier work made her recent progress seem greater.',['derogation of the past self','an editing method'],
 'Wilson和Ross把论文题为《从笨手到能手：人们对过去与现在自我的评价》。把过去的自己看作不太自信、不太善交际或不太独立，我们就能觉得现在的自己在这些方面强得多。借用Tim Wilson的术语，我们一直在编辑自己的故事。贬低过去的自我就是一种编辑方法。')

add(2,'逻辑关系','What makes the author’s claim of improvement compatible with his present shortcomings?',
 ['He says he is no longer shy.','He judges his writing against other people’s writing.','He treats being twenty-five as proof of maturity.','He compares his present limitations with worse remembered limitations.'],3,
 '为什么作者既承认目前的不足，又能说自己进步了？',['他说自己已经不害羞。','他拿自己的写作与别人的比较。','他把25岁当作成熟的证据。','他把现在的不足与记忆中更严重的不足比较。'],
 ['A still shy 明确现在仍害羞。','B 比较对象是过去的自己，非别人。','C twenty-five 是时间参照，不是成熟的充分证据。','D terribly shy/terrible writer 与far less shy/better writer相对；better不等于已是好作家，I think也保留回忆的不确定。'],
 ['I am still shy, but I was terribly shy when I was young (I think).','I am not a good writer, but I was a terrible writer when I was young.'],
 'far less','少得多；程度低得多','far加强less shy的比较程度，不表示完全不害羞','He is far less nervous than he was last year.',['far less shy','compared to my youth'],
 '我现在仍害羞，但年轻时害羞得厉害（我想是这样）。所以我可以说，与年轻时相比，我已经没那么害羞了。我不是个好作家，但年轻时我写得糟糕。与25岁时相比，我成了一个写得更好的作者。')

add(3,'语境词义','What does “have grown as a person” mean in this sentence?',
 ['Have developed personally over time.','Have become physically taller.','Have reached a particular birthday.','Have produced a longer written story.'],0,
 '本句have grown as a person是什么意思？',['随着时间在个人层面有所成长。','身体长得更高。','到了某个生日。','写出了更长的故事。'],
 ['A as a person限定为个人成长；can feel说明是这种成长感受。','B 把精神或人格成长错读为身高增长。','C over time没给年龄门槛。','D 此处grown的主语是I，不是故事的篇幅。'],
 ['I can feel that I have grown as a person over time.'],
 'over time','随着时间推移','说明成长感受具有时间跨度，不给出精确速度','Her confidence developed over time.',['grow as a person','change over time'],
 '这样一来，我就能觉得自己随着时间推移在个人层面有所成长。')

add(4,'细节','Why is story editing harder in the running example?',
 ['Older runners cannot remember any previous results.','The figures describe a study in which everyone improved.','Recorded times constrain how past performance can be portrayed.','Writing skill is measured with the same timing system.'],2,
 '跑步例子中，为什么故事编辑更困难？',['年长跑者记不起任何旧成绩。','数字是一项人人进步的研究结果。','已记录的时间限制了对过去表现的描述。','写作技能也用相同计时系统衡量。'],
 ['A know exactly与记不起相反。','B might look表假设示例；2:31到2:48用时增加，不能说跑得更快。','C objective performance及明确历次成绩说明客观记录使随意改写过去较难。','D 写作是前面较易贬低旧自我的领域，段中没说用马拉松计时评价写作。'],
 ['One area where story editing is difficult to implement is in objective performance.','The record might look something like 2:31 ten years ago, 2:39 five years ago, and 2:48 last month.'],
 'objective performance','客观表现','此处以可查的比赛时间为例，区别于回忆中的主观能力评价','The coach checked objective performance against the race records.',['objective performance','a marathon runner'],
 '我们能在许多领域贬低过去的自己，从成熟程度到写作能力再到道德品质。但在客观表现这个领域，故事编辑很难实施。例如，如果你是我这个年纪的马拉松跑者，就会清楚知道十年前、五年前和上个月的成绩。记录也许是十年前2小时31分、五年前2小时39分、上个月2小时48分。')

add(5,'推断','What would make a “chump to champ” account difficult in this example?',
 ['Grades that have not improved since the first semester.','Not yet having reached the second semester.','A complete absence of remembered academic results.','Improvement in subjects other than writing.'],0,
 '本例中什么情况会使“从笨手到能手”的叙事难成立？',['第一学期以来成绩没有提高。','还没有到第二学期。','完全不记得学业结果。','写作以外科目有所提高。'],
 ['A 原文直接给出If your grades haven’t improved；可有限推出没有成绩上升便难以拿成绩支持进步叙事。','B 情境设定已是大学一年级第二学期。','C remember exactly否定此项。','D 段中没按科目区分，也没说别科提高反而妨碍叙事。'],
 ['If your grades haven’t improved, it’s hard to employ a “chump to champ” narrative.'],
 'employ','采用；运用','宾语是叙事方式，不是雇用人员','She employed a different narrative to explain the setback.',['employ a narrative','academic grades'],
 '如果你正在读大学一年级第二学期，就会清楚记得第一学期学业表现如何。如果成绩没有提高，要采用“从笨手到能手”的叙事就很难。',support='limited-inference')

add(6,'细节','Who received the interview material in the experiment described here?',
 ['Only upper-class students who had always performed well.','Every first-year student at Duke University.','Half of recruited first-year students who had struggled in their first semester.','Only participants already selected for a large GPA increase.'],2,
 '本段实验中，谁观看了访谈材料？',['只有一直成绩很好的高年级学生。','杜克所有一年级学生。','招募的一年级首学期表现不佳学生中的一半。','只有已因GPA大涨而选中的参与者。'],
 ['A 混淆提供访谈故事的高年级学生与实验参与者；故事还包含早期表现不佳。','B recruited且Half限定样本和接受材料的比例。','C 招募对象为第二学期的一年级学生，首学期不佳；其中一半看改善经历访谈。','D GPA上涨是故事内容或后续考察，不是此处招募条件。没有据此补写随机分配细节。'],
 ['They recruited second-semester first-year students at Duke who did not do well in the first semester of college.','Half of them watched an interview with upper-class students'],
 'upper-class students','高年级学生','大学较高年级学生，非社会经济上层阶级','Upper-class students shared advice with new students.',['interview upper-class students','recruit first-year students'],
 '不过，即便是较客观的衡量指标，人们也会被个人成长叙事吸引。Tim Wilson与Patricia Linville做了一个引人兴趣的实验，展示这种情况如何发生。他们招募了杜克大学一年级第二学期、但第一学期表现不佳的学生。其中一半观看高年级学生访谈，听他们讲第一年成绩差、后来逐渐提高的经历。')

add(7,'细节','Which comparison correctly reports the survey information shown to the experimental group?',
 ['67% had improved GPAs, and 62% had exceeded their first-year expectations.','Both percentages refer to the experiment’s no-information group.','The sequence 2.0, 2.6, 3.2 describes every participant’s GPA.','67% had lower freshman grades than expected; 62% reported later GPA improvement.'],3,
 '哪项正确报告展示给实验组的调查信息？',['67%GPA提高，62%大一超预期。','两个百分比均指实验的无信息组。','2.0、2.6、3.2是每位参与者的GPA。','67%大一成绩低于预期；62%报告后来GPA提高。'],
 ['A 交换两个比例对应的事实，且把低于预期反为超过。','B 百分比来自高年级调查资料，控制组未收到信息。','C GPA序列只是一位受访者的经历。','D 67对应首年低于期待，62对应首学期到高年级显著提高，准确保留对象和时间。'],
 ['67% said their freshman grades were lower than they had anticipated; 62% of the students said their GPA had improved significantly'],
 'anticipated','预期；预计','入学时对成绩的期待，区别于后来的实际自报成绩','Her first results were lower than she had anticipated.',['lower than anticipated','improve significantly'],
 '一位受访者说，他的GPA从2.0升至2.6，再升至3.2。实验条件下的参与者还看到高年级学生的调查结果：“67%说大一成绩低于原先预期；62%说，自己的GPA从大一第一学期到高年级明显提高。”另一半参与者没有收到任何信息。')

add(8,'逻辑关系','Which sequence matches the assessment procedure?',
 ['A GRE task, a questionnaire, then the identical task the next day.','A questionnaire, an initial set of tasks, then another version a week later.','An anagram task only, followed by the questionnaire one year later.','Different subjects’ GPAs were compared without any reading task.'],1,
 '哪一顺序符合测量程序？',['GRE任务、问卷、次日完全相同任务。','问卷、首次任务组、一周后另一版本。','只有字谜，一年后问卷。','仅比较不同人的GPA，没有阅读任务。'],
 ['A questionnaire在前；间隔一周而非次日；another version不等于完全相同题。','B then及one week later给出顺序，两次都有阅读理解与字谜。','C 漏掉阅读理解，且时间错误。','D 段中明确每人完成GRE阅读任务，非只成绩比较。'],
 ['All the participants completed a questionnaire, then a brief version of GRE reading comprehension and anagram problems, and another version of GRE reading comprehension and anagram problems one week later.'],
 'anagram','变位词；字母重组题','把字母重新排列组成词的题型，与阅读理解一同施测','The class solved an anagram by rearranging the letters.',['anagram problems','reading comprehension'],
 '所有参与者先完成问卷，再做简短版的GRE阅读理解和字母重组题；一周后再做另一版本的GRE阅读理解和字母重组题。')

add(9,'同义改写','Which statement preserves the two comparisons in this passage?',
 ['The control group had the larger GRE gain and stronger GPA expectations.','Both groups already achieved their expected second-year GPAs.','The information group showed a larger GRE gain and expected greater GPA improvement.','Expectations improved, but no GRE performance difference was reported.'],2,
 '哪项保留本段的两个比较？',['控制组GRE增幅及GPA预期更强。','两组都已实现预期二年级GPA。','信息组GRE进步更多，并预期GPA提高更多。','仅预期改善，未报告GRE表现差异。'],
 ['A 两个比较方向都颠倒。','B expected指预期，不是本段已观察到的GPA成就。','C improved significantly more对应GRE变化，expected...greater extent对应未来GPA期望，区分实际测得与期待。','D 首句直接报告GRE从第一周到第二周的比较。不能由组均差异声称每个人都提高。'],
 ['improved significantly more from week one to week two','expected that their GPA would improve from the first to the second year to a greater extent'],
 'to a greater extent','在更大程度上','比较期望提高的幅度，非保证结果','The revised course encouraged participation to a greater extent.',['improve to a greater extent','the control condition'],
 'GPA信息条件下参与者的GRE表现，从第一周到第二周的提高幅度，显著大于没有GPA信息的控制条件参与者。实验条件下参与者还更期待自己的GPA从第一学年到第二学年有所提高；这种预期的幅度也高于控制组。')

add(10,'细节','Which pair of results belongs to the GPA information condition?',
 ['A GPA increase of .34 and a transfer rate of 5 percent.','A GPA decrease of .05 and a transfer rate of 5 percent.','A GPA increase of .34 and a transfer rate of 25 percent.','A GPA decrease of .05 and a transfer rate of 25 percent.'],0,
 '哪组结果属于GPA信息条件？',['GPA升0.34，转出率5%。','GPA降0.05，转出率5%。','GPA升0.34，转出率25%。','GPA降0.05，转出率25%。'],
 ['A 信息组+0.34、5%均与原文对应，时间分别截至大二第二学期和大二结束。','B 混入无信息组的GPA降幅。','C 混入无信息组的25%转出率。','D 两项都属于无信息条件。组别统计不等于每位学生都恰好变化相同GPA。'],
 ['those in the GPA information condition actually improved their GPA by .34','25 percent of students in the no-information condition transferred out of Duke','5 percent in the GPA information condition did.'],
 'whereas','然而；而','并列对照两条件下变化，不表示时间先后','The first group improved, whereas the second group declined slightly.',['whereas the control group','transfer out of a university'],
 '值得注意的是，从大一第一学期到大二第二学期，GPA信息条件下学生的GPA实际提高0.34，而无信息条件下学生的GPA下降0.05。最后，到大二结束，无信息条件下25%的学生转出杜克大学；GPA信息条件下这一比例为5%。')

add(11,'作者意图','What change in interpretation illustrates story editing here?',
 ['Replacing academic work with admiration for successful students.','Concluding that low grades can never be improved.','Treating admission to Duke as evidence that no struggle should occur.','Seeing a difficult first year as a common challenge rather than proof of personal inadequacy.'],3,
 '这里用什么理解变化说明故事编辑？',['以仰慕成功者取代学业努力。','认定低分永远不能提高。','把录取杜克当作不应遇到困难的证据。','把大一困难看成常见挑战，而非自己能力不够的证明。'],
 ['A 榜样提供改善的想法和希望，没有说代替做功课。','B possible to improve正相反。','C even smart kids struggle反对此种解读。','D 两种内心话的对比是关键：从“不够聪明”转为“聪明学生也会挣扎”。此处解释希望机制，不承诺每人必成功。'],
 ['Instead of saying, “I am not smart enough to be at Duke,” they learned to say, “First year is tough for everyone; even smart kids struggle.”'],
 'role model','榜样','经历相似困难而后来成功、可带来希望的人','An older student became a role model for the new class.',['have a role model','go through tough experiences'],
 'Wilson和Linville的实验表明，有一个榜样——知道有人经历过类似的艰难处境而最终成功——能带来一种想法和希望：提高表现并坚持下来是可能的。这里故事编辑的关键，在于学生如何看待自己第一学期糟糕的学业表现。他们不再说“我不够聪明，不配在杜克”，而学着说“大一对每个人都难；即使聪明的学生也会挣扎”。')

add(12,'作者意图','What purpose does the final question about Einstein’s struggles serve?',
 ['It asks readers to prove the equation before continuing.','It challenges the assumption that scientific ability makes effort unnecessary.','It reports that all students already identify closely with Einstein.','It establishes that the named scientists had identical lives.'],1,
 '末句问爱因斯坦也曾挣扎，有什么作用？',['要求读者先证明公式。','挑战有科学才能就无需努力的假设。','报告所有学生已很认同爱因斯坦。','确立三位科学家人生相同。'],
 ['A 文中是引出新视角的反问，不是解公式指令。','B everything comes naturally与struggled too对照，质疑天才毫不费力的印象。','C hard...identify说明认同困难。','D 并列举名不表示生平相同。本段最后仍是假设引导，实验结果在后文。'],
 ['we think that everything comes naturally to them','But what if you were told that Einstein struggled too?'],
 'identify with','认同；产生共鸣','觉得天才与自己有可相通之处，不是核验其身份','Students could identify with the scientist after hearing about his setbacks.',['identify with someone','come naturally to someone'],
 '同样，对我们大多数人来说，物理很难。想到伽利略、牛顿和爱因斯坦这样的天才，我们会觉得一切对他们都轻而易举，他们与我们全然不同。所以，必须学习E = mc2时，我们很难对爱因斯坦产生共鸣。但如果有人告诉你，爱因斯坦也曾挣扎呢？')

add(13,'细节','How did the information given to the two student groups differ?',
 ['One group heard about scientific struggles; the other heard only extraordinary achievements.','One group heard about Einstein; the other heard only about Galileo.','One group studied electromagnetism; the other studied only gravity.','One group received twenty-five years of instruction; the other received none.'],0,
 '给两组学生的信息有何差别？',['一组听科学家的挣扎，另一组只听非凡成就。','一组只听爱因斯坦，另一组只听伽利略。','一组学电磁学，另一组只学引力。','一组受教25年，另一组不受教。'],
 ['A while对照描述信息的侧重：struggles与only...accomplishments，学生都是十年级。','B 三位科学家都属于材料，不按人名分组。','C 混淆爱因斯坦研究目标与教学实验分组。','D 25年是书述爱因斯坦晚年的研究时长，非学生课程长度。'],
 ['telling one group of tenth-grade students about the struggles of Galileo, Newton, and Einstein, while telling another group only about their extraordinary accomplishments.'],
 'integrate','整合；使结合','本书叙述爱因斯坦试图把电磁与引力现象结合，尝试不等于成功','The project tried to integrate two separate models.',['integrate phenomena','extraordinary accomplishments'],
 '他不满意自己的相对论，因为它没有包含电磁学。他试图整合电磁和引力现象。遗憾的是，尽管生命最后25年都投入其中，他始终未能做到。Huang-Yao Hong和Xiaodong Lin-Siegler了解此事，于是做了实验：向一组十年级学生讲述伽利略、牛顿和爱因斯坦的挣扎，向另一组只讲他们的非凡成就。')

add(14,'推断','What does this sentence establish about the lessons?',
 ['Only the achievement group attended physics lessons.','The lessons differed in number between groups.','Students selected different subjects after the stories.','The students received the same three physics lessons.'],3,
 '本句确立了课程的什么信息？',['仅成就组参加物理课。','两组课次数不同。','听故事后学生选了不同科目。','学生上了相同的三节物理课。'],
 ['A All包括所有学生。','B three identical不支持次数差异。','C 句中没有选科安排。','D identical明确内容相同、three明确次数；这限制了用不同课堂内容解释组间结果，但单句本身不报告效果。'],
 ['All the students then attended three identical physics lessons.'],
 'identical','完全相同的','修饰三节物理课，说明两组之后接受同样课程','Both groups received identical instructions.',['identical lessons','attend a lesson'],
 '随后，所有学生都上了相同的三节物理课。',support='limited-inference')

add(15,'细节','Which outcome was reported for students who heard about struggles?',
 ['They remembered less but believed effort was unnecessary.','They were more interested and retained key concepts better.','They became convinced the scientists were simply born geniuses.','They were tested on a different set of subsequent lessons.'],1,
 '听挣扎故事的学生报告了哪项结果？',['记得较少，且认为无需努力。','兴趣更高，对关键概念记得更好。','更相信科学家只是天生天才。','测的是另一套后续课程。'],
 ['A 两个方向都反了。','B more interested与remembered...better明确支持，比较对象为只听主要成就者。','C born geniuses是成就条件学生的看法；挣扎组想到努力。','D 文中the three subsequent lessons指先前共同课程，不能凭结果捏造不同教学。'],
 ['were more interested in science at the end of the study','they remembered the key concepts learned during the three subsequent lessons better'],
 'subsequent','随后的；后续的','故事材料之后的三节物理课','The subsequent lesson revisited the same concept.',['subsequent lessons','remember key concepts'],
 '令人惊讶的是，到研究结束时，听过伟大科学家挣扎经历的学生，比只听过主要成就的学生对科学更有兴趣。此外，他们对随后三节课中学到的关键概念记得也更好。他们还认为伽利略、牛顿和爱因斯坦必须努力工作；而成就条件下学生认为这些人是天生的天才。')

add(16,'逻辑关系','Which statement distinguishes the proposed mechanism from the reported outcome?',
 ['Every intervention since 1982 tested exactly the same students.','Students’ normalization of difficulty was presented as a measured GPA increase.','Normalization is the author’s explanation; greater engagement and performance are reported effects.','The author concludes that people can control all external events.'],2,
 '哪项正确区分推测机制与报告结果？',['1982年以来每项干预研究都测同一批学生。','把困难正常化被报告为测得的GPA上涨。','正常化是作者解释；投入和表现提高是所述效果。','作者结论是人能控制所有外部事件。'],
 ['A diverse settings指多种环境，非同一学生。','B 本段高中科学课，不能移植杜克GPA结果。','C must have normalized表达作者对心理过程的推断；下一句总结课堂投入和表现提高。','D our story is in our control指叙事解释，不等于可控制全部客观事件。Redirect是作者提到的书名，非本工具指令。'],
 ['must have normalized the challenges they faced','learning about the scientists’ struggles increased high school students’ class engagement and performance.'],
 'normalized','使正常化；视为常见','把学习遇到的困难视为常见现象，而非个人无能的证据','Hearing similar stories normalized the difficulties she faced.',['normalize challenges','class engagement'],
 '了解科学家挣扎的学生，想必把自己遇到的挑战看得更正常了，就像杜克学生学会明白聪明的大一学生也会遇到困难一样。总体而言，了解科学家的挣扎提高了高中生的课堂投入和表现。自Wilson与Linville在1982年的开创性论文以来，许多这类干预研究已在不同环境中开展。对我而言，《Redirect》的主要启示是，我们能掌握自己的故事。',support='limited-inference')

add(17,'作者意图','What misunderstanding does the author explicitly reject?',
 ['That self-understanding can involve reinterpretation.','That a new narrative may support transformation.','That people can change their perspective on struggles.','That story editing requires removing every bad experience.'],3,
 '作者明确反对哪种误解？',['自我理解可涉及重新解释。','新叙事可能支持转变。','能改变看待挣扎的角度。','故事编辑必须删掉所有坏经历。'],
 ['A foundational step...self-understanding支持重新解释的作用。','B further transformation是所述可能方向。','C 首句明确可换视角。','D I am not saying...edit out all...Not at all明确否认；drop the old version指旧自我叙事，不授权编造或删除经历。'],
 ['I am not saying that you should edit out all the bad experiences to create a happier version of your life story. Not at all.'],
 'foundational','奠基性的；基础的','新的理解是后续自我认识与改变的基础步骤','Trust was a foundational part of their collaboration.',['a foundational step','edit out experiences'],
 '你能从不同视角看自己的挣扎，对这些挣扎的新解释，会成为自我理解和进一步转变的基础一步。编辑你的故事，放下旧版的自我，开始相信新版的自我叙事。我不是说，你应该删掉所有不好的经历，编出一个更快乐的人生版本。完全不是。')

add(18,'语境词义','What does “springboard” mean in this advice?',
 ['An experience used as a starting point for later change.','A device for permanently hiding a painful memory.','A guarantee that every difficult experience ends happily.','A reason to repeat the same harmful event.'],0,
 '此建议中springboard是什么意思？',['用作日后改变起点的经历。','永久藏起痛苦记忆的装置。','保证每段困难都有幸福结局。','重复同一有害事件的理由。'],
 ['A springboard作比喻，与point of redirection呼应：保留经历，将其作为改变支点。','B keep与隐藏删去相反。','C later transformation没承诺每件事都有好结局。','D use them不是让事件再发生。most, if not all意为即使不是全部，也要保留大多数。'],
 ['use them as a springboard for later transformation, as a point of redirection in your life story.'],
 'springboard','跳板；促成进一步发展的起点','坏经历被重新用作以后转变的支点，非物理跳板','The setback became a springboard for a new approach.',['a springboard for transformation','a point of redirection'],
 '你应该保留那些不好的经历，即使不是全部，也要保留大多数；不过，要把它们用作日后转变的跳板，作为人生故事中重新定向的节点。')

add(19,'作者意图','How should the reference to Virginia Woolf be understood?',
 ['As an experiment comparing novelists’ editing skills.','As evidence that earthquakes always enrich life.','As a rhetorical emphasis on the limits of editing an uneventful life.','As advice to seek dangerous experiences for better stories.'],2,
 '应如何理解弗吉尼亚·伍尔夫的提及？',['比较小说家编辑技能的实验。','地震总会使人生丰富的证据。','强调平淡无事的人生在编辑上有限度的修辞。','建议为好故事主动寻找危险。'],
 ['A I bet是作者修辞判断，非报告测量或文学实验。','B could edit是可能性，非灾害对所有人的保证效果。','C even...couldn’t用知名作家强调：仅有编辑技巧也不能凭空造出经历。','D if you’ve had是假定已有经历，没有建议制造灾难。'],
 ['You can’t make an uneventful life psychologically rich. I bet even Virginia Woolf couldn’t.'],
 'uneventful','平静无事的；缺少显著事件的','此处指缺少可供叙事加工的鲜明经历，并非道德贬义','The journey was safe and uneventful.',['an uneventful life','unusual experiences'],
 '你无法把平淡无事的人生变得心理丰富。我敢说，就连弗吉尼亚·伍尔夫也办不到。但如果你经历过地震、飓风等不同寻常的事，或人生艰难时期，就可以通过编辑，让这些经历对自己和他人更有意思。它们随后会成为你的故事、成为你是谁的一部分。')

add(20,'主旨','What relationship between experience and story editing does the passage describe?',
 ['Editing replaces the need for interesting experiences.','Experience supplies the material, and editing can make it richer and easier to remember.','A memorable story must exclude every difficult experience.','A rich life is defined solely by how often its story is retold.'],1,
 '本段怎样描述经历与故事编辑的关系？',['编辑可代替有趣经历。','经历提供材料，编辑可使叙事更丰富、更易记。','好记的故事必须排除所有困难。','丰富人生仅由故事复述次数定义。'],
 ['A experience itself处在核心，Unless明确经历不可缺。','B extract...aspects说明从现有经历中提炼；Another benefit补充记忆优势。','C 本段不要求删困难，前文还明确反对。','D 没有以讲述频率作为唯一标准。can表示可能，不保证任何编辑都有效。'],
 ['At the heart of a psychologically rich life is experience itself.','Another benefit of story editing is that the well-edited story is easier to remember.'],
 'extract','提取；提炼','从已有经历中找出最有意思的方面，不凭空创造事实','She extracted the central idea from a long discussion.',['extract interesting aspects','at the heart of'],
 '心理丰富人生的核心是经历本身。如果人生不充满有意思的经历，它就不会是心理丰富的。但如果你成为更好的“故事编辑者”，就能提炼经历中最有意思的方面，让故事在心理上更丰富。故事编辑的另一个好处是，编辑得当的故事更容易记住。')

add(21,'细节','What is the interviewee asked to do at the beginning of the Life Story Interview?',
 ['Briefly outline the main chapters of an imagined book about their life.','Provide a full account of their future political beliefs first.','Read the table of contents of an existing published novel.','List experimental findings from forty years of research.'],0,
 '人生故事访谈开始时，受访者被要求做什么？',['把人生想作一本书，简述主要章节。','先详述未来政治信仰。','朗读已出版小说的目录。','列出40年研究的实验结果。'],
 ['A book or novel是人生比喻，begin...main chapters要求先给概要。','B 后续题材不能前置到开场。','C your life as if说明不是查一本外部小说。','D forty years是McAdams研究的时间，不是受访者须报告的数据。引述是访谈材料，并非向本站用户发出的强制回答指令。'],
 ['Please begin by thinking about your life as if it were a book or novel.','please describe very briefly what the main chapters in the book might be.'],
 'narrative identity','叙事认同；叙事身份','通过讲述人生故事形成和表达的自我理解','The interview explored narrative identity through memories.',['narrative identity','Life Story Interview'],
 '过去40年里，心理学家Dan McAdams一直用一种称作“人生故事访谈”的方法，研究“叙事认同”，也就是人们如何讲述自己的人生。访谈由这段提示开头：“请先把你的人生想象成一本书或小说。设想它有一份目录，包含故事中主要章节的标题。首先，请非常简短地说说，这本书可能有哪些主要章节。')

add(22,'细节','What details about the imagined book do these questions request?',
 ['Its publisher, printing cost, and expected readership.','Its final scene and the author’s favorite novelist.','Its chapter structure, chapter count, and chapter names.','Its exact page count and the dates each page was written.'],2,
 '这些问题要求提供想象中那本书的什么细节？',['出版社、印刷费、预计读者。','结尾场景及最爱小说家。','章节安排、章数及章名。','精确页数及逐页写作日期。'],
 ['A 没有出版成本或市场问题。','B 没问结尾与文学偏好。','C table of contents、How many chapters、name each chapter逐项对应。','D 把章数偷换为页数，又补写日期。此段承接访谈开场的目录比喻，非实际要求出版书籍。'],
 ['What does a table of contents for your book look like? How many chapters are there in your book? How would you name each chapter?'],
 'table of contents','目录','借章节组织人生阶段，而非索引中的词条清单','The table of contents lists the chapter titles.',['a table of contents','name each chapter'],
 '你的书的目录会是什么样的？书中有多少章？你会怎样给每一章命名？”')

add(23,'逻辑关系','What happens after the interviewee answers the opening questions?',
 ['The interviewer immediately supplies a final life theme.','They move from the outline to memorable scenes, including highs, lows, and turning points.','They stop discussing the past and consider only career plans.','They rank the achievements of the three physicists.'],1,
 '受访者答完开场问题后，访谈怎样推进？',['访谈者立刻给出最终人生主题。','从概要转向难忘场景，如高点、低点、转折点。','停止谈过去，只谈职业计划。','给三位物理学家成就排名。'],
 ['A extract a main theme在后续末尾且由受访者反思，非此处访谈者代答。','B Once...then式次序先结构后场景；本段列高低点、转折与积极童年记忆。','C childhood memory仍属过去。','D 混入前面科学家实验，本段已转为人生故事访谈。'],
 ['Once the interviewee answers these questions, they are asked to think of a few key scenes that stand out in their story:'],
 'stand out','突出；特别显眼','指在人生叙事中格外鲜明、难忘的场景','One childhood scene still stands out in her memory.',['stand out in a story','a turning point'],
 '受访者回答这些问题后，会被请去想人生故事里几个格外鲜明的关键场景：你人生的高点是什么？低点是什么？转折点是什么？你能说出一段积极的童年记忆吗？')

add(24,'细节','Which memory is requested in this question?',
 ['A positive memory from early adulthood.','A prediction about a future disappointment.','The interviewee’s most recent professional success.','A negative memory from childhood.'],3,
 '本句询问哪类记忆？',['成年初期的积极记忆。','对未来失望的预测。','最近一次职业成功。','童年的负面记忆。'],
 ['A 同时改了情绪方向和人生阶段。','B memory指过去经历，不是未来预测。','C 句中无工作或最近一次限制。','D negative childhood memory同时限定负面性质和童年时期。保留本句简短来源，不重复上一单元的积极记忆问题。'],
 ['Can you name a negative childhood memory?'],
 'childhood','童年；儿童时期','限定所回忆经历发生的人生阶段','She described a vivid childhood memory.',['a childhood memory','a negative memory'],
 '你能说出一段负面的童年记忆吗？')

add(25,'逻辑关系','Which sequence matches this final part of the interview?',
 ['Imagine the future, discuss challenges and beliefs, then reflect on a main theme.','Extract a theme first, then end without discussing the future.','Discuss only political ideology, then list childhood memories.','Ask the interviewer to plan the future and supply the theme.'],0,
 '哪项符合本段访谈最后部分的顺序？',['想象未来、讨论挑战与信念、再反思主要主题。','先提炼主题，然后不谈未来就结束。','只谈政治思想，再列童年记忆。','让访谈者安排未来并提供主题。'],
 ['A Then...Then...Finally依次给未来、挑战及价值相关问题、最后反思提炼。','B 把Finally移到开头，且删掉未来问题。','C 漏掉梦想、宗教、价值等，并把前面的童年阶段放到结尾。','D 主语是interviewee，不能把想象反思工作转给interviewer。'],
 ['Then the interviewee is asked to imagine their future:','Then there are questions about challenges, religious and political ideology, and values.','Finally, the interviewee is asked to reflect upon their life story and extract a main theme.'],
 'reflect upon','反思；仔细思考','回看人生故事，寻找贯穿其中的主题','She took time to reflect upon the changes in her life.',['reflect upon a life story','extract a main theme'],
 '接着，受访者被要求想象未来：你人生的下一章是什么？你有哪些梦想、希望与计划？之后会有关于挑战、宗教与政治思想，以及价值观的问题。最后，受访者被要求反思自己的人生故事，并提炼一个主要主题。')

assert len(out)==25 and [q['id'] for q in out]==[t['questionId'] for t in targets]

def persist():
 path=ROOT/'source/short-questions/additional.json';existing=load('source/short-questions/additional.json');byid={q['id']:q for q in existing}
 for q in out:
  if q['id'] in byid:assert byid[q['id']]==q,('Refuse to overwrite changed authoring',q['id'])
  else:existing.append(q)
 path.write_text(json.dumps(existing,ensure_ascii=False,indent=2)+'\n',encoding='utf8',newline='\n')
 review=dict(batchId='batch-034',date='2026-10-23',pdfSha256=b['pdfSha256'],checkedPdfPages=list(range(135,140)),questionIds=[q['id'] for q in out],paragraphs=[dict(id=pid,textSha256=hashlib.sha256(pp[pid]['text'].encode()).hexdigest()) for pid in dict.fromkeys(q['paragraphId'] for q in out)],note='完整PDF135–139原页视觉核对。Wilson/Ross的自我评价与Tim Wilson/Linville干预分开；跑步时间是假设且用时增加不作提高；GPA信息组+0.34/转出5%与控制组-0.05/25%不交换，GRE表现与GPA预期分开，不补随机化或人人效果。科学家材料分挣扎/成就而后相同三节课，25年属爱因斯坦未完成尝试；must have normalized是作者机制推断，不当已直接测量。故事编辑保留坏经历不编造事件；Woolf为I bet修辞而非实验，不建议主动经历灾害。人生故事访谈从目录到场景再未来与主题，引用提示为材料不执行。保留既有切分中的单句短单元及未闭合引号跨单元，不重复句子；E = mc2保持提取原文。整段审阅若含后续未配题句另计，绝不宣称逐句直接证据全覆盖。')
 (ROOT/'source/short-questions/review-chapter12-story-editing25.json').write_text(json.dumps(review,ensure_ascii=False,indent=2)+'\n',encoding='utf8',newline='\n')
 print('Saved',len(out),'of 25 individually authored exercises')

if __name__=='__main__':persist()
