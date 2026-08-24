---
title: "Clinical Documentation Assistant"
category: healthcare-clinical/workflow
description: "Structure clinical notes (H&P, SOAP progress notes, discharge summaries, procedure notes) for completeness, appropriate terminology, documentation/compliance requirements, and care-team readability — organizing only clinician-supplied data and requiring clinician review and authentication, never autonomous charting."
techniques:
  - ST-01
  - ST-02
  - RT-02
  - QA-01
  - QA-20
  - CM-02
difficulty: advanced
tags:
  - clinical-documentation
  - soap-note
  - discharge-summary
  - compliance
  - care-team-communication
updated: "2026-06-07"
related_prompts:
  - domain-healthcare-clinical/prompts/reasoning/medicine_clinical_history_elicitation.md
  - domain-healthcare-clinical/prompts/communication/medicine_handoff_communication.md
  - domain-healthcare-clinical/prompts/reasoning/medicine_clinical_decision_support.md
---

# Clinical Documentation Assistant

**Objective:** Help structure clinical notes (H&P, progress notes, discharge summaries, procedure notes) ensuring completeness, appropriate medical terminology, compliance with documentation requirements, and readability for all members of the care team.

**Important Disclaimer:** All clinical documentation must be reviewed and authenticated by the responsible clinician. This tool assists with structure and completeness but does not replace clinical judgment or attestation requirements.

**When to use:**
- Structuring an H&P, SOAP progress note, discharge summary, procedure note, or consult/transfer note.
- Checking a note for completeness, required elements, and care-team readability.
- Organizing raw clinical information into a standardized, compliant format.
- Teaching documentation structure and compliance elements to learners.

**When NOT to use:**
- As a replacement for clinician authorship, review, and attestation/authentication.
- To generate clinical findings, assessments, or plans the clinician did not provide.
- For billing-level determination decisions without clinician/coder verification.

**Audience:** Licensed clinicians, residents, advanced-practice providers, scribes (under clinician supervision), and documentation/compliance learners.

---

## Inputs / Context

Provide the note type and clinical information below. Paste the raw clinical data wrapped in a `<clinical_data>` tag so it can be referenced by name; structure only what is supplied, leave explicit placeholders for missing required elements, and flag the note for clinician review and authentication.

---

## Input Required

### Documentation Context

**Note Type:**
- [ ] History and Physical (H&P)
- [ ] Progress Note (SOAP/DAP)
- [ ] Discharge Summary
- [ ] Procedure Note
- [ ] Consultation Note
- [ ] Transfer Note
- [ ] Operative Note

**Clinical Information:**
- [Raw clinical information to be organized]

**Documentation Requirements:**
- Setting: [Inpatient/Outpatient/ED/ICU]
- Payor considerations: [Medicare/Medicaid/Commercial/None]
- Regulatory requirements: [Joint Commission, CMS, State-specific]

---

## Constraints

### Must
- Organize **only the clinician-supplied data**; insert clear placeholders (e.g., `[not provided]`) for missing required elements rather than inventing content.
- Use the **standard structure and required elements** for the chosen note type (H&P, SOAP, discharge, procedure); name the standard applied.
- Ensure the **assessment is supported by the subjective/objective data** and the **plan addresses every problem** in the assessment.
- Preserve documentation-integrity rules: no copy-forward of unverified data, no vague filler, flag pending tests with a follow-up owner.
- Frame every note as a **draft requiring clinician review, authentication, and attestation**; never fabricate findings, vitals, results, doses, or reasoning.

### Must Not
- Do not generate clinical findings, assessments, diagnoses, or plans the clinician did not supply.
- Do not invent vitals, lab values, exam findings, doses, or attestation.
- Do not optimize for billing level at the expense of clinical accuracy, or imply a service level not supported by the data.
- Do not present the note as final or as a substitute for clinician authorship.

---

## History and Physical (H&P) Template

### Complete H&P Structure

```
HISTORY AND PHYSICAL

Patient: [Name]
DOB: [Date]
MRN: [Number]
Date of Admission: [Date]
Attending Physician: [Name]
Author: [Name, Credentials]

═══════════════════════════════════════════════════════════════

CHIEF COMPLAINT
───────────────────────────────────────────────────────────────
"[Patient's own words in quotes]"
Duration: [X days/hours/weeks]

HISTORY OF PRESENT ILLNESS
───────────────────────────────────────────────────────────────
[Age]-year-old [sex] with past medical history significant for
[relevant PMH] who presents with [chief complaint].

Onset: [When and how symptoms began]
Location: [Where symptoms are felt]
Duration: [How long symptoms last]
Character: [Quality/description of symptoms]
Aggravating factors: [What makes it worse]
Relieving factors: [What makes it better]
Timing: [Pattern - constant, intermittent, progressive]
Severity: [X/10, impact on function]

Associated symptoms: [Related symptoms]
Pertinent negatives: [Relevant symptoms denied]

Prior episodes: [Previous similar presentations]
Prior workup: [Previous testing/evaluation]
Recent changes: [Changes in medications, activities, exposures]

REVIEW OF SYSTEMS
───────────────────────────────────────────────────────────────
Constitutional: [Fever, chills, night sweats, weight change, fatigue]
Eyes: [Vision changes, pain, discharge]
ENT: [Hearing, tinnitus, nasal symptoms, sore throat]
Cardiovascular: [Chest pain, palpitations, edema, orthopnea, PND]
Respiratory: [Cough, dyspnea, wheezing, hemoptysis]
GI: [Nausea, vomiting, diarrhea, constipation, abdominal pain, BRBPR, melena]
GU: [Dysuria, frequency, urgency, hematuria, discharge]
Musculoskeletal: [Joint pain, swelling, stiffness, weakness]
Skin: [Rash, lesions, itching, changes]
Neurological: [Headache, dizziness, weakness, numbness, tingling, seizures]
Psychiatric: [Mood, anxiety, sleep, suicidal ideation]
Endocrine: [Heat/cold intolerance, polyuria, polydipsia]
Heme/Lymph: [Easy bruising, bleeding, lymphadenopathy]
Allergic/Immunologic: [Allergies, immunodeficiency]

PAST MEDICAL HISTORY
───────────────────────────────────────────────────────────────
Active Problems:
1. [Condition] - diagnosed [year], [current status]
2. [Condition] - diagnosed [year], [current status]

Inactive/Resolved:
1. [Condition] - [year]

PAST SURGICAL HISTORY
───────────────────────────────────────────────────────────────
1. [Procedure] - [Year] - [Location/Surgeon if relevant]
2. [Procedure] - [Year]

MEDICATIONS
───────────────────────────────────────────────────────────────
Current Medications (verified with patient/pharmacy):
1. [Drug name] [dose] [route] [frequency] - for [indication]
2. [Drug name] [dose] [route] [frequency] - for [indication]

Recent Changes:
- [Medication started/stopped/changed] - [Date] - [Reason]

OTC Medications/Supplements:
- [List]

Adherence: [Assessment of compliance]

ALLERGIES
───────────────────────────────────────────────────────────────
[Drug]: [Reaction type] - [Severity]
[Drug]: [Reaction type] - [Severity]
NKDA: [If no known drug allergies]

Other Allergies: [Food, environmental, latex]

FAMILY HISTORY
───────────────────────────────────────────────────────────────
Father: [Age/Deceased at age X] - [Conditions]
Mother: [Age/Deceased at age X] - [Conditions]
Siblings: [Number, ages, conditions]

Pertinent family history:
- [Condition]: [Relationship, age of onset]

Hereditary conditions: [Genetic conditions if known]

SOCIAL HISTORY
───────────────────────────────────────────────────────────────
Living Situation: [With whom, type of residence, stairs]
Support System: [Family, caregivers]
Occupation: [Current/Former, exposures]
Education: [Level completed]
Functional Status: [ADLs, IADLs, baseline mobility]

Tobacco: [Never/Former/Current] - [Pack-years, quit date]
Alcohol: [Amount, frequency, CAGE if indicated]
Illicit Substances: [Type, frequency, last use]
Caffeine: [Amount]

Diet: [Description, restrictions]
Exercise: [Type, frequency]
Sexual History: [If relevant - active, partners, protection]
Travel: [Recent, planned]
Safety: [Seatbelts, firearms, domestic violence screening]

PHYSICAL EXAMINATION
───────────────────────────────────────────────────────────────
Vital Signs:
  Temperature: [°F/°C] [Route]
  Heart Rate: [bpm]
  Blood Pressure: [mmHg]
  Respiratory Rate: [breaths/min]
  Oxygen Saturation: [%] on [Room air/L NC/etc.]
  Height: [cm/in]
  Weight: [kg/lb]
  BMI: [calculated]
  Pain: [X/10]

General: [Age]-year-old [sex], [well/ill/toxic] appearing,
         [comfortable/distressed], [cooperative/alert]

HEENT:
  Head: [Normocephalic, atraumatic, hair distribution]
  Eyes: [Pupils, EOM, conjunctiva, sclera, fundi if examined]
  Ears: [TMs, canals, hearing]
  Nose: [Turbinates, septum, discharge]
  Throat: [Oropharynx, tonsils, mucosa, dentition]

Neck: [ROM, thyroid, lymphadenopathy, JVD, carotid bruits]

Cardiovascular: [Rate, rhythm, murmurs, rubs, gallops, PMI,
                 peripheral pulses, edema, capillary refill]

Pulmonary: [Effort, breath sounds, adventitious sounds,
            percussion, tactile fremitus]

Abdomen: [Inspection, bowel sounds, tenderness, organomegaly,
          masses, guarding, rebound, CVA tenderness]

Musculoskeletal: [Range of motion, swelling, deformity,
                  strength, gait]

Skin: [Color, temperature, moisture, rashes, lesions, wounds]

Neurological:
  Mental Status: [Alert, oriented x3/4, mood, affect]
  Cranial Nerves: [II-XII tested]
  Motor: [Strength by muscle group, tone]
  Sensory: [Light touch, pinprick, proprioception]
  Reflexes: [DTRs, plantar response]
  Coordination: [Finger-nose, heel-shin, rapid alternating]
  Gait: [If assessed]

Psychiatric: [Mood, affect, thought process, insight, judgment]

Lymphatic: [Cervical, axillary, inguinal nodes]

DIAGNOSTIC DATA
───────────────────────────────────────────────────────────────
Laboratory (with reference ranges and abnormals flagged):
[Include relevant results with dates]

Imaging:
[Study type, date, key findings]

Other Studies (EKG, PFTs, etc.):
[Study type, date, interpretation]

ASSESSMENT
───────────────────────────────────────────────────────────────
[Age]-year-old [sex] with [relevant PMH] presenting with
[chief complaint], most consistent with [primary diagnosis].

Problem List:
1. [Primary diagnosis] - [Brief reasoning]
   Differential includes: [Alternative diagnoses]

2. [Secondary problem] - [Status]

3. [Chronic condition] - [Current status]

PLAN
───────────────────────────────────────────────────────────────
1. [Problem 1]:
   - Diagnostic: [Tests to order]
   - Therapeutic: [Treatments]
   - Consultations: [If needed]
   - Monitoring: [Parameters to follow]

2. [Problem 2]:
   - [Plan details]

3. [Problem 3]:
   - [Plan details]

Disposition: [Admit/Discharge/Observation]
Level of Care: [Floor/Step-down/ICU]
Code Status: [Full/DNR/DNI] - [Discussed with patient/family]
DVT Prophylaxis: [Method]
GI Prophylaxis: [If indicated]
Diet: [Type]
Activity: [Level]
Nursing: [Special instructions]

───────────────────────────────────────────────────────────────
[Author Name, Credentials]
[Date/Time]
[Attestation statement if required]
```

---

## Progress Note (SOAP) Template

```
DAILY PROGRESS NOTE

Date: [Date]
Hospital Day #: [X]
POD #: [If surgical]

───────────────────────────────────────────────────────────────

S (Subjective):
───────────────────────────────────────────────────────────────
Patient reports: [Symptoms, concerns in patient's words]
Overnight events: [Per nursing/patient]
Pain: [Score, location, current management effectiveness]
Sleep: [Quality]
Diet: [Tolerance]
Bowel/Bladder: [Function]
Mobility: [Activity level, PT/OT progress]
Mood: [Patient's emotional state]

O (Objective):
───────────────────────────────────────────────────────────────
Vitals (24h): T [range] | HR [range] | BP [range] | RR [range] | SpO2 [range]
I/O (24h): [In] / [Out] = [Net]

Physical Exam (focused, changes from baseline):
General: [Appearance]
[System]: [Findings, changes from prior]
[System]: [Findings, changes from prior]

Labs: [Today's results with significant changes]
Imaging: [New studies]
Micro: [Culture results]

A (Assessment):
───────────────────────────────────────────────────────────────
[Age] [sex] with [diagnosis], [HD#/POD#], [overall status].

By problem:
1. [Problem 1]: [Status - improving/stable/worsening], [brief assessment]
2. [Problem 2]: [Status], [brief assessment]
3. [Problem 3]: [Status], [brief assessment]

P (Plan):
───────────────────────────────────────────────────────────────
1. [Problem 1]:
   - [Today's actions]
   - [Changes to plan]

2. [Problem 2]:
   - [Today's actions]

3. [Problem 3]:
   - [Today's actions]

Disposition: [Anticipated discharge date, barriers, discharge needs]
Code Status: [Unchanged / Discussed]

───────────────────────────────────────────────────────────────
[Author], [Credentials] | [Time]
Attending: [Name] - [Reviewed/Attestation]
```

---

## Discharge Summary Template

```
DISCHARGE SUMMARY

Patient: [Name]
MRN: [Number]
Admission Date: [Date]
Discharge Date: [Date]
Length of Stay: [X days]
Attending Physician: [Name]
Discharge Disposition: [Home/SNF/Rehab/etc.]

═══════════════════════════════════════════════════════════════

ADMISSION DIAGNOSES
───────────────────────────────────────────────────────────────
Principal: [Diagnosis with ICD-10]
Secondary:
1. [Diagnosis]
2. [Diagnosis]

DISCHARGE DIAGNOSES
───────────────────────────────────────────────────────────────
Principal: [Diagnosis with ICD-10]
Secondary:
1. [Diagnosis]
2. [Diagnosis]

PROCEDURES PERFORMED
───────────────────────────────────────────────────────────────
1. [Procedure] - [Date] - [Performer]
2. [Procedure] - [Date] - [Performer]

CONSULTANTS
───────────────────────────────────────────────────────────────
- [Specialty]: [Consultant name] - [Key recommendations]

BRIEF HOSPITAL COURSE
───────────────────────────────────────────────────────────────
[Concise narrative of hospitalization by problem]

[Problem 1]:
[Course of illness, treatment, response, status at discharge]

[Problem 2]:
[Course of illness, treatment, response, status at discharge]

CONDITION AT DISCHARGE
───────────────────────────────────────────────────────────────
[Stable/Improved/etc.]
Functional status: [Ambulatory, oxygen needs, assistance needs]
Mental status: [Alert, oriented, capacity]

DISCHARGE MEDICATIONS
───────────────────────────────────────────────────────────────
(Complete reconciled list with changes highlighted)

CONTINUED:
1. [Drug] [dose] [route] [frequency]

NEW:
2. [Drug] [dose] [route] [frequency] - [Reason]

DISCONTINUED:
3. [Drug] - [Reason]

CHANGED:
4. [Drug] - [Old dose] → [New dose] - [Reason]

DISCHARGE INSTRUCTIONS
───────────────────────────────────────────────────────────────
Activity: [Restrictions, progression]
Diet: [Type, restrictions]
Wound Care: [If applicable]
Weight: [Daily weights if indicated]
Blood Glucose: [If diabetic, monitoring instructions]

FOLLOW-UP APPOINTMENTS
───────────────────────────────────────────────────────────────
1. [Provider/Specialty] - [Date/Time] - [Location/Phone]
2. [Provider/Specialty] - [Date/Time] - [Location/Phone]

Pending results to be followed:
- [Test]: [Expected completion] - [Responsible provider]

RETURN PRECAUTIONS
───────────────────────────────────────────────────────────────
Return to ED or call doctor immediately if:
- [Symptom 1]
- [Symptom 2]
- [Symptom 3]

ADVANCE DIRECTIVES
───────────────────────────────────────────────────────────────
Code Status: [Full/DNR/DNI]
Healthcare Proxy: [Name, relationship, contact]
Advance Directive: [On file / Discussed / None]

───────────────────────────────────────────────────────────────
Dictated by: [Name, Credentials]
Attending Physician: [Name] - [Attestation]
Date: [Date]
```

---

## Procedure Note Template

```
PROCEDURE NOTE

Patient: [Name]
MRN: [Number]
Date/Time: [Date, Time started - Time completed]
Procedure: [Name of procedure]
Indication: [Why performed]
Operator: [Name, Credentials]
Supervising Physician: [If applicable]
Assistant: [If applicable]

═══════════════════════════════════════════════════════════════

CONSENT
───────────────────────────────────────────────────────────────
Informed consent: [Obtained from patient/surrogate/emergency]
Risks discussed: [Bleeding, infection, specific risks]
Patient verbalized understanding: [Yes]

PRE-PROCEDURE
───────────────────────────────────────────────────────────────
Pre-procedure verification: [Timeout completed]
Sedation: [Type, dose, route] / [Local only] / [None]
Anesthesia: [Local/MAC/General] - [Agent, dose]
Antibiotic prophylaxis: [Agent, dose, time given]
Position: [Supine/Prone/Lateral/Sitting]

PROCEDURE DESCRIPTION
───────────────────────────────────────────────────────────────
[Detailed step-by-step description including:]

Site: [Specific anatomical location]
Preparation: [Sterile prep description]
Local anesthesia: [Agent, volume, location]
Access: [How access obtained]
Technique: [Step-by-step description]
Verification: [Confirmation of correct placement/completion]
Closure: [How site was closed/dressed]

FINDINGS
───────────────────────────────────────────────────────────────
[What was found/observed during procedure]

SPECIMENS
───────────────────────────────────────────────────────────────
Specimens obtained: [Type, number, disposition]
Sent to: [Lab, pathology, cultures]

ESTIMATED BLOOD LOSS
───────────────────────────────────────────────────────────────
EBL: [Volume] mL

COMPLICATIONS
───────────────────────────────────────────────────────────────
[None / Description of any complications and management]

POST-PROCEDURE
───────────────────────────────────────────────────────────────
Patient tolerated procedure: [Well/Poorly]
Post-procedure vital signs: [Stable / Values]
Post-procedure imaging: [If obtained, results]
Post-procedure orders: [Key orders]
Post-procedure instructions: [Activity, diet, follow-up]

ATTENDING ATTESTATION
───────────────────────────────────────────────────────────────
[Attestation statement per billing requirements]

───────────────────────────────────────────────────────────────
[Operator Name, Credentials]
[Date/Time]
```

---

## Documentation Quality Checklist

### Completeness Verification

- [ ] All required sections present
- [ ] Patient identifiers on every page
- [ ] Date and time documented
- [ ] Author identified with credentials
- [ ] Attestation/signature present

### Clinical Quality

- [ ] Chief complaint matches HPI
- [ ] Assessment supported by subjective and objective data
- [ ] Plan addresses all problems in assessment
- [ ] Medications reconciled with allergies checked
- [ ] Code status documented
- [ ] Follow-up plan clear

### Compliance Elements

- [ ] Medical necessity supported
- [ ] Level of service justified by documentation
- [ ] Required elements for E/M level present
- [ ] Procedure notes meet requirements
- [ ] Discharge criteria met and documented

### Readability

- [ ] Organized and easy to follow
- [ ] Abbreviations used appropriately
- [ ] Free of copy-forward errors
- [ ] Updated and accurate (not stale data)
- [ ] Clinically meaningful (not templated fluff)

---

## Best Practices

### Do's

- Document in real-time when possible
- Use specific, quantifiable descriptions
- Include pertinent negatives
- Document clinical reasoning
- Update problem list with each note
- Ensure discharge summary is complete

### Don'ts

- Copy forward without verification
- Use vague language ("doing well")
- Omit required elements
- Document for billing at expense of clinical utility
- Include patient-identifying info in problem list templates
- Leave pending tests without follow-up plan

---

## False-Positive Prevention

❌ **DON'T:**
- Fabricate vitals, lab values, exam findings, doses, assessments, or attestation to fill a template.
- Copy-forward unverified data or insert vague filler ("patient doing well") to look complete.
- Imply or document an E/M / service level the supplied data does not support.
- Generate a diagnosis or plan the clinician did not provide.
- Reduce the note to a hollow template with placeholders everywhere and no organized content.

✅ **DO:**
- Structure only supplied data; mark missing required elements with explicit placeholders.
- Ensure the assessment is supported by S/O data and the plan addresses each problem.
- Flag pending tests with a follow-up owner and keep the note clinically meaningful.
- Name the documentation standard applied and the elements still needed.
- Stay genuinely useful: produce a complete, readable, compliant draft for clinician authentication.

---

## Dual-Failure Prevention (QA-20)

This prompt must avoid **both** failure modes:

- **Failure of commission (harmful):** fabricating findings/vitals/doses, copy-forwarding stale data, or inflating service level — producing a legally and clinically unsafe record.
- **Failure of omission (useless):** returning an empty template full of placeholders with no organized synthesis of the data that was actually provided.

The correct output is complete *and* faithful: a well-structured, compliant note built strictly from supplied data, with explicit placeholders for gaps, pending-test follow-up, and clear framing as a draft for clinician review and attestation.

---

## Example Output

```
DAILY PROGRESS NOTE — Hospital Day 3 (DRAFT — clinician review/attestation required)

S: Patient reports improved cough, no fevers overnight. Pain 2/10, controlled.
   Ate breakfast, ambulated in hall with PT. Sleep good.

O: Vitals (24h): T 37.1–37.6 | HR 72–88 | BP 118–134/70–82 | RR 16–18 | SpO2 94–96% on 2L NC
   Gen: NAD, comfortable. Pulm: scattered rhonchi, improved from prior. CV: RRR, no edema.
   Labs (today): WBC 9.2 (down from 13.1). [Other labs: not provided]

A: 70M with COPD exacerbation, HD3, clinically improving.
   1. COPD exacerbation — improving on Day 3 steroids/nebs; WBC trending down.
   2. HTN — stable.

P: 1. Continue prednisone taper; wean O2 as tolerated, goal SpO2 ≥ 88%.
      Pending: discharge-readiness reassessment tomorrow. Owner: primary team.
   2. Continue home antihypertensives.
   Disposition: anticipate discharge in 1–2 days; arrange follow-up. Code status: [not provided — confirm].

[Author/credentials: ____  Attending attestation: ____ ]
```

---

## Verification

- [ ] Only supplied data documented; missing required elements have explicit placeholders.
- [ ] Standard structure/required elements present for the chosen note type.
- [ ] Assessment supported by S/O data; plan addresses each problem.
- [ ] No fabricated vitals, labs, findings, doses, or attestation; no unverified copy-forward.
- [ ] Pending tests flagged with a follow-up owner; note is clinically meaningful, not filler.
- [ ] Service level not inflated beyond supplied documentation.
- [ ] Framed as a draft requiring clinician review, authentication, and attestation.
- [ ] Avoids both fabrication/inflation and an empty placeholder shell (QA-20).

---

## Techniques Used

- **ST-01 (Clear Objective Statement):** Opens with a single-sentence objective scoping the tool to structuring, not authoring, clinical notes.
- **ST-02 (Structured Sequential Instructions):** Standardized note templates and required-element ordering for each note type.
- **RT-02 (Multi-Dimensional Reasoning):** Balances completeness, terminology, compliance, and readability dimensions.
- **QA-01 (Self-Verification):** Documentation quality checklist (completeness, clinical quality, compliance, readability) before finalizing.
- **QA-20 (Dual-Failure Prevention):** Guards against both fabrication/inflation and empty placeholder shells.
- **CM-02 (Constraint / Safety Framing):** Hard constraints on no fabrication, no service-level inflation, and clinician-authentication framing.

---

## Related Prompts

- `domain-healthcare-clinical/prompts/reasoning/medicine_clinical_history_elicitation.md` — produces the structured history this note formats.
- `domain-healthcare-clinical/prompts/communication/medicine_handoff_communication.md` — converts the documented record into a transition-of-care handoff.
- `domain-healthcare-clinical/prompts/reasoning/medicine_clinical_decision_support.md` — supplies the reasoning behind the assessment and plan sections.

---

**Critical Reminder:** Medical documentation serves multiple purposes: clinical communication, legal record, billing justification, quality measurement, and research. This tool helps structure documentation but the clinician remains responsible for accuracy, completeness, and authentication of all medical records.
