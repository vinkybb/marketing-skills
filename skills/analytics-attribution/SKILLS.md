# 模块：数据分析与归因（Analytics & Attribution）

## 21) marketing-kpi-framework（营销指标体系搭建）
- Use When：指标口径不统一、团队只看表面数据、难以驱动决策
- Inputs（必填）：业务目标、数据字段、现有报表结构
- Inputs（可选）：组织角色、指标刷新频率、阈值偏好
- Outputs：北极星指标、分层指标树、统一口径说明、预警阈值
- Workflow：目标对齐 → 指标分层 → 口径统一 → 预警机制定义
- 示例输入：`目标=新增付费用户，周期=季度，渠道=全渠道`

## 22) campaign-retrospective-writer（活动复盘生成）
- Use When：活动结束后需要快速沉淀可执行经验与下一轮动作
- Inputs（必填）：活动目标、执行数据、素材表现、异常记录
- Inputs（可选）：渠道成本、线索质量、团队反馈
- Outputs：结果摘要、成功因素、问题归因、下周期优化建议
- Workflow：目标回看 → 数据对照 → 问题归因 → 形成可执行结论
- Python 实现：`skills/analytics-attribution/campaign-retrospective-writer/main.py`
- 示例命令：`python3 skills/analytics-attribution/campaign-retrospective-writer/main.py --input-file skills/analytics-attribution/campaign-retrospective-writer/examples/input.json`
- 示例输入：`活动=新品首发，目标=500 条有效线索`
