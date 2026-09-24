---
title: "Iron Studies Interpretation"
category: domain-healthcare-clinical/interpretation
description: "Read ferritin, serum iron, TIBC, and transferrin saturation to separate absolute iron deficiency, inflammation, mixed states, and iron overload — with context-specific thresholds (CKD, HF, inflammation), source hunting, and iron repletion dosing."
techniques:
  - ST-02
  - ST-03
  - CM-01
  - RT-02
  - RT-05
difficulty: intermediate
tags:
  - hematology
  - iron-deficiency
  - hemochromatosis
  - anemia
  - interpretation
  - always-tired
  - hidden-blood-loss
updated: "2026-09-24"
related_prompts:
  - domain-healthcare-clinical/prompts/reasoning/workup_anemia.md
  - domain-healthcare-clinical/prompts/interpretation/interp_cbc_differential.md
  - domain-healthcare-clinical/prompts/acute-care/acute_gi_bleed.md
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

Interpret an iron panel and produce a committed classification — absolute iron deficiency, functional deficiency/anemia of inflammation, mixed, iron overload, or non-iron microcytosis — with the source investigation and repletion plan that follows.

Decision support for a licensed clinician: confirm iron product doses, phosphate monitoring and thresholds against the current guideline and local formulary. A symptomatic, bleeding, or unstable patient is escalated now, not after this output.

## When to Use

- A ferritin/iron/TIBC/TSAT panel needs a committed classification, in anemic or non-anemic patients (fatigue, HF, CKD).
- True iron deficiency must be separated from inflammation or a mixed state when ferritin looks "normal".
- A raised ferritin or TSAT raises the question of iron overload.
- Deficiency is confirmed and the source investigation and oral-vs-IV repletion plan are needed.

**Not this prompt if:**

- Anemia is being worked up from the CBC across all mechanisms → `domain-healthcare-clinical/prompts/reasoning/workup_anemia.md`; this prompt reads the iron panel itself, including in non-anemic patients (HF, CKD, fatigue, suspected overload).
- The CBC and smear are the question → `domain-healthcare-clinical/prompts/interpretation/interp_cbc_differential.md`.
- There is active GI bleeding → `domain-healthcare-clinical/prompts/acute-care/acute_gi_bleed.md`.

## Inputs

- Ferritin, serum iron, TIBC (or transferrin), transferrin saturation (TSAT = iron/TIBC × 100) — reference ranges are lab-dependent
- CBC: Hb, MCV, RDW, RBC count, platelets; reticulocyte count and reticulocyte Hb if available
- CRP/ESR; soluble transferrin receptor if available
- Context: age, sex, menstrual status, pregnancy, GI symptoms, NSAID/antiplatelet/anticoagulant use, PPI, bariatric surgery, celiac risk, CKD stage/dialysis, heart failure, transfusion history, alcohol, liver disease, family history of hemochromatosis
- Recent oral or IV iron (date, dose)

## Role

Senior hematology attending supporting the treating clinician.

## Reasoning Steps

1. **Stop and escalate first if:** symptomatic severe anemia (chest pain, dyspnea at rest, syncope, heart failure), hemodynamic instability, active or overt GI bleeding (melena, hematemesis, hematochezia), or features suggesting malignancy (weight loss, dysphagia, change in bowel habit, a mass) — arrange urgent evaluation first (resuscitation and transfusion decision, urgent endoscopy, or suspected-cancer pathway), then interpret the panel. Then **timing and confounders.** Serum iron has diurnal and meal variation — never diagnose from iron alone. Oral iron raises serum iron for hours; IV iron makes ferritin and TSAT uninterpretable for about 4 weeks. Ferritin is an acute-phase reactant (inflammation, infection, liver injury, malignancy raise it). Pregnancy and oral contraceptives raise TIBC.

2. **Absolute iron deficiency.** Ferritin <30 ng/mL is highly specific (<15 essentially diagnostic); TSAT <20%; TIBC high. Microcytosis and high RDW support but may be absent early.

3. **Iron deficiency in inflammation and specific diseases.** With inflammation, ferritin <100 ng/mL with TSAT <20% suggests true deficiency. Heart failure definition: ferritin <100, or 100–299 with TSAT <20%. CKD (non-dialysis): a trial of iron is reasonable when TSAT ≤30% and ferritin ≤500. Soluble transferrin receptor (high in deficiency, normal in inflammation) or sTfR/log ferritin index helps separate mixed states (cutoffs are assay-dependent).

4. **Anemia of inflammation.** Low serum iron, low–normal TIBC, TSAT low–normal, ferritin normal–high. Treat the underlying disease; iron alone will not correct it.

5. **Iron overload.** Fasting TSAT ≥45% + elevated ferritin → HFE genotyping (C282Y homozygosity; compound heterozygotes rarely overload). Ferritin >1,000 ng/mL raises concern for liver fibrosis → hepatology, liver elastography or MRI iron quantification. Secondary overload: transfusion, ineffective erythropoiesis (thalassemia, MDS), chronic liver disease, alcohol. **Hyperferritinemia with normal TSAT** is usually not overload — metabolic dysfunction (MASLD), alcohol, inflammation, malignancy; ferritin >10,000 raises HLH or adult-onset Still disease.

6. **Microcytosis without iron deficiency.** Normal/high ferritin, high RBC count, low RDW, Mentzer index (MCV/RBC) <13 → thalassemia trait → hemoglobin electrophoresis (normal electrophoresis does not exclude alpha-thalassemia trait). Also sideroblastic anemia, lead, anemia of inflammation.

7. **Find the source — iron deficiency is a finding, not a diagnosis.** Men and post-menopausal women: bidirectional endoscopy (colonoscopy + EGD) for GI malignancy. All: celiac serology (tTG-IgA with total IgA), H. pylori, urinalysis for hematuria, menstrual history, blood donation, bariatric surgery. Refractory to oral iron → malabsorption (celiac, atrophic gastritis, PPI, H. pylori), non-adherence, ongoing loss, IRIDA.

8. **Repletion.**
   - **Oral:** ferrous sulfate 325 mg (65 mg elemental) once daily or on alternate days (alternate-day dosing improves fractional absorption and tolerance); take with vitamin C source, apart from PPIs/calcium/tea. Expect reticulocytosis at 7–10 days and Hb rise of roughly 1 g/dL by 2–4 weeks; continue ~3 months after Hb normalizes to refill stores.
   - **IV** when intolerant, malabsorbing, CKD, HF, ongoing losses exceeding oral capacity, second/third trimester, or pre-operative timeline: ferric carboxymaltose 750 mg × 2 doses ≥7 days apart (monitor phosphate), ferric derisomaltose 1,000 mg single dose, iron sucrose 200 mg × 5, or low-molecular-weight iron dextran 1 g.
   - **Total deficit (Ganzoni):** weight (kg) × (target Hb − actual Hb, g/dL) × 2.4 + 500 mg stores.

9. **Pitfalls before signing.** "Normal ferritin" in an inflamed patient; checking ferritin within 4 weeks of IV iron; diagnosing IDA without a source plan; calling overload from ferritin alone; transfusing a stable, well-compensated IDA patient.

## Output Format

```
PANEL: [ferritin, iron, TIBC, TSAT vs lab ranges]
CONFOUNDERS: [inflammation, recent iron, pregnancy, liver disease]
CLASSIFICATION: [absolute deficiency / functional-inflammation / mixed / overload / non-iron microcytosis]
CONTEXT THRESHOLD APPLIED: [general / inflammation / HF / CKD]

SOURCE / CAUSE:
- [investigations in priority order]

ACTION:
- [repletion route, product, dose, total deficit]
- [recheck: test and interval]
- [referral]
```

## Verification

- [ ] Red flags (instability, overt bleeding, symptomatic severe anemia, malignancy features) addressed before the panel is classified.
- [ ] Each value compared with the lab's reference range; ferritin read against CRP/inflammation, and recent oral or IV iron timing noted.
- [ ] The context threshold applied is named (general, inflammation, HF, or CKD) with its source guideline.
- [ ] Every iron deficiency diagnosis is paired with a source plan appropriate to age and sex.
- [ ] IV product and total dose checked against weight, Hb, the Ganzoni deficit, phosphate risk, and local formulary.
- [ ] States what would change the classification (sTfR, repeat fasting TSAT, response to a trial of iron).

## False-Positive Prevention

- **A single low serum iron called iron deficiency.** Serum iron falls with time of day, recent meals, and acute illness; ferritin and TSAT decide.
- **A non-fasting or post-oral-iron TSAT ≥45% called hemochromatosis.** Repeat fasting and off iron before genotyping.
- **Iron prescribed for thalassemia-trait microcytosis because the MCV is low.** Check ferritin first; a normal ferritin with a high RBC count points away from deficiency.
- **HFE C282Y heterozygosity or H63D alone reported as hemochromatosis.** These genotypes rarely cause overload; look for another cause of the raised ferritin.

## Worked Example

**Input:** 67 y/o M, 3 months of fatigue and exertional dyspnea. Weight 80 kg. Hb 9.8 g/dL, MCV 74, RDW 17.5, platelets 420. Ferritin 11 ng/mL, iron 28 µg/dL, TIBC 430 µg/dL, TSAT 6.5%, CRP normal, Cr 1.0. On aspirin 81 mg and omeprazole 20 mg daily (reflux). No overt bleeding. Colonoscopy never done.

**Output:**

```
PANEL: Ferritin 11 (low), iron low, TIBC high, TSAT 6.5% (very low).
CONFOUNDERS: None — CRP normal, no recent iron.
CLASSIFICATION: Absolute iron deficiency anemia (microcytic, high RDW, reactive thrombocytosis).
CONTEXT THRESHOLD APPLIED: General (ferritin <30 diagnostic).

SOURCE / CAUSE:
- Occult GI blood loss until proven otherwise in a 67-year-old man — GI referral for bidirectional endoscopy (colonoscopy + EGD) within weeks, not months.
- Celiac serology (tTG-IgA + total IgA); H. pylori (stool antigen — hold PPI 2 weeks before, or biopsy at EGD).
- Urinalysis for hematuria.
- Aspirin: confirm indication; if primary prevention only, stop.

ACTION:
- IV iron preferred: PPI will blunt oral absorption and endoscopy timeline favors rapid repletion. Ganzoni deficit = 80 × (15 − 9.8) × 2.4 + 500 ≈ 1,500 mg → ferric carboxymaltose 750 mg IV × 2, one week apart (check phosphate before second dose), or ferric derisomaltose 1,000 mg then 500 mg.
- If IV unavailable: ferrous sulfate 325 mg every other day, taken separately from omeprazole.
- CBC and reticulocytes at 2–4 weeks; ferritin/TSAT no sooner than 4–8 weeks after the last IV dose.
- No transfusion — hemodynamically stable, Hb 9.8.
```
