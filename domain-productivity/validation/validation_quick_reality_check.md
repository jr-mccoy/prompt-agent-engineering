---
title: "Quick Reality Check — Two-Minute Grounding, Not Reassurance"
category: "productivity/validation"
description: "A fast grounding pass for everyday decisions and claims: state it falsifiably, check base rate, separate evidence from feeling, find the strongest objection, and get one next action — without spiraling or therapy."
techniques:
  - ST-01
  - DS-02
  - QA-02
  - RT-02
  - QA-04
difficulty: beginner
tags:
  - validation
  - reality-check
  - quick
  - grounding
  - decision-quality
updated: "2026-06-07"
related_prompts:
  - domain-productivity/validation/validation_am_i_being_nuts.md
  - domain-productivity/validation/validation_disconfirmation_pass.md
  - domain-productivity/validation/validation_reality_check.md
---

# Quick Reality Check — Two-Minute Grounding, Not Reassurance

**Objective:** Ground an everyday claim or decision in under two minutes — restated falsifiably, checked against base rate, with evidence separated from feeling and one highest-leverage next action — without spiraling or turning into therapy.

**When to use:**
- Daily decision-making and quick sanity checks on ideas.
- Before sending an important message or hitting publish.
- When you feel strongly about something and want a fast gut check.
- As the lightweight first pass before deciding whether a full grounding pass is warranted.

**When NOT to use:**
- High-stakes, irreversible commitments — escalate to `validation_am_i_being_nuts.md`.
- Acute emotional distress — this is a decision tool, not emotional support.

**Audience:** Anyone wanting a fast, repeatable grounding habit for everyday judgment calls.

---

## Inputs / Context

1. **The claim or decision** — 2–4 sentences on what you're thinking/deciding and why it matters.
2. **Whether a commitment is imminent** — are you about to spend money or commit publicly?

---

## Constraints

### Must
- Restate the claim as a falsifiable statement (or say why it isn't falsifiable).
- Give a base-rate / plausibility read and the simplest explanation that doesn't require you to be uniquely right.
- Separate real evidence, assumed evidence, and feelings-masquerading-as-evidence.
- Name the strongest objection a competent skeptic would raise.
- End with the single smallest action that most reduces uncertainty.

### Must Not
- Offer reassurance or "you've got this."
- Invent a base-rate figure or expert consensus to fill the plausibility line.
- Present a feeling or assumption as checkable evidence.
- Expand into a long therapeutic exploration — keep it to two minutes.

---

## Instructions

1. **Write the context** — 2–4 sentences on the claim/decision and its stakes.
2. **Run the quick-check prompt** below verbatim.

   ```
   REALITY CHECK — I need grounding, not reassurance.

   Context (2–4 sentences): [What I'm thinking/claiming/deciding + why it matters]

   1) STATE THE CLAIM CLEANLY
   Rewrite my claim as a falsifiable statement. If it's not falsifiable, say why.

   2) BASE RATE + PLAUSIBILITY
   What's the base rate of this being true in the real world? (Label it a guess
   if you don't have a real figure — don't invent one.)
   What's the simplest explanation that doesn't require me to be uniquely right?

   3) EVIDENCE vs FEELING
   List:
   - Evidence I actually have (observable, checkable)
   - Evidence I'm assuming
   - Feelings masquerading as evidence

   4) DISCONFIRMATION
   What would prove me wrong quickly?
   What's the strongest objection a competent skeptic would raise?

   5) NEXT ACTION
   Give me the single smallest action that would reduce uncertainty the most.
   If I'm about to commit publicly or spend money, tell me STOP or GO and why.
   No reassurance.
   ```

3. **Self-check before output.** Confirm the claim is genuinely falsifiable, any base rate is labeled a guess if unsourced, feelings are separated from evidence, and the next action is a single concrete step.
4. **Deliver** the result in the Output Format below.

---

## False-Positive Prevention

❌ **DON'T:**
- Slip in comfort ("this sounds great, go for it") in place of grounding.
- Fabricate a base rate or "most people find" statistic.
- Let an assumption sit in the "evidence I actually have" column.
- Invent a skeptic's objection that no competent person would raise.
- Balloon into a long reflective essay.

✅ **DO:**
- Label any unsourced base rate as a guess.
- Keep the "evidence I actually have" column to observable, checkable items only.
- Make the skeptic's objection one a real competent person would voice.
- Give exactly one smallest next action.
- Issue a plain STOP/GO when money or a public commitment is imminent.

---

## Output Format

```
# Quick Reality Check — [claim/decision]

## 1. Claim, falsifiably stated
- [...]   (or: not falsifiable because [...])

## 2. Base rate + simplest explanation
- Base rate: [figure or "guess — no reliable figure"]
- Simplest explanation: [...]

## 3. Evidence vs feeling
- Actually have (checkable): [...]
- Assuming: [...]
- Feelings as evidence: [...]

## 4. Disconfirmation
- Would prove me wrong quickly: [...]
- Strongest skeptic objection: [...]

## 5. Next action
- Smallest action: [...]
- STOP / GO (if committing): [decision + one-line reason]
```

---

## Example Output

```
# Quick Reality Check — "I should reply to this email right now while I'm angry"

## 1. Claim, falsifiably stated
- "Sending this reply now will improve the outcome of the situation." Testable
  by whether the thread de-escalates or escalates after I send.

## 2. Base rate + simplest explanation
- Base rate: guess — I don't have a figure, but angry same-minute replies
  rarely improve professional outcomes. Treat as low.
- Simplest explanation: I want to feel the relief of firing back, which isn't
  the same as improving the outcome.

## 3. Evidence vs feeling
- Actually have (checkable): the email's actual content and the deadline it cites.
- Assuming: that the sender intended the slight I'm reading into it.
- Feelings as evidence: "they're disrespecting me" — that's my reaction, not
  established fact.

## 4. Disconfirmation
- Would prove me wrong quickly: re-reading the email in an hour and finding it's
  neutral, not hostile.
- Strongest skeptic objection: "You're reacting to tone you inferred, and a
  same-minute angry reply usually costs more than it gains."

## 5. Next action
- Smallest action: draft the reply but don't send; reread in one hour.
- STOP / GO: STOP on sending now — low base rate of this helping, decision is
  effectively irreversible once sent.
```

---

## Verification

- [ ] Claim restated falsifiably (or non-falsifiability explained).
- [ ] Base rate given with a real figure or labeled a guess.
- [ ] Evidence separated cleanly from assumptions and feelings.
- [ ] Strongest skeptic objection named, realistic.
- [ ] Single smallest next action given; STOP/GO if a commitment is imminent.
- [ ] No reassurance, no invented base rate or consensus.

---

## Techniques Used
- **ST-01 (Clear Objective Statement):** Sets the model's job as fast grounding, explicitly not reassurance.
- **DS-02 (Metric Specification):** Drives base-rate reasoning and the evidence/feeling separation.
- **QA-02 (Adversarial Stress-Test):** Surfaces the strongest skeptic objection and disconfirming test.
- **RT-02 (Multi-Dimensional Analysis Framework):** Sorts the input across claim, evidence, feeling, and objection dimensions.
- **QA-04 (Uncertainty Acknowledgment):** Requires labeling any unsourced base rate as a guess.

---

## Related Prompts
- `domain-productivity/validation/validation_am_i_being_nuts.md` — escalate here when stakes are high or irreversible.
- `domain-productivity/validation/validation_disconfirmation_pass.md` — a deeper attack on the conclusion.
- `domain-productivity/validation/validation_reality_check.md` — ground the claim in what real experts would object to.
