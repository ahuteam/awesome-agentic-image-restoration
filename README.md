# Awesome Agentic Image Restoration

A curated, source-checked collection of research on agents for image restoration, computational imaging, and closely related adaptive image-processing systems.

This repository accompanies the review **Agentic Image Restoration: A Structured Review**. The catalogue follows a controller-centred taxonomy and distinguishes autonomous closed-loop agents from prompt-conditioned restoration networks and adjacent systems.

> Last verified: 16 August 2026. A dash in the **Code / project** column means that no author-linked public implementation was verified at the time of the audit. Retracted or withdrawn papers are not included.

![Conventional restoration, prompt-conditioned restoration, and closed-loop restoration agents](assets/figures/paradigm_comparison.png)

## At a glance

| Coverage | Current release |
|---|---|
| Time span | 2018–2026 |
| Curated papers and benchmark resources | 45 |
| Verified public code repositories | 23 |
| Verified author project pages | 3 |
| Controller categories | 5 |
| Application scope | Natural images, photography, driving, medical imaging, remote sensing, cultural heritage, and scientific microscopy |

### What this repository adds

- A controller-centred P1–P5 taxonomy that separates policy learning, conditional routing, tool-using MLLM agents, memory-augmented agents, and multi-agent systems.
- Direct links to stable paper records and author-linked code or project pages.
- A source-traceable quantitative review that keeps results within their original benchmark protocols.
- An explicit distinction between image-quality evaluation and agent-level evaluation, including tool calls, retries, latency, memory, cost, and failure recovery.
- A maintained withdrawal policy. Records with a confirmed retraction or withdrawal signal are removed rather than retained as a separate category.

## Contents

- [Review paper](#review-paper)
- [At a glance](#at-a-glance)
- [Visual overview](#visual-overview)
- [Taxonomy](#taxonomy)
- [Benchmarks and evaluation](#benchmarks-and-evaluation)
- [Open-source starting points](#open-source-starting-points)
- [P1: Cybernetic and reinforcement-learning agents](#p1-cybernetic-and-reinforcement-learning-agents)
- [P2: Prompt-conditioned restoration](#p2-prompt-conditioned-restoration)
- [P3: MLLM reasoning and tool use](#p3-mllm-reasoning-and-tool-use)
- [P4: Memory-augmented restoration agents](#p4-memory-augmented-restoration-agents)
- [P5: Multi-agent restoration systems](#p5-multi-agent-restoration-systems)
- [Domain extensions and evaluation suites](#domain-extensions-and-evaluation-suites)
- [Contributing](#contributing)
- [Citation](#citation)

## Review paper

- [Compiled review PDF](paper/agentic_image_restoration.pdf)
- [Overleaf-ready source package](paper/Agentic_image_restoration_Overleaf.zip)
- [Reference-verification summary](paper/reference_verification_report.md)

**Authors:** Yuezhe Yang, Chengru Li, Zhuodong Chai, Xingbo Dong, and Zhe Jin. Xingbo Dong is the corresponding author.

### Repository layout

```text
.
├── assets/figures/                         # GitHub-ready overview figures
├── paper/agentic_image_restoration.pdf    # Compiled review
├── paper/Agentic_image_restoration_Overleaf.zip
├── paper/reference_verification_report.md
└── README.md                               # Curated paper and code index
```

## Visual overview

### From restoration mapping to restoration agent

Conventional restoration applies a fixed mapping. Prompt-conditioned systems expose task control but generally remain open loop. Restoration agents add perception, scheduling, execution, verification, and conditional replanning.

### Four-component AIR anatomy

The review describes an AIR system through four interacting components: perception, decision, tool execution, and reflection or memory. This anatomy is orthogonal to the P1–P5 controller taxonomy and can be used to compare systems within the same category.

![Four-component anatomy of agentic image restoration](assets/figures/air_anatomy.png)

### Development timeline

The literature develops through overlapping controller paradigms rather than a single linear succession. Deep-RL tool selection and prompt routing remain relevant while MLLM tool use, memory-guided search, and multi-agent collaboration expand the action and feedback spaces.

![Development timeline of agentic image restoration](assets/figures/development_timeline.png)

## Taxonomy

| Class | Controller pattern | Typical capability |
|---|---|---|
| P1 | Cybernetic / reinforcement-learning controller | Selects actions, paths, or parameters from feedback |
| P2 | Prompt- or condition-routed restorer | Conditions a learned restoration mapping; usually open loop |
| P3 | MLLM reasoning and tool use | Diagnoses degradation and orchestrates external tools |
| P4 | Memory-augmented agent | Reuses episodic, causal, or distilled experience |
| P5 | Multi-agent system | Coordinates specialist agents or fast/slow roles |

### Classification guide

| Question | Interpretation |
|---|---|
| Does the system choose an action, route, path, or parameter from feedback? | P1 candidate |
| Does a prompt or learned condition modulate a fixed restoration network without an external action loop? | P2 candidate |
| Does an MLLM diagnose degradation and call external restoration tools? | P3 candidate |
| Does the controller retrieve, update, or reuse persistent restoration experience? | P4 candidate |
| Are multiple specialist or fast/slow agents coordinated explicitly? | P5 candidate |

Hybrid and boundary systems are labelled by their dominant controller. A generative restorer is not considered agentic solely because it accepts text. The decisive evidence is runtime control over actions, feedback, stopping, replanning, memory, or collaboration.

## Benchmarks and evaluation

### Dataset and protocol families

| Family | Representative resources | Main evaluation target |
|---|---|---|
| Mixed natural-image degradation | MiO100-derived protocols, CDD-11 | Degradation diagnosis, restoration order, tool coordination, and rollback |
| Denoising, deraining, dehazing, deblurring, and low light | BSD68, SIDD, Rain100L/H, SOTS, GoPro, RealBlur, LOL | Fidelity and perceptual restoration quality |
| High-resolution restoration | DIV2K and 4K derivatives | Recursive super-resolution and region-aware execution |
| Medical imaging | fastMRI-related protocols and AAPM low-dose CT | Sampling, reconstruction, parameter control, and physics-aware correction |
| Downstream perception | nuScenes and HRSC-Robust | Detection or perception utility after restoration |
| Scientific and cultural imaging | Microscopy, inscriptions, murals, and remote-sensing imagery | Domain validity, semantic preservation, and expert-guided recovery |

### Minimum reporting checklist

| Dimension | Recommended reporting |
|---|---|
| Output fidelity | PSNR and SSIM with dataset, split, degradation, and clean-reference availability |
| Perceptual quality | LPIPS, DISTS, or NR-IQA with metric direction and implementation |
| Downstream utility | Fixed downstream model, degraded-input baseline, mAP, mIoU, or task-specific error |
| Agent execution | Tool registry, calls, planning steps, retries, stop rule, and failure rate |
| Efficiency | End-to-end latency, hardware, VRAM, tokens or API cost, and concurrency |
| Robustness and safety | Worsening rate, hallucination or provenance failures, rollback behaviour, and audit trail |

Quantitative values should only be compared directly when inputs, degradation generation, available tools, feedback functions, and execution budgets are aligned. The review therefore reports source-traceable examples within their native protocols instead of constructing an artificial cross-paper leaderboard.

## Open-source starting points

For readers who want to reproduce the main controller patterns quickly:

| Pattern | Recommended project |
|---|---|
| Sequential tool selection | [RL-Restore](https://github.com/yuke93/RL-Restore) |
| Pixel-level reinforcement learning | [PixelRL](https://github.com/rfuruta/pixelRL) |
| Dynamic network-path selection | [Path-Restore](https://github.com/yuke93/Path-Restore) |
| Prompt-conditioned restoration | [PromptIR](https://github.com/va1shn9v/PromptIR) and [InstructIR](https://github.com/mv-lab/InstructIR) |
| MLLM tool orchestration | [AgenticIR](https://github.com/Kaiwen-Zhu/AgenticIR) |
| Iterative restore–assess loop | [RAR](https://github.com/saic-fi/RAR) |
| Joint plan and execution optimization | [OPERA](https://github.com/xsyshuishui/Opera) |
| Frequency-aware planning | [FAPE-IR](https://github.com/Programmergg/FAPE-IR) |
| Driving-oriented restoration | [JarvisIR](https://github.com/LYL1015/JarvisIR) |
| 4K super-resolution agent | [4KAgent](https://github.com/taco-group/4KAgent) |
| Medical reconstruction and sampling | [DUAL](https://github.com/yanweipang/mri) and [KSRO](https://github.com/Ruru-Xu/KSRO) |
| Domain-specific restoration agents | [RIR-Agent](https://github.com/Arispur-311/RIR-Agent), [EpiAgent](https://github.com/blackprotoss/EpiAgent), and [MAPGR](https://github.com/tiskun101-oss/MAPGR) |

## P1: Cybernetic and reinforcement-learning agents

| Year | Work | Venue | Paper | Code / project |
|---|---|---|---|---|
| 2018 | Intelligent Parameter Tuning in Optimization-Based Iterative CT Reconstruction via Deep Reinforcement Learning | IEEE TMI | [Paper](https://doi.org/10.1109/TMI.2018.2823679) | [Code](https://github.com/heixscy88/TMI_parameter_tuning) |
| 2018 | RL-Restore: Crafting a Toolchain for Image Restoration by Deep Reinforcement Learning | CVPR | [Paper](https://openaccess.thecvf.com/content_cvpr_2018/html/Yu_Crafting_a_Toolchain_CVPR_2018_paper.html) | [Code](https://github.com/yuke93/RL-Restore) |
| 2018 | Distort-and-Recover: Color Enhancement Using Deep Reinforcement Learning | CVPR | [Paper](https://openaccess.thecvf.com/content_cvpr_2018/html/Park_Distort-and-Recover_Color_Enhancement_CVPR_2018_paper.html) | — |
| 2019 | PixelRL: Fully Convolutional Network with Multi-Step Reinforcement Learning for Image Processing | AAAI | [Paper](https://doi.org/10.1609/aaai.v33i01.33013598) | [Code](https://github.com/rfuruta/pixelRL) |
| 2020 | Low-Dose CT Denoising via Joint Bilateral Filtering and Intelligent Parameter Optimization | CT Meeting | [Paper](https://arxiv.org/abs/2007.04768) | — |
| 2022 | Path-Restore: Learning Network Path Selection for Image Restoration | IEEE TPAMI | [Paper](https://doi.org/10.1109/TPAMI.2021.3080863) | [Code](https://github.com/yuke93/Path-Restore) |
| 2024 | Dual States Based Reinforcement Learning for Fast MR Scan and Image Reconstruction | Neurocomputing | [Paper](https://doi.org/10.1016/j.neucom.2023.127067) | [Code](https://github.com/yanweipang/mri) |
| 2024 | Intelligent Agent Planning for Optimizing Parallel MRI Reconstruction via a Large Language Model | EMBC | [Paper](https://doi.org/10.1109/EMBC53108.2024.10782629) | — |
| 2025 | Optimized MRI Sampling with Region-Specific Fidelity (KSRO) | Neurocomputing | [Paper](https://doi.org/10.1016/j.neucom.2025.130116) | [Code](https://github.com/Ruru-Xu/KSRO) |
| 2026 | PaAgent: Portrait-Aware Image Restoration Agent via Subjective-Objective Reinforcement Learning | arXiv | [Paper](https://arxiv.org/abs/2603.17055) | — |
| 2026 | Restore-R1: Efficient Image Restoration Agents via Reinforcement Learning with Multimodal LLM Perceptual Feedback | CVPR Findings | [Paper](https://openaccess.thecvf.com/content/CVPR2026F/html/Lu_Restore-R1_Efficient_Image_Restoration_Agents_via_Reinforcement_Learning_with_Multimodal_CVPRF_2026_paper.html) | — |

## P2: Prompt-conditioned restoration

| Year | Work | Venue | Paper | Code / project |
|---|---|---|---|---|
| 2022 | AirNet: All-in-One Image Restoration for Unknown Corruption | CVPR | [Paper](https://openaccess.thecvf.com/content/CVPR2022/html/Li_All-in-One_Image_Restoration_for_Unknown_Corruption_CVPR_2022_paper.html) | [Code](https://github.com/XLearning-SCU/2022-CVPR-AirNet) |
| 2023 | PromptIR: Prompting for All-in-One Blind Image Restoration | NeurIPS | [Paper](https://proceedings.neurips.cc/paper_files/paper/2023/hash/e187897ed7780a8c3f50a8fc8997e6b1-Abstract-Conference.html) | [Code](https://github.com/va1shn9v/PromptIR) |
| 2024 | InstructIR: High-Quality Image Restoration Following Human Instructions | ECCV | [Paper](https://arxiv.org/abs/2401.16468) | [Code](https://github.com/mv-lab/InstructIR) |
| 2024 | DA-CLIP: Distribution-Aware Prompting for Vision-Language Models | ICLR | [Paper](https://openreview.net/forum?id=HBA5UGjv7r) | [Code](https://github.com/Algolzw/daclip-uir) |
| 2024 | AutoDIR: Automatic All-in-One Image Restoration with Latent Diffusion | ECCV | [Paper](https://arxiv.org/abs/2310.10123) | [Code](https://github.com/jiangyitong/AutoDIR) |
| 2024 | OneRestore: A Universal Restoration Framework for Composite Degradation | ECCV | [Paper](https://arxiv.org/abs/2407.04621) | [Code](https://github.com/gy65896/OneRestore) |

## P3: MLLM reasoning and tool use

| Year | Work | Venue | Paper | Code / project |
|---|---|---|---|---|
| 2023 | Clarity ChatGPT: An Interactive and Adaptive Processing System for Image Restoration and Enhancement | arXiv | [Paper](https://arxiv.org/abs/2311.11695) | — |
| 2024 | RestoreAgent: Autonomous Image Restoration Agent via Multimodal Large Language Models | NeurIPS | [Paper](https://proceedings.neurips.cc/paper_files/paper/2024/hash/c78f639424b8d89ceb4f2efbb4dfe4f4-Abstract.html) | [Project](https://haoyuchen.com/RestoreAgent) |
| 2025 | JarvisIR: Elevating Autonomous Driving Perception with Intelligent Image Restoration | CVPR | [Paper](https://openaccess.thecvf.com/content/CVPR2025/html/Lin_JarvisIR_Elevating_Autonomous_Driving_Perception_with_Intelligent_Image_Restoration_CVPR_2025_paper.html) | [Code](https://github.com/LYL1015/JarvisIR) |
| 2025 | 4KAgent: Agentic Any Image to 4K Super-Resolution | NeurIPS | [Paper](https://proceedings.neurips.cc/paper_files/paper/2025/hash/f0075fe4e59652cf43148dcfab8d3c93-Abstract-Conference.html) | [Code](https://github.com/taco-group/4KAgent) |
| 2025/2026 | AgentMRI: A Vision-Language Model-Powered AI System for Self-Regulating MRI Reconstruction | JIIM | [Paper](https://doi.org/10.1007/s10278-025-01617-0) | — |
| 2026 | Restore, Assess, Repeat (RAR) | CVPR | [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Chen_Restore_Assess_Repeat_A_Unified_Framework_for_Iterative_Image_Restoration_CVPR_2026_paper.html) | [Code](https://github.com/saic-fi/RAR) |
| 2026 | EpiAgent: An Agent-Centric System for Ancient Inscription Restoration | CVPR | [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Zhu_EpiAgent_An_Agent-Centric_System_for_Ancient_Inscription_Restoration_CVPR_2026_paper.html) | [Code](https://github.com/blackprotoss/EpiAgent) |
| 2026 | SIMBA: An Agentic AI Platform for Single-Molecule Multi-Dimensional Imaging | bioRxiv | [Paper](https://doi.org/10.64898/2026.04.16.719005) | — |
| 2026 | FAPE-IR: Frequency-Aware Planning and Execution for All-in-One Image Restoration | CVPR | [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Liu_FAPE-IR_Frequency-Aware_Planning_and_Execution_Framework_for_All-in-One_Image_Restoration_CVPR_2026_paper.html) | [Code](https://github.com/Programmergg/FAPE-IR) |
| 2026 | OPERA: Joint Planning-Execution Optimization for Image Restoration | arXiv | [Paper](https://arxiv.org/abs/2605.22104) | [Code](https://github.com/xsyshuishui/Opera) |
| 2026 | DiTTo: Scalable Order-Aware All-in-One Image Restoration Agent | arXiv | [Paper](https://arxiv.org/abs/2605.30915) | [Project](https://cmlab-korea.github.io/DiTTo/) |
| 2025 | Q-Agent: Quality-Driven Chain-of-Thought Image Restoration Agent | arXiv | [Paper](https://arxiv.org/abs/2504.07148) | — |

## P4: Memory-augmented restoration agents

| Year | Work | Venue | Paper | Code / project |
|---|---|---|---|---|
| 2025 | AgenticIR: An Intelligent Agentic System for Complex Image Restoration Problems | ICLR | [Paper](https://proceedings.iclr.cc/paper_files/paper/2025/hash/921ac785fa9edc73cacaf2664f43d234-Abstract-Conference.html) | [Code](https://github.com/Kaiwen-Zhu/AgenticIR) |
| 2026 | SEAR: Self-Evolving Agentic Image Restoration via Deliberate Planning and Intuitive Execution | arXiv | [Paper](https://arxiv.org/abs/2606.28971) | — |
| 2026 | Causal-AgentIR: Self-Evolving Causal Memory for Adaptive Image Restoration Agents | arXiv | [Paper](https://arxiv.org/abs/2607.21125) | — |

## P5: Multi-agent restoration systems

| Year | Work | Venue | Paper | Code / project |
|---|---|---|---|---|
| 2026 | Multi-Agent Image Restoration (MAIR) | IJCV | [Paper](https://doi.org/10.1007/s11263-026-02792-5) | [Project](https://villa.jianzhang.tech/publication/200604/) |
| 2026 | Hybrid Agents for Image Restoration | CVPR | [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Li_Hybrid_Agents_for_Image_Restoration_CVPR_2026_paper.html) | — |
| 2026 | MAPGR: Multi-Agent Prompt-Guided Residual Diffusion for Ancient Mural Restoration | npj Heritage Science | [Paper](https://doi.org/10.1038/s40494-026-02607-3) | [Code](https://github.com/tiskun101-oss/MAPGR) |
| 2026 | CLEAR: Cognitive LLM-Empowered Adaptive Restoration for Robust Ship Detection | Remote Sensing | [Paper](https://doi.org/10.3390/rs18081142) | — |

## Domain extensions and evaluation suites

| Year | Work | Domain | Paper | Code / project |
|---|---|---|---|---|
| 2025 | Self-Explained Thinking Agent for Autonomous Microscopy Restoration (FMIRAgent) | Microscopy | [Paper](https://doi.org/10.21203/rs.3.rs-7116422/v1) | — |
| 2026 | RIR-Agent | Remote sensing | [Paper](https://doi.org/10.1016/j.eswa.2026.132495) | [Code](https://github.com/Arispur-311/RIR-Agent) |
| 2026 | ImagingBench | Computational imaging benchmark | [Paper](https://arxiv.org/abs/2607.07189) | — |
| 2026 | Imaging-101 | Computational imaging benchmark | [Paper](https://arxiv.org/abs/2607.10789) | [Code](https://github.com/AI4ImagingLab/imaging-101-release) |
| 2026 | Agentic Autoresearch for CT Reconstruction | CT reconstruction | [Paper](https://arxiv.org/abs/2607.22824) | — |
| 2025 | Prompt-Agent-Driven Integration of Foundation Model Priors for Low-Count PET Reconstruction | PET | [Paper](https://doi.org/10.1109/TMI.2025.3527155) | — |
| 2026 | PhotoAgent | Aesthetic photo editing | [Paper](https://arxiv.org/abs/2602.22809) | [Code](https://github.com/mdyao/PhotoAgent) |
| 2025 | PhotoArtAgent | Photo retouching | [Paper](https://arxiv.org/abs/2505.23130) | — |
| 2026 | RetouchIQ | Instruction-based photo retouching | [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Wu_RetouchIQ_MLLM_Agents_for_Instruction-Based_Image_Retouching_with_Generalist_Reward_CVPR_2026_paper.html) | — |

## Contributing

Contributions are welcome. Please open an issue or pull request with the paper title, publication record, stable paper URL, official code or project URL, and a short justification for its taxonomy placement. Withdrawn or retracted work will be removed after verification against the publisher or preprint record.

## Citation

Citation metadata will be updated when the review receives a permanent publication record. Until then, please cite the repository and the accompanying manuscript.

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
