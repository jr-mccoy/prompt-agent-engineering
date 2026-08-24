---
title: "PANCE / PANRE Pearl Drill — One Topic, Five Locked Pearl Shapes"
category: medical-education/learner-boards
difficulty: intermediate
intended_use: model-testing
description: "Drill a PANCE/PANRE high-yield topic by producing exactly five pearls in five locked shapes (epidemiology anchor, classic presentation, dead-giveaway lab/imaging, first-line management, board trap). Then deliver one PANCE-style vignette with answer and teardown."
techniques:
  - ST-02
  - ST-03
  - DS-29
  - NE-04
  - QA-01
  - CM-02
target_users:
  - pa-student
tags:
  - boards
  - pance
  - panre
  - pearls
  - high-yield
  - learner-tool
updated: "2026-05-12"
related_prompts:
  - domain-medical-education/learner-boards/boards_usmle_step2ck_vignette_drill.md
  - domain-medical-education/learner-boards/boards_high_yield_topic_blitz.md
  - domain-medical-education/learner-boards/boards_explain_this_answer.md
  - domain-medical-education/learner-clinical-reasoning/reason_clinical_pearl_extraction.md
---

## Objective

Produce a one-page PANCE/PANRE pearl card for a single topic, structured as exactly five pearls in five locked shapes. Then deliver one PANCE-style vignette + 4 options + teardown. End state: a card the learner can store and use as a board-day quick-recall.

## Your Role

PANCE tutor. You build the pearl card, deliver the vignette, wait for the answer, and teach.

## Inputs

- `topic`: free text (e.g., "Lyme disease early-localized," "acute pericarditis," "diverticulitis uncomplicated," "TIA per ABCD2," "preeclampsia with severe features")
- `learner_level`: `pa-student-didactic | pa-student-clinical | pa-student-board-prep | recertifying-PA`
- `phase`: `didactic | clinical-rotations | dedicated | PANRE-recert`
- `task_area`: optional — `cardiology | pulmonary | GI | renal | endocrine | infectious | neuro | psych | derm | musculoskeletal | reproductive | EENT | heme/onc | pediatrics`
- `depth`: `core` (must-know for board) | `extended` (adds outpatient management plus return-precautions detail)

## Method

1. **Lock the topic (CM-02).** One-line anchor + the single PANCE-testable fact.

2. **Five pearls in five locked shapes (DS-29 pattern, ST-03 format).** No skipping, no merging:
   - **Pearl 1 — Epidemiology anchor:** age band, sex skew, risk factors that almost always appear in PANCE stems for this topic (one sentence).
   - **Pearl 2 — Classic presentation:** the *exact* triad / pentad / phrase set that PANCE uses (one sentence; quote-style).
   - **Pearl 3 — Dead-giveaway lab/imaging:** the *one* finding that locks the dx in a board stem (one line).
   - **Pearl 4 — First-line management:** drug name, dose where relevant (or "and dosing"), and disposition (one line).
   - **Pearl 5 — Board trap:** the single most common distractor on this topic — what it looks like, and the swing feature.

3. **PANCE-style vignette + 4 options.** Build a 4–8-line stem in PANCE shape (focused HPI, exam, key lab/imaging). Lead-in is usually "most likely diagnosis," "best initial step," or "best next test." Distractors include the board-trap from Pearl 5.

4. **Wait.** "Your answer (A/B/C/D)?"

5. **Teardown (QA-01).** State correct answer, name the discriminating feature from the stem, walk each distractor by named condition, and tie the answer back to Pearl 3 or Pearl 4.

## Output Format

```
PANCE PEARL CARD — [topic]
Level: [...]   Phase: [...]   Task area: [...]   Depth: [...]

>>> ANCHOR

[one-line topic anchor]
Single PANCE-testable fact: [...]

>>> FIVE PEARLS

[1] Epidemiology anchor:   [...]
[2] Classic presentation:  "[exact PANCE phrasing]"
[3] Dead-giveaway:          [the one finding]
[4] First-line management: [drug + dose + disposition]
[5] Board trap:             [the look-alike + the swing feature]

>>> PANCE-STYLE VIGNETTE

[Stem, 4–8 lines]

[Lead-in]

A) [...]
B) [...]
C) [...]
D) [...]

>>> Your answer (A/B/C/D)?

>>> TEARDOWN (after answer)

Correct answer: [letter]
Discriminating feature: "[quote from stem]"
Anchor pearl: [#3 or #4]

A) [right/wrong + named condition or pearl-trap reference]
B) [...]
C) [...]
D) [...]

Trap audit: [name the failure mode]
```

## Variation Hooks

| Knob | Effect |
|---|---|
| `topic` | The topic |
| `learner_level` | PA-student / recert |
| `phase` | didactic / clinical / dedicated / PANRE |
| `task_area` | One of the PANCE task areas |
| `depth` | core / extended |
| `forced_distractor_topic` | Override default board trap |
| `paired_vignette` | Run two stems on the same topic, different lead-ins |

## Verification Checklist

- [ ] All five pearl shapes present in order; none skipped or merged.
- [ ] Classic presentation uses *PANCE-style language*, not paraphrase.
- [ ] Dead-giveaway is *one* finding, not a list.
- [ ] First-line management names a drug (and dose where standard) or named procedure.
- [ ] Board trap names a *neighbor condition* + a *swing feature*, not a vague warning.
- [ ] Vignette stem is PANCE-style: focused HPI + exam + key data.
- [ ] Distractors each represent a real condition's correct answer.
- [ ] Discriminating feature is a verbatim quote from stem.
- [ ] No invented drugs, doses, or specificity claims.
- [ ] Card fits on one screen.

## Worked Example (compact)

**Input:** topic = `early-localized Lyme disease`, learner_level = `pa-student-clinical`, phase = `dedicated`, task_area = `infectious`, depth = `core`.

**Output (excerpt):**

```
PANCE PEARL CARD — Early-localized Lyme disease (Borrelia burgdorferi)

>>> ANCHOR

Early-localized Lyme = erythema migrans (EM) ± low-grade systemic symptoms within ~3–30 days of tick bite in endemic area.
Single PANCE-testable fact: treat clinically based on EM in endemic area — serology not required at this stage.

>>> FIVE PEARLS

[1] Epidemiology anchor: northeast / upper midwest / Pacific NW US in late spring–early fall; outdoor exposure (camping, hiking, yard work). Endemic-area exposure is in every PANCE stem.
[2] Classic presentation: "expanding annular erythematous lesion with central clearing, > 5 cm in diameter, ± malaise, fatigue, myalgia, low-grade fever" (target lesion).
[3] Dead-giveaway: EM lesion in endemic area within 3–30 days of outdoor exposure. Serology has high false-negative in this window and is NOT required.
[4] First-line management: doxycycline 100 mg po BID × 10 days (adults, non-pregnant, ≥ 8yo). Pregnancy or < 8yo: amoxicillin or cefuroxime.
[5] Board trap: serology-first ("send ELISA before treating"). EM in endemic exposure = clinical diagnosis; serology delays treatment and is often falsely negative early.

>>> PANCE-STYLE VIGNETTE

A 34-year-old hiker returns from a camping trip in Connecticut and presents with a 6-cm expanding red rash with central clearing on her right thigh, noted 8 days ago. She reports mild fatigue and myalgias. Vitals are normal. Examination shows the rash as described; no joint effusion, no neurologic deficit, no facial weakness.

Which of the following is the most appropriate next step?

A) Send Lyme ELISA and await results before treatment
B) Doxycycline 100 mg PO twice daily for 10 days
C) Topical hydrocortisone and ID referral
D) Ceftriaxone 2 g IV daily for 14 days

>>> Your answer (A/B/C/D)?

[on answer "B"]

>>> TEARDOWN

Correct: B
Discriminating feature: "6-cm expanding red rash with central clearing ... camping trip in Connecticut ... 8 days ago" — EM in endemic-area exposure within the 3–30-day window. Clinical diagnosis.
Anchor pearl: #4 (first-line management).

A) Wrong — serology delays treatment and has high false-negative rate at this stage. Classic PANCE trap (Pearl #5).
B) Correct.
C) Wrong — represents a missed diagnosis treated as contact dermatitis.
D) Wrong — IV ceftriaxone is reserved for early-disseminated (carditis with high-grade AV block, neurologic Lyme, late Lyme arthritis refractory to po). Overshoot.

Trap audit: option A is the engineered serology-first trap; the failure mode is treating early-localized Lyme like a laboratory-confirmed diagnosis. PANCE rewards clinical diagnosis in the EM scenario.
```
