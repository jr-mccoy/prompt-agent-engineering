---
title: "CT Head Report Interpretation"
category: domain-healthcare-clinical/interpretation
description: "Turn a non-contrast CT head (± CTA/CTP) report into a committed clinical impression: hemorrhage compartment, mass effect, ischemia, and the neurosurgical, reversal, and stroke actions each finding triggers."
techniques:
  - ST-02
  - ST-03
  - CM-01
  - RT-02
  - RT-05
difficulty: advanced
tags:
  - neurology
  - neurosurgery
  - radiology
  - ct-head
  - interpretation
  - head-bleed
  - fall-on-blood-thinners
  - head-injury
updated: "2026-09-24"
related_prompts:
  - domain-healthcare-clinical/prompts/interpretation/interp_mri_brain.md
  - domain-healthcare-clinical/prompts/pharmacology/medicine_anticoagulation_decision_support.md
  - domain-healthcare-clinical/prompts/acute-care/acute_stroke_tpa_thrombectomy.md
---

> **Medical disclaimer — read before use.** This prompt is a decision-support and
> teaching aid for **licensed clinicians**. It is **not medical advice** and is not for
> patients to diagnose or treat themselves. Drug doses, thresholds and guideline
> references in it and in its worked example may be incomplete, outdated or wrong:
> verify each one against the current guideline, the product label and your local
> formulary, and follow your institution's protocols. It does not replace examination
> or clinical judgment. **Medical emergency: call your local emergency number (911 in
> the US).**
>
> **Review status:** clinical content and doses reviewed by AI only (2026-09-24);
> **not yet reviewed by a licensed clinician.**

## Objective

Read a CT head report (non-contrast, with CTA/CT perfusion if performed) in clinical context and produce a structured impression that names each finding, classifies it, states what the study can and cannot exclude, and commits to the action — neurosurgery call, anticoagulant reversal, BP target, thrombectomy pathway, or further imaging. The input is the radiologist's report or structured findings, not raw images.

Decision support for a licensed clinician: confirm reversal-agent and antihypertensive doses, renal adjustment and thresholds against the current guideline and local formulary; the operative decision belongs to neurosurgery. A patient with a falling GCS or herniation signs is escalated now, not after this output.

## When to Use

- A non-contrast CT head (± CTA/CTP) report is back after head trauma, a fall on an anticoagulant, a thunderclap headache, or a new deficit.
- Deciding whether a finding triggers neurosurgical review, anticoagulant reversal, a BP target, or the stroke pathway.
- Converting "cannot exclude" language into a next test or an explicit acceptance.

**Not this prompt if:**

- The stroke is confirmed and thrombolysis/thrombectomy eligibility and dosing are being run → `domain-healthcare-clinical/prompts/acute-care/acute_stroke_tpa_thrombectomy.md`, which runs the stroke treatment protocol; this prompt reads the imaging and routes to it.
- The study is an MRI brain → `domain-healthcare-clinical/prompts/interpretation/interp_mri_brain.md`.
- The headache is being worked up before imaging → `domain-healthcare-clinical/prompts/reasoning/workup_headache.md`.

## Inputs

- CT head report text: technique (non-contrast, contrast, CTA head/neck, CTP), findings, impression, comparison
- Time from symptom onset or last known well; time of scan
- Presentation: trauma mechanism, headache character (thunderclap), focal deficit and NIHSS, GCS, seizure, vomiting
- Anticoagulants and antiplatelets (drug, dose, time of last dose), platelet count, INR/aPTT
- Age, BP, known malignancy, prior imaging

## Role

Senior neurocritical care or emergency medicine attending supporting the treating clinician; reads the CT report at the bedside and plans the next hour.

## Reasoning Steps

1. **Stop and escalate first if:** falling GCS, a new fixed or dilated pupil, Cushing response, herniation, or acute hydrocephalus — request emergent neurosurgical review and start ICP measures now; any intracranial hemorrhage on an anticoagulant — start reversal now. Then **fix what the study is.** Non-contrast CT cannot exclude early ischemia, venous sinus thrombosis, or small posterior fossa lesions. State the time from onset: early infarct is often invisible in the first hours; a normal non-contrast CT within 6 hours of thunderclap onset, on a modern scanner read by an experienced reader, is highly sensitive for SAH in a neurologically intact patient — beyond that window, LP or CTA is required.

2. **Hemorrhage — classify by compartment.**
   - **Epidural:** biconvex, does not cross sutures, usually arterial (middle meningeal) with skull fracture; lucid interval then rapid decline.
   - **Subdural:** crescentic, crosses sutures, not the midline; acute hyperdense, subacute isodense (easily missed, especially bilateral), chronic hypodense; mixed density = acute-on-chronic.
   - **Subarachnoid:** basal cisterns/Sylvian fissures → aneurysmal until CTA says otherwise; perimesencephalic pattern → often non-aneurysmal but still needs vessel imaging; convexity sulcal SAH → trauma, RCVS, CAA.
   - **Intraparenchymal:** deep (basal ganglia, thalamus, pons, cerebellum) → hypertensive; lobar → amyloid angiopathy, AVM, tumor, venous infarction, hemorrhagic conversion. Estimate volume by ABC/2. CTA spot sign → expansion risk.
   - **Intraventricular:** extension or primary; watch for hydrocephalus.

3. **Mass effect and herniation.** Midline shift (mm, at septum pellucidum), basal cistern effacement, uncal/subfalcine/tonsillar herniation, hydrocephalus (temporal horn dilatation, trapped ventricle). These set urgency more than lesion size.

4. **Ischemia.** Hyperdense vessel sign, loss of grey–white differentiation, insular ribbon sign, sulcal effacement. Record ASPECTS (10-point, anterior circulation; lower = larger core) and CTA occlusion site (ICA, M1, M2, basilar). CTP core/penumbra mismatch extends the thrombectomy window. Eligibility thresholds follow the current stroke guideline and local protocol — route to the stroke pathway, do not re-derive it.

5. **Other findings.** Skull and skull-base fracture (pneumocephalus, air–fluid in sinuses), dense venous sinus or cord sign (→ CT venogram), mass with vasogenic edema (→ MRI with contrast), abscess, hydrocephalus without mass (→ NPH vs obstructive). Chronic small-vessel change and atrophy are background — do not attribute acute symptoms to them.

6. **Neurosurgical triggers (commonly used thresholds).** Acute SDH thickness >10 mm or midline shift >5 mm, and EDH >30 mL (Brain Trauma Foundation surgical management of TBI guidelines); cerebellar hemorrhage >3 cm or with brainstem compression or hydrocephalus; acute hydrocephalus → EVD. Below these, a deteriorating exam still wins.

7. **Anticoagulation and BP.** Any intracranial hemorrhage on an anticoagulant → reverse now: warfarin → 4F-PCC (INR/weight-dosed) + vitamin K 10 mg IV; factor Xa inhibitor → andexanet alfa (dose by drug, dose, timing; thrombotic risk (ANNEXA-I); availability/labeling vary — verify locally) or 4F-PCC 50 units/kg; dabigatran → idarucizumab 5 g IV. Platelet transfusion for antiplatelet-associated ICH only if going to surgery. Spontaneous ICH: target SBP ~140, avoid dropping below 130.

8. **Pitfalls before signing.** "Cannot exclude" language must be converted into a decision (next test or accept). Isodense bilateral SDH shows no shift. Posterior fossa beam-hardening hides cerebellar infarct. High hematocrit mimics hyperdense vessels. A negative CT does not exclude early ischemia, late-presenting SAH, CVST, or posterior circulation stroke. Always compare to prior: interval growth is the question in anticoagulated trauma.

## Output Format

```
STUDY: [technique, time from onset, comparison, what it cannot exclude]
HEMORRHAGE: [compartment, size/thickness/volume, location, age by density]
MASS EFFECT: [midline shift mm, cisterns, herniation, hydrocephalus]
ISCHEMIA: [early signs, ASPECTS, vessel occlusion, perfusion mismatch]
OTHER: [fracture, venous sinus, mass, incidental]

IMPRESSION:
1. [most significant finding] — [action: consult / reversal / BP / pathway]
2. [next finding] — [action]
3. [incidental or chronic] — [follow-up or none]

NEXT 60 MINUTES:
- [specific orders with doses]
- [repeat imaging interval]
```

## Verification

- [ ] Study limits stated with the time from onset (what a non-contrast CT cannot exclude at this time point).
- [ ] Each neurosurgical threshold attributed to its named guideline (Brain Trauma Foundation surgical management guidelines for traumatic SDH/EDH; the current ICH guideline for spontaneous hemorrhage) and compared as stated (strict > vs ≥) against the reported measurements.
- [ ] Reversal agent matched to the specific anticoagulant, dose, and time of last dose; doses checked against weight and renal function; local availability and labeling confirmed.
- [ ] BP target named with its source (spontaneous ICH guideline vs local TBI protocol) and not carried from one setting to the other.
- [ ] Every "cannot exclude" converted into a next test or an explicit acceptance.
- [ ] Repeat-imaging interval stated, with the exam change that triggers an earlier scan.

## False-Positive Prevention

- **Physiologic calcification called hemorrhage.** Pineal, choroid plexus, falx, and basal ganglia calcification are dense but not blood.
- **A dense falx or tentorium called a thin SDH or SAH,** especially in young patients or with a high hematocrit.
- **A measurement at a threshold treated as meeting it.** Surgical thresholds are strict (e.g., SDH >10 mm), and the exam and trajectory outweigh a single number.
- **Old infarct or encephalomalacia read as acute ischemia** without a prior study or the density of an established lesion (CSF-like, with volume loss).

## Worked Example

**Input:** 78 y/o F, fell from standing 3 hours ago, struck head. On apixaban 5 mg BID for AF, last dose 4 hours ago. GCS 14 (confused), no focal deficit, BP 176/94, weight 62 kg, platelets 210. Non-contrast CT head report: "12 mm acute right frontoparietal subdural hematoma with 6 mm leftward midline shift. Partial effacement of the right lateral ventricle. Basal cisterns patent. No skull fracture. Moderate chronic small-vessel ischemic change. No prior for comparison."

**Output:**

```
STUDY: Non-contrast CT, 3 h post-injury, no prior. Adequate for hemorrhage; does not assess expansion — repeat needed if not operated.
HEMORRHAGE: Acute right convexity SDH, 12 mm maximal thickness.
MASS EFFECT: 6 mm leftward midline shift, right lateral ventricle effacement; cisterns patent — no herniation yet.
ISCHEMIA: Not assessable/not the question; small-vessel change is chronic background.
OTHER: No fracture.

IMPRESSION:
1. Acute traumatic SDH meeting surgical thresholds (>10 mm and shift >5 mm) on an active factor Xa inhibitor — emergent neurosurgery for evacuation; reverse apixaban now.
2. Chronic small-vessel disease — no action.

NEXT 60 MINUTES:
- Request emergent neurosurgical review; the operative decision (e.g., craniotomy) rests with neurosurgery.
- Apixaban reversal: andexanet alfa low-dose regimen (apixaban ≤5 mg) — 400 mg IV bolus at 30 mg/min, then 4 mg/min for up to 120 min. Thrombotic risk (ANNEXA-I); availability/labeling vary — verify locally. If unavailable or per institutional protocol: 4F-PCC 50 units/kg (~3,100 units).
- Hold apixaban; restart timing decided with neurosurgery (typically days to weeks, individualized to bleed and stroke risk).
- BP target per local TBI protocol pending surgery; if lowering is needed: nicardipine 5 mg/h, titrate by 2.5 mg/h q5–15 min.
- Neuro checks q1h; any GCS drop ≥2 → immediate repeat CT and re-page neurosurgery.
- CBC, PT/INR, aPTT, anti-Xa (apixaban-calibrated) if available, type and screen, BMP.
- Seizure prophylaxis only if the neurosurgical TBI protocol specifies it (levetiracetam 500 mg IV BID × 7 days).
- If surgery is declined or deferred: repeat CT at 6 hours to assess expansion.
```
