---
title: "Neuropsychological / Cognitive Screening Interpretation"
category: psychology/assessment-testing
description: "Interpret cognitive-screening results (MoCA, MMSE, RBANS, SLUMS, Mini-Cog) into a referral-aware clinical read — distinguishing screening from full neuropsych evaluation, framing domain patterns without overcalling, and flagging when full evaluation or neurology referral is indicated."
techniques:
  - ST-04
  - DT-02
  - RT-02
  - QA-04
  - CM-02
difficulty: advanced
intended_use: model-testing
tags:
  - cognitive-screening
  - MoCA
  - MMSE
  - RBANS
  - neuropsychology-referral
  - domain-profile
  - dementia-differential
  - referral-aware
updated: "2026-06-08"
related_prompts:
  - domain-psychology/assessment-testing/psychology_test_battery_selection_aid.md
  - domain-psychology/assessment-testing/psychology_integrated_assessment_report_writer.md
  - domain-psychology/assessment-testing/psychology_capacity_evaluation_scaffold.md
  - domain-psychology/intake-assessment/psychology_screening_battery_interpreter.md
---

# Neuropsychological / Cognitive Screening Interpretation

## Objective

Given results from a brief cognitive screening instrument (e.g., MoCA, MMSE, RBANS, SLUMS, Mini-Cog), produce a referral-aware clinical interpretation that:

1. Reports the total score against the instrument's published cutoff/range band (by name only — no copyrighted item content or norm tables).
2. Frames the **domain pattern** (memory, executive function, attention, language, visuospatial, orientation) at the level the screen supports — and no further.
3. Explicitly distinguishes **screening from full neuropsychological evaluation**, naming what the screen cannot establish.
4. Applies **confounds** that can depress or inflate scores (delirium, depression, sensory deficit, education, language, acute medical illness) before any interpretation.
5. Flags **referral thresholds** — when a full neuropsychological evaluation, neurology referral, or medical workup is indicated rather than continued screening-level interpretation.

This is an interpretation scaffold; the screen does not diagnose dementia, MCI, or any neurological condition. All conclusions require clinician confirmation.

## When to Use

- A brief cognitive screen has been administered and the clinician needs an organized, appropriately cautious read.
- Differential framing of cognitive complaints (e.g., "is this depression, normal aging, or possible neurodegenerative process?") at the screening level.
- Deciding whether to refer for full neuropsychological evaluation or neurology rather than re-screening.
- Documentation of cognitive screening within an intake, capacity, or treatment-planning note.

## Inputs / Context Required

Provide what is available; mark unknowns rather than guessing.

- **Instrument and version** administered (MoCA / MMSE / RBANS / SLUMS / Mini-Cog / other) and **total score** `[clinician input required]`.
- **Subscale / index pattern** if the instrument provides one (e.g., RBANS index names: Immediate Memory, Visuospatial/Constructional, Language, Attention, Delayed Memory) — index-level scores/bands only, no item content.
- **Demographic/norm factors:** age, education years, primary language, literacy, sensory (vision/hearing) and motor status `[clinician input required]`.
- **Acute state factors:** current delirium signs, acute medical illness, substances/medications affecting cognition, fatigue, pain, mood state (active depression/anxiety) at time of testing.
- **Complaint and course:** the cognitive complaint, who raised it (self vs. informant), and **trajectory** (acute / stepwise / gradually progressive / fluctuating / static).
- **Functional impact:** any reported change in instrumental activities of daily living (IADLs) or daily functioning, with informant corroboration if available.
- **Prior screening scores** if any (for change-over-time), with dates.

## Constraints

### Must

- State the instrument's total-score interpretation as a **band relative to the published cutoff** (e.g., "below the standard cutoff," "in the normal range," "borderline") — never reproduce the copyrighted cutoff table or item content.
- Apply **confound screening before interpretation**: explicitly check delirium, depression/anxiety, sensory deficit, education/literacy, language, acute illness, and medication/substance effects, because each can invalidate a low score.
- Distinguish **screening vs. full evaluation** in the body of the interpretation: a screen flags concern and tracks gross change; it does not localize, diagnose a dementia subtype, or establish MCI vs. dementia.
- Interpret the **domain pattern only to the resolution the screen supports** — brief screens give coarse domain signals, not validated profiles; do not infer a specific etiology (Alzheimer's vs. vascular vs. Lewy body) from a screen.
- Incorporate **trajectory and functional impact**, because a screen score is far more meaningful when paired with course and IADL change.
- State **referral thresholds** explicitly: when to refer for full neuropsychological evaluation, when to refer to neurology, and when acute/medical workup takes precedence (e.g., suspected delirium, sudden change).
- Note **practice effects and floor/ceiling limits** when a prior score is provided, and avoid over-reading small score changes.
- Flag missing confound or trajectory data with `[clinician input required: ___]` rather than assuming.

### Must Not

- Do **not** reproduce copyrighted instrument content — no items, verbatim tasks, scoring keys, or copyrighted norm/cutoff tables. Reference instruments by name and interpret bands/index names only.
- Do not diagnose dementia, MCI, delirium, or any neurological condition from a screen.
- Do not specify a neurodegenerative subtype or localize a lesion from a brief screen.
- Do not interpret a low score without first ruling out delirium, depression, sensory deficit, language, and education confounds.
- Do not treat a screen as a substitute for full neuropsychological evaluation when the referral question demands one.
- Do not over-read small score differences between administrations as meaningful decline or improvement.
- Do not fabricate scores, index values, trajectory, or functional data.

## Instructions

1. **Confirm instrument, version, and score.** Identify the screen and report the total as a band relative to its published cutoff (no copyrighted figures). If a version-specific or education-adjusted cutoff applies, note it conceptually `[clinician input required]`.

2. **Run the confound check first.** Before interpreting, evaluate each confound and state whether it could account for or distort the result:
   - Delirium / acute fluctuating attention → if suspected, the screen is likely uninterpretable; medical workup precedes cognitive interpretation.
   - Depression/anxiety (pseudodementia pattern) → effort, processing speed, and memory can be depressed by mood.
   - Sensory deficit (vision/hearing) and motor limitation → may invalidate visuospatial/graphomotor items.
   - Education, literacy, and primary language → may lower scores independent of cognition; consider appropriately normed/translated alternatives.
   - Medication/substance effects and acute illness/pain/fatigue.

3. **Frame the domain pattern at screen resolution.** Using available subscale/index signals, describe which domains appear relatively preserved vs. relatively weak (memory, executive, attention, language, visuospatial, orientation). Explicitly state this is a coarse signal, not a validated profile.

4. **Integrate trajectory and function.** Combine the score with course (acute/progressive/fluctuating/static) and IADL change. Note that a low score with documented progressive IADL decline carries different weight than an isolated low score.

5. **Compare to prior screen (if available).** Note direction and magnitude of change, but caution against over-reading small changes given practice effects and measurement error.

6. **State the referral disposition.** Choose and justify one:
   - Continue monitoring / re-screen interval.
   - Refer for full neuropsychological evaluation.
   - Refer to neurology / medical workup.
   - Urgent medical evaluation (e.g., suspected delirium or acute change).

7. **Run verification.**

## Output Format

```
=== COGNITIVE SCREENING INTERPRETATION ===

Client: [Initials/MRN]    Date: [YYYY-MM-DD]
Instrument: [MoCA/MMSE/RBANS/SLUMS/Mini-Cog/other] (version: [v])
Total score band vs. cutoff: [below cutoff / borderline / within normal range]   `[clinician input required for raw score]`

─────────────────────────────────────────
CONFOUND CHECK (complete before interpreting)
─────────────────────────────────────────
| Confound                   | Present? | Impact on this result                     |
|----------------------------|----------|-------------------------------------------|
| Delirium / fluctuating attn| [Y/N/?]  | [if Y → screen may be uninterpretable]    |
| Depression / anxiety       | [Y/N/?]  | [...]                                      |
| Sensory (vision/hearing)   | [Y/N/?]  | [...]                                      |
| Education / literacy / language | [Y/N/?] | [...]                                  |
| Medication / substance     | [Y/N/?]  | [...]                                      |
| Acute illness / pain / fatigue | [Y/N/?] | [...]                                   |
Confound summary: [is the score interpretable as a cognitive signal? Y / N / qualified]

─────────────────────────────────────────
DOMAIN PATTERN (screen-level resolution only)
─────────────────────────────────────────
| Domain          | Relative signal (preserved / weak / not assessed) | Note |
|-----------------|---------------------------------------------------|------|
| Memory          | [ ]                                               | [ ]  |
| Executive       | [ ]                                               | [ ]  |
| Attention       | [ ]                                               | [ ]  |
| Language        | [ ]                                               | [ ]  |
| Visuospatial    | [ ]                                               | [ ]  |
| Orientation     | [ ]                                               | [ ]  |
Caveat: brief-screen domain signals are coarse and do not constitute a validated neuropsychological profile.

─────────────────────────────────────────
TRAJECTORY & FUNCTIONAL CONTEXT
─────────────────────────────────────────
Course: [acute / stepwise / gradually progressive / fluctuating / static]   `[clinician input required]`
IADL / functional change: [described + informant corroboration Y/N]
Prior screen (if any): [score band, date] → change: [direction/magnitude] (caution: practice effects)

─────────────────────────────────────────
SCREENING VS. FULL EVALUATION
─────────────────────────────────────────
This screen flags concern and tracks gross change. It does NOT: diagnose dementia or MCI,
distinguish neurodegenerative subtypes, localize, or substitute for full neuropsychological
evaluation.

─────────────────────────────────────────
REFERRAL DISPOSITION
─────────────────────────────────────────
[ ] Monitor / re-screen in [interval] — rationale: [ ]
[ ] Refer for FULL NEUROPSYCHOLOGICAL EVALUATION — rationale: [ ]
[ ] Refer to NEUROLOGY / medical workup — rationale: [ ]
[ ] URGENT medical evaluation (e.g., suspected delirium / acute change) — rationale: [ ]

─────────────────────────────────────────
CLINICIAN CONFIRMATION
─────────────────────────────────────────
Interpretation and disposition require clinician confirmation. `[clinician input required]`
```

## Verification

- [ ] Total score reported as a band relative to the published cutoff (no copyrighted table reproduced).
- [ ] Confound check (delirium, mood, sensory, education/language, medication, acute illness) completed before interpretation.
- [ ] If delirium or acute change is suspected, medical workup is prioritized over cognitive interpretation.
- [ ] Domain pattern is framed only at screen-level resolution, with the coarse-signal caveat present.
- [ ] No dementia/MCI diagnosis, subtype, or lesion localization is asserted from the screen.
- [ ] Trajectory and functional (IADL) context are integrated with the score.
- [ ] Prior-score comparison (if any) avoids over-reading small changes; practice effects noted.
- [ ] Screening-vs-full-evaluation distinction is stated explicitly in the body.
- [ ] Referral thresholds to full neuropsych / neurology / urgent medical workup are stated and justified.
- [ ] No copyrighted item content, tasks, scoring keys, or norm tables are reproduced.
- [ ] No scores, index values, trajectory, or functional data are fabricated; gaps carry `[clinician input required]`.
