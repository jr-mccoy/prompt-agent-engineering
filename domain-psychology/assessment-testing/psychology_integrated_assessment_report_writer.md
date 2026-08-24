---
title: "Integrated Assessment Report Writer"
category: psychology/assessment-testing
description: "Write an integrated psychological assessment report from multi-source findings — synthesizing referral question, background, behavioral observations, validity considerations, results organized BY DOMAIN/QUESTION, integrated interpretation, diagnostic impressions, and tailored recommendations as a narrative integration rather than a data dump."
techniques:
  - ST-04
  - DS-04
  - QA-04
  - CM-01
  - RT-02
difficulty: advanced
intended_use: model-testing
tags:
  - integrated-report
  - psychological-assessment
  - report-writing
  - by-domain-organization
  - validity-considerations
  - behavioral-observations
  - diagnostic-impressions
  - recommendations
updated: "2026-06-08"
related_prompts:
  - domain-psychology/assessment-testing/psychology_test_battery_selection_aid.md
  - domain-psychology/assessment-testing/psychology_neuropsych_screening_interpretation.md
  - domain-psychology/assessment-testing/psychology_personality_assessment_integration.md
  - domain-psychology/assessment-testing/psychology_feedback_session_planner.md
---

# Integrated Assessment Report Writer

## Objective

Produce an integrated psychological assessment report that **synthesizes** multi-source findings into a coherent narrative rather than listing results test-by-test. The report is organized so that each clinical conclusion is **anchored to the referral question** and built from **convergent evidence across data sources** (interview, behavioral observations, records, collateral, and named test instruments). It includes the standard sections — referral question, relevant background/history, behavioral observations, **validity/effort considerations**, results organized **by domain or by referral question (not by instrument)**, an **integrated interpretation** that reconciles convergent and discrepant findings, diagnostic impressions, and tailored, prioritized recommendations. The defining feature is **integration**: results are interpreted together, not reported as isolated scores. The clinician supplies the interpreted findings and judgments; this tool structures and synthesizes them.

## When to Use

- Writing up a completed psychological, psychoeducational, personality, or neuropsychological assessment that used multiple data sources.
- Converting a draft that reads as a test-by-test data dump into a domain-organized, integrated narrative.
- Producing a report whose conclusions must be defensible — each tied to the referral question and supported by convergent evidence.
- Preparing a report that will feed a therapeutic feedback session and downstream treatment, educational, or vocational planning.

This writer organizes and integrates supplied findings; it does not score tests, generate raw data, or render judgments the clinician has not made.

## Inputs / Context Required

Provide what is available; flag the rest. Do not fabricate scores, history, observations, or conclusions.

- **Referral question(s)** and **referral source** — the specific question(s) the report must answer `[clinician input required]`.
- **Relevant background/history** — developmental, medical, psychiatric, educational, occupational, social, and prior assessment, to the extent relevant to the question `[clinician input required]`.
- **Behavioral observations** during testing (engagement, affect, frustration tolerance, test-taking approach) `[clinician input required]`.
- **Data sources used** — interview, records, collateral, and the **named instruments** administered (names only) `[clinician input required]`.
- **Validity / effort considerations** — performance-validity and symptom-validity status and any factors affecting interpretability (named measures only, no items) `[clinician input required]`.
- **Interpreted findings by domain** — the clinician's conclusions per relevant domain (e.g., cognition, academic, attention/EF, emotional functioning, personality, adaptive functioning) `[clinician input required]`.
- **Convergent and discrepant findings** the clinician wants reconciled.
- **Diagnostic impressions** the clinician is forming (DSM-5-TR / ICD-10-CM), and the differential considered `[clinician input required]`.
- **Recommendation targets** — treatment, educational accommodations, vocational, referral, and follow-up needs.

## Constraints

### Must

- Open by **restating the referral question(s)** and make every major conclusion traceable back to a referral question.
- Organize the results/interpretation **by domain or by referral question — not test-by-test**. A given instrument may contribute to multiple domains; do not give each test its own results section.
- Include a **validity / effort section** that states whether results are interpretable and notes performance- and symptom-validity considerations (named measures and convergent indicators only).
- Build the **integrated interpretation** from **convergent evidence across sources**; explicitly reconcile discrepant findings rather than ignoring them, and qualify confidence accordingly.
- Report **behavioral observations** and tie them to interpretation where relevant (e.g., low effort, fatigue, or anxiety affecting performance).
- State **diagnostic impressions** as the clinician's, with the differential and the evidence supporting/weighing against each; distinguish what the data support from what remains uncertain.
- Make **recommendations specific, prioritized, and tied to findings** (each recommendation should map to a finding/question), and actionable for the report's audience.
- State the report's **scope and limits**: what the assessment can and cannot answer, the time-bound nature of findings, and referral triggers (e.g., medical workup, specialist evaluation, re-evaluation interval).

### Must Not

- Do not reproduce copyrighted instrument item content — no items, no verbatim questions, no proprietary scoring keys, and no exact normative tables. Report **interpreted scores by band/range and named index/subtest labels only**, and reference instruments **by name**.
- Do not write a test-by-test data dump; do not let instruments, rather than domains/questions, structure the results.
- Do not state conclusions unsupported by convergent data, and do not omit or bury discrepant findings.
- Do not over-reach the data: do not answer questions the battery cannot address, and do not present a tentative impression as a settled diagnosis.
- Do not fabricate scores, history, observations, validity data, or diagnoses; gaps carry `[clinician input required]`.

## Instructions

1. **Anchor to the referral.** Restate the referral question(s) and source. These define what the report must answer and how success is judged.

2. **Assemble background relevant to the question.** Include only history that bears on the referral question; summarize, do not transcribe records.

3. **Record behavioral observations.** Capture test-session behavior and flag anything affecting interpretability.

4. **State validity/effort first.** Before interpreting results, establish whether they are interpretable — performance- and symptom-validity status and any caveats (named measures only).

5. **Organize results by domain/question.** Group interpreted findings under domains or referral questions. For each domain, integrate evidence from all relevant sources/instruments; report bands/ranges and named indices, not raw items or scores tables that reconstruct the instrument.

6. **Integrate.** Write an interpretation that reconciles convergent and discrepant findings across sources, qualifies confidence, and ties back to the referral question(s).

7. **State diagnostic impressions.** Present the clinician's impressions with differential and supporting/contradicting evidence; separate supported conclusions from open questions.

8. **Write prioritized recommendations.** Map each recommendation to a finding/question; make them specific and actionable for the audience.

9. **State scope, limits, and referral triggers; run verification.**

## Output Format

```
=== INTEGRATED PSYCHOLOGICAL ASSESSMENT REPORT ===

IDENTIFYING INFORMATION: [initials/MRN]   Dates of evaluation: [ ... ]   Examiner: [ ... ]

REFERRAL QUESTION(S) & SOURCE
  Source: [ ... ]
  Question(s): [Q1] [Q2] ...  — the report's conclusions map back to these.

RELEVANT BACKGROUND / HISTORY
  [Developmental/medical/psychiatric/educational/occupational/social, relevant to the question only.]

DATA SOURCES / PROCEDURES (instruments by name only)
  - Clinical interview; records reviewed; collateral: [ ... ]
  - Instruments administered (names only): [ ... ]

BEHAVIORAL OBSERVATIONS
  [Engagement, affect, frustration tolerance, test-taking approach; note anything affecting interpretability.]

VALIDITY / EFFORT CONSIDERATIONS
  Performance-validity: [adequate / concerns — named measure(s)]    Symptom-validity: [ ... ]
  Interpretability: [results interpretable / interpret with caution because ...]

RESULTS & INTERPRETATION — ORGANIZED BY DOMAIN (not by test)
  Domain: [Cognitive / Intellectual]
    Integrated finding (band/range, named indices): [clinician input required]
    Convergent sources: [interview + instrument(s) + observation]
  Domain: [Attention / Executive Functioning]
    Integrated finding: [ ... ]    Discrepancies reconciled: [ ... ]
  Domain: [Academic / Learning]            [ ... ]
  Domain: [Emotional / Personality]        [ ... ]
  Domain: [Adaptive / Functional]          [ ... ]

INTEGRATED SUMMARY
  [Narrative synthesis across domains and sources, tied to each referral question; confidence qualified;
   discrepancies addressed rather than omitted.]

DIAGNOSTIC IMPRESSIONS
  [DSM-5-TR / ICD-10-CM impressions — the clinician's — with differential and supporting/weighing evidence;
   supported conclusions distinguished from open questions.] [clinician input required]

RECOMMENDATIONS (prioritized; each tied to a finding/question)
  1. [Recommendation] → addresses [finding/question]
  2. [ ... ]
  3. [ ... ]

SCOPE, LIMITS & FOLLOW-UP
  This assessment can answer: [ ... ]   It cannot answer: [ ... ]
  Findings reflect functioning at the time of evaluation. Re-evaluation interval: [ ... ]
  Referral triggers: [medical workup / specialist eval / safety pathway if indicated]
```

## Verification

- [ ] Referral question(s) and source are stated up front, and every major conclusion is traceable to a referral question.
- [ ] Results are organized by domain or by referral question — NOT test-by-test; no instrument has its own standalone results section.
- [ ] A validity/effort section establishes interpretability before results are interpreted (named measures only).
- [ ] The integrated interpretation is built from convergent evidence across sources and explicitly reconciles discrepant findings.
- [ ] Behavioral observations are reported and tied to interpretation where relevant.
- [ ] Diagnostic impressions are presented as the clinician's, with differential and supporting/contradicting evidence; supported vs. uncertain conclusions are distinguished.
- [ ] Recommendations are specific, prioritized, and each mapped to a finding/question.
- [ ] Scope, limits, time-bound nature of findings, and referral triggers are stated.
- [ ] No copyrighted item content, verbatim questions, scoring keys, or exact normative tables are reproduced — instruments referenced by name and findings reported by band/range and named index only.
- [ ] No scores, history, observations, validity data, or diagnoses are fabricated; gaps carry `[clinician input required]`.
