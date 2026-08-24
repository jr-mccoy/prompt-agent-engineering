---
title: "Motivated Reasoning Check — The Symmetry Test for Asymmetric Standards"
category: reasoning-craft/epistemic
description: "Run the asymmetric-standards test: take a conclusion the user holds and the evidence supporting it, then ask, item by item, whether they would accept that same evidence if it pointed the opposite way. Surfaces where the evidentiary bar is being applied asymmetrically — accepting weak support for the favored side while demanding strong support against it. Counters the failure mode of confusing 'I have evidence for this' with 'I would believe this regardless of which way the evidence cut.'"
techniques:
  - ST-01
  - ST-02
  - RT-02
  - DS-01
  - CM-02
  - QA-01
difficulty: intermediate
tags:
  - epistemic
  - motivated-reasoning
  - symmetry-test
  - bias-detection
  - self-audit
updated: "2026-05-21"
reasoning:
  styles: [adversarial, counterfactual, diagnostic]
  stakes: variable
  horizon: variable
  uncertainty: ambiguity
  evidence_quality: variable
  domain_complexity: variable
  collaboration: solo
  output_format: per_item_symmetry_table
  user_role: [analyst, researcher, executive, founder, individual]
  mode: [audit, diagnose]
related_prompts:
  - domain-reasoning-craft/epistemic/epistemic_evidence_against_yourself.md
  - domain-reasoning-craft/epistemic/epistemic_bias_specific_audit.md
  - domain-reasoning-craft/reasoning-moves/reasoning_bayesian_belief_update.md
---

# Motivated Reasoning Check

**Objective:** Test whether a conclusion is held because the evidence supports it, or because the user wants it to be true and is applying the evidentiary standard asymmetrically. The core move is the symmetry test: imagine the same evidence pointed the *opposite* way and ask, item by item, whether you'd find it persuasive. Walk through each supporting item — would you accept this study design, this expert, this sample size, this anecdote — if it cut against your conclusion? Surface the asymmetries, then produce a calibrated update. Distinct from `epistemic_evidence_against_yourself.md` (which gathers disconfirming evidence); this one audits the *standard* being applied to the evidence you already have.

**When to use:**
- You hold a conclusion you *want* to be true (it favors your plan, your team, your prior bet, your identity) and want to check whether your standards have slipped.
- A conclusion came easily and the supporting evidence felt obviously sufficient — ease is a warning sign.
- Before acting on a belief where being wrong is costly and the belief is emotionally or financially loaded.
- Reviewing a contested analysis where one side seems to apply a tougher standard to the other's evidence than to its own.

**When NOT to use:**
- The conclusion is one you have no stake in — motivated reasoning needs a motive; without one this test finds little.
- You need to surface *new* disconfirming evidence rather than re-examine the standard on existing evidence — use `epistemic_evidence_against_yourself.md`.
- The question is purely empirical with a clean test available; just run the test.

**Audience:** Analysts, founders, executives, researchers, and individuals checking a belief they have a stake in.

---

## Inputs / Context

1. **The conclusion held.** Stated plainly, including why the user wants it (or wants it to be false — motivated reasoning runs both directions).
2. **The supporting evidence, item by item.** Each study, data point, expert, anecdote, or argument cited for the conclusion.
3. **The stake.** What the user gains if the conclusion is true (or loses if false) — names the motive.
4. **The standard normally applied.** How the user usually evaluates evidence in this domain, if known.

---

## Constraints

### Must
- Name the **stake / motive** explicitly. Without a motive there's no motivated reasoning to find; with one, it's the lens for the audit.
- Run the symmetry test **per evidence item**: for each, ask "if this exact item pointed the other way, would I accept it?" Record the answer.
- Surface **asymmetries**: items accepted for the favored conclusion that would be rejected if reversed (or vice versa — demanding extra proof against a conclusion you want).
- Distinguish a **legitimate asymmetry** (a genuine reason this evidence is stronger in one direction) from a **motivated asymmetry** (a double standard tracking the desired conclusion).
- Produce a **calibrated update**: how the conclusion's confidence should change once asymmetries are corrected.
- Apply the test to **both directions** of stake — wanting something to be true, and wanting it to be false.

### Must Not
- Run the test only on conclusions the user is skeptical of. Motivated-reasoning checks are most needed on conclusions the user favors.
- Treat every asymmetry as illegitimate. Sometimes evidence genuinely is stronger one way; the test is whether the asymmetry has a reason independent of the desired answer.
- Conclude "you're being motivated" as a verdict on the person. The finding is about the standard applied to specific items, not the user's character.
- Let the symmetry test become a reason to flip to the opposite conclusion. Correcting an asymmetry recalibrates confidence; it doesn't mandate believing the reverse.
- Skip the stake. An audit with no named motive is just generic skepticism.

---

## Instructions

### Step 1 — State the conclusion and the stake
What's believed, and what the user gains if it's true (or loses if false). Name the direction of the motive.

### Step 2 — List the supporting evidence item by item
Enumerate each piece of support separately. Lumping them defeats the test.

### Step 3 — Reverse each item
For each item, construct the mirror: the same source / design / sample / expert producing the *opposite* result. Ask: "Would I accept this if it cut against me?"

### Step 4 — Record the answer and the gap
For each item: accept-both-ways (symmetric), accept-only-when-favorable (motivated asymmetry), or reject-both-ways (consistent skepticism). Note the gap where it exists.

### Step 5 — Legitimate vs motivated
For each asymmetry, test whether there's a reason it's genuinely stronger one way that has nothing to do with the desired conclusion. If yes, it's legitimate; if the only reason is "it agrees with me," it's motivated.

### Step 6 — Reverse-direction check
Also check the failure mode of demanding *extra* proof for things you want to be false (e.g., dismissing inconvenient evidence with standards you'd never apply to convenient evidence).

### Step 7 — Calibrated update
Recompute confidence in the conclusion using only the support that survives the symmetry test (i.e., evidence you'd accept regardless of direction). State the new confidence and what changed. Hand quantitative recomputation to `reasoning_bayesian_belief_update.md` if useful.

---

## False-Positive Prevention

1. **Self-exempt audit.** Running the test only on beliefs you doubt. Point it at the conclusion you most want to be true — that's where the asymmetry hides.
2. **Asymmetry over-detection.** Branding every directional difference as motivated. Some evidence really is stronger one way; require the asymmetry to lack any reason beyond "it agrees with me."
3. **Character verdict.** Concluding "you're biased" about the person. The finding is item-level: a standard applied unevenly to specific evidence.
4. **Flip-to-opposite error.** Treating a found asymmetry as license to believe the reverse. The correction is recalibration, not inversion.
5. **Missing the want-it-false direction.** Only checking inflated standards for favorable evidence and missing the deflated acceptance of "evidence that something I dread isn't true." Run both directions.
6. **Stake omission.** Auditing with no named motive. Without the stake, the test has nothing to anchor on.
7. **Lumped evidence.** Testing the body of support as a whole instead of item by item. The asymmetry usually lives in specific items.
8. **Symmetric-skepticism mislabel.** Counting "I'd reject this either way" as motivated reasoning. Consistent skepticism is the opposite of the failure mode.

---

## Output Format

```
# Motivated reasoning check — [conclusion]

## Conclusion and stake
- Conclusion: [what's believed]
- Stake / motive: [what the user gains if true / loses if false]
- Direction: [want it true / want it false]

## Per-item symmetry test
| # | Evidence item | Reversed version | Accept reversed? | Verdict |
|---|---------------|------------------|------------------|---------|
| 1 | [item]        | [same source, opposite result] | no | motivated asymmetry |
| 2 | [item]        | [...]            | yes              | symmetric |
| 3 | [item]        | [...]            | no (both ways)   | consistent skepticism |
| … |               |                  |                  |         |

## Asymmetry analysis
| Asymmetric item | Legitimate reason it's stronger one way? | Motivated? |
|-----------------|-------------------------------------------|------------|
| [item]          | [reason or "none beyond agreement"]       | yes/no     |

## Reverse-direction check
[Any evidence dismissed with a standard you wouldn't apply to convenient evidence]

## Calibrated update
- Support surviving the symmetry test: [which items]
- Prior confidence → revised confidence: [X% → Y%]
- What changed: [delta]
- Note: correcting an asymmetry recalibrates confidence; it does not mandate believing the opposite.
```

---

## Verification

- [ ] Stake / motive named, with direction (want-true / want-false).
- [ ] Each evidence item tested separately, not in aggregate.
- [ ] Reversed version constructed for each item with an accept/reject answer.
- [ ] Asymmetries classified legitimate vs motivated, with reasons.
- [ ] Reverse-direction (want-it-false) check performed.
- [ ] Calibrated update uses only symmetry-surviving support.
- [ ] Finding stated at the item level, not as a character verdict.
- [ ] Test applied to a favored conclusion, not only a doubted one.
