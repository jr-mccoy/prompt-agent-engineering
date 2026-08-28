---
title: "Data Readiness Assessment"
category: AI-ML/problem-framing-scoping
description: "Determine whether the available data is sufficient, representative, labeled, and legally usable to attempt the problem — before any modeling effort is committed."
techniques:
  - ST-02
  - RT-05
  - DS-06
  - CM-02
  - QA-12
difficulty: intermediate
tags:
  - data-readiness
  - labels
  - representativeness
  - data-governance
  - problem-framing
updated: "2026-05-29"
related_prompts:
  - domain-AI-ML/problem-framing-scoping/mlframe_ml_use_case_canvas.md
  - domain-AI-ML/problem-framing-scoping/mlframe_feasibility_risk_assessment.md
  - domain-AI-ML/data-for-ml/mldata_data_leakage_detector.md
---

# Data Readiness Assessment

**Objective:** Assess whether the data available for a proposed ML problem is sufficient in volume, representative of production conditions, adequately labeled, and legally/ethically usable — and return a GO / GO-WITH-WORK / NOT-READY verdict with the specific gaps that must close first.

**When to Use:**
- Before committing modeling resources to a use case.
- When a use case looks promising but data quality is unverified.
- To triage why a previous modeling attempt underperformed (often a data-readiness failure).

**When NOT to Use:**
- You need to hunt for leakage specifically in an existing pipeline (use `mldata_data_leakage_detector.md`).
- The question is whether ML is warranted at all (use `mlframe_is_this_ml_problem.md`).

## Inputs / Context

Provide what you can:
- **Target definition** — what's predicted and how the label is generated.
- **Data sources** — tables/streams, volume, history length, freshness/latency.
- **Labels** — how many, how produced (human/auto/proxy), label quality/agreement if known.
- **Representativeness** — does training data match the production population and time period?
- **Legal/ethical context** — consent, PII, regulated attributes, licensing/usage rights.
- **Known quality issues** — missingness, duplication, schema changes over time.

## Constraints

**Must:**
- Assess four dimensions explicitly: sufficiency (volume), representativeness, label adequacy, and legal/ethical usability.
- For each dimension, give a status (ready / gap / blocker) with the evidence behind it.
- Distinguish a fixable gap (collect more, relabel) from a hard blocker (no legal basis to use the data).

**Must Not:**
- Assume labels exist or are reliable without confirming how they're produced.
- Invent volume, label-agreement, or class-balance numbers — mark unknowns and how to measure them.
- Declare data "representative" without naming the production population it's compared against.

**Instructions:**

1. **Pin the target and label-generation mechanism.** State exactly what's predicted and how each label comes to exist (human annotation, system event, proxy). A noisy or proxy label caps achievable quality.

2. **Assess sufficiency.** Compare available volume — especially minority-class count — against the complexity of the problem. Flag where the positive class is too thin to learn from.

3. **Assess representativeness.** Compare the training population and time window to production: segments present/absent, distribution shift, seasonality, and any sampling bias in how data was collected.

4. **Assess label adequacy.** Examine label coverage, inter-annotator agreement (if human), proxy-vs-truth gap, and staleness. Note where label noise will dominate model error.

5. **Assess legal/ethical usability.** Check consent/usage rights, PII handling, regulated/protected attributes, and licensing. A failure here is a hard blocker regardless of data quality.

6. **Separate gaps from blockers and rank them.** Order issues by impact on feasibility and label each as fixable-with-work or hard-blocker.

7. **Render the verdict and the close-out plan.** Give GO / GO-WITH-WORK / NOT-READY, and for anything short of GO, the concrete work (collection, relabeling, governance review) needed.

**Output Format:**

A markdown readiness report:
- **Verdict** — GO / GO-WITH-WORK / NOT-READY + one-line rationale.
- **Dimension Scorecard** — table: Dimension | Status | Evidence | Gap/Blocker.
- **Top Gaps & Blockers (ranked)** — impact + fixable-with-work vs hard-blocker.
- **Close-Out Plan** — what to collect/fix/review before GO.
- **Open Measurements** — numbers to obtain (volume, agreement, balance).
- **INSUFFICIENT EVIDENCE** — a fourth verdict alongside GO / GO-WITH-WORK / NOT-READY, and materially different from NOT-READY: one says the data is inadequate, the other says nobody has looked. Use it where the assessment rests on a description of the data rather than on the data, and name the unblocking datum from Open Measurements that would produce a real verdict.

## Verification

- [ ] All four dimensions (sufficiency, representativeness, labels, legal) are assessed with evidence.
- [ ] Label-generation mechanism is named and its reliability considered.
- [ ] Representativeness is judged against a stated production population.
- [ ] Hard blockers (legal/ethical) are separated from fixable gaps.
- [ ] No volume/agreement/balance figure is invented; unknowns are listed to measure.
- [ ] Where the assessment rests on a description rather than on the data, the verdict is INSUFFICIENT EVIDENCE — distinct from NOT-READY — with the measurement that would resolve it named.

## False-Positive Prevention

❌ **DON'T:**
- Call data "ready" on total row count while the minority class has too few examples to learn.
- Assume labels are ground truth when they're a proxy (e.g., "clicked" ≠ "satisfied").
- Judge representativeness without comparing to the actual production population and time period.
- Treat a privacy/consent gap as a "data cleaning" task — it can be a hard legal blocker.

✅ **DO:**
- Count minority-class examples, not just total rows, against problem complexity.
- Trace each label to how it was generated and estimate its noise ceiling.
- Name the production population and check which segments are missing or under-sampled.
- Flag protected-attribute and consent issues to governance before any modeling.

## Example Output

```markdown
## Data Readiness: Early Sepsis Risk Flag (ICU)

### Verdict
GO-WITH-WORK — sufficient volume and legal basis, but label definition and representativeness
need closing before modeling.

### Dimension Scorecard
| Dimension | Status | Evidence | Gap/Blocker |
|---|---|---|---|
| Sufficiency | Gap | ~9k admissions; positives ~6% → ~540 positive cases | thin minority class (fixable: pool sites) |
| Representativeness | Gap | Data from 1 academic hospital; deploy target includes community ICUs | population shift (fixable: add sites) |
| Labels | Gap | Sepsis label = chart-coded post hoc; timing vs onset unclear | proxy/temporal noise (fixable: clinician adjudication subset) |
| Legal/ethical | Ready | IRB-approved, de-identified, usage rights confirmed | none |

### Top Gaps & Blockers (ranked)
1. Label timing vs true onset — caps temporal model validity (fixable: adjudicate a 200-case subset).
2. Single-site population — limits generalization (fixable: multi-site data agreement).
3. Thin positive class — (fixable: combine sites; consider cost-weighting).

### Close-Out Plan
Adjudicate a labeled subset for onset timing; secure ≥2 additional sites; recount class balance.

### Open Measurements
Inter-rater agreement on adjudicated labels; per-site class balance; missingness by vital sign.
```

**Techniques Used:**
- **ST-02 (Structured Sequential Instructions):** marches through the four readiness dimensions in order.
- **RT-05 (Evidence-Based Reasoning):** each status is tied to a concrete data fact.
- **DS-06 (Prioritization & Severity Guidance):** ranks gaps and separates blockers.
- **CM-02 (Constraint Specification):** legal usability is a binding constraint on the verdict.
- **QA-12 (False Positives Identification):** guards against "rows = ready" and proxy-label errors.

**Related Prompts:**
- `mlframe_ml_use_case_canvas.md` — the data cell that this prompt deepens.
- `mlframe_feasibility_risk_assessment.md` — fold readiness gaps into overall feasibility.
- `mldata_data_leakage_detector.md` — once data is in hand, check it doesn't leak.
