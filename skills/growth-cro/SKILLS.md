# 模块：增长与转化（Growth / CRO）

## 17) funnel-diagnostics（增长漏斗诊断）
- Use When：转化停滞、不同渠道表现差异大、核心环节效率未知
- Inputs（必填）：曝光/点击/注册/激活/付费等漏斗数据
- Inputs（可选）：分渠道/分人群数据、活动周期、版本变更记录
- Outputs：瓶颈环节、可能原因、修复优先级、预估收益
- Workflow：拆分漏斗 → 标记异常环节 → 假设归因 → 形成行动清单
- 示例输入：`周期=近 30 天，分渠道=搜索/信息流/私域`

## 18) experiment-designer（增长实验设计）
- Use When：需要把优化建议转为可验证的增长实验
- Inputs（必填）：实验目标、基线指标、可改动变量、实验周期
- Inputs（可选）：风险约束、流量上限、工程依赖
- Outputs：实验假设、分组设计、成功判定标准、复盘框架
- Workflow：提出假设 → 设计对照实验 → 设定指标与阈值 → 准备复盘模板
- 示例输入：`目标=注册转化+15%，变量=表单长度/按钮文案`

## 23) ab-test-sample-size（A/B 样本量计算器）
- Use When：上线实验前估算每组需要的最小样本量
- Inputs（必填）：`baseline_rate`、`mde`、`alpha`、`power`
- Outputs：每组样本量、总样本量、参数回显（JSON）
- Workflow：读取参数 → 计算双侧比例检验样本量 → 返回结构化结果
- Python 实现：`skills/growth-cro/ab-test-sample-size/main.py`
- 兼容旧路径：`skills/growth-cro/ab_test_sample_size.py`
- 示例命令：`python3 skills/growth-cro/ab-test-sample-size/main.py --baseline-rate 0.1 --mde 0.02 --alpha 0.05 --power 0.8`
