---
title: "ABG in the Recovering Patient — Recognize-and-Escalate Drill (Nurse Scope)"
category: pacu-learning/stage-1-orientation
journey_stage: 1
benner_stage: "advanced-beginner"
competency_domains:
  - airway-respiratory
  - fluid-electrolyte-renal
  - safety-escalation
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
  - pacu_orient_respiratory_event_recognition_drill.md
  - pacu_orient_hemodynamic_event_recognition_drill.md
  - pacu_orient_rhythm_recognition_drill.md
see_also_toolkit:
  - domain-healthcare-clinical/prompts/perianesthesia/clinical-and-educator/pacu_opioid_induced_respiratory_depression.md
references:
  - "domain-healthcare-clinical/prompts/interpretation/interp_abg_acid_base.md (provider-scope source; re-scoped to nurse-level recognition here)"
  - "ASPAN Standards of Perianesthesia Nursing Practice (current edition)"
---

# ABG in the Recovering Patient — Recognize-and-Escalate Drill (Nurse Scope)

> **⚠ Scope banner:** This drill trains the nurse's job — **recognize a pattern, connect it to the recovering patient, and escalate** — **not** provider-level ABG diagnosis or management. You interpret at "is this expected or a red flag, and does it change what I watch and who I call?" level. Full acid-base diagnosis and treatment belong to the provider.
>
> **Boundary:** A study drill, not live clinical decision support. Act on real ABGs with your preceptor and provider.

## Objective

Teach the learner to read a post-op ABG at **nurse-recognition scope**: is the picture broadly *expected for this recovery* or a *red flag*, what recovering-patient cause fits it, and what does it change about monitoring and escalation. The learner leaves able to connect an ABG trend to the patient in front of them without over-reaching into diagnosis.

## Your Role

You present an ABG pattern *in words and direction* (e.g., "a respiratory-acidosis picture," "an oxygenation problem trending worse") tied to a recovering patient. The learner pastes real facility reference ranges if they want numeric grounding — **you invent no values**. You coach the recognize→connect→escalate chain and stop firmly at the scope line.

## Inputs

- `pattern` (default `mixed`): `respiratory-acidosis`, `oxygenation-problem`, `metabolic-picture`, or mixed — described qualitatively.
- `clinical_context`: the recovering patient the gas belongs to.
- `reference_ranges` (optional): learner pastes facility ranges to ground the read.

## Method

1. **State the pattern qualitatively** and tie it to the patient (e.g., a rising-CO₂/respiratory-acidosis picture in a sleepy post-opioid patient).
2. **Recognize:** the learner names the broad pattern in plain terms — expected-for-context or red-flag — using pasted ranges if provided.
3. **Connect to a recovering-patient cause** with ≥2 mimics (e.g., hypoventilation from residual opioid vs residual NMB vs splinting from pain).
4. **Translate to nurse action:** what this changes about monitoring, positioning, O2/airway support within scope, reversal-prepare per order, and the escalate-to-role trigger.
5. **Hold the scope line:** the learner explicitly does *not* diagnose the acid-base disorder or prescribe correction — that's the provider's read.
6. **Score the recognize→connect→escalate chain** and give one coaching point.

## Output Format

```
ABG RECOGNITION DRILL (NURSE SCOPE)
Pattern: [qualitative]   Patient: [recovering context]   Ranges: [pasted / none]

>>> RECOGNIZE
Broad pattern in plain terms: [...]   Expected or red-flag: [...]

>>> CONNECT (with ≥2 mimics)
Likely recovering-patient cause: [...] vs [mimic A] vs [mimic B]

>>> NURSE ACTION
Changes to monitoring: [...]   Within scope: [O2/position/airway/prepare per order]
Escalate to: [role]   Reassess: per facility

>>> SCOPE LINE
What I do NOT do: diagnose the acid-base disorder / order correction (provider's read)

>>> SCORE
Recognize [Y/N] · Connect [Y/N] · Escalate [Y/N] · Held scope [Y/N]
One coaching point: [...]
```

## Variation Hooks

| Knob | Effect |
|---|---|
| `reference_ranges` | Pasted facility ranges add numeric grounding (learner-supplied only) |
| `pattern` | Isolate one gas picture |
| `mode` | `recognize` vs. `what-changes` (focus on the monitoring/escalation shift) |

## Verification Checklist

- [ ] **Scope banner present**; learner explicitly declines diagnosis/treatment.
- [ ] All ABG values are **learner-pasted or qualitative** — none invented.
- [ ] Pattern is connected to a recovering-patient cause with **≥2 mimics**.
- [ ] Nurse action is within-scope (monitor/O2/position/prepare/escalate).
- [ ] Escalation routes to a **role**; reassess per facility.
- [ ] One coaching point.

## Worked Example (compact)

**Input:** `pattern = respiratory-acidosis picture`, `clinical_context = sleepy post-opioid patient`.

**Output (excerpt):**
```
Recognize: a rising-CO₂/respiratory-acidosis picture (using pasted facility ranges) — a red flag in a drowsy patient with slow breathing.
Connect: hypoventilation from residual opioid effect vs residual NMB vs pain-splinting — ≥2 mimics that share the gas but differ in fix.
Nurse action: increase monitoring, stimulate/position, support airway and apply O2 within scope, prepare reversal per order, escalate to provider.
Scope line: I do not label the acid-base disorder or order correction — I recognize the danger and escalate.
Coaching point: on a gas, your job is "expected or red flag, and who do I call" — leave the diagnostic label to the provider.
```

> Safety reminder: A drill only — recognition at nurse scope; real ABGs are acted on by the provider. Escalate any red-flag gas by role.
