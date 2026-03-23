# 模块：广告投放与创意优化（Paid Media）

## 14) channel-budget-allocator（渠道预算分配）
- Use When：季度预算规划、投放结构重配、获客成本持续上升
- Inputs（必填）：总预算、目标类型、候选渠道、历史表现数据
- Inputs（可选）：毛利率、投放周期、风险偏好
- Outputs：预算拆分建议、测试预算比例、保守/均衡/激进三套方案
- Workflow：目标分解 → 渠道能力评估 → 预算切分 → 风险校准
- Python 实现：`skills/paid-media/channel-budget-allocator/main.py`
- 示例命令：`python3 skills/paid-media/channel-budget-allocator/main.py --total-budget 500000 --goal leads --channels-file skills/paid-media/channel-budget-allocator/examples/channels.json`
- 示例输入：`预算=50 万/月，目标=线索量，渠道=抖音/信息流/搜索`

## 15) ad-angle-generator（广告创意角度生成）
- Use When：CTR 下滑、素材疲劳、需要快速扩展创意池
- Inputs（必填）：产品卖点、目标人群、投放平台
- Inputs（可选）：禁用表达、品牌语调、竞品广告样本
- Outputs：利益型/痛点型/对比型/场景型角度与标题方向
- Workflow：拆解卖点 → 映射受众动机 → 生成角度 → 首轮筛选
- 示例输入：`卖点=7 天见效，受众=中小企业主，平台=抖音`

## 16) ad-copy-variant-generator（广告文案变体生成）
- Use When：同一素材需要批量 A/B 测试不同文案结构
- Inputs（必填）：创意角度、字数限制、CTA 类型、平台规范
- Inputs（可选）：落地页承接点、优惠信息、品牌名出现频次
- Outputs：短文案/中长文案、首句钩子、CTA 变体、测试分组建议
- Workflow：选择结构模板 → 生成多变体 → 合规检查 → 输出分组方案
- 示例输入：`角度=痛点型，CTA=立即咨询，字数<45`
