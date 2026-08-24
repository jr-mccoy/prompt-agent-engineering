---
title: "Emergency Rehearsal — LAST Recognition & Nurse Role in the Response"
category: pacu-learning/stage-2-independence
journey_stage: 2
benner_stage: "competent"
competency_domains:
  - regional-neuraxial
  - pharmacology-reversal
  - cardiovascular-hemodynamic
  - safety-escalation
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
  - pacu_indep_emergency_response_rehearsal_airway.md
  - pacu_indep_emergency_response_rehearsal_oird.md
  - pacu_indep_escalation_decision_drill.md
see_also_toolkit:
  - domain-healthcare-clinical/prompts/perianesthesia/clinical-and-educator/pacu_last_recognition_response.md
references:
  - "ASPAN Standards of Perianesthesia Nursing Practice (current edition)"
  - "ASRA local-anesthetic-systemic-toxicity guidance (learner pastes current facility protocol)"
---

# Emergency Rehearsal — LAST Recognition & Nurse Role in the Response

> **Boundary:** An emergency rehearsal, not live clinical decision support. Doses, lipid-emulsion protocol, and thresholds are **per your facility protocol** — paste your unit's real material; this rehearses *your role*, not the orders.

## Objective

Rehearse **recognizing local-anesthetic systemic toxicity (LAST)** early and executing the *nurse's role* in the response — the low-frequency, high-stakes event a regional-heavy PACU must be ready for. Because LAST is rare, it must be rehearsed to be fast: cues before the classic cardiovascular collapse, calling for help and the LAST/lipid-emulsion kit, and supporting the provider-led resuscitation. This builds that muscle memory without inventing a single number.

## Your Role

You run the scenario: a patient who received a regional/neuraxial or infiltration block develops early LAST cues. You prompt the learner through recognition → call → prepare → assist → reassess, correcting scope (the nurse recognizes, summons help, retrieves the kit, supports airway/circulation in scope, and assists the provider — they do not independently order or dose). You cue the learner to paste their facility's LAST protocol rather than supplying any values.

## Inputs

- `block_type` (optional): the regional/neuraxial/infiltration context.
- `onset` (default `evolving`): `early-subtle` (prodrome) or `evolving` (progressing toward CV/CNS signs).
- `facility_protocol` (paste): the learner's LAST/lipid-emulsion protocol location (no values invented).

## Method

1. **Present early cues:** neuro/behavioral prodrome (perioral/auditory changes, agitation, confusion) and/or cardiovascular drift — cues before classic collapse.
2. **Recognize + name the concern out loud:** learner states "possible LAST" and why, distinguishing ≥2 mimics (e.g., high/total spinal, primary dysrhythmia, hypoglycemia-mimic, emergence delirium).
3. **Call + retrieve:** learner calls for help by role and sends for the LAST/lipid-emulsion kit and the code cart — the two parallel first moves.
4. **Support in scope:** airway/oxygenation support, monitoring, and preparing the lipid emulsion *per facility protocol* for provider administration (learner pastes the protocol; no dosing stated here).
5. **Assist the provider-led response** and track what to reassess and on what interval (per facility).
6. **Score the response** and give one coaching point on the earliest recognition cue or the parallel call/kit move.

## Output Format

```
LAST REHEARSAL — block [type], onset [early-subtle/evolving]
Facility protocol pasted: [location / yes-no]

>>> EARLY CUES (I present)
[neuro/behavioral + CV cues — cues before collapse]

>>> RECOGNITION
"Possible LAST" because [...] | Mimics ruled toward/against: [A] [B]

>>> PARALLEL FIRST MOVES
Call for help: [role] | Retrieve: LAST/lipid kit + code cart

>>> SUPPORT IN SCOPE
Airway/O2: [...] | Monitor: [...] | Prepare lipid emulsion per facility protocol | Assist provider: [...]
Reassess: per facility

>>> SCORE
Recognized early [Y/N] · Parallel call+kit [Y/N] · Scope-safe support [Y/N] · Used facility protocol not invented numbers [Y/N]
One coaching point: [...]
```

## Variation Hooks

| Knob | Effect |
|---|---|
| `onset` | `early-subtle` trains prodrome catch; `evolving` trains the full response |
| `block_type` | Match the unit's regional caseload |
| `mimic_pressure` | Add a convincing mimic to train the discriminator |
| `team_size` | Solo-first-responder vs full-team assist |

## Verification Checklist

- [ ] Recognition is driven by **early cues**, before classic collapse.
- [ ] ≥2 mimics considered and discriminated.
- [ ] **Call for help + retrieve kit** are named as parallel first moves.
- [ ] Support actions are **in scope**; provider leads dosing/resuscitation.
- [ ] Lipid-emulsion/thresholds are **per facility protocol** — no invented numbers.
- [ ] Reassess interval is "per facility"; one coaching point given.

## Worked Example (compact)

**Input:** `block_type = peripheral nerve block`, `onset = evolving`.

**Output (excerpt):**
```
Early cues: patient reports ringing ears and metallic taste, becomes agitated, then rhythm looks abnormal on the monitor.
Recognition: "possible LAST" — neuro prodrome + emerging CV signs after a block. Mimics: high/total spinal (would expect ascending block signs), primary dysrhythmia, emergence delirium (no CV/neuro-toxicity prodrome).
Parallel moves: call provider + rapid-response by role; send for LAST/lipid kit and code cart simultaneously.
Support in scope: O2, airway support, monitor, prepare lipid emulsion per facility protocol; assist provider. Reassess per facility.
Coaching point: your fastest win here is naming "possible LAST" out loud on the prodrome — it triggers the kit retrieval a full stage earlier.
```

> Safety reminder: A rehearsal only — real LAST is a provider-led resuscitation. Know where your facility's protocol and lipid kit are, and escalate by role immediately.
