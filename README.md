# Marketing Skills

> 专为营销与增长团队打造的开源 AI Skill 库。赋予本地 Agent 接管和执行复杂营销任务的能力。

## 为什么做这个项目

大多数营销 AI 工具只能生成文案，但真实营销工作远比这复杂：
- 做市场研究时，需要快速扫描行业格局、识别机会与风险
- 定用户定位时，需要构建 ICP、输出 Persona、提炼定位声明
- 规划内容时，需要设计内容支柱、关键词聚类、多平台改写
- 投放广告时，需要预算分配、创意角度、文案变体
- 做增长实验时，需要漏斗诊断、实验设计、样本量计算
- 活动结束后，需要复盘归因、输出行动项

这个仓库将营销完整工作流拆解为 23 个独立 Skill，每个 Skill 都是「可消费的说明文档 + 可直接运行的代码」。

本地 AI Agent 可以读取 Skill 定义、理解输入输出、执行复杂任务。

## 核心场景覆盖

| 模块 | 能力 | Skill 示例 |
|------|------|-----------|
| 市场研究 | 行业扫描、竞品分析、用户声音挖掘 | `market-landscape-scan` |
| 用户定位 | ICP 构建、Persona 生成、定位声明 | `icp-builder`, `positioning-statement-crafter` |
| 内容规划 | 内容战略、发布日历、多平台改写 | `content-strategy-planner`, `multi-channel-rewriter` |
| SEO/GEO/AEO | 关键词聚类、SERP 分析、页面优化 | `keyword-cluster-builder` |
| 付费投放 | 渠道预算分配、广告创意、文案变体 | `channel-budget-allocator`, `ad-angle-generator` |
| 增长实验 | 漏斗诊断、实验设计、A/B 样本量计算 | `experiment-designer`, `ab-test-sample-size` |
| 私域运营 | 生命周期分层、召回自动化 | `lifecycle-segmentation` |
| 数据分析 | 指标体系、活动复盘 | `campaign-retrospective-writer` |

## 30 秒上手

```bash
# 1. 查看所有 Skill
ls skills/*/

# 2. 运行一个 Python Skill（关键词聚类）
python3 skills/seo-geo-aeo/keyword-cluster-builder/main.py \
  --business-domain "私域增长" \
  --locale zh-CN \
  --keywords-file skills/seo-geo-aeo/keyword-cluster-builder/examples/keywords.txt

# 3. 运行验证
python3 scripts/validate_skills.py
python3 -m unittest tests/test_python_skills.py
```

## 完整示例

### 渠道预算分配

```bash
python3 skills/paid-media/channel-budget-allocator/main.py \
  --total-budget 500000 \
  --goal leads \
  --channels-file skills/paid-media/channel-budget-allocator/examples/channels.json
```

输出：
```json
{
  "strategies": {
    "conservative": { "test_budget_ratio": 0.1 },
    "balanced": { "test_budget_ratio": 0.15 },
    "aggressive": { "test_budget_ratio": 0.25 }
  }
}
```

### A/B 测试样本量计算

```bash
python3 skills/growth-cro/ab-test-sample-size/main.py \
  --baseline-rate 0.1 \
  --mde 0.02 \
  --alpha 0.05 \
  --power 0.8
```

输出：
```json
{
  "per_group_sample_size": 3841,
  "total_sample_size": 7682
}
```

### 活动复盘

```bash
python3 skills/analytics-attribution/campaign-retrospective-writer/main.py \
  --input-file skills/analytics-attribution/campaign-retrospective-writer/examples/input.json
```

输出：复盘摘要、问题归因、可执行行动项

## 给 AI Agent 用

每个 Skill 都遵循统一结构，Agent 可以：

1. **读取 Skill 定义** → `skills/<module>/<skill>/SKILL.md`
2. **理解输入输出** → 查看文档中的 `输入` 和 `输出` 章节
3. **执行或调用** → 直接运行 `main.py` 或通过 API 调用

典型工作流串联：
```
market-landscape-scan → icp-builder → content-strategy-planner 
→ channel-budget-allocator → experiment-designer → campaign-retrospective-writer
```

## 仓库结构

```
marketing-skills/
├── skills/              # 23 个独立 Skill，按模块分组
│   ├── market-research/
│   ├── stp-brand/
│   ├── content/
│   ├── seo-geo-aeo/
│   ├── paid-media/
│   ├── growth-cro/
│   ├── crm-private-domain/
│   └── analytics-attribution/
├── scripts/             # 结构校验脚本
├── tests/               # 最小可运行测试
└── docs/                # 速查手册
```

## 文档索引

- [Skill 速查表](docs/SKILL_REFERENCE.md) - 按场景整理，适合"我有一个任务但不知道该用哪个 Skill"
- [模块索引](skills/market-research/SKILLS.md) - 各模块下的完整 Skill 列表

## 新增 Skill

1. 在 `skills/<module>/<skill-slug>/` 创建目录
2. 编写 `SKILL.md`（类型、说明、输入、输出、流程、示例）
3. 如需要可执行代码，添加 `main.py` 和 `examples/`
4. 更新模块级 `SKILLS.md`
5. 运行校验和测试

## 许可证

[MIT](LICENSE)
