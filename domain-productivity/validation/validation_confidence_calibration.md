---
title: "Confidence Calibration — Honest Score Plus Cheapest Tests to Raise It"
category: "productivity/validation"
description: "Rate a conclusion 1–10 on an anchored scale, expose the evidence gap holding the score down, and identify the cheapest tests that would move it — without manufacturing certainty."
techniques:
  - ST-01
  - RT-02
  - DS-02
  - QA-04
  - QA-02
difficulty: beginner
tags:
  - validation
  - confidence-calibration
  - uncertainty
  - evidence
  - decision-quality
updated: "2026-06-07"
related_prompts:
  - domain-productivity/validation/validation_quick_reality_check.md
  - domain-productivity/validation/validation_disconfirmation_pass.md
  - domain-productivity/validation/validation_audit_boundary_check.md
---

# Confidence Calibration — Honest Score Plus Cheapest Tests to Raise It

**Objective:** Assign a defensible confidence score (1–10) to a conclusion, name the specific evidence gap holding it down, and rank the cheapest tests that would raise it — catching the common error of treating a 5 like a 9.

**When to use:**
- After completing an analysis and before acting on its conclusion.
- To prioritize verification effort (what's the cheapest thing that moves the needle?).
- When you suspect you may be over-confident.
- Before presenting a conclusion as settled to others.

**When NOT to use:**
- Pure preference or taste calls where "confidence" doesn't apply.
- Decisions already made where you only need execution help.

**Audience:** Anyone holding a conclusion they're about to rely on and wanting an honest, actionable confidence read.

---

## Inputs / Context

1. **The conclusion** — one sentence stating what you believe to be true.
2. **The evidence you have** — what actually backs it (observable, checkable).
3. **The decision it feeds** — what you'll do if you trust it, and the stakes.

---

## Constraints

### Must
- Use the **anchored 1–10 scale** so the number means something consistent.
- Justify the score with the actual evidence, not a vibe.
- Identify the **specific missing evidence** holding the score down.
- Rank tests by cost-effectiveness (cheapest-that-moves-it first).
- Run the over-confidence check explicitly.

### Must Not
- Inflate the score to feel better, or deflate it to seem cautious.
- Invent supporting evidence, base rates, or expert agreement to justify a high score.
- Present an inferred figure as a measured one.
- Recommend an expensive test when a cheap one would move confidence as much.

### Scale anchors
- **1** = speculation / thin evidence
- **5** = plausible but significant uncertainty
- **9–10** = well-established; I'd bet money on it

---

## Instructions

1. **Collect inputs.** State the conclusion, the evidence you actually have, and the decision it feeds.
2. **Run the calibration prompt** below verbatim against the inputs.

   ```
   CONFIDENCE CALIBRATION

   Rate this conclusion 1–10 on this scale:
   1 = speculation / thin evidence
   5 = plausible but significant uncertainty
   10 = well-established; I'd bet money on it

   Then answer:
   1) What 2 cheapest tests would move confidence up by ~2 points?
   2) What 1 expensive test would move it up the most?
   3) What specific missing evidence is holding the score down?
   4) Am I treating this like a 9 when it's actually a 5? If so, why —
      what's driving the inflation (urgency, ego, sunk cost, AI agreement)?

   Rules: justify the number with real evidence. Label any base rate or
   figure you can't source as a guess. Do not invent expert agreement.
   ```

3. **Self-check before output.** Confirm the score is justified by actual evidence, the missing-evidence item is specific, the cheap tests really are cheaper than the expensive one, and the over-confidence answer is candid.
4. **Deliver** the result in the Output Format below.

---

## False-Positive Prevention

❌ **DON'T:**
- Anchor on a 7–8 by default to seem confident without evidence to match.
- Manufacture a base rate ("works ~70% of the time") to prop up the score.
- Cite "experts agree" or invented consensus as evidence.
- Label inference as verified fact in the justification.
- Recommend an expensive test as the only path when a cheap one moves it too.

✅ **DO:**
- Give a number you would actually defend out loud.
- Name the single specific piece of missing evidence by name.
- Mark any unsourced figure as a guess and say what would replace it.
- Order tests cheapest-first and state the expected point movement.
- Answer the over-confidence question honestly, naming the driver if present.

---

## Output Format

```
# Confidence Calibration — [conclusion]

## Score: X/10
- Justification (real evidence): [...]

## Cheap tests (do first)
1. [test] → expected +[n] points — checks: [...]
2. [test] → expected +[n] points — checks: [...]

## Expensive / definitive test
- [test] → expected +[n] points — checks: [...]

## Missing evidence holding the score down
- [specific item]

## Over-confidence check
- Am I treating a 5 like a 9? [yes/no] — driver if yes: [...]
```

---

## Example Output

```
# Confidence Calibration — "Switching to the new vendor will cut our infra bill 30%"

## Score: 4/10
- Justification: based on the vendor's published list prices vs our current
  list prices — but I have no quote for our actual usage tier, no data-egress
  estimate, and no migration-cost figure. One unverified comparison, no
  modeling of our real workload.

## Cheap tests (do first)
1. Request a real quote from the vendor for our actual usage → expected +2 —
   checks: whether the 30% holds at our tier, not at list price.
2. Pull last 3 months of egress/transfer from current billing → expected +1 —
   checks: the egress costs that headline pricing usually omits.

## Expensive / definitive test
- Run a 2-week shadow deployment of one service on the new vendor → +3 —
  checks: real measured cost and migration friction, not projected cost.

## Missing evidence holding the score down
- A quote tied to our actual usage profile (list-price comparison is not it).

## Over-confidence check
- Am I treating a 5 like a 9? Mild yes. Driver: the 30% headline number is
  attractive and I want the bill to drop, so I latched onto it before
  modeling our real workload.
```

---

## Verification

- [ ] Score uses the anchored 1–10 scale and is justified by real evidence.
- [ ] Cheap tests listed first, with expected point movement and what each checks.
- [ ] One expensive/definitive test named with expected movement.
- [ ] Specific missing evidence named (not "more data").
- [ ] Over-confidence check answered candidly, driver named if present.
- [ ] No invented base rates, figures, or expert agreement.

---

## Techniques Used
- **ST-01 (Clear Objective Statement):** Sets the model's job as honest calibration, not reassurance.
- **RT-02 (Multi-Dimensional Analysis Framework):** Maps evidence strength across dimensions to justify the score.
- **DS-02 (Metric Specification):** Defines the anchored scale and what each test must measure.
- **QA-04 (Uncertainty Acknowledgment):** Forces explicit labeling of guesses and the missing-evidence gap.
- **QA-02 (Adversarial Stress-Test):** Drives the over-confidence check ("treating a 5 like a 9").

---

## Related Prompts
- `domain-productivity/validation/validation_quick_reality_check.md` — the fast grounding pass when you need a number quickly.
- `domain-productivity/validation/validation_disconfirmation_pass.md` — attack the conclusion before you trust the score.
- `domain-productivity/validation/validation_audit_boundary_check.md` — check whether you can even verify the evidence yourself.
