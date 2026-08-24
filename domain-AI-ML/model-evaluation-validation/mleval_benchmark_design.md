---
title: "Benchmark Design (Contamination-Free)"
category: AI-ML/model-evaluation-validation
description: "Design a fair, contamination-free benchmark for a task — representative data, leak-proof splits, baselines, and protocols that resist teaching-to-the-test and gaming."
techniques:
  - ST-02
  - RT-02
  - DS-02
  - CM-02
  - QA-12
difficulty: advanced
tags:
  - benchmark-design
  - contamination
  - data-splits
  - baselines
  - overfitting
updated: "2026-05-29"
related_prompts:
  - domain-AI-ML/model-evaluation-validation/mleval_evaluation_harness_design.md
  - domain-AI-ML/model-evaluation-validation/mleval_baseline_comparison_protocol.md
  - domain-AI-ML/model-evaluation-validation/mleval_eval_result_skepticism_audit.md
---

# Benchmark Design (Contamination-Free)

**Objective:** Design a benchmark that measures real task ability — representative and well-specified data, a contamination-proof held-out set, mandatory baselines, and a scoring protocol that resists overfitting and teaching-to-the-test — so that scores on it transfer to the real world rather than rewarding memorization.

**When to Use:**
- Standing up an internal benchmark to compare models or vendors over time.
- A public/standard benchmark is suspected of contamination (test data seen in training, especially for LLMs).
- Replacing an ad-hoc test set that teams have started overfitting to.

**When NOT to Use:**
- You only need a per-project eval harness wired to one model (use `mleval_evaluation_harness_design.md`).
- You're auditing a single suspicious result (use `mleval_eval_result_skepticism_audit.md`).

## Inputs / Context

Provide what you can:
- **Task definition** — exactly what capability the benchmark must measure, and what "good" means.
- **Population the score should generalize to** — the real distribution the benchmark stands in for.
- **Data sources** — where benchmark items come from; whether models may have trained on them.
- **Models under test** — especially whether they are large pretrained models with broad web exposure.
- **Gaming risks** — how a team might inflate scores without real improvement.
- **Refresh constraints** — can the benchmark be rotated/renewed, and how often?

## Constraints

**Must:**
- Build a **contamination check**: confirm test items are not present in (or trivially derivable from) any model's training data, and document the method.
- Make the benchmark **representative** of the target population, with documented coverage of important slices and difficulty bands.
- Include **mandatory baselines** (random/majority/simple heuristic/strong prior model) so any score is interpretable.

**Must Not:**
- Reuse a single static test set indefinitely without a contamination/renewal plan — it decays into a memorization target.
- Fabricate item counts, contamination rates, or scores; describe the design, not invented outcomes.
- Let a single aggregate number stand as the benchmark — require slice and baseline reporting.

**Instructions:**

1. **Specify the capability and target population.** Define precisely what the benchmark measures and the real distribution it generalizes to; list the slices/difficulty bands that must be covered.

2. **Source and curate items.** Decide where items come from, how labels are produced and quality-controlled (inter-annotator agreement if human-labeled), and how ambiguous items are handled.

3. **Design contamination-proof partitions.** Choose a held-out set that models could not have seen; for pretrained models, prefer freshly created/post-cutoff items, canary strings, or transformations that defeat memorization. Document the contamination test.

4. **Define baselines and the bar.** Specify the trivial and strong baselines computed on the same items every time, so improvements are always relative.

5. **Lock the scoring protocol.** Fix the metric, operating point, averaging, and per-slice reporting; require confidence intervals; forbid per-submission threshold tuning on the test set.

6. **Anti-gaming and overfitting defenses.** Limit submission frequency against the hidden set, keep a private split, rotate items periodically, and watch for score patterns that indicate teaching-to-the-test rather than capability.

7. **Plan renewal.** Define how and how often items are refreshed/retired, who governs changes, and how versioned benchmark numbers stay comparable.

8. **Document validity threats.** State the ways the benchmark could be misleading (narrow coverage, label noise, residual contamination) so consumers calibrate trust.

**Output Format:**

A benchmark design doc:
- **Capability & Population** — what it measures and generalizes to.
- **Item Sourcing & Labeling** — provenance, QC, agreement.
- **Partitions & Contamination Test** — held-out design + the contamination-check method.
- **Baselines & Bar** — baselines computed every run.
- **Scoring Protocol** — metric, slices, CIs, submission rules.
- **Anti-Gaming & Renewal** — defenses and refresh policy.
- **Validity Threats** — documented limitations.

## Verification

- [ ] A contamination test is specified with its method, not just asserted.
- [ ] The benchmark documents coverage of the target population's key slices and difficulty bands.
- [ ] Mandatory baselines are computed on the same items every run.
- [ ] The scoring protocol forbids per-submission tuning on the test set and requires CIs.
- [ ] An anti-gaming defense (private split / submission limits / rotation) is in place.
- [ ] A renewal/refresh policy and documented validity threats are included.

## False-Positive Prevention

❌ **DON'T:**
- Assume a public benchmark is clean for a large pretrained model — web-scraped test items are frequently memorized.
- Treat one static held-out set as permanent; repeated submissions turn it into a training signal.
- Report a single benchmark number without baselines and slices — it hides where the score comes from.
- Let teams tune thresholds against the test set per submission and call the gains real.

✅ **DO:**
- Build and document a contamination test (post-cutoff items, canaries, dedup against training corpora).
- Keep a private split and rotate items so the benchmark measures capability, not exposure.
- Always report baselines and per-slice scores with CIs alongside the headline number.
- Limit submissions and watch for teaching-to-the-test signatures (gains that don't transfer to fresh items).

## Example Output

```markdown
## Benchmark Design: Internal Code-Generation Benchmark v1

### Capability & Population
Measures ability to implement small, well-specified functions from a spec + tests, generalizing to our
internal repo style. Slices: language (Py/TS/Go), difficulty (easy/med/hard), spec ambiguity (low/high).

### Item Sourcing & Labeling
240 freshly authored tasks written *after* the candidate models' training cutoffs; each has hidden unit
tests. Two engineers review each task; disputed tasks dropped. No items copied from public datasets.

### Partitions & Contamination Test
180 public-practice + 60 private held-out (never published). Contamination test: search each task's
prompt/solution against known training corpora and check for verbatim or near-duplicate matches; embed a
canary string in private items to detect future leakage.

### Baselines & Bar
- Empty/stub solution (compiles, fails tests) — floor.
- Retrieval-of-nearest-public-snippet heuristic.
- Prior in-house model (champion).

### Scoring Protocol
Metric: pass@1 on hidden tests, per-slice, with 95% bootstrap CIs. No per-submission test tuning.
Aggregate + per-slice rows mandatory.

### Anti-Gaming & Renewal
Max 1 private-split submission per model per week. 25% of items rotated quarterly. Watch for public-split
gains that don't replicate on the private split (teaching-to-the-test signature).

### Validity Threats
Small per-slice n (60 private) → wide CIs on hard slice; mitigated by quarterly growth. Residual
contamination risk if a model trained on our internal repo — checked via canary.
```

**Techniques Used:**
- **ST-02 (Structured Sequential Instructions):** capability → sourcing → partitions → baselines → scoring → anti-gaming → renewal.
- **RT-02 (Multi-Dimensional Analysis Framework):** balances representativeness, contamination, and gaming risk.
- **DS-02 (Metric Specification):** precise scoring protocol with baselines and CIs.
- **CM-02 (Constraint Specification):** the contamination-free and no-test-tuning rules are governing constraints.
- **QA-12 (False Positives Identification):** contamination and teaching-to-the-test are the central false-positive traps.

**Related Prompts:**
- `mleval_evaluation_harness_design.md` — wire the benchmark into a repeatable harness.
- `mleval_baseline_comparison_protocol.md` — specify the baselines the benchmark must include.
- `mleval_eval_result_skepticism_audit.md` — audit a benchmark score that looks too good.
