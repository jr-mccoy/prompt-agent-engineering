---
title: "Treatment Resistance Reformulation"
category: psychology/treatment-planning
description: "When the current plan is not producing meaningful change, systematically reformulate — without abandoning the client — by diagnosing the failure before changing the treatment."
techniques:
  - RT-02
  - RT-03
  - QA-04
  - DT-01
  - CM-01
difficulty: advanced
intended_use: model-testing
tags:
  - treatment-resistance
  - reformulation
  - non-response
  - treatment-planning
  - clinical-reasoning
  - measurement-based-care
updated: "2026-06-08"
related_prompts:
  - domain-psychology/treatment-planning/psychology_measurement_based_care_plan.md
  - domain-psychology/treatment-planning/psychology_modality_selection_decision_aid.md
  - domain-psychology/treatment-planning/psychology_stepped_care_decision_aid.md
  - domain-psychology/diagnostic-formulation/psychology_case_conceptualization_framework.md
---

# Treatment Resistance Reformulation

## Objective

When a client has not made meaningful progress after a reasonable treatment trial, systematically diagnose why before changing what. Prevent premature modality-switching or level-of-care escalation driven by clinician frustration rather than clinical reasoning. The output is a structured reformulation document that: (1) defines and documents the non-response, (2) works through a differential of contributing causes, (3) identifies the most probable explanation(s), and (4) generates a revised plan with testable hypotheses about what should change and why.

## When to Use

- When the primary outcome measure (e.g., PHQ-9, GAD-7, PCL-5) has not improved by the MCID after 8 or more sessions of active treatment.
- When the client or clinician is expressing hopelessness, frustration, or resignation about the current plan.
- When a supervisor or peer consultant has raised concern about lack of progress.
- When the treatment team is considering escalating level of care but the clinical picture is ambiguous.
- When the client is about to terminate prematurely and the clinician wants to present a revised rationale for continuing.
- Before referring out for a second opinion or specialty consultation.

## Inputs / Context Required

- **Treatment history to date**: modalities tried, duration of each, response or lack thereof. Include prior episodes, not just the current one.
- **Outcome trajectory data**: instrument name + scores at baseline and each administration (e.g., PHQ-9 over 12 sessions). If not formally tracked, describe clinical impression with dates.
- **Current formulation**: the case conceptualization that is guiding the current treatment (theory of change, maintaining factors, targeted mechanisms).
- **Diagnoses** (active, including any updates or additions since intake).
- **Medication status**: current psychotropic medications, dose, prescriber, duration, adherence, side effects. If none, note.
- **Session content to date**: what interventions have been tried? What has the client engaged with? What has been avoided?
- **Client engagement**: attendance record, homework completion, stated motivation level, in-session engagement quality.
- **Collateral factors**: major life events, new or ongoing stressors, relational changes, medical changes since treatment started.
- **Supervisor / peer consultation history**: has this case been presented for consultation? What was said?
- `[clinician input required: client's own explanation for why they feel they are not improving]`
- `[clinician input required: clinician's countertransference — feelings of frustration, boredom, helplessness — that may be informing the "stuck" perception]`

## Constraints

### Must

- Define non-response operationally using the outcome trajectory data before generating hypotheses. Non-response is not the same as slow response, partial response, or plateau after initial gains.
- Work through at least six categories of contributing cause before arriving at a conclusion: (1) diagnostic re-evaluation, (2) formulation accuracy, (3) treatment fidelity and technique delivery, (4) engagement / alliance, (5) external / maintaining factors, (6) medication / medical factors.
- Generate a differential of causes, not a single explanation. Rank by probability given the available evidence.
- Produce a revised plan with specific testable hypotheses: each change in the plan should be tied to a causal hypothesis that, if correct, predicts a specific improvement.
- Include explicit criteria for what would count as a response to the revised plan — do not leave the timeframe for re-evaluation open-ended.
- Flag when a diagnostic revision is warranted before changing the treatment.
- Flag when referral to a specialist (psychiatry, neuropsychology, eating disorders, substance use) is the appropriate next step rather than internal reformulation.
- Include the clinician's own contribution as a required dimension, not an optional one — this is not blame assignment but systemic diagnosis.

### Must Not

- Do not jump to a new modality without first establishing why the current one failed to work.
- Do not label the client as "treatment-resistant" without first ruling out therapist- and system-level contributions.
- Do not diagnose non-response on clinical impression alone when outcome data is available; use the data.
- Do not omit medication as a contributing factor when psychotropics are prescribed.
- Do not produce a reformulation that abandons goals the client still holds; revise the mechanism and method, not the destination.
- Do not fabricate prior therapy notes, medication records, or assessment scores; flag missing inputs with `[clinician input required]`.

## Instructions

1. **Define the non-response**: State the operational definition of non-response for this case. Anchor to outcome data where available. Distinguish between: (a) no improvement, (b) partial improvement with plateau, (c) initial improvement followed by deterioration, (d) improvement in scores but no functional change, (e) client's subjective experience of not improving despite score change. Document which pattern applies.

2. **Diagnostic re-evaluation** (Category 1): Is the current primary diagnosis still the best fit? Consider:
   - Have new features emerged since intake that suggest a revision (e.g., hypomanic episodes suggesting bipolar NOS; dissociative symptoms suggesting complex trauma; obsessional features missed at intake)?
   - Is there an unaddressed or underweighted comorbidity that is driving the non-response (e.g., ADHD impairing homework completion, untreated SUD fueling depression)?
   - Does the presentation fit a condition with a different evidence-based treatment than the one in use (e.g., what was treated as GAD is better explained by social anxiety disorder or OCD)?

3. **Formulation accuracy** (Category 2): Does the current theory of change still account for what is maintaining the presenting problem? Consider:
   - What was the original maintaining mechanism (e.g., avoidance → anxiety → depression)?
   - Has the mechanism been correctly targeted? Is there evidence in session that the maintenance model is being addressed?
   - Is there a deeper maintaining factor that the surface formulation missed (e.g., core schema, early attachment disruption, secondary gain, medical maintaining factor)?

4. **Treatment fidelity and technique delivery** (Category 3): Has the intervention been delivered with adequate fidelity? Consider:
   - Was the protocol delivered with structural integrity (correct sequence, correct dose, correct components)?
   - Has the intervention been watered down by therapeutic drift, excessive supportiveness, or avoidance of challenging components (e.g., skipping exposure, not pushing for specificity in cognitive restructuring)?
   - Is the clinician competent in this modality? Has supervision flagged technique concerns?

5. **Engagement and alliance** (Category 4): Consider:
   - What is the quantified engagement picture (attendance %, homework completion %, SRS or alliance scores)?
   - Is there a rupture — recognized or unrecognized — in the therapeutic alliance?
   - Has the client expressed ambivalence about change, goals, or the clinician that has not been fully addressed?
   - Is the client engaging in session but not generalizing outside it? (session-bound gains)

6. **External and maintaining factors** (Category 5): Consider:
   - What ongoing life stressors, trauma exposures, or environmental conditions are maintaining the presenting problem independent of the treatment?
   - Is the client in an active abusive or chronically unsafe environment that the treatment plan has not adequately addressed?
   - Have new events (loss, relationship change, job change) reset the baseline since treatment began?
   - Is the support system undermining rather than supporting gains?

7. **Medication and medical factors** (Category 6): Consider:
   - Is a psychotropic medication needed that has not been tried?
   - Is a current medication contributing to symptoms (akathisia → agitation/anxiety; SSRI-emergent emotional blunting; benzodiazepine use maintaining avoidance)?
   - Is there an unaddressed medical condition with psychiatric overlap (hypothyroidism, sleep apnea, chronic pain, neurological, endocrine)?
   - Is the prescriber aligned with the psychotherapy plan?

8. **Rank the differential**: Assign each category a likelihood rating (High / Moderate / Low / Unlikely based on available evidence). Identify the top 1–2 most probable explanations.

9. **Generate revised plan with testable hypotheses**: For each high-probability contributing cause, write: (a) the hypothesis, (b) the specific change to the plan that tests it, (c) what improvement within what timeframe would confirm the hypothesis, (d) what would disconfirm it.

10. **Identify referral / consultation indications**: State whether a specialist referral or additional consultation is recommended, and to whom.

11. **Run verification.**

## Output Format

```
=== TREATMENT RESISTANCE REFORMULATION ===

NON-RESPONSE DEFINITION
Pattern: [No improvement / Partial plateau / Initial gains + deterioration / Score-function discordance / Client-report discordance]
Evidence: [Instrument trajectory — e.g., "PHQ-9: Baseline 21 → Session 4: 19 → Session 8: 18 → Session 12: 19"]
Non-response criterion met at: Session [N] (date: [YYYY-MM-DD])
[clinician input required: outcome data if not formally tracked]

────────────────────────────────────────────────────────
CONTRIBUTING CAUSE DIFFERENTIAL

CATEGORY 1 — DIAGNOSTIC RE-EVALUATION
Hypothesis: [Is the diagnosis still accurate?]
Evidence for revision / confirmation: [...]
Likelihood: [High / Moderate / Low / Unlikely]
Action if high likelihood: [Specify]

CATEGORY 2 — FORMULATION ACCURACY
Original maintaining mechanism: [...]
Evidence mechanism was correctly targeted: [...]
Possible missed or deeper maintaining factor: [...]
Likelihood of formulation gap: [High / Moderate / Low / Unlikely]

CATEGORY 3 — TREATMENT FIDELITY
Protocol used: [Name]
Fidelity indicators: [Attendance, component delivery, supervision feedback]
Evidence of therapeutic drift or technique avoidance: [...]
Likelihood: [High / Moderate / Low / Unlikely]

CATEGORY 4 — ENGAGEMENT AND ALLIANCE
Attendance: [%]     Homework completion: [%]     Alliance score (SRS if available): [X]
Identified rupture or ambivalence: [Yes / No / Possible]
Session-bound gains without generalization: [Yes / No]
Likelihood: [High / Moderate / Low / Unlikely]

CATEGORY 5 — EXTERNAL / MAINTAINING FACTORS
Active stressors or maintaining environments: [...]
Exposure to ongoing trauma or unsafe conditions: [Yes / No — describe]
Support system impact: [Supportive / Neutral / Undermining]
Likelihood: [High / Moderate / Low / Unlikely]

CATEGORY 6 — MEDICATION AND MEDICAL FACTORS
Psychotropics (current): [Med, dose, duration, adherence, side effects]
Medication consideration (needed but not tried / may be contributing to symptoms): [...]
Relevant medical conditions: [...]
Likelihood: [High / Moderate / Low / Unlikely]

────────────────────────────────────────────────────────
RANKED DIFFERENTIAL

| Rank | Category | Likelihood | Primary evidence |
|------|----------|------------|-----------------|
| 1 | [Category #] | [High] | [Key indicator] |
| 2 | [Category #] | [Moderate] | [Key indicator] |
| 3 | [Category #] | [Moderate] | [Key indicator] |

────────────────────────────────────────────────────────
REVISED PLAN WITH TESTABLE HYPOTHESES

Hypothesis 1: [State causal hypothesis]
  Plan change: [Specific modification to modality, technique, frequency, or target]
  Success criterion: [What improvement within what timeframe confirms hypothesis]
  Disconfirmation criterion: [What result at what timeframe would refute hypothesis]
  Re-evaluation date: [YYYY-MM-DD]

Hypothesis 2: [State causal hypothesis]
  [same structure]

Hypothesis 3 (if applicable): [...]

────────────────────────────────────────────────────────
REFERRAL / CONSULTATION INDICATIONS

[ ] Psychiatric consultation / medication evaluation recommended: [Rationale]
[ ] Specialty referral (eating disorders / SUD / neuropsychology / other): [Rationale]
[ ] Peer consultation or supervision with modality specialist recommended: [Rationale]
[ ] Second opinion from independent clinician: [Rationale]
[ ] None at this time — reformulation sufficient: [Rationale]

[clinician input required: client's own account of why they feel stuck]
[clinician input required: clinician countertransference reflection — frustration, helplessness, boredom]
```

## Verification

- [ ] Non-response operationally defined using outcome trajectory data, not clinical impression alone.
- [ ] All six contributing-cause categories evaluated, not just the most obvious.
- [ ] Each category given a likelihood rating with supporting evidence.
- [ ] Ranked differential produced with ≥ 2 probable causes identified.
- [ ] Revised plan includes testable hypotheses — each change is tied to a causal hypothesis.
- [ ] Each hypothesis has both a success criterion (confirms) and a disconfirmation criterion (refutes).
- [ ] Re-evaluation date specified for each hypothesis; not open-ended.
- [ ] Clinician's own contribution (fidelity, drift, countertransference) addressed — not omitted.
- [ ] Referral / consultation indications evaluated and documented.
- [ ] Client's goals preserved in revised plan; mechanism changed, not destination.
- [ ] Nothing fabricated; missing inputs flagged with `[clinician input required]`.
