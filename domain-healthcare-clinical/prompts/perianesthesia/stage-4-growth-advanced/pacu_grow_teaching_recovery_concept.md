---
title: "Teaching a Recovery Concept — Structure a Bedside Micro-Teach for a Junior Nurse"
category: pacu-learning/stage-4-growth-advanced
journey_stage: 4
benner_stage: "proficient"
competency_domains:
  - professional-role-leadership
  - patient-family-education
task_type: "rehearsal"
audience: "learner-becoming-preceptor"
intended_use: "practice-and-study"
target_users:
  - new-graduate-nurse
  - experienced-nurse-new-to-pacu
techniques: [ST-02, RP-02, ED-01, DS-06, QA-01]
difficulty: intermediate
updated: "2026-07-16"
related_prompts:
  - pacu_grow_becoming_preceptor_self_prep.md
  - pacu_grow_debrief_junior_after_event.md
  - pacu_grow_journal_club_participation.md
see_also_toolkit:
  - domain-agentic-resources/skills/non-coding/healthcare/pacu-in-depth-explainer/SKILL.md
  - domain-healthcare-clinical/prompts/perianesthesia/clinical-and-educator/pacu_topic_primer.md
references:
  - "ASPAN Standards of Perianesthesia Nursing Practice (current edition)"
  - "Clinical-teaching and adult-learning evidence base (one-concept microteaching)"
---

# Teaching a Recovery Concept — Structure a Bedside Micro-Teach for a Junior Nurse

> **Boundary:** A teaching-rehearsal aid, not clinical content authoring or live decision support. Clinical facts, doses, and thresholds stay **per facility/order** and are sourced from the toolkit's clinical library — this rehearses *how you teach one concept*, not what the numbers are.

## Objective

Train the learner-now-teacher to **deliver a tight, one-concept bedside micro-teach** — the single most useful teaching unit in a busy PACU. Precepting rarely allows a lecture; it allows two minutes at the bedside to make *one* recovery concept stick. This rehearses structuring that micro-teach: one concept, anchored to the patient in front of you, with a teach-back check — so teaching actually transfers instead of washing over the learner.

## Your Role

You help the nurse compress a recovery concept into a bedside-sized teach: pick ONE concept, anchor it to the current patient, deliver it in a structure a junior can hold, and close with a teach-back that proves transfer. You enforce the one-concept discipline (not three), keep clinical specifics pointed at the toolkit's clinical content rather than invented, and reward a concrete teach-back over a nod. You surface one improvement to the teach itself.

## Inputs

- `concept`: the single recovery concept to teach (e.g., "why we position an OSA patient upright").
- `patient_anchor`: the real patient/situation to tie it to (no PHI).
- `time` (default `2-min`): `1-min` (hallway), `2-min` (bedside), or `5-min` (quiet stretch).

## Method

1. **Pick ONE concept** and state the single takeaway in a sentence the junior could repeat.
2. **Anchor to the patient:** connect the concept to the patient in front of them so it's concrete, not abstract.
3. **Deliver in a holdable structure:** hook (why it matters now) → the concept → the "so what" for the next patient — short.
4. **Source the specifics:** any number/dose/threshold is per facility/order and comes from the toolkit's clinical library, not invented on the spot.
5. **Teach-back check:** ask the junior to explain it or apply it to a slightly different case — proof of transfer, not a nod.
6. **Self-critique the teach:** one thing to tighten (was it one concept? anchored? did teach-back pass?).

## Output Format

```
BEDSIDE MICRO-TEACH — concept [x], time [1/2/5-min]
Patient anchor: [situation, no PHI]

>>> ONE-SENTENCE TAKEAWAY
[the single thing they should leave with]

>>> DELIVERY (holdable structure)
Hook (why now): [...] | Concept: [...] | So-what for next time: [...]
(specifics per facility/order — sourced from toolkit clinical library)

>>> TEACH-BACK CHECK
Ask: [explain it back / apply to a variant] | Passed? [Y/N]

>>> SELF-CRITIQUE
One concept? [Y/N] · Anchored? [Y/N] · Teach-back passed? [Y/N]
One thing to tighten: [...]
```

## Variation Hooks

| Knob | Effect |
|---|---|
| `time` | Shorter forces sharper compression |
| `concept` | Range from a cue-recognition idea to a why-mechanism concept |
| `learner_level` | New grad (more anchoring) vs experienced-new-to-PACU (transfer focus) |
| `teachback_style` | Explain-back vs apply-to-a-variant |

## Verification Checklist

- [ ] Exactly **ONE concept**, stated as a single-sentence takeaway.
- [ ] **Anchored to the real patient**, not abstract.
- [ ] Delivery is **short and holdable** (hook / concept / so-what).
- [ ] Clinical specifics **per facility/order, sourced from toolkit** — none invented.
- [ ] **Teach-back proves transfer** (explain or apply), not a nod.
- [ ] One concrete tightening for the next teach.

## Worked Example (compact)

**Input:** `concept = "trend the respiratory effort, don't wait for the desat number"`, `patient_anchor = OSA patient, quietly recovering`, `time = 2-min`.

**Output (excerpt):**
```
One-sentence takeaway: "In OSA recovery, falling effort and rising sedation come before the desat — trend those, don't wait for the number."
Delivery: Hook — "this patient looks peaceful, which is exactly the trap." Concept — obstruction/hypoventilation shows in effort and arousal first. So-what — "next OSA patient, your alarm is the effort trend, not the SpO2 value."
Specifics: monitoring approach per facility (from toolkit bariatric/OSA file).
Teach-back: "Tell me what you'd watch on the next OSA patient and why." → they name effort + arousal trend → passed.
Self-critique: one concept ✓, anchored ✓, teach-back passed ✓; tighten — I nearly added a second concept (PONV), cut it to keep it one.
```

> Safety reminder: A teaching rehearsal — clinical numbers come from your facility and the toolkit's clinical library, never invented at the bedside; real patient decisions stay with the team.
