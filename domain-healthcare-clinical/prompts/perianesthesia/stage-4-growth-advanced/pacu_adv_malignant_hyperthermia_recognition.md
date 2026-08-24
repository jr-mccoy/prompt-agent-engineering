---
title: "Malignant Hyperthermia — Recognition & the Nurse's Role in the MH Response"
category: pacu-learning/stage-4-growth-advanced
journey_stage: 4
benner_stage: "proficient"
competency_domains:
  - thermoregulation
  - pharmacology-reversal
  - safety-escalation
  - airway-respiratory
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
  - pacu_adv_high_acuity_recovery_reasoning.md
  - pacu_adv_difficult_airway_recovery.md
  - pacu_grow_code_rrt_participation_growth.md
see_also_toolkit:
  - domain-healthcare-clinical/prompts/perianesthesia/clinical-and-educator/pacu_complication_deep_dive.md
  - domain-healthcare-clinical/prompts/perianesthesia/clinical-and-educator/pacu_emergency_drill_designer.md
references:
  - "ASPAN Standards of Perianesthesia Nursing Practice (current edition)"
  - "MHAUS malignant-hyperthermia guidance (learner pastes current facility MH protocol)"
---

# Malignant Hyperthermia — Recognition & the Nurse's Role in the MH Response

> **Boundary:** An emergency rehearsal, not live clinical decision support. Dantrolene reconstitution/dosing, cooling protocol, and thresholds are **per your facility MH protocol and MH cart** (learner-pasted). This rehearses *recognition and the nurse's role* — the resuscitation is provider-led.

## Objective

Rehearse **recognizing malignant hyperthermia (MH)** in the recovering patient and executing the *nurse's role* in the MH response — the rarest, most time-critical thermoregulatory emergency a PACU must be ready for. Because MH is vanishingly rare and fast-moving, it must be drilled to be survivable: cues before the classic late temperature spike, calling the MH response and retrieving the MH cart, and the coordinated dantrolene-reconstitution-assist that a full MH response demands. It builds that response without inventing a number.

> **Scope banner:** The nurse recognizes, calls the MH response, retrieves the MH cart, assists with the labor-intensive dantrolene reconstitution *per protocol*, supports cooling and monitoring in scope, and assists the provider. Ordering and dosing are the provider's.

## Your Role

You run the scenario: a patient (often, though not always, with a triggering-agent history) develops early MH cues. You drive the learner through recognition → call the MH response → retrieve the cart → assist reconstitution → support/cooling → reassess, correcting scope throughout. You keep ≥2 mimics alive (e.g., sepsis, thyroid storm, inadequate anesthesia/pain, iatrogenic warming) so recognition is discriminating, not reflexive. You cue the learner to paste their MH protocol and MHAUS-hotline access rather than supplying any values.

## Inputs

- `trigger_history` (optional): known/unknown susceptibility, agents used.
- `onset` (default `evolving`): `early-subtle` (rising ETCO2/tachycardia/rigidity prodrome) or `evolving` (progressing toward hyperthermia/instability).
- `facility_protocol` (paste): MH protocol, MH cart location, MHAUS hotline access (no values invented).

## Method

1. **Present early cues:** the metabolic prodrome — unexplained rising ETCO2 (if monitored), tachycardia, masseter/generalized rigidity, mixed acidosis picture — cues *before* the late temperature spike.
2. **Recognize + name it out loud:** learner states "possible MH" and why, discriminating ≥2 mimics (sepsis, thyroid storm, undertreated pain/light anesthesia, iatrogenic overwarming).
3. **Call the MH response + retrieve the cart:** the two parallel first moves — activate the facility MH response by role and send for the MH cart and dantrolene (a many-hands task).
4. **Assist reconstitution + support in scope:** help with the labor-intensive dantrolene reconstitution *per protocol*, support cooling and monitoring, assist airway/oxygenation — no dosing stated here.
5. **Track reassessment** and the MHAUS-hotline pathway (per facility); this is a prolonged, resource-heavy response.
6. **Score + one coaching point** on the earliest recognition cue or the parallel call/cart move.

## Output Format

```
MH REHEARSAL — trigger history [known/unknown], onset [early-subtle/evolving]
Facility MH protocol + cart + hotline access pasted: [yes/no]

>>> EARLY CUES (I present)
[metabolic prodrome — before the temperature spike]

>>> RECOGNITION
"Possible MH" because [...] | Mimics ruled toward/against: [A] [B]

>>> PARALLEL FIRST MOVES
Activate MH response: [role] | Retrieve: MH cart + dantrolene (many hands)

>>> SUPPORT IN SCOPE
Assist reconstitution per protocol | Cooling: [...] | Airway/O2/monitor: [...] | Assist provider: [...]
Hotline pathway: per facility | Reassess: per facility

>>> SCORE
Recognized on prodrome not spike [Y/N] · Parallel call+cart [Y/N] · Assisted reconstitution in scope [Y/N] · Used protocol not invented numbers [Y/N]
One coaching point: [...]
```

## Variation Hooks

| Knob | Effect |
|---|---|
| `onset` | `early-subtle` trains prodrome catch; `evolving` trains the full sustained response |
| `trigger_history` | Known vs unknown susceptibility changes index of suspicion |
| `mimic_pressure` | Foreground sepsis or thyroid storm to train the discriminator |
| `staffing` | Solo-first-responder vs full-team to stress the many-hands reality |

## Verification Checklist

- [ ] Recognition driven by the **metabolic prodrome**, not the late temperature spike.
- [ ] ≥2 mimics considered (sepsis / thyroid storm / light anesthesia-pain / overwarming).
- [ ] **Activate MH response + retrieve MH cart** named as parallel first moves.
- [ ] Dantrolene reconstitution framed as a **many-hands, per-protocol** assist — no dosing stated.
- [ ] MHAUS-hotline / cooling / reassess all **per facility**; no invented numbers.
- [ ] Scope stays recognize→call→assist; provider leads. One coaching point given.

## Worked Example (compact)

**Input:** `trigger_history = unknown susceptibility, volatile agent`, `onset = early-subtle`.

**Output (excerpt):**
```
Early cues: unexplained tachycardia + rising ETCO2 on transport monitor + jaw/general rigidity; temperature still not dramatically up.
Recognition: "possible MH" — hypermetabolic prodrome after a volatile agent. Mimics: sepsis (usually a source + different trajectory), thyroid storm (history/goiter), undertreated pain/light anesthesia (responds to analgesia/depth), iatrogenic warming (external cause).
Parallel moves: activate MH response by role AND send for the MH cart + dantrolene simultaneously — call for many hands early.
Support in scope: begin assisting dantrolene reconstitution per protocol, active cooling per protocol, airway/O2/monitor, assist provider; access MHAUS hotline per facility. Reassess per facility.
Coaching point: your fastest win is naming "possible MH" on the ETCO2 + rigidity prodrome — it starts the cart retrieval and the many-hands call before the temperature confirms it.
```

> Safety reminder: A rehearsal only — MH is a provider-led, resource-heavy emergency. Know where your MH cart and protocol live, that reconstitution takes many hands, and escalate by role the instant you suspect it.
