---
title: "DOPS Rubric Author (Direct Observation of Procedural Skills)"
category: medical-education/educator-rubrics-wba
description: "Author a Direct Observation of Procedural Skills (DOPS) form anchored to a specific procedure (e.g., central line, LP, intubation, suturing, IUD placement, joint injection). Includes a step-by-step checklist with verbatim observable behaviors at each step, a 9-point overall scale with band anchors, safety-critical step flags (auto-fail items), forced narrative, inter-rater calibration appendix. Refuses to ship without naming the safety-critical steps and the auto-fail criteria."
techniques:
  - ST-02
  - ST-03
  - DS-01
  - CM-02
  - DT-05
  - QA-12
difficulty: advanced
intended_use: model-testing
target_users:
  - clinical-educator
  - residency-program-director
  - simulation-faculty
  - cbme-faculty
tags:
  - dops
  - procedural-assessment
  - workplace-based-assessment
  - rubric
  - safety-critical
updated: "2026-05-18"
related_prompts:
  - domain-medical-education/educator-rubrics-wba/assess_minicex_rubric_author.md
  - domain-medical-education/educator-rubrics-wba/assess_epa_observation_form_author.md
  - domain-medical-education/educator-rubrics-wba/assess_entrustment_scale_designer.md
---

## Objective

Produce a DOPS form for one specific procedure: step-by-step checklist with verbatim observable behaviors per step, 9-point overall scale with band anchors, named safety-critical steps with auto-fail rules, post-procedure complication / communication elements, forced narrative, and inter-rater calibration appendix. Refuse to ship without identifying safety-critical steps and stating their auto-fail criteria.

## Your Role

Procedural-assessment rubric author. You design DOPS forms that distinguish technique adequate-for-indirect-supervision from technique that could harm a patient.

## Inputs

- `procedure_name`: e.g., "internal jugular central venous catheter placement," "lumbar puncture," "endotracheal intubation," "knee arthrocentesis," "IUD placement," "deep laceration suturing"
- `learner_level`: as before
- `setting`: simulation / supervised live / live with backup / independent
- `procedure_competency_target_level`: the supervision level a satisfactory rating supports (e.g., Chen-O-Brien or Dreyfus stage)
- `safety_critical_steps`: list of steps that, if missed or done incorrectly, automatically render the procedure unsafe
- `complication_recognition_list`: complications the learner must recognize and respond to
- `framework_basis`: `ACGME milestones | RCS UK DOPS | RCPSC | nurse-procedural / NCSBN`

## Method

1. **Decompose the procedure (DS-01 — task-decomposition).** Break into 8–20 discrete steps in order. Each step has:
   - A verbatim observable behavior at the satisfactory level.
   - A common error.
   - A safety-critical flag (yes/no).
   For a CVL: e.g., universal precautions/time-out → patient positioning → sterile prep + drape → ultrasound technique → needle insertion + flash → wire advancement → wire visualization → dilator → catheter → confirm wire withdrawal → secure → ultrasound/CXR confirmation.

2. **Lock safety-critical steps + auto-fail rules (CM-02).** Name each safety-critical step explicitly. State the auto-fail rule (e.g., "Wire visualization never confirmed before dilator → automatic unsatisfactory regardless of other steps").

3. **9-point overall scale with band anchors (DT-05).**
   - 1–3 unsatisfactory: cannot perform safely; safety-critical step missed; would require direct hands-on intervention.
   - 4–6 satisfactory: performs procedure safely with indirect supervision available; minor non-safety errors; needs minor coaching.
   - 7–9 superior: performs efficiently and teaches others; recognizes and manages complications independently; technique transferable.

4. **Post-procedure elements (ST-02).**
   - Procedural note completed and accurate.
   - Complication recognition (post-hoc Q&A or live observation).
   - Communication with patient + team about indication, risks, what was found.

5. **Forced narrative (ST-02).** Three required stems (≤ 100 words each):
   - One thing the learner did well (specific observed behavior).
   - One specific area for improvement.
   - Auto-fail observed? (yes/no; if yes, describe).

6. **Source-fidelity audit (QA-12).** Each procedural-standard reference cited.

7. **Inter-rater calibration appendix (ST-03).** Two worked-example procedural narratives with expected step-by-step scoring and target overall rating.

## Output Format

```
DOPS FORM — [procedure_name] — Learner level: [...] — Setting: [...]

>>> HEADER
Learner: ______________   Date: _______   Evaluator: ______________
Procedure attempt #: ____ (this learner)   Total prior attempts (logged): ____
Indication for procedure: _____________________________
Patient ASA / acuity: _________
Setting: simulation / supervised live / live with backup / independent

>>> STEP CHECKLIST (each: not-done / done-with-coaching / done-independently / not-applicable)

Step 1 — [step description]
Observable behavior (satisfactory): [verbatim]
Common error: [verbatim]
Safety-critical: yes / no
Rating: ☐ not-done   ☐ done-with-coaching   ☐ done-independently   ☐ NA

Step 2 — [...]
[...]
Rating: ...

...

Step N — [...]
[...]

>>> SAFETY-CRITICAL AUTO-FAIL RULES
1. [Named step] missed or incorrect → automatic unsatisfactory.
2. [Named step] missed or incorrect → automatic unsatisfactory.
3. ...

>>> COMPLICATION RECOGNITION
| Complication | Recognized? | Response appropriate? |
|---|---|---|
| [each from complication_recognition_list] | yes / no / not-observed | yes / no / not-observed |

>>> POST-PROCEDURE
Procedural note: present / absent / incomplete (describe)
Patient communication post-procedure: yes / no / not-observed
Team communication / handoff: yes / no / not-observed

>>> 9-POINT OVERALL RATING
Unsatisfactory (1–3) anchor: "Cannot complete procedure safely; safety-critical step missed; required hands-on intervention; would not entrust without direct supervision."
Satisfactory (4–6) anchor: "Completes procedure safely with indirect supervision; minor non-safety coaching offered; would entrust with backup available."
Superior (7–9) anchor: "Completes procedure independently and efficiently; could supervise a junior; recognized and managed complication or near-miss appropriately."
Rating: ___

Auto-fail observed? ☐ yes ☐ no
If yes, which rule + describe: _____________________________

>>> FORCED NARRATIVE (each ≤ 100 words, required)
1. Best-observed behavior:
   _______________________________________________

2. Highest-priority improvement (specific behavior + next-step):
   _______________________________________________

3. Auto-fail / safety concern (leave blank if none):
   _______________________________________________

>>> EVALUATOR SIGNATURE
Evaluator: ______________   Time observing: ____ min   Time in feedback: ____ min   Date: _______
Learner sign-off: ______________   Date: _______

>>> INTER-RATER CALIBRATION APPENDIX

Worked Example A — Satisfactory CVL
Scenario: PGY2 places R IJ CVL on a stable inpatient. Time-out done. Ultrasound-guided. Wire visualized in long axis pre-dilator. Confirms wire withdrawal at end. CXR post-line. Brief teach-back about indication with patient family.
Expected per-step ratings: most done-independently; ultrasound step done-with-coaching (suboptimal needle visualization briefly).
Expected overall: 6.
Auto-fail: no.

Worked Example B — Unsatisfactory CVL
Scenario: PGY1 attempts R IJ CVL. Skips wire visualization step before dilator. Wire is withdrawn but never visualized in vessel beforehand.
Expected: regardless of other steps, automatic unsatisfactory due to safety-critical rule. Recommended overall: 2.
Auto-fail: yes (Rule 1).

Calibration discussion (new raters): "Walk through each step's verbatim anchor. For any step rated differently from peers, discuss the specific behavior observed. Target κ ≥ 0.7 on overall (procedural assessments can hit higher κ than Mini-CEX). For safety-critical steps, target κ ≥ 0.85."

>>> SOURCE-FIDELITY AUDIT
| Reference | Source | Status |
|---|---|---|
| Procedural standard / consensus | [e.g., SCCM ICU CVL guidelines 2024, ACS suturing standards] | verified |
| Ultrasound-guided CVL technique | NEJM 2011 long-axis vs short-axis review | verified |
| Auto-fail rule rationale | unit-level adverse-event review | locally documented |

>>> REJECTED ELEMENT (minimum 1)
Considered: a single overall rating without step-level checklist.
Rejected: hides where in the procedure the learner needs coaching; defeats DOPS purpose.
Replaced with: step-by-step + overall.
```

## Variation Hooks

| Knob | Effect |
|---|---|
| `procedure_name` | Drives step list and safety-critical rules entirely |
| `learner_level` | Recalibrates satisfactory band (intern's satisfactory CVL ≠ fellow's superior CVL) |
| `setting` | `simulation` permits coaching at every step; `supervised live` shifts to indirect; `independent` excludes coaching column |
| `framework_basis` | ACGME milestones / RCS UK / RCPSC / NCSBN — adjusts anchor language and competency mapping |
| `include_team_dynamics` | Adds team-communication and closed-loop element (e.g., for codes / RSI) |
| `include_consent` | Adds informed-consent observation step (for elective procedures) |

## Verification Checklist

- [ ] Step list 8–20 items in procedural order.
- [ ] Each step has verbatim observable behavior + common error + safety-critical flag.
- [ ] Safety-critical steps named with explicit auto-fail rules.
- [ ] 9-point overall scale anchored at three bands with behavioral language.
- [ ] Complication recognition table included.
- [ ] Post-procedure documentation / communication elements included.
- [ ] Forced narrative section with 3 required stems.
- [ ] Inter-rater calibration appendix with 2 worked examples (one with auto-fail).
- [ ] Cohen κ targets: overall ≥ 0.7; safety-critical steps ≥ 0.85.
- [ ] Source-fidelity audit populated.
- [ ] At least one rejected element shown.

## Worked Example (compact)

**Input:** `procedure_name = "Internal jugular CVL"`, `learner_level = PGY2`, `setting = supervised live`, `safety_critical_steps = [time-out, sterile field maintenance, wire-visualization-before-dilator, confirm-wire-withdrawal, post-line CXR before non-emergent use]`, `complication_recognition_list = [arterial puncture, pneumothorax, retained-wire, line-tip-misplacement]`.

**Output:** see Output Format block above — instantiated for IJ CVL with 12 steps, 5 auto-fail rules, and the two worked-example narratives in the appendix.
