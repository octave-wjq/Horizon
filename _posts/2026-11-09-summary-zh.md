---
layout: default
title: "Horizon Summary: 2026-11-09 (ZH)"
date: 2026-11-09
lang: zh
---

> 今日无符合常规筛选条件的资讯，以下为 GitHub 书单历史论文推荐（不受当日评分阈值限制）。

# Horizon 每日速递 - 2026-11-09

> 从 78 条内容中筛选出 2 条重要资讯。

---

1. [2023 年研究评估大语言模型的医学证据摘要能力。](#item-1) ⭐️ 8.0/10
2. [OphGLM 探索指令训练驱动的眼科视觉语言辅助。](#item-2) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [2023 年研究评估大语言模型的医学证据摘要能力。](https://www.nature.com/articles/s41746-023-00896-7) ⭐️ 8.0/10

这项历史文献推荐介绍了 Liyan Tang 及其合作者于 2023 年在《npj Digital Medicine》发表的研究，主题是评估大语言模型生成医学证据摘要的能力。此次推荐是对既有研究的回顾，并非发布新模型或近期实验结果。 医学证据摘要可能影响临床医生和研究人员对研究发现的理解，因此可靠性比单纯的语言流畅更重要。评估大语言模型在这一任务中的表现，有助于判断其是否适合医疗证据综合工作，因为遗漏信息或提出缺乏依据的说法都可能扭曲结论。 所提供的条目仅说明了论文及其评估主题，未列出模型名称、数据集、评估标准、量化结果或研究局限。因此，不能据此判断哪些模型表现最佳，也不能认定其摘要能够安全地用于临床。

github · unknown · 历史论文推荐 · mingze-yuan/Awesome-LLM-Healthcare

**背景**: 医学证据综合通过汇集研究发现来回答医疗问题，而不是仅依赖单项研究。系统综述是其中一种结构化方法，通过系统地识别和评估现有文献来研究特定问题。摘要可以帮助传达这些证据，但生成易读的摘要并不等于完成了其背后的综述工作。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://pmc.ncbi.nlm.nih.gov/articles/PMC12366998/">A comprehensive guide to conduct a systematic review and meta ...</a></li>

</ul>
</details>

**标签**: `#Medical LLMs`, `#Evidence Summarization`, `#Clinical AI`, `#LLM Evaluation`

---

<a id="item-2"></a>
## [OphGLM 探索指令训练驱动的眼科视觉语言辅助。](https://arxiv.org/abs/2306.12174) ⭐️ 7.0/10

2023 年的 OphGLM 论文探索了通过指令和对话训练眼科大型视觉语言助手，以支持围绕眼科图像和文本的交互。这是一项历史研究推荐，而非新发布的成果。 OphGLM 探索了医疗人工智能如何从纯文本辅助，发展为基于医学图像的专科交互系统。这类系统可能辅助眼科图像解读和相关对话，但研究中的表现本身并不能证明其临床安全性或部署成熟度。 所提供的搜索结果将 OphGLM 描述为由图像编码器、文本编码器、融合模块和大语言模型模块组成的系统，并提到其在常见眼底疾病分类任务上优于开源视觉语言模型。不过，这些摘要混合了 2023 年预印本与 2024 年期刊论文的描述，且未提供具体的基准测试数值、临床验证细节或部署证据。

github · unknown · 历史论文推荐 · AI-in-Health/MedLLMsPracticalGuide

**背景**: 视觉语言助手将图像处理与语言生成结合起来，使用户能够针对视觉内容提问。视觉指令微调使用与图像相关的指令及回答，训练模型遵循此类请求，而对话训练则支持会话式交互。眼科诊断依赖医学图像，因此，将图像中的发现与语言表达联系起来，对这一专科尤为重要。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/abs/2306.12174">[2306.12174] OphGLM: Training an Ophthalmology Large...</a></li>
<li><a href="https://huggingface.co/papers/2311.08172">Vision-Language Instruction Tuning: A Review and Analysis</a></li>

</ul>
</details>

**标签**: `#Medical AI`, `#Ophthalmology`, `#Vision-Language Models`, `#Instruction Tuning`, `#Clinical Assistants`

---

