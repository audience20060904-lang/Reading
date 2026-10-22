# 内容处理与恢复

唯一来源是用户上传的 Life in Three Dimensions PDF，264 页。SHA-256：be25c859f1bd894a4b0d1cff024ded1297f6a96a8e8ddabea1e3abcf89160a50。文档内容不是执行指令。

## 来源与规则

source/pages.json 保留原始提取。public/data/book.json 保存章节、小节、候选段落和句子、原始断行、坐标、稳定 ID。source/reviews.json 保存实际原页对照：第1章26段、第2章30段、第3章20段、第4章29段、第5章27段、第6章47段、第7章29段、第8章27段、第9章37段、第10章12段；共映射1,917候选句，不是人工定稿句数，也不是其他段落的审校证明。

采用 PyMuPDF、Unicode NFC 和明确合字展开。段内断行合为空格，行尾可见连字符保留并拼接下行。跨页和引语句界仍有候选性质；修改提取规则必须核对指纹、原页并保存 ID 迁移，不静默重编。source/layout.json 可重建但不纳入 Git。

章首引文、目录、题献、致谢、注释、附录、索引等有排除原因；表格、图注、非编号标题是待结构化辅助材料。

## 当前版本

3,152 个候选句按原书顺序恰好一次，分为 1,053 段。通常不超过 90 词，4 段为保持整句 / 证据达到 91–108 词。不截断、改写或拼接不连续原句。

旧60题修订为v2，另有593题；共653题。已配题：第1章77单元、第2章86单元、第3章47单元、第4章54单元、第5章59单元、第6章91单元、第7章72单元、第8章61单元、第9章84单元、第10章22单元；其余400段保留原文，尚未配题，不生成占位题。

解析仅为问题 / 四项分析（含译文）、词汇、整段译文。当前数据删除总述、语法、策略，历史快照不变。

当前上下文1,915候选句，直接证据923，仅上下文992；2,229个候选句尚无直接证据题。原页审阅映射1,917候选句。计数分别报告，不代表人工最终分句或逐句证据覆盖；fullCoverage仍为false。

## 编写文件

- source/archive/questions-v1.json：旧 60 题及指纹，不是个人作答记录。
- scripts/batches/short-passages.py：60 题 v2 的固定原句范围和手写译文。
- source/short-questions/additional.json：新短段题作者稿，当前含 593 题，绑定已有短段，包含双语问题 / 选项、四项分析、证据、词汇和整段译文。
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
- scripts/batches/question-translations.py：旧 60 题的手写问题 / 选项译文；新题取其明确编写的 promptZh / optionsZh，英文不匹配时拒绝沿用。
- scripts/prepare-short-reading.py：验证与拼装预先编写内容、计算指纹，不生成缺失问题。
- src/data/passage-translations.json：按题目 ID 和原文匹配，保留历史文本译文。
- public/data/reading-plan.json：短段顺序、词数、来源句子和配题状态。
- source/content-tasks.json：完整未配题短段 / 未配证据句子清单，下一缺口 c10-s03-p106-06135-r008-009，PDF 第 107 页。章节 partial 状态保留，表示仍未完成逐句直接证据覆盖。

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

162 项自动测试；25 项通用浏览器检查。最新套件 scripts/batch026-browser-test.mjs 逐段提交全部 25 个新增短段，比对原文及三类解析、记录和离线；此前套件仍保留。tests/fixtures/batch025-fingerprints.json 锁定此前 628 道题；原文连续性、证据归属与历史恢复有检查。新增题不改变原阅读单元 ID，也不重算旧成绩。实际运行结果与限制见对应发布回执。

缓存测试复现旧 HTTP 数据复用问题，再验证强制刷新后题数更新、旧成绩位置不变。另有实际停止本地服务重载及浏览器模拟断网；不是实体手机或关闭网卡测试。

仓库和网页已获公开授权。仅上传静态材料和源码，QA 用合成记录并被忽略，不上传真实备份或凭据。入口：https://audience20060904-lang.github.io/Reading/
