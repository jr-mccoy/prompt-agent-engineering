---
title: "EPA Observation Form Author (Entrustable Professional Activity Workplace Assessment)"
category: medical-education/educator-rubrics-wba
description: "Author an EPA observation form for one specific Entrustable Professional Activity (e.g., AAMC Core EPA 1 — gather history and physical; ACGME EPA — manage a patient in heart failure exacerbation). Output includes EPA definition, observable behaviors per nested competency, the 5-level entrustment scale (with verbatim band anchors), context modifiers (acuity / complexity / chart access), forced narrative, and inter-rater calibration appendix. Refuses to ship an EPA form that does not specify the supervision-level rubric or that uses anchors lacking observable behavior."
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
  - clerkship-director
  - cbme-faculty
  - competency-committee-member
tags:
  - epa
  - entrustment
  - workplace-based-assessment
  - cbme
  - supervision-level
updated: "2026-05-18"
related_prompts:
  - domain-medical-education/educator-rubrics-wba/assess_minicex_rubric_author.md
  - domain-medical-education/educator-rubrics-wba/assess_dops_rubric_author.md
  - domain-medical-education/educator-rubrics-wba/assess_cbd_rubric_author.md
  - domain-medical-education/educator-rubrics-wba/assess_entrustment_scale_designer.md
---

## Objective

Produce a workplace-based assessment form for one named EPA: EPA definition + nested competencies / milestones + observable behaviors at each entrustment level + 5-level entrustment scale (Chen-O-Brien or ten Cate variants) with verbatim band anchors + context modifiers + forced narrative + inter-rater calibration appendix. Refuse to ship without a stated supervision-level rubric or with anchors that omit observable behaviors.

## Your Role

EPA assessment-form architect. Your forms turn a high-level professional activity into a specific, observable rating that a competency committee can defend at promotion.

## Inputs

- `epa_id`: e.g., "AAMC Core EPA 1," "AAMC EPA 10 — Recognize a Patient Requiring Urgent or Emergent Care," "AAIM ACP EPA 4 — Care of Hospitalized Patient with End-of-Life Issues"
- `epa_definition`: the official narrative definition
- `nested_competencies`: list of competencies / milestones the EPA integrates (e.g., communication, medical knowledge, patient care)
- `learner_level`: as before
- `entrustment_scale`: `Chen-O-Brien 5-level | ten-Cate 5-level | AAMC 4-level supervision | program-specific` (default Chen-O-Brien)
- `context_modifiers`: acuity, complexity, language barrier, chart access, time pressure
- `expected_entrustment_at_level`: target supervision level for `learner_level` (e.g., MS4 target = level 3 / indirect supervision; PGY2 target = level 4 / direct supervision available)
- `framework_basis`: AAMC / ACGME / ABIM / specialty society

## Method

1. **EPA + nested competency lock (DS-01 — EPA-as-integrated-competency).** State the EPA's official definition, then list nested competencies (e.g., "this EPA integrates ACGME competencies: PC1, PC3, MK2, CS1, ICS1"). Each nested competency gets an observable-behavior anchor in the form.

2. **5-level entrustment scale with verbatim anchors (DT-05 — supervision bands).**
   - **Level 1 — Observation only.** Not allowed to perform.
   - **Level 2 — Direct supervision present.** Performs only with supervisor in room.
   - **Level 3 — Indirect supervision (proactive).** Performs with supervisor immediately available; supervisor reviews work at decision points.
   - **Level 4 — Indirect supervision (reactive).** Performs; supervisor available on request; review post-hoc.
   - **Level 5 — Distant / unsupervised.** Performs autonomously; may supervise others.
   Each level requires verbatim observable-behavior anchors specific to this EPA at this level.

3. **Observable-behavior list per nested competency (ST-02).** Per competency, list 2–4 verbatim observable behaviors that map to entrustment levels. Avoid "understands" / "appreciates" / "shows insight" — use utterance, action, or document phrasing.

4. **Context modifiers (CM-02 — explicit context).** State that entrustment level is context-specific. The form captures:
   - Acuity at observation: routine / moderate / high.
   - Complexity: routine / moderate / complex.
   - Language / cultural barrier: yes / no.
   - Chart access: full / partial / none.
   - Time pressure: standard / compressed.
   Entrustment may differ across contexts; form requires assessor to specify the context.

5. **Forced narrative (ST-02).** Three required stems: ≤ 100 words each. Best behavior, top improvement, escalation flag.

6. **Refusal guard (CM-02).** If any anchor omits observable behavior or any level lacks an anchor, refuse to ship.

7. **Source-fidelity audit (QA-12).** Cite EPA-framework documentation; cite supervision-scale reference.

8. **Inter-rater calibration appendix (ST-03).** Two worked-example assessments at different supervision levels; calibration discussion script.

## Output Format

```
EPA OBSERVATION FORM — [epa_id] — Learner level: [...] — Framework: [...]

>>> EPA DEFINITION
[Official narrative definition, verbatim from the framework.]

>>> NESTED COMPETENCIES INTEGRATED
| Competency / Milestone | Code |
|---|---|
| [e.g., Patient Care 1] | PC1 |
| [...] | ... |

>>> CONTEXT OF THIS OBSERVATION
Acuity: routine / moderate / high
Complexity: routine / moderate / complex
Language or cultural barrier: yes / no
Chart access: full / partial / none
Time pressure: standard / compressed
Observation duration: ____ min

>>> OBSERVABLE BEHAVIORS PER COMPETENCY
| Competency | Observable behavior 1 | Behavior 2 | Behavior 3 | Behavior 4 (if Sup) |
|---|---|---|---|---|
| [PC1] | "[verbatim]" | "[verbatim]" | "[verbatim]" | "[verbatim]" |
| [...] | ... | ... | ... | ... |
[Each behavior tagged to the entrustment level it represents.]

>>> ENTRUSTMENT SCALE (Chen-O-Brien 5-level)

LEVEL 1 — Observation only
Anchor: "Cannot perform key elements safely; required hands-on intervention; supervisor reluctant to allow even partial participation."
Verbatim behavior examples for this EPA: [...]

LEVEL 2 — Direct supervision (in room)
Anchor: "Performs with supervisor physically present and able to intervene immediately; multiple safety-critical prompts needed."
Verbatim behavior examples: [...]

LEVEL 3 — Indirect supervision (proactive)
Anchor: "Performs with supervisor immediately available; supervisor reviews at decision points (e.g., differential, plan, disposition); minor coaching at non-safety steps."
Verbatim behavior examples: [...]

LEVEL 4 — Indirect supervision (reactive)
Anchor: "Performs without prompt; supervisor available on request; post-hoc review reveals no safety-critical issues."
Verbatim behavior examples: [...]

LEVEL 5 — Distant / unsupervised
Anchor: "Performs autonomously without need for supervision; can teach the EPA; can supervise a junior learner."
Verbatim behavior examples: [...]

>>> ENTRUSTMENT DECISION
Today's entrustment level (this context): ☐ 1 ☐ 2 ☐ 3 ☐ 4 ☐ 5
Target level for learner_level: [...]
Gap from target: ___ (negative / zero / positive)

>>> FORCED NARRATIVE (each ≤ 100 words)
1. Best-observed behavior:
   _______________________________________________

2. Highest-priority improvement (specific behavior + next-step):
   _______________________________________________

3. Escalation flag (safety concern / professionalism / repeat low entrustment):
   _______________________________________________

>>> EVALUATOR SIGNATURE
Evaluator: ______________   Time observing: ____ min   Date: _______
Learner sign-off: ______________   Date: _______

>>> INTER-RATER CALIBRATION APPENDIX

Worked Example A — Entrustment level 4 observation
Scenario: PGY2 IM observes the EPA "Recognize a patient requiring urgent care." Resident receives a deteriorating ward patient, identifies severe sepsis, initiates bundle, escalates appropriately. Supervisor reviewed post-hoc; no safety gaps.
Expected: Level 4 (reactive indirect supervision). Verbatim utterance support: "Resident said: 'qSOFA positive, lactate 4.2, starting fluids and broad-spectrum, ICU notified.'"
Common rater error: Level 5 if rater equates "no help needed" with "could be unsupervised" — but EPA-level 5 requires demonstrated supervisory capability not assessed here.

Worked Example B — Entrustment level 2 observation
Scenario: MS3 same EPA. Identifies "patient looks unwell" but cannot articulate specific deterioration criteria; supervisor needed to prompt qSOFA computation and bundle initiation; multiple safety-critical prompts.
Expected: Level 2. Common rater error: Level 3 if rater rates effort rather than independence.

Calibration discussion (new raters): focus on independence dimension, not effort or content knowledge. Target Cohen κ on overall entrustment ≥ 0.6.

>>> SOURCE-FIDELITY AUDIT
| Reference | Source | Status |
|---|---|---|
| EPA definition | [AAMC 2014 / ACGME-specialty / specialty society] | verified |
| Chen-O-Brien 5-level scale | Chen 2015 Acad Med | verified |
| ten Cate 5-level | ten Cate 2015 Med Teach | verified |
| Framework integration | [AAMC EPA Toolkit / specialty body] | verified |

>>> REJECTED ELEMENT (minimum 1)
Considered: anchor "Demonstrates good clinical reasoning."
Rejected: not observable; no behavior phrasing.
Replaced with: "Articulates 3-item differential with weights and discriminating features in oral presentation."
```

## Variation Hooks

| Knob | Effect |
|---|---|
| `entrustment_scale` | Chen-O-Brien 5-level / ten-Cate 5-level / AAMC 4-level — wording differs slightly |
| `framework_basis` | AAMC Core EPAs (UME) / ACGME EPAs (GME specialty) / RCPSC EPAs / specialty-society EPAs |
| `learner_level` | Target entrustment level changes; e.g., MS4 = level 3 typical |
| `context_modifiers` | Form explicitly notes context-specific entrustment; same learner may be level 4 in routine and level 2 in complex |
| `include_summative_recommendation` | Adds a "would you recommend for advancement to next supervision phase?" item |
| `include_co-activity_log` | If EPA requires N entrustments before progression, links to log |

## Verification Checklist

- [ ] EPA definition stated verbatim from framework.
- [ ] Nested competencies listed with codes.
- [ ] Observable behaviors per competency are utterance-or-action phrased.
- [ ] All 5 entrustment levels have verbatim anchors.
- [ ] Context modifiers captured.
- [ ] Entrustment decision explicit with gap-from-target.
- [ ] Forced narrative with 3 stems.
- [ ] Inter-rater calibration appendix with 2 worked examples.
- [ ] Cohen κ ≥ 0.6 stated.
- [ ] Source-fidelity audit populated.
- [ ] At least one rejected element shown.

## Worked Example (compact)

**Input:** `epa_id = "AAMC Core EPA 10 — Recognize a Patient Requiring Urgent or Emergent Care"`, `learner_level = MS4`, `entrustment_scale = Chen-O-Brien 5-level`, `expected_entrustment_at_level = 3`, `framework_basis = AAMC Core EPAs`.

**Output:** see Output Format block above — instantiated for EPA 10 with deteriorating-ward-patient scenario and calibration appendix.
