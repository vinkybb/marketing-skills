# campaign-retrospective-writer（活动复盘生成）

## 类型
Python Skill

## 说明
用于输入活动目标、执行数据和异常记录，自动输出亮点、问题和下一步行动项。

## 适用场景
- 活动结束后需要快速沉淀可执行经验与下一轮动作

## 输入
### 必填
- 活动目标
- 执行数据
- 素材表现
- 异常记录

### 可选
- 渠道成本
- 线索质量
- 团队反馈

## 输出
- 结果摘要
- 成功因素
- 问题归因
- 下周期优化建议

## 执行流程
1. 对比目标与结果。
2. 标记亮点与偏差。
3. 生成问题归因。
4. 输出行动项与优先级。

## 命令行
- 脚本路径：`skills/analytics-attribution/campaign-retrospective-writer/main.py`
- 输入方式：使用 `--input-file` 传入 JSON

## 示例
### 输入示例
`活动=新品首发，目标=500 条有效线索`

### 示例命令
```bash
python3 skills/analytics-attribution/campaign-retrospective-writer/main.py \
  --input-file temp/retrospective_input.json
```

### 输出示例
- highlights：表现超预期的指标与渠道
- issues：偏差最大的指标和归因
- action_items：下轮优先优化动作

