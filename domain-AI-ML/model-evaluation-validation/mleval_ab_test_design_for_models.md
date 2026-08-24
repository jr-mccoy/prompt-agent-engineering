---
title: "A/B Test Design for Model Comparison"
category: AI-ML/model-evaluation-validation
description: "Design an online A/B test to compare models — randomization unit, power and duration, guardrail metrics, and handling of novelty and network effects — so the winner is real and safe."
techniques:
  - ST-02
  - RT-02
  - DS-02
  - CM-02
  - QA-12
difficulty: advanced
tags:
  - ab-testing
  - online-experiment
  - statistical-power
  - guardrail-metrics
  - network-effects
updated: "2026-05-29"
related_prompts:
  - domain-AI-ML/model-evaluation-validation/mleval_offline_online_alignment.md
  - domain-AI-ML/model-evaluation-validation/mleval_statistical_significance_testing.md
  - domain-AI-ML/model-evaluation-validation/mleval_metric_selection_guide.md
---

# A/B Test Design for Model Comparison

**Objective:** Design an online controlled experiment that can credibly decide whether a challenger model beats the champion on the business outcome — specifying the randomization unit, the powered sample size and duration, the primary and guardrail metrics, and the handling of novelty, primacy, and network effects — so the launch decision is trustworthy and safe.

**When to Use:**
- Promoting a model to production and you want online evidence, not just offline metrics.
- Offline gains don't transfer and you need a properly designed online test to confirm or refute them.
- Comparing two serving strategies where user behavior (not just accuracy) determines value.

**When NOT to Use:**
- You only have offline predictions to compare (use `mleval_statistical_significance_testing.md`).
- The proxy metric itself is in doubt (use `mleval_offline_online_alignment.md` first).

## Inputs / Context

Provide what you can:
- **Decision** — what the test must decide and the launch criteria.
- **Primary online metric** — the business outcome (and its baseline value/variance, if known).
- **Guardrail metrics** — what must not regress (latency, revenue, complaints, a key subgroup).
- **Unit of interaction** — user, session, device, or higher (does one unit's treatment affect another?).
- **Traffic volume** and the minimum effect size worth detecting (MDE).
- **Known dynamics** — novelty/primacy effects, seasonality, marketplace/social network coupling.

## Constraints

**Must:**
- Choose the **randomization unit** to match the unit of independence and the interference structure (cluster/switchback if units affect each other).
- **Power the test**: compute sample size and duration for the MDE and metric variance *before* launch; commit to the duration.
- Pre-register the **primary metric, guardrails, and decision rule** to prevent post-hoc cherry-picking.

**Must Not:**
- Stop the test early at the first significant moment without a sequential-testing correction (peeking inflates false positives).
- Fabricate baseline rates, variance, or required sample sizes; if inputs are missing, state the formula and what's needed.
- Use user-level randomization when treatment spills across users (marketplace/social) — that biases the estimate.

**Instructions:**

1. **Define the decision and primary metric.** State the launch criterion and the single primary online metric. Confirm (via offline–online alignment) it tracks the real outcome before committing traffic.

2. **Choose the randomization unit and design.** Pick user/session/cluster/switchback based on interference. If one unit's treatment affects another's outcome (recommendations to shared inventory, social features), use cluster randomization or a switchback design and say why.

3. **Power and duration.** Using the baseline rate, variance, MDE, and desired power (e.g., 80%) and significance, compute the sample size and the calendar duration — including enough time to clear novelty/primacy and at least one full seasonal cycle (e.g., a week).

4. **Specify guardrails and stopping rules.** List guardrail metrics that auto-halt the test if breached, and define a valid stopping rule (fixed-horizon or a sequential/Bayesian method with correction) — no naked peeking.

5. **Handle novelty, primacy, and network effects.** Plan to read metrics over time (not just the final average), exclude or model the novelty window, and check for cross-unit interference if randomization is below the interference unit.

6. **Pre-register analysis.** Fix the primary test, the correction for any secondary metrics, the segments to report, and the decision rule (ship / hold / iterate) before data collection.

7. **Plan the readout.** Report the primary effect with a CI, guardrail status, time-trend, and segment breakdown; tie the verdict to the pre-registered rule and note residual risks.

**Output Format:**

An experiment design doc:
- **Decision & Primary Metric** — criterion and the metric.
- **Randomization Design** — unit, design (simple/cluster/switchback), and rationale.
- **Power & Duration** — MDE, baseline/variance assumptions, sample size, calendar duration.
- **Guardrails & Stopping Rule** — auto-halt metrics and the valid stopping method.
- **Dynamics Handling** — novelty/primacy/seasonality/network plan.
- **Pre-Registered Analysis** — primary test, corrections, segments, decision rule.

## Verification

- [ ] The randomization unit matches the interference structure (cluster/switchback if spillover exists).
- [ ] Sample size and duration are powered for a stated MDE and committed before launch.
- [ ] Primary metric, guardrails, and decision rule are pre-registered.
- [ ] The stopping rule corrects for peeking (fixed-horizon or sequential method).
- [ ] Novelty/primacy and seasonality are addressed in the duration/readout plan.
- [ ] No baseline rates, variances, or sample sizes are fabricated; missing inputs are flagged.

## False-Positive Prevention

❌ **DON'T:**
- Peek daily and ship the moment p<0.05 — repeated looks at a fixed-horizon test inflate the false-positive rate.
- Randomize at the user level when the feature couples users (shared marketplace inventory, social graph) — spillover biases both arms.
- Read only the final-day average and miss a novelty spike that fades, or a trend that's still moving.
- Launch under-powered and interpret a null as "no difference" when the test couldn't have detected the MDE.

✅ **DO:**
- Commit to a powered duration, or use a proper sequential/Bayesian test if you must monitor continuously.
- Match the randomization unit to the interference structure; use cluster/switchback designs when units interact.
- Read the metric over time and exclude/model the novelty window before judging steady-state effect.
- Compute power up front so a null result is informative, not just inconclusive.

## Example Output

```markdown
## A/B Design: Search Ranker — Challenger vs. Champion

### Decision & Primary Metric
Ship the challenger only if it lifts 7-day query-success rate without breaching guardrails.
Primary: query-success rate (clicked + dwell ≥ 30s). Confirmed to track retention via offline–online alignment.

### Randomization Design
User-level randomization, 50/50. Interference check: ranking does not consume shared finite inventory →
spillover negligible → simple user-level randomization is valid (documented).

### Power & Duration
Baseline success ≈ 42%, MDE = +1.0pp, 80% power, α=0.05 → ~38,000 users/arm.
At current traffic that's ~9 days; extend to 14 days to clear novelty and cover two weekly cycles.

### Guardrails & Stopping Rule
Auto-halt if: p99 latency > 350ms, revenue-per-session −2%, or complaint rate +20%.
Fixed-horizon analysis at day 14 (no early ship). Continuous monitoring only for guardrail safety, not for the primary call.

### Dynamics Handling
Read success rate by day; exclude days 1–2 (novelty) from the steady-state estimate but report both.
Seasonality covered by spanning two full weeks.

### Pre-Registered Analysis
Primary: two-proportion test on query-success with 95% CI. Secondary metrics Benjamini–Hochberg corrected.
Report overall + new-vs-returning user segments. Decision rule: ship iff primary CI lower bound > 0 and no guardrail breach.
```

**Techniques Used:**
- **ST-02 (Structured Sequential Instructions):** decision → unit → power → guardrails → dynamics → pre-registration → readout.
- **RT-02 (Multi-Dimensional Analysis Framework):** balances power, interference, dynamics, and safety.
- **DS-02 (Metric Specification):** precise primary/guardrail metric definitions.
- **CM-02 (Constraint Specification):** power, duration, and guardrails are governing constraints.
- **QA-12 (False Positives Identification):** peeking, spillover, and under-powering are the central traps.

**Related Prompts:**
- `mleval_offline_online_alignment.md` — validate the proxy before spending traffic on the test.
- `mleval_statistical_significance_testing.md` — the offline counterpart when no online test is possible.
- `mleval_metric_selection_guide.md` — choose the primary and guardrail metrics the test will use.
