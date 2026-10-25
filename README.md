# 三维 · IELTS 阅读工作室

只学习 Shigehiro Oishi 的 Life in Three Dimensions。React、TypeScript、Vite、IndexedDB；无 AI API、运行时出题、注册或云端学习数据库。

网页：https://audience20060904-lang.github.io/Reading/
公开源码：https://github.com/audience20060904-lang/Reading

## 当前短段版

界面使用黑白灰、蓝色操作强调、系统字体与居中单列阅读布局。桌面为顶部导航，手机为底部五项导航；全站支持浅色、深色主题和减少动态效果偏好。原文、题目与已提交解析的顺序保持不变，淡蓝查词保留。样式在src/design.css，响应式检查可运行node scripts/ui-redesign-browser-test.mjs（桌面、320/390px手机、768/1024px视口）。

阅读练习页首显示当前小节的原书英文标题，随阅读位置更新。提交前，英文原文放在题目前；提交后，原文及来源信息移到第三部分整段中文译文上方，同一段原文只显示一次。

解析只保留：问题与四项分析（含中文翻译）、重点词汇、整段译文。原文、问题、选项为英语（原书夹用其他语言时保留原字）；提交后才显示三类中文解析，译文在最后。当前题目 JSON 也移除了总述、语法、策略，历史快照原样保留。

来源例外：q-c11-062 对应 PDF 第131页日语谚语被提取断行后的 `起).` 续片，并非独立英文段。保留原ID与字符，以来源续接辨识题说明，未补造英文；详见 source/short-questions/batch033-source-notes.json。q-c13-018/019 也保留了跨页 `Once we / actually lived…` 的同一句续接，不视为独立最终句界。短段数与候选句数不能当作独立、人工定稿英文段句数。

来源审计已补回：PDF144块5、第160块5的作者导语按原页位置补为3个短段和3道题；原1053题及原阅读单元不变。source/source-audit-review.json记录21个实际PDF原页、32个章首块及17个辅助材料块的视觉核对。三个阶段标题、两张表和三幅图已恢复为8组辅助材料，并按原页块顺序进入章节原文浏览；这些材料不计叙事候选句、配题数或作答成绩。两个原书副标题用作未编号章首分组，不增加87个原书编号小节的数量。

- 全部 3,160 个候选正文句按原书顺序分为 1,056 个短段，无遗漏或重复句子 ID。
- 通常不超过 90 词；为保留整句和证据，4 段为 91–108 词。没有删词、改写或拼接不连续原句。
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

当前283项自动测试。通用浏览器套件25项；末尾25段使用 node scripts/batch042-browser-test.mjs。来源审计和新增3题使用 node scripts/batch043-browser-test.mjs，检查原页顺序、旧题指纹和成绩、图表恢复、子路径与离线缓存。所有浏览器作答均为隔离合成记录，实际发布结果记录在对应回执中。

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

## 离线、备份与讨论

在线打开并等待设置显示“离线缓存已就绪”，然后同一地址可离线访问或添加到主屏幕。浏览器可能回收缓存，请备份重要记录。

缓存按子路径隔离，内容或生成逻辑改变时更新。安装使用 Request(cache: reload) 刷新 HTTP 旧数据，防止旧题库装入新缓存；只清理同作用域缓存，不删除 IndexedDB。联网刷新、待缓存就绪后重新打开。

设置支持 JSON 完整备份、CSV 历史、JSON 导入校验与覆盖提醒。可先备份或取消，覆盖不是合并。备份包含私人记录和书籍片段，应自行保管，不上传真实备份。设备、浏览器和域名之间不自动同步，使用 JSON 恢复。

没有内置聊天机器人。Ask ChatGPT 组合书名、章节、原文、英文问题 / 选项及疑问，已提交才附选择和正确答案。需手动粘贴；ChatGPT 不能自动读取本机数据。摘要只包含少量相关题目、错题 ID、位置和难词。

## 真实覆盖和后续内容

| 项目 | 当前数量 |
|---|---:|
| PDF 页数 / 章节 / 编号小节 | 264 / 14 / 87 |
| 候选段落 / 候选句 | 459 / 3,160 |
| 原页对照段落 / 其中映射的候选句 | 459 / 3,160（非人工定稿句数） |
| 无遗漏无重复短段 | 1,056 |
| 已配题 / 待配题短段 | 1056 / 0 |
| 当前题目上下文 / 仅上下文句 | 3,160 / 1,662 |
| 直接证据 / 尚无直接证据题候选句 | 1,498 / 1,662 |

public/data/reading-plan.json 报告分段覆盖，public/data/coverage.json 报告题目证据覆盖。前后置材料和章首引文等有排除原因；8组表格、图示与非编号标题已恢复为正文辅助材料，另有2个未编号章首分组。原 PDF 不上传。

CONTENT.md说明更新流程。source/content-tasks.json的未配题短段与source/content-audit-tasks.json的已知正文待办均为空。后续如要扩充逐句证据题，须新增稳定题号并保留旧快照，不得把目前1498个直接证据候选句写成3160句全部直接配题。

## GitHub Pages

用户已同意仓库和网页 Public。main 为源码，gh-pages 为构建文件。没有上传凭据、node_modules、缓存、真实备份，也没有创建付费运行资源。

Pages 来源为 Deploy from a branch → gh-pages → / (root)。build:pages 验证 /Reading/ 子路径、manifest、资源和离线范围并添加 .nojekyll。测试后把 dist/ 内容更新到 gh-pages 根目录，保留普通提交历史并移除旧资源，不需要强推。只更新 main 不会自动发布。

旧 Sites 站点与 GitHub Pages 域名不同，记录不自动互通。Codespaces 配置仅保留为可选入口；未创建资源，若自行使用须注意计费并保持端口 Private。
