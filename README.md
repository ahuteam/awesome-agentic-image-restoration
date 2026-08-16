# Agentic Image Restoration

Our team built this project for the paper **Agentic Image Restoration: A Structured Review**.

This companion resource organizes the Agentic Image Restoration literature through a controller-centered taxonomy and provides source-linked papers, public implementations, benchmark resources, and evaluation guidance.

<p align="center">
  <img src="assets/figures/paradigm_comparison.png" alt="Comparison of conventional restoration, prompt-conditioned restoration, and restoration agents" width="900">
</p>

<p align="center"><sub><strong>Figure 1.</strong> Conventional models use a fixed input-to-output mapping, prompt-conditioned models add task instructions, and restoration agents operate through a closed perceive-plan-execute-verify loop.</sub></p>

## Contents

- [Abstract](#abstract)
- [Section 1: Introduction](#section-1--introduction)
- [Section 2: Unified taxonomy](#section-2--unified-taxonomy-of-agentic-image-restoration-systems)
- [Sections 3–7: Controller families](#sections-37--controller-families-and-related-systems)
- [Section 8: Benchmarks and evaluation](#section-8--benchmarks-evaluation-protocols-and-system-metrics)
- [Source-linked manuscript tables](EVIDENCE_TABLES.md)
- [Citation](#citation)

## Abstract

Multimodal foundation models and autonomous systems are extending image restoration from static forward mappings to closed-loop Agentic Image Restoration (AIR). Conventional CNN, Vision Transformer, and diffusion restorers follow predetermined inference procedures and usually lack explicit degradation diagnosis, runtime tool composition, output verification, or persistent experience. AIR introduces decision processes that observe intermediate states, select and execute restoration actions, assess the result, and may revise subsequent actions or memory. We review representative studies published from 2018 to 2026 and introduce a five-category controller taxonomy comprising Cybernetic Reinforcement Learning (P1), Prompt-Conditioned Restoration (P2), MLLM Reasoning and Tool Use (P3), Memory-Augmented Restoration Agents (P4), and Multi-Agent Restoration Systems (P5). A four-component anatomy of perception, decision, action, and reflection or memory provides an orthogonal descriptive framework. We synthesize evidence across natural photography, 4K super-resolution, autonomous driving, medical reconstruction, remote sensing, and scientific microscopy, followed by a protocol-aware discussion of benchmarks and evaluation.

## Section 1 — Introduction

The review treats restoration as a broad computational-imaging problem covering degradation removal, reconstruction, super-resolution, low-light and contrast enhancement, and related quality-improvement tasks. Section 1 contrasts fixed forward models, prompt-conditioned models, and closed-loop agents; introduces the physical degradation model and a POMDP abstraction for AIR; defines the review scope; and states the three main contributions. Figure 1 above provides the corresponding paradigm comparison.

### Review contributions

- A four-component anatomy describes AIR systems through perception, decision, action, and reflection or memory.
- A five-category taxonomy distinguishes reinforcement-learning controllers, prompt-conditioned restoration, MLLM tool use, memory-augmented agents, and multi-agent systems.
- Each indexed work is linked to its publication record and to an author-provided code or project page when available.
- Quantitative results retain their original datasets, degradations, metrics, and evaluation protocols.

### Foundations and adjacent imaging methods discussed in Section 1

| Work | Venue | Year | Paper | Code / project |
|---|---|---:|---|---|
| Nonlinear Total Variation Based Noise Removal Algorithms | Physica D | 1992 | [Paper](https://doi.org/10.1016/0167-2789(92)90242-F) | — |
| Image Denoising by Sparse 3-D Transform-Domain Collaborative Filtering | IEEE TIP | 2007 | [Paper](https://doi.org/10.1109/TIP.2007.901238) | — |
| Learning a Deep Convolutional Network for Image Super-Resolution | ECCV | 2014 | [Paper](https://doi.org/10.1007/978-3-319-10593-2_13) | — |
| Beyond a Gaussian Denoiser: Residual Learning of Deep CNN for Image Denoising | IEEE TIP | 2017 | [Paper](https://doi.org/10.1109/TIP.2017.2662206) | [Code](https://github.com/cszn/DnCNN) |
| SwinIR: Image Restoration Using Swin Transformer | ICCV Workshops | 2021 | [Paper](https://doi.org/10.1109/ICCVW54120.2021.00210) | [Code](https://github.com/JingyunLiang/SwinIR) |
| Learning Transferable Visual Models From Natural Language Supervision | ICML | 2021 | [Paper](https://proceedings.mlr.press/v139/radford21a.html) | [Code](https://github.com/openai/CLIP) |
| Restormer: Efficient Transformer for High-Resolution Image Restoration | CVPR | 2022 | [Paper](https://doi.org/10.1109/CVPR52688.2022.00564) | [Code](https://github.com/swz30/Restormer) |
| Simple Baselines for Image Restoration | ECCV | 2022 | [Paper](https://doi.org/10.1007/978-3-031-20071-7_2) | [Code](https://github.com/megvii-research/NAFNet) |
| Towards Robust Blind Face Restoration with Codebook Lookup Transformer | NeurIPS | 2022 | [Paper](https://proceedings.neurips.cc/paper_files/paper/2022/hash/c573258c38d0a3919d8c1364053c45df-Abstract-Conference.html) | [Code](https://github.com/sczhou/CodeFormer) |
| Exploiting Diffusion Prior for Real-World Image Super-Resolution | IJCV | 2024 | [Paper](https://doi.org/10.1007/s11263-024-02168-7) | [Code](https://github.com/IceClear/StableSR) |
| Abandoning the Bayer-Filter To See in the Dark | CVPR | 2022 | [Paper](https://openaccess.thecvf.com/content/CVPR2022/html/Dong_Abandoning_the_Bayer-Filter_To_See_in_the_Dark_CVPR_2022_paper.html) | — |
| RawFormer: An Efficient Vision Transformer for Low-Light RAW Image Enhancement | IEEE SPL | 2022 | [Paper](https://doi.org/10.1109/LSP.2022.3233005) | — |
| $L^2$DM: A Diffusion Model for Low-Light Image Enhancement | PRCV | 2023 | [Paper](https://doi.org/10.1007/978-981-99-8552-4_11) | — |
| Low-Light Image Enhancement with Luminance Duality | Knowledge-Based Systems | 2025 | [Paper](https://doi.org/10.1016/j.knosys.2025.114420) | — |
| Lightweight Omnidirectional Super-Resolution via Frequency-Spatial Fusion and Equirectangular Projection Correction | Journal of Electronic Imaging | 2025 | [Paper](https://doi.org/10.1117/1.JEI.34.2.023008) | — |
| RawRWKV: An Efficient Raw Image Enhancement Framework via RWKV Architecture | Signal, Image and Video Processing | 2025 | [Paper](https://doi.org/10.1007/s11760-025-04940-9) | — |
| EvRWKV: A Continuous Interactive RWKV Framework for Effective Event-Guided Low-Light Image Enhancement | IEEE TCSVT | 2026 | [Paper](https://doi.org/10.1109/TCSVT.2026.3672491) | — |
| PriP: A Training-Free Low-Light Image Enhancement Framework via Content and Illumination Synergistic Guidance | Computers & Graphics | 2026 | [Paper](https://doi.org/10.1016/j.cag.2026.104676) | — |

## Section 2 — Unified Taxonomy of Agentic Image Restoration Systems

| Category | Controller pattern | Defining capability |
|---|---|---|
| P1 | Cybernetic or reinforcement-learning controller | Selects actions, paths, regions, or parameters from feedback |
| P2 | Prompt- or condition-routed restorer | Conditions a learned restoration mapping, usually without an external tool loop |
| P3 | MLLM reasoning and tool use | Diagnoses degradation and orchestrates restoration tools |
| P4 | Memory-augmented restoration agent | Retrieves, updates, or reuses restoration experience |
| P5 | Multi-agent restoration system | Coordinates specialist agents or fast and slow roles |

The categories follow the dominant runtime controller. Hybrid and boundary systems are indexed according to the mechanism that governs action selection, feedback, replanning, memory, or collaboration.

The full architectural matrix, including `Paper` and `Code / project` for every row, is provided in the **[Section 2 source-linked table](EVIDENCE_TABLES.md#section-2--architectural-taxonomy)**.

### Figures 2 and 3

### Four-component AIR anatomy

<p align="center">
  <img src="assets/figures/air_anatomy.png" alt="Four-component anatomy of Agentic Image Restoration" width="900">
</p>

<p align="center"><sub><strong>Figure 2.</strong> Four-component anatomy of AIR. Perception translates a degraded input into an actionable observation, the decision brain selects from a heterogeneous tool space, reflection determines whether to stop, retry, or roll back, and memory records useful experience.</sub></p>

### Development timeline

<p align="center">
  <img src="assets/figures/development_timeline.png" alt="Development timeline of Agentic Image Restoration" width="900">
</p>

<p align="center"><sub><strong>Figure 3.</strong> Representative AIR developments from 2018 to 2026 across cybernetic reinforcement learning, prompt-conditioned routing, MLLM tool orchestration, memory-augmented search, and multi-agent collaboration.</sub></p>

## Sections 3–7 — Controller Families and Related Systems

Titles reproduce the linked publication records. The year column gives the year of the cited version of record or preprint and does not combine online-first and issue years. A dash indicates that no author-linked public implementation was verified.

### Section 3 — Cybernetic Reinforcement Learning

Section 3 formulates cybernetic restoration as sequential decision making over observations, actions, transitions, rewards, and stopping rules. It follows the methodological progression from global parameter tuning and discrete toolchains to pixel-level policies, network-path routing, MRI sampling control, and region-specific acquisition policies.

| Work | Venue | Year | Paper | Code / project |
|---|---|---:|---|---|
| Intelligent Parameter Tuning in Optimization-Based Iterative CT Reconstruction via Deep Reinforcement Learning | IEEE TMI | 2018 | [Paper](https://doi.org/10.1109/TMI.2018.2823679) | [Code](https://github.com/heixscy88/TMI_parameter_tuning) |
| Crafting a Toolchain for Image Restoration by Deep Reinforcement Learning | CVPR | 2018 | [Paper](https://openaccess.thecvf.com/content_cvpr_2018/html/Yu_Crafting_a_Toolchain_CVPR_2018_paper.html) | [Code](https://github.com/yuke93/RL-Restore) |
| Distort-and-Recover: Color Enhancement using Deep Reinforcement Learning | CVPR | 2018 | [Paper](https://openaccess.thecvf.com/content_cvpr_2018/html/Park_Distort-and-Recover_Color_Enhancement_CVPR_2018_paper.html) | — |
| Fully Convolutional Network with Multi-Step Reinforcement Learning for Image Processing | AAAI | 2019 | [Paper](https://doi.org/10.1609/aaai.v33i01.33013598) | [Code](https://github.com/rfuruta/pixelRL) |
| Low Dose CT Denoising via Joint Bilateral Filtering and Intelligent Parameter Optimization | CT Meeting | 2020 | [Paper](https://arxiv.org/abs/2007.04768) | — |
| Path-Restore: Learning Network Path Selection for Image Restoration | IEEE TPAMI | 2022 | [Paper](https://doi.org/10.1109/TPAMI.2021.3080863) | [Code](https://github.com/yuke93/Path-Restore) |
| Dual states based reinforcement learning for fast MR scan and image reconstruction | Neurocomputing | 2024 | [Paper](https://doi.org/10.1016/j.neucom.2023.127067) | [Code](https://github.com/yanweipang/mri) |
| Intelligent Agent Planning for Optimizing Parallel MRI Reconstruction via a Large Language Model | EMBC | 2024 | [Paper](https://doi.org/10.1109/EMBC53108.2024.10782629) | — |
| A Reinforcement Learning Approach for Optimized MRI Sampling with Region-Specific Fidelity | Neurocomputing | 2025 | [Paper](https://doi.org/10.1016/j.neucom.2025.130116) | [Code](https://github.com/Ruru-Xu/KSRO) |
| PaAgent: Portrait-Aware Image Restoration Agent via Subjective-Objective Reinforcement Learning | arXiv | 2026 | [Paper](https://arxiv.org/abs/2603.17055) | [Code, release announced](https://github.com/WYJGR/PaAgent) |
| Restore-R1: Efficient Image Restoration Agents via Reinforcement Learning with Multimodal LLM Perceptual Feedback | CVPR Findings | 2026 | [Paper](https://openaccess.thecvf.com/content/CVPR2026F/html/Lu_Restore-R1_Efficient_Image_Restoration_Agents_via_Reinforcement_Learning_with_Multimodal_CVPRF_2026_paper.html) | — |

### Section 4 — Prompt-Modulated and Condition-Routing Systems

Section 4 separates implicit or learned degradation prompts from language and vision-language conditioning. It also identifies the P2-P3 boundary: model-internal routing can be iterative without becoming an external tool-using MLLM agent, so controller location and runtime feedback determine the category.

| Work | Venue | Year | Paper | Code / project |
|---|---|---:|---|---|
| All-in-One Image Restoration for Unknown Corruption | CVPR | 2022 | [Paper](https://openaccess.thecvf.com/content/CVPR2022/html/Li_All-in-One_Image_Restoration_for_Unknown_Corruption_CVPR_2022_paper.html) | [Code](https://github.com/XLearning-SCU/2022-CVPR-AirNet) |
| PromptIR: Prompting for All-in-One Image Restoration | NeurIPS | 2023 | [Paper](https://proceedings.neurips.cc/paper_files/paper/2023/hash/e187897ed7780a8c3f50a8fc8997e6b1-Abstract-Conference.html) | [Code](https://github.com/va1shn9v/PromptIR) |
| InstructIR: High-Quality Image Restoration Following Human Instructions | ECCV | 2024 | [Paper](https://arxiv.org/abs/2401.16468) | [Code](https://github.com/mv-lab/InstructIR) |
| Controlling Vision-Language Models for Multi-Task Image Restoration | ICLR | 2024 | [Paper](https://openreview.net/forum?id=HBA5UGjv7r) | [Code](https://github.com/Algolzw/daclip-uir) |
| Multimodal Prompt Perceiver: Empower Adaptiveness, Generalizability and Fidelity for All-in-One Image Restoration | CVPR | 2024 | [Paper](https://openaccess.thecvf.com/content/CVPR2024/html/Ai_Multimodal_Prompt_Perceiver_Empower_Adaptiveness_Generalizability_and_Fidelity_for_All-in-One_CVPR_2024_paper.html) | [Code](https://github.com/hhb072/MPerceiver-Code) |
| AutoDIR: Automatic All-in-One Image Restoration with Latent Diffusion | ECCV | 2024 | [Paper](https://arxiv.org/abs/2310.10123) | [Code](https://github.com/jiangyitong/AutoDIR) |
| OneRestore: A Universal Restoration Framework for Composite Degradation | ECCV | 2024 | [Paper](https://arxiv.org/abs/2407.04621) | [Code](https://github.com/gy65896/OneRestore) |
| Language-Driven All-in-One Adverse Weather Removal | CVPR | 2024 | [Paper](https://openaccess.thecvf.com/content/CVPR2024/html/Yang_Language-driven_All-in-one_Adverse_Weather_Removal_CVPR_2024_paper.html) | [Code](https://github.com/noxsine/LDR) |
| SPIRE: Semantic Prompt-Driven Image Restoration | ECCV | 2024 | [Paper](https://arxiv.org/abs/2312.11595) | [Project](https://chenyangqiqi.github.io/tip/) |
| Scaling Up to Excellence: Practicing Model Scaling for Photo-Realistic Image Restoration In the Wild | CVPR | 2024 | [Paper](https://openaccess.thecvf.com/content/CVPR2024/html/Yu_Scaling_Up_to_Excellence_Practicing_Model_Scaling_for_Photo-Realistic_Image_CVPR_2024_paper.html) | [Code](https://github.com/Fanghua-Yu/SUPIR) |
| DreamClear: High-Capacity Real-World Image Restoration with Privacy-Safe Dataset Curation | NeurIPS | 2024 | [Paper](https://proceedings.neurips.cc/paper_files/paper/2024/hash/6452474601429509f3035dc81c233226-Abstract-Conference.html) | [Code](https://github.com/shallowdream204/DreamClear) |
| UniRes: Universal Image Restoration for Complex Degradations | ICCV | 2025 | [Paper](https://openaccess.thecvf.com/content/ICCV2025/html/Zhou_UniRes_Universal_Image_Restoration_for_Complex_Degradations_ICCV_2025_paper.html) | — |

### Section 5 — Single-MLLM Reasoning and Tool-Orchestrating Agents

Section 5 follows the complete controller loop from explicit degradation diagnosis and task-coupled perception to planning, tool selection, verification, iteration, and rollback. The table includes general restoration controllers and application-specific systems in driving, MRI, cultural heritage, microscopy, remote sensing, and scientific imaging.

| Work | Venue | Year | Paper | Code / project |
|---|---|---:|---|---|
| Clarity ChatGPT: An Interactive and Adaptive Processing System for Image Restoration and Enhancement | arXiv | 2023 | [Paper](https://arxiv.org/abs/2311.11695) | — |
| RestoreAgent: Autonomous Image Restoration Agent via Multimodal Large Language Models | NeurIPS | 2024 | [Paper](https://proceedings.neurips.cc/paper_files/paper/2024/hash/c78f639424b8d89ceb4f2efbb4dfe4f4-Abstract.html) | [Project](https://haoyuchen.com/RestoreAgent) |
| JarvisIR: Elevating Autonomous Driving Perception with Intelligent Image Restoration | CVPR | 2025 | [Paper](https://openaccess.thecvf.com/content/CVPR2025/html/Lin_JarvisIR_Elevating_Autonomous_Driving_Perception_with_Intelligent_Image_Restoration_CVPR_2025_paper.html) | [Code](https://github.com/LYL1015/JarvisIR) |
| 4KAgent: Agentic Any Image to 4K Super-Resolution | NeurIPS | 2025 | [Paper](https://proceedings.neurips.cc/paper_files/paper/2025/hash/f0075fe4e59652cf43148dcfab8d3c93-Abstract-Conference.html) | [Code](https://github.com/taco-group/4KAgent) |
| Q-Agent: Quality-Driven Chain-of-Thought Image Restoration Agent through Robust Multimodal Large Language Model | arXiv | 2025 | [Paper](https://arxiv.org/abs/2504.07148) | — |
| AgentMRI: A Vison Language Model-Powered AI System for Self-regulating MRI Reconstruction with Multiple Degradations | JIIM | 2026 | [Paper](https://doi.org/10.1007/s10278-025-01617-0) | — |
| Restore, Assess, Repeat: A Unified Framework for Iterative Image Restoration | CVPR | 2026 | [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Chen_Restore_Assess_Repeat_A_Unified_Framework_for_Iterative_Image_Restoration_CVPR_2026_paper.html) | [Code](https://github.com/saic-fi/RAR) |
| EpiAgent: An Agent-Centric System for Ancient Inscription Restoration | CVPR | 2026 | [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Zhu_EpiAgent_An_Agent-Centric_System_for_Ancient_Inscription_Restoration_CVPR_2026_paper.html) | [Code](https://github.com/blackprotoss/EpiAgent) |
| SIMBA: An Agentic AI Platform for Single-Molecule Multi-Dimensional Imaging | bioRxiv | 2026 | [Paper](https://doi.org/10.64898/2026.04.16.719005) | [Project](https://simba-website-indol.vercel.app/) |
| FAPE-IR: Frequency-Aware Planning and Execution Framework for All-in-One Image Restoration | CVPR | 2026 | [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Liu_FAPE-IR_Frequency-Aware_Planning_and_Execution_Framework_for_All-in-One_Image_Restoration_CVPR_2026_paper.html) | [Code](https://github.com/Programmergg/FAPE-IR) |
| OPERA: An Agent for Image Restoration with End-to-End Joint Planning–Execution Optimization | arXiv | 2026 | [Paper](https://arxiv.org/abs/2605.22104) | [Code](https://github.com/xsyshuishui/Opera) |
| DiTTo: Scalable Order-Aware All-in-One Image Restoration Agent | arXiv | 2026 | [Paper](https://arxiv.org/abs/2605.30915) | [Project](https://cmlab-korea.github.io/DiTTo/) |

### Section 6 — Memory-Augmented and Search-Guided Evolving Agents

Section 6 distinguishes referenceable experience, episodic memory, deliberate search, and causal memory. AgenticIR uses depth-first rollback and stored experience, SEAR combines an intuitive executor with deliberate P-MCTS, and Causal-AgentIR updates a persistent causal memory graph.

| Work | Venue | Year | Paper | Code / project |
|---|---|---:|---|---|
| An Intelligent Agentic System for Complex Image Restoration Problems | ICLR | 2025 | [Paper](https://proceedings.iclr.cc/paper_files/paper/2025/hash/921ac785fa9edc73cacaf2664f43d234-Abstract-Conference.html) | [Code](https://github.com/Kaiwen-Zhu/AgenticIR) |
| Self-Evolving Agentic Image Restoration via Deliberate Planning and Intuitive Execution | arXiv | 2026 | [Paper](https://arxiv.org/abs/2606.28971) | — |
| Causal-AgentIR: Self-Evolving Causal Memory for Adaptive Image Restoration Agents | arXiv | 2026 | [Paper](https://arxiv.org/abs/2607.21125) | — |

### Section 7 — Multi-Agent and Heterogeneous Collaborative Systems

Section 7 covers scheduler-specialist organisation, fast-slow collaboration, feedback roles, and domain-specific coordination. The systems differ in whether roles correspond to restoration experts, processing speeds, reasoning stages, or evidence-handling responsibilities.

| Work | Venue | Year | Paper | Code / project |
|---|---|---:|---|---|
| Multi-Agent Image Restoration | IJCV | 2026 | [Paper](https://doi.org/10.1007/s11263-026-02792-5) | [Project](https://villa.jianzhang.tech/publication/200604/) |
| Hybrid Agents for Image Restoration | CVPR | 2026 | [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Li_Hybrid_Agents_for_Image_Restoration_CVPR_2026_paper.html) | — |
| MAPGR: Multi-Agent Prompt-Guided Residual Diffusion for Ancient Mural Restoration | npj Heritage Science | 2026 | [Paper](https://doi.org/10.1038/s40494-026-02607-3) | [Code](https://github.com/tiskun101-oss/MAPGR) |
| CLEAR: A Cognitive LLM-Empowered Adaptive Restoration Framework for Robust Ship Detection in Complex Maritime Scenarios | Remote Sensing | 2026 | [Paper](https://doi.org/10.3390/rs18081142) | — |

### Cross-section domain extensions and evaluation suites

| Work | Primary manuscript section | Venue | Year | Paper | Code / project |
|---|---:|---|---:|---|---|
| Self-Explained Thinking Agent for Autonomous Microscopy Restoration | 5 | Research Square | 2025 | [Paper](https://doi.org/10.21203/rs.3.rs-7116422/v1) | — |
| RIR-Agent: An Interactive Framework for Effective and Adaptive Restoration of Remote Sensing Imagery | 5 | Expert Systems with Applications | 2026 | [Paper](https://doi.org/10.1016/j.eswa.2026.132495) | [Code](https://github.com/Arispur-311/RIR-Agent) |
| Does AI Understand Imaging? A Systematic Benchmark of Agentic AI for Computational Imaging Tasks | 8 | arXiv | 2026 | [Paper](https://arxiv.org/abs/2607.07189) | — |
| Imaging-101: Benchmarking LLM Coding Agents on Scientific Computational Imaging | 8 | arXiv | 2026 | [Paper](https://arxiv.org/abs/2607.10789) | [Code](https://github.com/AI4ImagingLab/imaging-101-release) |
| Agentic Autoresearch for CT Reconstruction | 1 | arXiv | 2026 | [Paper](https://arxiv.org/abs/2607.22824) | — |
| Prompt-Agent-Driven Integration of Foundation Model Priors for Low-Count PET Reconstruction | 1 | IEEE TMI | 2025 | [Paper](https://doi.org/10.1109/TMI.2025.3527155) | — |
| PhotoAgent: Exploratory Visual Aesthetic Planning with Large Vision Models | 5, 6 | arXiv | 2026 | [Paper](https://arxiv.org/abs/2602.22809) | [Code](https://github.com/mdyao/PhotoAgent) |
| PhotoArtAgent: Intelligent Photo Retouching with Language Model-Based Artist Agents | 5 | arXiv | 2025 | [Paper](https://arxiv.org/abs/2505.23130) | — |
| RetouchIQ: MLLM Agents for Instruction-Based Image Retouching with Generalist Reward | 5 | CVPR | 2026 | [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Wu_RetouchIQ_MLLM_Agents_for_Instruction-Based_Image_Retouching_with_Generalist_Reward_CVPR_2026_paper.html) | — |

## Section 8 — Benchmarks, Evaluation Protocols, and System Metrics

Section 8 covers agent evaluation suites and execution sandboxes, dataset and degradation-protocol families, source-traceable quantitative examples, multidimensional quality and utility metrics, execution behaviour, efficiency, safety, and the information required to reproduce an agent run.

| Evaluation dimension | Representative scope | Paper / implementation links |
|---|---|---|
| Restoration fidelity | PSNR and SSIM with the dataset, split, degradation, and reference availability reported | [SSIM paper](https://doi.org/10.1109/TIP.2003.819861) |
| Perceptual quality | LPIPS, DISTS, MANIQA, MUSIQ, CLIP-IQA, or other source-defined perceptual metrics | [LPIPS paper/code](https://github.com/richzhang/PerceptualSimilarity), [DISTS paper/code](https://github.com/dingkeyan93/DISTS), [MUSIQ paper](https://openaccess.thecvf.com/content/ICCV2021/html/Ke_MUSIQ_Multi-Scale_Image_Quality_Transformer_ICCV_2021_paper.html), [MANIQA paper/code](https://github.com/IIGROUP/MANIQA), [CLIP-IQA paper/code](https://github.com/IceClear/CLIPIQA) |
| Downstream utility | Detection, segmentation, recognition, reconstruction, or scientific measurement performance | [JarvisIR paper/code](https://github.com/LYL1015/JarvisIR), [CLEAR paper](https://doi.org/10.3390/rs18081142) |
| Agent execution | Tool calls, planning steps, retries, stopping rules, failure recovery, and worsening rate | [RestoreAgent project](https://haoyuchen.com/RestoreAgent), [4KAgent paper/code](https://github.com/taco-group/4KAgent) |
| Efficiency | End-to-end latency, hardware, memory, model or API version, and execution budget | [Hybrid Agents paper](https://openaccess.thecvf.com/content/CVPR2026/html/Li_Hybrid_Agents_for_Image_Restoration_CVPR_2026_paper.html) |

Results should be compared directly only when the input construction, degradation protocol, available tools, feedback function, and execution budget are aligned.

### Source-linked Section 8 tables

| Manuscript table | Direct link | Included links |
|---|---|---|
| Benchmark datasets and protocol families | [Open table](EVIDENCE_TABLES.md#section-8--benchmark-datasets) | Dataset sources, representative AIR papers, and available code or project pages |
| Representative quantitative results | [Open table](EVIDENCE_TABLES.md#section-8--representative-quantitative-results) | Paper and code links repeated for every numerical row |
| Evaluation metrics and reproducibility | [Open table](EVIDENCE_TABLES.md#section-8--evaluation-metrics-and-reproducibility) | Metric papers, implementations, evaluation-suite papers, and code |

## Citation

Citation metadata will be updated when the paper receives a permanent publication record.

```bibtex
@misc{yang2026agenticrestoration,
  title  = {Agentic Image Restoration: A Structured Review},
  author = {Yang, Yuezhe and Li, Chengru and Chai, Zhuodong and Dong, Xingbo and Jin, Zhe},
  year   = {2026},
  note   = {Manuscript}
}
```

## Acknowledgements

This work was supported by the National Natural Science Foundation of China (Grant No. 62306003).
