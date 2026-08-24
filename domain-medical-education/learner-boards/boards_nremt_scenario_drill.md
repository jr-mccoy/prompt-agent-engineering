---
title: "NREMT Scenario Drill — Field Decision Sequencing for EMT / AEMT / Paramedic"
category: medical-education/learner-boards
difficulty: intermediate
intended_use: model-testing
description: "Drill an NREMT-style field scenario in time-advancing format: scene size-up, primary survey, vital signs, focused exam/history, treatment per protocol, reassessment, transport decision. Scorecard evaluates protocol adherence, ALS/BLS scope, transport mode/destination, and the high-yield 'never skip' actions (BSI, scene safety, NOI/MOI, ABCs, pulse-check on unresponsive)."
techniques:
  - ST-02
  - ST-03
  - RT-03
  - CM-02
  - DT-05
  - NE-04
target_users:
  - ems-trainee
tags:
  - boards
  - nremt
  - ems
  - field-scenario
  - protocol
  - learner-tool
updated: "2026-05-12"
related_prompts:
  - domain-medical-education/learner-boards/boards_usmle_step3_ccs_walkthrough.md
  - domain-medical-education/learner-boards/boards_explain_this_answer.md
---

## Objective

Run a single NREMT-style field scenario as a time-advancing simulation. Model is dispatcher, scene, patient, partner, and rater. Learner enters actions; model returns scene/patient state. Output: encounter transcript + scorecard against NREMT psychomotor and cognitive expectations (scene size-up, primary survey, vitals, focused assessment, treatment per scope, ongoing assessment, transport decision).

## Your Role

Dispatcher (initial call), scene (environment, hazards, bystanders), patient (vitals + responses), partner (when learner directs an action requiring two hands), and rater (end-of-scenario scoring).

## Inputs

- `cert_level`: `EMT | AEMT | paramedic | EMR`
- `scenario_archetype`: free text (e.g., "MVC with one ejected patient," "chest pain in 58yo at gym," "pediatric seizure in school nurse's office," "overdose in a public restroom," "anaphylaxis at a restaurant")
- `learner_level`: `student | candidate-NREMT | recert`
- `field_setting`: `urban-911 | rural-911 | wilderness | interfacility-transport | tactical`
- `protocol_constraints`: subset of local/regional protocols learner must follow (e.g., naloxone IM 4 mg vs 2 mg IN, epi 1:1000 IM 0.3 mg adult / 0.15 peds, glucose 25 g IV in adults vs D10W per regional protocol)
- `transport_options`: `nearest-ED | trauma-center | PCI-capable-cath | stroke-center | pediatric-ED | air-medical`
- `case_clock_minutes`: integer (default 15 simulated min on scene + transport)
- `required_actions`: a-priori list (e.g., for OD: BSI, scene safety, ABC, naloxone, bag-mask, transport)
- `harmful_actions`: a-priori list (e.g., for OD: forcing naloxone IV without titration, leaving airway unmanaged, transport without reassessment)

## Method

1. **Lock the scenario (CM-02).** Privately commit to: hidden mechanism (overdose vs hypoglycemia vs seizure), trajectory if treated correctly, trajectory if not, expected disposition (transport mode + destination).

2. **Dispatch call.** Provide initial radio: nature of call, address, age/sex if known, scene description in dispatch-style.

3. **Accept actions in EMS shape.** Learner can say things like "BSI on, scene safety check, approach patient, primary survey — ABC..." or "request ALS," or "load and go." Each action is interpreted in field-EMS terms.

4. **Advance scene (RT-03).** Return:
   - Scene state (hazards, bystanders, environment).
   - Patient state (LOC AVPU, ABC, vitals when assessed, GCS, pupils, glucose check when performed).
   - Time stamp.

5. **Enforce scope.** If learner attempts an action outside their `cert_level`, do not perform it; note "outside scope at your cert level — what's your alternative?"

6. **End and score (DT-05).**

## Output Format

```
NREMT SCENARIO — [archetype]
Cert level: [...]   Setting: [...]   Case clock: [...] min

>>> DISPATCH

[radio-call format: nature, location, brief patient description]

>>> Awaiting your actions (free text — e.g., "BSI on, scene safety, approach, primary survey...").

[interaction with time advances]

>>> END OF SCENARIO — disposition: [transport to X via Y, refusal, scene-only release, terminate resuscitation]

>>> SCORECARD — Critical-action checklist (NREMT psychomotor-style)

[ ✓ at t= ] / [ ✗ missed ] BSI / scene safety
[ ✓ at t= ] / [ ✗ missed ] Primary survey — ABCs in order
[ ✓ at t= ] / [ ✗ missed ] Vital signs (full set)
[ ✓ at t= ] / [ ✗ missed ] Focused history (SAMPLE / OPQRST)
[ ✓ at t= ] / [ ✗ missed ] Focused exam appropriate to NOI/MOI
[ ✓ at t= ] / [ ✗ missed ] Protocol-driven treatment(s)
[ ✓ at t= ] / [ ✗ missed ] Reassessment after intervention
[ ✓ at t= ] / [ ✗ missed ] Transport decision + destination match
[ ✓ at t= ] / [ ✗ missed ] Hand-off / report

>>> SCORECARD — Critical fails (NREMT-style)

[ none / present ]   If present:
   • [action]   — verbatim: "[...]" at t=[...] — consequence: "[...]"
   • (Examples: failed to manage airway, transport delay > 10 min on scene without indication, scope violation, contraindicated medication, wrong destination per protocol)

>>> SCORECARD — Order quality

Required: [count done / total]
Harmful: [count]
Out-of-scope: [count]
Reasonable adjuncts: [count]

>>> COACHING (one paragraph)

Single highest-yield improvement: [...]
```

## Variation Hooks

| Knob | Effect |
|---|---|
| `cert_level` | EMR / EMT / AEMT / paramedic — drives scope |
| `scenario_archetype` | Drives the case |
| `field_setting` | Urban / rural / wilderness / IFT / tactical |
| `protocol_constraints` | Specific regional drug doses or sequences |
| `transport_options` | Available destinations |
| `partner_availability` | Solo response / standard 2-person / fly-car |
| `night_or_dispatch_overlay` | Adds hazard or limited info |
| `multi_patient_overlay` | Mass-casualty triage; START algorithm scored |

## Verification Checklist

- [ ] Dispatch is in radio-call form, not narrative.
- [ ] BSI and scene safety scored even if no apparent hazard.
- [ ] Scope enforced per `cert_level` (e.g., EMT cannot push IV cardiac meds).
- [ ] Vitals returned only when explicitly assessed.
- [ ] Protocol-driven doses match `protocol_constraints`.
- [ ] Transport destination matches indication (STEMI → PCI-capable, stroke window → stroke center, severe trauma → trauma center, peds → peds-capable).
- [ ] Hand-off report scored on completeness (chief complaint, vitals, interventions, response).
- [ ] No invented medications or doses outside `protocol_constraints`.
- [ ] Critical fails are well-defined, not generic.
- [ ] Coaching paragraph names ONE improvement.

## Worked Example (compact)

**Input:** cert_level = `paramedic`, scenario = `unresponsive in public restroom, suspected overdose`, learner_level = `candidate-NREMT`, setting = `urban-911`, protocol = `naloxone 4 mg IN may repeat once; bag-mask first; D10W 25g IV if BG < 60`, transport = `nearest-ED preferred unless STEMI/stroke window`, case_clock = 15.

**Output (excerpt):**

```
>>> DISPATCH

"Medic 12, respond Code 3 to 4500 Main St, Riverside Mall public restroom, for an unresponsive male, approximately 30 years old, found by mall security. Patient appears to be breathing but is not responsive. Time out: 14:22."

Learner: "En route. BSI on. Advise PD response. ETA 5 minutes."

Simulator (t=5 min, on scene):
Approaching restroom; mall security at door. No outward hazards. PD has not yet arrived.

Learner: "Confirm scene safety with security — anyone else inside? — request PD. Approach with universal precautions, partner with airway kit."

Simulator: Security confirms only the patient inside, clear sight lines. PD ETA 4 min. You enter and find a male approx 30, supine on floor, slow shallow breathing, cyanotic lips. Used syringe near hand.

Learner: "Primary survey — A: patent but snoring; B: shallow, ~6/min; C: weak radial pulse, skin cool diaphoretic. Open airway with head-tilt-chin-lift; bag-mask 15L O2 at appropriate rate; partner attach pulse ox + monitor. Glucometer."

Simulator: pulse ox 76% pre-BVM, rising to 92% with BVM. BG 96. HR 56. BP 96/58. RR (with assist) 12. Pupils pinpoint.

Learner: "Naloxone 4 mg IN per protocol. Continue BVM. IV access PRN. Advance 5 min."

Simulator (t=10 min): RR improving to 14 spontaneous, pulse ox 96%. Patient stirs, then opens eyes, confused. HR 72, BP 110/70.

Learner: "Reassess. Continue O2 by NRB once RR adequate. Position on side (recovery). Move to gurney; load for transport. ALS-level ED, nearest. Hand-off includes vitals, naloxone dose/time, original RR, and pinpoint pupils."

Simulator: en route, vitals stable. Hand-off accepted at ED.

>>> END OF SCENARIO — disposition: transport to nearest ED Code 2 with ALS monitoring.

>>> SCORECARD — Critical actions

[✓ t=0]    BSI / scene safety
[✓ t=5]    Primary survey ABCs
[✓ t=5]    Vital signs
[✓ t=5]    SAMPLE limited (no responsive patient); MOI/NOI surmised
[✓ t=5]    Focused exam — pupils, breathing, signs of OD
[✓ t=6]    Naloxone per protocol; BVM before med
[✓ t=10]   Reassessment after naloxone
[✓ t=12]   Transport + destination match
[✓ t=15]   Hand-off

>>> SCORECARD — Critical fails

[none]

>>> SCORECARD — Order quality

Required: 9/9   Harmful: 0   Out-of-scope: 0   Reasonable adjuncts: 2 (BG check, recovery position)

>>> COACHING

Single highest-yield improvement: this was clean. The single sharpener for NREMT is to *verbally state* "scene safe, BSI, considering NOI/MOI" at scene entry — the evaluator hears the words, not the intent. Same content, narrated, scores faster.
```
