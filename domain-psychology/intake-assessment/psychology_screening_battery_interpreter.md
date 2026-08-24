---
title: "Intake Screening Battery Interpreter"
category: psychology/intake-assessment
description: "Compile and interpret an intake screening battery (PHQ-9, GAD-7, PCL-5, AUDIT, C-SSRS) into a clinician-ready summary with flag logic, score tables, and actionable clinical notes."
techniques:
  - ST-04
  - DT-02
  - QA-04
  - CM-02
  - DS-04
difficulty: intermediate
intended_use: model-testing
tags:
  - screening
  - PHQ-9
  - GAD-7
  - PCL-5
  - AUDIT
  - C-SSRS
  - measurement-based-care
  - intake
  - cpt-90791
updated: "2026-06-08"
related_prompts:
  - domain-psychology/documentation/psychology_intake_assessment_note.md
  - domain-psychology/risk-crisis/psychology_columbia_suicide_risk_assessment.md
  - domain-psychology/intake-assessment/psychology_substance_use_history_intake_module.md
  - domain-psychology/intake-assessment/psychology_mental_status_exam_compiler.md
---

# Intake Screening Battery Interpreter

## Objective

Given raw scores from a standard intake screening battery — PHQ-9, GAD-7, PCL-5, AUDIT, and C-SSRS — produce a structured clinician-ready interpretation summary that:

1. Tables all scores with validated severity bands for each instrument.
2. Identifies co-occurring elevation patterns (e.g., PHQ-9 ≥ 15 + PCL-5 ≥ 33) and their clinical implications.
3. Flags mandatory action items (suicidal ideation on C-SSRS Item 5 or 6, AUDIT Zone III/IV, PCL-5 positive screen) with disposition guidance.
4. Produces a structured "Screening Battery Summary" section ready for insertion into a 90791/90792 intake note.
5. Notes the screening-vs-diagnosis distinction throughout: elevated scores identify probable clinical range, not diagnoses.

## When to Use

- At the beginning of a first clinical session to synthesize pre-administered self-report measures before the clinician interview begins.
- When a referring provider or intake coordinator has collected measure scores and the treating clinician needs an organized clinical read.
- As the outcome-measures section of a biopsychosocial intake note (CPT 90791/90792).
- For measurement-based care baseline documentation.

## Inputs / Context Required

Provide all available scores. Indicate "not administered" rather than leaving fields blank so the output correctly flags missing data.

- **PHQ-9 total score** (0–27) and Item 9 response (the suicidality item, 0–3).
- **GAD-7 total score** (0–21).
- **PCL-5 total score** (0–80) and, if available, subscale scores (Cluster B re-experiencing, Cluster C avoidance, Cluster D negative cognitions/mood, Cluster E arousal/reactivity) and the specific item driving highest elevation.
- **AUDIT total score** (0–40), and if the 10-item form was not used, note whether AUDIT-C (3-item) was substituted (scores 0–12).
- **C-SSRS version used** (Lifetime/Recent, Since Last Visit, Screener) and item-level responses: Ideation Types 1–5, Intensity items if any Type > 0, Behavior items (actual attempt, preparatory behavior, interrupted/aborted attempt), and lethality/medical damage if attempt present.
- **Date measures were administered** and **method** (paper self-report, digital platform, clinician-administered).
- **Any additional measures** administered (MDQ, ASRS, DAST-10, PC-PTSD-5, etc.) with scores.
- **Client demographics** relevant to norm-set selection (age, gender, clinical vs. community setting).

## Constraints

### Must

- Present every score in a formatted table with the instrument name, score, validated severity band, and clinical cutoff used — citing the primary validation study's cutoff for each instrument (e.g., PHQ-9 ≥ 10 for moderate depression; PCL-5 ≥ 31–33 for probable PTSD in civilian samples).
- Treat C-SSRS Items 4 and 5 (active ideation with plan, active ideation with intent) as mandatory safety flags requiring immediate clinical response; the output must include a "SAFETY FLAG" label in the interpretation.
- Flag PHQ-9 Item 9 response ≥ 1 as a safety flag requiring C-SSRS follow-up if not already completed.
- Identify co-occurring high elevations (e.g., PHQ + PCL-5 both in clinical range) and note the evidence base for comorbidity implications on treatment complexity.
- Include a brief "Screening vs. Diagnosis" caveat in the summary reminding the reader that elevated scores identify cases for clinical evaluation; diagnoses require clinical interview applying DSM-5-TR criteria.
- Note any scores that fall below the instrument's minimum reliable change (MRC) threshold from a previous administration, if a prior score is provided.
- Flag missing instruments with `[Not administered — consider adding at: reason]`.

### Must Not

- Do not assign a DSM-5-TR diagnosis from screening scores alone.
- Do not omit C-SSRS item-level detail; a total "score" alone is not sufficient for C-SSRS — item endorsements drive the safety response.
- Do not use AUDIT-C cutoffs (≥ 4 women / ≥ 5 men) as if they are AUDIT-10 cutoffs — differentiate clearly.
- Do not interpret PCL-5 using DSM-IV PCL-C cutoffs; use DSM-5-TR aligned cutoffs (≥ 31–33 civilian, ≥ 38 for military validation samples, or the Weathers et al. 2013 guidance).
- Do not suppress low scores — document them as negative screens with the score and band.
- Do not fabricate scores; where input is incomplete, flag with `[clinician input required: ___]`.

## Instructions

1. **Parse inputs.** Accept all scores as provided. For each measure, confirm the version/form used and apply the correct scoring algorithm and severity-band table.

2. **Build the score table.** For each instrument administered:
   - Instrument name and version.
   - Date administered.
   - Total score.
   - Severity band (use the validated categories: PHQ-9: Minimal 0–4 / Mild 5–9 / Moderate 10–14 / Moderately Severe 15–19 / Severe 20–27; GAD-7: Minimal 0–4 / Mild 5–9 / Moderate 10–14 / Severe 15–21; PCL-5: below cutoff / probable PTSD at ≥ 31 or ≥ 33 per setting; AUDIT: Zone I 0–7 / Zone II 8–15 / Zone III 16–19 / Zone IV 20–40).
   - One-sentence clinical interpretation.

3. **Parse C-SSRS separately.** Do not table C-SSRS like a continuous scale. Instead:
   - List each ideation type endorsed (Types 1–5) with descriptors.
   - List behavior items endorsed.
   - If any Type ≥ 4 or any behavior item is endorsed, generate a SAFETY FLAG block specifying the items, the clinical urgency tier (urgent/emergent), and required disposition steps.

4. **Generate co-occurrence pattern analysis.** Identify any two-or-more-measure elevation patterns from the table below; note each pattern's clinical implication:
   - PHQ-9 ≥ 10 + GAD-7 ≥ 10: high comorbidity burden; assess which is primary.
   - PHQ-9 ≥ 10 + PCL-5 ≥ 31: probable MDD+PTSD comorbidity; treatment sequencing is non-trivial.
   - PCL-5 ≥ 31 + AUDIT Zone II+: trauma/SUD comorbidity; assess self-medication.
   - PHQ-9 Item 9 ≥ 1 + C-SSRS ideation endorsed: safety convergence; mandatory safety planning response.

5. **Draft the Screening Battery Summary section.** Format for direct insertion into a 90791/90792 note.

6. **List clinical action items.** Numbered list: what the clinician must address before session ends based on this battery, in priority order.

7. **Run verification.**

## Output Format

```
=== INTAKE SCREENING BATTERY SUMMARY ===

Client: [Initials/MRN]    Date of Service: [YYYY-MM-DD]
Measures administered: [List]    Method: [self-report / clinician-administered / digital platform]

─────────────────────────────────────────
SCORE TABLE
─────────────────────────────────────────
| Measure     | Version | Date       | Score | Severity Band          | Clinical Read                              |
|-------------|---------|------------|-------|------------------------|--------------------------------------------|
| PHQ-9       | [v]     | YYYY-MM-DD | X/27  | [Band]                 | [One sentence]                             |
| PHQ-9 Item 9| —       | YYYY-MM-DD | X/3   | [0=none / 1-3=flag]    | [Flag or negative]                         |
| GAD-7       | [v]     | YYYY-MM-DD | X/21  | [Band]                 | [One sentence]                             |
| PCL-5       | [v]     | YYYY-MM-DD | X/80  | [Below cutoff / Probable PTSD] | [One sentence]                   |
| AUDIT       | [10-item / AUDIT-C] | YYYY-MM-DD | X | Zone [I-IV]  | [One sentence]                             |
| C-SSRS      | [version] | YYYY-MM-DD | See detail below | —        | See C-SSRS block below                    |
| [Other]     | [v]     | YYYY-MM-DD | X     | [Band]                 | [One sentence]                             |

─────────────────────────────────────────
C-SSRS ITEM-LEVEL DETAIL
─────────────────────────────────────────
Ideation:
  Type 1 — Wish to be dead:            [Yes / No]
  Type 2 — Active ideation, no plan:   [Yes / No]
  Type 3 — Active ideation, method:    [Yes / No]
  Type 4 — Active ideation, plan:      [Yes / No] ← SAFETY FLAG if Yes
  Type 5 — Active ideation, intent:    [Yes / No] ← SAFETY FLAG if Yes

Highest ideation type endorsed: [None / Type X]
Intensity items completed: [Yes / No — if Type > 0]
  Frequency: [X times per day/week]
  Duration: [fleeting / < 1 hr / > 1 hr / continuous]
  Controllability: [easily / somewhat / not at all]
  Deterrents: [Yes / None identified]
  Reason: [clinician input required]

Behavior items:
  Preparatory behavior:                [Yes / No]
  Interrupted attempt:                 [Yes / No]
  Aborted attempt:                     [Yes / No]
  Actual attempt (since last visit / lifetime): [Yes / No — specify]
  Most recent attempt: [date if known]    Medical lethality: [None / Low / Moderate / High]

⚠️ SAFETY FLAG: [Generated only if Type 4/5 endorsed or behavior item endorsed]
  Items endorsed: [List]
  Urgency tier: [Urgent — address before session ends / Emergent — ED/crisis level evaluation now]
  Required disposition: [Safety plan / Higher LOC evaluation / Emergency contact / Mandated action]

─────────────────────────────────────────
CO-OCCURRENCE PATTERN ANALYSIS
─────────────────────────────────────────
[Pattern 1]: [Instruments elevated] — Implication: [...]
[Pattern 2]: [Instruments elevated] — Implication: [...]
[None identified if no co-elevation]

─────────────────────────────────────────
SCREENING VS. DIAGNOSIS NOTE
─────────────────────────────────────────
These scores identify probable clinical-range presentations. DSM-5-TR diagnoses require
clinical interview applying full diagnostic criteria. Elevated scores increase pre-test
probability for the corresponding diagnosis and should guide interview focus.

─────────────────────────────────────────
CLINICAL ACTION ITEMS (priority order)
─────────────────────────────────────────
1. [Highest priority — safety items first]
2. [...]
3. [...]

─────────────────────────────────────────
MISSING INSTRUMENTS
─────────────────────────────────────────
[Instrument not administered] — Consider adding because: [clinical rationale].

─────────────────────────────────────────
BILLING NOTE
─────────────────────────────────────────
Screening battery interpreted as part of CPT 90791/90792. Scores documented in record.
Outcome measures to be re-administered per measurement-based care schedule: [frequency].
```

## Verification

- [ ] Every administered measure appears in the score table with version, date, score, validated severity band, and one-sentence interpretation.
- [ ] Severity bands match the published validation cutoffs for each instrument (not generic high/medium/low labels).
- [ ] C-SSRS is documented at the item level, not as a single total score.
- [ ] PHQ-9 Item 9 is called out separately from the total score.
- [ ] Any C-SSRS Type 4 or 5 endorsement or behavior-item endorsement generates a SAFETY FLAG with urgency and disposition.
- [ ] Co-occurrence patterns section is present (even if "None identified").
- [ ] Screening vs. diagnosis caveat is included.
- [ ] Missing instruments are flagged with rationale for consideration.
- [ ] Billing note references CPT 90791 or 90792 correctly.
- [ ] No diagnosis is assigned from screening scores alone.
- [ ] No scores are fabricated; gaps carry `[clinician input required]`.
