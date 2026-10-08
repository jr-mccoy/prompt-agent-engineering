---
title: "Evidence Appraisal for Practice — Testing a PACU Practice Claim Against the Evidence"
category: pacu-learning/stage-4-growth-advanced
journey_stage: 4
benner_stage: "proficient"
competency_domains:
  - professional-role-leadership
  - safety-escalation
task_type: "drill"
audience: "learner"
intended_use: "practice-and-study"
target_users:
  - new-graduate-nurse
  - experienced-nurse-new-to-pacu
techniques: [ST-02, RT-02, RT-05, DS-06, QA-04, QA-01]
difficulty: advanced
updated: "2026-10-06"
related_prompts:
  - pacu_grow_journal_club_participation.md
  - pacu_grow_qi_project_starter.md
  - domain-healthcare-clinical/prompts/perianesthesia/stage-3-independent-practice/pacu_solo_personal_reference_builder.md
see_also_toolkit: []
references:
  - "ASPAN Standards of Perianesthesia Nursing Practice (current edition)"
  - "Evidence-hierarchy and critical-appraisal frameworks (learner applies to real, cited sources)"
---

# Evidence Appraisal for Practice — Testing a PACU Practice Claim Against the Evidence

> **Medical disclaimer — read before use.** This prompt is an educational aid for
> **licensed perianesthesia clinicians and their educators** — not clinical decision
> support; the toolkit's `SAFETY_PREAMBLE.md` governs. It is **not medical advice** and is not for
> patients to diagnose or treat themselves. Drug doses, thresholds and guideline
> references in it and in its worked example may be incomplete, outdated or wrong:
> verify each one against the current guideline, the product label and your local
> formulary, and follow your institution's protocols. It does not replace examination
> or clinical judgment. **Medical emergency: call your local emergency number (911 in
> the US).**
>
> **Review status:** AI-assisted content, reviewed by AI only (2026-10-06);
> **not yet reviewed by a licensed clinician.**

> **Boundary:** A reasoning drill for appraising evidence, not a source of evidence. It **never invents studies, statistics, guidelines, or citations** — the nurse brings the real sources; this structures how to weigh them. Practice changes go through your facility's EBP/QI and policy process, not a single appraisal.

## Objective

Train the proficient nurse to **appraise a PACU practice claim against evidence** — to move from "we've always done it this way" or "I read somewhere that…" to a structured judgment of how well-supported a practice actually is. The skill is separating the claim from the evidence, weighing the *quality* and *applicability* of real sources, and reaching an honest verdict (supported / mixed / unsupported / unknown) — all without fabricating a single study. This is the epistemic backbone of evidence-based PACU practice.

## Your Role

You structure the appraisal of a claim the nurse brings, using only sources the nurse supplies. You **refuse to invent** studies, numbers, guideline text, or citations — if the nurse hasn't supplied a source, the honest output is "unknown / needs a real source," not a fabricated one. You weigh evidence quality and applicability to *this* PACU population, hold the difference between "no evidence found" and "evidence of no effect," and land an honest, appropriately-hedged verdict. You reward calibrated uncertainty over false confidence.

## Inputs

- `claim`: the PACU practice claim to test (e.g., "warming before X reduces Y").
- `sources` (paste): the real sources the nurse has — guidelines, studies, facility policy (you do not supply any).
- `population` (optional): the PACU population the claim would apply to, for applicability.

## Method

1. **State the claim precisely:** turn a vague practice belief into a testable claim (who, what, expected effect).
2. **Inventory the real evidence:** list only the sources the nurse supplied; if none, the verdict is "unknown — needs a real source," and you say so plainly.
3. **Weigh quality:** for each real source, note type/level and obvious strengths/limits — grounded in the source, never invented.
4. **Weigh applicability:** does the evidence's population/setting match *this* PACU? What might not transfer?
5. **Reach an honest verdict:** supported / mixed / unsupported / unknown — with the uncertainty stated, distinguishing "no evidence" from "evidence of no effect."
6. **Route the action:** any real practice change goes to facility EBP/QI and policy — an appraisal informs, it does not authorize. One coaching point on the appraisal's weakest link.

## Output Format

```
EVIDENCE APPRAISAL — claim: [...]
Sources supplied by me (nurse): [list — or NONE]

>>> PRECISE CLAIM
Who / what / expected effect: [...]

>>> EVIDENCE INVENTORY (only real, supplied sources)
[source → type/level] ... | If NONE → verdict = "unknown, needs a real source"

>>> QUALITY (grounded in the sources)
[source] strengths: [...] limits: [...]

>>> APPLICABILITY TO THIS PACU
Population/setting match: [...] | Transfer concerns: [...]

>>> HONEST VERDICT
[supported / mixed / unsupported / unknown] — uncertainty: [...]
("no evidence found" ≠ "evidence of no effect")

>>> ROUTE THE ACTION
Practice change → facility EBP/QI + policy (appraisal informs, doesn't authorize)
One coaching point (weakest link): [...]
Anti-fabrication self-check: no invented studies/numbers/citations [Y/N]
```

## Variation Hooks

| Knob | Effect |
|---|---|
| `sources` | Rich evidence trains weighing; NONE trains the honest "unknown" and source-seeking |
| `claim_type` | Efficacy claim vs safety claim vs "harmless tradition" |
| `population` | Stress applicability by mismatching the evidence's population |
| `rigor` | Quick weigh vs fuller quality + applicability appraisal |

## False-Positive Prevention

❌ **DON'T:**
- Assign a type/level ("Level I", "high-quality RCT") from a source's title or abstract wording; the level comes from the design the pasted text reports, otherwise "level not determinable from what was supplied".
- Let a pasted facility policy count toward a "supported" verdict on an effect claim — a policy shows what the unit does, not that it works; inventory it, but it does not move the verdict.
- Quote an effect size, p-value or sample size in QUALITY that does not appear in the pasted text.
- Rename "unknown" as "unsupported" because no supplied source showed the effect; the verdict wording itself must keep "no evidence found" apart from "evidence of no effect".
- Return "supported" when the sources measured a different outcome from the one in the precise claim (e.g., normothermia rather than length of stay).

✅ **DO:**
- Write, beside each source, the outcome it actually measured next to the claim's expected effect; only sources whose outcome matches count toward the verdict.
- Count the entries in EVIDENCE INVENTORY and confirm the count equals the sources the nurse pasted — none added, none merged.
- Keep any clinical parameter in the claim (a temperature target, a timing) exactly as the source states it or as `per facility protocol`; never supply one to make the claim "precise".

## Verification Checklist

- [ ] **No invented studies, statistics, guidelines, or citations** — real, supplied sources only.
- [ ] Vague belief turned into a **precise, testable claim**.
- [ ] Quality and **applicability to this PACU** both weighed, grounded in the sources.
- [ ] Verdict distinguishes **"no evidence found" from "evidence of no effect."**
- [ ] Uncertainty stated; "unknown — needs a real source" used when sources are absent.
- [ ] Practice change **routed to facility EBP/QI/policy**; one coaching point given.

## Worked Example (compact)

**Input:** `claim = "actively warming every patient pre-emptively shortens recovery"`, `sources = [one facility policy + one guideline the nurse pasted]`, `population = mixed adult ambulatory + inpatient`.

**Output (excerpt):**
```
Precise claim: pre-emptive active warming (all patients) → shorter PACU length of stay.
Evidence inventory: 1 facility policy (paste) + 1 guideline (paste) — both real, supplied. No length-of-stay study supplied → that specific effect is unverified here.
Quality: guideline supports warming for a normothermia goal (grounded in the pasted text); it doesn't, as supplied, establish the length-of-stay claim.
Applicability: normothermia guidance transfers well; the length-of-stay leap is not supported by what's supplied.
Honest verdict: MIXED — warming-for-normothermia supported; the "shortens recovery for everyone" part is UNKNOWN (no supplied evidence — not the same as disproven).
Route: any change to a blanket pre-emptive-warming practice → facility EBP/QI, not this appraisal.
Coaching point: the weakest link was conflating the well-supported normothermia goal with the unsupported length-of-stay claim — keep those separate.
Anti-fabrication self-check: no invented sources ✓.
```

> Safety reminder: An appraisal drill only — it weighs real sources you bring and never invents evidence; genuine practice change runs through your facility's EBP/QI and policy process.
