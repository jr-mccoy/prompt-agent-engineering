---
title: "Treatment Non-Response Decision Tree"
category: psychology/measurement-based-care
description: "A structured decision tree for when a client is not responding by the expected point: rule out measurement artifact, alliance, adherence, dose, diagnosis-fit, and comorbidity before sequencing reformulate / intensify / augment / switch modality / step up level of care / refer."
techniques:
  - RT-02
  - DT-01
  - DS-02
  - QA-04
  - CM-02
difficulty: advanced
intended_use: model-testing
tags:
  - measurement-based-care
  - treatment-non-response
  - decision-tree
  - treat-to-target
  - reformulation
  - augmentation
  - feedback-informed-treatment
updated: "2026-06-08"
related_prompts:
  - domain-psychology/measurement-based-care/psychology_individual_rom_trajectory_analyzer.md
  - domain-psychology/treatment-planning/psychology_treatment_resistance_reformulation.md
  - domain-psychology/treatment-planning/psychology_stepped_care_decision_aid.md
  - domain-psychology/measurement-based-care/psychology_mbc_implementation_plan_for_practice.md
---

# Treatment Non-Response Decision Tree

## Objective

Provide a structured, sequenced decision tree for the not-on-track / non-responding case — a client who has not reached response or remission by the expected point on routine outcome monitoring (ROM). Before any treatment change, the tree forces rule-out of the cheap, reversible explanations (measurement artifact, alliance strain, adherence, dose/duration, diagnostic fit, unaddressed comorbidity). Only then does it sequence the corrective options: reformulate the case, intensify the current treatment, augment, switch modality, step up level of care, or refer out. The output is a defensible, treat-to-target decision record showing what was ruled out, what was selected, and the re-measurement plan that closes the loop.

## When to Use

- When the individual ROM trajectory analyzer (or a registry caseload flag) has classified a client as not-on-track or non-responding past the expected point.
- At the formal non-response review (commonly session 8, or the equivalent week in IOP/PHP) when MCID-level improvement has not been achieved.
- When a treatment has plateaued for ≥4 sessions without reaching the remission band.
- When a treat-to-target / collaborative-care protocol requires a documented "adjust treatment" step before continuing.
- When a supervisor or treatment team needs a structured rationale for why a treatment is being changed (or held).

## Inputs / Context Required

- **ROM trajectory**: the primary-instrument score series, baseline severity, current session, and the not-on-track / non-response determination (with method).
- **Primary instrument(s)**: PHQ-9, GAD-7, PCL-5, OCI-R/Y-BOCS, ORS/OQ-45, AUDIT/DAST-10 — to apply correct MCID, remission band, and RCI.
- **Current treatment**: modality, specific techniques, frequency, duration delivered, and medication if any.
- **Adherence data**: attendance, homework/skills completion, medication adherence.
- **Alliance data**: SRS/WAI-SR series if collected.
- **Diagnosis and formulation**: current DSM-5-TR diagnoses, case formulation, and known comorbidities (including SUD, medical, personality, neurodevelopmental).
- **Prior treatment history**: what has been tried this episode and in prior episodes, with response.
- `[clinician input required: whether a structured diagnostic re-assessment is feasible, or whether diagnostic fit must be judged clinically this cycle]`
- `[clinician input required: medication status and prescriber involvement, if augmentation or step-up may involve pharmacotherapy]`

## Constraints

### Must

- Confirm the non-response determination is real before acting: verify the trajectory exceeds measurement error (RCI/MCID) and that the "expected point" was correctly applied for this baseline severity. A noise-level read is not non-response.
- Work the rule-out gate **in order** before considering any treatment switch: (1) measurement artifact, (2) alliance, (3) adherence/dose/duration, (4) diagnostic fit, (5) unaddressed comorbidity. Document the disposition of each.
- Prefer the least disruptive effective change: exhaust optimize-the-current-treatment options (alliance repair, adherence, dose/duration, fidelity) before escalating to switch / augment / step-up.
- Use instrument-correct anchors throughout (PHQ-9 remission ≤4 / MCID 5; GAD-7 remission ≤4 / MCID 4; PCL-5 ≥31–33 probable PTSD / MCID 10); tie any reliable-change claim to a published RCI.
- Attach a **re-measurement plan** to every selected action: the metric, the next decision point, and the threshold that defines success of the adjustment (closing the feedback loop).
- Screen risk at the gate: any active PHQ-9 item-9 / PCL-5 elevation or deterioration is handled as a safety item and can override the sequence (may require step-up / safety planning before further treatment-change analysis).
- Flag when non-response after adequate optimization warrants reformulation (route to the treatment-resistance reformulation prompt) or referral.

### Must Not

- Do not switch or augment treatment before ruling out measurement artifact, alliance, adherence, and dose — most "non-response" resolves at these gates.
- Do not call a treatment a failure if it was never delivered at adequate dose/duration with fidelity (under-dosing is not non-response).
- Do not change multiple variables at once such that the next ROM read cannot attribute change; change one lever, then re-measure (unless safety requires more).
- Do not skip the diagnostic-fit and comorbidity gates; a mistargeted or comorbidity-confounded treatment will not respond no matter how it is intensified.
- Do not fabricate MCID/RCI values or an expected-treatment-response curve; label any approximation.
- Do not defer an active risk flag to the treatment-change discussion.

## Instructions

1. **Confirm non-response is real (entry gate).** Verify the trajectory exceeds RCI/MCID-level criteria and that the expected point was applied correctly for the baseline severity. If it is within measurement error, stop and re-measure rather than acting.

2. **Safety screen.** Check for active risk (PHQ-9 item 9, PCL-5 elevation, reliable deterioration). If present, address safety / consider step-up before continuing the tree; note that safety can override the optimization sequence.

3. **Gate 1 — Measurement artifact.** Could the score mislead? Check instrument-vs-target match, response style/bias, language/literacy fit, timing of administration, and whether the wrong domain is being measured (e.g., tracking depression while the active problem is trauma). Disposition: cleared / corrective action.

4. **Gate 2 — Alliance.** Review SRS/WAI-SR. If below cut or declining, prioritize rupture repair / collaborative review before any technique change. Disposition: cleared / repair plan.

5. **Gate 3 — Adherence, dose, duration, fidelity.** Was the treatment actually delivered as intended — attendance, homework/skills practice, medication adherence, adequate number of sessions, delivered with fidelity? If under-dosed or low-adherence, the corrective action is to deliver an adequate course, not to switch. Disposition: cleared / dose-correction plan.

6. **Gate 4 — Diagnostic fit.** Is the formulation still correct? Reconsider missed/changed diagnosis, subtype, or a maintaining mechanism not yet targeted. If fit is in doubt, re-assess. Disposition: cleared / re-assessment plan.

7. **Gate 5 — Comorbidity.** Is an unaddressed comorbidity (SUD, trauma, personality, neurodevelopmental, medical, sleep) blocking response? If so, the comorbidity may need to be sequenced or treated concurrently. Disposition: cleared / comorbidity plan.

8. **Select the corrective action (only after gates).** If gates are cleared and non-response persists, sequence from least to most disruptive:
   - **Reformulate** the case (route to reformulation prompt) and re-target.
   - **Intensify** current treatment (frequency, dose, between-session work).
   - **Augment** (add an evidence-based component or pharmacotherapy via prescriber).
   - **Switch modality** to a different evidence-based treatment for the target.
   - **Step up level of care** (route to stepped-care decision aid).
   - **Refer** out (specialty, higher acuity, or different discipline).
   Change one lever where safety permits.

9. **Attach the re-measurement plan.** Define the metric, the next decision point (session/week), and the threshold that defines success of this adjustment. Specify the fallback if the adjustment also fails.

10. **Run verification.**

## Output Format

```
=== TREATMENT NON-RESPONSE DECISION TREE ===

ENTRY GATE — IS NON-RESPONSE REAL?
Instrument: [..]  Baseline: [..]  Current: [#/score]  Expected point applied: [session/week]
Exceeds RCI/MCID criterion? [Yes → proceed | No → re-measure, do not act]
Method for "expected": [Formal ETR / severity-anchored approximation — labeled]

SAFETY SCREEN
[ ] No active risk — proceed.
[ ] Active risk (PHQ-9 item 9 / PCL-5 / deterioration): [describe] → [safety action / consider step-up] — may override sequence.

────────────────────────────────────────────────────────
RULE-OUT GATES (work in order)

| Gate | Question | Finding | Disposition (cleared / corrective action) |
|------|----------|---------|-------------------------------------------|
| 1. Measurement artifact | Right instrument, domain, timing, response bias? | [..] | [..] |
| 2. Alliance | SRS/WAI-SR below cut or declining? | [..] | [..] |
| 3. Adherence / dose / duration / fidelity | Delivered as intended at adequate dose? | [..] | [..] |
| 4. Diagnostic fit | Formulation still correct? Missed Dx/mechanism? | [..] | [..] |
| 5. Comorbidity | Unaddressed comorbidity blocking response? | [..] | [..] |

Gate summary: [Which gate(s) explained the non-response, if any — corrective action taken there first.]

────────────────────────────────────────────────────────
CORRECTIVE ACTION (only if gates cleared and non-response persists)

Selected (least → most disruptive; pick one lever where safety permits):
[ ] Reformulate case → route to treatment-resistance reformulation
[ ] Intensify current treatment: [frequency/dose/between-session change]
[ ] Augment: [added component / pharmacotherapy via prescriber]
[ ] Switch modality: [from ___ to ___ (evidence-based for target)]
[ ] Step up level of care → route to stepped-care decision aid
[ ] Refer out: [specialty / discipline / acuity]
Rationale: [Why this lever, why now, why least-disruptive-effective.]

────────────────────────────────────────────────────────
RE-MEASUREMENT PLAN (close the loop)
Metric: [instrument + threshold]
Next decision point: [session/week]
Success threshold for this adjustment: [e.g., ≥ MCID by session N]
Fallback if adjustment fails: [next lever / reformulation / referral]
Documenting clinician + review: [clinician input required]
```

## Verification

- [ ] Non-response confirmed to exceed RCI/MCID before any action (noise-level read sent back to re-measurement).
- [ ] Safety screen completed; active risk handled first and allowed to override the sequence.
- [ ] All five rule-out gates worked in order with a documented disposition each.
- [ ] Optimize-current-treatment options (alliance, adherence, dose, fidelity) exhausted before switch/augment/step-up.
- [ ] Under-dosed / low-fidelity treatment not labeled as non-response.
- [ ] Diagnostic-fit and comorbidity gates not skipped.
- [ ] Corrective action selected from the least→most-disruptive sequence; one lever changed where safety permits.
- [ ] Instrument-correct anchors used (PHQ-9 / GAD-7 / PCL-5 / OCI-R, etc.); RCI claims tied to published values.
- [ ] Re-measurement plan attached: metric, next decision point, success threshold, fallback.
- [ ] Reformulation / step-up / referral routed to the appropriate companion prompt.
- [ ] No fabricated MCID/RCI/ETR; approximations labeled.
- [ ] Missing inputs flagged with `[clinician input required]`.
