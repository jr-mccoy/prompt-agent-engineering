---
title: "MRI Brain Report Interpretation"
category: domain-healthcare-clinical/interpretation
description: "Read an MRI brain report sequence by sequence (DWI/ADC, FLAIR, SWI, contrast) to classify lesions — infarct, demyelination, mass, infection, microbleeds — and commit to diagnosis-specific next steps."
techniques:
  - ST-02
  - ST-03
  - CM-01
  - RT-02
  - RT-05
difficulty: advanced
tags:
  - neurology
  - radiology
  - mri-brain
  - multiple-sclerosis
  - interpretation
  - scan-shows-lesions
  - new-neurologic-deficit
  - incidental-scan-finding
updated: "2026-09-24"
related_prompts:
  - domain-healthcare-clinical/prompts/interpretation/interp_ct_head.md
  - domain-healthcare-clinical/prompts/acute-care/acute_stroke_tpa_thrombectomy.md
  - domain-medical-education/learner-foundational-sciences/study_neuroanatomy_lesion_localization_drill.md
---

## Objective

Read an MRI brain report in clinical context and produce a structured impression: what each sequence shows, what lesion class the pattern indicates, whether criteria for a specific diagnosis are met, and the concrete next step (treatment, biopsy, LP, antibody testing, follow-up interval). Input is the report or structured findings, not images.

Decision support for a licensed clinician: confirm doses, gadolinium decisions in renal impairment, and diagnostic criteria against the current guideline and local protocol. A patient with an acute neurologic emergency is escalated now, not after this output.

## When to Use

- An MRI brain (± orbits, MRA/MRV) report is back and you need a committed lesion class and next step.
- Deciding whether white-matter lesions meet MS dissemination criteria or are non-specific.
- Separating ring-enhancing lesions (abscess, metastasis, glioma, lymphoma, demyelination) before biopsy or steroids.
- Deciding which incidental findings need no follow-up.

**Not this prompt if:**
- The study is a non-contrast CT head, CTA, or CT perfusion — use `domain-healthcare-clinical/prompts/interpretation/interp_ct_head.md`.
- The live question is acute reperfusion eligibility and dosing — use `domain-healthcare-clinical/prompts/acute-care/acute_stroke_tpa_thrombectomy.md`.
- The result in hand is a lumbar puncture — use `domain-healthcare-clinical/prompts/interpretation/interp_csf.md`.

## Inputs

- MRI report: sequences performed (T1, T2, FLAIR, DWI/ADC, SWI/GRE, post-gadolinium T1, MRA/MRV, perfusion, spectroscopy), findings, impression, comparison
- Presentation: tempo (hyperacute, subacute, chronic, relapsing), focal deficits, seizures, headache, fever, cognitive change, visual symptoms
- Age, immune status (HIV, transplant, chemotherapy), cancer history, vascular risk factors
- Steroid exposure before imaging, eGFR (gadolinium), prior MRI

## Role

Senior neurology attending (with neuroradiology fluency) supporting the treating clinician; reads the MRI report alongside them and commits to an impression they can verify.

## Reasoning Steps

1. **Sequence inventory.** Name what was done and what was not. No contrast → cannot characterize enhancement (tumor, abscess, active demyelination). No SWI/GRE → microbleeds and calcification not assessed. No MRV → venous sinus thrombosis not excluded.

   **Stop and escalate now if:** acute infarct in a patient still within a reperfusion window or with a suspected large-vessel/basilar occlusion (stroke team); hemorrhage, mass, or edema with midline shift, herniation, or hydrocephalus (neurosurgery); suspected abscess, encephalitis, or venous sinus thrombosis with falling consciousness or seizures. Act on these before completing the routine read.

2. **Diffusion.** True restriction = bright DWI + dark ADC: acute infarct, pyogenic abscess (central), highly cellular tumor (lymphoma), CJD (cortical ribboning, basal ganglia), epidermoid. Bright DWI + bright ADC = T2 shine-through, not restriction. For stroke: DWI-positive/FLAIR-negative mismatch suggests onset within ~4.5 hours in wake-up stroke — route to the thrombolysis pathway.

3. **Enhancement pattern.**
   - **Ring-enhancing:** metastasis (grey–white junction, multiple, edema out of proportion), abscess (thin smooth ring, restricted center), glioblastoma (thick irregular ring, necrosis, crosses corpus callosum), tumefactive demyelination (incomplete/open ring), subacute infarct, radiation necrosis, toxoplasmosis (immunocompromised, basal ganglia).
   - **Homogeneous periventricular enhancing mass with restricted diffusion** → primary CNS lymphoma: withhold steroids until biopsy.
   - **Meningeal:** smooth dural (pachymeningeal) → intracranial hypotension, post-surgery, IgG4, dural metastasis; leptomeningeal (sulcal, cranial nerves) → bacterial/TB/fungal meningitis, carcinomatosis, sarcoid.

4. **White matter lesions.**
   - **MS pattern:** ovoid periventricular lesions perpendicular to ventricles, juxtacortical/cortical, infratentorial, spinal cord. Current McDonald criteria (2017; a later revision adds the optic nerve as a dissemination-in-space region — [VERIFY] which revision applies): dissemination in space = ≥1 T2 lesion in ≥2 of 4 regions (periventricular, cortical/juxtacortical, infratentorial, spinal cord). Dissemination in time = simultaneous enhancing and non-enhancing lesions, a new lesion on follow-up, or CSF-specific oligoclonal bands.
   - **Small-vessel ischemic disease:** punctate/confluent deep and periventricular caps, spares U-fibers and corpus callosum, age and vascular-risk appropriate.
   - **Other:** PRES (posterior parieto-occipital vasogenic edema, BP/immunosuppressant/eclampsia), PML (asymmetric, non-enhancing, U-fiber involvement, immunosuppressed/natalizumab), ADEM (large, bilateral, post-infectious, often children), NMOSD (area postrema, periependymal, long cord lesions), MOGAD.

5. **SWI/GRE.** Lobar/cortical microbleeds and superficial siderosis → cerebral amyloid angiopathy (anticoagulation and antiplatelet risk shifts); deep microbleeds → hypertensive arteriopathy; grey–white junction microbleeds after trauma → diffuse axonal injury.

6. **Specific-pattern checks.** Mammillary bodies/medial thalami/periaqueductal → Wernicke (thiamine now). Mesial temporal FLAIR hyperintensity → HSV encephalitis (acyclovir) vs autoimmune limbic encephalitis. Hippocampal sclerosis in epilepsy. Pituitary: microadenoma <10 mm, macroadenoma ≥10 mm (chiasm compression → visual fields).

7. **Incidentals that do not need chasing.** Pineal cyst, arachnoid cyst, developmental venous anomaly, enlarged perivascular spaces, small stable meningioma in an older adult — name them as benign so the patient is not re-imaged indefinitely.

8. **Pitfalls before signing.** Steroids before biopsy can make lymphoma vanish. Non-specific white matter hyperintensities in migraine or vascular-risk patients are over-called as MS — require the typical distribution and clinical syndrome. DWI can be negative in small early brainstem infarcts. Gadolinium in severe CKD: group II agents carry very low NSF risk but document the decision. Always exclude mimics before labeling MS.

## Output Format

```
SEQUENCES: [performed; key omissions]
DWI/ADC: [true restriction vs shine-through; location]
FLAIR/T2: [lesion distribution and morphology]
SWI/GRE: [microbleeds pattern, siderosis]
ENHANCEMENT: [pattern, meningeal involvement]
VESSELS/VENOUS: [MRA/MRV findings if done]

PATTERN: [infarct / demyelination / neoplasm / infection / vascular / toxic-metabolic]
CRITERIA: [e.g., McDonald DIS/DIT met or not]

IMPRESSION:
1. [diagnosis or leading differential] — [action with doses]
2. [next] — [action]
3. [incidental] — [no follow-up / interval]
```

## Verification

- [ ] Stop-and-escalate triggers (infarct in window, mass effect/herniation, hydrocephalus, abscess/encephalitis, venous thrombosis) addressed before the routine read.
- [ ] Every sequence conclusion traced to a stated finding; missing sequences (no contrast, no SWI, no MRV) named as limits, not read as negative.
- [ ] Diagnostic criteria (McDonald DIS/DIT) applied region by region and attributed to the named criteria and revision.
- [ ] Steroid timing checked against a possible lymphoma before any steroid recommendation.
- [ ] Doses and gadolinium use checked against weight and eGFR; each dose confirmed against the current guideline.
- [ ] States what would change the impression (antibody results, spinal imaging, biopsy, follow-up MRI).

## False-Positive Prevention

- **T2 shine-through read as restriction:** bright DWI counts only with dark ADC.
- **Non-specific white-matter hyperintensities over-called as MS** in migraine, vascular-risk, or older patients — require typical distribution plus a compatible clinical syndrome.
- **Ring enhancement assumed to be tumor** when abscess, tumefactive demyelination, or subacute infarct fits the diffusion and tempo better.
- **Incidentals named as cause:** pineal cyst, DVA, perivascular spaces, or a small stable meningioma blamed for the presenting symptom.

## Worked Example

**Input:** 34 y/o F, 4 days of blurred vision in the left eye with pain on eye movement. Six months ago had 2 weeks of right-leg numbness that resolved. Exam: left RAPD, visual acuity 20/80 OS. MRI brain and orbits with/without gadolinium: "Nine T2/FLAIR hyperintense ovoid lesions: six periventricular oriented perpendicular to the lateral ventricles, two juxtacortical, one in the left middle cerebellar peduncle. One periventricular lesion enhances; the others do not. Left optic nerve T2 hyperintensity and enhancement over the intraorbital segment. No restricted diffusion. SWI unremarkable."

**Output:**

```
SEQUENCES: Full brain + orbit protocol with contrast. No spinal cord imaging yet.
DWI/ADC: No restriction.
FLAIR/T2: Periventricular (perpendicular), juxtacortical, and infratentorial lesions — typical MS distribution.
SWI/GRE: No microbleeds.
ENHANCEMENT: One enhancing periventricular lesion + non-enhancing lesions; left optic nerve enhancement (short intraorbital segment).

PATTERN: Inflammatory demyelination.
CRITERIA: Current McDonald criteria (2017; [VERIFY] which revision applies) — DIS met (periventricular, juxtacortical, infratentorial = 3 of 4 regions); the left optic nerve lesion may also count as a DIS region under the newer revision. DIT met (simultaneous enhancing and non-enhancing lesions). Two clinical attacks (prior sensory episode, current optic neuritis).

IMPRESSION:
1. Relapsing-remitting multiple sclerosis presenting with left optic neuritis.
   - Methylprednisolone 1 g IV daily × 3 days — speeds visual recovery; does not change final acuity. An oral taper is not routinely required; per treating neurologist.
   - Exclude mimics before labeling: AQP4-IgG and MOG-IgG (serum, cell-based assay), B12, HIV, treponemal antibody, ANA. Short-segment, anterior optic nerve involvement and brain lesion pattern favor MS over NMOSD/MOGAD.
   - MRI cervical and thoracic spine with contrast (baseline cord lesion burden, prognosis).
   - Before DMT: hepatitis B serologies, VZV IgG, JCV antibody, pregnancy test, CBC, LFTs, TB screen per agent.
   - Neurology MS clinic within 2–4 weeks to start a high-efficacy disease-modifying therapy given multiple lesions and early relapse.
   - Repeat MRI brain with contrast at ~6 months as new baseline after DMT start.
2. No incidental findings requiring follow-up.
```
