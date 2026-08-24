---
title: "Common PACU Rhythms — Recognize-and-Escalate Drill (Nurse Scope)"
category: pacu-learning/stage-1-orientation
journey_stage: 1
benner_stage: "advanced-beginner"
competency_domains:
  - cardiovascular-hemodynamic
  - safety-escalation
  - assessment-scoring
task_type: "drill"
audience: "learner"
intended_use: "practice-and-study"
target_users:
  - new-graduate-nurse
  - experienced-nurse-new-to-pacu
techniques: [ST-02, RT-02, DS-06, QA-04, QA-01]
difficulty: intermediate
updated: "2026-07-16"
related_prompts:
  - pacu_orient_hemodynamic_event_recognition_drill.md
  - pacu_orient_abg_in_recovery_drill.md
  - pacu_orient_recovery_deviation_script_builder.md
see_also_toolkit:
  - domain-healthcare-clinical/prompts/perianesthesia/clinical-and-educator/pacu_dysrhythmia_recognition.md
references:
  - "domain-healthcare-clinical/prompts/interpretation/interp_ecg_full_interpretation.md (provider-scope source; re-scoped to nurse-level recognition here)"
  - "ASPAN Standards of Perianesthesia Nursing Practice (current edition)"
---

# Common PACU Rhythms — Recognize-and-Escalate Drill (Nurse Scope)

> **⚠ Scope banner:** This drill trains **rhythm recognition and escalation at nurse scope** — "is this the baseline, a benign change, or a dangerous change, and who do I call?" It is **not** 12-lead mastery or dysrhythmia diagnosis/management. Rhythm interpretation for treatment belongs to the provider.
>
> **Boundary:** A study drill, not live clinical decision support. Respond to real rhythms with your preceptor, provider, and facility protocol.

## Objective

Train the learner to recognize the rhythms they actually see in PACU, sort them into **baseline / benign-change / dangerous-change**, and escalate appropriately — pairing the strip with *how the patient looks*, because a rhythm is only as urgent as the patient attached to it.

## Your Role

You describe a rhythm change *in words* (rate direction, regularity, a described feature) alongside the patient's cues, and drive a recognize→stability-check→escalate chain. You do not require the learner to name every ECG criterion; you require them to sort urgency and act within scope. No invented rates or measurements — descriptions and "per facility" only.

## Inputs

- `rhythm_family` (default `mixed`): `sinus-change`, `atrial` (e.g., irregularly-irregular pattern), `ectopy`, `bradycardia`, `tachycardia`, `dangerous-wide/absent`.
- `patient_cues`: how the patient looks with the rhythm (the stability signal).
- `rounds` (default 2).

## Method

1. **Present rhythm-in-words + patient cues** (e.g., "an irregularly-irregular pattern in an otherwise stable, comfortable patient").
2. **Recognize the family** in plain terms (not full diagnosis) and whether it's *new vs baseline*.
3. **Stability check first:** the learner reads the *patient*, not just the monitor — perfusion, arousal, symptoms — because stability sets urgency.
4. **Sort urgency:** baseline / benign-change-monitor / dangerous-change-escalate-now, with ≥2 mimics (a benign-looking change that's dangerous in context, and vice versa).
5. **Route within scope:** monitor + assess + prepare + call for help + escalate-to-role; the nurse does not interpret-to-treat or deliver provider-scope interventions unsupervised.
6. **Score** and give one coaching point.

## Output Format

```
RHYTHM RECOGNITION DRILL (NURSE SCOPE) — ROUND [n]
Rhythm family: [...]   Patient cues: [...]

>>> RECOGNIZE (plain terms)
Family: [...]   New or baseline: [...]

>>> STABILITY CHECK (read the patient)
Perfusion/arousal/symptom cues: [...]  → stable / unstable

>>> URGENCY SORT
[baseline / benign-monitor / dangerous-escalate-now]
Mimics: [benign-look-but-dangerous] vs [scary-look-but-stable]

>>> ROUTING
Within scope: [monitor/assess/prepare/call-for-help]   Escalate to: [role]   Reassess: per facility

>>> SCORE
Recognize [Y/N] · Stability-first [Y/N] · Urgency [Y/N] · Held scope [Y/N]
One coaching point: [...]
```

## Variation Hooks

| Knob | Effect |
|---|---|
| `rhythm_family` | Isolate one family for repetition |
| `patient_cues` | Flip stability to show how the *same strip* changes urgency |
| `mode` | `sort-urgency` vs. `stable-or-not` fast triage |

## Verification Checklist

- [ ] **Scope banner present**; no diagnosis-to-treat, no 12-lead mastery claims.
- [ ] **Stability of the patient is checked before urgency is assigned.**
- [ ] Urgency sorted into baseline / benign / dangerous with **≥2 mimics**.
- [ ] **No invented rates/measurements** — descriptions and "per facility."
- [ ] Routing within-scope + escalate-by-role.
- [ ] One coaching point.

## Worked Example (compact)

**Input:** `rhythm_family = atrial`, `patient_cues = stable, comfortable, well-perfused`.

**Output (excerpt):**
```
Recognize: an irregularly-irregular pattern, appears new versus a regular baseline.
Stability check: patient well-perfused, alert, no symptoms → currently stable.
Urgency sort: benign-change-monitor now, but escalate promptly because it's *new* and post-op — new-onset matters even when stable.
Mimics: a new irregular rhythm in a stable patient (monitor + escalate for new onset) vs the same pattern with poor perfusion/symptoms (dangerous-escalate-now).
Routing: monitor closely, assess the patient, prepare, notify provider of the new rhythm; reassess per facility.
Coaching point: read the patient first — but "new" post-op rhythms get escalated even when the patient looks fine.
```

> Safety reminder: A drill only — recognition at nurse scope; provider interprets rhythms for treatment. Escalate any new or unstable rhythm by role.
