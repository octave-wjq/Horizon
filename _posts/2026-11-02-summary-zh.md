---
layout: default
title: "Horizon Summary: 2026-11-02 (ZH)"
date: 2026-11-02
lang: zh
---

> 从 77 条内容中筛选出 1 条重要资讯。

---

1. [生理轨迹比测量模式更能支持重症死亡风险模型迁移。](#item-1) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [生理轨迹比测量模式更能支持重症死亡风险模型迁移。](https://arxiv.org/abs/2610.42126) ⭐️ 8.0/10

所提供的预印本报告在第 48 小时预测院内死亡风险，使用 7,762 名 MetaVision 患者的数据训练，并在 21,682 名 MIMIC-IV 患者及覆盖 204 家医院的 43,878 名 eICU 患者中评估。在最新测量值的基础上加入生理轨迹摘要后，模型在外部 eICU 数据上的对数损失降低了 0.00922（95%置信区间：0.00704 至 0.01148），而测量频率和时间特征在模型迁移后未显示明确的额外收益。 临床模型不仅可能学习患者的生理变化，也可能学习医院如何安排测量，因此其性能容易受到测量实践差异的影响。这些结果支持在部署前同时检验跨人群迁移能力和输入数据的测量条件，而不能假定在本地有效的观测模式特征也能推广到其他环境。 在观测数量保持一致时，相比随机保留测量值，保留分散于整个时间窗口的测量值使包含观测模式的模型（R3）对数损失降低 0.03280，而生理轨迹模型（R2）降低 0.00703；当测量可用性下降时，本地原本有益的 R3 增量转为有害。这并非前瞻性临床验证，而且尽管所提供的摘要报告了实质性结果，其 arXiv 编号 2610.42126 对应 2026 年 10 月，晚于当前日期 2026 年 2 月 11 日，因此发表元数据尚无法核实。

rss · arXiv q-bio.QM · 11月2日 05:00

**背景**: MIMIC-III、MIMIC-IV 和 eICU 都是重症监护研究数据集，其中 eICU 包含多家医院的数据，可用于超出单一机构范围的模型评估。生理轨迹概括测量值随时间的变化，观测模式则描述何时测量以及测量的频率。由于测量决策与患者状况有关，这些模式可能包含预测信息，但这些信息也可能随临床实践变化而改变。对数损失用于评价预测概率，数值越低表示表现越好。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0235424">Benchmarking machine learning models on multi-centre eICU critical ...</a></li>
<li><a href="https://pmc.ncbi.nlm.nih.gov/articles/PMC7810439/">Informative presence and observation in routine health data ...</a></li>

</ul>
</details>

**标签**: `#Clinical AI`, `#ICU Mortality Prediction`, `#Model Transportability`, `#Measurement Bias`, `#External Validation`

---