---
title: "Geriatric Depression vs. Dementia Differential (Pseudodementia Screening)"
category: psychology/populations/geriatric
description: "Structured differential framework distinguishing depression-related cognitive impairment (pseudodementia) from early neurodegenerative dementia in older adults, integrating GDS, Mini-Cog/MoCA/MMSE, Cornell scale, Wells' pseudodementia features, and an elevated late-life suicide risk screen."
techniques:
  - DT-02
  - RT-02
  - RT-03
  - DS-04
  - QA-04
difficulty: advanced
intended_use: model-testing
tags:
  - geriatric
  - depression
  - dementia
  - pseudodementia
  - differential
  - cognitive-screen
  - GDS
  - MoCA
  - cornell-scale
  - late-life-suicide-risk
updated: "2026-06-08"
related_prompts:
  - domain-psychology/populations/geriatric/psychology_geriatric_intake_with_polypharmacy_review.md
  - domain-psychology/populations/geriatric/psychology_geriatric_grief_and_late_life_transitions.md
  - domain-psychology/diagnostic-formulation/psychology_case_conceptualization_framework.md
  - domain-psychology/risk-crisis/psychology_columbia_suicide_risk_assessment.md
---

# Geriatric Depression vs. Dementia Differential (Pseudodementia Screening)

## Objective

Produce a structured differential analysis distinguishing **depression-related cognitive impairment ("pseudodementia," more accurately depressive cognitive impairment)** from **early neurodegenerative dementia** (and from the comorbid "depression-superimposed-on-dementia" picture) in an older adult presenting with concurrent low mood and cognitive complaints. The output:

1. Organizes presentation features into a side-by-side differential matrix.
2. Applies named screening instruments (GDS, Cornell Scale, Mini-Cog/MoCA/MMSE) and interprets their bands without reproducing copyrighted item text.
3. Applies Wells' classic pseudodementia features as a heuristic, not a diagnostic rule.
4. Screens explicitly for elevated late-life suicide risk (older adults, especially older men, carry disproportionate completed-suicide rates).
5. Routes to the correct next step: neurocognitive/medical workup, depression treatment trial, or both.

This prompt supports clinical reasoning; it does not replace formal neuropsychological testing, neuroimaging, or physician evaluation.

## When to Use

- An older adult (typically 60+) presents with new or worsening memory complaints **and** depressive symptoms, and the source of the cognitive impairment is ambiguous.
- A patient with diagnosed depression shows cognitive complaints out of proportion to mood, or vice versa.
- A collateral informant reports cognitive or functional decline and the clinician must triage whether to pursue a mood-treatment trial, a dementia workup, or both in parallel.
- Treatment of a presumed depression has not improved cognition, prompting reconsideration of a neurodegenerative process.

## When NOT to Use

- For acute confusion / fluctuating consciousness suggestive of **delirium** — delirium is a medical emergency and takes priority; route to urgent medical evaluation (consider CAM screen) before this differential.
- As a substitute for formal neuropsychological evaluation or neuroimaging when a dementia workup is clinically indicated.
- For a patient already carrying an established, well-characterized dementia diagnosis where the question is purely behavioral management (use a BPSD-focused protocol instead).
- For younger adults where the depression-vs-dementia base rates and instrument validation differ.

## Inputs / Context Required

- **Demographics:** Age, education level (affects cognitive screen cutoffs), primary language, sensory status (vision/hearing — uncorrected deficits confound cognitive screens).
- **Presenting complaint:** Whose concern (patient vs. collateral), onset, course, and timeline of mood vs. cognitive symptoms.
- **Cognitive screen data (if available):** MMSE, MoCA, or Mini-Cog scores with administration conditions; prior baseline scores if any.
- **Mood screen data (if available):** GDS-15 or GDS-30 score; for patients with established cognitive impairment, Cornell Scale for Depression in Dementia (informant + patient).
- **Functional status:** ADLs (Katz) and IADLs (Lawton) with informant corroboration; note which functions are lost and the pattern.
- **Collateral history:** Informant report on memory, language, executive function, personality change, and effort/engagement.
- **Medical/medication context:** Active conditions, recent medication changes (link to `psychology_geriatric_intake_with_polypharmacy_review.md` for anticholinergic/Beers review), substance use, sleep, vascular risk factors.
- `[clinician input required: any neurological signs, prior neuroimaging, or physician/neurology evaluation already completed]`
- `[clinician input required: current suicide-risk indicators — ideation, plan, access to lethal means, recent losses]`

## Constraints

### Must

- Present the differential as a **probabilistic weighting**, not a binary verdict; the two conditions co-occur ("depression-superimposed-on-dementia") and either can mask the other.
- Apply and interpret named instruments by their **band structure** (e.g., GDS-15 suggestive cutoffs, MoCA <26 impairment threshold adjusted for education) without reproducing copyrighted item wording.
- Use Wells' classic pseudodementia features (rapid onset, patient distress/complaints emphasizing deficits, "I don't know" answers, variable/poor effort, preserved attention, mood preceding cognitive change) as a **heuristic flag set**, explicitly noting it is sensitive but not specific.
- Screen for elevated late-life suicide risk in every case and route a positive screen to a formal suicide-risk assessment (`psychology_columbia_suicide_risk_assessment.md`).
- Flag reversible/contributory medical drivers (B12/folate, thyroid, medication burden, sensory deficits, sleep apnea, vascular disease) and recommend medical workup hooks.
- Recommend a concrete next step: depression treatment trial, neurocognitive/medical workup, or both in parallel — with the reasoning.
- Flag every missing data element with `[clinician input required: ...]`.

### Must Not

- Do not deliver a definitive dementia diagnosis or rule one out from screening data alone; formal evaluation is required for diagnosis.
- Do not reproduce copyrighted instrument item text (MMSE, MoCA, GDS, Cornell); reference by name and interpret bands only.
- Do not fabricate specific scores, imaging findings, or neurological signs not provided.
- Do not attribute cognitive impairment to depression and defer a dementia workup when red-flag neurodegenerative features are present.
- Do not omit the suicide-risk screen, even when mood appears mild.

## Differential Feature Matrix

| Feature | Favors Depressive Cognitive Impairment (Pseudodementia) | Favors Early Neurodegenerative Dementia |
|---------|--------------------------------------------------------|------------------------------------------|
| Onset | Relatively rapid, datable; family can often pinpoint | Insidious, gradual, hard to date |
| Symptom sequence | Mood change precedes cognitive complaints | Cognitive/functional change precedes (or no clear mood antecedent) |
| Patient's stance toward deficits | Distressed, emphasizes and complains of memory loss | Often minimizes, unaware, or unconcerned (anosognosia) |
| Typical answer style | "I don't know" / gives up easily; effort variable | Confabulates or near-misses; attempts answers |
| Effort on testing | Poor / inconsistent effort | Genuine effort with true errors |
| Attention/concentration | Often relatively preserved | Frequently impaired early (esp. non-amnestic types) |
| Memory pattern | Inconsistent; improves with cueing/recognition | Encoding deficit; poor recognition; cueing does not rescue (in AD-type) |
| Diurnal pattern | Mood/cognition often worse in morning | Often "sundowning" — worse late day |
| Functional loss pattern | Disproportionate to objective deficit; motivation-linked | Progressive, stepwise (vascular) or steady decline |
| Course over weeks | Improves with mood treatment | Stable or progressive despite mood treatment |
| Neurological signs | Typically absent | May have focal/extrapyramidal signs, gait change |

> Caveat: This matrix lists *tendencies*. Atypical presentations are common, comorbidity is the rule in older adults, and a normal screen does not exclude either condition.

## Instructions

1. **Organize the timeline.** Build a side-by-side timeline of mood symptoms and cognitive/functional symptoms. Establish which came first and the rate of change. Note informant source for each data point.

2. **Interpret cognitive screens.** Apply MMSE/MoCA/Mini-Cog results against education-adjusted bands. Note administration confounds (sensory deficits, language, fatigue, low effort). If no screen available, recommend one and specify which.

3. **Interpret mood screens.** Apply GDS-15/GDS-30 banding. If the patient has established cognitive impairment limiting self-report reliability, prioritize the Cornell Scale for Depression in Dementia (informant-integrated).

4. **Apply Wells' pseudodementia heuristic.** Tally which classic features are present; treat as a flag set raising the probability of a depressive contribution, not as a diagnosis.

5. **Score the differential matrix.** Walk each row; weight the overall picture toward depressive cognitive impairment, neurodegenerative dementia, or a comorbid picture. State confidence.

6. **Screen reversible/medical contributors.** Flag B12/folate, TSH, medication/anticholinergic burden, sensory deficits, sleep, substance use, vascular risk — recommend medical workup hooks. Cross-reference the polypharmacy review prompt.

7. **Screen suicide risk.** Apply a brief late-life suicide-risk screen; route any positive to formal assessment. Document protective factors and access to means.

8. **Recommend next steps.** Specify: depression treatment trial, neurocognitive/medical workup, or both in parallel — with reasoning and a re-assessment timeframe (a depression trial that fails to improve cognition over an adequate course shifts probability toward dementia).

9. **Run verification.**

## Output Format

```
=== GERIATRIC DEPRESSION vs. DEMENTIA DIFFERENTIAL ===

Patient: [Initials/MRN]   Age: [N]   Education: [years]   Date: [YYYY-MM-DD]
Clinician: [Name, credentials]
Primary referral question: [...]
Sensory/language confounds noted: [Vision: ... | Hearing: ... | Language/interpreter: ...]

─────────────────────────────────────────
SYMPTOM TIMELINE
─────────────────────────────────────────
Mood symptom onset/course: [...]
Cognitive/functional symptom onset/course: [...]
Which preceded: [Mood-first / Cognitive-first / Unclear — informant: ...]

─────────────────────────────────────────
COGNITIVE SCREEN
─────────────────────────────────────────
Instrument: [Mini-Cog / MoCA / MMSE / Not administered]
Score: [N / max]   Education-adjusted interpretation: [Within normal / Borderline / Impaired]
Administration confounds: [...]
Memory pattern (cueing/recognition response): [Rescued by cueing / Not rescued / Not assessed]
[clinician input required: prior baseline score if available]

─────────────────────────────────────────
MOOD SCREEN
─────────────────────────────────────────
Instrument: [GDS-15 / GDS-30 / Cornell Scale for Depression in Dementia]
Score: [N]   Band interpretation: [No/mild/moderate/severe depression suggestive range]
Cornell used (if cognitively impaired): [Yes — informant + patient integrated / No]

─────────────────────────────────────────
WELLS' PSEUDODEMENTIA FEATURE TALLY (heuristic — sensitive, not specific)
─────────────────────────────────────────
[ ] Relatively rapid, datable onset
[ ] Mood change preceded cognitive complaints
[ ] Patient emphasizes/complains of deficits (distress)
[ ] "I don't know" answers / gives up
[ ] Variable or poor effort on testing
[ ] Attention relatively preserved
Features present: [N/6]   Interpretation: [...]

─────────────────────────────────────────
FUNCTIONAL STATUS
─────────────────────────────────────────
ADLs (Katz): [Independent / dependent in: ...]
IADLs (Lawton): [Independent / dependent in: ...]
Functional loss proportionate to objective cognition: [Yes / Disproportionate — motivation-linked]

─────────────────────────────────────────
DIFFERENTIAL WEIGHTING
─────────────────────────────────────────
Leaning: [Depressive cognitive impairment / Neurodegenerative dementia / Comorbid (depression-superimposed-on-dementia) / Indeterminate]
Confidence: [Low / Moderate / High]
Key discriminating features driving the weighting: [...]
Red-flag neurodegenerative features present: [None / List: focal signs, anosognosia, non-rescue with cueing, gait change, ...]

─────────────────────────────────────────
REVERSIBLE / MEDICAL CONTRIBUTORS TO WORK UP
─────────────────────────────────────────
[ ] B12 / folate   [ ] TSH   [ ] Medication / anticholinergic burden (see polypharmacy review)
[ ] Sensory deficits (vision/hearing)   [ ] Sleep / OSA   [ ] Substance use   [ ] Vascular risk / prior CVA
Other: [...]

─────────────────────────────────────────
SUICIDE-RISK SCREEN (late-life elevated risk)
─────────────────────────────────────────
Ideation: [Present — passive/active / Absent]
Plan / intent: [...]   Access to lethal means (incl. firearms): [...]
Recent losses / role changes / isolation: [...]
Protective factors: [...]
Screen result: [Negative / Positive — route to formal C-SSRS assessment]
[clinician input required: disposition if positive]

─────────────────────────────────────────
RECOMMENDED NEXT STEPS
─────────────────────────────────────────
[ ] Depression treatment trial — modality/med: [...]; reassessment window: [N weeks]
[ ] Neurocognitive workup / neuropsych referral
[ ] Neuroimaging / physician/neurology evaluation
[ ] Both in parallel
Decision rule applied: [If mood treatment fails to improve cognition over adequate course → shift toward dementia workup]
Capacity / driving / safety concerns to address: [...]
[clinician input required: ...]
```

## Verification

- [ ] Symptom timeline establishes mood-first vs. cognitive-first sequence (or documents it as unclear).
- [ ] Cognitive screen interpreted against education-adjusted bands; confounds noted; no copyrighted item text reproduced.
- [ ] Mood screen interpreted by band; Cornell Scale used when cognitive impairment limits self-report.
- [ ] Wells' pseudodementia features tallied and explicitly labeled as heuristic (sensitive, not specific).
- [ ] Functional status documented via Katz/Lawton with proportionality assessment.
- [ ] Differential delivered as probabilistic weighting with confidence, not a binary diagnosis.
- [ ] Comorbid "depression-superimposed-on-dementia" possibility explicitly considered.
- [ ] Reversible/medical contributors flagged with workup hooks (incl. polypharmacy cross-reference).
- [ ] Late-life suicide-risk screen completed; positive routed to formal assessment.
- [ ] Delirium excluded as the acute driver before applying this differential.
- [ ] Concrete next step recommended with a reassessment window and decision rule.
- [ ] No fabricated scores, imaging, or neurological signs; gaps flagged with `[clinician input required: ...]`.
