---
layout: default
title: "Horizon Summary: 2026-08-01 (ZH)"
date: 2026-08-01
lang: zh
---

> 从 112 条内容中筛选出 7 条重要资讯。

---

1. [睡眠基础模型预测未来疾病风险。](#item-1) ⭐️ 8.5/10
2. [无状态 MCP 2.0 让智能体工具协议重获实用性](#item-2) ⭐️ 8.0/10
3. [KAISEN 压力测试临床模型公平性审计。](#item-3) ⭐️ 8.0/10
4. [Anthropic 提出用代码执行提升 MCP 智能体效率](#item-4) ⭐️ 8.0/10
5. [PolyAI 推出 Dialog-RSN-1 音频原生语音模型。](#item-5) ⭐️ 7.0/10
6. [面向流动网络的疫情再生数指标](#item-6) ⭐️ 7.0/10
7. [Transformer 根据胰岛素和碳水预测血糖](#item-7) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [睡眠基础模型预测未来疾病风险。](https://news.google.com/rss/articles/CBMiX0FVX3lxTE1Bb18waG5OdVN5MEEyNFhpMFJfN05fQmxVNjRXb2tLV2hubmlQczQxUTQzRDd1Y216TlZ6d0VTaEFZakRRaFBVLVRyRGNaaS00SHU4ZkJnMFcxbTFoendR?oc=5) ⭐️ 8.5/10

2026 年 1 月 6 日发表在《Nature Medicine》的一项研究报告了一种深度学习多模态睡眠基础模型，该模型基于多导睡眠监测记录开发。该模型能够完成常见睡眠分析任务，并利用睡眠数据预测未来疾病风险。 睡眠记录包含大脑、心脏、呼吸和肌肉活动等长期、无创信号，因此可能成为可规模化风险分层的重要数据来源。这项工作还表明，基础模型方法有望降低睡眠医学和数字健康工作流程对人工标注数据的依赖。 该模型使用多导睡眠监测产生的丰富多模态数据，而非单一睡眠信号；作者将这一方法描述为学习“睡眠语言”。现有材料尚未说明队列规模、外部验证结果、校准情况、前瞻性临床效用、部署成熟度或模型可用性。

google\_news · Nature · 1月6日 08:00

**背景**: 多导睡眠监测是一种临床睡眠检查，会在睡眠期间记录多种生理信号。这些信号可包括脑活动、心脏活动、呼吸和肌肉活动，从而支持对睡眠模式和睡眠障碍的评估。基础模型通常通过大规模数据学习可广泛复用的表征，随后可用较少的特定任务标注数据支持多个下游任务。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.nature.com/articles/s41591-025-04133-4">A multimodal sleep foundation model for disease prediction</a></li>
<li><a href="https://pubmed.ncbi.nlm.nih.gov/41495409/">A multimodal sleep foundation model for disease prediction</a></li>

</ul>
</details>

**标签**: `#medical-ai`, `#foundation-models`, `#digital-health`, `#sleep-medicine`, `#disease-prediction`

---

<a id="item-2"></a>
## [无状态 MCP 2.0 让智能体工具协议重获实用性](https://simonwillison.net/2026/Jul/31/stateless-mcp/#atom-everything) ⭐️ 8.0/10

Simon Willison 认为，通常被称为 MCP 2.0 的 2026-07-28 MCP 规范以无状态协议核心取代了强制的面向会话流程，使 MCP 显著更易使用。他通过构建用于探查 MCP 服务器的 mcp-explorer，并开展 Datasette MCP 集成工作，展示了这一变化带来的机会。 无状态请求不再要求服务器保存会话 ID，也无需将客户端持续路由到同一台后端机器，因此 MCP 更适合可扩展的 Web 和无服务器部署。Willison 还认为，相较于向智能体提供不受限制的 shell 和互联网访问，受约束且可审计的 MCP 工具更安全，也更容易由运行在本地的小型模型操作。 在旧版 MCP 中，客户端必须先发送 \`initialize\` 请求并取得 \`Mcp-Session-Id\`，之后才能调用工具。在无状态流程中，单个 \`POST /mcp\` 请求即可携带 \`MCP-Protocol-Version\`、方法、工具名称、JSON-RPC 载荷和客户端元数据；该候选版本还引入了扩展框架、Tasks、MCP Apps、授权加固以及弃用政策。

rss · Simon Willison · 7月31日 23:13

**背景**: MCP 即模型上下文协议，是一种向由 LLM 驱动的智能体框架暴露工具的标准。Anthropic 于 2024 年 11 月推出该协议，它在 2025 年受到广泛关注。有状态的 HTTP 设计要求服务器跨请求保存信息，而无状态设计则让每个请求携带可被独立处理所需的上下文。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://blog.modelcontextprotocol.io/posts/2026-07-28-release-candidate/">The 2026-07-28 MCP Specification Release Candidate</a></li>
<li><a href="https://devblogs.microsoft.com/dotnet/announcing-v20-of-the-official-mcp-csharp-sdk/">Announcing v2.0 of the official MCP C# SDK - .NET Blog</a></li>
<li><a href="https://github.com/mhalle/datasette-mcp">GitHub - mhalle/datasette-mcp: First pass at a Datasette MCP server</a></li>

</ul>
</details>

**标签**: `#MCP`, `#agent systems`, `#stateless architecture`, `#LLM tools`, `#production deployment`

---

<a id="item-3"></a>
## [KAISEN 压力测试临床模型公平性审计。](https://arxiv.org/abs/2607.28608) ⭐️ 8.0/10

KAISEN 提出了一套可复现的五阶段流程，用于临床风险模型的亚组分层、差异测量、机制诊断、事后缓解和漂移监测。该研究在一个合成基准上对流程进行了压力测试，覆盖 16 项疾病任务、Healthy People 2030 的 15 个社会决定因素维度以及 3 个预先指定的交叉群体。 临床模型可能在总体上看似准确，却对不同患者亚组产生明显不同的错误率，因此仅看总体指标会掩盖公平性风险。KAISEN 将公平性评估定位为端到端的工程与治理流程，同时表明某些审计结论在现实的失效条件下可能不稳定或具有误导性。 按群体优化阈值在全部 48 次留出运行中都降低了均等机会差异，而尽管群体级 Platt scaling 是更好的校准方法，它只在 48 次运行中的 19 次改善了该差异。该诊断在 144 个受控案例中全部分类正确，却未发现 48 个存在代理变量设定错误的模型驱动案例；CUSUM 漂移监测的失效更多取决于队列随机种子而非疾病，且所有结论均来自合成数据，不能证明临床有效性。

rss · arXiv q-bio.QM · 7月31日 04:00

**背景**: 临床风险模型用于估计患者发生某种医疗结局的可能性，常被用于支持筛查、分诊或治疗决策。均等机会差异用于比较不同群体之间的错误表现，以识别模型是否对按社会决定因素及其交叉定义的人群产生不均衡表现。校准衡量预测概率是否与实际结局频率相符，但更好的校准并不一定会降低均等机会差异。

**标签**: `#clinical-ai`, `#fairness-auditing`, `#medical-machine-learning`, `#model-evaluation`, `#health-equity`

---

<a id="item-4"></a>
## [Anthropic 提出用代码执行提升 MCP 智能体效率](https://news.google.com/rss/articles/CBMibkFVX3lxTE0wZlpvbE81SXhDeFppSjUzb1RKQ0FxckN5VDFZNm9TQlE1RXdNclc2TW5XOV9qcE5kUkswSjdQdWt1eldrTnBEZFBjMkVraFByOHFsVkJENlRBS3Q2NU5Mel9oUW4xZmFETjZ4X25n?oc=5) ⭐️ 8.0/10

Anthropic 介绍了一种模式：AI 智能体编写并执行代码来编排模型上下文协议（MCP）工具，而不是让模型反复直接调用工具。其 2025 年 11 月 4 日的文章称，该方法最多可将上下文开销降低 98.7%。 随着智能体接入更多工具，反复将工具定义和中间结果放入模型上下文会消耗大量令牌并增加延迟。将多步骤编排转移到可执行代码中，可能在保留 MCP 互操作工具接口的同时，使生产环境智能体更低成本、更易扩展且更具可组合性。 所报告的收益针对上下文开销，并不意味着端到端任务性能或成本必然普遍改善。代码执行还引入了需要妥善控制的执行环境，而所提供材料并未说明基准测试方法、安全约束或实际部署结果。

google\_news · Anthropic · 11月4日 08:00

**背景**: MCP 是一项开源标准，用于将 AI 应用连接到外部系统，包括数据源和工具。它将原本需要在每个模型应用与外部服务之间单独定制的集成方式标准化。在传统工具使用中，LLM 会在其上下文中接收工具规范、选择调用并处理返回结果；代码执行可以将这类工作流的一部分转移到程序中。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.anthropic.com/engineering/code-execution-with-mcp">Code execution with MCP: building more efficient AI agents</a></li>
<li><a href="https://modelcontextprotocol.io/docs/getting-started/intro">What is the Model Context Protocol (MCP)? - Model Context Protocol</a></li>
<li><a href="https://cloud.google.com/discover/what-is-model-context-protocol">What is Model Context Protocol (MCP)? A guide | Google Cloud</a></li>

</ul>
</details>

**标签**: `#MCP`, `#AI agents`, `#production LLMs`, `#tool use`, `#agent architecture`

---

<a id="item-5"></a>
## [PolyAI 推出 Dialog-RSN-1 音频原生语音模型。](https://www.marktechpost.com/2026/07/30/polyai-releases-dialog-rsn-1-an-audio-native-dialog-model-that-fuses-turn-taking-speech-recognition-function-calling-and-response/) ⭐️ 7.0/10

PolyAI 推出了 Dialog-RSN-1，这是一种直接处理来电者音频的音频原生对话模型，可联合处理轮次切换、语音识别、函数调用和回复生成。该公司称，这一按请求运行的模型已在实际部署中实现低于 300 毫秒的响应，同时保留了可独立控制的 TTS 输出。 将这些语音代理环节整合到一个模型中，可能减少不同系统之间的交接，从而降低延迟，并保留仅依赖文本转写流程中可能丢失的对话线索。该设计面向生产级语音代理，同时通过独立的 TTS 组件保持对合成语音的控制能力。 Dialog-RSN-1 被描述为按请求运行，而不是持续开启的流式模型，因此 PolyAI 报告的延迟不应被解读为持续流式性能的证据。现有报道没有提供基准测试方法、错误分析、定价信息，或对低于 300 毫秒部署声明的独立验证。

rss · MarkTechPost · 7月31日 05:06

**背景**: 传统语音代理系统通常将自动语音识别、语言模型推理、工具或函数调用，以及文本转语音合成等独立组件连接起来。轮次切换是指判断说话者何时结束发言，以及系统何时应当回应的过程。音频原生模型直接接收语音音频，因此除语音内容外，还可能利用时间节奏等声学信息。

**标签**: `#voice agents`, `#production LLMs`, `#audio-native models`, `#enterprise AI`, `#function calling`

---

<a id="item-6"></a>
## [面向流动网络的疫情再生数指标](https://arxiv.org/abs/2607.28514) ⭐️ 7.0/10

arXiv 预印本 2607.28514 推导了将日内人群流动纳入其中的、基于流动网络的更新方程。该研究定义了多个尺度上的瞬时再生数，包括地点的流入和流出指标、地点之间的传播、会面地点以及整个网络的指标。 当人们在一个地点感染、移动后又在另一个地点造成后续感染时，传统的地点特异性 R\(t\) 估计可能产生误导。这些指标有望帮助公共卫生团队识别应重点干预的地点和流动通道，并估计干预所需的强度、类型和持续时间。 作者将该框架应用于多种网络上的疫情模拟及手机数据，并指出忽略日内流动的方法会使地点层面和网络层面的传播潜力估计产生偏差。这是一篇建模预印本，摘要未提供临床验证或实际业务部署的证据。

rss · arXiv q-bio.QM · 7月31日 04:00

**背景**: 瞬时再生数 R\(t\) 表示在当前条件下，一名感染者在某一时刻平均造成的后续感染数量。更新方程方法通过感染代际之间的时间分布，将新增病例与较早发生的感染联系起来，以推断这一数值。人类流动网络将地点表示为相互连接的节点、将地点间移动表示为连边，因此可以跨空间尺度分析传播，而不是把每个地点都视为封闭人群。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.healthknowledge.org.uk/public-health-textbook/research-methods/1a-epidemiology/epidemic-theory">Epidemic theory (effective &amp; basic reproduction numbers, epidemic thresholds) &amp; techniques for analysis of infectious disease data (construction &amp; use of epidemic curves, generation numbers, exceptional reporting &amp; identification of significant clusters) | Health Knowledge</a></li>
<li><a href="https://pmc.ncbi.nlm.nih.gov/articles/PMC7833723/">Modeling epidemic spread in transportation networks : A review - PMC</a></li>
<li><a href="https://www.researchgate.net/publication/373052114_Estimating_the_instantaneous_reproduction_number_R_t_by_using_particle_filter">(PDF) Estimating the instantaneous reproduction number ( R t ) by using particle filter</a></li>

</ul>
</details>

**标签**: `#epidemiology`, `#mobility-networks`, `#infectious-disease-modeling`, `#digital-health`, `#arXiv`

---

<a id="item-7"></a>
## [Transformer 根据胰岛素和碳水预测血糖](https://www.reddit.com/r/MachineLearning/comments/1vc1txc/i_have_trained_a_model_to_predict_my_blood_sugar_p/) ⭐️ 7.0/10

作者发布了一个仅编码器、BERT 风格的 Transformer：它利用历史血糖、碳水化合物和胰岛素数据，以及计划中的碳水化合物和胰岛素事件，预测未来两小时的血糖。该项目提供四种模型规模，最大模型约有 1700 万个参数、16 层和 16 个注意力头，并以 MIT 许可证发布源码、模型权重和评估数据。 短时血糖预测与 1 型糖尿病管理密切相关，因为进餐和胰岛素会迅速改变血糖，并带来低血糖或高血糖风险。该工作还探索了从模拟数据向多个真实 1 型糖尿病数据集迁移，但所提供的说明尚未证明其临床安全性、独立测试准确性或是否适合用于治疗决策。 该模型使用 8 至 24 小时的可变上下文窗口，屏蔽未来血糖值，同时允许对可用输入进行双向注意力计算；它还可通过自回归方式预测超过最初两小时的时间范围。模型将血糖表示为映射到 40 至 400 范围的 Kovatchev 风险空间，使用 DILATE 损失拟合中位数预测、使用 pinball 损失拟合不确定性区间，并采用 Kendall-Gal 加权组合这些目标。

reddit · r/MachineLearning · /u/0xdeadf1sh · 7月31日 20:09

**背景**: 1 型糖尿病患者需要使用胰岛素管理血糖，因此碳水化合物摄入和胰岛素给药是血糖预测的重要信号。Transformer 是一种利用注意力机制建模序列中关系的神经网络架构，可用于血糖读数和治疗事件等时间序列输入。不确定性区间用于表达未来血糖的合理可能范围，而不是将单一预测值视为确定结果。

**标签**: `#medical AI`, `#diabetes`, `#time-series forecasting`, `#transformers`, `#clinical decision support`

---