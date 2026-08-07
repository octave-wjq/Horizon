---
layout: default
title: "Horizon Summary: 2026-08-07 (ZH)"
date: 2026-08-07
lang: zh
---

> 从 104 条内容中筛选出 12 条重要资讯。

---

1. [一款基础模型面向人脑 MRI 分析。](#item-1) ⭐️ 9.0/10
2. [SleepFM 利用睡眠数据预测疾病风险。](#item-2) ⭐️ 9.0/10
3. [SPIKE-Bench 衡量 LLM 生成毒素序列的风险](#item-3) ⭐️ 8.5/10
4. [Anthropic 介绍利用 MCP 代码执行提升人工智能代理效率](#item-4) ⭐️ 8.5/10
5. [Cloudflare 发布面向 AI 智能体的 Kitesurf 浏览器运行时。](#item-5) ⭐️ 8.0/10
6. [OpenAI 与 APA 合作推进青少年心理健康 AI](#item-6) ⭐️ 7.0/10
7. [Prime Intellect 开源 Prime Agent 智能体框架](#item-7) ⭐️ 7.0/10
8. [生存感知贝叶斯网络避免丢失预后信号](#item-8) ⭐️ 7.0/10
9. [基于博弈的机械通气决策推断。](#item-9) ⭐️ 7.0/10
10. [TCellAlign 统一跨单细胞研究的 T 细胞标签](#item-10) ⭐️ 7.0/10
11. [双向扩散模型可估计滚动预测漂移。](#item-11) ⭐️ 7.0/10
12. [vllm.cpp 将类 vLLM 推理服务移植到 C++20。](#item-12) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [一款基础模型面向人脑 MRI 分析。](https://news.google.com/rss/articles/CBMiX0FVX3lxTFBhR1V0Znd0Q1FRSS12OWc0bExxaU9sRDA3MHVLeTliNjdxUFRMX2NmTjFuOWhsLVowYkFCSlpCVjN3N0pfUGdMNDRNZ25ZX3pHT0NZT2JyVlFJZTZ4UWYw?oc=5) ⭐️ 9.0/10

《Nature》报道了一种可泛化的基础模型，旨在支持多类神经影像应用中的人脑 MRI 分析。所提供的条目未说明该模型名称、训练数据、评估基准或发布日期。 可复用的人脑 MRI 模型有望减少为每项神经影像任务、每个机构或每种扫描仪设置分别训练系统的需求。其实际意义取决于它能否在多样化的临床和研究数据上保持可靠表现，而非仅在开发数据集上有效。 现有内容确认了论文主题及其“可泛化”的主张，但没有提供方法细节或临床验证证据。条目也未提供代码、数据可用性、模型局限性、监管状态或临床使用准备程度的信息。

google\_news · Nature · 2月5日 08:00

**背景**: MRI 是一种用于检查人脑内部结构的成像方法，因此对神经影像研究和临床评估很重要。神经影像分析利用脑部图像研究解剖结构及其他可测量特征，但数据会因采集设置和机构不同而变化。基础模型通常旨在学习可复用的表征，并在经过适配后支持多种下游任务。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.hopkinsmedicine.org/health/conditions-and-diseases/anatomy-of-the-brain">Brain Anatomy and How the Brain Works - Johns Hopkins Medicine</a></li>
<li><a href="https://en.wikipedia.org/wiki/Human_brain">Human brain - Wikipedia</a></li>

</ul>
</details>

**标签**: `#medical-imaging-ai`, `#brain-mri`, `#foundation-models`, `#neuroimaging`, `#biomedical-ai`

---

<a id="item-2"></a>
## [SleepFM 利用睡眠数据预测疾病风险。](https://news.google.com/rss/articles/CBMiX0FVX3lxTE1Bb18waG5OdVN5MEEyNFhpMFJfN05fQmxVNjRXb2tLV2hubmlQczQxUTQzRDd1Y216TlZ6d0VTaEFZakRRaFBVLVRyRGNaaS00SHU4ZkJnMFcxbTFoendR?oc=5) ⭐️ 9.0/10

《自然》报道了一种多模态睡眠基础模型，相关报道将其称为 SleepFM，它利用睡眠相关生理数据预测疾病风险。相关报道指出，该模型使用约 6.5 万名参与者、近 60 万小时的多导睡眠监测记录进行训练，并评估了 130 种疾病的风险。 面向睡眠数据的可复用基础模型，可能使一晚临床睡眠监测不仅用于评估传统睡眠障碍，也能成为更广泛疾病风险分层的信号。它还可能为需要融合多种生理时间序列的数字健康和医疗 AI 系统提供通用建模方法。 所提供的《自然》条目未给出论文的验证指标、各疾病的具体表现、参与者人口统计信息，或预测能够改善临床结局的证据。报道中的输入是多导睡眠监测，这是一种包含多个生理信号通道的临床检查，因此不应直接假定其结果能够迁移到消费级睡眠追踪设备。

google\_news · Nature · 1月6日 08:00

**背景**: 多模态学习是一种整合多种输入或数据模态的深度学习方法。在这一研究中，相关模态是通过多导睡眠监测记录的睡眠相关生理信号。基础模型通常先通过大规模训练学习可复用的表征，再适配到下游预测任务。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.m.wikipedia.org/wiki/Multimodal_Learning">Multimodal learning - Wikipedia</a></li>
<li><a href="https://aicompasses.com/p/stanford-s-ai-predicts-disease-risk-from-sleep-data">Stanford’s AI Predicts Disease Risk From Sleep Data</a></li>

</ul>
</details>

**标签**: `#medical-ai`, `#foundation-models`, `#digital-health`, `#sleep-medicine`, `#multimodal-learning`

---

<a id="item-3"></a>
## [SPIKE-Bench 衡量 LLM 生成毒素序列的风险](https://arxiv.org/abs/2608.02684) ⭐️ 8.5/10

研究人员推出了 SPIKE-Bench，这是一项生物安全基准，包含覆盖七类功能的 631 条精选毒素设计提示词，并配套使用三阶段 SPIKE 漏斗来筛查模型生成的蛋白质序列。该研究审计了 32 个 LLM，报告最高达 50.7%的功能性有害率，并提出专用分类器 BioSafe-Guard，旨在降低预测的功能性风险，同时保留良性用途的实用性。 这项工作弥补了 LLM 安全评估中的一个缺口：仅凭文本拒绝无法判断模型给出的氨基酸序列是否具有生物学合理性，或是否被预测为有毒。它为具备蛋白质生成能力的模型和生物医学 AI 开发者提供了以功能为导向的评估方法，用于衡量可能降低有害蛋白质工程门槛的风险。 SPIKE 漏斗依次评估输出是否遵从提示词、是否具有生物学合理性，以及是否被预测为有毒，从而提供各阶段诊断结果和汇总的功能性有害率 FHR。作者报告称，FHR 主要与生物序列生成能力相关，而非与对齐行为相关，因此拒绝率不能可靠预测功能性风险；这些结果属于计算筛查信号，并非对毒性的实验验证。

rss · arXiv q-bio.QM · 8月6日 04:00

**背景**: LLM 除了能生成自然语言文本，也能生成氨基酸序列，因此可被用于蛋白质工程相关任务。蛋白质序列由氨基酸组成，其排列顺序会影响蛋白质能否合理地形成具有功能的结构。SPIKE-Bench 使用计算过滤器评估序列输出，因为普通的语言安全测试无法判断生成序列是否具有合理的生物学功能或预测毒性。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/html/2608.02684">A Blind Spot in Alignment: Quantifying Biosecurity Risks in Large Language Models</a></li>
<li><a href="https://arxiv.org/abs/2608.02684">[2608.02684] A Blind Spot in Alignment: Quantifying Biosecurity Risks in Large Language Models</a></li>

</ul>
</details>

**标签**: `#AI biosecurity`, `#LLM safety evaluation`, `#protein engineering`, `#biomedical AI`, `#benchmark`

---

<a id="item-4"></a>
## [Anthropic 介绍利用 MCP 代码执行提升人工智能代理效率](https://news.google.com/rss/articles/CBMibkFVX3lxTE0wZlpvbE81SXhDeFppSjUzb1RKQ0FxckN5VDFZNm9TQlE1RXdNclc2TW5XOV9qcE5kUkswSjdQdWt1eldrTnBEZFBjMkVraFByOHFsVkJENlRBS3Q2NU5Mel9oUW4xZmFETjZ4X25n?oc=5) ⭐️ 8.5/10

Anthropic 介绍了结合模型上下文协议（MCP）使用代码执行的方法，使人工智能代理能够通过可执行代码组合并运行多次工具交互。这样可以避免在每次交互中都把所有工具定义和结果直接放入模型上下文。 将工具编排转移到可执行代码中，可以减少上下文和工具模式带来的开销，并可能降低成本、提升代理执行多步骤工作流的能力。对于需要让大型语言模型连接大量外部工具和数据源的生产系统，这种方法尤其具有参考价值。 这种模式通常让代理编写编排脚本，再由执行环境运行脚本并协调 MCP 工具调用。现有材料没有提供部署指标、独立验证结果，也没有说明沙箱、权限控制和其他安全限制的具体细节。

google\_news · Anthropic · 11月4日 08:00

**背景**: MCP 是 Anthropic 推出的开放标准，用于规范人工智能系统（例如大型语言模型）连接外部工具、系统和数据的方式。在传统工具调用设计中，工具模式和返回结果会作为一次次独立交互传入模型上下文。结合 MCP 的代码执行方式，则允许生成的代码协调多次工具调用，从而减少模型需要反复处理的编排信息。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Model_Context_Protocol">Model Context Protocol - Wikipedia</a></li>
<li><a href="https://github.com/ramhaidar/Code-Executor-MCP">GitHub - ramhaidar/ Code -Executor- MCP : Implements...</a></li>

</ul>
</details>

**标签**: `#MCP`, `#AI agents`, `#agent engineering`, `#code execution`, `#LLM production`

---

<a id="item-5"></a>
## [Cloudflare 发布面向 AI 智能体的 Kitesurf 浏览器运行时。](https://www.marktechpost.com/2026/08/06/cloudflare-introduces-kitesurf-an-agent-first-web-browser-that-runs-entirely-in-v8-isolates-on-cloudflare-workers/) ⭐️ 8.0/10

Cloudflare 推出了 Kitesurf，这是一款无状态、以智能体为先的浏览器，可在 Cloudflare Workers 的 V8 隔离环境中运行，且不依赖 Chromium。据报道，该产品可通过 browser=kitesurf 参数支持现有的 Puppeteer、Playwright 和 MCP 客户端，并在测试阶段免费提供。 如果其兼容性和基准测试结果能够在生产环境中得到验证，Kitesurf 可能降低浏览器自动化的 CPU 和内存成本，并让更多相互隔离的智能体会话运行在共享的 Workers 基础设施上。这直接面向使用网页的 AI 智能体的一项核心扩展难题，因为这类智能体通常依赖相对重量级的 Chromium 浏览器。 据报道，Kitesurf 在 12 周内完成构建，采用了包括 Blitz、Stylo 和 Boa JavaScript 引擎在内的 Rust 组件，并通过了超过 215,000 项 Web Platform Tests。Cloudflare 称，在截图和 HTML 提取工作负载中，其 CPU 使用量比 Chromium 低 3.1 至 3.8 倍、内存使用量低 4.7 至 7.0 倍；这些属于厂商公布的基准结果，仍需独立的生产环境验证。

rss · MarkTechPost · 8月6日 19:35

**背景**: Cloudflare Workers 使用 V8 隔离环境，它是一种轻量级执行上下文，可隔离代码和内存访问，同时允许多个隔离环境共享同一个进程。Playwright 和 Puppeteer 等浏览器自动化工具通常以编程方式控制浏览器，用于导航、检查页面、截图和提取数据等任务。MCP 即模型上下文协议，使 AI 系统能够连接外部工具和服务，其中包括浏览器控制服务器。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://developers.cloudflare.com/workers/reference/security-model/">Security model · Cloudflare Workers docs</a></li>
<li><a href="https://developers.cloudflare.com/workers/reference/how-workers-works/">How Workers works · Cloudflare Workers docs</a></li>
<li><a href="https://github.com/microsoft/playwright-mcp">GitHub - microsoft /playwright- mcp : Playwright MCP server · GitHub</a></li>

</ul>
</details>

**标签**: `#AI agents`, `#browser automation`, `#Cloudflare Workers`, `#agent infrastructure`, `#MCP`

---

<a id="item-6"></a>
## [OpenAI 与 APA 合作推进青少年心理健康 AI](https://openai.com/index/openai-and-apa-partner-to-advance-responsible-ai) ⭐️ 7.0/10

OpenAI 与美国心理学会（APA）宣布建立合作关系，以推进与青少年心理健康相关的负责任 AI 使用，并制定循证指南、资源和保障措施。该公告明确聚焦青少年心理健康和负责任 AI，但未说明具体研究方案、产品部署或验证结果。 与 APA 合作可能有助于将心理学专业知识和循证要求纳入年轻人可能使用的 AI 系统的设计与治理中。这一点尤为重要，因为心理健康聊天机器人和健康应用可能影响脆弱用户，而不同地区对 AI 辅助心理健康服务的政策保护仍不一致。 现有材料描述的是拟制定的指南、资源和保障措施，而不是已经完成的临床干预或经过评估的 AI 系统。APA 关于生成式 AI 聊天机器人的健康建议呼吁开展纳入边缘化群体和临床脆弱群体的实验设计，以及临床有效性与安全性研究；公告未说明该合作是否包含这些环节。

rss · OpenAI Blog · 8月6日 06:00

**背景**: 循证指南意味着建议应建立在系统性研究和评估之上，而非仅凭对工具益处的假设。在青少年心理健康领域，保障措施可包括在广泛使用前评估其对临床脆弱用户的安全性和有效性的流程。生成式 AI 聊天机器人能够生成对话式回应，但其用于心理健康场景时，会引发其是否有益、安全以及是否得到适当治理的担忧。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.apa.org/topics/artificial-intelligence-machine-learning/health-advisory-chatbots-wellness-apps">Health advisory: Use of generative AI chatbots and wellness applications for mental health</a></li>
<li><a href="https://mhaipolicy.org/">[The Mental Health AI Policy Project]</a></li>

</ul>
</details>

**标签**: `#mental-health-ai`, `#youth-safety`, `#clinical-governance`, `#responsible-ai`, `#digital-health`

---

<a id="item-7"></a>
## [Prime Intellect 开源 Prime Agent 智能体框架](https://www.marktechpost.com/2026/08/06/prime-intellect-releases-prime-agent/) ⭐️ 7.0/10

Prime Intellect 已开源 Prime Agent，这是一套面向编程和研究任务的智能体框架，结合了递归语言模型（RLM）与 Continual Harness。该框架将子智能体作为持久化 IPython 内核中的可调用函数运行，并允许智能体在执行过程中修改提示词、技能、记忆和子智能体规范。 该设计将任务委派变成长期运行执行环境中的编程操作，可能使智能体比传统的对话加工具调用循环拥有更灵活的递归工作流。其可自我编辑的状态模型也反映出更广泛的趋势：智能体在单次任务执行期间适应自身的运行工件，而不只是在重置后的任务回合之间调整。 项目 README 表示，每个智能体都在带有已运行事件循环的持久化 IPython 内核中执行，并且可调用的 \`rlm\` 会被预先注入内核命名空间以进行递归调用。Prime Intellect 报告称，使用 Opus 5 在 ARC-AGI-3 上获得了 95.5% 的 RHAE Best@1 成绩，略高于其报告的 95.4% 人类专家基线，但现有材料未提供方法细节、独立复现、成本或延迟数据。

rss · MarkTechPost · 8月6日 09:00

**背景**: 递归语言模型会将工作上下文视为类似 REPL 环境中的变量，使智能体能够通过普通函数调用来调用其他智能体。IPython 是交互式 Python 执行环境；保持其内核持久化，意味着代码、变量和运行时状态可以跨多个步骤继续保留。Continual Harness 是一种在线适应方法，其中提示词、记忆、技能和子智能体定义都是持久状态，智能体可在一次运行期间创建、读取、更新或删除这些状态。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/PrimeIntellect-ai/rlm-harness/blob/main/README.md">rlm -harness/README.md at main · PrimeIntellect-ai/ rlm -harness</a></li>
<li><a href="https://huggingface.co/papers/2605.09998">Paper page - Continual Harness : Online Adaptation for Self -Improving...</a></li>
<li><a href="https://www.marktechpost.com/2026/08/06/prime-intellect-releases-prime-agent/">Prime Intellect Releases Prime Agent : An Open-Source RLM Harness...</a></li>

</ul>
</details>

**标签**: `#agent systems`, `#open source`, `#recursive language models`, `#agent orchestration`, `#AI evaluation`

---

<a id="item-8"></a>
## [生存感知贝叶斯网络避免丢失预后信号](https://arxiv.org/abs/2608.04046) ⭐️ 7.0/10

这篇 arXiv 预印本以 Cox 部分对数似然替代贝叶斯网络特征选择中的二元生存标签评分，作者将该方法称为生存感知贝叶斯网络。该方法在头颈癌的五种终点与队列组合，以及另外三种癌症类型中，找回了结局二值化后遗漏的预后特征。 将生存结局二值化会排除删失患者，并把事件发生时间的信息压缩为任意阈值，从而可能改变哪些临床变量被判断为具有预后意义。这项工作支持在对患者长期结局建模的临床机器学习研究中默认采用生存分析方法。 作者的消融实验表明，性能改进来自时间到事件评分公式，而不只是因为保留了更多患者。这篇论文目前是 arXiv 预印本，因此其临床验证、队列多样性和可复现性材料仍需进一步评估。

rss · arXiv q-bio.QM · 8月6日 04:00

**背景**: 生存分析用于建模事件发生前的时间，例如死亡或疾病复发，并能处理随访结束时尚未观察到最终结局的删失数据。Cox 部分似然是常用的生存分析目标函数，它利用事件发生时间和风险集，无需完整指定基线风险函数。贝叶斯网络是一类图形概率模型，可用于识别变量之间的关系，包括候选临床特征与结局之间的关系。

**标签**: `#clinical-machine-learning`, `#survival-analysis`, `#prognostic-modeling`, `#bayesian-networks`, `#medical-ai`

---

<a id="item-9"></a>
## [基于博弈的机械通气决策推断。](https://arxiv.org/abs/2510.15127) ⭐️ 7.0/10

作者提出了一种基于博弈的逆向推断方法，通过比较分类后的 ICU 状态的相对后果，为机械通气决策的后续强化学习分析生成比较模型。该方法先在合成数据上验证，再应用于真实 ICU 数据；结果显示，不同呼吸类型的后果及其相对排序会随患者亚组、时间、比较量和效应时间尺度而变化。 机械通气管理的影响具有延迟性和情境依赖性，而随机试验证据未必覆盖真实 ICU 实践中的全部情况。这项工作提供了从观察性重症监护数据中生成与数据一致的反事实假设的方法，可能为后续优化和个体化研究提供支持，但并不意味着该方法已经可以投入临床使用。 论文将核心难题表述为推断一个具有时空依赖性的奖励过程，因为患者状态、通气操作与后续结果之间的关系并不能预先确定。其报告的真实数据结果主要揭示了数据生成过程的复杂性，而非临床结局改善；摘要也没有提供数据集特征、定量验证结果或前瞻性评估证据。

rss · arXiv q-bio.QM · 8月6日 04:00

**背景**: 基于观察性医疗数据的因果推断旨在估计：若采取不同治疗决策，结果可能会如何变化；但临床记录中的治疗选择会受到患者病情及其他混杂因素影响。强化学习通过最大化轨迹上的累积奖励来优化连续决策，因此需要有意义地定义奖励和状态转移。在重症监护中，结局往往延迟出现且患者高度异质，这使这些定义尤其困难，因此论文先推断相对比较关系，而不是直接宣称绝对治疗效应。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://pmc.ncbi.nlm.nih.gov/articles/PMC9300826/">Learning Causal Effects From Observational Data in Healthcare ...</a></li>
<li><a href="https://arxiv.org/pdf/2103.05612">Challenges for Reinforcement Learning in Healthcare</a></li>

</ul>
</details>

**标签**: `#clinical-ai`, `#critical-care`, `#mechanical-ventilation`, `#causal-inference`, `#reinforcement-learning`

---

<a id="item-10"></a>
## [TCellAlign 统一跨单细胞研究的 T 细胞标签](https://arxiv.org/abs/2607.24093) ⭐️ 7.0/10

TCellAlign 提出了一套以证据为基础的多智能体工作流，可将不同研究中异构的、研究特定的 T 细胞群体标签映射到标准化命名体系，同时保留原始术语及其支持证据。作者还构建了一个人工验证的基准数据集，覆盖 44 项已发表研究、超过 700 万个细胞、CZ CELLxGENE 注释以及健康、癌症、感染性疾病和炎症性疾病四类生物学场景。 即使不同研究描述的是生物学上等价的细胞，不一致的细胞群体名称仍会阻碍单细胞数据集之间的比较与整合。TCellAlign 通过生成可比较且可追溯至文献证据的标签，可能支持更可靠的生物医学知识整合，并为未来基础模型提供标准化的细胞数据。 该框架将文献检索、信息提取、命名体系引导的对齐和基于证据的裁决拆分为模块化阶段。摘要称，它在语义一致性上优于基于本体的基线方法，并在开源和闭源 LLM 后端上保持转录组一致性，但所提供材料未给出各任务指标，也未列出评测的具体模型。

rss · arXiv q-bio.QM · 8月6日 04:00

**背景**: 单细胞研究在单个细胞分辨率下测量分子特征，例如基因表达谱，并通常为推断出的细胞群体分配标签。Cell Ontology 是用于动物细胞类型的结构化受控词汇表，旨在提高生物数据的互操作性。然而，已发表研究和公共数据集经常采用措辞或粒度不同的本地标签，因此仅有标准化术语尚不足以完全解决跨研究标签对齐问题。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://obofoundry.org/ontology/cl.html">Cell Ontology (CL)</a></li>
<li><a href="https://pmc.ncbi.nlm.nih.gov/articles/PMC551541/">An ontology for cell types - PMC - NIH</a></li>

</ul>
</details>

**标签**: `#single-cell genomics`, `#biomedical AI`, `#multi-agent systems`, `#cell ontology`, `#knowledge integration`

---

<a id="item-11"></a>
## [双向扩散模型可估计滚动预测漂移。](https://www.reddit.com/r/MachineLearning/comments/1vh2gn1/roundtrip_consistency_bidirectional_diffusion/) ⭐️ 7.0/10

Alexander Scheinker 的预印本提出了一种带方向条件的双向潜在扩散模型，可通过方向标志将动力系统向前或向后推进。该研究提出，先前向滚动再反向滚动后的重建差异，可在测试时作为无真实标签的指标来估计原本不可观测的长时程滚动误差。 生成式动力学模型在自回归滚动过程中会累积微小预测误差，而部署后的系统通常没有未来真实数据来衡量这种漂移。若单一模型的诊断方法确实无需集成模型、留出数据或控制方程，就可能让数字孪生和科学机器学习工作流中的不确定性监测更易实施。 论文报告称，在同一个网络中联合训练前向和反向动力学，在两个方向上都优于分别专门训练的两个方向模型。该指标需要在前向滚动后额外执行一次反向滚动，并且它是误差代理指标，而不是对真实未来状态的直接观测。

reddit · r/MachineLearning · /u/Clean-Hovercraft5825 · 8月6日 12:10

**背景**: 潜在扩散模型在压缩后的潜在表示中生成或预测数据，而不是直接在原始高维数据空间中处理。在滚动预测中，模型会反复把自己的输出作为下一步输入，因此误差可能在许多个模拟时间步中不断累积。往返一致性利用这样的思路：当学习到的动力学可靠时，一次前向转移再进行相应的反向转移，应当能够恢复起始状态。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/abs/2608.00675">[2608.00675] Round - Trip Consistency : Bidirectional Diffusion...</a></li>
<li><a href="https://huggingface.co/stable-diffusion-v1-5/stable-diffusion-v1-5">stable- diffusion -v1-5/stable- diffusion -v1-5 · Hugging Face</a></li>

</ul>
</details>

**标签**: `#diffusion-models`, `#digital-twins`, `#scientific-machine-learning`, `#uncertainty-estimation`, `#self-supervised-evaluation`

---

<a id="item-12"></a>
## [vllm.cpp 将类 vLLM 推理服务移植到 C++20。](https://www.reddit.com/r/LocalLLaMA/comments/1vh9lx4/i_ported_vllms_serving_stack_to_c20_66_mib_binary/) ⭐️ 7.0/10

一名独立开发者发布了 vllm.cpp，这是从零实现的、采用 C++20 的类 vLLM 大语言模型服务系统，推理时不需要 Python 或 PyTorch，生成的二进制文件为 66 MiB。该项目称已在约 25 种模型架构上与固定版本的 vLLM 参考实现逐个 token 对照，输出保持一致。 紧凑且不依赖解释器的服务栈，可能让大语言模型推理更容易嵌入其他产品，或部署到对依赖、安全和体积有严格要求的环境中。该项目试图保留与 vLLM 相近的服务技术，可能让更多部署场景获得通常依赖大型 Python 服务栈的高吞吐能力。 vllm.cpp 包含连续批处理、分块分页 KV 缓存、自动前缀缓存、推测解码以及兼容 OpenAI 的服务器，并支持 safetensors、GGUF、CUDA、CPU、Metal 和部分 Vulkan 路径。公开基准仅覆盖有限硬件，且仍缺少真实硬件上的多 GPU 支持、ROCm、服务端 LoRA、HTTP 多模态、嵌入模型和重排序模型等能力。

reddit · r/LocalLLaMA · /u/mudler\_it · 8月6日 16:45

**背景**: 大语言模型推理会在 KV 缓存中保留先前 token 的键和值张量，因此缓存的内存管理会显著影响服务器可同时处理的请求数量。分页 KV 缓存将存储空间划分为固定大小的块，并把每个请求的逻辑块映射到物理块，从而无需一次分配连续的大块内存。自动前缀缓存可复用具有相同提示词前缀的请求已经完成的计算，而推测解码则由更快的草稿模型先提出 token，再由目标模型验证。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://training.continuumlabs.ai/inference/why-is-inference-important/paged-attention-and-vllm">Paged Attention and vLLM | Continuum Labs</a></li>
<li><a href="https://introl.com/blog/kv-cache-optimization-memory-efficiency-production-llms-guide">KV Cache Optimization: Memory Efficiency for Production... | Introl Blog</a></li>
<li><a href="https://research.google/blog/looking-back-at-speculative-decoding/">Looking back at speculative decoding</a></li>

</ul>
</details>

**标签**: `#LLM serving`, `#inference deployment`, `#vLLM`, `#C++`, `#differential testing`

---