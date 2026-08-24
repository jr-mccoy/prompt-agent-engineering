---
title: "Selective Prediction and Abstention Design"
category: AI-ML/model-evaluation-validation
description: "Design when a model should decline to predict — deriving the abstention threshold from the cost of a wrong answer versus the cost of the fallback, sizing the deferral load against real capacity, and measuring whether the humans receiving deferrals do better than the model would have."
techniques:
  - DS-02
  - RT-02
  - CM-02
  - QA-12
  - DS-06
difficulty: advanced
tags:
  - selective-prediction
  - abstention
  - human-in-the-loop
  - deferral
  - risk-coverage
updated: "2026-08-22"
related_prompts:
  - domain-AI-ML/model-evaluation-validation/mleval_uncertainty_quantification_design.md
  - domain-AI-ML/model-evaluation-validation/mleval_conformal_prediction_design.md
  - domain-AI-ML/model-evaluation-validation/mleval_ood_detection_design.md
  - domain-AI-ML/agentic-ai-systems/aiagent_human_in_the_loop_design.md
---

# Selective Prediction and Abstention Design

**Objective:** Decide when a model should decline to answer — deriving the threshold from the cost of a wrong answer against the cost and capacity of the fallback, and then verifying the assumption the whole design rests on: that whoever or whatever receives the deferred cases actually does better than the model would have.

**When to Use:**
- A fallback path exists — a human reviewer, a simpler model, a manual process — and you must decide what reaches it.
- Confident errors are expensive and the system currently answers everything.
- An abstention mechanism exists but its threshold was set by intuition and never validated.

**When NOT to Use:**
- There is no fallback; abstention with nowhere to send the case is a refusal, not a design.
- The question is how to produce the confidence signal — use `mleval_uncertainty_quantification_design.md` first.
- The deferral target is a human approving an agent's action — use `../agentic-ai-systems/aiagent_human_in_the_loop_design.md`.

## Inputs / Context

- **Fallback path** — who or what handles deferred cases, their capacity per period, and their turnaround time.
- **Fallback accuracy** — how well the fallback performs on the cases it would receive. Frequently unmeasured, and the design's central assumption.
- **Cost of a model error** — by error type, since false positives and false negatives rarely cost the same.
- **Cost of a deferral** — reviewer time, latency, and any user-visible delay.
- **Confidence signal available** — calibrated probability, uncertainty estimate, conformal set size, or OOD flag.
- **Coverage requirement** — any floor on the fraction of cases the model must handle automatically for the system to be worth running.

## Constraints

**Must:**
- Verify that the fallback is **better than the model on the deferred cases specifically**. Deferring to a reviewer who is worse on hard cases makes the system worse while appearing more cautious — this is the design's central and most-skipped check.
- Derive the threshold from the cost of an error versus the cost of a deferral, and report the resulting coverage and selective risk at that point.
- Size the deferral volume against the fallback's real capacity, including peaks, not the average.
- Report a risk–coverage relationship rather than a single accuracy figure, so the trade is visible.
- Define what happens when the fallback is saturated — this is a design decision, not an incident.

**Must Not:**
- Report accuracy on the covered cases only and present it as system accuracy; a model that answers 40% of cases at 99% accuracy is not a 99%-accurate system.
- Assume the human fallback is more accurate; measure it on comparable cases, or state clearly that the assumption is unverified.
- Assert deferral-rate norms, risk–coverage results, or human-accuracy figures from memory; mark quantities `[measure on your data]`.
- Set the threshold from a round confidence number rather than from the cost ratio.
- Ignore what deferral does to latency where the user is waiting.

**Instructions:**

1. **Map the fallback.** Who or what receives deferrals, capacity per period including peak, turnaround time, and the cost per case. If the fallback is a human team, get the real number, not the headcount.

2. **Measure fallback accuracy on hard cases — the decisive step.** Take cases the model would defer and measure how the fallback performs on those specifically. General reviewer accuracy on all cases is not the relevant quantity; deferred cases are hard by construction. If this cannot be measured, say so plainly and treat the entire design as resting on an unverified assumption.

3. **Choose the confidence signal.** Calibrated probability, uncertainty estimate, conformal set size, or an OOD flag — or a combination, where different signals catch different failure types. State what each contributes.

4. **Build the risk–coverage curve.** For a range of thresholds, plot selective risk against coverage. This curve is the design's central artifact; it shows what each increment of caution costs in automation.

5. **Derive the threshold from costs.** Combine the cost of each error type, the cost of a deferral, and the fallback's accuracy on deferred cases. The optimum is where the marginal error avoided stops being worth the marginal deferral — and if fallback accuracy on hard cases is close to the model's, that point may be "defer nothing", which is a legitimate finding.

6. **Check capacity, including peaks.** Deferral volume at the chosen threshold against real capacity at peak. If it does not fit, adjust the threshold, stage the rollout, or expand capacity — but state which, rather than shipping a threshold the fallback cannot absorb.

7. **Design saturation behaviour.** When deferrals exceed capacity: queue with a stated maximum wait, raise the threshold temporarily and record that the system is operating in a degraded mode, or fail closed. Decide in advance, and make the degraded mode visible.

8. **Check abstention fairness.** Report deferral rate by subgroup. A model that abstains disproportionately on one group delivers a systematically slower or different service to that group, which is a fairness issue even when accuracy looks even.

9. **Define monitoring.** Coverage drift, selective risk drift, fallback accuracy over time, and queue depth. Falling fallback accuracy is the signal that quietly invalidates the design.

**Output Format:**

A markdown design:
- **Fallback Map** — who, capacity (mean and peak), turnaround, cost per case.
- **Fallback Accuracy on Deferred Cases** — measured, or declared unverified.
- **Confidence Signal** — chosen signals and what each contributes.
- **Risk–Coverage Curve** — table or description across thresholds.
- **Threshold Derivation** — cost inputs, chosen point, resulting coverage and selective risk.
- **Capacity Check** — volume at threshold vs peak capacity.
- **Saturation Behaviour** — the defined response.
- **Abstention Fairness** — deferral rate by subgroup.
- **Monitoring** — signals and the degradation each reveals.

## Verification

- [ ] Fallback accuracy is measured on the cases that would be deferred, or explicitly declared unverified.
- [ ] The risk–coverage relationship is reported, not a single accuracy number.
- [ ] Covered-case accuracy is never presented as system accuracy.
- [ ] The threshold follows from the cost ratio and the fallback's measured accuracy.
- [ ] Deferral volume is checked against peak capacity, not average.
- [ ] Saturation behaviour is defined in advance.
- [ ] Deferral rate is reported by subgroup.
- [ ] Monitoring includes fallback accuracy over time.
- [ ] No deferral norms or human-accuracy figures are asserted from memory.

## False-Positive Prevention

❌ **DON'T:**
- Report "99.2% accuracy" for a model that abstains on 40% of cases; that is the accuracy of the easy 60%, and the system's accuracy includes what the fallback does with the rest.
- Assume reviewers outperform the model on deferred cases — deferred cases are hard by construction, and general reviewer accuracy is measured on a mix dominated by easy ones.
- Set the threshold at a round confidence value; the cost ratio, not the number's tidiness, determines where it belongs.
- Size deferrals against average capacity and discover the queue at month-end peak.
- Ship without a saturation plan, so the first overload becomes an incident rather than a designed degraded mode.
- Ignore subgroup deferral rates — a group that is deferred twice as often waits twice as long, whatever the accuracy table says.

✅ **DO:**
- Measure the fallback on hard cases specifically, and accept "defer nothing" as a legitimate outcome if it is not better.
- Publish the risk–coverage curve so the cost of caution is visible to whoever sets the threshold.
- State system accuracy as the combination of covered and deferred paths.
- Check peak capacity and stage the rollout if it does not fit.
- Define the degraded mode in advance and make it observable.
- Track fallback accuracy over time; its decline invalidates the design silently.

## Example Output

```markdown
## Abstention Design: Invoice Coding Automation
Model assigns GL codes to supplier invoices; low-confidence invoices go to the AP team.

### Fallback Map
| Attribute | Value |
|---|---|
| Fallback | AP team, 6 FTE |
| Capacity | ~340 invoices/day sustained; **~180/day at month-end** (other duties peak) |
| Turnaround | same day normally; 2 days at month-end |
| Cost per deferral | ~4 minutes of AP time |

### Fallback Accuracy on Deferred Cases — the decisive measurement
Sampled 200 invoices the model would defer at a candidate threshold and had them coded blind by
AP, then adjudicated by the finance controller.
| Coder | Accuracy on these hard cases |
|---|---|
| Model (had it not abstained) | `[measure]` |
| AP team | `[measure]` |

**This comparison decides whether the design is worth building at all.** If AP is not
meaningfully better on these specific invoices, deferring them adds cost and delay without
improving accuracy, and the correct output of this prompt is "do not abstain; invest in the
model instead". General AP accuracy across all invoices is not the relevant number — it is
dominated by the easy ones the model would never defer.

### Confidence Signal
Combination, because the failure types differ:
- **Calibrated probability** — catches genuinely ambiguous invoices (aleatoric).
- **OOD flag on supplier identity** — catches new suppliers absent from training, where the
  probability is often confidently wrong.
Either signal firing defers. Using probability alone would miss the new-supplier case entirely,
which is the one finance most cares about.

### Risk–Coverage Curve
| Threshold | Coverage | Selective risk (error on covered) | Deferrals/day |
|---|---|---|---|
| 0.50 | `[measure]` | `[measure]` | `[measure]` |
| 0.70 | `[measure]` | `[measure]` | `[measure]` |
| 0.85 | `[measure]` | `[measure]` | `[measure]` |
| 0.95 | `[measure]` | `[measure]` | `[measure]` |

### Threshold Derivation
A miscoded invoice costs a correction cycle plus month-end reconciliation effort; a deferral
costs ~4 minutes. The ratio favours deferring, but only to the extent AP is actually better —
so the threshold is bounded by the measured gap above, not by the cost ratio alone.

### Capacity Check
The binding constraint is **month-end (~180/day)**, not the sustained figure. A threshold sized
to normal capacity will overflow exactly when invoice volume peaks and AP has least slack.
Sizing against 180/day, not 340/day, is the difference between a working design and a
predictable month-end incident.

### Saturation Behaviour
Queue with a 1-day maximum wait. Beyond that, the threshold **automatically raises** to the
next tier and the system enters a **declared degraded mode**: a banner on the AP dashboard, and
the affected invoices tagged for post-hoc sampling. Auto-coding more invoices at lower
confidence is an accepted, visible trade — not a silent one.

### Abstention Fairness
Deferral rate by supplier segment:
| Segment | Deferral rate |
|---|---|
| Large established suppliers | `[measure]` |
| **Small / new suppliers** | `[measure — expected higher]` |
| Foreign-currency invoices | `[measure]` |

Small and new suppliers will defer more often, so they get paid more slowly. That is a real
business consequence of an accuracy-driven threshold, and it belongs in front of finance rather
than buried in a fairness appendix.

### Monitoring
- Coverage and selective risk, weekly.
- **AP accuracy on deferred invoices, quarterly** — if it declines, the design's premise has
  failed and the threshold should move regardless of what the model is doing.
- Queue depth and days in degraded mode.
- Deferral rate by supplier segment, monthly.
```

**Techniques Used:**
- **DS-02 (Metric Specification):** selective risk, coverage, and fallback accuracy are defined together as the joint acceptance criterion.
- **RT-02 (Multi-Dimensional Analysis Framework):** threshold × coverage × capacity × subgroup is the design grid.
- **CM-02 (Constraint Specification):** the measure-the-fallback rule and the never-report-covered-accuracy-as-system-accuracy rule bound what may be claimed.
- **QA-12 (False Positives Identification):** rejects the assumption that a human fallback is better on hard cases.
- **DS-06 (Prioritization and Severity Guidance):** cost asymmetry by error type drives where the threshold lands.

**Related Prompts:**
- `mleval_uncertainty_quantification_design.md` — produces the confidence signal this consumes.
- `mleval_conformal_prediction_design.md` — set size as an alternative abstention trigger.
- `mleval_ood_detection_design.md` — the novelty signal in the combined trigger above.
- `../agentic-ai-systems/aiagent_human_in_the_loop_design.md` — the agent-action counterpart.
