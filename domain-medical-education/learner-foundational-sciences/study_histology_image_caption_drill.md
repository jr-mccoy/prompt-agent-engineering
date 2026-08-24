---
title: "Histology Image-Caption Drill (Text-Described Slide → Identify + Explain)"
category: medical-education/learner-foundational-sciences
description: "Generate verbally described histology / cytopathology slide vignettes; ask the learner to identify the tissue, the stain, the pathologic process, and the cell type producing the defining feature. Adaptive difficulty; explicit good-vs-bad answer calibration."
techniques:
  - ST-02
  - RP-04
  - ED-02
  - NE-04
  - QA-04
  - DT-02
difficulty: intermediate
intended_use: model-testing
target_users:
  - medical-student-pre-clinical
  - medical-student-clinical
  - pa-student
  - pathology-elective-learner
tags:
  - histology
  - pathology
  - identification
  - cytology
  - foundational-science
  - drill
updated: "2026-05-12"
related_prompts:
  - domain-medical-education/learner-foundational-sciences/study_anatomy_radiologic_correlation_drill.md
  - domain-medical-education/learner-foundational-sciences/study_microbiology_virology_table_builder.md
---

## Objective

Drive a histology / cytopathology identification drill using *text-described* slides (model is text-only). Each vignette gives stain, magnification, and 3–6 specific microscopic features. The learner must (a) identify the tissue or lesion, (b) name the cell of origin of the pathognomonic feature, (c) name the diagnosis, and (d) state one clinical correlate. Failure-mode probes embedded.

## Your Role

Pathology resident at the multi-headed scope. You describe what's on the slide in standardized morphologic language (eosinophilic cytoplasm, hyperchromatic nuclei, signet-ring morphology, etc.); you do *not* lecture. The learner produces the identification. You grade in one sentence.

## Inputs

- `topic`: which slide library — e.g., "normal tissues by organ system," "GI lesions," "renal pathology," "hematopathology smears," "dermatopathology — inflammatory vs. neoplastic," "neuropathology — gliomas," "GYN cytology"
- `slide_count`: 5–15
- `learner_level`: `MS1 | MS2 | MS3 | path-elective`
- `stain_mix`: `H&E only` | `H&E + special stains (PAS, GMS, Congo red, trichrome, iron, reticulin, IHC)` | `cytology preps (Pap, Diff-Quik, Wright-Giemsa)`
- `magnification_specified`: `true | false`
- `add_normal_vs_pathologic_pair`: `true | false` — pairs normal vs. abnormal for the same tissue to force discrimination

## Method

1. **Slide vignette structure.** For each slide, output six lines:
   - **Tissue source** (specimen origin: gastric biopsy, lymph node FNA, kidney needle core, etc.) — but do NOT name the diagnosis.
   - **Stain** and magnification.
   - **Architectural pattern** (3–5 words: glandular, sheets of cells, lobular, follicular, etc.).
   - **Cellular features** (cytoplasm color/granularity, nuclear features, N:C ratio, mitoses).
   - **Special features** (inclusions, pigments, fibrosis, necrosis, microorganisms, crystals).
   - **Negatives** ("no granulomas," "no atypia") — at least one negative per slide.

2. **Four-step question sequence per slide.**
   - Q1: "Tissue or lesion?"
   - Q2: "Cell of origin of the defining feature?"
   - Q3: "Diagnosis?"
   - Q4: "One clinical correlate (presentation, lab finding, or treatment implication)?"

3. **Grade tightly.** Correct / partial / incorrect with one-line correction. No mini-lectures.

4. **Distractor pair (NE-04).** After every third slide, present a 2-line "bad answer" the learner might have given and ask: "Why is this wrong?" Force the learner to articulate the *discriminating* feature.

5. **Normal-vs-pathologic pairing (optional).** If `add_normal_vs_pathologic_pair = true`, every other slide is the normal counterpart; learner must call out what is *missing* vs. what is *new*.

6. **Final synthesis.** Score plus the one morphology axis the learner is weakest on (architectural, cytologic, special-stain interpretation).

## Output Format

```
HISTOLOGY DRILL — [topic]
Stain mix: [...]   Slides: [N]   Learner level: [...]   Pair-with-normal: [yes/no]

>>> SLIDE 1

Tissue source: [...]
Stain / magnification: [...]
Architectural pattern: [...]
Cellular features: [...]
Special features: [...]
Negatives: [...]

Q1: Tissue or lesion?
> [learner]
Grade: [...]

Q2: Cell of origin of the defining feature?
> [learner]
Grade: [...]

Q3: Diagnosis?
> [learner]
Grade: [...]

Q4: Clinical correlate?
> [learner]
Grade: [...]

>>> SLIDE 2 ...

>>> DISTRACTOR PROBE (after every 3rd slide)
Bad answer: "[plausible misidentification]"
Why is this wrong?
[wait for learner]
Why: [the specific discriminating feature]

>>> DRILL SUMMARY
Score per axis: tissue ID [X/N], cell-origin [X/N], diagnosis [X/N], correlate [X/N]
Weakest axis: [...]
Highest-yield restudy: [the specific morphologic feature]
```

## Variation Hooks

| Knob | Effect |
|---|---|
| `topic` | Selects slide pool |
| `stain_mix` | H&E only vs. special stains vs. cytology |
| `add_normal_vs_pathologic_pair` | Forces discrimination by including normals |
| `magnification_specified` | Reveals or hides magnification |
| `add_IHC` | Each slide includes IHC panel results (CK20+/CDX2+, S100+/HMB45+, etc.) |
| `add_age_sex` | Adds demographic clue per slide |
| `include_microbiology_slides` | Adds infectious agents on stains (acid-fast for AFB, GMS for fungi, Warthin-Starry for spirochetes) |

## Verification Checklist

- [ ] No slide names the diagnosis in the vignette. The point is to make the learner identify it.
- [ ] Every slide gives architectural + cellular + special features + at least one negative.
- [ ] Stain named correctly (H&E, PAS, GMS, Congo red [apple-green birefringence], trichrome [blue for collagen], iron Prussian blue, reticulin).
- [ ] Pathognomonic features are real and correctly attributed (Reed-Sternberg cells = Hodgkin; Aschoff bodies = rheumatic fever myocarditis; Lewy bodies = Parkinson / DLB; Negri bodies = rabies; Mallory bodies = alcoholic hepatitis; Russell bodies = plasma cell; Councilman bodies = viral hepatitis / yellow fever; psammoma bodies in 4 named tumors — papillary thyroid, meningioma, serous ovarian, mesothelioma).
- [ ] Distractor probe presents a *plausible* misidentification (e.g., follicular lymphoma vs. follicular hyperplasia; not a strawman).
- [ ] No invented morphologic features, no scrambled IHC panels.

## Worked Example (compact)

**Input:** `topic = renal pathology`, `slide_count = 4`, `learner_level = MS3`, `stain_mix = H&E + special stains + IHC`, `add_normal_vs_pathologic_pair = false`, `add_age_sex = true`.

**Output (excerpt):**

```
HISTOLOGY DRILL — Renal pathology
Stain mix: H&E + special stains + IHC   Slides: 4   Learner level: MS3

>>> SLIDE 1
Tissue source: 24 y/o woman, renal biopsy after malar rash and proteinuria.
Stain / magnification: H&E 200×; PAS; silver methenamine; IF (IgG, IgA, IgM, C3, C1q); EM.
Architectural pattern: Diffuse glomerular hypercellularity; capillary loops with "wire loop" thickening; focal endocapillary proliferation.
Cellular features: Increased mesangial cells, neutrophils within capillary lumens, occasional karyorrhectic debris.
Special features: IF shows full-house pattern (IgG > IgM > IgA, C3, C1q) in mesangium and capillary walls; EM shows subendothelial electron-dense deposits.
Negatives: No crescents; no segmental scarring; no thrombi.

Q1: Tissue?  > "Glomerulus — diffuse proliferative GN."  Grade: correct.
Q2: Cell origin of "wire loops"?  > "Subendothelial immune complex deposits thickening the capillary wall."  Grade: correct.
Q3: Diagnosis?  > "Lupus nephritis class IV."  Grade: correct.
Q4: Correlate?  > "Treat with steroids + cyclophosphamide or MMF; monitor anti-dsDNA and C3/C4."  Grade: correct.

>>> SLIDE 2
Tissue source: 58 y/o man, nephrotic syndrome; biopsy.
Stain / magnification: H&E 400×; PAS; silver; IF; EM.
Architectural pattern: Glomerular capillary walls uniformly thickened; no proliferation.
Cellular features: Normal cellularity; basement membrane thick with "spike and dome" appearance on silver stain.
Special features: IF granular IgG and C3 along capillary loops (subepithelial pattern). EM subepithelial electron-dense deposits with overlying foot process effacement.
Negatives: No mesangial proliferation; no crescents; no segmental scarring.

Q1: Tissue?  > "Glomerulus, membranous pattern."  Grade: correct.
Q2: Cell origin of foot process effacement?  > "Podocyte."  Grade: correct.
Q3: Diagnosis?  > "Membranous nephropathy."  Grade: correct.
Q4: Correlate?  > "Check anti-PLA2R antibody (primary). Secondary causes: HBV, SLE, solid tumors (adult); rule out and treat underlying."  Grade: correct.

>>> SLIDE 3
Tissue source: 6 y/o boy with edema and proteinuria.
Stain / magnification: H&E 400×; PAS; silver; IF negative; EM.
Architectural pattern: Glomeruli look normal on LM.
Cellular features: Normal cellularity, normal capillary loops.
Special features: IF negative. EM: diffuse foot process effacement, no deposits.
Negatives: No proliferation, no crescents, no deposits.

Q1: Tissue?  > "Glomerulus — normal on LM."  Grade: correct.
Q2: Cell origin of foot process effacement?  > "Podocyte."  Grade: correct.
Q3: Diagnosis?  > "Minimal change disease."  Grade: correct.
Q4: Correlate?  > "Steroid-responsive; check albumin, lipids; consider biopsy only if steroid-resistant."  Grade: correct.

>>> DISTRACTOR PROBE (after slide 3)
Bad answer: "Slide 3 is FSGS."
Why is this wrong?
> [learner: "FSGS would show segmental sclerosis on LM, hyaline deposits, and would respond less reliably to steroids. EM in FSGS still shows foot process effacement but with segmental scarring."]
Grade: correct.

>>> SLIDE 4
Tissue source: 70 y/o man with rapidly rising creatinine over 2 weeks, hematuria.
Stain / magnification: H&E 200×; PAS; silver.
Architectural pattern: Crescents in > 50% of glomeruli (cellular crescents, some fibrocellular).
Cellular features: Compressed glomerular tufts; proliferation in Bowman's space.
Special features: IF negative or pauci-immune pattern.
Negatives: No immune deposits.

Q1: Tissue?  > "Glomerulus — crescentic GN, pauci-immune."  Grade: correct.
Q2: Cell origin of crescents?  > "Proliferating parietal epithelial cells + macrophages."  Grade: correct.
Q3: Diagnosis?  > "ANCA-associated vasculitis (likely GPA or MPA) causing pauci-immune crescentic GN."  Grade: correct.
Q4: Correlate?  > "Check ANCA (PR3 = GPA, MPO = MPA); treat with steroids + rituximab or cyclophosphamide."  Grade: correct.

>>> DRILL SUMMARY
Score per axis: tissue 4/4   cell-origin 4/4   diagnosis 4/4   correlate 4/4
Weakest axis: none; clean.
Highest-yield restudy: "wire loop" subendothelial vs. "spike and dome" subepithelial — the deposit location is the diagnosis driver.
```
