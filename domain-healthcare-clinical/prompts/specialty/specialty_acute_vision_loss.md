---
title: "Acute Vision Loss Assessment"
category: domain-healthcare-clinical/specialty
description: "Localize acute vision loss (media, retina, optic nerve, chiasm, retrochiasmal) by laterality, pain, and duration, identify CRAO, GCA, retinal detachment, and optic neuritis, and commit to stroke-pathway, steroid, and ophthalmology timing."
techniques:
  - ST-02
  - ST-03
  - CM-01
  - RT-02
  - RT-05
difficulty: advanced
tags:
  - ophthalmology
  - neuro-ophthalmology
  - emergency-medicine
  - specialty-assessment
  - sudden-blindness
  - curtain-over-eye
updated: "2026-09-24"
related_prompts:
  - domain-healthcare-clinical/prompts/specialty/specialty_red_eye_workup.md
  - domain-healthcare-clinical/prompts/acute-care/acute_stroke_tpa_thrombectomy.md
  - domain-medical-education/learner-foundational-sciences/study_neuroanatomy_lesion_localization_drill.md
---

## Objective

Assess a patient with sudden or rapidly progressive vision loss: establish laterality (monocular vs binocular), duration (transient vs persistent), and pain; localize the lesion along the visual pathway; identify the time-critical diagnoses (central retinal artery occlusion, giant cell arteritis, macula-on retinal detachment, acute angle closure, pituitary apoplexy, occipital stroke); and write the immediate orders and referral timing.

Decision support for a licensed clinician: confirm doses, renal/hepatic adjustment and thresholds against the current guideline and local formulary. Vision loss with a neurologic deficit, or an unstable patient, is escalated now (stroke pathway), not after this output.

## When to Use

- Sudden or rapidly progressive loss of vision in one or both eyes, transient or persistent, usually in a white, quiet eye.
- A patient over 50 with new visual symptoms plus headache, jaw pain or raised inflammatory markers (the giant cell arteritis question).
- Flashes, new floaters or a spreading curtain, where retinal detachment has to be recognized and timed.
- An ED or urgent-care consult that needs localization, immediate orders and referral timing now.

**Not this prompt if:**
- The eye is red and painful and the workup starts there → [`specialty_red_eye_workup.md`](specialty_red_eye_workup.md); most acute vision loss here presents with a white, quiet eye.
- The presentation is a hemispheric stroke in which vision is one deficit among many and the question is reperfusion → [`acute_stroke_tpa_thrombectomy.md`](../acute-care/acute_stroke_tpa_thrombectomy.md).

## Inputs

- Laterality: one eye or both — did the patient cover each eye? (Patients with homonymous hemianopia often report loss "in the eye" on the side of the field defect.)
- Onset (seconds, hours, days), duration (transient minutes vs persistent), progression, pattern (curtain, shade from above/below, central blur, whole field, floaters, flashes)
- Pain: none, periocular pain worse with eye movement, headache, jaw claudication, scalp tenderness
- Associated: diplopia, focal neuro deficits, headache severity/thunderclap, systemic symptoms (fever, weight loss, polymyalgia symptoms)
- Risk: age, vascular risk factors, AF, carotid disease, diabetes, myopia, prior cataract surgery, recent trauma, MS history, PDE5 inhibitor use, pregnancy/postpartum, pituitary tumor
- Exam: visual acuity each eye with pinhole, RAPD (swinging flashlight), color vision (Ishihara or red desaturation), confrontation fields each eye, IOP, fundus (disc, macula, vessels, hemorrhages, cherry-red spot, emboli), EOM, full neuro exam, temporal artery palpation
- Labs/imaging available: ESR, CRP, platelets, glucose, CBC, prior imaging

## Role

Senior attending neuro-ophthalmologist supporting the treating clinician on an ED consult. Localize first, then act on the time-critical diagnosis without waiting for the perfect test.

## Reasoning Steps

1. **Confirm and quantify the loss.** Visual acuity each eye with pinhole (pinhole improvement = refractive/media cause), confrontation fields each eye separately, RAPD, color. Document as a baseline — every subsequent decision references it.
   - **Stop and escalate now if:** vision loss with any focal neurologic deficit or within the stroke-treatment window (stroke code); suspected CRAO (stroke-equivalent pathway); age >50 with headache, jaw claudication or scalp tenderness (IV steroids today); thunderclap headache with ophthalmoplegia or hypotension (pituitary apoplexy); red painful eye with high IOP (angle closure). Act on these before completing the rest of the workup.

2. **Monocular or binocular.**
   - **Monocular** → lesion anterior to the chiasm: media (cornea, lens, vitreous), retina, or optic nerve.
   - **Binocular** with homonymous field defect → retrochiasmal (optic tract, radiations, occipital cortex) → treat as stroke until proven otherwise.
   - **Bitemporal** defect → chiasm (pituitary mass, apoplexy).

3. **Transient vs persistent.**
   - **Transient monocular vision loss (amaurosis fugax)**, seconds to minutes, "curtain" → retinal TIA from carotid/cardiac embolism → same-day stroke workup (MRI with DWI, carotid imaging, ECG/telemetry, echo). In patients >50, also check ESR/CRP — GCA can present with transient visual loss before permanent loss.
   - Transient visual obscurations lasting seconds with position change + headache → papilledema (IIH, mass) → fundoscopy, neuroimaging.
   - Binocular transient with scintillating positive phenomena, marching over 5–60 min → migraine aura (diagnosis of exclusion in first episode over age 50).

4. **Persistent monocular, painless — work through the fundus.**
   - **CRAO:** sudden, profound (often counting fingers or worse), RAPD, pale retina with cherry-red spot, attenuated/box-carred arterioles, occasionally visible Hollenhorst plaque. This is a stroke equivalent. Refer to a stroke center immediately (same pathway as ischemic stroke); stroke-unit admission or urgent TIA-clinic-level workup. Intravenous thrombolysis within a short window is being used at some centers but evidence is limited and practice varies — decision belongs to the local stroke team. Conservative maneuvers (ocular massage, anterior chamber paracentesis, hyperventilation) are unproven. In patients >50, check ESR/CRP/platelets for arteritic CRAO.
   - **Branch RAO:** sectoral field loss and sectoral retinal whitening — same embolic workup.
   - **CRVO:** "blood and thunder" fundus — diffuse hemorrhages, dilated tortuous veins, disc edema. Risk: HTN, glaucoma, diabetes, hyperviscosity. Ophthalmology within days; anti-VEGF for macular edema; screen for neovascularization (neovascular glaucoma).
   - **Retinal detachment:** flashes, new shower of floaters, then a curtain or shadow progressing. Macula-on (central acuity preserved) → same-day retinal surgery evaluation to save central vision. Macula-off → urgent (within days). Posterior vitreous detachment with new floaters alone still needs dilated exam within 24 h to exclude a retinal tear.
   - **Vitreous hemorrhage:** diabetic proliferative retinopathy, retinal tear, trauma; no red reflex; B-scan ultrasound to exclude detachment behind the blood.
   - **Wet AMD:** central distortion (metamorphopsia on Amsler grid), older patient → ophthalmology within 1 week for anti-VEGF.
   - **Anterior ischemic optic neuropathy:** pale or swollen disc, altitudinal field defect, RAPD.
     - **Arteritic (GCA):** age >50, headache, jaw claudication, scalp tenderness, PMR, fever/weight loss, chalky-white disc edema, very high ESR/CRP, thrombocytosis. Fellow eye can be lost within days. Start steroids immediately on clinical suspicion — do not wait for biopsy.
     - **Non-arteritic (NAION):** age 50–70, vascular risk, small crowded disc ("disc at risk") in the fellow eye, often noticed on waking (nocturnal hypotension), PDE5 inhibitor association. No proven treatment; control vascular risk, avoid nocturnal hypotension.

5. **Persistent monocular, painful.**
   - **Optic neuritis:** subacute over hours-days, pain with eye movement, reduced acuity and color vision, RAPD, central scotoma; disc normal (retrobulbar) in two-thirds. Young adult, female predominance. MRI brain and orbits with gadolinium — white matter lesions determine MS risk. Atypical features (bilateral, painless, severe, no recovery by 3 weeks, disc hemorrhage, marked disc edema, Asian or African descent) → test AQP4-IgG and MOG-IgG. Per ONTT, IV methylprednisolone 1 g daily × 3 days (then oral taper) speeds recovery without changing final acuity; oral prednisone alone at standard dose was associated with more recurrence and is avoided. NMOSD/MOGAD with severe loss → early plasma exchange discussion.
   - **Acute angle closure:** red, painful, halos, fixed mid-dilated pupil, high IOP — see red eye workup.
   - **Arteritic AION** may be painful via headache.

6. **Binocular / neurologic.**
   - **Occipital or posterior cerebral artery stroke:** homonymous hemianopia, may be macular-sparing, normal fundi and pupils → stroke code (thrombolysis/thrombectomy eligibility per stroke pathway).
   - **Pituitary apoplexy:** thunderclap headache, bitemporal loss or acuity loss, ophthalmoplegia, hypotension → MRI pituitary, stress-dose hydrocortisone 100 mg IV immediately, neurosurgery.
   - **PRES:** severe hypertension, eclampsia, immunosuppressants, cortical blindness, seizures.
   - **Papilledema with vision loss:** IIH (fulminant) or mass → neuroimaging with venography, LP opening pressure after imaging; fulminant IIH needs urgent CSF diversion.
   - **Functional vision loss:** diagnosis only after objective testing (RAPD absent, normal fundi, inconsistent fields, optokinetic response) — never the first assumption.

7. **Giant cell arteritis steroid dosing.**
   - Vision loss or amaurosis present: methylprednisolone 500–1000 mg IV daily × 3 days, then prednisone 1 mg/kg/day (commonly 60 mg).
   - No visual symptoms: prednisone 40–60 mg daily.
   - Temporal artery biopsy — segment ≥1.5 cm (per local pathology guidance) — within 1–2 weeks of starting steroids — yield persists; temporal artery ultrasound (halo sign) is an accepted alternative in experienced centers. Add aspirin per local practice; bone protection; PJP prophylaxis consideration on prolonged high-dose steroids; tocilizumab as steroid-sparing therapy is rheumatology's call.

## Output Format

```
BASELINE: VA OD/OS (pinhole) | RAPD | color | fields | IOP | fundus

LOCALIZATION: [media / retina / optic nerve / chiasm / retrochiasmal]
PATTERN: [monocular vs binocular, transient vs persistent, painful vs painless]

WORKING DIAGNOSIS: [specific]
DIFFERENTIAL: [2–3 alternatives + distinguishing finding]

TIME-CRITICAL ACTIONS (now):
- [stroke pathway activation / IV steroids / retina surgery call / IOP lowering / hydrocortisone]

WORKUP:
- Labs: [ESR, CRP, platelets, glucose, lipids, A1c, AQP4/MOG, etc.]
- Imaging: [MRI brain with DWI, MRI orbits with gad, CTA/MRA head and neck, carotid US, B-scan]
- Cardiac: [ECG, telemetry, echo]

TREATMENT: [drug, dose, route, duration]

REFERRAL / DISPOSITION: [ophthalmology/retina/neuro-ophthalmology/neurology/stroke — emergent, same day, days]

FELLOW-EYE / SECONDARY PREVENTION: [ ]

PITFALLS TO AVOID:
- [ ]
```

## Verification

- [ ] Laterality was established by covering each eye, and the localization matches the exam (RAPD, fields, fundus) rather than the patient's description alone.
- [ ] Each time-critical diagnosis (CRAO, GCA, macula-on detachment, angle closure, apoplexy, occipital stroke) is marked present or excluded, with the finding that decides it.
- [ ] In any patient over 50, ESR/CRP/platelets were obtained or GCA explicitly excluded before calling NAION or embolic disease.
- [ ] Steroid, thrombolysis and referral-timing statements name the pathway or trial used (ONTT, local stroke protocol, rheumatology/ophthalmology policy); confirm doses, renal adjustment and thresholds against the current guideline and local formulary.
- [ ] The output states what finding would change the working diagnosis (e.g., normal inflammatory markers and a crowded fellow disc → NAION).

## False-Positive Prevention

- **A normal fundus read as "nothing wrong."** A normal fundus fits retrobulbar optic neuritis, early CRAO before whitening, and occipital stroke — check RAPD and fields before reassuring or calling the loss functional.
- **A monocular complaint taken at face value.** Homonymous hemianopia is often reported as loss "in one eye"; test each eye's fields separately before localizing anterior to the chiasm.
- **A modestly raised ESR/CRP over-called as GCA — or normal values used to dismiss it.** ESR rises with age and anemia, and a minority of GCA has normal markers; weigh jaw claudication, PMR and temporal-artery findings rather than one number.
- **Pinhole-correctable blur treated as neuro-ophthalmic.** Improvement with pinhole points to refractive or media causes (cataract, cornea) — it does not need brain imaging.
- **An old fundus finding blamed for new loss.** Disc drusen, a tilted disc or old chorioretinal scars may be longstanding; compare with prior exams before attributing the acute loss to them.

## Worked Example

**Input:** 74 y/o F with 3 weeks of new bitemporal headaches, pain chewing, fatigue, morning shoulder stiffness. Woke today with loss of the lower half of vision in the left eye. Two days ago had a 5-minute episode of "graying out" in the left eye that resolved. Exam: VA OD 20/25, OS 20/200. Left RAPD. Inferior altitudinal defect OS. Fundus OS: pale, swollen disc; OD: normal disc with normal cup. Tender, nodular, pulseless left temporal artery. ESR 88, CRP 64 mg/L, platelets 520. Neuro exam otherwise normal.

**Output:**

```
BASELINE: VA OD 20/25, OS 20/200 | left RAPD | red desaturation OS | inferior altitudinal defect OS | IOP normal | OS pale disc edema; OD normal disc (not crowded)

LOCALIZATION: Left optic nerve head (anterior ischemic optic neuropathy).
PATTERN: Monocular, persistent, preceded by transient monocular loss; painless eye with headache and jaw claudication.

WORKING DIAGNOSIS: Arteritic AION from giant cell arteritis — jaw claudication, scalp/temporal artery findings, PMR symptoms, ESR 88, CRP 64, thrombocytosis, pallid disc edema, and a normal (not crowded) fellow disc.
DIFFERENTIAL:
- NAION — would expect a crowded disc at risk in the fellow eye and normal inflammatory markers; neither present.
- CRAO — no cherry-red spot; arteritic CRAO remains on the spectrum of GCA and would be managed identically.
- Compressive optic neuropathy — not acute; no.

TIME-CRITICAL ACTIONS (now):
- Methylprednisolone 1 g IV now, daily × 3 days. Do not wait for biopsy. The right eye is at risk within days.
- Admit for IV steroids and visual monitoring.

WORKUP:
- Labs: CBC, BMP, glucose, A1c baseline (steroid hyperglycemia), LFTs, QuantiFERON/hepatitis B screen if prolonged immunosuppression anticipated.
- Temporal artery biopsy within 1–2 weeks, segment ≥1.5 cm (per local pathology guidance); temporal artery ultrasound in the interim if available.
- Consider vascular imaging (CTA/MRA or PET) for large-vessel involvement if symptoms (arm claudication, bruits, BP asymmetry).

TREATMENT:
- After IV pulse: prednisone 60 mg PO daily (≈1 mg/kg), taper directed by rheumatology once symptoms and markers controlled.
- Calcium/vitamin D; bisphosphonate for bone protection on long-term high-dose steroids.
- PPI while on high-dose steroid if GI risk.
- PJP prophylaxis discussion given anticipated prolonged high-dose therapy.
- Rheumatology to decide on tocilizumab as steroid-sparing agent.

REFERRAL / DISPOSITION: Admit. Neuro-ophthalmology today; rheumatology inpatient consult; surgery/vascular for biopsy.

FELLOW-EYE / SECONDARY PREVENTION: Daily VA and fields OD during admission; instruct patient to report any transient dimming in the right eye immediately.

PITFALLS TO AVOID:
- Do not label this NAION because the patient is vascular-aged — jaw claudication plus ESR/CRP make GCA the diagnosis until biopsy says otherwise.
- Do not hold steroids pending biopsy; biopsy yield persists for 1–2 weeks after starting.
- Do not dismiss the prior transient episode — amaurosis in a patient >50 is GCA or embolic until excluded.
- Do not expect recovery of the left eye; the goal of treatment is protecting the right.
```
