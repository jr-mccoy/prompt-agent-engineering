---
title: "Science-Specific Code Review for Research Software"
category: science/teaching-research-methods
description: "Produce a scientific code-review checklist and a teaching-exercise guide that target correctness, reproducibility, and numerical stability rather than generic software-engineering style."
techniques:
  - ST-01
  - ST-03
  - RT-03
  - QA-01
  - QA-02
  - DS-02
difficulty: advanced
tags:
  - code-review
  - scientific-software
  - reproducibility
  - numerical-stability
  - research-software-engineering
  - data-leakage
  - teaching-exercise
  - open-science
updated: "2026-06-26"
related_prompts:
  - domain-science/teaching-research-methods/science_data_analysis_workshop_designer.md
  - domain-science/teaching-research-methods/science_reproducibility_workshop_designer.md
  - domain-science/computational/science_computational_reproducibility_environment.md
  - domain-science/computational/science_open_source_research_software_repo_layout.md
---

# Science-Specific Code Review for Research Software

**Objective:** Generate a code-review framework for research software that goes beyond generic engineering style and targets the failure modes that corrupt scientific results: whether the code implements the intended method or equation, whether a result can be regenerated bit-for-bit (or within stated tolerance), whether the numerics are stable, and whether ML-for-science pipelines leak. The output is a usable review checklist plus a guide to running the review as a hands-on teaching exercise for a lab or workshop.

**When to use:** A research group, lab, or course needs to review computational analysis code (a model, simulation, data pipeline, or ML-for-science workflow) for scientific validity before it backs a figure, dataset, or paper — or wants to teach reviewers how to do this.

**Required inputs:**
- **Discipline.** The scientific field (e.g., climate modeling, genomics, condensed-matter physics, computational chemistry, ecology). Shapes which numerical and provenance concerns dominate.
- **Level / audience.** Who performs the review (e.g., grad students new to research software, a lab with mixed experience, RSE workshop participants).
- **Code under review.** What the code does and its language/stack (`[user-supplied]` — paste or describe). What scientific claim or artifact it supports.

**Optional inputs:**
- **Known-good reference.** Any analytic solution, published benchmark, prior implementation, or hand-calculation the code can be checked against.
- **ML component.** Whether the pipeline trains/evaluates a model (triggers the data-leakage section).
- **Existing tests / CI.** What automated checks already run.
- **Risk level.** Whether the result is exploratory or destined for publication / a regulatory submission.

**Constraints — Must:**
- Begin by confirming discipline and reviewer level, then tailor the checklist weighting to that field's dominant failure modes.
- Cover all five science-specific axes: (1) scientific correctness, (2) reproducibility, (3) numerical stability, (4) data leakage for ML-for-science, (5) documentation and citability.
- For each finding, state the *scientific consequence* (e.g., "biases the estimate," "result is irreproducible across machines"), not just the code smell.
- Distinguish checks that need a domain expert from checks any reviewer can run.
- Recommend tests against analytic/known cases and edge cases wherever a ground truth exists.
- Weave Open-Science defaults (seeds, environment capture, data provenance, archiving) into the reproducibility axis.
- Cross-reference `domain-software-engineering/` for generic concerns (readability, security, dependency hygiene, performance) instead of re-deriving them.

**Constraints — Must Not:**
- Do not invent papers, datasets, code facts, or citations the user hasn't supplied. If needed and not supplied, mark `[user-supplied]` and ask.
- Do not assert the code is correct or reproducible — surface evidence and gaps; the review produces findings, not a certification.
- Do not duplicate generic SWE review content; defer it to the cross-referenced engineering material and stay on scientific failure modes.
- Do not use "novel," "groundbreaking," "first-ever," or "gold standard" in any drafted text.

**Instructions:**

1. **Scope and weight the review.** Confirm discipline and reviewer level. From the code description, identify which of the five axes carry the most risk for this artifact (e.g., a stochastic simulation foregrounds seeds + numerical stability; a genomics pipeline foregrounds provenance + leakage). Note where a domain expert is required.
2. **Scientific correctness.** Check that the code implements the *intended* method/equation, not a plausible neighbor: trace each equation/algorithm step to code; verify units and dimensional consistency; confirm boundary/initial conditions, sign conventions, and indexing. Recommend unit tests against analytic solutions, conserved quantities, symmetry/invariance properties, and at least one published or hand-computed benchmark. Add edge cases (zero, empty, NaN/Inf inputs, boundaries of valid domain).
3. **Reproducibility.** Check for fixed random seeds (and that all stochastic sources are seeded), captured environment (versions/lockfile/container), recorded data provenance (source, version, checksum), and deterministic output. Confirm a documented one-command path from raw inputs to the result. Cross-reference `domain-science/computational/science_computational_reproducibility_environment.md`.
4. **Numerical stability.** Look for catastrophic cancellation (subtracting near-equal large numbers), ill-conditioning, unsafe floating-point equality comparisons, accumulation error in long sums/loops, untested convergence criteria and tolerances, overflow/underflow, and off-by-one errors in indexing, time-stepping, or unit conversions. Recommend stability checks: perturb inputs, vary precision, compare against a higher-precision or independent implementation.
5. **Data leakage (ML-for-science).** If a model is trained/evaluated, check that splits are made before any fitting/normalization/feature selection, that grouped/temporal structure is respected (no subject/site/time leakage), that the test set is touched once, and that metrics match the scientific question. Flag target leakage and pre-processing fit on the full dataset.
6. **Documentation and citability.** Check that the method, assumptions, parameters, and limitations are documented; that the software is citable (license, version, citation file/DOI); and that the link between code, data, and the specific figure/table is recorded. Cross-reference `domain-science/computational/science_open_source_research_software_repo_layout.md`.
7. **Defer generic concerns.** List generic SWE issues (style, security, dependency hygiene, performance, CI structure) as out-of-scope-here and point to `domain-software-engineering/`.
8. **Produce the teaching-exercise guide.** Turn the checklist into a session: a worked example, how to seed deliberate bugs across the five axes for trainees to find, live "review-the-reviewer" discussion, and a rubric. Apply The Carpentries pedagogy (live coding, formative checks, sticky notes for pacing/confusion).
9. **Assemble outputs and verify.** Emit the locked format and run the verification checklist.

**Output format (locked):**

```
## Review Scope
Discipline: [...] | Reviewer level: [...] | Artifact under review: [...]
Highest-risk axes for this code: [...]
Domain-expert sign-off required for: [...]

## Science Code-Review Checklist

### 1. Scientific Correctness
- [ ] <check> — scientific consequence if it fails: <...> — who can run it: <any reviewer / domain expert>
Recommended tests (analytic / known-case / edge): [...]

### 2. Reproducibility
- [ ] <check> — consequence: <...>
One-command reproduce path documented? [yes / no / gap]

### 3. Numerical Stability
- [ ] <check> — consequence: <...>
Recommended stability probes: [...]

### 4. Data Leakage (ML-for-science) — [applicable / not applicable]
- [ ] <check> — consequence: <...>

### 5. Documentation & Citability
- [ ] <check> — consequence: <...>

## Deferred to Generic Engineering Review
[items] → see domain-software-engineering/

## Findings (if code supplied)
| Axis | Finding | Scientific consequence | Severity | Suggested fix |
|---|---|---|---|---|
| [...] | [...] | [...] | [...] | [...] |

## Teaching-Exercise Guide
- Learning outcomes: [...]
- Worked example: [...]
- Seeded-bug bank (≥1 per axis): [...]
- Session flow (Carpentries: live coding + formative checks + sticky notes): [...]
- Rubric: [...]

## Open Items Needing User Input
[user-supplied] markers: [...]
```

**Reporting-standard alignment:** No formal reporting standard for scientific code review; aligns to The Carpentries pedagogy + FAIR/FAIR4RS (citable, versioned, environment-captured research software) and standard numerical-analysis practice.

**Verification checklist (before delivering):**
- [ ] Discipline and reviewer level confirmed and used to weight the checklist.
- [ ] All five science-specific axes present, each with scientific-consequence framing.
- [ ] Correctness checks recommend tests against analytic/known cases plus edge cases.
- [ ] Reproducibility axis covers seeds, environment, provenance, deterministic output, one-command reproduce.
- [ ] Numerical-stability axis names concrete failure modes (cancellation, conditioning, convergence, off-by-one).
- [ ] Data-leakage section marked applicable/not-applicable correctly.
- [ ] Generic SWE concerns deferred to `domain-software-engineering/`, not re-derived.
- [ ] No fabricated papers/datasets/code-facts; gaps marked `[user-supplied]`.
- [ ] No banned promotional language in any drafted text.

**False-positive matrix:**

| Risk | What "looks right but isn't" | Guardrail |
|---|---|---|
| Style mistaken for science | Review fixates on naming/formatting while the equation is wrong | Lead with correctness-to-intended-method; defer style to generic review |
| Passing tests ≠ correct | Unit tests pass but only cover the happy path, not analytic/edge cases | Require at least one analytic/benchmark and explicit edge cases |
| "It runs" mistaken for reproducible | Output regenerates on one machine but seeds/environment uncaptured | Demand seed + environment + provenance + cross-machine determinism |
| Silent numerical error | Plausible-looking numbers from cancellation or non-converged solver | Probe with perturbation, higher precision, independent implementation |
| Hidden leakage | High ML score from normalization/feature selection fit before split | Verify split precedes all fitting; respect group/temporal structure; test set used once |
| Overconfident sign-off | Checklist completed implies "validated" | Output is findings + gaps, never a certification; require domain-expert sign-off where flagged |
