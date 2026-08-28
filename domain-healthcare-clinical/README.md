# Healthcare & Clinical: Comprehensive Guide

> Part of the [Non-Coding Quick Start](../NON_CODING_QUICK_START.md) system.
> This domain covers clinical decision support, patient communication, medical education, and healthcare documentation.

---

## When This Domain Applies

### Trigger Phrases

Route to this domain when the request mentions:

| Category | Trigger Phrases |
|----------|----------------|
| **Clinical Decisions** | "patient with...", "treatment options for", "differential diagnosis", "clinical decision", "evidence-based" |
| **Patient Communication** | "explain to patient", "patient education", "informed consent", "discharge instructions", "goals of care", "serious illness conversation" |
| **Documentation** | "clinical note", "H&P", "progress note", "handoff", "documentation" |
| **Medical Education** | "teach medical students", "case presentation", "clinical reasoning", "medical curriculum", "bedside teaching", "precepting" |
| **Quality/Safety** | "adverse event", "quality improvement", "patient safety", "medication error" |
| **Research Support** | "literature synthesis", "clinical study", "evidence review", "PICO" |
| **Emergency/Triage** | "triage", "acuity", "disposition", "acute care", "ESI", "decision rules" |
| **Mental Health/Psychiatry** | "psychiatric assessment", "suicide risk", "mental status exam", "safety planning", "capacity evaluation" |
| **Geriatrics** | "elderly patient", "falls", "polypharmacy", "cognitive decline", "functional status", "frailty", "Beers criteria" |
| **Palliative Care** | "goals of care", "serious illness", "hospice", "advance directive", "code status", "comfort care" |
| **Preventive Care** | "screening", "immunization", "wellness visit", "preventive care", "USPSTF" |
| **Pediatrics** | "pediatric", "child", "infant", "weight-based dosing", "developmental milestones" |
| **Care Transitions** | "discharge planning", "care coordination", "readmission prevention", "medication reconciliation" |
| **Infection/Stewardship** | "antibiotic", "antimicrobial", "stewardship", "de-escalation", "resistance" |
| **Telehealth** | "virtual visit", "telehealth", "telemedicine", "remote assessment" |
| **Lab Interpretation** | "lab results", "diagnostic test", "CBC", "metabolic panel", "interpret results" |
| **Surgical/Pre-op** | "pre-operative", "surgical risk", "clearance", "cardiac risk" |
| **Imaging/Radiology** | "which imaging", "CT vs MRI", "appropriateness criteria", "incidentaloma", "incidental finding", "Fleischner", "Bosniak", "TI-RADS" |
| **Oncology** | "tumor board", "cancer case", "staging", "chemotherapy", "targeted therapy", "biomarker", "NCCN" |
| **Cardiology (HFrEF/AC)** | "GDMT", "heart failure titration", "four pillars", "anticoagulation", "CHA2DS2-VASc", "HAS-BLED", "DOAC" |
| **Obstetrics** | "prenatal", "pregnancy risk", "preeclampsia prevention", "level of maternal care", "gestational diabetes screening" |
| **Addiction Medicine** | "substance use disorder", "opioid use disorder", "MOUD", "buprenorphine", "naloxone", "harm reduction", "ASAM" |
| **Sepsis/Acute Infection** | "sepsis", "septic shock", "Hour-1 bundle", "lactate", "source control" |
| **Renal/Hepatic Dosing** | "renal dose", "CrCl", "dialysis dosing", "hepatic impairment", "Child-Pugh", "CRRT dosing" |
| **Med Reconciliation** | "reconcile medications", "BPMH", "admission meds", "discharge meds", "home medications" |
| **Coding/Billing** | "E/M coding", "level of service", "MDM", "medical decision making", "99213", "99214", "time-based" |
| **Prior Auth/Appeals** | "prior authorization", "medical necessity letter", "denial appeal", "peer-to-peer" |
| **Nursing Escalation** | "nurse SBAR", "escalate to provider", "clinical deterioration", "rapid response" |
| **Medication Admin Safety** | "high-alert medication", "independent double check", "LASA", "look-alike sound-alike", "medication safety" |
| **Social Determinants** | "SDOH screen", "food insecurity", "housing instability", "IPV screen", "social work referral", "warm handoff" |

### User Personas

| Persona | Typical Needs |
|---------|--------------|
| **Physicians (Primary Care)** | Chronic disease management, preventive screening, goals-of-care conversations |
| **Physicians (Emergency)** | Triage decision support, clinical decision rules, disposition planning |
| **Physicians (Hospital/ICU)** | Care transitions, antibiotic stewardship, pre-operative assessment |
| **Psychiatrists/Psych NPs** | Psychiatric assessment, suicide risk evaluation, capacity determination |
| **Geriatricians** | Comprehensive geriatric assessment, polypharmacy review, frailty evaluation |
| **Surgeons/Proceduralists** | Informed consent communication, pre-operative optimization |
| **Pediatricians** | Age-adapted clinical reasoning, weight-based dosing, developmental screening |
| **Palliative Care Specialists** | Goals-of-care conversations, hospice transitions, serious illness communication |
| **Nurses** | Nursing assessment, care planning, handoff communication, patient education |
| **Medical Students/Residents** | Clinical reasoning coaching, bedside teaching, case presentations |
| **Healthcare Administrators** | Quality improvement, policy development, documentation standards |
| **Allied Health** | Patient communication, documentation, care planning |
| **Researchers** | Literature synthesis, study design, evidence evaluation |

### Out of Scope

- **Medical advice to patients directly** - This domain supports healthcare professionals, not patients
- **Diagnosis or treatment recommendations** - Supports reasoning, doesn't replace clinical judgment
- **Prescription guidance** - Always requires licensed professional oversight
- **Real-time emergency triage replacement** - Supports structured triage reasoning but does not replace bedside clinical assessment in real time (see `medicine_emergency_triage_decision_support.md` for structured triage reasoning support)

### Direct Related Resource Links

- [Psychology Specialty Resources](../domain-psychology/)
- [Non-Coding Healthcare Skills](../domain-agentic-resources/skills/non-coding/healthcare/)
- [Healthcare Image Generation Prompts](../domain-image-generation/healthcare/)

### Cross-Domain References

- **Psychotherapy/counseling frameworks** → See `domain-psychology/` (covers case conceptualization, cognitive distortion identification, therapeutic technique explanation)
- **This domain covers the medical/psychiatric angle** — structured clinical psychiatric assessment, risk evaluation, and psychopharmacology, complementing the therapy-focused psychology domain

---

## Critical Domain-Specific Considerations

### What Makes Healthcare Unique

Healthcare prompts operate in a domain where:

1. **Stakes are High** - Errors can cause patient harm or death
2. **Uncertainty is Inherent** - Medicine operates on probabilities, not certainties
3. **Context is Complex** - Multiple comorbidities, medications, and patient factors interact
4. **Evidence Evolves** - Guidelines change as new research emerges
5. **Regulation Applies** - HIPAA, informed consent, documentation requirements
6. **Shared Decision-Making** - Patient values and preferences must be incorporated

### The Medical Reasoning Difference

Unlike other domains, healthcare prompts must:

| Requirement | Why It Matters | How to Address |
|-------------|---------------|----------------|
| **Acknowledge uncertainty** | Overconfidence kills | Always include confidence levels |
| **Cite evidence quality** | Not all studies are equal | Use GRADE or similar frameworks |
| **Consider contraindications** | One size doesn't fit all | Systematically check patient factors |
| **Support, not replace** | Clinical judgment is paramount | Frame as decision support |
| **Handle edge cases** | Rare conditions can be serious | Include safety netting |
| **Respect patient autonomy** | Values vary | Support shared decision-making |

### Critical Success Factors

For healthcare prompts to be valuable, they must:

1. **Be Evidence-Based** - Reference guidelines, cite studies, grade evidence quality
2. **Acknowledge Limits** - State what's known, uncertain, and unknown
3. **Consider the Whole Patient** - Comorbidities, medications, preferences, social factors
4. **Support Not Replace** - Enhance clinician reasoning, don't dictate decisions
5. **Enable Safety Checks** - Include verification steps and red flag detection
6. **Facilitate Communication** - Bridge between clinical knowledge and patient understanding

### Common Failure Modes

| Failure | Example | Prevention |
|---------|---------|------------|
| **Overconfidence** | "The diagnosis is clearly X" | Always state confidence levels and differential |
| **Missing context** | Generic advice for complex patient | Require comprehensive patient information |
| **Outdated information** | Old guidelines | Note publication dates, recommend verification |
| **One-size-fits-all** | Same recommendation regardless of patient factors | Systematically address patient-specific considerations |
| **Ignoring uncertainty** | Presenting probabilities as certainties | Use explicit uncertainty language |
| **Scope creep** | Providing actual medical advice | Clear disclaimers, support framing |

---

## Recommended Techniques

### Core Techniques (Always Use)

| Technique | Application in Healthcare | Example |
|-----------|--------------------------|---------|
| **ST-02 Sequential Instructions** | Multi-step clinical reasoning processes | History → Exam → Differential → Testing → Treatment |
| **QA-04 Uncertainty Acknowledgment** | Calibrated confidence in findings | "High confidence (strong evidence)", "Low confidence (limited data)" |
| **CM-01 Context Framing** | Comprehensive patient context specification | PICO format, patient demographics, comorbidities |
| **ST-03 Output Specification** | Structured clinical documentation | SOAP notes, handoff templates, consult requests |
| **RT-05 Evidence-Based** | Guideline and literature references | "Per AHA 2023 guidelines...", "GRADE: Moderate" |

### Situational Techniques

| Situation | Add Technique | Why |
|-----------|--------------|-----|
| Treatment decisions | RT-02 Multi-Dimensional Analysis | Weigh risks, benefits, alternatives, patient preferences |
| Diagnostic workup | RT-03 Tree of Thoughts | Explore differential diagnosis branches |
| Patient education | CM-02 Audience Adaptation | Adjust complexity for health literacy |
| Quality improvement | DS-01 Framework Application | Apply systematic QI methodologies |
| Safety analysis | QA-02 Adversarial Thinking | Identify potential failure modes |

---

## Quality Indicators for Healthcare

### What "Good" Looks Like

**A high-quality healthcare prompt output:**

1. **States Evidence Quality**
   - Cites specific guidelines with dates
   - Notes level of evidence (RCT vs. observational vs. expert opinion)
   - Acknowledges when evidence is limited or conflicting

2. **Calibrates Confidence**
   - Uses explicit confidence levels (High/Moderate/Low)
   - Distinguishes between "likely" and "definite"
   - Notes what would change the assessment

3. **Considers Patient Factors**
   - Addresses contraindications
   - Accounts for comorbidities
   - Incorporates patient preferences when known

4. **Includes Safety Checks**
   - Flags red flags and warning signs
   - Notes when to seek additional consultation
   - Provides follow-up recommendations

5. **Supports Communication**
   - Translates clinical concepts for patients when needed
   - Provides shared decision-making points
   - Includes documentation guidance

### Confidence Calibration Framework

```markdown
## Evidence Grading (GRADE-aligned)

**High Confidence:**
- Multiple high-quality RCTs
- Consistent results across studies
- Directly applicable to patient population
- "Further research unlikely to change confidence"

**Moderate Confidence:**
- RCTs with limitations
- Consistent observational studies
- Mostly applicable population
- "Further research may change confidence"

**Low Confidence:**
- Observational studies only
- Inconsistent results
- Limited applicability
- "Further research likely to change confidence"

**Very Low Confidence:**
- Case reports or expert opinion
- Conflicting evidence
- Extrapolation required
- "Very uncertain about estimate"
```

### False-Positive Prevention for Healthcare

**DON'T:**

- Present diagnostic possibilities as confirmed diagnoses
- Recommend specific medications without clinical oversight
- State "the patient should" instead of "consider" or "discuss"
- Provide time-critical advice (emergencies need direct assessment)
- Assume normal baselines without patient-specific data
- Ignore social determinants of health
- Give generic advice when specific patient factors are provided
- Present guidelines as absolute rules (they're recommendations)

**DO:**

- Frame all output as decision support for qualified clinicians
- Include explicit uncertainty acknowledgment
- Note when guidelines may not apply to specific patient
- Provide alternatives for when first-line options are contraindicated
- Include "discuss with patient" for preference-sensitive decisions
- State "verify current guidelines" for rapidly evolving topics
- Flag when specialist consultation may be warranted
- Include safety netting and red flag criteria

---

## Existing Prompts in This Repository

> **Note:** Healthcare prompts are now located in `domain-healthcare-clinical/prompts/` for better organization.

### Exemplar Prompts (Study These)

| Prompt | Location | What It Demonstrates |
|--------|----------|---------------------|
| `medicine_clinical_decision_support.md` | [prompts/](prompts/reasoning/medicine_clinical_decision_support.md) | **Gold Standard** - PICO framework, evidence grading, risk-benefit analysis, uncertainty handling, safety checklist |
| `medicine_differential_diagnosis_generator.md` | [prompts/](prompts/reasoning/medicine_differential_diagnosis_generator.md) | Systematic differential generation with probability weighting and red flag identification |
| `medicine_patient_education_adapter.md` | [prompts/](prompts/communication/medicine_patient_education_adapter.md) | Health literacy adaptation, teach-back methods, cultural considerations |

### All Healthcare Prompts (63 total — 41 clinical + 22 medical education/HPE)

#### Core Clinical Reasoning (Existing)
| Prompt | Purpose |
|--------|---------|
| `medicine_clinical_decision_support.md` | Treatment decision reasoning framework (Gold Standard) |
| `medicine_differential_diagnosis_generator.md` | Systematic differential diagnosis |
| `medicine_clinical_history_elicitation.md` | History-taking frameworks |
| `medicine_drug_interaction_checker.md` | Interaction analysis support |
| `medicine_literature_synthesizer.md` | Evidence synthesis |

#### Communication & Documentation (Existing)
| Prompt | Purpose |
|--------|---------|
| `medicine_patient_education_adapter.md` | Patient communication adaptation |
| `medicine_handoff_communication.md` | SBAR and handoff templates |
| `medicine_clinical_documentation.md` | Note writing assistance |

#### Quality & Safety (Existing)
| Prompt | Purpose |
|--------|---------|
| `medicine_adverse_event_analyzer.md` | Safety event analysis |
| `medicine_quality_improvement.md` | QI project support |

#### Nursing (Existing + New)
| Prompt | Purpose |
|--------|---------|
| `nursing_quick_reference_handbook_creator_prompt.md` | Nursing reference creation |
| `nursing_clinical_assessment_framework.md` | **NEW** — Head-to-toe assessment, nursing diagnosis (NANDA), care plan development |

#### Emergency & Acute Care (New)
| Prompt | Purpose |
|--------|---------|
| `medicine_emergency_triage_decision_support.md` | **NEW** — ESI triage, clinical decision rules (HEART, Wells, Ottawa), disposition |
| `medicine_antibiotic_stewardship_advisor.md` | **NEW** — Empiric selection, de-escalation, duration, IV-to-PO, resistance stewardship |

#### Mental Health & Psychiatry (New)
| Prompt | Purpose |
|--------|---------|
| `medicine_psychiatric_assessment_support.md` | **NEW** — MSE, suicide/violence risk, capacity evaluation, safety planning |

#### Primary Care & Preventive (New)
| Prompt | Purpose |
|--------|---------|
| `medicine_chronic_disease_management_planner.md` | **NEW** — Longitudinal care plans, monitoring schedules, medication titration |
| `medicine_preventive_care_screening_advisor.md` | **NEW** — USPSTF/ACS/ACIP screening recommendations, immunization schedules |
| `medicine_lab_diagnostic_interpreter.md` | **NEW** — Lab panel interpretation, pattern recognition, Bayesian reasoning |

#### Palliative & End-of-Life (New)
| Prompt | Purpose |
|--------|---------|
| `medicine_goals_of_care_conversation_guide.md` | **NEW** — REMAP/SPIKES frameworks, code status, hospice transitions, family meetings |

#### Transitions & Coordination (New)
| Prompt | Purpose |
|--------|---------|
| `medicine_care_coordination_transitions.md` | **NEW** — Discharge planning, medication reconciliation, readmission prevention |

#### Special Populations (New)
| Prompt | Purpose |
|--------|---------|
| `medicine_pediatric_clinical_reasoning.md` | **NEW** — Age-adapted reasoning, weight-based dosing, developmental assessment |
| `medicine_geriatric_care_assessment.md` | **NEW** — Functional status, cognition, falls, polypharmacy, frailty |

#### Procedural & Surgical (New)
| Prompt | Purpose |
|--------|---------|
| `medicine_informed_consent_communicator.md` | **NEW** — Consent conversations, risk disclosure, comprehension verification |
| `medicine_surgical_preoperative_assessment.md` | **NEW** — Cardiac/pulmonary risk, peri-operative medication management |

#### Education & Telehealth (New)
| Prompt | Purpose |
|--------|---------|
| `medicine_clinical_teaching_framework.md` | **NEW** — One-Minute Preceptor, SNAPPS, Socratic method, feedback delivery |
| `medicine_telehealth_virtual_visit_guide.md` | **NEW** — Remote assessment, modified exam, escalation criteria |

#### Medical Education / Health Professions Education (New — 2026-05)

> **For health professions educators, faculty, and curriculum designers.** Full routing guide, competency frameworks, and technique recommendations: [`domain-medical-education/README.md`](../domain-medical-education/README.md)

**Case & Scenario Design (7 prompts)**
| Prompt | Purpose |
|--------|---------|
| `medical-education/case-scenario-design/meded_pbl_case_writer.md` | Write PBL trigger packets, facilitator guide, SDL resource suggestions |
| `medical-education/case-scenario-design/meded_tbl_application_exercise_designer.md` | Design TBL iRAT/tRAT sets and 4S application exercises |
| `medical-education/case-scenario-design/meded_virtual_patient_case_builder.md` | Build branching virtual patient cases with decision nodes and consequence logic |
| `medical-education/case-scenario-design/meded_progressive_disclosure_case_designer.md` | Design sequential cases with commitment steps and phase-by-phase revelation |
| `medical-education/case-scenario-design/meded_standardized_patient_scenario_writer.md` | Write SP scripts, doorway information, hidden history, emotional cues |
| `medical-education/case-scenario-design/meded_osce_station_designer.md` | Design complete OSCE stations: student task card, SP instructions, examiner checklist, standard-setting guidance |
| `medical-education/case-scenario-design/meded_simulation_scenario_designer.md` | Design simulation scenarios: manikin states, confederate roles, debriefing objectives |

**Assessment Tools (6 prompts)**
| Prompt | Purpose |
|--------|---------|
| `medical-education/assessment-tools/meded_nbme_style_mcq_writer.md` | Write NBME/USMLE-format clinical vignette MCQs with distractor rationale |
| `medical-education/assessment-tools/meded_oral_exam_case_designer.md` | Design oral exam cases with graduated probing questions and evaluator scoring guide |
| `medical-education/assessment-tools/meded_assessment_rubric_builder.md` | Build analytic/holistic/entrustment rubrics with behaviorally-anchored descriptors |
| `medical-education/assessment-tools/meded_workplace_based_assessment_tools.md` | Design mini-CEX, DOPS, CBD, EPA observation forms with feedback facilitation guides |
| `medical-education/assessment-tools/meded_milestone_narrative_writer.md` | Write ACGME milestone narratives with behavioral evidence and developmental framing |
| `medical-education/assessment-tools/meded_clinical_skills_checklist_designer.md` | Design observable-behavior checklists for clinical procedures and communication skills |

**Feedback & Remediation (3 prompts)**
| Prompt | Purpose |
|--------|---------|
| `medical-education/feedback-remediation/meded_learner_feedback_composer.md` | Compose specific, evidence-based feedback using R2C2/AID/SBI frameworks |
| `medical-education/feedback-remediation/meded_remediation_plan_designer.md` | Design root-cause-driven remediation plans with SMART goals and reassessment criteria |
| `medical-education/feedback-remediation/meded_debriefing_guide_designer.md` | Design PEARLS/GAS/advocacy-inquiry debriefing guides with facilitation scripts |

**Teaching Methods (6 prompts)**
| Prompt | Purpose |
|--------|---------|
| `medical-education/teaching-methods/meded_preceptor_teaching_script_writer.md` | Write scripted OMP and SNAPPS dialogue for specific clinical situations |
| `medical-education/teaching-methods/meded_small_group_facilitation_guide.md` | Design small-group facilitation guides with discussion questions and group dynamics management |
| `medical-education/teaching-methods/meded_journal_club_teaching_guide.md` | Design journal club facilitation guides with article-type-specific critique frameworks |
| `medical-education/teaching-methods/meded_lecture_redesign_planner.md` | Redesign lectures using chunking, retrieval practice, and interleaving |
| `medical-education/teaching-methods/meded_flipped_classroom_module_designer.md` | Design flipped classroom modules with pre-class packages and readiness assurance |
| `medical-education/teaching-methods/meded_faculty_development_module_designer.md` | Design faculty development modules targeting Kirkpatrick Level 3 behavior change |

#### Imaging & Radiology (New — 2026-04)
| Prompt | Purpose |
|--------|---------|
| `medicine_imaging_ordering_rationale.md` | **NEW** — Modality selection, ACR appropriateness criteria, protocol specification, documentation for prior auth |
| `medicine_incidental_findings_management.md` | **NEW** — Fleischner / Bosniak / TI-RADS / O-RADS follow-up, stopping rules, patient-facing communication |

#### Oncology (New — 2026-04)
| Prompt | Purpose |
|--------|---------|
| `medicine_oncology_case_framer.md` | **NEW** — Tumor board case structuring, staging, biomarkers, options with guideline anchors, decision question |

#### Cardiology Depth (New — 2026-04)
| Prompt | Purpose |
|--------|---------|
| `medicine_heart_failure_titration_advisor.md` | **NEW** — HFrEF GDMT four-pillar audit, next-step titration, pre/post-change monitoring |
| `medicine_anticoagulation_decision_support.md` | **NEW** — Agent/dose/duration across AF, VTE, mechanical valve; periprocedural plan |

#### Obstetrics (New — 2026-04)
| Prompt | Purpose |
|--------|---------|
| `medicine_prenatal_risk_stratification.md` | **NEW** — Antepartum risk inventory, level-of-care assignment, aspirin prophylaxis, surveillance plan |

#### Addiction Medicine (New — 2026-04)
| Prompt | Purpose |
|--------|---------|
| `medicine_addiction_medicine_assessment.md` | **NEW** — DSM-5-TR SUD assessment, ASAM level of care, MAT eligibility, harm reduction, non-stigmatizing language |

#### Sepsis / Acute Infection (New — 2026-04)
| Prompt | Purpose |
|--------|---------|
| `medicine_sepsis_recognition_framework.md` | **NEW** — Organ dysfunction screen, Hour-1 bundle, source control, mimics, escalation |

#### Clinical Pharmacy (New — 2026-04)
| Prompt | Purpose |
|--------|---------|
| `medicine_renal_hepatic_dose_adjustment.md` | **NEW** — CrCl-based dosing, AKI vs CKD, iHD/CRRT/PD, Child-Pugh, TDM |
| `medicine_medication_reconciliation.md` | **NEW** — BPMH from ≥2 sources, discrepancy classification, transition-specific lens, patient-facing list |

#### Coding & Revenue Cycle (New — 2026-04)
| Prompt | Purpose |
|--------|---------|
| `medicine_em_coding_level_justification.md` | **NEW** — 2021/2023 AMA E/M leveling by MDM or time; documentation justification |
| `medicine_prior_authorization_letter.md` | **NEW** — Medical necessity drafting, appeals, peer-to-peer prep |

#### Nursing Depth (New — 2026-04)
| Prompt | Purpose |
|--------|---------|
| `nursing_sbar_clinical_escalation.md` | **NEW** — Urgency triage, SBAR script, read-back, chain-of-command escalation |
| `nursing_medication_administration_safety.md` | **NEW** — Rights of administration, high-alert IDC, LASA screen, drug-specific pre-checks |

#### Allied Health / Social Work (New — 2026-04)
| Prompt | Purpose |
|--------|---------|
| `allied_health_sdoh_screening_response.md` | **NEW** — Urgency triage, warm handoff, protective documentation, closed-loop follow-up across food / housing / IPV / transportation / benefits |

#### Reference
| Resource | Purpose |
|----------|---------|
| `field_guide.md` | Healthcare field guide with technique recommendations |

---

## Planned Reorganization (Deferred)

The prompts directory is currently flat. As the domain grows past 40 prompts, a subdirectory structure modeled on `domain-software-engineering/` will improve discovery. Proposed layout:

```
prompts/
├── clinical-reasoning/      # differential, decision support, history, labs
├── specialties/             # cardiology, oncology, OB, psychiatry, pediatric, geriatric, addiction, ID
├── communication/           # patient ed, informed consent, goals-of-care, handoff, SBAR
├── documentation/           # clinical docs, E/M coding, prior auth
├── pharmacy-meds/           # interactions, stewardship, reconciliation, dose adjustment
├── safety-quality/          # adverse events, QI, sepsis recognition, med admin safety
├── care-coordination/       # transitions, chronic disease, telehealth, preventive
├── nursing/                 # assessment, SBAR, med safety, handbook creator
├── allied-health/           # SDOH, future PT/OT/SW
└── education-research/      # teaching, literature synthesis
```

This reorganization is deferred to a follow-up change to keep the diff reviewable and cross-references safely auditable.

---

## Templates

### Template 1: Clinical Decision Support

```markdown
# Clinical Decision Support Request

**Important:** This output supports clinical reasoning but does not replace physician judgment. All decisions must be made by qualified healthcare professionals.

## Clinical Question

**PICO Format:**
- **P**atient: [Age, sex, relevant demographics, presenting condition]
- **I**ntervention: [Treatment/test being considered]
- **C**omparison: [Alternative options]
- **O**utcome: [Desired clinical outcomes]

## Patient Context

**Demographics:** [Age, sex, weight if relevant]

**Primary Condition:** [Diagnosis or chief complaint]

**Comorbidities:**
- [Condition 1]
- [Condition 2]

**Current Medications:**
- [Medication 1 - dose]
- [Medication 2 - dose]

**Allergies:** [List with reaction types]

**Relevant Labs/Imaging:** [Pertinent results]

**Patient Preferences:** [If known - values, concerns, treatment goals]

**Social Factors:** [Insurance, adherence history, support system]

## Instructions

1. Identify relevant evidence (guidelines, key studies)
2. Apply evidence to this specific patient
3. Analyze risks and benefits for each option
4. Consider contraindications and patient factors
5. Provide recommendation with confidence level
6. Include shared decision-making points
7. Note safety checks and follow-up needs

## Expected Output Format

- Clinical question in PICO format
- Evidence summary with quality grades
- Patient-specific analysis
- Risk-benefit comparison
- Recommendation with confidence level
- Implementation guidance
- Safety checklist
- Shared decision-making points
```

### Template 2: Patient Education Adaptation

```markdown
# Patient Education Material

**Objective:** Adapt clinical information for patient understanding

## Clinical Topic
[Medical condition, treatment, or procedure to explain]

## Patient Profile

**Health Literacy Level:**
- [ ] Limited (6th grade reading level)
- [ ] Adequate (8th-9th grade)
- [ ] Proficient (no adaptation needed)

**Patient Characteristics:**
- Age: [Relevant for examples and concerns]
- Language preference: [Primary language]
- Cultural considerations: [If known]
- Learning preferences: [Visual, verbal, hands-on]

## Key Messages (3-5 Maximum)
1. [Most critical information]
2. [Second priority]
3. [Third priority]

## Required Elements

**Must Include:**
- What the condition/treatment IS (simple terms)
- What the patient SHOULD DO (clear actions)
- When to SEEK HELP (red flags)
- How to ASK QUESTIONS (empowerment)

**Must Avoid:**
- Medical jargon without explanation
- Overwhelming detail
- Scary statistics without context
- Assumptions about prior knowledge

## Output Format

Structure as:
1. Opening hook (why this matters to patient)
2. Simple explanation (analogy from daily life)
3. What to do (numbered action steps)
4. Warning signs (when to call/return)
5. Questions to ask your doctor
6. Summary in 2-3 sentences

## Verify Understanding

Include teach-back questions:
- "In your own words, what is the most important thing to remember?"
- "What will you do differently after this?"
```

### Template 3: Clinical Handoff Communication

```markdown
# Clinical Handoff Communication

**Framework:** SBAR (Situation-Background-Assessment-Recommendation)

## Handoff Type
- [ ] Shift change
- [ ] Unit transfer
- [ ] Discharge to outpatient
- [ ] Referral to specialist
- [ ] Code/emergency handoff

## Patient Information

**Identifiers:** [Name, MRN, DOB, Room]

**S - Situation:**
- Current condition in one sentence
- Why handoff is occurring now
- Stability status: [Stable/Guarded/Critical]

**B - Background:**
- Admission diagnosis and date
- Relevant medical history (brief)
- Key events this shift/hospitalization
- Current treatment plan

**A - Assessment:**
- Current vital signs
- Trending concerns
- Active problems (prioritized)
- What I'm worried about

**R - Recommendation:**
- Immediate tasks pending
- Follow-up items with timeframes
- Contingency plans: "If X happens, then Y"
- Outstanding consultations/results

## Critical Information

**Allergies:** [List with reactions]

**Code Status:** [Full code/DNR/DNI/Comfort]

**Isolation:** [Type if applicable]

**Safety Concerns:** [Fall risk, suicide precaution, etc.]

## Pending Items

| Item | Expected Time | Action if Abnormal |
|------|--------------|-------------------|
| [Lab/result] | [When] | [What to do] |

## Questions for Receiver

Ask receiving clinician:
- "What questions do you have?"
- "Would you like me to clarify anything?"
- "Do you feel you have enough information to care for this patient safely?"
```

### Template 4: Differential Diagnosis Framework

```markdown
# Differential Diagnosis Generator

**Disclaimer:** This supports clinical reasoning. Final diagnosis requires comprehensive evaluation by qualified clinicians.

## Presentation

**Chief Complaint:** [Patient's primary concern in their words]

**History of Present Illness:**
- Onset: [When did this start?]
- Location: [Where exactly?]
- Duration: [Constant vs. intermittent?]
- Character: [Quality/description]
- Aggravating factors: [What makes it worse?]
- Relieving factors: [What helps?]
- Associated symptoms: [What else?]

**Pertinent Positives:** [Symptoms that ARE present]

**Pertinent Negatives:** [Symptoms that ARE NOT present - helps narrow differential]

**Relevant History:**
- Past medical: [Relevant conditions]
- Medications: [Current meds]
- Family: [Relevant family history]
- Social: [Relevant exposures, habits]

## Physical Exam Findings
[Key findings on examination]

## Available Data
[Labs, imaging, prior workups]

## Instructions

Generate differential diagnosis:

1. **Most Likely Diagnoses (3-5)**
   - Probability estimate (%)
   - Key supporting findings
   - Key findings that would be expected but missing
   - Next step to confirm/exclude

2. **Must-Not-Miss Diagnoses**
   - Serious conditions that MUST be considered
   - Probability if low but consequence if missed is high
   - Minimum workup required to exclude

3. **Other Considerations**
   - Less likely but possible diagnoses
   - What would elevate their probability

4. **Red Flags**
   - Findings that require urgent action
   - Findings that would change management immediately

## Output Format

### Primary Differential
| Diagnosis | Probability | Key Supportive | Key Missing | Next Step |
|-----------|-------------|----------------|-------------|-----------|
| [Dx 1] | [%] | [Findings] | [Expected but absent] | [Test/action] |

### Must-Not-Miss
| Diagnosis | Why Dangerous | How to Exclude |
|-----------|---------------|----------------|
| [Dx] | [Consequence if missed] | [Minimum workup] |

### Red Flags Present
- [ ] None identified
- [ ] [Flag 1]: [Required action]
- [ ] [Flag 2]: [Required action]
```

### Template 5: Quality Improvement Analysis

```markdown
# Quality Improvement Project Framework

**Methodology:** PDSA (Plan-Do-Study-Act) Cycle

## Problem Statement

**What is the problem?**
[Describe in specific, measurable terms]

**Who is affected?**
[Patient population, staff, system]

**How big is the problem?**
- Current performance: [Baseline metric]
- Target performance: [Goal metric]
- Gap: [Difference to close]

**Why does it matter?**
- Patient impact: [Harm, outcomes, experience]
- Staff impact: [Workload, satisfaction]
- System impact: [Cost, efficiency, reputation]

## Root Cause Analysis

**Use 5 Whys:**
1. Why does [problem] occur? → [Answer 1]
2. Why does [Answer 1] occur? → [Answer 2]
3. Why does [Answer 2] occur? → [Answer 3]
4. Why does [Answer 3] occur? → [Answer 4]
5. Why does [Answer 4] occur? → [Root Cause]

**Fishbone Diagram Categories:**
- People: [Contributing factors]
- Process: [Contributing factors]
- Equipment: [Contributing factors]
- Environment: [Contributing factors]
- Materials: [Contributing factors]
- Measurement: [Contributing factors]

## Intervention Design

**Proposed Change:**
[What specifically will be different?]

**Evidence Base:**
- [ ] Literature support: [Citations]
- [ ] Internal precedent: [Similar initiatives]
- [ ] Expert recommendation: [Source]

**Resources Required:**
- Time: [Staff time needed]
- Training: [What and for whom]
- Equipment/supplies: [If any]
- Cost: [Estimated]

## PDSA Cycle

### Plan
- Objective: [What are we trying to accomplish?]
- Predictions: [What do we think will happen?]
- Data collection: [What will we measure, how, when?]

### Do
- Implementation steps: [Numbered actions]
- Timeline: [Specific dates]
- Who is responsible: [Named individuals]

### Study
- Results vs. predictions: [Compare]
- Lessons learned: [What worked, what didn't]
- Unintended consequences: [Any surprises?]

### Act
- Adopt: [If successful, how to spread?]
- Adapt: [If partially successful, what to modify?]
- Abandon: [If unsuccessful, what to try next?]

## Sustainability Plan

- How will this become standard practice?
- Who owns ongoing monitoring?
- What triggers re-evaluation?
```

---

## Worked Example

### Scenario: Physician Requesting Anticoagulation Decision Support

**User says:** "I have a 72-year-old patient with new atrial fibrillation. She has a history of diabetes and hypertension. I'm trying to decide about anticoagulation. Can you help me think through this?"

**Step 1: Classification**

- Task Type: DECIDE (choosing between treatment options)
- Domain: Healthcare/Clinical (clinical treatment decision)
- Specific Area: Anticoagulation decision-making

**Step 2: Context Gathering**

From the request, we have:
- Age: 72
- New diagnosis: Atrial fibrillation
- Comorbidities: Diabetes, hypertension

Missing information (would ask or note as limitations):
- Renal function (affects DOAC dosing)
- Bleeding history
- Fall risk
- Current medications (interactions)
- Patient preferences
- Weight

**Step 3: Template Selection**

Use **Template 1: Clinical Decision Support** - this is a treatment decision requiring systematic analysis of risks, benefits, and evidence.

**Step 4: Customization**

Apply to anticoagulation specifically:
- Add CHA₂DS₂-VASc score calculation
- Add HAS-BLED score calculation
- Include DOAC vs. warfarin comparison
- Note guideline recommendations (AHA/ACC/HRS)

**Step 5: Quality Check**

Verify output includes:
- [ ] Stroke risk quantification
- [ ] Bleeding risk quantification
- [ ] Contraindication check
- [ ] Drug interaction check (if meds known)
- [ ] Patient-specific factors
- [ ] Guideline-aligned recommendation
- [ ] Confidence level
- [ ] Shared decision-making points
- [ ] Safety monitoring plan

**Final Prompt:**

```markdown
# Anticoagulation Decision Support

**Important:** This supports clinical reasoning. Anticoagulation decisions require physician judgment considering complete patient context.

## Clinical Question (PICO)

**Patient:** 72-year-old female with newly diagnosed atrial fibrillation, diabetes, hypertension
**Intervention:** Oral anticoagulation
**Comparison:** No anticoagulation, aspirin alone
**Outcome:** Stroke prevention balanced against bleeding risk

## Patient Information

**Demographics:** 72F
**Primary Condition:** New-onset atrial fibrillation
**Comorbidities:** Type 2 diabetes mellitus, hypertension

**Information Needed (note if unavailable):**
- Renal function (Cr, CrCl)
- Weight
- Bleeding history
- Fall risk assessment
- Current medications
- Patient preferences regarding bleeding vs. stroke risk

## Instructions

1. **Calculate Stroke Risk (CHA₂DS₂-VASc)**
   - Score this patient with available information
   - Note components present/absent
   - Interpret annual stroke risk

2. **Calculate Bleeding Risk (HAS-BLED)**
   - Score with available information
   - Identify modifiable risk factors
   - Interpret bleeding risk

3. **Apply Guidelines**
   - AHA/ACC/HRS atrial fibrillation guidelines
   - Anticoagulation thresholds
   - DOAC vs. warfarin recommendations

4. **Patient-Specific Analysis**
   - Factors favoring anticoagulation
   - Factors requiring caution
   - Contraindications (absolute/relative)

5. **Compare Options**
   - DOAC options with dosing considerations
   - Warfarin (when preferred)
   - No anticoagulation (when appropriate)

6. **Provide Recommendation**
   - Include confidence level
   - Note what could change recommendation
   - Shared decision-making discussion points

7. **Safety Plan**
   - Monitoring requirements
   - Drug interactions to check
   - Patient education points
   - When to reassess

## Output Format

### Risk Assessment
- CHA₂DS₂-VASc: [Score] - [Annual stroke risk %]
- HAS-BLED: [Score] - [Bleeding risk interpretation]
- Net clinical benefit: [Assessment]

### Recommendation
- Recommendation: [Specific recommendation]
- Confidence: [High/Moderate/Low]
- Basis: [Guidelines/Evidence quality]

### Shared Decision-Making Points
- How to explain stroke risk to patient
- How to explain bleeding risk to patient
- What patient values to explore

### Safety Monitoring
- Labs to check before starting
- Ongoing monitoring schedule
- When to stop and reassess
```

**Expected Output Quality Markers:**

- Calculates CHA₂DS₂-VASc: 4 points minimum (age 1, female 1, DM 1, HTN 1) = ~4% annual stroke risk
- Notes information gaps (renal function, weight) affect DOAC choice
- References 2023 AHA/ACC/HRS guidelines
- Recommends anticoagulation based on score ≥2
- Discusses DOAC preference over warfarin for most patients
- Includes shared decision-making language
- Notes renal function needed for dosing
- Acknowledges bleeding risk but quantifies benefit

---

## Anti-Patterns for Healthcare

### Mistake 1: Providing Definitive Medical Advice

**Problem:** Stating diagnoses or treatments as if AI is the treating clinician

**Bad Prompt:**
```
What medication should I prescribe for my patient's hypertension?
```

**Good Prompt:**
```
For a clinical decision support analysis of antihypertensive options for a 55-year-old patient with newly diagnosed hypertension and diabetes, please provide:
- First-line options per JNC/AHA guidelines with evidence levels
- Patient-specific considerations (diabetes → ACEi/ARB preference)
- Contraindication checklist
- Monitoring requirements for each option
Frame as decision support for the treating physician to discuss with patient.
```

**Why it matters:** The AI's role is to support clinical reasoning with evidence, not to make treatment decisions.

---

### Mistake 2: Ignoring Uncertainty

**Problem:** Presenting clinical information as certain when medicine is probabilistic

**Bad Prompt:**
```
My patient has chest pain. Tell me what's causing it.
```

**Good Prompt:**
```
Generate a differential diagnosis for a 58-year-old male with acute onset chest pain, described as substernal pressure, radiating to left arm, with diaphoresis. Include:
- Probability estimates for each diagnosis
- Must-not-miss diagnoses regardless of probability
- Key distinguishing features for each
- Red flags requiring immediate action
- What additional information would change the differential
Acknowledge uncertainty explicitly in your assessment.
```

**Why it matters:** Overconfidence in diagnosis leads to anchoring bias and missed diagnoses.

---

### Mistake 3: Generic Recommendations for Complex Patients

**Problem:** Not accounting for patient-specific factors that change recommendations

**Bad Prompt:**
```
What's the best treatment for Type 2 diabetes?
```

**Good Prompt:**
```
Provide clinical decision support for diabetes medication selection for:
- 68-year-old with T2DM (A1c 8.5%)
- CKD Stage 3b (eGFR 35)
- History of heart failure (EF 40%)
- Currently on metformin 1000mg BID
Consider:
- Renal dosing requirements
- Cardiovascular benefit data
- Contraindications for this patient
- Guideline recommendations (ADA 2024)
- What to discuss with patient regarding options
```

**Why it matters:** Comorbidities fundamentally change treatment selection - one size does not fit all.

---

### Mistake 4: Missing Safety Netting

**Problem:** Not including what to watch for and when to seek help

**Bad Prompt:**
```
Create patient instructions for someone going home after a concussion.
```

**Good Prompt:**
```
Create discharge instructions for mild concussion (GCS 15, CT negative) for a 22-year-old patient, written at 6th-grade reading level. Include:
- What symptoms are normal and expected
- Red flag symptoms requiring immediate return to ED (with specific examples)
- Activity restrictions with timeline
- When they can return to sports/work (stepwise protocol)
- Who to contact with questions
- Follow-up appointment information
Format with clear headers and bullet points. Include a section they can show family members watching them.
```

**Why it matters:** Patients need to know when their situation is changing in a dangerous direction.

---

### Mistake 5: Not Verifying Patient Understanding

**Problem:** Assuming information delivery equals patient comprehension

**Bad Prompt:**
```
Explain diabetes management to a patient.
```

**Good Prompt:**
```
Create a diabetes self-management education session for a newly diagnosed Type 2 diabetic patient with limited health literacy. Include:
- Key concepts (limited to 3-4 most critical)
- Analogy for blood sugar (relatable everyday comparison)
- Specific action steps (numbered, concrete)
- Teach-back questions to verify understanding
- Visual aids description (what pictures would help)
- Follow-up resources in simple language
Structure so each concept can be checked for understanding before moving to the next.
```

**Why it matters:** Patients with low health literacy may nod along without understanding. Teach-back verifies actual comprehension.

---

## Quick Reference Card

```
╔═══════════════════════════════════════════════════════════════════════════╗
║                   HEALTHCARE PROMPT QUICK REFERENCE                        ║
╠═══════════════════════════════════════════════════════════════════════════╣
║                                                                           ║
║  ALWAYS INCLUDE:                                                          ║
║  □ Clinical disclaimer (supports reasoning, doesn't replace judgment)     ║
║  □ Evidence grading (cite sources with quality level)                     ║
║  □ Uncertainty acknowledgment (confidence: High/Med/Low)                  ║
║  □ Patient-specific factors (not generic advice)                          ║
║  □ Safety checks (contraindications, red flags, follow-up)                ║
║                                                                           ║
║  KEY FRAMEWORKS:                                                          ║
║  • Clinical questions: PICO (Patient, Intervention, Comparison, Outcome)  ║
║  • Evidence quality: GRADE (High → Very Low)                              ║
║  • Handoff: SBAR (Situation, Background, Assessment, Recommendation)      ║
║  • Quality improvement: PDSA (Plan, Do, Study, Act)                       ║
║                                                                           ║
║  CONFIDENCE CALIBRATION:                                                  ║
║  • High: Multiple RCTs, consistent results, directly applicable          ║
║  • Moderate: RCTs with limitations, or consistent observational          ║
║  • Low: Observational only, inconsistent, or extrapolated                ║
║  • Very Low: Case reports, expert opinion, or conflicting evidence       ║
║                                                                           ║
║  RED FLAG PATTERNS:                                                       ║
║  ✗ "The diagnosis is..." → ✓ "The most likely diagnosis is... (75%)"    ║
║  ✗ "You should prescribe..." → ✓ "Guidelines recommend considering..."  ║
║  ✗ Generic treatment advice → ✓ "For this patient specifically..."       ║
║  ✗ No uncertainty → ✓ "We're less certain about X because..."            ║
║                                                                           ║
║  EXEMPLAR PROMPTS TO STUDY:                                               ║
║  • medicine_clinical_decision_support.md (decision framework)             ║
║  • medicine_differential_diagnosis_generator.md (diagnostic reasoning)   ║
║  • medicine_patient_education_adapter.md (communication)                  ║
║                                                                           ║
╚═══════════════════════════════════════════════════════════════════════════╝
```

---

## Related Resources

| Resource | Purpose |
|----------|---------|
| [NON_CODING_QUICK_START.md](../NON_CODING_QUICK_START.md) | Universal non-coding principles |
| [domain-healthcare-clinical/prompts/](./prompts/) | All healthcare prompts (consolidated here) |
| [PROMPT_QUALITY_STANDARDS.md](../PROMPT_QUALITY_STANDARDS.md) | Quality tier definitions |
| [techniques/MASTER_TECHNIQUE_INDEX.md](../techniques/MASTER_TECHNIQUE_INDEX.md) | Complete technique catalog |

---

*Document Version: 2.1*
*Created: 2026-01-26*
*Updated: 2026-03-04 — Expanded from 11 to 26 prompts, added 2 templates*
*Updated: 2026-04-15 — Expanded from 26 to 41 prompts: added imaging (2), oncology (1), cardiology depth (2), obstetrics (1), addiction medicine (1), sepsis (1), clinical pharmacy (2), coding/revenue cycle (2), nursing depth (2), allied health / SDOH (1). Expanded trigger-phrase table to route the new prompts. Proposed subdirectory structure documented for follow-up.*
*Updated: 2026-05-15 — Added medical education / HPE subdirectory with 22 purpose-specific prompts for health professions educators (case design, assessment tools, feedback/remediation, teaching methods). Total: 63 prompts.*
*Domain: Healthcare & Clinical*
