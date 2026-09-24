---
title: "Synovial, Pleural, and Ascitic Fluid Interpretation"
category: domain-healthcare-clinical/interpretation
description: "Interpret body-fluid analyses — synovial (cell count, crystals, culture), pleural (Light's criteria, pH/glucose, parapneumonic staging), and ascitic (SAAG, total protein, PMN count) — and commit to drainage, antibiotic, and diagnostic action."
techniques:
  - ST-02
  - ST-03
  - CM-01
  - RT-02
  - RT-05
difficulty: advanced
tags:
  - rheumatology
  - pulmonology
  - hepatology
  - body-fluids
  - interpretation
  - hot-swollen-joint
  - fluid-on-lung
  - belly-fluid
  - tap-results
updated: "2026-09-24"
related_prompts:
  - domain-healthcare-clinical/prompts/reasoning/workup_joint_pain_arthritis.md
  - domain-healthcare-clinical/prompts/pharmacology/medicine_antibiotic_stewardship_advisor.md
  - domain-healthcare-clinical/prompts/acute-care/medicine_sepsis_recognition_framework.md
---

## Objective

Read a synovial, pleural, or ascitic fluid analysis and produce a committed classification and action: septic vs crystal vs inflammatory joint; transudate vs exudate and complicated vs uncomplicated parapneumonic effusion; portal-hypertensive vs non-portal ascites and SBP vs secondary peritonitis.

Decision support for a licensed clinician: confirm antibiotic and albumin doses, renal/hepatic adjustment, and diagnostic thresholds against the current guideline and local formulary. A septic or unstable patient is escalated now, not after this output.

## When to Use

- A joint aspirate, pleural tap, or paracentesis result is back and needs a committed classification and action.
- Deciding septic vs crystal vs inflammatory arthritis, transudate vs exudate, complicated vs uncomplicated parapneumonic effusion, or SBP vs secondary peritonitis.
- Checking whether a borderline Light's or SAAG result is being misclassified (diuretics, mismatched serum sample).

**Not this prompt if:**
- The joint has not been tapped yet and the task is working up joint pain from history and exam — use `domain-healthcare-clinical/prompts/reasoning/workup_joint_pain_arthritis.md`; this prompt reads the aspirate once it is back.
- The fluid is cerebrospinal — use `domain-healthcare-clinical/prompts/interpretation/interp_csf.md`.
- The question is narrowing antibiotics on a final culture and susceptibility — use `domain-healthcare-clinical/prompts/interpretation/interp_microbiology_culture_sensitivity.md`.

## Inputs

- Fluid type, appearance, volume, how obtained (ultrasound-guided, native vs prosthetic joint)
- Cell count and differential, RBC; Gram stain, culture (bottles inoculated at bedside?), crystals (polarized microscopy)
- Pleural: fluid protein, LDH, glucose, pH (blood-gas analyzer), cholesterol, triglycerides, amylase, ADA, hematocrit, cytology, NT-proBNP; paired serum protein, LDH (and lab ULN), albumin, glucose
- Ascitic: fluid albumin, total protein, PMN count, glucose, LDH, amylase, triglycerides, cytology; same-day serum albumin
- Context: fever, sepsis, recent antibiotics, immunosuppression, anticoagulation, cirrhosis/HF/CKD/malignancy, diuretics, prosthetic joints, pneumonia course, imaging (loculations, septations)

## Role

Senior internal medicine attending (with rheumatology, pulmonary, and hepatology fluency) supporting the treating clinician; reads the tap results and commits to a classification and action they can verify.

## Reasoning Steps

**Stop and escalate first (any fluid):** suspected septic joint (native or prosthetic) — same-day orthopedics for drainage, antibiotics after aspiration; SBP or suspected secondary peritonitis (polymicrobial, Runyon criteria) — antibiotics now, surgical review for perforation; empyema or frank pus — chest tube and antibiotics today; any patient meeting sepsis criteria — sepsis pathway before the rest of this read.

### Synovial fluid

1. **Cell count bands (native joint, approximate):** normal <200 WBC/µL; non-inflammatory 200–2,000; inflammatory 2,000 to ~50,000; septic typically >50,000 — but septic arthritis occurs below 50,000 (early, gonococcal, immunosuppressed, partially treated). Prosthetic joints use much lower thresholds (chronic PJI roughly >3,000 cells/µL with >80% neutrophils) — apply the institution's PJI criteria.
2. **Crystals:** monosodium urate — needle-shaped, strongly negatively birefringent (gout). CPP — rhomboid, weakly positively birefringent (pseudogout). Crystals do not exclude infection; septic and crystal arthritis coexist.
3. **Gram stain and culture:** Gram stain sensitivity is limited; a negative stain does not exclude septic arthritis. Inoculate blood culture bottles to raise yield.
4. **Hemarthrosis:** trauma, anticoagulation, hemophilia, pigmented villonodular synovitis, fracture (fat globules → lipohemarthrosis = intra-articular fracture).
5. **Action:** suspected septic native joint → drainage (arthroscopic/open or serial aspiration) + empiric vancomycin (plus ceftriaxone 1–2 g IV daily if gram-negative or gonococcal risk), narrowed by culture. Gout flare → colchicine 1.2 mg then 0.6 mg 1 h later, NSAID, or intra-articular/oral steroid once infection is not the concern.

### Pleural fluid

6. **Light's criteria — exudate if any one:** fluid/serum protein >0.5; fluid/serum LDH >0.6; fluid LDH >2/3 of the serum ULN. Light's misclassifies about a quarter of transudates on diuretics as exudates → serum-minus-pleural albumin gradient >1.2 g/dL (or protein gradient >3.1 g/dL) supports transudate; pleural NT-proBNP markedly elevated supports HF.
7. **Parapneumonic staging:** pH <7.20, glucose <60 mg/dL, positive Gram stain/culture, or frank pus → complicated effusion/empyema → drain. Loculated on ultrasound adds weight. pH must be measured in a blood-gas analyzer, anaerobically; lidocaine and air contamination distort it.
8. **Other exudate clues:** low glucose — empyema, rheumatoid, malignancy, TB, lupus, esophageal rupture. Lymphocytic exudate — TB (ADA >40 U/L supportive), malignancy, lymphoma, post-CABG. Triglycerides >110 mg/dL → chylothorax (<50 excludes); high cholesterol with low TG → pseudochylothorax. Fluid/blood hematocrit >0.5 → hemothorax. High amylase → pancreatitis, esophageal rupture. Fluid/serum creatinine >1 → urinothorax. Single cytology sensitivity is moderate — repeat once before pleural biopsy.
9. **Action:** complicated parapneumonic/empyema → small-bore chest tube; intrapleural tPA 10 mg + DNase 5 mg BID × 3 days for loculated/poorly draining collections; antibiotics with anaerobic coverage (e.g., ampicillin-sulbactam 3 g IV q6h, or ceftriaxone + metronidazole), no aminoglycosides; thoracic surgery (VATS) if drainage fails.

### Ascitic fluid

10. **SAAG (same-day serum albumin − ascitic albumin):** ≥1.1 g/dL → portal hypertension (cirrhosis, cardiac ascites, Budd-Chiari, sinusoidal obstruction, massive liver metastases). <1.1 → peritoneal carcinomatosis, TB, pancreatic, nephrotic, serositis.
11. **Total protein:** SAAG ≥1.1 with protein ≥2.5 g/dL → cardiac ascites or Budd-Chiari; <2.5 → cirrhosis. Protein <1.5 g/dL in cirrhosis → higher SBP risk (prophylaxis consideration).
12. **SBP:** ascitic PMN ≥250 cells/mm³ (correct hemorrhagic fluid by subtracting 1 PMN per 250 RBCs) → treat: ceftriaxone 2 g IV daily (or cefotaxime 2 g IV q8h), usually 5 days, and IV albumin 1.5 g/kg day 1 and 1 g/kg day 3 when Cr >1, BUN >30, or bilirubin >4. Bedside inoculation of blood culture bottles raises culture yield.
13. **Secondary bacterial peritonitis (Runyon criteria):** ≥2 of total protein >1 g/dL, glucose <50 mg/dL, LDH above serum ULN — or polymicrobial culture → CT for perforation/abscess, broaden to anaerobic coverage, surgical consult.
14. **Other:** TG >200 mg/dL → chylous; amylase high → pancreatic ascites; cytology positive in peritoneal carcinomatosis but usually negative with HCC or liver metastases alone.

15. **Pitfalls before signing.** Assuming crystals exclude infection; Light's on diuretics; pleural pH from a syringe with air or lidocaine; SAAG with serum albumin from another day; missing SBP because the patient "looks well" (many are afebrile); treating a polymicrobial ascites culture as SBP.

## Output Format

```
FLUID: [type, appearance, how obtained]
KEY VALUES: [cell count/differential; chemistries with paired serum; micro; crystals/cytology]
CLASSIFICATION: [septic / crystal / inflammatory / non-inflammatory — OR — transudate / exudate (criterion met) + parapneumonic stage — OR — SAAG high/low + SBP / secondary peritonitis / other]
MOST LIKELY ETIOLOGY: [1., 2.]

ACTION:
- [drainage / procedure]
- [antibiotics or disease-specific therapy with doses]
- [pending tests to chase]
- [repeat tap or imaging]
```

## Verification

- [ ] Septic joint, SBP/secondary peritonitis, and empyema addressed before routine classification.
- [ ] Every classification traced to a named value with its paired serum value, same-day where required (Light's, SAAG).
- [ ] Each threshold attributed to its named criterion (Light's, Runyon, SAAG ≥1.1, PMN ≥250) and adjusted for context (prosthetic joint, diuretics, hemorrhagic fluid).
- [ ] Antibiotic and albumin doses checked against weight and renal function and the current guideline or local protocol.
- [ ] Pending tests (culture, cytology, ADA) listed with the decision each would change.
- [ ] States what would change the conclusion (culture growth, failed drainage, repeat tap).

## False-Positive Prevention

- **Transudate called exudate on diuretics:** check the albumin or protein gradient before chasing a malignant or infective cause.
- **Crystals taken as the whole answer** when septic and crystal arthritis coexist.
- **Bloody tap over-called as SBP** without correcting PMN for RBCs (1 PMN per 250 RBCs).
- **Spurious pleural pH** from air, lidocaine, or a non-blood-gas analyzer leading to an unnecessary chest tube.

## Worked Example

**Input:** 61 y/o M, day 6 of treatment for right lower lobe community-acquired pneumonia on ceftriaxone 1 g daily + azithromycin; persistent fever 38.7 and pleuritic pain. Ultrasound: moderate right effusion with septations. Thoracentesis: turbid fluid; pH 7.08, glucose 38 mg/dL (serum 110), LDH 1,850 U/L (serum 320; lab serum ULN 250), protein 4.8 g/dL (serum 6.8), WBC 18,000/µL (88% neutrophils), Gram stain negative, culture pending. Cr 0.9, no allergies.

**Output:**

```
FLUID: Pleural, turbid, ultrasound-guided, septated collection.
KEY VALUES: Protein ratio 4.8/6.8 = 0.71 (>0.5); LDH ratio 1,850/320 = 5.8 (>0.6); fluid LDH 1,850 > 2/3 ULN (167). pH 7.08, glucose 38. WBC 18,000 neutrophilic. Gram stain negative.
CLASSIFICATION: Exudate (all three Light's criteria). Complicated parapneumonic effusion — pH <7.20 and glucose <60, septated. Not frank pus.
MOST LIKELY ETIOLOGY:
1. Complicated parapneumonic effusion evolving toward empyema (strep, anaerobes, S. aureus most likely).
2. Less likely: malignancy or TB — revisit only if culture negative and no response to drainage.

ACTION:
- Small-bore chest tube (12–14 Fr) today with regular saline flushes.
- Septated collection → intrapleural alteplase 10 mg + dornase alfa 5 mg BID × 3 days if drainage is poor at 24 h (or start now per local pleural protocol).
- Change antibiotics to cover anaerobes: stop ceftriaxone/azithromycin; ampicillin-sulbactam 3 g IV q6h. Add vancomycin only if MRSA risk factors or culture grows S. aureus.
- Chase pleural culture (send in blood culture bottles if more fluid is taken) and blood cultures.
- Repeat chest imaging (ultrasound or CT) at 48–72 h; thoracic surgery consult for VATS decortication if persistent sepsis or undrained collection despite tube + fibrinolytic.
- Total antibiotic course typically ≥3 weeks, oral step-down (amoxicillin-clavulanate 875/125 mg BID) once afebrile and drained, guided by culture and imaging.
```
