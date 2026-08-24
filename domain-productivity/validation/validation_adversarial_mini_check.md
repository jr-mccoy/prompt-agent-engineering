---
title: "Adversarial Mini-Check — Pre-Ship Overconfidence Catch"
category: "productivity/validation"
description: "A fast five-step adversarial verification for high-stakes, low-reversibility decisions that forces failure-finding, evidence discipline, stakes analysis, and honest confidence calibration before you ship."
techniques:
  - QA-01
  - QA-02
  - DS-02
  - RT-02
  - QA-04
difficulty: intermediate
tags:
  - validation
  - decision-making
  - risk-assessment
  - pre-mortem
  - confidence-calibration
  - anti-fabrication
updated: "2026-06-19"
related_prompts:
  - domain-productivity/validation/validation_final_gate.md
  - domain-productivity/validation/validation_reality_check.md
  - domain-productivity/validation/validation_disconfirmation_pass.md
---

# Adversarial Mini-Check — Pre-Ship Overconfidence Catch

**Objective:** Force systematic problem-finding at the exact moments overconfidence runs away — right before you ship something costly to reverse — and produce a clear proceed / pause / stop verdict grounded in evidence and honest confidence.

**When to use:**
- Before sending high-stakes communications (executive emails, client proposals).
- Before financial commitments (large purchases, investments, contracts).
- Before publishing content with reputational weight.
- Before deploying code to production, especially without a clean rollback.
- For any high-stakes decision with limited reversibility.

**When NOT to use:**
- Low-stakes, easily reversible decisions where the analysis overhead exceeds the risk.
- As a rubber stamp to manufacture the feeling of having checked.

**Audience:** Anyone about to commit to a decision or action that's expensive or hard to undo.

---

## Inputs / Context

1. **The decision/action under review** — one or two sentences on what's being shipped or decided.
2. **The claims it rests on** — what you're treating as true to justify shipping.
3. **Stakes and reversibility** — what breaks if you're wrong, and how hard it is to undo.

---

## Constraints

### Must
- Work through all five steps; do not skip any because you "feel confident."
- Name specific failure modes, specific experts (by name/role), and specific tests — not "someone" or "it might break."
- Label each claim as fact, inference, or assumption, with what would falsify it.
- End with one verdict: PROCEED, PAUSE, or STOP.

### Must Not
- Treat the check as a formality that always returns "proceed."
- Claim something was verified when it was only assumed — label guesses as guesses.
- Assert false consensus ("experts agree this is fine") or invent a reviewer who didn't review.
- Let time pressure override the process on high-stakes, low-reversibility decisions.

---

## Instructions

1. **Run the five-step check below verbatim**, applying it to your decision.

```
ADVERSARIAL MINI-CHECK — find the problems, do not seek reassurance.

1) AUDIT BOUNDARY
   - List every skill required to verify this work end-to-end.
   - Honestly state whether I have each skill; if not, name the specific person
     who does (by name/role, not "someone").

2) ATTEMPT TO BREAK IT
   - List the 3 most likely failure modes (each: likelihood H/M/L, impact H/M/L).
   - State the single strongest objection a credible domain expert would raise,
     and my honest response to it.

3) EVIDENCE DISCIPLINE
   - For each key claim: is it FACT, INFERENCE, or ASSUMPTION?
   - What evidence would falsify it? What would raise confidence?
   - What source type would I trust (primary docs, benchmarks, logs, papers)?

4) STAKES & REVERSIBILITY
   - If I'm wrong, what specifically breaks and how bad (1–10)?
   - Is this reversible? At what cost?
   - Current confidence (1–10) with justification.

5) CALIBRATE CONFIDENCE
   - 2 cheap tests that would move confidence up ~2 points.
   - 1 expensive test that would move it the most.
   - Honest check: am I treating this like a 9 when it's actually a 5?

RULES:
- Be specific: "the payment API may time out under load", not "it might break".
- Name real experts ("Sarah, security lead"), not "the team".
- Distinguish "I checked" from "I assumed"; label assumptions as assumptions.
- Do NOT invent expert consensus or claim a review happened that didn't.
- If reversibility is low and no qualified expert has reviewed: STOP and escalate.
```

2. **Apply the customization for your decision type** (below) if relevant.
3. **Set the verdict** — PROCEED, PAUSE (run named tests first), or STOP (escalate to a named person).
4. **Deliver** the result in the Output Format below.

**Customization:**
- **Code deployments:** add rollback-plan verification and monitoring-dashboard checks.
- **Communications:** add recipient-impact analysis and a "what if this leaks" scenario.
- **Financial decisions:** add maximum-downside and liquidity-impact analysis.
- **Hiring decisions:** add reference-check verification and probation reversibility.

---

## False-Positive Prevention

❌ **DON'T:**
- Use this as a rubber stamp — going through the motions without genuine problem-finding.
- Accept vague answers ("someone will review it" instead of "Jane reviews it Tuesday").
- Conflate familiarity with correctness ("I've done this before" ≠ "I verified this").
- Claim a reviewer or consensus that doesn't exist.

✅ **DO:**
- State specific, concrete failure modes.
- Name the actual person who could verify what you can't.
- Distinguish "I checked" from "I assumed" and label the assumptions.
- Document what you're NOT checking and why that's acceptable.
- Escalate when stakes are high and reversibility is low.

---

## Output Format

```markdown
## Adversarial Mini-Check Results

### Decision/Action Under Review
[Brief description of what's being shipped/decided]

### 1. Audit Boundary
**Skills Required:**
- [ ] [Skill] — I have / [Name] has
- [ ] [Skill] — I have / [Name] has
**Gap Assessment:** [verification capability summary]

### 2. Breaking Attempt
**Top 3 Failure Modes:**
1. [Most likely] — Likelihood: H/M/L | Impact: H/M/L
2. [Second] — Likelihood: H/M/L | Impact: H/M/L
3. [Third] — Likelihood: H/M/L | Impact: H/M/L
**Strongest Expert Objection:** > "[what a skeptical expert would say]"
**My Response:** [how I'd address it — honestly, even if weak]

### 3. Evidence Discipline
| Claim | Type (Fact/Inference/Assumption) | Falsification | Source I'd Trust |
|-------|----------------------------------|---------------|------------------|
| [Claim] | [type] | [what would disprove it] | [source type] |
**Key Uncertainties:** [what I don't know that matters]

### 4. Stakes & Reversibility
**If Wrong:** [what breaks]: [how bad, 1–10]
**Reversibility:** High / Medium / Low
**Reversal Cost:** [time/money/reputation to undo]
**Current Confidence:** [X]/10 — [justification]

### 5. Confidence Calibration
**Cheap Tests (~+2 points):** 1. [test] — [time]  2. [test] — [time]
**Expensive Test (biggest boost):** [test] — [time/cost]
**Calibration Check:** [am I overconfident? honest answer]

### Verdict
[ ] PROCEED — confidence sufficient, risks acceptable
[ ] PAUSE — run [specific test(s)] before proceeding
[ ] STOP — escalate to [specific person] because [reason]
```

---

## Verification

- [ ] All five steps completed; none skipped on grounds of confidence.
- [ ] Failure modes, experts, and tests are specific and named.
- [ ] Each claim labeled fact / inference / assumption with a falsification.
- [ ] Stakes and reversibility stated with a justified confidence number.
- [ ] No invented consensus or phantom reviewers; assumptions labeled as such.
- [ ] A single clear verdict (PROCEED / PAUSE / STOP) is given.

---

## Techniques Used
- **QA-01 (Self-Check / Verification Step):** Forces explicit problem-finding before output.
- **QA-02 (Adversarial Stress-Test):** "Find problems, no reassurance" stance against the decision.
- **DS-02 (Metric/Criteria Specification):** Separates facts from inference and requires falsification criteria and source types.
- **RT-02 (Multi-Dimensional Analysis Framework):** Five lenses — audit boundary, failure modes, evidence, stakes, calibration.
- **QA-04 (Uncertainty Acknowledgment):** Confidence scoring with honest calibration; bars fabricated certainty and false consensus.

---

## Related Prompts
- `domain-productivity/validation/validation_final_gate.md` — broader, more comprehensive pre-launch checklist.
- `domain-productivity/validation/validation_reality_check.md` — surface the objections a credible expert would actually raise.
- `domain-productivity/validation/validation_disconfirmation_pass.md` — go from finding objections to fully attacking the conclusion.
