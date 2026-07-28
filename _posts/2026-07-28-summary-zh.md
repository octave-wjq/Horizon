---
layout: default
title: "Horizon Summary: 2026-07-28 (ZH)"
date: 2026-07-28
lang: zh
---

> 从 89 条内容中筛选出 8 条重要资讯。

---

1. [SleepFM 利用睡眠记录预测疾病风险](#item-1) ⭐️ 9.0/10
2. [NVIDIA 发布用于手术机器人的 Cosmos-H-Dreams](#item-2) ⭐️ 8.5/10
3. [190 万成人研究显示肾功能公式结果存在分歧](#item-3) ⭐️ 8.0/10
4. [Anthropic 探讨结合 MCP 的 AI 智能体代码执行](#item-4) ⭐️ 8.0/10
5. [神经活动基础模型可泛化至新刺激类型。](#item-5) ⭐️ 8.0/10
6. [Kimi 开源用于智能体 RL 训练的 AgentENV](#item-6) ⭐️ 7.0/10
7. [新方法区分传染性与既往免疫](#item-7) ⭐️ 7.0/10
8. [网织红细胞力学与受限血流及高原病相关](#item-8) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [SleepFM 利用睡眠记录预测疾病风险](https://news.google.com/rss/articles/CBMiX0FVX3lxTE1Bb18waG5OdVN5MEEyNFhpMFJfN05fQmxVNjRXb2tLV2hubmlQczQxUTQzRDd1Y216TlZ6d0VTaEFZakRRaFBVLVRyRGNaaS00SHU4ZkJnMFcxbTFoendR?oc=5) ⭐️ 9.0/10

研究人员报告了 SleepFM，这是一种多模态睡眠基础模型，基于约 6.5 万名参与者超过 58.5 万小时的多导睡眠监测记录训练而成。该《Nature Medicine》研究采用可适配多种 PSG 配置的对比学习方法，并报告了其在睡眠分析任务和未来疾病预测上的表现。 PSG 包含丰富的生理信息，但难以在不同机构之间实现标准化和整合，这限制了其更广泛的应用。能够从异构睡眠记录中学习的模型，可能使睡眠数据更适用于风险分层和医疗 AI 研究；不过，其临床实用性仍取决于验证和部署证据。 多导睡眠监测是睡眠评估的金标准，可采集多种生理信号；SleepFM 的设计目标是适配不同的 PSG 导联配置，而非仅适用于固定的传感器组合。所提供材料未给出针对具体疾病的性能指标、外部验证细节，或该系统已经在临床照护中部署的证据。

google\_news · Nature · 1月6日 08:00

**背景**: 多导睡眠监测，即 PSG，是一种夜间睡眠检查，会记录用于分析睡眠及相关障碍的生理信号。基础模型会先在大型、多样化数据集上进行预训练，使其学到的表征能够用于或适配后续任务。多模态学习会整合多类信号的信息，这一点与 PSG 相关，因为 PSG 记录可包含多种生理测量数据。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.nature.com/articles/s41591-025-04133-4">A multimodal sleep foundation model for disease prediction</a></li>
<li><a href="https://www.medrxiv.org/content/10.1101/2025.02.04.25321675v1">A Multimodal Sleep Foundation Model Developed with 500K Hours of Sleep Recordings for Disease Predictions | medRxiv</a></li>
<li><a href="https://pubmed.ncbi.nlm.nih.gov/39974074/">A Multimodal Sleep Foundation Model Developed with 500K Hours of Sleep Recordings for Disease Predictions - PubMed</a></li>

</ul>
</details>

**标签**: `#medical AI`, `#foundation models`, `#sleep medicine`, `#disease prediction`, `#multimodal learning`

---

<a id="item-2"></a>
## [NVIDIA 发布用于手术机器人的 Cosmos-H-Dreams](https://huggingface.co/blog/nvidia/cosmos-h-dreams) ⭐️ 8.5/10

NVIDIA 的 Cosmos-H-Dreams 是一种动作条件生成模拟器，可根据机器人指令实时生成手术视频序列。Hugging Face 的文章介绍了一条教师到学生的蒸馏训练流程，用于降低 Cosmos-H-Surgical-Simulator 在长自回归生成过程中的计算成本。 实时视觉模拟器可让手术机器人团队在使用实体系统前生成并测试更多操作场景，从而有望加速数据生成、训练和验证。其实际价值取决于生成的动态与视觉效果能否可靠迁移到真实手术环境，因为该领域的错误具有很高的安全风险。 该系统面向动作条件生成，因此模拟视频会响应实时机器人指令，而不是固定的预录序列。据报道，其部署目标是一张 RTX PRO 6000 GPU，但现有材料尚未给出独立的下游机器人性能或临床性能基准。

rss · Hugging Face Blog · 7月27日 09:32

**背景**: 仿真到现实迁移是指在模拟环境中训练或验证机器人系统，并使其能够在物理世界中有效工作的难题。手术场景尤其难以模拟，因为组织和器械会发生形变、相互作用，并产生复杂的视觉变化。此前的机器人辅助手术研究表明，视觉仿真到现实方法可以将组织牵拉策略迁移到真实系统，但这也说明真实任务成功率仍是严格的衡量标准。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://huggingface.co/blog/nvidia/cosmos-h-dreams">NVIDIA Cosmos-H-Dreams: Bringing Real - Time Generative ...</a></li>
<li><a href="https://cornfordandcross.com/healthcare-operations/unlocking-real-time-generative-simulation-in-surgical-ai-using-nvidia-technologi/">Unlocking Real - Time Generative Simulation In Surgical AI Using...</a></li>
<li><a href="https://arxiv.org/abs/2406.06092">[2406.06092] Sim-To-Real Transfer for Visual Reinforcement Learning of Deformable Object Manipulation for Robot-Assisted Surgery</a></li>

</ul>
</details>

**标签**: `#surgical-robotics`, `#medical-ai`, `#generative-simulation`, `#sim-to-real`, `#digital-health`

---

<a id="item-3"></a>
## [190 万成人研究显示肾功能公式结果存在分歧](https://arxiv.org/abs/2607.22504) ⭐️ 8.0/10

一项回顾性多中心研究评估了 1909042 名成人的肾功能估算和肾衰竭预测公式；这些人于 2012 至 2014 年间至少有一次血清肌酐检测，并随访至 2025 年 1 月。去除种族变量的 2021 EKFC 和 2021 CKD-EPI 公式给出了存在分歧的 eGFR 估计，而 2006 MDRD 对五年内肾衰竭的区分能力最高，AUROC 为 0.862。 所选用的 eGFR 公式会改变个人的估计肾功能和群体 CKD 患病率，从而影响分期、转诊决策、监测和流行病学比较。由于不同出生地区的 CKD 患病率也存在显著差异，这些发现对公平的临床决策支持尤为重要。 两种按种族分层的公式，即 2006 MDRD 和 2009 CKD-EPI，显示出相近的校准表现；但两种去除种族变量的公式向相反方向改变估计值：2021 EKFC 给出的 GFR 更低，而 2021 CKD-EPI 高于既有公式。经年龄调整后的 CKD 患病率从 2021 CKD-EPI 的 8.5%到 EKFC 的 10.8%不等，并且从出生于东部撒哈拉以南非洲人群的 8.9%到出生于南亚人群的 15.3%不等。

rss · arXiv q-bio.QM · 7月27日 04:00

**背景**: 肾小球滤过率，即 GFR，反映肾脏过滤血液的效率；eGFR 则是通常结合血清肌酐和人口学变量计算得出的估计值。CKD 通常按 eGFR 进行分期，因此更换计算公式可能改变哪些患者达到某一分期阈值。MDRD 和 CKD-EPI 是已被广泛使用的 eGFR 公式系列，而肾衰竭风险方程用于估计患者在特定时间范围内进展至肾衰竭的风险。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.kidney.org/kidney-topics/estimated-glomerular-filtration-rate-egfr">Estimated GFR (eGFR) Test: Kidney Function Levels, Stages , and...</a></li>
<li><a href="https://www.kidney.org/sites/default/files/docs/mdrd-study-and-ckd-epi-gfr-estimating-equations-summary-ta.pdf">PDF MDRD Study and CKD-EPI GFR estimating equations summary ta</a></li>
<li><a href="https://www.bmj.com/content/385/bmj-2023-078063">Predicting the risks of kidney failure and death in adults... | The BMJ</a></li>

</ul>
</details>

**标签**: `#clinical-AI`, `#kidney-disease`, `#clinical-risk-prediction`, `#health-equity`, `#real-world-evidence`

---

<a id="item-4"></a>
## [Anthropic 探讨结合 MCP 的 AI 智能体代码执行](https://news.google.com/rss/articles/CBMibkFVX3lxTE0wZlpvbE81SXhDeFppSjUzb1RKQ0FxckN5VDFZNm9TQlE1RXdNclc2TW5XOV9qcE5kUkswSjdQdWt1eldrTnBEZFBjMkVraFByOHFsVkJENlRBS3Q2NU5Mel9oUW4xZmFETjZ4X25n?oc=5) ⭐️ 8.0/10

Anthropic 发布了将代码执行与模型上下文协议（MCP）结合起来的指导，用于构建更高效的 AI 智能体。该内容将代码执行定位为一种让智能体使用 MCP 连接工具并降低工具调用开销的方法。 MCP 正在成为连接 AI 应用、外部工具和数据源的一种互操作模式，因此效率改进会影响生产环境中的智能体系统。减少不必要的工具调用可能降低延迟和成本，并让智能体更有效地协调多步骤任务。 所提供的条目没有包含实现细节、基准测试、支持的执行环境或量化的效率提升。因此，它说明了架构方向，但读者仍需查阅 Anthropic 的完整文章，以评估安全边界、运营权衡和实现深度。

google\_news · Anthropic · 11月4日 08:00

**背景**: MCP 是一种用于标准化 AI 系统如何发现和使用外部工具、服务及数据源的协议。AI 智能体通常需要反复调用工具来检索信息或执行操作，这会增加模型上下文开销、延迟和成本。代码执行使智能体能够将工作流的一部分表达为可执行逻辑，从而可能合并原本需要多次独立工具交互的操作。

**标签**: `#MCP`, `#AI agents`, `#production LLMs`, `#agent architecture`, `#code execution`

---

<a id="item-5"></a>
## [神经活动基础模型可泛化至新刺激类型。](https://news.google.com/rss/articles/CBMiX0FVX3lxTE1DWjR3aVhLZHkxVm00elVkQlY0QTZUNzFkcFVLSTFnZHJYODVLdng5VDFpQlZzT2JMeDJrTjlCVlR1WFZ5X1JVUzVIcE4xZXVwN2ZJZ25ONnEzWXNrcUhN?oc=5) ⭐️ 8.0/10

研究人员利用来自多只小鼠视觉皮层的大规模神经活动数据训练了一种基础模型，使其能够预测神经元对任意自然视频的反应。该模型还能泛化到此前未见的刺激领域，包括相干运动和噪声模式，并且只需极少额外训练即可适应新的小鼠。 能够跨动物和跨刺激类型迁移的模型，可能减少实验所需的大量昂贵神经记录数据。它也为更具数据效率的神经科学模型提供了基础，但这项工作针对的是小鼠视觉皮层，而非临床脑机接口应用。 报告称，训练数据来自 MICrONS 功能连接组数据集，包含多只小鼠视觉皮层的活动记录。除视频反应预测外，Nature 的结果还涉及细胞类型、树突特征和连接性的预测；所提供材料并未证明其具备临床性能或临床应用准备度。

google\_news · Nature · 4月9日 07:00

**背景**: 神经活动记录了动物处理感觉输入时神经元不断变化的电信号。基础模型先在广泛的大规模数据上训练，因此能够适应或泛化到训练中未被完全覆盖的任务和输入。视觉皮层负责处理视觉信息，因此视频、运动和噪声模式等可控视觉刺激适合用于检验反应预测模型。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.nature.com/articles/s41586-025-08829-y">Foundation model of neural activity predicts response to new stimulus types | Nature</a></li>
<li><a href="https://pubmed.ncbi.nlm.nih.gov/36993435/">Foundation model of neural activity predicts response to new stimulus types and anatomy - PubMed</a></li>

</ul>
</details>

**标签**: `#neuroscience`, `#biomedical-ai`, `#foundation-models`, `#neural-decoding`, `#medical-engineering`

---

<a id="item-6"></a>
## [Kimi 开源用于智能体 RL 训练的 AgentENV](https://www.marktechpost.com/2026/07/27/kimi-ai-and-kvcache-ai-open-sources-agentenv/) ⭐️ 7.0/10

Moonshot AI 的 Kimi 团队与 kvcache-ai 在 Kimi K3 Open Day 期间以 MIT 许可证开源了 AgentENV（AENV）。该分布式沙箱系统在 Firecracker microVM 中运行智能体工作负载，并通过兼容 E2B 的 API 支持毫秒级快照、恢复和最多 16 路分叉。 智能体 RL 需要在工具使用环境中反复运行、评估和重置智能体，因此更快的隔离环境有望缩短训练迭代时间并降低基础设施成本。兼容 E2B 的接口也可能降低已使用 AI 生成代码沙箱的开发者的接入门槛。 Firecracker 使用轻量级 microVM，旨在结合硬件虚拟化的隔离能力与接近容器的速度和资源效率。所提供的公告没有给出基准测试、架构细节、部署证据，也未说明快照和分叉性能在真实分布式训练负载下会如何变化。

rss · MarkTechPost · 7月27日 20:48

**背景**: 智能体强化学习通过交互、反馈和奖励训练大语言模型，使其能够作为自主智能体完成多步骤任务，而不只是预测文本。这类任务通常需要执行代码或调用工具，因此隔离且可重置的执行环境对于安全性和可复现评估都很重要。E2B 是用于在安全云端沙箱中运行 AI 生成代码的开源基础设施，因此 API 兼容性可以帮助现有应用集成替代的沙箱后端。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/firecracker-microvm/firecracker">GitHub - firecracker-microvm/firecracker: Secure and fast microVMs for serverless computing. · GitHub</a></li>
<li><a href="https://inclusionai.github.io/AReaL/tutorial/agentic_rl.html">Agentic Reinforcement Learning — AReaL Documentation</a></li>

</ul>
</details>

**标签**: `#agentic RL`, `#agent engineering`, `#AI infrastructure`, `#sandboxing`, `#open source`

---

<a id="item-7"></a>
## [新方法区分传染性与既往免疫](https://arxiv.org/abs/2607.21657) ⭐️ 7.0/10

这篇预印本提出了一种基于守恒定律的方法，可从单条流行病时间序列中分别估计病原体的基本再生数 R0 和流行前易感人群比例 x-。对美国费城 1918 年秋季流感波次的重新分析估计 R0 约为 2.7、x- 约为 0.8，表明约 20% 的人口此前已具有免疫力。 对流行病时间序列进行拟合通常只能识别有效再生数 Reff，它将病原体的内在传染性与人群既有免疫状态混合在一起。将两者分离有望改进对历史疫情的分析，并帮助公共卫生建模人员区分病原体传播能力的变化与人群易感性变化。 该方法使用“流行病动量”，即按个体潜在传染能力对感染流行率加权的量，而不只依赖流行率本身。作者在随机流行病模拟中测试了该方法，并以 1918 年案例作为说明，因此摘要尚未证明其具有前瞻性的临床或实际部署验证。

rss · arXiv q-bio.QM · 7月27日 04:00

**背景**: R0 指在完全易感人群中，一名感染者平均预期造成的二代感染人数。Reff 反映免疫和干预措施等现实条件；当剩余易感者减少时，它可能低于 R0。在标准流行病拟合中，R0 与初始易感比例可能彼此混淆，因为二者的乘积决定了早期的有效传播能力；相关的动量研究提出了一条旨在解决这一可辨识性问题的守恒定律。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.abc.net.au/news/2021-07-28/what-are-k-numbers-r-numbers-explain-covid-superspreading/100330124">We&#x27;ve heard of R numbers . But what are k numbers ? And how do...</a></li>
<li><a href="https://arxiv.org/html/2511.01939v2">Epidemic “momentum” and a conservation law for infectious disease dynamics</a></li>

</ul>
</details>

**标签**: `#epidemiology`, `#infectious-disease-modeling`, `#public-health-ai`, `#statistical-inference`, `#arXiv`

---

<a id="item-8"></a>
## [网织红细胞力学与受限血流及高原病相关](https://arxiv.org/abs/2607.21810) ⭐️ 7.0/10

这篇预印本结合微流控实验与耗散粒子动力学模拟，量化了三类网织红细胞如何影响狭窄通道中的血流。在 5 微米通道内，最硬的 R1 细胞比更软的细胞慢 30%至 50%，而柔软的前导细胞可使后方硬细胞的临界通过压力降低约 12%。 该研究提出了一个力学框架，通过细胞的临界压力梯度将正常高原适应、慢性高原病高黏滞血症和镰状细胞性状相关脾综合征联系起来。它可能改进微血管血流模型，并有助于区分由红细胞压积升高导致的血液增稠与单个细胞力学变化。 模拟发现，后方细胞并未获得此前假设的、由尾流引起的数量级通过阈值下降；相反，前导细胞的顺应性决定了拥挤单列运输。该模型复现了对照血液的剪切变稀特性，并将慢性高原病的高黏滞性主要归因于红细胞压积驱动的拥挤，而非单细胞流变性质改变。

rss · arXiv q-bio.QM · 7月27日 04:00

**背景**: 网织红细胞是未成熟的红细胞，在成熟过程中会转变为常见的双凹圆盘状红细胞，其形态和细胞膜力学性质也会随之变化。在狭窄微血管和微流控通道中，红细胞必须发生显著变形，因此硬度和形状差异会影响通过速度、堵塞和整体黏度。耗散粒子动力学是一种粗粒化的介观模拟方法，可在不模拟每个原子的情况下描述流体和软物质的集体行为。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://pmc.ncbi.nlm.nih.gov/articles/PMC5937146/">Cytoskeleton Remodeling Induces Membrane Stiffness and Stability ...</a></li>
<li><a href="https://en.wikipedia.org/wiki/Dissipative_particle_dynamics">Dissipative particle dynamics - Wikipedia</a></li>
<li><a href="https://pmc.ncbi.nlm.nih.gov/articles/PMC5844650/">Hydrodynamics in Cell Studies - PMC - NIH</a></li>

</ul>
</details>

**标签**: `#biomedical-engineering`, `#microfluidics`, `#red-blood-cells`, `#computational-biomechanics`, `#mountain-sickness`

---