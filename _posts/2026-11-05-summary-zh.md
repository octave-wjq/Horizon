---
layout: default
title: "Horizon Summary: 2026-11-05 (ZH)"
date: 2026-11-05
lang: zh
---

> 从 108 条内容中筛选出 4 条重要资讯。

---

1. [Morpheus.AI 智能体自主构建并改进虚拟组织模型。](#item-1) ⭐️ 8.0/10
2. [CellCanon 将细胞预测、循证解释与测量驱动更新相结合。](#item-2) ⭐️ 8.0/10
3. [专家引导的大模型抽取扩充靶向蛋白降解数据。](#item-3) ⭐️ 8.0/10
4. [“小科学家”发现科研智能体循环常不敌简单采样。](#item-4) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [Morpheus.AI 智能体自主构建并改进虚拟组织模型。](https://arxiv.org/abs/2611.05413) ⭐️ 8.0/10

Morpheus.AI 预印本介绍了一种将大语言模型智能体与 Morpheus 仿真器结合的方法，可针对 15 项基准研究自主生成、运行并改进虚拟组织模型，其中 5 项研究没有已发表的模型。使用前沿大语言模型时，实际运行仿真的智能体对各研究特定标准的达成率为 83%至 86%，每个模型耗时不到两小时，费用低于 4 美元。 构建机制性组织模型通常需要兼具生物学、数学和编程知识，因此自动化这一流程可能降低利用计算模型检验假说的门槛。这些结果表明，连接科学仿真器的大语言模型智能体有望承担超越代码生成的研究任务，但所报告的基准结果并不能证明其临床有效性或实际部署成熟度。 83%至 86%衡量的是各研究特定标准的达成率，并非通用的生物学准确率；摘要将这一表现与实际运行仿真的智能体联系起来。所提供的摘要未说明具体使用哪款前沿大语言模型，也未明确所报费用是否包含全部计算开支，因此对其效率的解读仍有限制。

rss · arXiv q-bio.QM · 11月5日 05:00

**背景**: 虚拟组织模型以计算方式表示细胞及其相互作用，帮助研究者将观测结果与有关生物机制的假说联系起来。Morpheus 将基于细胞的模型与常微分方程、反应扩散系统相结合，支持多尺度建模。研究者可以使用生物学术语和数学表达式描述模型，而不必依赖传统编程代码。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://morpheus.gitlab.io/">Morpheus</a></li>

</ul>
</details>

**标签**: `#Biomedical AI`, `#LLM Agents`, `#Virtual Tissue Modeling`, `#Scientific Automation`, `#Agent Evaluation`

---

<a id="item-2"></a>
## [CellCanon 将细胞预测、循证解释与测量驱动更新相结合。](https://arxiv.org/abs/2611.05890) ⭐️ 8.0/10

CellCanon 预印本提出了一种智能体式细胞世界模型，通过共享世界状态，将单细胞表达预测、关联来源的解释和观测驱动的修订连接起来。作者报告，在覆盖三种细胞系的 339 个预留 SciPlex3 条件上，相比各项指标表现最好的基线，其差异表达 AUPRC、差异表达宏平均 F1 和变化方向宏平均 F1 分别相对提高 63.3%、17.3%和 7.2%。 将预测与可追溯证据及后续测量连接起来，有望帮助研究人员迭代完善对细胞响应的假设，而不只是依赖彼此孤立的静态预测。报告中的词元用量下降也表明，语言模型辅助的生物学分析可能变得更加经济，但这些基准结果尚不能证明其临床价值，也不能确立其在已评估场景之外的泛化能力。 CellCanon 在针对不同基因的数值输出中复用条件层面的生物学证据；与匹配药物—细胞队列上的逐基因推理相比，其预测和解释功能测得的语言模型词元用量分别下降 99.77%和 98.41%。在模拟实验反馈中，更新功能为每种药物使用一个已测量的来源情境，无需改变模型权重，就在差异表达 AUPRC 和宏平均 F1 上超过最佳微调基线；作者还报告，解释功能在基于来源证据的基准中，为所有可回答问题给出正确答案及支持证据，并识别出所有证据不足的情况，但摘要未说明该基准的规模。

rss · arXiv q-bio.QM · 11月5日 05:00

**背景**: 单细胞扰动研究测量单个细胞对药物处理等干预的响应，帮助研究人员探究基因功能和调控网络。差异表达描述不同条件之间基因表达的变化，预测这些变化是评估细胞响应模型的一种方式。AUPRC 概括识别差异表达基因时精确率与召回率之间的权衡，而宏平均 F1 对各类别的 F1 分数取平均；变化方向评估则关注表达是升高还是降低。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.nature.com/articles/s41592-025-02980-0?error=cookies_not_supported&amp;code=932fb11c-e20a-4a25-aedf-40ce9f1fe38b">Benchmarking algorithms for generalizable single - cell perturbation ...</a></li>
<li><a href="https://pmc.ncbi.nlm.nih.gov/articles/PMC12400816/">AUPRC: a metric for evaluating the performance of in-silico ...</a></li>

</ul>
</details>

**标签**: `#Biomedical AI`, `#Single-Cell Modeling`, `#Agentic World Models`, `#Perturbation Prediction`, `#Evidence-Grounded Reasoning`

---

<a id="item-3"></a>
## [专家引导的大模型抽取扩充靶向蛋白降解数据。](https://arxiv.org/abs/2605.11221) ⭐️ 8.0/10

研究人员报告了一套专家参与的大语言模型工作流，仅利用七篇经过标注的分子胶文献，便实现了记录级 F1 达到 0.98，并仅通过替换术语就迁移至蛋白水解靶向嵌合体（PROTAC）抽取任务，取得 F1 ≥ 0.93 的成绩。该工作流应用于符合条件的 PubMed Central 开放获取文献后，从 598 篇论文中新增 4,483 条记录，形成了包含 7,622 条靶向蛋白降解记录、公开提供并实行版本管理且设计为每月更新的 AutoTPD+ 数据库。 该工作流针对药物化学中的一个数据瓶颈：有价值的测定结果分散在论文正文、表格和补充材料中，难以直接用作结构化训练数据。在受控的替代模型比较中，使用 AutoTPD+ 训练的 PROTAC 降解活性模型，相比使用原始 PROTAC-DB 数据训练的模型，误差降低了 8.9%至 18.2%，显示出科研应用价值，但并不代表已证实临床效果。 该方法利用交叉验证式提示词优化，根据少量专家标注调整抽取指令；生成的 AutoTPD 中，分子胶和 PROTAC 记录数量分别比标准化参考数据集多 81%和 92%。专家抽查分别确认 100 条新增分子胶记录中的 92 条、40 条新增 PROTAC 记录中的 33 条正确，因此，较高的基准 F1 不应被理解为所有实际应用场景下的准确率，也不等同于独立验证。

rss · arXiv q-bio.QM · 11月5日 05:00

**背景**: 靶向蛋白降解利用细胞自身的蛋白质清除机制去除特定蛋白，而不只是抑制其活性。PROTAC 将结合目标蛋白的部分与结合 E3 泛素连接酶的部分连接起来，而诱导降解的分子胶则促进目标蛋白与连接酶复合物之间的相互作用。要正确解读测定记录，需要将化合物身份、目标蛋白、招募因子、实验条件与测定终点关联起来，例如表示产生 50%降解所需浓度的 DC50，以及表示最大观测降解程度的 Dmax。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://pmc.ncbi.nlm.nih.gov/articles/PMC9910052/">Molecular Glues : The Adhesive Connecting Targeted Protein ...</a></li>
<li><a href="https://arxiv.org/html/2605.11221v2">Agentic Literature Extraction Augments Targeted Protein ...</a></li>
<li><a href="https://huggingface.co/datasets/ailab-bio/AutoTPDplus">ailab-bio/AutoTPDplus · Datasets at Hugging Face</a></li>

</ul>
</details>

**标签**: `#Biomedical AI`, `#LLM Information Extraction`, `#Targeted Protein Degradation`, `#Human-in-the-Loop`, `#Drug Discovery`

---

<a id="item-4"></a>
## [“小科学家”发现科研智能体循环常不敌简单采样。](https://arxiv.org/abs/2608.16951) ⭐️ 8.0/10

“小科学家”的修订版摘要报告称，其科学方法智能体框架生成了 DNA 基序发现算法 DALE：在采用打乱序列作为负例的基准上，覆盖 132 个 ENCODE 转录因子的平均 AUROC 达到 0.842，高于 STREME 的 0.803，且运行速度快 11 倍。然而，一项预注册的受控评估发现，十种循环变体中有七种未能胜过使用相同模型和提示词的单次生成采样基线，完整框架虽然消耗了 7—8 倍的词元，表现仍不及盲目采样。 因此，这项工作的核心贡献不仅是一个性能更好的生物算法，还在于提供证据表明：复杂的科学方法流程可能增加成本，却未必比简单的采样与筛选更能促进发现。对于构建人工智能科研智能体的团队，这些结果凸显了设置可比采样基线和衡量词元效率的重要性，但并不能据此断言大语言模型推理或科学发现能力存在普遍上限。 科学家智能体利用结构化诊断，循环执行假设、预测、编码、测试与结果核对，并由独立的库恩智能体在进展停滞时引入新的问题框架；但在所报告的拆解评估中，不使用该框架、仅采用极简提示词的变体，在得分和单位词元收益上均表现最佳。在一个留出的基因组基准上，最佳循环产物与最佳采样基线候选的得分仅相差 0.002，DALE 的得分也相近，因此最初优于 STREME 的结果本身并不能证明智能体循环带来了收益。

rss · arXiv q-bio.QM · 11月5日 05:00

**背景**: DNA 序列基序是与生物功能相关的重复出现的序列模式，例如与转录因子结合有关的模式。STREME 用于发现相对于对照序列，在目标序列中富集的短小、无间隙基序。打乱后的序列可以作为评估序列分析结果的对照，因此，解读基序发现基准时，需要关注负例的构造方式。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Sequence_motif">Sequence motif - Wikipedia</a></li>
<li><a href="https://snystrom.com/memes-manual/reference/runStreme.html">Denovo motif discovery of target regions using STREME — runStreme</a></li>
<li><a href="https://www.bioinformatics.org/sms2/shuffle_dna.html">Shuffle DNA - Bioinformatics</a></li>

</ul>
</details>

**标签**: `#AI for Science`, `#LLM Agents`, `#Computational Biology`, `#Automated Algorithm Discovery`, `#Agent Evaluation`

---