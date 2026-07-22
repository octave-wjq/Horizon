---
layout: default
title: "Horizon Summary: 2026-07-22 (ZH)"
date: 2026-07-22
lang: zh
---

> 从 108 条内容中筛选出 7 条重要资讯。

---

1. [SleepFM 利用睡眠信号预测疾病风险](#item-1) ⭐️ 9.0/10
2. [CLARK 利用化验趋势提升肾衰竭风险预测](#item-2) ⭐️ 8.0/10
3. [Anthropic 推广通过 MCP 执行代码](#item-3) ⭐️ 8.0/10
4. [神经活动基础模型泛化至新视觉刺激](#item-4) ⭐️ 8.0/10
5. [偏好学习扩展抗体表达排序](#item-5) ⭐️ 7.0/10
6. [从人体模型旋转直接提取临床关节角度](#item-6) ⭐️ 7.0/10
7. [CORE 实现多染色全切片图像细胞级配准](#item-7) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [SleepFM 利用睡眠信号预测疾病风险](https://news.google.com/rss/articles/CBMiX0FVX3lxTE1Bb18waG5OdVN5MEEyNFhpMFJfN05fQmxVNjRXb2tLV2hubmlQczQxUTQzRDd1Y216TlZ6d0VTaEFZakRRaFBVLVRyRGNaaS00SHU4ZkJnMFcxbTFoendR?oc=5) ⭐️ 9.0/10

《自然·医学》报道了 SleepFM，这是一种多模态睡眠基础模型，使用约 6.5 万名参与者的超过 58.5 万小时多导睡眠监测记录进行训练。该模型采用对比学习来适应不同的 PSG 传感器配置，并通过睡眠相关生理信号预测疾病风险。 SleepFM 有望让睡眠检查中临床信息丰富但利用不足的数据，更有效地用于识别神经系统、循环系统、血液系统、精神以及内分泌和代谢疾病的风险。它可处理不同 PSG 导联配置的能力，可能提升基于睡眠实验室数据训练的 AI 模型的泛化性。 多导睡眠监测可记录脑活动、心脏活动、呼吸、腿部运动和眼球运动等信号。报告的比较显示，SleepFM 在多数疾病类别上的预测表现优于仅使用人口统计学信息的模型和端到端 PSG 基线模型，但所提供材料尚未说明它应如何用于常规临床决策。

google\_news · Nature · 1月6日 08:00

**背景**: 多导睡眠监测，即 PSG，是睡眠评估的金标准，因为它能在睡眠期间记录多个生理系统的信号。基础模型会在大规模、多样化数据集上训练，以学习可复用的表征并支持多种下游任务。睡眠紊乱与肥胖、2 型糖尿病、高血压、卒中和心血管疾病等状况相关，因此睡眠记录可能是具有价值的疾病相关信号来源。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.nature.com/articles/s41591-025-04133-4">A multimodal sleep foundation model for disease prediction | Nature Medicine</a></li>
<li><a href="https://pubmed.ncbi.nlm.nih.gov/39974074/">A Multimodal Sleep Foundation Model Developed with 500K Hours of Sleep Recordings for Disease Predictions - PubMed</a></li>
<li><a href="https://med.stanford.edu/news/all-news/2026/01/ai-sleep-disease.html">New AI model predicts disease risk while you sleep</a></li>

</ul>
</details>

**标签**: `#medical AI`, `#foundation models`, `#sleep medicine`, `#multimodal learning`, `#disease prediction`

---

<a id="item-2"></a>
## [CLARK 利用化验趋势提升肾衰竭风险预测](https://arxiv.org/abs/2607.17000) ⭐️ 8.0/10

研究人员推出了 CLARK，这是一种可解释模型，它利用常规化验结果的重复测量值，而非仅使用最新一次测量值来估计肾衰竭风险。在涵盖 540 万人、其中包括 270,009 名 CKD 患者和 12,087 例肾脏替代治疗启动事件的队列中，其两年平均精确率为 0.541，高于静态仅 eGFR 模型的 0.516。 KFRE 类方法用于估计中重度 CKD 患者在未来两年或五年内需要肾脏替代治疗的可能性，但单次测量模型忽略了化验指标变化所提供的信息。如果 CLARK 的结果能够在前瞻性研究中得到推广，基于 EHR 的决策支持或可识别更多可能从及时肾脏疾病干预中获益的患者，尤其是在较长期的预测范围内。 CLARK 的中位随访时间为 10.4 年，并且在不同化验指标组合和预测时间范围内提升了区分能力，在干预阈值下对高风险患者的识别也有所改善。该报告仍是一篇预印本，尚未证明其前瞻性临床效用、跨机构验证能力，或模型使用是否能够改善患者结局。

rss · arXiv q-bio.QM · 7月21日 04:00

**背景**: 慢性肾病是肾功能长期下降的疾病，可能进展为肾衰竭；此时患者可能需要透析或肾移植等肾脏替代治疗。肾衰竭风险方程 KFRE 是一种经过验证的工具，可估计 CKD 3a 至 5 期患者在未来两年或五年内接受肾脏替代治疗的风险。纵向建模利用指标随时间变化的方向和模式，而不是把患者最新一次化验值视为完整的临床图景；EHR 记录能够提供这类连续信息。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.ukkidney.org/health-professionals/information-resources/uk-eckd-guide/ckd-staging">CKD staging | UK Kidney Association</a></li>
<li><a href="https://link.springer.com/article/10.1186/s12911-019-1009-3">Predicting diabetes clinical outcomes using longitudinal risk factor trajectories | BMC Medical Informatics and Decision Making | Springer Nature Link</a></li>

</ul>
</details>

**标签**: `#clinical-ai`, `#kidney-disease`, `#ehr`, `#risk-prediction`, `#longitudinal-modeling`

---

<a id="item-3"></a>
## [Anthropic 推广通过 MCP 执行代码](https://news.google.com/rss/articles/CBMibkFVX3lxTE0wZlpvbE81SXhDeFppSjUzb1RKQ0FxckN5VDFZNm9TQlE1RXdNclc2TW5XOV9qcE5kUkswSjdQdWt1eldrTnBEZFBjMkVraFByOHFsVkJENlRBS3Q2NU5Mel9oUW4xZmFETjZ4X25n?oc=5) ⭐️ 8.0/10

Anthropic 发布了将代码执行与模型上下文协议（MCP）结合起来构建更高效 AI 智能体的指导方案。该方法让智能体通过代码整合并编排与 MCP 工具的交互，而非完全依赖大量单独的工具调用。 随着智能体接入越来越多的外部服务，反复向 LLM 暴露所有工具及其结果会增加上下文消耗和编排开销。代码执行为生产级智能体开发者提供了一种可复用模式，可更紧凑、更灵活地处理多步骤工具工作流。 MCP 定义了主机、客户端和服务器等不同角色；作为主机的智能体可通过客户端访问一个或多个 MCP 服务器提供的服务。所提供材料没有给出基准测试结果、支持的运行时细节或安全限制，因此应将效率提升视为架构层面的指导，而非已量化的性能结论。

google\_news · Anthropic · 11月4日 08:00

**背景**: 模型上下文协议（MCP）是 Anthropic 于 2024 年 11 月推出的开放标准和开源框架，用于连接包括 LLM 在内的 AI 系统与外部工具及数据系统。它将集成边界标准化，使 AI 应用能够通过 MCP 服务器与服务交互，而不必为每个连接单独开发定制集成。在智能体工作流中，代码执行是指模型能够编写或运行代码，以组合工具操作并处理其输出。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Model_Context_Protocol">Model Context Protocol - Wikipedia</a></li>

</ul>
</details>

**标签**: `#MCP`, `#AI agents`, `#agent engineering`, `#code execution`, `#LLM production`

---

<a id="item-4"></a>
## [神经活动基础模型泛化至新视觉刺激](https://news.google.com/rss/articles/CBMiX0FVX3lxTE1DWjR3aVhLZHkxVm00elVkQlY0QTZUNzFkcFVLSTFnZHJYODVLdng5VDFpQlZzT2JMeDJrTjlCVlR1WFZ5X1JVUzVIcE4xZXVwN2ZJZ25ONnEzWXNrcUhN?oc=5) ⭐️ 8.0/10

一项发表于《Nature》的研究报道了一种在多只小鼠视觉皮层神经活动上训练的基础模型，可预测神经元对任意自然视频的反应。该模型只需极少量额外训练便可泛化到新小鼠，并预测对连贯运动和噪声图案等未见刺激领域的反应。 这一结果表明，大规模神经记录可能包含可复用的结构，使模型能够预测训练中未使用过的刺激。这类模型有望提高感觉神经科学实验的效率，并最终为神经解码和神经工程系统提供参考，但该研究针对的是小鼠视觉皮层，并非临床应用。 据报道，该模型使用 MICrONS 功能连接组数据集训练，还可预测细胞类型、树突特征和连接关系。其已展示的泛化能力局限于论文所报告的视觉皮层记录与刺激条件，因此尚不能证明它能在其他脑区、物种或任务中取得同等表现。

google\_news · Nature · 4月9日 07:00

**背景**: 基础模型是在广泛的大规模数据上训练的模型，其学到的表征可以用较少的额外数据适配或泛化到相关任务。神经反应预测模型将视频等呈现的刺激映射为预期的神经元活动模式。功能连接组学把神经活动测量与神经元连接方式的解剖信息结合起来，使模型能够关联反应、细胞特性和神经回路属性。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.nature.com/articles/s41586-025-08829-y">Foundation model of neural activity predicts response to new stimulus types | Nature</a></li>
<li><a href="https://pubmed.ncbi.nlm.nih.gov/36993435/">Foundation model of neural activity predicts response to new stimulus types and anatomy - PubMed</a></li>

</ul>
</details>

**标签**: `#neuroscience-ai`, `#foundation-models`, `#neuroengineering`, `#biomedical-ai`, `#neural-decoding`

---

<a id="item-5"></a>
## [偏好学习扩展抗体表达排序](https://arxiv.org/abs/2607.16263) ⭐️ 7.0/10

作者提出了一种基于偏好学习的框架，将 Direct Preference Optimization（DPO）适配到蛋白质语言模型中，用于抗体表达排序。该方法结合了 1,254 条带有定量标签的序列和 400 万条弱监督的骆驼科来源抗体序列，并报告在多数评估指标上优于基线方法。 实验表达测量数据稀缺且成本高昂，是抗体设计中的重要瓶颈。如果报告的结果能够泛化，该方法可帮助抗体工程团队利用大量免疫来源序列数据，为实验测试筛选并优先排序候选抗体。 该方法引入联合掩码对数似然近似和基于 IMGT 的对齐，使 DPO 训练能够处理长度可变的抗体序列。现有证据仅来自一个多样化的内部数据集；摘要未给出绝对性能数值、湿实验验证细节，也未证明其可泛化到其他数据集或抗体类别。

rss · arXiv q-bio.QM · 7月21日 04:00

**背景**: 抗体表达排序用于估计哪些候选抗体序列更可能被成功表达，是进入实验室表征前的重要步骤。蛋白质语言模型从大规模蛋白质序列集合中学习统计规律，并可适配于后续的设计任务。DPO 是一种无需强化学习的偏好学习方法，它训练模型让偏好样本的概率高于较不偏好的样本，而不需要单独拟合奖励模型。IMGT 提供了用于分析免疫球蛋白和抗体序列的标准化规范与资源。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/pdf/2305.18290">Direct Preference Optimization</a></li>
<li><a href="https://pmc.ncbi.nlm.nih.gov/articles/PMC7555362/">Immunoglobulins or Antibodies : IMGT ® Bridging Genes, Structures...</a></li>

</ul>
</details>

**标签**: `#protein language models`, `#antibody engineering`, `#weak supervision`, `#preference learning`, `#drug discovery`

---

<a id="item-6"></a>
## [从人体模型旋转直接提取临床关节角度](https://arxiv.org/abs/2607.17639) ⭐️ 7.0/10

这篇预印本提出了一种基于校准表的方法，可将参数化人体模型输出的各身体节段旋转矩阵直接转换为具有临床可解释性的关节角度，而无需逆运动学。该方法在 OpenCap LabValidation 上使用单部智能手机视频和 GEM-X，在 15 个角度上的汇总平均绝对误差为 4.50 度；仅更换校准表后，SAM 3D Body 的结果为 4.66 度。 其报告的准确度与 OpenCap Monocular 在相同队列和参考标准上的 4.8 度结果处于同一范围，同时省去了基于优化的拟合步骤。如果能在临床人群和临床结局中得到验证，这条更简单的流程可使基于智能手机的运动评估更适用于诊所、居家监测、远程康复和分散式研究。 该方法采用国际生物力学学会的约定，将人体模型的节段旋转映射为临床关节角度，并称可通过实时单摄像头视频流运行。每次录制只需要视频，不需要受试者身高、相机内参数据库或逐受试者模型缩放；但目前证据仍是预印本中的验证结果，尚非针对临床结局的验证。

rss · arXiv q-bio.QM · 7月21日 04:00

**背景**: 参数化人体模型会从视觉数据估计人体姿态，并通常用旋转矩阵表示每个身体节段在三维空间中的朝向。旋转矩阵是表达三维方向的数学表示，但它并不会自动对应临床医生使用的解剖学关节角度。传统肌肉骨骼工作流程通常采用逆运动学，即通过优化过程使模型的关节坐标拟合观测到的运动；这项工作则使用一个针对模型的小型校准表来完成这种转换。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/html/2607.17639">Direct Clinical Joint Angle Extraction from Parametric Body Model ...</a></li>
<li><a href="https://www.opencap.ai/">OpenCap is open -source software for markerless human movement...</a></li>
<li><a href="https://pmc.ncbi.nlm.nih.gov/articles/PMC10312696/">AddBiomechanics: Automating model scaling, inverse kinematics, and inverse dynamics from human motion data through sequential optimization - PMC</a></li>

</ul>
</details>

**标签**: `#clinical-motion-analysis`, `#computer-vision`, `#digital-health`, `#biomechanics`, `#parametric-body-models`

---

<a id="item-7"></a>
## [CORE 实现多染色全切片图像细胞级配准](https://arxiv.org/abs/2511.03826) ⭐️ 7.0/10

CORE 是一种由粗到细的图像配准框架，用于在细胞核层面对多染色全切片图像（WSI）进行对齐。该方法结合组织感知的全局对齐、形状感知的细胞核点集匹配，以及基于 Coherent Point Drift（CPD）的非刚性位移估计，并在三个公开数据集和两个私有数据集上进行了评估。 跨染色的精确对齐可使病理学家和计算模型比较不同成像模态下对应的细胞结构。这解决了数字病理中的实际障碍，因为载玻片制备会引入形变和错位，使全切片图像之间难以直接比较。 粗配准阶段利用基于提示的组织掩膜排除伪影和非组织区域，随后结合组织形态与预训练特征提取器的加速稠密特征匹配。论文声称其在明场和免疫荧光 WSI 上优于现有方法的泛化性、精度和鲁棒性，但所提供的摘要未给出基准数值、外部验证方案或可复现性细节。

rss · arXiv q-bio.QM · 7月21日 04:00

**背景**: 全切片图像是病理玻片的超大规模数字扫描图像，不同染色通常会突出显示不同的组织成分。图像配准旨在估计从一张图像映射到另一张图像的变换，以处理平移、旋转、制备导致的形变和模态差异。CPD 是一种概率点集配准方法，可将点集对应关系视为概率密度估计问题，从而支持刚性和非刚性对齐。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://bigpicture.eu/news/how-whole-slide-image-registration-supports-ai-pathology">How whole slide image registration supports AI in pathology</a></li>
<li><a href="https://arxiv.org/abs/0905.2635">[0905.2635] Point-Set Registration: Coherent Point Drift</a></li>

</ul>
</details>

**标签**: `#medical imaging AI`, `#digital pathology`, `#whole-slide imaging`, `#image registration`, `#computational pathology`

---