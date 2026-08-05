---
layout: default
title: "Horizon Summary: 2026-08-05 (ZH)"
date: 2026-08-05
lang: zh
---

> 从 111 条内容中筛选出 8 条重要资讯。

---

1. [基础模型面向通用脑部 MRI 分析](#item-1) ⭐️ 9.0/10
2. [睡眠基础模型可预测疾病风险。](#item-2) ⭐️ 9.0/10
3. [LeDXA 从 DXA 扫描中提取全身健康信号](#item-3) ⭐️ 8.5/10
4. [Anthropic 推广面向 MCP 智能体的代码执行](#item-4) ⭐️ 8.5/10
5. [病理学基础模型图谱中承载信号的是什么？乳腺癌患者级对照基准测试](#item-5) ⭐️ 7.8/10
6. [EasyBCI 智能体：迈向脑机接口的通用神经数据预处理](#item-6) ⭐️ 7.5/10
7. [OpenAI 加强第三方网络安全评估治理](#item-7) ⭐️ 7.0/10
8. [GRAIN 按活性成分建模药物。](#item-8) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [基础模型面向通用脑部 MRI 分析](https://news.google.com/rss/articles/CBMiX0FVX3lxTFBhR1V0Znd0Q1FRSS12OWc0bExxaU9sRDA3MHVLeTliNjdxUFRMX2NmTjFuOWhsLVowYkFCSlpCVjN3N0pfUGdMNDRNZ25ZX3pHT0NZT2JyVlFJZTZ4UWYw?oc=5) ⭐️ 9.0/10

《Nature Neuroscience》报道了“用于人脑 MRI 分析的可泛化基础模型”，搜索结果将该模型称为 BrainIAC，即脑影像自适应核心。该研究由 Mass General Brigham 和 Harvard Medical School 的医学人工智能项目团队主导，并对应 DOI 10.1038/s41593-026-02202-6。 能够在不同脑部 MRI 任务和数据集之间迁移的模型，有望减少对昂贵的任务专用临床标注的依赖，并使 AI 工具更能适应多样的神经影像工作流程。这直接应对了临床部署的核心障碍，因为不同机构的 MRI 数据往往存在差异、噪声或不完整问题。 所提供材料没有说明模型架构、预训练数据规模、基准测试指标、外部验证结果，也没有说明代码和数据是否可用。因此，该信息能够支持其研究意义，但不足以证明其已具备临床部署条件，或优于专用系统。

google\_news · Nature · 2月5日 08:00

**背景**: 脑部 MRI 是一种无创影像方法，用于呈现脑部结构，并辅助评估神经系统疾病。基础模型通过数据学习广泛表征，之后可适配多个下游任务，而不必为每项任务分别构建模型。在临床 MRI 中，扫描仪、采集协议和数据质量的差异，可能导致仅在单一机构训练的模型在其他机构表现不佳。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.linkedin.com/posts/nandhakumar16_neuroscience-ai-aiinhealthcare-activity-7425429257813696513-oXfG">#neuroscience #ai #aiinhealthcare #medicalimaging #foundationmodels...</a></li>
<li><a href="https://deeplearn.org/arxiv/733444/towards-brain-mri-foundation-models-for-the-clinic:-findings-from-the-fomo25-challenge">Towards Brain MRI Foundation Models for the Clinic: Findings from...</a></li>
<li><a href="https://www.medindia.net/news/brainiac-a-new-foundation-model-for-brain-mri-222360-1.htm">Brain Imaging Adaptive Core (BrainIAC): A New AI Foundation ...</a></li>

</ul>
</details>

**标签**: `#medical-imaging-ai`, `#brain-mri`, `#foundation-models`, `#clinical-ai`, `#biomedical-ai`

---

<a id="item-2"></a>
## [睡眠基础模型可预测疾病风险。](https://news.google.com/rss/articles/CBMiX0FVX3lxTE1Bb18waG5OdVN5MEEyNFhpMFJfN05fQmxVNjRXb2tLV2hubmlQczQxUTQzRDd1Y216TlZ6d0VTaEFZakRRaFBVLVRyRGNaaS00SHU4ZkJnMFcxbTFoendR?oc=5) ⭐️ 9.0/10

《自然》杂志于 2026 年 1 月 6 日报道了一种基于深度学习的多模态基础模型，该模型利用多导睡眠监测衍生的睡眠记录进行训练。该模型能够完成常见睡眠分析任务，并从多模态睡眠数据中预测未来疾病风险。 这项工作表明，睡眠记录有望成为可规模化利用的数字生物标志物来源，用于超越传统睡眠医学评估的风险分层。它也说明，基础模型方法可能减少临床传感工作流程对任务专用标注数据的需求。 该模型从多模态多导睡眠监测信号中学习，这些信号涵盖睡眠期间的脑、心脏、呼吸和肌肉活动等生理系统。所提供的材料未给出队列规模、外部验证结果、特定疾病的性能指标或临床部署证据。

google\_news · Nature · 1月6日 08:00

**背景**: 多导睡眠监测是一种综合性睡眠检查，可在受试者睡眠期间记录多种生理信号。基础模型先在广泛数据上训练，使其学到的表征能够适配多个后续任务。多模态模型结合不同类型信号的信息，因此可以捕捉单一测量可能遗漏的相互作用。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.nature.com/articles/s41591-025-04133-4">A multimodal sleep foundation model for disease prediction</a></li>
<li><a href="https://www.nature.com/articles/s41591-025-04133-4.pdf">A multimodal sleep foundation model for disease prediction</a></li>

</ul>
</details>

**标签**: `#medical AI`, `#foundation models`, `#digital health`, `#sleep medicine`, `#disease prediction`

---

<a id="item-3"></a>
## [LeDXA 从 DXA 扫描中提取全身健康信号](https://arxiv.org/abs/2608.02208) ⭐️ 8.5/10

研究人员推出了 LeDXA，这是一种基于 JEPA 的自监督视觉模型，从零开始在 11,540 份无标注 Human Phenotype Project 全身 DXA 扫描上训练。该模型在内部测试及 47,400 份外部 UK Biobank 扫描中，据称在疾病、生物标志物、年龄和遗传性状预测方面优于扫描仪导出的 DXA 指标和 DINOv3。 这项工作表明，常规采集的 DXA 图像可能含有超出标准骨密度和身体成分读数的预后信息。若其临床用途得到独立验证，这类表征可在无需新增扫描的情况下，将成熟的影像检查扩展为更广泛的风险与衰老评估来源。 在 UK Biobank 中位数 4.3 年的随访期间，LeDXA 对新发疾病的预测优于表格化 DXA 指标；其最高风险四分位中包含 66%的新发髋关节病病例，而表格指标对应比例为 41%。该模型的外部实际年龄预测达到 r = 0.88、平均绝对误差为 2.90 年；但这仍是一篇观察性预印本，尚未证明前瞻性临床效用、校准表现、亚组表现或工作流程收益。

rss · arXiv q-bio.QM · 8月4日 04:00

**背景**: DXA 也称为 DEXA，它使用两种 X 射线能量水平和较低辐射剂量来测量骨矿物质密度及区域身体成分。自监督学习可利用无标注数据训练模型，因此在学习表征阶段不需要人工提供结果标签。JEPA 类方法通过预测图像区域的潜在表征而非重建像素进行学习；DINOv3 则是以显著更大规模训练的通用自监督视觉基础模型。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.ncbi.nlm.nih.gov/books/NBK519042/">Dual-Energy X-Ray Absorptiometry - StatPearls - NCBI Bookshelf</a></li>
<li><a href="https://arxiv.org/abs/2301.08243">[2301.08243] Self-Supervised Learning from Images with a Joint-Embedding Predictive Architecture</a></li>
<li><a href="https://ai.meta.com/blog/dinov3-self-supervised-vision-model/">DINOv3: Self-supervised learning for vision at unprecedented scale</a></li>

</ul>
</details>

**标签**: `#medical-imaging-ai`, `#self-supervised-learning`, `#DXA`, `#clinical-risk-prediction`, `#biological-aging`

---

<a id="item-4"></a>
## [Anthropic 推广面向 MCP 智能体的代码执行](https://news.google.com/rss/articles/CBMibkFVX3lxTE0wZlpvbE81SXhDeFppSjUzb1RKQ0FxckN5VDFZNm9TQlE1RXdNclc2TW5XOV9qcE5kUkswSjdQdWt1eldrTnBEZFBjMkVraFByOHFsVkJENlRBS3Q2NU5Mel9oUW4xZmFETjZ4X25n?oc=5) ⭐️ 8.5/10

Anthropic 发布了将代码执行与模型上下文协议（MCP）工具结合使用的指导方案，使 AI 智能体能够以编程方式协调工具调用并处理中间数据。该架构将部分多工具工作流编排从模型反复调用工具转移到可执行代码中完成。 对于需要查询 API、数据库或计算服务的生产级智能体，这种模式有望减少上下文窗口膨胀、工具调用开销和延迟。随着 MCP 标准化语言模型连接外部系统的方式，它与构建可靠多工具智能体的开发者密切相关。 MCP 服务器可以暴露供语言模型调用的工具，用于执行数据库查询、API 调用和计算等操作。所提供的文章摘录没有给出实现细节、基准测试、沙箱要求或量化的效率提升，因此无法仅依据现有材料独立评估其实际权衡。

google\_news · Anthropic · 11月4日 08:00

**背景**: 模型上下文协议（MCP）是 Anthropic 于 2024 年 11 月推出的开放标准，用于将包括大语言模型在内的 AI 系统连接到外部工具、系统和数据源。MCP 工具使模型能够与训练数据之外的系统交互，例如获取最新信息或执行操作。代码执行为智能体提供了可编程层，用于组合工具输出并控制工作流，而不必让模型在对话上下文中携带每一项中间结果。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Model_Context_Protocol">Model Context Protocol - Wikipedia</a></li>
<li><a href="https://modelcontextprotocol.io/specification/2025-06-18/server/tools">Tools - Model Context Protocol</a></li>
<li><a href="https://cloud.google.com/discover/what-is-model-context-protocol">What is Model Context Protocol (MCP)? A guide | Google Cloud</a></li>

</ul>
</details>

**标签**: `#MCP`, `#AI agents`, `#agent architecture`, `#code execution`, `#production LLMs`

---

<a id="item-5"></a>
## [病理学基础模型图谱中承载信号的是什么？乳腺癌患者级对照基准测试](https://arxiv.org/abs/2608.00105) ⭐️ 7.8/10

该基准测试评估病理学基础模型嵌入能否在患者层面预测留出的乳腺癌分子程序评分。结果显示存在显著但依赖于具体程序的预测信号，其中 UNI2 表现最佳。

rss · arXiv q-bio.QM · 8月4日 04:00

**标签**: `#medical-ai`, `#computational-pathology`, `#foundation-models`, `#breast-cancer`, `#benchmarking`

---

<a id="item-6"></a>
## [EasyBCI 智能体：迈向脑机接口的通用神经数据预处理](https://arxiv.org/abs/2607.29007) ⭐️ 7.5/10

EasyBCI 提出了一种由人工监督的两阶段大语言模型智能体，可在六类脑机接口数据模态中规划、执行、验证并复用神经信号预处理工作流，同时无需向模型暴露原始记录数据。

rss · arXiv q-bio.QM · 8月4日 04:00

**标签**: `#BCI`, `#medical AI`, `#LLM agents`, `#neural data preprocessing`, `#human-in-the-loop`

---

<a id="item-7"></a>
## [OpenAI 加强第三方网络安全评估治理](https://openai.com/index/third-party-cyber-evaluations-involving-openai-models) ⭐️ 7.0/10

OpenAI 披露了与其模型第三方评估相关的近期网络安全事件。该公司表示，将为测试的执行方式和治理流程引入更严格的安全措施。 外部网络安全评估能够揭示高能力 AI 模型是否带来安全风险，但评估过程本身也可能引入运营风险。这些变化与在安全敏感的智能体或工具调用流程中使用模型的组织有关，因为测试访问权限、控制措施和监督机制都需要被谨慎管理。 所提供的材料未说明受影响的模型、事件数量或具体性质，也未给出量化评估结果。OpenAI 公布的应对重点是加强评估执行和第三方访问治理的保障措施，而不是披露技术基准数据。

rss · OpenAI Blog · 8月4日 19:00

**背景**: 网络安全评估用于检验 AI 系统可能如何被用于安全相关活动，或如何对这类活动产生影响，其中包括智能体行为和对外部工具的访问。第三方评估者能够提供独立测试，但其对高能力模型和测试环境的访问需要受到治理，以限制滥用、意外暴露和运营中断。AI 安全实践日益将评估基础设施和评估者访问权限视为开发生命周期中对安全敏感的组成部分。

**标签**: `#AI safety`, `#cybersecurity`, `#model evaluations`, `#AI governance`, `#production AI`

---

<a id="item-8"></a>
## [GRAIN 按活性成分建模药物。](https://arxiv.org/abs/2608.00098) ⭐️ 7.0/10

GRAIN 是一种药物推荐框架，它以活性成分表示药物，并结合纵向 EHR 建模、药物级相互作用图、成分级相互作用图和共处方图。在严格匹配的 MIMIC-IV 实验设置下，它优于重新实现的 MambaHealth 基线，并将药物级 DDI 比率从 0.1875 降至 0.0948。 多重用药可能使患者面临有害的药物-药物相互作用，因此，能够在提升处方预测能力的同时明确降低相互作用风险的推荐系统，可能有助于更安全的临床决策。以活性成分为中心的表示方式，也可能比将每个药物代码视为互不相关的标记更符合药理学知识。 GRAIN 使用选择性状态空间骨干网络，以线性时间处理长且不规则的就诊序列，并根据验证集 DDI 比率通过比例控制器自适应调整准确性与安全性的目标权重。它通过 RxNorm 将药物代码标准化为活性成分，并提出成分级 DDI 比率；但该研究仍是预印本，所报告的结果本身并不能证明其具有前瞻性临床安全性或已具备部署条件。

rss · arXiv q-bio.QM · 8月4日 04:00

**背景**: 电子健康记录会保存诊断、操作和用药历史，这些信息可用于预测患者后续可能需要的药物组合。多重用药通常指同时服用五种或更多药物，并可能增加不良相互作用的风险。与通常具有二次注意力计算成本的标准 Transformer 相比，Mamba 相关的选择性状态空间模型旨在以线性扩展方式处理长序列。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/html/2608.00098v1">IngMamba: Ingredient-Level Drug–Drug Interaction Modeling</a></li>
<li><a href="https://en.wikipedia.org/wiki/Polypharmacy">Polypharmacy - Wikipedia</a></li>
<li><a href="https://galileo.ai/blog/mamba-linear-scaling-transformers">How Mamba Beats Transformers at Long Sequences | Galileo</a></li>

</ul>
</details>

**标签**: `#medical-ai`, `#clinical-nlp`, `#ehr`, `#medication-recommendation`, `#drug-safety`

---