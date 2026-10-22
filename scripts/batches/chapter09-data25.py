"""25 individually authored exercises for frozen targets, PDF pages 93-97.
Preserve printed English, source positions and all previously published questions.
"""
from pathlib import Path
import json,hashlib
ROOT=Path(__file__).resolve().parents[2]
load=lambda p:json.loads((ROOT/p).read_text(encoding='utf8'))
b=load('public/data/book.json');plan=load('public/data/reading-plan.json');targets=load('source/short-questions/batch024-targets.json')['targets']
ss={s['id']:s for s in b['sentences']};pp={p['id']:p for p in b['paragraphs']};out=[]
def add(i,kind,prompt,options,answer,prompt_zh,options_zh,analyses,quotes,word,meaning,context,example,collocations,translation,support='explicit'):
 t=targets[i-1];u=next(u for u in plan['units'] if u['id']==t['readingUnitId']);group=[ss[sid] for sid in u['sentenceIds']];p=pp[u['paragraphId']];text=p['text'][group[0]['start']:group[-1]['end']]
 assert hashlib.sha256(text.encode()).hexdigest()==t['passageSha256'];evidence=[]
 for quote in quotes:
  offset=text.find(quote);assert offset>=0,(i,quote);start=group[0]['start']+offset;end=start+len(quote);touching=[s for s in group if s['start']<end and s['end']>start]
  evidence.append(dict(quote=quote,sentenceIds=[s['id'] for s in touching],sources=list({(r['pdfPage'],r['block']):r for s in touching for r in s['sources']}.values())))
 assert word.lower() in text.lower(),(i,word)
 out.append(dict(id=t['questionId'],version=1,readingUnitId=u['id'],chapterId=u['chapterId'],sectionId=u['sectionId'],paragraphId=u['paragraphId'],sentenceIds=u['sentenceIds'],passage=text,prompt=prompt,options=options,answer=answer,type=kind,promptZh=prompt_zh,optionsZh=options_zh,analyses=analyses,evidence=evidence,vocabulary=[dict(word=word,meaning=meaning,context=context,example=example,collocations=collocations)],translation=translation,support=support,editorialStatus='PDF第93–97页原页核对；哲学和人物引述、个人反应、实验评分与回顾调查分别归属；maybe和相关限制保留，不扩大因果或群体标签'))







add(1,'主旨','What contrast does Rollins draw between physical existence and art?',
 ['Technology guarantees that every life has meaning.','Art is simply another way to earn money and watch screens.','Meeting physical needs alone does not supply the significance he attributes to art.','Physical existence is described as impossible without modern screens.'],2,
 'Rollins 如何对比物质生存与艺术？',['科技保证每个人生有意义。','艺术只是赚钱和看屏幕的另一方式。','仅满足物质需要，并不具有他赋予艺术的意义。','没有现代屏幕就不可能生存。'],
 ['A Technology is no savior 否定这种保证。','B exact opposite 表明对照，不是等同赚钱看屏幕。','C physical existence...doesn’t mean anything 后转向艺术，概括其价值判断。','D 举例生活活动不等于没有屏幕无法生存。这是 Rollins 的艺术观，不是作者实验得出的普遍生存定律。'],
 ['all aspects of our physical existence—but that doesn’t mean anything. Art is the exact opposite.'],
 'savior','拯救者；救星','no savior 在引语中否认科技能单独提供终极意义','The new tool was useful, but it was no savior for the failing plan.',['technology is no savior','be seen as a savior'],
 '有人问传奇爵士萨克斯手 Sonny Rollins 艺术、尤其艺术为何重要时，他的回答令人联想 Kant 的审美判断：“科技不是救星。我们能吃、睡、看屏幕、赚钱——这些都属物质生存，却不意味什么。艺术恰好相反。它无限，没有它，世界就不会是如今这样。（引语续下段）')

add(2,'细节','What two effects of art are paired at the end of Rollins’s quotation?',
 ['Encouraging exploration and revealing the limits of what we know.','Eliminating intuition and making every political view identical.','Preventing new discoveries and confirming complete knowledge.','Replacing every emotional experience with a new fact.'],0,
 'Rollins 引语末尾并列艺术哪两项作用？',['鼓励探索，显露我们所知的局限。','消除直觉，使政治观点一致。','阻止发现，确认已知一切。','用新事实替代全部情感体验。'],
 ['A inspires...find something new 与 highlights what we don’t know 分别对应。','B intuition 被视为艺术所代表的东西，非需消除。','C 两项方向都反了。','D 此处没有把情感都换成事实。both...and 提示并列，不能只保留其中一项。'],
 ['both inspires us to go out and find something new and highlights what we don’t know.'],
 'veneer','表面装饰；表层外衣','political veneer 比喻覆盖一切的争议性政治表层，不是木板材料','The debate hid personal concerns beneath a veneer of certainty.',['a political veneer','beneath the veneer'],
 '“它代表非物质的灵魂：直觉，以及我们心里的感受。今天艺术比以往更重要，因为它比覆盖一切的争议性政治外衣更长久……艺术既激励我们出去发现新事物，也让我们看见自己不知道什么。”')

add(3,'细节','What does Brooks say he is trying to counteract?',
 ['Spending too much time learning a musical instrument.','A complete lack of interest in any public issue.','His inability to find any works of art.','Being too caught up in politics.'],3,
 'Brooks 说自己试图应对什么？',['学乐器耗时太多。','完全不关心公共议题。','找不到任何艺术作品。','过度卷入政治。'],
 ['A 没有乐器学习的信息。','B enmeshed in politics 表示卷入过多，非毫不关心。','C I flee to the arts 指转向艺术，未说找不到。','D too much...enmeshed in politics 与 countermeasures 前后对应。这是文章作者的自述，不是建议所有人忽视政治。'],
 ['I spend too much of my time enmeshed in politics'],
 'enmeshed','被卷入的；纠缠其中的','Brooks 描述被政治占据过多时间','She became enmeshed in arguments that distracted her from her work.',['be enmeshed in politics','be enmeshed in disputes'],
 'David Brooks 在文章 The Power of Art in a Political Age 中呼应 Rollins。他写道：“像很多人一样，我把太多时间耗在政治纠缠之中……所以我试着采取应对办法。我逃向艺术。”')

add(4,'主旨','What benefit of art does Brooks emphasize?',
 ['Its value depends entirely on teaching a new factual claim.','It expands emotional experience rather than merely adding facts.','It prevents viewers from responding with awe.','It works only through novels and never through visual art.'],1,
 'Brooks 强调艺术什么益处？',['价值完全取决于教会新事实。','扩大情感体验，而不只是增加事实。','阻止观者敬畏。','只靠小说，视觉艺术无效。'],
 ['A haven’t learned a new fact...had a new experience 是对照，非事实唯一标准。','B widen your emotional repertoire 概括情绪体验扩展。','C childlike awe 明确允许敬畏。','D sculpture 与 looking at art 包含视觉艺术。引语是观点说明，不是对每个观众必定发生的实测保证。'],
 ['artworks widen your emotional repertoire.','you haven’t learned a new fact, but you’ve had a new experience.'],
 'repertoire','可运用的范围；积累的储备','emotional repertoire 指可感受的情绪范围，不是音乐曲目清单','The story widened her emotional repertoire.',['emotional repertoire','widen one’s repertoire'],
 '他说，艺术“促使你停下、呼吸、敞开心，接纳它给予的东西，常怀孩子般的惊叹与敬意……作品扩大你的情感范围。读诗或看雕塑，你未必学到新事实，却有了新体验”。不只小说与诗，看艺术也能让我们向新体验敞开。')

add(5,'主旨','What problem is associated with “Das Gerede” in this account?',
 ['It leaves people with too much independent reflection.','It prevents any information from being passed between people.','It obscures importance through repeated chatter and distraction instead of deep thought.','It refers only to incorrect pronunciation of philosophical terms.'],2,
 '这里的 Das Gerede 有什么问题？',['使人独立深思过多。','阻止人们传递任何信息。','以不断闲谈和分心代替深思，遮蔽重要之事。','只指哲学术语发音错误。'],
 ['A without thinking deeply 与深思过多相反。','B passing the word along 正在传递信息，问题是缺少深入思考。','C obscures what is truly important 与 distraction 支持此项。','D 文中定义为 endless chatter，不是发音问题。这里呈现 Heidegger 的哲学论述，非注意力实验。'],
 ['the endless chatter of everyday life obscures what is truly important.'],
 'obscures','遮蔽；使不清楚','闲谈让重要事物不易被深入看见','Constant interruptions obscure the main issue.',['obscure what matters','obscure the truth'],
 'Rollins 与 Brooks 的艺术观让我想到 Martin Heidegger 的 Das Gerede，即无尽闲谈。在 Being and Time 中，他认为我们沿着“闲话与传话的路径”生活，日常无尽闲谈遮蔽真正重要之事。在这种世界中，我们不经独立深思就好像明白一切，还不断遭遇“随时可能分心”的轰炸。')

add(6,'逻辑关系','What consequence of chatter and distractions is described?',
 ['They leave little room for deep thinking or encounters with the sublime.','They guarantee a stable feeling of rootedness.','They remove all tasks from people’s to-do lists.','They prove that every conversation is equally harmful.'],0,
 '闲谈与分心带来什么后果？',['很少留下深思或接近崇高之物的空间。','保证人有稳定的扎根感。','移除待办清单的一切任务。','证明每种谈话都同样有害。'],
 ['A rarely have a moment...think deeply...sublime 直接对应。','B uprooted, groundless 与稳定相反。','C to-do lists 仍在，并未消失。','D 当前是作者概括，不是每种谈话伤害相同的实验。rarely 是很少，不是绝无可能。'],
 ['we rarely have a moment to think deeply, or to convene with the sublime.'],
 'sublime','崇高的事物；超越日常的壮美','这里指可引起敬畏的体验对象，非待办事项','The landscape offered a brief encounter with the sublime.',['the sublime','convene with the sublime'],
 '社交媒体是无尽闲谈，寒暄也是。它让生活感觉失根、无依、漂浮。在待办清单与无尽分心之间，我们很少有片刻深入思考，或与崇高之物相会。')

add(7,'细节','How certain is the author about the role of Rothko’s biography in his response?',
 ['He reports a controlled experiment proving the role of biography.','He says biography cannot influence any viewer.','He states that depression necessarily improves artistic quality.','He offers background knowledge as a possible explanation, not a certainty.'],3,
 '作者多确定 Rothko 生平知识对自身反应的作用？',['报告受控实验已证明生平的作用。','说生平不会影响任何观者。','断言抑郁必定提高艺术质量。','把背景知识作为一种可能解释，而非定论。'],
 ['A For me 和 maybe 表明个人体验及猜测，不是实验。','B maybe because 没排除影响。','C 没有疾病提升艺术的因果论。','D maybe because I know 保留解释的不确定性。人物死亡按书中描述呈现，不添加原因、细节或医学诊断。'],
 ['maybe because I know Rothko was depressed and ultimately took his own life.'],
 'visceral','切身强烈的；直觉性的','形容看画的直接感受，不是测量生理器官','The performance produced a visceral response in the audience.',['a visceral experience','a visceral response'],
 '对我而言，艺术与运动给了少有的机会，逃离日常闲谈。看 Mark Rothko 的 No. 13（White, Red on Yellow）与其他色域画，总是独特、切身强烈的体验。简单色彩与模糊线条使我平静、投入，甚至感动，也许因为我知道他曾抑郁，最终结束了自己的生命。')

add(8,'逻辑关系','What does the opening “Or maybe” do?',
 ['It cancels the author’s report of ever visiting the museum.','It introduces the alternative that biography may not explain the reaction.','It proves that the painting has no emotional effect.','It identifies a second painting as the only possible cause.'],1,
 '开头 Or maybe 起什么作用？',['取消曾到博物馆的陈述。','提出另一可能：生平知识也许不解释反应。','证明画没有情感作用。','认定另一幅画是唯一原因。'],
 ['A many times 仍保留多次到访。','B nothing to do with this background knowledge 是替代解释。','C draws me in 表示仍有吸引。','D 没有另一幅画或唯一原因。Maybe 连同上一段 maybe 表示未定，不能选定任何解释为已证明。'],
 ['Or maybe it has nothing to do with this background knowledge.'],
 'draws me in','吸引我投入其中','形容注意被画吸引，不是画面里画入作者','The opening scene draws me in immediately.',['draw someone in','be drawn into a painting'],
 '或者，也许这与背景知识毫无关系。我曾多次坐在 Metropolitan Museum of Art 的 No. 13 前。它吸引我投入其中，让我忘掉其他一切。')

add(9,'作者意图','What distinction does Rothko’s quotation emphasize?',
 ['A painting can only report an event that happened to its creator.','Art has value only when its biography is fully known.','Encountering a painting can itself constitute an experience.','Paintings and experiences are defined as unrelated things.'],2,
 'Rothko 的引语强调什么区别？',['画只能报告创作者亲历事件。','只有完全知道生平艺术才有价值。','面对一幅画，本身就可以构成体验。','画与体验被定义为互不相关。'],
 ['A not about 与只能报告相反。','B 引语没有生平知识的必要条件。','C It is an experience 将作品当体验本身。','D 不是切断关系，而是把体验置于核心。这是艺术家阐释，非量化实验。'],
 ['A painting is not about an experience. It is an experience.'],
 'experience','体验；亲身感受','引语后一句强调作品本身带来的遭遇，而非仅描绘别人的经历','Seeing the installation in person was an experience of its own.',['an aesthetic experience','experience a painting'],
 '正如 Mark Rothko 曾说：“一幅画不是关于某次体验的东西。它就是一次体验。”')

add(10,'主旨','What general distinction did Berlyne report?',
 ['The same complexity level always maximized pleasure and interest.','Complex figures were typically more pleasant and less interesting.','Simple figures were always both unpleasant and uninteresting.','Pleasantness and interestingness had different optimal complexity levels.'],3,
 'Berlyne 报告什么一般区别？',['同一复杂度总使愉悦和趣味同时最高。','复杂图通常更愉悦、更无趣。','简单图总是不愉悦又无趣。','愉悦与趣味各有不同最佳复杂度。'],
 ['A different, optimal levels 否定同一最佳点。','B 原文把较愉悦归简单、较有趣归复杂，方向相反。','C simple 通常更愉悦，不是总不愉悦。','D major finding 直接概括。typically 保留一般趋势，不改成人人每次都一样。'],
 ['different, optimal levels of complexity for pleasantness and interestingness.'],
 'optimal','最佳的；最适宜的','对不同评价指标，最佳复杂程度可能不同','The optimal level of detail depends on the purpose of the task.',['optimal levels of complexity','an optimal balance'],
 'Daniel Berlyne 在 1971 年的 Aesthetics and Psychobiology 中总结一系列审美判断实验。主要发现是，愉悦与趣味各有不同最佳复杂程度。简单几何图通常比复杂图更愉悦，复杂图则通常比简单图更有趣。')

add(11,'细节','Which two factors were manipulated in the geometric-figure experiment?',
 ['Symmetry and the number of elements.','Color and the participants’ income.','The artist’s biography and political views.','Whether participants had studied novels in childhood.'],0,
 '几何图形实验操纵哪两个因素？',['对称性与元素数量。','颜色与参与者收入。','艺术家的生平与政见。','童年是否读过小说。'],
 ['A first...symmetry 与 other...number of elements 直接列出。','B 没有收入或颜色操纵。','C 这是前面谈论艺术的主题，不是本实验因素。','D 把后面阅读调查移到当前实验。简单对称最愉悦的排序是结果，不要混成另一个被操纵因素。'],
 ['the first was symmetry','the other was the number of elements'],
 'symmetry','对称性','指图形元素的对称和同质程度，与数量是两个因素','The design uses symmetry to create a sense of balance.',['symmetry of a figure','simple and symmetrical'],
 '一项实验中，Berlyne 操纵几何图形两个因素：一是对称性，即元素多对称、多同质；二是元素数量，即一至五个或许多个。有些图简单对称，有些简单不对称，有些复杂对称，另一些复杂不对称。参与者认为简单对称最愉悦，其后依次为复杂对称、简单不对称、复杂不对称。对称性是愉悦的关键。')

add(12,'逻辑关系','What contrast is expressed by the ratings?',
 ['The most pleasing figures were also the most interesting.','The most pleasing simple symmetrical figures were the least interesting.','Complexity increased pleasantness and reduced interest.','Asymmetry made no difference to either judgment.'],1,
 '这些评分呈现什么对比？',['最愉悦的也最有趣。','最愉悦的简单对称图反而最无趣。','复杂性提高愉悦、降低趣味。','不对称对两评价都无影响。'],
 ['A least interesting 与最有趣相反。','B rated most pleasing...least interesting 直接形成对比。','C 两方向颠倒。','D asymmetry added interestingness...detracted pleasantness 明说有差异。不能把 pleasing 和 interesting 当同一指标。'],
 ['simple and symmetrical figures (rated most pleasing) to also be the least interesting.'],
 'detracted from','减损；降低','增加复杂性和不对称性时，愉悦性下降，与趣味上升对照','The visual clutter detracted from the design’s clarity.',['detract from pleasantness','add interest but detract from pleasure'],
 '然而，Berlyne 发现，参与者把最愉悦的简单对称图也评为最无趣。复杂性与不对称增添趣味，却降低愉悦。')

add(13,'细节','How were the thirteen paintings divided in the study?',
 ['Seven calming and six disturbing paintings.','Thirteen calming paintings and no disturbing ones.','Six calming and seven disturbing paintings.','Six geometric figures and seven poems.'],2,
 '研究中的十三幅画怎样分组？',['七幅平静、六幅扰人。','十三幅都平静，没有扰人的。','六幅平静、七幅扰人。','六个几何图与七首诗。'],
 ['A 对调六和七。','B The other seven were disturbing 明示另一类。','C thirteen...six...other seven 数量与分类吻合。','D 当前是 classical paintings，不是前后研究刺激混合。题目考材料构成，不把作品描绘事件当现实发生或实验行为。'],
 ['thirteen classical paintings, six of which were calming','The other seven were disturbing'],
 'disturbing','令人不安的；令人震动的','描述作品给观者的感受类别，不是指实验中实际伤害了人','The unsettling image was disturbing to some viewers.',['a disturbing painting','calming versus disturbing'],
 '较近时候，Paul Silvia 与 Samuel Turner Jr. 做了一项有趣审美判断实验。参与者看十三幅古典画，其中六幅平静，如 Edgar Degas 的 Dance Foyer at the Opera 和 Claude Monet 的 The Water Lily Pond。另七幅令人不安，如 Francis Bacon 的 Figure with Meat——惊恐教皇周围两具牛尸——和 Francisco Goya 的 Saturn Devouring His Son，即神吞食人肉的画面。')

add(14,'细节','Which characteristics predicted pleasantness ratings?',
 ['Comprehensibility, familiarity and simplicity.','Disturbingness and unpleasantness alone.','The number of novels read by the artist.','Participants’ ability to identify the painter’s death date.'],0,
 '哪些特征预测愉悦评分？',['可理解性、熟悉性与简单性。','只有扰人程度和不愉悦。','画家读过的小说数量。','参与者识别画家死亡日期的能力。'],
 ['A predicted by 后明确列三项，解释句也强调易懂和简单。','B 是下一部分关于趣味的方向，非愉悦预测。','C 没有画家阅读量。','D 没有死亡日期测试。评分之间的预测关系不自动证明改变任一特征就必然造成每个人更快乐。'],
 ['pleasantness ratings were predicted by comprehensibleness, familiarity, and simpleness.'],
 'comprehensible','可理解的；易懂的','指参与者觉得画容易理解的程度，不是客观唯一正确解读','The short explanation made the abstract image more comprehensible.',['more comprehensible','comprehensible or incomprehensible'],
 '这些画相当震撼、怪诞，尤其与 Monet 著名的宁静温暖画作相比。每看完一幅，参与者报告它多有趣或无趣、多无聊或吸引人、多享受或不享受、多愉悦或不愉悦、多可理解或难懂、多熟悉或陌生。结果显示，可理解性、熟悉性与简单性可预测愉悦评分。也就是说，画越易懂、越简单，就越愉悦。')

add(15,'逻辑关系','What pattern is reported for interestingness?',
 ['Only calming paintings were found interesting.','Interestingness and unpleasantness always moved in opposite directions.','The findings prove all distressing events enrich real life.','More disturbing and unpleasant paintings received greater interestingness ratings.'],3,
 '关于趣味性，报告什么模式？',['只有平静画被认为有趣。','趣味和不愉悦总反向变化。','结果证明所有现实痛苦事件都丰富人生。','更扰人、更不愉悦的画得到更高趣味评价。'],
 ['A more disturbing...more interesting 不限平静画。','B 本片段二者同向，非总反向。','C 画作评分不能推广为所有真实痛苦都益于人生。','D In contrast 引出与愉悦不同的预测关系，保留 paintings 的范围。interesting 不能直接改成 happy。'],
 ['the more disturbing and unpleasant they were, the more interesting the paintings were.'],
 'unpleasantness','不愉悦性；令人不舒服的程度','画作可能不舒服却有趣，两个评分维度分开','Unpleasantness and interest were rated separately.',['ratings of unpleasantness','disturbingness and unpleasantness'],
 '相比之下，扰人程度与不愉悦程度预测趣味评分。也就是说，画越扰人、越不愉悦，反而越有趣。')

add(16,'细节','What differed between the groups reading the abstract poem?',
 ['They were given entirely different poems.','One group received background information about the same poem.','One group was told to avoid reading the title under all conditions.','Only one group was permitted to report interest.'],1,
 '阅读抽象诗的组别之间什么不同？',['读完全不同的诗。','其中一组获得同一首诗的背景信息。','一组被要求在所有条件下避开标题。','只有一组可以报告趣味。'],
 ['A same poem 明确刺激文本相同。','B with more background information 包括标题和 Haifisch 的词义。','C 原文对比有无信息，不是要求所有条件避标题。','D 两组都涉及理解与兴趣，没有只准一组评价。不要补写未给出的随机分组或长期影响。'],
 ['read the same poem but with more background information'],
 'background information','背景信息','例如诗题与 Haifisch 的德语词义，用来帮助理解同一诗作','Background information helped the class interpret the poem.',['provide background information','with more background information'],
 '另一实验中，Silvia 探索理解的作用。例如，让参与者读 Scott MacLeod 著名的抽象诗 The Life of Haifisch。没有任何背景信息的人无法理解，也不觉得有趣。相比之下，读同一首诗却得到更多背景信息的人——如标题和 Haifisch 在德语中意为“鲨鱼”的解释——觉得它更易懂、有趣得多。')

add(17,'逻辑关系','What condition is stated for appreciating art?',
 ['At least a minimal degree of comprehensibility.','Complete simplicity with no ambiguity.','Total incomprehensibility for every viewer.','A requirement to know every detail of the artist’s life.'],0,
 '欣赏艺术需要什么条件？',['至少最低程度的可理解性。','完全简单且无歧义。','对每个观众都完全难懂。','必须知道艺术家全部生平细节。'],
 ['A at least minimally comprehensible 直接对应。','B 最低可理解不等于完全简单或无歧义。','C 与 must be...comprehensible 相反。','D 没有生平细节的必要要求。必要条件也不是充分保证：能理解不等于一定喜欢。'],
 ['For art to be appreciated, it must be at least minimally comprehensible.'],
 'minimally','最低限度地','给出理解门槛，而不是要求完全透明、毫无复杂性','The instructions must be minimally clear before the task begins.',['at least minimally comprehensible','minimally clear'],
 '这里有一条微妙的界线。艺术要被欣赏，至少必须有最低限度的可理解性。')

add(18,'细节','What information did the researchers ask over 5,000 people to report?',
 ['Only their scores on a randomly assigned childhood reading program.','Only their parents’ political views and school grades.','Childhood reading habits, current cognitive styles and perceived richness.','The physiological effects of viewing Rothko paintings.'],2,
 '研究者向五千多人询问什么？',['仅询问随机分配的童年阅读项目得分。','仅父母政见与学校成绩。','童年阅读习惯、当前认知风格和自觉丰富性。','观看 Rothko 画作的生理反应。'],
 ['A asked...habits 是回顾询问，不是随机给童年项目。','B 当前列项没有父母政见或成绩。','C 三个项目均与末句逐一对应。','D 把此前个人观画与当前调查混淆。over 5,000 是五千多，非恰好五千；perceived 是自我感知，不是全知客观评分。'],
 ['their reading habits during childhood, their current cognitive styles, and their perceived levels of psychological richness.'],
 'perceived','感知到的；自认为的','限定丰富性是受访者对自身的评价','The survey measured perceived levels of stress.',['perceived psychological richness','perceived levels of'],
 '在 University of Virginia 时，我有机会与两位学生 Erin Westgate 和 Nick Buttrick 合作，一起阅读 Paul Silvia 等人的实验美学文献。我们想知道，早年读各种书是否帮助读者欣赏更多复杂性、过更丰富的智性生活。于是向五千多人询问童年阅读习惯、当前认知风格，以及自觉心理丰富程度。')

add(19,'作者意图','What does the second sentence signal about the original assumption?',
 ['It confirms every genre had an identical effect.','It proves reading was randomly assigned in childhood.','It says the researchers had made no prediction.','The findings were more complicated than the general prediction.'],3,
 '第二句怎样回应最初假设？',['确认每类书效果相同。','证明童年阅读被随机分配。','说研究者完全没作预测。','结果比一般性预测更复杂。'],
 ['A more intricate 不等于完全相同。','B 没有随机分配，associated 也非因果。','C We assumed 明示原先预测。','D than...anticipated 表示实际结果超出原先简单预想。本片段尚未列出具体书类差异，不提前编写方向。'],
 ['Our findings were more intricate than we had anticipated.'],
 'intricate','复杂而细致的','结果具有不止一种简单关系，尚未在此句展开','The analysis revealed an intricate pattern.',['intricate findings','more intricate than anticipated'],
 '我们原先假设，一般而言阅读会与更灵活的认知风格、更高心理丰富性相关。但结果比预料的更复杂。')

add(20,'细节','Which contrast between childhood reading groups is reported?',
 ['Literary-fiction readers were less attributionally complex; romance readers more so.','Literary-fiction readers showed greater attributional complexity, while heavy romance readers showed less.','Both groups were reported to have exactly identical cognitive styles.','The researchers assigned adults to become lifelong romance readers.'],1,
 '报告了两类童年阅读群体什么差别？',['文学小说读者归因复杂性较低，言情读者较高。','文学小说读者较高，而大量言情读者较低。','两组认知风格完全一样。','研究者把成人随机变成终身言情读者。'],
 ['A 两个方向都反转。','B indeed more...literary fiction 与 unexpectedly...romance...less 对应。','C 结果明确不同，不是完全一样。','D grew up reading 是既有经历，不是被分配的人生。这是群体关联，不能把阅读类型当因果或给每位读者贴能力标签。'],
 ['reading a lot of literary fiction were indeed more attributionally complex','reading a lot of romance novels were significantly less attributionally complex'],
 'attributionally complex','归因复杂的','能想到一个人某行为的多种原因，而非只贴单一标签','An attributionally complex explanation considered several motives.',['attributional complexity','more attributionally complex'],
 '首先，如预测，童年读很多文学小说的人，归因更复杂——即能想到某人为何那样行动的多种原因——成年心理生活也比没这样读的人更丰富。其次，出乎意料，童年读很多言情小说的人，归因复杂性显著低于没这样读的人。与较少读言情者相比，他们似乎更倾向“本质化”。')

add(21,'逻辑关系','What contrast does the example of Joe illustrate?',
 ['A single fixed label versus recognizing behavior may vary across relationships.','Proof that Joe is a real participant who always behaves identically.','Evidence that every romance reader dislikes both sport and opera.','The claim that no one can ever act generously.'],0,
 'Joe 的例子说明什么对比？',['单一固定标签，与认识行为可随关系而不同。','证明 Joe 是实际参与者且总行为一致。','证明每位言情读者都讨厌运动和歌剧。','没人能慷慨的主张。'],
 ['A jerk 对照对某些人不好却能对无家者慷慨，展示非单一本质化。','B for example 是说明性人物，不能当真实追踪对象。','C tended 和例子均不能扩大到每位读者；opera is for old people 也非同义于讨厌。','D sweet and generous 直接允许慷慨。其他量表复现不等于已证明阅读造成变化。'],
 ['Joe could be a jerk to some but also sweet and generous to homeless people'],
 'essentialize','本质化；用固定本质概括','把人或事简化成单一不变标签，与考虑多种情境原因对照','We should avoid essentializing people from a single action.',['essentialize a person','less likely to essentialize'],
 '例如，早期言情读者往往持较简化世界观：Joe 是讨厌鬼，Jill 是天使，棒球无聊，歌剧给老人看，等等。相反，童年读很多文学小说的人较不本质化，更可能想到 Joe 对某些人很差，却也可能对无家者友善慷慨。第三，这些发现用其他指标，如本质主义量表，也得到复现。')

add(22,'有限推断','What does the statistical-control result support?',
 ['Every possible confounder was removed and causation proved.','Age, gender and education were randomly assigned.','The association persisted after accounting for the listed demographic and political variables.','Reading habits had no relationship with cognitive complexity.'],2,
 '统计控制结果支持什么？',['排除所有混杂因素，并证明因果。','年龄、性别和教育被随机分配。','考虑列出的人口与政治变量后，关联仍存在。','阅读习惯与认知复杂性无关系。'],
 ['A 控制列出变量不等于所有混杂，也不能证明因果。','B statistically controlling 是分析调整，非随机分配人生属性。','C remained significant after...control 准确保留结论范围。','D link...was there 明示关系仍在。不能从显著推到效果必然很大或对每个人成立。'],
 ['remained significant after statistically controlling for participants’ age, gender, education, income, and political orientation'],
 'controlling for','在统计上控制；调整……的影响','分析中考虑列出的差异，不是实际控制人的性别年龄','The association remained after controlling for age.',['statistically control for','control for education and income'],
 '在统计上控制年龄、性别、教育、收入与政治倾向后，结果仍显著：大量阅读文学小说与认知复杂性的联系仍在，不能仅归结为这些读者教育较多、年纪较大或政治更自由派。',support='limited-inference')

add(23,'逻辑关系','What limitation accompanies the empirical support for Trilling’s thesis?',
 ['The studies measured only historical book prices.','No relationship was observed at all.','Reading was experimentally proved to cause all reported differences.','The studies were correlational, leaving causality for future tests.'],3,
 '对 Trilling 论点的实证支持附带什么限制？',['研究只测历史书价。','完全没发现关系。','实验已证明阅读造成全部差异。','研究是相关性的，因果仍需未来检验。'],
 ['A 没有书价测量。','B empirical support 不等于没关联。','C correlational 明确排除此处的因果证明。','D 最后一句直接给出限制。哲学文学论点获部分数据支持，也不使其每句话成为实验定律。'],
 ['Our studies were correlational, so the causal role of reading literature needs to be tested in the future.'],
 'correlational','相关性的','观察变量之间联系，未据此确立阅读的因果作用','A correlational study can identify a link without proving its cause.',['correlational studies','a correlational finding'],
 '最终，我们找到了支持 Lionel Trilling 在 1950 年 The Liberal Imagination 中主要论点的实证证据：“文学是最充分、最精确考虑多样性、可能性、复杂性与困难的人类活动。”我们的研究是相关性的，所以阅读文学的因果作用仍需未来检验。')

add(24,'语境词义','What does “perspective-taking” mean in the passage?',
 ['Judging behavior only from an outside observer’s viewpoint.','Seeing another person’s behavior from that person’s own perspective.','Taking photographs of people from several camera angles.','Assuming every character has an identical motive.'],1,
 '本段 perspective-taking 是什么意思？',['只从外部观察者角度评判行为。','从行为者自身视角看其行为。','从多个镜头角度拍人。','假设所有角色动机一致。'],
 ['A rather than 明确区分观察者视角。','B 括号中解释即行为者自身角度。','C 是心理理解，不是摄影。','D 没有动机一致的要求。associated 与 appears 保留关联和谨慎措辞，不能改成文学必然造成能力提升。'],
 ['see another person’s behavior from that person’s perspective rather than from an observer’s perspective'],
 'perspective-taking','换位思考；视角采择','尝试从对方的立场理解其行为，而非只凭旁观判断','Perspective-taking helped her understand a colleague’s choice.',['perspective-taking skills','better perspective-taking'],
 '总体而言，阅读文学与更高认知复杂性、更好的换位思考能力相关——即从行为者自身而非观察者视角看待其行为的技能——而且似乎帮助我们欣赏自己人生的起伏。')

add(25,'作者意图','What question is introduced for the new series of experiments?',
 ['Whether a multiple-view figure would be visually richer than a single-view figure.','Whether the earlier correlational survey had already proved causality.','Whether every painting has exactly the same complexity.','Whether perspective change has already been empirically confirmed in all contexts.'],0,
 '新一系列实验引入什么问题？',['多视角图是否比单视角图在视觉上更丰富。','此前相关调查是否已证明因果。','每幅画是否复杂度完全相同。','视角改变是否已在所有场景实证确认。'],
 ['A tested whether 后明示 multiple views 与 one view 的比较。','B 本段转换到视觉实验，不是宣布先前调查因果成立。','C 比较视图数量，不是所有画相同。','D so far...not provided empirical evidence 明确承认此前未给证据。本片段只提出检验，未报告结果，不提前把后文答案写入当前证据。'],
 ['tested whether a figure with multiple views, like a figure-ground drawing, would be more visually rich than a figure with one view.'],
 'figure-ground','图形与背景的；图底关系的','可通过图形和背景的切换产生不同视图，是比较例子','The figure-ground drawing could be interpreted in two ways.',['a figure-ground drawing','figure-ground perception'],
 '我反复主张，视角改变是心理丰富体验的关键，但到此为止尚未为该主张提供实证证据。在一系列实验中，Jordan Axt、Hyewon Choi 和我检验：像图底关系图那样有多个视角的图形，是否比只有一个视角的图形在视觉上更丰富。')

assert len(out)==25 and [q['id'] for q in out]==[t['questionId'] for t in targets]

def persist():
 path=ROOT/'source/short-questions/additional.json';existing=load('source/short-questions/additional.json');byid={q['id']:q for q in existing}
 for q in out:
  if q['id'] in byid:assert byid[q['id']]==q,('Refuse to overwrite changed authoring',q['id'])
  else:existing.append(q)
 path.write_text(json.dumps(existing,ensure_ascii=False,indent=2)+'\n',encoding='utf8',newline='\n')
 review=dict(batchId='batch-024',date='2026-10-22',pdfSha256=b['pdfSha256'],checkedPdfPages=list(range(93,98)),questionIds=[q['id'] for q in out],paragraphs=[dict(id=pid,textSha256=hashlib.sha256(pp[pid]['text'].encode()).hexdigest()) for pid in dict.fromkeys(q['paragraphId'] for q in out)],note='完整PDF93–97原页视觉核对。Rollins/Brooks/Heidegger/Rothko是引述或个人体验；Rothko反应的maybe保留不确定性。几何图形与画作愉悦/趣味分开，提供诗歌背景比较不改成诗歌不同。5000余人是回顾自报关联，统计控制非因果证明，阅读类型结果不变成所有读者标签。末段仅提出多视角实验问题，未提前写入结果。')
 (ROOT/'source/short-questions/review-chapter09-data25.json').write_text(json.dumps(review,ensure_ascii=False,indent=2)+'\n',encoding='utf8',newline='\n')
 print('Saved',len(out),'of 25 individually authored exercises')

if __name__=='__main__':persist()
