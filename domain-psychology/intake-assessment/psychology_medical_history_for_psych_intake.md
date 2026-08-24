---
title: "Medical History for Psychiatric Intake"
category: psychology/intake-assessment
description: "Compile a psychiatric-relevant medical history section covering diagnoses, medications, labs, and conditions with bidirectional psychiatric-medical interaction for a 90791/90792 intake note."
techniques:
  - ST-04
  - DT-02
  - RT-02
  - CM-02
  - QA-04
difficulty: intermediate
intended_use: model-testing
tags:
  - medical-history
  - medications
  - labs
  - psychotropic-interaction
  - medical-psychiatric-interface
  - intake
  - cpt-90791
  - cpt-90792
updated: "2026-06-08"
related_prompts:
  - domain-psychology/documentation/psychology_intake_assessment_note.md
  - domain-psychology/intake-assessment/psychology_psychiatric_history_compiler.md
  - domain-psychology/intake-assessment/psychology_substance_use_history_intake_module.md
  - domain-psychology/intake-assessment/psychology_screening_battery_interpreter.md
---

# Medical History for Psychiatric Intake

## Objective

Compile a psychiatric-relevant medical history section that:

1. Documents active and significant past medical diagnoses with their relationship to psychiatric presentation and psychotropic prescribing.
2. Creates a current medication reconciliation list (all medications, doses, prescribers) flagging drug-drug interactions relevant to psychotropic initiations.
3. Identifies conditions requiring pre-prescribing laboratory evaluation (metabolic panel, thyroid, CBC, renal/hepatic function, ECG, pregnancy test).
4. Flags medical conditions that commonly present with or mimic psychiatric symptoms (thyroid disease, autoimmune encephalitis, vitamin deficiencies, sleep apnea, TBI, seizure disorders, cardiac arrhythmia).
5. Documents surgical history, allergies, and reproductive/pregnancy status.
6. Produces a Medical History section ready for insertion into the 90791/90792 biopsychosocial intake note.

## When to Use

- At all adult psychiatric and behavioral health intakes; this section is required for 90791/90792 and CARF/Joint Commission standards.
- When CPT 90792 is appropriate (evaluation with medical services by MD, DO, NP, PA) — the medical history section carries greater weight.
- When a client presents with multiple medical conditions, polypharmacy, or a recent medical event that may be driving or complicating the psychiatric presentation.
- When psychiatric medications are to be initiated and baseline labs are clinically indicated.

## Inputs / Context Required

- **Active medical diagnoses:** Condition name, approximate onset or date of diagnosis, treating provider (type), current management status (controlled / uncontrolled / new / under evaluation).
- **Significant past medical history:** Prior hospitalizations (non-psychiatric), surgeries, significant resolved conditions.
- **Current medications (all):** Medication name (generic and trade), dose, frequency, prescribing provider, indication. Include OTC medications, supplements, vitamins, and herbal preparations.
- **Allergies:** Drug allergies with reaction type (anaphylaxis / rash / GI intolerance / other); drug intolerances; environmental allergies if relevant.
- **Recent laboratory values:** Metabolic panel (glucose, electrolytes, BUN/creatinine), liver function tests (AST/ALT/total bilirubin), CBC, thyroid (TSH, free T4), lipid panel, HbA1c, vitamin D, B12, folate; if available — renal function (eGFR), ECG (QTc interval), urine drug screen, blood alcohol level, pregnancy test.
- **Head injuries / TBI:** History, dates, LOC, post-concussive symptoms, neuroimaging.
- **Seizure history:** Type, last seizure, current anticonvulsants, neurologist.
- **Sleep:** Sleep apnea (diagnosed or suspected, treated with CPAP/BiPAP), restless legs, chronic insomnia.
- **Cardiac history:** Arrhythmia, cardiomyopathy, QTc prolongation history, syncope, pacemaker — directly relevant to psychotropic QTc-prolonging risk.
- **Thyroid history:** Hypothyroid, hyperthyroid, thyroiditis, current TSH.
- **Metabolic health:** Diabetes type, HbA1c, obesity, metabolic syndrome — relevant to antipsychotic metabolic monitoring.
- **Autoimmune conditions:** Lupus, MS, anti-NMDA receptor encephalitis risk factors, inflammatory conditions — relevant to psychiatric mimics.
- **Reproductive / pregnancy status (if applicable):** Current pregnancy, breastfeeding, contraception, postpartum period (within 12 months), plans for pregnancy.
- **Primary care provider:** Name, practice, last visit, PCP engagement status.

## Constraints

### Must

- List every current medication including OTC, supplements, and herbals — these carry interaction potential with psychotropics (e.g., St. John's wort induces CYP3A4; fish oil at high doses may potentiate anticoagulants with lithium; many herbals affect serotonin).
- Flag clinically significant drug-drug interaction concerns relevant to the planned or existing psychotropic regimen, using standard interaction categories (major / moderate / minor / contraindicated).
- Identify which laboratory tests are indicated prior to initiating likely psychotropic medications, citing the clinical rationale (e.g., baseline metabolic panel and ECG before starting an antipsychotic; TSH before initiating lithium; CBC before clozapine initiation).
- Flag medical conditions that can present as or exacerbate psychiatric symptoms; for each flagged condition, note the clinical relevance to the differential diagnosis.
- Document QTc-relevant cardiac history and any medications already on the client's regimen with known QTc-prolonging effect (crediblemeds.org risk categories: known risk / conditional risk / possible risk / no known risk).
- Document reproductive status and pregnancy-relevant psychotropic safety considerations whenever reproductive-age clients are included.
- Note last PCP visit and PCP coordination plan.

### Must Not

- Do not recommend specific medications in this history section; flag the relevant considerations and defer prescribing decisions to the prescribing provider.
- Do not omit the allergy section — even "NKDA" (no known drug allergies) must be explicitly stated.
- Do not confuse a prior prescription list with a current medication list; verify currency of each medication with the client.
- Do not fabricate laboratory values; flag absent labs with `[clinician input required: order these baseline labs before initiating X]`.
- Do not ignore OTC or supplement history under the assumption they are clinically irrelevant.

## Instructions

1. **Compile the active medical diagnoses list.** For each condition, note: whether controlled or uncontrolled; whether it has documented psychiatric implications; and whether it requires management-level coordination with the treating medical provider.

2. **Build the medication reconciliation table.** Include every agent with dose, frequency, and prescriber. Flag OTC and supplements. Note the indication for each.

3. **Generate the drug-drug interaction flag list.** Identify any current medications that present clinically significant interactions with psychotropic agents likely to be relevant for this client. Use standard interaction categories. Note the mechanism briefly.

4. **List indicated baseline laboratories.** For each anticipated psychotropic class (e.g., antipsychotics, lithium, mood stabilizers, SSRIs/SNRIs in special populations), specify which labs should be obtained before initiation and which are repeat-monitoring labs.

5. **Flag psychiatric mimic conditions.** Review the medical history and identified lab gaps for conditions known to present with depressive, anxious, psychotic, or cognitive symptoms: thyroid dysfunction, B12/folate/vitamin D deficiency, sleep apnea, TBI, seizures, autoimmune encephalitis, chronic pain, cardiac disease.

6. **Document reproductive status and pregnancy-relevant considerations** if applicable.

7. **Summarize medical-psychiatric interface.** Write a brief paragraph describing how the medical history intersects with the psychiatric presentation and treatment plan.

8. **Run verification.**

## Output Format

```
=== MEDICAL HISTORY (Psychiatric Intake) ===

Client: [Initials/MRN]    Date of Service: [YYYY-MM-DD]
PCP: [Name, practice, last visit date]    PCP coordination planned: [Yes / No / TBD]
CPT: [90791 | 90792]

─────────────────────────────────────────
ACTIVE MEDICAL DIAGNOSES
─────────────────────────────────────────
| Diagnosis          | Onset / Dx Year | Treating Provider  | Status          | Psychiatric Relevance |
|--------------------|-----------------|--------------------|-----------------|-----------------------|
| [Hypothyroidism]   | [YYYY]          | [PCP — Dr. X]      | [Controlled — TSH 2.1] | [Relevant: untreated hypo mimics depression; monitor TSH with lithium] |
| [Type 2 Diabetes]  | [YYYY]          | [PCP]              | [Uncontrolled — HbA1c 9.2] | [Relevant: antipsychotic metabolic monitoring required] |
| [...]              | [...]           | [...]              | [...]           | [...]                 |

Surgical history: [...]
Head injuries / TBI: [None reported / Date, LOC duration, post-concussive symptoms, imaging]
Seizure history: [None / Type, last seizure, current anticonvulsant, neurologist]

─────────────────────────────────────────
ALLERGIES
─────────────────────────────────────────
Drug allergies: [NKDA / Medication — reaction type (anaphylaxis / rash / GI intolerance)]
Drug intolerances: [Medication — intolerance description]
Environmental allergies (if clinically relevant): [...]

─────────────────────────────────────────
CURRENT MEDICATION RECONCILIATION
─────────────────────────────────────────
| Medication (generic / trade) | Dose | Frequency | Indication | Prescriber | OTC/Supplement |
|------------------------------|------|-----------|------------|------------|----------------|
| [Levothyroxine (Synthroid)]  | [100 mcg] | [Daily] | [Hypothyroidism] | [PCP] | [Rx] |
| [Lorazepam (Ativan)]         | [1 mg] | [PRN — up to TID] | [Anxiety] | [PCP] | [Rx] |
| [Metformin (Glucophage)]     | [500 mg] | [BID] | [T2DM] | [PCP] | [Rx] |
| [Fish oil]                   | [2 g] | [Daily] | [Self-prescribed — cardiac] | [N/A] | [OTC supplement] |
| [St. John's Wort]            | [300 mg] | [Daily] | [Self-prescribed — mood] | [N/A] | [⚠️ OTC — CYP3A4 inducer — significant interaction risk] |
| [...]                        | [...] | [...] | [...] | [...] | [...] |

─────────────────────────────────────────
⚠️ DRUG-DRUG INTERACTION FLAGS
─────────────────────────────────────────
[For each clinically significant interaction between current medications and anticipated
psychotropic additions:]

Flag 1: [St. John's Wort + SSRIs] — Category: CONTRAINDICATED
  Mechanism: CYP3A4 induction reduces SSRI levels; serotonin syndrome risk at supratherapeutic
  doses. Recommend discontinuation of St. John's Wort before initiating any serotonergic agent.

Flag 2: [Lorazepam (existing benzo) + anticipated benzodiazepine or gabapentinoid] — Category: MAJOR
  Mechanism: Additive CNS/respiratory depression. Relevant if anxiolytic augmentation planned.

Flag 3: [clinician input required: review full interaction profile before initiating X]

─────────────────────────────────────────
INDICATED BASELINE LABORATORIES
─────────────────────────────────────────
Labs already available:
  | Lab                | Date       | Value              | Clinical Note              |
  |--------------------|------------|--------------------|----------------------------|
  | TSH                | YYYY-MM-DD | [X mIU/L]          | [Within range / Elevated / Low] |
  | HbA1c              | YYYY-MM-DD | [X%]               | [...]                      |
  | [Other]            | YYYY-MM-DD | [X]                | [...]                      |

Labs to obtain before treatment initiation:
  | Lab                | Rationale                                          | Urgency   |
  |--------------------|----------------------------------------------------|-----------|
  | CMP (metabolic panel) | Baseline before antipsychotic; renal function for lithium | Before Rx |
  | Fasting lipid panel | Baseline metabolic monitoring — antipsychotic     | Before Rx |
  | CBC                | Baseline if clozapine or carbamazepine considered  | Before Rx |
  | ECG (QTc interval) | QTc-prolonging agents (antipsychotics, TCAs, citalopram ≥ 40 mg) | Before Rx |
  | Urine drug screen  | [If not already done]                              | Today / First visit |
  | Urine pregnancy test | Reproductive-age client; teratogenic risk medications | Before Rx |
  | [Other]            | [Rationale]                                        | [Timing]  |

QTc Considerations:
  Baseline QTc if known: [X ms / Not available — ECG recommended]
  Current medications with QTc-prolonging risk: [List with CredibleMeds.org risk category]
  Clinical threshold: QTc > 500 ms is generally a contraindication to adding QTc-prolonging
  agents; QTc 450–500 ms warrants caution and cardiology input.

─────────────────────────────────────────
PSYCHIATRIC MIMIC FLAGS
─────────────────────────────────────────
[For each condition present or suspected that may be contributing to the psychiatric presentation:]

Thyroid: [TSH result or status — if elevated or untreated hypothyroid, note contribution to
depressive symptoms; if low TSH, note contribution to anxiety/agitation/mood lability]

Sleep apnea: [Diagnosed / Suspected by symptoms (snoring, witnessed apnea, morning headaches,
non-restorative sleep, BMI > 30) / Not suspected — if suspected, refer for sleep study before
attributing all cognitive and mood symptoms to primary psychiatric disorder]

TBI / head injury: [None / Present — note post-concussive symptoms that overlap with depression,
ADHD, or PTSD]

B12 / folate / vitamin D: [Lab result or status — deficiencies can present with fatigue, cognitive
slowing, depressive symptoms, peripheral neuropathy]

Autoimmune / inflammatory: [Anti-NMDA receptor encephalitis risk factors if new-onset psychosis
in young female or after viral illness; lupus psychiatric manifestations; MS]

Seizure / subclinical ictal activity: [If mood / behavior / cognition changes are paroxysmal,
consider EEG]

Cardiac arrhythmia: [Palpitations, syncope, anxiety-like presentations — may indicate arrhythmia]

─────────────────────────────────────────
REPRODUCTIVE / PREGNANCY STATUS
─────────────────────────────────────────
[Applicable for reproductive-age clients:]
Current pregnancy: [Yes — gestational age / No / Unknown — test recommended]
Breastfeeding: [Yes / No]
Contraception: [Method / None / Not applicable]
Plans for pregnancy in next 12 months: [Yes / No / Uncertain]
Psychotropic teratogenicity considerations: [Note any medications of concern for current
reproductive status — e.g., valproate Category X, lithium Ebstein anomaly risk, paroxetine
PPHN risk — flag for prescribing discussion, do not make prescribing decisions here]

─────────────────────────────────────────
MEDICAL-PSYCHIATRIC INTERFACE SUMMARY
─────────────────────────────────────────
[Two to four sentence paragraph: How the medical history intersects with the psychiatric
presentation. Which medical conditions are actively contributing to or complicating the
psychiatric diagnosis. Which labs are outstanding before safe prescribing can proceed.
Which medical conditions require coordination with the PCP or specialist before or during
psychiatric treatment.]

─────────────────────────────────────────
BILLING NOTE
─────────────────────────────────────────
Medical history documented as part of CPT [90791 | 90792].
90792 billable if this evaluation was conducted by MD/DO/NP/PA with E&M component.
PCP communication to be initiated: [Yes — ROI status / No / Patient declined].
```

## Verification

- [ ] Active medical diagnoses table complete with psychiatric relevance noted for each condition.
- [ ] NKDA or specific allergies explicitly documented — never blank.
- [ ] Medication reconciliation includes all Rx, OTC, supplements, and herbals with doses.
- [ ] Drug-drug interaction flags generated for any clinically significant pairs involving anticipated psychotropics.
- [ ] Baseline laboratory table specifies what is available and what needs to be ordered before prescribing begins.
- [ ] QTc-relevant history and current QTc-prolonging medications noted.
- [ ] Psychiatric mimic conditions reviewed — each major category addressed (thyroid, sleep apnea, TBI, B12/folate/D, autoimmune, seizure, cardiac).
- [ ] Reproductive status documented for reproductive-age clients.
- [ ] Medical-psychiatric interface summary is integrative, not a list.
- [ ] PCP coordination plan noted.
- [ ] Gaps flagged with `[clinician input required: ...]`; missing labs flagged with recommended timing.
- [ ] No specific prescribing recommendations made within this section.
