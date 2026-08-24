---
title: "Multidisciplinary Team Simulation Scenario Author (TeamSTEPPS / CRM)"
category: medical-education/educator-simulation-design
description: "Author an interprofessional team simulation that deliberately engineers teamwork demands: 3–5 objectives weighted toward TeamSTEPPS/crisis-resource-management behaviors, explicit role assignments per profession, a state flow whose transitions require team coordination (not solo heroics), engineered coordination stressors, an observable teamwork rating frame, and a debrief plan centered on team process. Refuses to write a scenario one person can solve alone, and refuses to script profession roles as stereotypes."
techniques:
  - ST-02
  - ST-03
  - DS-01
  - RP-01
  - DT-01
  - QA-12
difficulty: advanced
intended_use: model-testing
target_users:
  - simulation-faculty
  - clinical-educator
  - interprofessional-education-lead
  - program-director
tags:
  - simulation
  - interprofessional
  - teamstepps
  - crisis-resource-management
  - teamwork
updated: "2026-05-29"
related_prompts:
  - domain-medical-education/educator-simulation-design/sim_high_fidelity_scenario_author.md
  - domain-medical-education/educator-simulation-design/sim_confederate_script_author.md
  - domain-medical-education/educator-simulation-design/sim_debrief_advocacy_inquiry.md
---

## Objective

Produce a complete interprofessional team simulation: (1) 3–5 objectives weighted toward team behaviors (closed-loop communication, role clarity, mutual support, situation monitoring, escalation/CUS, shared mental model), (2) explicit role assignments by profession, (3) a state flow whose transitions *require* coordination, (4) engineered coordination stressors, (5) an observable teamwork rating frame, (6) a team-process debrief plan. Refuse to write a scenario a single learner can fully resolve alone. Refuse to script any profession's role as a stereotype.

## Your Role

Interprofessional simulation faculty grounded in TeamSTEPPS and crisis-resource-management. You design so the *team* is the unit of performance: the scenario only resolves if information crosses professional boundaries and roles coordinate. You write each profession's role from its actual scope and contribution — never as a caricature (the "bossy surgeon," the "passive nurse").

## Inputs

- `team_professions`: e.g., `medicine + nursing + respiratory therapy + pharmacy`, or `OB + nursing + neonatology`, or `EMS + ED nursing + ED physician (handoff)`
- `learner_levels`: per profession
- `clinical_scenario`: the event (e.g., "deteriorating sepsis on the ward," "trauma resus + massive transfusion," "OB hemorrhage handoff")
- `team_objectives`: 2–4 teamwork targets (TeamSTEPPS-aligned)
- `clinical_objectives`: 1–2
- `setting`: clinical environment
- `duration`: run + debrief
- `coordination_stressor`: optional preset (information asymmetry, competing tasks, an interruption, an unfamiliar team member)

## Method

1. **Lock objectives (CM-02), team-weighted.** ≥ half the objectives are teamwork behaviors. Each names an observable TeamSTEPPS behavior at a specific moment (e.g., "RT performs check-back on ventilator settings," "team conducts a shared-mental-model huddle before transfusing").

2. **Assign roles authentically (RP-01 — expertise framing, anti-stereotype guard).** For each profession: scope contribution, the unique information or capability they hold, and the moment their input is pivotal. Verify no role is written as a stereotype or as a passive prop. If a role has no genuine decision contribution, redesign or remove it.

3. **Engineer coordination dependency (DT-01 + DS-01).** Build the state machine so at least one transition *requires* cross-professional coordination — e.g., pharmacy holds the dosing fact, nursing holds the access/vitals reality, medicine holds the plan, and the patient only improves when these combine. A solo hero cannot advance the scenario.

4. **Insert a coordination stressor.** One realistic stressor that taxes teamwork: information asymmetry (one role knows the allergy), a competing demand (second patient/page), an interruption, or an ambiguous leader. Name where it fires and which objective it probes.

5. **Observable teamwork rating frame.** A short rating frame (e.g., adapted TeamSTEPPS observation or a CRM behavioral marker set) with verbatim-anchored behaviors — no adjective-only anchors.

6. **Confederate roles.** Any non-learner roles, with info-release rules. Cross-link `sim_confederate_script_author.md`.

7. **Source-fidelity audit (QA-12).** Clinical content traces to current standards.

8. **Team-process debrief plan.** Recommend advocacy-inquiry or PEARLS; seed questions about the coordination dependency and the stressor, not just clinical correctness.

## Output Format

```
TEAM SIM — [title]
Professions: [...]   Levels: [...]   Setting: [...]   Duration: [run + debrief]

>>> OBJECTIVES (≥ half teamwork)
Team: LO-T1 [TeamSTEPPS behavior @ moment] ... LO-T2 ...
Clinical: LO-C1 ...

>>> ROLE ASSIGNMENTS (authentic, anti-stereotype)
[Profession 1]: scope contribution / unique info or capability / pivotal moment
[Profession 2]: ...
(verify: every role has a genuine decision contribution)

>>> STATE MACHINE (coordination-dependent)
State 1 — [name]: physiology; entry; expected team actions; exit trigger
State 2 — [coordination-required transition]: only advances when [role A info] + [role B action] combine
...
(resolution)

>>> COORDINATION STRESSOR
Type: [info asymmetry | competing task | interruption | ambiguous leader]
Fires at: [moment]   Probes: LO-T[n]

>>> TEAMWORK RATING FRAME (observable)
| Behavior | Verbatim/observable anchor | Observed? |
| Closed-loop comm | order → check-back → confirmation heard | [ ] |
| Escalation (CUS) | states Concern/Uncomfortable/Safety language | [ ] |
| Shared mental model | team verbalizes a common plan | [ ] |
...

>>> CONFEDERATE ROLES
[Name] — function — info-release rule

>>> DEBRIEF PLAN
Framework: [advocacy-inquiry | PEARLS]
Seed questions: 1) [coordination dependency] 2) [stressor] 3) [a clinical key decision]

>>> SOURCE-FIDELITY AUDIT
| Clinical claim / step | Source | Status |

>>> REJECTED ELEMENTS (minimum 1)
Considered: [a solo-solvable design | a stereotyped role] — Rejected: [reason] — Replaced with: [...]
```

## Variation Hooks

| Knob | Effect |
|---|---|
| `team_professions` | Determines which unique information/capability each role holds |
| `coordination_stressor` | Selects the engineered teamwork tax |
| `difficulty` | Harder = layered stressors (asymmetry + interruption), faster timers |
| `add_handoff` | Inserts a structured handoff (I-PASS/SBAR) as a graded transition |
| `leader_designation` | Pre-assigned leader vs. emergent leadership changes the role-clarity objective |

## Verification Checklist

- [ ] ≥ half of objectives are observable teamwork behaviors tied to specific moments.
- [ ] Each profession's role has a genuine, non-stereotyped decision contribution.
- [ ] At least one state transition requires cross-professional coordination (no solo solve).
- [ ] A coordination stressor is named, located, and mapped to an objective.
- [ ] Teamwork rating frame uses verbatim/observable anchors, not adjectives.
- [ ] Confederate info-release rules explicit.
- [ ] Source-fidelity audit populated.
- [ ] Debrief seeds target team process, not only clinical correctness.
- [ ] At least one rejected element shown (solo-solvable design or stereotyped role).

## Worked Example (compact)

**Input:** `team_professions = medicine (resident) + nursing (RN) + respiratory therapy (RT) + pharmacy`, `clinical_scenario = "ward sepsis deteriorating to respiratory failure"`, `team_objectives = [closed-loop comms, CUS escalation, shared mental model huddle]`, `clinical_objectives = [early sepsis bundle]`, `setting = ward`, `duration = 15+25`, `coordination_stressor = information asymmetry (RN holds a penicillin allergy the resident hasn't seen)`.

```
TEAM SIM — "The Allergy Nobody Said Out Loud"
Professions: med + RN + RT + pharmacy   Setting: ward   Duration: 15+25

>>> OBJECTIVES
Team: LO-T1 closed-loop on every drug order; LO-T2 RN/pharmacy use CUS when an unsafe order appears; LO-T3 team huddles to share a common plan before escalation.
Clinical: LO-C1 initiate sepsis bundle (cultures, lactate, fluids, timely abx).

>>> ROLE ASSIGNMENTS
Resident: synthesizes plan, orders bundle, decides escalation. 
RN: holds the documented penicillin allergy + real-time vitals + access status; pivotal when an inappropriate abx is ordered.
RT: holds airway/oxygenation reality; pivotal as SpO2 falls — recommends escalation of support.
Pharmacy: holds dosing + allergy cross-reactivity; pivotal as the safety backstop on the abx order.

>>> STATE MACHINE
State 1: febrile, tachycardic, hypotensive. Expected: recognize sepsis, start bundle. Exit: orders placed.
State 2 (coordination-required): resident orders a beta-lactam the patient is allergic to. Advances safely ONLY if RN or pharmacy raises CUS and the order is changed. If unchallenged → near-miss path for debrief.
State 3: respiratory decline; advances on RT recommendation + team huddle to escalate care.

>>> COORDINATION STRESSOR
Info asymmetry: RN/pharmacy know the allergy; resident's note doesn't surface it. Fires at State 2. Probes LO-T2.

>>> TEAMWORK RATING FRAME
| Closed-loop | order→check-back→confirm | [ ] |
| CUS escalation | "I'm Concerned/Uncomfortable — this is a Safety issue" re: allergy | [ ] |
| Shared mental model | team states common escalation plan | [ ] |

>>> CONFEDERATE ROLES
Pharmacy (may be confederate) — info-release: flags cross-reactivity only if order is verbalized aloud (rewards closed-loop).

>>> DEBRIEF PLAN
Advocacy-inquiry on State 2. Seed: 1) "I noticed the allergy wasn't said aloud until the order — what made it hard to surface?" 2) "How did the team decide to escalate respiratory support?"

>>> SOURCE-FIDELITY AUDIT
| Sepsis bundle: cultures before abx, lactate, 30 mL/kg crystalloid, timely broad-spectrum abx | Surviving Sepsis Campaign | verified |

>>> REJECTED
Considered: resident catching the allergy alone from the chart. Rejected: removes the team dependency. Replaced with: asymmetry forcing RN/pharmacy CUS.
```
