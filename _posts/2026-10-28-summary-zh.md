---
layout: default
title: "Horizon Summary: 2026-10-28 (ZH)"
date: 2026-10-28
lang: zh
---

> 从 111 条内容中筛选出 5 条重要资讯。

---

1. [ARMD-Predict 利用四家医疗中心数据提前预测抗生素敏感性。](#item-1) ⭐️ 8.0/10
2. [PhysioCircuit 检验患者预测是否遵循可编辑的生理机制。](#item-2) ⭐️ 8.0/10
3. [ECG-RSI 通过经验证的波形编辑与反馈训练提升心电图解读能力。](#item-3) ⭐️ 8.0/10
4. [斯坦福与哈佛的报告审视临床人工智能的实际表现。](#item-4) ⭐️ 8.0/10
5. [本地部署的医疗人工智能智能体旨在提高临床决策可靠性。](#item-5) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [ARMD-Predict 利用四家医疗中心数据提前预测抗生素敏感性。](https://arxiv.org/abs/2610.32998) ⭐️ 8.0/10

ARMD-Predict 预印本介绍了利用四家学术医疗中心的 750 万条培养—抗生素观测记录开发的模型，用于在培养结果出炉前预测抗生素敏感性及特定病原体的耐药性。在采用同期、按患者分组的测试集评估的 23 个汇总数据敏感性模型中，住院患者尿培养和血培养的 AUROC 中位数分别为 0.77 和 0.70；采用按时间划分并重新训练的评估方式后，AUROC 下降约 0.04。 在等待培养结果期间，针对患者个体的预测可能帮助医生选择经验性抗生素，在充分覆盖潜在病原体与避免不必要的广谱治疗之间取得平衡。不过，中等水平的区分能力及按时间评估时的性能下降意味着，这些结果支持进一步验证，而非直接投入临床；多中心数据汇总测试也不能证明模型能够泛化至未参与研究的医院。 以 95%阳性预测值为目标的探索性阈值，将 55%的头孢曲松敏感住院尿培养观测记录识别为可考虑缩窄抗菌谱治疗的对象，并将 60%的耐药观测记录标记为需要扩大抗菌覆盖范围，但阈值的选择与评估使用了同一批测试记录，因此这些估计的可信度受到限制。病原体分类器的前三候选准确率为 51.3%至 83.3%，而耐药表型 AUROC 以已知实际病原体为条件，并非完整病原体识别至耐药预测流程的表现；模型仍需独立的校准评估、阈值验证及前瞻性端到端验证。

rss · arXiv q-bio.QM · 10月27日 04:00

**背景**: 经验性抗生素治疗是在实验室培养明确病原体及其对哪些抗生素敏感之前开始的治疗；ARMD-Predict 使用开具培养医嘱前记录的电子健康档案信息，估计患者个体的药物敏感概率。AUROC 衡量模型在不同阈值下区分敏感与耐药观测记录的排序能力，而阳性预测值衡量在某个特定阈值下，被判定为阳性的预测有多大比例正确。按患者分组划分数据可避免同一患者的记录同时出现在训练集和测试集中，按时间验证则检验模型跨时间的表现；验证数据应反映模型预期应用的人群与场景。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://healthrex.github.io/ARMD-Predict/">ARMD-Predict: predicting antibiotic resistance before culture ...</a></li>
<li><a href="https://arxiv.org/html/2610.32998v1">ARMD-Predict: multi-site machine learning topredict ...</a></li>
<li><a href="https://www.bmj.com/content/384/bmj-2023-074820">Evaluation of clinical prediction models (part 2): how to... | The BMJ</a></li>

</ul>
</details>

**标签**: `#Clinical AI`, `#Antimicrobial Resistance`, `#EHR Prediction`, `#Clinical Decision Support`, `#Multi-site Evaluation`

---

<a id="item-2"></a>
## [PhysioCircuit 检验患者预测是否遵循可编辑的生理机制。](https://arxiv.org/abs/2610.33022) ⭐️ 8.0/10

该论文提出 PhysioCircuit 多智能体系统，将器官表示为智能体，并通过记录作用方向、时间延迟和证据的可编辑生理机制卡片连接起来。论文还提出 PhysioCircuit-Bench 基准，涵盖三个器官系统、治疗事件和真实重症监护住院病例，用于检验预测是否在预期时间窗口内沿预期方向响应干预。 这种方法检验纵向患者预测是否对指定的生理关系作出响应，而不只是复现患者记录中的相关性。可检查的机制和受控的图结构比较有望提高临床语言模型评估的价值，但符合生理预期本身并不能证明临床有效性或因果有效性。 专家定义的图在推理期间保持固定，以支持受控的边干预；摘要称，其边级干预方向一致性指标（IDAR）显著优于全连接图、随机图和反向图，并报告了独立临床医生评审，以及无需重新训练、仅通过配置即可迁移到新器官系统的能力。不过，所提供的摘要没有给出具体数值、队列特征、评审流程或前瞻性临床验证，因此尚难判断其稳健性和实际部署成熟度。

rss · arXiv q-bio.QM · 10月27日 04:00

**背景**: 纵向患者预测关注患者状况如何随时间变化，而不是只估计某个单一结局。器官图将器官表示为节点，将生理影响表示为有方向的连接，其中时间延迟描述某种影响需要多久才会显现。反事实评估考察干预条件下预测如何变化；PhysioCircuit 的 IDAR 检查响应方向和时间是否符合预期，并不能据此证明预测与患者实际接受干预后会发生的情况一致。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/html/2610.33022v1">Physiology as Topology: Intervenable Organ Graphs for ...</a></li>
<li><a href="https://arxiv.org/abs/2610.33022">[2610.33022] Physiology as Topology: Intervenable Organ ...</a></li>

</ul>
</details>

**标签**: `#Clinical AI`, `#Multi-agent systems`, `#Patient trajectory forecasting`, `#Physiological modeling`, `#Counterfactual evaluation`

---

<a id="item-3"></a>
## [ECG-RSI 通过经验证的波形编辑与反馈训练提升心电图解读能力。](https://arxiv.org/abs/2610.17718) ⭐️ 8.0/10

ECG-RSI 预印本提出了一种递归自我改进框架，将经验证的心电图波形合成与反馈引导的训练干预选择相结合。在七项基准测试中，经过三轮训练，Qwen3.5-35B-A3B 的平均问答准确率从 34.57%升至 56.04%，平均分类 F1 分数从 24.27 升至 34.03。 这些结果表明，合成心电图训练数据若能针对模型不断变化的薄弱环节，并核查波形编辑是否符合预期证据，可能带来更有效的监督。将错误诊断与干预选择分开，也回应了模型评估中的一个普遍问题：反馈数据上的进步未必能够迁移到独立基准测试。 该框架通过信号重新测量核查波形编辑，利用构造错误指导生成器修正，并根据学习模型的错误提出干预方案，再在单独的选择集上比较；在保留的训练轨迹中，优选监督方式从直接强化转向针对易混淆情形的对比。持续反馈纠正带来的外部基准收益逐渐减小，且所提供的摘要并未证实其经过前瞻性临床验证。

rss · arXiv q-bio.QM · 10月27日 04:00

**背景**: 心电图以波形记录心脏的电活动，心电图模型则解读这些波形，以完成分类和问答等任务。合成波形编辑能够生成具有指定信号变化的训练样本，因此，编辑后的信号与配套问题之间必须保持一致。在 ECG-RSI 中，递归自我改进是指反复利用错误修正数据生成过程，并选择后续训练干预，而不是假定每次反馈驱动的调整都能提升泛化能力。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/abs/2610.17718">[2610.17718] ECG-RSI: Recursive Self-Improvement through Targeted ...</a></li>
<li><a href="https://openreview.net/forum?id=rEHu5Pwfqw">ECG-RSI: Towards Recursive Self-Improvement via Feedback-Driven...</a></li>

</ul>
</details>

**标签**: `#Medical AI`, `#ECG Interpretation`, `#Recursive Self-Improvement`, `#Synthetic Data`, `#Model Evaluation`

---

<a id="item-4"></a>
## [斯坦福与哈佛的报告审视临床人工智能的实际表现。](https://news.google.com/rss/articles/CBMihAFBVV95cUxPU0I2QVRNcWg2SE1vVElPaWdxNkJQbU8tZTUtV1JRdnBnV2dtTEVHNngzbmEtUVdVcTEzOFl0T0ltUHp3OW5ZTU9NaUduNWpLZHlDbDZkMjRnR200eVRyREEyMF8xdjIwVl9yS3poa2NnTmkwVVUtSllZUnlMU21Rbm1jRjg?oc=5) ⭐️ 8.0/10

斯坦福大学介绍了一份由斯坦福与哈佛共同推出的临床人工智能现状报告，审视哪些进展能够在真实临床实践中经受检验。所提供的材料仅包含文章标题，因此无法据此核实报告的方法与具体发现。 对临床医生和医疗机构而言，基准测试成绩优异并不足以证明人工智能工具能在日常诊疗中可靠运行。这份报告所强调的方向，涉及实验表现与支持临床部署的证据之间的差距。 所提供的内容未列出发布日期、研究数量、受评系统、性能指标或患者结局数据。因此，目前无法确定哪些方法成功或失败，也无法判断报告呈现的是原创评估还是对既有证据的综合梳理。

google\_news · Stanford University · 1月15日 08:00

**背景**: 临床人工智能是指用于辅助临床工作的人工智能，包括支持诊断和治疗决策。基准评估通常检验系统在特定数据集上的表现，而真实世界评估则考察其在实际诊疗条件下的表现。所提供的搜索结果强调了一项担忧：在经过整理的数据集上取得较高的回顾性准确率，未必足以证明系统已具备临床使用条件。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.nature.com/articles/s41591-025-04198-1">Principles to guide clinical AI readiness and move from ...</a></li>

</ul>
</details>

**标签**: `#Clinical AI`, `#Clinical Validation`, `#Healthcare Deployment`, `#AI Evaluation`

---

<a id="item-5"></a>
## [本地部署的医疗人工智能智能体旨在提高临床决策可靠性。](https://news.google.com/rss/articles/CBMiX0FVX3lxTE5VanUybXZENTJjdXN1V1FRTFlfZU9Dblo2WWpuMXljeHIwaEdlTUgzc2F1V2YySWhYd2ZnSFFnRXV5TkdOanVvTFJ2NEdDQV9qWUpzODBHRXhXN2QxTzQ0?oc=5) ⭐️ 8.0/10

所提供的《自然·医学》搜索结果称，研究人员开发并评估了一种完全在本地部署的临床人工智能智能体，将本地运行控制与多视角可靠性框架相结合。其目标是支持选择性自主运行，但现有材料未说明如何授权智能体自主采取行动。 本地部署可让医疗机构更充分地掌控敏感临床数据和系统运行，而可靠性评估则解决另一个问题：智能体的建议是否值得信赖。兼顾这两方面可能有助于临床决策支持系统走向实际应用，但仅在本地运行并不能证明其临床安全性。 所提供的摘录未披露模型规格、评估队列、性能指标、硬件要求或临床验证细节，因此无法判断其可靠性主张的证据强度。《自然·医学》搜索结果标注的日期为 2026 年 9 月 15 日，但此处未独立核实全文及其发表状态。

google\_news · Nature · 9月15日 07:00

**背景**: 临床决策支持系统帮助医务人员评估信息并作出诊疗决策；将系统称为人工智能智能体，强调的是其执行任务的能力，而不仅是生成一次回答。本地部署意味着系统在机构自身的基础设施内运行，而非依赖远程托管服务。本地运行控制与决策可靠性是不同的属性，因此所引述的研究描述将本地运行与独立的可靠性框架结合起来。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.nature.com/articles/s41591-026-04609-x">On-premise medical AI agents for reliable clinical decision ...</a></li>
<li><a href="https://www.ertas.ai/blog/on-premise-healthcare-ai-infrastructure">On-Premise Healthcare AI: Architecture and Infrastructure Guide</a></li>

</ul>
</details>

**标签**: `#Medical AI`, `#Clinical Decision Support`, `#AI Agents`, `#On-Premise Deployment`, `#AI Reliability`

---