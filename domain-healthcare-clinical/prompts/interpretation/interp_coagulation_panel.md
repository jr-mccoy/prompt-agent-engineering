---
title: "Coagulation Panel Interpretation"
category: domain-healthcare-clinical/interpretation
description: "Read PT/INR, aPTT, fibrinogen, D-dimer, mixing studies, and platelet count to localize bleeding/clotting disorder and direct workup."
techniques:
  - ST-02
  - ST-03
  - CM-01
  - RT-02
  - RT-05
difficulty: advanced
tags:
  - hematology
  - coagulation
  - bleeding
  - dic
  - interpretation
updated: "2026-05-08"
---

## Objective

Read a coagulation panel and produce a structured interpretation: localize the abnormality to factor deficiency, factor inhibitor, anticoagulant effect, consumptive process, or platelet/vascular issue. Direct the next test and the immediate action when bleeding or thrombosis is active.

## Inputs

- PT and INR
- aPTT
- Fibrinogen
- D-dimer
- Platelet count and MPV (from CBC if available)
- TT (thrombin time), reptilase time, mixing studies, factor levels, anti-Xa, lupus anticoagulant — if available
- Patient context: bleeding or thrombosis presentation, anticoagulant medications (warfarin, DOAC, heparin/LMWH, argatroban, bivalirudin), liver disease, malnutrition/poor PO, recent antibiotics, malignancy, pregnancy, known factor deficiency, transfusion history

## Role

Senior hematologist or ICU attending interpreting coags at the bedside.

## Reasoning Steps

1. **Map abnormalities to pathway.**
   - **Isolated PT/INR elevation:** extrinsic (factor VII) or common pathway. Common causes: warfarin, vitamin K deficiency (early), liver disease (early), factor VII deficiency.
   - **Isolated aPTT elevation:** intrinsic pathway (factors VIII, IX, XI, XII; HMWK, prekallikrein). Common causes: heparin, factor VIII or IX deficiency (hemophilia A or B), vWD (severe — VIII low), lupus anticoagulant (paradoxical — prolonged aPTT but thrombosis), factor XII deficiency (long aPTT, no bleeding).
   - **Both PT and aPTT elevated:** common pathway (factors II, V, X, fibrinogen) or multiple deficiencies. Causes: warfarin (advanced), vitamin K deficiency (advanced), liver disease, DIC, supratherapeutic heparin, direct thrombin or Xa inhibitors (DOACs), massive transfusion, dilutional, congenital (rare).
   - **Both PT and aPTT normal but bleeding:** platelet disorder (count or function), vWD type 1, factor XIII deficiency (poor wound healing), vascular cause, fibrinolysis disorder.

2. **Mixing study.** Mix patient plasma 1:1 with normal plasma; recheck PT or aPTT.
   - **Corrects** → factor deficiency. Order specific factor levels.
   - **Does not correct** → inhibitor. Most commonly lupus anticoagulant (associated with thrombosis, not bleeding) or factor VIII inhibitor (acquired hemophilia — bleeding emergency, often in elderly with autoimmune background or postpartum).

3. **Fibrinogen.**
   - Low (<150): consumption (DIC), severe liver disease, dilutional, congenital afibrinogenemia / dysfibrinogenemia.
   - Below 100 in active bleeding → cryoprecipitate transfusion (10 units pooled or 1 dose) targets ~50–100 mg/dL increase.
   - Pregnancy elevates fibrinogen (normal 400–600 third trimester); a "normal" fibrinogen of 200 in postpartum hemorrhage is actually low.

4. **D-dimer.**
   - Elevated: any active fibrin formation/breakdown — VTE, DIC, sepsis, malignancy, pregnancy, recent surgery/trauma. High sensitivity, low specificity. Useful as a rule-out test for VTE in low pre-test probability with age-adjusted threshold (age × 10 ng/mL for >50 y/o).
   - Markedly elevated D-dimer + low fibrinogen + low platelets + prolonged PT/aPTT + schistocytes → DIC.

5. **DIC scoring (ISTH overt DIC).** Sum:
   - Platelet count: >100 = 0, 50–100 = 1, <50 = 2
   - Fibrin marker (D-dimer): no rise = 0, moderate = 2, strong = 3
   - PT prolongation: <3 sec = 0, 3–6 = 1, >6 = 2
   - Fibrinogen: >100 = 0, <100 = 1
   - **Score ≥5 = overt DIC.** Treat the underlying cause; supportive component therapy if bleeding (platelets <50 with bleeding → transfuse to >50; fibrinogen <100–150 → cryo; INR >1.5–2 with bleeding → FFP; vitamin K). Heparin only in selected thrombotic-predominant DIC.

6. **Specific anticoagulant identification.**
   - **Warfarin:** isolated INR elevation early; both prolonged late. Vitamin K reversal: PO 1–5 mg for INR 4.5–10 without bleeding; IV 5–10 mg + 4-factor PCC (25–50 units/kg by INR and weight) for major bleeding. FFP 10–15 mL/kg if PCC unavailable.
   - **Heparin:** prolonged aPTT primarily (UFH); LMWH typically does not prolong aPTT and requires anti-Xa. Reverse UFH with protamine 1 mg per 100 units of heparin given in last hour (max 50 mg). Reverse LMWH partially with protamine if within ~8 hours.
   - **DOACs:**
     - Direct thrombin inhibitor (dabigatran): elevates aPTT and TT; idarucizumab 5 g IV reverses.
     - Direct Xa inhibitors (apixaban, rivaroxaban, edoxaban): may modestly elevate PT; specific anti-Xa (drug-calibrated) confirms; andexanet alfa or 4F-PCC for major bleeding (andexanet preferred but expensive).
   - **Argatroban:** prolongs aPTT; use in HIT.
   - **Lupus anticoagulant:** prolonged aPTT, mixing study does not correct, dRVVT confirms. Paradoxical — patients clot, do not bleed.

7. **Platelet integration.**
   - Always read coags with platelet count. Bleeding patient with normal coags + low platelets → ITP, TTP, HIT, DIC, drug-induced, sepsis.
   - Bleeding with normal coags + normal platelets → vWD (most common inherited bleeding disorder), platelet function defect (uremia, antiplatelet meds), factor XIII deficiency, vascular.

8. **Liver disease pearls.**
   - Liver synthesizes most coagulation factors AND most natural anticoagulants (protein C, S, antithrombin). The "rebalanced hemostasis" of cirrhosis means INR does not predict bleeding risk well — INR 2.5 in cirrhosis ≠ same bleeding risk as INR 2.5 on warfarin.
   - Do not transfuse FFP based on INR alone in cirrhosis without active bleeding or imminent procedure.

## Output Format

```
PT/INR: [value, prolongation]
aPTT: [value, prolongation]
FIBRINOGEN: [value]
D-DIMER: [value]
PLATELETS: [value]
MIXING STUDY (if reported): [corrects / does not correct]

PATTERN: [extrinsic-only / intrinsic-only / both / consumptive / inhibitor / anticoagulant effect / platelet/vascular]

DIFFERENTIAL (in order given context):
1. [most likely]
2. [next]
3. [next]

ACTION:
- [next test to confirm]
- [reversal / replacement product if bleeding]
- [treat underlying cause]
```

## Worked Example

**Input:** 64 y/o M, day 3 admission for E. coli urosepsis. Started bleeding from IV sites and gums today. Vitals: BP 88/52 on norepi, HR 122, T 38.4. Labs now (from baseline normal on admission): PT 22 (INR 2.1), aPTT 58, fibrinogen 110, D-dimer 12,000, platelets 48 (was 220 on admission), Cr 2.3 (was 1.0). Smear: schistocytes present. No anticoagulants.

**Output:**

```
PT/INR: 22 / 2.1 — prolonged
aPTT: 58 — prolonged
FIBRINOGEN: 110 — low
D-DIMER: 12,000 — markedly elevated
PLATELETS: 48 — moderate-severe thrombocytopenia, dropped from 220
MIXING STUDY: not performed (consumption pattern; mixing study unnecessary at this stage)

PATTERN: Consumptive coagulopathy — both pathways prolonged, low fibrinogen, high D-dimer, dropping platelets, schistocytes, in setting of severe sepsis. ISTH score: platelets 50–100 (1) — actually <50 (2), D-dimer strong rise (3), PT prolonged ~5 sec (1), fibrinogen <100 borderline (count as 0 since 110). Score ~6 → overt DIC.

DIFFERENTIAL:
1. Sepsis-induced overt DIC — diagnosis fits cleanly: gram-negative urosepsis, multi-organ dysfunction (AKI), MAHA features (schistocytes), consumptive coag pattern, active bleeding.
2. Less likely given clinical context: TTP (would have neuro findings, more profound thrombocytopenia, severe MAHA — ADAMTS13 still worth checking), HUS (renal-predominant), HIT (no heparin exposure described, 4Ts low).

ACTION:
- Source control and infection management is the actual treatment for sepsis-DIC. Verify antibiotic coverage matches culture sensitivities; resuscitate hemodynamics.
- Component therapy because patient is actively bleeding:
  - Platelets: transfuse to keep >50 in active bleeding (1 dose apheresis or 6-pack pooled, expect rise of ~30–50K)
  - Fibrinogen: cryoprecipitate 10 units (1 dose), target fibrinogen >150 in active bleeding
  - FFP 10–15 mL/kg (~700–1000 mL for this patient) to address factor depletion since INR 2.1 with active bleeding
  - Vitamin K 10 mg IV (cheap, addresses any concurrent vitamin K depletion from poor PO and antibiotics)
- Recheck full coag panel and CBC q4–6h while bleeding active.
- Heparin is NOT indicated here — bleeding-predominant DIC. Heparin is considered only in thrombosis-predominant DIC (e.g., purpura fulminans, large-vessel thrombosis with acute promyelocytic leukemia).
- Monitor for end-organ ischemia from microvascular thrombi: AKI is established, watch mental status, perfusion, troponin.
- Send ADAMTS13 to definitively rule out TTP since schistocytes are present and the combination of MAHA + thrombocytopenia + AKI + fever + neurologic features (if any develop) is the TTP pentad. If ADAMTS13 unavailable in real time and clinical suspicion for TTP rises, start plasma exchange empirically.
- Avoid further contrast, NSAIDs, nephrotoxins; renally adjust everything.
```
