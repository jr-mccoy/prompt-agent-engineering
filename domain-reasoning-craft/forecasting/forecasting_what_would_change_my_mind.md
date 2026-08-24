---
title: "What Would Change My Mind — Falsifiability Tripwires for a Belief or Forecast"
category: reasoning-craft/forecasting
description: "Force a forecaster or believer to specify in advance what observable evidence would move their belief by stated amounts in either direction. Produces tripwires the user agrees to honor when triggered, defeats motivated reasoning ex post, and exposes beliefs that are unfalsifiable (and therefore not really forecasts)."
techniques:
  - ST-01
  - ST-02
  - RT-02
  - DS-01
  - CM-02
  - QA-01
difficulty: intermediate
tags:
  - forecasting
  - falsifiability
  - belief-update
  - tripwires
  - calibration
updated: "2026-05-10"
reasoning:
  styles: [bayesian, falsificationist, pre-commitment]
  stakes: variable
  horizon: months_to_years
  uncertainty: ambiguity
  evidence_quality: variable
  domain_complexity: variable
  collaboration: solo
  output_format: tripwire_table
  user_role: [analyst, founder, investor, executive, researcher, individual]
  mode: [forecast, audit, document]
related_prompts:
  - domain-reasoning-craft/reasoning-moves/reasoning_bayesian_belief_update.md
  - domain-reasoning-craft/forecasting/forecasting_super_forecaster_decomposition.md
  - domain-reasoning-craft/epistemic/epistemic_evidence_against_yourself.md
---

# What Would Change My Mind

**Objective:** Take a forecast or belief and force the user to specify, in advance, what observable evidence would move their belief by specific amounts in either direction. Produces a tripwire table the user pre-commits to honor when an item is triggered. Defeats two failure modes: ex-post motivated reasoning (rationalizing why new evidence "doesn't really count"), and unfalsifiable beliefs (those for which no evidence would change the believer's mind, which by definition aren't forecasts at all).

**When to use:**
- A high-stakes forecast (investment thesis, strategic bet, hiring decision, policy position) where the user wants pre-committed update rules.
- A team disagreement where surfacing each side's tripwires reveals what they're actually predicting.
- A long-running thesis that has not been re-examined; tripwires let you check whether the original conditions still hold.
- Personal beliefs where the user suspects motivated reasoning ("I would update if X, but X never quite seems to happen").
- After a `reasoning_bayesian_belief_update` to set the next-evidence pointers concretely.

**When NOT to use:**
- The belief is about an unobservable phenomenon (metaphysical, definitional, purely values-based). Tripwires require observables.
- The decision deadline is so close that no tripwire could trigger in time.
- The forecast is one-shot with no intermediate observables.

**Audience:** Investors, founders, analysts, researchers, executives, anyone whose track record depends on updating beliefs honestly when evidence demands it.

---

## Inputs / Context

1. **The belief or forecast.** State as a probability or outcome with horizon. ("I am 75% confident X by date Y.")
2. **The decision tied to the belief.** What action is contingent on this forecast holding?
3. **Time horizon.** When is the forecast resolved, and how far between now and then are observables expected?
4. **Update direction the user expects to be hardest.** Most people are more resistant to one direction than the other; surfacing this is part of the work.
5. **Personal honesty contract.** Will the user actually act on a triggered tripwire, or are they writing tripwires they won't honor? If the latter, the exercise has no value.

---

## Constraints

### Must
- Produce tripwires in **both** directions (would strengthen the belief AND would weaken it). Asymmetric tripwires reveal motivated reasoning.
- Make each tripwire **observable** (not "if I become convinced", but "if X is publicly reported / measured / observed").
- Specify the magnitude of update each tripwire triggers (small / moderate / large), pre-committed in advance.
- Include at least one "decisive" tripwire in each direction — evidence that would be sufficient to flip the user's qualitative position.
- Distinguish between **leading** tripwires (early signals) and **lagging** tripwires (confirmation after the fact).
- Surface unfalsifiability: if the user cannot generate any tripwire that would weaken their belief, name this and stop. The belief is not a forecast.

### Must Not
- Accept tripwires the user wouldn't actually honor. The deliverable is pre-commitment, not theater.
- Allow tripwires phrased as "if I become convinced". Convince by what?
- Set tripwires so far in the future they cannot bind the current decision.
- Allow asymmetric magnitudes ("large evidence required to weaken; tiny evidence sufficient to strengthen") without flagging as motivated reasoning.
- Skip the unfalsifiability check.

---

## Instructions

### Step 1 — Restate the belief
Write the belief / forecast as a probability or outcome with a horizon. Note the action that depends on it.

### Step 2 — Identify update-resistant direction
Ask: which direction of update would feel hardest to make? Why? (Sunk cost, public commitment, identity attached, financial exposure.) Surface this before generating tripwires; resistance shapes which tripwires the user is likely to discount.

### Step 3 — Generate strengthening tripwires
List 3–5 observable events that, if they occurred, would push the belief upward. For each:
- The observable (specific, measurable, attributed)
- Magnitude of update (small / moderate / large)
- Time window during which it could occur
- The source or channel where the observable would be seen (outlet, dataset, dashboard, report)

### Step 4 — Generate weakening tripwires
List 3–5 observable events that, if they occurred, would push the belief downward. Same fields. Pay extra attention here — these are the ones the user is likely to evade.

### Step 5 — Decisive tripwires in each direction
Identify (or generate) at least one observable in each direction that would be **sufficient** for a qualitative flip — strong upward to "act on the thesis confidently" or strong downward to "abandon the thesis."

### Step 6 — Asymmetry check
Compare strengthening vs weakening tripwires:
- Are the magnitudes asymmetric (much larger evidence required to weaken)? Why?
- Are weakening tripwires phrased so vaguely they could be evaded? Sharpen them.
- Are decisive-weakening tripwires effectively impossible to observe? That's unfalsifiability hiding behind specificity.

### Step 7 — Unfalsifiability check
If the user genuinely cannot generate weakening tripwires, the belief is not a forecast — it's a commitment, a value, or a defended identity. Name this and stop the prompt; the belief is not the right object for this tool.

### Step 8 — Leading vs lagging
Mark each tripwire as **leading** (would trigger before the forecast resolves) or **lagging** (would only confirm after the fact). Leading tripwires are operationally useful; lagging ones are mostly for after-action review.

### Step 9 — Pre-commitment statement
Draft a statement the user signs (mentally or in writing): "If [tripwire] triggers by [date], I will update my probability from [X] to [Y] and take action [Z]." The statement is the artifact.

### Step 10 — Monitoring plan
- How will the user actually observe these tripwires? (Calendar reminder, alert, weekly review.)
- Who else, if anyone, will hold them accountable?

---

## False-Positive Prevention

1. **Vague tripwires.** "If the market changes" is not a tripwire. "If category penetration falls below 12% by Q3" is.
2. **Asymmetric magnitudes.** Requiring a triple-blind RCT to weaken but a single anecdote to strengthen is motivated reasoning. Force symmetric evidence standards.
3. **Decisive-weakening evasion.** A common pattern: weakening tripwires that are technically observable but practically impossible. Name the evasion.
4. **Magic-window tripwires.** "If X happens in the next two weeks" — the tripwire never fires because the window is wrong. Pick windows that match the actual rate of evidence arrival in this domain.
5. **Theater pre-commitment.** Writing tripwires the user has no intention of honoring. Test by asking what they would do *today* if a tripwire had already fired ex-post.
6. **Confusing prediction with values.** "I believe in this regardless of evidence" is fine for values, useless for forecasts. Don't smuggle one into the other.
7. **Single-source dependence.** All tripwires sourced from the same outlet / dataset can be jointly biased. Spread sources.
8. **Update-magnitude inflation.** Marking everything "large update" produces noise. Most evidence updates beliefs modestly; reserve "large" for genuinely diagnostic observables.

---

## Output Format

```
# Tripwires for [belief / forecast]

## Belief
- Statement: [forecast with probability and horizon]
- Action contingent on it: [decision]
- Update-resistant direction: [up / down] — because [reason]

## Strengthening tripwires
| # | Observable                  | Time window | Update magnitude | Source        | Leading/Lagging |
|---|-----------------------------|-------------|------------------|---------------|-----------------|
| 1 | [specific, measurable]      | [Q3 2026]   | moderate         | [outlet/data] | leading         |
| 2 | …                           |             |                  |               |                 |

## Weakening tripwires
| # | Observable                  | Time window | Update magnitude | Source        | Leading/Lagging |
|---|-----------------------------|-------------|------------------|---------------|-----------------|
| 1 | [specific, measurable]      | [date]      | moderate         | [source]      | leading         |
| 2 | …                           |             |                  |               |                 |

## Decisive tripwires (qualitative flip)
- Decisive strengthen: [observable] → action: [act on thesis confidently]
- Decisive weaken:    [observable] → action: [abandon / restructure thesis]

## Asymmetry check
- Magnitudes symmetric? [yes / no — note]
- Weakening tripwires evadable? [yes / no — sharpening done]
- Decisive-weakening practically observable? [yes / no — note]

## Unfalsifiability check
- User able to generate weakening tripwires? [yes / no]
- If no: this belief is not a forecast. Reclassify as [value / commitment / identity] and stop.

## Pre-commitment
> If [tripwire] triggers by [date], I will update my probability from [X] to [Y] and take action [Z].

(Repeat for each load-bearing tripwire.)

## Monitoring plan
- Observation method: [how the user will actually see tripwires fire]
- Review cadence: [weekly / monthly]
- Accountability: [name, or self]
```

---

## Verification

- [ ] At least 3 strengthening AND 3 weakening tripwires.
- [ ] Each tripwire is observable (specific, measurable, attributed).
- [ ] Update magnitudes pre-committed, not assigned ex post.
- [ ] At least one decisive tripwire in each direction.
- [ ] Symmetry of evidence standards checked and any asymmetry justified.
- [ ] Unfalsifiability check performed.
- [ ] Pre-commitment statements drafted for load-bearing tripwires.
- [ ] Monitoring plan exists.
- [ ] No tripwires the user has no intention of honoring.
- [ ] No "if I become convinced" or other unobservable phrasings.
