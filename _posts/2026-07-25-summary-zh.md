---
layout: default
title: "Horizon Summary: 2026-07-25 (ZH)"
date: 2026-07-25
lang: zh
---

> 从 82 条内容中筛选出 7 条重要资讯。

---

1. [BrainIAC 实现通用脑 MRI 分析](#item-1) ⭐️ 9.0/10
2. [Nature 报道睡眠模型用于疾病预测。](#item-2) ⭐️ 9.0/10
3. [Code execution with MCP: building more efficient AI agents - Anthropic](#item-3) ⭐️ 8.0/10
4. [SGLang v0.5.16 新增 DSpark 与 Inkling 服务支持](#item-4) ⭐️ 7.5/10
5. [轻量级 LLM 在 EHR 表型识别中出现推理错误](#item-5) ⭐️ 7.5/10
6. [MSB 利用不完整生物标志物数据改进免疫治疗耐药预测](#item-6) ⭐️ 7.5/10
7. [endoExplain: A reproducible protocol for auditing score-localisation discordance in colonoscopy image classifiers](#item-7) ⭐️ 7.5/10

---

<a id="item-1"></a>
## [BrainIAC 实现通用脑 MRI 分析](https://news.google.com/rss/articles/CBMiX0FVX3lxTFBhR1V0Znd0Q1FRSS12OWc0bExxaU9sRDA3MHVLeTliNjdxUFRMX2NmTjFuOWhsLVowYkFCSlpCVjN3N0pfUGdMNDRNZ25ZX3pHT0NZT2JyVlFJZTZ4UWYw?oc=5) ⭐️ 9.0/10

《Nature Neuroscience》于 2026 年 2 月 5 日报道了 BrainIAC，这是一种面向人类脑 MRI 分析的通用基础模型。该模型采用对比式自监督学习训练，并在七项下游应用中得到验证，其中包括 MRI 序列分类和卒中发生时间预测。 可复用的 MRI 表征模型有望减少为每项神经影像任务和每个数据集从头训练独立模型的需求。这可能提升神经影像 AI 开发的可扩展性，因为特定任务模型往往难以在不同临床环境中实现泛化。 BrainIAC 使用对比式自监督学习，因此能够从 MRI 数据中学习，而无需为每个训练样本提供标签。报道的验证覆盖七项异质性下游应用，但所提供材料未说明队列规模、外部临床验证、模型开放情况或前瞻性临床终点。

google\_news · Nature · 2月5日 08:00

**背景**: 脑 MRI 可生成多种成像序列，分别突出不同的组织特性，并用于评估神经系统疾病。基础模型先在广泛数据上进行预训练以学习可复用表征，随后再适配或评估于特定下游任务。在神经影像领域，AI 已被用于病灶检测、分割和图像特征定量分析，但在不同机构和应用之间保持稳健性能仍是一项重要挑战。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.nature.com/articles/s41593-026-02202-6">A generalizable foundation model for analysis of human brain MRI | Nature Neuroscience</a></li>
<li><a href="https://pmc.ncbi.nlm.nih.gov/articles/PMC8530432/">Diverse Applications of Artificial Intelligence in Neuroradiology - PMC</a></li>

</ul>
</details>

**标签**: `#medical-imaging-ai`, `#brain-mri`, `#foundation-models`, `#neuroimaging`, `#biomedical-ai`

---

<a id="item-2"></a>
## [Nature 报道睡眠模型用于疾病预测。](https://news.google.com/rss/articles/CBMiX0FVX3lxTE1Bb18waG5OdVN5MEEyNFhpMFJfN05fQmxVNjRXb2tLV2hubmlQczQxUTQzRDd1Y216TlZ6d0VTaEFZakRRaFBVLVRyRGNaaS00SHU4ZkJnMFcxbTFoendR?oc=5) ⭐️ 9.0/10

Nature 报道了一种多模态睡眠基础模型，旨在利用睡眠相关数据预测疾病风险。所提供的材料未说明该模型的训练数据、评估的疾病种类或验证结果。 如果该模型能够证明具有准确性和临床实用性，可复用的睡眠相关信号模型或将支持风险分层和数字健康应用。这项工作也反映出业界正更关注用于纵向生理数据的基础模型，而不只是单一用途的预测系统。 “多模态”表示该模型使用不止一种睡眠相关输入，但现有材料没有说明具体包含哪些模态。其临床价值将取决于尚未提供的细节，包括队列规模、外部验证、前瞻性表现，以及预测是否能够改善医疗决策。

google\_news · Nature · 1月6日 08:00

**背景**: 睡眠相关数据能够记录生理和行为模式随时间发生的变化，因此可能包含与疾病风险相关的信号。基础模型通常先从广泛数据中学习可复用的模式，随后可用于预测等下游任务。多模态模型结合不同类型的输入，以便可能捕捉互补信息。

**标签**: `#medical AI`, `#foundation models`, `#digital health`, `#sleep medicine`, `#disease prediction`

---

<a id="item-3"></a>
## [Code execution with MCP: building more efficient AI agents - Anthropic](https://news.google.com/rss/articles/CBMibkFVX3lxTE0wZlpvbE81SXhDeFppSjUzb1RKQ0FxckN5VDFZNm9TQlE1RXdNclc2TW5XOV9qcE5kUkswSjdQdWt1eldrTnBEZFBjMkVraFByOHFsVkJENlRBS3Q2NU5Mel9oUW4xZmFETjZ4X25n?oc=5) ⭐️ 8.0/10

Anthropic describes using code execution alongside the Model Context Protocol to build AI agents that interact with tools and data more efficiently.

google\_news · Anthropic · 11月4日 08:00

**标签**: `#MCP`, `#AI agents`, `#agent engineering`, `#LLM production`, `#code execution`

---

<a id="item-4"></a>
## [SGLang v0.5.16 新增 DSpark 与 Inkling 服务支持](https://github.com/sgl-project/sglang/releases/tag/v0.5.16) ⭐️ 7.5/10

SGLang v0.5.16 新增 DSpark，这是一种由置信度驱动的推测解码算法，会依据草稿结果的置信度调整验证窗口大小，而非采用固定草稿长度。该版本还新增了对 Inkling 的服务支持；Inkling 是一个拥有 9750 亿参数和 100 万 Token 上下文窗口的多模态 MoE 模型。 DSpark 面向生产推理中的核心权衡：在不依赖可能对不同请求效率不佳的固定验证长度的前提下，提高解码吞吐量。Inkling 支持扩大了 SGLang 部署超大规模、长上下文多模态 MoE 工作负载的能力，并覆盖 Blackwell、H200 以及 AMD MI350X/MI355X 系统。 SGLang 报告称，在 B300 上以 TP8 运行 DeepSeek-V4-Pro、批量大小为 1 时，DSpark 达到 383.7 tok/s，平均接受长度约为 5；启用时需要设置\`--speculative-algorithm DSPARK\`和\`SGLANG\_RAGGED\_VERIFY\_MODE=compact\`。该结果依赖具体硬件、模型和工作负载；同时该版本移除了实验性的 QServe W4A8 和 FBGEMM FP8 路径，并使 NVFP4 GEMM 依赖 FlashInfer。

github · Qiaolin-Yu · 7月25日 00:13

**背景**: 推测解码通过让草稿过程先提出 Token，再由目标模型验证这些 Token 来加速自回归 LLM 生成，因此一次验证可能接受多个 Token。DSpark 采用置信度调度验证，即利用置信度估计决定每次需要验证多少草稿输出，以平衡草稿速度与被接受的概率。MoE 模型会将 Token 路由到选定的专家子网络，而滑动窗口注意力、完整注意力和 Mamba2 线性注意力等混合注意力设计，旨在让长上下文推理更具可行性。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://hyper.ai/en/papers/DSpark">DSpark : Confidence -Scheduled Speculative Decoding with... | HyperAI</a></li>
<li><a href="https://www.emergentmind.com/topics/dspark">DSpark : Speculative Decoding</a></li>
<li><a href="https://www.emergentmind.com/topics/2mamba">2 Mamba : Second -Order Linear Attention</a></li>

</ul>
</details>

**标签**: `#LLM serving`, `#speculative decoding`, `#SGLang`, `#inference optimization`, `#multimodal models`

---

<a id="item-5"></a>
## [轻量级 LLM 在 EHR 表型识别中出现推理错误](https://arxiv.org/abs/2507.23146) ⭐️ 7.5/10

该论文扩展了 PHEONA 评估框架，用于评估复杂 EHR 计算表型识别中的解释正确性错误和不忠实错误。研究评估了 Mistral Small 24B、Phi-4 14B 和 Qwen-distilled DeepSeek-r1 32B，发现所有模型均存在推理错误；当少样本示例与错误表型一致时，准确率下降了 5% 至 10%。 计算表型识别用于构建患者队列，因此即使模型在简单任务上看似准确，错误推理仍可能影响后续临床研究及其他基于 EHR 的分析。结果提醒团队，不能在未进行针对性评估的情况下，假定轻量级模型或标注为推理模型的系统能够可靠处理多疗法表型。 该研究聚焦于急性呼吸衰竭呼吸支持治疗的可计算表型；此前的工作发现，模型在概念分类和单疗法表型上的表现优于多疗法表型。使用具有误导性的少样本示例进行提示词修改后，准确率至少下降 5%，最高下降 10%，具体幅度取决于模型和思维链类型。

rss · arXiv q-bio.QM · 7月24日 04:00

**背景**: 计算表型识别将临床定义转化为可执行的规则，以便从电子健康记录数据中识别患者群体。这些队列可用于临床研究等工作，但人工病历审查非常耗时。PHEONA 是用于评估 LLM 表型识别任务表现的框架；本研究将评估范围从最终答案准确率扩展到检查模型给出的解释是否正确，以及是否忠实反映其决策过程。

**标签**: `#clinical-LLMs`, `#computational-phenotyping`, `#EHR`, `#LLM-evaluation`, `#reasoning-reliability`

---

<a id="item-6"></a>
## [MSB 利用不完整生物标志物数据改进免疫治疗耐药预测](https://arxiv.org/abs/2605.25050) ⭐️ 7.5/10

研究人员提出了面向整块缺失多模态临床数据的交叉验证后期融合生存建模框架，即具有整块缺失值的多模态堆叠方法 MSB。在 PIONeeR 研究的 443 名晚期非小细胞肺癌患者中，MSB 相较线性模型、随机生存森林和梯度提升方法的无进展生存期 C 指数表现分别提高了 15.9%、5.4%和 2.1%。 临床生物标志物研究中，部分患者常会缺少完整的检测或数据来源模块，而传统模型可能排除这些患者或产生有偏估计。MSB 有望让肿瘤学研究更充分地利用不完整的多模态队列来识别免疫治疗耐药预测因子，但其临床价值仍需外部验证。 MSB 先独立拟合各模态特异性模型，再通过交叉验证的堆叠元学习器合并预测，覆盖来自八类异构来源的 378 项生物标志物。在线性模型中，它将五折交叉验证重复三次的训练—测试泛化差距从 0.380 降至 0.055；置换重要性分析显示，常规实验室指标、临床特征和 PD-L1 表达是主要预测因素，而缺失模块指示变量的重要性极低。

rss · arXiv q-bio.QM · 7月24日 04:00

**背景**: 多模态学习将不同类型的患者信息结合起来，例如临床特征、实验室检测和生物标志物检测结果。整块缺失不同于单个数值缺失：它指某位患者的整个数据模态都不存在，例如未进行某项特定检测。生存分析用于建模无进展生存期等事件发生时间结局，而一致性指数用于衡量模型按相对风险排序患者的能力。

**标签**: `#medical-ai`, `#clinical-oncology`, `#multimodal-learning`, `#survival-analysis`, `#immunotherapy`

---

<a id="item-7"></a>
## [endoExplain: A reproducible protocol for auditing score-localisation discordance in colonoscopy image classifiers](https://arxiv.org/abs/2607.19372) ⭐️ 7.5/10

endoExplain proposes a reproducible protocol to measure when colonoscopy image-classifier confidence scores and CAM-based lesion localisation disagree across models, explanation methods, and external datasets.

rss · arXiv q-bio.QM · 7月24日 04:00

**标签**: `#medical-imaging-ai`, `#colonoscopy`, `#explainable-ai`, `#model-evaluation`, `#clinical-ai`

---