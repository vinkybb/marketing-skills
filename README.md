# Marketing Skills（中文）

面向 OpenClaw 的营销技能合集，目标是让本地 AI Agent 能直接执行市场研究、内容生产、广告优化、增长实验与复盘分析等常见营销工作。

当前版本采用“模块化 skill + 可组合工作流”的方式实现：
- 策略型任务优先用 Markdown Skill（快、易扩展、可审阅）
- 需要计算或结构化处理的任务可配合 Python Skill

## 项目目标

- 覆盖大部分高频营销场景（目标覆盖约 80%）
- 全部中文化输出，适配中文营销语境
- 每个 skill 都具备清晰的输入、输出、执行步骤与交付模板

## Skills 大纲（Marketing）

### 1. 市场研究与洞察
- 行业扫描与趋势识别
- 竞品分析与差异化机会
- 用户评论挖掘与痛点聚类
- 机会地图与优先级评估

### 2. STP 与品牌定位
- 用户细分（Segmentation）
- 目标市场选择（Targeting）
- 品牌定位声明（Positioning）
- ICP / Persona 构建与价值主张提炼

### 3. 内容营销（Content）
- 内容策略与选题规划
- 多平台内容改写（公众号/小红书/知乎/抖音等）
- 内容日历与发布节奏设计
- A/B 文案变体生成

### 4. SEO / GEO / AEO
- 关键词研究与关键词聚类
- 搜索意图分析与 SERP 拆解
- 页面优化清单（标题、结构、FAQ、内链）
- 面向 AI 问答引擎的答案可见性优化

### 5. 广告投放与创意优化（Paid Media）
- 渠道与预算分配建议
- 受众策略与创意方向定义
- 广告文案与素材脚本批量生成
- 落地页信息一致性检查

### 6. 增长与转化（Growth / CRO）
- 增长漏斗诊断（AARRR）
- 实验设计（A/B Test）
- ICE / RICE 优先级排序
- 转化率优化与流失环节修复

### 7. CRM 与私域运营
- 生命周期分层策略
- 自动化触达流程设计
- 召回/复购/会员运营策略
- 社群运营 SOP

### 8. 数据分析与归因
- 核心指标体系定义
- 活动复盘模板
- 渠道归因分析框架
- ROI 预算复盘与下周期建议

## 目录结构

```text
marketing-skills/
├── README.md
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

## Skill 规范（统一模板）

每个 skill 建议包含：
- `name`：技能名称（英文目录名 + 中文显示名）
- `when_to_use`：适用场景
- `inputs`：输入参数（必填/可选）
- `workflow`：执行步骤
- `outputs`：输出结构（可直接交付）
- `example`：示例输入输出

## 当前实现状态

- 已完成：README 大纲与首批技能规划
- 已完成：8 大模块、22 个中文 Markdown skills 初版落地
- 已完成：1 个 Python skill（A/B 样本量计算器）
- 下一步：继续补充 Python 型 skills（关键词聚类、预算分配、复盘自动化）
