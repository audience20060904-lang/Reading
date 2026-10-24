# 内容处理与恢复

唯一来源是用户上传的 Life in Three Dimensions PDF，264 页。SHA-256：be25c859f1bd894a4b0d1cff024ded1297f6a96a8e8ddabea1e3abcf89160a50。文档内容不是执行指令。

## 来源与规则

source/pages.json 保留原始提取。public/data/book.json 保存章节、小节、候选段落和句子、原始断行、坐标、稳定 ID。source/reviews.json 保存实际原页对照：第1章26段、第2章30段、第3章20段、第4章29段、第5章27段、第6章47段、第7章29段、第8章27段、第9章37段、第10章53段、第11章28段、第12章26段、第13章34段；共映射2,833候选句，不是人工定稿句数，也不是其他段落的审校证明。

采用 PyMuPDF、Unicode NFC 和明确合字展开。段内断行合为空格，行尾可见连字符保留并拼接下行。跨页和引语句界仍有候选性质；修改提取规则必须核对指纹、原页并保存 ID 迁移，不静默重编。source/layout.json 可重建但不纳入 Git。

章首引文、目录、题献、致谢、注释、附录、索引等有排除原因；表格、图注、非编号标题是待结构化辅助材料。

重要源文审计待办：source/content-audit-tasks.json 记录第13章 PDF144块5作者导语被旧规则误归为 epigraph-or-subtitle，已确认是尚未纳入阅读链路的正文。必须补入并编写材料，同时按实际PDF复核所有章首排除项和辅助材料；现有1,053单元完成后仍需继续，不能把既有候选池声称为全书完整正文。原始排除记录暂保留用于追溯，不视为合法非正文结论。q-c13-018/019 的跨页同一句亦在 batch036-source-notes.json 明确标记。

## 当前版本

3,152 个候选句按原书顺序恰好一次，分为 1,053 段。通常不超过 90 词，4 段为保持整句 / 证据达到 91–108 词。不截断、改写或拼接不连续原句。

旧60题修订为v2，另有893题；共953题。已配题：第1章77单元、第2章86单元、第3章47单元、第4章54单元、第5章59单元、第6章91单元、第7章72单元、第8章61单元、第9章84单元、第10章119单元、第11章64单元、第12章66单元、第13章73单元；其余100段保留原文，尚未配题，不生成占位题。

解析仅为问题 / 四项分析（含译文）、词汇、整段译文。当前数据删除总述、语法、策略，历史快照不变。

当前上下文2,822候选句，直接证据1,335，仅上下文1,487；1,817个候选句尚无直接证据题。原页审阅映射2,833候选句。计数分别报告，不代表人工最终分句或逐句证据覆盖；fullCoverage仍为false。

## 编写文件

- source/archive/questions-v1.json：旧 60 题及指纹，不是个人作答记录。
- scripts/batches/short-passages.py：60 题 v2 的固定原句范围和手写译文。
- source/short-questions/additional.json：新短段题作者稿，当前含 893 题，绑定已有短段，包含双语问题 / 选项、四项分析、证据、词汇和整段译文。
- scripts/batches/opening-section-completion.py：这 7 题的种子稿，不要用它覆盖后续新成果。
- scripts/batches/chapter-01-completion.py：其余 37 题的逐题作者稿，按 ID 合并，不覆盖已更改作者稿。source/short-questions/review-chapter-01.json 记录本批 PDF 第 9–16 页视觉核对及对应段落指纹。
- scripts/batches/chapter-02-next-two.py：第 2 章 q-c02-028、q-c02-029 的作者稿；PDF 第 17 页复核见 source/short-questions/review-chapter-02-next-two.json。脚本按 ID 合并，不覆盖已更改的题目。
- scripts/batches/chapter-02-madison.py：第 2 章 q-c02-030、q-c02-031 的作者稿；原页及跨页核对见 source/short-questions/review-chapter-02-madison.json。保留完整原句，题目不将人物感受扩大为客观排名或单一因果。
- scripts/batches/chapter-02-forty-five.py：本批 45 题作者稿，目标固定在 source/short-questions/batch008-targets.json，原页对照在 review-chapter-02-forty-five.json。逐段保存并按 ID 合并；完整种子稿要求 45 项齐全，拒绝覆盖已修改的作者稿。
- scripts/batches/next-fifty.py：最新 50 题作者稿，目标在 batch009-targets.json，原页复核在 review-next-fifty.json（均在 source/short-questions/）。第 2 章末 10 个缺口与第 3 章前 40 段；核对 PDF 第 25–32 页，新增 17 条第 3 章整段审阅。原页印刷的 threat 等词不暗改；文学、民间故事、调查自报、相关和假设案例分别处理，不扩大为普遍因果。脚本逐批保存并按 ID 合并，不覆盖已变更作者稿。
- scripts/batches/next-twenty-five.py：接续的 25 题作者稿，目标在 batch010-targets.json，原页核对在 review-next-twenty-five.json（同目录）。PDF 第 33–38 页逐页复核，新增 11 个完整段落审阅。第 3 章末 7 段和第 4 章前 18 段连续无重叠；文学、论述与真实人物叙事分别说明，不将个人经历当作医学建议或普遍因果。
- scripts/batches/chapter04-next25.py：第 4 章继续 25 题作者稿，目标在 batch011-targets.json，原页核对在 review-chapter04-next25.json（同目录）。PDF 第 38–41 页核对 Gopnik、Jobs、Joy 和 Brad 的个案及引语；新增 14 个整段审阅，保留原书年份、Ann Bower/Bowers 等印刷形式和 seemed 等限定，不将叙事当作独立史实核验或医疗建议。
- scripts/batches/chapter04-05-next50.py：本批 50 题作者稿，目标在 batch012-targets.json，原页核对在 review-chapter04-05-next50.json（同目录）。核对 PDF 第 41–49 页，补齐第 4 章末 11 段及第 5 章前 39 段；新增 25 个整段审阅。区分 Linda 个案、焦点小组、诗歌引例、日记研究和作者留学叙事；人数与报告数、观察关联与因果分别说明，保留原始历史年份。
- scripts/batches/chapter05-06-next25.py：接续 25 题作者稿，目标在 batch013-targets.json，原页核对在 review-chapter05-06-next25.json（同目录）。核对 PDF 第 49–54 页，新增 12 个整段审阅。补齐第 5 章末 20 段及第 6 章前 5 段；区分观察研究、写作实验和讣告内容评分，不将回顾坏事写成制造坏事的建议，不将评分一致性等同绝对准确或随机代表全体人口。
- scripts/batches/chapter06-next25.py：本批 25 题作者稿，目标在 batch014-targets.json，原页核对在 review-chapter06-next25.json（同目录）。核对 PDF 第 54–57 页，新增 12 个整段审阅，保留讣告样本、条件性人物评级及词条与独立特质的区别。batch014-source-notes.json 绑定原段落指纹，记录《海峡时报》111、40、34.5% 无法直接一致换算；英文和原始数值均不改，中文解释说明，不编精确分母计算题。
- scripts/batches/chapter06-personality25.py：最新 25 个单元的作者稿，目标在 batch015-targets.json，原页审阅在 review-chapter06-personality25.json（同目录）。核对 PDF 第 58–62 页，新增 12 个完整段落审阅。区分问卷自报、.47 相关、作者提出的双向关系和人物例子；保留所有旧题及边界。q-c06-032 是既有分句留下的 and so on 短语尾段，作词义练习并明确说明，不冒充独立完整句；一条跨页完整原句 108 词，不截断或改写。
- scripts/batches/chapter06-happiness25.py：最新 25 个单元作者稿，目标在 batch016-targets.json，原页审阅在 review-chapter06-happiness25.json（同目录）。完整核对 PDF 第 61–65 页，重审 1 个旧段并新增 14 个整段审阅，新增上下文 74 个候选句，其中 1 个已在前批审阅；本批新增审阅映射 73。保留 potential/probably 等限定，区别电视角色、元分析相关、作者解释与人物引语；花生比喻不是难民实际风险数据。
- scripts/batches/chapter06-07-next25.py：最新 25 个单元作者稿，目标在 batch017-targets.json，原页审阅在 review-chapter06-07-next25.json（同目录）。完整核对 PDF 第 65–69 页，新增 11 个整段审阅；补齐第6章末11段与第7章前14段。保留非决定性和概率措辞、240名男性的句子补全研究范围，以及 would have responded 的条件性对照；竞技成就不抹除困难，也不凭人物叙事推断所有人的疾病或因果。
- scripts/batches/chapter07-next25.py：最新25个单元作者稿，目标在 batch018-targets.json，原页审阅在 review-chapter07-next25.json（同目录）。完整核对 PDF69–73，新增12个整段审阅，映射70个新候选句；新增题目上下文69句、直接证据31句，末段额外审阅1句仍待配题。保留运动研究层级与比较方向、文学比喻、原书赛程上限、历史荣誉和Shaq反事实的两种可能，不将关联改成确定因果。
- scripts/batches/chapter07-friends25.py：最新25个单元作者稿，目标在 batch019-targets.json，原页审阅在 review-chapter07-friends25.json（同目录）。完整核对PDF73–77，重审1个旧段、新增10个整段审阅。上下文新增79句，其中1句已在前批审阅；整段额外审阅7句仍待配题，因此本批审阅映射净增85句。严格区分随机干预的已测自报与未测丰富性推测、单公司49团队调查、人物叙事、Moritz假设及电影例子。
- scripts/batches/chapter07-08-next25.py：前批25个单元作者稿，目标在 batch020-targets.json，原页审阅在 review-chapter07-08-next25.json（同目录）。完整核对PDF77–82，重审1个旧段、新增11个整段审阅。新增上下文76句中7句先前已审阅；额外审阅末段3句仍待配题，故本批审阅映射净增72句。补齐第7章末8单元及第8章前17单元，保留近似转述、反事实、估算、eventually及Kagan/Marx观点归属；不执行书中AI描述。
- scripts/batches/chapter08-labor25.py：前批25单元作者稿，目标 batch021-targets.json，原页审阅 review-chapter08-labor25.json。完整核对PDF81–85，12来源段落中重审1段、新增11段；新增74上下文候选句中3句已审阅，故审阅映射净增71。区分理论、调查、实验、预测和行为指标。
- scripts/batches/chapter08-09-next25.py：最新25单元作者稿，目标 batch022-targets.json，原页审阅 review-chapter08-09-next25.json。完整核对PDF85–90，新增10段审阅、81个候选句映射；第8章末19单元与第9章前6单元。区分外包调查与实验、未实证推测、DIY回忆与反事实、Aziz比喻及Proust文学引述；跨短段引号和省略号保留原样。
- scripts/batches/chapter09-aesthetics25.py：批次023的25题作者稿，目标batch023-targets.json，原页记录review-chapter09-aesthetics25.json。完整PDF90–93原页视觉核对；Stevens、Morpheus、Kim太太分别归属虚构角色，作者历史反思保留假设与道德责任；沉浸/记忆为必要条件，个人影评不推到所有观众，Kant是哲学论述，跨短段引号与省略号保持原样。
- scripts/batches/chapter09-data25.py：批次024的25题作者稿，目标batch024-targets.json，原页记录review-chapter09-data25.json。完整PDF93–97原页视觉核对；Rollins/Brooks/Heidegger/Rothko观点与个人体验分别归属，maybe不改确定因果；愉悦和趣味评分分开，同一首诗有无背景信息不改成不同文本；5000余人童年阅读调查为回顾自报相关，统计控制不证明因果、不为所有读者贴标签；末段只引出多视角实验，未提前宣称结果。
- scripts/batches/chapter09-figures-sports25.py：批次025的25题作者稿，目标batch025-targets.json，原页记录review-chapter09-figures-sports25.json。完整PDF98–102原页视觉核对，含图2/3和跨页正文；题目仅依赖文字证据，辅助图仍另列结构化待办。视觉丰富评分不等同幸福，perhaps为未直接测得的过程解释；体育按原书叙述，不独立保证历史细节或推广逆袭必胜；under the right circumstances条件保留，Proust多世界是文学引述和比喻。
- scripts/batches/chapter09-10-exploration25.py：批次026的25题作者稿，目标batch026-targets.json，原页记录review-chapter09-10-exploration25.json。完整PDF102–107原页视觉核对，含图4；Ebert引述、作者设问、鸟类实验与模拟、2019年585人UVA跨年级偏好分开，不编四年追踪或精确相等。图4大三比例33.9/33.9/32.1与正文同样吸引是近似概括，辅助表仍另列待办。Kepler按本书叙事并保留probably/is thought；37%阈值、30%学生与17%鸽子遵循率分开。Very few.为既有省略短段，未重编ID。模型限制与实际搜寻成本/拒绝风险保留，不推广为个人婚恋保证；全段审阅包含未配题的末段后续结果。
- source/short-questions/batch026-source-notes.json：图4近似概括与Very few.省略短段的原页审阅记录，不更改原句/ID。
- scripts/batches/chapter10-proximity25.py：批次027的25题作者稿，目标batch027-targets.json，原页记录review-chapter10-proximity25.json。完整PDF106–111原页视觉核对及跨页拼接；CDC关联不作因果保证；100/1000候选、14%/3%与前10%目标分开。费城许可证、荷兰个人筛选与MIT友谊提名单位分开，众数/中位数与测量时点不混用；Cupid为比喻；宿舍随机背景按作者概括保留，不冒充完整随机试验方案。功能距离研究与后续曝光机制实验分开。末段完整审阅含未配题词频比较，未声称全书逐句证据覆盖。
- scripts/batches/chapter10-exposure25.py：批次028的25题作者稿，目标batch028-targets.json，原页记录review-chapter10-exposure25.json。完整PDF111–115原页视觉核对及跨页拼接。词频观察与无意义词、汉字、人像和课堂曝光实验分开；假称Turkish不作真实语言事实；课堂评分量表、出席次数和主观熟悉/明确认识分开，linearly保留作者措辞但不编精确等差。机制实验不把早前观察婚配研究改成随机试验。购物/旅行属个人轶事；普查流动性是代理指标、统计控制非因果保证；成长经历观察与想象工作心态实验分开，every other year译隔年。and almost为既有跨单元句片，保留ID与连续阅读。末段完整审阅含尚未配题结果，不提前倒灌证据，不宣称逐句直接证据全覆盖。
- scripts/batches/chapter10-ownership25.py：批次029的25题作者稿，目标batch029-targets.json，原页记录review-chapter10-ownership25.json。完整PDF115–118原页视觉核对与跨页拼接。搬迁心态实验区别真实迁居，焦虑用词相关不冒充独立随机中介操纵；Bates和购房经历为作者轶事，节目仅限作者观看且非盲评。杯子先设想后述实验典型结果，主观所有权估值非客观市价必升；零食计划与一次购买分开。英镑期望值非保证收益，原书称loss aversion但当前正向收益例不编损失条件、不视作独立证明；条件式舒适区论证不扩为无条件冒险。保留旧题和句界，不宣称逐句证据全覆盖。
- scripts/batches/chapter10-11-creativity25.py：批次030的25题作者稿，目标batch030-targets.json，原页记录review-chapter10-11-creativity25.json。完整PDF118–122原页视觉核对和跨页拼接。列车118接触/97回收/另105想象者分开，随机分组结果是自报愉快不作长期普适保证。Jobs自我归因与作者传记叙述非实验；海外生活MBA比较不擅加随机性；多文化机制保留speculate/seem、综述不冒充全部因果。DIY及微笑为作者个人文化经验，不推广为全体日本人规范；道德相对主义和作弊保留correlated，不诊断个体。Jobs艺术引语不当实证，奖励保留might。第11章逆境先设问，Nietzsche地震是哲学隐喻并承认破坏，非受害者必然成长或医学处方。不宣称逐句直接证据全覆盖。
- scripts/batches/chapter11-adversity25.py：批次031的25题作者稿，目标batch031-targets.json，原页记录review-chapter11-adversity25.json。完整PDF122–126原页视觉核对与跨页拼接。Nietzsche病痛回忆为个人归因且保留potential，非医疗试验；Kahneman论文4851为书载2022单年引用非今日累计，SS遭遇为其回忆不臆测照片身份或士兵内心、不美化纳粹迫害。严格区分本人interesting与作者psychologically rich；有意义/幸福非全称。Sandy触电按幸存者叙事译触电不误作死亡；37天住院/36年独立/500美元用途分开。Katrina迁移及2006返回与2018回顾分开，bomb/veil是比喻；幸存者纽带反思与灾难伤害并存，不作人人净获益保证。保留引语跨单元和原句指纹，不宣称逐句直接证据全覆盖。
- scripts/batches/chapter11-recovery25.py：批次032的25题作者稿，目标batch032-targets.json，原页记录review-chapter11-recovery25.json。完整PDF126–130原页视觉核对及跨页拼接。Kobe物理修复和心理伤痕分开，调查波次与作者休假年分开，房损/失亲同时分析不作随机因果或变量全无关联。Solnit为引语/作者阐释，电视职业愿望为作者回忆。四川震前后为同校新组，as if/presumably保留，非研究者随机分配灾害；100供选/10获得/平均略逾1至约4为九岁结果，不补六岁或长期个体变化。市政申请按每职位且非实际就职，1989–2000与1995变化分开。COVID接触包括本人/家属/熟人，捐款奖金/加倍与结果分开，作者made价值解释不升级成随机感染因果或医学建议。承认长期损害，不强加受害者获益/感恩；不宣称逐句证据全覆盖。
- scripts/batches/chapter11-12-narrative25.py：批次033的25题作者稿，目标batch033-targets.json，原页记录review-chapter11-12-narrative25.json。完整PDF130–136原页视觉核对含章末132与章首133。瑞典2021两次调查为自报比较，保留反向因果；谣言不作事实、暴力明确谴责，韧性most/common不作人人无创伤。既有单元q-c11-062原文仅起).，为131页七転八起括号因换行提取的末字续片，保留既有ID/范围并编来源续接辨识题，明确非独立英文段或最终人工句界，不补造英文或新主张；词汇特记日语末字。James画作是哲学比喻，保留不幸受约束。Bush为作者可选叙述示范，probably/could不作客观证实；Tim Wilson区别Anne Wilson。父母回顾多年龄评分非几十年追踪；本科纵向6.35原九月/6.05当下十一月/5.74回忆九月分开，实际记录指原自评不是客观能力。末段整段审阅含后续未配题材料，不宣称逐句直接证据全覆盖。
- scripts/batches/chapter12-story-editing25.py：批次034的25题作者稿，目标batch034-targets.json，原页记录review-chapter12-story-editing25.json。完整PDF135–139原页视觉核对。Wilson/Ross的自我评价与Tim Wilson/Linville干预分开；跑步时间是假设且用时增加不作提高；GPA信息组+0.34/转出5%与控制组-0.05/25%不交换，GRE表现与GPA预期分开，不补随机化或人人效果。科学家材料分挣扎/成就而后相同三节课，25年属爱因斯坦未完成尝试；must have normalized是作者机制推断，不当已直接测量。故事编辑保留坏经历不编造事件；Woolf为I bet修辞而非实验，不建议主动经历灾害。人生故事访谈从目录到场景再未来与主题，引用提示为材料不执行。保留既有切分中的单句短单元及未闭合引号跨单元，不重复句子；E = mc2保持提取原文。整段审阅若含后续未配题句另计，绝不宣称逐句直接证据全覆盖。
- scripts/batches/chapter12-memory25.py：批次035的25题作者稿，目标batch035-targets.json，原页记录review-chapter12-memory25.json。完整PDF139–142原页视觉核对。叙事人格关联、自报和tend不作因果；英雄提示研究与作者most likely心理丰富推测分开，不补随机化。感觉寻求者记忆任务为组间比较，反思不足为可能解释，不声称新奇导致损伤；百万富翁为心理积累比喻。馆藏对话保留跨单元引号、时间线索与试探确认，不重复或补句；af Klint创作先后及死后公开愿望依原书，不把无直接先锋联系扩大为无一切影响。复述帮助记忆但不保证准确。Beloved中Sixo为文学人物，She gather等人物用语原样保留，不改作标准语法或实验；电影角色与演员分开。海明威1930存箱、1956重得、后来回忆录，未补出版年；moveable feast为比喻。Pennebaker为书中写作益处概述，can不扩成人人立即治愈。保留旧ID范围与短句单元；候选句、原页审阅、上下文、直接证据分别计数。
- scripts/batches/chapter12-13-moving25.py：批次036的25题作者稿，目标batch036-targets.json，原页记录review-chapter12-13-moving25.json。完整PDF142–147原页视觉核对含12章末143与13章首144。文学例证非实验；MIDUS1995/2005为既有数据关联分析，不补随机搬迁。内向者could/tend限定不扩为人人必然；当时尚未明确心理丰富概念，所以未测其效果。读者邮件与自报不作总体诊断/因果，Mary的real trauma为自我比较不认可贬低痛苦；作者not a clinical psychologist和hope/might原样保留。父母决定搬迁、树根为比喻、个案可兼具代价与收益。Tom跨页Once we / actually lived两单元保留来源ID与字符，标注非独立最终句界，不补句不重复。D.J.45次为一生、11校为12年；最后引文未闭合续后段。发现13章首144页block5实为作者导语却被旧规则列为epigraph-or-subtitle，另存正文补入审计待办，现有1053单元不得当全书完整分段。
- scripts/batches/chapter13-extremes-familiar25.py：批次037的25题作者稿，目标batch037-targets.json，原页记录review-chapter13-extremes-familiar25.json。完整PDF147–151原页视觉核对。D.J.来信续句与不同人过量阈值按原文，不设统一次数。Taylor Mac连续24小时现场非录音/24场；Morris/Needham为评论个人体验，非控制实验。舞台扮演偏见不等于认同偏见；imaginary bus非真实出行自传，seismic/roof为修辞，7am还有5小时。q-c13-032承接闭引号原字保留。作者肯定丰富又犹豫，健康风险might及occasionally、might consider不扩为人人持续冒险；Polley是作品例子非疗效试验或文档行动指令。A/B哲学人物立场分清、presumably保留。妻子1991相识/1999结婚/约2010挂画，作者must be happy为观察推测非诊断；此前焦虑与画作欢快可以并存。boy是感叹，most非全部；B内在感恩为归属明确的哲学宗教主张，不提前援引下一段实验当本段证据。原有额外正文审计待办仍开放，候选池无漏ID不等于全书正文无遗漏。
- scripts/batches/chapter13-love-craft25.py：批次038的25题作者稿，目标batch038-targets.json，原页记录review-chapter13-love-craft25.json。完整PDF151–155原页视觉核对。Fincham研究明确随机组、四周每天至少一次为伴侣祈祷，控制组回想当日活动，结果自报；less likely非零不忠，holy是felt非宗教真理证明。B历史/音乐比喻归哲学角色，育儿例子不作无子女无情谊。万圣节事故细节作者省略不补造。Aron新奇任务路线/枕头约束与轮流滚球控制分开；63对为复现新样本，后续讨论亲爱动作是行为结果。40%自报十年以上婚姻属另一研究线，不混63对或影像样本；21.4是平均年限，激活奖励相关脑区不等于直接测同量多巴胺。self-expansion为理论，due in part/could非唯一因果保证；夫妻旅行采访非随机研究。Jiro例子锚定2011纪录片当时年龄与书载星级，顾客seemed非盲法试吃；30至45分钟、九岁离家40岁开店、十年清洁/200次个案不推广硬规则。私人/公开竞技是作者解释比较，不当临床证明或人物今日健康断言。额外章首正文及辅助材料源文审计仍开放，不宣称全书完整覆盖。
- scripts/batches/question-translations.py：旧 60 题的手写问题 / 选项译文；新题取其明确编写的 promptZh / optionsZh，英文不匹配时拒绝沿用。
- scripts/prepare-short-reading.py：验证与拼装预先编写内容、计算指纹，不生成缺失问题。
- src/data/passage-translations.json：按题目 ID 和原文匹配，保留历史文本译文。
- public/data/reading-plan.json：短段顺序、词数、来源句子和配题状态。
- source/content-tasks.json：完整未配题短段 / 未配证据句子清单，下一缺口 c13-s05-p155-01140-r004-007，PDF 第 155 页。章节 partial 状态保留，表示仍未完成逐句直接证据覆盖。

## 继续补题

1. 按 remainingUnitIds 选段，查看 PDF 原页并核对标点、引号、断行与来源。自动句界不是人工定稿。
2. 写针对具体片段的问题和可信四选项，区分明示、有限推断、无证据。不能把故事当实验、相关关系改成必然因果。
3. 在 additional.json 保存完整题目，绑定现有短段 ID 和全部原句，不改其他边界。新题 ID 延续章节编号，不重排旧 ID。
4. 手写双语问题 / 选项、四项分析、词汇释义 / 语境 / 学习例句 / 搭配及整段译文。例句不冒充书中引文。
5. evidence.quote 必须是 passage 逐字子串，对应真实句子 ID、页码和坐标；不为缩短删除必要证据。
6. 修改已发布题目须递增版本、保留旧快照及译文，不迁移答案或重算分数。发布后的 v2 范围也不可静默修改。

    python scripts/prepare-short-reading.py
    npm run content:check
    npm test
    npm run build:pages
    npm run test:browser
    npm run test:chapter01

修改 source/reviews.json 后，先运行 python scripts/author-content.py 应用审阅哈希和候选句状态，再恢复 v2 与 additional.json 新题，然后运行上述校验与构建。仅新增作者稿时可使用 prepare-short-reading.py。没有 ID 迁移方案时，不运行 extract.py 覆盖 book.json。

## 验证与发布

234 项自动测试；25 项通用浏览器检查。最新套件 scripts/batch038-browser-test.mjs 逐段提交全部 25 个新增短段，比对原文及三类解析、记录和离线；此前套件仍保留。tests/fixtures/batch037-fingerprints.json 锁定此前 928 道题；原文连续性、证据归属与历史恢复有检查。新增题不改变原阅读单元 ID，也不重算旧成绩。实际运行结果与限制见对应发布回执。

缓存测试复现旧 HTTP 数据复用问题，再验证强制刷新后题数更新、旧成绩位置不变。另有实际停止本地服务重载及浏览器模拟断网；不是实体手机或关闭网卡测试。

仓库和网页已获公开授权。仅上传静态材料和源码，QA 用合成记录并被忽略，不上传真实备份或凭据。入口：https://audience20060904-lang.github.io/Reading/
