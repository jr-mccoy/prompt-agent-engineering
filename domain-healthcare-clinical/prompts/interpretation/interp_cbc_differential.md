---
title: "CBC with Differential Interpretation"
category: domain-healthcare-clinical/interpretation
description: "Interpret a complete blood count with differential, identify cytopenia or proliferation patterns, characterize anemia by indices, and direct workup."
techniques:
  - ST-02
  - ST-03
  - CM-01
  - RT-02
  - RT-05
difficulty: intermediate
tags:
  - hematology
  - cbc
  - anemia
  - cytopenia
  - interpretation
updated: "2026-05-08"
---

## Objective

Read a CBC with differential and produce a structured interpretation: which lineages are abnormal, the specific pattern (e.g., microcytic anemia with low retic, neutrophilic leukocytosis with left shift, isolated thrombocytopenia), the leading differential, and the next workup step.

## Inputs

- WBC with differential (neutrophils, lymphocytes, monocytes, eosinophils, basophils — % and absolute), bands/blasts if reported
- RBC count, Hgb, Hct, MCV, MCH, MCHC, RDW
- Reticulocyte count or reticulocyte index if available
- Platelet count, MPV
- Smear comments (if available): schistocytes, spherocytes, target cells, teardrops, blasts, Howell-Jolly, polychromasia, rouleaux, dysplastic features
- Patient context: age, sex, presenting problem, medications (chemo, antibiotics, methimazole, clozapine, valproate), comorbidities, recent infections, transfusion history, bleeding/menstrual history

## Role

Senior internist or hematologist reading the CBC with the chart open.

## Reasoning Steps

1. **Lineage triage.** Walk all three:
   - WBC: leukocytosis (>11), leukopenia (<4), or normal with differential abnormality
   - Hgb: anemia (M <13.5, F <12) or polycythemia (M >17, F >15)
   - Platelets: thrombocytopenia (<150) or thrombocytosis (>450)

2. **WBC abnormalities.**
   - **Neutrophilia (ANC >7.5):** infection (bacterial), inflammation, stress/steroids, smoking, splenectomy, CML (very high counts with left shift, basophilia, eosinophilia). Left shift (bands, metamyelocytes) → bacterial infection or marrow stress. Toxic granulation, Döhle bodies, vacuolization → severe infection.
   - **Neutropenia (ANC <1.5; severe <0.5):** drug-induced (chemo, clozapine, methimazole, sulfa, valproate), viral (HIV, hepatitis, parvo), autoimmune, B12/folate deficiency, marrow infiltration, congenital. ANC <0.5 + fever = febrile neutropenia, treat empirically immediately.
   - **Lymphocytosis:** viral (EBV, CMV, pertussis), CLL (older patients, persistent lymphocytosis with smudge cells).
   - **Lymphopenia:** HIV, steroids, chemo, sepsis, lymphoma.
   - **Monocytosis:** chronic infection (TB, endocarditis), CMML, autoimmune.
   - **Eosinophilia:** parasites, atopy, drug reaction (DRESS), adrenal insufficiency, hypereosinophilic syndrome, eosinophilic GPA.
   - **Basophilia:** myeloproliferative neoplasm (especially CML).
   - **Blasts on differential:** acute leukemia until proven otherwise — urgent heme consult, peripheral smear review, flow cytometry.

3. **Anemia workup by MCV.**
   - **Microcytic (MCV <80):** iron deficiency (high RDW, low ferritin, low Tsat), thalassemia (high RBC count for the Hgb, normal RDW, target cells, abnormal hemoglobin electrophoresis), anemia of chronic disease (low Tsat, normal/high ferritin), sideroblastic, lead toxicity.
   - **Normocytic (MCV 80–100):** acute blood loss, hemolysis (high retic, high LDH, low haptoglobin, high indirect bili — characterize as immune or non-immune with DAT, smear), early iron deficiency, anemia of chronic disease, CKD (low EPO), bone marrow suppression.
   - **Macrocytic (MCV >100):** B12 deficiency (hypersegmented neutrophils, neuro signs), folate deficiency, alcohol, liver disease, hypothyroidism, drugs (MTX, hydroxyurea, AZT), MDS, reticulocytosis (large young RBCs).
   - **Reticulocyte index = retic% × (Hct/45) / maturation factor (1 if Hct >35, 1.5 if 25–35, 2 if 15–25, 2.5 if <15).** RI >2 = appropriate response (hemolysis, blood loss). RI <2 = hypoproliferative (deficiency, marrow problem, EPO deficit).

4. **RDW.** Elevated RDW = mixed population. Iron deficiency raises RDW; thalassemia trait does not — early discriminator.

5. **Polycythemia.**
   - Spurious (hemoconcentration) vs absolute. Check EPO, JAK2 V617F (PV), look for secondary causes (smoking, OSA, COPD, high altitude, EPO-secreting tumor, testosterone).

6. **Platelet abnormalities.**
   - **Thrombocytopenia:** rule out pseudothrombocytopenia (EDTA clumping — repeat citrate tube). Then categorize:
     - Decreased production: marrow suppression, B12/folate, infiltration, congenital
     - Increased destruction: ITP (isolated, normal smear, normal MCV), TTP (MAHA + neuro + renal + fever + thrombocytopenia — schistocytes), HIT (4Ts score), DIC (consumption + fibrin breakdown), drug-induced (heparin, vanc, quinine, sulfa), HUS, antiphospholipid, evans
     - Sequestration: hypersplenism (cirrhosis, lymphoma)
   - **Thrombocytosis:** reactive (infection, inflammation, iron deficiency, post-splenectomy, malignancy) vs primary (ET, PV, CML, MF — check JAK2, CALR, MPL).

7. **Combined cytopenias.**
   - Bicytopenia or pancytopenia raises concern for marrow failure (MDS, aplastic anemia, leukemia, infiltration), hypersplenism, B12/folate, or sepsis with DIC. Smear is essential — ask for it explicitly.

8. **Smear pearls.**
   - Schistocytes → MAHA (TTP, HUS, DIC, malignant HTN, severe pre-eclampsia, HELLP)
   - Spherocytes → AIHA, hereditary spherocytosis
   - Teardrops + nucleated RBCs → marrow infiltration / myelophthisis
   - Target cells → liver disease, thalassemia, post-splenectomy
   - Howell-Jolly bodies → asplenia / hyposplenism
   - Rouleaux → multiple myeloma, inflammation
   - Bite cells → G6PD deficiency
   - Auer rods → AML

## Output Format

```
WBC: [count, ANC, ALC, AMC, AEC] — [pattern]
RBC/HGB: [Hgb, MCV, RDW, retic] — [classification]
PLATELETS: [count, MPV] — [pattern]
SMEAR (if available): [key findings]

PRIMARY ABNORMALITY: [one-line summary]
DIFFERENTIAL (in order of likelihood given context):
1. [most likely]
2. [next]
3. [next]

ACTION:
- [labs / smear review / consult]
- [treatment now if indicated]
- [follow-up cadence]
```

## Worked Example

**Input:** 68 y/o M with fatigue x 3 months, 10 lb weight loss, no overt bleeding. CBC: WBC 4.2 (neut 60%, lymph 30%, mono 8%, eos 2%), Hgb 8.4, MCV 105, RDW 18.5, retic 1.2%, platelets 95. Smear: hypersegmented neutrophils, oval macrocytes, occasional teardrops. BMP normal. No meds.

**Output:**

```
WBC: 4.2 (ANC 2.5, ALC 1.3) — low-normal, no leukocytosis
RBC/HGB: Hgb 8.4, MCV 105 (macrocytic), RDW 18.5 (high, mixed population), retic 1.2% (RI <1, hypoproliferative)
PLATELETS: 95 — mild thrombocytopenia
SMEAR: Hypersegmented neutrophils, oval macrocytes, teardrops

PRIMARY ABNORMALITY: Macrocytic anemia + thrombocytopenia + hypoproliferative response, with hypersegmented neutrophils on smear (megaloblastic features) and occasional teardrops (raising marrow infiltration as a competing concern).

DIFFERENTIAL:
1. B12 deficiency — hypersegmented neutrophils + macrocytic + bicytopenia + hypoproliferative is the classic megaloblastic picture. Causes in this age group: pernicious anemia (autoimmune intrinsic factor), atrophic gastritis, prior gastric surgery, PPI/metformin chronic use, dietary (less common at this age).
2. Folate deficiency — same morphologic picture; alcohol use, malabsorption, MTX, phenytoin.
3. Myelodysplastic syndrome — age, bicytopenia, teardrops should not be ignored. Need bone marrow biopsy to characterize if B12/folate not deficient or if cytopenias persist after replacement.
4. Combined B12 deficiency + early MDS — both can coexist.

ACTION:
- B12 and folate levels now; if B12 borderline (200–400), confirm with methylmalonic acid and homocysteine
- Iron studies, TSH, LDH, haptoglobin, indirect bili (rule out concurrent hemolysis)
- If B12 low: IM cyanocobalamin 1000 mcg daily x 1 week, then weekly x 4 weeks, then monthly. High-dose oral 1000–2000 mcg daily is acceptable alternative if absorption is intact and patient prefers.
- Anti-IF and anti-parietal cell antibodies if pernicious anemia suspected
- Watch K and platelets in first week of B12 replacement (rapid erythropoiesis can cause hypokalemia)
- If cytopenias do not improve after 4 weeks of replacement, or if teardrops/blasts emerge, bone marrow biopsy for MDS
- Heme consult if MDS workup needed
```
