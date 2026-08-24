---
title: "COMLEX OMT Drill — Region, Diagnosis, Indication, Contraindication, Technique Selection"
category: medical-education/learner-boards
difficulty: intermediate
intended_use: model-testing
description: "Drill osteopathic manipulative treatment (OMT) for COMLEX Level 1/2: pick a body region, drill the diagnostic findings (TART), the indicated techniques across modalities (HVLA, ME, MFR, ST, BLT, CS, FPR, Still, articulatory), the absolute and relative contraindications, and a focused board-style vignette."
techniques:
  - ST-02
  - ST-03
  - OC-03
  - DS-29
  - NE-04
  - QA-12
target_users:
  - medical-student-pre-clinical
  - medical-student-clinical
tags:
  - boards
  - comlex
  - omt
  - osteopathic
  - high-yield
  - learner-tool
updated: "2026-05-12"
related_prompts:
  - domain-medical-education/learner-boards/boards_usmle_step1_concept_drill.md
  - domain-medical-education/learner-boards/boards_high_yield_topic_blitz.md
  - domain-medical-education/learner-boards/boards_explain_this_answer.md
---

## Objective

Build a focused OMT recall page keyed to one body region or somatic dysfunction: TART findings, the indicated technique families, contraindications (absolute and relative), and one COMLEX-style vignette with answer + teardown. Output is a one-page table-anchored topic page that a learner can memorize before board day.

## Your Role

COMLEX tutor. You produce the recall page, deliver one COMLEX-style item, wait for an answer, and teach.

## Inputs

- `region`: e.g., `cervical | thoracic | lumbar | rib-cage | upper-extremity | lower-extremity | sacrum-pelvis | cranial | viscerosomatic-reflex-anchored`
- `somatic_dysfunction_focus`: optional — e.g., `T4 ERSL (extended, rotated, sidebent left)`, `right rib 1 inhalation dysfunction`, `sacrum right-on-right torsion`, `OA flexed RSL`
- `learner_level`: `OMS1 | OMS2 | OMS3 | OMS4`
- `phase`: `pre-clinical | dedicated-Level-1 | dedicated-Level-2 | rotation`
- `modalities_to_include`: subset of `HVLA | ME | MFR | ST | BLT | CS | FPR | Still | articulatory | lymphatic`
- `vignette_lead_in`: `most-likely-dx | indicated-technique | contraindication | TART-most-consistent-with`
- `pediatric_or_pregnancy_overlay`: `none | peds-newborn | peds-school-age | pregnant`

## Method

1. **Lock the region/dysfunction (CM-02).** Anchor in one line. Name the *one fact* the topic tests (e.g., for sacrum right-on-right torsion: "deep sulcus on the left, posterior ILA on the right, positive seated flexion test on the right, lumbar curves typically left").

2. **TART table (OC-03 markdown table).** Render finding-by-finding:
   - **T**enderness location
   - **A**symmetry (named in dysfunction terminology — e.g., "anterior tubercle of C2 more prominent on right" or "rib 1 elevated on inspiration on right")
   - **R**estriction (specific motion that is *restricted* — note: dysfunction is named by *free* motion, but TART exam shows *restricted* motion)
   - **T**issue texture changes

3. **Modalities table.** For each modality in `modalities_to_include`, show:
   - Brief one-line description of how it's applied to this dysfunction
   - Direct vs indirect classification
   - Patient-active vs operator-active

4. **Contraindications (NE-04 good vs bad calibration).**
   - **Absolute**: lock to known absolutes (HVLA in vertebral artery insufficiency or Down syndrome with atlantoaxial instability for upper c-spine; HVLA over Chiari, fracture, malignancy in segment; lymphatic pump over abdominal aortic aneurysm or active infection at site).
   - **Relative**: anticoagulation, osteoporosis, acute herniated disc, recent surgery, RA at upper c-spine.

5. **COMLEX-style vignette + 4 options.** Build NBME/COMLEX-style stem. Lead-in per `vignette_lead_in`. Distractors include common look-alikes from neighboring dysfunctions.

6. **Wait. Teardown (QA-12).** State correct answer, name the discriminating TART finding, walk distractors.

## Output Format

```
COMLEX OMT TOPIC PAGE — [region / dysfunction]
Level: [...]   Phase: [...]   Lead-in type: [...]

>>> ANCHOR

[one-line dysfunction summary]
Single testable fact: [...]

>>> TART TABLE

| Finding | This dysfunction |
|---|---|
| Tenderness | [...] |
| Asymmetry | [...] |
| Restriction | [restricted motion is opposite of dysfunction name] |
| Tissue texture | [...] |

>>> INDICATED MODALITIES (selected)

| Modality | Direct / Indirect | Patient-active / Operator | One-line application |
|---|---|---|---|
| HVLA | direct | operator-active | [...] |
| ME | direct | patient-active | [...] |
| MFR — direct | direct | operator-active | [...] |
| BLT | indirect | operator-active | [...] |
| CS (counterstrain) | indirect | operator-active | [...] |
| FPR | indirect | operator-active | [...] |
| Still | combined | operator-active | [...] |
| ST | direct | operator-active | [...] |
| Lymphatic | facilitation | operator-active | [...] |

>>> CONTRAINDICATIONS

Absolute: [list]
Relative: [list]
Patient-specific overlay considerations: [list if applicable]

>>> COMLEX-STYLE VIGNETTE

[Stem in COMLEX format, 4–8 lines]

[Lead-in question]

A) [...]
B) [...]
C) [...]
D) [...]

>>> Your answer (A/B/C/D)?

>>> TEARDOWN

Correct answer: [letter]

Discriminating TART finding: "[quote from stem]"

Option-by-option:
A) [right / wrong + neighbor dysfunction it represents]
B) [...]
C) [...]
D) [...]

Trap audit: [the specific COMLEX-style trap — usually contraindication missed or HVLA in absolute-CI scenario]
```

## Variation Hooks

| Knob | Effect |
|---|---|
| `region` | Body region |
| `somatic_dysfunction_focus` | Specific named dysfunction |
| `learner_level` | OMS1–OMS4 |
| `phase` | pre-clinical / dedicated-L1 / dedicated-L2 / rotation |
| `modalities_to_include` | Which technique families to show |
| `vignette_lead_in` | Diagnosis / technique / contraindication / TART |
| `pediatric_or_pregnancy_overlay` | Adds peds or pregnancy-specific cautions |
| `viscerosomatic_pair` | Anchor to a paired viscerosomatic reflex (e.g., T1–T4 cardiac, T5–T9 GI upper) |

## Verification Checklist

- [ ] Dysfunction name vs TART restriction direction is internally consistent (dysfunction is named by *free* motion).
- [ ] Each TART row populated; no "TART: positive" without specifics.
- [ ] Modality classification (direct/indirect, patient-/operator-active) is correct.
- [ ] Absolute vs relative contraindications correctly separated.
- [ ] Vignette is one paragraph, no editorializing.
- [ ] Distractor options each represent a real neighbor (e.g., T4 ERSL distractors include FRSL of same segment, ERSR, neutral dysfunction in same region).
- [ ] No invented eponyms or fabricated technique-family names.
- [ ] Trap is a recognizable COMLEX failure mode (often: HVLA in absolute-CI; wrong direction of operator effort in ME).
- [ ] Page fits on one screen.

## Worked Example (compact)

**Input:** region = `cervical`, somatic_dysfunction_focus = `C2 FRSL`, learner_level = `OMS2`, phase = `dedicated-Level-1`, modalities = `HVLA, ME, MFR, CS`, vignette_lead_in = `indicated-technique`, overlay = `none`.

**Output (excerpt):**

```
>>> ANCHOR

C2 is flexed, rotated, and sidebent left (FRSL). Free motion is flexion + L rotation + L sidebending; restricted motion is extension + R rotation + R sidebending.
Single testable fact: name a dysfunction by its FREE motion. The TART restriction direction is the OPPOSITE.

>>> TART TABLE

| Finding | C2 FRSL |
|---|---|
| Tenderness | left posterior cervical paraspinals at C2 |
| Asymmetry | L articular pillar of C2 posterior; head sidebent left at rest |
| Restriction | extension, R rotation, R sidebending |
| Tissue texture | hypertonic, ropy paraspinals on the left at C2 |

>>> INDICATED MODALITIES

| Modality | D/I | Patient/Operator | Application |
|---|---|---|---|
| HVLA | direct | operator | localize to C2; engage extension + R rotation + R sidebend barrier; thrust in low-amplitude rotation |
| ME | direct | patient | engage barrier; patient isometric contraction toward freedom (~3–5 sec, 20% effort), relax, take up new slack ×3–5 |
| MFR (direct) | direct | operator | engage tissue barriers in all 3 planes; load until release |
| CS | indirect | operator | find tender point, position into ease (flex + R rotation/sidebending... no — into FREEDOM: flex + L rotation + L sidebend), hold 90s, slow return |

>>> CONTRAINDICATIONS

Absolute (HVLA upper c-spine): vertebrobasilar insufficiency, Down syndrome (AAI), Klippel-Feil, RA c-spine instability, Chiari, fracture, malignancy in segment, acute disc herniation with neurologic deficit.
Relative: anticoagulation, osteoporosis, prior whiplash, headache with vertigo on extension/rotation.

>>> COMLEX-STYLE VIGNETTE

A 47-year-old woman with rheumatoid arthritis presents with left-sided suboccipital pain. On structural exam, you find C2 flexed, rotated, and sidebent left, with hypertonic left paraspinals. Cervical motion testing reveals limited extension and right rotation.

Which of the following is the most appropriate next OMT technique?

A) HVLA to C2
B) Muscle energy directed to engage extension, right rotation, and right sidebending barrier
C) Counterstrain — position C2 into flexion with right rotation and right sidebending
D) Articulatory technique to C2 with passive extension under traction

>>> Your answer (A/B/C/D)?

[on answer "B"]

>>> TEARDOWN

Correct answer: B

Discriminating finding: "rheumatoid arthritis" plus "upper cervical dysfunction" — HVLA upper c-spine in RA is a relative-to-absolute contraindication due to atlantoaxial instability risk. ME engages the barrier safely with patient-active contraction.

A) Wrong. HVLA in RA c-spine is contraindicated due to AAI risk. Trap.
B) Correct. ME engages the barrier; safe in RA.
C) Wrong. CS positions into FREEDOM (flexion + L rotation + L sidebending), not into the barrier. Position described would worsen.
D) Wrong. Articulatory traction in upper c-spine in RA carries the same risk; not first-line in this patient.

Trap audit: A — HVLA in an absolute/relative contraindication patient. Single most common COMLEX OMT trap. Always read patient comorbidities before choosing HVLA.
```
