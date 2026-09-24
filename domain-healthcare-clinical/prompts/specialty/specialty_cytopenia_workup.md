---
title: "Cytopenia Workup (Thrombocytopenia, Neutropenia, Bicytopenia, Pancytopenia)"
category: domain-healthcare-clinical/specialty
description: "Work up unexplained thrombocytopenia, neutropenia, or multilineage cytopenias: verify the count, catch the emergencies (TTP, HIT, APL, febrile neutropenia, HLH), classify by mechanism, order the targeted panel, and decide on marrow biopsy and treatment."
techniques:
  - ST-02
  - ST-03
  - CM-01
  - RT-02
  - RT-05
difficulty: advanced
tags:
  - hematology
  - thrombocytopenia
  - neutropenia
  - specialty-assessment
  - low-platelets
  - low-white-count
  - low-blood-counts
updated: "2026-09-24"
related_prompts:
  - domain-healthcare-clinical/prompts/interpretation/interp_cbc_differential.md
  - domain-healthcare-clinical/prompts/reasoning/workup_anemia.md
  - domain-healthcare-clinical/prompts/pharmacology/medicine_anticoagulation_decision_support.md
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

Take a patient with one or more unexplained cytopenias to a mechanism-based diagnosis and plan, the way a hematology consultant does: verify that the cytopenia is real, identify the hematologic emergencies that need action today, classify by production vs destruction vs sequestration vs dilution, order a targeted rather than shotgun workup, decide whether bone marrow examination is needed, and write the treatment and monitoring.

Decision support for a licensed clinician: confirm doses, renal/hepatic adjustment and thresholds against the current guideline and local formulary. A bleeding, febrile neutropenic or unstable patient is escalated now, not after this output.

## When to Use

- Unexplained low platelets or low neutrophils, alone or with anemia (bi- or pancytopenia), on an inpatient or outpatient CBC.
- A falling platelet count in a hospitalized patient where HIT, TTP, DIC or a drug cause has to be sorted out today.
- Deciding whether a patient needs a bone marrow biopsy, and what to send with it.

**Not this prompt if:**
- You need a single CBC read and its pattern named → [`interp_cbc_differential.md`](../interpretation/interp_cbc_differential.md).
- The only abnormality is anemia → [`workup_anemia.md`](../reasoning/workup_anemia.md). This prompt is the consultant-level workup of platelet and neutrophil cytopenias and of any multilineage cytopenia.

## Inputs

- CBC with differential: WBC, ANC, ALC, Hgb, MCV, RDW, platelets, reticulocytes; prior CBCs with dates (trend is essential)
- Peripheral smear: schistocytes, platelet clumps, giant platelets, blasts, promyelocytes/Auer rods, dysplasia (hypolobated/hypogranular neutrophils), teardrops, nucleated RBCs, hypersegmented neutrophils, large granular lymphocytes, spherocytes
- Clinical: bleeding (mucocutaneous vs deep), fevers, infections, B symptoms, lymphadenopathy, splenomegaly, liver disease/alcohol, autoimmune symptoms, thrombosis, neurologic change, pregnancy, diet/bariatric surgery, travel, sexual/HIV risk
- Medications with start dates: heparin (any exposure, including flushes), linezolid, TMP-SMX, beta-lactams, vancomycin, valproate, carbamazepine, clozapine, methimazole/PTU, azathioprine/6-MP, methotrexate, chemotherapy, quinine (including tonic water), NSAIDs, PPIs, checkpoint inhibitors, zinc supplements
- Labs available: BMP, LFTs, LDH, haptoglobin, bilirubin, DAT, PT/INR, aPTT, fibrinogen, D-dimer, ferritin, triglycerides, B12, folate, copper, HIV, HCV, HBV, TSH, ANA, SPEP/free light chains, PNH flow, ADAMTS13, PF4 antibody
- Ancestry (Duffy-null phenotype), family history of low counts

## Role

Senior attending hematologist on consult service supporting the treating (primary) team with a consult note. Fast on emergencies, disciplined on workup, and explicit about when a marrow is and is not needed.

## Reasoning Steps

1. **Verify the cytopenia.**
   - **Stop and escalate now if:** active or intracranial bleeding with severe thrombocytopenia, fever with ANC <0.5, new neurologic change or renal failure with schistocytes, blasts or promyelocytes on the smear, or hemodynamic instability — go directly to the step 2 actions and call hematology; verification continues in parallel.
   - Repeat the count. Review the smear yourself.
   - **Pseudothrombocytopenia:** EDTA-dependent platelet clumping → platelet clumps on smear; repeat in citrate or heparin tube. No workup, no transfusion.
   - **Hemodilution:** after large-volume resuscitation or in late pregnancy (gestational thrombocytopenia, typically >70–80 × 10⁹/L, third trimester, resolves postpartum).
   - **Duffy-null associated neutrophil count** (formerly "benign ethnic neutropenia"): common in people of African and Middle Eastern ancestry, ANC typically 1.0–1.5 × 10⁹/L (occasionally lower), no increased infection risk, stable over years. Recognizing it prevents unnecessary marrows and chemotherapy dose delays. Duffy phenotyping confirms.
   - **Trend:** acute drop (days) vs chronic stable vs progressive. A chronic, stable, isolated mild cytopenia is a different problem from a new one.

2. **Catch the emergencies first — any of these changes today's plan.**
   - **Febrile neutropenia** (ANC <0.5, or expected to fall <0.5, with T ≥38.3 °C once or ≥38.0 °C sustained): blood cultures ×2 and empiric antipseudomonal beta-lactam within 60 min — cefepime 2 g IV q8h, piperacillin-tazobactam 4.5 g IV q6h, or meropenem 1 g IV q8h (renally adjusted); add vancomycin only for specific indications (hemodynamic instability, catheter infection, skin/soft tissue infection, pneumonia, MRSA colonization).
   - **TTP:** thrombocytopenia + microangiopathic hemolysis (schistocytes, high LDH, low haptoglobin, high indirect bilirubin, negative DAT) ± neurologic or renal involvement. PLASMIC score (1 point each: platelets <30, hemolysis, no active cancer, no solid-organ or stem cell transplant, MCV <90, INR <1.5, creatinine <2.0 mg/dL); 6–7 = high probability. Send ADAMTS13 before plasma, then start therapeutic plasma exchange, methylprednisolone 1 g IV daily ×3 (or prednisone 1 mg/kg), and consider caplacizumab and rituximab with hematology. Do not transfuse platelets unless life-threatening bleeding.
   - **HIT:** 4Ts score (Thrombocytopenia magnitude, Timing 5–10 days after heparin or ≤1 day with recent exposure, Thrombosis, oTher causes) — 0–3 low (HIT very unlikely), 4–5 intermediate, 6–8 high. Intermediate/high → stop all heparin including flushes, start non-heparin anticoagulant (argatroban, bivalirudin, fondaparinux, or a DOAC in stable patients), send PF4-heparin antibody ± functional assay (SRA). No warfarin until platelets recover; no platelet transfusion unless bleeding.
   - **Acute leukemia / APL:** circulating blasts, or promyelocytes with Auer rods ± DIC (low fibrinogen, high INR) → APL is a medical emergency: start ATRA on suspicion before genetic confirmation, aggressive cryoprecipitate/platelet/plasma support (fibrinogen >150 mg/dL, platelets >30–50 × 10⁹/L), urgent hematology.
   - **DIC:** consumptive coagulopathy in sepsis, trauma, obstetric catastrophe, malignancy → treat the driver; transfuse to bleeding/procedure thresholds. ISTH DIC score if needed.
   - **HLH:** persistent fever, splenomegaly, bi/pancytopenia, ferritin very high (often >10,000 ng/mL is striking), hypertriglyceridemia, low fibrinogen, transaminitis → HScore / HLH-2004 criteria, soluble IL-2 receptor, marrow; hematology urgently.
   - **Severe aplastic anemia:** pancytopenia with low retic, empty marrow — isolate, avoid transfusions from family members (risk of sensitization against a potential sibling HSCT donor); use irradiated, leukoreduced products; refer to a transplant center.

3. **Classify by mechanism.**
   - **Decreased production:** nutritional (B12, folate, copper — especially after bariatric surgery or with zinc excess), alcohol, drugs, viral (HIV, HCV, parvovirus B19, EBV, CMV), marrow failure (aplastic anemia, PNH), clonal (MDS, CCUS), infiltration (leukemia, lymphoma, myeloma, metastatic carcinoma, myelofibrosis, granulomatous disease).
   - **Increased destruction/consumption:** immune (ITP, drug-induced immune thrombocytopenia or neutropenia, SLE, Evans syndrome), MAHA (TTP, HUS, DIC, HELLP, malignant hypertension), HIT, infection/sepsis.
   - **Sequestration:** hypersplenism (cirrhosis/portal hypertension, splenomegaly from any cause) — typically mild-moderate, platelets usually >40–50 × 10⁹/L.
   - **Clues:** macrocytosis + cytopenias → B12/folate, alcohol, liver disease, MDS, drugs (methotrexate, azathioprine, hydroxyurea), copper deficiency; teardrops + nucleated RBCs (leukoerythroblastic) → infiltration/fibrosis; large granular lymphocytes + neutropenia ± RA → LGL leukemia/Felty.

4. **Order a targeted panel — tier by what the pattern suggests.**
   - **Tier 1 (almost all):** repeat CBC with smear review, retic, BMP, LFTs, LDH, haptoglobin, bilirubin, PT/INR, aPTT, fibrinogen, B12, folate, HIV, HCV, HBV (also needed before rituximab/immunosuppression).
   - **Tier 2 (by pattern):** copper and zinc (neuropathy, bariatric surgery, zinc supplements, unexplained anemia + neutropenia), DAT (hemolysis or Evans), ANA ± anti-dsDNA (young women, other autoimmune features), TSH, SPEP/free light chains (age >50, anemia, renal dysfunction), ferritin/triglycerides/fibrinogen (HLH), PNH flow cytometry (hemolysis + cytopenia, thrombosis at unusual sites, aplastic anemia), H. pylori (adult ITP — eradication can raise platelets in some populations), abdominal ultrasound for spleen size and liver morphology, parvovirus/EBV/CMV PCR.
   - Avoid shotgun testing — antiplatelet antibody assays are not useful for ITP diagnosis.

5. **Decide on bone marrow aspirate and biopsy.** Indicated when:
   - Blasts, promyelocytes, dysplasia, or leukoerythroblastic smear.
   - Unexplained bi/pancytopenia after tier 1–2 workup, or progressive cytopenias.
   - Suspected MDS, aplastic anemia, infiltrative disease, HLH, or LGL leukemia (flow can be peripheral).
   - Isolated thrombocytopenia with atypical features for ITP (age >60, systemic symptoms, abnormal other lineages, failure of first-line therapy) — typical ITP does not need a marrow.
   - Send: aspirate morphology, core biopsy with reticulin, flow cytometry, cytogenetics/karyotype, FISH as indicated, myeloid NGS panel.

6. **Treat by diagnosis.**
   - **ITP (adult):** treat if platelets <30 × 10⁹/L or bleeding (ASH 2019 guideline). Prednisone 1 mg/kg/day (max ~80 mg) for ≤6 weeks including taper, or dexamethasone 40 mg daily × 4 days; add IVIG 1 g/kg (repeat day 2 if needed) for bleeding or rapid rise before a procedure. Second line: thrombopoietin receptor agonists (eltrombopag, romiplostim, avatrombopag), rituximab, fostamatinib, splenectomy (delayed ≥12 months where possible).
   - **Drug-induced:** stop the drug; platelet or neutrophil recovery typically within 5–10 days of the offending agent (longer for long half-life drugs). Clozapine agranulocytosis → stop permanently, G-CSF in selected cases, no rechallenge.
   - **Nutritional:** B12 1000 µg IM daily × 1 week, weekly × 4 weeks, then monthly (or oral 1000–2000 µg daily if absorption intact); folate 1 mg daily after B12 repleted/excluded; copper replacement and stop excess zinc.
   - **Hypersplenism:** usually no treatment; manage portal hypertension; TPO-RA (avatrombopag, lusutrombopag) before planned procedures in chronic liver disease.
   - **MDS, aplastic anemia, leukemia, LGL, HLH:** hematology-directed disease therapy.

7. **Transfusion and safety thresholds.**
   - Platelets: prophylactic <10 × 10⁹/L (stable, hypoproliferative); <20 with fever/sepsis per many protocols; ≥50 for most invasive procedures and major bleeding; ≥100 for neurosurgery/CNS bleeding; central line insertion commonly <20 threshold for transfusion. Thresholds differ by society and procedure — state the one used. Avoid prophylactic platelet transfusion in TTP and HIT.
   - Neutropenia: neutropenic precautions (hand hygiene, no rectal temperatures), G-CSF only for specific indications (chemotherapy-induced with high risk, severe congenital neutropenia, selected drug-induced).
   - Hold IM injections and antiplatelets when platelets are markedly low; reassess anticoagulation (commonly held <50 × 10⁹/L unless high thrombotic risk — individualize).

## Output Format

```
VERIFICATION: [repeat count, smear review, pseudothrombocytopenia/Duffy-null/hemodilution excluded or present, trend]

LINEAGES AFFECTED: [platelets / neutrophils / RBC — severity grade]

EMERGENCY SCREEN:
- Febrile neutropenia: [ ]
- TTP (PLASMIC [score]): [ ]
- HIT (4Ts [score]): [ ]
- APL / acute leukemia: [ ]
- DIC / HLH / severe aplastic anemia: [ ]
- Immediate actions: [ ]

MECHANISM: [production / destruction / sequestration / dilution — supporting findings]

DIFFERENTIAL (ranked):
1. [ ]
2. [ ]
3. [ ]

WORKUP:
- Tier 1: [ ]
- Tier 2 (pattern-driven): [ ]
- Bone marrow: [indicated / not indicated — reason; studies to send]

TREATMENT:
- [drug, dose, route, duration; drug discontinuations]

TRANSFUSION / SAFETY: [thresholds applied; anticoagulation/antiplatelet decisions; precautions]

MONITORING: [CBC frequency, response criteria, follow-up]

PITFALLS TO AVOID:
- [ ]
```

## Verification

- [ ] Pseudothrombocytopenia, hemodilution and Duffy-null associated neutrophil count were considered, and the cytopenia was confirmed on repeat count and smear before any workup.
- [ ] Every emergency in step 2 is marked present or excluded, with PLASMIC and 4Ts itemized from the actual inputs.
- [ ] Each ordered test maps to a stated mechanism or pattern, and the bone marrow decision is explicit with its reason.
- [ ] Transfusion and anticoagulation thresholds name the society or protocol applied; antimicrobial and anticoagulant doses are adjusted for weight, renal and hepatic function — confirm doses, renal adjustment and thresholds against the current guideline and local formulary.
- [ ] Drug causes are checked against start dates, and the output states which result would change the leading diagnosis.

## False-Positive Prevention

- **A drug blamed by association.** A drug started long before a stable count, or after the count had already fallen, is an unlikely cause; match onset to exposure before stopping a needed medication.
- **HIT pursued despite a low 4Ts score.** A 4Ts of 0–3 makes HIT very unlikely; sending PF4 antibodies and switching anticoagulant anyway invites false-positive results and harm from non-heparin agents.
- **A positive PF4 ELISA read as HIT.** Low-OD positives are common after surgery and heparin exposure; interpret the optical density and confirm with a functional assay when pretest probability is not high.
- **A mild, stable cytopenia sent straight to marrow.** Mild isolated thrombocytopenia or neutropenia that is stable over years with a normal smear usually needs trend and surveillance, not biopsy.
- **Consumptive, splenic or marrow causes labeled ITP.** ITP is a diagnosis of exclusion; sepsis, liver disease and hypersplenism explain many low platelets in hospitalized patients.

## Worked Example

**Input:** 71 y/o M, post-op day 7 after total knee arthroplasty, on enoxaparin 40 mg SC daily since POD 0 (no heparin in the prior 100 days). Platelets: pre-op 245, POD 1 210, POD 3 198, POD 7 82 × 10⁹/L. New painful swollen left calf today; duplex shows left popliteal DVT. Hgb 10.8 (post-op, stable), WBC 8.1. No sepsis, INR 1.1, fibrinogen 420. Smear: no clumps, no schistocytes. Meds also include cefazolin (stopped POD 1), acetaminophen, oxycodone.

**Output:**

```
VERIFICATION: Citrate repeat 80 × 10⁹/L; smear without clumps or schistocytes. Real, isolated, new thrombocytopenia — a >50% fall (61% from the POD 1 value of 210; 67% from the pre-op 245), nadir well above 20.

LINEAGES AFFECTED: Platelets only (moderate). Hgb stable post-op; WBC normal.

EMERGENCY SCREEN:
- Febrile neutropenia: no.
- TTP: no MAHA (no schistocytes), PLASMIC not applicable.
- HIT: 4Ts — Thrombocytopenia >50% fall, nadir ≥20 = 2; Timing onset day 5–10 = 2; Thrombosis new DVT = 2; oTher causes — none convincing (cefazolin stopped day 1, no sepsis, no DIC) = 2. Total 8 → high probability.
- APL/leukemia, DIC, HLH: no (normal fibrinogen/INR, no blasts).
- Immediate actions: stop enoxaparin now; remove any heparin flushes/heparin-coated lines; start argatroban 2 µg/kg/min IV (reduce to 0.5–1.2 µg/kg/min if hepatic dysfunction or critical illness), titrate to aPTT 1.5–3× baseline. Alternative in this stable patient: fondaparinux 7.5 mg SC daily (weight 50–100 kg; CrCl adequate) or a DOAC (e.g., rivaroxaban 15 mg BID × 21 days then 20 mg daily).
- Send PF4-heparin antibody ELISA and, if OD intermediate, serotonin release assay. Do not wait for results to change anticoagulant.

MECHANISM: Immune-mediated platelet activation and consumption (HIT type II) with thrombosis (HITT).

DIFFERENTIAL (ranked):
1. HIT with thrombosis — 4Ts 8, classic timing and DVT.
2. Post-operative hemodilution/consumption — would occur days 1–3 and recover, not fall on day 7.
3. Drug-induced immune thrombocytopenia (non-heparin) — cefazolin stopped day 1; unlikely.

WORKUP:
- Tier 1: CBC daily, smear, PT/INR, fibrinogen, BMP, LFTs (argatroban is hepatically cleared).
- Bilateral lower-extremity duplex (done: left DVT); assess upper extremities if lines present — HIT thrombosis is frequently multifocal.
- Bone marrow: not indicated.

TREATMENT:
- Non-heparin anticoagulation as above, at therapeutic (not prophylactic) intensity because thrombosis is present.
- Warfarin only after platelets ≥150 × 10⁹/L, overlapping ≥5 days with argatroban and until INR therapeutic for 24 h (argatroban raises INR — use a protocol for transition), or transition directly to a DOAC.
- Duration: 3 months of anticoagulation for HIT with thrombosis (provoked DVT).
- Allergy list: "Heparin — HIT (confirmed/suspected, date)" — avoid heparin for future exposures; re-exposure beyond ~100 days after antibody clearance is sometimes permitted for cardiac surgery only under hematology guidance.

TRANSFUSION / SAFETY: No platelet transfusion — not bleeding, and platelets may fuel thrombosis in HIT. Hold NSAIDs.

MONITORING: Daily CBC until platelets >150; expected recovery within ~1 week. Daily aPTT on argatroban. Watch for new limb ischemia, skin necrosis at injection sites, adrenal hemorrhage (abdominal/flank pain, hypotension).

PITFALLS TO AVOID:
- Do not wait for the PF4 antibody to stop heparin when 4Ts is intermediate or high.
- Do not "switch to prophylactic dose" — HIT with thrombosis needs therapeutic non-heparin anticoagulation.
- Do not start warfarin at low platelet counts — protein C depletion can cause venous limb gangrene.
- Do not assume LMWH is safe — enoxaparin causes HIT, less often than unfractionated heparin but not rarely.
```
