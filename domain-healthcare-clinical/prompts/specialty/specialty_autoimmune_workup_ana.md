---
title: "Positive ANA and Systemic Autoimmune Workup"
category: domain-healthcare-clinical/specialty
description: "Interpret an ANA by titer and HEp-2 pattern against pretest probability, order the right follow-on autoantibodies and organ screens, and reach a committed disease call (SLE, Sjögren, SSc, myositis, MCTD, drug-induced) or a stop-testing decision."
techniques:
  - ST-02
  - ST-03
  - CM-01
  - RT-02
  - RT-05
difficulty: advanced
tags:
  - rheumatology
  - autoimmune
  - ana
  - specialty-assessment
updated: "2026-09-24"
---

## Objective

Take a positive (or pending) antinuclear antibody and turn it into a decision: either a specific systemic autoimmune diagnosis with organ staging and initial therapy, or a documented reason to stop testing. The prompt weighs titer, HEp-2 pattern, and clinical pretest probability together and chooses follow-on serologies by pattern and phenotype. Distinct from `reasoning/workup_joint_pain_arthritis.md` and `reasoning/workup_rash_differential.md`, which start from a symptom and list ANA among many tests — this prompt starts from the ANA result and owns its interpretation.

## Inputs

- ANA method (indirect immunofluorescence on HEp-2 vs solid-phase/ELISA), titer, pattern (ICAP code if reported)
- Why it was ordered (specific features vs fatigue/nonspecific screening)
- Clinical features: rash (photosensitive, malar, discoid), oral/nasal ulcers, alopecia, inflammatory arthritis, serositis, Raynaud, sclerodactyly, skin thickening, puffy fingers, dysphagia/GERD, sicca, parotid swelling, proximal weakness, mechanic's hands, Gottron papules, heliotrope rash, interstitial lung disease, cytopenias, thrombosis, pregnancy losses, neuropsychiatric events
- Labs available: CBC with differential, creatinine, urinalysis with microscopy, urine protein-to-creatinine ratio, C3/C4, ESR/CRP, CK, LFTs, TSH
- Medications (hydralazine, procainamide, isoniazid, minocycline, TNF inhibitors, others)
- Family history, sex, age, pregnancy plans

## Role

Senior attending rheumatologist answering an e-consult on a positive ANA.

## Reasoning Steps

1. **Set pretest probability before reading the result.** ANA by HEp-2 IIF is sensitive but not specific. Low-titer positives are common in healthy people (roughly a quarter to a third at 1:40; ~5% at 1:160), in older adults, in relatives of patients with autoimmune disease, and in thyroid disease, infection, malignancy, and liver disease. A positive ANA with no compatible clinical features needs no further autoantibody testing.

2. **Read titer and pattern.**
   - Titer ≥1:160 is more meaningful than 1:40–1:80. The 2019 EULAR/ACR SLE classification uses ANA ≥1:80 on HEp-2 cells as its entry criterion.
   - Homogeneous (AC-1): dsDNA, nucleosome, histone → SLE, drug-induced lupus.
   - Speckled (AC-2/4/5): Sm, U1-RNP, SSA/Ro, SSB/La, Scl-70 → SLE, MCTD, Sjögren, SSc.
   - **Dense fine speckled (AC-2, anti-DFS70):** when isolated, argues *against* systemic autoimmune disease.
   - Centromere (AC-3): limited cutaneous SSc, also primary biliary cholangitis overlap.
   - Nucleolar (AC-8/9/10): SSc (Th/To, PM/Scl, U3-RNP).
   - Cytoplasmic (AC-19/20 and others): antisynthetase (Jo-1) and other myositis antibodies, AMA; may be reported "ANA negative." Anti-Ro can be missed on some platforms — send SSA directly if Sjögren or neonatal lupus risk is the question.
   - Solid-phase/ELISA ANA misses some antibodies; confirm with HEp-2 IIF when the result and phenotype disagree.

3. **Order follow-on serologies by phenotype and pattern — not a shotgun panel.**
   - SLE features: anti-dsDNA, anti-Sm, C3, C4, antiphospholipid antibodies (lupus anticoagulant, anticardiolipin, anti-β2GPI), direct Coombs.
   - Sicca: SSA/Ro (Ro52 and Ro60), SSB/La, RF.
   - Raynaud / skin thickening: Scl-70, centromere, RNA polymerase III.
   - Proximal weakness, ILD, mechanic's hands: CK, aldolase, myositis-specific and associated antibody panel (Jo-1 and other antisynthetase, MDA5, Mi-2, TIF1-γ, NXP2, SRP, HMGCR).
   - Raynaud + puffy hands + arthritis + myositis: U1-RNP (high titer supports MCTD).
   - Suspected drug-induced lupus: anti-histone; stop the drug.

4. **Screen organs in every patient with a plausible systemic diagnosis:** CBC with differential, creatinine, urinalysis with microscopy (hematuria, casts), urine protein-to-creatinine ratio, LFTs, CK; chest imaging and PFTs with DLCO if ILD features or SSc/myositis antibodies; echocardiogram if SSc (pulmonary hypertension screening).

5. **Apply the relevant classification criteria as a check, not a gate.** Classification criteria are built for research cohorts; a patient can have the disease and not meet them.
   - **SLE — 2019 EULAR/ACR:** entry ANA ≥1:80; then weighted items, counting only the highest in each domain, total ≥10 with ≥1 clinical item. Clinical domains: constitutional (fever 2); hematologic (leukopenia 3, thrombocytopenia 4, autoimmune hemolysis 4); neuropsychiatric (delirium 2, psychosis 3, seizure 5); mucocutaneous (non-scarring alopecia 2, oral ulcers 2, subacute cutaneous or discoid lupus 4, acute cutaneous lupus 6); serosal (effusion 5, acute pericarditis 6); musculoskeletal (joint involvement 6); renal (proteinuria >0.5 g/24 h 4, class II or V nephritis 8, class III or IV nephritis 10). Immunologic domains: antiphospholipid antibodies 2; complement (low C3 or C4 3, both low 4); SLE-specific antibodies (anti-dsDNA or anti-Sm 6).
   - Use the corresponding ACR/EULAR criteria for Sjögren (2016), SSc (2013), and idiopathic inflammatory myopathy (2017) where relevant.

6. **Commit to a disease call and stage organ involvement.** Name the diagnosis, which organs are involved, and severity (organ-threatening vs non-organ-threatening).

7. **Initial management for what you diagnose.**
   - SLE: hydroxychloroquine ≤5 mg/kg/day actual body weight for all patients unless contraindicated; baseline retinal exam then annual screening from year 5 (sooner with risk factors). Proteinuria >0.5 g/day or active sediment → nephrology for kidney biopsy before induction. Glucocorticoids at the lowest effective dose with a taper plan. Sun protection, vaccination, bone health, cardiovascular risk. Check antiphospholipid status before pregnancy; anti-Ro positivity needs fetal heart monitoring in pregnancy.
   - Other diagnoses: name the first-line agent and the organ monitoring plan.

8. **When the answer is "not autoimmune":** state the ANA is likely incidental, stop further autoantibody testing, do not repeat the ANA, and list the specific new features that should prompt re-evaluation.

9. **Verify.** Confirm each ordered antibody maps to a stated feature or pattern. Check that the classification score counts only the highest item per domain. Confirm organ screening (urinalysis especially) was done before calling disease mild.

## Output Format

```
PRETEST PROBABILITY: [low / intermediate / high — features supporting]

ANA READ: [method, titer, pattern → antibody families implied]

FOLLOW-ON TESTING:
- [antibody/test — reason]
- Do not send: [tests without an indication]

ORGAN SCREEN: [CBC, creatinine, UA/UPCR, LFT, CK, imaging/PFT/echo as indicated — results or orders]

CLASSIFICATION CHECK: [criteria set, itemized score, met/not met]

DIAGNOSIS: [committed call, organ involvement, severity — or "no systemic autoimmune disease"]

PLAN:
- Therapy: [drug, dose, monitoring]
- Referrals: [nephrology biopsy, pulmonology, ophthalmology, etc.]
- Follow-up: [interval, labs]

PITFALLS:
- [low-titer overcalling, DFS70, cytoplasmic/Ro missed, repeat ANA, skipping UA]
```

## Worked Example

**Input:** 29 y/o F, 3 months of symmetric wrist/MCP pain with 1 h of morning stiffness, a photosensitive malar rash sparing the nasolabial folds, and painless oral ulcers. Exam: synovitis of bilateral 2nd–3rd MCPs, malar erythema. ANA 1:640 homogeneous (HEp-2 IIF). CBC: WBC 3.4, Hgb 11.8, Plt 162. Creatinine 0.8. UA: 2+ protein, 8 RBC/hpf, no casts. Not on medications.

**Output:**

```
PRETEST PROBABILITY: High — inflammatory polyarthritis, photosensitive malar rash, oral ulcers, leukopenia in a young woman.

ANA READ: 1:640 homogeneous on HEp-2 → dsDNA/nucleosome/histone family; consistent with SLE. No drug exposure, so drug-induced lupus unlikely.

FOLLOW-ON TESTING:
- Anti-dsDNA, anti-Sm, SSA/SSB (pregnancy counseling), C3, C4.
- Antiphospholipid antibodies (LA, aCL, anti-β2GPI).
- Direct Coombs, reticulocyte count, LDH, haptoglobin (mild anemia).
- Urine protein-to-creatinine ratio, repeat urinalysis with microscopy.
- Do not send: myositis or SSc panels — no features.

ORGAN SCREEN: Leukopenia present; proteinuria and hematuria need quantifying; creatinine normal.

CLASSIFICATION CHECK (2019 EULAR/ACR), provisional on pending labs:
- Entry: ANA 1:640 ≥1:80 ✓
- Musculoskeletal: joint involvement 6
- Mucocutaneous: acute cutaneous lupus 6 (highest item; oral ulcers not added)
- Hematologic: leukopenia 3
- Clinical subtotal 15 → criteria already met (≥10). Renal and immunologic items will add weight and matter for staging.

DIAGNOSIS: Systemic lupus erythematosus with mucocutaneous, musculoskeletal, hematologic, and possible renal involvement. Renal involvement makes this potentially organ-threatening until quantified.

PLAN:
- Hydroxychloroquine 300 mg daily (≤5 mg/kg/day; weight 62 kg). Baseline retinal exam.
- Prednisone 10 mg daily with taper over 6–8 weeks for arthritis and rash, pending renal staging.
- If UPCR >0.5 g/g or active sediment on repeat: urgent nephrology referral for kidney biopsy before induction therapy (class determines mycophenolate vs other regimens).
- Sun protection, contraception counseling (HCQ is pregnancy-compatible; avoid estrogen if antiphospholipid positive), vaccines, lipid and BP screening.
- Follow-up 2–4 weeks with serologies, UPCR, CBC.

PITFALLS:
- Do not stop at "ANA positive" — the urinalysis here is the most important result.
- Oral ulcers do not add to the mucocutaneous score once acute cutaneous lupus counts.
- Do not repeat the ANA to monitor disease; follow dsDNA, complement, UPCR, and CBC.
```
