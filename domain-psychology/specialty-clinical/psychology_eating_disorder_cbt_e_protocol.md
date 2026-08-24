---
title: "Eating Disorder CBT-E — Session Protocol (Regular Eating & Weight Monitoring)"
category: psychology/specialty-clinical
description: "Generate a stage-anchored CBT-E session plan with regular eating, collaborative in-session weighing, and dietary-rule work for transdiagnostic eating disorders."
techniques:
  - ST-04
  - RT-02
  - DT-02
  - NE-02
  - QA-04
  - CM-02
difficulty: advanced
tags:
  - eating-disorders
  - cbt-e
  - transdiagnostic
  - regular-eating
  - body-image
  - protocol-fidelity
intended_use: model-testing
updated: "2026-06-08"
related_prompts:
  - domain-psychology/specialty-clinical/psychology_eating_disorder_fbt_phase_planner.md
  - domain-psychology/treatment-planning/psychology_relapse_prevention_plan_designer.md
  - domain-psychology/diagnostic-formulation/psychology_dsm5_differential_generator.md
---

# Eating Disorder CBT-E — Session Protocol (Regular Eating & Weight Monitoring)

## Objective
Generate a single 50-minute session plan placed within enhanced cognitive behavior therapy for eating disorders (CBT-E; Fairburn, *Cognitive Behavior Therapy and Eating Disorders*, 2008), the leading transdiagnostic treatment derived from CBT-BN. The plan locates the session inside the four-stage architecture — Stage 1 (sessions 1–8, twice weekly: engagement, the personalized transdiagnostic formulation, real-time self-monitoring, regular eating, collaborative weekly in-session weighing), Stage 2 (a brief review/joint stocktaking), Stage 3 (the core maintaining mechanisms: over-evaluation of shape/weight, dietary restraint and rules, body-checking/avoidance/feeling fat, and event/mood-triggered changes in eating), and Stage 4 (ending and relapse prevention) — across 20 sessions for non-low-weight patients or 40 sessions with a weight-regain pathway for low-weight patients. It distinguishes **CBT-E focused** (the default, targeting the core eating-disorder psychopathology) from **CBT-E broad** (adding modules for clinical perfectionism, core low self-esteem, or marked interpersonal difficulties when these maintain the disorder). The clinical frame is collaborative, formulation-driven, and explicitly non-prescriptive about reducing food intake; weight is monitored together, never reported back to the patient outside the weighing procedure.

## When to Use
- Adult or older-adolescent patient with anorexia nervosa, bulimia nervosa, binge-eating disorder, or OSFED who is medically stable enough for outpatient care.
- Planning a Stage 1 session establishing the formulation, self-monitoring, and regular eating.
- Building a Stage 3 session targeting dietary rules, body-checking, or mood-triggered eating.
- Designing the low-weight weight-regain pathway with collaborative weighing.
- Not appropriate when the patient meets criteria for a higher level of care (medical instability, BMI below the locally agreed outpatient threshold, electrolyte derangement, syncope, bradycardia, rapid weight loss, or failed outpatient trial) — in that case the output is a step-up coordination note, not a session plan.

## Inputs / Context
- Diagnosis, illness duration, current BMI / % expected body weight, and weight trajectory.
- Current CBT-E stage and session number; focused vs broad track.
- Self-monitoring records and the in-session weight from collaborative weighing (graphed across 4 weeks).
- Behaviors present: restriction, binge episodes, self-induced vomiting, laxative/diuretic misuse, driven exercise.
- Body-checking and body-avoidance behaviors; "feeling fat" triggers.
- `[clinician input required: current medical-monitoring status — labs (electrolytes/phosphate), vitals, and whether the patient remains within the agreed outpatient safety parameters]`
- `[clinician input required: the patient's individualized maintaining-mechanism formulation diagram already developed in Stage 1]`
- `[clinician input required: which CBT-E module(s), if any, the broad form will add and the clinical justification]`

## Constraints

### Must
- Open every session with collaborative in-session weighing: weigh together, plot the point on the 4-week graph, and interpret the trend (not a single reading) before any other agenda item.
- Anchor the session to the correct stage and its sanctioned procedures (e.g., regular eating belongs to Stage 1; addressing over-evaluation of shape/weight belongs to Stage 3).
- Implement **regular eating** as three meals plus two-to-three planned snacks at regular intervals, with the explicit rule of not eating between planned occasions — sequence behavior change before cognitive change.
- Match dietary-rule work to the patient's specific rules and address them as testable predictions, not as moral failures.
- For the low-weight pathway, frame Stage 1 around weight regain (target ~0.5 kg/week outpatient), tie energy intake to that goal, and verify medical monitoring is current.
- Address purging as a maintaining behavior (the binge–purge cycle and the false belief that purging undoes intake) and replace it with response prevention plus regular eating.
- State the CPT code and a risk-reassessment hook keyed to medical instability.

### Must Not
- Must not provide any guidance, meal plan, or rule that reduces overall eating, prescribes weight loss, or endorses a "goal weight" framed as thinness.
- Must not report the patient's weight number outside the collaborative weighing procedure or react to it in a way that reinforces over-evaluation.
- Must not fabricate self-monitoring entries, binge/purge frequencies, lab values, or weights — these come from the records and the in-session weighing.
- Must not target body-image or self-esteem modules before regular eating and weight stability are established.
- Must not continue outpatient CBT-E when the inputs indicate medical instability instead of stepping up care.

## Instructions
1. Confirm stage, session number, track (focused/broad), and current medical-monitoring status; if unstable, switch output to a step-up coordination note and stop.
2. Write the collaborative weighing block: the procedure, the 4-week trend interpretation, and the planned debrief of the patient's reaction.
3. Review homework: self-monitoring records, regular-eating adherence, and any behavioral experiments since last session.
4. Set the session target from the stage (Stage 1: formulation + regular eating; Stage 3: a specific maintaining mechanism).
5. Build the in-session intervention: for Stage 1, install or troubleshoot regular eating; for Stage 3, run the module-specific procedure (addressing dietary rules as predictions, body-checking reduction, "feeling fat" decoupling, or proactive problem-solving for event/mood-triggered eating).
6. For low-weight patients, specify the weight-regain rationale and the energy adjustment tied to the ~0.5 kg/week target.
7. Specify the next homework with concrete monitoring and one behavioral experiment.
8. Complete the outcome/risk block, billing, and supervisor co-sign line for low-weight or high-acuity cases.

## Output Format
```
=== CBT-E SESSION PLAN ===
Patient: [initials]    Session #: [n] of [20/40]    Date: [date]
Diagnosis: [dx]    Stage: [1/2/3/4]    Track: [focused/broad]
Current BMI / %EBW: [value]    Medical monitoring current: [Y/N — params]

--- COLLABORATIVE WEIGHING ---
In-session weight (this visit): [recorded together]
4-week trend: [interpretation of the graph, not the single point]
Patient reaction & debrief: [plan]

--- HOMEWORK REVIEW ---
Self-monitoring adherence: [summary from records]
Regular eating (3 meals + [n] snacks; no eating between): [adherence]
Behaviors since last session: [restriction / binges / purge / exercise — from records]

--- SESSION TARGET (stage-anchored) ---
[e.g., Stage 1: install regular eating | Stage 3: dietary-rule experiment]

--- INTERVENTION ---
Procedure: [step-by-step]
Dietary rules addressed (as predictions): [rule -> test]
Body-checking / avoidance work (if Stage 3): [plan]
Low-weight pathway (if applicable): regain target ~0.5 kg/wk; energy adjustment [detail]

--- HOMEWORK ---
Monitoring: [what to record]
Behavioral experiment: [single, specific]

--- OUTCOME / RISK ---
Risk reassessment: [medical instability indicators — step up if present]
Disposition: [continue outpatient / step up / coordinate]

--- BILLING ---
CPT: [90837 (60 min) | 90834 (45 min)]
Add-on / coordination: [if medical-team contact]
Clinician: ______________  Supervisor co-sign (low-weight/high-acuity): ______________
```

## Verification
- [ ] Session is anchored to the correct CBT-E stage and uses only that stage's sanctioned procedures.
- [ ] Collaborative weighing is the first agenda item and interprets the 4-week trend, not a single reading.
- [ ] Regular eating is structured as meals + planned snacks with the no-eating-between rule.
- [ ] No guidance reduces overall intake or prescribes weight loss.
- [ ] Low-weight pathway ties intake to the ~0.5 kg/week regain target and confirms current medical monitoring.
- [ ] Purging is handled via response prevention, not reinforced.
- [ ] Risk-reassessment hook and step-up criteria are explicit; CPT and co-sign line present.
- [ ] No fabricated self-monitoring entries, behavior frequencies, labs, or weights — all come from the records and in-session weighing.
