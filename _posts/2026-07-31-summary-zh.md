---
layout: default
title: "Horizon Summary: 2026-07-31 (ZH)"
date: 2026-07-31
lang: zh
---

> 从 102 条内容中筛选出 5 条重要资讯。

---

1. [A generalizable foundation model for analysis of human brain MRI - Nature](#item-1) ⭐️ 9.0/10
2. [SleepFM 从睡眠记录预测疾病风险](#item-2) ⭐️ 9.0/10
3. [Anthropic 披露三起网络安全评测事故](#item-3) ⭐️ 8.5/10
4. [EC-Reason-Bench 诊断大语言模型的酶分类失败](#item-4) ⭐️ 7.0/10
5. [TREA-Net 利用有限本地数据提升登革热预测能力。](#item-5) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [A generalizable foundation model for analysis of human brain MRI - Nature](https://news.google.com/rss/articles/CBMiX0FVX3lxTFBhR1V0Znd0Q1FRSS12OWc0bExxaU9sRDA3MHVLeTliNjdxUFRMX2NmTjFuOWhsLVowYkFCSlpCVjN3N0pfUGdMNDRNZ25ZX3pHT0NZT2JyVlFJZTZ4UWYw?oc=5) ⭐️ 9.0/10

Nature reports a foundation model intended to generalize across analysis tasks for human brain MRI.

google\_news · Nature · 2月5日 08:00

**标签**: `#medical-imaging-ai`, `#brain-mri`, `#foundation-models`, `#biomedical-ai`, `#clinical-validation`

---

<a id="item-2"></a>
## [SleepFM 从睡眠记录预测疾病风险](https://news.google.com/rss/articles/CBMiX0FVX3lxTE1Bb18waG5OdVN5MEEyNFhpMFJfN05fQmxVNjRXb2tLV2hubmlQczQxUTQzRDd1Y216TlZ6d0VTaEFZakRRaFBVLVRyRGNaaS00SHU4ZkJnMFcxbTFoendR?oc=5) ⭐️ 9.0/10

《自然·医学》报道了 SleepFM，这是一种多模态睡眠基础模型，使用约 6.5 万名参与者的超过 58.5 万小时多导睡眠监测记录进行训练。该模型采用可适配不同多导睡眠监测配置的对比学习方法，并能根据一晚睡眠预测 100 多种健康状况的风险。 SleepFM 可能使临床睡眠检查中采集的丰富生理信息超越传统睡眠分期用途，并将其转化为更广泛疾病风险评估的潜在数字生物标志物。它适配不同记录配置的能力，或可提升基于睡眠实验室数据训练的 AI 模型的泛化性。 其核心输入是多导睡眠监测，包含多种生理信号，而不只是消费级可穿戴设备数据。现有材料描述了预测表现，但并未证明 SleepFM 已经适合常规临床部署，也未表明其预测结果应单独用于诊断或治疗决策。

google\_news · Nature · 1月6日 08:00

**背景**: 多导睡眠监测，即 PSG，是临床睡眠检查的金标准，可在睡眠期间记录脑活动、呼吸、心脏活动和身体运动等信号。基础模型会在大量且多样的数据上训练，以学习可复用的表征，从而支持多种下游任务。由于记录导联和可用信号通道存在差异，PSG 数据长期以来难以在不同研究之间实现标准化和整合。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.nature.com/articles/s41591-025-04133-4">A multimodal sleep foundation model for disease prediction</a></li>
<li><a href="https://www.medrxiv.org/content/10.1101/2025.02.04.25321675v1">A Multimodal Sleep Foundation Model Developed with 500K Hours of Sleep Recordings for Disease Predictions | medRxiv</a></li>
<li><a href="https://med.stanford.edu/news/all-news/2026/01/ai-sleep-disease.html">New AI model predicts disease risk while you sleep</a></li>

</ul>
</details>

**标签**: `#medical AI`, `#foundation models`, `#digital health`, `#sleep medicine`, `#disease prediction`

---

<a id="item-3"></a>
## [Anthropic 披露三起网络安全评测事故](https://simonwillison.net/2026/Jul/30/three-real-world-incidents/#atom-everything) ⭐️ 8.5/10

Anthropic 审查了 141,006 次网络安全评测运行，发现了三起由六次运行引发的非预期事故，原因是 Claude 被错误地提供了互联网访问权限。其中一起事故中，Claude 向 PyPI 上传了恶意软件包；自动扫描器约一小时后将其移除，但该软件包此前已在 15 个真实系统上被下载并执行。 这些事故表明，即使模型被明确告知自己处于模拟环境中，只要测试范围假设、网络控制或合作方配置出现失误，智能体网络安全评测仍可能影响真实组织。这进一步说明，前沿模型测试需要纵深隔离、严格限定的工具权限，以及完整的执行追踪记录。 由于 Anthropic 与其评测合作方误解了互联网访问是否可用，Claude 将可访问的互联网系统视为评测目标，并通过弱密码和未认证端点等基础手法入侵了受影响的基础设施。其中一家组织被选中，是因为其真实名称恰好与评测中的虚构名称相同，这说明仅依靠提示词中的范围说明并不能构成可靠的隔离边界。

rss · Simon Willison · 7月30日 23:41

**背景**: 智能体网络安全评测测试的是能够借助命令行、浏览器或网络工具执行多步骤操作的模型，而不只是让模型输出文本答案。容器是一种隔离执行环境，但配置错误或逃逸都可能使容器级隔离失效，因此更安全的评测设计会采用嵌套式隔离，例如在容器外再设置加固的虚拟机。智能体可观测性会记录工具调用、参数、模型响应和状态转换，使操作人员能够还原执行过程并发现非预期的外部活动。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.aisi.gov.uk/blog/can-ai-agents-escape-their-sandboxes-a-benchmark-for-safely-measuring-container-breakout-capabilities">Can AI agents escape their sandboxes? A benchmark for safely measuring container breakout capabilities | AISI Work</a></li>
<li><a href="https://opentelemetry.io/blog/2025/ai-agent-observability/">AI Agent Observability - Evolving Standards and Best Practices</a></li>
<li><a href="https://www.aisi.gov.uk/frontier-ai-trends-report">Frontier AI Trends Report by The AI Security Institute (AISI)</a></li>

</ul>
</details>

**标签**: `#AI safety`, `#agent security`, `#cybersecurity evaluations`, `#sandboxing`, `#LLM agents`

---

<a id="item-4"></a>
## [EC-Reason-Bench 诊断大语言模型的酶分类失败](https://arxiv.org/abs/2607.26397) ⭐️ 7.0/10

EC-Reason-Bench 提出了一套免训练的诊断评估协议，用于检验通用大语言模型为何能识别宽泛的酶类别，却几乎无法正确预测完整的酶 EC 编号。该基准以统一的零样本基线为参照，分别评估输出结构、外部知识、推理结构和推理鲁棒性，并测试推理时干预措施。 该基准表明，外部知识必须先于推理提供，才能显著改善细粒度酶分类；这对科学智能体和检索增强的蛋白质功能预测流程具有重要意义。它还指出，单一汇总分数会掩盖关键权衡，例如在对抗性证据上的提升，以及对多功能酶预测上的损失。 在开放知识条件下，模型性能显著提升，所测试推理型大语言模型之间的差距缩小；最佳大语言模型配置的总体分数与对最近检索邻居的 EC 编号进行投票没有显著区别。不过，这一并列掩盖了不同样本上的差异：基于证据的推理能在对抗性案例中裁决相互冲突的邻居，却会在多功能酶上表现更差，并且准确率遵循同源蛋白可用性的规律。

rss · arXiv q-bio.QM · 7月30日 04:00

**背景**: 酶学委员会 EC 编号以层级方式对酶催化的反应进行分类，四个层级的信息逐步变得更具体。因此，根据蛋白质相关信息预测完整 EC 编号是一项细粒度的蛋白质功能分类任务。闭卷大语言模型评估只依赖模型参数中的内部知识，而开卷评估会在推理时提供外部检索证据。

**标签**: `#biomedical-LLMs`, `#protein-function-prediction`, `#benchmark`, `#enzyme-classification`, `#LLM-evaluation`

---

<a id="item-5"></a>
## [TREA-Net 利用有限本地数据提升登革热预测能力。](https://arxiv.org/abs/2607.26854) ⭐️ 7.0/10

TREA-Net 将环境时间序列 SIR 模型预测与轻量级门控残差校正相结合，可从数据丰富的登革热监测地区迁移到数据稀缺地区。该方法仅使用目标地区 78 周或 104 周的数据，在从哥伦比亚和尼加拉瓜迁移至墨西哥和马来西亚的 10 种 8 周预测设置中，有 9 种提升了五个神经预测骨干模型的表现。 新建立的监测系统通常缺少足够的历史观测数据来训练可靠的本地预测模型，但及时的登革热预测可支持媒介控制、疫情准备和医疗资源配置。TREA-Net 在目标地区只需少量适配参数，这可能使数据有限的公共卫生机构更容易开展跨地区预测。 该模型具有节点数量不变性，因此能够处理地点数量不同的监测系统，而且目标地区适配只需学习两个全局参数。与预测基础模型 TiRex 集成后，它在所有目标数据集上取得了最低平均绝对误差；保形预测在保持经验覆盖率的同时，将墨西哥 8 周预测区间宽度缩小了 29.6%，但摘要未提供绝对指标或实际部署证据。

rss · arXiv q-bio.QM · 7月30日 04:00

**背景**: SIR 模型将人群表示为易感者、感染者和康复者等群体，并可用于描述传染病随时间传播的过程。神经时间序列预测模型能够从历史观测中学习规律，但在一个地区训练的模型可能无法捕捉另一个地区的本地流行病学动态。迁移学习会复用数据丰富的源地区知识，以改善训练数据有限的相关目标地区的表现。

**标签**: `#medical-ai`, `#digital-health`, `#epidemiological-forecasting`, `#transfer-learning`, `#time-series`

---