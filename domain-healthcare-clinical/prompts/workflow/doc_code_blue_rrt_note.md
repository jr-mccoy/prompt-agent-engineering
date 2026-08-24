---
title: "Code Blue / Rapid Response Note"
category: domain-healthcare-clinical/workflow
description: "Generate a resuscitation event note — code blue or rapid response — with timeline, ACLS interventions, rhythms, medications with times, ROSC/outcome, and post-event disposition."
techniques:
  - ST-02
  - ST-03
  - CM-01
  - RT-02
  - RT-05
difficulty: advanced
tags:
  - documentation
  - code-blue
  - rapid-response
  - resuscitation
updated: "2026-06-19"
---

## Objective

Produce a resuscitation event note that reconstructs a code blue or rapid response into an accurate, time-stamped record: what triggered it, the chronologic interventions (compressions, rhythms, shocks, drugs with doses and times), the response, the outcome (ROSC, ongoing, or termination), and the post-event plan. The note must capture the timeline precisely — it is a clinical, quality, and medicolegal document.

## Inputs

- Event type (code blue/cardiac arrest vs. rapid response/deterioration) and location
- Trigger: what prompted the call (found unresponsive, monitored arrest, respiratory distress, etc.)
- Time of event onset, time of arrival of the team
- Initial rhythm and assessment
- Interventions with times: CPR, defibrillation/cardioversion (energy), airway management, medications (drug, dose, route, time)
- Rhythm changes and pulse checks
- Outcome: ROSC and time, ongoing resuscitation, or termination with time and decision rationale
- Post-event disposition and immediate plan; team members present

## Role

Code team leader or documenting clinician writing the event note immediately after the resuscitation.

## Reasoning Steps

1. **Anchor the event in time and place.** Onset time, location, who found/called, time the team arrived. The timeline is the spine of the note.

2. **Record the initial assessment and rhythm.** Responsiveness, pulse, breathing, the first monitored rhythm (shockable vs. non-shockable), and any immediately reversible causes considered (the Hs and Ts).

3. **Document interventions chronologically with times.** CPR start/stop, each defibrillation with energy delivered, airway interventions (BVM, intubation, supraglottic), and each medication with dose, route, and time (epinephrine 1 mg IV q3–5min, amiodarone 300 mg, etc.). Pair drug administration to the ACLS algorithm and the rhythm.

4. **Track rhythm and pulse checks** at each cycle — what the rhythm was, whether a pulse was present, decisions made (shock, continue CPR, etc.).

5. **Address reversible causes** that were considered and treated during the code (hyperkalemia → calcium/bicarb, hypoxia → airway, tension pneumothorax → decompression, etc.).

6. **State the outcome unambiguously:** ROSC with time and post-ROSC vitals/rhythm; or ongoing resuscitation handed off; or termination of efforts with the time, total duration, and the basis for the decision (and whether family was present/informed).

7. **Document the post-event plan** for survivors: disposition (ICU), post-arrest care (targeted temperature consideration, post-ROSC ECG, labs, pressors), and family communication.

8. **List the team and confirm accuracy.** Record who ran and participated in the code. Times and doses must be accurate; do not reconstruct details not known.

## Output Format

```
EVENT: [code blue / rapid response] | LOCATION: | DATE:
EVENT ONSET TIME: / TEAM ARRIVAL TIME:
TRIGGER: [what prompted the call]

INITIAL ASSESSMENT:
- Responsiveness/pulse/breathing:
- Initial rhythm:
- Reversible causes considered (Hs/Ts):

RESUSCITATION TIMELINE:
[HH:MM] — [intervention: CPR start, rhythm, shock @ [J], drug + dose + route, pulse check result]
[HH:MM] — ...

REVERSIBLE CAUSES ADDRESSED: [list + treatment]

OUTCOME:
- [ROSC @ time + post-ROSC vitals/rhythm] OR [ongoing, handed off] OR [efforts terminated @ time, total duration, basis, family]

POST-EVENT PLAN:
- [disposition, post-arrest care, labs/ECG, pressors, family communication]

TEAM PRESENT: [code leader + roles]
```

## Worked Example

**Input:** Code blue, telemetry floor, monitored patient found pulseless. Onset 03:14, team arrived 03:15. Initial rhythm VF. CPR started 03:14. Shock 200 J at 03:15, epinephrine 1 mg IV 03:16, CPR continued; 03:17 rhythm check still VF, shock 200 J, amiodarone 300 mg IV 03:18; 03:19 still VF, shock, CPR; epinephrine 1 mg 03:21; 03:23 rhythm organized, pulse present — ROSC. Post-ROSC BP 96/58, intubated during code at 03:20. K returned 6.8 from labs drawn at start; calcium gluconate and insulin/D50 given 03:22. Transferred ICU.

**Output:**

```
EVENT: Code blue (cardiac arrest) | LOCATION: Telemetry floor | DATE: [date]
EVENT ONSET TIME: 03:14 / TEAM ARRIVAL TIME: 03:15
TRIGGER: Monitored patient on telemetry found pulseless; telemetry showed ventricular fibrillation.

INITIAL ASSESSMENT:
- Unresponsive, pulseless, not breathing.
- Initial rhythm: ventricular fibrillation (shockable).
- Reversible causes considered: hyperkalemia (recent illness/renal), hypoxia, acidosis; labs drawn at onset.

RESUSCITATION TIMELINE:
03:14 — Pulselessness confirmed; high-quality CPR initiated. Pads placed.
03:15 — Rhythm VF → defibrillation 200 J (biphasic); CPR resumed immediately.
03:16 — Epinephrine 1 mg IV; CPR continued.
03:17 — Rhythm check: VF persists → defibrillation 200 J; CPR resumed.
03:18 — Amiodarone 300 mg IV bolus; CPR continued.
03:19 — Rhythm check: VF persists → defibrillation 200 J; CPR resumed.
03:20 — Endotracheal intubation performed; tube confirmed by capnography; ventilation continued.
03:21 — Epinephrine 1 mg IV (second dose); CPR continued.
03:22 — Stat K returned 6.8 → calcium gluconate 1 g IV, regular insulin 10 units IV + D50, sodium bicarbonate given for presumed hyperkalemic contribution.
03:23 — Rhythm check: organized rhythm with palpable pulse — ROSC achieved.

REVERSIBLE CAUSES ADDRESSED: Hyperkalemia (K 6.8) — calcium gluconate, insulin/dextrose, bicarbonate. Hypoxia — secured airway.

OUTCOME:
- ROSC at 03:23. Post-ROSC BP 96/58, intubated and ventilated, organized rhythm on monitor. Total arrest-to-ROSC interval ~9 minutes.

POST-EVENT PLAN:
- Transfer to ICU for post-arrest care.
- Post-ROSC 12-lead ECG, repeat BMP/VBG, recheck K and treat ongoing hyperkalemia (consider dialysis if refractory/renal failure).
- Hemodynamic support: norepinephrine for MAP ≥65 as needed; targeted temperature management consideration per post-arrest protocol given comatose state.
- Identify and treat hyperkalemia etiology.
- Family notified of the event and ICU transfer.

TEAM PRESENT: Code team leader (documenting), airway/anesthesia, compressions rotation, pharmacy, bedside RN, recorder.
```
