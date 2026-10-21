# 三维 · IELTS 阅读工作室

只学习 Shigehiro Oishi 的 *Life in Three Dimensions: How Curiosity, Exploration, and Experience Make a Fuller, Better Life*。React + TypeScript + Vite + IndexedDB；无 AI API、无运行时出题、无注册、无云端学习数据库。

## 现在可以使用

Windows 双击 `start-reading.cmd`，然后在浏览器打开 **http://127.0.0.1:4173/**。首次安装需要网络与 Node.js 22.12+（本次使用 Node 24）。也可以：

```powershell
npm ci
npm run content:check
npm test
npm run build
npm run preview -- --port 4173 --strictPort
```

开发模式：`npm run dev`。**离线缓存只在生产构建 / 生产预览中验证**，不要用 `file://` 双击 HTML。此工作区为 `D:\1\Reading`；本地默认只监听 127.0.0.1。

当前入口从第 1 章正文第一句开始（PDF 第 7 页，已视觉核对）：

> Yoshi was born in a small mountain town on the island of Kyushu, Japan, known for its green tea and clementines.

另一指定句 “But first we need to start with the question: What is a good life?” 保留跳转，位于 PDF 第 9 页。没有示例历史、预填成绩或默认第 9 题。

## 已实现的学习流程

- 原文 → 英文问题 → 四个英文选项 → 自己点击提交 → 正误及正确答案 → 五部分中文解析及末尾整段参考译文 → 自己点击下一题。
- 未提交时不渲染解析，不在 Ask ChatGPT 消息中添加选择、答案或解析。题库文件离线包含答案，因此这不是防作弊系统。
- 真实章节 / 小节目录、原文搜索、句子定位、原始断行和坐标查看；逐句已读、小节已读；难词收藏。
- IndexedDB 保存当前位置、选择、提交解析、时间、耗时、作答次数、题目版本 / SHA-256 内容指纹，以及完整历史题目快照。
- 统计总次数、去重题数、正确次数、整体 / 章节 / 题型正确率、阅读进度、错题和近期记录。错题按每题最新一次提交判断；旧错误不会被删除。
- JSON 完整备份、CSV 历史、导入校验与明确覆盖提醒；学习摘要与单题上下文复制。ChatGPT 无法自动读取本机数据，需手动粘贴。
- 手机 / 桌面、深浅主题、字号、减少动画偏好。无外部字体或资源依赖。

阅读进度 = **单句手动已读与手动已读小节内句子的并集 / 全书候选叙事正文句子**。答题不自动标记已读；手动已读不会伪造答案、增加作答数或正确次数。正确率使用所有真实提交次数，重练计入分母；去重题数单独展示。

## 内容现状：尚未完成全书逐句配题

本次从实际 PDF 重新提取，未找到可用源码 ZIP，未沿用交接中的数字。

| 项目 | 本次结果 |
|---|---:|
| PDF 页数 | 264 |
| 正文章节 / 编号小节 | 14 / 87 |
| 候选叙事段落 / 候选句子 | 457 / 3,152 |
| 原页视觉核对段落 | 第 1 章 26 段 + 第 2 章 30 段，映射 417 个候选句子 |
| 已保存练习 | 60（第 1 章 33；第 2 章 27） |
| 出现在练习上下文中的候选句子 | 371 |
| 仅作上下文 | 275 |
| 直接作为题目证据 | 96 |
| 尚未配直接证据题 | 3,056 |

**417 是已核对段落中自动候选句子的映射数，不是经过人工定稿的句子总数。** 题目为逐题编写的学习材料；逐字引文与提取文本精确匹配。第 1、2 章叙事段落已作原页对照，第 3–14 章仍待逐页视觉核对。词汇例句由学习材料作者编写，界面明确注明其不是书中引文。

第 3–14 章保留实际提取的原文与真实目录，尚无练习，不生成占位题。全书完成状态始终为 false。覆盖报告同时在设置界面和 `public/data/coverage.json` 提供；按章、按小节、按未处理句子 ID 的恢复清单见 `source/content-tasks.json`。第 1 章虽每节有题，仍远未逐句配题。

章首引文 / 署名、封面、目录、题献、致谢、注释、附录、索引等有明确排除记录。**表格、图注和非编号小标题属于待结构化的正文辅助材料，暂不计叙事句子，不把它们冒充非正文或已完成内容。** 原始提取仍保存在 `source/pages.json` 与书籍数据的结构记录；PDF 图片本身不在本站内重新发布。

## 离线使用与更新

先在线打开生产页面，在设置中确认“离线缓存已就绪”。可用 Edge / Chrome 的“安装应用”或添加到主屏幕；缓存完成后，同一地址可以离线打开。首次安装 / 缓存需要网络，浏览器可能回收长期未用的缓存；个人进度请备份。

正文 / 题库是静态 JSON，个人进度在独立 IndexedDB。更新题库后先备份，再更新源码、运行检查 / 构建，启动同一端口并在线重载。Service Worker 内容指纹变化时安装新缓存，删除**同作用域**旧版本；根路径和 `/Reading/` 路径缓存互不清除。旧作答使用历史快照，不按新答案重算。

Vite 默认 `base: './'`，manifest 的 id / scope / start_url、脚本 / JSON 请求、Service Worker 注册均相对当前部署目录；已实际测试根路径与 `/Reading/`。要指定固定子路径可设置 `APP_BASE=/Reading/` 后构建。不要随意换协议、域名或端口：IndexedDB 按浏览器 origin 隔离。换设备 / 浏览器时用 JSON 恢复。

## 备份与恢复

设置 → JSON 完整备份。文件包含书籍片段及私人学习记录，请自行保管。恢复：选择 JSON → 格式与成绩 / 快照一致性校验 → 检视记录数 → 先下载现有备份 → 确认覆盖。覆盖不是合并。CSV 不用于恢复。

备份不具备密码加密或第三方签名；不要导入不可信文件。清除网站数据、隐身模式退出或更换 origin 均可能使本机记录不可用。项目不会上传真实学习备份。

## 验证

```powershell
npm run content:check
npm test
npm run build
npm run test:browser
```

当前自动测试 36 项；浏览器检查 20 项。覆盖答案判断、统计、IndexedDB 持久化、顺序 / 上下题、备份 / 导入、起始句、来源匹配、报告与虚假覆盖声明、离线构建合同。

浏览器脚本使用真实 Chromium / Edge。若环境没有 Playwright：先 `npm install --no-save playwright`，再 `npx playwright install chromium`；Windows 默认使用已安装的 Edge，可用 `BROWSER_PATH` 指定可执行文件。Codex 本机使用其自带 Playwright，无需安装浏览器。脚本创建临时学习记录，仅写入 `qa/`（Git 忽略），不会污染用户 4173 端口的数据。

验证包含：桌面 / 390px 手机截图、提交前消息无答案、真实提交 / 刷新 / 重练 / 备份恢复、根与子路径缓存、浏览器 `setOffline` 模拟断网，以及**实际停止 HTTP 服务后的页面重载与记录恢复**。没有关闭 Windows 网卡；模拟断网与服务停止测试分别记录，不能声称物理断网测试。

## GitHub Pages、手机使用与公开源码

用户于 2026-10-21 明确同意将 Reading 仓库改为 Public，以免费使用 GitHub Pages；此授权更新了最初要求 Private 的决定。源码仓库：https://github.com/audience20060904-lang/Reading

**正式网页：https://audience20060904-lang.github.io/Reading/**

已于 2026-10-21 成功部署，GitHub [Pages 部署记录](https://github.com/audience20060904-lang/Reading/actions/runs/39544582095) 为 success；匿名 HTTPS 返回 200。真实 Edge 线上验证 7 项通过：起始原文 / 四选项 / 未提交隐藏解析、9 个线上文件与本地已测构建逐字节一致、390px 布局、提交反馈及最底部整段译文、刷新恢复、子路径缓存 / 模拟离线重载、无运行时异常。没有声称已在实体手机或关闭 Windows 网卡后测试。

`main` 保存源码；`gh-pages` 保存已经构建的网页，包括完整题库、原文、整段译文及离线资源，根目录含 `.nojekyll`。没有上传真实学习备份、凭据、访问令牌、node_modules 或测试缓存。未创建 Codespace 或购买套餐。

Pages 已设为 **Deploy from a branch → gh-pages → / (root)**，无需再次启用。GitHub 连接器缺少 Pages 管理能力，本次通过本机 Git Credential Manager 中正确账号已有的登录授权，调用 GitHub 官方接口完成公开和启用；授权值仅在进程内存中使用，没有写入项目或输出。

[GitHub 官方要求](https://docs.github.com/en/pages/getting-started-with-github-pages/creating-a-github-pages-site)：Free 账户可从 Public 仓库使用 Pages。当前网页和仓库均公开；所有访问者可查看 / 下载网页资源与源码，个人学习记录仍仅保存在各自浏览器中。

构建和更新：

```powershell
npm ci
npm run content:check
npm test
npm run build:pages
npm run test:browser
```

`build:pages` 先执行完整生产构建 / 离线缓存生成，再检查 HTML、manifest、缓存清单中的资源均能在 `/Reading/` 下解析，最后写入 `.nojekyll`。把新 `dist/` 的**内容**更新到 `gh-pages` 分支根目录，不要把 `dist` 文件夹整体嵌套进去；删除上一版本不再使用的构建文件。保留分支历史，用普通提交更新，不需要强推。设置页来源配置一次即可，后续更新该分支会重新发布。只更新 main 源码不会自动更新 gh-pages。

验证脚本使用真实 Edge，分别加载 `/` 与区分大小写的 `/Reading/`，验证缓存作用域隔离与离线重载。该脚本验证本地构建；线上部署已另行验证，但没有进行实体手机测试。

手机 Safari / Chrome 打开上述 GitHub HTTPS 地址即可，无需启动电脑服务。首次在线打开并等待“离线缓存已就绪”后可添加到主屏幕。每位访问者的作答、阅读标记和难词只保存在各自浏览器的 IndexedDB。

设备之间、localhost 与公网域名之间、此前 Sites 域名与 GitHub 域名之间，记录都不会自动同步。使用 JSON 备份在新地址导入。旧 Sites 站点 https://life-three-dimensions-reading.stablestork18.chatgpt.site 仍保留；它不是 GitHub Pages，也不能作为 GitHub 已上线的证明。

Codespaces 配置仅作为可选开发入口保留，未创建运行资源。若自行使用，注意计费额度并保持转发端口 Private。

## 继续处理内容

详见 `CONTENT.md`。恢复清单和三批题目已实际保存；不是只有提取脚本。第 3 批新增第 2 章 15 道题（稳定 ID q-c02-013 至 q-c02-027），按原文位置插入；原有 45 题的内容与指纹全部保留。下一批从第 3 章 PDF 第 27 页开始，同时继续回补第 1、2 章 remainingEvidenceIds 中的未配题句子。题目不能靠模板机械填满，各批提交须连同覆盖变化保存。

## 整段参考译文

现有 60 道题均预先配有当前完整英文片段的中文参考译文，保存在 `src/data/passage-translations.json`，随网页一起离线缓存，不在运行时调用翻译服务。仅选择选项时不显示；提交后在全部解析的最后展开。历史作答根据题目 ID 与当时原文精确匹配，原有成绩和题目快照保持不变。新增或改动英文片段时，应同步核对并补充译文；测试会检查当前所有题目的匹配情况。
