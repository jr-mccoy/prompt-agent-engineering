---
title: "Computational Reproducibility Environment"
category: science/computational
description: "Capture the full computational stack — pinned dependencies, container image, seeds, data versioning, parameterized config, and CI that rebuilds the environment and reproduces a key result — so a study is computationally reproducible by a third party."
techniques:
  - ST-01
  - ST-03
  - RT-01
  - QA-01
  - CM-02
  - DS-02
difficulty: advanced
tags:
  - reproducibility
  - containerization
  - lockfile
  - seed-control
  - data-versioning
  - continuous-integration
  - fair4rs
  - the-turing-way
updated: "2026-06-26"
related_prompts:
  - domain-science/computational/science_open_source_research_software_repo_layout.md
  - domain-science/computational/science_numerical_convergence_audit.md
  - domain-science/methods-foundations/science_reproducibility_self_audit.md
  - domain-science/disciplines/chemistry/chem_computational_chemistry_validation_protocol.md
---

# Computational Reproducibility Environment

**Objective:** Specify the complete environment and automation needed so that a third party (or your future self) can reproduce a computational study's key results from a clean checkout. Capture every layer of the stack — pinned dependencies via a lockfile, a container image, OS/hardware notes, fixed random seeds, versioned and checksummed data, parameterized configuration, a single-command runner, and continuous integration that rebuilds the environment and reproduces a key result/figure on every commit. The deliverable turns "it works on my machine" into a portable, automated, FAIR-aligned reproduction.

**When to use:** Before submitting a computational study for publication or review, when handing a project to collaborators, or when retrofitting reproducibility onto an existing analysis or simulation pipeline.

**Required inputs:**
- **Discipline.** [user-supplied] (e.g., bioinformatics, climate modeling, computational chemistry, data science)
- **Study type.** [user-supplied — typically `computational/simulation` or `computational/analysis`]
- **Language / runtime ecosystem.** Python, R, Julia, C++/Fortran, mixed, etc. (drives lockfile and container choice).
- **Key result to reproduce.** The specific figure, table, or summary statistic that CI will regenerate as the reproduction target.
- **Data characteristics.** Size, provenance, and sensitivity (public, restricted, or private/sensitive). Mark `[user-supplied]` if unknown.

**Optional inputs:**
- Hardware/accelerator dependence (GPU, specific BLAS/LAPACK, MPI) and any known nondeterminism.
- Existing environment artifacts (an `environment.yml`, `requirements.txt`, `renv.lock`, `Dockerfile`).
- Compute scale (single workstation vs. HPC/cluster) and scheduler (Slurm, etc.).
- Whether a workflow manager (Snakemake, Nextflow, targets, Make) is already in use.

**Constraints — Must:**
- Specify a **lockfile** that pins exact transitive dependency versions (e.g., `conda-lock`, `renv`, Nix, `uv`/`pip-tools` compiled lock) — not loose version ranges.
- Specify a **container** (Docker, or Apptainer/Singularity for HPC) so the OS-level and system-library stack is captured and portable.
- Record **OS and hardware notes**, including sources of nondeterminism (GPU kernels, multithreaded BLAS reductions, MPI rank ordering) and the mitigation (fixed thread counts, deterministic flags, documented tolerance).
- Set and record **fixed random seeds** at every stochastic layer; state where exact bitwise reproduction is not achievable and define an acceptable numerical tolerance instead.
- **Version data** and record **checksums** (and a retrieval method) so inputs are pinned, with a synthetic/test dataset used where data is private.
- **Parameterize configuration** (a config file, not hard-coded constants) and provide a **one-command runner** (`make reproduce`, a workflow target, or equivalent).
- Provide **CI** that, on each commit, rebuilds the environment from the lockfile/container and reproduces the key result, failing if it drifts beyond tolerance.
- Align the stack with **FAIR4RS** principles and **The Turing Way** reproducibility guidance; name them where a layer maps to them.
- Default to the **Open Science** posture: containerized, pinned, archivable, and citable. For sensitive data, the public/CI path uses **synthetic or test data**; the real-data path is documented separately with access controls.

**Constraints — Must Not:**
- Do not invent citations, DOIs, tool version numbers, benchmark values, or convergence thresholds. If needed and not supplied, mark `[user-supplied]` and ask.
- Do not pin to loose ranges (`>=`, `^`, `~`) where exact reproduction is the goal — use compiled lockfiles.
- Do not commit private/sensitive data or secrets to the repo or CI; CI must run on synthetic/test data when real data is restricted.
- Do not claim "reproducible" when only the analysis script is shared but the environment, seeds, or data versions are not pinned.
- Do not use promotional language ("novel", "groundbreaking", "first-ever", "gold standard") in the drafted plan.

**Instructions:**

1. **Inventory the stack.** Enumerate every layer that affects results: OS, system libraries, language runtime, packages, data, configuration, hardware/accelerators. Reproducibility fails at the layer you forget.
2. **Pin dependencies with a lockfile.** Choose the lockfile matched to the ecosystem and compile exact transitive versions. Distinguish the human-readable manifest from the machine-resolved lock.
3. **Containerize.** Write (or specify) a container that installs from the lockfile, so the environment is portable across machines and HPC. Note Apptainer/Singularity where Docker is unavailable.
4. **Control determinism.** Set seeds at each stochastic boundary; pin thread counts and library determinism flags; document residual nondeterminism (e.g., GPU atomics) and the tolerance you accept instead of bitwise equality.
5. **Version and checksum data.** Pin input data by version and checksum with a documented retrieval step. Where data is sensitive, generate a synthetic/test dataset that exercises the same pipeline for CI.
6. **Parameterize and provide a one-command runner.** Move tunables into a config file; expose a single entry point (`make reproduce` / workflow runner) that goes from clean checkout to the key result.
7. **Wire CI.** Configure CI to rebuild the environment from the lockfile/container, run the pipeline on synthetic/public data, regenerate the key result/figure, and compare against a stored expected output within tolerance — failing the build on drift.
8. **Self-check on a clean machine.** Confirm a fresh clone + container + one command reproduces the target. List the layers verified and any that remain machine-dependent.

**Output format (locked):**

```
## Reproducibility Scope
- Discipline / study type:
- Runtime ecosystem:
- Key result CI will reproduce:
- Data sensitivity (public / restricted / sensitive):

## Reproducibility Stack
| Layer | Tool | Artifact | Notes |
|-------|------|----------|-------|
| OS / system libs | container base | Dockerfile/Apptainer def |  |
| Dependencies | conda-lock / renv / Nix / uv |  lockfile | exact pins |
| Data | DVC / checksums / synthetic |  data manifest + hashes |  |
| Config | config file | params.yaml/json |  |
| Randomness | seeds / determinism flags | recorded seeds + tolerance |  |
| Runner | make / workflow manager | one-command entry point |  |

## Determinism & Hardware Notes
- Sources of nondeterminism:
- Mitigations (seeds, thread pins, flags):
- Bitwise vs. tolerance-based reproduction:

## CI Plan
- Trigger: every commit / PR
- Steps: rebuild env from lock → run on synthetic/public data → regenerate key result → compare to expected within tolerance
- Failure condition (drift threshold):

## Open Science / Sensitive-Data Posture
- Public/CI path (synthetic or test data):
- Real-data path (access-controlled, documented separately):
```

**Reporting-standard alignment:** FAIR4RS (FAIR Principles for Research Software) and The Turing Way reproducible-research guidance; containerization and lockfile practices consistent with research-software-engineering norms.

**Verification checklist (before delivering):**
- [ ] A compiled lockfile pins exact transitive dependency versions.
- [ ] A container captures the OS/system-library layer (Docker or Apptainer/Singularity).
- [ ] Seeds are fixed and recorded; residual nondeterminism is documented with a tolerance.
- [ ] Input data is versioned and checksummed; sensitive data uses a synthetic/test substitute in CI.
- [ ] Configuration is parameterized and a one-command runner exists.
- [ ] CI rebuilds the environment and reproduces a key result on each commit.
- [ ] No secrets or private data are committed to the repo or CI.
- [ ] No fabricated version numbers or thresholds; unknowns marked `[user-supplied]`.

**False-positive matrix:**

| Risk | What "looks right but isn't" | Guardrail |
|---|---|---|
| "Reproducible" = script shared | Code is public but env/seeds/data unpinned | Require full stack: lockfile + container + seeds + data versions |
| Loose version ranges | `requirements.txt` with `>=` "works today" | Compile an exact lockfile; CI rebuild catches drift |
| Hidden nondeterminism | Results vary run-to-run on GPU/threads | Document sources; pin threads/flags; define a tolerance |
| Works-on-my-machine | Passes locally, fails on a clean container | CI rebuild from scratch on each commit |
| Sensitive data leak | Real dataset committed to make CI pass | CI runs on synthetic/test data; real path access-controlled |
| Stale expected output | CI compares to an output that itself drifted | Tie expected output to a pinned, documented reference |
