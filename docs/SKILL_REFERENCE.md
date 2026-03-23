# Skill Reference

这份文档用于快速查阅每个 skill 的定位、输入、输入示意、实现方式和示例交付。  
表格里的内容主要用于帮助理解每个 skill 的输出形态和使用方式。

| 模块 | Skill | 作用 | 输入 | 输入示意 | 实现方式 | 示例交付 |
| --- | --- | --- | --- | --- | --- | --- |
| Market Research | `market-landscape-scan` | 快速判断一个营销赛道的规模、趋势、机会和风险。 | 行业名称、目标市场、时间窗口、分析维度 | `帮我看一下 AI 外呼 在中国市场近 24 个月的行业机会，重点看规模、竞争和渠道。` | Markdown Skill | `行业概览：AI 外呼市场近 24 个月保持高增速；机会点：中小企业线索自动化；风险：合规与数据质量。` |
| Market Research | `competitor-gap-analysis` | 对比我方和竞品在产品、内容、渠道、价格上的差距，输出突破方向。 | 我方产品简介、竞品列表、对比维度 | `我们做营销自动化，帮我对比 3 家竞品在价格、功能、内容和渠道上的差距，给我突破建议。` | Markdown Skill | `竞品差距矩阵：我方在内容教育和案例沉淀上偏弱；90 天建议：优先补案例页、搜索词承接页和销售话术。` |
| Market Research | `user-voice-mining` | 从评论、客服记录和社区讨论中提炼用户痛点、抱怨和真实需求。 | 评论文本、平台来源、目标用户类型 | `这是 500 条小红书评论和客服工单，帮我提炼用户最常见的抱怨点和需求。` | Markdown Skill | `高频痛点：上手门槛高、效果反馈慢、价格解释不清；建议：补首屏解释、上线 FAQ、增加案例证据。` |
| STP & Brand | `icp-builder` | 从高价值客户样本中抽出理想客户画像和排除画像。 | 高价值客户样本、行业或角色信息、客单价或生命周期价值 | `根据过去半年成交客户，帮我总结最值得投放的人群画像，顺便告诉我应该排除哪些客户。` | Markdown Skill | `ICP：20-100 人 SaaS 公司市场负责人；排除画像：预算小于 1 万、无内容团队、决策周期过短。` |
| STP & Brand | `persona-generator` | 把目标客群细化成多个可用于内容、投放、销售沟通的角色卡。 | 目标人群、核心任务、购买阻力、决策链角色 | `我们的客户里有老板、市场经理和运营，帮我拆成 3 个 Persona，写清目标、痛点和阻碍。` | Markdown Skill | `Persona A：增长负责人，关注 ROI 和归因；Persona B：老板，关注获客成本和确定性；Persona C：运营，关注执行复杂度。` |
| STP & Brand | `positioning-statement-crafter` | 生成品牌定位声明、价值主张和禁用表达。 | 目标客群、品类、核心收益、差异化证据 | `我们是做营销自动化的，目标客户是中型 B2B 团队，核心优势是提升线索到成交效率，帮我写定位。` | Markdown Skill | `定位声明：面向中型 B2B 团队的营销自动化平台，帮助市场团队缩短线索到成交周期。` |
| Content | `content-strategy-planner` | 规划内容支柱、栏目结构、漏斗阶段内容分工和发布节奏。 | 业务目标、目标用户、主阵地平台、内容资源 | `下个季度我要靠内容拿线索，主阵地是公众号和视频号，团队 2 个人，帮我做内容策略。` | Markdown Skill | `内容支柱：行业趋势 / 实战案例 / 方法论 / 产品教育；节奏：每周 3 篇图文 + 2 条短视频。` |
| Content | `editorial-calendar-generator` | 把内容策略变成月度或周度排期表。 | 月份、主题池、营销节点、平台优先级 | `帮我做 4 月内容日历，包含新品发布和五一节点，平台优先级是公众号、小红书、视频号。` | Markdown Skill | `第 1 周：行业趋势解读；第 2 周：客户案例拆解；第 3 周：工具清单；第 4 周：活动预热。` |
| Content | `multi-channel-rewriter` | 把一份核心内容快速改成适合公众号、小红书、知乎、短视频的平台版本。 | 原始内容、目标平台、字数限制、语气风格 | `这是一篇 2000 字长文，帮我改成公众号、小红书和抖音口播三个版本，语气更直接一点。` | Markdown Skill | `公众号版：方法论长文；小红书版：清单体表达；抖音版：30 秒口播脚本 + 开头钩子。` |
| SEO / GEO / AEO | `keyword-cluster-builder` | 把一组关键词聚成主题簇，方便搭建内容矩阵和栏目结构。 | 关键词列表、业务领域、语言或地域 | `我有一批关键词：私域运营、用户召回、会员体系、积分体系，帮我自动聚类。` | Python Skill | `cluster_1：私域运营 / 私域用户召回；cluster_2：会员体系搭建 / 会员积分体系。` |
| SEO / GEO / AEO | `serp-intent-analyzer` | 判断关键词背后的搜索意图和头部结果页模式。 | 关键词列表、目标搜索引擎 | `帮我分析“营销自动化工具推荐”这个词的搜索意图，看看适合写什么内容。` | Markdown Skill | `关键词“营销自动化工具推荐”对应商业调查意图；建议内容形式：榜单 + 评测维度 + 对比表。` |
| SEO / GEO / AEO | `page-seo-optimizer` | 为单页内容给出标题、结构、FAQ、内链等 SEO 优化建议。 | 页面内容、目标关键词、页面目标 | `这是我们的产品页，目标关键词是“线索培育系统”，帮我做 SEO 优化建议。` | Markdown Skill | `建议标题：线索培育系统怎么选；建议补充：FAQ 3 条、案例模块 1 个、内链到价格页和案例页。` |
| SEO / GEO / AEO | `answer-engine-optimizer` | 让内容更适合被 AI 问答系统引用，输出高密度问答块和证据增强建议。 | 目标问题集合、现有内容、品牌主张 | `我有 30 个客户常问问题，帮我整理成更容易被 AI 问答系统引用的内容结构。` | Markdown Skill | `问答块：什么是线索培育系统；补充建议：加入定义、适用场景、可信来源和结构化问答。` |
| Paid Media | `channel-budget-allocator` | 根据预算、目标和渠道表现，输出保守、均衡、激进三套预算方案。 | 总预算、目标类型、候选渠道、历史表现数据 | `我有 50 万预算，目标是拿线索，渠道是搜索、信息流、短视频，帮我给三套预算分法。` | Python Skill | `保守：搜索 40%，短视频 39%，信息流 21%；激进：短视频 50%，信息流 33%，搜索 17%。` |
| Paid Media | `ad-angle-generator` | 围绕卖点和目标人群扩展广告创意方向。 | 产品卖点、目标人群、投放平台 | `产品卖点是 7 天见效，用户是中小企业主，平台是抖音，帮我想几组广告角度。` | Markdown Skill | `角度 1：痛点型“线索跟进太慢”；角度 2：对比型“人工跟进 vs 自动培育”；角度 3：场景型“老板每天盯报表”。` |
| Paid Media | `ad-copy-variant-generator` | 为同一创意方向生成多组文案变体，方便 A/B 测试。 | 创意角度、字数限制、CTA 类型、平台规范 | `按痛点型角度帮我写 3 组广告文案，每条 45 字以内，CTA 是立即咨询。` | Markdown Skill | `变体 A：直接痛点 + CTA；变体 B：收益承诺 + CTA；变体 C：案例证据 + CTA。` |
| Growth / CRO | `funnel-diagnostics` | 分析曝光、点击、注册、激活、付费等环节中的瓶颈。 | 漏斗数据 | `这是近 30 天的曝光、点击、注册、激活、付费数据，帮我找出漏斗里最卡的地方。` | Markdown Skill | `异常段：点击到注册转化率低；可能原因：落地页信息不一致；建议：优化首屏和表单长度。` |
| Growth / CRO | `experiment-designer` | 把增长想法变成可执行、可验证的实验方案。 | 实验目标、基线指标、可改动变量、实验周期 | `我想提升注册转化 15%，能动的变量是表单长度和按钮文案，帮我设计实验。` | Markdown Skill | `实验假设：缩短注册表单字段数可提升注册率 15%；分组：控制组 vs 两组实验组；周期：14 天。` |
| Growth / CRO | `ab-test-sample-size` | 估算实验每组最少需要多少样本量。 | `baseline_rate`、`mde`、`alpha`、`power` | `基线转化率 10%，最小可检测提升 2%，显著性 0.05，power 0.8，帮我算样本量。` | Python Skill | `输入：baseline_rate=0.1, mde=0.02；输出：per_group_sample_size=3841, total_sample_size=7682。` |
| CRM & Private Domain | `lifecycle-segmentation` | 基于行为和交易数据做用户生命周期分层。 | 用户行为数据、交易记录、最近活跃时间 | `帮我按新客、活跃、沉睡、高价值做用户分层，并给每层的运营建议。` | Markdown Skill | `分层结果：新客 / 活跃 / 沉睡 / 高价值；运营动作：新客教育、活跃促活、沉睡召回、高价值会员权益。` |
| CRM & Private Domain | `winback-automation-planner` | 为沉睡用户设计多触点召回流程。 | 目标人群、可用渠道、权益资源、触达频控规则 | `我们想召回沉睡用户，可用短信、企微、公众号，7 天最多触达 3 次，帮我设计流程。` | Markdown Skill | `召回流程：短信首触达 -> 企微补触达 -> 公众号权益提醒；监控指标：打开率、回流率、复购率。` |
| Analytics & Attribution | `marketing-kpi-framework` | 为营销团队搭建北极星指标、分层指标树和预警机制。 | 业务目标、数据字段、现有报表结构 | `我们的目标是季度新增付费用户，帮我设计一套北极星指标和分层指标体系。` | Markdown Skill | `北极星指标：新增付费用户数；支撑指标：线索量、转化率、CAC、留存率；预警阈值：CAC 环比上涨 20%。` |
| Analytics & Attribution | `campaign-retrospective-writer` | 根据活动目标、执行数据和异常记录自动生成复盘摘要。 | 活动目标、执行数据、素材表现、异常记录 | `这是新品首发活动的数据，帮我自动写一版复盘，拆出亮点、问题和行动项。` | Python Skill | `亮点：有效线索达成率 108%；问题：短视频 CPA 偏高；行动项：减少低效投放并补充新素材。` |

## Python Skills 补充说明

| Skill | 输入形式 | 典型命令 | 主要输出 |
| --- | --- | --- | --- |
| `keyword-cluster-builder` | `--keyword` 重复传参，或 `--keywords-file` | `python3 skills/seo-geo-aeo/keyword-cluster-builder/main.py --business-domain "私域增长" --locale zh-CN --keywords-file skills/seo-geo-aeo/keyword-cluster-builder/examples/keywords.txt` | JSON：关键词数量、簇列表、标签、优先级 |
| `channel-budget-allocator` | `--channels-file` 传入 JSON 渠道数据 | `python3 skills/paid-media/channel-budget-allocator/main.py --total-budget 500000 --goal leads --channels-file skills/paid-media/channel-budget-allocator/examples/channels.json` | JSON：保守 / 均衡 / 激进三套预算方案 |
| `ab-test-sample-size` | 命令行参数输入实验参数 | `python3 skills/growth-cro/ab-test-sample-size/main.py --baseline-rate 0.1 --mde 0.02 --alpha 0.05 --power 0.8` | JSON：每组样本量、总样本量、参数回显 |
| `campaign-retrospective-writer` | `--input-file` 传入活动 JSON | `python3 skills/analytics-attribution/campaign-retrospective-writer/main.py --input-file skills/analytics-attribution/campaign-retrospective-writer/examples/input.json` | JSON：summary、highlights、issues、action_items |
