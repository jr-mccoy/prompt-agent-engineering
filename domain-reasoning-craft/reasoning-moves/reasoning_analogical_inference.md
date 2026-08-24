---
title: "Analogical Inference — Predict from a Known Case to an Unknown One"
category: reasoning-craft/reasoning-moves
description: "Use a known case to predict outcomes in an unknown one via structural analogy. Force explicit mapping (what corresponds to what), test the underlying structure, identify disanalogies (where the cases differ in ways that matter), and bound the inference. Distinct from analogy-for-ideation: this is analogy-for-prediction."
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
  - analogy
  - inference
  - mapping
  - prediction
updated: "2026-05-10"
reasoning:
  styles: [analogical, structural, inductive]
  stakes: variable
  horizon: variable
  uncertainty: ambiguity
  evidence_quality: variable
  domain_complexity: cross_domain
  collaboration: solo
  output_format: structured_mapping_with_inference
  user_role: [analyst, strategist, scientist, founder, policy]
  mode: [forecast, audit, synthesize]
related_prompts:
  - domain-ideation/ideation_cross_domain_analogy_mining.md
  - domain-reasoning-craft/reasoning-moves/reasoning_reference_class_forecast.md
  - domain-reasoning-craft/reasoning-moves/reasoning_counterfactual_analysis.md
---

# Analogical Inference

**Objective:** Use a known case as a model for predicting outcomes in an unknown case. Distinct from `ideation_cross_domain_analogy_mining.md` (which is for generating ideas) — this prompt is for *inference*: I know what happened in case A; what does that tell me about case B? Force explicit structural mapping, test the underlying structure, identify disanalogies, and bound the inference to what the analogy actually supports.

**When to use:**
- Predicting outcomes for a novel situation where direct evidence is sparse but a comparable case exists.
- Reasoning about a market entry by analogy to a similar prior entry.
- Strategic forecasting where historical analogs are being invoked.
- Personal decisions where someone's past experience seems applicable to your situation.

**When NOT to use:**
- Reference-class forecasting when many cases exist (use `reasoning_reference_class_forecast.md` — better discipline).
- Pure ideation (use the cross-domain mining prompt).
- Cases where the analogy is being used persuasively rather than analytically.

**Audience:** Analysts, strategists, scientists, founders, policy people, anyone reasoning from one case to another.

---

## Inputs / Context

1. **Source case (known).** What happened, with timeline and outcomes.
2. **Target case (unknown).** What you're trying to predict.
3. **Why this analogy.** What initial mapping made the user reach for this comparison.
4. **Stakes.** What decision rides on the inference.

---

## Constraints

### Must
- Force **explicit element-by-element mapping**: what in source corresponds to what in target.
- Identify the **underlying structural pattern** (mechanism, dynamics, actor incentives) that makes the cases comparable.
- Identify **disanalogies**: ways the cases differ. For each: does the difference matter for the inference?
- State what the analogy supports vs what it doesn't.
- Output: predicted outcome with confidence anchored on **mapping strength**, not on the strength of the source-case outcome.
- If multiple plausible source cases exist, surface the others — single-analogy reasoning is brittle.

### Must Not
- Map at surface-level features ("both have the word 'platform' in the description").
- Ignore disanalogies because they're inconvenient.
- Treat the source-case outcome's strength as evidence for the target outcome.
- Stretch the analogy past what the structural mapping supports.
- Use the analogy as a closing argument when the disanalogies are doing more work than the analogy.

---

## Instructions

### Step 1 — State both cases
Source: what happened, when, with what outcome.
Target: what's being predicted, by when.

### Step 2 — Surface mapping
What does the user think corresponds to what?

| Source element | Target element |
|----------------|----------------|
| [actor] | [actor] |
| [resource] | [resource] |
| [environment] | [environment] |
| [trigger] | [trigger] |
| [...] | [...] |

### Step 3 — Underlying structural pattern
What's the pattern that makes these cases comparable? (Examples: "platform with cold-start network effects entering an incumbent-dominated market"; "incumbent introducing a new product line that cannibalizes its own cash cow"; "small team building infrastructure for an emerging standard.")

The pattern is the actual unit of comparison; surface features are not.

### Step 4 — Test mapping rigor
For each mapped element pair: does the correspondence hold at the structural level? Score: strong / moderate / weak.

### Step 5 — Identify disanalogies
List 4–8 ways the cases differ. For each:
- Does the difference matter for the predicted outcome?
- If yes, in which direction does it push?
- How much?

If most disanalogies push the prediction the same way, the analogy may be misleading.

### Step 6 — Alternative source cases
Are there other historical / comparable cases that would map equally well or better? List 2–3. Compare predicted outcomes across analogies. Convergence increases confidence; divergence reveals the analogy is not load-bearing.

### Step 7 — Bound the inference
What does the analogy actually support?
- Direction of outcome (up / down)
- Magnitude (rough order)
- Timing (rough)
- Specific mechanism (stronger inference)
- Specific quantitative outcome (weaker inference; rarely justified by analogy alone)

### Step 8 — Predicted outcome with confidence
- Predicted outcome
- Confidence: anchored on mapping strength, disanalogy patterns, alternative analogies
- What evidence would meaningfully strengthen or weaken this prediction

---

## False-Positive Prevention

1. **Surface analogy.** Same word ≠ same structure. The mapping must be at mechanism level.
2. **Disanalogy denial.** Inconvenient disanalogies are usually the most informative ones.
3. **Outcome-strength contagion.** "It worked spectacularly in case A, so it'll work spectacularly in case B" — the strength of the source outcome doesn't transfer; only the direction may.
4. **Single-analogy lock-in.** One analogy is rarely conclusive. Sketch alternatives.
5. **Stretched mapping.** Forcing correspondence on elements that don't match is the central failure mode.
6. **Persuasion vs analysis.** "Steam → electricity → AI" is rhetoric; analyze before accepting.
7. **Hindsight contamination in the source.** If the source case looks clean only in hindsight, don't lift "it worked because of X" as a transferable lesson without checking ex-ante visibility.

---

## Output Format

```
# Analogical inference — [target case]

## Source case (known)
- What happened: [...]
- Timeline: [...]
- Outcome: [...]

## Target case (unknown)
- What's being predicted: [...]
- Deadline: [...]

## Element-by-element mapping
| Source | Target | Correspondence (strong/mod/weak) |
|--------|--------|-----------------------------------|
| [...]  | [...]  | strong                            |
| [...]  | [...]  | moderate                          |
| ...    | ...    |                                   |

## Underlying structural pattern
- [Mechanism / dynamics / structure that makes them comparable]

## Mapping rigor
- Overall strength: [strong / moderate / weak]
- Anchored on: [strongest mapped element]

## Disanalogies
| # | Difference | Matters for outcome? | Direction | Magnitude |
|---|------------|----------------------|-----------|-----------|
| 1 | [...]      | yes                  | weakens   | medium    |
| ... |          |                      |           |           |

- Pattern of disanalogies: [push same direction / split / minor]

## Alternative source cases
| Source case | Mapping strength | Predicted outcome direction |
|-------------|------------------|------------------------------|
| [name]      | strong           | up                           |
| [name]      | moderate         | down                         |

- Convergence across analogies? [yes / no — implication]

## Inference bounds
- Direction: [up / down / lateral]
- Magnitude: [rough order]
- Timing: [rough]
- Specific mechanism: [if mapping supports]

## Predicted outcome
- Prediction: [...]
- Confidence: [low / moderate / high]
- Anchored on: [mapping strength + disanalogy pattern + alternative-analogy convergence]

## What would update
- Strengthen prediction: [evidence]
- Weaken prediction: [evidence]
```

---

## Verification

- [ ] Element-by-element mapping with correspondence ratings.
- [ ] Underlying structural pattern named.
- [ ] At least 4 disanalogies surfaced and assessed.
- [ ] Alternative source cases considered.
- [ ] Inference bounds explicit (direction OK; magnitude rough; quantitative outcome rarely).
- [ ] Confidence anchored on mapping strength.
- [ ] No surface-feature analogies.
- [ ] No outcome-strength contagion.
