---
title: "Low-Fidelity Simulation Scenario Author (Task-Trainer / Verbal-Driven)"
category: medical-education/educator-simulation-design
description: "Author a complete low-fidelity simulation scenario built on a task trainer, partial-task model, or verbal/paper-driven format: 2–4 measurable objectives, a simple state flow, scripted facilitator cues, an expected-actions checklist, equipment list, and a debrief hook. Matches scenario complexity to fidelity — refuses to over-engineer a manikin-grade physiologic trajectory onto a skill that a task trainer teaches better."
techniques:
  - ST-02
  - ST-03
  - DS-01
  - CM-02
  - DT-01
  - QA-12
difficulty: intermediate
intended_use: model-testing
target_users:
  - clinical-educator
  - simulation-faculty
  - curriculum-designer
  - program-director
tags:
  - simulation
  - low-fidelity
  - task-trainer
  - scenario-design
  - INACSL
updated: "2026-05-29"
related_prompts:
  - domain-medical-education/educator-simulation-design/sim_high_fidelity_scenario_author.md
  - domain-medical-education/educator-simulation-design/sim_pre_brief_psychological_safety_script.md
  - domain-medical-education/educator-simulation-design/sim_debrief_plus_delta_facilitation.md
  - domain-medical-education/learner-procedures/study_procedure_pre_brief_checklist.md
---

## Objective

Produce a complete low-fidelity simulation package: (1) 2–4 measurable learning objectives, (2) a simple linear or two-branch state flow, (3) facilitator cue script (what is said/shown when), (4) an observable expected-actions checklist, (5) equipment/moulage list, (6) a debrief hook. Match scenario depth to fidelity: low-fidelity scenarios teach discrete skills, single decisions, or protocol steps — not multi-system physiologic deterioration. Refuse to bolt a full vital-sign trajectory onto a scenario whose objective is a discrete task.

## Your Role

Simulation scenario author working to INACSL Healthcare Simulation Standards of Best Practice (Simulation Design). You design the *smallest sufficient* scenario: enough realism to make the objective assessable, no more. You'd rather run a crisp 8-minute task-trainer station than a bloated immersive case that buries one objective under production value.

## Inputs

- `learner_level`: `MS1 | MS2 | MS3 | MS4 | intern | resident-junior | nursing-student | new-grad-RN | PA-student | EMS-trainee | allied-health-student`
- `target_skill`: the discrete skill or decision (e.g., "sterile gloving," "NG tube placement confirmation," "STEMI activation decision," "epi auto-injector teaching")
- `modality`: `task trainer | partial-task model | paper/verbal case | role-play | hybrid (trainer + verbal)`
- `objectives`: 2–4 (provided OR generated and confirmed)
- `time_available`: minutes per learner/station (default 10)
- `group_format`: `1:1 | small group rotating | station circuit`
- `assessment_stakes`: `formative | summative checkpoint`

## Method

1. **Lock objectives (CM-02).** 2–4 objectives, each behavior-anchored and observable in `time_available`. Reject vague objectives ("understand sterile technique") in favor of "maintain sterile field through glove application with zero contamination breaks." If `assessment_stakes = summative`, each objective must map to a checklist line.

2. **Fidelity match (DS-01 — INACSL design standard, refusal guard).** Confirm low fidelity is correct for the objective. If the objective requires real-time physiologic feedback (titrating pressors to a BP response), flag that this belongs in `sim_high_fidelity_scenario_author.md` and downscope here to the trainable low-fi sub-skill.

3. **Build the state flow (DT-01).** Low-fi flow is linear or single-branch:
   - **State 0 — Setup/orientation:** what the learner sees and is told.
   - **State 1 — Task/decision:** the core action.
   - **Branch (optional):** correct path vs. one engineered error path with a facilitator cue.
   - **State 2 — Resolution:** end condition that signals the station is complete.

4. **Facilitator cue script.** Scripted, verbatim where it matters: opening stem, the prompt that starts the task, the single cue that fires if the learner stalls, and the standardized response to the most common wrong move (a cue, not the answer).

5. **Expected-actions checklist (DT-05-style, observable).** Dichotomous (done / not done) or 3-anchor. Every line is an observable behavior with a verbatim phrasing standard — no "appropriate," no "thorough."

6. **Equipment + moulage list.** Exactly what's needed; nothing decorative. Flag any consumable cost.

7. **Source-fidelity audit (QA-12).** Any clinical threshold, dose, or protocol step cited must trace to a current standard or be marked `[verify before use]`. No invented protocol steps.

## Output Format

```
LOW-FIDELITY SIM — [title]
Level: [...]   Modality: [...]   Time: [N min]   Format: [...]   Stakes: [...]

>>> OBJECTIVES (observable)
LO1: [behavior] (→ checklist C1)
LO2: ...
(2–4)

>>> FIDELITY-MATCH NOTE
[One line confirming low-fi is correct, or what was downscoped from a higher-fi version.]

>>> STATE FLOW
State 0 (Setup): [what learner sees + is told — verbatim opening]
State 1 (Task): [core action; how it is initiated]
  Branch-correct: [end condition]
  Branch-error: [most common wrong move] → Facilitator cue: "[verbatim cue, not the answer]"
State 2 (Resolution): [end condition that closes the station]

>>> FACILITATOR CUE SCRIPT
Opening stem: "[verbatim]"
Start prompt: "[verbatim]"
Stall cue (if no action in ~[N]s): "[verbatim]"
Standardized error response: "[verbatim cue]"

>>> EXPECTED-ACTIONS CHECKLIST
C1 [→LO1]: [observable behavior]                      [ ] done [ ] not
C2 [→LO2]: ...
(critical-safety lines marked ★ = auto-fail if missed at summative stakes)

>>> EQUIPMENT / MOULAGE
- [item] x[qty]   ([consumable cost flag if any])

>>> DEBRIEF HOOK
Recommended debrief: [plus-delta for ≤10 min stations | PEARLS if reasoning-heavy]
Two opening questions tied to LO1 / the error branch.

>>> SOURCE-FIDELITY AUDIT
| Clinical claim / protocol step | Source / standard | Status |
|---|---|---|

>>> REJECTED ELEMENTS (minimum 1)
Considered: [over-built element, e.g., a deterioration trajectory] — Rejected: [reason] — Replaced with: [...]
```

## Variation Hooks

| Knob | Effect |
|---|---|
| `modality` | Task trainer = more checklist; verbal case = more cue script |
| `assessment_stakes` | Summative locks each LO to a checklist line + names ★ auto-fail items |
| `group_format` | Circuit format adds a reset/turnover note between learners |
| `time_available` | <8 min → drop the error branch; ≥12 min → add a second decision |
| `add_distractor` | Inserts one realistic but irrelevant stimulus to test prioritization |

## Verification Checklist

- [ ] 2–4 objectives, each observable in the time budget.
- [ ] Fidelity-match note confirms low-fi is the right tool (or names the downscope).
- [ ] State flow is linear or single-branch (not a multi-state physiologic cascade).
- [ ] Facilitator cues are verbatim and redirect rather than reveal the answer.
- [ ] Every checklist line is an observable behavior with no adjective-only anchors.
- [ ] Safety-critical lines marked ★ when stakes are summative.
- [ ] Equipment list has no decorative items; consumable costs flagged.
- [ ] Source-fidelity audit populated; no invented protocol steps.
- [ ] At least one rejected (over-built) element shown.

## Worked Example (compact)

**Input:** `learner_level = nursing-student`, `target_skill = "NG tube placement confirmation before feeding"`, `modality = partial-task model`, `time = 10`, `format = station circuit`, `stakes = summative`.

```
LOW-FIDELITY SIM — "Confirm Before You Feed"
Level: nursing-student   Modality: partial-task   Time: 10 min   Format: circuit   Stakes: summative

>>> OBJECTIVES
LO1: State and perform the institution's confirmation steps before instilling anything (→C1–C4)
LO2: Withhold feeding when placement is unconfirmed (→C5)

>>> FIDELITY-MATCH NOTE
Low-fi correct: objective is a confirmation protocol, not titration. Downscoped a "patient desats during feeding" arc to the high-fi library.

>>> STATE FLOW
State 0: Learner finds a mannequin torso with NG tube taped, a syringe, pH strips, an order "Begin tube feeds."
State 1: Learner must confirm placement before starting feeds.
  Branch-correct: aspirate → pH ≤5.5 documented → states X-ray is gold standard for initial placement → proceeds.
  Branch-error: starts feeding after auscultation only → Facilitator cue: "Walk me through how you know the tip is gastric."
State 2: Learner either holds feeds pending X-ray or proceeds per a confirmed result.

>>> FACILITATOR CUE SCRIPT
Opening: "You're caring for this patient at start of shift. Here is the order."
Start prompt: "What do you do first?"
Stall cue: "What has to be true before anything goes down this tube?"
Standardized error response: "Auscultation alone — is that sufficient per policy? Why or why not?"

>>> EXPECTED-ACTIONS CHECKLIST
C1 ★ Verifies order + patient ID                       [ ]
C2 Aspirates gastric contents / checks pH              [ ]
C3 States radiographic confirmation is the standard for initial placement [ ]
C4 Documents confirmation method + result              [ ]
C5 ★ Withholds feeding if placement unconfirmed        [ ]

>>> EQUIPMENT
NG partial-task torso x1, 60mL catheter-tip syringe, pH strips, simulated gastric fluid (cost flag).

>>> DEBRIEF HOOK
Plus-delta. Q1: "What confirmed gastric placement for you?" Q2 (error branch): "When is auscultation misleading?"

>>> SOURCE-FIDELITY AUDIT
| pH ≤5.5 supports gastric placement | AACN / institutional policy | verify against local policy |
| X-ray = standard for initial confirmation | institutional policy | verified |

>>> REJECTED
Considered: feeding-aspiration desaturation arc. Rejected: requires physiologic feedback (high-fi). Replaced with: confirm-or-hold decision.
```
