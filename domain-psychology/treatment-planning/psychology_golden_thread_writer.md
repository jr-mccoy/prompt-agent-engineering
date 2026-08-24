---
title: "Golden Thread Writer"
category: psychology/treatment-planning
description: "Walk a single problem through the complete problem → goal → SMART objective → intervention → measurement chain to produce a self-consistent, audit-ready golden thread."
techniques:
  - DT-01
  - ST-04
  - DS-02
  - CM-01
  - QA-04
difficulty: intermediate
intended_use: model-testing
tags:
  - golden-thread
  - treatment-planning
  - SMART-goals
  - interventions
  - measurement
  - care-planning
  - documentation
updated: "2026-06-08"
related_prompts:
  - domain-psychology/treatment-planning/psychology_smart_treatment_goal_generator.md
  - domain-psychology/treatment-planning/psychology_measurement_based_care_plan.md
  - domain-psychology/documentation/psychology_initial_treatment_plan.md
  - domain-psychology/treatment-planning/psychology_relapse_prevention_plan_designer.md
---

# Golden Thread Writer

## Objective

Produce a fully linked, single-problem golden thread: a five-ring chain in which each element is derived explicitly from the prior one. The chain runs:

**Problem statement → Long-term goal → SMART objective(s) → Named intervention(s) → Measurement method + threshold**

Every link in the chain must be traceable in both directions. A reviewer reading any single element should be able to reconstruct the ring above it (why we are doing this) and the ring below it (how we will know it worked). Output must withstand a Joint Commission, CARF, Medicaid, or MCO utilization-review audit.

## When to Use

- When drafting one problem thread at a time and assembling threads into a full treatment plan.
- When a supervisor or utilization reviewer has flagged a broken link in an existing plan (e.g., goal does not match the problem, or the intervention has no tied objective).
- When onboarding a supervisee to treatment-plan documentation standards.
- When a mid-treatment reformulation is needed and only one problem is being revised.
- As a teaching or QA tool applied to a plan already written, to verify internal consistency.

## Inputs / Context Required

- **Problem statement**: functional description of the presenting impairment (1–4 sentences). Include domain (occupational, relational, safety, self-care, academic).
- **Diagnosis** (DSM-5-TR / ICD-10-CM): anchors severity language and appropriate instrument selection.
- **Baseline outcome measure score(s)**: instrument name + score + administration date.
- **Client's own words**: at least one verbatim or near-verbatim quote about what they want from treatment.
- **Episode length / level of care**: outpatient / IOP / PHP / residential; total planned sessions or weeks.
- **Modality(ies) available**: individual psychotherapy, group, skills group, med management, family, etc.
- **Clinician's theoretical orientation or protocol**: CBT, DBT, ACT, EMDR, psychodynamic, MI, or integrative.
- `[clinician input required: any constraints on frequency, session length, or co-occurring providers]`

## Constraints

### Must

- Follow the five-ring sequence in order; output each ring as a labeled block.
- Derive the goal explicitly from the problem (annotate the link: "This goal addresses [specific aspect of problem]").
- Write objectives using the template: *"By [date], client will [behavior/score] as measured by [instrument/method], [threshold], for [consistency window]."*
- Name the evidence-based intervention technique precisely — not modality alone (e.g., "CBT — behavioral activation with activity scheduling" not "CBT").
- Attach each intervention to the specific objective(s) it advances; use the Intervention-to-Objective link annotation.
- Name the measurement instrument and specify both the response threshold (e.g., PHQ-9 ≤ 9) and the consistency criterion (e.g., 3 consecutive sessions).
- Include one progress-note bridge sentence per objective: a single sentence a clinician can paste into a session note to report on that objective.
- Flag any broken link with `[clinician input required: ...]` rather than inventing content.

### Must Not

- Do not allow a goal that does not trace directly to the functional impairment in the problem statement.
- Do not allow an intervention that cannot be traced to at least one objective.
- Do not allow an objective that has no named measurement method or no numeric/behavioral threshold.
- Do not use modality names without specifying the named technique within the modality.
- Do not write problem statements as diagnostic labels alone ("Problem: depression").
- Do not fabricate baseline scores, client quotes, or clinician names.

## Instructions

1. **Ring 1 — Functional Problem Statement**: Restate the problem in functional language. Specify: (a) the symptom cluster or behavior, (b) the functional domains it impairs (work, relationships, self-care, safety, school), (c) the severity anchor (baseline instrument score or behavioral frequency), (d) the duration/onset.

2. **Ring 2 — Long-Term Goal**: Draft one narrative goal sentence that is (a) client-meaningful and experiential rather than diagnostic, (b) directly tied to the functional impairment named in Ring 1, (c) realistic for the episode length and level of care, (d) inclusive of the client's own words. Annotate: "This goal addresses [aspect of Ring 1 problem]."

3. **Ring 3 — SMART Objectives (1–3 per goal)**: Draft objectives following the template. For each, verify all five SMART dimensions:
   - **S** — names a specific behavior or score, not a category.
   - **M** — names the instrument or observable behavioral count.
   - **A** — threshold is within MCID norms for the instrument or clinically feasible given episode length.
   - **R** — objective advances the Ring 2 goal; annotate the connection.
   - **T** — has a start date and target date derived from the episode timeframe.

   Apply the immeasurability self-test: two independent clinicians given the same data at the target date could both reliably determine "met" or "not met."

4. **Ring 4 — Named Interventions**: For each objective, attach 1–3 interventions. Each intervention specifies:
   - Modality (individual, group, family, med management, peer support, case management)
   - Named technique (evidence-based protocol or manualized name)
   - Frequency and session length
   - Responsible clinician (name + credentials placeholder if draft)
   - Estimated start date
   - Objective ID it advances

   Derivation annotation: "This intervention advances Objective [#] by [mechanism]."

5. **Ring 5 — Measurement Method + Threshold**: For each objective, write the full measurement specification:
   - Instrument name + version (e.g., PHQ-9, PCL-5, GAD-7, AUDIT, Y-BOCS, OCI-R, WHODAS 2.0, SDS, PDSS-SR, behavioral frequency count).
   - Administration schedule (every session / every 2 sessions / monthly).
   - Response threshold (numeric score or behavioral frequency defining improvement).
   - Remission / "met" threshold (score or behavioral criterion that marks the objective complete).
   - Consistency criterion (how many consecutive data points must meet threshold before marking "met").

6. **Progress-Note Bridge**: For each objective, write one sentence formatted for copy-paste into a SOAP or BIRP progress note. Example: "Objective 1.A.i: Client reported PHQ-9 = [score] today (baseline [score]); [met/not met] 3-consecutive-session threshold."

7. **Broken-Link Audit**: After drafting all five rings, read the chain backward from Ring 5 to Ring 1. For each link, confirm the derivation annotation is present and accurate. Flag any gap.

8. **Run verification.**

## Output Format

```
=== GOLDEN THREAD ===

RING 1 — FUNCTIONAL PROBLEM STATEMENT
Problem: [Functional language. Include: symptom/behavior cluster | impaired domains | severity anchor (instrument score or behavioral frequency) | duration/onset.]

───────────────────────────────────────────
RING 2 — LONG-TERM GOAL
Goal: [Narrative, client-meaningful sentence.]
  Client's own words: "[Quote or paraphrase.]"
  Episode target date: [YYYY-MM-DD]
  Derivation: "This goal addresses [specific aspect of Ring 1 problem]."

───────────────────────────────────────────
RING 3 — SMART OBJECTIVES

Objective 1 (Symptom reduction):
  Statement: "By [YYYY-MM-DD], client will [specific behavior / score change] as measured by
  [instrument], achieving [threshold], for [consistency window, e.g., 3 consecutive sessions]."
  S: [Specify what is being measured]
  M: [Instrument / behavioral count]
  A: [Rationale for achievability — MCID reference or clinical norm]
  R: "Advances Goal by [mechanism]."
  T: Start [YYYY-MM-DD] | Target [YYYY-MM-DD]
  Status: Not started

Objective 2 (Functional / behavioral):
  Statement: "By [YYYY-MM-DD], client will [behavior] as verified by [method], [frequency threshold],
  for [consistency window]."
  S / M / A / R / T: [same structure]
  Status: Not started

Objective 3 (Skill acquisition / self-monitoring) [if applicable]:
  [same structure]

───────────────────────────────────────────
RING 4 — NAMED INTERVENTIONS

| ID | Tied to Obj | Modality | Named Technique | Frequency | Duration | Responsible | Start |
|----|-------------|----------|-----------------|-----------|----------|-------------|-------|
| I1 | Obj 1 | [Modality] | [Evidence-based technique name] | [freq] | [min] | [Clinician] | [Date] |
| I2 | Obj 1, 2 | [Modality] | [Named technique] | [freq] | [min] | [Clinician] | [Date] |
| I3 | Obj 2 | [Modality] | [Named technique] | [freq] | [min] | [Clinician] | [Date] |

  Derivation annotations:
  - I1 advances Obj 1 by [mechanism].
  - I2 advances Obj 1 and 2 by [mechanism].
  - I3 advances Obj 2 by [mechanism].

───────────────────────────────────────────
RING 5 — MEASUREMENT METHOD + THRESHOLD

Measurement for Objective 1:
  Instrument: [PHQ-9 / GAD-7 / PCL-5 / behavioral count / other]
  Administration schedule: [Every session / every 2 sessions / monthly]
  Response threshold: [≥ X-point reduction from baseline]
  Remission / "Met" threshold: [Score ≤ X]
  Consistency criterion: [3 consecutive sessions at or below threshold]

Measurement for Objective 2:
  Method: [Behavioral count / self-report log / structured observation]
  Tracking: [How and by whom]
  "Met" threshold: [Frequency × duration]
  Consistency criterion: [N consecutive weeks]

Measurement for Objective 3 [if applicable]:
  [same structure]

───────────────────────────────────────────
PROGRESS-NOTE BRIDGE SENTENCES

Obj 1: "Objective [#]: Client reported [instrument] = [score] today (baseline [score]);
  [met / not yet met] [N]-consecutive-session threshold."
Obj 2: "Objective [#]: Client reported [behavior] on [N] of 7 days this week per self-report log;
  [on track / not on track] toward [threshold] × [N-week consistency window]."
Obj 3: "[...]"

───────────────────────────────────────────
BROKEN-LINK AUDIT
- Ring 1 → Ring 2: [Confirmed / FLAG: ...]
- Ring 2 → Ring 3: [Confirmed / FLAG: ...]
- Ring 3 → Ring 4: [Confirmed / FLAG: ...]
- Ring 4 → Ring 5: [Confirmed / FLAG: ...]
- Ring 5 → Ring 3 (backward): [Confirmed / FLAG: ...]

GAPS / CLINICIAN INPUT REQUIRED
- [clinician input required: ...]
```

## Verification

- [ ] All five rings present and labeled.
- [ ] Ring 1 is functional (names impaired domain, severity anchor, duration) — not a diagnostic label alone.
- [ ] Ring 2 goal traces directly to the functional impairment in Ring 1; derivation annotation present.
- [ ] Every objective in Ring 3 passes all five SMART dimensions; immeasurability self-test applied.
- [ ] Every objective has a start date and target date proportional to the episode timeframe.
- [ ] Every intervention in Ring 4 names the specific evidence-based technique, not just the modality.
- [ ] Every intervention is tied to at least one objective by ID; derivation annotation present.
- [ ] Every objective in Ring 5 has a named instrument or operational behavioral count, an administration schedule, a response threshold, a remission/"met" threshold, and a consistency criterion.
- [ ] Progress-note bridge sentence written for each objective.
- [ ] Broken-link audit run in both directions; all gaps flagged.
- [ ] No vague objective language ("feel better," "manage," "cope with").
- [ ] Nothing fabricated; all missing inputs flagged with `[clinician input required]`.
