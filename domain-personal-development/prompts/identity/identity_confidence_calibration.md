---
title: "Calibrate Confidence Against Evidence in Both Directions"
category: personal-development/identity
description: "Two-mode self-assessment: impostor-syndrome correction (where evidence is being ignored) and overconfidence audit (where evidence is being inflated). Same calibration scaffolding, different direction."
techniques:
  - ST-01
  - ST-02
  - OC-08
  - RT-05
  - QA-04
  - QA-12
difficulty: intermediate
tags:
  - identity
  - confidence
  - impostor-syndrome
  - overconfidence
  - calibration
  - self-assessment
updated: "2026-05-08"
related_prompts:
  - domain-personal-development/prompts/identity/identity_self_talk_audit.md
  - domain-personal-development/prompts/identity/identity_values_clarification.md
  - domain-productivity/validation/validation_confidence_calibration.md
  - domain-personal-development/prompts/agency/agency_decision_post_mortem.md
---

# Calibrate Confidence Against Evidence in Both Directions

**Objective:** Compare the user's stated confidence in a specific capability or identity claim against the evidence they actually have. Output the gap and a calibration move. Two modes: **Impostor mode** (suspect evidence is being ignored) and **Overconfidence mode** (suspect evidence is being inflated). Same scaffolding, opposite direction.

**When to use:** The user is making a decision (taking on a role, declining one, making a claim, accepting feedback) and wants to check whether their self-assessment is grounded. Distinct from `validation_confidence_calibration.md` which calibrates confidence in a specific *decision*; this one calibrates confidence in a *capability* or *identity claim* about the self.

**Audience:** An individual self-assessing. Not for performance review of others. Not clinical: chronic, debilitating impostor-syndrome belongs with a therapist, and chronic overconfidence with destructive consequences typically requires more than a prompt.

---

## Inputs Required

1. **The capability or identity claim being assessed.** One sentence. Concrete, not abstract. Examples: "I'm a senior backend engineer," "I can deliver this talk well," "I'm a good parent," "I'm bad at sales."
2. **Mode declaration.** Either:
   - **Impostor mode** — user suspects they are *underestimating* themselves, dismissing positive evidence, feeling like a fraud despite competence.
   - **Overconfidence mode** — user suspects they (or an external observer suggested they) are *overestimating* themselves, dismissing negative evidence, taking on more than the evidence supports.
   - If the user can't decide which mode, ask: *"Are you about to refuse an opportunity that scares you, or are you about to commit to one without verification?"* The first is impostor mode; the second is overconfidence mode.
3. **Confidence rating now.** 0–100% on the claim from input 1. Single number.
4. **Recent positive evidence.** 5–8 specific things that, if true, would support the claim. With dates and specifics: "Shipped X to N users on date," "Got promoted because of Y," "User Z said Q." Not vibes.
5. **Recent negative evidence.** 3–5 specific things that, if true, would *contradict* the claim. Same specificity. Failures, gaps, instances where the capability did not show up.
6. **Recent feedback received.** What credible sources (peers, manager, customers, users) actually said. Verbatim or close paraphrase.

If input 4 has zero items in **impostor mode**, the user has no calibration data to work from — recommend collecting evidence over 30 days first.
If input 5 has zero items in **overconfidence mode**, the user is too inside the claim to see contradictions; ask a trusted second party to fill in input 5 before continuing.

---

## Instructions

### Step 1 — Restate mode and refuse the wrong-mode answer

State which mode is active. Refuse the temptations of the other mode:

- **In Impostor mode:** the prompt's job is *not* to tell the user they're amazing. The job is to weigh evidence neutrally and report whether their internal estimate matches it.
- **In Overconfidence mode:** the prompt's job is *not* to tear the user down. Same job: weigh evidence neutrally.

This neutrality is the core mechanism. Both modes share it; only the suspected direction of error differs.

### Step 2 — Audit positive evidence (input 4)

For each item, label one of three:
- **Solid** — happened, attributable, repeatable. Counts.
- **Partial** — happened, but partially attributable to others, luck, or favorable conditions. Counts at fractional weight; specify the fraction qualitatively.
- **Discountable** — happened but doesn't support the specific claim, or is too old (> 18 months for a capability claim, > 3 years for an identity claim).

Sum: how many Solid + Partial items are there? In impostor mode, this is often higher than the user's gut said.

### Step 3 — Audit negative evidence (input 5)

Same labeling:
- **Solid** — instance where the capability genuinely was not present, attributable, recent.
- **Partial** — failure where conditions were unusual or context-specific. Counts at fractional weight.
- **Discountable** — instance that doesn't actually contradict the claim (different scope, much older context, specifically caused by an external factor).

Sum: how many Solid + Partial items? In overconfidence mode, this is often higher than the user's gut said.

### Step 4 — Audit feedback (input 6)

Tag each feedback item:
- **Independent** — from someone with no incentive to flatter or harm the user. Highest weight.
- **Coupled** — from someone with stakes (boss, customer, person you manage). Useful but not independent.
- **Discountable** — feedback so vague ("you're great!") it has no information content, or so emotionally driven (post-conflict) it isn't a clean signal.

In impostor mode, watch for the user discounting Independent + positive feedback as "just being nice." That's discounting evidence (see `identity_self_talk_audit.md` distortion #8).

In overconfidence mode, watch for over-weighting Coupled + positive feedback — flattery from people with stakes is not the same as quality.

### Step 5 — Produce a calibrated estimate

Given the audited evidence, produce a confidence range (low, central, high) on the claim from input 1. Examples:
- "Solid claim 70–85%. Range reflects two areas of unknown: [X], [Y]."
- "Solid claim 35–50%. Solid evidence supports a narrower version of the claim: '[narrower claim].'"

Compare to input 3 (user's stated confidence). Name the gap:
- **Impostor mode result:** "Stated 30%; evidence supports 65–80%. Gap = 35–50 points."
- **Overconfidence mode result:** "Stated 90%; evidence supports 55–70%. Gap = 20–35 points."

If the gap is small (< 10 points), the user is well-calibrated. Say so plainly.

### Step 6 — Diagnose the gap mechanism

The gap exists because of one or more known patterns. Pick the top one:

| Pattern | Mode | Description |
|---|---|---|
| Discounting positive evidence | Impostor | Solid items rated as Discountable, often as "luck" or "they were being nice." |
| Anchoring on a single failure | Impostor | One Solid negative outweighs many Solid positives. |
| Past-self conviction | Impostor | The claim is being assessed against a much older (and lower) version of the user's capability. |
| Comparison-as-floor | Impostor | Someone else's outcome treated as the bar; user underweights own evidence. |
| Inflating partial evidence | Overconfidence | Partial items rated as Solid; user takes credit for shared outcomes. |
| Discounting negative evidence | Overconfidence | Solid negatives reframed as one-offs or context-specific. |
| Confusing flattery with feedback | Overconfidence | Coupled feedback treated as Independent. |
| Identity over-extension | Overconfidence | Claim is being made at a wider scope than evidence supports ("I'm a great X" when evidence only supports "I'm a competent X under conditions Y"). |

Explain the named pattern in one paragraph using the user's specific evidence.

### Step 7 — Calibration move

Pick one of the following based on mode:

**Impostor mode →** the move is to *act on the calibrated estimate*, not the gut estimate. Specifically: take the action the user has been refusing because they didn't feel ready (apply, propose, offer, charge, lead). Set a date this week.

**Overconfidence mode →** the move is to *narrow the claim* until the evidence supports it, or *collect the missing evidence* before acting. Specifically: either rephrase the commitment ("I can deliver Y under Z conditions" rather than "I can deliver anything"), or run a small-stakes test before committing.

Either way: one move, this week, observable.

### Step 8 — Set a 60-day recalibration

State a 60-day check-in question — what evidence in the next 60 days would update the estimate, and in which direction.

---

## Constraints

### Must
- Declare mode explicitly at the top of the output.
- Audit all three input categories (positive evidence, negative evidence, feedback) with the same three-tier labeling.
- Produce a calibrated range and name the gap to stated confidence.
- Diagnose the gap with one named pattern from the table.
- Output exactly one calibration move, this week, observable.
- Acknowledge if the user is well-calibrated (gap < 10 points) instead of inventing a problem.

### Must Not
- In impostor mode, output reassurance or affirmations. The job is calibration, not comfort.
- In overconfidence mode, output criticism or moral judgment. The job is calibration, not punishment.
- Diagnose mental health conditions.
- Recommend therapy as the move (refer if symptoms warrant; don't prescribe it as the calibration step).
- Add patterns to the gap-mechanism table.
- Average the user's stated confidence and the calibrated estimate. Stated confidence is *data*; calibrated estimate is the answer.

---

## False-Positive Prevention

1. **Don't let the user pick the mode that flatters them.** Impostor mode users sometimes pick it because the prompt feels validating; overconfidence mode users sometimes refuse to pick it because of ego. The triage question in Step 1 helps; ask it directly.
2. **Don't accept "I have no positive evidence" at face value (impostor mode).** That answer is itself the symptom. Ask for the last six months of work in any form.
3. **Don't accept "I have no negative evidence" at face value (overconfidence mode).** That answer is itself the symptom. Insist on input 5 or refer to an external source.
4. **Don't conflate confidence in a claim with confidence in a decision.** This prompt is for capability/identity claims. Decision-level confidence belongs to `validation_confidence_calibration.md`.
5. **Don't issue both impostor and overconfidence verdicts simultaneously** ("you're under-confident here and over-confident there"). One claim, one mode, one calibration. If the user has two claims, run the prompt twice.
6. **Watch for distortion compounding.** If the impostor-mode user dismisses the prompt's calibrated estimate ("yeah but…"), name it as discounting-evidence and continue.

---

## Output Format

```
**Mode:** Impostor / Overconfidence
**Claim being assessed:** [restated]
**Stated confidence (input 3):** [%]

## Evidence audit
### Positive (input 4)
| Item | Label (Solid / Partial / Discountable) | Note |
| ... | ... | ... |
**Total:** [N Solid, M Partial, K Discountable]

### Negative (input 5)
[same structure]

### Feedback (input 6)
| Source | Item | Tag (Independent / Coupled / Discountable) |
| ... | ... | ... |

## Calibrated estimate
[Low–Central–High range], reflecting [the unknowns].

## Gap to stated confidence
[stated %] vs [calibrated range] = [N points] in the [under / over] direction.
*If gap < 10 points: "Well-calibrated. No correction needed."*

## Gap mechanism
**Pattern:** [from table]
**How it shows up in your evidence:** [one paragraph using user's specifics]

## Calibration move (this week)
[Specific physical action, by when, observable.]

## 60-day recalibration check
What evidence in the next 60 days would move the estimate, and in which direction.
```

---

## Verification

- [ ] Mode declared at top.
- [ ] All three input categories audited with the three-tier labeling.
- [ ] Calibrated estimate is a range, not a single number.
- [ ] Gap to stated confidence is quantified.
- [ ] Gap mechanism is one named pattern from the table.
- [ ] One calibration move, this week, observable.
- [ ] If gap < 10 points, "well-calibrated" called out — no invented problem.
- [ ] No reassurance, no moralizing, no clinical interpretation.
