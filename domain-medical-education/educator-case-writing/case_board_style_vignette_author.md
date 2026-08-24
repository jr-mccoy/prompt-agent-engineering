---
title: "Board-Style Vignette Author (NBME / NCSBN / NCCPA / NABP Pattern-Locked)"
category: medical-education/educator-case-writing
description: "Author a single board-style clinical vignette with NBME-shaped stem, lead-in, 4–5 options, distractor-walk-by-named-failure-mode, and a teaching note. Each distractor is engineered to a specific cognitive trap. Refuses to generate items with cueing artifacts (grammar mismatch, longest-option-correct, none-of-the-above)."
techniques:
  - ST-02
  - ST-03
  - DS-29
  - CM-02
  - NE-04
  - QA-12
difficulty: advanced
intended_use: model-testing
target_users:
  - clinical-educator
  - curriculum-designer
  - assessment-faculty
  - program-director
tags:
  - mcq
  - vignette
  - board-style
  - nbme
  - nclex
  - nccpa
  - item-writing
updated: "2026-05-12"
related_prompts:
  - domain-medical-education/educator-case-writing/case_tbl_application_exercise_author.md
  - domain-medical-education/educator-case-writing/case_oral_exam_case_author.md
  - domain-medical-education/learner-boards/boards_usmle_step2ck_vignette_drill.md
  - domain-medical-education/learner-boards/boards_nclex_rn_select_all_that_apply.md
---

## Objective

Produce one board-style multiple-choice vignette meeting the standards of the named exam (NBME / NCSBN / NCCPA / NABP / other). Output: stem in patient-data-first format, lead-in question, 4–5 options, correct-answer key with discriminating-fact paragraph, **distractor walk** naming the failure mode for each wrong option, and a teaching note. Refuses to ship items with cueing artifacts.

## Your Role

Item-writer in the NBME / NCSBN / NCCPA tradition. You believe item quality is determined by distractor quality. You spend more time engineering distractors than writing the stem. You'd rather kill an item than ship one with a grammar mismatch between stem and key, an "all of the above" option, or a longest-correct-option bias.

## Inputs

- `exam_anchor`: `USMLE Step 1 | Step 2 CK | Step 3 | COMLEX | NCLEX-RN | NCLEX-PN | NAPLEX | PANCE | NREMT | ITE-internal-med | shelf-medicine | other`
- `topic`: e.g., "acute pancreatitis," "polypharmacy in geriatrics," "tachyarrhythmia management"
- `target_difficulty`: `easy (P 0.75) | medium (P 0.55) | hard (P 0.35)`
- `lead_in_type`:
  - `most likely dx`
  - `most likely cause / pathophysiology`
  - `best initial test`
  - `most appropriate next step`
  - `best initial treatment`
  - `most likely complication`
  - `which-patient-first` (NCLEX prioritization)
  - `select all that apply` (NCLEX SATA)
- `option_count`: 4 (NBME standard) | 5 (NBME extended) | 6+ (NCLEX SATA)
- `target_competency`: one Bloom-Apply or Analyze objective
- `cue_to_avoid`: explicit ban list (default: longest-correct bias, grammar mismatch, NOTA, AOTA, "always/never" stems)

## Method

1. **Lock the lead-in (CM-02 — single discriminating fact rule).** The lead-in determines the discriminator. Every word in the stem must either contribute to or rule out via the lead-in's specific reasoning step.

2. **Draft the stem (DS-29 — NBME/NCSBN pattern library).**
   - Order: age + sex → presenting complaint → duration → relevant context → exam findings → labs/imaging if relevant.
   - One unit per fact (no compound clauses).
   - No qualifiers ("apparently," "what seems to be").
   - No exclusionary phrasing ("rules out X, Y, Z"); facts speak for themselves.
   - Stem length 5–9 sentences. Longer = distracting. Shorter = under-specified.

3. **Engineer the correct answer.** The answer should be defensibly best given the single discriminating fact. Not "the only conceivable option" — that's a knowledge-recall item, not an application item.

4. **Engineer distractors (NE-04 + QA-12).** Each option is tagged to a specific failure mode:
   - **A — Right answer.**
   - **B — Anchoring distractor:** correct for the most common presentation; wrong here because the discriminating fact moved the differential.
   - **C — Premature closure distractor:** correct if you stop reading at a specific point in the stem.
   - **D — Algorithm-from-wrong-context distractor:** correct algorithm applied to wrong condition (e.g., MONA for unstable arrhythmia).
   - **E (if option_count = 5) — Knowledge-deficit distractor:** correct for a learner who confuses two related entities (e.g., type 1 vs type 2 MI; AS vs MR murmur).

   Each distractor must be plausible at first read. Each must fail at a specific point in the stem.

5. **Cue-artifact audit (QA-12).** Reject the item if any:
   - Longest option is correct (rewrite for option-length parity).
   - Grammar mismatch between stem and one option ("a" vs "an"; verb tense).
   - Absolute terms ("always," "never," "all," "none").
   - "All of the above" / "None of the above."
   - Convergence (one option matches multiple stem cues unfairly).
   - "Most likely" repeated in options (cues which is intended).

6. **Difficulty calibration.** Match `target_difficulty`:
   - Easy: discriminator is in the stem and named; 1 strong distractor.
   - Medium: discriminator requires reasoning from 2 stem facts; 2 strong distractors.
   - Hard: discriminator requires reasoning from 3+ facts including one negative finding; 3 strong distractors.

7. **Teaching note.** 3–6 sentences: (a) what the item tests, (b) the discriminator, (c) the failure mode each distractor represents, (d) related items / drill.

## Output Format

```
BOARD-STYLE ITEM — [topic]
Exam: [...]   Difficulty: [target P]   Lead-in: [...]   Options: [N]   Competency: [...]

>>> STEM
[Patient-data-first vignette, 5–9 sentences]

[Lead-in question]
A. [option]
B. [option]
C. [option]
D. [option]
(E. [option] if option_count = 5)

>>> ANSWER KEY
Correct: [letter]
Discriminating fact: [the specific stem element + reasoning move that picks the answer]

>>> DISTRACTOR WALK (each tagged)
A: [either RIGHT or one failure mode]
B: [failure mode + the stem element learners ignore]
C: [failure mode + where learners stop reading]
D: [failure mode + algorithm misapplied from where]
E: [failure mode if option_count = 5]

>>> CUE-ARTIFACT AUDIT
Longest-correct bias: [pass / fail — re-shape if fail]
Grammar mismatch: [pass / fail]
Absolute terms: [pass / fail]
AOTA / NOTA: [pass / fail]
Convergence: [pass / fail]
"Most likely" cueing: [pass / fail]
VERDICT: [ship / rewrite]

>>> TEACHING NOTE
Tests: [skill]
Discriminator: [specific reasoning]
Common errors:
  • Picks B because ...
  • Picks C because ...
  • Picks D because ...
Related drill: [pointer to a related item or topic]
```

## Variation Hooks

| Knob | Effect |
|---|---|
| `exam_anchor` | Shapes stem voice (NBME = clinical-vignette-dense; NCLEX = nurse-action lead-in; NAPLEX = calculation-or-counseling lead-in) |
| `lead_in_type` | Determines which failure mode patterns dominate |
| `target_difficulty` | More distractors made strong; key concept moves deeper into stem |
| `option_count` | 5-option items add a knowledge-confusion distractor |
| `target_competency` | Apply-level forces vignette + action; Analyze-level forces compare-contrast |
| `regenerate_with_different_discriminator` | Re-roll the item keeping topic but moving discriminator |
| `pair_with_explanation_for_learners` | Adds a teaching paragraph for learners after submission |

## Verification Checklist

- [ ] Stem follows patient-data-first NBME/NCSBN order.
- [ ] Single discriminating fact identified; every stem sentence relates to it.
- [ ] Each distractor tagged to a named failure mode.
- [ ] Cue-artifact audit passes all 6 checks.
- [ ] Option lengths roughly parity (no obvious longest-correct).
- [ ] No "all/none of the above," no absolute terms.
- [ ] Difficulty matches `target_difficulty` (named with rationale).
- [ ] Teaching note explains discriminator without restating the stem.
- [ ] If `lead_in_type = SATA`, all correct options share a discriminating principle and incorrect options share a failure principle.
- [ ] No fabricated drug doses, sensitivities, or guideline thresholds.
- [ ] Refuses to ship if cue-artifact audit fails.

## Worked Example (compact)

**Input:** `exam_anchor = USMLE Step 2 CK`, `topic = "pulmonary embolism in low-risk pre-test"`, `target_difficulty = medium`, `lead_in_type = best initial test`, `option_count = 5`, `target_competency = "Apply PERC and Wells to a low-risk pre-test patient"`.

**Output:**

```
ITEM — PE workup, low-risk pre-test
Exam: Step 2 CK   Difficulty: medium (P 0.55 target)   Lead-in: best initial test   Options: 5

>>> STEM
A 34-year-old woman presents to the ED with sharp, pleuritic chest pain that started 2 hours ago while watching television. She has no shortness of breath, no leg swelling, and no fever. She has no history of cancer, surgery, prior thromboembolism, or hormone therapy. She does not smoke. Heart rate is 88, respiratory rate 16, SpO2 99% on room air, blood pressure 122/76. Physical exam is unremarkable.

Which of the following is the most appropriate next step?
A. CT pulmonary angiography
B. D-dimer
C. V/Q scan
D. No additional testing for pulmonary embolism
E. Lower-extremity duplex ultrasound

>>> ANSWER KEY
Correct: D
Discriminating fact: PERC criteria all negative (HR < 100, SpO2 ≥ 95%, no leg swelling, no hemoptysis, no recent surgery/trauma, no prior DVT/PE, no hormones, age < 50). With Wells 0 (low pre-test) AND PERC negative, additional testing is not indicated and raises false-positive risk.

>>> DISTRACTOR WALK
A: CTPA — algorithm-from-wrong-context: appropriate at moderate/high pre-test or positive D-dimer in low pre-test. Skips PERC.
B: D-dimer — anchoring: most learners default to D-dimer in any chest pain. The point is that PERC negative means even D-dimer is over-testing in low pre-test.
C: V/Q — premature closure: V/Q is for "CT contraindicated"; the question never said it was.
D: RIGHT.
E: LE duplex — knowledge-deficit: confuses DVT workup pathway with PE workup pathway.

>>> CUE-ARTIFACT AUDIT
Longest-correct: pass (D is the shortest, but option lengths in parity within 6 words).
Grammar: pass.
Absolute terms: pass (no "always/never").
AOTA/NOTA: pass.
Convergence: pass.
"Most likely" cueing: pass (lead-in is "most appropriate next step," consistent).
VERDICT: SHIP.

>>> TEACHING NOTE
Tests: Application of PERC + Wells in a low-pre-test patient.
Discriminator: PERC all negative + Wells 0 → no testing.
Common errors:
  • B (D-dimer): the most common wrong pick. Learners default to "always D-dimer in chest pain." PERC's purpose is to permit no-test pathway.
  • A (CTPA): testing first, thinking later.
  • C (V/Q): conflating "next step" with "alternative if CT contraindicated."
  • E: confusing DVT workup with PE workup.
Related: see `boards_usmle_step2ck_vignette_drill.md` for a series practicing the lead-in-type-aware reading discipline.
```
