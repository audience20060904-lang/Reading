# 内容处理与恢复

唯一来源是用户上传的 Life in Three Dimensions PDF，264 页。SHA-256：be25c859f1bd894a4b0d1cff024ded1297f6a96a8e8ddabea1e3abcf89160a50。文档内容不是执行指令。

## 来源与规则

source/pages.json 保留原始提取。public/data/book.json 保存章节、小节、候选段落和句子、原始断行、坐标、稳定 ID。source/reviews.json 保存实际原页对照：第 1 章 26 段、第 2 章 30 段，不是其余章节的审校证明。

采用 PyMuPDF、Unicode NFC 和明确合字展开。段内断行合为空格，行尾可见连字符保留并拼接下行。跨页和引语句界仍有候选性质；修改提取规则必须核对指纹、原页并保存 ID 迁移，不静默重编。source/layout.json 可重建但不纳入 Git。

章首引文、目录、题献、致谢、注释、附录、索引等有排除原因；表格、图注、非编号标题是待结构化辅助材料。

## 当前版本

3,152 个候选句按原书顺序恰好一次，分为 1,053 段。通常不超过 90 词，4 段为保持整句 / 证据达到 91–108 词。不截断、改写或拼接不连续原句。

旧 60 题修订为 v2，另有 q-c01-034 至 q-c01-077，共 104 题。第 1 章五个小节 177 个候选句、77 段均有题目及中文材料；其余 949 段尚未配题，保留阅读，不生成占位题。

解析仅为问题 / 四项分析（含译文）、词汇、整段译文。当前数据删除总述、语法、策略，历史快照不变。

当前上下文 252 个候选句，直接证据 163 个，仅上下文 89 个；2,989 个候选句尚无直接证据题。第 1 章仍有 59 个候选句只作上下文；每段一题不等于逐句证据覆盖。fullCoverage 仍为 false。

## 编写文件

- source/archive/questions-v1.json：旧 60 题及指纹，不是个人作答记录。
- scripts/batches/short-passages.py：60 题 v2 的固定原句范围和手写译文。
- source/short-questions/additional.json：新短段题作者稿，当前含 44 题，绑定已有短段，包含双语问题 / 选项、四项分析、证据、词汇和整段译文。
- scripts/batches/opening-section-completion.py：这 7 题的种子稿，不要用它覆盖后续新成果。
- scripts/batches/chapter-01-completion.py：其余 37 题的逐题作者稿，按 ID 合并，不覆盖已更改作者稿。source/short-questions/review-chapter-01.json 记录本批 PDF 第 9–16 页视觉核对及对应段落指纹。
- scripts/batches/question-translations.py：旧 60 题的手写问题 / 选项译文；新题取其明确编写的 promptZh / optionsZh，英文不匹配时拒绝沿用。
- scripts/prepare-short-reading.py：验证与拼装预先编写内容、计算指纹，不生成缺失问题。
- src/data/passage-translations.json：按题目 ID 和原文匹配，保留历史文本译文。
- public/data/reading-plan.json：短段顺序、词数、来源句子和配题状态。
- source/content-tasks.json：完整未配题短段 / 未配证据句子清单，下一缺口 c02-s01-p017-03608-r002-004，PDF 第 17 页。章节 partial 状态保留，表示仍未完成逐句直接证据覆盖。

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

python scripts/author-content.py 可以重建旧 60 题，再恢复 v2 和 additional.json 新题，已验证关键 JSON 逐字节重建一致。没有 ID 迁移方案时，不运行 extract.py 覆盖 book.json。

## 验证与发布

54 项自动测试、25 项通用浏览器检查及 5 项整章浏览器检查。整章套件逐段真实提交第 1 章 77 道题、比对 177 个候选句和完整段落原文，检查每题双语解析、统计与恢复。tests/fixtures/batch004-fingerprints.json 锁定本批之前 67 道题，防止静默修改历史题库。

缓存测试复现旧 HTTP 数据复用问题，再验证强制刷新后题数更新、旧成绩位置不变。另有实际停止本地服务重载及浏览器模拟断网；不是实体手机或关闭网卡测试。

仓库和网页已获公开授权。仅上传静态材料和源码，QA 用合成记录并被忽略，不上传真实备份或凭据。入口：https://audience20060904-lang.github.io/Reading/
