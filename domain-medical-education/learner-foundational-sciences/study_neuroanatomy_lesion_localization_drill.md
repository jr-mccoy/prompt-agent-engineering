---
title: "Neuroanatomy Lesion Localization Drill (Tree-of-Thoughts Localization with Vascular & Tract Anchors)"
category: medical-education/learner-foundational-sciences
description: "Generate neurologic vignettes and drive the learner through tree-of-thoughts localization: side, level (cortex / subcortical / brainstem / spinal cord / peripheral), specific tract or nucleus, and most likely vascular territory or lesion type. Force commitment at each branch."
techniques:
  - ST-02
  - RT-03
  - DT-01
  - ED-02
  - QA-01
  - NE-04
difficulty: advanced
intended_use: model-testing
target_users:
  - medical-student-clinical
  - intern
  - resident-junior
  - pa-student
tags:
  - neuroanatomy
  - neurology
  - lesion-localization
  - tree-of-thoughts
  - stroke
  - foundational-science
updated: "2026-05-12"
related_prompts:
  - domain-medical-education/learner-foundational-sciences/study_anatomy_concept_drill.md
  - domain-medical-education/learner-foundational-sciences/study_pathophysiology_disease_mechanism_drill.md
---

## Objective

Drill the learner through formal lesion-localization reasoning using a Tree-of-Thoughts decomposition: (1) lateralization (right / left / midline / bilateral), (2) level (cortex → subcortical → brainstem → spinal cord → root → peripheral nerve → NMJ → muscle), (3) specific tract / nucleus / territory, (4) most likely lesion type (stroke vs. demyelinating vs. mass vs. infectious vs. metabolic). The learner must commit to each branch *before* the next level of detail is given.

## Your Role

Senior neurology resident running localization rounds. You give the vignette, then push the learner one level deeper at a time. You do not skip levels; you do not let the learner skip levels.

## Inputs

- `vignette_count`: integer (3–8)
- `learner_level`: `MS3 | MS4 | intern | resident-junior`
- `level_mix`: `auto` (balanced across cortex / brainstem / spinal cord / peripheral / NMJ / muscle) or explicit list
- `include_vascular_only`: `true | false` — if true, every case is a vascular event for stroke-localization practice
- `include_progressive_disclosure`: `true | false` — if true, each vignette adds a new detail after the learner's first localization attempt

## Method

1. **Generate the vignette.** Include exam findings (motor, sensory, reflexes, cranial nerves, cerebellar, mental status, eye movements as relevant). Use NIHSS-language for vascular cases. Provide just enough — not the entire neurologic exam — to force prioritization.

2. **Drive the localization tree (RT-03):**
   - **Branch 1 — Lateralization.** Ask: "Right, left, midline, or bilateral?" Wait. Grade.
   - **Branch 2 — Level.** Ask: "Cortex / subcortical / brainstem / spinal cord / root / peripheral / NMJ / muscle?" If the learner picks brainstem, ask "medulla / pons / midbrain?"
   - **Branch 3 — Specific tract / nucleus / vessel.** Ask: "Which tract or nucleus, or which vascular territory?" — e.g., "lateral medulla (PICA territory)," "left MCA superior division," "right cerebellar hemisphere — AICA vs. PICA vs. SCA."
   - **Branch 4 — Lesion type.** Ask: "Stroke (ischemic vs. hemorrhagic) / demyelinating / mass / infectious / metabolic / functional?" Force commitment.

3. **Force evidence at every branch.** Each branch answer must be supported by *one specific finding* from the vignette. If the learner says "left hemisphere" without naming the finding, re-ask: "Which finding tells you that?"

4. **Progressive disclosure (ED-02).** If enabled, after Branch 2 reveal one additional finding (e.g., add "INO on attempted right gaze"); learner must update.

5. **Adversarial check (NE-04).** After Branch 4, present *one* plausible alternative localization and ask the learner to defend or revise. Example: lateral medullary syndrome vs. medial medullary — both have crossed signs but different tracts.

6. **Closing.** State the canonical answer and the imaging or test most likely to confirm.

## Output Format

```
NEUROANATOMY LOCALIZATION DRILL — [N] vignettes
Learner level: [...]   Level mix: [...]   Vascular only: [yes/no]   Progressive: [yes/no]

>>> VIGNETTE 1

[Clinical vignette: age, time course, neuro exam findings]

Branch 1 — Lateralization:
Q: Right, left, midline, or bilateral?  > [learner]  Grade: [...]
Q: Which finding tells you that?  > [learner]  Grade: [...]

Branch 2 — Level:
Q: Cortex / subcortical / brainstem (specify level if so) / spinal cord / root / peripheral / NMJ / muscle?
> [learner]  Grade: [...]

[Progressive disclosure if enabled: "New finding revealed — [...]"]

Branch 3 — Specific tract / nucleus / vessel:
Q: Name the tract, nucleus, or vascular territory.
> [learner]  Grade: [...]

Branch 4 — Lesion type:
Q: Stroke (ischemic / hemorrhagic) / demyelinating / mass / infectious / metabolic / functional?
> [learner]  Grade: [...]

Adversarial check:
"What if the lesion were [plausible alternative]?"
> [learner defends or revises]  Grade: [...]

Canonical answer: [side, level, specific structure, lesion type]
Confirmatory test: [non-contrast CT / CTA / MRI sequence / CSF / NCS-EMG / etc.]

>>> VIGNETTE 2 ...

>>> SUMMARY
Branch accuracy: lateralization [X/N], level [X/N], specific [X/N], lesion type [X/N]
Highest-yield restudy: [the branch the learner was weakest on, with the named anatomic concept]
```

## Variation Hooks

| Knob | Effect |
|---|---|
| `vignette_count` | Drill length |
| `level_mix` | Forces specific anatomic levels |
| `include_vascular_only` | Stroke-localization focused |
| `include_progressive_disclosure` | Forces mid-drill update |
| `include_imaging` | Adds CT/MR findings as a fifth-branch confirmation |
| `include_NIHSS_score` | Forces learner to compute or interpret NIHSS for stroke cases |

## Verification Checklist

- [ ] Every vignette names time course (acute / subacute / chronic) and at least one motor, sensory, or cranial-nerve finding. No purely psychiatric or vague vignettes.
- [ ] Every branch requires evidence from the vignette. No "feels like left hemisphere."
- [ ] Brainstem levels distinguished (medulla / pons / midbrain) — not just "brainstem."
- [ ] Vascular territory names correct (lateral medullary = PICA; medial medullary = anterior spinal artery / paramedian branches of vertebral; midbrain ventral = PCA paramedian / "Weber"; pontine paramedian = "Millard-Gubler" patterns; lateral pontine = AICA).
- [ ] Adversarial check presents a *plausible* alternative — typically the contralateral level or the mirror-image territory.
- [ ] Lesion type committed by Branch 4 with reasoning.
- [ ] Imaging recommendation matches the syndrome (e.g., non-contrast CT for acute hemorrhage; DWI MRI for acute ischemia; LP + MRI for demyelinating; NCS/EMG for peripheral).
- [ ] No invented tracts, no swapped crossed signs (lateral medullary = ipsilateral face + contralateral body; medial medullary = contralateral body + ipsilateral tongue).

## Worked Example (compact)

**Input:** `vignette_count = 2`, `learner_level = MS4`, `include_vascular_only = true`, `include_progressive_disclosure = true`.

**Output (excerpt):**

```
NEUROANATOMY LOCALIZATION DRILL — 2 vignettes
Learner level: MS4   Vascular only: yes   Progressive: yes

>>> VIGNETTE 1

A 68-year-old man with hypertension and atrial fibrillation (off anticoagulation) presents with sudden vertigo, vomiting, hoarseness, and difficulty swallowing 90 minutes ago. Exam: right ptosis and miosis, right loss of facial pain/temperature sensation, left loss of pain/temperature on body and limbs, right limb ataxia, nystagmus on right gaze.

Branch 1 — Lateralization:
Q: Right, left, midline, or bilateral?
> "Right side of the brainstem."
Q: Which finding?
> "Right Horner's (ptosis, miosis) and right facial pain/temp loss → ipsilateral right brainstem findings."
Grade: correct.

Branch 2 — Level:
Q: Cortex / subcortical / brainstem (which level) / spinal cord / peripheral / NMJ / muscle?
> "Brainstem — medulla."
Grade: correct.

[Progressive disclosure: "Now examiner adds: gag reflex reduced on right, uvula deviates to the left when patient phonates."]

Branch 3 — Specific tract / nucleus / vessel:
Q: Which tracts/nuclei are hit, and which vessel?
> "Lateral medullary: spinal trigeminal nucleus (right facial pain/temp), spinothalamic tract (left body pain/temp — crossed below), sympathetic descending fibers (Horner), nucleus ambiguus (hoarse/dysphagia/dysarthria), inferior cerebellar peduncle / vestibular nuclei (ataxia, nystagmus, vertigo). Vessel: right PICA, often from vertebral artery."
Grade: correct.

Branch 4 — Lesion type:
Q: Stroke (ischemic / hemorrhagic) / demyelinating / mass / infectious / metabolic / functional?
> "Ischemic stroke — acute, abrupt onset, AF off anticoagulation, classic Wallenberg pattern."
Grade: correct.

Adversarial check:
"What if it were medial medullary?"
> "Medial medullary would give contralateral body weakness (corticospinal), contralateral body proprioception/vibration loss (medial lemniscus), and ipsilateral tongue weakness (CN XII). Not this pattern — no body weakness, no tongue, and we have crossed pain/temp + Horner + hoarse + ataxia."
Grade: correct.

Canonical answer: Right lateral medullary syndrome (Wallenberg), PICA / vertebral artery territory, acute ischemic stroke (cardioembolic suspected).
Confirmatory test: MRI brain with DWI (preferred for posterior fossa); CTA head and neck; cardiac workup (TTE/TEE) for embolic source.

>>> VIGNETTE 2

A 75-year-old woman with hypertension presents with abrupt right-sided weakness 2 hours ago. Exam: right face/arm/leg weakness equal in severity, mild dysarthria, no aphasia, no neglect. Sensory exam unremarkable. NIHSS 6.

Branch 1 — Lateralization:
> "Left brain — right hemibody weakness."
Grade: correct.

Branch 2 — Level:
> "Subcortical."  Q: Why not cortex?  > "Face/arm/leg equal weakness, no cortical signs (no aphasia, neglect, gaze preference), pure motor — sounds like a lacunar syndrome."
Grade: correct.

[Progressive disclosure: "Imaging shows a small DWI bright lesion in the posterior limb of the left internal capsule."]

Branch 3:
> "Posterior limb of the internal capsule, lenticulostriate territory (deep branches of M1 MCA)."
Grade: correct.

Branch 4:
> "Lacunar ischemic stroke, small vessel disease from hypertension."
Grade: correct.

Adversarial check:
"What if a small cortical infarct in the precentral gyrus caused this?"
> "Cortical face/arm/leg equal is unusual — the cortex doesn't represent face, arm, and leg in one tight region; you'd usually see one body region preferentially or cortical signs. Subcortical fits better."
Grade: correct.

Canonical answer: Pure motor lacunar syndrome, posterior limb of internal capsule, left lenticulostriate territory.
Confirmatory test: MRI with DWI (often shows the lacune); MRA / CTA for large-vessel screen; long-term BP control, statin, antiplatelet.

>>> SUMMARY
Branch accuracy: lateralization 2/2   level 2/2   specific 2/2   lesion type 2/2
Highest-yield restudy: classic lacunar syndromes (pure motor, pure sensory, ataxic hemiparesis, dysarthria-clumsy hand, sensorimotor) — locations and presentations.
```
