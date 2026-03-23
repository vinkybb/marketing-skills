# channel-budget-allocator（渠道预算分配）

## 类型
Python Skill

## 说明
用于根据总预算、渠道表现和风险偏好，输出保守、均衡、激进三套预算分配方案。

## 适用场景
- 季度预算规划、投放结构重配、获客成本持续上升

## 输入
### 必填
- 总预算
- 目标类型
- 候选渠道
- 历史表现数据

### 可选
- 毛利率
- 投放周期
- 风险偏好

## 输出
- 渠道预算拆分建议
- 测试预算比例
- 保守方案
- 均衡方案
- 激进方案

## 执行流程
1. 解析渠道指标。
2. 对效率、稳定性与扩量潜力做归一化评分。
3. 按三种策略生成预算比例。
4. 输出结构化 JSON 结果。

## 命令行
- 脚本路径：`skills/paid-media/channel-budget-allocator/main.py`
- 输入方式：使用 `--channels-file` 传入 JSON 渠道列表

## 示例
### 输入示例
`预算=50 万/月，目标=线索量，渠道=抖音/信息流/搜索`

### 示例命令
```bash
python3 skills/paid-media/channel-budget-allocator/main.py \
  --total-budget 500000 \
  --goal leads \
  --channels-file temp/channels.json
```

### 输出示例
- conservative：更高权重给稳定渠道
- balanced：兼顾效率与扩量
- aggressive：提高高潜渠道与测试预算

