# 三维 · 私人 IELTS 阅读工作室

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

- 原文 → 英文问题 → 四个英文选项 → 自己点击提交 → 正误及正确答案 → 五部分中文解析 → 自己点击下一题。
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
| 原页视觉核对段落 | 第 1 章 26 段，映射 177 个候选句子 |
| 已保存练习 | 45（第 1 章 33；第 2 章 12） |
| 出现在练习上下文中的候选句子 | 237 |
| 仅作上下文 | 171 |
| 直接作为题目证据 | 66 |
| 尚未配直接证据题 | 3,086 |

**177 是已核对段落中自动候选句子的映射数，不是经过人工定稿的句子总数。** 题目为逐题编写的学习材料；逐字引文与提取文本精确匹配。除第 1 章外，其余章节仍待逐页视觉核对。词汇例句由学习材料作者编写，界面明确注明其不是书中引文。

第 3–14 章保留实际提取的原文与真实目录，尚无练习，不生成占位题。全书完成状态始终为 false。覆盖报告同时在设置界面和 `public/data/coverage.json` 提供；按章、按小节、按未处理句子 ID 的恢复清单见 `source/content-tasks.json`。第 1 章虽每节有题，仍远未逐句配题。

章首引文 / 署名、封面、目录、题献、致谢、注释、附录、索引等有明确排除记录。**表格、图注和非编号小标题属于待结构化的正文辅助材料，暂不计叙事句子，不把它们冒充非正文或已完成内容。** 原始提取仍保存在 `source/pages.json` 与书籍数据的结构记录；PDF 图片本身不在本站内重新发布。

## 离线使用与更新

先在线打开生产页面，在设置中确认“离线缓存已就绪”。可用 Edge / Chrome 的“安装应用”或添加到主屏幕；缓存完成后，同一地址可以离线打开。首次安装 / 缓存需要网络，浏览器可能回收长期未用的缓存；个人进度请备份。

正文 / 题库是静态 JSON，个人进度在独立 IndexedDB。更新题库后先备份，再更新源码、运行检查 / 构建，启动同一端口并在线重载。Service Worker 内容指纹变化时安装新缓存，删除**同作用域**旧版本；根路径和 `/reading/` 路径缓存互不清除。旧作答使用历史快照，不按新答案重算。

Vite 默认 `base: './'`，manifest 的 id / scope / start_url、脚本 / JSON 请求、Service Worker 注册均相对当前部署目录；已实际测试根路径与 `/reading/`。要指定固定子路径可设置 `APP_BASE=/Reading/` 后构建。不要随意换协议、域名或端口：IndexedDB 按浏览器 origin 隔离。换设备 / 浏览器时用 JSON 恢复。

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

当前自动测试 28 项；浏览器检查 17 项。覆盖答案判断、统计、IndexedDB 持久化、顺序 / 上下题、备份 / 导入、起始句、来源匹配、报告与虚假覆盖声明、离线构建合同。

浏览器脚本使用真实 Chromium / Edge。若环境没有 Playwright：先 `npm install --no-save playwright`，再 `npx playwright install chromium`；Windows 默认使用已安装的 Edge，可用 `BROWSER_PATH` 指定可执行文件。Codex 本机使用其自带 Playwright，无需安装浏览器。脚本创建临时学习记录，仅写入 `qa/`（Git 忽略），不会污染用户 4173 端口的数据。

验证包含：桌面 / 390px 手机截图、提交前消息无答案、真实提交 / 刷新 / 重练 / 备份恢复、根与子路径缓存、浏览器 `setOffline` 模拟断网，以及**实际停止 HTTP 服务后的页面重载与记录恢复**。没有关闭 Windows 网卡；模拟断网与服务停止测试分别记录，不能声称物理断网测试。

## 私人 GitHub 与浏览器入口

使用仅含初始化 README 的既有 Private 仓库 `audience20060904-lang/Reading`。建议名称 `life-in-three-dimensions-reading` 本次未找到；连接器没有新建仓库工具，没有声称成功新建它。写入前后均检查 Private 与 push 权限。

**源码仓库地址不是网页地址。** 本次提供本地浏览器入口与 Codespaces 配置；不启用公开 Pages，不创建付费运行资源。Private 仓库不等于 Pages 私人，含全书内容的构建不能未经确认公开发布。

若以后自行选择 Codespaces：它可能消耗计费额度，先查看账户余额 / 费用，再由你手动创建。配置在 `.devcontainer/devcontainer.json`；进入后运行：

```sh
npm run preview -- --host 0.0.0.0 --port 4173 --strictPort
```

打开 Ports 面板，确认 4173 的 Visibility 是 **Private**，再打开它给出的浏览器地址；可用 `gh codespace ports visibility 4173:private -c "$CODESPACE_NAME"` 强制设置。GitHub 文档说明默认转发端口为 Private，只允许创建者登录访问；配置文件本身不应被视为无法更改的访问控制：[GitHub Codespaces 安全](https://docs.github.com/en/codespaces/reference/security-in-github-codespaces)、[端口访问范围](https://docs.github.com/en/codespaces/developing-in-a-codespace/forwarding-ports-in-your-codespace)。没有创建 Codespace，因此不存在可报告的 `*.app.github.dev` 运行链接。

## 继续处理内容

详见 `CONTENT.md`。恢复清单和两批题目已实际保存；不是只有提取脚本。顺序：第 2 章剩余逐字核对与未配题句子 → 第 3 章 → 后续章节；同时处理第 1 章仍无证据题的句子。题目不能靠模板机械填满，各批提交须连同覆盖变化保存。
