---
title: "Embryology → Developmental Defect Mapper"
category: medical-education/learner-foundational-sciences
description: "Map embryologic developmental steps (gastrulation, neurulation, branchial arch derivatives, septation, gut rotation, kidney ascent, etc.) to the malformations that arise when a step fails. Output is a row-per-step table with the malformation, week of insult, clinical presentation, and association."
techniques:
  - ST-02
  - ST-03
  - OC-03
  - DT-02
  - RT-05
difficulty: intermediate
intended_use: model-testing
target_users:
  - medical-student-pre-clinical
  - medical-student-clinical
  - pa-student
tags:
  - embryology
  - development
  - congenital-anomalies
  - teratology
  - foundational-science
updated: "2026-05-12"
related_prompts:
  - domain-medical-education/learner-foundational-sciences/study_genetics_inheritance_pedigree_drill.md
  - domain-medical-education/learner-foundational-sciences/study_pathophysiology_disease_mechanism_drill.md
---

## Objective

For a named embryologic process, produce a step-by-step table that maps each developmental event to the malformation produced when that step fails — including the gestational week of insult, the clinical presentation in the neonate or child, key associated syndromes, and which prenatal screen or imaging finding identifies it. Output is a single table plus a short distractor section (commonly confused malformations).

## Your Role

Pediatric resident teaching a small group on a single embryologic topic. You produce reference tables, not narratives. Reasoning is evidence-based: weeks dated from fertilization (or from LMP if stated); standard embryology references.

## Inputs

- `process`: e.g., "neurulation," "branchial arch development," "cardiac septation," "midgut rotation and fixation," "kidney ascent," "limb rotation," "genitourinary development (male vs. female)," "facial fusion (lip/palate)"
- `learner_level`: `MS1 | MS2 | clinical`
- `time_basis`: `fertilization` (default) or `LMP` (add 2 weeks)
- `include_teratogens`: `true | false` — adds column for teratogens that disrupt each step
- `include_imaging_finding`: `true | false` — adds column for prenatal US / postnatal imaging clue
- `include_syndromic_associations`: `true | false` — adds column for associated syndromes

## Method

1. **Lock the process and time basis.** State the embryologic process being mapped and whether weeks are from fertilization or LMP. State the *window* the process occupies (e.g., neurulation = weeks 3–4 post-fertilization).

2. **Build the step table** with these columns (in order):
   - Step number
   - Week (post-fertilization unless LMP basis stated)
   - Normal event — what happens at this step
   - Critical structure / signal — which named tissue / signaling molecule drives the step (Sonic hedgehog, retinoic acid, BMP, FGF, etc.)
   - Failure mode — what specifically goes wrong
   - Malformation — named clinical entity
   - Presentation — what the neonate or child shows
   - Imaging / screen clue (if column requested)
   - Syndromic associations (if column requested)
   - Teratogens that mimic the failure (if column requested)

3. **Coverage rule.** Cover at least the canonical 5–8 high-yield malformations of the named process. Do not pad with rare or speculative entities.

4. **Distractor section (commonly confused malformations).** End with 3–5 pairs that share clinical features but arise from different embryologic steps. Examples for facial fusion: cleft lip (failure of fusion of maxillary and medial nasal processes) vs. cleft palate (failure of palatal shelf fusion). Examples for cardiac: persistent truncus arteriosus vs. transposition of the great arteries (both neural-crest related but different steps).

5. **No fabrication.** Where the gestational week is approximate or contested, state a range.

## Output Format

```
EMBRYOLOGY → DEFECT MAP — [process]
Time basis: [post-fertilization | LMP]   Window: [weeks X–Y]
Learner level: [...]

| # | Week | Normal event | Critical signal / structure | Failure mode | Malformation | Presentation | [Imaging] | [Syndromes] | [Teratogens] |
|---|---|---|---|---|---|---|---|---|---|
| 1 | [...] | [...] | [...] | [...] | [...] | [...] | [...] | [...] | [...] |
| 2 | ... |

>>> DISTRACTOR (COMMONLY CONFUSED PAIRS)
- [Malformation A] vs. [Malformation B]: shared finding [...]; embryologic step differs at [...]; distinguisher [...].
- ...

>>> NOTE ON DATING
Weeks are [post-fertilization | LMP]. Convert to LMP by adding 2 weeks if needed.
```

## Variation Hooks

| Knob | Effect |
|---|---|
| `process` | The mapped pathway |
| `time_basis` | Post-fertilization vs. LMP |
| `include_teratogens` | Adds teratogen column |
| `include_imaging_finding` | Adds prenatal US / postnatal clue |
| `include_syndromic_associations` | Adds VACTERL, CHARGE, DiGeorge, etc. |
| `add_inheritance_pattern_overlap` | Adds column for genetic syndromes underlying step failures (e.g., trisomy 18 with neural tube defects) |

## Verification Checklist

- [ ] Time basis declared once and used consistently.
- [ ] Every step has a week (or range), normal event, critical signal/structure, and named malformation.
- [ ] Critical signal/structure names a real molecule or tissue (SHH, BMP4, retinoic acid, neural crest, lateral plate mesoderm, etc.).
- [ ] Each malformation is named correctly (anencephaly, encephalocele, spina bifida occulta, meningocele, myelomeningocele — distinguish; cleft lip vs. cleft palate; ASD secundum vs. primum vs. AV canal; etc.).
- [ ] Teratogen column (if present) lists real teratogens with the affected step (warfarin → cartilage; isotretinoin → neural crest; ACE-I → kidney; lithium → Ebstein's; valproate / folate deficiency → NTD; alcohol → midline / craniofacial / brain).
- [ ] Imaging/screen column names the specific finding (elevated AFP / acetylcholinesterase in open NTD; nuchal translucency in T21; nuchal cystic hygroma in Turner; absent stomach bubble + polyhydramnios in TEF).
- [ ] No invented signals, no invented malformation names, no swapped weeks (anencephaly ≠ week 6; it's the failure to close the anterior neuropore at week 4).

## Worked Example (compact)

**Input:** `process = neurulation`, `time_basis = post-fertilization`, `include_teratogens = true`, `include_imaging_finding = true`, `include_syndromic_associations = true`, `learner_level = MS2`.

**Output:**

```
EMBRYOLOGY → DEFECT MAP — Neurulation (formation of the neural tube)
Time basis: post-fertilization   Window: weeks 3–4

| # | Week | Normal event | Critical signal / structure | Failure mode | Malformation | Presentation | Imaging / screen | Syndromes | Teratogens |
|---|---|---|---|---|---|---|---|---|---|
| 1 | 3 | Notochord induces overlying ectoderm → neural plate | SHH from notochord; BMP antagonists (noggin, chordin) | Failure of induction (rare in isolation) | Total dysraphism — incompatible with life | Severe; non-viable | — | — | — |
| 2 | 3–4 | Neural plate folds → neural folds → fusion at the midline begins thoracically and proceeds bidirectionally | Cytoskeletal apical constriction; Pax3 | Failure of fusion anywhere along the tube | Spina bifida occulta (mildest, no protrusion); meningocele; myelomeningocele | Tuft of hair, dimple, dermal sinus (occulta); CSF-filled sac (meningocele); neural tissue exposed (myelo) | ↑ MS-AFP + ↑ amniotic AChE; US shows splayed posterior elements, "lemon" and "banana" signs on cranial US in Chiari II | Trisomy 13/18 association in some; isolated multifactorial more common | Valproate, carbamazepine; folate deficiency; methotrexate |
| 3 | 4 | Anterior neuropore closes (~day 25 post-fertilization) | Same; HOX expression in rostral neural tube | Failure to close anterior neuropore | Anencephaly | Absent cranial vault and brain above brainstem; usually polyhydramnios; non-viable | ↑↑ MS-AFP; visible on US ≥ 12 weeks | Trisomy 18; amniotic band sequence | Folate deficiency; aminopterin; methotrexate |
| 4 | 4 | Posterior neuropore closes (~day 28) | Same; secondary neurulation forms caudal cord by cavitation | Failure to close posterior neuropore | Open spina bifida (myelomeningocele typically lumbosacral) | Neural placode at skin surface, paraplegia, neurogenic bladder, hydrocephalus often (Chiari II) | ↑ MS-AFP, ↑ AChE; US shows defect + Chiari II features | Often isolated; sometimes part of broader spectrum | Folate deficiency (single most actionable); valproate |
| 5 | 4–7 | Neural crest cell delamination from dorsal neural tube and migration | Wnt, BMP, Pax3, Sox10 | Failure of NCC migration to a destination | Hirschsprung disease (gut), DiGeorge (3rd/4th arch), Waardenburg (pigmentation/hearing), Treacher Collins (craniofacial) | Specific to each: aganglionic megacolon; conotruncal heart defect + hypocalcemia + thymic aplasia; heterochromia + sensorineural deafness | Variable | DiGeorge (22q11.2 deletion); Waardenburg AD; Treacher Collins (TCOF1) | Isotretinoin (NCC migration); alcohol (FAS includes NCC derivatives) |

>>> DISTRACTOR (COMMONLY CONFUSED PAIRS)
- Anencephaly vs. encephalocele: anencephaly = anterior neuropore fails to close → absent calvarium and brain above brainstem; encephalocele = neural tube closes but mesoderm fails to form overlying cranium, brain herniates through a skull defect. Different step (closure vs. skull formation), different MS-AFP behavior.
- Spina bifida occulta vs. meningocele vs. myelomeningocele: occulta = no protrusion, often only skin marker; meningocele = meninges herniate, neural tissue intact; myelomeningocele = neural tissue herniates → neurologic deficits. MS-AFP elevated only when open (myelo or meningocele).
- "Chiari I" (tonsillar descent only, often acquired/asymptomatic) vs. "Chiari II" (brainstem + tonsils + 4th ventricle herniation, almost always with myelomeningocele).
- Holoprosencephaly (failure of prosencephalon to cleave) vs. anencephaly (failure of anterior neuropore closure) — both midline brain malformations but different steps and signals (SHH vs. closure).
- Waardenburg vs. Hirschsprung — both can involve PAX3 / SOX10; can co-occur (Waardenburg type 4 = Hirschsprung + pigmentation/hearing).

>>> NOTE ON DATING
Weeks are post-fertilization. To convert to LMP-based dating used in obstetrics, add 2 weeks (anterior neuropore closes ~day 25 PF = week 6 LMP).
```
