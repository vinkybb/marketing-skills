# ab-test-sample-size（A/B 样本量计算器）

## 类型
Python Skill

## 说明
用于在实验开始前估算每组需要的最小样本量，便于判断实验周期与流量需求。基于**双侧**比例检验的渐近公式。

**`mde` 含义（重要）**：命令行参数 `--mde` 表示**绝对转化率差**，即备择比例 = `baseline_rate + mde`（均为 0–1 内的小数）。例如基线 10%（0.1）、mde 0.02 表示期望检出备择组约 **12%**（0.12），而不是「相对基线 +20%」。若你习惯相对提升，请先换算为绝对差再输入。

## 适用场景
- 上线实验前估算每组需要的最小样本量

## 输入
### 必填
- `baseline_rate`：基线转化率（0–1）
- `mde`：最小可检测的**绝对**转化率提升（0–1），见上文说明

### 可选
- `alpha`：显著性水平，默认 `0.05`
- `power`：统计功效，默认 `0.8`

## 输出
- 每组样本量
- 总样本量
- 参数回显

## 执行流程
1. 读取输入参数。
2. 计算双侧比例检验样本量。
3. 输出结构化 JSON 结果。

## 命令行
- 脚本路径：`skills/growth-cro/ab-test-sample-size/main.py`

## 示例
### 输入示例
`baseline_rate=0.1, mde=0.02, alpha=0.05, power=0.8`

### 示例命令
```bash
python3 skills/growth-cro/ab-test-sample-size/main.py \
  --baseline-rate 0.1 \
  --mde 0.02 \
  --alpha 0.05 \
  --power 0.8
```

### 输出示例
- `per_group_sample_size`
- `total_sample_size`
- 参数回显 JSON

