# Marketing Skills for OpenClaw

一个面向营销团队和增长团队的开源技能库，目标不是“多写一些营销文案”，而是让本地 AI Agent 能直接完成一整条营销工作链路里的高频任务：

- 市场研究
- 用户定位
- 内容规划
- SEO 与关键词结构
- 广告预算分配
- 增长实验设计
- 活动复盘

当前仓库包含：

- 8 个模块
- 23 个独立 skill
- 4 个可直接运行的 Python skills
- 1 个结构校验脚本
- 1 组最小可运行测试

## 先看这个

如果别人第一次打开这个仓库，只需要先看这 4 件事：

1. 这个仓库能做什么：看下方的 `Skill Map`
2. 怎么最快跑起来：看 `3 分钟上手`
3. 跑出来是什么样：看 `效果展示`
4. 这些结果有没有验证过：看 `测试结果`

如果你需要一份“每个 skill 是干什么的、怎么实现、会产出什么”的完整参考表，直接看 [docs/SKILL_REFERENCE.md](/Users/sanbu/Code/2026重要开源项目/vinky/marketing-skills/docs/SKILL_REFERENCE.md)。

## 怎么看参考表

[docs/SKILL_REFERENCE.md](/Users/sanbu/Code/2026重要开源项目/vinky/marketing-skills/docs/SKILL_REFERENCE.md) 这张表不是目录清单，而是一张“怎么选 skill”的速查表。它会告诉你：

- 有哪些可用 skill
- 每个 skill 解决什么问题
- 需要什么输入
- 人通常会怎么提这个需求
- 最后大概会交付什么

适合在这些情况下直接看这张表：

- 你刚拿到这个仓库，想先知道有哪些能力可用
- 你已经有一个营销任务，但不知道该用哪个 skill
- 你想快速判断一个 skill 需要什么输入，避免来回试
- 你想向别人展示这个仓库，不想只贴目录

下面是 3 行简化示例，作用只是让你一眼看懂表格怎么读：

| Skill | 什么情况下可用 | 输入示意 | 会给你什么 |
| --- | --- | --- | --- |
| `market-landscape-scan` | 想快速看一个新赛道值不值得做 | `帮我看一下 AI 外呼在中国市场近 24 个月的行业机会。` | 行业概览、机会点、风险点 |
| `channel-budget-allocator` | 手上有预算，想分配到不同投放渠道 | `我有 50 万预算，目标是拿线索，渠道是搜索、信息流、短视频。` | 保守 / 均衡 / 激进三套预算方案 |
| `campaign-retrospective-writer` | 活动结束后，想快速产出复盘 | `这是新品首发活动的数据，帮我拆出亮点、问题和行动项。` | 复盘摘要、问题归因、行动项 |

如果你是第一次使用，建议先按这个顺序看：

1. 先看 `Skill Map`，知道能力范围
2. 再看 `docs/SKILL_REFERENCE.md`，判断该选哪个 skill
3. 最后去具体目录看 `SKILL.md` 或直接运行 Python skill

## 3 分钟上手

### 1. 看模块索引

```bash
sed -n '1,200p' skills/market-research/SKILLS.md
```

### 2. 看一个独立 skill

```bash
sed -n '1,220p' skills/seo-geo-aeo/keyword-cluster-builder/SKILL.md
```

### 3. 直接跑一个 Python skill

```bash
python3 skills/seo-geo-aeo/keyword-cluster-builder/main.py \
  --business-domain "私域增长" \
  --locale zh-CN \
  --keywords-file skills/seo-geo-aeo/keyword-cluster-builder/examples/keywords.txt
```

### 4. 跑完整验证

```bash
python3 scripts/validate_skills.py
python3 -m unittest tests/test_python_skills.py
```

## Skill Map

### Market Research
- `market-landscape-scan`：行业全景扫描与机会识别
- `competitor-gap-analysis`：竞品差距分析与突破点识别
- `user-voice-mining`：用户评论与反馈痛点挖掘

### STP & Brand
- `icp-builder`：理想客户画像构建
- `persona-generator`：多角色 Persona 生成
- `positioning-statement-crafter`：品牌定位声明生成

### Content
- `content-strategy-planner`：内容战略与内容支柱规划
- `editorial-calendar-generator`：内容日历与发布节奏
- `multi-channel-rewriter`：多平台内容改写

### SEO / GEO / AEO
- `keyword-cluster-builder`：关键词聚类与主题结构搭建
- `serp-intent-analyzer`：SERP 与搜索意图分析
- `page-seo-optimizer`：页面 SEO 优化建议
- `answer-engine-optimizer`：面向 AI 问答引擎的内容优化

### Paid Media
- `channel-budget-allocator`：渠道预算分配建议
- `ad-angle-generator`：广告创意角度生成
- `ad-copy-variant-generator`：广告文案多变体生成

### Growth / CRO
- `funnel-diagnostics`：漏斗诊断与瓶颈定位
- `experiment-designer`：增长实验设计
- `ab-test-sample-size`：A/B 实验样本量计算

### CRM & Private Domain
- `lifecycle-segmentation`：生命周期分层策略
- `winback-automation-planner`：召回自动化流程设计

### Analytics & Attribution
- `marketing-kpi-framework`：营销指标体系设计
- `campaign-retrospective-writer`：活动复盘自动摘要

## 最值得展示的 4 个能力

如果你要把这个仓库发给别人看，不要只发目录，直接让对方看下面 4 个命令和输出。

### 1. 关键词聚类

命令：

```bash
python3 skills/seo-geo-aeo/keyword-cluster-builder/main.py \
  --business-domain "私域增长" \
  --locale zh-CN \
  --keywords-file skills/seo-geo-aeo/keyword-cluster-builder/examples/keywords.txt
```

输出摘要：

```json
{
  "keyword_count": 4,
  "clusters": [
    {
      "cluster_id": "cluster_1",
      "label": "会员体系搭建",
      "size": 2
    },
    {
      "cluster_id": "cluster_2",
      "label": "私域运营",
      "size": 2
    }
  ]
}
```

### 2. 渠道预算分配

命令：

```bash
python3 skills/paid-media/channel-budget-allocator/main.py \
  --total-budget 500000 \
  --goal leads \
  --channels-file skills/paid-media/channel-budget-allocator/examples/channels.json
```

输出摘要：

```json
{
  "strategies": {
    "conservative": {
      "test_budget_ratio": 0.1
    },
    "balanced": {
      "test_budget_ratio": 0.15
    },
    "aggressive": {
      "test_budget_ratio": 0.25
    }
  }
}
```

### 3. A/B 样本量计算

命令：

```bash
python3 skills/growth-cro/ab-test-sample-size/main.py \
  --baseline-rate 0.1 \
  --mde 0.02 \
  --alpha 0.05 \
  --power 0.8
```

输出摘要：

```json
{
  "per_group_sample_size": 3841,
  "total_sample_size": 7682
}
```

### 4. 活动复盘自动摘要

命令：

```bash
python3 skills/analytics-attribution/campaign-retrospective-writer/main.py \
  --input-file skills/analytics-attribution/campaign-retrospective-writer/examples/input.json
```

输出摘要：

```json
{
  "summary": {
    "goal_count": 2,
    "highlight_count": 3,
    "issue_count": 3
  },
  "action_items": [
    "针对 成交数 复盘转化链路并补充下轮修正动作。",
    "下轮降低 短视频 的低效投放并重新验证素材与定向。"
  ]
}
```

## 测试结果

测试结果就应该直接写在 README 里，而不是放在聊天记录、提交说明或者脑子里。  
这版仓库已经在 **2026-03-23** 实际验证过以下内容：

| 验证项 | 命令 | 结果 |
| --- | --- | --- |
| skill 结构校验 | `python3 scripts/validate_skills.py` | 通过，识别到 23 个 skill 目录 |
| Python skill 单测 | `python3 -m unittest tests/test_python_skills.py` | 通过，4 个测试全部通过 |
| 关键词聚类示例 | `python3 skills/seo-geo-aeo/keyword-cluster-builder/main.py ...` | 通过，输出 2 个关键词簇 |
| 预算分配示例 | `python3 skills/paid-media/channel-budget-allocator/main.py ...` | 通过，输出 3 套预算策略 |
| A/B 样本量示例 | `python3 skills/growth-cro/ab-test-sample-size/main.py ...` | 通过，输出每组样本量 3841 |
| 活动复盘示例 | `python3 skills/analytics-attribution/campaign-retrospective-writer/main.py ...` | 通过，输出亮点、问题和行动项 |

如果你后面要继续增强展示效果，优先做这两件事：

1. 把这张表保留并持续更新
2. 再加 GitHub Actions，把同样的命令自动跑起来

## 推荐展示方式

如果你要把这个项目发给别人、发到群里、放到作品集或者开源主页，推荐按这个顺序展示：

1. 先截 README 里的 `Skill Map`
2. 再贴 `关键词聚类` 和 `预算分配` 两个真实输出
3. 最后贴 `测试结果` 表，说明这不是只写了文档，而是已经跑通过

这样别人能同时看到三件事：

- 你覆盖了哪些营销场景
- 这些场景不是空话，已经有可运行结果
- 这个仓库不是草稿，至少做过最基本的验证

## 如何新增一个 skill

1. 选择所属模块，并确定英文 slug 和中文标题
2. 在对应目录下创建 `skills/<module>/<skill-slug>/SKILL.md`
3. 按统一结构补全 `类型`、`说明`、`适用场景`、`输入`、`输出`、`执行流程`、`示例`
4. 如果是 Python skill，再补 `main.py` 和 `examples/`
5. 在模块级 `SKILLS.md` 中补登记
6. 更新本 README 中的 `Skill Map` 和 `完整文件清单`
7. 运行校验和测试

## 统一结构

每个独立 skill 目录都遵循同一套结构：

### Markdown skill
- `SKILL.md`

### Python skill
- `SKILL.md`
- `main.py`
- `examples/`

模块级还保留一个 `SKILLS.md`，用于快速浏览整个模块下的 skill 索引。

## 典型工作流

一个完整的营销工作流可以这样串起来：

1. `market-landscape-scan`：先看赛道趋势、机会和风险
2. `icp-builder` + `positioning-statement-crafter`：明确目标客户和定位
3. `content-strategy-planner` + `keyword-cluster-builder`：规划内容支柱和关键词结构
4. `multi-channel-rewriter` + `channel-budget-allocator`：准备内容分发和预算方案
5. `experiment-designer` + `ab-test-sample-size`：把优化点变成增长实验
6. `campaign-retrospective-writer`：活动结束后自动输出复盘

## 仓库结构

如果你只是想快速理解目录，看这一版简化结构就够了：

```text
marketing-skills/
├── README.md
├── .gitignore
├── scripts/
│   └── validate_skills.py
├── temp/
│   └── TODO.md
├── tests/
│   └── test_python_skills.py
└── skills/
    ├── market-research/
    ├── stp-brand/
    ├── content/
    ├── seo-geo-aeo/
    ├── paid-media/
    ├── growth-cro/
    ├── crm-private-domain/
    └── analytics-attribution/
```

## 完整文件清单

### Root
- `README.md`
- `.gitignore`
- `scripts/validate_skills.py`
- `temp/TODO.md`
- `tests/test_python_skills.py`

### analytics-attribution
- `skills/analytics-attribution/SKILLS.md`
- `skills/analytics-attribution/marketing-kpi-framework/SKILL.md`
- `skills/analytics-attribution/campaign-retrospective-writer/SKILL.md`
- `skills/analytics-attribution/campaign-retrospective-writer/main.py`
- `skills/analytics-attribution/campaign-retrospective-writer/examples/input.json`

### content
- `skills/content/SKILLS.md`
- `skills/content/content-strategy-planner/SKILL.md`
- `skills/content/editorial-calendar-generator/SKILL.md`
- `skills/content/multi-channel-rewriter/SKILL.md`

### crm-private-domain
- `skills/crm-private-domain/SKILLS.md`
- `skills/crm-private-domain/lifecycle-segmentation/SKILL.md`
- `skills/crm-private-domain/winback-automation-planner/SKILL.md`

### growth-cro
- `skills/growth-cro/SKILLS.md`
- `skills/growth-cro/ab-test-sample-size/SKILL.md`
- `skills/growth-cro/ab-test-sample-size/main.py`
- `skills/growth-cro/ab_test_sample_size.py`
- `skills/growth-cro/experiment-designer/SKILL.md`
- `skills/growth-cro/funnel-diagnostics/SKILL.md`

### market-research
- `skills/market-research/SKILLS.md`
- `skills/market-research/market-landscape-scan/SKILL.md`
- `skills/market-research/competitor-gap-analysis/SKILL.md`
- `skills/market-research/user-voice-mining/SKILL.md`

### paid-media
- `skills/paid-media/SKILLS.md`
- `skills/paid-media/channel-budget-allocator/SKILL.md`
- `skills/paid-media/channel-budget-allocator/main.py`
- `skills/paid-media/channel-budget-allocator/examples/channels.json`
- `skills/paid-media/ad-angle-generator/SKILL.md`
- `skills/paid-media/ad-copy-variant-generator/SKILL.md`

### seo-geo-aeo
- `skills/seo-geo-aeo/SKILLS.md`
- `skills/seo-geo-aeo/keyword-cluster-builder/SKILL.md`
- `skills/seo-geo-aeo/keyword-cluster-builder/main.py`
- `skills/seo-geo-aeo/keyword-cluster-builder/examples/keywords.txt`
- `skills/seo-geo-aeo/serp-intent-analyzer/SKILL.md`
- `skills/seo-geo-aeo/page-seo-optimizer/SKILL.md`
- `skills/seo-geo-aeo/answer-engine-optimizer/SKILL.md`

### stp-brand
- `skills/stp-brand/SKILLS.md`
- `skills/stp-brand/icp-builder/SKILL.md`
- `skills/stp-brand/persona-generator/SKILL.md`
- `skills/stp-brand/positioning-statement-crafter/SKILL.md`

## Roadmap

### v0.1
- 完成模块级索引
- 完成 23 个独立 skill 目录
- 完成 4 个 Python skills
- 补齐示例、校验脚本和最小测试

### v0.2
- 为更多 skill 增加输入模板和输出模板
- 增加批量生成器和脚手架
- 增加更多营销分析型工具

### v0.3
- 引入更完整的测试数据集
- 增加多语言版本
- 支持更复杂的工作流组合和自动化编排
