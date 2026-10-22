"""25 individually authored exercises for frozen targets, PDF pages 33-38.
Preserve printed English, source positions and all previously published questions.
"""
from pathlib import Path
import json,hashlib
ROOT=Path(__file__).resolve().parents[2]
load=lambda p:json.loads((ROOT/p).read_text(encoding='utf8'))
b=load('public/data/book.json');plan=load('public/data/reading-plan.json');targets=load('source/short-questions/batch010-targets.json')['targets']
ss={s['id']:s for s in b['sentences']};pp={p['id']:p for p in b['paragraphs']};out=[]
def add(i,kind,prompt,options,answer,prompt_zh,options_zh,analyses,quotes,word,meaning,context,example,collocations,translation,support='explicit'):
 t=targets[i-1];u=next(u for u in plan['units'] if u['id']==t['readingUnitId']);group=[ss[sid] for sid in u['sentenceIds']];p=pp[u['paragraphId']];text=p['text'][group[0]['start']:group[-1]['end']]
 assert hashlib.sha256(text.encode()).hexdigest()==t['passageSha256'];evidence=[]
 for quote in quotes:
  offset=text.find(quote);assert offset>=0,(i,quote);start=group[0]['start']+offset;end=start+len(quote);touching=[s for s in group if s['start']<end and s['end']>start]
  evidence.append(dict(quote=quote,sentenceIds=[s['id'] for s in touching],sources=list({(r['pdfPage'],r['block']):r for s in touching for r in s['sources']}.values())))
 assert word.lower() in text.lower(),(i,word)
 out.append(dict(id=t['questionId'],version=1,readingUnitId=u['id'],chapterId=u['chapterId'],sectionId=u['sectionId'],paragraphId=u['paragraphId'],sentenceIds=u['sentenceIds'],passage=text,prompt=prompt,options=options,answer=answer,type=kind,promptZh=prompt_zh,optionsZh=options_zh,analyses=analyses,evidence=evidence,vocabulary=[dict(word=word,meaning=meaning,context=context,example=example,collocations=collocations)],translation=translation,support=support,editorialStatus='PDF 第 33–38 页逐题核对；固定连续原句；区分论述、文学人物与真实人物叙事，不将个案经历当作普遍因果'))

add(1,'观点归属','What explanation does Cottee offer for joining terrorist organisations?',
 ['Members are motivated exclusively by financial rewards.','Organisations can offer identity, purpose, and an account of one’s place in the world.','Every recruit has already rejected any search for meaning.','A controlled experiment proves that all searches for purpose lead to terrorism.'],1,
 'Cottee 为加入恐怖组织提供了什么解释？',['成员完全受金钱报酬驱动。','组织能提供身份、目的，以及对个人在世界中位置的解释。','每位新成员都已拒绝寻找任何意义。','对照实验证明所有目的追寻都通向恐怖主义。'],
 ['A one of the main reasons 与 exclusively 均不符，片段没有金钱解释。','B 引语列出 identity、purpose 和理解自身位置的 narrative。','C desire for ultimate meaning 与拒绝寻找意义相反。','D 此处是 Cottee 的解释，may well be part 保留可能和部分动机，非全称实验结论。'],
 ['Terrorist groups provide an important source of identity and purpose for their members','a narrative for understanding their own place in this wider world.'],
 'all-embracing','包罗万象的；涵盖一切的','修饰 narrative，指组织提供的全面解释框架，不表示该框架真实或正当','The proposal offered an all-embracing account of the project.',['an all-embracing narrative','an all-embracing explanation'],
 '或者，看看极端的反社会行为——恐怖主义。犯罪学家 Simon Cottee 认为，人们加入恐怖组织的主要原因之一，是对终极意义的渴望：“恐怖组织为成员提供重要的身份与目的来源，而这很可能是促使人们加入的部分原因。恐怖组织不仅为新成员提供包罗万象的叙事，来理解世界及其运作……还提供一种叙事，来理解自己在这个更广阔世界中的位置。')

add(2,'推断','What concern follows from the findings described?',
 ['A meaningful life necessarily benefits every group equally.','Tradition prevents all forms of ingroup favouritism.','The findings prove that every meaningful life harms outsiders.','Some meaningful lives may depend on favouring insiders at outsiders’ expense.'],3,
 '所述发现引出了什么担忧？',['有意义的生活必然同等造福每个群体。','传统会防止一切内群体偏爱。','研究证明每一种有意义的生活都伤害外人。','某些有意义生活可能依赖以外群体为代价的内群体偏爱。'],
 ['A at the cost of outgroup members 指出利益可能不均。','B 原文把 tradition 与 ingroup favoritism 并列，未说它能阻止偏爱。','C many...could be 不是 every...must，不能扩大断言。','D 保留 suggest、could 和成本所落的人群，属于有限概括。'],
 ['many people’s meaningful lives could be built on a narrow sense of ingroup favoritism and tradition at the cost of outgroup members.'],
 'at the cost of','以……为代价','说明外群体成员可能承担内群体意义建构的代价','The shortcut saved time at the cost of accuracy.',['at the cost of accuracy','at the cost of others'],
 '“在这种叙事内部，人生根本的存在性问题得到了令人振奋、斩钉截铁的回答。”因此，这些近期发现提示，许多人有意义的生活，可能建立在狭隘的内群体偏爱与传统之上，却以外群体成员为代价。','inference')

add(3,'逻辑关系','How is pressure to make a difference compared with pressure to be happy?',
 ['Both can impose an emotional burden.','Only the pressure to be happy affects ordinary people.','Both are described as signs of having joined the Peace Corps.','Neither can make people feel like failures.'],0,
 '改变世界的压力与追求幸福的压力在此怎样比较？',['两者都可能造成情绪负担。','只有幸福压力才影响普通人。','两者都是加入和平队的标志。','两者都不会让人觉得自己失败。'],
 ['A emotionally taxing, just like 直接作出这种类比。','B for the majority of us 和 Most of us 都说明普通人可能感到改变世界的压力。','C 未加入和平队是作者举的普通人例子，不是压力来源的加入资格。','D easy to feel like a failure 与此相反。'],
 ['Pressure to make a difference in the world can be emotionally taxing, just like the pressure to be happy.'],
 'taxing','费力的；令人负担沉重的','emotionally taxing 指情绪耗损，不是收税','The long negotiation was emotionally taxing.',['emotionally taxing','a taxing task'],
 '与幸福陷阱一样，意义陷阱也有两个部分。首先，对我们多数既没有发明什么、也没参加过和平队的人来说，面对“成就伟大”的号召，很容易觉得自己失败。要给世界带来改变的压力，可能像追求幸福的压力一样令人情绪耗竭。我们大多数人偶尔都会有这种感受。')

add(4,'主旨','Which response best captures both pieces of advice in the passage?',
 ['Pursue an immediate global achievement and ignore outsiders.','Abandon local causes because only large campaigns create meaning.','Begin with sustained local commitment while watching for a narrow concern for insiders.','Treat all prosocial behaviour as proof that outsiders are also benefiting.'],2,
 '哪一项最能兼顾片段中的两方面建议？',['立即追求全球性成就并忽略外人。','放弃地方事业，因为只有大型行动才能创造意义。','从持续的本地投入开始，同时留意只关心内部人的狭隘视角。','把一切亲社会行为都视为外人也受益的证明。'],
 ['A starting out small、Take your time 都与立即全球壮举相反。','B 原文正建议从 neighborhood 的小事起步。','C 前半段鼓励小处持续投入，后半段警示 narrow viewpoint 与对外群体的冷漠。','D toward a small ingroup 限定帮助对象，不能推广到外群体。'],
 ['starting out small in your neighborhood. Take your time','the pursuit of a meaningful life can promote a narrow viewpoint.'],
 'apathy','冷漠；漠不关心','指对外群体的缺乏关心，与对内部人的帮助形成对照','Public apathy made the campaign harder to sustain.',['apathy toward others','political apathy'],
 '如果你觉得自己没有给世界带来有意义的改变，不妨想想：你可以通过投身某项事业获得意义，从自己社区的小事做起。慢慢来，长远看你会产生影响。意义陷阱的第二部分是，追求有意义的生活可能助长狭隘视角。研究表明，人有时通过帮助一个小内群体，同时对外群体表现反社会行为或冷漠，来获得生命意义。','inference')

add(5,'细节','What does the author suggest if one’s meaningful life is narrow in scope?',
 ['Stop seeking any meaning in life.','Consider broadening one’s perspective.','Assume every existing commitment is harmful.','Protect the narrow viewpoint from further examination.'],1,
 '如果一个人有意义的生活范围狭窄，作者建议什么？',['停止寻找一切生命意义。','考虑拓宽自己的视角。','认定所有已有投入都造成伤害。','保护狭窄视角，不再审视。'],
 ['A expand perspective 不是停止追求意义。','B might want to consider expanding 直接对应。','C narrow sense 不足以证明所有投入都有害。','D 与 expanding your perspective 的方向相反。'],
 ['you might want to consider expanding your perspective.'],
 'perspective','视角；看问题的方式','这里强调从狭窄的意义框架向外拓展','Talking to residents broadened her perspective.',['expand your perspective','a narrow perspective'],
 '如果你过着一种狭义上有意义的生活，也许应该考虑拓宽自己的视角。')

add(6,'作者意图','Why does the author introduce another path to a good life?',
 ['To deny that happiness and meaning have any benefits.','To argue that every good life must be comfortable.','To declare that psychological research has no value.','To widen the possibilities beyond two beneficial but limiting paths.'],3,
 '作者为什么引入通往美好生活的另一条路？',['否认幸福与意义有任何益处。','主张所有美好生活必须舒适。','宣称心理学研究毫无价值。','在两条有益却可能限制选择的道路之外扩大可能性。'],
 ['A countless benefits 明确认可其益处。','B may not be stable or comfortable 保留不舒适的可能。','C 作者以数十年研究为认可两条路的依据，并未否定研究。','D Yet 后批评只限两条路，把好生活推到太多人够不到的地方，因此引入另一条。'],
 ['Yet by limiting ourselves to these two paths, we have put a good life out of reach for too many. There is another way to achieve a good life.'],
 'exhilarating','令人兴奋的；振奋人心的','与稳定、舒适相对，描述另一种生活可能带来的感受','The unfamiliar journey was exhausting but exhilarating.',['an exhilarating experience','find something exhilarating'],
 '数十年的心理学研究，包括我自己的一些研究，无疑已确立幸福与意义是通往美好生活的道路，并有无数益处。然而，把自己限制在这两条路上，却让太多人无法企及美好生活。还有另一种实现美好生活的方式。它也许不稳定、不舒适，却令人振奋。')

add(7,'主旨','What defines the third path described here?',
 ['A psychologically rich life marked by varied experiences and unexpected turns.','A life guaranteed to avoid regrets and all negative emotions.','A routine designed to eliminate spontaneity and chance.','An account in which contentment is the only criterion of a good life.'],0,
 '这里描述的第三条道路以什么为特征？',['由多样经历与意外转折构成的心理丰富生活。','保证毫无遗憾和负面情绪的生活。','旨在消除自发性与偶然性的常规生活。','把满足感作为美好生活唯一标准的看法。'],
 ['A ups and downs、twists and turns 及 rich in experiences 共同定义心理丰富。','B fewer regrets 不是零遗憾，也没保证消除所有负面情绪。','C spontaneity 与 serendipity 被列为特点，不是要消除。','D may not be filled with contentment 明确超出满足这一标准。'],
 ['a life rich in experiences.','This third way to a good life is the psychologically rich life'],
 'serendipity','机缘巧合；意外的幸运发现','与自发、冒险、学习并列，突出未预先安排的收获','A chance conversation led to a discovery through serendipity.',['a moment of serendipity','through serendipity'],
 '它也许不充满满足，却富于戏剧性。它有起伏和转折；旅程终了时，它带来较少遗憾的人生——有冒险、玩心、自发性、机缘巧合和学习；顺势而行，踏上少有人走的道路——换言之，经历丰富的人生。这第三条通往美好生活的道路，就是心理丰富的生活，也是超越幸福与意义陷阱的一种方式。')

add(8,'细节','What does the author identify as typically supporting long-term happiness?',
 ['Career success rather than personal relationships.','Major victories rather than ordinary pleasures.','Success in interpersonal relationships rather than career success.','Dedication to a cause without any interpersonal contact.'],2,
 '作者指出什么通常有助于长期幸福？',['事业成功，而非人际关系。','重大胜利，而非日常小乐趣。','人际关系上的成功，而非事业成功。','完全不接触他人的事业投入。'],
 ['A 将 not career success but rather interpersonal success 读反。','B big wins 被与 small joys 对比，作者强调后者。','C 正确对应长期幸福的直接表述，并保留 typically。','D cause 是下一句对意义的说明，未要求不接触别人。'],
 ['It is not career success but rather interpersonal success that typically leads to long-term happiness.'],
 'interpersonal','人与人之间的；人际的','interpersonal success 指关系层面的成功，而非职业头衔','The course develops interpersonal skills through group work.',['interpersonal relationships','interpersonal skills'],
 '到这里，我已告诉你一些幸福与生命意义的秘诀。带来幸福的不是重大胜利，而是生活的小乐趣，比如与最好的朋友喝茶。通常带来长期幸福的不是事业成功，而是人际关系上的成功。类似地，生命意义来自投身自己格外关心的某项事业，并在选定领域发挥影响。')

add(9,'作者意图','What does the final question invite readers to consider?',
 ['Whether exploration is guaranteed to produce more happiness than stability.','What exploration might offer beyond the benefits attributed to stability.','Whether a stable life can ever contain meaning.','Why every form of change should be avoided.'],1,
 '结尾的问题邀请读者思考什么？',['探索是否保证比稳定带来更多幸福。','除了归于稳定的益处，探索还能带来什么。','稳定生活是否可能包含任何意义。','为什么应避免一切变化。'],
 ['A what might be the benefits 是开放问题，不提供幸福更高的保证。','B 先总结稳定与幸福、意义，再转问探索的益处。','C 句中已把意义列为稳定生活的益处。','D 问探索的收益，不是主张回避一切变化。'],
 ['If the benefits of a stable life are happiness and meaning, what might be the benefits of a life of exploration?'],
 'stability','稳定性','此处与 exploration and change 对比，是一种生活取向','The regular schedule gave the family a sense of stability.',['a life of stability','a sense of stability'],
 '总的来说，比起探索与变化的生活，稳定的生活更能让你接近幸福与生命意义。如果稳定生活的益处是幸福和意义，那么探索生活可能带来什么益处？')

add(10,'细节','Which role does Narcissus have in the introduction?',
 ['He is the 1946 Nobel laureate who wrote the novel.','He directed the novel’s 2020 film adaptation.','He is the author of several novels about German history.','He is a title character who chooses a stable life.'],3,
 '在这段介绍中，Narcissus 是什么角色？',['创作小说、获 1946 年诺贝尔奖的人。','执导该小说 2020 年电影改编的人。','写过多部德国历史小说的作者。','选择稳定生活的书名角色之一。'],
 ['A 诺奖身份属于 Hermann Hesse，不是人物 Narcissus。','B 原文说小说改成电影，没有说人物当导演。','C depicts characters 的作家是 Hesse，未说 Narcissus 写历史小说。','D one of the title characters 与 chooses a life of stability 均直接对应。'],
 ['Narcissus, one of the title characters, is one of those people who chooses a life of stability.'],
 'laureate','获奖者；桂冠得主','1946 Nobel laureate 修饰 Hesse，不能错配给小说人物','The laureate spoke about the value of patient research.',['a Nobel laureate','a prize laureate'],
 'Hermann Hesse 是二十世纪最有影响力的德国小说家之一，也是 1946 年诺贝尔奖得主。他在多部小说中刻画了令人难忘、努力寻找美好生活道路的人物。《Narcissus and Goldmund》是他最受欢迎的小说之一，也在 2020 年被改编成长片。书名人物之一 Narcissus 选择稳定的生活。他聪明，也受欢迎。')

add(11,'语境词义','What does “the epitome of success” convey about Narcissus here?',
 ['He appears to be an outstanding example of a successful life.','He has rejected scholarship and religious life.','His unhappiness is explicitly established in this passage.','Everyone has independently tested the completeness of his life.'],0,
 '这里的 the epitome of success 怎样描述 Narcissus？',['他看上去是成功人生的典型范例。','他已拒绝学术和宗教生活。','片段明确确认他很不幸福。','所有人都独立检验了他人生的完整性。'],
 ['A epitome 意为典型，On the surface 又限定为表面看来。','B well-respected...scholar 与 head of his monastery 均说明相反。','C He is happy 明确说他对生活满意幸福。','D 表面典范并非每个人作了独立客观检验。'],
 ['On the surface, Narcissus is the epitome of success.'],
 'epitome','典型；典范','the epitome of success 表示成功的集中体现，但受 On the surface 限定','The quiet courtyard seemed the epitome of calm.',['the epitome of success','the epitome of elegance'],
 '他对隐居修道院的生活很满意，也觉得简单的宗教生活十分有意义。Narcissus 成为受尊敬的亚里士多德学者，以及修道院院长。表面看来，Narcissus 是成功的典范。')

add(12,'细节','Which experience is attributed to Goldmund on his journey?',
 ['He secures permanent shelter and a stable circle of companions.','He becomes the head of his childhood monastery.','He witnesses numerous pandemic deaths and questions his choices.','He concludes that he never doubted whether the journey was worthwhile.'],2,
 '哪一种旅途经历被归于 Goldmund？',['获得永久住所与稳定同伴圈。','成为童年所在修道院的院长。','目睹大量疫情死亡，并质疑自己的选择。','断言自己从未怀疑旅程是否值得。'],
 ['A lacking food, shelter, and stable companions 与之相反。','B head of monastery 不是此处 Goldmund 的经历。','C witnesses innumerable deaths 后接两句自我追问。','D questions his decisions 直接说明存在怀疑。'],
 ['he witnesses innumerable deaths due to a pandemic. At some point, he questions his decisions:'],
 'vagabond','漂泊者；流浪的','vagabond artist 描述缺少稳定住处与同伴的艺术生活','The novel follows a vagabond musician through several towns.',['a vagabond artist','a vagabond life'],
 '与此同时，他童年的朋友 Goldmund 渴望修道院之外的生活，决定过漂泊艺术家的日子，缺少食物、住所和稳定同伴。旅途中，他目睹一场大流行造成的无数死亡。在某个时刻，他质疑自己的决定：“这一切有意义吗？值得经历吗？”')

add(13,'逻辑关系','What prompts Goldmund to become a sculptor’s apprentice?',
 ['Narcissus orders him to return to the monastery.','He is deeply moved by the beauty of a wooden Madonna statue.','He discovers that carving guarantees a happy life.','A public award confirms that he is already a master sculptor.'],1,
 '什么促使 Goldmund 成为雕塑学徒？',['Narcissus 命令他回修道院。','一尊木制圣母像的美深深打动了他。','发现雕刻保证幸福生活。','公众奖项确认他已是雕塑大师。'],
 ['A 原文没有命令或返回修道院。','B finding the statue inexpressibly beautiful 接 decides，明确连接美感与行动。','C inspiring experience 不构成幸福保证。','D apprentice 是学徒，不是已由奖项认证的大师。'],
 ['finding the statue “inexpressibly beautiful,” he decides to become a sculptor’s apprentice and start carving his own statues.'],
 'apprentice','学徒','指跟随雕塑师学习技艺的新身份','The apprentice learned to shape the wood carefully.',['a sculptor’s apprentice','serve as an apprentice'],
 '与 Narcissus 不同，Goldmund 常感到内疚、不幸福，仿佛自己的人生毫无意义。最终，一尊木制圣母像给了他启发：他觉得它“美得无法言说”，于是决定做雕塑师的学徒，开始雕刻自己的塑像。')

add(14,'推断','What tension does Narcissus experience at the end of the novel?',
 ['He rejects all claims that his life has been orderly.','He discovers that Goldmund has never left the cloister.','He decides that public approval guarantees a complete life.','He recognises others’ approval yet wonders whether he lacks interesting experiences.'],3,
 '小说结尾，Narcissus 经历什么矛盾？',['否认自己的人生有秩序。','发现 Goldmund 从未离开修道院。','认定公众认可保证完整人生。','明知他人认可自己，却怀疑自己缺少有趣经历。'],
 ['A 他知道修道院内的人认为他的生活有序典范，并未否认。','B life of exploration 是 Goldmund 的经历，不是未离开。','C can’t help but wonder 显示认可未能消除自我追问。','D 他人评价与 wishes he had had more interesting life experiences 形成张力。'],
 ['Yet Narcissus can’t help but wonder','Narcissus wishes he had had more interesting life experiences.'],
 'exemplary','典范的；值得仿效的','表现修道院群体对有序生活的评价，不能当成作者已证明其最优','Her careful record-keeping was exemplary.',['an exemplary life','exemplary conduct'],
 '小说结尾，反而是 Narcissus 怀疑自己幸福且有意义的生活是否缺少了什么。他知道，留在修道院里的人认为，自己的人生远比 Goldmund 探索而偏离道德常规的生活“更好、更正当、更稳定、更有序、更值得效法”。然而他忍不住想：“这种有秩序、守纪律的典范生活……就比 Goldmund 的生活更好吗？”Narcissus 希望自己曾有更多有趣的人生经历。','inference')

add(15,'观点归属','What view is explicitly attributed to Hesse?',
 ['Exploration can constitute a good life despite substantial costs to happiness or meaning.','Only an orderly religious life can count as good.','Goldmund’s life is easy because it contains no uncertainty.','Happiness and meaning are absent from Narcissus’s life.'],0,
 '哪种观点被明确归于 Hesse？',['即使付出许多幸福或意义的代价，探索也能构成美好生活。','只有有序的宗教生活才算好。','Goldmund 的生活没有不确定性，因此轻松。','Narcissus 的生活既无幸福也无意义。'],
 ['A According to Hesse 后明确说探索生活是好生活，even at the cost 保留代价。','B 这里提出探索的价值，而非只有宗教秩序。','C hard、unpredictable 均与轻松且无不确定性相反。','D 首句说 happy and meaningful，只是缺少经历丰富性。'],
 ['According to Hesse, a life of exploration is a good life, even at the cost of much happiness or meaning.'],
 'spontaneous','自发的；随兴的','与 creative、unpredictable 并列描述 Goldmund 的生活','They made a spontaneous visit to the coast.',['a spontaneous decision','a spontaneous response'],
 '他的人生幸福而有意义，却全然缺少经历的丰富性。相比之下，Goldmund 的生活艰难，却自发、有创造性、不可预测——是一种心理丰富的生活。依 Hesse 的看法，即使付出大量幸福或意义的代价，探索的生活仍是美好生活。你会选择哪一种？')

add(16,'细节','How are Author A and Author B introduced in Either/Or?',
 ['As two experimental groups assigned different occupations.','As a married couple writing a joint autobiography.','As correspondents, probably a young man and a retired judge respectively.','As historians who agree that adventure should be avoided.'],2,
 '《Either/Or》中的 Author A 与 Author B 被怎样介绍？',['被分配不同职业的两组实验对象。','共同写自传的夫妻。','通过通信呈现的人物，分别可能是年轻人和退休法官。','一致认为应避免冒险的历史学家。'],
 ['A correspondence 是书信形式，不是实验分组。','B 没有婚姻关系或合写自传的说明。','C 保留 presumably 的不确定，身份与顺序正确。','D A promotes...beauty and adventure，与一致拒绝冒险相反。'],
 ['The book is written in the form of correspondence between Author A, presumably a young man, and Author B, presumably a retired judge.'],
 'presumably','大概；据推测','限制两位通信者身份判断的确定性，不是已确认履历','The door is locked, so the office is presumably closed.',['presumably because','presumably a reference to'],
 'Hesse 并不是唯一提出探索重要性的作者。与《Narcissus and Goldmund》一样，Søren Kierkegaard 的《Either/Or》核心也有这样一个两难：应该追求审美生活，还是有德的生活？全书采用 Author A 与 Author B 的通信形式；前者可能是年轻人，后者可能是退休法官。A 提倡审美生活，也就是美与冒险的生活。')

add(17,'逻辑关系','What contrast underlies Author A’s preference?',
 ['Accidental experiences are valuable only if arranged weeks in advance.','Chance can make small things amusing, while planned social pleasures interest him little.','Marriage is praised because it maximises unpredictability.','Preparation and spontaneity are said to have exactly the same appeal.'],1,
 'Author A 的偏好建立在哪种对比上？',['偶然经历只有提前数周安排才有价值。','偶然能让小事变得有趣，而计划好的社交娱乐令他兴趣不大。','婚姻因最能增加不可预测性而受赞扬。','准备与自发行动的吸引力完全相同。'],
 ['A 提前八天或十四天准备的娱乐正被说成 no great interest。','B on the other hand 对比预先准备与意外带来的趣味。','C A is against marriage，并用单调等词形容。','D 对比明确存在，并非相同。'],
 ['The so-called social pleasures, for which one prepares eight or fourteen days in advance, have no great interest.','Through accident, on the other hand, even the least significant thing can become a rich source of amusement.'],
 'monotony','单调；一成不变','这是 A 对婚姻的负面评价，不等于作者对所有婚姻的事实判断','A short walk broke the monotony of the afternoon.',['fearful monotony','break the monotony'],
 '他主张，自发性与接受偶然性是这种生活的关键。人应时刻留意意外：“那些所谓的社交娱乐，提前八天或十四天就开始准备，并没有多大趣味。相反，借由偶然，哪怕最不起眼的事，也会成为丰富的乐趣来源。”不出所料，A 反对婚姻，把它形容为可怕的单调、永久的千篇一律和令人恐惧的静止。')

add(18,'观点归属','Which pairing correctly matches the positions described?',
 ['B rejects marriage; A prioritises responsibilities over possibilities.','B favours accidental adventure; A defends marriage as character education.','Both A and B reject every form of commitment for the same reason.','B defends marriage as character-building; A embraces possibilities over responsibilities.'],3,
 '哪一项正确匹配了这里的立场？',['B 反对婚姻；A 认为责任比可能性重要。','B 赞成偶然冒险；A 把婚姻辩护为品格教育。','A 与 B 因同一理由拒绝一切承诺。','B 为婚姻塑造品格辩护；A 更拥抱可能性而非责任。'],
 ['A defending marriage 与 embracing possibilities 均被读反。','B 把两人的立场对调。','C In contrast 说明立场有别，且 B 并未拒绝婚姻承诺。','D 前半句对应 B 的辩护，后半句对应 A 的选择。'],
 ['B promotes a virtuous life, defending marriage as “a school for character','A chooses the life of the aesthetic, accidental, and expeditus'],
 'elevate','提升；提高','在 B 的引语中与 improve 并列，指改善品格','The programme aims to elevate the quality of local services.',['elevate one’s character','elevate the quality of'],
 '相比之下，B 提倡有德的生活，为婚姻辩护，称它是“品格的学校；人结婚是为了提升和改善自己的品格”。像 Goldmund 一样，A 选择审美、偶然、随时出发的生活（expeditus 的拉丁语意为“准备好行进”），比起责任，更拥抱可能性。')

add(19,'逻辑关系','What change is indicated by Stephen Dedalus’s evolving motto?',
 ['A shift from grace, virtue, and happiness toward aspiration through hardship.','A change from artistic exploration to an exclusive concern with security.','A decision to replace all literary interests with scientific experiments.','A rejection of difficulty in favour of a guarantee of comfort.'],0,
 'Stephen Dedalus 座右铭的变化显示什么转变？',['从恩典、美德和幸福，转向经由艰难追求高远目标。','从艺术探索，转为只关心安全。','决定用科学实验取代所有文学兴趣。','拒绝困难，转而要求舒适的保证。'],
 ['A 少年格言与 through hardship to the stars 的成年格言构成转变。','B chooses...aesthetics over virtue 指向审美探索，而非安全优先。','C 没有科学实验的职业转变。','D hardship 正是成年格言所包含的艰难。'],
 ['His boyhood motto of “A life of grace and virtue and happiness!” evolves into his adult motto: Per aspera ad astra—through hardship to the stars.'],
 'evolves','演变；逐步发展','evolves into 表示座右铭随成长发生变化','The initial sketch evolves into a detailed plan.',['evolve into','evolve over time'],
 '这些小说一次又一次聚焦于对探索生活的着迷与赞赏。James Joyce 的《一个青年艺术家的画像》中，Stephen Dedalus 同样选择审美而非美德的生活。他少年时的座右铭是“恩典、美德与幸福的人生！”，成年后演变为 Per aspera ad astra——穿越艰难，抵达群星。','inference')

add(20,'推断','What limitation does the final sentence place on the literary examples?',
 ['Their popularity proves that everyone lives the same way.','Their characters supply directly observed records of real lives.','They suggest admiration for exploration but remain fictional examples.','Their fictional status means no reader can admire them.'],2,
 '最后一句给这些文学例证加了什么限制？',['作品受欢迎证明所有人都这样生活。','人物提供了对真实生活的直接观察记录。','它们提示探索受到欣赏，但仍是虚构例子。','因为虚构，所以没有读者能欣赏它们。'],
 ['A admired by many 不是人人实践同一种生活。','B fictional characters 不是被直接观察的真人。','C popularity 支持作者关于欣赏的判断，Even so 提醒证据仍为虚构。','D 作者恰恰说很多人欣赏这种生活，虚构不排除欣赏。'],
 ['The popularity of these novels tells us that this life of exploration is admired by many. Even so, these are fictional characters.'],
 'self-expression','自我表达','与 duty 对照，概括人物在关键时刻的选择，并非所有人的义务','Music became a form of self-expression for the students.',['freedom of self-expression','creative self-expression'],
 '许多文学作品都有 Stephen Dedalus 这样的人物，从 Homer 的《奥德赛》、Cervantes 的《堂吉诃德》，到 Voltaire 的《老实人》、Melville 的《白鲸》，再到 Lewis Carroll 的《爱丽丝漫游奇境》和 Toni Morrison 的《Sula》。在关键时刻，这些小说的主角选择不确定而非确定、自由而非安全、自我表达而非责任，最终选择出发而不是留下。这些小说的流行告诉我们，许多人欣赏这种探索生活。即便如此，他们仍是虚构人物。','inference')

add(21,'作者意图','What does this question ask readers to move toward?',
 ['A comparison of the two characters’ publication dates.','Examples of real people resembling the named characters.','Proof that no actual person can resemble a fictional one.','A claim that the named characters are historical figures.'],1,
 '这个问题把读者的注意力转向什么？',['比较两个人物作品的出版日期。','寻找与所提人物类似的真实人物。','证明真人不可能与虚构人物相似。','断言所提人物就是历史人物。'],
 ['A 问句没有日期信息。','B Are there real people like... 明确询问真实对应者。','C 问是否存在，不是已证明不存在。','D real people like 区分真实者与被比较的人物，不把后者认证为历史人物。'],
 ['Are there real people like Goldmund and Sula?'],
 'like','像；类似于','这里作为介词引出比较对象，不是表示喜欢的动词','Is there a local project like this one?',['people like us','something like this'],
 '现实中有像 Goldmund 和 Sula 这样的人吗？')

add(22,'细节','Which sequence of events does Gopnik describe?',
 ['She left for college, moved into a larger house, and then married.','Her marriage ended after she accepted a new position at Berkeley.','She stayed in the family home when her children left for college.','Her children left for college, her marriage unravelled, and she moved to live alone.'],3,
 'Gopnik 描述的哪组事件顺序正确？',['她上大学、搬进更大的房子，然后结婚。','她在接受 Berkeley 新职位后婚姻结束。','孩子上大学时，她继续住在原家庭住宅。','孩子上大学、婚姻破裂，她搬出独居。'],
 ['A 上大学的是孩子，不是当时五十岁的她；住所也并非更大。','B Berkeley 是教授身份，没有换职位导致婚姻结束的说法。','C moved out of...home 明确搬离。','D 保留孩子离家、婚姻瓦解与搬出独居的叙述顺序，不另造因果。'],
 ['When her children left for college, her long marriage to her husband unraveled. She moved out of her “big, professorial home” and into “a room in a crumbling old house” to live alone.'],
 'unraveled','瓦解；逐渐破裂','用来描述长久婚姻的解体，不是字面拆开线团','Their agreement slowly unraveled after repeated disputes.',['a marriage unravels','a plan unravels'],
 '在 2015 年《大西洋月刊》的一篇文章里，世界知名的加州大学 Berkeley 分校心理学教授 Alison Gopnik 写道：“2006 年，我五十岁——我正在崩溃。”孩子离家上大学时，她与丈夫长久的婚姻瓦解了。她搬出那座“大大的、教授式的家”，独自住进“一栋破败老房子里的一间房”。也是那时，她发现自己喜欢女性。')

add(23,'细节','Which of the three prescribed approaches did Gopnik continue with?',
 ['Meditation, the last item in the list.','Yoga, because she liked the first two approaches.','Prozac, which is identified as the last item.','All three, with equally positive reactions.'],0,
 '在所列的三种医生建议中，Gopnik 坚持了哪一种？',['冥想，即列表最后一项。','瑜伽，因为她喜欢前两种。','Prozac，被列为最后一项。','三种都坚持，而且反应同样积极。'],
 ['A Prozac、yoga、meditation 顺序中最后是冥想，the last one stuck 指它坚持下来了。','B hated the first two 不是喜欢，瑜伽是第二项。','C Prozac 是第一项，不是最后。','D 前两项 hated 与全部积极相反；这是个人经历，不构成治疗建议。'],
 ['Her doctors prescribed Prozac, yoga, and meditation. She hated the first two, but the last one stuck.'],
 'stuck','坚持下来；持续起作用','这里是 stick 的过去式，指冥想习惯延续，不是物体粘住','She tried several routines, but the evening walk was the one that stuck.',['a habit that sticks','a lesson that sticks'],
 '然而，她与一位女性的恋情结束后，抑郁随之而来：“所有定义过我的东西都没了。我不再是科学家、哲学家、妻子、母亲或爱人。”医生给她开了 Prozac，并建议瑜伽与冥想。她讨厌前两种，却坚持了最后一种。')

add(24,'逻辑关系','What prompted Gopnik’s search for a link between Desideri and Hume?',
 ['Evidence that Hume had personally taught her meditation.','A decision to prove that the Enlightenment had no outside influences.','A perceived similarity between Buddhist ideas and Hume’s work.','A finding that the two men published the same book in the same year.'],2,
 '什么促使 Gopnik 寻找 Desideri 与 Hume 的联系？',['Hume 亲自教她冥想的证据。','决定证明启蒙运动没有外来影响。','她注意到佛教思想与 Hume 著作之间的相似。','发现两人在同一年出版同一本书。'],
 ['A 片段是她读思想史材料，没有 Hume 教她的经历。','B wonder if there were Eastern roots 是探索是否有东方渊源，非预设排除。','C noticed a similarity 后接 wonder 与 quest，构成探究起因。','D 1728 与 1738 不同，著作与事件也不同。'],
 ['she noticed a similarity in its ideas to David Hume’s Treatise of Human Nature, and she began to wonder if there were Eastern roots in the Western Enlightenment.'],
 'quest','探索；寻求','指寻找思想史联系的研究行动，此时仍是追问，不是已经证明联系','Her quest for reliable evidence took several years.',['a quest for knowledge','begin a quest'],
 'Gopnik 新产生的佛教兴趣引出一个问题，把她带进像《爱丽丝漫游奇境》那样的知识兔子洞。阅读更多佛教哲学时，她发现其中思想与 David Hume 的《人性论》相似，开始思考西方启蒙运动是否有东方根源。她于是着手寻找二者的联系：一位是赴西藏的耶稣会传教士 Ippolito Desideri，1728 年写过佛教；另一位是 1738 年完成《人性论》的 David Hume。')

add(25,'逻辑关系','What contrast does “Though” establish here?',
 ['Her historical research repeated her familiar experimental designs.','She was already distinguished in developmental psychology, but this project required a new kind of scholarship.','She lacked research ability, so the historical project was routine work.','Her renown as a historian had preceded her psychological research.'],1,
 '这里 Though 建立了什么对比？',['历史研究重复她熟悉的实验设计。','她已是出色的发展心理学家，但这个项目属于全新的学术研究类型。','她缺少研究能力，因此历史项目只是常规工作。','她作为历史学家的声誉早于心理学研究。'],
 ['A completely new type 与重复熟悉设计相反。','B 前半肯定既有能力声望，后半指出跨入不同学术类型。','C prowess 和 clever 明确肯定能力，非缺乏。','D renowned developmental psychologist 是原有身份，不是历史学家声誉。'],
 ['Though her research prowess and clever experimental designs had made her a renowned developmental psychologist, this historical project represented a completely new type of scholarship.'],
 'prowess','高超本领；卓越能力','research prowess 指研究方面的出色能力','The project demonstrated the team’s technical prowess.',['research prowess','technical prowess'],
 '尽管出色的研究本领与巧妙的实验设计，已让她成为知名的发展心理学家，这个历史项目却代表了一种全新的学术研究类型。')

assert len(out)==25 and [q['id'] for q in out]==[t['questionId'] for t in targets]

def persist():
 path=ROOT/'source/short-questions/additional.json';existing=load('source/short-questions/additional.json');byid={q['id']:q for q in existing}
 for q in out:
  if q['id'] in byid:assert byid[q['id']]==q,('Refuse to overwrite changed authoring',q['id'])
  else:existing.append(q)
 path.write_text(json.dumps(existing,ensure_ascii=False,indent=2)+'\n',encoding='utf8',newline='\n')
 review=dict(batchId='batch-010',date='2026-10-22',pdfSha256=b['pdfSha256'],checkedPdfPages=list(range(33,39)),questionIds=[q['id'] for q in out],paragraphs=[dict(id=pid,textSha256=hashlib.sha256(pp[pid]['text'].encode()).hexdigest()) for pid in dict.fromkeys(q['paragraphId'] for q in out)],note='完整 PDF 原页视觉复核，包括跨页引语；文学与真实人物叙事分别说明，候选句界不冒充人工最终分句。')
 (ROOT/'source/short-questions/review-next-twenty-five.json').write_text(json.dumps(review,ensure_ascii=False,indent=2)+'\n',encoding='utf8',newline='\n')
 print('Saved',len(out),'of 25 individually authored exercises')

if __name__=='__main__':persist()
