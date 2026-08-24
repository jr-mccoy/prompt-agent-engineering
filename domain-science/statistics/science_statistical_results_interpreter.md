---
title: "Statistical Results Interpreter"
category: science/statistics
description: "Turn user-supplied numeric results into a calibrated interpretation that separates statistical from practical significance, refuses absence-of-evidence spin, and states the inferential ceiling of the design."
techniques:
  - ST-01
  - RT-01
  - QA-02
  - CM-02
  - DS-02
  - QA-01
difficulty: advanced
tags:
  - results-interpretation
  - p-value-spin
  - absence-of-evidence
  - equivalence-testing
  - harking
  - causal-vs-associational
  - calibrated-claims
  - confirmatory-exploratory
updated: "2026-06-26"
related_prompts:
  - domain-science/statistics/science_effect_size_and_uncertainty_reporter.md
  - domain-science/statistics/science_statistical_test_selector.md
  - domain-science/statistics/science_multiple_comparisons_strategy.md
  - domain-science/methods-foundations/science_power_and_sample_size_calculator.md
---

# Statistical Results Interpreter

**Objective:** Take supplied numeric results (estimates, intervals, p-values, design facts) and produce a calibrated interpretation that distinguishes statistical from practical significance, refuses to read a non-significant result as "no effect," flags p-only spin and HARKing, keeps confirmatory and exploratory claims apart, and states what the design and data can and cannot support. It produces interpretation text aligned with the ASA statement on p-values and SAMPL/CONSORT/STROBE reporting norms.

**When to use:** When drafting the Results/Discussion or reviewing a manuscript's claims — after analyses are complete — to ensure conclusions are warranted by the numbers and the design.

**Required inputs:**
- **Discipline.** [user-supplied]
- **Study type.** [user-supplied] (observational / experimental / computational / quasi-experimental)
- **The numeric results.** Effect estimates, intervals, p-values, n, and which comparisons they belong to — `[user-supplied]`.
- **Design facts.** Randomized? Controlled? Blinded? Confounders adjusted? Sampling frame?
- **Pre-registration status.** Which results are pre-specified primary vs secondary vs exploratory.

**Optional inputs:**
- Smallest effect size of interest (SESOI) and any equivalence-test (TOST) results.
- The multiplicity strategy applied (if any).
- The originally stated hypotheses (to detect HARKing against later claims).
- Known limitations (missing data, attrition, measurement error).

**Constraints — Must:**
- Separate statistical significance from practical significance for every result.
- For non-significant results, refuse "no effect" / "no difference" claims; point to interval width and/or equivalence testing (absence of evidence ≠ evidence of absence).
- Flag p-only spin (significance reported without magnitude) and HARKing (exploratory findings presented as if pre-specified).
- Keep confirmatory and exploratory claims in separate, labeled buckets.
- State the inferential ceiling: what the design supports — causal vs associational, generalizability bounds.
- Interpret only supplied numbers; never generate or impute values.

**Constraints — Must Not:**
- Do not invent citations, DOIs, datasets, effect sizes, or instrument/vendor specs. If needed and not supplied, mark `[user-supplied]` and ask.
- Do not infer causation from an observational design.
- Do not equate p > 0.05 with a null effect, or p < 0.05 with importance or with a high probability the hypothesis is true.
- Do not use the words "novel," "groundbreaking," "first-ever," or "gold standard" in any drafted interpretation text.
- Do not upgrade an exploratory result to a confirmatory claim.

**Instructions:**

1. **Confirm inputs.** Restate discipline, study type, the supplied results, design facts, and pre-registration status. Mark missing values `[user-supplied]` and ask — do not fill them in.
2. **Catalog each result.** List every estimate with its interval, p-value, and which hypothesis/comparison it belongs to (primary/secondary/exploratory).
3. **Split significance.** For each result, state statistical significance and, separately, practical significance vs the SESOI.
4. **Handle non-significant results.** Replace any "no effect" reading with an interval-width statement and, if available, an equivalence-testing conclusion; otherwise state the result is inconclusive.
5. **Stress-test the claims (adversarial).** Probe for p-only spin, HARKing, selective reporting, and over-generalization beyond the sample.
6. **Set the inferential ceiling.** Declare whether the design licenses causal or only associational language, and note generalizability limits.
7. **Build the interpretation table.** For each result: the defensible claim and the specific over-claim to avoid.
8. **Bucket confirmatory vs exploratory.** Label confirmatory conclusions; mark exploratory ones hypothesis-generating.
9. **Self-check.** Run the verification checklist and false-positive matrix.

**Output format (locked):**

```
## Inputs Confirmed
[discipline, study type, supplied results, design facts, pre-registration status]

## Results Catalog
| Result | Estimate + interval | p | Comparison | Status (primary/secondary/exploratory) |
|---|---|---|---|---|

## Interpretation Table
| Result | Defensible claim | Over-claim to avoid |
|---|---|---|

## Non-Significant Results
[interval-width / equivalence reading; explicit "inconclusive" where applicable]

## Inferential Ceiling
- Causal vs associational:
- Generalizability bounds:

## Confirmatory vs Exploratory
- Confirmatory conclusions:
- Exploratory (hypothesis-generating):
```

**Reporting-standard alignment:** ASA statement on p-values (Wasserstein & Lazar 2016) and "moving to a world beyond p<0.05"; SAMPL guidelines; CONSORT item 22 / STROBE item 20 (interpretation consistent with results and limitations). Estimation framing per Cumming's "new statistics"; equivalence via TOST.

**Verification checklist (before delivering):**
- [ ] Statistical vs practical significance separated for every result.
- [ ] No non-significant result interpreted as "no effect"; interval/equivalence cited instead.
- [ ] p-only spin and HARKing flagged where present.
- [ ] Confirmatory and exploratory claims labeled and kept apart.
- [ ] Causal vs associational ceiling stated for the design.
- [ ] Generalizability bounds noted.
- [ ] Only supplied numbers interpreted; nothing imputed or invented.
- [ ] No invented citations/specs; gaps marked `[user-supplied]`.

**False-positive matrix:**

| Risk | What "looks right but isn't" | Guardrail |
|---|---|---|
| Null misread | "No significant difference" → "the groups are equivalent" | Require interval width and/or TOST before any equivalence claim; else "inconclusive" |
| Causal leap | Observational association written as "X causes Y" | Restrict to associational language unless design (randomization) licenses causation |
| p-only spin | "Significant (p<0.001)" with no magnitude | Demand effect size + interval; route to the effect-size reporter |
| HARKing | Exploratory subgroup framed as the pre-stated hypothesis | Check against pre-registration; label exploratory as hypothesis-generating |
| Significance = truth | Treating p<0.05 as "the hypothesis is probably true" | State that p is not the probability the null/hypothesis is true (per ASA) |
