---
title: "Reality Check — Real Expert Objections Without Fake Consensus"
category: "productivity/validation"
description: "Surface the standard objections credible experts would actually raise about a conclusion, each anchored to the source types they'd cite — explicitly forbidding invented 'experts agree' polling and labeling any guess as a guess."
techniques:
  - ST-01
  - RT-02
  - QA-02
  - DS-02
  - QA-04
difficulty: intermediate
tags:
  - validation
  - expert-objections
  - source-grounding
  - anti-fabrication
  - blind-spots
updated: "2026-06-07"
related_prompts:
  - domain-productivity/validation/validation_disconfirmation_pass.md
  - domain-productivity/validation/validation_audit_boundary_check.md
  - domain-productivity/validation/validation_quick_reality_check.md
---

# Reality Check — Real Expert Objections Without Fake Consensus

**Objective:** Identify the standard objections a credible expert would genuinely raise about a conclusion and tie each one to the source types they'd point to — replacing the AI failure mode of "experts agree that…" with honest, verifiable, source-anchored objections.

**When to use:**
- To ground a conclusion in what knowledgeable people would actually challenge.
- When you lack domain expertise and need to know where the objections live.
- Before presenting to an audience that knows the field better than you.
- To find blind spots your own reasoning can't see.

**When NOT to use:**
- Matters of pure preference where "expert objection" doesn't apply.
- When you need a full attack on the conclusion — use the disconfirmation pass instead.

**Audience:** Anyone presenting or relying on a conclusion in a field where credible experts could push back.

---

## Inputs / Context

1. **The conclusion** — one or two sentences on what you're claiming.
2. **The field** — the domain whose experts would weigh in.
3. **Your evidence** — what currently backs the claim (so objections can target the gaps).

---

## Constraints

### Must
- List the top standard objections a *credible* expert would raise (typically three).
- For each objection, name the **source types** the expert would point to (primary docs, official specs, case law, benchmark results, accepted textbooks, audit logs).
- Label any objection you're unsure about as a guess.
- Keep objections to ones a real, competent expert would actually voice.

### Must Not
- Invent "10 experts would say…" or any fabricated polling/consensus.
- Name specific real people as holding objections they may not hold.
- Cite a fabricated study, statistic, or standard as the source.
- Pad to three objections with weak or invented ones.

---

## Instructions

1. **Collect inputs.** State the conclusion, the field, and the evidence behind it.
2. **Run the reality-check prompt** below verbatim.

   ```
   REALITY CHECK — what would experts object to?

   1) List the top 3 standard objections a credible expert in this field would
      raise about my conclusion.
   2) For each objection, name the SOURCE TYPES they would point to
      (primary docs, official specs, case law, benchmark results, accepted
      textbooks, audit logs, etc.).
   3) For each, note whether you're confident this is a standard objection or
      guessing.

   Rules:
   - If you're guessing about expert objections, label it as a guess.
   - Do NOT invent "10 experts would say…" polling or fabricated consensus.
   - Do NOT attribute objections to named real people.
   - If only 1–2 genuine objections exist, give only those.
   ```

3. **Self-check before output.** Confirm each objection is one a competent expert would actually raise, each is anchored to source *types* (not invented sources), and any uncertainty is labeled as a guess.
4. **Deliver** the result in the Output Format below.

---

## False-Positive Prevention

❌ **DON'T:**
- Write "experts broadly agree that…" with no basis.
- Manufacture a consensus or a poll of imaginary experts.
- Attribute an objection to a named person without grounds.
- Cite a specific study or statistic that may not exist.
- Invent a third objection just to reach a round number.

✅ **DO:**
- Anchor every objection to source *types* an expert would actually consult.
- Label objections you're unsure about as guesses.
- Give fewer objections when only fewer are genuine.
- Keep each objection to something a competent practitioner would really say.
- Tie objections to the specific gaps in the stated evidence.

---

## Output Format

```
# Reality Check — [conclusion]

## Objection 1
- Objection: [...]
- Source types they'd cite: [...]
- Confidence: [standard objection / guess]

## Objection 2
- Objection: [...]
- Source types they'd cite: [...]
- Confidence: [standard objection / guess]

## Objection 3 (only if genuine)
- Objection: [...]
- Source types they'd cite: [...]
- Confidence: [standard objection / guess]

## Note
- [if fewer than 3 genuine objections exist, say so]
```

---

## Example Output

```
# Reality Check — "Our new pricing page A/B test proves the higher price lifts revenue"

## Objection 1
- Objection: The test likely lacked the sample size / duration to reach
  significance, so the "lift" may be noise.
- Source types they'd cite: the experiment's own power calculation, the raw
  conversion counts per arm, and a standard A/B significance calculator.
- Confidence: standard objection.

## Objection 2
- Objection: Revenue-per-visitor can rise while total conversions fall; if you
  measured revenue but not retention, you may have traded long-term LTV for a
  short-term per-sale bump.
- Source types they'd cite: cohort retention data, refund/chargeback logs, and
  accepted unit-economics references (LTV/CAC).
- Confidence: standard objection.

## Objection 3 (only if genuine)
- Objection: Novelty/seasonality confound — if the test ran during a promotion
  or a launch spike, the result won't generalize.
- Source types they'd cite: the marketing calendar/changelog and prior-period
  baseline conversion data.
- Confidence: guess — depends on when the test ran, which isn't stated.

## Note
- Objections 1–2 are standard; objection 3 is conditional on test timing.
```

---

## Verification

- [ ] Objections are ones a competent expert would actually raise.
- [ ] Each objection anchored to specific source types.
- [ ] Objections you're unsure about labeled as guesses.
- [ ] No invented polling, consensus, named people, or fabricated studies.
- [ ] Fewer than three objections given if only fewer are genuine.

---

## Techniques Used
- **ST-01 (Clear Objective Statement):** Sets the model's job as surfacing genuine expert objections, not manufacturing consensus.
- **RT-02 (Multi-Dimensional Analysis Framework):** Simulates the credible-expert perspective across the field's standard challenges.
- **QA-02 (Adversarial Stress-Test):** Drives the objection-finding against the conclusion.
- **DS-02 (Metric Specification):** Requires each objection to be anchored to specific, verifiable source types.
- **QA-04 (Uncertainty Acknowledgment):** Forces labeling of guessed objections and prevents fabricated certainty.

---

## Related Prompts
- `domain-productivity/validation/validation_disconfirmation_pass.md` — go from listing objections to fully attacking the conclusion.
- `domain-productivity/validation/validation_audit_boundary_check.md` — identify which expert can actually verify the objections.
- `domain-productivity/validation/validation_quick_reality_check.md` — the fast everyday grounding pass.
