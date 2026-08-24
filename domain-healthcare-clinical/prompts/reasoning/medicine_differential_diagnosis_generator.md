---
title: "Differential Diagnosis Generator"
category: healthcare-clinical/reasoning
description: "Generate a probability-ranked differential diagnosis from a clinical presentation, with supporting/refuting features, distinguishing tests, 'can't-miss' diagnoses, and a prioritized diagnostic workup — as decision support, not autonomous diagnosis."
techniques:
  - ST-01
  - RT-02
  - DS-02
  - QA-01
  - QA-20
difficulty: advanced
tags:
  - differential-diagnosis
  - clinical-reasoning
  - decision-support
  - diagnostic-workup
  - cant-miss
updated: "2026-06-07"
related_prompts:
  - domain-healthcare-clinical/prompts/reasoning/medicine_clinical_decision_support.md
  - domain-healthcare-clinical/prompts/reasoning/medicine_clinical_history_elicitation.md
  - domain-healthcare-clinical/prompts/pharmacology/medicine_drug_interaction_checker.md
---

# Differential Diagnosis Generator

**Objective:** Generate a probability-ranked differential diagnosis from a clinical presentation — with supporting and refuting features, distinguishing tests, flagged "can't-miss" diagnoses, and a prioritized diagnostic workup — to support, not replace, clinician reasoning.

**Important Disclaimer:** This tool is for educational and clinical decision support only. It does not replace clinical judgment. All differential diagnoses must be validated by qualified healthcare professionals considering the full clinical context.

**When to use:**
- Building or stress-testing a differential for a presenting complaint.
- Teaching diagnostic reasoning (problem representation, illness scripts, framework selection).
- Checking for anchoring or premature closure on an obvious diagnosis.
- Identifying which test will best discriminate between competing diagnoses.

**When NOT to use:**
- As a substitute for a clinician's history, physical exam, and judgment.
- For an unstable or rapidly deteriorating patient who needs immediate evaluation and stabilization, not a written differential.
- When patient-specific data is too thin to reason responsibly — gather more first.

**Audience:** Licensed clinicians, residents, advanced-practice providers, and health-professions students working under supervision.

---

## Inputs / Context

Supply the case data below. Paste raw clinical data wrapped in a `<case_data>` tag so it can be referenced by name; reason only from what is inside `<case_data>` and flag what is missing.



### Clinical Presentation

Please provide the following information:

**Chief Complaint:**
- [Primary symptom and duration]

**Key History of Present Illness:**
- [Onset, progression, quality, severity, timing, modifying factors]

**Vital Signs (if available):**
- Temperature, Heart Rate, Blood Pressure, Respiratory Rate, O2 Saturation

**Relevant Physical Exam Findings:**
- [Positive and pertinent negative findings]

**Initial Test Results (if available):**
- Labs, imaging, ECG, etc.

**Patient Demographics:**
- Age, sex, relevant comorbidities

**Risk Factors:**
- [Relevant exposures, travel, occupation, medications]

---

## Constraints

### Must
- Ground every diagnosis and probability in established clinical epidemiology and evidence; cite the source TYPE (clinical decision rule, guideline, primary literature, textbook/expert consensus) rather than inventing a citation.
- Flag every point where clinician verification — history, exam, or confirmatory test — is required before acting.
- Always surface "can't-miss" (life-threatening / time-sensitive) diagnoses even when their probability is low.
- State a confidence level and name what additional information would change the assessment.
- Never fabricate test characteristics, probability figures, decision-rule thresholds, or citations; if a figure is uncertain, say so and give a qualitative range.

### Must Not
- Do not present output as a definitive diagnosis or replace clinician judgment.
- Do not omit refuting features or features that don't fit — a one-sided differential is unsafe.
- Do not anchor on the first or most obvious diagnosis without considering mimics.
- Do not recommend tests that will not meaningfully change management.

---

## Instructions

### Step 1: Problem Representation

Synthesize the presentation into a concise clinical summary:

**Semantic Qualifier Format:**
"[Age]-year-old [sex] with [relevant PMH] presenting with [duration] of [key symptoms], with [key exam/test findings]."

**Identify:**
- Anatomical location(s) affected
- Pathophysiological process (infectious, inflammatory, vascular, neoplastic, traumatic, metabolic, degenerative, congenital, autoimmune)
- Acuity (hyperacute, acute, subacute, chronic)

### Step 2: Generate Initial Differential

Using a systematic approach, consider diagnoses across categories:

**Framework Options:**
- **Anatomical:** Consider each organ system that could produce the symptoms
- **Pathophysiological:** Apply the mnemonic VINDICATE (Vascular, Infectious, Neoplastic, Degenerative, Iatrogenic, Congenital, Autoimmune, Traumatic, Endocrine/Metabolic)
- **Epidemiological:** Consider common diagnoses first, then rare

### Step 3: Prioritize by Probability

For each diagnosis, estimate probability considering:

1. **Base Rate:** How common is this condition in the relevant population?
2. **Clinical Features:** How well does the presentation match the classic presentation?
3. **Risk Factors:** Does the patient have risk factors that increase likelihood?
4. **Epidemiology:** Geographic, seasonal, exposure considerations

**Probability Categories:**
- **High (>30%):** Most likely diagnosis
- **Moderate (10-30%):** Should be actively considered
- **Low (2-10%):** Possible but less likely
- **Very Low (<2%):** Unlikely but dangerous ("can't miss")

### Step 4: Identify "Can't Miss" Diagnoses

Regardless of probability, flag diagnoses that are:
- Life-threatening if missed
- Time-sensitive for treatment
- Have high morbidity if delayed

---

## Output Format

### Differential Diagnosis Report

```
CLINICAL SUMMARY
================
[One-sentence semantic qualifier summarizing the case]

PRIMARY DIAGNOSTIC CONSIDERATION
================================
1. [Diagnosis Name]
   Probability: [High/Moderate/Low] ([X]%)

   Supporting Features:
   - [Feature 1 from presentation]
   - [Feature 2 from presentation]
   - [Feature 3 from presentation]

   Features Against:
   - [Atypical or missing feature]

   Key Distinguishing Features:
   - [What would you expect to see/not see with this diagnosis]

   Recommended Workup:
   - [Test 1]: Looking for [specific finding]
   - [Test 2]: Looking for [specific finding]

   Red Flags to Monitor:
   - [Warning sign indicating worsening]

ALTERNATIVE DIAGNOSES
=====================
2. [Diagnosis Name]
   Probability: [X]%

   Supporting Features:
   - [Feature 1]
   - [Feature 2]

   Features Against:
   - [Feature]

   Key Distinguishing Test:
   - [Test]: [Expected finding if positive]

3. [Diagnosis Name]
   Probability: [X]%

   Supporting Features:
   - [Feature 1]
   - [Feature 2]

   Features Against:
   - [Feature]

   Key Distinguishing Test:
   - [Test]: [Expected finding if positive]

[Continue for additional diagnoses...]

CAN'T MISS DIAGNOSES
====================
Even if lower probability, actively rule out:

- [Diagnosis]:
  Why it's critical: [Consequence if missed]
  How to rule out: [Key test or finding]

- [Diagnosis]:
  Why it's critical: [Consequence if missed]
  How to rule out: [Key test or finding]

DIAGNOSTIC WORKUP PRIORITY
==========================
Immediate (within hours):
1. [Test] - Rules out [diagnosis]
2. [Test] - Evaluates for [diagnosis]

Soon (within 24-48 hours):
1. [Test] - Further characterizes [finding]
2. [Test] - Assesses for [diagnosis]

Consider if initial workup unrevealing:
1. [Test] - Evaluates for [diagnosis]

CLINICAL DECISION POINTS
========================
If [Test Result]:
  - Increases probability of [Diagnosis A]
  - Proceed with [Next step]

If [Test Result]:
  - Increases probability of [Diagnosis B]
  - Proceed with [Next step]

UNCERTAINTY ACKNOWLEDGMENT
==========================
Confidence Level: [High/Moderate/Low]

Limitations of this analysis:
- [What information would improve accuracy]
- [What assumptions were made]
- [Areas of diagnostic uncertainty]

Recommend specialist consultation if:
- [Indication for specialty referral]
```

---

## Reasoning Quality Checks

### Self-Verification

After generating the differential, verify:

1. **Completeness Check:**
   - Have I considered all organ systems that could cause these symptoms?
   - Have I applied a systematic framework (VINDICATE, anatomical, etc.)?
   - Have I included common AND dangerous diagnoses?

2. **Consistency Check:**
   - Does each diagnosis actually explain the key findings?
   - Are my probability estimates internally consistent?
   - Have I accounted for features that DON'T fit each diagnosis?

3. **Bias Check:**
   - Am I anchoring on an obvious diagnosis?
   - Have I considered mimics and atypical presentations?
   - Am I affected by availability bias (recent similar case)?

4. **Can't Miss Check:**
   - What diagnosis, if missed, would cause the most harm?
   - Have I explicitly addressed how to rule it out?

### Flag Uncertainty

State explicitly:
- Which diagnoses you are most/least confident about
- What additional information would change your assessment
- Where the evidence is weak or conflicting

---

## False-Positive Prevention

❌ **DON'T:**
- Fabricate probability percentages, test sensitivity/specificity, or decision-rule cutoffs to sound precise.
- Cite a specific study, score, or guideline you cannot actually support — name the source TYPE instead.
- Drop "can't-miss" diagnoses because they are statistically unlikely.
- Present a confident single diagnosis and omit the competing possibilities.
- Hedge so heavily ("could be anything") that the differential gives the clinician no usable signal.

✅ **DO:**
- State the evidence TYPE behind each probability (epidemiology, decision rule, primary literature, expert consensus).
- Give a calibrated confidence level and qualitative probability bands when exact numbers aren't reliable.
- Flag life-threatening mimics explicitly and say how to rule each out.
- Recommend clinician confirmation for any actionable conclusion.
- Stay genuinely useful: commit to a ranked, discriminating workup the clinician can act on.

---

## Dual-Failure Prevention (QA-20)

This prompt must avoid **both** failure modes:

- **Failure of commission (harmful):** asserting a diagnosis or probability with false confidence, omitting a dangerous diagnosis, or fabricating a figure/citation that a clinician might rely on.
- **Failure of omission (useless):** retreating into "consult a specialist / could be anything / I can't say" without producing a structured, discriminating differential.

The correct output is decisive *and* bounded: a ranked differential with explicit supporting/refuting evidence, named source types, flagged uncertainty, can't-miss diagnoses, and a workup that narrows the list — while clearly framing the whole thing as input to clinician judgment.

---

## Special Considerations by Presentation Type

### Chest Pain
Always consider: ACS, PE, aortic dissection, tension pneumothorax, esophageal rupture, pericarditis/tamponade

### Shortness of Breath
Always consider: PE, pneumothorax, acute coronary syndrome, anaphylaxis, airway obstruction

### Altered Mental Status
Always consider: Hypoglycemia, hypoxia, intracranial process (stroke, bleed, mass), infection (meningitis, sepsis), toxic/metabolic, Wernicke's

### Abdominal Pain
Always consider by location and severity: Appendicitis, cholecystitis, pancreatitis, bowel obstruction, ischemic bowel, ruptured AAA, ectopic pregnancy

### Fever
Consider by pattern and associated symptoms: Infection (localize source), malignancy, autoimmune/inflammatory, drug fever

### Headache
Always consider: SAH, meningitis, temporal arteritis (in elderly), mass lesion, cerebral venous thrombosis

---

## Process Guidelines

### Evidence-Based Approach
- Base probabilities on published literature and clinical epidemiology when possible
- Cite clinical decision rules when applicable (Wells criteria, HEART score, etc.)

### Patient-Specific Calibration
- Adjust base rates for patient demographics, comorbidities, and risk factors
- Consider atypical presentations in elderly, immunocompromised, or diabetic patients

### Iterative Refinement
- Update differential as new information becomes available
- Be willing to revise probability estimates with new data

### Diagnostic Stewardship
- Recommend tests that will meaningfully change management
- Consider test characteristics (sensitivity, specificity) in interpretation
- Avoid unnecessary testing that won't change clinical decisions

---

**Critical Reminder:** This tool generates diagnostic hypotheses to support clinical reasoning. It does not replace the clinician's responsibility to:
- Perform thorough history and physical examination
- Consider the full clinical context
- Apply appropriate clinical judgment
- Recognize when urgent intervention is needed
- Consult specialists when appropriate

All probability estimates are approximations and must be interpreted in context.

---

## Example Output

```
CLINICAL SUMMARY
================
58-year-old man with hypertension and a 30-pack-year smoking history presenting
with 2 hours of substernal pressure-like chest pain radiating to the left arm,
associated with diaphoresis and dyspnea. Initial ECG shows nonspecific ST changes.

PRIMARY DIAGNOSTIC CONSIDERATION
================================
1. Acute Coronary Syndrome (NSTEMI / unstable angina)
   Probability: High

   Supporting Features:
   - Substernal pressure radiating to left arm with diaphoresis (classic anginal pattern)
   - Cardiac risk factors: age, male sex, HTN, heavy smoking
   - Exertional/dyspneic component

   Features Against:
   - Initial ECG nonspecific (does not exclude NSTEMI)

   Key Distinguishing Features:
   - Serial troponin elevation; dynamic ECG changes

   Recommended Workup:
   - Serial high-sensitivity troponin: looking for rise/fall pattern
   - Serial/repeat ECG: looking for evolving ischemic changes
   - Risk score (e.g., HEART score) to stratify

   Red Flags to Monitor:
   - Ongoing/worsening pain, hemodynamic instability, new arrhythmia

CAN'T MISS DIAGNOSES
====================
- Aortic dissection:
  Why it's critical: Catastrophic if anticoagulated as ACS by mistake.
  How to rule out: Pulse/BP differential, mediastinal widening on CXR; CT angiography if suspected.

- Pulmonary embolism:
  Why it's critical: Time-sensitive; overlaps with dyspnea + chest pain.
  How to rule out: Apply a validated rule (e.g., Wells/PERC); D-dimer or CTPA per pretest probability.

DIAGNOSTIC WORKUP PRIORITY
==========================
Immediate (within minutes-hours):
1. ECG (serial) - evaluates for ACS
2. High-sensitivity troponin (serial) - evaluates for myocardial injury
3. CXR - screens for dissection/alternative cause

UNCERTAINTY ACKNOWLEDGMENT
==========================
Confidence Level: Moderate-High that this is a cardiac/vascular emergency requiring
workup; specific diagnosis pending troponin trend and imaging.

Limitations of this analysis:
- Probabilities reflect clinical epidemiology and decision-rule logic (source TYPE:
  clinical decision rules + guideline-based risk stratification), not patient-specific
  calculated values.
- No physical exam findings (pulse differential, lung exam) were provided.

Recommend specialist consultation if:
- Troponin positive / ECG evolves → urgent cardiology.
- Dissection or PE suspected → emergent imaging and appropriate consult.

NOTE: This is decision support. Confirm with full clinical evaluation; do not act on any
single element above without clinician verification.
```

---

## Verification

- [ ] Differential is probability-ranked and uses a systematic framework.
- [ ] Each diagnosis lists supporting AND refuting features.
- [ ] "Can't-miss" diagnoses are flagged regardless of probability, with a rule-out plan.
- [ ] Source TYPE is stated for probabilities and decision rules; no fabricated figures or citations.
- [ ] A confidence level and information-that-would-change-it are stated.
- [ ] Recommended tests are discriminating and change management.
- [ ] Output is framed as decision support, with clinician verification flagged.
- [ ] Avoids both false confidence and uselessly vague hedging (QA-20).

---

## Techniques Used

- **ST-01 (Clear Objective Statement):** Opens with a single-sentence objective scoping the task to decision support.
- **RT-02 (Multi-Dimensional Reasoning):** Reasons across anatomical, pathophysiological, and epidemiological axes plus probability and "can't-miss" dimensions.
- **DS-02 (Evidence-Based Standards):** Anchors probabilities and tests to clinical epidemiology, decision rules, and stated source types.
- **QA-01 (Self-Verification):** Built-in completeness, consistency, bias, and can't-miss checks before finalizing.
- **QA-20 (Dual-Failure Prevention):** Explicitly guards against both harmful false confidence and unhelpful over-hedging.

---

## Related Prompts

- `domain-healthcare-clinical/prompts/reasoning/medicine_clinical_decision_support.md` — moves from a chosen diagnosis to a structured treatment decision.
- `domain-healthcare-clinical/prompts/reasoning/medicine_clinical_history_elicitation.md` — gathers the structured history that feeds this differential.
- `domain-healthcare-clinical/prompts/pharmacology/medicine_drug_interaction_checker.md` — checks the medication implications once a working diagnosis is set.
