---
title: "High-Fidelity Simulation Scenario Author (Immersive Manikin / State-Based)"
category: medical-education/educator-simulation-design
description: "Author a complete high-fidelity, state-based immersive simulation: 3–5 measurable objectives, a multi-state scenario flow with physiologic states and explicit transition triggers, expected and anticipated-error learner actions per state, confederate roles, equipment/moulage, programming notes for the manikin, and a linked debrief plan. Every state transition fires on a named learner action or a timer — never on facilitator whim. Refuses to advance physiology in a way that punishes correct action or rewards an unsafe one."
techniques:
  - ST-02
  - ST-03
  - DS-01
  - DS-29
  - DT-01
  - QA-12
difficulty: advanced
intended_use: model-testing
target_users:
  - simulation-faculty
  - clinical-educator
  - curriculum-designer
  - program-director
  - assessment-faculty
tags:
  - simulation
  - high-fidelity
  - state-based-design
  - scenario-flow
  - INACSL
updated: "2026-05-29"
related_prompts:
  - domain-medical-education/educator-simulation-design/sim_low_fidelity_scenario_author.md
  - domain-medical-education/educator-simulation-design/sim_vital_sign_trajectory_designer.md
  - domain-medical-education/educator-simulation-design/sim_confederate_script_author.md
  - domain-medical-education/educator-simulation-design/sim_debrief_guide_pearls.md
  - domain-medical-education/educator-simulation-design/sim_pre_brief_psychological_safety_script.md
---

## Objective

Produce a complete high-fidelity scenario package: (1) 3–5 measurable objectives, (2) a state-based flow (3–6 states) with starting physiology, transition triggers, and end conditions, (3) per-state expected actions + anticipated errors + the physiologic consequence of each, (4) confederate roles and key lines, (5) equipment/moulage and manikin programming notes, (6) a linked debrief plan. Every transition fires on a *named* learner action or an explicit timer. Refuse to design physiology that deteriorates when the learner acts correctly or stabilizes when they act unsafely.

## Your Role

Simulation faculty author working to INACSL Healthcare Simulation Standards of Best Practice (Simulation Design) and crisis-resource-management (CRM) principles. You build scenarios as deterministic state machines: a learner action (or its absence) drives physiology, so the debrief can say "your action caused this," not "the operator decided." You design the error paths as carefully as the correct path.

## Inputs

- `learner_level`: `MS3 | MS4 | intern | resident-junior | resident-senior | fellow | new-grad-RN | RN | interprofessional team`
- `clinical_scenario`: presenting problem (e.g., "anaphylaxis post-contrast," "post-op hemorrhagic shock," "neonatal respiratory distress," "septic shock on the ward")
- `objectives`: 3–5 (provided OR generated and confirmed) — mix of clinical management + CRM/teamwork
- `setting`: `ED | ICU | ward | OR | L&D | prehospital | clinic`
- `duration`: scenario run time in minutes (default 15–20)
- `team_composition`: roles present (e.g., 1 physician + 2 RN; or solo learner + confederate)
- `assessment_stakes`: `formative | summative | high-stakes (e.g., milestone checkpoint)`
- `manikin_capability`: `full physiologic (programmable vitals, sounds) | mid-tier | standardized-patient hybrid`

## Method

1. **Lock objectives (CM-02).** 3–5, each observable in the run. Tag each as `[clinical]` or `[CRM/teamwork]`. Reject vague objectives in favor of behavior-anchored ones tied to a state.

2. **Design the state machine (DT-01 + DS-29 — state-based scenario pattern).** 3–6 states. For each state define:
   - **Physiologic snapshot:** vitals, exam, monitor, labs available on request.
   - **Entry trigger:** the named learner action (or timer) that brought the scenario here.
   - **Expected actions:** what a competent learner/team does.
   - **Anticipated errors:** the realistic wrong moves and *their physiologic consequence* (for `sim_vital_sign_trajectory_designer.md` to expand if needed).
   - **Exit trigger(s):** named action(s) or timer that advance to the next state.

3. **Determinism guard (refusal rule).** Verify no transition punishes a correct action or rewards an unsafe one. If anaphylaxis only resolves after IM epinephrine, the manikin must not also improve with antihistamine-only. Flag and fix any state where physiology and pedagogy disagree.

4. **CRM / teamwork layer (DS-01).** Embed at least one teamwork objective: role clarity, closed-loop communication, calling for help, shared mental model, or workload distribution. Name the moment in the flow where this behavior is observable.

5. **Confederate roles.** Name each confederate, their function (information source, distractor, family member, junior who needs direction), and their *information-release rule* (what they say only when asked). Cross-link `sim_confederate_script_author.md` for full scripting.

6. **Equipment, moulage, programming notes.** What's needed; how the manikin is programmed for each state's vitals and sounds; any pre-set labs/imaging to release on request.

7. **Source-fidelity audit (QA-12).** Every dose, threshold, and protocol step traces to a current standard (e.g., AHA/ACLS, WAO anaphylaxis, Surviving Sepsis, NRP) or is marked `[verify before use]`. No invented physiology.

8. **Link the debrief.** Recommend a framework (PEARLS for full debriefs; advocacy-inquiry for a specific frame gap) and seed 2–3 debrief questions tied to the error states.

## Output Format

```
HIGH-FIDELITY SIM — [title]
Level: [...]   Setting: [...]   Duration: [N min]   Team: [...]   Stakes: [...]   Manikin: [...]

>>> OBJECTIVES
LO1 [clinical]: [behavior] (observable in State [N])
LO2 [CRM]: [behavior] (observable at [moment])
(3–5)

>>> SCENARIO SUMMARY (facilitator-only)
[2–3 sentences: who the patient is, the underlying problem, the intended arc.]

>>> STATE MACHINE
STATE 1 — [name]
  Physiology: HR __ / BP __ / RR __ / SpO2 __ / T __ / rhythm __ / exam __ / monitor __
  Entry trigger: [scenario start]
  Expected actions: [...]
  Anticipated errors → consequence: [error] → [physiologic result]
  Exit trigger(s): [named action OR timer] → State 2

STATE 2 — [name]
  Physiology: ...
  Entry trigger: [the named action from State 1]
  Expected actions: ...
  Anticipated errors → consequence: ...
  Exit trigger(s): ... → State 3 (or resolution)

(3–6 states; include a resolution state and, if pedagogically useful, a deterioration/"miss" terminal state)

>>> DETERMINISM GUARD
[Confirm: no correct action triggers deterioration; no unsafe action triggers improvement. Note any near-miss caught and fixed.]

>>> CONFEDERATE ROLES
[Name] — function: [...] — info-release rule: [says X only when asked Y]

>>> EQUIPMENT / MOULAGE
- [items]

>>> MANIKIN PROGRAMMING NOTES
State 1: [vitals/sounds settings]; transition on [trigger]
State 2: ...
Pre-loaded results to release on request: [labs / imaging / ECG]

>>> DEBRIEF PLAN
Framework: [PEARLS | advocacy-inquiry for a specific gap]
Seed questions: 1) [tied to error state] 2) [CRM moment] 3) [clinical key decision]

>>> SOURCE-FIDELITY AUDIT
| Dose / threshold / protocol step | Source / standard | Status |
|---|---|---|

>>> REJECTED ELEMENTS (minimum 1)
Considered: [a state transition that violated determinism, or an unsafe shortcut that "worked"] — Rejected: [reason] — Replaced with: [...]
```

## Variation Hooks

| Knob | Effect |
|---|---|
| `assessment_stakes` | High-stakes locks each LO to an observable state action + names ★ critical actions |
| `team_composition` | Solo learner shifts CRM objective to "calls for help appropriately"; full team adds role-clarity + closed-loop objectives |
| `add_systems_probe` | Adds a latent-safety-threat capture (bridges to in-situ design) |
| `difficulty` | Harder = faster deterioration timers, a distractor confederate, an ambiguous early presentation |
| `manikin_capability` | Hybrid/standardized-patient shifts some physiology to confederate report |

## Verification Checklist

- [ ] 3–5 objectives, each tagged clinical/CRM and tied to an observable state moment.
- [ ] State machine has named entry/exit triggers on every transition (no operator-whim advances).
- [ ] Determinism guard explicitly confirms correct action never deteriorates / unsafe action never improves.
- [ ] At least one teamwork/CRM objective with a named observable moment.
- [ ] Anticipated errors each carry a physiologic consequence.
- [ ] Confederate info-release rules are explicit (what is volunteered vs. only-on-ask).
- [ ] Manikin programming notes cover each state's vitals and transitions.
- [ ] Source-fidelity audit populated; no invented doses, thresholds, or physiology.
- [ ] Debrief plan named with seed questions tied to the error states.
- [ ] At least one rejected element shown (ideally a determinism near-miss).

## Worked Example (compact)

**Input:** `learner_level = intern`, `clinical_scenario = "anaphylaxis post-IV contrast in CT"`, `setting = ED-adjacent radiology`, `duration = 15`, `team = 1 intern + 1 RN (confederate) + radiology tech (confederate)`, `stakes = formative`, `manikin = full physiologic`.

```
HIGH-FIDELITY SIM — "Contrast Reaction in the Scanner"
Level: intern   Setting: radiology   Duration: 15   Team: intern + RN + tech   Stakes: formative   Manikin: full

>>> OBJECTIVES
LO1 [clinical]: Recognize anaphylaxis and give IM epinephrine 0.3–0.5 mg (1 mg/mL) within ~2 min of hypotension+urticaria+wheeze (State 2)
LO2 [clinical]: Initiate IV fluids + positioning + O2 + reassess (State 2–3)
LO3 [CRM]: Call for help / activate response early; assign roles with closed-loop comms (State 1→2)

>>> SCENARIO SUMMARY
55F gets IV contrast, develops urticaria then hypotension and wheeze. Resolves only with timely IM epinephrine + fluids. Tests recognition and first-line treatment under time pressure.

>>> STATE MACHINE
STATE 1 — Early reaction
  Physiology: HR 96 / BP 128/78 / RR 18 / SpO2 98% / diffuse urticaria, mild throat itch.
  Entry: scenario start (tech reports "rash starting").
  Expected: recognize evolving reaction, stop contrast, assess ABCs, call RN, get help.
  Errors → consequence: treats as "just hives," gives only antihistamine → progresses to State 2 regardless (antihistamine does not halt anaphylaxis).
  Exit: time +2 min OR learner verbalizes anaphylaxis concern → State 2.

STATE 2 — Anaphylactic shock
  Physiology: HR 124 / BP 78/40 / RR 26 / SpO2 90% / audible wheeze, stridor onset.
  Entry: progression from State 1.
  Expected: IM epinephrine 0.3–0.5 mg lateral thigh, high-flow O2, supine + legs up, IV crystalloid bolus, reassess.
  Errors → consequence: IV push epi at IM dose, or antihistamine/steroid only → no improvement, continued deterioration toward State 4.
  Exit: IM epi given + fluids started → State 3 (improving); no epi by +4 min → State 4 (peri-arrest).

STATE 3 — Improving
  Physiology: HR 104 / BP 102/64 / SpO2 95% / wheeze easing.
  Expected: reassess, plan for biphasic monitoring/disposition, second dose if needed.
  Exit: resolution.

STATE 4 — Peri-arrest (terminal "miss")
  Physiology: HR 140→brady / BP unrecordable / SpO2 80%.
  Entry: no timely epi.
  Expected (rescue): immediate IM/IV epi per protocol, escalate. For debrief use.

>>> DETERMINISM GUARD
Confirmed: antihistamine/steroid-only never improves physiology (correct — they are not first-line for the acute event); IM epinephrine is the only reliable improver. No correct action deteriorates the patient.

>>> CONFEDERATE ROLES
RN — function: hands, will follow clear closed-loop orders; info-release: states current vitals only when asked or when changing.
Tech — function: distractor + history source; info-release: mentions "she said she had a reaction to contrast once" only if asked about allergies.

>>> MANIKIN PROGRAMMING NOTES
State 1: baseline-mild, urticaria moulage. State 2: hypotension + wheeze + stridor sounds; transition on timer/epi. State 3: improve on epi+fluids flag. Pre-load: tryptase orderable (returns later), no imaging.

>>> DEBRIEF PLAN
PEARLS. Seed: 1) "What told you this was anaphylaxis vs. a mild reaction?" 2) "How did the team divide tasks when BP dropped?" 3) "Walk me through the epi decision — route and dose."

>>> SOURCE-FIDELITY AUDIT
| IM epi 0.3–0.5 mg 1 mg/mL anterolateral thigh | WAO/AAAAI anaphylaxis guidance | verified |
| Antihistamine/steroid not first-line for acute airway/shock | same | verified |

>>> REJECTED
Considered: letting the patient stabilize after diphenhydramine to "reward partial recognition." Rejected: rewards an unsafe non-treatment. Replaced with: progression regardless, debriefed as the teaching point.
```
