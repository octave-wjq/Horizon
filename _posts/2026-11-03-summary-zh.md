---
layout: default
title: "Horizon Summary: 2026-11-03 (ZH)"
date: 2026-11-03
lang: zh
---

> 从 121 条内容中筛选出 3 条重要资讯。

---

1. [Legora 在无法查看客户执行轨迹的情况下构建法律智能体。](#item-1) ⭐️ 8.0/10
2. [小型人工智能模型可从常规病理切片预测 HER2 状态。](#item-2) ⭐️ 8.0/10
3. [LightMIS 仅用 13.1 万参数实现面向边缘设备的医学图像分割。](#item-3) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [Legora 在无法查看客户执行轨迹的情况下构建法律智能体。](https://latent.space/p/building_legal_agents_when_you_can_t_see_the_data_-_jacob_lauritzen_cto_of_legora/) ⭐️ 8.0/10

Legora 首席技术官雅各布·劳里岑讨论了如何在客户保密要求使开发者无法查看执行轨迹的情况下，构建和测试法律人工智能智能体。所提供的摘录称，由于数据属于律师事务所的客户，Legora 无法读取智能体为律师工作时产生的任何执行轨迹。 执行轨迹有助于开发者诊断故障并评估智能体的可靠性，因此无法访问这些记录会给生产部署带来实际障碍。Legora 的情况凸显了法律人工智能面临的一项矛盾：如何在不暴露实际工作中处理的客户机密信息的前提下，提升系统质量。 文中描述的限制涉及开发者对执行轨迹的访问，而不仅仅是对训练数据的访问，因此评估和调试智能体的实际行为尤其困难。摘录没有披露具体的评估方法、监控安排、可靠性指标或部署结果，因此无法据此确定 Legora 如何应对这一限制。

rss · Latent Space · 11月2日 22:54

**背景**: 执行轨迹记录人工智能智能体完成任务时采取的一系列步骤，帮助开发者调查其行为。智能体可观测性将执行轨迹与日志、指标等其他信号结合起来，以支持调试和运行监控。当这些记录包含客户机密信息时，限制访问能够保护相关信息，但也会减少开发者分析故障时可以查看的证据。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://zambo.dev/guides/ai-agent-receipts-vs-observability/">AI Agent Receipts vs. Logs, Traces , and Observability</a></li>
<li><a href="https://www.langchain.com/langsmith/observability">LangSmith: Agent &amp; LLM Observability Platform</a></li>

</ul>
</details>

**标签**: `#Production AI Agents`, `#Legal AI`, `#Agent Evaluation`, `#Privacy`, `#Observability`

---

<a id="item-2"></a>
## [小型人工智能模型可从常规病理切片预测 HER2 状态。](https://arxiv.org/abs/2610.40662) ⭐️ 8.0/10

一篇 arXiv 预印本报告了一款拥有 2200 万参数的病理图像编码器，其切片分类器可从常规苏木精－伊红（H&amp;E）染色图像预测 HER2 状态，在从 TCGA-BRCA 到 Yale-HER2 的外部验证中取得 0.812 的曲线下面积（AUC），表现与参数量约为其 4 倍和 50 倍的编码器相当。作者称，该系统已作为仅供研究使用的预读工具集成到病理平台，并公开了模型权重、逐张切片预测结果及图表数据。 据作者报告，该小型系统无需 GPU 即可在 5 至 6 秒内处理一张切片，有望降低 HER2 预测工具的使用门槛，并帮助为结果不明确的病例安排确证检测的优先顺序。然而，其在不同外部队列中的表现差异明显，接入研究平台并不等于已证明前瞻性临床获益或治疗决策安全性。 该 ViT-S/16 编码器结合自监督训练、来自 H-optimus-0 的知识蒸馏和两轮 JEPA 优化；五个经交叉验证训练的注意力切片分类器对预测概率取平均，并使用训练数据预先确定判定阈值。作者另外报告，已部署系统在 Yale-HER2、HEROHE 和 BCNB 活检队列上的 AUC 分别为 0.82、0.75 和 0.63，在 HEROHE 的 85 例免疫组织化学（IHC）2+疑难病例中，区分原位杂交（ISH）扩增与非扩增肿瘤的 AUC 为 0.76；这些区分能力指标并不能确定所选阈值下的敏感度或特异度。

rss · arXiv q-bio.QM · 11月2日 05:00

**背景**: HER2 状态有助于判断患者是否适合接受 HER2 靶向治疗；IHC 用于评估蛋白表达，ISH 用于评估基因扩增，并帮助明确 IHC 2+这类不确定结果。常规 H&amp;E 切片展示的是组织形态，因此从这类图像预测 HER2 属于间接推断，而非直接测量该生物标志物。JEPA 是一种自监督学习方法，通过从上下文区域预测目标区域的图像表征来学习，而不是重建原始像素。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/html/2506.10006">HER 2 Expression Prediction with Flexible Multi-Modal Inputs via...</a></li>
<li><a href="https://arxiv.org/abs/2301.08243">[2301.08243] Self-Supervised Learning from Images with a Joint...</a></li>

</ul>
</details>

**标签**: `#Medical AI`, `#Computational Pathology`, `#HER2 Prediction`, `#External Validation`, `#Efficient Models`

---

<a id="item-3"></a>
## [LightMIS 仅用 13.1 万参数实现面向边缘设备的医学图像分割。](https://www.reddit.com/r/MachineLearning/comments/1xm8dbo/lightmis_ultralightweight_medical_image/) ⭐️ 8.0/10

作者介绍了 LightMIS，这是一款用于二维二分类医学图像分割的模型，拥有 13.1 万参数，直接聚合编码器的多尺度特征，不使用需要学习的逐阶段解码器。据作者报告，其按成像模态计算的宏平均 Dice 和 IoU 接近 nnWNet，同时参数量减少 98.14%、浮点运算量减少 94.58%，在 Arm Mali-G52 MC2 图形处理器上的运行速度约为后者的 10.5 倍。 这些结果表明，显著缩小的分割模型有望在资源受限的边缘设备上支持医学图像处理，同时在已报告的总体准确性指标上保持较小差距。真实设备测量和完整的图形处理器算子覆盖率提供了超越理论运算量的部署证据，但并不意味着模型已具备临床应用条件。 作者使用相同的 nnU-Net v2.3.1 流程，在涵盖五种成像模态的六个数据集上从头训练各模型，并报告所有 LightMIS 变体均实现 100%的图形处理器算子覆盖率，无需回退到中央处理器执行；代码、模型检查点和复现细节也已公开。摘录未提供各数据集的具体分数、不确定性估计或临床验证，因此，观测到的宏平均指标接近，并不能证明模型在不同任务或设备上均具有同等表现。

reddit · r/MachineLearning · /u/OkLion2068 · 11月2日 20:22

**背景**: 二分类医学图像分割将图像中的每个像素划分为目标区域或背景；Dice 和交并比（IoU）用于衡量预测区域与参考区域的重叠程度。编码器的多尺度特征包含不同空间分辨率的信息，而需要学习的逐阶段解码器则通过多个学习阶段逐步重建分割结果。参数量和浮点运算量分别反映模型规模与计算工作量，但实际设备速度还取决于硬件能否执行全部所需算子，而不必回退到中央处理器。

**标签**: `#Medical Image Segmentation`, `#Edge AI`, `#Efficient Deep Learning`, `#Healthcare AI`, `#Open Source`

---