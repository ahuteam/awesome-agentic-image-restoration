# Agentic Image Restoration: A Narrative Review

Companion resource for **Agentic image restoration links closed-loop controllers with protocol-aware evaluation: A Narrative Review**.

This repository organises restoration literature by runtime control, feedback, memory and coordination. It supplies a source-linked corpus and protocol audit, not a restoration implementation or a cross-paper performance leaderboard. The paper is under revision; no acceptance or publication DOI is claimed.

## Start here

| Resource | Purpose |
|---|---|
| [Study inventory](data/included_studies.csv) | 49 unique technical records, citation keys, titles, sources, roles and overlapping descriptors |
| [Reference library](data/reference_library.csv) | 89 source-library entries; technical records separated from background/context |
| [Applied audit](data/applied_audit.csv) | 11 representative systems: control evidence, output/process evidence and unresolved comparison fields |
| [Protocol audit](data/protocol_audit.csv) | Interpretation and missingness for source-defined quantitative blocks |
| [Evidence tables](EVIDENCE_TABLES.md) | Detailed historical, source-linked tables, read with the current coding rules |
| [Paper catalogue](docs/PAPER_CATALOGUE.md) | Existing paper/code/project links and figure resources |
| [Method and data dictionary](docs/METHODOLOGY.md) | Scope, evidence roles, coding and limitations |
| [Contributing](CONTRIBUTING.md) | How to propose a paper, correction or reproducibility update |

## What counts as agentic control?

For this review, feedback-contingent runtime control means that an updated observation or evaluation can change a subsequent restoration action, parameter, sequence or stopping decision. A prompt, a training reward, or a fixed iterative schedule alone does not establish this property. This is an operational coding rule, not a universal definition of agency.

| Descriptor | What it records | Important boundary |
|---|---|---|
| P1 | Reinforcement-learning action selector | Training rewards are distinct from feedback available at deployment |
| P2 | Adjacent prompt/conditioned comparator | Conditioning alone is not coded as feedback-driven AIR |
| P3 | Language/vision-language tool-action selector | Explicit reasoning text alone does not verify effective control |
| P4 | Reusable experience across inputs | Episode-local history or a temporary search tree is not automatically persistent memory |
| P5 | Distributed control among coordinating roles | May overlap with P3 and P4; role count does not prove better performance |

Labels overlap. Causal-AgentIR is a language-model tool controller with reusable graph memory and coordinating roles; its inventory labels are P3+P4+P5. AgenticIR and SEAR are recorded with P3+P4. Every study retains one ID even when it receives several descriptors. The inventory also separates adjacent comparators, contextual extensions and evaluation suites.

## How to interpret the numbers

- Compare a baseline and an ablation within the same source only after checking inputs, executor checkpoints, assessors and budgets.
- The same benchmark name does not establish identical degradation generation, crop/colour conventions, model tools or metric implementation.
- Keep single-task scores, macro-averages across tasks, and mixed-degradation group averages separate.
- Tool-call count, controller-inference time and complete pipeline time measure different costs.
- Missing sample units or uncertainty prevent statistical-superiority claims; missing audit evidence does not prove an absent capability.

Two worked examples in the revision illustrate these limits: Hybrid Agents trades task-specific fidelity for faster agent inference in a fast-route ablation, whereas SEAR reports fewer calls with memory under its own Group B protocol. Neither comparison establishes a universal winner.

## Scope and provenance

The original narrative covers literature dated 1 January 2018–9 August 2026. The 89 and 49 counts describe retained source material, not database hits or an exhaustive screening flow. Historical full-domain screening denominators are not recovered. A medical-subdomain ledger cannot substitute for them. Separately dated searches and their raw responses are retained in the revision workspace; they are not represented as a completed new screening exercise.

The 11-system audit is purposive and documentary, not a full 49-study quality assessment, an independent benchmark rerun or a validated risk-of-bias score. Primary-paper claims remain attributed to their original authors. Preprint status and the cited source version should be checked before reuse.

## Validate the data

Only Python's standard library is required:

```bash
python3 scripts/validate_evidence.py
```

The check verifies unique study IDs/citation keys, 49/89 corpus accounting, source identifiers, permitted evidence roles and that audit references resolve to known studies. It does not validate every scientific claim or external website. CI runs the same check for proposed changes.

## Citation and reuse

Use [CITATION.cff](CITATION.cff) for the resource title and contributors. Cite primary papers for their methods and results. No code-archive DOI is assigned in this repository; a GitHub URL is not a substitute for a DOI deposit required by a journal. Third-party papers, code and images remain subject to their own licences; this repository does not relicense them.
