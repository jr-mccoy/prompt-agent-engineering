---
title: "Cerebrospinal Fluid Interpretation"
category: domain-healthcare-clinical/interpretation
description: "Read opening pressure, cell count and differential, protein, glucose ratio, stains, PCR, and special studies to classify CSF as bacterial, viral, TB/fungal, hemorrhagic, inflammatory, neoplastic, or pressure-only — and commit to treatment."
techniques:
  - ST-02
  - ST-03
  - CM-01
  - RT-02
  - RT-05
difficulty: advanced
tags:
  - neurology
  - infectious-disease
  - meningitis
  - csf
  - interpretation
  - spinal-tap-results
  - fever-and-stiff-neck
  - sudden-worst-headache
updated: "2026-09-24"
related_prompts:
  - domain-healthcare-clinical/prompts/reasoning/workup_headache.md
  - domain-healthcare-clinical/prompts/pharmacology/medicine_antibiotic_stewardship_advisor.md
  - domain-medical-education/learner-procedures/study_central_line_lp_checklist_drill.md
---

## Objective

Interpret a lumbar puncture result as a pattern and commit to the category, the most likely etiology, the treatment to start or continue (with doses), and the additional studies still needed.

Decision support for a licensed clinician: confirm antimicrobial and steroid doses, renal adjustment and thresholds against the current guideline and local formulary. Suspected bacterial meningitis or a falling level of consciousness is treated and escalated now, not after this output.

## When to Use

- A lumbar puncture result (cell count, protein, glucose, stains, PCR) is back and the pattern and treatment need to be committed.
- Suspected meningitis or encephalitis where empirical antimicrobials must be continued, narrowed, or stopped.
- Thunderclap headache with a normal CT where the LP must separate subarachnoid hemorrhage from a traumatic tap.
- Raised opening pressure, high protein, or pleocytosis without an obvious infection (IIH, Guillain-Barré, MS, leptomeningeal disease).

**Not this prompt if:**

- No LP has been done and the headache itself is being worked up → `domain-healthcare-clinical/prompts/reasoning/workup_headache.md`.
- Altered mental status without a CSF result → `domain-healthcare-clinical/prompts/reasoning/workup_altered_mental_status.md`.
- The fluid is pleural, ascitic, or synovial → `domain-healthcare-clinical/prompts/interpretation/interp_synovial_pleural_ascitic_fluid.md`.

## Inputs

- Opening pressure (position — lateral decubitus required for a valid value), appearance
- Cell count with differential (tube 1 and last tube), RBC count
- Protein, glucose with simultaneous serum glucose, lactate
- Gram stain, culture, multiplex meningitis/encephalitis PCR, HSV PCR, enterovirus PCR, cryptococcal antigen, VDRL, AFB/TB PCR, cytology/flow cytometry, oligoclonal bands/IgG index, autoimmune encephalitis antibodies, xanthochromia (spectrophotometry)
- Clinical context: age, immune status (HIV, transplant, steroids), tempo, fever, meningism, altered mental status, focal signs, seizures, rash, recent neurosurgery/shunt, antibiotics before LP (timing), headache onset (thunderclap), CT head result
- Normal adult reference (lab-dependent): WBC ≤5 cells/µL (mononuclear), protein ~15–45 mg/dL, CSF:serum glucose ratio ≥0.6, opening pressure ~10–20 cm H2O (≤25 generally accepted upper limit). Neonates and infants have different ranges.

## Role

Senior neurology or infectious diseases attending supporting the treating clinician; reads the LP results at the bedside.

## Reasoning Steps

1. **Stop and escalate first if:** suspected bacterial meningitis and antibiotics not yet given (dexamethasone + empirical antibiotics now — never wait for CT or CSF results); falling GCS, new focal deficit, seizures, or herniation signs; purpura or septic shock (suspected meningococcal disease); a CSF picture of subarachnoid hemorrhage (CTA and neurosurgery now). Then **validity checks.** Opening pressure only valid lying down, legs relaxed. Glucose must be compared with serum drawn at the same time (hyperglycemia raises CSF glucose). Traumatic tap: correct WBC by roughly 1 WBC per 500–1,000 RBCs (or use the peripheral WBC:RBC ratio), and protein rises about 1 mg/dL per 1,000 RBCs.

2. **Pattern classification.**

   | Pattern | WBC | Predominant | Protein | Glucose ratio |
   |---|---|---|---|---|
   | Bacterial | typically 1,000–5,000 (can be lower early) | neutrophils | high (often >100–200) | low (<0.4) |
   | Viral | 10–500 | lymphocytes (neutrophils early) | normal–mildly high | normal |
   | TB / fungal | 50–500 | lymphocytes | high (TB often very high) | low |
   | Inflammatory / demyelinating | <50 | lymphocytes | normal–mildly high | normal |
   | Albuminocytologic dissociation | <10 | — | high | normal |

   CSF lactate >3.5–4 mmol/L supports bacterial over viral meningitis in patients not pre-treated.

3. **Specific patterns.**
   - **HSV encephalitis:** lymphocytic, often RBCs, temporal lobe findings. HSV PCR can be negative in the first 72 h — repeat in 3–7 days if suspicion persists; do not stop acyclovir on an early negative.
   - **Cryptococcal:** very high opening pressure, CrAg positive (high sensitivity), minimal cells in advanced HIV.
   - **Neurosyphilis:** lymphocytic pleocytosis, CSF VDRL specific but insensitive.
   - **Guillain-Barré:** high protein, WBC <10; WBC >50 suggests HIV, Lyme, lymphoma, poliomyelitis-like illness instead.
   - **MS:** ≥2 CSF-specific oligoclonal bands, elevated IgG index, WBC usually <50.
   - **Leptomeningeal carcinomatosis/lymphoma:** high protein, may have low glucose; cytology ± flow cytometry — send ≥10 mL, repeat up to 3 LPs if first is negative.
   - **Autoimmune encephalitis:** mild lymphocytic pleocytosis, OCB; send paired serum and CSF antibodies (NMDAR more sensitive in CSF).
   - **Drug-induced aseptic meningitis:** NSAIDs, TMP-SMX, IVIG, lamotrigine — neutrophilic possible.
   - **Idiopathic intracranial hypertension:** opening pressure >25 cm H2O with normal contents.

4. **SAH vs traumatic tap.** Falling RBC count from tube 1 to last tube supports traumatic tap but does not exclude SAH. Xanthochromia develops from roughly 2–12 h after the bleed, so spectrophotometry is most sensitive on an LP done ≥12 h after headache onset; it is the discriminator, and visual inspection is less sensitive than spectrophotometry.

5. **Partially treated meningitis.** Antibiotics sterilize CSF culture within hours, but pleocytosis, high protein, and low glucose persist for days — treat a bacterial pattern as bacterial. Multiplex PCR helps identify the organism.

6. **Treatment commitments.**
   - **Suspected bacterial meningitis (adult, community):** dexamethasone 0.15 mg/kg (≈10 mg) IV q6h × 4 days, first dose before or with the first antibiotic dose; vancomycin (loading 20–35 mg/kg, then AUC/trough-guided) + ceftriaxone 2 g IV q12h; add ampicillin 2 g IV q4h if age >50, immunocompromised, pregnant, or alcohol use (Listeria). Continue dexamethasone only if pneumococcal or in settings where it is indicated.
   - **Encephalitis:** acyclovir 10 mg/kg IV q8h (dose on ideal body weight in obesity; hydrate; renally adjust).
   - **Cryptococcal meningitis:** liposomal amphotericin B + flucytosine induction; therapeutic LPs to lower pressure.

7. **Pitfalls before signing.** Delaying antibiotics for CT or LP; glucose ratio without paired serum glucose; stopping acyclovir on an early negative HSV PCR; reading early viral neutrophilia as bacterial without the rest of the pattern; single negative cytology excluding malignancy; opening pressure measured sitting.

## Output Format

```
OPENING PRESSURE: [value, valid Y/N]
CELLS: [WBC corrected, differential, RBC trend tube 1 → last]
PROTEIN: [value]
GLUCOSE: [CSF, serum, ratio]
STAINS / PCR / ANTIGEN: [results]

PATTERN: [bacterial / viral / TB-fungal / hemorrhagic / inflammatory / neoplastic / pressure-only / normal]
MOST LIKELY ETIOLOGY: [1., 2.]

ACTION:
- [antimicrobials/steroids with doses — continue, start, stop]
- [pending tests to chase]
- [complications to watch]
- [public health / contacts]
```

## Verification

- [ ] Glucose ratio uses a serum glucose drawn at the same time; opening pressure recorded as lateral decubitus or flagged as invalid.
- [ ] Traumatic-tap correction applied (or stated as not needed) before WBC and protein are classified.
- [ ] Pattern call traced to each input value (WBC, differential, protein, glucose ratio, lactate), with antibiotic pre-treatment and its timing accounted for.
- [ ] Every antimicrobial and steroid dose checked against weight, renal function, the current meningitis/encephalitis guideline, and local formulary.
- [ ] Early-negative HSV PCR, a single negative cytology, and LP timing relative to headache onset are reported as limits, not exclusions.
- [ ] States what result would change the call (culture and susceptibilities, repeat PCR, repeat cytology).

## False-Positive Prevention

- **Oligoclonal bands called MS-specific without paired serum.** Matching bands in serum mean systemic synthesis, not CSF-specific; the clinical and MRI picture must also fit.
- **A multiplex PCR hit accepted as the cause when the CSF does not fit it.** Panels produce false positives and can detect latent virus (e.g., HHV-6); check the target against cells, protein, and glucose.
- **A few cells or a mildly raised protein from a traumatic tap called pleocytosis or albuminocytologic dissociation** before RBC correction is applied.
- **Falling RBC count from tube 1 to the last tube taken as excluding SAH.** It supports a traumatic tap but does not rule out a bleed; xanthochromia timing decides.

## Worked Example

**Input:** 58 y/o M, 75 kg, 24 hours of fever, severe headache, and confusion. Temp 39.4, neck stiffness, GCS 13, no focal deficit. CT head normal. Blood cultures drawn; dexamethasone 10 mg IV, vancomycin, and ceftriaxone 2 g given 30 minutes before LP. LP (lateral decubitus): opening pressure 36 cm H2O, cloudy. WBC 2,400/µL (92% neutrophils), RBC 20, protein 280 mg/dL, glucose 18 mg/dL (serum 126 → ratio 0.14), lactate 8 mmol/L. Gram stain: gram-positive diplococci. PCR panel: Streptococcus pneumoniae detected.

**Output:**

```
OPENING PRESSURE: 36 cm H2O — elevated, valid position.
CELLS: WBC 2,400, 92% PMN; RBC 20 (no traumatic correction needed).
PROTEIN: 280 mg/dL — markedly elevated.
GLUCOSE: 18 / 126 → ratio 0.14 — severely low.
STAINS / PCR / ANTIGEN: Gram-positive diplococci; S. pneumoniae PCR positive.

PATTERN: Bacterial.
MOST LIKELY ETIOLOGY: Pneumococcal meningitis (confirmed).

ACTION:
- Continue dexamethasone 10 mg IV q6h × 4 days (pneumococcal — benefit established).
- Continue vancomycin (AUC-guided) + ceftriaxone 2 g IV q12h until susceptibilities. If penicillin/ceftriaxone susceptible by meningitis breakpoints → stop vancomycin, finish ceftriaxone for 10–14 days total.
- Ampicillin not needed — organism identified.
- Elevated ICP: head of bed 30°, avoid hypotonic fluids, normocapnia, treat fever; neuro checks q1h; repeat CT if GCS falls or new focal signs (hydrocephalus, empyema, venous thrombosis, infarct).
- Look for the portal: otitis media/mastoiditis, sinusitis (CT temporal bones/sinuses if symptoms), CSF leak (recurrent meningitis, prior head trauma), asplenia, HIV test, alcohol use.
- Audiology before discharge (sensorineural hearing loss is common after pneumococcal meningitis).
- Droplet precautions and contact chemoprophylaxis are NOT required for pneumococcus.
- Pneumococcal vaccination after recovery.
```
