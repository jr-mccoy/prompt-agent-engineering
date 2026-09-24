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
updated: "2026-09-24"
---

## Objective

Read a CT head report (non-contrast, with CTA/CT perfusion if performed) in clinical context and produce a structured impression that names each finding, classifies it, states what the study can and cannot exclude, and commits to the action — neurosurgery call, anticoagulant reversal, BP target, thrombectomy pathway, or further imaging. The input is the radiologist's report or structured findings, not raw images. Distinct from `acute_stroke_tpa_thrombectomy.md`, which runs the stroke treatment protocol; this prompt reads the imaging and routes to it.

## Inputs

- CT head report text: technique (non-contrast, contrast, CTA head/neck, CTP), findings, impression, comparison
- Time from symptom onset or last known well; time of scan
- Presentation: trauma mechanism, headache character (thunderclap), focal deficit and NIHSS, GCS, seizure, vomiting
- Anticoagulants and antiplatelets (drug, dose, time of last dose), platelet count, INR/aPTT
- Age, BP, known malignancy, prior imaging

## Role

Senior neurocritical care or emergency medicine attending reading the CT report at the bedside and deciding the next hour.

## Reasoning Steps

1. **Fix what the study is.** Non-contrast CT cannot exclude early ischemia, venous sinus thrombosis, or small posterior fossa lesions. State the time from onset: early infarct is often invisible in the first hours; a normal non-contrast CT within 6 hours of thunderclap onset, on a modern scanner read by an experienced reader, is highly sensitive for SAH in a neurologically intact patient — beyond that window, LP or CTA is required.

2. **Hemorrhage — classify by compartment.**
   - **Epidural:** biconvex, does not cross sutures, usually arterial (middle meningeal) with skull fracture; lucid interval then rapid decline.
   - **Subdural:** crescentic, crosses sutures, not the midline; acute hyperdense, subacute isodense (easily missed, especially bilateral), chronic hypodense; mixed density = acute-on-chronic.
   - **Subarachnoid:** basal cisterns/Sylvian fissures → aneurysmal until CTA says otherwise; perimesencephalic pattern → often non-aneurysmal but still needs vessel imaging; convexity sulcal SAH → trauma, RCVS, CAA.
   - **Intraparenchymal:** deep (basal ganglia, thalamus, pons, cerebellum) → hypertensive; lobar → amyloid angiopathy, AVM, tumor, venous infarction, hemorrhagic conversion. Estimate volume by ABC/2. CTA spot sign → expansion risk.
   - **Intraventricular:** extension or primary; watch for hydrocephalus.

3. **Mass effect and herniation.** Midline shift (mm, at septum pellucidum), basal cistern effacement, uncal/subfalcine/tonsillar herniation, hydrocephalus (temporal horn dilatation, trapped ventricle). These set urgency more than lesion size.

4. **Ischemia.** Hyperdense vessel sign, loss of grey–white differentiation, insular ribbon sign, sulcal effacement. Record ASPECTS (10-point, anterior circulation; lower = larger core) and CTA occlusion site (ICA, M1, M2, basilar). CTP core/penumbra mismatch extends the thrombectomy window. Eligibility thresholds follow the current stroke guideline and local protocol — route to the stroke pathway, do not re-derive it.

5. **Other findings.** Skull and skull-base fracture (pneumocephalus, air–fluid in sinuses), dense venous sinus or cord sign (→ CT venogram), mass with vasogenic edema (→ MRI with contrast), abscess, hydrocephalus without mass (→ NPH vs obstructive). Chronic small-vessel change and atrophy are background — do not attribute acute symptoms to them.

6. **Neurosurgical triggers (commonly used thresholds).** Acute SDH ≥10 mm thick or midline shift ≥5 mm; EDH >30 mL; cerebellar hemorrhage >3 cm or with brainstem compression or hydrocephalus; acute hydrocephalus → EVD. Below these, a deteriorating exam still wins.

7. **Anticoagulation and BP.** Any intracranial hemorrhage on an anticoagulant → reverse now: warfarin → 4F-PCC (INR/weight-dosed) + vitamin K 10 mg IV; factor Xa inhibitor → andexanet alfa (dose by drug, dose, timing) or 4F-PCC 50 units/kg; dabigatran → idarucizumab 5 g IV. Platelet transfusion for antiplatelet-associated ICH only if going to surgery. Spontaneous ICH: target SBP ~140, avoid dropping below 130.

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
1. Acute traumatic SDH meeting surgical thresholds (≥10 mm and shift ≥5 mm) on an active factor Xa inhibitor — emergent neurosurgery for evacuation; reverse apixaban now.
2. Chronic small-vessel disease — no action.

NEXT 60 MINUTES:
- Neurosurgery at bedside now; OR planning for craniotomy.
- Apixaban reversal: andexanet alfa low-dose regimen (apixaban ≤5 mg) — 400 mg IV bolus at 30 mg/min, then 4 mg/min for up to 120 min. If unavailable or per institutional protocol: 4F-PCC 50 units/kg (~3,100 units).
- Hold apixaban; restart timing decided with neurosurgery (typically days to weeks, individualized to bleed and stroke risk).
- SBP <160 in traumatic SDH pending surgery: nicardipine 5 mg/h, titrate by 2.5 mg/h q5–15 min.
- Neuro checks q1h; any GCS drop ≥2 → immediate repeat CT and re-page neurosurgery.
- CBC, PT/INR, aPTT, anti-Xa (apixaban-calibrated) if available, type and screen, BMP.
- Seizure prophylaxis only if the neurosurgical TBI protocol specifies it (levetiracetam 500 mg IV BID × 7 days).
- If surgery is declined or deferred: repeat CT at 6 hours to assess expansion.
```
