---
title: "Echocardiogram Report Interpretation"
category: domain-healthcare-clinical/interpretation
description: "Read a transthoracic echo report — LV/RV function, diastolic grading, valve severity, pulmonary pressure, pericardium — reconcile discordant measurements, and commit to heart failure, valve, or further-imaging action."
techniques:
  - ST-02
  - ST-03
  - CM-01
  - RT-02
  - RT-05
difficulty: advanced
tags:
  - cardiology
  - echocardiography
  - heart-failure
  - valvular-disease
  - interpretation
  - heart-ultrasound
  - tight-heart-valve
  - weak-heart-pump
updated: "2026-09-24"
related_prompts:
  - domain-healthcare-clinical/prompts/reasoning/workup_dyspnea.md
  - domain-healthcare-clinical/prompts/care-plans/careplan_hfref_gdmt.md
  - domain-healthcare-clinical/prompts/pathophysiology/patho_cardiac_hemodynamics.md
---

## Objective

Read an echocardiogram report and produce a clinically committed interpretation: HF phenotype by EF, filling pressure status, RV function and pulmonary pressure, severity grade of each valve lesion with discordance resolved, pericardial physiology, and the action each implies. Input is the report's measurements and narrative.

Decision support for a licensed clinician: confirm drug doses, renal adjustment and severity thresholds against the current guideline and local formulary. Tamponade physiology, cardiogenic shock, or syncope with severe AS is escalated now, not after this output.

## When to Use

- A transthoracic echo report needs an HF phenotype, a filling-pressure call, and a severity grade for each valve lesion with an action.
- Valve grading is discordant (e.g., small AVA with a low gradient) and must be reconciled before referral.
- A new echo is compared with a prior to decide whether EF, a lesion, or pulmonary pressure has truly changed.

**Not this prompt if:**

- The HF phenotype is settled and GDMT is being titrated → `domain-healthcare-clinical/prompts/care-plans/careplan_hfref_gdmt.md` (or `domain-healthcare-clinical/prompts/care-plans/careplan_hfpef.md`).
- Dyspnea is being worked up and no echo is available yet → `domain-healthcare-clinical/prompts/reasoning/workup_dyspnea.md`.
- The study is an ECG → `domain-healthcare-clinical/prompts/interpretation/interp_ecg_full_interpretation.md`.

## Inputs

- Echo report: LVEF (method: biplane Simpson vs visual), LV dimensions/volumes, wall thickness, LV mass index, relative wall thickness, regional wall motion, GLS if reported
- Diastolic parameters: E, A, E/A, septal and lateral e', average E/e', LA volume index, TR peak velocity
- RV: size, TAPSE, S', FAC; RVSP/PASP estimate; IVC size and collapse
- Valves: velocities, gradients, areas (AVA, MVA), regurgitant quantification (vena contracta, EROA, regurgitant volume), stroke volume index
- Pericardium, masses, thrombus, vegetations, shunts/bubble study
- Clinical context: symptoms, BP and HR at time of study, rhythm, prior echo, BNP/NT-proBNP, indication

## Role

Senior cardiology attending (echo-boarded) supporting the treating clinician; interprets the study for the primary team.

## Reasoning Steps

1. **Stop and escalate first if:** tamponade physiology with hypotension, a new severe regurgitant lesion or ventricular free-wall/septal rupture after MI, a mobile LV/LA thrombus or large vegetation, an aortic dissection flap, or severe AS with syncope and hemodynamic compromise — contact cardiology/cardiac surgery now. Then **LV systolic function.** Classify: HFrEF ≤40%, HFmrEF 41–49%, HFpEF ≥50%; HF with improved EF (HFimpEF) if previously ≤40%, now >40%, and with a ≥10-point rise from baseline. Visual EF has ±5–10% variability — do not call a change of 5% real without the same method. Regional wall motion by territory (LAD: anterior, septal, apical; RCA: inferior, inferoseptal; LCx: lateral). Reduced GLS with preserved EF → early myocardial dysfunction (chemotherapy cardiotoxicity, amyloid with apical sparing); GLS normal values are vendor-dependent.

2. **LV geometry.** Concentric hypertrophy (↑ mass, RWT >0.42) → hypertension, aortic stenosis, HCM, infiltrative (amyloid: thick walls with low voltage on ECG). Septum ≥15 mm with LVOT gradient ≥30 mmHg → obstructive HCM physiology. Dilated LV with global hypokinesis → dilated cardiomyopathy workup.

3. **Diastolic function (ASE 2016 approach (check for a newer ASE update), normal EF).** Four variables: septal e' <7 or lateral e' <10 cm/s; average E/e' >14; LAVI >34 mL/m²; TR velocity >2.8 m/s. >50% abnormal → diastolic dysfunction; grade I–III by E/A and filling pressure. With reduced EF, elevated E/e' and LAVI indicate raised filling pressures. Atrial fibrillation, mitral disease, and paced rhythms invalidate the standard algorithm.

4. **RV and pulmonary pressure.** TAPSE <17 mm or S' <9.5 cm/s → RV systolic dysfunction. RVSP = 4(TR Vmax)² + RAP; RAP from IVC (≤2.1 cm with >50% collapse ≈ 3 mmHg; >2.1 cm with <50% collapse ≈ 15 mmHg; otherwise ≈ 8). TR velocity >2.8 m/s raises PH probability; echo estimates, right heart catheterization confirms. Poor TR envelope → RVSP unreliable.

5. **Valves — grade and reconcile.**
   - **Aortic stenosis severe:** Vmax ≥4.0 m/s, mean gradient ≥40 mmHg, AVA ≤1.0 cm² (AVAi ≤0.6 cm²/m²). Discordant (small AVA, low gradient): check LVOT diameter measurement error first; then classical low-flow low-gradient (EF <50% → dobutamine stress echo) vs paradoxical low-flow (EF ≥50%, SVi <35 mL/m² → CT aortic valve calcium score; severe likely at ≥2,000 AU men, ≥1,200 AU women).
   - **Mitral regurgitation:** primary vs secondary mechanism matters; severe primary MR ≈ vena contracta ≥0.7 cm, EROA ≥0.4 cm², regurgitant volume ≥60 mL. Secondary MR thresholds and management differ; optimize GDMT before judging severity.
   - **Aortic regurgitation, mitral stenosis (MVA ≤1.5 cm² severe), tricuspid regurgitation, prosthetic valve gradients vs baseline post-implant echo.**

6. **Pericardium and masses.** Effusion size; tamponade physiology — RA systolic collapse, RV diastolic collapse, plethoric IVC, exaggerated respiratory variation in mitral inflow (>25%) — tamponade remains a clinical diagnosis. LV apical thrombus after anterior MI → anticoagulate. Vegetations: TTE sensitivity is limited — negative TTE does not exclude endocarditis (TEE for S. aureus bacteremia, prosthetic valves, high suspicion).

7. **Pitfalls before signing.** Grading AS on one parameter; ignoring BP (hypertension at study time lowers the AS gradient and worsens MR); comparing EF across modalities (echo vs MRI vs nuclear); applying diastolic grading in AF; RVSP from a weak TR jet; calling "normal study" in unexplained HFpEF without considering amyloid.

## Output Format

```
LV: [EF + method, HF category, size, geometry, regional WMA, GLS]
DIASTOLIC: [grade, filling pressure elevated Y/N, criteria used]
RV/PA: [size, TAPSE/S', RVSP, PH probability]
VALVES: [each lesion — severity — concordant or reconciled]
PERICARDIUM/OTHER: [effusion, physiology, thrombus, vegetation, shunt]
CHANGE FROM PRIOR: [date, what changed]

IMPRESSION:
1. [most significant] — [action: GDMT / heart team / anticoagulation / further imaging]
2. [next] — [action]
3. [follow-up echo interval]
```

## Verification

- [ ] EF method stated, and the HF category (including the HFimpEF criteria) applied per the 2021 universal HF definition or current HF guideline.
- [ ] Every valve lesion graded on several concordant parameters, with any discordance explained (measurement error, flow state) before severity is committed.
- [ ] BP, HR, and rhythm at the time of the study considered before grading AS, MR, and diastolic function.
- [ ] Diastolic grading used only where the algorithm is valid (not AF, significant mitral disease, or paced rhythm), naming the ASE version applied.
- [ ] Each impression traced to a reported measurement; intervention thresholds and pathways attributed to the named guideline and year (e.g., ACC/AHA 2020 valvular heart disease).
- [ ] States what would change the call (CT calcium score, dobutamine stress echo, TEE, repeat echo).

## False-Positive Prevention

- **Trivial findings named as the cause of symptoms.** Trace or mild regurgitation, a PFO, or a small effusion rarely explain dyspnea or syncope.
- **An RVSP estimate labeled "pulmonary hypertension".** Echo gives a PH probability; right heart catheterization makes the diagnosis.
- **Echo collapse signs called tamponade in a patient without clinical tamponade.** Tamponade is a clinical and hemodynamic diagnosis.
- **A hyperdynamic LVOT gradient (dehydration, sepsis, inotropes) or sigmoid septum called obstructive HCM** without wall thickness criteria and a gradient in a euvolemic state.

## Worked Example

**Input:** 79 y/o F, 6 months progressive exertional dyspnea, one episode of exertional syncope. BP 128/70 at study, sinus rhythm, BSA 1.6 m². TTE: "LVEF 60% (biplane). Concentric LVH, small LV cavity. Heavily calcified trileaflet aortic valve with restricted opening. AV Vmax 3.6 m/s, mean gradient 32 mmHg, AVA (continuity) 0.78 cm², AVAi 0.49 cm²/m², LVOT diameter 1.9 cm, SVi 30 mL/m². Average E/e' 16, LAVI 42 mL/m², TR Vmax 3.0 m/s, IVC 1.8 cm with >50% collapse. RVSP 39 mmHg. No pericardial effusion."

**Output:**

```
LV: EF 60% biplane — preserved. Concentric LVH with small cavity. No regional WMA reported.
DIASTOLIC: Elevated filling pressure — E/e' 16, LAVI 42, TR 3.0 m/s (3 of 3 available criteria abnormal).
RV/PA: RVSP 4(3.0)² + 3 = 39 mmHg — intermediate PH probability, likely post-capillary from elevated LV filling pressure.
VALVES: Aortic stenosis — discordant grading: AVA 0.78 cm² and AVAi 0.49 (severe range) but Vmax 3.6 m/s and mean gradient 32 mmHg (moderate range). SVi 30 mL/m² (<35) with EF ≥50% → paradoxical low-flow low-gradient severe AS is likely. LVOT 1.9 cm — a small or under-measured LVOT would falsely lower AVA; confirm measurement.
PERICARDIUM/OTHER: None.
CHANGE FROM PRIOR: No prior provided.

IMPRESSION:
1. Probable paradoxical low-flow low-gradient severe AS, symptomatic (dyspnea, exertional syncope).
   - Confirm severity: CT aortic valve calcium score (severe likely if ≥1,200 AU in a woman); CT also gives the LVOT area to recompute AVA and TAVR planning anatomy.
   - Heart valve team referral now. At 79 with confirmed severe symptomatic AS, ACC/AHA 2020 places her in the 65–80 age band where SAVR vs TAVR is a shared Heart Team decision (TAVR often favored with advancing age and surgical risk).
   - Until intervention: avoid vasodilators and aggressive preload reduction; no strenuous exertion; low-dose diuretic only for congestion (furosemide 20 mg PO daily as needed), watching for hypotension.
2. Concentric LVH with small cavity and HFpEF physiology — consistent with AS; if CT calcium score is low (moderate AS), screen for cardiac amyloid (serum/urine immunofixation, free light chains, technetium pyrophosphate scan), which commonly coexists with AS in this age group.
3. Follow-up: post-procedure baseline echo 30 days after valve replacement; if intervention deferred, repeat echo in 6 months or sooner with symptom change.
```
