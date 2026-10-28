# 三维 · IELTS 阅读工作室

只学习 Shigehiro Oishi 的 Life in Three Dimensions。React、TypeScript、Vite、IndexedDB；无 AI API、运行时出题、注册或云端学习数据库。学习记录仅保存在本机浏览器，可通过 JSON 备份在设备间手动迁移。

网页：https://audience20060904-lang.github.io/Reading/
公开源码：https://github.com/audience20060904-lang/Reading

<!-- evidence-progress:start -->
## 直接证据补题 · 候选来源 ID 已覆盖

当前本地已准备1653道补题，已验证发布1653道；尚未发布的本地批次不得当作线上完成。总题库2709题（1056道主问题＋1653道补题），3160个候选来源 ID 关联到题目证据引文（关联本身不保证该句直接支持正确答案），仍有0个待补。后文1499/1661等数值记录此前修复阶段，当前以本节、public/data/coverage.json及真实发布回执为准。

该 ID 清单包含列表编号、标点、签名及跨页片段，并非人工定稿的完整句子数；原有主问题的证据有时只是句子中的片段。编号和断句可与相邻正文共用一道题。不能据此声称全书人工逐句审校完成，fullCoverage 保持 false。

<!-- evidence-progress:end -->

### 证据语义审阅与词汇补充

2026-10-27 起，对既有证据关联继续进行人工语义复核：`source/semantic-evidence/audit.json` 保存首批 261 个仅部分引用的候选 ID、来源与逐项状态；其中 3 项已核对实际 PDF 第 8 页，2 项的现有问题直接得到引文支持，1 项已另编问题，剩余 258 项尚待逐项复核。部分引用并不必然缺题；完整引用也不自动证明题目直接考查该句。此前 `source/evidence-final-audit.json` 是原候选 ID 关联阶段的历史快照，不是语义复核完成证明。

词汇目录在原有 624 处的基础上新增 35 处（共 659 处），包括语境中的难词和熟词偏义，点击淡蓝色词可查看本段含义及适用的其他常见含义；目录仍不是完整词典。


## 当前短段版

界面使用黑白灰、蓝色操作强调、系统字体与居中单列阅读布局。桌面为顶部导航，手机为底部五项导航；全站支持浅色、深色主题和减少动态效果偏好。原文、题目与已提交解析的顺序保持不变，淡蓝查词保留。样式在src/design.css，响应式检查可运行node scripts/ui-redesign-browser-test.mjs（桌面、320/390px手机、768/1024px视口）。

阅读练习页首显示当前小节的原书英文标题，随阅读位置更新。提交前，英文原文放在题目前；提交后，原文及来源信息移到第三部分整段中文译文上方，同一段原文只显示一次。

解析只保留：问题与四项分析（含中文翻译）、重点词汇、整段译文。原文、问题、选项为英语（原书夹用其他语言时保留原字）；提交后才显示三类中文解析，译文在最后。当前题目 JSON 也移除了总述、语法、策略，历史快照原样保留。

2026-10-25 断句修复：已核对实际 PDF 第49、58、103、114、131、146–147、158、167–169页，修复9处边界、18个短段，包括问话后的叙述、and so on 列举结尾、完整日语谚语以及 Once we / actually lived、sitting / quietly、Stop by a / gallery。没有添加推测词语，也没有重复英文。1056个单元ID与3160个候选句ID原顺序保留；候选ID边界仍用于来源审计，不冒充人工最终句数。

public/data/questions.json和reading-plan.json保留1056题发布基线；src/data/sentence-repair-catalog.json保存18题及单元的预编新版，首页与章节浏览实际使用这一修订层。旧题、旧翻译、旧快照完整保留。已提交的旧题刷新仍恢复原解析，可主动重练新版；修订题的旧未提交选项会清空，防止把另一版本的选择计入新题。

来源作者稿与实际原页记录在source/sentence-repairs.json、source/sentence-repair-review.json。同段精确取片，跨页英文只以一个空格相接，日语断行字符直接相接；所有源字符与顺序保留。旧的batch来源备注是当时状态，当前展示以上述修订层为准。

来源审计已补回：PDF144块5、第160块5的作者导语按原页位置补为3个短段和3道题；原1053题及原阅读单元不变。source/source-audit-review.json记录21个实际PDF原页、32个章首块及17个辅助材料块的视觉核对。三个阶段标题、两张表和三幅图已恢复为8组辅助材料，并按原页块顺序进入章节原文浏览；这些材料不计叙事候选句、配题数或作答成绩。两个原书副标题用作未编号章首分组，不增加87个原书编号小节的数量。

- 全部 3,160 个候选正文句按原书顺序分为 1,056 个短段，无遗漏或重复句子 ID。
- 通常不超过 90 词；为保留整句和证据，5 段为 91–108 词。没有删词、改写或拼接不连续原句。
- 当前1056题：原1053题保留，新增 q-c13-102、q-c13-103、q-c14-073，均有问题与四选项中文译文、四项分析、词汇及完整段落译文。
- 仍有 0 段没有题目与中文材料。保留真实原文并标明状态，不生成占位题、不制造作答记录。
- 所有已确认的14章叙事正文均已进入阅读链路并逐段配题。候选句界仍有历史跨页、引语及日语续片例外；原页审阅映射计数不等于人工最终句数，也不等于逐句直接证据覆盖。

首页仍从第 1 章正文第一句开始（PDF 第 7 页）：

> Yoshi was born in a small mountain town on the island of Kyushu, Japan, known for its green tea and clementines.

第一、二题使用不同原句，不再反复展示整段。“But first we need to start with the question: What is a good life?” 仍可搜索定位（PDF 第 9 页）。没有预填成绩。

## 运行与验证

Windows 双击 start-reading.cmd，或使用 Node.js 22.12+ 执行：

    npm ci
    npm run content:check
    npm test
    npm run build:pages
    npm run test:browser
    npm run test:chapter01
    npm run preview -- --port 4173 --strictPort

打开 http://127.0.0.1:4173/ 。开发使用 npm run dev。不要用 file:// 双击 HTML，离线只在生产构建中工作。

当前316项自动测试。通用浏览器套件25项；末尾25段使用 node scripts/batch042-browser-test.mjs。来源审计和新增3题使用 node scripts/batch043-browser-test.mjs，检查原页顺序、旧题指纹和成绩、图表恢复、子路径与离线缓存。所有浏览器作答均为隔离合成记录，实际发布结果记录在对应回执中。

脚本使用 Playwright 和 Chromium；Windows 默认 Edge，可设置 BROWSER_PATH。缺少依赖时安装 npm install --no-save playwright，再执行 npx playwright install chromium。QA 使用隔离浏览器和合成记录，仅写入被忽略的 qa/，不读取用户 4173 端口数据。

第 1 章套件可用 READING_TEST_URL 指向已部署网页；如本机网络依赖代理，可用 READING_TEST_PROXY 指定已有 HTTP 代理，不会修改系统网络设置。本批 5 项线上检查及验证限制见 source/releases/batch-005.json。

2026-10-22 的两段补充可运行 node scripts/batch006-browser-test.mjs，同样支持上述网址和代理环境变量；其 5 项检查覆盖两题实际提交、答案隐藏、双语解析、导航、统计和模拟离线。发布结果保存在 source/releases/batch-006.json。

紧随其后的 Madison 两段使用同一浏览器脚本：READING_TEST_BATCH 设为 batch007，READING_TEST_QUESTION_IDS 设为 q-c02-030,q-c02-031。原页复核位于 PDF 第 17–18 页，发布结果见 source/releases/batch-007.json。

此前批次的作者稿、冻结目标、审阅和发布回执均保留。末尾25题见scripts/batches/chapter14-final25.py与batch-042回执；本次补漏见scripts/batches/audited-openings.py、batch043-targets.json、review-audited-openings.json及batch-043回执。source/additive-body.json保存新增原始块，source/structural-materials.json保存结构化图表及来源。

包括桌面、390px 手机视口、浏览器模拟断网及实际停止本地 HTTP 服务后的重载；不是实体手机或关闭 Windows 网卡测试。

## 点击查词

阅读练习和章节原文中的淡蓝色词可点击，显示“本段中的意思”和“其他常见意思”。只标注预先选定的难词、熟词偏义或词组，未标蓝的普通词不会弹窗。当前475个实际可查词条、624处具体语境标注，分布于14章；这是精选词表，不表示所有难词均已收录。常用义较单一的词不会强行列出第二义。

查词支持手机、键盘Tab/Enter、Escape和点击遮罩关闭，关闭后焦点返回原词。弹窗不显示题目答案或整段翻译，也不产生作答、已读或成绩记录。首次缓存完成后全部释义可离线查看，不调用AI或在线词典。旧题和历史快照不改写；无法精确匹配来源的旧片段保持纯文本。

词表作者稿：source/word-lexicon.tsv；位置与语境义由scripts/prepare-word-lookups.py编译到src/data/word-lookups.json，范围报告在source/word-lookup-review.json。上下文词义来自已编写词汇条目的meaning，而非选项分析；其他义项为另行整理的词义说明，不是原书英文引文。更新后运行该脚本、npm test、npm run build:pages及node scripts/word-lookup-browser-test.mjs。

## 阅读与旧记录

上一段 / 下一段按全书原句顺序推进，未配题段不会跳过。配有题目的段落须提交后继续。章节浏览使用同一组短段，可搜索原文及稳定句子 ID，选择“从本段继续阅读”。

阅读进度 = 手动已读句子与已读小节所含句子的并集 / 3,160 个候选句（辅助材料不计入分母）。标记本段已读不产生答案或正确次数，答题和切换段落不自动标记已读。

IndexedDB 保存位置、答案、正误、时间、次数、耗时、版本 / 指纹、完整历史快照、已读和难词。正确率按全部真实提交计算，去重按题目 ID 另计；错题按最新一次提交判断，旧错误保留。

首次升级进入新版短段，不套用旧版答案；旧成绩不变。统计页可主动回看旧解析，刷新仍恢复该历史会话。历史译文按题目 ID 和原文精确匹配，不套用新片段。

## 本章进度与存档

练习页首显示当前 Chapter 与本章阅读位置百分比，计算为当前短段在本章的顺序号 ÷ 本章短段数（保留一位小数）。它是位置指示；跳转到章末可显示100%，但不会产生已读、作答或正确记录。统计页手动已读口径保持独立。

本机数据库保持原名称、版本1和state键，旧记录就地兼容。选择、提交、位置、偏好即时写入；未提交用时每5秒保存。每次不同学习状态在同一事务中保留最多3个旧恢复点（计时不挤占），设置中可确认恢复。主记录损坏时尝试有效恢复点，显示恢复提示，不偷偷归零。修订号在同一事务内检查，旧标签页不能覆盖另一标签页较新的存档；遇此提示请刷新旧页。可在设置中申请持久存储，浏览器不保证授予，主动清除站点数据仍会删除全部本机存档与恢复点。

本机存档不跨设备自动同步。手机和电脑分别保存各自记录；迁移时先从原设备导出 JSON，在另一设备导入并确认覆盖，题目快照和历史成绩一并恢复。无需账号、仓库令牌或云服务。全部本机恢复点损坏时，加载错误页仍提供 JSON 恢复入口，确认前保留原始数据。

存档与进度单元测试在 tests/archive.test.ts；独立浏览器测试在 scripts/archive-browser-test.mjs，只使用隔离合成记录。

## 离线、备份与讨论

在线打开并等待设置显示“离线缓存已就绪”，然后同一地址可离线访问或添加到主屏幕。浏览器可能回收缓存，请备份重要记录。

缓存按子路径隔离，内容或生成逻辑改变时更新。安装使用 Request(cache: reload) 刷新 HTTP 旧数据，防止旧题库装入新缓存；只清理同作用域缓存，不删除 IndexedDB。联网刷新、待缓存就绪后重新打开。

设置支持 JSON 完整备份、CSV 历史、JSON 导入校验与覆盖提醒。可先备份或取消，覆盖不是合并。备份包含私人记录和书籍片段，应自行保管，不上传真实备份。设备、浏览器和域名之间不自动同步，使用 JSON 手动迁移。

没有内置聊天机器人。Ask ChatGPT 组合书名、章节、原文、英文问题 / 选项及疑问，已提交才附选择和正确答案。需手动粘贴；ChatGPT 不能自动读取本机数据。摘要只包含少量相关题目、错题 ID、位置和难词。

## 真实覆盖和后续内容

| 项目 | 当前数量 |
|---|---:|
| PDF 页数 / 章节 / 编号小节 | 264 / 14 / 87 |
| 候选段落 / 候选句 | 459 / 3,160 |
| 原页对照段落 / 其中映射的候选句 | 459 / 3,160（非人工定稿句数） |
| 无遗漏无重复短段 | 1,056 |
| 已配题 / 待配题短段 | 1056 / 0 |
| 当前题目上下文 / 仅上下文候选 ID | 3,160 / 0 |
| 直接证据关联 / 尚无证据关联的候选 ID | 3,160 / 0 |
| 完整引文包含 / 仅部分引用的候选 ID | 2,908 / 252 |
| 题目总数（主问题 + 补题） | 2,709（1,056 + 1,653） |
| 语义候选清单已复核 / 待复核 | 128 / 133 |

public/data/reading-plan.json 报告分段覆盖，public/data/coverage.json 报告题目证据覆盖。前后置材料和章首引文等有排除原因；8组表格、图示与非编号标题已恢复为正文辅助材料，另有2个未编号章首分组。原 PDF 不上传。

CONTENT.md说明更新流程。source/content-tasks.json的未配题短段与source/content-audit-tasks.json的已知正文待办均为空。目前每个既有候选 ID 都有证据关联；其中完整引文与部分引用分别统计。这不等于每句已独立设题或2709题已全部人工审校。语义清单由261个机械筛选候选组成，其已复核数也不代表全库已审题数。继续依据 `source/semantic-evidence/audit.json` 逐项核对，修订时保留稳定题号、递增版本并保留旧快照。

## GitHub Pages

用户已同意仓库和网页 Public。main 为源码，gh-pages 为构建文件。没有上传凭据、node_modules、缓存、真实备份，也没有创建付费运行资源。

Pages 来源为 Deploy from a branch → gh-pages → / (root)。build:pages 验证 /Reading/ 子路径、manifest、资源和离线范围并添加 .nojekyll。测试后把 dist/ 内容更新到 gh-pages 根目录，保留普通提交历史并移除旧资源，不需要强推。只更新 main 不会自动发布。

旧 Sites 站点与 GitHub Pages 域名不同，记录不自动互通。Codespaces 配置仅保留为可选入口；未创建资源，若自行使用须注意计费并保持端口 Private。

断句修订的重建顺序：node scripts/repair-sentence-boundaries.mjs → npm run content:check → npm test → npm run build:pages → node scripts/sentence-repairs-browser-test.mjs。编译器只拼装已写好且已审阅的JSON，验证基线、来源和字符，不生成题目。任何原稿流水线重建后均须再次运行断句编译器；不得静默覆盖已发布基线。

## 继续逐句直接证据任务

先检查 source/evidence-tasks.json、Git、source/releases/evidence-*.json；有未发布批次必须恢复。运行 node scripts/start-evidence-batch.mjs 会优先返回现有批次；只有前批真实发布后才冻结最前面的至多25个缺口及原文/父题指纹。作者手动编写batchNNN-author.json，保留实际PDF整页核对与逐题审阅到batchNNN-review.json；不运行AI API，不在网站生成题目。

完整作者稿经 node scripts/compile-evidence-questions.mjs 编译为 public/data/evidence-questions.json，再运行 npm run content:check、npm test、npm run build:pages、node scripts/evidence-browser-test.mjs。EVIDENCE_BATCH=001指定批次；READING_TEST_URL和READING_TEST_PROXY可用于线上验证。通过构建、浏览器与线上资源指纹核对后保存真实回执，再继续下一批。已发布题目指纹不能被静默覆盖。

主问题与补题共用原来的短段，界面显示本段第几题；提交后手动点击下一题，最后一题后才进入下一段。原文只有一个显示实例，阅读单元与源ID不复制。新题自带问题/选项中文译文和整段翻译，导出JSON时完整保留。纯本地存档和历史成绩不变；手动已读不冒充答题。

## 编校补记：贴纸研究覆盖说明

第五十批最后一道补题（`qe-c11-0081`）分析末尾关于“下一批”的附带说明不准确：九岁儿童震前、震后的平均捐赠数早已由原题 `q-c11-046` 直接覆盖，并非下一批新缺口。该补题考的是实际捐出数量这一行为测量，不涉及上述均值是否已经配题；正确答案、原文证据、旧题指纹与历史成绩均保留。详见 [编校记录](source/evidence-questions/batch051-previous-review-erratum.json)。


## B2 及以上词汇扩充（2026-10-28）

目前共有 **2030 个词条、5048 处可点击位置**，覆盖 14 章。本次续批新增 144 个词条、433 处标注，补充心理学术语、文学表达、专业词和熟词偏义；此前 1886 个词条、4615 处标注的内容与位置完整保留。点击淡蓝色词可查看该处的词义和适用的其他常见含义。正文、题目和成绩均保留。

筛选参考 [Oxford 3000 分级清单](https://www.oxfordlearnersdictionaries.com/external/pdf/wordlists/oxford-3000-5000/The_Oxford_3000_by_CEFR_level.pdf) 和 [Oxford 5000 分级清单](https://www.oxfordlearnersdictionaries.com/external/pdf/wordlists/oxford-3000-5000/The_Oxford_5000_by_CEFR_level.pdf)。官网文件直连返回 403，本地参考读取其 GitHub 镜像 PDF，并将来源及文件哈希记在作者稿中；参考 PDF 不随网站或仓库发布。中文释义为独立编写或复用现有题库的词汇注释，没有复制词典释义。

等级只用于词头筛选，不能替代具体词义的难度判定。专业词、文学词和高级短语另行选择，不把所有清单外词汇称为 C2。严格筛出的 B2/C1 候选位置已处理或记录排除理由（人名、地名或普通语法用法）；这不等于全书所有 B2/C1/C2 义项已最终人工穷尽。

继续处理时编辑 `source/b2-vocabulary/author-notes.json` 的具体原文位置及释义；`corpus-glosses.tsv` 保存本轮通用词义和其他常见义的作者材料，`coverage.json` 保存筛选范围与排除项目。运行 `npm run vocab:compile` 校验来源字符、句子 ID 和不重叠规则，再运行测试与生产构建。该编译命令只装配预编写的标注，不在线推断词义。`tests/fixtures/word-lookups-v3.json` 是本次之前的完整词表快照，用于检查旧数据未被覆盖。

`source/b2-vocabulary/unclassified-candidates.json` 另存未分级长词形的恢复清单（含实际位置）。它们可能是低级词的屈折形式，并不等于全部都是 C2 难词；须先核对词义和难度再加入。

最新续批作者稿为 `source/b2-vocabulary/advanced-02.tsv`，具体句子的不同义项与排除理由在 `advanced-02-senses.json`。例如 agreeable 区分人格特质与“乐于接受建议”，self-determination 区分心理学理论与群体自主；Non-neurotic 以完整词匹配，不拆成含义相反的 neurotic。程序只装配已写好的释义，不在浏览器中猜测词义。新增 433 处标注的来源文本与实际 PDF 中 112 页、223 个来源块比对通过；另视觉核对第 12、31、42、66 页，不把文本比对称为每页视觉审校。

`advanced-02-review.json` 保存本批范围、标注 ID、排除记录和验证结果。恢复清单中的 152 个词形已记录审阅结果，仍有 1327 个未分级词形待判断，其中可能包含基础词变形；这不是“还缺1327个难词”的计数，也不宣称全书高级义项已穷尽。`tests/fixtures/word-lookups-v4-fingerprints.json` 冻结上版每个词条和标注的指纹，测试阻止改写旧内容。可运行 `node scripts/advanced-vocabulary-browser-test.mjs` 验证本续批；线上验证另设 `READING_TEST_URL`。本地测试包含停掉 HTTP 服务后缓存重载，线上断网检查使用浏览器离线模式，两者分别记录。手机检查为 390px Edge 视口，不等于真机验证。

## 题目细节校对（2026-10-28）

本轮对 2709 题做结构及译文匹配检查，人工对照实际 PDF 的 15 页复核 23 题、25 个部分引用候选，修订其中 12 题。修正修窗句译文过度表达已完成结果、解析依赖未显示前文、人物指代不精确、贴纸题残留下一批备注等问题，并改善 11 道主问题的干扰项。托尔斯泰题扩展原句引文，补齐夫妻相爱这个前提。英文原文、题号、阅读顺序及答案位置均保留。

作者稿、上版完整题目与校对报告分别在 `source/question-revisions/review-001.json`、`review-001-baseline.json` 和 `review-001-report.json`。运行 `npm run questions:compile` 将预写修订编译到 `src/data/question-revision-catalog.json`；应用在原始主问题、断句修复与补题组合后载入新版。旧题文件不覆盖，已提交记录继续显示自己的旧快照和成绩；重新练习才采用新版本。未提交的旧选择在选项改版后清空，避免误套新选项。版本、指纹、双语材料和完整题目快照会随 JSON 备份保存。

运行 `npm run content:check`、`npm test`、`npm run build:pages`、`node scripts/question-review-browser-test.mjs` 验证。线上检查可设置 `READING_TEST_URL` 和 `READING_TEST_PROXY`。回执记录 12 题的新指纹后，该批编译器拒绝改写已发布修订；后续校对须建立新的版本批次，保留上一批作者稿和基线。

`source/semantic-evidence/audit.json` 的语义候选待办由 258 减少至 233；这些是待复核的来源候选，不等于错误题数。全库结构检查不等于 2709 题都完成了人工语义审校。题目长度统计仅用于筛选潜在猜题线索，不能机械地把最长项都判错或强行缩短正确答案。

续批 002 对照 PDF 第 27–32 页，复核下一组 25 个语义候选、20 道题，修订其中 15 道。重点保留 might 的可能性、or 的选择关系、相关与分数一致的区别、often comes with 的伴随关系，以及 Mason 的假设人物属性。语义候选待办目前为 208。首批 12 道已发布修订题的指纹完整保留，本轮答案位置、原文和阅读顺序不变。作者稿、基线、固定目标及报告分别见 `source/question-revisions/review-002*.json`。

`source/question-revisions/manifest.json` 按时间列出各批次。`npm run questions:compile` 顺序重放作者稿，核对每一批自己的基线和发布回执，再汇编最新版本；同一题在后续新批次中可以再次递增版本，早先已发布的作者稿不能改写。浏览器检查默认验证最新一批，可用 `REVIEW_BATCH=001` 或 `REVIEW_BATCH=002` 指定批次，报告保存在忽略的 `qa/` 目录。运行时仍只读取预编本地内容。

续批 003 复核 25 个来源候选、18 道题，修订 9 道；语义候选待办为 183。补齐 A/B 生活立场题被截断的证据，移除 Jobs 职业概括题不必要的年龄限制，保留思想史叙事中的推断归属和原书时间语境。之前两批的 27 道修订题保持原发布指纹。

阅读界面现支持提交后在第三部分的原文上以金色定位本题证据，淡蓝色仍表示可查词。标记只包裹原文字符，重叠引文合并；重复片段无法按来源句消歧时不猜位置。提交前不显示证据标记，历史快照依据自己的证据定位。题型统计将现有 36 个标签归并为 8 组展示，正确率按提交次数加权，原始标签和分数仍保存在历史及导出中；未知新标签独立保留。手机标题与留白适度收紧，正文宽度和手动下一题流程不变。

`source/optimization-tasks.json` 保存连续处理检查点：先恢复未发布批次，再处理语义清单最前面的至多 25 个候选；每批验证并发布后接着下一批。界面验证、题目审校和全库完成状态分别记录，不能以单批通过替代剩余待办完成。

续批 004 实际核对 PDF 第 39–45 页，复核 25 个来源候选、19 道题，修订其中 8 道；语义候选待办为 158。补齐 Joy 丧亲的独立证据，完整引用和解旅程、退休条件及偶尔工作的句子，明确 Linda 的 two of whom 指孙辈。其余题经核对后保留，不机械重写。2709 题中的来源 ID 关联仍不等于逐句已独立考查或全库语义校对完成。

修订可在已有引文之后追加证据：旧引文的顺序、来源 ID 和 PDF 引用保留；新增项必须逐字包含当前片段中的完整来源候选，并使用书籍记录中准确的页码、块号和坐标。编译与内容检查都验证这些条件；伪造句子、错绑来源或改写历史批次会被拒绝。追加证据也会递增题目版本，已提交的旧快照继续使用自己的证据。

续批 005 实际核对 PDF 第 45–56 页，复核 25 个来源候选、23 道题，修订其中 11 道；语义清单已复核128个，尚有133个待审。区分日记记录要求与实际报告份数，补齐奖学金费用清单，消除单句题干依赖前文姓名的问题，并保留组间自报、材料缺漏和条件推论的范围。逐题判断记录见 `source/question-revisions/review-005-report.json`；前四批已发布作者稿和指纹保留。
