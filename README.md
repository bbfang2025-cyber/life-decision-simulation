# 人生决策推演 · Life Decision Simulation

> 一个装进 AI 就能用的决策技能：**四位顾问轮流上场，一人一轮，一人一把尺子。**
> 顺序由外到内——先拆清、再敢砍、再算远、最后听心。

你问它"该不该走"，它**不会**马上回答"走"或"不走"。它先把你的情况摆成六格，缺哪格补哪格，问完才让四位顾问上场：

| 轮次 | 顾问 | 用的方法 | 他管什么 |
|---|---|---|---|
| 一 · 拆解 | **马斯克** | 第一性原理 | 你名义上在决定 A，实际在决定什么 |
| 二 · 取舍 | **乔布斯** | 减法 | 你舍不得的是什么，砍掉哪个你最疼 |
| 三 · 长期 | **芒格** | 逆向思维 | 别算能赢多少，先算怎么会一次输光 |
| 四 · 内心 | **王阳明** | 致良知 | 你心里那个别扭的点，是良知还是私心 |

**核心规矩一句话：四步里有一步没过，这个决定就先别做。**

---

## 它和别的"人生规划 AI"有什么不同

**1. 它先问，不先答。**
多数人纠结几周，输给的往往不是"选错了"，而是从来没把前提摊开看过：她到底在哪座城市、回老家有没有具体工作、"收入减半"减到多少。这些没拿到之前，任何"去 / 不去"都是编的。

**2. 每一句话都有署名。**
你不会听到一句来路不明的"综合考虑"。每位顾问上场都要亮身份、报方法、下判断、给判定——**你始终知道这句话是谁说的、凭什么这么说。**

**3. 判定是硬的，不许骑墙。**
每位顾问给"过 / 没过"，总判三选一（可以去做 / 缓做先验证 / 不建议）。想听"看你更看重什么"这种话，这里没有。

---

## 它怎么跑

```
接住（不评价）
  ↓
拆话：把他的话拆成 决定 / 代价 / 人 / 重量词
  ↓
六格体检（内部，不输出）：选项 · 时点 · 数字 · 人 · 底线 · 证据
  ↓  └─ 前五格缺一格 → 不许出总判；第六格缺 → 总判强制降级为"缓做"
按"翻转力"排序，一次只问一个，全场最多 6 问
  ↓
四位顾问依次上场（每人固定五句式：亮身份 → 报方法 → 下判断 → 重构 → 追问）
  ↓
第二轮校准（"哪一步你答得最卡" / "结论和你想要的不一样，你会怎么做"）
  ↓
《人生决策推演报告》八节
```

**重量词**是这个技能最特别的一节。用户不会说"我在意这个"，但会不自觉把它念出来——"干了 5 年""都这个岁数了""还在异地"。前三步一个字都不提，留到王阳明那一轮原样递回去：

> "你从头到尾说了三次'五年'，但一次都没说这五年你得到了什么。"

**翻转力排序**是另一半核心。不问最重要的，问**最能翻转结论的**：

> "女朋友在哪座城市"就是翻转级——她在北京，你回去是自己造出异地；她在老家，你回去是结束异地；她在第三城，你回不回都是异地。一个词，三种人生。

---

## 快速开始

**最省事**：下载 [`dist/人生决策推演_下载与安装.pdf`](dist/人生决策推演_下载与安装.pdf)——里面有国内直连 zip 地址和一页"给 AI 的安装指令"，把 PDF 丢给你的 AI 就能自动下载并装好。

### 方式一：装进支持技能的工具（推荐）

```bash
# WorkBuddy
git clone https://github.com/bbfang2025-cyber/life-decision-simulation.git \
  ~/.workbuddy/skills/life-decision-simulation

# Claude Code / Claude 桌面版
git clone https://github.com/bbfang2025-cyber/life-decision-simulation.git \
  ~/.claude/skills/life-decision-simulation
```

装好后直接说人话，越具体越好：

> "我在北京做运营五年了，想回老家，收入得减半，女朋友还在异地，我该不该走？"

说不清也没关系——调起来之后它一条一条反过来问你。也可以语音输入，想到哪说到哪，反而不容易漏。

### 方式二：把整包丢给 AI，让它自己装

仓库里 `dist/人生决策推演_完整安装版_拖给AI就能装.pdf` 是**自安装 PDF**：正文就是这四个文件的原始 markdown，带 BEGIN/END 定界标记和拼行规则。把它拖进任何能读写本地文件的 AI（WorkBuddy / Claude / Cursor），说：

> "按这份 PDF 第 2 页的安装说明，把文件完整装到我的技能目录。"

### 方式三：不装，粘贴就能用

`dist/人生决策推演_提示词版_小红书私信.pdf` 是一段约 4600 字的纯提示词，机制全保留。粘到任意聊天 AI 的**自定义指令 / 智能体 / 系统提示词**里即可（豆包＝创建智能体，ChatGPT＝Custom Instructions，DeepSeek＝直接当第一条消息发）。

---

## 目录结构

```
SKILL.md                                  # 主文件：四步流程、四位顾问、判定标准
references/
├── 提问总库.md                            # 48 问，按六格分类，每问标注"什么答案会翻转结论"
└── 示范_北京回老家_完整报告.md             # 一次完整推演：六问实录 + 四位顾问台词 + 整份报告
使用说明.md                                # 给人看的：怎么装、怎么问、会拿到什么
dist/
├── 人生决策推演_完整安装版_拖给AI就能装.pdf   # 自安装版（22 页，正文即源码）
└── 人生决策推演_提示词版_小红书私信.pdf       # 提示词版（6 页，粘贴即用）
```

---

## 你会拿到什么

一份八节的《人生决策推演报告》：

1. 这件事（一句话重述）
2. **你话里的重量词**——你反复强调却没解释的那个词
3. **四位顾问的推演**——每位标清"马斯克 · 第一性原理"这种出处，逐个给"过 / 没过"
4. **总判**——可以去做 / 缓做先验证 / 不建议，三选一
5. 顾问分歧点（打得最凶的地方，通常就是真风险）
6. 最关键的待验证项（当前最可能推翻结论的那个未知数）
7. 行动计划：7 天 / 30 天 / 90 天各一个具体动作
8. 什么情况下该回来重新推演一遍

每个判断都带标签：**【已确认】是你说的，【合理推断】是推出来的，【待验证】要你用行动确认。**

---

## 几条设计原则

- **问比答值钱。** 六格缺格时给建议，给的是顾问自己的投射，不是你的答案。
- **宁可说"我还不知道"，也不许拿想象当依据。** 所以会有"缓做，先验证"这个总判。
- **顾问不许串味。** 马斯克只用第一性原理，芒格只管长期。四个人说话一个味儿，这个方法就废了。
- **顾问可以打架，而且必须打。** 芒格说"账算得过来可以走"、王阳明说"不能走，你有一半在怕被笑"——这不是矛盾，是分工：**芒格保证你不死，王阳明保证你不悔，两个都得过。**
- **不装神。** 算不出来的就说算不出来，不输出"成功率 90%"这种不可验证的数字。

---

## 边界与免责

- **不适用**：大额投资、医疗方案、法律纠纷、心理危机。遇到这些它会直接说超出范围，建议找持牌专业人士；用户情绪明显危机时先停流程、先安顿人。
- **不替你做决定。** 四位顾问是四个视角，选择权始终在你。
- 示例里的人和数字**全部虚构**，只用来演示流程，真实使用时一格都不许照抄。
- 四位人物的方法（第一性原理 / 减法 / 逆向思维 / 致良知）是他们公开讲过、反复讲过的理论；具体到某件人生小事上，是这些方法的**应用**，不是本人意见。这个技能不编一套"听着像"的道理冒充他们。

---

## License

[MIT](LICENSE) © 2026 Fang Bin

拿去改、拿去商用都行，保留版权声明即可。如果你把它改得更好用，欢迎提 PR。

---

## English

**Life Decision Simulation** is a portable AI skill for hard personal decisions — leaving a city, quitting a job, switching careers, buying a home, marriage or separation.

Instead of answering "should I?", it runs a fixed pipeline: extract the hidden **weight words** from what you said → audit six information gaps (options / timing / numbers / people / bottom lines / evidence) → ask at most six questions ordered by **flip power** → then hand the floor to four advisors, each with one method and one verdict:

- **Elon Musk** — first principles: what are you *actually* deciding?
- **Steve Jobs** — subtraction: what are you unwilling to give up?
- **Charlie Munger** — inversion: how would this blow up?
- **Wang Yangming** — innate knowing: is that discomfort conscience, or vanity?

**If any of the four steps fails, the decision waits.** Output is an eight-section report with evidence tags and a 7/30/90-day action plan.

Works as a drop-in skill (WorkBuddy / Claude) or as a single paste-in prompt. Content is in Chinese; the method is language-agnostic.
