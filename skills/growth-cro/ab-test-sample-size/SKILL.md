# ab-test-sample-size（A/B 样本量计算器）

## 类型
Python Skill

## 说明
用于在实验开始前估算每组需要的最小样本量，便于判断实验周期与流量需求。

## 适用场景
- 上线实验前估算每组需要的最小样本量

## 输入
### 必填
- `baseline_rate`
- `mde`
- `alpha`
- `power`

### 可选
- 无

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

