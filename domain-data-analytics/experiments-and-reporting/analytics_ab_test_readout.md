---
title: "A/B Test Readout — Validity Gates, Primary Result, Guardrails, Novelty, Multiplicity, and a Decision Memo"
category: data-analytics/experiments-and-reporting
description: "Read out a finished product or business A/B test in gated order — sample ratio mismatch, exposure and pre-registration checks, then the primary metric with an interval, guardrails against stated margins, novelty and time trends, and multiple-comparison control on secondaries and segments — and end in a one-page decision memo that separates what was measured from what is inferred."
techniques:
  - QA-08
  - RT-05
  - QA-04
  - QA-02
  - AG-08
difficulty: advanced
tags:
  - ab-test-readout
  - experiment-analysis
  - sample-ratio-mismatch
  - guardrail-metrics
  - decision-memo
  - business-analytics
  - not-significant
  - explaining-results
  - stakeholder-summary
updated: "2026-09-24"
related_prompts:
  - domain-data-analytics/framing-and-metrics/analytics_metric_definition_spec.md
  - domain-AI-ML/model-evaluation-validation/mleval_ab_test_design_for_models.md
  - domain-agentic-resources/skills/marketing/ab-test-setup/SKILL.md
---

# A/B Test Readout

**Objective:** Turn a finished experiment's raw results into a decision memo that a
product or business owner can act on, after the result has passed the validity
checks that most often turn a "win" into an artefact.

**When to Use:**
- An experiment has reached its planned sample size or duration and needs a ship / no-ship call.
- A result looks surprisingly good (or bad) and you want to check it before it is announced.
- Several teams read the same test differently and you need one written readout.
- A segment "win" is being cited and nobody has checked whether it survives multiplicity.

**When NOT to use:**
- The test has not launched — design it with `domain-agentic-resources/skills/marketing/ab-test-setup/`
  (hypothesis, sample size, duration); that skill's analysis checklist is the short
  version of this readout.
- You are comparing ML models online — `domain-AI-ML/model-evaluation-validation/mleval_ab_test_design_for_models.md`.
- You are A/B testing prompts — `domain-prompt-engineering/evaluation/regression/regression_ab_test_runner_prompt.md`.
- You need a research-grade multiplicity strategy — `domain-science/statistics/science_multiple_comparisons_strategy.md`.

## Inputs / Context

1. **The pre-registration or test plan** — hypothesis, primary metric, guardrails with
   margins, planned sample size, duration, MDE. If none exists, say so; the readout
   is then exploratory by default.
2. **Assignment counts** per arm, and the intended split.
3. **Exposure definition** — assigned vs actually exposed.
4. **Results** — per-arm counts or means and variances for primary, guardrails, secondaries.
5. **Daily or weekly breakdown** of the treatment effect.
6. **Segment results** anyone intends to cite.
7. **Any incidents** during the run — outages, releases, marketing pushes.

## Method

Each gate must pass before the next is read (QA-08). A failed gate stops the readout
at that point and becomes the headline.

1. **Gate 1 — Sample ratio mismatch.** Chi-square test of observed vs intended
   assignment counts. Flag at p < 0.001. An SRM means assignment or logging is broken;
   do not interpret any metric until it is explained.

2. **Gate 2 — Run integrity.** Planned duration and sample reached; test not stopped
   early on a peek; no mid-test change to the variant, allocation, or metric; full
   weekly cycles covered; exposure logging consistent across arms.

3. **Gate 3 — Primary metric (RT-05).** Report the absolute and relative effect with
   a 95% interval, not only a p-value. Compare the interval with the MDE the test was
   powered for. State the computation (e.g. two-proportion z-test, Welch t-test, CUPED
   if pre-registered).

4. **Gate 4 — Guardrails (AG-08).** Each guardrail has a pre-stated margin. A guardrail
   **fails** if the interval's harmful bound crosses the margin. "Not significant" is not
   "safe" — an underpowered guardrail proves nothing.

5. **Gate 5 — Novelty and time.** Plot the effect by day since first exposure. A
   large early effect decaying toward zero is novelty (or a learning effect in reverse).
   Report the effect in the most recent stable window as well as the overall one.
   Check that metrics with a lag (refunds, renewals) have matured for all users.

6. **Gate 6 — Multiplicity.** Count the secondaries and segments examined. Apply Holm
   (or Benjamini–Hochberg if pre-registered) to anything not pre-registered as primary.
   Label every segment result **exploratory** unless it was pre-registered.

7. **Attack the result (QA-02).** Would the decision change if the effect were at the
   lower end of its interval? If the result were a novelty effect? If the lagged
   guardrail kept worsening?

8. **Write the memo (QA-04).** Decision, the measured result, what is inferred beyond
   it, confidence, and what would reverse the decision. Tag inferred numbers — annualised
   revenue impact is always an inference.

## Output Format

```
# Experiment readout — [name]   Dates: [..]   Owner: [..]

## Decision
[Ship | Don't ship | Extend | Ship with conditions] — [one sentence why]

## Gates
| Gate | Check | Result | Pass? |
|---|---|---|---|

## Primary metric
| Arm | n | Value | Δ abs [95% CI] | Δ rel | vs MDE |
|---|---|---|---|---|---|

## Guardrails
| Guardrail | Margin | Δ [95% CI] | Pass? | Mature? |
|---|---|---|---|---|

## Novelty / time trend
## Secondaries and segments (adjusted; exploratory unless pre-registered)
| Metric / segment | Δ | Raw p | Adjusted p | Label |
|---|---|---|---|---|

## Measured vs inferred
## What would reverse this decision
## Confidence: [H/M/L]
```

## Verification

- [ ] SRM checked with a stated threshold before any metric is read.
- [ ] Planned sample and duration reached; no early stop.
- [ ] Primary effect has an interval and is compared with the MDE.
- [ ] Every guardrail has a margin and a maturity status.
- [ ] Effect by exposure day has been examined.
- [ ] Every non-primary result is multiplicity-adjusted and labelled.
- [ ] Projected impact numbers are tagged as inferred.
- [ ] The memo states what would reverse the decision.

## False-Positive Prevention

1. **Reading metrics through an SRM.** A 50/50 test that landed 50.4/49.6 on 100,000
   users has a real problem. Stop and find it.
2. **Peeking and stopping.** A test stopped the first day p dipped below 0.05 has a
   false-positive rate far above 5%. If it was stopped early without a sequential
   design, the result is exploratory.
3. **"Guardrail not significant" = safe.** Only an interval inside the margin shows
   safety.
4. **Immature lagged metrics.** Refunds and cancellations that take 30 days to show
   will look better than they are in a 14-day readout. Mark them immature.
5. **Segment mining.** The mobile-only "+14%" out of twelve segments is the expected
   false positive. Adjust and label it.
6. **Novelty read as a permanent lift.** Report the late-window effect separately.
7. **Presenting projected annual revenue as a measured result.** It multiplies a
   point estimate by assumptions. Tag it and give the range from the interval.
8. **A significant result smaller than the MDE.** It may be real but too small to act
   on. Say whether it clears the threshold the business set.

## Example Output

```
# Experiment readout — Annual-plan default on pricing page   Dates: 2026-09-01 → 09-14

## Decision
Hold at current allocation until the refund window matures (2026-10-14), then
decide. The primary metric wins, but the refund guardrail exceeds its margin and
is not yet mature.

## Gates
| Gate | Check | Result | Pass? |
|---|---|---|---|
| 1 SRM | 50,120 vs 49,880 (50/50) | χ² = 0.58, p = 0.45 | Pass |
| 2 Integrity | 14 days, 100k planned; no early stop; no mid-test change | as planned | Pass |
| 3 Primary | 14-day paid conversion | see below | Pass |
| 4 Guardrails | 30-day refund rate among converters | margin exceeded | **Fail (immature)** |
| 5 Novelty | effect by exposure day | decays | Caution |
| 6 Multiplicity | 4 secondaries, 3 segments | Holm applied | Pass |

## Primary metric (two-proportion z-test)
| Arm | n | Paid conversion | Δ abs [95% CI] | Δ rel | vs MDE (0.30 pts) |
|---|---|---|---|---|---|
| Control | 50,120 | 5.00% (2,506) | | | |
| Annual default | 49,880 | 5.40% (2,693) | +0.40 pts [+0.12, +0.68] | +8.0% | point above, lower bound below |

## Guardrails
| Guardrail | Margin | Δ [95% CI] | Pass? | Mature? |
|---|---|---|---|---|
| Refund rate (converters) | +1.0 pt | 4.1% → 5.6%: +1.5 pts [+0.3, +2.7] | Fail | No — 30-day window closes for last users on 10-14 |
| Support tickets / 1k users | +0.5 | +0.1 [−0.3, +0.5] | Pass | Yes |

## Novelty / time trend
Days 1–3 of exposure: +0.62 pts. Days 8–14: +0.28 pts [−0.05, +0.61]. The effect
roughly halves and its late-window interval includes zero.

## Secondaries and segments (exploratory)
| Metric / segment | Δ | Raw p | Holm p | Label |
|---|---|---|---|---|
| Mobile paid conversion | +14% rel | 0.011 | 0.077 | Exploratory, not significant after adjustment |
| Avg first-invoice value | +22% | <0.001 | <0.001 | Expected: annual plans bill 12 months |

## Measured vs inferred
Measured: +0.40 pts paid conversion; +1.5 pts refunds among converters (immature).
Net of refunds: 4.79% → 5.10% (+0.31 pts) [measured, immature].
Inferred: "+$410k annual bookings" [inference — point estimate × traffic forecast;
the lower CI bound gives ~$120k; excludes refund growth].

## What would reverse this decision
Refund increase still above +1.0 pt once mature, or net-of-refund lift CI including zero → don't ship.

## Confidence: Medium
```

## Techniques Used

- **QA-08 Gate-Based Verification** — six ordered gates, each of which can stop the readout.
- **RT-05 Evidence-Based Reasoning** — every claim carries counts, an interval, and the test used.
- **QA-04 Uncertainty Acknowledgment** — measured vs inferred, confidence, and reversal conditions.
- **QA-02 Adversarial Stress-Test** — the decision is tested at the lower CI bound, under novelty, and against a worsening lagged guardrail.
- **AG-08 Evidence-Based Decision Gates** — guardrails pass only on an interval inside a stated margin.

## Related Prompts

- `domain-data-analytics/framing-and-metrics/analytics_metric_definition_spec.md` — specify the primary and guardrail metrics.
- `domain-AI-ML/model-evaluation-validation/mleval_ab_test_design_for_models.md` — the ML-model version of experiment design.
- `domain-agentic-resources/skills/marketing/ab-test-setup/SKILL.md` — test design and sample size before launch.
