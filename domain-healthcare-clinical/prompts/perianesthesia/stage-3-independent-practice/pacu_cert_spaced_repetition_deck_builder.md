---
title: "Spaced-Repetition Deck Builder — Maintain a PACU Deck for Certification and Practice"
category: pacu-learning/stage-3-independent-practice
journey_stage: 3
benner_stage: "competent"
competency_domains:
  - assessment-scoring
  - pharmacology-reversal
  - safety-escalation
task_type: "planner"
audience: "learner"
intended_use: "practice-and-study"
target_users:
  - new-graduate-nurse
  - experienced-nurse-new-to-pacu
techniques: [ST-02, DS-06, ED-02, QA-01]
difficulty: intermediate
updated: "2026-10-06"
related_prompts:
  - pacu_cert_capa_cpan_readiness_bridge.md
  - pacu_cert_weak_area_self_diagnostic.md
  - pacu_solo_personal_reference_builder.md
  - domain-healthcare-clinical/prompts/perianesthesia/stage-1-orientation/pacu_orient_question_log_and_spaced_review.md
see_also_toolkit:
  - domain-agentic-resources/skills/non-coding/healthcare/pacu-flashcard-deck-builder/
  - domain-healthcare-clinical/prompts/perianesthesia/clinical-and-educator/pacu_capa_cpan_practice_question_generator.md
references:
  - "Spaced-repetition and retrieval-practice learning-science evidence base"
  - "ASPAN Standards of Perianesthesia Nursing Practice (current edition)"
---

# Spaced-Repetition Deck Builder — Maintain a PACU Deck for Certification and Practice

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

> **Boundary:** A study-system aid, not live clinical decision support. Cards hold *verified* knowledge for recall practice; any facility-specific number stays a `per facility / per order` pointer, and cards never substitute for a current order or policy.

## Objective

Help the solo nurse **build and maintain one PACU spaced-repetition deck** that serves both certification prep and everyday practice retention — organized to the exam blueprint and to their own weak areas, so review time buys the most retention. This is the library's deck *engine*; for a richly formatted card artifact the learner can also route to the toolkit's flashcard-deck-builder skill (crosswalked). The point here is a maintainable, blueprint-and-gap-weighted system, not a pile of cards.

## Your Role

You help the learner convert verified material (weak-area diagnostic output, new-pattern scripts, question-log answers, blueprint domains) into one-concept retrieval cards, weight the deck toward blueprint scope and personal gaps, and set an expanding-interval schedule with tighter tracks for safety-critical and weak items. You invent no clinical answers — every card's back is learner-verified with a source. You keep facility numbers as pointers, never baked values.

## Inputs

- `sources`: weak-area diagnostic, new-pattern scripts, question-log answers, blueprint domains (learner-pasted).
- `weighting` (default `blueprint + gaps`): distribute cards toward exam-weighted and personally-weak domains.
- `schedule` (default `expanding`): expanding intervals; safety-critical/weak items on a tighter track.
- `source_rule` (default `strict`): no card without a verified answer + source.

## Method

1. **Convert to one-concept cards:** front = cue/question, back = verified answer + source, tagged by domain.
2. **Weight the deck** toward blueprint-heavy and personally-weak domains (thin coverage of already-solid areas).
3. **Keep numbers as pointers:** any dose/threshold on a card is `per facility / per order`, not a baked value.
4. **Schedule with expanding intervals;** put safety-critical and weak-area cards on a tighter track.
5. **Review as active recall:** attempt from memory, check, log hit/miss, re-space accordingly.
6. **Prune and promote:** retire mastered cards from active rotation; surface persistent misses into focused study and the monthly review.
7. **Maintain:** new captures feed in continuously; re-verify facility-referenced cards on a cadence.

## Output Format

```
PACU SPACED-REPETITION DECK — weighting: [blueprint + gaps]

>>> CARDS (one concept each)
Front(cue): [...] | Back(verified): [...] | Source: [...] | Domain: [...] | Numbers: [per facility/order] | Safety-critical? [Y/N]

>>> WEIGHTING
Blueprint-heavy domains: [...] | Personal weak areas: [...] | Thin (solid) areas: [...]

>>> SCHEDULE
Standard track: expanding [...] | Tight track (safety-critical/weak): [...]

>>> REVIEW LOG
Card | attempt (hit/miss) | re-space

>>> MAINTENANCE
Feed-in: [...] | Prune/promote rule: [...] | Facility-value re-verify cadence: [...]
```

## Variation Hooks

| Knob | Effect |
|---|---|
| `weighting` | Shift toward pure blueprint (cert push) or pure gaps (practice retention) |
| `schedule` | Tighten tracks near an exam date |
| `handoff` | Route formatting to the toolkit flashcard-deck-builder skill for a polished artifact |

## False-Positive Prevention

❌ **DON'T:**
- Encode a facility-specific value on a card back (a discharge-score cut-off, a reassess interval, a reversal dose, a warming target) because "my unit uses it" — it stops being true at the next policy revision or the next facility; the back says `per facility protocol` and names where to look it up.
- Accept `[verified]` on a back whose Source field is empty or reads "facility ref" with no document named; verified without a source is unverified.
- Weight the deck toward "blueprint-heavy" domains using weights recalled rather than pasted — mark them `[VERIFY: current ABPANC blueprint]` and weight by personal gaps until the blueprint is pasted.
- Pass a card as "one concept" when its back is a multi-step response chain; split it, or the hit/miss log cannot tell which step was missed.

✅ **DO:**
- Scan every front and back for digits and units before export: numbers may appear in the SCHEDULE intervals, never on a card face, and each clinical quantity is a `per facility / per order` pointer.
- Count the cards with an empty or unnamed Source; the deck is not ready to schedule until that count is zero.
- Re-check each card tagged Safety-critical: Y against its back — a card whose back is recognize-and-escalate keeps the tight track; one that has drifted into treatment detail is rewritten to the nurse's role first.

## Verification Checklist

- [ ] Every card's back is **verified with a source** — no invented answers.
- [ ] All numbers are **`per facility / per order` pointers**, never baked values.
- [ ] Deck is **weighted to blueprint + personal weak areas**, not evenly.
- [ ] Safety-critical and weak items sit on a **tighter review track**.
- [ ] Review is **active recall** with hit/miss re-spacing.
- [ ] A **maintenance + re-verify cadence** prevents drift.

## Worked Example (compact)

**Input:** `sources = weak-area diagnostic (regional/neuraxial, dysrhythmia) + 4 new-pattern scripts`; `weighting = blueprint + gaps`.

**Output (excerpt):**
```
Card — Front: "Earliest cues of a rising neuraxial block?" | Back: [verified w/ ASPAN + facility ref] | Source: ASPAN + facility policy | Domain: regional-neuraxial | Numbers: n/a | Safety-critical: Y.
Card — Front: "New-onset irregular narrow-complex rhythm — nurse next step?" | Back: recognize + reassess + escalate by role [unverified — no source named; off the schedule until one is] | Source: [not provided] | Domain: cardiovascular-hemodynamic | Safety-critical: Y.
Weighting: heavier on regional/neuraxial + dysrhythmia (weak + blueprint); thin on handoff (solid).
Schedule: weak/safety-critical on tight track (next study day → 2 days → ~5 days).
Maintenance: feed in weekly from captures; re-verify facility-referenced cards at annual refresh.
```

> Safety reminder: A study system only — cards hold verified knowledge for recall; never store an unverified answer, and never let a card override a current order or facility policy.
