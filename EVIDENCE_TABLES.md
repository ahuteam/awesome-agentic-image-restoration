# Evidence Tables

These tables accompany **Agentic Image Restoration: A Structured Review**. Terminology, datasets, metrics, and numerical values follow the source-aligned manuscript. Values from different datasets or protocols should not be treated as a pooled leaderboard.

[Back to the project overview](README.md)

## Contents

- [Architectural taxonomy](#architectural-taxonomy)
- [Prompt-conditioned systems](#prompt-conditioned-systems)
- [General restoration and editing controllers](#general-restoration-and-editing-controllers)
- [Application-specific controllers](#application-specific-controllers)
- [Memory and search systems](#memory-and-search-systems)
- [Multi-agent systems](#multi-agent-systems)
- [Benchmark datasets](#benchmark-datasets)
- [Representative quantitative results](#representative-quantitative-results)
- [Evaluation and reproducibility](#evaluation-and-reproducibility)

## Architectural taxonomy

| Work | Category | Venue / year | Perception | Action | Feedback / memory | Domain |
|---|---|---|---|---|---|---|
| RL-Restore | P1 | CVPR 2018 | CNN state features | Discrete operator pool (12) | PSNR reward and stop action | Natural images |
| Distort-and-Recover | P1 | CVPR 2018 | Global image state | Discrete global colour actions | Unpaired distort-and-recover reward | Photo retouching |
| PixelRL | P1 | AAAI 2019 | Pixel-wise spatial context | Pixel-level discrete actions | Multi-step pixel reward | Natural images |
| Path-Restore | P1 | TPAMI 2022 | Path-complexity router | Sub-network routing paths | Efficiency-gain signal | Natural images |
| CT-DRL | P1 | TMI 2018 | Iteration-state features | Reconstruction parameters | Scalar quality reward | Medical CT |
| MRI-RL | P1 | Neurocomputing 2024 | Dual k-space states | Sampling-trajectory actions | SSIM reward | Medical MRI |
| AirNet | P2 | CVPR 2022 | Contrastive degradation embedding | Single-backbone feature modulation | Open loop | Natural images |
| PromptIR | P2 | NeurIPS 2023 | Input-conditioned learned prompts | Prompt-modulated Transformer | Open loop | Natural images |
| InstructIR | P2 | ECCV 2024 | Natural-language instruction parsing | Instruction-conditioned network | Open loop | Natural images |
| DA-CLIP | P2 | ICLR 2024 | CLIP content and degradation embeddings | Content and degradation control | Open loop | Natural images |
| AutoDIR | P2/B | ECCV 2024 | BIQA degradation identification or text | Structure-corrected latent diffusion | Iterative BIQA routing | Natural images |
| OneRestore | P2 | ECCV 2024 | Scene and degradation description | Composite-degradation restorer | Open loop | Natural images |
| Clarity ChatGPT | P3 | Preprint 2023 | ChatGPT and CLIP degradation detection | Classical and deep-learning tool set | Iterative user feedback | Natural images |
| RestoreAgent | P3 | NeurIPS 2024 | MLLM degradation report | Scored deep-learning API registry | History-based replanning and rollback | Natural images |
| JarvisIR | P3 | CVPR 2025 | Driving VLM diagnosis | Weather-operator pipeline | IQA reward and perception evaluation | Autonomous driving |
| 4KAgent | P3 | NeurIPS 2025 | VLM and IQA perception | Quality-driven mixture of experts | Recursive execution and reflection | Super-resolution |
| RAR | P2/B | CVPR 2026 | Learned latent assessor | End-to-end latent restoration | Restore-assess-repeat | Natural images |
| AgentMRI | P3 | JIIM 2026 | Medical VLM classification | Three CycleGAN correction paths | Consensus gate and stop decision | Medical MRI |
| EpiAgent | P3 | CVPR 2026 | Observe-conceive loop | Inscription-restoration tools | Execute-reevaluate refinement | Cultural heritage |
| SIMBA | P3 | Preprint 2026 | Natural-language scientific description | JSON tool-call sequences | Execution verification | Microscopy |
| FAPE-IR | P3 | CVPR 2026 | Frequency-aware planner | High- and low-frequency LoRA experts | Planner-conditioned execution | Natural images |
| Restore-R1 | P1/B | CVPR Findings 2026 | Frozen visual encoder | RL-learned tool selector | DeQA-Score increment | Natural images |
| AgenticIR | P4 | ICLR 2025 | Multimodal diagnosis | Specialised tool registry | Depth-first rollback and experience | Natural images |
| SEAR | P4 | Preprint 2026 | Episodic fingerprint | Intuitive executor and deliberate planner | P-MCTS with episodic memory | Natural images |
| Causal-AgentIR | P4 | Preprint 2026 | Quality, degradation, and history | Causal memory graph | Persistent graph updating | Natural images |
| MAIR | P5 | IJCV 2026 | Scheduler | Seven specialist agents | Sequential scheduling and candidate comparison | Natural images |
| Hybrid Agents | P5 | CVPR 2026 | Fast, Slow, and Feedback agents | Request-dependent restoration | Feedback-based selection | Natural images |
| MAPGR | P5 | npj Heritage Science 2026 | Visual reasoning, prompt, and execution roles | Residual diffusion | Evidence propagation and abstention | Cultural heritage |

## Prompt-conditioned systems

| Work | Venue / year | Conditioning signal | Restoration interface | Runtime loop |
|---|---|---|---|---|
| AirNet | CVPR 2022 | Contrastive degradation representation | Unified restoration network | Open |
| PromptIR | NeurIPS 2023 | Learned degradation prompts | Prompt-modulated Transformer | Open |
| InstructIR | ECCV 2024 | Natural-language instruction | Instruction-conditioned network | Open |
| DA-CLIP | ICLR 2024 | Degradation-aware CLIP representation | Conditioned restoration network | Open |
| MPerceiver | CVPR 2024 | Multimodal prompt perception | Multi-task restoration network | Model-internal |
| AutoDIR | ECCV 2024 | BIQA-inferred degradation or user text | Structure-corrected latent diffusion | Iterative BIQA routing |
| OneRestore | ECCV 2024 | Scene and degradation representation | Composite-degradation restorer | Open |
| LDR | CVPR 2024 | Vision-language degradation description | Sparse MoE restoration network | Model-internal |
| SPIRE | ECCV 2024 | Content and restoration-strength text prompts | Controlled generative restorer | Open |
| UniRes | ICCV 2025 | Complex-degradation formulation | Specialists combined during diffusion sampling | Model-internal |
| SUPIR | CVPR 2024 | Semantic and perceptual condition | Generative restoration model | Open |
| DreamClear | NeurIPS 2024 | Real-world degradation and semantic condition | Generative restoration model | Open |

## General restoration and editing controllers

| Work and status | Controller | Execution | Feedback |
|---|---|---|---|
| RestoreAgent, NeurIPS 2024 | MLLM degradation and model planner | Ordered specialist-model calls | Source-defined sequence score and execution history |
| 4KAgent, NeurIPS 2025 | VLM-IQA perception agent | Quality-driven mixture of experts | Recursive execution-reflection |
| Q-Agent, preprint 2025 | Quality-driven chain-of-thought agent | Specialist restoration algorithms | Objective IQA-guided greedy decisions |
| OPERA, preprint 2026 | RL-optimised planner | Jointly trained restoration tools | Final restoration quality |
| DiTTo, preprint 2026 | Order-aware agent | Simulator-supported specialist tools | Degradation identification and action ordering |
| Restore-R1, CVPR Findings 2026 | Lightweight visual actor-critic policy | Specialised restoration functions | Per-step DeQA-Score improvement |
| PhotoAgent, ICML 2026 oral | Tree-search aesthetic planner | Multi-step editing actions | Learned aesthetic reward and visual feedback |
| PhotoArtAgent, preprint 2025 | Language-model artist agents | Retouching parameters | Iterative reflection |
| RetouchIQ, CVPR 2026 | RL-trained MLLM agent | Lightroom controls | Generalist retouching reward |
| FAPE-IR, CVPR 2026 | Frozen MLLM planner | LoRA-MoE diffusion executor | Restoration objective across seven tasks |
| RAR, CVPR 2026 boundary case | Learned latent controller | End-to-end latent iterations | Learned assessment without an external MLLM tool loop |

## Application-specific controllers

| Work and status | Controller | Execution | Feedback |
|---|---|---|---|
| JarvisIR, CVPR 2025 | Driving-oriented MLLM controller | Restoration modules before perception | Downstream perception utility |
| AgentMRI, JIIM 2026 | Medical VLM agent | Three CycleGAN correction paths | Consensus-based corruption classification |
| EpiAgent, CVPR 2026 | Observe-conceive planner | Inscription-restoration tools | Execute-reevaluate refinement |
| SIMBA, preprint 2026 | Language-to-workflow agent | JSON-schema scientific tools | Input validation and execution response |
| FMIRAgent, Research Square 2025 | Self-explaining MLLM assistant | Microscopy restoration algorithms | User or simulated iterative feedback |
| RIR-Agent, ESWA 2026 | MLLM perception and LLM planner | Remote-sensing toolbox | Adaptation, rollback, or manual feedback |

## Memory and search systems

| Work | Status | Search / control | Memory | Source-reported example |
|---|---|---|---|---|
| AgenticIR | ICLR 2025 | Depth-first rollback and rescheduling | Self-explored referenceable experience | MiO100 Group A: 21.04 dB PSNR and 0.6818 SSIM |
| SEAR | Preprint 2026 | Intuitive executor and deliberate P-MCTS | Episodic state fingerprints | MiO100 Group A: 21.8042 dB PSNR and 0.6961 SSIM; Group B memory ablation: 8.15 versus 16.75 tool calls |
| Causal-AgentIR | Preprint 2026 | Multi-agent causal reasoning | Self-evolving causal memory | All-in-one five-task average: 35.55 dB PSNR |

## Multi-agent systems

| Work | Venue / year | Roles | Coordination | Source-reported example |
|---|---|---|---|---|
| MAIR | IJCV 2026 | Scheduler and seven experts | Sequential scheduling and candidate comparison | 35.42 s, 1.82 invocations, and paired real-world PSNR of 21.67 dB |
| Hybrid Agents | CVPR 2026 | Fast, Slow, and Feedback | Request-dependent fast or slow execution and feedback | Random direct prompts use about 12% of full runtime; 0.08-0.13 s versus 0.75-1.05 s with the fast route disabled |
| MAPGR | npj Heritage Science 2026 | Visual reasoning, prompt, and execution roles | Prompt-guided dual-stream residual diffusion | Evidence propagation with low-confidence abstention |
| CLEAR | Remote Sensing 2026 | Fast and slow processing | Conditional restoration before detection | Overall mAP50 of 86.92%; 11.8 FPS assumes a 5% trigger rate |

## Benchmark datasets

| Dataset | Domain | Degradation types | Primary evaluation focus | Representative AIR works |
|---|---|---|---|---|
| MiO100-derived mixed protocols | Natural images | Composite noise, blur, haze, rain, and JPEG | Multi-degradation tool routing and backtracking | RAR, Restore-R1, AgenticIR, MAIR, Hybrid Agents, Causal-AgentIR |
| DIV2K and high-resolution derivatives | High-resolution natural images | Downscaling, blur, and artefacts | Recursive tile-based super-resolution | RL-Restore, 4KAgent |
| MiO100 | Natural images | Synthetic single or composite degradations | Degradation perception, restoration-order planning, and multi-tool coordination | AgenticIR, MAIR, 4KAgent, Restore-R1, DiTTo |
| CDD-11 | Natural images | Composite low light, haze, rain, and snow | Composite-degradation perception and joint restoration | OneRestore |
| MIT-Adobe FiveK | Aesthetic photography | Exposure, colour, and contrast | Continuous slider tuning and aesthetic preference | Distort-and-Recover |
| Test100, Test1200, Rain100H, Rain100L | Natural rainy scenes | Rain streaks with varying density and patterns | Single-image deraining and robustness | Causal-AgentIR |
| Snow100K, SRRS, CSD | Natural snowy scenes | Snow particles and streaks | Single-image desnowing | PaAgent, InstructIR, Causal-AgentIR |
| RESIDE, SOTS | Indoor and outdoor natural images | Atmospheric haze | Single-image dehazing | PromptIR, Causal-AgentIR |
| GoPro, HIDE, RealBlur | Dynamic and human-centric scenes | Camera, object, and human motion blur | Dynamic-scene and human-aware deblurring | Causal-AgentIR |
| BSD68, Urban100, Kodak24, SIDD | Natural and urban images | Gaussian noise at multiple levels | Denoising across noise levels and structures | PixelRL, PaAgent, PromptIR, InstructIR, Causal-AgentIR |
| LOL | Natural low-light scenes | Low illumination, often with noise | Illumination and detail restoration | Hybrid Agents, Causal-AgentIR |
| fastMRI and related MRI protocols | Medical MRI | Study-specific 4×-6× k-space undersampling and corruption | Sampling optimisation, reconstruction, and correction | DUAL, intelligent-agent planning, KSRO, AgentMRI |
| AAPM Low-Dose CT | Medical CT | Low-photon Poisson noise and streak artefacts | Iterative reconstruction parameter tuning | Shen et al., Patwari et al. |
| nuScenes and HRSC-Robust | Autonomous driving and maritime remote sensing | Fog, rain, snow, low light, and other adverse conditions | Downstream driving and ship-detection performance | JarvisIR, CLEAR |

## Representative quantitative results

| Work | Dataset / setting | Primary metric | Result |
|---|---|---|---|
| RL-Restore | DIV2K, mild unseen degradation | PSNR / SSIM | 28.04 dB / 0.6498 |
| RL-Restore | DIV2K, moderate degradation | PSNR / SSIM | 26.45 dB / 0.5587 |
| RL-Restore | DIV2K, severe unseen degradation | PSNR / SSIM | 25.20 dB / 0.4777 |
| PixelRL | BSD68, σ = 15 | PSNR | 31.49 dB |
| PixelRL | BSD68, σ = 25 | PSNR | 28.94 dB |
| PixelRL | BSD68, σ = 50 | PSNR | 25.95 dB |
| Path-Restore | Darmstadt Noise Dataset, Path-Restore-Ext | PSNR / SSIM | 39.72 dB / 0.9591 |
| Path-Restore | SIDD | PSNR / SSIM | 38.21 dB / 0.946 |
| Distort-and-Recover | MIT-Adobe FiveK expert C, RANDOM 250 | Mean L² error / SSIM | 10.99 / 0.905 |
| Distort-and-Recover | MIT-Adobe FiveK expert C, distort-and-recover scheme | Mean L² error / SSIM | 12.15 / 0.910 |
| PaAgent | CSD | PSNR / SSIM | 37.95 dB / 0.98 |
| PaAgent | BSD68, σ = 15 | PSNR / SSIM | 34.39 dB / 0.94 |
| PaAgent | BSD68, σ = 25 | PSNR / SSIM | 29.36 dB / 0.85 |
| PaAgent | BSD68, σ = 50 | PSNR / SSIM | 27.03 dB / 0.79 |
| AirNet | Five-condition average: BSD68 σ = 15, 25, 50; SOTS; Rain100L | PSNR / SSIM | 31.20 dB / 0.910 |
| PromptIR | Five-condition average: BSD68 σ = 15, 25, 50; SOTS; Rain100L | PSNR / SSIM | 32.06 dB / 0.913 |
| InstructIR | BSD68, Rain100L, SOTS, GoPro, LOL | PSNR / SSIM | 29.55 dB / 0.907 |
| OneRestore | CDD-11 | PSNR / SSIM | 28.72 dB / 0.8821 |
| RAR | MiO100, two degradations, eight combinations | PSNR / SSIM / LPIPS | 20.46 dB / 0.7144 / 0.1299 |
| RAR | MiO100, two degradations, four combinations | PSNR / SSIM / LPIPS | 21.04 dB / 0.7326 / 0.1269 |
| RAR | MiO100, three degradations, four combinations | PSNR / SSIM / LPIPS | 19.33 dB / 0.6579 / 0.1489 |
| Restore-R1 | Setting I, five two-degradation combinations | PSNR / SSIM / LPIPS; MANIQA / CLIP-IQA / MUSIQ / DeQA | 19.513 dB / 0.647 / 0.365; 0.349 / 0.525 / 63.003 / 3.657 |
| Restore-R1 | Setting II, three two-degradation combinations | PSNR / SSIM / LPIPS; MANIQA / CLIP-IQA / MUSIQ / DeQA | 17.958 dB / 0.636 / 0.385; 0.343 / 0.530 / 63.344 / 3.599 |
| Restore-R1 | Setting III, four three-degradation combinations | PSNR / SSIM / LPIPS; MANIQA / CLIP-IQA / MUSIQ / DeQA | 17.650 dB / 0.563 / 0.475; 0.295 / 0.473 / 57.756 / 3.247 |
| Restore-R1 | Setting IV, three combinations of four or five degradations | PSNR / SSIM / LPIPS; MANIQA / CLIP-IQA / MUSIQ / DeQA | 16.180 dB / 0.473 / 0.564; 0.233 / 0.389 / 49.810 / 2.864 |
| AgenticIR | MiO100, two degradations, eight combinations | PSNR / SSIM / LPIPS | 21.04 dB / 0.6818 / 0.3148 |
| AgenticIR | MiO100, two degradations, four combinations | PSNR / SSIM / LPIPS | 20.55 dB / 0.7009 / 0.3072 |
| AgenticIR | MiO100, three degradations, four combinations | PSNR / SSIM / LPIPS | 18.82 dB / 0.5474 / 0.4493 |
| MAIR | MiO100, two degradations, eight combinations | PSNR / SSIM / LPIPS | 21.02 dB / 0.6715 / 0.2963 |
| MAIR | MiO100, two degradations, four combinations | PSNR / SSIM / LPIPS | 20.92 dB / 0.7004 / 0.2788 |
| MAIR | MiO100, three degradations, four combinations | PSNR / SSIM / LPIPS | 19.42 dB / 0.5544 / 0.4142 |
| Hybrid Agents | DF2K, Gaussian noise, fast route enabled versus disabled | PSNR / SSIM | 30.25 / 0.867 versus 30.63 / 0.874 |
| Hybrid Agents | Rain100H, fast route enabled versus disabled | PSNR / SSIM | 30.04 / 0.893 versus 30.03 / 0.893 |
| Hybrid Agents | RESIDE-6K, fast route enabled versus disabled | PSNR / SSIM | 29.92 / 0.960 versus 29.92 / 0.960 |
| Hybrid Agents | LOL, fast route enabled versus disabled | PSNR / SSIM | 22.60 / 0.825 versus 22.61 / 0.828 |
| Causal-AgentIR | Five-task average: Test100, Snow100K, SOTS-Indoor, GoPro, CBSD68 | PSNR / SSIM | 35.55 dB / 0.964 |

## Evaluation and reproducibility

### Minimum metric families

| Dimension | Examples | Required context |
|---|---|---|
| Fidelity | PSNR, SSIM | Dataset, split, degradation, reference availability |
| Perception | LPIPS, DISTS, no-reference IQA | Metric direction, implementation, aggregation |
| Utility | mAP, mIoU, OCR or scientific error | Downstream model and degraded-input baseline |
| Execution | Calls, steps, retries, failures | Tool registry, stopping rule, budget |
| Efficiency | Latency, VRAM, tokens, cost | Hardware, model or API version, concurrency |
| Safety | Worsening rate, hallucination, provenance | Failure definition and audit trail |

### Protocol information required for reproducible agent evaluation

| Component | What to disclose | Why it matters | Typical failure |
|---|---|---|---|
| Input generation | Source images, degradation order and severity, random seed | Determines difficulty and ordering ambiguity | Different mixtures reported under the same benchmark name |
| Controller | Model and version, prompt, decoding, memory initialisation | Changes diagnosis and planning behaviour | Silent model or API updates |
| Tools | Exact checkpoints, parameters, permitted order | Defines the executable action space | Comparing systems with unequal tool strength |
| Feedback | Metric implementation, reference access, stopping rule | Determines retry and termination | Test-time access to unavailable ground truth |
| Budget | Calls, tokens, time, hardware, parallelism | Required for efficiency claims | Reporting tool time while omitting controller time |
| Statistics | Repetitions, variance, confidence intervals, failure cases | Agent decisions can be stochastic | Single-run point estimates |
