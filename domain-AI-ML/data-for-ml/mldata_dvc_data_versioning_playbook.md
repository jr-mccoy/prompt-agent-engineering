---
title: "DVC Data Versioning & Pipeline Playbook"
category: AI-ML/data-for-ml
description: "Stand up DVC for dataset versioning and reproducible ML pipelines — remote storage, tracked data/artifacts, pipeline DAG (dvc.yaml), git-coupled data versions, and train/serve consistency — without inventing version-specific command behavior."
techniques:
  - ST-02
  - CM-02
  - RT-10
  - DS-02
  - QA-01
difficulty: intermediate
tags:
  - dvc
  - data-versioning
  - data-lineage
  - reproducibility
  - mlops
updated: "2026-06-19"
related_prompts:
  - domain-AI-ML/data-for-ml/mldata_data_versioning_lineage.md
  - domain-AI-ML/mlops-infrastructure/mlops_reproducibility_audit.md
  - domain-AI-ML/data-for-ml/mldata_data_leakage_detector.md
---

# DVC Data Versioning & Pipeline Playbook

**Objective:** Turn "our datasets aren't versioned" into a concrete DVC setup — remote storage configuration, tracked datasets/artifacts, a reproducible pipeline DAG (`dvc.yaml` stages), and git-coupled data versions — so any experiment can be tied to the exact data that produced it and re-run deterministically.

**When to Use:**
- You have chosen DVC (git-based data versioning) and need an opinionated setup walkthrough.
- Datasets and model artifacts are too large for git but must be versioned alongside code.
- You need reproducible data → features → train pipelines whose outputs are cache-aware and re-runnable.

**When NOT to Use:**
- You have not decided *whether* DVC fits vs. alternatives — start with `mldata_data_versioning_lineage.md`.
- You need a full reproducibility audit across the stack — use `mlops_reproducibility_audit.md`.
- Your concern is leakage in the splits/features themselves — use `mldata_data_leakage_detector.md`.

## Inputs / Context

Provide what you can:
- **DVC version** and remote backend (S3, GCS, Azure, SSH, local) with access method.
- **Repository layout** — monorepo vs. data-only repo; where data, code, and pipelines live.
- **Dataset sizes & change frequency** — drives caching and remote strategy.
- **Pipeline stages** — the data → features → train → evaluate steps you want reproducible.
- **Team workflow** — how data is shared, and whether CI runs pipelines.

## Constraints

**Must:**
- Ask for the DVC version and remote backend before giving commands; flag version-sensitive behavior.
- Couple every data version to a git commit so code + data versions move together.
- Make the pipeline DAG declarative (`dvc.yaml`) with explicit deps/outs so stages re-run only when inputs change.

**Must Not:**
- Invent DVC command flags, config keys, or remote-setup syntax — mark "verify against your DVC version's docs."
- Recommend committing large data blobs into git or storing credentials in tracked files.
- Treat `dvc repro` outputs as reproducible if seeds/params/environment are uncaptured.

**Instructions:**

1. **Set up the repo and remote.** Initialize DVC in the git repo, configure the remote backend and credentials (via environment/secret store, not tracked files), and decide the cache strategy (shared cache for teams/CI).

2. **Track datasets and artifacts.** Add raw datasets and large artifacts to DVC tracking so git stores pointers and the remote stores content. Establish a directory convention (raw / interim / processed) and a tag scheme for dataset versions.

3. **Define the pipeline DAG.** Author `dvc.yaml` stages (e.g., ingest → clean → features → split → train → evaluate) with explicit `deps`, `params`, and `outs`. Put tunable values in `params.yaml` so they are tracked and diffable.

4. **Couple data to code versions.** Establish the convention that a git commit + its DVC lock file (`dvc.lock`) together pin the exact data + params + outputs. Tag releases so a model can be traced to a precise data state.

5. **Wire reproducibility hooks.** Capture seeds and environment (lockfile) within the pipeline; ensure `dvc repro` regenerates outputs deterministically. Cross-link `mlops_reproducibility_audit.md`.

6. **Establish the team workflow.** Define push/pull conventions (`dvc push`/`dvc pull` against the remote), how branches handle divergent data, and how CI fetches the right data version for a run.

7. **Guard train/serve and leakage consistency.** Ensure the split and feature stages are pinned and shared so training and downstream consumers use the same data version; cross-link `mldata_data_leakage_detector.md` for split correctness.

8. **Define validation.** Provide a smoke test: clone fresh, `dvc pull` a tagged version, `dvc repro`, and confirm outputs match the recorded `dvc.lock` (reproducible) — then change a param and confirm only affected stages re-run.

**Output Format:**

A markdown setup playbook:
- **Remote & Cache Setup** — backend, credentials method, cache strategy
- **Tracking Conventions** — directory layout, dataset tagging
- **Pipeline DAG** — `dvc.yaml` stages with deps/params/outs (table)
- **Data↔Code Coupling** — how commit + dvc.lock pin a version
- **Reproducibility Hooks** — seeds, environment, params
- **Team Workflow** — push/pull, branches, CI fetch
- **Smoke Test** — fresh clone → pull → repro validation
- **Verify-in-Docs** — version-sensitive commands flagged

## Verification

- [ ] The remote backend and credential handling are specified (no secrets in tracked files).
- [ ] Each data version is coupled to a git commit + `dvc.lock`.
- [ ] The pipeline DAG declares explicit deps/params/outs so stages re-run selectively.
- [ ] Seeds, params, and environment are captured for deterministic `dvc repro`.
- [ ] Train and downstream consumers reference the same pinned data version.
- [ ] DVC commands/flags are flagged "verify against your version," not asserted.

## False-Positive Prevention

❌ **DON'T:**
- Call data "versioned" because files are in a remote, while no git commit pins which version a model used.
- Treat `dvc repro` as reproducible when seeds, params, or environment aren't captured — outputs can still drift.
- Store remote credentials in a tracked config file.
- Quote DVC command flags or `dvc.yaml` schema keys from memory as version-stable.

✅ **DO:**
- Pin every model to a (git commit + dvc.lock) pair so data + code + params are jointly reproducible.
- Capture seeds, params (`params.yaml`), and environment so `dvc repro` is deterministic.
- Inject remote credentials via environment/secret store outside version control.
- Mark version-specific commands and schema as "verify against your DVC version's docs."

## Example Output

```markdown
## DVC Playbook: Tabular Risk Model (S3 remote, monorepo)

### Remote & Cache Setup
- DVC (verify version); remote = s3://acme-ml-dvc; creds via env/secret store.
- Shared cache on CI runners to avoid re-downloads.

### Tracking Conventions
- data/raw, data/interim, data/processed; dataset tags `data-v{N}`.
- Large model artifacts tracked via DVC; pointers in git.

### Pipeline DAG (dvc.yaml)
| Stage | deps | params | outs |
|---|---|---|---|
| clean | data/raw, src/clean.py | clean.* | data/interim |
| features | data/interim, src/feat.py | feat.* | data/processed |
| split | data/processed | split.seed | data/splits |
| train | data/splits, src/train.py | train.* | models/model.pkl |
| evaluate | models/model.pkl, data/splits | — | metrics.json |

### Data↔Code Coupling
git commit + dvc.lock pin exact data + params + outputs. Release tags trace model → data-v{N}.

### Reproducibility Hooks
split.seed + train.seed in params.yaml; environment lockfile; deterministic repro. See mlops_reproducibility_audit.md.

### Team Workflow
dvc push after repro; dvc pull on checkout; CI pulls the tagged version for the run; branches keep their own dvc.lock.

### Smoke Test
Fresh clone → dvc pull data-v8 → dvc repro → outputs match dvc.lock. Change feat.* param → only features/split/train/evaluate re-run.

### Verify-in-Docs
- Remote-add syntax and cache config for your DVC version.
- dvc.yaml stage schema (deps/params/outs) specifics.
```

**Techniques Used:**
- **ST-02 (Structured Sequential Instructions):** remote → tracking → DAG → coupling → reproducibility → workflow → validation.
- **CM-02 (Constraint Specification):** no-fabrication, no-secrets-in-git, and data↔code coupling constraints govern the setup.
- **RT-10 (Troubleshooting / Operational Reasoning):** organized around what actually makes pipelines reproducible and selectively re-runnable.
- **DS-02 (Metric Specification):** the DAG includes an explicit evaluate stage emitting tracked metrics.
- **QA-01 (Self-Verification):** the fresh-clone smoke test validates reproducibility and selective re-runs.

**Related Prompts:**
- `mldata_data_versioning_lineage.md` — choose DVC vs. alternatives and design lineage before this playbook.
- `mlops_reproducibility_audit.md` — full-stack reproducibility checklist the hooks feed into.
- `mldata_data_leakage_detector.md` — verify the split/feature stages don't leak before pinning them.
