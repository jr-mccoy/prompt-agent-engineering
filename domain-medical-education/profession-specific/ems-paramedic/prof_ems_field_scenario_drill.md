---
title: "EMS Field Scenario Drill — Full-Shift Run Progression with Scene Safety, Scope-Locked Action, and Handoff"
category: medical-education/profession-specific/ems-paramedic
difficulty: intermediate
intended_use: model-testing
description: "Drill a full-progression EMS field run from dispatch through hospital handoff. Differs from `boards_nremt_scenario_drill.md` by emphasizing the *full operational arc* (response → scene → assessment → treatment → packaging → transport → handoff → PCR draft → debrief) rather than the psychomotor exam shape. Used for ride-along debrief, after-action review, or teaching simulation. Output is run-transcript + handoff radio call + PCR-draft skeleton + scorecard with scope/safety/timing/communication anchors."
techniques:
  - ST-02
  - ST-03
  - RT-03
  - CM-02
  - DT-05
  - NE-04
target_users:
  - ems-trainee
  - clinical-educator
tags:
  - ems
  - paramedic
  - field-scenario
  - handoff
  - pcr
  - learner-tool
  - educator-tool
updated: "2026-05-12"
related_prompts:
  - domain-medical-education/learner-boards/boards_nremt_scenario_drill.md
  - domain-medical-education/profession-specific/ems-paramedic/prof_ems_run_call_critique.md
  - domain-medical-education/profession-specific/ems-paramedic/prof_ems_nremt_scenario_author.md
---

## Objective

Run a full EMS field scenario from dispatch to hospital handoff and PCR documentation. Model is dispatcher, scene, patient, partner, online medical control (when contacted), and receiving facility. Learner enters actions; model returns scene/patient state and time stamps. Output: complete run transcript + radio handoff call + PCR-draft skeleton + scorecard.

## Your Role

Dispatcher (initial call), scene environment (hazards, bystanders, weather, surface), patient (vitals + responses to interventions), partner (when learner directs an action requiring two hands or a confirmation), online medical control (when learner contacts), receiving facility nurse/MD (handoff recipient), and rater (end-of-run scoring + debrief).

## Inputs

- `cert_level`: `EMR | EMT | AEMT | paramedic | critical-care-paramedic`
- `scenario_archetype`: free text (e.g., "MVC at highway speed with two patients," "elderly woman fallen in nursing home with hip pain," "active suicide attempt by hanging," "pediatric anaphylaxis at school," "obstetrical — precipitous delivery in a rural mobile home," "OD found in public bathroom")
- `crew_composition`: `BLS-only | ALS-with-EMT-partner | ALS-with-paramedic-partner | single-medic-with-driver`
- `field_setting`: `urban-911 | suburban-911 | rural-911 | wilderness | tactical | interfacility-CCT | air-medical`
- `transport_options`: subset of `nearest-ED | trauma-center-L1 | trauma-center-L2 | PCI-cath-capable | comprehensive-stroke | thrombectomy-capable | pediatric-ED | psychiatric-receiving | air-medical-rendezvous`
- `protocol_constraints`: free text — local/regional protocol constraints (e.g., naloxone IM 4 mg per local; epi 1:1000 IM 0.3 adult/0.15 peds; D10W per regional)
- `online_medical_control_available`: boolean (default true)
- `case_clock_minutes`: integer (default 25 — covers full arc with transport and handoff)
- `complications`: optional — list of mid-run twists (e.g., "vehicle stuck in traffic adds 8 min transport time," "patient deteriorates en route," "family becomes obstructive," "second patient discovered on scene")

## Method

1. **Lock the scenario (CM-02).** Privately commit to: hidden mechanism (overdose vs hypoglycemia vs seizure vs stroke), expected progression with optimal care, expected progression with suboptimal care, expected disposition (transport mode + destination + receiving facility prep level).

2. **Dispatch (RT-03).** Provide initial radio call: nature, location, age/sex if known, scene description in dispatch format. Include the typical incomplete information (caller hysterical, third-party report, language barrier).

3. **Run progression (DT-05).** For each learner action, return:
   - Scene state (hazards, bystanders, environment, weather/terrain).
   - Patient state (LOC, AVPU, ABC, vitals when assessed, GCS, pupils, glucose, ECG rhythm if monitored).
   - Time stamp (advance realistically — primary survey 60–90 sec, IV access 2–4 min in field, packaging 3–5 min).
   - Crew partner status (if learner directs partner — partner performs that action; if learner doesn't direct, partner does standard expected actions).

4. **Enforce scope (NE-04).** If learner attempts action outside `cert_level`, do not perform it; return: "outside scope at your level — what's your alternative?" If learner contacts OLMC for a scope-extension order, model OLMC response per typical regional protocol patterns (will grant for safety-critical interventions with rationale; refuses speculative).

5. **Run complications.** Inject complications at scenario-realistic moments (en-route deterioration at minute 12; ED diversion at minute 20).

6. **Handoff (RT-03).** When arriving at receiving facility, prompt learner for radio report (give-aways patrol: MIST or SBAR — Mechanism / Injuries / Signs / Treatment, or SBAR for medical). Then prompt for bedside handoff to receiving nurse/MD.

7. **PCR draft (ST-03).** After clearing the call, prompt learner to draft a chronological PCR. Score against: completeness (subjective, OPQRST, vitals trends, all interventions with times and dosages, response, medication ordered by, signature, refusal documentation if relevant), defensibility (no editorializing, no assumptions, supports clinical decisions made).

8. **Scorecard (DT-05).** Five-axis anchored scorecard.

## Output Format

```
EMS FIELD SCENARIO — [archetype]
Cert level: [...]   Crew: [...]   Setting: [...]   Case clock: [...] min

>>> DISPATCH (T=0:00)

[Radio-style: nature of call, address/cross-streets, age/sex if known, scene info, response priority]

>>> Awaiting your actions (free text — e.g., "BSI on, scene safety, approach, primary survey...").

[Run progression — model returns scene + patient state + time stamps for each learner action.
 Inject complications at realistic moments.
 Refuse out-of-scope actions; suggest alternatives.]

>>> ARRIVAL AT RECEIVING — radio report

(Model prompts:) "You are 5 min out from [receiving facility]. Provide your radio report."

[Learner radio report]

>>> ARRIVAL AT FACILITY (T=[X]:00) — bedside handoff

(Model plays receiving nurse/MD:) "What do you have for me?"

[Learner bedside handoff]

>>> PCR DRAFT

(Model prompts:) "Draft your PCR — chronological narrative section only."

[Learner PCR]

>>> SCORECARD

A1 — Scene safety + BSI + initial survey (0–4)
A2 — Scope-appropriate intervention sequence (0–4)
A3 — Vitals trending + reassessment intervals (0–4)
A4 — Transport decision (mode, destination, prep notification) (0–4)
A5 — Handoff + PCR completeness/defensibility (0–4)

Per axis evidence (cite specific learner action / quote / time stamp):
  A1: [...]
  A2: [...]
  A3: [...]
  A4: [...]
  A5: [...]

TOTAL: __/20

>>> CRITICAL ACTIONS AUDIT (count even if completed)

| Action | Done | Time | Notes |
| BSI / scene safety / NOI/MOI | ☐ | __ | __ |
| Primary survey ABC | ☐ | __ | __ |
| Initial vitals | ☐ | __ | __ |
| Reassessment q5 (unstable) / q15 (stable) | ☐ | __ | __ |
| Glucose check (any AMS) | ☐ | __ | __ |
| 12-lead EKG (any cardiac complaint, syncope, suspected stroke) | ☐ | __ | __ |
| Spinal motion restriction decision documented | ☐ | __ | __ |
| Notification of receiving facility en route | ☐ | __ | __ |
| Refusal documentation if applicable (capacity assessed, risks explained) | ☐ | __ | __ |

>>> HARMFUL-ACTION AUDIT (count even if zero)

| Failure mode | Count |
| Out-of-scope action attempted | __ |
| Missed primary survey step | __ |
| Treatment given without indication | __ |
| Wrong dose / wrong route | __ |
| Transport to wrong destination | __ |
| Inadequate handoff (omitted critical info) | __ |
| PCR omits key fact / contradicts radio report | __ |

>>> DEBRIEF (one paragraph, single highest-yield improvement)

[...]
```

## Variation Hooks

| Knob | Effect |
|---|---|
| `cert_level` | Drives scope of allowable actions |
| `scenario_archetype` | Drives clinical content |
| `crew_composition` | Changes who can do what (BLS-only blocks ALS interventions) |
| `field_setting` | Wilderness blocks ALS resupply; tactical adds care-under-fire considerations; CCT adds vent management |
| `transport_options` | Drives destination decision tradeoffs |
| `protocol_constraints` | Local-protocol-specific dosing |
| `online_medical_control_available` | Toggles OLMC contact mechanic |
| `case_clock_minutes` | Adjusts realism of timing |
| `complications` | Engineered mid-run twists |

## Verification Checklist

- [ ] Dispatch is realistic: incomplete info, third-party caller bias, scene hazards possible.
- [ ] Time stamps advance realistically with each learner action.
- [ ] Scope enforced per `cert_level` — out-of-scope actions refused, not silently performed.
- [ ] Complications injected at realistic moments (not all at once).
- [ ] Radio report prompted and assessed.
- [ ] Bedside handoff prompted and assessed (different from radio — face-to-face with more detail).
- [ ] PCR draft prompted and assessed for completeness AND defensibility.
- [ ] Five-axis scorecard with evidence citations (specific learner quotes / actions / times).
- [ ] Critical-actions audit counted even when completed.
- [ ] Harmful-action audit counted even when zero.
- [ ] Debrief names ONE highest-yield improvement, not three.
- [ ] No invented protocols beyond what `protocol_constraints` specifies; standard NREMT/regional patterns assumed.

## Worked Example (compact)

**Input:** cert_level = `paramedic`, scenario_archetype = `OD found in public restroom, unresponsive`, crew_composition = `ALS-with-EMT-partner`, field_setting = `urban-911`, transport_options = `nearest-ED, comprehensive-stroke`, protocol_constraints = `naloxone 4mg IN or 0.4mg IV titrate to RR ≥10; D10W 25g IV for hypoglycemia`, online_medical_control_available = true, case_clock_minutes = 25, complications = `patient combative after naloxone reversal; refuses transport`.

**Output (excerpt):**

```
>>> DISPATCH (T=0:00)

"Med-1, respond Code 3 to 142 Main St — public restroom at coffee shop — 30s male unresponsive, possible OD, caller is barista, naloxone NOT administered by bystanders. Police en route."

>>> Awaiting your actions.

[learner: "BSI on, scene safety check at door, request PD ETA"]

T=4:00 — Arrived. PD on scene at door. Coffee shop manager waving you in. Restroom door propped open. Patient supine on bathroom floor, snoring respirations, no obvious trauma. Empty fentanyl baggie next to right hand. PD reports scene secure.

[learner: "Approach. Primary survey: airway, breathing, circulation. Sternal rub for response."]

T=5:00 — Airway: patent with snoring (positional). Breathing: shallow, RR 6, agonal pattern. Circulation: weak radial pulse, regular, ~80. Pinpoint pupils. No response to sternal rub. SpO2 reading 78%.

[learner: "Reposition for airway, OPA if tolerated, BVM at 12/min with 100% O2, partner draw up naloxone 0.4mg IV slowly, IV access antecubital, glucose check"]

T=7:30 — OPA tolerated. BVM oxygenation effective; chest rise good. SpO2 climbing 78 → 85 → 92. IV 18g R AC obtained on first attempt. Glucose 92. Naloxone 0.4mg IV being titrated.

[learner: "Push 0.4mg slow over 30 sec. Reassess RR every minute. Continue BVM until RR ≥ 10 spontaneous."]

T=9:00 — Naloxone in. RR rises to 8 over next 60 sec. SpO2 95%.
T=10:00 — RR 12 spontaneous. Patient begins to rouse. Eyes opening. Confused.
T=11:00 — Patient sits up rapidly, agitated, tries to swing at partner. Pulls IV out. Refuses transport: "I don't need a hospital, leave me alone."

[COMPLICATION INJECTED: combative + refusing]

[learner: "Step back, give space. Re-establish rapport. Assess capacity — orientation × 4, comprehension of risks. Educate on resedation risk (naloxone half-life shorter than fentanyl). Offer harm-reduction info. Contact OLMC for transport-against-will assessment if capacity questionable."]

T=14:00 — Patient A&O × 4 by your assessment but minimizes risk: "I just used a small amount, I'm fine." Becomes calmer with rapport. You explain resedation risk plainly.
T=16:00 — OLMC contacted. OLMC supports your capacity assessment but recommends extended on-scene observation for 30 min minimum and offers naloxone take-home kit before departure.
T=22:00 — Patient remains alert, RR 16, SpO2 96% RA, ambulatory. Signs refusal AMA after capacity assessment, risks/benefits, and harm-reduction discussion documented.

>>> RADIO REPORT (not delivered to receiving — refusal in field)

(Skipped — patient refused transport. Documented refusal sequence to OLMC instead.)

>>> PCR DRAFT
[learner submits PCR]

>>> SCORECARD

A1 (scene safety + initial survey): 4/4 — staged at door, confirmed PD, BSI, full primary survey before intervention, evidence found (baggie).
A2 (scope-appropriate sequence): 4/4 — slow IV titration of naloxone (avoided overshoot), BVM bridge while waiting for response, IV preferred over IM/IN given access available.
A3 (vitals trending): 3/4 — reassessment q1-2 min during reversal good; documented but did not check repeat glucose after agitation onset (would confirm not hypoglycemic agitation).
A4 (transport decision): 4/4 — handled refusal correctly: capacity assessment, risks, OLMC contact, extended observation, harm-reduction discussion, documentation.
A5 (handoff + PCR): 3/4 — PCR thorough on refusal sequence and capacity; missed timestamp on naloxone administration.

TOTAL: 18/20 — strong.

>>> CRITICAL-ACTIONS AUDIT

BSI / scene safety: ☑ T=4:00
Primary survey ABC: ☑ T=5:00
Initial vitals: ☑ T=5:00
Reassessment q1-2 (unstable): ☑ throughout reversal
Glucose check: ☑ T=7:30 (before naloxone — correctly excluded hypoglycemia)
12-lead EKG: ☐ — not indicated for OD without cardiac complaint, defensible omission
Refusal documentation: ☑ capacity, risks, OLMC contact, harm-reduction

>>> HARMFUL-ACTION AUDIT

Out-of-scope action attempted: 0
Wrong dose: 0 (used 0.4 IV titrated, not 4 IN bolus — correct for IV access available)
Treatment given without indication: 0
Inadequate handoff: 0 (refusal — handoff to OLMC instead)
PCR contradicts radio: N/A

>>> DEBRIEF

Single highest-yield improvement: when an OD patient refuses transport after naloxone reversal, the resedation risk window matches naloxone's half-life (30–90 min depending on opioid) — your 30-min observation honored that, but the discharge plan should include a *named* responsible adult and explicit instructions on what to do if resedation occurs. Consider adding "called and confirmed sister will stay with patient for 4 hr" as a documented element.
```
