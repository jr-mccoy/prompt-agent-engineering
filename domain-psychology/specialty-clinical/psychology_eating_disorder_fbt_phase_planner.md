---
title: "Family-Based Treatment (FBT) — Phase Planner for Adolescent Eating Disorders"
category: psychology/specialty-clinical
description: "Generate a phase-anchored FBT plan that mobilizes parents to refeed, externalizes the illness, and sequences phase transitions to weight restoration and adolescent autonomy."
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
  - fbt
  - maudsley
  - adolescent
  - parental-refeeding
  - phase-planning
intended_use: model-testing
updated: "2026-06-08"
related_prompts:
  - domain-psychology/specialty-clinical/psychology_eating_disorder_cbt_e_protocol.md
  - domain-psychology/populations/child-adolescent/psychology_adolescent_intake_with_developmental_lens.md
  - domain-psychology/treatment-planning/psychology_relapse_prevention_plan_designer.md
---

# Family-Based Treatment (FBT) — Phase Planner for Adolescent Eating Disorders

## Objective
Generate a phase-anchored treatment plan for manualized Family-Based Treatment (FBT; Lock & Le Grange, *Treatment Manual for Anorexia Nervosa: A Family-Based Approach*), the Maudsley-derived, outpatient first-line treatment for adolescent anorexia nervosa (with an adapted protocol for bulimia nervosa). FBT proceeds through three phases over roughly 15–20 sessions across about 12 months. **Phase 1 (full parental control of refeeding)** establishes the therapist's *agnostic stance* on etiology, raises parental anxiety to mobilize action, *externalizes the illness* (separating the adolescent from the eating disorder), conducts the family meal in session, and puts parents fully in charge of restoring weight and interrupting compensatory behaviors. **Phase 2 (gradual return of control)** begins once weight is steadily restoring and the adolescent accepts parental demands; control over eating is handed back to the adolescent in developmentally appropriate increments. **Phase 3 (adolescent issues & identity)** addresses normal adolescent development, autonomy, and the parent–child relationship once weight is restored and eating is age-appropriate. The plan specifies weight-trajectory milestones, % expected body weight (%EBW) targets, and the criteria gating each phase transition. The clinical frame is non-blaming, parent-empowering, and explicitly externalizing.

## When to Use
- Adolescent (typically ~12–18) with anorexia nervosa or bulimia nervosa living with caregivers able to participate.
- Planning Phase 1 (parental refeeding and the in-session family meal) or sequencing the move into Phase 2/3.
- Re-planning when weight restoration stalls or a phase transition is being considered.
- Setting weight-trajectory milestones and %EBW gates collaboratively with the medical team.
- Not appropriate when the adolescent is medically unstable or below the agreed outpatient safety threshold (then output is a medical step-up/admission coordination note), or when there is no caregiver able to take charge of refeeding.

## Inputs / Context
- Age, diagnosis, illness duration, current weight, height, %EBW, and weight trajectory since intake.
- Current FBT phase and session number; family composition and who attends.
- Behaviors present: restriction, binge/purge, driven exercise; level of parental control achieved so far.
- Status of the in-session family meal (completed? outcome?).
- `[clinician input required: current medical-monitoring status and the medical team's agreed outpatient safety parameters / target weight range]`
- `[clinician input required: the family's current capacity and unity around refeeding — points of caregiver disagreement or undermining]`
- `[clinician input required: phase-transition readiness judgment — is weight restoring steadily and is the adolescent accepting parental demands?]`

## Constraints

### Must
- Hold the *agnostic stance*: do not attribute cause; redirect from blame toward action.
- *Externalize the illness* throughout — language separates the adolescent from the eating-disorder behaviors.
- In Phase 1, place parents fully in charge of refeeding and compensatory-behavior interruption; the therapist consults to the parents, not the adolescent's plate.
- Tie phase transitions to explicit criteria: Phase 1→2 requires steady weight restoration plus the adolescent accepting parental control; Phase 2→3 requires near-complete weight restoration with developmentally appropriate self-management.
- State weight milestones in %EBW and a steady-gain expectation (commonly ~0.5–1 kg/week early outpatient) coordinated with the medical team.
- Confirm current medical monitoring; escalate to admission criteria if instability is present.
- Include a supervisor co-sign line and a billing block.

### Must Not
- Must not blame, pathologize, or criticize parents for the illness, nor frame family dynamics as the cause.
- Must not hand control of eating back to the adolescent before Phase 1 weight criteria are met.
- Must not contradict the medical team's safety parameters or substitute psychotherapy for required medical monitoring.
- Must not fabricate weights, %EBW values, lab data, or the family-meal outcome — these come from records and the treatment team.
- Must not advise any reduction in the adolescent's prescribed energy intake during the weight-regain phase.

## Instructions
1. Confirm phase, session number, current %EBW, trajectory, and medical-monitoring status; if unstable, switch output to a step-up/admission coordination note and stop.
2. Set the phase-specific therapeutic stance and externalizing language to use this session.
3. For Phase 1: plan the family meal (if not done) or the parental-refeeding coaching, including unifying caregivers and interrupting compensatory behaviors.
4. For Phase 2: specify the increment of control to return and the conditions for it, monitoring that weight gain continues.
5. For Phase 3: plan the adolescent-development / autonomy and relationship work, with relapse-prevention scaffolding.
6. State the weight milestone for this period in %EBW and the steady-gain target coordinated with medical.
7. Specify the phase-transition criteria being evaluated and whether they are met.
8. Complete the outcome/risk block, billing, and supervisor co-sign line.

## Output Format
```
=== FBT PHASE PLAN ===
Adolescent: [initials]    Age: [yrs]    Session #: [n] of [~15-20]    Date: [date]
Diagnosis: [dx]    Phase: [1/2/3]    Attending: [family members]
Current weight / %EBW: [value]    Trajectory since intake: [up/flat/down]
Medical monitoring current: [Y/N — params; target weight range]

--- THERAPEUTIC STANCE ---
Agnostic stance / externalization language for this session: [examples]

--- PHASE-SPECIFIC PLAN ---
Phase 1 (parental refeeding):
  Family meal: [planned/completed — outcome]
  Parental coaching: [unify caregivers; interrupt compensatory behaviors]
Phase 2 (return of control):
  Increment returned: [specific, conditional on continued gain]
Phase 3 (adolescent issues):
  Developmental / autonomy / relationship focus: [plan]

--- WEIGHT MILESTONE ---
%EBW target this period: [value]    Steady-gain target: [~kg/week, coordinated w/ medical]

--- PHASE-TRANSITION REVIEW ---
Criteria evaluated: [Phase 1->2: steady restoration + adolescent accepts control |
                     Phase 2->3: near-full restoration + age-appropriate self-management]
Met? [Y/N — rationale]

--- OUTCOME / RISK ---
Risk reassessment: [medical instability indicators -> escalate if present]
Disposition: [continue outpatient / step up / coordinate with medical]

--- BILLING ---
CPT: [90847 family w/ patient | 90846 family w/o patient | 90837]
Clinician: ______________  Supervisor co-sign: ______________
```

## Verification
- [ ] Plan is anchored to the correct FBT phase and uses that phase's sanctioned procedures.
- [ ] Agnostic stance and illness externalization are present; no parental blame.
- [ ] Phase 1 places parents fully in charge of refeeding; control is not returned prematurely.
- [ ] Phase-transition criteria are explicit and tied to weight restoration plus autonomy.
- [ ] Weight milestone is stated in %EBW with a steady-gain target coordinated with the medical team.
- [ ] Medical-monitoring status confirmed; escalation criteria stated.
- [ ] Billing and supervisor co-sign line present.
- [ ] No fabricated weights, %EBW, labs, or family-meal outcomes — all come from records and the treatment team.
