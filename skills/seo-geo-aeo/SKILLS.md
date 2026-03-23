# 模块：SEO / GEO / AEO

## 10) keyword-cluster-builder（关键词聚类）
- Use When：构建内容矩阵、优化站点主题权重、规划栏目结构
- Inputs（必填）：种子关键词、业务领域、语言/地域
- Inputs（可选）：搜索量、词难度、商业价值标签
- Outputs：关键词簇、主词-长尾映射、内容优先级清单
- Workflow：扩词 → 去噪 → 意图聚类 → 机会排序
- Python 实现：`skills/seo-geo-aeo/keyword-cluster-builder/main.py`
- 示例命令：`python3 skills/seo-geo-aeo/keyword-cluster-builder/main.py --business-domain "私域增长" --locale zh-CN --keywords-file skills/seo-geo-aeo/keyword-cluster-builder/examples/keywords.txt`
- 示例输入：`种子词=私域运营/用户召回/会员体系`

## 11) serp-intent-analyzer（SERP 意图分析）
- Use When：写内容前先判断搜索意图和结果页竞争结构
- Inputs（必填）：关键词列表、目标搜索引擎
- Inputs（可选）：竞品 URL、目标排名区间
- Outputs：意图标签、内容类型建议、页面结构建议
- Workflow：采样结果页 → 分类意图 → 总结头部特征 → 输出结构建议
- 示例输入：`关键词=营销自动化工具推荐`

## 12) page-seo-optimizer（页面 SEO 优化器）
- Use When：老页面流量下滑、新页面上线前质量检查
- Inputs（必填）：页面内容、目标关键词、页面目标
- Inputs（可选）：站内链接策略、FAQ 池、品牌术语
- Outputs：标题与描述建议、H 结构建议、FAQ 与内链建议、修复清单
- Workflow：结构审查 → 关键词布局 → 可读性优化 → 技术检查
- 示例输入：`页面=产品页，关键词=线索培育系统`

## 13) answer-engine-optimizer（AEO 答案引擎优化）
- Use When：希望提升在 AI 问答结果中的可见度与引用概率
- Inputs（必填）：目标问题集合、现有内容、品牌主张
- Inputs（可选）：可信来源链接、术语规范
- Outputs：高密度问答块、可引用段落、证据增强建议
- Workflow：问题标准化 → 生成答案块 → 增强可验证性 → 语义统一
- 示例输入：`问题集=客户常见 30 问，品牌主张=高转化低成本`
