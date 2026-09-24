---
title: "Dermatologic Lesion Analysis"
category: domain-healthcare-clinical/specialty
description: "Describe a single skin lesion morphologically, apply ABCDE, ugly-duckling, EFG and dermoscopic criteria, rank the neoplastic differential, and commit to monitor, biopsy technique, or urgent excision."
techniques:
  - ST-02
  - ST-03
  - CM-01
  - RT-02
  - RT-05
difficulty: advanced
tags:
  - dermatology
  - melanoma
  - skin-cancer
  - specialty-assessment
  - changing-mole
  - suspicious-spot
  - bleeding-mole
updated: "2026-09-24"
related_prompts:
  - domain-healthcare-clinical/prompts/reasoning/workup_rash_differential.md
  - domain-healthcare-clinical/prompts/interpretation/interp_pathology_report.md
  - domain-healthcare-clinical/prompts/pharmacology/pharm_anticoag_periprocedural_bridging.md
---

## Objective

Assess a single discrete skin lesion (pigmented or non-pigmented, suspected benign vs neoplastic) the way a dermatologist does at the bedside: precise morphologic description, structured melanoma and keratinocyte-cancer criteria, a ranked differential, and a committed action — reassure, photograph and monitor, biopsy (with the correct technique), or urgent excision/referral.

Decision support for a licensed clinician: confirm doses, renal/hepatic adjustment and thresholds (including margin and SLNB criteria) against the current guideline and local formulary. A lesion with signs of spread, infection or uncontrolled bleeding is escalated now, not after this output.

## When to Use

- A single mole or spot that is new, changing, bleeding, or looks different from the patient's other moles.
- A non-pigmented bump or scaly patch on sun-damaged skin where skin cancer is the question.
- Choosing the right biopsy technique and writing a pathology request the pathologist can use.

**Not this prompt if:**
- The problem is a diffuse or inflammatory eruption → [`workup_rash_differential.md`](../reasoning/workup_rash_differential.md); this prompt is for one lesion where the question is "is this a skin cancer, and how do I sample it?"
- The biopsy is back and the task is reading the pathology report → [`interp_pathology_report.md`](../interpretation/interp_pathology_report.md).

## Inputs

- Lesion description or image description: site, size (mm), primary morphology (macule, papule, plaque, nodule), color(s), border, surface (scale, crust, ulceration, bleeding), symmetry
- Evolution: new vs longstanding, change in size/shape/color, symptoms (itch, bleeding, tenderness), time course
- Dermoscopic findings if available: network, globules, dots, streaks/pseudopods, regression structures, blue-white veil, vessel pattern, milia-like cysts, leaf-like areas
- Comparison with the patient's other nevi (signature nevus pattern)
- Risk factors: personal or family history of melanoma, >50 nevi or atypical nevi, Fitzpatrick type, blistering sunburns, tanning-bed use, chronic UV (outdoor work), immunosuppression (solid-organ transplant, CLL, biologics), prior keratinocyte cancers, radiation, arsenic
- Patient: age, anticoagulation, anatomic constraints (face, digit, nail, genital, acral)

If dermoscopy is not supplied, reason from clinical morphology and state what dermoscopy would add.

## Role

Senior attending dermatologist supporting the treating primary care clinician on a curbside about a lesion they are worried about. Precise morphologic vocabulary, a committed disposition, and a biopsy plan the pathologist can actually read.

## Reasoning Steps

1. **Describe before you diagnose.** Primary lesion type, size in mm (measured, not estimated), color(s) counted, border quality, surface change, distribution relative to other lesions. A vague description ("dark mole") produces a vague plan.
   - **Stop and escalate now if:** a known or suspected skin cancer with new lymphadenopathy, neurologic or systemic symptoms (possible metastatic disease — urgent oncology/dermatology); a nodule enlarging over weeks, or a firm red-violet nodule in an older or immunosuppressed patient (nodular melanoma or Merkel cell carcinoma — same-week excision); uncontrolled bleeding; or spreading erythema, necrosis, or pain out of proportion with fever (infection — treat as such).

2. **Apply melanoma criteria — all of them.**
   - **ABCDE:** Asymmetry, Border irregularity, Color variegation (≥2–3 colors; blue, black, gray, white, red are more concerning than tan/brown), Diameter >6 mm, Evolving. Evolution is the most important single criterion — a small changing lesion outranks a large stable one.
   - **Ugly duckling sign:** a lesion that looks different from the patient's other nevi is suspicious even if it passes ABCDE.
   - **EFG for nodular melanoma:** Elevated, Firm, Growing for >1 month. Nodular and amelanotic melanomas fail ABCDE; do not let a symmetric pink papule reassure you.
   - **Weighted 7-point checklist** (UK practice): major — change in size, irregular shape, irregular color (2 points each); minor — diameter ≥7 mm, inflammation, oozing, change in sensation (1 point each). Score ≥3 prompts urgent referral in UK guidance; thresholds are pathway-specific.
   - **Special sites:** acral lesions (parallel ridge pattern on dermoscopy is concerning; parallel furrow is typically benign), nail (longitudinal melanonychia >3 mm, widening, multiple colors, Hutchinson sign — periungual pigment), face in the elderly (lentigo maligna — slow-growing irregular macule on sun-damaged skin).

3. **Apply dermoscopy criteria if available.**
   - **3-point checklist:** asymmetry of color/structure, atypical network, blue-white structures — ≥2 of 3 is suspicious and warrants excision.
   - Melanoma-specific structures: atypical/broadened network, irregular streaks or pseudopods, irregular dots/globules, regression (white scar-like areas, peppering), blue-white veil, atypical (polymorphous, dotted/linear irregular) vessels, negative network.
   - Benign patterns: reticular symmetric network, homogeneous globular pattern, symmetric starburst in a child (Spitz/Reed pattern — still excise in adults).

4. **Evaluate keratinocyte cancers and mimics.**
   - **BCC:** pearly/translucent papule, rolled border, arborizing telangiectasia, central ulceration ("rodent ulcer"); superficial BCC = scaly pink patch with thread-like border. Dermoscopy: arborizing vessels, leaf-like areas, blue-gray ovoid nests, spoke-wheel structures, ulceration.
   - **cSCC:** keratotic, often tender, indurated papule/nodule on sun-damaged skin; rapid growth over weeks with central keratin plug suggests keratoacanthoma-type SCC (treat as SCC). Transplant recipients: SCC dominates and is more aggressive.
   - **Actinic keratosis:** rough, sandpaper scale on erythematous base; induration, tenderness, bleeding, or rapid growth → biopsy for SCC.
   - **Benign mimics:** seborrheic keratosis (stuck-on, milia-like cysts, comedo-like openings, fissures/ridges), dermatofibroma (firm, dimple sign, central white patch with peripheral delicate network), cherry/thrombosed angioma (red-blue lacunae), solar lentigo, hemangioma. A "seborrheic keratosis" that is changing or inflamed out of proportion should still be sampled.

5. **Risk-weight the finding.** Same lesion carries a different post-test probability in a transplant recipient, a patient with prior melanoma, or someone with a familial melanoma syndrome. State how risk changes the threshold.

6. **Commit to a disposition.**
   - **Benign, confident:** reassure; no follow-up beyond routine skin checks.
   - **Equivocal, flat, not changing, low risk:** baseline photograph (overview + dermoscopic) and short-term digital monitoring at ~3 months; any change → excise. Do not monitor raised or nodular lesions — excise.
   - **Suspicious for melanoma:** excisional biopsy.
   - **Suspicious for BCC/SCC:** shave or punch biopsy adequate for diagnosis.
   - **Rapid growth, ulcerated nodule, or suspected nodular/amelanotic melanoma:** same-week excision or urgent dermatology.

7. **Specify biopsy technique precisely.**
   - **Suspected melanoma:** full-thickness excisional biopsy with 1–3 mm clinical margins, oriented along the long axis of the anticipated wide excision (lymphatic drainage / relaxed skin tension lines on the limb axis). Avoid wide margins and rotation flaps before diagnosis — they disrupt sentinel node mapping.
   - Deep saucerization (scoop) shave is an accepted alternative when it captures the full lesion to adequate depth; a superficial shave that transects the base destroys Breslow depth staging.
   - **Large lesions or cosmetically sensitive sites (face lentigo maligna, acral, nail):** incisional or punch biopsy of the most atypical (darkest, most raised) area, or multiple sampling; nail matrix biopsy by dermatology/hand surgery.
   - **BCC/SCC:** tangential shave including dermis, or punch through the thickest part; for suspected infiltrative or recurrent tumors, punch to depth.
   - Pathology requisition: site, size, clinical differential ("r/o melanoma"), history of change, and request margin status.

8. **Anticipate the pathology-driven next step.** For confirmed melanoma, re-excision margins scale with Breslow depth (in situ 0.5–1 cm; ≤1.0 mm 1 cm; 1.01–2.0 mm 1–2 cm; >2.0 mm 2 cm per NCCN-style margin tables) and sentinel lymph node biopsy is discussed from T1b (AJCC 8th: Breslow 0.8–1.0 mm, or <0.8 mm with ulceration) upward — SLNB thresholds are guideline- and edition-dependent, confirm against the current version. BCC/SCC definitive treatment depends on subtype, site, and risk features (Mohs for high-risk facial or recurrent tumors).

## Output Format

```
LESION DESCRIPTION:
- Site / size (mm) / morphology / colors / border / surface
- Evolution and symptoms

CRITERIA APPLIED:
- ABCDE: [each letter, positive/negative]
- Ugly duckling: [yes/no]
- EFG (if raised): [yes/no]
- Dermoscopy: [3-point checklist score, key structures, or "not available — would add X"]

RISK MODIFIERS: [listed, and how they shift threshold]

DIFFERENTIAL (ranked):
1. [diagnosis — key supporting/opposing features]
2. [ ]
3. [ ]

DISPOSITION: [reassure / photo + 3-month monitoring / biopsy / urgent excision or referral]

BIOPSY PLAN (if indicated):
- Technique: [excisional 1–3 mm margins / saucerization / punch / incisional of most atypical area]
- Orientation and site considerations
- Pathology request: [clinical differential, history, margins]

ANTICIPATED NEXT STEP BY PATHOLOGY RESULT:
- [melanoma → re-excision margin by Breslow ± SLNB discussion; BCC/SCC → definitive modality]

SURVEILLANCE / COUNSELING:
- [full-skin exam interval, self-exam, photoprotection, first-degree relative screening if melanoma]

PITFALLS TO AVOID:
- [shave transection of a possible melanoma, reassurance by symmetry in a nodular lesion, etc.]
```

## Verification

- [ ] The lesion was described with measured size, counted colors and primary morphology before any diagnosis was named.
- [ ] ABCDE, ugly duckling and EFG were each applied, and no raised or nodular lesion was reassured on ABCDE alone.
- [ ] The disposition follows from the criteria and risk modifiers; monitoring is offered only for flat, non-changing, low-risk lesions.
- [ ] The biopsy technique preserves Breslow depth when melanoma is possible, and any periprocedural anticoagulant decision is stated.
- [ ] Margin and SLNB thresholds name the guideline and staging edition; confirm doses, renal adjustment and thresholds against the current guideline and local formulary.

## False-Positive Prevention

- **A seborrheic keratosis or dermatofibroma excised as "atypical."** Milia-like cysts, comedo-like openings, or a central white patch with a dimple sign are reliably benign; do not excise on color count alone when benign structures are clear.
- **A large but stable longstanding nevus called melanoma on diameter.** Diameter >6 mm without change or other criteria is a weak signal; evolution outranks size.
- **Every atypical nevus treated as the ugly duckling.** In a patient with many similar dysplastic-appearing nevi, compare against the patient's own signature pattern — excise the outlier, photograph and monitor the rest.
- **Benign acral or nail pigment over-called.** A parallel-furrow pattern on acral skin and a narrow, uniform, stable nail band are typically benign; reserve urgency for parallel-ridge pattern, widening bands or Hutchinson sign.
- **A traumatized or thrombosed benign lesion over-called.** Recent trauma, irritation or thrombosis (e.g., of an angioma) can darken or bleed a benign lesion; if uncertain, sample it rather than stage it.

## Worked Example

**Input:** 58 y/o M, farmer, Fitzpatrick II, father had melanoma. Wife noticed a mole on his upper back "getting darker" over 6 months. Exam: 9 × 7 mm asymmetric macule with a small raised area at its inferior edge; tan, dark brown, black, and a gray-blue zone; notched border. It looks unlike his ~40 other uniform brown nevi. Dermoscopy: atypical broadened network at one pole, irregular peripheral streaks, blue-white veil over the raised area. On apixaban for AF.

**Output:**

```
LESION DESCRIPTION:
- Upper back, 9 × 7 mm, predominantly macular with a 2–3 mm papular component inferiorly; four colors (tan, dark brown, black, gray-blue); notched irregular border; no ulceration.
- Documented darkening over 6 months.

CRITERIA APPLIED:
- ABCDE: A+ B+ C+ (4 colors including blue-gray) D+ (9 mm) E+ (darkening, new raised area).
- Ugly duckling: yes — outlier among ~40 uniform nevi.
- EFG: the new papular focus is the part that worries me most — possible vertical growth phase.
- Dermoscopy: 3-point checklist 3/3 (asymmetry, atypical network, blue-white structures); irregular streaks.

RISK MODIFIERS: first-degree relative with melanoma, chronic occupational UV, fair skin. These lower my threshold further; this lesion would warrant excision without them.

DIFFERENTIAL (ranked):
1. Invasive melanoma (superficial spreading with a possible nodular component) — every clinical and dermoscopic criterion positive.
2. Severely dysplastic nevus — possible, but blue-white veil and streaks on a changing lesion in a 58-year-old do not allow that assumption.
3. Pigmented BCC — no arborizing vessels or ovoid nests; unlikely.

DISPOSITION: Excisional biopsy this week. Not a candidate for monitoring (raised, changing, 3/3 dermoscopy).

BIOPSY PLAN:
- Elliptical full-thickness excision with 2 mm clinical margins, to subcutaneous fat, long axis oriented to allow later wide re-excision along relaxed skin tension lines of the upper back. Primary linear closure; no flap.
- Apixaban: continue — excisional biopsy on the trunk is low bleeding risk; hold pressure, layered closure.
- Pathology request: "Upper back, 9 mm changing pigmented lesion with raised focus and blue-white veil — r/o melanoma. Please report Breslow depth, ulceration, mitotic rate, microsatellites, margins."

ANTICIPATED NEXT STEP BY PATHOLOGY RESULT:
- Melanoma in situ → re-excision with 0.5–1 cm margins.
- Invasive, Breslow ≤1.0 mm → 1 cm wide excision; SLNB discussion if T1b (0.8–1.0 mm or ulcerated).
- Breslow >1.0 mm → 1–2 cm margins by depth, SLNB discussion, surgical oncology / melanoma clinic.
- Severely dysplastic nevus with positive margin → re-excise to clear margins.

SURVEILLANCE / COUNSELING:
- Full-skin exam by dermatology; if melanoma confirmed, surveillance interval by stage (typically every 3–6 months initially).
- Monthly self-exam with partner; baseline total-body photography given nevus count and family history.
- Recommend skin checks for his siblings and children.
- Photoprotection for outdoor work: wide-brim hat, UPF clothing, SPF 30+ reapplied.

PITFALLS TO AVOID:
- Do not shave this superficially — a transected base loses Breslow depth, which drives margins, SLNB, and staging.
- Do not excise with wide margins or close with a rotation flap before diagnosis — it disrupts lymphatic mapping.
- Do not let the patient's large number of benign nevi normalize the outlier.
- Do not stop anticoagulation for a trunk excision.
```
