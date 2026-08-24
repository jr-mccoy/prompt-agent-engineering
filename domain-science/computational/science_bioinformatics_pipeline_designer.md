---
title: "Bioinformatics Pipeline Designer"
category: science/computational
description: "Designs a reproducible bioinformatics pipeline as a staged DAG with per-stage QC gates, version-pinned containerized tools, captured parameters, a small test dataset with a CI smoke test, and a deposit/reproducibility plan."
techniques:
  - ST-01
  - ST-03
  - RT-01
  - QA-01
  - CM-02
  - DS-02
difficulty: advanced
tags:
  - bioinformatics
  - reproducibility
  - workflow-design
  - containerization
  - version-pinning
  - qc-gates
  - provenance
  - fair
updated: "2026-06-26"
related_prompts:
  - domain-science/computational/science_genomics_qc_protocol.md
  - domain-science/computational/science_open_source_research_software_repo_layout.md
  - domain-science/methods-foundations/science_reproducibility_self_audit.md
  - domain-science/disciplines/biology/bio_genomics_study_design.md
---

# Bioinformatics Pipeline Designer

**Objective:** Produce a reproducible, auditable bioinformatics pipeline specification: a staged directed-acyclic-graph (DAG) of processing steps, each with a fail-fast QC gate, a version-pinned and containerized tool, captured parameters, defined inputs/outputs, plus a small test dataset, a CI smoke test, and a deposit/reproducibility plan. The artifact satisfies FAIR principles, The Turing Way reproducibility guidance, and prevailing workflow-manager conventions (nf-core / Nextflow / Snakemake / WDL / CWL).

**When to use:** At the design or refactor stage of a computational analysis, before any production run — when you are turning an ad-hoc set of scripts into a portable, re-runnable, provenance-tracked pipeline. For generic CI/testing/architecture-quality review (independent of scientific correctness) route to `domain-software-engineering/`; for repository scaffolding use `domain-science/computational/science_open_source_research_software_repo_layout.md`.

**Required inputs:**
- **Discipline.** Subfield (e.g., DNA-seq, RNA-seq, metagenomics, ATAC-seq).
- **Study type.** Observational / experimental / computational-reanalysis / method-development.
- **Scientific goal and primary output.** The terminal artifact (e.g., variant calls, count matrix, assembled genome).
- **Input data type and scale.** Format(s), approximate sample count, per-sample size, reference/annotation if any.
- **Compute target.** Local workstation / HPC scheduler / cloud — and any data-access restriction (open vs controlled/PHI).

**Optional inputs:**
- Preferred workflow manager or container runtime, if mandated.
- Existing scripts or tool list to wrap.
- Reference build / annotation versions ([user-supplied]).
- Project QC thresholds or a community standard to inherit them from.

**Constraints — Must:**
- Represent the pipeline as an explicit DAG: every stage declares inputs, tool, parameters, outputs, and a QC gate with a defined pass/fail condition (fail-fast).
- Pin an exact version for every tool and dependency, and specify a container (Docker / Singularity / Apptainer) or a locked environment (conda-lock) per stage.
- Capture all parameters and config in version-controlled files, never hard-coded inline.
- Define a small synthetic or subsampled test dataset and a CI smoke test that runs the full DAG end-to-end.
- Emit provenance/logging per stage (tool version, parameters, input checksums, timestamps).
- Default to an Open Science branch: containerized + version-pinned, code in a VCS with a release tag and an archive (e.g., software-heritage / Zenodo DOI), outputs deposited to a public accession. Name controlled/PHI data as the explicit non-default exception with its handling.
- State reporting-standard alignment explicitly (FAIR; The Turing Way; workflow-manager convention).

**Constraints — Must Not:**
- Do not invent citations, DOIs, dataset accessions, tool version numbers, or numeric QC thresholds. If needed and not supplied, mark `[user-supplied]` and ask.
- Do not place a tool in the DAG without a QC gate or a stated, justified reason it has none.
- Do not use `latest` tags, unpinned dependencies, or non-reproducible installs.
- Do not describe any drafted output as "novel", "groundbreaking", "first-ever", or "gold standard".
- Do not silently couple scientific QC with generic code-quality review — flag the latter as out of scope (route to `domain-software-engineering/`).

**Instructions:**

1. **Restate goal and terminal artifact.** Confirm discipline, study type, primary output, input data type/scale, and compute target. Flag any missing required input before designing.
2. **Decompose into stages.** List the minimal stages from raw input to terminal artifact; order them and express dependencies as a DAG. Mark fan-out (per-sample) vs fan-in (cohort merge) points.
3. **Assign tool + pinned version + container per stage.** For each stage name the tool, its exact pinned version (`[user-supplied]` if unknown), and the container/lock mechanism. Note where a community workflow (e.g., an nf-core module) already encapsulates the stage.
4. **Define the QC gate per stage.** For each stage specify the gate metric, its pass condition (threshold `[user-supplied]` or cited standard — never invented), and the fail-fast behavior. Distinguish hard-stop gates from inspect-then-decide gates.
5. **Capture parameters and config.** Specify which parameters are exposed in config, their defaults, and how they are recorded for provenance. Separate environment config from scientific parameters.
6. **Specify the test dataset and CI smoke test.** Define a small synthetic/subsampled dataset that exercises every stage and the expected smoke-test assertions (runs to completion, gate logic fires, output schema matches).
7. **Specify provenance and logging.** State what each stage records (versions, params, input checksums, runtime, exit status) and where logs/reports aggregate.
8. **Address scalability and the compute target.** Note per-stage resource hints and how the same DAG runs locally vs HPC vs cloud without code change (manager profiles / executors).
9. **Specify the deposit/reproducibility plan.** Open Science default (public accession + VCS release tag + archive DOI + container digest) or the named controlled-access exception. Run the self-check (QA-01) against the verification checklist before delivering.

**Output format (locked):**

```
## Pipeline Overview
[goal, terminal artifact, compute target, open/controlled data branch]

## Stage DAG
[stage list + dependency edges; fan-out / fan-in points]

## Stage Table
| Stage | Input | Tool | Pinned version | Container/lock | Key parameters | QC gate (metric → pass condition → fail action) | Output |
|---|---|---|---|---|---|---|---|

## Parameters & Config Capture
[exposed parameters, defaults, provenance recording]

## Test Dataset & CI Smoke Test
[dataset description; smoke-test assertions]

## Provenance & Logging
[per-stage records; aggregation/report]

## Scalability Plan
[local vs HPC vs cloud; resource hints]

## Deposit & Reproducibility Plan
[Open Science default OR controlled-access exception; accession/DOI/tag/digest targets, marked [user-supplied] where unknown]

## Open Questions / [user-supplied] Items
[missing thresholds, versions, accessions to resolve]
```

**Reporting-standard alignment:** FAIR principles; The Turing Way (reproducible research); workflow-manager conventions (nf-core / Nextflow / Snakemake / WDL / CWL); provenance capture consistent with GA4GH-style portability expectations.

**Verification checklist (before delivering):**
- [ ] Discipline and study type captured as the first inputs.
- [ ] Every stage in the DAG has a tool, a pinned version (or `[user-supplied]`), and a container/lock.
- [ ] Every stage has a QC gate with an explicit pass condition and fail-fast behavior (or a stated justified exception).
- [ ] No invented thresholds, versions, accessions, or DOIs — placeholders marked `[user-supplied]`.
- [ ] Parameters/config are version-controlled, not inline.
- [ ] A small test dataset and a CI smoke test covering the full DAG are specified.
- [ ] Provenance/logging contents and aggregation are defined.
- [ ] Open Science deposit default present; controlled-access exception named if applicable.
- [ ] No banned promotional language in drafted text; generic code-quality review flagged out of scope.

**False-positive matrix:**

| Risk | What "looks right but isn't" | Guardrail |
|---|---|---|
| Pinning theater | Versions written but tools installed unpinned at runtime | Require container digest / conda-lock per stage, not just a version string |
| Decorative QC gates | Gates listed but never enforced (warn-only) | Each gate states fail-fast behavior; smoke test asserts the gate fires |
| Invented thresholds | Plausible numeric cutoffs presented as standards | All thresholds `[user-supplied]` or cited to a named standard, never asserted |
| Reproducible-in-name-only | Code "in VCS" but no tagged release or archived artifact | Deposit plan requires release tag + archive DOI + container digest |
| Scope creep into SWE | Pipeline doc drifts into generic CI/lint/architecture review | Flag generic code quality as `domain-software-engineering/` scope |
