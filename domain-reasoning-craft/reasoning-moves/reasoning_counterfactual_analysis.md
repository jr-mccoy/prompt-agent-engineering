---
title: "Counterfactual Analysis — Construct and Stress-Test 'What Would Have Happened Instead'"
category: reasoning-craft/reasoning-moves
description: "Construct a disciplined counterfactual: identify the antecedent that would have to change, hold the rest of the world fixed (or model what else would shift), trace the causal chain, and stress-test the result. Used for attribution ('did action X cause outcome Y?'), credit assignment, regret analysis, and policy evaluation."
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
  - counterfactual
  - causal-reasoning
  - attribution
  - what-if
updated: "2026-05-10"
reasoning:
  styles: [counterfactual, causal, simulation]
  stakes: variable
  horizon: variable
  uncertainty: deep
  evidence_quality: variable
  domain_complexity: variable
  collaboration: solo
  output_format: causal_chain
  user_role: [analyst, strategist, executive, policy, founder, individual]
  mode: [audit, synthesize]
related_prompts:
  - domain-reasoning-craft/reasoning-moves/reasoning_first_principles_reconstruction.md
  - domain-reasoning-craft/systems/systems_unintended_consequence_scan.md
  - domain-decision-making/decisioning_regret_minimization.md
---

# Counterfactual Analysis

**Objective:** Construct a disciplined "what would have happened instead" analysis. Identify the precise antecedent change, decide what else would shift along with it (the realistic counterfactual world) versus what is held fixed (the idealized "ceteris paribus" version), trace the causal chain to the new outcome, and stress-test against alternative counterfactual paths. Used to attribute causation, assign credit/blame, evaluate decisions in hindsight, and project the value of past or future interventions.

**When to use:**
- Attribution: "Did our marketing campaign cause the revenue lift, or would it have happened anyway?"
- Credit / blame: "Did the new manager turn the team around, or would the prior trajectory have done it?"
- Regret / post-decision review: "If I had taken the other job, where would I be?"
- Policy evaluation: "What would have happened without this regulation?"
- Investment ex-post: "Was this a good bet given what was knowable then?"

**When NOT to use:**
- The question can be answered by direct evidence rather than counterfactual reasoning. (E.g., a randomized experiment was run — use the data.)
- The system is so complex and chaotic that a counterfactual is fully indeterminate. Acknowledge and stop.
- The user wants to relitigate a closed decision for emotional reasons; a counterfactual will not resolve that. Use a regret-minimization or post-decision-review prompt instead.

**Audience:** Analysts, strategists, policy people, executives, founders, individuals doing post-decision review.

---

## Inputs / Context

1. **The actual outcome.** What happened, in concrete terms with dates and magnitudes.
2. **The antecedent action / event.** What you want to imagine differently.
3. **The proposed counterfactual.** What you imagine happening instead. ("We didn't run the campaign", "I took job B", "the regulation didn't pass".)
4. **What else would have shifted.** Other variables that would plausibly co-move with the change. Most counterfactual errors come from forgetting these.
5. **Time horizon.** How far downstream are you tracking effects? (Days, months, years.)
6. **Standard of evidence.** What would a skeptic require to accept your counterfactual? (Comparable cases, mechanism, dose-response, etc.)

---

## Constraints

### Must
- Specify the counterfactual precisely. "We didn't do the campaign" is incomplete; specify what was done instead with the freed budget and time.
- Decide and label whether the counterfactual is **idealized** (only the named variable changes) or **realistic** (other variables co-shift). Different questions require different versions.
- Trace the causal chain step by step from the antecedent change to the new outcome, noting at each step what other variables enter.
- Identify points in the chain where the chain branches — different plausible counterfactual outcomes — and assign rough probabilities.
- Compare the counterfactual outcome distribution to the actual outcome to compute the *attribution* (how much of the actual outcome is plausibly due to the actual antecedent vs. would have happened anyway).
- Stress-test by constructing at least one *alternative* counterfactual that would have led to a similar outcome. If many counterfactuals lead to similar outcomes, the antecedent's contribution was small.

### Must Not
- Run a counterfactual where the antecedent change is impossible (would have required violating physics, time travel, or knowledge unavailable at the decision point).
- Hold "everything else equal" without checking whether anything else would plausibly have moved. Most real counterfactuals are joint counterfactuals.
- Treat the modeled counterfactual world as the only possible counterfactual world. There are many; sample several.
- Claim attribution from a single counterfactual run. Attribution requires comparing across counterfactual paths.
- Use counterfactual analysis to relitigate values disagreements ("if I had been a different person…"). Counterfactuals are about the world's response to a different input, not about being a different agent.

---

## Instructions

### Step 1 — Pin down the actual
Restate the actual outcome with date, magnitude, and the antecedent in question. One paragraph.

### Step 2 — Specify the counterfactual antecedent
Replace the antecedent with the counterfactual version. Be explicit about *what was done instead*. "Did not run campaign" → "Spent the budget on ABM instead" or "Banked the budget" or "Ran the campaign two months later". Each yields a different counterfactual world.

### Step 3 — Idealized vs realistic
Choose:
- **Idealized counterfactual:** only the named antecedent changes; everything else held fixed. Useful for isolating the specific mechanism's contribution. Often unrealistic.
- **Realistic counterfactual:** other variables co-shift in plausible ways. Useful for "what would have actually happened." Harder to specify precisely.

State which version you're running and why. Often you run both and compare.

### Step 4 — Trace the causal chain
Step by step, from antecedent change to new outcome:
- t=0: antecedent change
- t=1: immediate effects
- t=2: downstream effects
- t=3: secondary effects, behavior changes, market responses
- ...
- t=N: outcome at the specified horizon

At each step, note: what mechanism connects this step to the next? What else enters?

### Step 5 — Branch points
Where in the chain does the path realistically branch? At each branch, name the alternative paths and assign a rough probability. The counterfactual outcome is then a distribution, not a single value.

### Step 6 — Outcome distribution
- P25 outcome under counterfactual:
- P50 outcome:
- P75 outcome:

Compare to the actual outcome.

### Step 7 — Attribution computation
Attribution to the actual antecedent ≈ (actual outcome − P50 counterfactual outcome) / actual outcome — or expressed as "X% of the actual outcome is attributable to the antecedent; the rest would have happened under the counterfactual."

If the counterfactual P25–P75 range straddles the actual outcome, attribution is small or unreliable.

### Step 8 — Alternative counterfactual stress-test
Construct at least one different counterfactual antecedent (e.g., a different alternative action). If multiple plausible counterfactuals lead to similar outcomes, the actual antecedent had limited counterfactual leverage. If they diverge widely, attribution of the actual outcome to the actual antecedent becomes plausible.

### Step 9 — Verdict
- Attribution magnitude: small / moderate / large
- Confidence in the counterfactual: low / moderate / high (anchored on how much of the chain rested on speculation vs. well-modeled mechanisms, and assessed against the user's stated standard of evidence — would the named skeptic accept this counterfactual?)
- Decision implication: what does this attribution mean for the decision currently in front of the user (repeat the action / not / different version)?

---

## False-Positive Prevention

1. **The lonely counterfactual.** Reasoning from a single counterfactual world and claiming attribution. Always run at least 2–3.
2. **Fixed-everything illusion.** Holding everything else equal in a domain where the antecedent change would itself have triggered other changes (competitors respond, budgets reallocate, talent moves). Realistic counterfactuals require realistic co-shifts.
3. **Hindsight contamination.** Building the counterfactual using information that wasn't available at the decision point. Counterfactuals at the time of decision use only ex-ante information.
4. **Reversed-causation slip.** Confusing "X happened, then Y happened" with "X caused Y." Counterfactual reasoning is a tool to test causation, not to assume it.
5. **Magnitude inflation.** It is easy to construct dramatic counterfactual differences. The plausibility of the chain shrinks rapidly with each link; report a distribution and weight short-chain counterfactuals more heavily than long-chain ones.
6. **Identity counterfactuals.** "If I had been a more disciplined person…" is not a counterfactual about the world; it's a counterfactual about the agent. These are usually unproductive — they smuggle in a different person, then ask what they would have done.
7. **Single-mechanism tunneling.** Tracing only one causal mechanism while ignoring parallel ones. The chain section should explicitly invite alternative mechanisms.

---

## Output Format

```
# Counterfactual analysis — [topic]

## Actual world
- Outcome: [concrete, with date / magnitude]
- Antecedent in question: [action / event]

## Counterfactual antecedent
- Counterfactual: [precise description, including what was done instead]
- Mode: [idealized / realistic]
- Justification: [why this mode]

## Causal chain
| t  | Event                          | Mechanism                  | Other variables entering |
|----|--------------------------------|----------------------------|--------------------------|
| 0  | [antecedent change]            | —                          | —                        |
| 1  | [immediate effect]             | [mechanism]                | [others]                 |
| 2  | [downstream effect]            | [mechanism]                | [others]                 |
| …  |                                |                            |                          |

## Branch points
- Branch 1: at t=[n], path A vs B, probabilities [p / 1-p], reason [...]
- Branch 2: …

## Counterfactual outcome distribution
- P25: [value / description]
- P50: [value / description]
- P75: [value / description]
- Range straddles actual outcome? [yes / no]

## Attribution
- Actual outcome:           [value]
- P50 counterfactual:       [value]
- Attribution to antecedent: ~[%] of the actual outcome
- Attribution magnitude:    [small / moderate / large]

## Alternative counterfactual (stress-test)
- Alternative antecedent:   [different counterfactual]
- Outcome under alternative: [value / range]
- Implication for attribution: [if alternative also yields actual outcome → low attribution to original; if alternative yields very different outcome → original antecedent had real leverage]

## Verdict
- Attribution: [magnitude]
- Confidence: [low / moderate / high, anchored on chain plausibility]
- Decision implication: [what to do with this finding]
```

---

## Verification

- [ ] Actual outcome and antecedent are concrete with dates / magnitudes.
- [ ] Counterfactual antecedent specifies what was done *instead*, not just "didn't do it."
- [ ] Idealized vs realistic mode is named and justified.
- [ ] Causal chain has at least 3 steps with mechanisms.
- [ ] At least one branch point with probabilities is named.
- [ ] Outcome reported as a distribution (P25 / P50 / P75), not a point.
- [ ] Attribution is computed and labeled small / moderate / large.
- [ ] At least one alternative counterfactual was constructed for stress-testing.
- [ ] Confidence in the counterfactual is rated and anchored on chain plausibility.
- [ ] If evaluating decision quality, no post-decision information is used inside the counterfactual chain.
