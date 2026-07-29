---
layout: default
title: "Horizon Summary: 2026-07-29 (ZH)"
date: 2026-07-29
lang: zh
---

> 从 119 条内容中筛选出 9 条重要资讯。

---

1. [INSIGHT 从组织学图像绘制结直肠癌生存风险图](#item-1) ⭐️ 9.0/10
2. [A multimodal sleep foundation model for disease prediction - Nature](#item-2) ⭐️ 9.0/10
3. [国产 AI 虚拟细胞研究登上《Cell》](#item-3) ⭐️ 8.0/10
4. [DR. INFO 在 HealthBench Hard 获得 0.68 分](#item-4) ⭐️ 8.0/10
5. [神经活动基础模型可泛化至新刺激](#item-5) ⭐️ 8.0/10
6. [通用大语言模型在医学基准中超越临床 AI 工具](#item-6) ⭐️ 8.0/10
7. [FRIGID 扩展质谱分子生成能力](#item-7) ⭐️ 7.5/10
8. [AI 编程智能体重塑科学计算](#item-8) ⭐️ 7.0/10
9. [TCellAlign 统一跨单细胞研究的 T 细胞标签](#item-9) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [INSIGHT 从组织学图像绘制结直肠癌生存风险图](https://arxiv.org/abs/2512.22262) ⭐️ 9.0/10

INSIGHT 是一种图神经网络，可利用 II/III 期结直肠癌的常规组织学图像预测生存结局，并生成患者层面的空间分辨风险图。在 TCGA（n=342）、SURGEN（n=336）及大型独立验证队列中，其 C 指数为 0.68-0.69，高于 pTNM 分期的 0.44-0.58。 该研究表明，常规采集的病理切片可提供超出传统病理 TNM 分期的预后信息，可能改善局限期结直肠癌患者的风险分层。其分子层面的交叉验证还将图像风险模式与和治疗研究相关的上皮、基质及免疫程序联系起来，从而提高了可解释性。 INSIGHT 的风险图复现了已有的预后组织病理学特征，并将细胞核实心度和圆形度识别为可量化的风险相关指标。整合空间转录组学、空间蛋白质组学、bulk RNA-seq 和单细胞参考数据后，高风险区域与上皮去分化和胎儿样程序、SPP1+巨噬细胞、LAMP3+树突状细胞及适应性免疫功能障碍相关；但该研究仍是预印本，尚未证明其在前瞻性临床部署中的效用。

rss · arXiv q-bio.QM · 7月28日 04:00

**背景**: II/III 期结直肠癌通常指局限性或区域扩散性疾病，其预后和治疗决策常依赖病理 TNM 分期，该分期描述肿瘤范围及淋巴结受累情况。常规组织学是病理医生检查标准染色组织切片的方法；组织成分的空间排列可反映肿瘤与微环境之间的相互作用，而这些信息难以用少量人工特征概括。图神经网络可将组织表示为相互连接的细胞或区域，使模型能够学习局部组织邻域和全切片模式。C 指数用于衡量生存模型按风险排序患者的能力，数值越高表示区分能力越强。

**标签**: `#medical-ai`, `#computational-pathology`, `#survival-analysis`, `#graph-neural-networks`, `#colorectal-cancer`

---

<a id="item-2"></a>
## [A multimodal sleep foundation model for disease prediction - Nature](https://news.google.com/rss/articles/CBMiX0FVX3lxTE1Bb18waG5OdVN5MEEyNFhpMFJfN05fQmxVNjRXb2tLV2hubmlQczQxUTQzRDd1Y216TlZ6d0VTaEFZakRRaFBVLVRyRGNaaS00SHU4ZkJnMFcxbTFoendR?oc=5) ⭐️ 9.0/10

Nature reports a multimodal sleep foundation model designed to predict disease risk from sleep-related physiological data.

google\_news · Nature · 1月6日 08:00

**标签**: `#medical AI`, `#digital health`, `#foundation models`, `#sleep medicine`, `#disease prediction`

---

<a id="item-3"></a>
## [国产 AI 虚拟细胞研究登上《Cell》](https://mp.weixin.qq.com/s?__biz=MzIzNjc1NzUzMw==&amp;mid=2247907924&amp;idx=3&amp;sn=654ebf40eb186cf7ff0653d51ed2af96) ⭐️ 8.0/10

据该新闻称，一项中国 AI 虚拟细胞研究发表于《Cell》主刊。该研究构建统一的生物表征空间，旨在对细胞状态进行建模，并计算预测药物扰动效应，以支持虚拟试药。 跨生物数据的统一表征有望更方便地连接细胞测量结果与候选药物的预测反应。若获得实验验证，该方法可在成本更高的实验室研究之前帮助筛选化合物并探索作用机制。 现有材料未披露模型架构、训练数据规模、数据模态、基准结果，以及实验或临床验证情况。因此，所称虚拟试药应理解为计算预测目标，不能据此认为它能够替代实验室或临床测试。

rss · 量子位 · 7月28日 09:58

**背景**: 虚拟细胞利用计算模型和生物数据，模拟或预测细胞在不同生理、生化或治疗条件下的行为。统一生物表征空间是指将异质的生物学观测编码为可供模型比较和预测的共同形式。这类系统旨在降低假设验证的时间和成本，但其实际价值取决于预测准确性以及在真实实验中的验证。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://zhuanlan.zhihu.com/p/27643347211">AI虚拟细胞，生命科学的“终极沙盘”？ - 知乎</a></li>
<li><a href="https://m.aitntnews.com/newDetail.html?newId=11455">Cell：AI虚拟细胞，生命科学的“终极沙盘”？</a></li>

</ul>
</details>

**标签**: `#medical-ai`, `#virtual-cell`, `#drug-discovery`, `#biomedical-foundation-models`, `#cell-biology`

---

<a id="item-4"></a>
## [DR. INFO 在 HealthBench Hard 获得 0.68 分](https://arxiv.org/abs/2509.02594) ⭐️ 8.0/10

DR. INFO 论文在包含 1,000 个示例的 HealthBench Hard 子集上评估了一套智能体式检索增强生成临床支持助手。论文报告其得分为 0.68，高于文中列出的独立前沿模型分数，其中 GPT-5 为 0.46。 这一结果表明，结合检索和智能体工作流的临床系统在真实、开放式医疗对话中可能优于独立模型。这一点很重要，因为临床部署不仅需要在选择题医学考试中表现良好，还需要准确性、指令遵循、上下文处理能力以及恰当的沟通方式。 HealthBench 使用由医生编写、针对每段对话的评分量表，衡量准确性、完整性和指令遵循等行为维度。论文还报告，在与 OpenEvidence 及 Pathway.md（现为 Doximity 的 DoxGPT）进行的独立 100 样本比较中，DR. INFO 得分为 0.72，同时指出上下文感知和回答完整性仍有改进空间。

rss · arXiv q-bio.QM · 7月28日 04:00

**背景**: HealthBench 是一个开放式临床 LLM 基准，包含 5,000 段由用户或医疗专业人员参与的多轮对话。它使用 262 名医生制定的 48,562 项对话专属标准评估回答，而不是依赖单一标准答案。检索增强生成会为 LLM 补充检索到的外部信息，而智能体式系统能够采用多步骤工作流来决定如何检索和组织回答。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://cdn.openai.com/pdf/bd7a39d5-9e9f-47b3-903c-8b847ca650c7/healthbench_paper.pdf">HealthBench: Evaluating Large Language Models Towards Improved Human Health</a></li>
<li><a href="https://arxiv.org/html/2509.02594v1">OpenAI’s HealthBench in Action: Evaluating an LLM-Based Medical Assistant on Realistic Clinical Queries</a></li>

</ul>
</details>

**标签**: `#clinical-llm`, `#medical-ai`, `#rag`, `#agentic-systems`, `#llm-evaluation`

---

<a id="item-5"></a>
## [神经活动基础模型可泛化至新刺激](https://news.google.com/rss/articles/CBMiX0FVX3lxTE1DWjR3aVhLZHkxVm00elVkQlY0QTZUNzFkcFVLSTFnZHJYODVLdng5VDFpQlZzT2JMeDJrTjlCVlR1WFZ5X1JVUzVIcE4xZXVwN2ZJZ25ONnEzWXNrcUhN?oc=5) ⭐️ 8.0/10

Nature 报道了一种基于神经活动数据训练的基础模型，它能够预测训练期间未出现过的刺激类型所引发的大脑反应。所提供的新闻内容未说明模型名称、数据集、实验环境或性能指标。 对未见刺激实现泛化是神经解码和计算神经科学中的核心难题，因为采集带标签的脑活动数据成本高且规模有限。具备这种能力的模型可能提升生物医学建模的数据效率，并最终支持研究和脑机接口开发，但该报道尚未证明任何临床应用。 现有描述仅支持该模型能够预测此前未见刺激类型的反应这一结论；其中没有提供神经记录方式、实验对象、模型架构、比较基线或误差指标等信息。因此，这项成果应被视为研究进展，而非经过验证的临床神经解码证据。

google\_news · Nature · 4月9日 07:00

**背景**: 神经活动记录反映了与脑细胞和神经回路相关的、不断变化的电信号或其他相关信号。神经解码利用这些测量数据来估计人或动物在刺激下感知、意图或执行的行为。基础模型通常在广泛的数据集上训练，以便其学到的表征能够适应或泛化到训练中未被明确包含的任务或数据条件。

**标签**: `#medical AI`, `#computational neuroscience`, `#foundation models`, `#neural decoding`, `#biomedical machine learning`

---

<a id="item-6"></a>
## [通用大语言模型在医学基准中超越临床 AI 工具](https://news.google.com/rss/articles/CBMiX0FVX3lxTE54SDl4dzQxX3BOdU9sNjRMWU8tQ29mYVpxRURxeWlZZ20zQVpramJCZVd0QlVOZmZqb3JvVkc2Qm5jaURhV3NCdVNIdUJIQTZHdjhlbEZEcDB6eG5wUDN3?oc=5) ⭐️ 8.0/10

《自然-医学》于 2026 年 6 月 12 日发表的一项评估，将临床 AI 工具 OpenEvidence 和 UpToDate Expert AI 与 GPT-5.2、Gemini 3.1 Pro 及 Claude Opus 4.6 进行了比较。通用前沿大语言模型在该研究的医学基准评估中超过了这些专用临床工具。 这一结果挑战了“面向医疗的专用产品必然比领先通用模型具有更强医学推理能力”的假设。因此，医疗机构应依据自身任务、工作流程、安全要求和实际结果评估模型，而不应只因其医疗领域定位而进行选择。 这项《自然-医学》研究评估了两种临床工具和三种前沿大语言模型，其第一阶段使用了 500 道 MedQA 题目。基准测试表现更好并不自动证明临床实用性，部署评估还需要考察工作流程整合、稳健性、公平性、幻觉、持续监测以及与患者相关的结果。

google\_news · Nature · 6月12日 07:00

**背景**: 大语言模型通过从大规模数据集中学习模式来生成和理解文本，通用 AI 产品和临床 AI 产品都可以采用这类模型。MedQA 等医学问答基准用于衡量结构化医学知识和推理任务的表现，但无法完全复现真实医疗系统中杂乱的临床记录或多步骤工作。因而，现实医疗场景中的 AI 评估必须超越准确率，进一步衡量临床决策、安全性、工作流程影响以及部署后的模型漂移。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.nature.com/articles/s41591-026-04431-5">General-purpose large language models outperform specialized clinical AI tools on medical benchmarks | Nature Medicine</a></li>
<li><a href="https://hai.stanford.edu/news/stanford-develops-real-world-benchmarks-for-healthcare-ai-agents">Stanford Develops Real-World Benchmarks for Healthcare AI ...</a></li>
<li><a href="https://publichealthaihandbook.com/implementation/evaluation.html">Evaluating AI Systems for Healthcare – The Public Health AI Handbook</a></li>

</ul>
</details>

**标签**: `#clinical-llms`, `#medical-ai`, `#benchmarking`, `#model-evaluation`, `#healthcare-deployment`

---

<a id="item-7"></a>
## [FRIGID 扩展质谱分子生成能力](https://arxiv.org/abs/2604.16648) ⭐️ 7.5/10

FRIGID 是一种扩散语言模型框架，可通过中间指纹表示和已确定的化学式，根据串联质谱生成分子结构。该方法在数亿个无标注分子结构上训练，并在推理时利用碎裂模型引导的重新掩码和去噪来修正与质谱不一致的候选结构。 从串联质谱中识别未知小分子仍是代谢组学及相关发现流程中的重要瓶颈。FRIGID 表明，大规模无标注分子训练和额外的推理时计算都能显著改善从头结构解析，对生物医学研究和药物发现流程具有潜在价值。 论文报告称，FRIGID 在具有挑战性的 MassSpecGym 基准上取得了超过 18%的 Top-1 准确率，并在 NPLIB1 上将领先方法的 Top-1 准确率提高至三倍。其优化循环使用前向碎裂模型定位不一致的片段，作者还报告性能会随推理时计算量增加而呈对数线性扩展；摘要未提供外部部署或验证证据。

rss · arXiv q-bio.QM · 7月28日 04:00

**背景**: 串联质谱通过反复测量分子及其产生的碎片来识别分子片段，但多个结构可能产生相似的质谱。从头结构解析试图直接根据这些证据推断此前未知的分子结构，而不是只从固定的库中选择。扩散模型会迭代地将带噪声或被掩码的表示转换为候选输出；在这里，FRIGID 将这一过程用于分子表示，并根据预测的碎裂行为检查候选结构。

**标签**: `#biomedical AI`, `#molecular generation`, `#mass spectrometry`, `#diffusion models`, `#drug discovery`

---

<a id="item-8"></a>
## [AI 编程智能体重塑科学计算](https://openai.com/index/scientific-computing-agentic-ai) ⭐️ 7.0/10

OpenAI 发布了一份实地报告，介绍科学家如何使用 AI 编程智能体改造科学计算工作流，并加速包括基因组学在内的软件开发与科学发现。该报告认为，这类智能体正在降低工程人力和专业能力对不同科学项目的限制。 科学团队通常依赖专业软件、数据管道和高性能计算工作流，因此更快的实现速度能够缩短从研究设想到可分析结果之间的周期。该报告也将关注点转向一个核心运营挑战：研究人员仍必须依靠人类判断来验证智能体生成的代码和科学输出。 OpenAI 所引用的结论主要是定性的：这些项目在范围上差异很大，而所提供材料没有给出部署指标、评估方法或技术架构。在基因组学中，工作流通常需要将定制的数据集和处理步骤转换为计算命令，因此正确性、可复现性和审查尤为重要。

rss · OpenAI Blog · 7月28日 17:00

**背景**: AI 编程智能体是能够通过迭代使用工具和反馈来协助编写、修改、测试及组织软件的系统。科学计算是指利用软件和计算基础设施分析数据、运行模拟或执行研究管道。基因组学是一个典型案例，因为处理遗传数据通常需要复杂、可配置的高性能计算工作流。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://openai.com/index/scientific-computing-agentic-ai/">Scientific computing in the age of agentic AI | OpenAI</a></li>
<li><a href="https://aws.amazon.com/vi/blogs/architecture/genomics-workflows-part-3-automated-workflow-manager/?nc2=h_mo-lang">Genomics workflows , Part 3: automated workflow manager</a></li>

</ul>
</details>

**标签**: `#agentic-ai`, `#scientific-computing`, `#genomics`, `#biomedical-ai`, `#ai-coding-agents`

---

<a id="item-9"></a>
## [TCellAlign 统一跨单细胞研究的 T 细胞标签](https://arxiv.org/abs/2607.24093) ⭐️ 7.0/10

TCellAlign 提出了一套由命名体系引导的多智能体工作流，通过检索文献、提取证据和基于证据的裁决，将研究特定的 T 细胞群体标签对齐到标准术语。作者还构建了一个经人工验证的基准数据集，涵盖 44 项已发表研究、超过 700 万个细胞，以及健康、癌症、感染性疾病和炎症性疾病四类场景。 不一致的细胞类型标签使得不同单细胞研究中表面上等价的 T 细胞群体难以比较，从而限制了可重复性和生物学知识整合。在保留证据的前提下实现标准化，可能使整合数据集更可靠，并支持后续分析及细胞基础模型训练。 该框架在分配可跨研究比较的标准化标签时，会保留每项研究的原始术语及其支持证据，而不是直接替换原始注释。摘要称其相较基于本体的方法具有更强的语义一致性，并且在开源和闭源 LLM 后端下保持了转录组一致性，但未提供详细的基准指标或外部验证结果。

rss · arXiv q-bio.QM · 7月28日 04:00

**背景**: 单细胞研究测量单个细胞的分子特征，并通常为 T 细胞亚型或功能状态等细胞群体分配标签。即使不同研究组依据的标记物或证据存在重叠，它们也常为生物学上相似的群体使用不同名称。Cell Ontology 和领域命名框架等受控词表旨在使这些注释能够互操作，但将已发表研究中的标签映射到这些词表，需要解读研究背景和支持证据。

**标签**: `#medical-ai`, `#single-cell-genomics`, `#multi-agent-systems`, `#biomedical-knowledge-graphs`, `#data-standardization`

---