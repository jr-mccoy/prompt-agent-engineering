---
title: "Abductive Inference — Best Explanations for an Observation"
category: reasoning-craft/reasoning-moves
description: "Given a surprising observation, generate 4–6 candidate explanations across categories (mechanism, intent, error, deception, coincidence, structural), score each on prior plausibility and explanatory fit, identify the most parsimonious vs most mechanism-rich, and design a single discriminating observation that would distinguish among them."
techniques:
  - ST-01
  - ST-02
  - RT-02
  - DS-01
  - DS-02
  - CM-02
  - QA-01
difficulty: intermediate
tags:
  - reasoning
  - abduction
  - explanation
  - hypothesis
  - everyday
updated: "2026-05-10"
reasoning:
  styles: [abductive, taxonomic, plausibility]
  stakes: variable
  horizon: minutes_to_hours
  uncertainty: ambiguity
  evidence_quality: variable
  domain_complexity: variable
  collaboration: solo
  output_format: ranked_explanations_plus_test
  user_role: [analyst, manager, individual, journalist, detective]
  mode: [diagnose, audit]
related_prompts:
  - domain-research-academic/research_hypothesis_generator.md
  - domain-reasoning-craft/reasoning-moves/reasoning_counterfactual_analysis.md
  - domain-reasoning-craft/epistemic/epistemic_disagreement_diagnosis.md
---

# Abductive Inference

**Objective:** Given a surprising observation, generate 4–6 candidate explanations spanning common categories, score each on prior plausibility and explanatory fit, identify the most parsimonious vs the most mechanism-rich, and design a single observation that would discriminate among them. Distinct from `research_hypothesis_generator.md` (which is for research design) — this is the everyday move of "given this surprising fact, what's the best explanation?"

**When to use:**
- A surprising metric movement, behavior change, message, or event.
- Diagnosing why something happened (root cause).
- Reading someone's intent from their actions.
- Detective-style reasoning in business, personal, or policy contexts.
- A team is jumping to one explanation and you want to widen the candidate set.

**When NOT to use:**
- Cases where the cause is obvious from direct evidence.
- Pure prediction (use forecasting prompts).
- Research-design hypothesis generation (use the dedicated prompt).

**Audience:** Analysts, managers, individuals reading puzzling situations, journalists, anyone needing to explain a surprising fact.

---

## Inputs / Context

1. **The observation.** What was seen, when, in what context.
2. **What's surprising about it.** What expectation does it violate?
3. **What you already know** about the actors / system involved.
4. **Stakes.** What decision rides on the explanation.

---

## Categories of explanation

| Category | Example for "team's metric dropped" |
|----------|--------------------------------------|
| **Mechanism / causal** | New deploy broke a feature in the funnel |
| **Intent** | Someone deliberately changed the target |
| **Error** | Logging bug, definition change |
| **Deception** | Numbers manipulated by reporter |
| **Coincidence / regression to mean** | Prior period was unusually high |
| **Structural / external** | Market shift, competitor move |
| **Selection / sampling** | Population being measured changed |

## Constraints

### Must
- Generate **4–6 explanations** spanning at least 4 categories.
- For each: explanation in one sentence, mechanism, prior plausibility, explanatory fit (does it explain everything observed or only some).
- Identify the **most parsimonious** (fewest assumptions / unobserved entities).
- Identify the **most mechanism-rich** (best explanatory coverage).
- These are often *different* explanations; surface the tension.
- Design **one discriminating observation** — a single check whose result would best narrow the candidate set.
- Use **base rates of explanations** (e.g., logging bugs are more common than coordinated user behavior shifts).

### Must Not
- Stop at the first plausible explanation.
- Conflate "I want it to be X" with "X is most plausible."
- Score parsimony as the verdict; parsimony is a tiebreaker.
- Generate explanations that all share the same discriminating observation (they're functionally one explanation).
- Skip the "coincidence" category — it's often the right answer for short observation windows.

---

## Instructions

### Step 1 — Sharpen the observation
Restate what was observed. Specify: what, when, where, by what measure, magnitude, baseline.

### Step 2 — Generate candidate explanations across categories
Walk through the categories above. Generate 4–6 explanations.

### Step 3 — Per-explanation scoring
| Explanation | Prior plausibility | Explanatory fit | Other predictions |
|-------------|---------------------|------------------|-------------------|
| [E1]        | high                | full             | [...]             |
| [E2]        | medium              | partial          | [...]             |
| ... | | | |

- **Prior plausibility:** how often this kind of explanation is true in this kind of situation, before evidence.
- **Explanatory fit:** does this account for all of what was observed, or only some.
- **Other predictions:** what else this explanation predicts that we could check.

### Step 4 — Parsimony vs mechanism richness
- **Most parsimonious:** fewest unusual assumptions or entities required.
- **Most mechanism-rich:** explains the most observations.

These are often different. The right choice depends on whether you trust your observation completeness (rich) or want to start from the simplest hypothesis (parsimonious).

### Step 5 — Discriminating observation
Design ONE check whose result would most narrow the candidate set:
- The check
- Predicted result under each candidate explanation
- Cost / feasibility
- What it rules in / out

### Step 6 — Recommended action
- If the discriminating check is cheap: do it; suspend judgment until result.
- If the check is expensive but stakes are high: do it.
- If the check is infeasible: weight remaining explanations by prior × fit, act on the leader, monitor for disconfirmation.

---

## False-Positive Prevention

1. **Single-explanation tunneling.** First plausible explanation often isn't the most likely.
2. **Category skipping.** Always check measurement / coincidence / sampling explanations, especially for sudden changes.
3. **Wishful explanation.** "Customers love it more" before checking "we accidentally turned off email throttling."
4. **Distinct-on-paper, identical-in-test.** Two explanations that share all observable predictions are one explanation.
5. **Parsimony as verdict.** Tiebreaker, not decisive.
6. **Coincidence-blindness.** For short windows or extreme prior periods, regression to mean is often correct.
7. **Base-rate ignorance.** "Logging bug" is much more common than "coordinated user behavior shift" for sudden metric changes.

---

## Output Format

```
# Abductive inference — [observation]

## Observation (sharp)
- What: [...]
- When: [...]
- Magnitude / baseline: [...]
- What's surprising: [violates which expectation]

## Candidate explanations
| # | Explanation | Category | Prior plausibility | Explanatory fit | Other predictions |
|---|-------------|----------|---------------------|------------------|-------------------|
| E1 | [...]       | mechanism | high              | full             | [...]             |
| E2 | [...]       | error     | high              | full             | [...]             |
| E3 | [...]       | coincidence | moderate        | partial          | [...]             |
| E4 | [...]       | intent    | low               | full             | [...]             |
| ... |            |           |                    |                  |                   |

## Parsimony vs mechanism richness
- Most parsimonious: E[#]
- Most mechanism-rich: E[#]
- Tension: [explain if different]

## Discriminating observation
- Check: [single observable]
- Predicted result per candidate:
  - E1: [...]
  - E2: [...]
  - E3: [...]
  - E4: [...]
- Cost: [low / med / high]
- Feasibility: [easy / moderate / hard]
- Rules in / rules out: [what each result would rule in or out]

## Recommended action
- [Run the check / act on leader / monitor]
- Reasoning: [...]
```

---

## Verification

- [ ] 4–6 explanations across at least 4 categories.
- [ ] Coincidence / regression-to-mean considered.
- [ ] Measurement / sampling considered.
- [ ] Each explanation has prior plausibility, fit, other predictions.
- [ ] Parsimonious vs mechanism-rich named separately.
- [ ] One discriminating observation designed with predicted results per candidate.
- [ ] Action recommended.
- [ ] No single-explanation tunneling.
