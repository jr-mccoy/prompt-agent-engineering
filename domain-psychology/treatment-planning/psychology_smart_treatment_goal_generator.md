---
title: "SMART Treatment Goal Generator"
category: psychology/treatment-planning
description: "Convert a clinical problem statement into SMART goals with objective-level measurement criteria suitable for treatment-plan documentation."
techniques:
  - DS-02
  - DT-01
  - ST-04
  - CM-01
  - QA-04
difficulty: intermediate
intended_use: model-testing
tags:
  - treatment-planning
  - SMART-goals
  - measurement
  - golden-thread
  - documentation
  - care-planning
updated: "2026-06-08"
related_prompts:
  - domain-psychology/treatment-planning/psychology_golden_thread_writer.md
  - domain-psychology/treatment-planning/psychology_measurement_based_care_plan.md
  - domain-psychology/documentation/psychology_initial_treatment_plan.md
  - domain-psychology/treatment-planning/psychology_relapse_prevention_plan_designer.md
---

# SMART Treatment Goal Generator

## Objective

Convert a clinician-supplied problem statement into a set of properly structured treatment goals and measurable objectives that satisfy SMART criteria (Specific, Measurable, Achievable, Relevant, Time-bound) and withstand utilization-review scrutiny. Each objective must name its measurement method and a numeric or behavioral threshold so that progress note writers can quote the objective verbatim and mark it "met" or "not met" without ambiguity.

## When to Use

- During initial treatment-plan drafting (typically session 1–3) to operationalize a problem list.
- When an existing goal is flagged by a supervisor, utilization reviewer, or accreditation auditor as immeasurable or too vague.
- When transitioning a client between levels of care (e.g., IOP → outpatient) and the new plan requires problem-specific reformulation.
- When a client's presenting problem changes mid-treatment and the plan must be updated with a new or modified goal.

## Inputs / Context Required

- **Problem statement** (functional language, ≥ 1 sentence): the clinician's summary of what impairs the client's functioning.
- **Diagnosis** (DSM-5-TR / ICD-10-CM code + descriptor): used to anchor expected severity ranges for validated instruments.
- **Baseline outcome-measure score(s)**: e.g., PHQ-9 = 18 (severe), GAD-7 = 15 (severe), PCL-5 = 52, or "not yet administered."
- **Client's own words for what they want to change**: at least one direct quote when available.
- **Timeframe**: anticipated episode length (e.g., 12 weeks outpatient, 30-day IOP).
- **Level of care**: outpatient individual / group / IOP / PHP / residential — affects feasibility standards.
- **Clinician's modality**: helps set intervention-side realistic targets.
- `[clinician input required: any medical, occupational, or social constraints on goal scope]`

## Constraints

### Must

- Apply all five SMART dimensions to every objective written.
- Name a specific validated measurement instrument or observable behavioral indicator for each objective.
- Specify a numeric threshold or behavioral frequency that defines "met" (e.g., PHQ-9 ≤ 9, attend work ≥ 4 days/week for 3 consecutive weeks, self-injurious behavior 0 occurrences in 30 days).
- Set target dates proportional to the stated episode timeframe; short-term objectives (4–8 weeks) and long-term goals (full episode) must both appear.
- Distinguish a **long-term goal** (experiential, client-meaningful, narrative) from **measurable objectives** (operationalized sub-steps).
- Include the client's voice — at least one goal per problem must incorporate the client's own language.
- Flag any objective that cannot be operationalized with the available information using `[clinician input required: specify measurement method for ...]`.

### Must Not

- Do not write goals that merely restate the diagnosis ("Resolve major depressive disorder," "Reduce PTSD").
- Do not write immeasurable objectives ("Client will feel better," "Client will manage anxiety," "Client will be more functional").
- Do not set target thresholds that are not clinically validated or that exceed realistic episode-length norms (e.g., PHQ-9 = 0 by week 4 from a severe baseline is not achievable).
- Do not fabricate baseline scores or client quotes; use `[clinician input required]` placeholders.
- Do not produce more than 3 measurable objectives per goal; focus prevents dilution.

## Instructions

1. **Read and re-state the problem** in functional terms: what does this problem prevent the client from doing? Name the specific domain (occupational, interpersonal, self-care, safety, academic).

2. **Anchor to baselines**: Record the baseline outcome-measure score(s) and map them to severity bands (e.g., PHQ-9 15–19 = moderately severe depression). If baselines are missing, insert `[clinician input required: administer PHQ-9 / GAD-7 / PCL-5 at next session and update before plan is signed]`.

3. **Draft the long-term goal**: Write a narrative sentence in accessible language, client-meaningful, tied to functional restoration (not symptom elimination). Incorporate the client's own words where provided.

4. **Draft short-term objectives (1–3 per goal)**:
   - Each objective follows this template: *"By [target date], client will [specific behavior or score change] as measured by [instrument / behavioral count / structured observation], [threshold / frequency], for [duration of consistency]."*
   - First objective: typically a symptom-reduction target using a validated scale.
   - Second objective: a behavioral or functional target (attendance, task completion, relational).
   - Third objective (if needed): a skill-acquisition or self-monitoring target.

5. **Select measurement methods**: Use validated instruments where diagnosis-specific norms exist. Prefer instruments already administered at intake. If no validated scale applies, specify a behavioral count with operational definition.

   | Domain | First-line Instrument | Score Range Reference |
   |--------|----------------------|----------------------|
   | Depression | PHQ-9 | 0–4 minimal, 5–9 mild, 10–14 moderate, 15–19 mod-severe, 20–27 severe |
   | Anxiety (generalized) | GAD-7 | 0–4 minimal, 5–9 mild, 10–14 moderate, 15–21 severe |
   | PTSD | PCL-5 | Probable PTSD ≥ 31–33; clinical threshold ≥ 38 in many settings |
   | Alcohol use | AUDIT | Hazardous ≥ 8; harmful ≥ 16; probable dependence ≥ 20 |
   | Substance use | DAST-10 | Low ≥ 1, Moderate ≥ 3, Substantial ≥ 6, Severe ≥ 9 |
   | Panic / agoraphobia | PDSS-SR | Severity ≥ 8 clinical range |
   | OCD | Y-BOCS / OCI-R | Y-BOCS: Moderate 16–23, Severe 24–31 |
   | Functional impairment | WHODAS 2.0 / SDS | SDS 0–30; score ≥ 5/10 per domain = functional impairment |
   | Global functioning | CGAS (child) / GAF-equivalent | Clinician-rated, document anchor |
   | Behavioral count | Clinician-defined | e.g., "panic attacks/week," "days worked," "self-harm episodes/month" |

6. **Set target thresholds**: Use established minimally clinically important differences (MCIDs) and response benchmarks:
   - PHQ-9: ≥ 5-point reduction = response; score ≤ 9 = remission threshold used in most trials.
   - GAD-7: ≥ 4-point reduction = response; score ≤ 7 = remission threshold.
   - PCL-5: ≥ 10-point reduction = clinically significant change; ≤ 33 = below probable threshold.
   - For behavioral targets: define minimum frequency, minimum streak length, and observation window (e.g., "3 consecutive weeks").

7. **Set target dates**: Divide the episode timeframe into short-term (first third) and long-term (end of episode). Example for 12-week outpatient: short-term objectives target weeks 4–6; long-term goal targets week 12.

8. **Apply the immeasurability self-test**: For every objective, ask: "Could two different clinicians, given the same client data at week 12, independently and reliably agree whether this objective was met?" If not, revise until yes.

9. **Run verification** (see below).

## Output Format

```
=== SMART GOAL SET ===

PROBLEM STATEMENT
[Functional language. Example: "Depressive symptoms (PHQ-9 = 18) interfering with work attendance,
parenting responsibilities, and sleep — present for 6 months following job loss."]

BASELINE MEASURES
- PHQ-9: [score] ([severity band]) — administered [date]
- [Other instrument]: [score] — administered [date]
- [clinician input required: administer _____ before plan is signed if not yet done]

────────────────────────────────────────────────────────────
LONG-TERM GOAL
Goal: [Narrative, client-meaningful sentence incorporating client's voice.]
Client's own words: "[Direct quote or paraphrase from intake.]"
Episode target date: [YYYY-MM-DD]

────────────────────────────────────────────────────────────
SHORT-TERM OBJECTIVES

Objective 1 (Symptom reduction):
  "By [date], client will reduce depressive symptoms from PHQ-9 = [baseline] to ≤ [threshold]
   as measured by PHQ-9 administered at each session, sustained over 3 consecutive sessions."
  Measurement: PHQ-9 (clinician-administered at each session)
  Threshold: Score ≤ [X]
  Consistency requirement: 3 consecutive sessions at or below threshold
  Start date: [YYYY-MM-DD]     Target date: [YYYY-MM-DD]
  Status: Not started

Objective 2 (Functional / behavioral):
  "By [date], client will [specific behavior — e.g., attend work ≥ 4 days per week]
   as verified by [method — e.g., self-report work log reviewed in session],
   for 3 consecutive weeks."
  Measurement: [Behavioral count / observation method]
  Threshold: [Frequency or count]
  Consistency requirement: [e.g., 3 consecutive weeks]
  Start date: [YYYY-MM-DD]     Target date: [YYYY-MM-DD]
  Status: Not started

Objective 3 (Skill acquisition / self-monitoring) [if applicable]:
  "By [date], client will [specific skill use — e.g., complete a mood log ≥ 5 of 7 days per week]
   as documented by [method], for 4 consecutive weeks."
  Measurement: [Method]
  Threshold: [Frequency]
  Consistency requirement: [Duration]
  Start date: [YYYY-MM-DD]     Target date: [YYYY-MM-DD]
  Status: Not started

────────────────────────────────────────────────────────────
IMMEASURABILITY FLAGS
- [List any objectives that could not be fully operationalized; state what clinician input is needed.]

NEXT STEP
- [ ] Clinician confirms objectives with client and obtains signature.
- [ ] Objectives entered into treatment-plan template with discharge criteria.
- [ ] Link to golden-thread writer for full problem → goal → objective → intervention → measurement chain.
```

## Verification

- [ ] Each objective contains a specific behavior or score change (Specific).
- [ ] Each objective names a validated instrument or observable behavioral count (Measurable).
- [ ] Thresholds are within MCID benchmarks for the named instrument; behavioral targets are plausible given episode length and level of care (Achievable).
- [ ] Goals connect to the functional impairment stated in the problem (Relevant).
- [ ] Every objective has a target date proportional to the episode timeframe (Time-bound).
- [ ] At least one goal per problem includes the client's own language.
- [ ] No objective uses vague language ("feel better," "manage," "improve").
- [ ] No goal merely restates the diagnosis.
- [ ] Total objectives across the plan: ≤ 8 for outpatient; ≤ 12 for IOP/PHP.
- [ ] Missing baselines flagged with `[clinician input required]`.
- [ ] Immeasurability self-test applied: two clinicians could independently determine met/not-met.
