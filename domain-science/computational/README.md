# `domain-science/computational/`

The computational / dry-lab layer for the working scientist: reproducible pipelines, per-stage QC, the omics analysis plans, simulation verification & validation, data management and metadata, and the ML-for-science validity audits. Composes on top of [`../methods-foundations/`](../methods-foundations/) and [`../statistics/`](../statistics/), and supports the discipline modules in [`../disciplines/`](../disciplines/).

**Domain boundary:** this is *computational-research craft* — scientific correctness, reproducibility, and the validity of claims drawn from computation. Generic software engineering (CI/testing/architecture review as engineering) lives in [`../../domain-software-engineering/`](../../domain-software-engineering/); [`science_open_source_research_software_repo_layout.md`](science_open_source_research_software_repo_layout.md) is the explicit bridge between the two.

## Map (Phase 2C — 14 prompts)

### Pipelines & omics analysis

| File | Coverage |
|---|---|
| [`science_bioinformatics_pipeline_designer.md`](science_bioinformatics_pipeline_designer.md) | Pipeline DAG with fail-fast QC gates, version pinning, containerization, test data + CI smoke test |
| [`science_genomics_qc_protocol.md`](science_genomics_qc_protocol.md) | Per-stage QC (read / alignment / variant / sample) with metric → threshold → action → remediation |
| [`science_single_cell_analysis_plan.md`](science_single_cell_analysis_plan.md) | scRNA-seq: doublet/ambient, MAD-based cell QC, integration, clustering (flagged as a researcher DF), annotation, pseudobulk DE |
| [`science_proteomics_analysis_plan.md`](science_proteomics_analysis_plan.md) | DDA/DIA, target-decoy FDR at the right level, protein inference, MNAR missingness, PTM localization, PRIDE deposit |

### Simulation & numerics

| File | Coverage |
|---|---|
| [`science_simulation_validation_protocol.md`](science_simulation_validation_protocol.md) | V&V hierarchy (code vs solution verification vs validation), calibration≠validation, UQ + sensitivity (ASME V&V / AIAA) |
| [`science_numerical_convergence_audit.md`](science_numerical_convergence_audit.md) | ≥3-level refinement study, observed order, Richardson extrapolation + Grid Convergence Index, asymptotic-range check |

### Reproducibility & research software

| File | Coverage |
|---|---|
| [`science_computational_reproducibility_environment.md`](science_computational_reproducibility_environment.md) | Lockfile + container + seeds + data checksums + one-command reproduce + CI that rebuilds and reproduces a figure (FAIR4RS) |
| [`science_open_source_research_software_repo_layout.md`](science_open_source_research_software_repo_layout.md) | rOpenSci/FAIR4RS repo skeleton, CITATION.cff, semantic-version release + Zenodo DOI, JOSS-readiness — **bridge to domain-software-engineering** |

### Data management & metadata

| File | Coverage |
|---|---|
| [`science_data_management_plan_drafter.md`](science_data_management_plan_drafter.md) | Funder-aware DMP (NIH/NSF/Wellcome/ERC structure), storage/sharing/preservation, access tiers, maDMP |
| [`science_data_dictionary_designer.md`](science_data_dictionary_designer.md) | Variable-level dictionary: units, allowed values, missingness codes, provenance, PII flags (tidy-data) |
| [`science_metadata_schema_builder.md`](science_metadata_schema_builder.md) | Right schema by discipline (MIBBI / ISA / Dublin Core / DataCite / schema.org) + repository crosswalk |
| [`science_synthetic_data_generator_design.md`](science_synthetic_data_generator_design.md) | Surrogate data preserving structure without disclosure risk; privacy-vs-utility + re-identification checks |

### ML for science

| File | Coverage |
|---|---|
| [`science_ml_for_science_validation_audit.md`](science_ml_for_science_validation_audit.md) | Kapoor–Narayanan leakage taxonomy audit → claim-validity verdict (what the model results can and cannot support) |
| [`science_ml_for_science_benchmark_design.md`](science_ml_for_science_benchmark_design.md) | Claim-matched held-out split, fair baselines, calibration, ablations, subgroup error analysis, reproducible eval |

## Floor (per [`../README.md`](../README.md))

Every prompt requires discipline + study type; forbids fabricated citations, dataset accessions, tool version numbers, and numeric QC/convergence thresholds (`[user-supplied]` or cite the standard); locks the output format; names the relevant community standard (FAIR / FAIR4RS, The Turing Way, nf-core, MIAME/MINSEQE/MIAPE, ASME V&V, GCI, rOpenSci, REFORMS, Kapoor–Narayanan); preserves the pre-specified-vs-exploratory distinction (thresholds, clustering, eval protocols locked before the test set / production runs); defaults to the Open Science branch (containerized, pinned, archived, public deposit) with closed/controlled-access data named as the non-default exception; and ends with a verification checklist + false-positive matrix.

See [`../EXPANSION_ROADMAP.md`](../EXPANSION_ROADMAP.md) for the remaining phases and build order.
