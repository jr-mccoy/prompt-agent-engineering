---
title: "Audit Boundary Check — Can I Actually Verify This?"
category: "productivity/validation"
description: "A focused capability check that asks whether you personally have the skills to verify AI-generated or complex work, and if not, names the specific role that can — before you trust or act on the output."
techniques:
  - ST-01
  - DS-02
  - RT-02
  - QA-02
  - CM-02
difficulty: intermediate
tags:
  - validation
  - capability-assessment
  - expert-review
  - anti-fabrication
  - audit
updated: "2026-06-07"
related_prompts:
  - domain-productivity/validation/validation_confidence_calibration.md
  - domain-productivity/validation/validation_final_gate.md
  - domain-productivity/validation/validation_am_i_being_nuts.md
---

# Audit Boundary Check — Can I Actually Verify This?

**Objective:** Determine whether you personally possess the skills required to verify a piece of complex or AI-generated work end-to-end, and — if you don't — name the specific role that can, before you trust or act on it.

**When to use:**
- After completing a complex analysis you can't fully trace yourself.
- Before acting on AI-generated recommendations in a domain you don't own.
- When working outside your area of expertise.
- Before any irreversible decision based on output you can't independently check.

**When NOT to use:**
- Work fully inside your own expertise where you can verify every step.
- Trivial or easily-reversible outputs where the cost of being wrong is near zero.

**Audience:** Professionals, founders, and analysts relying on AI or specialist output they cannot fully audit themselves.

---

## Inputs / Context

1. **The work product** — what was produced (analysis, recommendation, document, calculation, code, legal/medical interpretation).
2. **The domain** — what field the work sits in.
3. **What you'll do with it** — the action that depends on it, and the stakes if it's wrong.
4. **Your own background** — relevant skills you actually have (be honest).

---

## Constraints

### Must
- Frame the question as *capability* ("who can verify this?"), not *credentials* ("who's qualified?").
- Name a **specific role** for review (e.g., "tax attorney," "SRE," "clinical pharmacist"), never "someone smart."
- List the concrete verification steps a real expert would actually run.
- State plainly when you lack a required skill — label the gap, don't paper over it.

### Must Not
- Invent that the work has "already been peer-reviewed" or that "experts agree" when no such review occurred.
- Rubber-stamp the work as verifiable just because it looks competent.
- Recommend a vague reviewer ("a professional," "an expert") with no role attached.
- Claim a verification step is sufficient without saying what it actually checks.

---

## Instructions

1. **Collect inputs.** Note the work product, its domain, the dependent action and stakes, and your own relevant skills.
2. **Run the boundary-check prompt** below verbatim against the inputs.

   ```
   STOP — AUDIT BOUNDARY CHECK

   1) What skills are required to verify what we've produced end-to-end?
      (Examples: reproduce the analysis, trace sources, test edge cases,
      interpret statute, run a backtest, check proofs, validate causality.)

   2) What would a real expert do to verify this quickly?
      List the specific checks they'd run, in order.

   3) Do I personally have those skills?
      If not, say so plainly. No bluffing.

   4) If I don't, who should review this before I trust it?
      Be specific about the ROLE (e.g., "tax attorney," "SRE,"
      "clinical pharmacist," "Lean formalization expert"),
      not vague ("someone smart").

   5) Until that review happens, what is the safe interim stance?
      (e.g., treat as draft, don't commit funds, don't publish.)
   ```

3. **Self-check before output.** Confirm the required-skills list is specific, the expert-check steps are concrete actions (not "review it carefully"), the self-assessment is honest, and every recommended reviewer is a named role.
4. **Deliver** the result in the Output Format below.

---

## False-Positive Prevention

❌ **DON'T:**
- Claim the work is "already verified" or "consensus-backed" when no review has happened.
- Recommend "an expert" with no specific role — that's an answer-shaped non-answer.
- List a verification step ("look it over") that doesn't actually test anything.
- Assert you have a skill you don't, to avoid admitting a gap.
- Mark something low-risk to skip the review when the stakes are real.

✅ **DO:**
- Tie each verification step to *what* it would catch if the work were wrong.
- Name the exact role (and, if relevant, the seniority) needed to verify.
- State capability gaps plainly: "I cannot verify the statutory interpretation."
- Point to source *types* an expert would check (case law, specs, audit logs), not invented authorities.
- Recommend a safe interim stance when verification is still pending.

---

## Output Format

```
# Audit Boundary Check — [work product]

## 1. Skills required to verify (end-to-end)
- [skill] — verifies: [what part]
- [skill] — verifies: [what part]

## 2. What an expert would do to verify (concrete steps)
1. [check] — catches: [failure it would surface]
2. [check] — catches: [...]

## 3. Do I have those skills?
- Have: [...]
- Don't have: [...] (plainly stated)

## 4. Who should review before I trust this
- Role: [specific role] — for: [which part]

## 5. Safe interim stance (until review)
- [draft / no commitment / no publish / etc.]
```

---

## Example Output

```
# Audit Boundary Check — AI-generated R&D tax-credit memo

## 1. Skills required to verify (end-to-end)
- Federal/state R&D credit law (IRC §41) — verifies: which activities qualify
- Tax accounting — verifies: the qualified-expense calculation and base amount
- Documentation standards — verifies: whether the substantiation survives audit

## 2. What an expert would do to verify (concrete steps)
1. Re-test each claimed activity against the §41 four-part test — catches:
   non-qualifying activities padded into the credit.
2. Recompute the credit from the underlying payroll/contractor figures —
   catches: arithmetic and base-period errors.
3. Check that contemporaneous documentation exists for each claim —
   catches: positions that look fine on paper but fail under examination.

## 3. Do I have those skills?
- Have: I can read the payroll inputs and follow the arithmetic.
- Don't have: I cannot reliably apply the §41 four-part test or judge
  whether the documentation would survive an IRS exam. Plainly: I can't
  audit the legal qualification.

## 4. Who should review before I trust this
- Role: a CPA or tax attorney with R&D-credit experience — for the
  qualification analysis and audit-defensibility of the documentation.

## 5. Safe interim stance (until review)
- Treat the memo as a draft estimate only. Do not file, and do not report
  the credit figure to investors as settled, until a qualified reviewer signs off.
```

---

## Verification

- [ ] Required-skills list is specific, not generic.
- [ ] Each expert-check step is a concrete action tied to what it catches.
- [ ] Self-assessment is honest; capability gaps stated plainly.
- [ ] Every recommended reviewer is a named role, not "someone smart."
- [ ] A safe interim stance is given for the pending-review period.
- [ ] No invented prior review, peer review, or expert consensus.

---

## Techniques Used
- **ST-01 (Clear Objective Statement):** Frames the model as a capability auditor whose sole job is to locate the verification boundary.
- **DS-02 (Metric Specification):** Defines what each verification step must actually measure or catch.
- **RT-02 (Multi-Dimensional Analysis Framework):** Simulates the expert perspective — what a domain specialist would check.
- **QA-02 (Adversarial Stress-Test):** Treats the work as something to attack and surface failure modes, not approve.
- **CM-02 (Constraint Specification):** Enforces the must/must-not rules (specific role, honest gaps, no invented review).

---

## Related Prompts
- `domain-productivity/validation/validation_confidence_calibration.md` — score how much you trust the conclusion once you know who can verify it.
- `domain-productivity/validation/validation_final_gate.md` — the pre-commitment STOP gate when expert review is missing.
- `domain-productivity/validation/validation_am_i_being_nuts.md` — the full 10-section grounding pass for high-stakes calls.
