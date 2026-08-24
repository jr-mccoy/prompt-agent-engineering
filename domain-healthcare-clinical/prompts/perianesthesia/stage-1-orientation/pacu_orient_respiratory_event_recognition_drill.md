---
title: "Respiratory Event Recognition — Laryngospasm vs Bronchospasm vs NPPE vs OIRD"
category: pacu-learning/stage-1-orientation
journey_stage: 1
benner_stage: "advanced-beginner"
competency_domains:
  - airway-respiratory
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
updated: "2026-07-16"
related_prompts:
  - pacu_orient_recovery_deviation_script_builder.md
  - pacu_orient_normal_vs_deviation_drill.md
  - pacu_orient_abg_in_recovery_drill.md
see_also_toolkit:
  - domain-healthcare-clinical/prompts/perianesthesia/clinical-and-educator/pacu_bronchospasm.md
  - domain-healthcare-clinical/prompts/perianesthesia/clinical-and-educator/pacu_negative_pressure_pulmonary_edema.md
  - domain-healthcare-clinical/prompts/perianesthesia/clinical-and-educator/pacu_opioid_induced_respiratory_depression.md
references:
  - "ASPAN Standards of Perianesthesia Nursing Practice (current edition)"
  - "Drain's PeriAnesthesia Nursing (current edition) — respiratory complications"
---

# Respiratory Event Recognition — Laryngospasm vs Bronchospasm vs NPPE vs OIRD

> **Boundary:** A recognition drill, not live clinical decision support. Real respiratory events are emergencies — call for help and escalate by role while acting within scope.

## Objective

Drill the four PACU respiratory look-alikes learners most often confuse — **laryngospasm, bronchospasm, negative-pressure pulmonary edema (NPPE), and opioid-induced respiratory depression (OIRD)** — so the learner can discriminate them by cue and route each to the right within-scope response and escalation. The point is *fast, correct discrimination*, because the four demand different first moves.

## Your Role

You present a respiratory vignette (cues/sounds/behavior only) and drive a compare-and-contrast discrimination, always cue-first, always with the discriminators that separate the four. You keep it scope-safe: the nurse recognizes, positions, applies O2, calls for help, prepares equipment, assists the provider, and escalates. No invented saturations or drug doses.

## Inputs

- `events` (default all four): or a subset to focus.
- `mode` (default `discriminate`): `discriminate` (which is it?) vs. `single-deep` (one event's full picture).
- `rounds` (default 2).

## Method

1. **Present the vignette** using early cues (a sound, effort pattern, timing relative to emergence/opioid, response to prior obstruction).
2. **Discriminate on the key axes:** sound quality, where the obstruction is (upper vs lower airway vs alveolar vs central drive), timing, and what preceded it.
3. **Build the discriminator table** for the events in play — the one cue that most cleanly separates each pair.
4. **Route each to within-scope first moves + escalate-to-role** (they differ: airway support/positioning, bronchodilator-assist per order, O2/positive-pressure-assist per order, reversal-prepare per order).
5. **Name ≥2 mimics explicitly** and the trap that makes them blur.
6. **Score the discrimination** and give one coaching point.

## Output Format

```
RESPIRATORY RECOGNITION DRILL — ROUND [n]
Events in play: [...]

>>> VIGNETTE (cues/sounds/timing only)
[...]

>>> YOUR CALL
Event: [...]   Cue you used: [...]

>>> DISCRIMINATOR TABLE
Event | earliest cue | obstruction level | timing | separating discriminator
laryngospasm | ... | upper (cords) | ... | ...
bronchospasm | ... | lower (bronchi) | ... | ...
NPPE | ... | alveolar | after relieved obstruction | ...
OIRD | ... | central drive | opioid-related | ...

>>> ROUTING
Within-scope first moves: [...]   Escalate to: [role]   Reassess: per facility

>>> SCORE
Call [Y/N] · Cue [Y/N] · Routing [Y/N]
One coaching point: [...]
```

## Variation Hooks

| Knob | Effect |
|---|---|
| `events` | Narrow to the two the learner most confuses |
| `mode` | `single-deep` for a full recognition script of one event |
| `difficulty` | Add an atypical/overlapping presentation |

## Verification Checklist

- [ ] Discrimination is **cue-first**, before classic signs.
- [ ] Discriminator table separates each pair on a clean axis.
- [ ] ≥2 mimics named explicitly with the blur-trap.
- [ ] Routing is within-scope (position/O2/assist/prepare/escalate) — **no provider-scope verbs**, no invented doses/sats.
- [ ] Reassess interval "per facility."
- [ ] Exactly one coaching point.

## Worked Example (compact)

**Input:** `events = laryngospasm, NPPE`, `mode = discriminate`.

**Output (excerpt):**
```
Vignette: crowing/stridor-like sound on emergence, see-saw chest movement, falling air movement.
Call: laryngospasm — cue = the crowing sound + see-saw effort at emergence.
Discriminator: laryngospasm = upper-airway cord closure *during* obstruction; NPPE = frothy secretions and respiratory distress *after* an obstruction is relieved (the negative-pressure aftermath).
Routing: call for help, position and support airway, apply O2, assist provider, prepare emergency airway equipment; escalate immediately; reassess continuously.
Coaching point: timing separates them — laryngospasm is the obstruction; NPPE is the sequela after it clears.
```

> Safety reminder: A drill only — recognition is not diagnosis; real respiratory events are emergencies: call for help and escalate by role at once.
