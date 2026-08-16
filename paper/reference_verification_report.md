# Final reference and numerical audit

Audit date: 16 August 2026

## Scope

The final manuscript was checked at four levels.

1. Every active citation key was matched to a BibTeX record.
2. Bibliographic metadata and status were queried against DOI, Crossref, arXiv, publisher, proceedings, or official project records.
3. Chapter 8 numerical examples were compared with the corresponding tables in the supplied primary-paper PDFs.
4. The compiled PDF was checked for undefined citations, broken references, table overflow, and figure clipping.

## Reference-integrity result

- Active bibliography entries: 87
- Active cited keys: 87
- Missing citation keys: 0
- Unused bibliography entries: 0
- Duplicate DOI assignments: 0
- Retained records with a withdrawal or retraction signal: 0
- EvoIR-Agent occurrences in active TeX or BibTeX: 0
- Undefined citations or references in the final LaTeX log: 0

The automated online pass returned 79 direct passes and eight records requiring manual review. These eight flags were caused by access or extraction limitations rather than conflicting bibliographic evidence. The records were adjudicated as follows.

| Record | Automated issue | Manual adjudication |
|---|---|---|
| AAPM Low-Dose CT dataset | DOI landing-page title extraction | DOI and TCIA collection metadata are consistent with the BibTeX record |
| FMIRAgent | Crossref author parser mismatch | DOI title and the primary preprint record match |
| CLIP | Primary URL fetch error | CVPR proceedings record retained |
| SUPIR | Primary URL fetch error | CVPR proceedings record retained |
| DA-CLIP | OpenReview page-title extraction | OpenReview record, title, and authors match |
| RetouchIQ | Primary URL fetch error | CVPR 2026 proceedings record retained |
| C2PA specification | Specification-page title extraction | Official C2PA specification record retained |
| LOL dataset paper | Primary URL fetch error | BMVC paper metadata retained |

Two MRI records were added to support the dataset and protocol discussion. Their DOI metadata passed the final online check.

- Chang et al., *Intelligent Agent Planning for Optimizing Parallel MRI Reconstruction via a Large Language Model*, DOI 10.1109/EMBC53108.2024.10782629.
- Xu and Oksuz, *A Reinforcement Learning Approach for Optimized MRI Sampling with Region-Specific Fidelity*, DOI 10.1016/j.neucom.2025.130116.

EvoIR-Agent was removed from the benchmark taxonomy, quantitative table, references, and repository catalogue. The official arXiv record for 2605.22208 states that the manuscript was temporarily withdrawn for institutional clearance and compliance review.

## Chapter 8 numerical corrections

The following corrections were made without deleting valid comparison rows.

| Work | Final source-checked values or setting clarification |
|---|---|
| RAR | Group A 20.46 / 0.7144 / 0.1299; Group B 21.04 / 0.7326 / 0.1269; Group C 19.33 / 0.6579 / 0.1489 |
| Restore-R1 | Restored all four settings and all seven reported metrics. Setting IV is 16.180 / 0.473 / 0.564 and 0.233 / 0.389 / 49.810 / 2.864 |
| MAIR | Group A 21.02 / 0.6715 / 0.2963; Group B 20.92 / 0.7004 / 0.2788; Group C 19.42 / 0.5544 / 0.4142 |
| Hybrid Agents | Values now show fast route enabled versus disabled, rather than presenting the disabled condition without its setting label |
| Causal-AgentIR | 35.55 dB / 0.964 is labelled as the five-task average over Test100, Snow100K, SOTS-Indoor, GoPro, and CBSD68 |
| Path-Restore | The DND result 39.72 dB / 0.9591 is labelled Path-Restore-Ext |
| AirNet and PromptIR | Results are labelled as the five-condition average including three BSD68 noise levels, SOTS, and Rain100L |

The RL-Restore, PixelRL, Distort-and-Recover, PaAgent, InstructIR, OneRestore, and AgenticIR rows were retained after confirmation against their source tables.

## Layout and figure result

The two content-heavy Chapter 8 long tables use landscape pages and fixed-width ragged columns. All cells remain inside the table boundary in the final PDF. The three supplied PDF figures are included without `trim` or `clip`; their complete source canvases and all diagram nodes are visible in the compiled pages.
