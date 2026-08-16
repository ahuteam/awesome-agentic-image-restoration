# Awesome Agentic Image Restoration

A curated, source-checked collection of research on agents for image restoration, computational imaging, and closely related adaptive image-processing systems.

This repository accompanies the review **Agentic Image Restoration: A Structured Review**. The catalogue follows a controller-centred taxonomy and distinguishes autonomous closed-loop agents from prompt-conditioned restoration networks and adjacent systems.

> Last verified: 16 August 2026. A dash in the **Code / project** column means that no author-linked public implementation was verified at the time of the audit. Retracted or withdrawn papers are not included.

## Contents

- [Review paper](#review-paper)
- [Taxonomy](#taxonomy)
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

## Taxonomy

| Class | Controller pattern | Typical capability |
|---|---|---|
| P1 | Cybernetic / reinforcement-learning controller | Selects actions, paths, or parameters from feedback |
| P2 | Prompt- or condition-routed restorer | Conditions a learned restoration mapping; usually open loop |
| P3 | MLLM reasoning and tool use | Diagnoses degradation and orchestrates external tools |
| P4 | Memory-augmented agent | Reuses episodic, causal, or distilled experience |
| P5 | Multi-agent system | Coordinates specialist agents or fast/slow roles |

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
