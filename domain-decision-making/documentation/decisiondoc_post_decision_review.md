---
title: "Post-Decision Review — Calibration Against Prior Expectations"
category: decision-making/documentation
description: "Run at a pre-committed checkpoint (e.g., 6 months after a hire, 1 year after a major decision), this review compares the actual outcome to what you predicted at decision time — not merely to 'good vs bad.' Because hindsight makes most outcomes look obvious, the review forces an honest comparison against the original calibrated expectations: predicted vs actual, calibration delta, surprises, and calibration lessons for future decisions of the same type. Counters hindsight bias and outcome bias by anchoring to recorded forecasts."
techniques:
  - ST-01
  - ST-02
  - RT-02
  - DS-01
  - CM-02
  - QA-01
difficulty: intermediate
tags:
  - decision-documentation
  - post-decision-review
  - calibration
  - hindsight-bias
  - forecasting
updated: "2026-05-10"
reasoning:
  styles: [calibration, retrospective, bayesian]
  stakes: variable
  horizon: months
  uncertainty: risk
  evidence_quality: moderate
  domain_complexity: variable
  collaboration: solo_or_team
  output_format: structured
  user_role: [pm, executive, founder, manager, individual, analyst]
  mode: [audit, forecast, document]
related_prompts:
  - domain-decision-making/documentation/decisiondoc_after_action_report.md
  - domain-decision-making/documentation/decisiondoc_options_memo.md
  - domain-reasoning-craft/reasoning-moves/reasoning_bayesian_belief_update.md
---

# Post-Decision Review

**Objective:** At a **pre-committed checkpoint** — six months after a hire, a year after a strategic decision, a quarter after a launch — compare the actual outcome to **what you predicted at decision time**, not merely to a vague "good or bad." The discipline is **calibration against recorded expectations.** Hindsight makes almost every outcome look like it was obvious all along, which quietly destroys the lessons a review should produce. By anchoring to the *predictions you actually made* (ideally written down in the original options memo, log entry, or forecast), this review measures the gap between expectation and reality, distinguishes outcomes you genuinely foresaw from ones you got right by luck or wrong despite good reasoning, and extracts **calibration lessons** that improve future decisions of the same type.

This is the complement to `decisiondoc_after_action_report.md`. The AAR asks "was the decision sound and what's transferable?" This review asks "how well-calibrated were my predictions, and how do I forecast better next time?"

**When to use:**
- A decision had a checkpoint set at decision time ("revisit in 6 months") and that checkpoint has arrived.
- A hire, investment, bet, or strategy is now far enough along to compare outcome to forecast.
- You want to improve your forecasting/calibration as a decision-maker, not just record what happened.
- Recurring decision types (hiring, vendor selection, project sizing) where calibration compounds across instances.

**When NOT to use:**
- No predictions were recorded at decision time and none can be honestly reconstructed — calibration needs a prior to compare against. (If you can reconstruct the prior honestly, proceed; if reconstruction would be fiction, do an AAR instead.)
- You want decision-quality and transferable-lessons analysis — use the after-action report.
- The decision is too recent for the outcome to be legible.

**Audience:** PMs, executives, founders, managers, analysts, and individuals improving their calibration on recurring decision types.

---

## Inputs / Context

1. **The decision** and its decision date.
2. **The predictions made at decision time** — expected outcomes, ideally with probabilities, ranges, or confidence levels. Pull from the original memo/log/forecast if available.
3. **The pre-committed checkpoint** — when this review was scheduled, and why that interval.
4. **Actual outcomes** at the checkpoint, with evidence.
5. **The decision type** — so calibration lessons can be filed against a recurring class.

---

## Constraints

### Must
- Anchor to the **predictions recorded at decision time.** If they were probabilistic or ranged, compare on that basis. If only qualitative, reconstruct the prediction honestly and label it reconstructed.
- For each prediction, state **predicted vs actual** and the **calibration delta** (over-optimistic / over-pessimistic / well-calibrated; for probabilistic claims, whether the event landed inside or outside the stated range/confidence).
- Separate **foreseen** outcomes (predicted and occurred) from **surprises** (occurred but unpredicted) and **non-events** (predicted but didn't occur).
- Diagnose the **direction of miscalibration** — does this decision-maker, on this decision type, tend to be over-confident, over-optimistic on timelines, over-pessimistic on risk, etc.?
- Produce **calibration lessons** filed against the **decision type**, phrased to adjust future forecasts ("on hires, I'm consistently 3 months optimistic on ramp — pad next estimate").
- Distinguish **prediction error** (the forecast was wrong) from **decision error** (the choice was wrong) — they're different. A well-reasoned decision can have a badly-calibrated forecast attached, and you fix the forecast, not necessarily the decision.

### Must Not
- Grade against "did it turn out well" instead of "did it match the forecast." A pleasant surprise is still a calibration miss.
- Let hindsight rewrite the original prediction ("I always knew it would go this way"). Use the recorded prior; flag reconstruction.
- Treat a within-range outcome as a miss, or an outside-range outcome as a hit, because of how it *felt*. Calibration is mechanical: did reality land where the forecast said it would?
- Confuse a lucky-but-unforecast good outcome with good calibration. It's a surprise; log it as one.
- Produce lessons untethered from a decision type. Calibration compounds only when filed against a recurring class.
- Reopen the decision-quality debate here — that's the AAR's job. Stay on calibration.

---

## Instructions

### Step 1 — Recover the original predictions
Pull the predictions made at decision time. For each: the predicted outcome, with probability/range/confidence if it existed. If only qualitative existed, reconstruct honestly and mark `[reconstructed]`.

### Step 2 — Record actual outcomes
At the checkpoint, the actual result for each predicted dimension, with evidence. Neutral.

### Step 3 — Compare predicted vs actual per dimension
For each: predicted, actual, and whether the actual landed where the prediction said (inside range / matched / over / under). This is the calibration measurement.

### Step 4 — Classify each result
- **Foreseen:** predicted and occurred (calibration hit).
- **Surprise:** occurred but not predicted (calibration miss — even if pleasant).
- **Non-event:** predicted but didn't occur (calibration miss).

### Step 5 — Diagnose miscalibration direction
Across the dimensions, is there a pattern? Over-optimistic on upside, over-confident on certainty, under-weighting tail risk, optimistic on timelines? Name the systematic tilt.

### Step 6 — Separate prediction error from decision error
State plainly: was the forecast miscalibrated, the decision wrong, both, or neither? A sound decision with a miscalibrated forecast means fix the forecasting habit, not the decision process.

### Step 7 — Calibration lessons (filed by decision type)
For the decision type, the adjustment for next time: the systematic correction to apply to future forecasts of this class. Quantified where possible ("pad hire-ramp estimates by ~3 months").

### Step 8 — Next checkpoint (if ongoing)
If the decision is still unfolding, set the next pre-committed checkpoint and what to predict for it now (so the next review has a fresh prior).

---

## False-Positive Prevention

1. **Outcome-grading.** Scoring "did it go well" instead of "did it match the forecast." A good surprise is a calibration miss — log it as one.
2. **Hindsight rewrite.** "I always knew." Anchor to the recorded prediction; mark any reconstruction as reconstructed and treat it skeptically.
3. **Feel-based scoring.** Calling a miss a hit because the outcome was pleasant. Calibration is mechanical: did reality land in the predicted region?
4. **Lucky-hit laundering.** Treating an unforecast good outcome as evidence of good calibration. It's a surprise, not a hit.
5. **Prediction/decision conflation.** Blaming the decision for a forecast error (or vice versa). Separate the two; they have different fixes.
6. **Untyped lessons.** Calibration notes not filed against a recurring decision class. They compound only when typed.
7. **Range gaming.** Retroactively widening the original range to claim the outcome was "in range." Use the range as recorded.
8. **Decision-quality drift.** Re-litigating whether the decision was right here. That's the AAR; this review stays on calibration.

---

## Output Format

```
# Post-Decision Review — [decision]
**Decided:** [date]   |   **Checkpoint:** [date, pre-committed interval]   |   **Decision type:** [class]

## Predictions made at decision time
| # | Predicted outcome | Probability / range / confidence | Source [recorded/reconstructed] |
|---|-------------------|----------------------------------|---------------------------------|
| 1 | [...]             | [e.g., 70% / 6–9 months / high]  | recorded                        |
| 2 | [...]             | [...]                            | [reconstructed]                 |

## Actual outcomes at checkpoint
| # | Actual outcome | Evidence |
|---|----------------|----------|
| 1 | [...]          | [...]    |

## Predicted vs actual (calibration)
| # | Predicted | Actual | Landed where predicted? | Delta (over/under/calibrated) |
|---|-----------|--------|-------------------------|-------------------------------|
| 1 | [...]     | [...]  | inside range / matched / no | [...]                     |

## Classification
- **Foreseen (hits):** [...]
- **Surprises (occurred, unpredicted):** [...]
- **Non-events (predicted, didn't occur):** [...]

## Miscalibration direction
- Systematic tilt on this decision type: [over-optimistic timelines / over-confident / under-weighted tail risk / well-calibrated]

## Prediction error vs decision error
- Forecast miscalibrated? [yes/no — how]
- Decision wrong? [yes/no — but defer full decision-quality analysis to the AAR]

## Calibration lessons (filed under: [decision type])
- [adjustment for future forecasts of this type — quantified where possible]

## Next checkpoint (if ongoing)
- Date: [...]
- Predictions to test then (set now): [...]
```

---

## Verification

- [ ] Compared to recorded decision-time predictions, not to "good vs bad."
- [ ] Reconstructed predictions (if any) marked as such and treated skeptically.
- [ ] Predicted vs actual stated per dimension with a calibration delta.
- [ ] Results classified as foreseen / surprise / non-event.
- [ ] Surprises (including pleasant ones) counted as calibration misses.
- [ ] Systematic miscalibration direction diagnosed for the decision type.
- [ ] Prediction error separated from decision error.
- [ ] Calibration lessons filed against a recurring decision type, quantified where possible.
- [ ] Original ranges used as recorded (no retroactive widening).
- [ ] Next checkpoint and fresh predictions set if the decision is ongoing.
