# keyword-cluster-builder（关键词聚类）

## 类型
Python Skill

## 说明
用于输入关键词列表后输出主题簇、主词标签与内容优先级建议，适合做 SEO 内容矩阵和栏目规划。

## 适用场景
- 构建内容矩阵、优化站点主题权重、规划栏目结构

## 输入
### 必填
- 关键词列表
- 业务领域
- 语言或地域

### 可选
- 搜索量
- 词难度
- 商业价值标签
- 最低相似度阈值

## 输出
- 关键词簇列表
- 主词标签
- 主词与长尾映射
- 内容优先级建议

## 执行流程
1. 标准化关键词文本。
2. 计算相似度并完成聚类。
3. 为每个簇生成标签与主词。
4. 输出结构化 JSON 结果。

## 命令行
- 脚本路径：`skills/seo-geo-aeo/keyword-cluster-builder/main.py`
- 输入方式：`--keyword` 重复传参，或使用 `--keywords-file`

## 示例
### 输入示例
`种子词=私域运营/用户召回/会员体系`

### 示例命令
```bash
python3 skills/seo-geo-aeo/keyword-cluster-builder/main.py \
  --business-domain "私域增长" \
  --locale "zh-CN" \
  --keyword "私域运营" \
  --keyword "私域用户召回" \
  --keyword "会员体系搭建"
```

### 输出示例
- cluster_1：私域运营、私域用户召回
- cluster_2：会员体系搭建
- 每个簇包含标签、关键词列表与建议优先级

