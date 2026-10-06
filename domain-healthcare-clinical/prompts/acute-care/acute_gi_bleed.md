---
title: "Acute GI Bleed Management"
category: domain-healthcare-clinical/acute-care
description: "Manage upper or lower GI bleeding with resuscitation, risk stratification, pharmacologic therapy, transfusion thresholds, and endoscopic timing."
techniques:
  - ST-02
  - ST-03
  - CM-01
  - RT-02
  - RT-05
difficulty: intermediate
tags:
  - gi
  - hemorrhage
  - critical-care
  - endoscopy
updated: "2026-10-06"
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
> **Review status:** AI-assisted content, reviewed by AI only (2026-10-06);
> **not yet reviewed by a licensed clinician.**

## Objective

Manage acute upper or lower GI bleeding: localize, resuscitate, risk-stratify, give pharmacologic therapy by source, transfuse appropriately, and time endoscopic intervention.

## Inputs

- Presentation: hematemesis, melena, hematochezia, coffee-ground emesis, syncope, abdominal pain
- Vitals: HR, BP, orthostatic if stable, mental status
- Labs: Hgb, platelets, INR, BMP (BUN/Cr ratio), lactate, type and crossmatch
- History: prior GI bleed, varices, NSAIDs, anticoagulants, antiplatelets, alcohol use, cirrhosis, malignancy, recent endoscopy or surgery
- Comorbidities: CAD, CKD, decompensated heart failure (transfusion threshold considerations)

## Reasoning Steps

1. **Localize: upper vs lower GI bleed.**
   - **Upper (above ligament of Treitz):** hematemesis, coffee-ground emesis, melena (black tarry — usually from ≥150 mL blood), elevated BUN/Cr ratio (>30 — protein digestion from blood).
   - **Lower (below ligament of Treitz):** hematochezia (bright red blood per rectum). But brisk upper GI bleed can cause hematochezia (~10% of cases) — if hematochezia with hemodynamic instability, do NG aspirate or upper endoscopy first to rule out upper source. NG bilious without blood does not fully exclude upper source (post-pyloric).
   - **Obscure GI bleed (5%):** small bowel; capsule endoscopy or push enteroscopy after upper and lower workup negative.

2. **Resuscitate.**
   - 2 large-bore PIVs (16G or 18G).
   - IV fluids: NS or LR bolus 1 L; titrate to perfusion. Avoid massive crystalloid in cirrhotic/variceal — worsens portal pressure and dilutes clotting factors.
   - Activate massive transfusion protocol if hemodynamic instability and ongoing brisk bleeding.
   - Type and crossmatch.

3. **Transfusion thresholds (variceal/non-variceal upper, lower bleeds):**
   - **Restrictive: Hgb 7 g/dL** in stable non-variceal upper GI bleed (Villanueva trial — restrictive better than liberal).
   - **Hgb 8 g/dL** for active CAD or stable angina (per AABB).
   - **Hgb 9 g/dL** historically in massive hemorrhage / unstable patients — but balanced products (1:1:1) are the better framework for active hemorrhage rather than Hgb-driven.
   - Platelets with active bleeding → transfuse below the threshold in current guidance for the bleed type (non-variceal vs cirrhotic/variceal) [VERIFY: current ACG / ESGE non-variceal guidance; Baveno VII / current AASLD guidance for cirrhosis].
   - INR >1.5–2 with active bleeding → FFP, vitamin K, or PCC (if on warfarin). In cirrhosis, INR does not reflect bleeding risk and INR-driven correction is not routinely recommended in variceal bleeding [VERIFY: Baveno VII / current AASLD guidance].

4. **Risk stratify upper GI bleed.**
   - **Glasgow-Blatchford score** (admission, no endoscopy needed): score 0 → outpatient management acceptable; score >0 → admit and endoscope.
   - **Rockall score** (post-endoscopy): mortality and rebleed prediction.
   - **AIMS65** (mortality): albumin <3, INR >1.5, altered mental status, SBP ≤90, age ≥65.

5. **Pharmacologic therapy (upper).**
   - **PPI:** pantoprazole 80 mg IV bolus, then 8 mg/h infusion × 72 h, OR pantoprazole 40 mg IV BID. Reduces rebleeding after high-risk lesions on endoscopy.
   - **Variceal bleed (suspected by cirrhosis history, hematemesis, hemodynamic compromise):**
     - **Octreotide 50 mcg IV bolus then 50 mcg/h infusion × 3–5 days.** Splanchnic vasoconstriction.
     - **Empiric antibiotics:** ceftriaxone 1 g IV daily × 7 days. Reduces SBP, mortality, and rebleeding in cirrhotic GI bleed.
     - **Endoscopic band ligation** definitive treatment.
     - Beta-blocker (carvedilol or nadolol) for primary and secondary prophylaxis after acute bleed resolves.

6. **Pharmacologic therapy (lower).**
   - PPI not routinely indicated for lower GI bleed.
   - Anticoagulant management: hold; reverse if life-threatening bleed (vitamin K + 4F-PCC for warfarin; idarucizumab or 4F-PCC for dabigatran; andexanet or 4F-PCC for Xa inhibitors).
   - Antiplatelet: hold aspirin and P2Y12 unless within 1 month of DES (high stent thrombosis risk — discuss with cardiology, may continue at least one antiplatelet).

7. **Endoscopy timing.**
   - **Upper GI bleed:** within 24 h of presentation in admitted patients. Earlier (≤6–12 h) for variceal bleed or hemodynamic instability after stabilization. Avoid pre-stabilization endoscopy — desaturation, aspiration risk.
   - **Lower GI bleed:** colonoscopy within 24 h after rapid bowel prep for hospitalized patients; provides diagnostic yield and therapeutic potential. Severe ongoing bleed → consider CT angiography first (faster localization, then IR for embolization).
   - **Capsule endoscopy / enteroscopy:** for obscure GI bleed after EGD and colonoscopy negative.

8. **Adjunctive considerations.**
   - **Erythromycin 250 mg IV** 30–90 min before EGD — improves visualization by clearing stomach (prokinetic, motilin agonist).
   - **NG lavage:** historically used to clear stomach pre-EGD; not universally needed if erythromycin used or visualization adequate.
   - **Airway protection:** intubation for active hematemesis, altered mental status, or aspiration risk before endoscopy.
   - **CT angiography:** for severe lower GI bleed when endoscopy not yielding source; identifies active extravasation.
   - **Interventional radiology embolization:** if endoscopy fails or for pseudoaneurysmal sources.
   - **Surgery:** rarely needed; reserved for failure of endoscopic and IR approaches.

9. **Disposition.**
   - ICU for hemodynamic instability, ongoing transfusion, variceal bleed, advanced age with comorbidity.
   - Step-down for moderate severity.
   - Floor for stable, low-risk, with planned endoscopy.
   - Outpatient management for very-low-risk patients (Glasgow-Blatchford 0).

10. **Secondary prevention.**
    - H. pylori testing and eradication for ulcer disease.
    - Hold NSAIDs; if needed, COX-2 selective with PPI cover.
    - PPI continuation for high-risk ulcer features.
    - Beta-blocker (carvedilol or nadolol) for variceal patients.
    - Endoscopic surveillance for variceal patients per guidelines.
    - Re-evaluate antiplatelet/anticoagulant indications and consider GI prophylaxis.

## False-Positive Prevention

❌ **DON'T:**
- Write "Glasgow-Blatchford very high" or "AIMS65 high" under SEVERITY without scoring each item from the supplied BUN, Hgb, SBP, HR and history.
- Fill the TRANSFUSION line with FFP or PCC for a cirrhotic variceal bleed just because INR is above the step-3 cut-off; state the specific reason for any product beyond pRBC in that patient.
- Settle LOCALIZATION as lower from hematochezia while HR/BP show instability, without saying whether an upper source has been excluded.
- Leave the reversal slot as "not applicable" when the med list shows an antiplatelet or anticoagulant, or name an agent when none is listed.
- Read the first Hgb as the measure of blood loss; in acute hemorrhage it under-reads until equilibration, so report it with its timepoint and trend.

✅ **DO:**
- Score Glasgow-Blatchford item by item (BUN converted to mmol/L if reported in mg/dL, Hgb by sex band, SBP, HR, melena, syncope, hepatic disease, cardiac failure) and show the total; the worked example's inputs sum to 16.
- Name which threshold branch the TRANSFUSION target came from (stable non-variceal, active CAD, active hemorrhage with ratio-based replacement).
- Check that ENDOSCOPY TIMING agrees with the localization and variceal suspicion stated earlier in the same output.
- Tag octreotide, PPI and antibiotic durations `[VERIFY: current guideline/formulary]` when the clinician has not supplied a local order set.

## Output Format

```
LOCALIZATION: [upper / lower / obscure]
SUSPECTED SOURCE: [PUD / varices / gastritis / Mallory-Weiss / Dieulafoy / diverticular / angiodysplasia / cancer / colitis / hemorrhoids / etc.]
SEVERITY: [hemodynamic status, Glasgow-Blatchford if upper]

RESUSCITATION:
- 2 large-bore PIVs
- IV fluids [type, rate]
- Type and cross
- MTP if indicated

TRANSFUSION:
- Hgb threshold: [7 / 8 / 9]
- Platelets, FFP, vitamin K [as indicated]

PHARMACOTHERAPY:
- Upper non-variceal: pantoprazole 80 mg IV bolus + 8 mg/h
- Upper variceal: octreotide + ceftriaxone
- Anticoagulant reversal [agent, dose if indicated]

ENDOSCOPY TIMING:
- [≤6–12 h variceal / 24 h other / colonoscopy after bowel prep]

ADJUNCTS:
- Erythromycin pre-EGD
- Airway protection if needed
- CT angio / IR if endoscopy fails

DISPOSITION:
- [ICU / step-down / floor]

WORKUP:
- CBC, INR, BMP, lactate, type and cross, LFT (cirrhosis assessment)
- ECG, troponin if elderly or concern for demand ischemia

PITFALLS:
- [over-resuscitation in variceal, missed upper source in hematochezia, etc.]
```

## Worked Example

**Input:** 56 y/o M with cirrhosis (alcohol), presenting with two episodes of large-volume hematemesis. BP 88/52, HR 124, alert. Hgb 7.2 (down from 11.4 baseline 6 months ago), platelets 65, INR 1.8. Lactate 3.6, BUN 42, Cr 1.1. Last EGD 1 year ago: large esophageal varices, no banding done.

**Output:**

```
LOCALIZATION: Upper GI bleed (hematemesis).
SUSPECTED SOURCE: Variceal hemorrhage. Cirrhosis with known large unbanded varices and acute hematemesis with hemodynamic instability — variceal bleed is the working diagnosis until endoscopy confirms or refutes.
SEVERITY: Hemodynamically unstable (HR 124, SBP <90), high-risk (cirrhosis, coagulopathy, thrombocytopenia, lactate elevated). Glasgow-Blatchford 16: BUN 42 mg/dL ≈ 15 mmol/L → 4; Hgb 7.2 (male, <10) → 6; SBP 88 (<90) → 3; HR 124 (≥100) → 1; hepatic disease → 2; melena, syncope, cardiac failure not reported → 0.

RESUSCITATION:
- 2 large-bore PIVs (16G).
- IV fluids: NS or LR 500 mL bolus, titrate carefully — DO NOT over-resuscitate in variceal bleed (raises portal pressure, worsens bleeding). Target SBP ~90, MAP ~65; do not chase normotension.
- Activate massive transfusion protocol — hemodynamically unstable, ongoing bleeding.
- Type and crossmatch sent.

TRANSFUSION:
- Hgb 7.2 with active variceal bleed and hemodynamic instability — transfuse pRBC. Restrictive Hgb 7 threshold from Villanueva still applies; do not over-transfuse (raises portal pressure). Goal Hgb ~7–8 g/dL during active bleed.
- Platelets 65 with active bleed: transfuse only against the current guidance threshold for cirrhotic/variceal bleeding or a stated endoscopic-procedure requirement, and record that reason [VERIFY: Baveno VII / current AASLD guidance; local transfusion protocol].
- INR 1.8: no FFP, vitamin K or PCC for the INR alone — patient is not on warfarin, and in cirrhosis INR-driven correction is not routinely recommended in variceal bleeding (FFP volume also raises portal pressure) [VERIFY: Baveno VII / current AASLD guidance].
- Note: cirrhosis has "rebalanced hemostasis"; INR does not predict bleeding well. Any product beyond pRBC needs a specific stated reason in this patient.

PHARMACOTHERAPY:
- Octreotide 50 mcg IV bolus NOW, then 50 mcg/h continuous infusion for 3–5 days (splanchnic vasoconstriction reduces portal pressure).
- Pantoprazole 80 mg IV bolus then 8 mg/h infusion (variceal bleeding can be mixed with peptic source and PPI is cheap; will continue or stop based on endoscopic findings).
- Ceftriaxone 1 g IV daily × 7 days (empiric antibiotic prophylaxis in cirrhotic GI bleed — reduces SBP, mortality, rebleed; standard of care).
- Lactulose initiation (later) — encephalopathy risk after large GI bleed in cirrhotic.

ENDOSCOPY TIMING:
- EGD within 12 hours after stabilization. If unstable despite resuscitation, may need urgent EGD with airway protected.
- Endoscopic band ligation is the definitive treatment for variceal bleed.
- If banding fails: balloon tamponade (Sengstaken-Blakemore or Minnesota tube) as bridge; TIPS (transjugular intrahepatic portosystemic shunt) within 24–72 h for failed endoscopic therapy or as first-line in high-risk variceal bleed (early TIPS in selected high-risk patients).

ADJUNCTS:
- Erythromycin 250 mg IV 30–90 min before EGD to improve gastric visualization.
- Airway protection: intubation indicated for active hematemesis with altered mental status, copious bleeding, or imminent endoscopy in agitated patient. Anesthesia and GI coordinated.
- Avoid NG tube in known varices unless directly needed (rarely needed if erythromycin given).

DISPOSITION:
- ICU. Continuous monitoring, frequent vitals, large-bore access, transfusion ongoing, octreotide drip, awaiting EGD.
- GI / hepatology consult immediately.
- IR aware in case TIPS needed.

WORKUP:
- CBC, INR/PTT, fibrinogen, BMP, LFT (full panel for cirrhosis assessment), lactate, type and cross.
- ABG / VBG.
- ECG and troponin (hemodynamically unstable — demand ischemia possible).
- CXR (aspiration assessment).
- MELD-Na for severity / prognosis.
- Ascites: paracentesis with cell count and culture if any concern for SBP (cirrhotic with GI bleed has high SBP rate — that is why ceftriaxone is given empirically).

PITFALLS TO AVOID:
- Over-resuscitation with crystalloid → raises portal pressure → worsens bleeding. Restrictive transfusion strategy and judicious crystalloid.
- Missing variceal source by anchoring on PUD — patient has known large varices; treat as variceal until proven otherwise.
- Forgetting empiric antibiotics in cirrhotic bleed — major omission.
- Aggressively correcting INR in cirrhosis without active bleeding driver — rebalanced hemostasis means INR does not directly predict bleeding.
- Failing to recognize encephalopathy onset post-bleed; protein load from blood + portal-systemic shunting precipitates HE; lactulose proactively.
- Failing to plan TIPS or transfer to TIPS-capable center if endoscopic failure; the window for early TIPS closes if rebleed occurs.
- Discharging without secondary prophylaxis: non-selective beta-blocker + repeat banding cycle.
```
