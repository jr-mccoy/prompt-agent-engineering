---
title: "Thrombophilia Workup (Inherited and Acquired)"
category: domain-healthcare-clinical/specialty
description: "Decide whether thrombophilia testing will change management after VTE or unusual-site thrombosis, choose the panel, time each assay around anticoagulation and the acute event, and act on the result — antiphospholipid syndrome first."
techniques:
  - ST-02
  - ST-03
  - CM-01
  - RT-02
  - RT-05
difficulty: advanced
tags:
  - hematology
  - thrombosis
  - antiphospholipid-syndrome
  - specialty-assessment
updated: "2026-09-24"
---

## Objective

Produce a hematology consult answer to "should this patient get a thrombophilia workup?": decide whether any result would change anticoagulant choice, duration, or family counseling; order only the tests that would; time each assay so it is interpretable; and state the management consequence of each possible result. Distinct from `pharmacology/medicine_anticoagulation_decision_support.md` and `pharmacology/pharm_doac_selection_by_profile.md`, which choose and dose the anticoagulant once the indication is settled — this prompt decides what testing is worth doing and how it reshapes that indication.

## Inputs

- Index event: DVT/PE, site (lower limb, upper limb, cerebral venous, splanchnic/portal/hepatic, arterial), date, imaging
- Provocation: major transient (surgery, trauma, immobilization ≥3 days), minor transient (estrogen, pregnancy/postpartum, long travel), persistent (active cancer, IBD), or unprovoked
- Prior thrombotic events, pregnancy morbidity (losses ≥10 weeks, ≥3 early losses, preterm delivery for preeclampsia/placental insufficiency)
- Family history: first-degree relatives with VTE, age at event, known thrombophilia in the family
- Current anticoagulant (heparin, LMWH, warfarin, DOAC) and start date
- Baseline labs: CBC (cytopenias, erythrocytosis, thrombocytosis), aPTT before anticoagulation, LFTs, creatinine, urinalysis, hemolysis markers
- Clinical clues: livedo, thrombocytopenia, SLE features, hemolysis, hemoglobinuria, splenomegaly, age-appropriate cancer screening status
- The decision on the table: stop vs continue anticoagulation, drug choice, estrogen or pregnancy plans, relative testing

## Role

Senior attending hematologist answering a thrombosis consult for a colleague. Commits to what to test, when, and what each answer changes.

## Reasoning Steps

1. **Name the decision the test would change.** If none, recommend no testing and say why. Most inherited thrombophilia results do not change duration after a first VTE: a provoked event with a major transient factor gets time-limited therapy regardless; an unprovoked proximal DVT/PE usually warrants extended therapy regardless. Test when the answer changes drug choice (APS → warfarin), duration (a borderline case where a strong thrombophilia tips toward extended therapy), pregnancy/estrogen planning, or testing of relatives.

2. **Screen for antiphospholipid syndrome first** — the one result that most often changes the drug.
   - Test when: unprovoked VTE in a younger patient, arterial thrombosis under ~50, thrombosis at an unusual site, recurrent VTE, pregnancy morbidity as above, SLE or other autoimmune disease, unexplained prolonged baseline aPTT, livedo, or thrombocytopenia.
   - Panel: lupus anticoagulant (two tests on different principles — dRVVT plus an LA-sensitive aPTT), anticardiolipin IgG/IgM, anti-β2-glycoprotein I IgG/IgM.
   - Persistence: a positive result must be repeated ≥12 weeks apart before labeling APS.
   - Risk profile: triple positivity (LA + aCL + anti-β2GPI) and high titers carry the highest thrombotic risk.

3. **Time each assay around the event and the anticoagulant.**
   - Genetic tests (factor V Leiden, prothrombin G20210A by PCR) are unaffected by acute thrombosis or any anticoagulant — can be sent at any time.
   - Antithrombin activity: lowered by acute thrombosis and by heparin; defer until off heparin.
   - Protein C and protein S (free protein S antigen preferred): lowered by warfarin, acute thrombosis, liver disease; protein S also by pregnancy and estrogen. Defer until ≥2 weeks off warfarin and after the acute phase.
   - Lupus anticoagulant: DOACs and warfarin cause false positives (and sometimes false negatives); test before anticoagulation starts, or use a DOAC-adsorbent pretreatment if the laboratory offers one, and interpret any on-therapy LA cautiously. aCL and anti-β2GPI immunoassays are not affected by anticoagulants.
   - DOACs can also distort clot-based protein C/S and APC-resistance assays and some antithrombin assays; confirm with the lab which methods are interpretable on the current drug.

4. **Unusual-site thrombosis adds its own panel.**
   - Splanchnic (portal, mesenteric, hepatic vein/Budd-Chiari) or cerebral venous thrombosis: JAK2 V617F (then CALR/MPL if negative and MPN still suspected), PNH flow cytometry (FLAER/CD59) especially with cytopenias, hemolysis, or iron deficiency, APS panel, and local factors (cirrhosis, pancreatitis, intra-abdominal infection, head/neck infection).
   - Arterial thrombosis in a young patient: APS panel; inherited venous thrombophilias add little.

5. **Cancer screening in unprovoked VTE:** history, exam, CBC, CMP, chest X-ray, and age/sex-appropriate screening are up to date. Routine extensive CT screening has not been shown to improve outcomes; escalate only for specific clues.

6. **Interpret results and assign consequence.**
   - Confirmed APS with venous thrombosis: warfarin, INR 2–3, generally indefinite; avoid DOACs in high-risk (especially triple-positive) APS and in arterial APS.
   - Heterozygous factor V Leiden or prothrombin mutation: weak risk factors; do not by themselves extend therapy after a provoked event; relevant to estrogen avoidance and pregnancy prophylaxis decisions.
   - Antithrombin deficiency, homozygous or compound heterozygous FVL/PT, protein C or S deficiency confirmed on repeat: stronger risk; supports extended therapy in borderline cases and pregnancy prophylaxis; test first-degree relatives when it would change their estrogen or pregnancy decisions.
   - JAK2-positive: MPN workup and hematology management (cytoreduction, aspirin as indicated) in addition to anticoagulation.
   - PNH clone: hematology for complement inhibition; anticoagulation.
   - A single low protein C/S/AT value is not a diagnosis — repeat off confounders.

7. **Verify before signing.** For every test ordered, state the decision it serves. For every abnormal result, confirm the patient was off the interfering drug and outside the acute phase. Do not label APS from one positive test or inherited deficiency from one on-therapy level.

## Output Format

```
DECISION AT STAKE: [what a result would change — or "none: no testing"]

EVENT CLASSIFICATION: [site; provoked (major/minor transient, persistent) vs unprovoked; recurrence]

TESTING PLAN:
- Send now: [assay — why — unaffected by current therapy]
- Defer: [assay — until when — what interferes]
- Do not send: [assay — why it would not change management]

UNUSUAL-SITE ADD-ONS: [JAK2 / PNH / local factors, or N/A]

RESULT → ACTION MAP:
- If [result]: [drug, duration, family/pregnancy consequence]

ANTICOAGULATION NOW: [agent, dose, planned duration pending results]

PITFALLS:
- [timing/interference errors, single-test labeling, testing that changes nothing]
```

## Worked Example

**Input:** 41 y/o M, unprovoked right femoral DVT and segmental PE 4 months ago, on apixaban 5 mg BID. Mother had a DVT at 55. Baseline aPTT drawn in the ED before heparin was 44 s (ref 25–35). Platelets 128. Mild livedo reticularis on the thighs. No autoimmune history. Asks whether he can stop anticoagulation at 6 months.

**Output:**

```
DECISION AT STAKE: Drug choice. Duration is already settled — an unprovoked proximal DVT with PE in a man gets extended anticoagulation whatever the inherited panel shows. The unexplained baseline aPTT prolongation, mild thrombocytopenia, and livedo raise APS, which would move him from apixaban to warfarin.

EVENT CLASSIFICATION: First unprovoked proximal DVT + PE.

TESTING PLAN:
- Send now: anticardiolipin IgG/IgM and anti-β2GPI IgG/IgM (immunoassays, unaffected by apixaban).
- Send now with caveat: lupus anticoagulant (dRVVT + LA-sensitive aPTT) only if the lab uses DOAC-adsorbent pretreatment; otherwise draw at apixaban trough and treat a positive LA as provisional.
- Repeat all positive APS tests at ≥12 weeks.
- Do not send: protein C, protein S, antithrombin, FVL, prothrombin mutation. None changes his extended-therapy plan, and protein C/S/AT are unreliable on anticoagulation. His mother's DVT at 55 does not change this.

UNUSUAL-SITE ADD-ONS: N/A (typical site). CBC repeat and smear for the thrombocytopenia.

RESULT → ACTION MAP:
- Persistent triple positivity (or LA + high-titer antibody): switch apixaban to warfarin, INR goal 2–3, indefinite; overlap with LMWH until INR ≥2 on two consecutive days.
- Single low-titer antibody, LA negative, not persistent: stay on apixaban, extended duration; consider reduced-dose apixaban 2.5 mg BID after 6 months of full dose.
- All negative: extended apixaban; rheumatology review only if other autoimmune features emerge.

ANTICOAGULATION NOW: Continue apixaban 5 mg BID. Do not stop at 6 months.

PITFALLS:
- An LA drawn on a DOAC without adsorbent is uninterpretable.
- One positive antiphospholipid test is not APS; the 12-week repeat is required.
- A full inherited panel here would spend money and create false "deficiencies" without changing management.
```
