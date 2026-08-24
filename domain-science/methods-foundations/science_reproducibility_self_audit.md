---
title: "Reproducibility Self-Audit (FAIR-Aligned)"
category: science/methods-foundations
description: "Scored FAIR-aligned and computational-reproducibility audit of a study's data, code, environment, and documentation, producing a gap-and-fix table before submission or deposit."
techniques:
  - ST-01
  - QA-01
  - DS-02
  - CM-02
  - ST-03
  - RT-01
difficulty: advanced
tags:
  - reproducibility
  - fair-principles
  - data-availability
  - code-availability
  - computational-environment
  - version-control
  - persistent-identifiers
  - open-science
updated: "2026-06-26"
related_prompts:
  - domain-science/methods-foundations/science_experimental_design_advisor.md
  - domain-science/methods-foundations/science_replicability_premortem.md
  - domain-science/methods-foundations/science_methods_section_drafter.md
---

# Reproducibility Self-Audit (FAIR-Aligned)

**Objective:** Audit whether an independent person, given only what you are about to publish, could re-run your exact analytic pipeline on your exact data and obtain your exact result. This prompt scores the study against the FAIR principles (Findable, Accessible, Interoperable, Reusable) and against the requirements of computational reproducibility — data deposit, version-controlled and archived code, captured environment, fixed seeds, and runnable documentation — emitting a gap-and-fix table per item with a FAIR sub-score.

**When to use:** Before submitting a manuscript, posting a preprint, or depositing a dataset/code release. Run it once the analysis is frozen so that the audited artifacts match what will be published.

**Scope note — reproducibility, not replicability.** Following the Turing Way / NASEM (2019) distinction: *reproducibility* = **same data + same code → same result** — that is what this prompt audits. *Replicability* = **new data + same method, independent team → same conclusion** — audited by the sibling prompt `science_replicability_premortem.md`. A study can be fully reproducible (re-runs bit-for-bit) yet fail to replicate (the effect vanishes on fresh data), and vice versa. These are orthogonal; run both.

**Required inputs:**
- **Discipline.** <field> `[user-supplied]`
- **Study type.** <observational / experimental / computational / simulation / mixed; for any data-bearing study> `[user-supplied]`
- **Data sensitivity.** Open / restricted-but-shareable / controlled-access (human-subjects, PII, endangered-species localities, commercial). This selects the default branch (see below). `[user-supplied]`
- **Artifacts that exist today.** Raw data, processed data, analysis code, environment spec, README, data dictionary — which of these are written and where they currently live. `[user-supplied]`

**Optional inputs:**
- Target repository/accession (e.g., generic disciplinary archive) `[user-supplied]`.
- Version-control host and whether a release/tag exists `[user-supplied]`.
- Archival DOI plan (e.g., Zenodo deposit of a tagged release) `[user-supplied]`.
- Licenses chosen for data and for code `[user-supplied]`.
- Compute scale / whether a one-command reproduce is feasible.

**Branch (default = Open Science):**
- **Default — Open Science:** raw + processed data and code are deposited in a public, persistent-identifier-bearing repository under open licenses.
- **Non-default — Controlled-access / proprietary:** when data sensitivity is restricted or controlled, substitute (a) metadata-only deposit with a documented access procedure, (b) synthetic or simulated example data that exercises the pipeline, and (c) a data-availability statement naming the access body. Name this branch explicitly in the output; do not silently downgrade openness.

**Constraints — Must:**
- Score each audit item as **Present / Partial / Absent** with the observed evidence, the gap, and the concrete fix (DS-02, QA-01).
- Compute a FAIR sub-score (count or proportion of FAIR facets satisfied) and a computational-reproducibility sub-score, reported separately.
- Distinguish **pre-specified** analysis scripts from **exploratory/ad-hoc** scripts; both must be archived, but exploratory ones must be labeled so reproducers know which path produced the headline numbers.
- Reference The Turing Way (reproducible-research practice), the FAIR principles, and discipline-appropriate deposit archives **generically** (do not fabricate a specific repository name/URL unless supplied).

**Constraints — Must Not:**
- Do not invent citations, DOIs, dataset names, repository URLs, or instrument/vendor specs. If needed and not supplied, mark `[user-supplied]` and ask.
- Do not score an item Present on a promise — "we will deposit on acceptance" is Partial at best until a persistent identifier exists.
- Do not recommend posting sensitive raw data; route to the controlled-access branch instead.
- Do not use promotional language: ban "novel," "groundbreaking," "first-ever," "gold standard."

**Instructions:**

1. **Inventory artifacts.** List every artifact that exists, where it lives, and whether it carries a persistent identifier. Anything not written yet is Absent.
2. **Findable.** Check that data and code have persistent identifiers (DOI/accession), rich metadata, and are indexed/searchable in a repository — not merely "available on request."
3. **Accessible.** Verify retrievability via a standard protocol, with an explicit access procedure (open download, or documented controlled-access steps), and that metadata persist even if data are restricted.
4. **Interoperable.** Check open/standard file formats, controlled vocabularies/ontologies where applicable, and a data dictionary defining every variable, unit, and code.
5. **Reusable.** Verify clear licenses (separately for data and code), provenance, and documentation sufficient for reuse.
6. **Computational environment & determinism.** Confirm the environment is captured (container image, dependency lockfile, or session/environment info) and that random seeds are fixed wherever stochastic steps exist.
7. **Runnability.** Check for a README with run instructions and, ideally, a one-command reproduce (script/Make target/workflow) that regenerates the reported figures and tables from the deposited inputs.
8. **Code provenance.** Confirm code is in version control with a tagged release, and that the release is archived to a persistent-identifier store (e.g., a Zenodo deposit of the tag) rather than only a moving branch.
9. **Score and prioritize.** Fill the audit table, compute both sub-scores, and rank the gaps as Blocking / Recommended / Optional for the chosen branch.

**Output format (locked):**

```
## Branch & Inputs
- Branch (Open Science / Controlled-access): 
- Discipline / study type / data sensitivity:

## Artifact Inventory
| Artifact | Exists? | Location | Persistent ID? |
|---|---|---|---|

## FAIR + Computational-Reproducibility Audit
| Item | FAIR facet / Repro dimension | Status (Present/Partial/Absent) | Evidence | Gap | Fix | Priority |
|---|---|---|---|---|---|---|
(Items must include, at minimum: raw data deposited; processed data deposited;
data dictionary / codebook; open/standard formats; persistent identifiers;
data license; code in version control; tagged release archived to DOI store;
code license; environment captured (container/lockfile/session-info);
random seeds fixed; README + run instructions; one-command reproduce.)

## Scores
- FAIR sub-score: [satisfied facets / total] — [F _/_  A _/_  I _/_  R _/_]
- Computational-reproducibility sub-score: [satisfied items / total]

## Pre-Specified vs Exploratory Scripts
| Script / pipeline | Produces headline result? | Pre-specified or ad-hoc | Archived? |
|---|---|---|---|

## Prioritized Remediation
- Blocking (before submission/deposit):
- Recommended:
- Optional:

## Data & Code Availability Statement (draft)
[branch-appropriate statement; name access body for controlled-access]
```

**Reporting-standard alignment:** FAIR Principles (Wilkinson et al. 2016, named generically), The Turing Way reproducible-research guidance, TOP Guidelines (data/code transparency tiers), and journal data/code availability statement requirements. For biomedical work, align deposits with the relevant disciplinary archives (named only when `[user-supplied]`). Cross-reference the manuscript's reproducibility statement in `science_methods_section_drafter.md`.

**Verification checklist (before delivering):**
- [ ] Branch (Open Science default vs controlled-access) chosen and stated explicitly.
- [ ] Every audit item scored Present/Partial/Absent with observed evidence, not a promise.
- [ ] Persistent identifiers required for any Present score on Findable/code-archive items.
- [ ] FAIR sub-score and computational-reproducibility sub-score reported separately.
- [ ] Environment capture and fixed seeds explicitly checked for any stochastic step.
- [ ] Data and code licenses audited separately.
- [ ] Pre-specified vs exploratory scripts distinguished and both archived.
- [ ] No fabricated repository names/DOIs/accessions; unknowns marked `[user-supplied]`.

**False-positive matrix:**

| Risk | What "looks right but isn't" | Guardrail |
|---|---|---|
| "Available on request" mistaken for FAIR | Data-availability statement says "from the corresponding author on reasonable request" | Score Findable/Accessible Absent; only a persistent-identifier deposit (or documented controlled-access procedure) counts |
| Runs-on-my-machine | Code "works" but depends on uncaptured local environment | Require container/lockfile/session-info; an un-pinned environment is Partial |
| Moving branch as archive | Linking a Git branch/HEAD instead of a tagged, DOI-archived release | Require a tagged release archived to a persistent-identifier store; branches mutate |
| Reproducibility claimed as replicability | "Fully reproducible" implying the finding is robust to new data | Reaffirm same-data/same-code scope; route new-data robustness to `science_replicability_premortem.md` |
| Stochasticity ignored | Pipeline with randomness scored Present despite no fixed seed | Treat any unseeded stochastic step as Absent on determinism |
| Sensitive data over-shared | Recommending public raw deposit for human-subjects/PII data | Switch to controlled-access branch: metadata + access procedure + synthetic example data |
