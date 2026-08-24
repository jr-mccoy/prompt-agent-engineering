---
title: "Final Gate — Pre-Commitment STOP Check for Irreversible Decisions"
category: "productivity/validation"
description: "A last gate before a public commitment or high-stakes decision: assess failure severity, reversibility, minimum verification, expert-review status, and AI-induced confidence — with a hard STOP when reversibility is low and review is missing."
techniques:
  - ST-01
  - CM-02
  - QA-02
  - DS-02
  - QA-04
difficulty: intermediate
tags:
  - validation
  - pre-commitment
  - reversibility
  - stop-gate
  - decision-quality
updated: "2026-06-07"
related_prompts:
  - domain-productivity/validation/validation_am_i_being_nuts.md
  - domain-productivity/validation/validation_audit_boundary_check.md
  - domain-productivity/validation/validation_disconfirmation_pass.md
---

# Final Gate — Pre-Commitment STOP Check for Irreversible Decisions

**Objective:** Run a last gate before a public commitment or hard-to-undo decision, tying a STOP/GO call to failure severity, reversibility, and whether the verification and human review actually match the level of risk.

**When to use:**
- Before publishing content that affects reputation.
- Before financial commitments or contractual/legal agreements.
- Before any decision that is hard or expensive to undo.
- When you feel suddenly confident and aren't sure the confidence is earned.

**When NOT to use:**
- Low-stakes, easily reversible choices — a quick gut check suffices.
- Decisions you've already gathered full expert review on and only need to execute.

**Audience:** Anyone standing at the edge of an irreversible or public commitment who wants one disciplined pause.

---

## Inputs / Context

1. **The commitment** — what you're about to do, stated plainly.
2. **Failure scenario** — what "wrong" looks like and how bad it gets.
3. **Reversibility** — whether and at what cost you could unwind it.
4. **Verification so far** — what you've checked, including any human expert review.
5. **Time pressure** — the real deadline vs. a self-imposed one.

---

## Constraints

### Must
- Tie the final STOP/GO explicitly to **reversibility × verification strength**.
- Enforce the hard STOP: low reversibility **and** missing expert review → "STOP."
- When STOP, give the **next best action** (who to consult, what to test, or how to downgrade the decision).
- Distinguish AI-induced confidence from confidence earned by verification.
- Include the future-regret projection ("six months from now…").

### Must Not
- Wave the decision through because it sounds plausible or because the user is eager.
- Invent that expert review happened, or claim "experts would approve."
- Treat a self-imposed deadline as if it were externally fixed.
- Manufacture reassurance to ease the commitment.

---

## Instructions

1. **Collect inputs.** Note the commitment, the failure scenario, reversibility, verification so far, and the true time pressure.
2. **Run the final-gate prompt** below verbatim against the inputs.

   ```
   FINAL GATE — before a public commitment or high-stakes decision

   1) If this is wrong, what does failure look like? How bad is it?
   2) Reversibility: can I unwind this, or am I locked in? At what cost?
   3) What is the minimum acceptable verification for this level of risk?
      Have I met it?
   4) Have I gotten human expert review? If not, why not?
   5) Am I rushing because the AI made me feel confident, or because the
      time pressure is genuinely real (and is the deadline external)?
   6) Six months from now, if this was wrong, what will I wish I had done today?
   7) Am I resisting external review because I'm afraid it will contradict me?

   STOP CONDITION:
   If reversibility is LOW and expert review is MISSING, say "STOP."
   Then give the next best action: who to consult, what to test, or how to
   downgrade the decision to something reversible.

   No reassurance. Do not invent that review has happened.
   ```

3. **Self-check before output.** Confirm the reversibility read is honest, the verification is judged against the *risk level* (not just "I looked at it"), the STOP condition fired if it should have, and the next action is concrete.
4. **Deliver** the result in the Output Format below.

---

## False-Positive Prevention

❌ **DON'T:**
- Issue a GO just because the plan reads well or the user is in a hurry.
- Claim expert review occurred when it didn't, or that "experts agree."
- Accept a self-imposed deadline as a reason to skip verification.
- Soften the STOP into "proceed with caution" when the hard condition is met.
- Pad with comfort that undercuts the gate's purpose.

✅ **DO:**
- Make the STOP/GO follow mechanically from reversibility × verification.
- Fire the hard STOP when low reversibility meets missing review.
- Name a specific reviewer role and a concrete next test when stopping.
- Separate "the AI made me feel sure" from "I verified this."
- State the future-regret answer plainly.

---

## Output Format

```
# Final Gate — [commitment]

## 1. Failure scenario + severity
- [...]

## 2. Reversibility
- [reversible / low / locked-in] — unwind cost: [...]

## 3. Minimum verification for this risk
- Required: [...]
- Met?: [yes/no — gap]

## 4. Human expert review
- Status: [done / missing] — if missing, why: [...]

## 5. Rush check
- Driver: [real external deadline / AI-induced confidence / self-imposed]

## 6. Future-regret projection
- [...]

## 7. External-review resistance
- [...]

## DECISION: STOP / GO
- Reason (reversibility × verification): [...]
- If STOP, next best action: [who / what test / how to downgrade]
```

---

## Example Output

```
# Final Gate — Posting a public "we never had a data breach" statement

## 1. Failure scenario + severity
- If a breach later surfaces that predates the statement, we've published a
  false public claim. Severity: high — regulatory exposure plus permanent
  credibility damage.

## 2. Reversibility
- Low. A retraction doesn't undo screenshots, archives, or press pickup.
  Unwind cost: reputational and possibly legal.

## 3. Minimum verification for this risk
- Required: security team confirms no known breach across all systems and
  the legal team signs off on the wording.
- Met?: No — only the marketing draft exists; security hasn't confirmed.

## 4. Human expert review
- Status: Missing (security + legal). Why: PR wants it out before the
  competitor's announcement this afternoon.

## 5. Rush check
- Driver: self-imposed competitive timing, not an external regulatory deadline.

## 6. Future-regret projection
- If wrong, I'll wish I'd spent the two hours to get security + legal sign-off
  instead of racing a competitor's press cycle.

## 7. External-review resistance
- Mild — there's an unspoken worry security might say "we can't certify that,"
  which is exactly the information we need before publishing.

## DECISION: STOP
- Reason: reversibility is LOW and expert review (security + legal) is MISSING —
  the hard STOP condition is met.
- Next best action: get written security confirmation and legal sign-off on the
  exact wording; if security can't certify, downgrade the claim to "we have no
  evidence of a breach and take security seriously," which is defensible.
```

---

## Verification

- [ ] Failure severity and reversibility both assessed honestly.
- [ ] Verification judged against the risk level, with the gap named.
- [ ] Expert-review status stated; reason given if missing.
- [ ] Rush driver classified (external / AI-induced / self-imposed).
- [ ] Hard STOP fired when low reversibility met missing review.
- [ ] On STOP, a concrete next action (role / test / downgrade) is given.
- [ ] No invented review, no manufactured reassurance.

---

## Techniques Used
- **ST-01 (Clear Objective Statement):** Casts the model as a pre-commitment gate, not a cheerleader.
- **CM-02 (Constraint Specification):** Encodes the hard STOP condition (low reversibility + missing review → STOP).
- **QA-02 (Adversarial Stress-Test):** Probes failure severity and external-review resistance.
- **DS-02 (Metric Specification):** Defines "minimum acceptable verification for this level of risk."
- **QA-04 (Uncertainty Acknowledgment):** Separates AI-induced confidence from verified confidence.

---

## Related Prompts
- `domain-productivity/validation/validation_am_i_being_nuts.md` — the full grounding pass to run before reaching this gate.
- `domain-productivity/validation/validation_audit_boundary_check.md` — determine who the missing reviewer should be.
- `domain-productivity/validation/validation_disconfirmation_pass.md` — attack the conclusion before the gate.
