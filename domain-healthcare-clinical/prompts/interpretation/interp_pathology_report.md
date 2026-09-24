---
title: "Surgical Pathology Report Interpretation"
category: domain-healthcare-clinical/interpretation
description: "Read a surgical pathology or cytology report — diagnosis language, adequacy, grade, margins, nodes, pTNM, biomarkers, addenda — check radiology-pathology concordance, and commit to the treatment, testing, and surveillance each element triggers."
techniques:
  - ST-02
  - ST-03
  - CM-01
  - RT-02
  - RT-05
difficulty: advanced
tags:
  - oncology
  - pathology
  - cancer-staging
  - biomarkers
  - interpretation
  - biopsy-results
  - new-cancer-diagnosis
  - breast-cancer
updated: "2026-09-24"
related_prompts:
  - domain-healthcare-clinical/prompts/reasoning/workup_lymphadenopathy.md
  - domain-healthcare-clinical/prompts/specialty/medicine_oncology_case_framer.md
  - domain-healthcare-clinical/prompts/pathophysiology/patho_oncogenesis_tumor_biology.md
---

## Objective

Read a pathology report element by element, translate the diagnostic language into a clinical decision, identify what is missing or pending, check concordance with imaging and the clinical picture, and commit to the next step — re-biopsy, further surgery, systemic therapy referral, biomarker or germline testing, tumor board, or surveillance interval.

Decision support for a licensed clinician: confirm staging, biomarker cut-offs, testing criteria, and any doses against the current guideline (AJCC, CAP, tumor-specific) and local formulary. A critical or unexpected malignant result is communicated to the treating team now, not after this output.

## When to Use

- A final surgical pathology, biopsy, or cytology report is back and you need it translated into the next decision.
- Checking a report for missing elements, pending addenda, or radiology–pathology discordance before acting.
- Deciding which biomarker, genomic, or germline testing the result triggers.
- Setting a surveillance interval from a benign or premalignant result (polyps, thyroid FNA, cervical cytology).

**Not this prompt if:**
- The task is presenting the whole cancer case to tumor board — use `domain-healthcare-clinical/prompts/specialty/medicine_oncology_case_framer.md`.
- The report is a microbiology culture — use `domain-healthcare-clinical/prompts/interpretation/interp_microbiology_culture_sensitivity.md`.
- The question is choosing or explaining the chemotherapy regimen — use `domain-healthcare-clinical/prompts/pharmacology/pharm_chemotherapy_regimen_explainer.md`.

## Inputs

- Pathology report: specimen and procedure (core biopsy, FNA, excision, resection), laterality, diagnosis line, microscopic description, synoptic (CAP-style) summary, ancillary studies, comments, addenda/amendments, date
- For cancer: histologic type, grade, size, margins (closest distance, which margin), lymphovascular and perineural invasion, lymph nodes (positive/examined, size of deposit, extranodal extension), pTNM with prefix (y, r), treatment effect after neoadjuvant therapy
- Biomarkers: ER/PR/HER2, Ki-67, MMR/MSI, PD-L1 (assay and score type), driver mutations (EGFR, ALK, ROS1, KRAS, BRAF, etc.), others by tumor
- For benign/premalignant: polyp histology, size, number, dysplasia grade; cytology category (e.g., Bethesda thyroid)
- Clinical context: imaging findings and category (e.g., BI-RADS), age, menopausal status, family history, prior treatment, performance status

## Role

Senior oncology attending (surgical or medical, as the specimen dictates) supporting the treating clinician; reads the final report with the chart open and commits to actions they can verify.

## Reasoning Steps

1. **Identity and specimen.** Correct patient, laterality, site, procedure, and date. Preliminary/frozen-section diagnoses are provisional. Check for addenda (biomarkers often arrive as addenda) and amendments that change the diagnosis.

   **Stop and escalate if:** a critical or unexpected result (new malignancy not anticipated, malignancy in a specimen sent as benign, infection such as TB or fungus in tissue) — confirm it has been communicated to the treating team promptly and documented; a diagnosis that is discordant with the clinical or imaging picture, or a wrong-patient/laterality mismatch — request pathology review before anyone acts on it.

2. **Translate diagnostic language.** "Diagnostic of" / "consistent with" → act. "Suggestive of" / "suspicious for" / "atypical" → not definitive; usually more tissue before definitive oncologic surgery or chemotherapy. "Non-diagnostic" or "insufficient" → re-sample, not reassurance.

3. **Sampling and concordance.** Core biopsy and FNA undersample: grade can rise and invasive components can appear at resection. A benign result that does not explain the imaging (e.g., a BI-RADS 5 mass with benign core) is discordant → repeat biopsy or excision. Likewise, a diagnosis that does not fit the clinical picture → request pathology re-review or second opinion.

4. **Tumor characteristics.** Histologic type, grade, size (pathologic size may differ from imaging), LVI, PNI — each feeds adjuvant decisions.

5. **Margins.** Positive vs close vs negative, and which margin. Adequate margin definitions are tumor- and context-specific (e.g., "no ink on tumor" for invasive breast cancer with breast-conserving surgery and radiation); a positive margin → re-excision or radiation boost discussion. A close margin against a fascial plane may need no further surgery.

6. **Nodes.** Number positive / examined; macro- vs micrometastasis vs isolated tumor cells; extranodal extension. Too few nodes examined can understage.

7. **Stage.** Pathologic stage (pTNM) requires the resection; a biopsy alone gives clinical stage. Use the prefix correctly (ypTNM after neoadjuvant therapy is prognostic in its own right). For cancers with prognostic stage groups (e.g., breast in AJCC 8th edition), compute both anatomic and prognostic stage.

8. **Biomarkers — interpret by assay rules.**
   - **Breast HER2:** IHC 3+ positive; 2+ equivocal → ISH decides; IHC 1+ or 2+/ISH-negative = HER2-low (relevant for HER2-directed antibody–drug conjugates in metastatic disease).
   - **MMR/MSI:** deficient MMR in colorectal or endometrial cancer → Lynch evaluation (MLH1/PMS2 loss → MLH1 promoter hypermethylation or BRAF V600E testing to separate sporadic from germline); also predicts immunotherapy benefit in advanced disease.
   - **PD-L1:** score type (TPS vs CPS) and assay are tumor- and drug-specific — do not transfer thresholds between them.
   - **NSCLC:** broad molecular panel before first-line systemic therapy in advanced non-squamous disease.
   - **Pending markers:** list them and do not finalize therapy until back.

9. **Germline testing triggers.** Apply current criteria by tumor (e.g., all ovarian, pancreatic, and metastatic prostate cancers; breast cancer — per ASCO–SSO 2024, offer BRCA1/2 testing to all newly diagnosed patients aged ≤65 and to selected patients >65 (personal/family history, ancestry, triple-negative, PARP-inhibitor eligibility); dMMR tumors not explained by methylation; strong family history).

10. **Benign/premalignant outputs.** Colon polyps — surveillance interval by number, size, histology, and dysplasia per current US Multi-Society Task Force guidance (e.g., 1–2 tubular adenomas <10 mm → 7–10 years; adenoma ≥10 mm, villous component, or high-grade dysplasia → 3 years). Thyroid FNA Bethesda category → management tier. Cervical cytology → risk-based colposcopy pathway.

11. **Pitfalls before signing.** Acting on a frozen section as final; missing the addendum with the biomarker that changes therapy; treating "suspicious for" as diagnostic; accepting a discordant benign biopsy; quoting clinical stage as pathologic; applying PD-L1 cutoffs across assays; incidental findings in the specimen (e.g., appendiceal neuroendocrine tumor) left unaddressed.

## Output Format

```
SPECIMEN: [procedure, site, laterality, date, final vs preliminary, addenda]
DIAGNOSIS (translated): [definitive / suggestive / non-diagnostic — what it means]
CONCORDANCE: [imaging and clinical fit — concordant / discordant]
TUMOR: [type, grade, size, LVI, PNI]
MARGINS: [status, closest margin and distance — adequate Y/N]
NODES: [positive/examined, deposit size, ENE]
STAGE: [pTNM (prefix) → anatomic stage; prognostic stage if applicable]
BIOMARKERS: [results with interpretation; pending list]
MISSING / PENDING: [what must come back before decisions]

ACTION:
1. [surgical / re-biopsy]
2. [systemic therapy referral / expected pathway]
3. [radiation]
4. [genomic / germline testing]
5. [tumor board, surveillance interval]
```

## Verification

- [ ] Critical or discordant results flagged and their communication confirmed before routine interpretation.
- [ ] Every action traced to a named report element (diagnosis line, margin, node count, biomarker, stage).
- [ ] Stage labeled correctly as clinical vs pathologic, with the right prefix (y, r) and AJCC edition named.
- [ ] Biomarker thresholds applied by the assay and score type reported; germline criteria attributed to a named guideline and year.
- [ ] Missing or pending elements listed, with decisions that depend on them held.
- [ ] States what would change the plan (addendum result, genomic score, germline result, re-review).

## False-Positive Prevention

- **Hedged language treated as definitive:** "suspicious for" or "atypical" acted on as cancer without more tissue.
- **Discordant benign core accepted as reassurance** when it does not explain a high-suspicion imaging finding.
- **Close margin over-called as inadequate** when it abuts a fascial plane or meets the tumor-specific definition of adequate.
- **Thresholds transferred across assays:** PD-L1 TPS vs CPS, or HER2-low vs HER2-negative, applied to the wrong drug or tumor.

## Worked Example

**Input:** 54 y/o F, post-menopausal (LMP 3 years ago), screen-detected 1.8 cm left breast mass (BI-RADS 5). Core biopsy: invasive ductal carcinoma. Underwent lumpectomy + sentinel node biopsy; plans whole-breast radiation. No neoadjuvant therapy. No known family history of breast/ovarian/pancreatic/prostate cancer. Final report: "Invasive carcinoma of no special type (ductal), Nottingham grade 2 (3+2+1 = 6). Tumor size 1.9 cm. Margins negative; closest posterior margin 1 mm (at pectoralis fascia). No lymphovascular invasion. Sentinel lymph nodes: 1 of 3 positive, 4 mm metastatic deposit, no extranodal extension. ER 95% strong, PR 70% moderate, HER2 IHC 2+, ISH negative (HER2/CEP17 ratio 1.3, average HER2 copy number 2.8). Ki-67 18%. pT1c pN1a(sn)."

**Output:**

```
SPECIMEN: Left lumpectomy + SLNB, final report, biomarkers complete.
DIAGNOSIS (translated): Definitive invasive breast carcinoma, NST.
CONCORDANCE: Concordant with BI-RADS 5 imaging and core biopsy.
TUMOR: NST, grade 2, 1.9 cm, no LVI.
MARGINS: Negative ("no ink on tumor" is adequate for invasive disease with radiation); 1 mm posterior margin is at the pectoralis fascia — no re-excision.
NODES: 1/3 SLN positive, 4 mm macrometastasis, no ENE.
STAGE: pT1c pN1a(sn) M0 → anatomic stage IIA. Look up the AJCC 8th pathological prognostic stage using grade 2, ER+, PR+, HER2−; for this biology it is lower than the anatomic stage.
BIOMARKERS: HR-positive (ER 95%, PR 70%). HER2-negative (IHC 2+, ISH non-amplified) — classify as HER2-low for future metastatic options. Ki-67 18%.
MISSING / PENDING: Genomic recurrence score not yet sent.

ACTION:
1. Surgery: complete. Axillary dissection not required — meets Z0011-type criteria (T1–2, 1–2 positive sentinel nodes, breast-conserving surgery with planned whole-breast radiation, no neoadjuvant therapy).
2. Systemic: send a 21-gene recurrence score — post-menopausal with 1–3 positive nodes; RS ≤25 → endocrine therapy alone (no chemotherapy benefit in this group); RS >25 → chemotherapy then endocrine therapy. Endocrine therapy: anastrozole 1 mg daily for at least 5 years; baseline DEXA; calcium/vitamin D. Node-positive stage II HR+/HER2− disease is eligible for adjuvant ribociclib with an aromatase inhibitor — discuss with medical oncology. Not eligible for adjuvant abemaciclib on high-risk criteria (1 node, grade 2, <5 cm).
3. Radiation: whole-breast radiation (the premise for omitting ALND); radiation oncology to decide on regional nodal irradiation.
4. Germline testing: offer BRCA1/2 testing — per ASCO–SSO 2024 guidance, all newly diagnosed breast-cancer patients aged ≤65 are offered it (she is 54), regardless of family history; genetic counseling per local pathway; a pathogenic variant would change surgical, risk-reduction, and adjuvant (PARP-inhibitor) discussions.
5. Present at multidisciplinary tumor board; survivorship plan with annual mammography starting 6 months after radiation.
```
