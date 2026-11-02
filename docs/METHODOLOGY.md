# Methodology and data dictionary

This is a narrative synthesis. The original set has 49 studies and an 89-entry supporting library. Three revision additions yield 52 studies: 48 controller/adjacent-comparator records, two contextual extensions and two evaluation resources, with a 92-entry library. AIR50–AIR52 are STAR-RL, TIR-Agent and EvoIR-Agent. Primary method sections were checked to examine hierarchical coordination, RL-trained language-model control and reusable experience, respectively; they were not selected by a performance threshold. This is a purposive addition, not the complete eligible yield of the supplementary search. These numbers are corpus accounting, not observed search/screening yields.

## Inclusion roles

- `controller`: an identifiable runtime action interface is described. The feedback criterion must still be checked per deployed configuration.
- `adjacent`: a conditioning or internally iterative comparator retained to examine the control boundary; not automatically AIR.
- `extension`: a contextual medical or research-workflow study; not counted as direct evidence for a universal runtime controller.
- `evaluation`: an evaluation suite rather than a restoration controller.

## Files

`included_studies.csv`: `study_id` is stable within this snapshot; `key` is the source-library citation key; `title`, `year`, `doi`, `url`, `eprint`, `journal`, `booktitle` and `source_url` identify the cited record. `labels` allows overlapping descriptors. `role` records the inclusion purpose. `coding_basis` states provenance; it is not a replication claim.

`reference_library.csv`: contains the preserved 89 entries plus three revision additions and its technical/background role. It is not a search-results export.

`applied_audit.csv`: `control_evidence`, `output_or_utility`, `process_evidence`, `unresolved_comparison_fields` and `source_locator` apply reporting questions to 11 representative systems. The fields contain source-linked descriptions rather than a summed quality score. Not established means insufficient evidence for this audit, not proof of absence.

`protocol_audit.csv`: `setting` identifies the source-specific protocol; `comparison_status` distinguishes within-source comparisons from conditional or incompatible cross-paper contrasts; `sample_unit` and `uncertainty` record extraction limits; `interpretation` constrains reuse. Repeated corrupted instances of one base image and repeated controller seeds are different units.

## Reproducibility limits

Historical per-database yields, duplicate removal and staged exclusions are unavailable. Do not draw an 89-to-49 screening flow. The separately dated revision search has a bounded, single AI-assisted method-verification ledger (see SEARCH_PROVENANCE.md); it is not exhaustive inclusion or recovered historical screening. Full-text source checks, test configuration matching and final author verification remain necessary before strong cross-system claims.

P1/P3 concern the selector, P4 reusable state and P5 coordination. P2 is adjacent conditioning. These are overlapping descriptive axes, not an exhaustive or validated ontology. The word causal in a system title does not by itself establish identified causal effects.

## Verified planning boundaries

OPERA (arXiv:2605.22104v1, Section 4.1) generates a complete plan in one forward pass. It is an adjacent single-shot P3 planning comparator. JarvisIR (arXiv:2504.04158v1, Section 3) uses human-feedback training alignment and reports downstream utility; these are not evidence that intermediate outputs alter deployed restoration decisions. It is retained as a P3 feedback boundary. Mechanism labels alone never establish AIR eligibility.
