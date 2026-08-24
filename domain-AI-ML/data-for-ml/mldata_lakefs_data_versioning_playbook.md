---
title: "lakeFS Data Versioning Playbook"
category: AI-ML/data-for-ml
description: "Stand up lakeFS for git-like versioning over object-storage data lakes — repositories, branches, commits, merges, and CI-style data validation hooks — so ML datasets are reproducible and isolated, without inventing version-specific API behavior."
techniques:
  - ST-02
  - CM-02
  - RT-10
  - DS-02
  - QA-01
difficulty: intermediate
tags:
  - lakefs
  - data-versioning
  - data-lineage
  - reproducibility
  - mlops
updated: "2026-06-19"
related_prompts:
  - domain-AI-ML/data-for-ml/mldata_data_versioning_lineage.md
  - domain-AI-ML/data-for-ml/mldata_dvc_data_versioning_playbook.md
  - domain-AI-ML/mlops-infrastructure/mlops_reproducibility_audit.md
---

# lakeFS Data Versioning Playbook

**Objective:** Turn an object-storage data lake into a version-controlled, reproducible substrate using lakeFS — repositories over your bucket, branches for isolated experimentation, commits as immutable data versions, merges for promotion, and hooks for data validation — so any ML run can pin and reproduce the exact lake state it used.

**When to Use:**
- Your data lives in object storage (S3/GCS/Azure) at a scale where git/DVC file-tracking is impractical, and you want git-like semantics over the lake.
- You need isolated branches for experiments/ETL without copying data, plus atomic promotion via merge.
- You want pre-merge data-quality gates (hooks) before a dataset version becomes "production."

**When NOT to Use:**
- You haven't decided *whether* lakeFS vs. DVC vs. other approaches — start with `mldata_data_versioning_lineage.md`.
- Your datasets are small/file-scale and code-coupled — `mldata_dvc_data_versioning_playbook.md` may fit better.
- You need a full-stack reproducibility audit — use `mlops_reproducibility_audit.md`.

## Inputs / Context

Provide what you can:
- **lakeFS deployment** — self-hosted vs. managed; **lakeFS version**; metadata store backing it.
- **Object store** — S3/GCS/Azure bucket(s) and the storage namespace lakeFS will manage.
- **Access pattern** — engines reading the lake (Spark, query engines, training jobs) and how they address paths.
- **Branching needs** — per-experiment, per-ETL-job, or per-environment branches.
- **Validation needs** — data-quality checks to enforce before merge (schema, row counts, null rates).

## Constraints

**Must:**
- Ask for the lakeFS version and object store before giving setup steps; flag version-sensitive behavior.
- Pin every ML run to a specific lakeFS commit ID (immutable) so the data state is reproducible.
- Define the branch/merge model and what gate (hooks/CI) governs promotion to the main branch.

**Must Not:**
- Invent lakeFS API endpoints, CLI flags, hook config schema, or pricing — mark "verify against current lakeFS docs."
- Treat a branch reference as a reproducible pin (branches move) — only commit IDs are immutable.
- Bypass merge hooks for production data promotion.

**Instructions:**

1. **Provision the repository.** Create a lakeFS repository over the target storage namespace; confirm the metadata store and access credentials (via secret store). State how engines/clients address `lakefs://repo/ref/path`.

2. **Define the branching model.** Establish branch conventions: `main` as the validated production lineage, experiment/ETL branches for isolated work, and (optionally) environment branches. Branching is zero-copy — emphasize that.

3. **Establish commit conventions.** Treat each commit as an immutable data version with metadata (author, message, source job, code SHA). The commit ID is the reproducible pin a model records.

4. **Design the merge/promotion flow.** Define how an experiment/ETL branch is merged into `main` only after validation passes — atomic promotion of a data version, with the commit recorded.

5. **Add data-quality hooks.** Configure pre-merge/pre-commit hooks (schema checks, row-count bounds, null-rate thresholds) so invalid data cannot become a production version. Mark hook schema as verify-in-docs.

6. **Wire reproducibility.** Record the lakeFS commit ID alongside git SHA, seed, and environment for each ML run so the run pins data + code + params. Cross-link `mlops_reproducibility_audit.md`.

7. **Integrate with compute & CI.** Show how training/ETL jobs read from a pinned ref and how CI creates ephemeral branches to test a data change, runs hooks, and merges on success.

8. **Define validation.** Provide a smoke test: branch from main, write data, commit, run hooks, merge; then have a job read the merged commit ID and confirm it reads the exact expected state; confirm an invalid commit is blocked by hooks.

**Output Format:**

A markdown setup playbook:
- **Repository & Access** — namespace, metadata store, addressing scheme
- **Branching Model** — branches and their roles (table)
- **Commit Conventions** — metadata + immutable-pin rule
- **Merge / Promotion Flow** — branch → validate → merge to main
- **Data-Quality Hooks** — checks enforced before merge
- **Reproducibility Wiring** — commit ID + git SHA + seed per run
- **Compute & CI Integration** — pinned reads, ephemeral branches
- **Smoke Test** — branch/commit/hook/merge validation
- **Verify-in-Docs** — version-sensitive items flagged

## Verification

- [ ] ML runs pin a commit ID (immutable), not a branch name.
- [ ] The branch/merge model defines how data reaches `main` and the gate that governs it.
- [ ] Pre-merge data-quality hooks are specified (schema/counts/nulls), not assumed.
- [ ] Each run records lakeFS commit ID + git SHA + seed + environment.
- [ ] Credentials use a secret store; addressing scheme for engines is explicit.
- [ ] lakeFS API/CLI/hook schema is flagged "verify," not asserted.

## False-Positive Prevention

❌ **DON'T:**
- Record a branch name (e.g., `main`) as the data version for a run — branches advance, so the pin is not reproducible.
- Promote data to `main` without running validation hooks, letting bad schema/nulls become "production."
- Quote lakeFS hook YAML keys or API routes from memory as version-stable.
- Assume zero-copy branching means unlimited free storage — committed object versions still accumulate.

✅ **DO:**
- Pin runs to immutable commit IDs and store them with the run's code/seed/environment.
- Gate every merge to `main` on data-quality hooks; block invalid commits.
- Mark all API/CLI/hook-schema specifics as "verify against your lakeFS version."
- Set a retention/garbage-collection policy for old committed object versions.

## Example Output

```markdown
## lakeFS Playbook: Clickstream Feature Lake (S3, self-hosted)

### Repository & Access
- Repo `clickstream` over s3://acme-lake/clickstream; metadata store backed (verify); creds via secret store.
- Engines address lakefs://clickstream/<ref>/path; Spark configured with lakeFS endpoint.

### Branching Model
| Branch | Role |
|---|---|
| main | validated production lineage |
| etl/daily-{date} | isolated daily ingestion |
| exp/{ticket} | experiment data edits |

### Commit Conventions
Each commit: message, author, source_job, code_sha. Commit ID is the reproducible pin.

### Merge / Promotion Flow
etl/daily-* → run hooks → merge into main (atomic). Failed hooks block merge.

### Data-Quality Hooks
Pre-merge: schema matches contract; row count within ±X% of trailing avg; null rate < threshold on key columns. (Verify hook schema.)

### Reproducibility Wiring
Each training run records lakeFS commit ID + git_sha + seed + env lockfile. See mlops_reproducibility_audit.md.

### Compute & CI Integration
Jobs read pinned commit ID; CI branches ephemeral copy, applies change, runs hooks, merges on success, deletes branch.

### Smoke Test
Branch from main → write+commit → hooks pass → merge; job reads merged commit ID → confirms exact state. Inject bad-schema commit → hook blocks merge.

### Verify-in-Docs
- API/CLI syntax, hook config schema for your lakeFS version.
- Garbage-collection / retention configuration.
```

**Techniques Used:**
- **ST-02 (Structured Sequential Instructions):** repository → branching → commits → merge → hooks → reproducibility → validation.
- **CM-02 (Constraint Specification):** no-fabrication, immutable-pin, and hook-gated-merge constraints govern the setup.
- **RT-10 (Troubleshooting / Operational Reasoning):** built around what makes lake state reproducible and safely promotable at scale.
- **DS-02 (Metric Specification):** data-quality hooks are defined as concrete thresholds (counts, null rates, schema).
- **QA-01 (Self-Verification):** the smoke test validates pinning, hook enforcement, and merge end-to-end.

**Related Prompts:**
- `mldata_data_versioning_lineage.md` — choose lakeFS vs. alternatives and design lineage first.
- `mldata_dvc_data_versioning_playbook.md` — the file/code-coupled alternative for smaller, code-tied datasets.
- `mlops_reproducibility_audit.md` — full-stack reproducibility checklist the commit-ID pin feeds into.
