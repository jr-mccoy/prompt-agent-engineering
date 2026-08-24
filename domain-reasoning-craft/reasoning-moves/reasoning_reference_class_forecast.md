---
title: "Reference-Class Forecasting — Outside-View Base Rate Discipline"
category: reasoning-craft/reasoning-moves
description: "Force an outside-view forecast by selecting an explicit reference class for an event or project, deriving its base rate, and then making case-specific adjustments only after the base rate is locked. Counters planning fallacy and inside-view optimism by anchoring on what comparable cases actually did."
techniques:
  - ST-01
  - ST-02
  - RT-02
  - DS-01
  - CM-02
  - QA-01
difficulty: intermediate
tags:
  - reasoning
  - forecasting
  - outside-view
  - base-rate
  - planning-fallacy
updated: "2026-05-10"
reasoning:
  styles: [inductive, probabilistic, analogical]
  stakes: variable
  horizon: months_to_years
  uncertainty: ambiguity
  evidence_quality: variable
  domain_complexity: variable
  collaboration: solo
  output_format: structured_table_plus_estimate
  user_role: [planner, analyst, founder, project_manager, forecaster]
  mode: [forecast, audit]
related_prompts:
  - domain-reasoning-craft/reasoning-moves/reasoning_bayesian_belief_update.md
  - domain-reasoning-craft/reasoning-moves/reasoning_outside_view_inside_view.md
  - domain-reasoning-craft/forecasting/forecasting_super_forecaster_decomposition.md
---

# Reference-Class Forecasting

**Objective:** Produce a forecast (cost / duration / success rate / outcome distribution) by first locking in the outside view: pick an explicit reference class of comparable past cases, derive their base rate, and only then layer case-specific adjustments. Resist the temptation to start from the inside view ("here's why this case is different") because that is where planning fallacy lives.

**When to use:**
- A project, launch, deal, or decision has a forecast attached (cost, time, success probability) and you want it grounded in what comparable efforts actually did.
- You suspect the inside view is over-optimistic (almost always true for self-generated estimates).
- You are advising someone whose forecast you want to stress-test against history.

**When NOT to use:**
- The case is genuinely without precedent (radically novel domain). Reference-class forecasting still helps, but flag it: any reference class will be loose.
- You only need a directional answer, not a quantified one. Use a faster heuristic.
- The forecast is for an event whose base rate is already common knowledge in the user's domain. Skip to adjustment.
- No computable statistical base rate exists and the work is qualitative reference-class comparison plus reconciliation — use `reasoning_outside_view_inside_view.md` instead.

**Audience:** Project managers, founders, analysts, planners, forecasters, anyone whose estimates routinely come in optimistic.

---

## Inputs / Context

1. **The forecast question.** Phrased as a measurable outcome with a deadline (e.g., "Will this 12-month migration finish on time and under $400K?").
2. **The case at hand.** Brief description: scope, team, environment, anything load-bearing.
3. **The user's current estimate.** What they would forecast if asked right now. We collect this *first* so it can be compared against the outside view, not contaminate it.
4. **Available information about prior comparable cases.** Studies, post-mortems, internal data, public benchmarks. If none, say so — the prompt then operates on the user's recall.
5. **Domain expertise.** Is the user expert enough to identify comparable cases, or do they need help defining the reference class?

---

## Constraints

### Must
- Capture the user's inside-view estimate **before** doing reference-class work, sealed off from the outside-view computation.
- Define the reference class explicitly: criteria for inclusion, criteria for exclusion, and at least 5 example cases (or fewer if the domain is small, with a note on small-N risk).
- Report the base rate as a distribution if possible (median, P25, P75) — not a single point estimate.
- Make adjustments to the base rate explicit and individually justified. Each adjustment names which feature of the case differs from the reference class and by how much it shifts the estimate.
- End with a final forecast that is the base rate ± documented adjustments, plus the user's inside view next to it.
- Flag the gap between inside view and outside view. Large gaps mean the user is either drawing on private information the reference class doesn't capture, or is committing planning fallacy.

### Must Not
- Build a reference class so narrow that only one or two cases qualify. A class of N=2 has no statistical purchase.
- Define the reference class to match the user's lean ("projects similar to mine" → "successful projects similar to mine").
- Apply more than 3–4 adjustments. Adjustment cascades destroy the discipline.
- Replace the base rate with the inside view. The inside view is for sanity-checking the outside view, not the other way around.
- Compute spurious precision from sparse data. With N=5, report rounded ranges.

---

## Instructions

### Step 1 — Capture the inside view (sealed)
Ask the user for their current best estimate. Record it. Do not let this number influence the next steps.

### Step 2 — Define the reference class
- Inclusion criteria (3–6 features that make a case comparable).
- Exclusion criteria (1–3 features that disqualify a case).
- Tradeoff: tight class = more comparable but smaller N; loose class = larger N but noisier base rate. Pick a middle ground and state which way you erred.

### Step 3 — Populate the reference class
List actual cases (5–20 if possible). For each, record the outcome on the forecast variable (cost, duration, success/failure, etc.). If the user can only name 2–3, draw on widely-cited benchmarks for the rest, attributed.

### Step 4 — Compute the base-rate distribution
- Median outcome
- 25th and 75th percentile (or min/max if N is small)
- Hit rate (% of cases that met some standard threshold)

### Step 5 — Identify case-specific adjustments
List 2–4 features of the current case that differ materially from the reference-class median. For each, state:
- The feature
- Which direction it moves the estimate (better / worse)
- A rough magnitude (small: ±10%, medium: ±30%, large: ±50%+)
- Why this adjustment is justified by mechanism, not by hope

### Step 6 — Compute the adjusted outside-view forecast
Start from the base-rate median. Apply each adjustment. Report the new central estimate and a range that widens with the adjustments.

### Step 7 — Compare inside view vs outside view
Place them side by side. Compute the gap. Three patterns:
- **Inside ≈ outside:** the user's intuition is calibrated against history. Trust it more.
- **Inside << outside (more optimistic):** classic planning fallacy. Recommend the outside view, or force the user to name the private information that justifies the gap.
- **Inside >> outside (more pessimistic):** rarer; either the user has private bad-news information, or they're discounting their own competence relative to peers. Probe.

### Step 8 — Final forecast and confidence
State the final forecast as a range with explicit P50 / P75 / P90 (or min / median / max if data is sparse). State which view it is anchored on and why.

---

## False-Positive Prevention

1. **Class-of-one trap.** "There's nothing else like this project." Often false. Push for at least 5 comparable cases even if the analogy is loose; loose comparables are still better than zero outside view.
2. **Reference-class gerrymandering.** The user (or you) may be tempted to define the class to support the desired conclusion. Test by asking: "Would I have defined this class the same way before knowing what I wanted to forecast?"
3. **Survivorship in the class.** If the only available comparable cases are the ones that got written up, the base rate is biased toward success. Note this.
4. **Adjustment-stacking.** Each "this case is different" adjustment increases variance. After 4 adjustments, you've effectively abandoned the outside view. Cap at 4 and prefer fewer.
5. **Inside-view contamination.** The inside-view estimate is captured first and sealed by design; the failure is looking at or adjusting toward that sealed number while defining the class or computing the base rate. The seal only works if the base rate is built blind to it.
6. **Optimism leak in adjustments.** If all 3–4 adjustments push in the same direction (better outcome), that's a signal of motivated reasoning. Force at least one adjustment in the opposite direction or admit the case may be unusually advantaged.

---

## Output Format

```
# Reference-class forecast — [forecast question]

## Inside view (captured first)
- User's current estimate: [value]
- Stated reasoning: [one sentence]

## Reference class
- Inclusion criteria: [bullets]
- Exclusion criteria: [bullets]
- Class width tradeoff: [tighter / looser, with note]

## Cases
| # | Case                       | Outcome on forecast variable | Source        |
|---|----------------------------|------------------------------|---------------|
| 1 | [name]                     | [value]                      | [source]      |
| … |                            |                              |               |

## Base rate
- Median outcome: [value]
- P25 / P75: [values]
- Hit rate (met threshold X): [%]
- N: [number]
- Caveats: [survivorship / small-N / source quality]

## Case-specific adjustments
| Feature differing from class median | Direction | Magnitude | Mechanism |
|-------------------------------------|-----------|-----------|-----------|
| [feature]                           | better    | +20%      | [why]     |
| …                                   |           |           |           |

## Outside-view forecast (adjusted)
- Central estimate: [value]
- Range (P25–P75): [low – high]

## Inside vs outside
- Inside view:  [value]
- Outside view: [value]
- Gap: [size and direction]
- Interpretation: [calibrated / planning-fallacy / pessimism / private-info]

## Final forecast
- P50: [value]
- P75: [value]
- P90: [value]
- Anchored on: [outside view / blended] — because [reason]
```

---

## Verification

- [ ] Inside view was captured before reference-class work began.
- [ ] Reference class has explicit inclusion + exclusion criteria.
- [ ] At least 5 cases listed (or N stated and small-N risk flagged).
- [ ] Base rate reported as a distribution, not a point.
- [ ] Adjustments are 2–4 in count, individually justified by mechanism.
- [ ] Inside-view vs outside-view gap is named and interpreted.
- [ ] Final forecast is a range with P50/P75/P90 (or equivalent under sparse data).
- [ ] No silent re-anchoring on the inside view.
- [ ] All adjustments don't push in the same direction without explicit justification.
