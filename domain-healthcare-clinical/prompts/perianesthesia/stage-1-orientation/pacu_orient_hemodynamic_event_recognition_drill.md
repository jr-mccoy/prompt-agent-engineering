---
title: "Hemodynamic Event Recognition — Hypotension / Hypertension / Dysrhythmia"
category: pacu-learning/stage-1-orientation
journey_stage: 1
benner_stage: "advanced-beginner"
competency_domains:
  - cardiovascular-hemodynamic
  - safety-escalation
  - pharmacology-reversal
task_type: "drill"
audience: "learner"
intended_use: "practice-and-study"
target_users:
  - new-graduate-nurse
  - experienced-nurse-new-to-pacu
techniques: [ST-02, RT-02, RT-05, DS-06, QA-04, QA-01]
difficulty: intermediate
updated: "2026-10-06"
related_prompts:
  - pacu_orient_recovery_deviation_script_builder.md
  - pacu_orient_rhythm_recognition_drill.md
  - pacu_orient_prioritization_rule_drill.md
see_also_toolkit:
  - domain-healthcare-clinical/prompts/perianesthesia/clinical-and-educator/pacu_post_op_hypertension.md
  - domain-healthcare-clinical/prompts/perianesthesia/clinical-and-educator/pacu_dysrhythmia_recognition.md
  - domain-healthcare-clinical/prompts/perianesthesia/clinical-and-educator/pacu_drug_vasopressors_reference.md
references:
  - "ASPAN Standards of Perianesthesia Nursing Practice (current edition)"
  - "Drain's PeriAnesthesia Nursing (current edition) — cardiovascular recovery"
---

# Hemodynamic Event Recognition — Hypotension / Hypertension / Dysrhythmia

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

> **Boundary:** A recognition drill, not live clinical decision support. Manage real hemodynamics with your preceptor, provider order, and facility protocol.

## Objective

Drill the learner to recognize the common post-op hemodynamic patterns and — the Stage-1 discipline — **hunt the reversible cause before assuming a drug is the answer**. The learner practices mapping a BP/HR/rhythm trend to its likeliest fixable cause, the within-scope response, and the escalate-to-role trigger.

## Your Role

You present a hemodynamic trend (direction and cues, never invented numbers) and run a reversible-cause-first analysis. You always surface ≥2 mimics that share the same reading but need opposite fixes. You keep it scope-safe — the nurse checks, addresses fixable causes within scope, prepares/assists, and escalates; the nurse does not order or titrate vasoactives.

## Inputs

- `pattern` (default `mixed`): `hypotension`, `hypertension`, `tachycardia`, `bradycardia`, `dysrhythmia`, or mixed.
- `surgical_context` (optional).
- `rounds` (default 2).

## Method

1. **Present the trend** (rising/falling across checks + accompanying cues — pain behavior, bladder, temperature/shivering, bleeding signs, emergence).
2. **Reversible causes first:** the learner lists the fixable causes *before* any pharmacologic framing (pain, full bladder, hypoventilation/hypoxia, hypovolemia/bleeding, temperature, residual anesthetic/vasodilation, anxiety/emergence).
3. **Map cause → nurse check → within-scope action → escalate-to-role.**
4. **Run ≥2 mimics:** same reading, different fix (e.g., hypotension from hypovolemia vs from residual vasodilation).
5. **Set the escalation trigger:** persistent trend after fixable causes addressed, or any unstable pattern → escalate now.
6. **Introduce dysrhythmia at recognition level** (recognize + escalate; deep rhythm work lives in the rhythm drill). Score and give one coaching point.

## Output Format

```
HEMODYNAMIC RECOGNITION DRILL — ROUND [n]
Pattern: [...]   Context: [...]

>>> TREND (direction + cues, no numbers)
[...]

>>> REVERSIBLE CAUSES FIRST
[category list]

>>> CAUSE MAP
cause → what I check → within-scope action → escalate to [role]

>>> MIMICS (same reading, different fix)
[A] vs [B]

>>> ESCALATION TRIGGER
[persistent trend / instability] → escalate now

>>> SCORE
Reversible-first [Y/N] · Mimics [Y/N] · Scope-safe [Y/N]
One coaching point: [...]
```

## Variation Hooks

| Knob | Effect |
|---|---|
| `pattern` | Isolate one pattern for depth |
| `surgical_context` | Bleeding-risk cases raise the hypovolemia lens |
| `mode` | `cause-hunt` vs. `escalate-or-watch` decision framing |

## False-Positive Prevention

❌ **DON'T:**
- Score `Reversible-first: Y` because a cause list sits above the cause map when a pressor, a fluid bolus, or an antihypertensive is already named in the trend narrative, the mimic text, or the coaching point.
- Count a mimic pair whose halves need the same response ("hypovolemia vs bleeding" is one cause twice) — a pair counts only when the fix or the urgency differs.
- List a reversible cause that cannot produce the presented direction of BP and HR change just to lengthen the list; padding reads as thoroughness.
- Turn "falling" or "rising" into a numeric cut-off or a pressure target to make the escalation trigger feel concrete — it stays `per facility protocol` / `per provider order`.

✅ **DO:**
- Check every cause-map row: could the item in "what I check" actually confirm or exclude that cause (dressing/drain output for bleeding, bladder assessment for retention)? A row whose check cannot discriminate scores N.
- Read `Scope-safe [Y/N]` against every verb in the output, including mimic and coaching lines — "titrate", "start", "bolus", "give" without `per provider order` makes it N.
- For a dysrhythmia round, confirm the output stops at recognize + patient stability + escalate and hands off to the rhythm drill without naming a treatment.

## Verification Checklist

- [ ] Reversible causes listed **before** any pharmacologic framing.
- [ ] Each cause maps to nurse check → within-scope action → escalate-by-role.
- [ ] ≥2 mimics (same reading, different fix).
- [ ] **No BP/HR numbers or thresholds invented**; no order/titrate verbs.
- [ ] Dysrhythmia kept at recognize-and-escalate.
- [ ] Reassess/escalation trigger stated; one coaching point.

## Worked Example (compact)

**Input:** `pattern = hypotension`, `surgical_context = abdominal with blood loss`.

**Output (excerpt):**
```
Trend: BP trending down across checks with rising heart rate and pale, cool cues.
Reversible causes first: hypovolemia/bleeding, residual vasodilation, hypoventilation, pain-then-vagal.
Cause map: hypovolemia → check dressing/drain output, perfusion cues, trend → within scope: position, ensure IV access/fluids per order, monitor closely → escalate to provider now given the bleeding context.
Mimics: falling BP from ongoing bleeding (needs source control/escalation) vs from residual vasodilation (often improves as anesthetic wears) — same reading, very different urgency.
Coaching point: in a bleeding-risk case, a downward BP trend with a rising HR is escalate-now, not watch-and-wait.
```

> Safety reminder: A drill only — hunt causes here, but manage real hemodynamics with your preceptor and provider order; escalate instability by role immediately.
