# 三维 · IELTS 阅读工作室

只学习 Shigehiro Oishi 的 Life in Three Dimensions。React、TypeScript、Vite、IndexedDB；无 AI API、运行时出题、注册或云端学习数据库。

网页：https://audience20060904-lang.github.io/Reading/
公开源码：https://github.com/audience20060904-lang/Reading

## 当前短段版

解析只保留：问题与四项分析（含中文翻译）、重点词汇、整段译文。原文、问题、选项为英语；提交后才显示三类中文解析，译文在最后。当前题目 JSON 也移除了总述、语法、策略，历史快照原样保留。

- 全部 3,152 个候选正文句按原书顺序分为 1,053 个短段，无遗漏或重复句子 ID。
- 通常不超过 90 词；为保留整句和证据，4 段为 91–108 词。没有删词、改写或拼接不连续原句。
- 当前 503 题：原有 60 题修订为短段 v2，另有 443 道新短段题。第 1–7 章的 77、86、47、54、59、91、72 个单元均已配题和完整中文材料。第 8 章已配到前 17 个单元；最新 25 题为 q-c07-065 至 q-c07-072 及 q-c08-001 至 q-c08-017。
- 仍有 550 段没有题目与中文材料。保留真实原文并标明状态，不生成占位题、不制造作答记录。
- 原文全部进入阅读链路，不等于全书题库完成，也不等于自动句界都已人工定稿。

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

当前 126 项自动测试。通用浏览器套件 25 项，另有第 1 章完整练习套件 5 项。最新 25 段有独立套件 node scripts/batch020-browser-test.mjs，共 5 项，按序真实提交全部 25 个新增短段，验证双语材料、原文连续性、统计、历史恢复及模拟离线。QA 使用隔离合成记录。各次实际运行结果记录在对应发布回执中。

脚本使用 Playwright 和 Chromium；Windows 默认 Edge，可设置 BROWSER_PATH。缺少依赖时安装 npm install --no-save playwright，再执行 npx playwright install chromium。QA 使用隔离浏览器和合成记录，仅写入被忽略的 qa/，不读取用户 4173 端口数据。

第 1 章套件可用 READING_TEST_URL 指向已部署网页；如本机网络依赖代理，可用 READING_TEST_PROXY 指定已有 HTTP 代理，不会修改系统网络设置。本批 5 项线上检查及验证限制见 source/releases/batch-005.json。

2026-10-22 的两段补充可运行 node scripts/batch006-browser-test.mjs，同样支持上述网址和代理环境变量；其 5 项检查覆盖两题实际提交、答案隐藏、双语解析、导航、统计和模拟离线。发布结果保存在 source/releases/batch-006.json。

紧随其后的 Madison 两段使用同一浏览器脚本：READING_TEST_BATCH 设为 batch007，READING_TEST_QUESTION_IDS 设为 q-c02-030,q-c02-031。原页复核位于 PDF 第 17–18 页，发布结果见 source/releases/batch-007.json。

此前批次的作者稿、冻结目标、审阅和发布回执均保留。最新25个单元在 scripts/batches/chapter07-08-next25.py；目标与原文指纹在 source/short-questions/batch020-targets.json，原页核对在 review-chapter07-08-next25.json。固定此前478题指纹，补齐第7章末8单元和第8章前17单元。PDF77–82完整核对，重审1个旧段、新增11段；区分近似转述、反事实、假设估算、历史时点与人物观点。额外审阅3个候选句仍待配题。发布结果见 source/releases/batch-020.json。此前数字问题与短语尾段记录均保留。

包括桌面、390px 手机视口、浏览器模拟断网及实际停止本地 HTTP 服务后的重载；不是实体手机或关闭 Windows 网卡测试。

## 阅读与旧记录

上一段 / 下一段按全书原句顺序推进，未配题段不会跳过。配有题目的段落须提交后继续。章节浏览使用同一组短段，可搜索原文及稳定句子 ID，选择“从本段继续阅读”。

阅读进度 = 手动已读句子与已读小节所含句子的并集 / 3,152 个候选句。标记本段已读不产生答案或正确次数，答题和切换段落不自动标记已读。

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
| 候选段落 / 候选句 | 457 / 3,152 |
| 原页对照段落 / 其中映射的候选句 | 217 / 1,455（非人工定稿句数） |
| 无遗漏无重复短段 | 1,053 |
| 已配题 / 待配题短段 | 503 / 550 |
| 当前题目上下文 / 仅上下文句 | 1,452 / 723 |
| 直接证据 / 尚无直接证据题候选句 | 729 / 2,423 |

public/data/reading-plan.json 报告分段覆盖，public/data/coverage.json 报告题目证据覆盖。前后置材料和章首引文等有排除原因；表格、图注、非编号标题保留为正文辅助材料待办。原 PDF 不上传。

CONTENT.md 说明继续流程；source/content-tasks.json 保存每章未审校、未配证据句子与未配题短段 ID。下一批从第 8 章第 3 小节缺口 c08-s03-p081-05745-r004-004（PDF 第 81–82 页）开始。第 1–7 章虽然每个单元均有题，仍不能将段落完整配题等同逐句证据覆盖。

## GitHub Pages

用户已同意仓库和网页 Public。main 为源码，gh-pages 为构建文件。没有上传凭据、node_modules、缓存、真实备份，也没有创建付费运行资源。

Pages 来源为 Deploy from a branch → gh-pages → / (root)。build:pages 验证 /Reading/ 子路径、manifest、资源和离线范围并添加 .nojekyll。测试后把 dist/ 内容更新到 gh-pages 根目录，保留普通提交历史并移除旧资源，不需要强推。只更新 main 不会自动发布。

旧 Sites 站点与 GitHub Pages 域名不同，记录不自动互通。Codespaces 配置仅保留为可选入口；未创建资源，若自行使用须注意计费并保持端口 Private。
