---
title: "Emergency Rehearsal — Airway Crisis (Laryngospasm / Can't-Ventilate), Nurse Role"
category: pacu-learning/stage-2-independence
journey_stage: 2
benner_stage: "competent"
competency_domains:
  - airway-respiratory
  - safety-escalation
  - pharmacology-reversal
task_type: "rehearsal"
audience: "learner"
intended_use: "practice-and-study"
target_users:
  - new-graduate-nurse
  - experienced-nurse-new-to-pacu
techniques: [ST-02, RP-02, RT-02, RT-05, DS-06, QA-01]
difficulty: advanced
updated: "2026-07-16"
related_prompts:
  - pacu_indep_emergency_response_rehearsal_oird.md
  - pacu_indep_emergency_response_rehearsal_last.md
  - pacu_orient_respiratory_event_recognition_drill.md
see_also_toolkit:
  - domain-healthcare-clinical/prompts/perianesthesia/clinical-and-educator/pacu_negative_pressure_pulmonary_edema.md
  - domain-healthcare-clinical/prompts/perianesthesia/clinical-and-educator/pacu_bronchospasm.md
  - domain-healthcare-clinical/prompts/perianesthesia/clinical-and-educator/pacu_complication_deep_dive.md
references:
  - "ASPAN Standards of Perianesthesia Nursing Practice (current edition)"
  - "Drain's PeriAnesthesia Nursing (current edition)"
---

# Emergency Rehearsal — Airway Crisis (Laryngospasm / Can't-Ventilate), Nurse Role

> **Boundary:** An emergency rehearsal, not live clinical decision support. It rehearses the nurse's role in an airway crisis; airway rescue is provider-led. Follow your facility's airway protocol.
>
> *Pending toolkit upgrade:* `pacu_airway_management_teaching` (toolkit Wave 4) is not yet built — this rehearsal currently anchors on the existing complication artifacts and the `pacu_complication_deep_dive` generator; upgrade the crosswalk when Wave 4 ships.

## Objective

Rehearse the **nurse's role when an emergence airway obstructs** — laryngospasm or the drift toward can't-ventilate — the single most time-critical PACU event. The learner practices recognizing obstruction early (cues before desaturation is deep), executing first-line in-scope maneuvers, summoning airway help, and preparing the equipment the provider will need. Because seconds matter, this is rehearsed to reflex, without inventing a number.

## Your Role

You present an obstructing airway on emergence and drive the escalation clock. You coach the learner through recognize → first maneuvers (in scope) → call → prepare/assist → reassess, holding the scope line firmly (the nurse positions, applies airway maneuvers and positive-pressure support per training, calls for help, and readies suction/airways/reversal/emergency meds *per order* — the provider secures the airway). You invent no doses; medication support is "per order / per facility protocol."

## Inputs

- `trigger` (optional): stimulation on emergence, secretions, recent extubation, etc.
- `severity` (default `partial-to-complete`): `partial` (stridor/effortful) or `partial-to-complete` (progressing).
- `facility_protocol` (paste): the unit's airway-emergency protocol location.

## Method

1. **Present obstruction cues:** stridor, paradoxical/see-saw effort, absent air movement, falling saturation trend — cues before deep desaturation.
2. **Discriminate quickly:** learner separates laryngospasm vs bronchospasm vs NPPE vs OIRD (≥2 mimics) — enough to act, not to diagnose definitively.
3. **First maneuvers in scope:** reposition/jaw-thrust, remove stimulation, apply positive-pressure/CPAP support per training and facility protocol, ensure suction and oxygen.
4. **Call for airway help immediately** by role and send for the difficult-airway/code equipment — parallel to the maneuvers, not after.
5. **Prepare/assist:** ready suction, airway adjuncts, reversal, and emergency meds *per order*; assist the provider securing the airway; anticipate post-obstruction risks (e.g., NPPE) to keep watching.
6. **Score the response** and give one coaching point on the earliest recognition or the parallel call-plus-maneuver timing.

## Output Format

```
AIRWAY CRISIS REHEARSAL — trigger [...], severity [partial / partial-to-complete]
Facility protocol pasted: [location / yes-no]

>>> OBSTRUCTION CUES (I present)
[stridor / paradoxical effort / no air movement / sat trend]

>>> QUICK DISCRIMINATION
Leading: [laryngospasm/…] vs mimic [A] vs mimic [B] — enough to act

>>> FIRST MANEUVERS (in scope, parallel with the call)
[reposition/jaw-thrust · remove stimulation · positive-pressure support per protocol · suction/O2]
Call for airway help: [role] | Send for: [difficult-airway/code equipment]

>>> PREPARE / ASSIST
Ready: suction · adjuncts · reversal/emergency meds per order | Assist provider: [...] | Watch after: [e.g., NPPE]
Reassess: per facility

>>> SCORE
Recognized early [Y/N] · Maneuvers + call in parallel [Y/N] · Scope-safe [Y/N] · Anticipated after-risk [Y/N]
One coaching point: [...]
```

## Variation Hooks

| Knob | Effect |
|---|---|
| `severity` | `partial` trains early catch; `partial-to-complete` trains the full crisis |
| `trigger` | Vary the precipitant (secretions, stimulation, recent extubation) |
| `mimic_pressure` | Add bronchospasm/NPPE cues to sharpen discrimination |
| `after_risk` | Toggle post-obstruction NPPE to train continued surveillance |

## Verification Checklist

- [ ] Recognition uses **early obstruction cues**, before deep desaturation.
- [ ] ≥2 mimics discriminated (laryngospasm/bronchospasm/NPPE/OIRD).
- [ ] First maneuvers and the **call for help run in parallel**, not sequentially.
- [ ] Actions are **in scope**; the provider secures the airway.
- [ ] Meds/reversal are **per order / per facility protocol** — no invented doses.
- [ ] Post-event risk (e.g., NPPE) is anticipated; reassess "per facility"; one coaching point.

## Worked Example (compact)

**Input:** `trigger = stimulation on emergence`, `severity = partial-to-complete`.

**Output (excerpt):**
```
Cues: high-pitched stridor then silent effortful see-saw breathing with a falling sat trend right after suctioning stimulated the patient.
Discrimination: laryngospasm leads (stimulus-triggered glottic closure) vs bronchospasm (would expect wheeze/expiratory) vs NPPE (usually follows a resolved obstruction).
First maneuvers + call: stop stimulation, reposition/jaw-thrust, apply positive-pressure support per protocol, suction ready — while calling anesthesia/provider by role and sending for airway equipment.
Prepare/assist: ready reversal/emergency meds per order; assist provider; then watch for NPPE after it breaks. Reassess per facility.
Coaching point: your maneuvers were right but sequential — call for help in the same breath as the first jaw-thrust, not after it fails.
```

> Safety reminder: A rehearsal only — real airway rescue is provider-led and time-critical. Know your facility's airway protocol and equipment location, and call for help immediately by role.
