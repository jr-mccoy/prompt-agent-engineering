---
title: "Assessment Battery Selection Aid"
category: psychology/assessment-testing
description: "Translate a referral question into a defensible assessment battery — mapping referral question to constructs, candidate instruments (named only), and a battery design with time/cost/burden tradeoffs and referral thresholds."
techniques:
  - ST-04
  - DT-02
  - RT-02
  - QA-04
  - CM-02
difficulty: advanced
intended_use: model-testing
tags:
  - assessment
  - test-battery
  - referral-question
  - construct-mapping
  - cognitive-testing
  - personality-testing
  - forensic-awareness
  - battery-design
updated: "2026-06-08"
related_prompts:
  - domain-psychology/assessment-testing/psychology_neuropsych_screening_interpretation.md
  - domain-psychology/assessment-testing/psychology_adhd_testing_battery_design.md
  - domain-psychology/assessment-testing/psychology_autism_testing_battery_design.md
  - domain-psychology/assessment-testing/psychology_integrated_assessment_report_writer.md
---

# Assessment Battery Selection Aid

## Objective

Given a referral question and the client's clinical context, produce a structured battery-selection plan that:

1. Restates the referral question precisely and identifies what it can and cannot answer.
2. Decomposes the referral question into the **constructs** that must be measured to answer it.
3. Maps each construct to **candidate instruments** (referenced by name only) with their role (core / supplemental / validity).
4. Proposes a **tiered battery design** (core battery + conditional add-ons) with explicit time, cost, and examinee-burden tradeoffs.
5. Flags **referral-out thresholds** — when the question exceeds the scope of a standard psychological battery (e.g., neuropsychology, neurology, forensic specialist, medical workup).

This is a planning scaffold. Instrument selection, administration, scoring, and interpretation are the examiner's clinical responsibilities; all selections require examiner confirmation.

## When to Use

- A referral question arrives ("rule out ADHD," "differential dementia vs. depression," "capacity to consent," "personality contribution to treatment failure") and the examiner must design a battery before testing begins.
- Pre-authorization or scope-of-work planning where time and cost must be justified to a payer or referrer.
- Triage of whether a presenting question is answerable in-house or requires referral to a sub-specialist (neuropsych, forensic, medical).
- Teaching or supervision: demonstrating the referral-question → construct → instrument reasoning chain.

## Inputs / Context Required

Provide what is available; mark unknowns rather than guessing.

- **Referral question** verbatim, and **referral source** (self, treating clinician, school, attorney, court, disability/insurance, employer) — the source shapes validity and forensic considerations `[clinician input required]`.
- **Setting and purpose:** clinical, educational/eligibility, forensic, disability/fitness-for-duty, research. Forensic and disability contexts raise the stakes on validity/effort testing.
- **Examinee characteristics:** age, primary language, education, sensory/motor limitations, suspected acuity (acute crisis vs. stable), known medical/neurological history `[clinician input required]`.
- **Constraints:** total time available, payer/CPT limits, examinee tolerance/fatigue, available qualified administration level (e.g., who can administer/score restricted instruments).
- **Prior testing:** any instruments already administered and when (to avoid practice effects and redundancy).
- **Differential of interest:** the conditions that must be distinguished (e.g., ADHD vs. anxiety vs. learning disorder vs. sleep).

## Constraints

### Must

- Restate the referral question and explicitly separate what a psychological battery **can** answer from what it **cannot** (e.g., a battery does not provide a neuroimaging diagnosis, a legal determination, or a medical etiology).
- Decompose the question into named constructs before naming any instrument — instrument selection follows construct mapping, never precedes it.
- For each instrument, state its **role** (core measure of the target construct / supplemental / validity or effort measure / collateral or rating scale) and the **construct** it indexes.
- Build the battery with at least one **validity/effort consideration** appropriate to the setting (symptom validity and/or performance validity, especially in forensic, disability, or external-incentive contexts).
- State **administration-qualification level** awareness (some instruments require specific examiner qualifications) and **time/burden** estimates per tier.
- Include explicit **referral-out thresholds**: name the conditions under which the examiner should refer to neuropsychology, neurology, forensic specialist, or medical workup rather than proceeding.
- Apply **multi-method / multi-informant** reasoning where the construct warrants it (e.g., do not rest a developmental or behavioral question on a single self-report).
- Note **cultural, linguistic, and norm-applicability** considerations — flag when an instrument's norms may not apply to the examinee.

### Must Not

- Do **not** reproduce any copyrighted instrument content — no test items, no verbatim questions, no proprietary scoring keys, no copyrighted normative tables. Reference instruments by name and interpret only structure, index names, and score-range bands.
- Do not name an instrument without tying it to a construct and a role.
- Do not propose a battery that ignores examinee burden, time limits, or qualification requirements.
- Do not present the battery as answering questions outside a psychological assessment's scope (medical etiology, legal verdict, neuroimaging findings).
- Do not fabricate availability of scores, prior results, or examinee history — use `[clinician input required: ___]`.
- Do not omit validity/effort planning in any external-incentive context.

## Instructions

1. **Restate and bound the referral question.** Write the question precisely. State the decision it must inform. Then write a short "Answerable / Not answerable by this battery" pair so scope is explicit from the start.

2. **Decompose into constructs.** List the constructs that must be measured to answer the question (e.g., for "rule out ADHD in an adult": sustained/selective attention, executive function, developmental history of symptoms, current functional impairment, and differential constructs — mood, anxiety, sleep, learning, substance use).

3. **Map constructs to candidate instruments (named only).** For each construct, name 1–3 candidate instruments and mark each as core, supplemental, validity/effort, or rating-scale/informant. Examples of instrument *families* to draw from by domain (name only):
   - General cognition / IQ: WAIS-IV / WISC-V.
   - Cognitive screening: MoCA, MMSE, RBANS, SLUMS, Mini-Cog.
   - Memory and executive (full neuropsych): refer out unless qualified.
   - Personality (self-report): MMPI-2-RF / MMPI-3, PAI.
   - Personality (performance-based): Rorschach R-PAS.
   - ADHD: Conners, CAARS, ASRS, Vanderbilt, BRIEF-2; continuous performance tests (TOVA/CPT) with caveats.
   - Autism: ADOS-2, ADI-R, AQ, RAADS-R, CAT-Q, SRS-2, Vineland.
   - Validity/effort: symptom-validity and performance-validity measures appropriate to setting.

4. **Design the tiered battery.** Build a **Core battery** (administered to everyone for this referral) and **Conditional add-ons** (triggered by specific findings or differentials). For each tier, estimate administration time and examinee burden.

5. **Add validity/effort layer.** Specify the symptom-validity and/or performance-validity approach appropriate to the setting; escalate in forensic/disability/external-incentive contexts.

6. **Apply norm and cultural calibration.** Flag any instrument whose norms may not fit the examinee's age, language, education, or cultural background, and note adjustments or alternatives.

7. **Set referral-out thresholds.** State when the question should leave the psychological battery entirely (e.g., progressive cognitive decline → neurology + full neuropsych; legal competency standard → forensic specialist; suspected delirium/medical cause → medical workup first).

8. **Run verification.**

## Output Format

```
=== ASSESSMENT BATTERY SELECTION PLAN ===

Examinee: [Initials/ID]    Date: [YYYY-MM-DD]    Setting: [clinical/educational/forensic/disability/research]
Referral source: [self / clinician / school / court / disability / employer]

─────────────────────────────────────────
REFERRAL QUESTION & SCOPE
─────────────────────────────────────────
Question (verbatim): [text]
Decision it informs: [text]
This battery CAN answer:    [bulleted]
This battery CANNOT answer: [bulleted — route elsewhere]

─────────────────────────────────────────
CONSTRUCT DECOMPOSITION → CANDIDATE INSTRUMENTS
─────────────────────────────────────────
| Construct to measure | Why it's needed | Candidate instrument(s) (name only) | Role            |
|----------------------|-----------------|-------------------------------------|-----------------|
| [construct]          | [link to Q]     | [instrument]                        | Core/Suppl/Valid/Rating |
| [construct]          | [link to Q]     | [instrument]                        | ...             |

─────────────────────────────────────────
BATTERY DESIGN (TIERED)
─────────────────────────────────────────
CORE BATTERY (administer to all for this referral):
  - [instrument] — [construct] — est. time [min] — burden [low/med/high]
  - [instrument] — ...
  Validity/effort layer: [symptom-validity / performance-validity approach]
  Core total est. time: [min]

CONDITIONAL ADD-ONS (triggered by):
  - IF [finding/differential] → add [instrument] ([construct]) — est. time [min]
  - IF [finding/differential] → add [instrument] — ...

─────────────────────────────────────────
TIME / COST / BURDEN TRADEOFFS
─────────────────────────────────────────
| Option        | Instruments | Est. total time | Examinee burden | Answers the question? |
|---------------|-------------|-----------------|-----------------|-----------------------|
| Lean          | [list]      | [min]           | [low/med]       | [partial/yes]         |
| Standard      | [list]      | [min]           | [med]           | [yes]                 |
| Comprehensive | [list]      | [min]           | [high]          | [yes + differentials] |
Recommended: [option] because [rationale]

─────────────────────────────────────────
NORM / CULTURAL / LINGUISTIC FLAGS
─────────────────────────────────────────
[Instrument] — [norm-applicability or language concern + adjustment] `[clinician input required]`

─────────────────────────────────────────
REFERRAL-OUT THRESHOLDS
─────────────────────────────────────────
Refer to NEUROPSYCHOLOGY (full eval) if: [criteria]
Refer to NEUROLOGY / MEDICAL workup if:   [criteria]
Refer to FORENSIC specialist if:           [criteria]
Defer testing pending [medical/acuity] resolution if: [criteria]

─────────────────────────────────────────
EXAMINER CONFIRMATION
─────────────────────────────────────────
All instrument selections, qualification requirements, and scope decisions require examiner
confirmation. `[clinician input required]`
```

## Verification

- [ ] Referral question is restated verbatim with explicit can/cannot-answer scope.
- [ ] Constructs are decomposed before any instrument is named.
- [ ] Every named instrument is tied to a construct and a role (core/supplemental/validity/rating).
- [ ] A validity/effort layer is present and escalated for external-incentive settings.
- [ ] The battery is tiered (core + conditional) with time and burden estimates.
- [ ] Time/cost/burden tradeoff table offers at least two options with a reasoned recommendation.
- [ ] Norm-applicability, cultural, and linguistic flags are present where relevant.
- [ ] Referral-out thresholds to neuropsychology / neurology / forensic / medical are explicitly stated.
- [ ] No copyrighted item content, verbatim questions, scoring keys, or norm tables are reproduced.
- [ ] No scores, prior results, or history are fabricated; gaps carry `[clinician input required]`.
- [ ] All selections are tagged for examiner confirmation.
