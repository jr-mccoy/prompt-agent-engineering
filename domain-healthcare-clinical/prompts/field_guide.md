# Medicine & Healthcare Field Guide

**Purpose:** Prompt engineering techniques and ideas specifically curated for healthcare professionals, medical educators, clinical researchers, health administrators, and health technology developers.

**Library framing (v2, 2026-05-08):** This domain is built for **model testing and training**, not for production patient-care deployment. Prompts request the kind of direct, prescriptive clinical reasoning a senior attending writes for a peer colleague. Disclaimer headers, "support not replace" framing, and escalation boilerplate have been intentionally removed so that test signal reflects raw clinical capability rather than guardrail performance. Production wrappers handle deployment-time safety framing as a separate concern. See `EXPANSION_ROADMAP.md` for the full v2 framing rationale and lane-by-lane authoring standards.

---

## Prompt Categories for Medicine & Healthcare

### Core Clinical Reasoning (Original 10)

1. **Clinical History Elicitation Assistant** — Guide systematic patient history-taking through structured questioning sequences covering chief complaint, HPI, PMH, medications, allergies, family history, social history, and review of systems.

2. **Differential Diagnosis Generator** — Generate ranked differential diagnosis lists with probability estimates, key distinguishing features, and suggested diagnostic steps.

3. **Patient Education Material Adapter** — Transform complex medical information into patient-friendly explanations calibrated to health literacy level.

4. **Clinical Decision Support Reasoner** — Walk through clinical reasoning for treatment decisions with evidence quality, guidelines, patient factors, and risk-benefit analysis.

5. **Medical Literature Synthesizer** — Analyze research papers extracting study design, population, outcomes, limitations, and practice applicability.

6. **Handoff Communication Structurer** — Generate structured SBAR/I-PASS handoff communications ensuring critical information transfer.

7. **Adverse Event Analyzer** — Systematically analyze clinical adverse events using root cause analysis frameworks.

8. **Clinical Documentation Assistant** — Structure clinical notes ensuring completeness and compliance with documentation requirements.

9. **Drug Interaction and Contraindication Checker** — Evaluate medication lists for interactions, contraindications, and monitoring requirements.

10. **Quality Improvement Project Designer** — Design QI projects using PDSA, Lean, or Six Sigma methodologies.

### Expanded Clinical Areas (15 New Prompts)

11. **Emergency Triage Decision Support** — ESI-based triage reasoning with validated clinical decision rules (HEART, Wells, Ottawa) and disposition support.

12. **Psychiatric Assessment Support** — Structured MSE, suicide/violence risk assessment, capacity evaluation, safety planning, and biopsychosocial formulation.

13. **Chronic Disease Management Planner** — Longitudinal care plans with monitoring schedules, medication titration pathways, and self-management goals.

14. **Goals-of-Care Conversation Guide** — REMAP/SPIKES frameworks for serious illness conversations, code status discussions, and hospice transitions.

15. **Care Coordination and Transitions** — Discharge planning, medication reconciliation, readmission prevention, and post-discharge follow-up.

16. **Preventive Care Screening Advisor** — USPSTF/ACS/ACIP-based personalized screening and immunization recommendations.

17. **Pediatric Clinical Reasoning** — Age-adapted reasoning with weight-based dosing, developmental assessment, and age-specific differentials.

18. **Geriatric Care Assessment** — Comprehensive geriatric assessment covering functional status, cognition, falls, polypharmacy, and frailty.

19. **Informed Consent Communicator** — Structured consent conversations with risk disclosure, alternatives, and comprehension verification.

20. **Antibiotic Stewardship Advisor** — Empiric selection, de-escalation, duration optimization, and antimicrobial resistance stewardship.

21. **Laboratory and Diagnostic Interpreter** — Systematic lab interpretation with pattern recognition and Bayesian pre-test/post-test reasoning.

22. **Surgical Pre-operative Assessment** — Cardiac/pulmonary risk stratification and peri-operative medication management.

23. **Clinical Teaching Framework** — One-Minute Preceptor, SNAPPS, Socratic method, and feedback delivery for medical education.

24. **Telehealth Virtual Visit Guide** — Remote assessment techniques, modified physical examination, and escalation criteria.

25. **Nursing Clinical Assessment Framework** — Head-to-toe assessment, NANDA nursing diagnosis formulation, and individualized care planning.

---

## Relevant Prompt Engineering Techniques

### Tier 1: Essential Techniques for Medicine

#### NE-01: Single-Question Pacing Protocol
**Relevance:** Clinical history-taking and patient interaction
**Pattern:** Ask one question at a time, wait for response before proceeding
**Medical Application:** Patient interviews, symptom exploration, history elicitation
**Why Essential:** Mirrors proper clinical interviewing; prevents missing critical information; allows adaptive follow-up

#### QA-01: Chain-of-Verification
**Relevance:** Diagnostic and treatment safety
**Pattern:** Self-critique after initial response, verify claims with evidence, revise
**Medical Application:** Differential diagnosis validation, treatment plan review, dosing checks
**Why Essential:** Medical errors have severe consequences; verification is non-negotiable

#### RT-05: Evidence-Based Reasoning
**Relevance:** Clinical decision-making
**Pattern:** Require specific evidence for each claim with sources
**Medical Application:** Treatment recommendations, guideline application, literature interpretation
**Why Essential:** Medicine is evidence-based; recommendations must be traceable to evidence

#### RT-02: Multi-Dimensional Analysis Framework
**Relevance:** Comprehensive patient assessment
**Pattern:** Analyze from multiple dimensions systematically
**Medical Application:** Biopsychosocial assessment, systems-based review, holistic care planning
**Why Essential:** Patients are complex; single-dimension analysis misses critical factors

#### QA-04: Uncertainty Acknowledgment
**Relevance:** Clinical honesty and safety
**Pattern:** State confidence levels, acknowledge limitations, suggest verification
**Medical Application:** Diagnostic uncertainty, prognosis discussions, treatment recommendations
**Why Essential:** Overconfidence in medicine is dangerous; uncertainty must be explicit

---

### Tier 2: Highly Valuable Techniques

#### NE-07: Emotional Validation First
**Relevance:** Patient communication and rapport
**Pattern:** Acknowledge emotional impact before proceeding to clinical content
**Medical Application:** Breaking bad news, discussing prognosis, addressing patient fears
**Why Valuable:** Patients can't process information when emotionally overwhelmed; validation enables engagement

#### DT-02: Specific Focus Areas with Examples
**Relevance:** Systematic review and assessment
**Pattern:** Detailed enumeration of what to look for with concrete examples
**Medical Application:** Review of systems, physical exam findings, safety screening
**Why Valuable:** Prevents omissions in systematic assessments

#### ST-02: Structured Sequential Instructions
**Relevance:** Clinical protocols and procedures
**Pattern:** Numbered step-by-step instructions for complex tasks
**Medical Application:** Procedure checklists, diagnostic algorithms, treatment protocols
**Why Valuable:** Reduces errors in complex multi-step clinical processes

#### RP-01: Expert Role Assignment
**Relevance:** Specialist-level reasoning
**Pattern:** Assign specific expert persona with relevant expertise
**Medical Application:** Specialty consultations, complex case analysis, rare disease consideration
**Why Valuable:** Activates domain-specific reasoning patterns

#### NE-10: Probability-Weighted Scenarios
**Relevance:** Prognosis and risk communication
**Pattern:** Multiple scenarios with explicit probability weights
**Medical Application:** Outcome discussions, risk stratification, shared decision-making
**Why Valuable:** Communicates realistic ranges rather than false precision

---

### Tier 3: Valuable Supporting Techniques

#### DS-06: Prioritization and Severity Guidance
**Relevance:** Clinical triage and urgency assessment
**Pattern:** Rank findings by severity/urgency with explicit criteria
**Medical Application:** Problem list prioritization, triage decisions, treatment sequencing
**Supporting Role:** Ensures most critical issues addressed first

#### CM-01: Explicit Context Framing
**Relevance:** Case presentation and handoffs
**Pattern:** Provide all relevant background information upfront
**Medical Application:** Clinical case presentation, consultation requests, handoff communication
**Supporting Role:** Ensures complete information transfer

#### OC-01: Output Format Templates
**Relevance:** Standardized clinical documentation
**Pattern:** Exact formatting templates showing required structure
**Medical Application:** SOAP notes, SBAR handoffs, procedure notes
**Supporting Role:** Ensures documentation completeness and standardization

#### QA-02: Adversarial Stress-Test
**Relevance:** Safety and error prevention
**Pattern:** Attack your own answer to find vulnerabilities
**Medical Application:** Treatment plan review, diagnostic reasoning validation
**Supporting Role:** Identifies potential errors before they reach patients

#### RT-03: Tree of Thoughts
**Relevance:** Diagnostic reasoning
**Pattern:** Generate multiple approaches, compare pros/cons, select best
**Medical Application:** Differential diagnosis, treatment option analysis
**Supporting Role:** Systematic consideration of alternatives

---

### Tier 4: Specialized Applications

#### NE-08: Catchall Context Gathering
**Relevance:** Initial patient presentation
**Pattern:** Open-ended collection of unstructured information before systematic questioning
**Medical Application:** Chief complaint exploration, "tell me what's going on" opening
**Specialized Use:** Patient-centered history start

#### DT-04: Layered Analysis Structure
**Relevance:** Complex case analysis
**Pattern:** Both micro-level (specific findings) and macro-level (patterns, trends) analysis
**Medical Application:** Case synthesis, system-level quality review
**Specialized Use:** Complex multi-problem patients

#### RP-03: Multi-Persona Debate
**Relevance:** Multidisciplinary case discussion
**Pattern:** Simulate debate between experts with different priorities
**Medical Application:** Tumor board discussions, ethics consultations, complex care planning
**Specialized Use:** When multiple valid approaches exist

#### NE-11: Embedded Calculation Formulas
**Relevance:** Clinical calculations and risk scores
**Pattern:** Direct calculation formulas embedded in the prompt
**Medical Application:** GFR calculation, MELD score, CHADS-VASc, drug dosing
**Specialized Use:** Quantitative clinical assessments

#### AG-08: Evidence-Based Decision Gates
**Relevance:** Clinical quality checkpoints
**Pattern:** Require evidence/proof, not just assertions, for approval
**Medical Application:** Pre-procedure verification, medication reconciliation
**Specialized Use:** Safety-critical decision points

---

### Tier 5: Quality Assurance for Medical Content

#### QA-05: Citation Requirements
**Relevance:** Medical-legal and evidence standards
**Pattern:** Cite specific sources for claims, distinguish facts from interpretation
**Quality Application:** Ensuring recommendations are traceable to evidence

#### NE-06: Self-Audit Requirements
**Relevance:** Documentation and reasoning verification
**Pattern:** Verify output meets specific criteria before completion
**Quality Application:** Ensuring completeness of clinical assessments

#### AG-02: Skeptical Default Stance
**Relevance:** Diagnostic humility
**Pattern:** Default to skepticism, requiring overwhelming proof for certainty
**Quality Application:** Preventing premature diagnostic closure

#### DS-02: Metric Specification
**Relevance:** Clinical outcome measurement
**Pattern:** Define specific, measurable criteria
**Quality Application:** Quality improvement metrics, treatment goals

#### CM-02: Constraint Specification
**Relevance:** Clinical boundaries and contraindications
**Pattern:** Explicit must/must-not requirements
**Quality Application:** Safety constraints, contraindication adherence

---

## Technique Combinations for Medicine

### Clinical History Taking
```
NE-01 (Single-Question Pacing) + NE-08 (Catchall Context) + DT-02 (Focus Areas) + NE-07 (Emotional Validation)
```

### Differential Diagnosis
```
RT-05 (Evidence-Based) + RT-03 (Tree of Thoughts) + QA-01 (Verification) + QA-04 (Uncertainty) + DS-06 (Prioritization)
```

### Treatment Planning
```
RT-02 (Multi-Dimensional) + NE-10 (Probability Scenarios) + QA-02 (Stress-Test) + CM-02 (Constraints)
```

### Patient Communication
```
NE-07 (Emotional Validation) + RP-02 (Audience Framing) + QA-04 (Uncertainty) + NE-01 (Pacing)
```

### Clinical Documentation
```
OC-01 (Format Templates) + ST-02 (Sequential Instructions) + NE-06 (Self-Audit) + CM-01 (Context)
```

### Quality Improvement
```
RT-02 (Multi-Dimensional) + DT-04 (Layered Analysis) + DS-02 (Metrics) + DT-01 (Task Breakdown)
```

### Emergency Triage and Acute Care
```
DS-06 (Prioritization) + NE-11 (Embedded Calculations) + ST-02 (Sequential Instructions) + QA-04 (Uncertainty) + RT-05 (Evidence-Based)
```

### Psychiatric Assessment and Risk Evaluation
```
ST-02 (Sequential Instructions) + RT-02 (Multi-Dimensional/Biopsychosocial) + QA-04 (Uncertainty) + CM-01 (Context) + QA-02 (Adversarial/Challenging Assumptions)
```

### Goals-of-Care and Serious Illness Conversations
```
NE-07 (Emotional Validation First) + ST-02 (Sequential/REMAP/SPIKES) + CM-02 (Constraints) + QA-04 (Uncertainty) + RP-01 (Expert Role)
```

### Geriatric Comprehensive Assessment
```
RT-02 (Multi-Dimensional) + NE-11 (Embedded Calculations/Scores) + DS-06 (Prioritization) + ST-02 (Sequential) + QA-04 (Uncertainty)
```

### Preventive Care and Screening
```
RT-05 (Evidence-Based/USPSTF) + NE-10 (Probability/NNS) + CM-01 (Context/Demographics) + ST-02 (Sequential) + QA-04 (Uncertainty)
```

### Pediatric Clinical Reasoning
```
RT-03 (Tree of Thoughts/Age-Stratified) + NE-11 (Weight-Based Dosing) + CM-02 (Age-Specific Constraints) + RT-02 (Multi-Dimensional) + NE-07 (Parent Communication)
```

### Care Transitions and Discharge Planning
```
ST-02 (Sequential/Checklist) + OC-01 (Format Templates) + CM-01 (Context) + DS-06 (Prioritization/Risk) + QA-02 (Adversarial/Failure Modes)
```

### Antibiotic Stewardship
```
RT-05 (Evidence-Based/Guidelines) + ST-02 (Sequential/Empiric→De-escalation) + DS-06 (Spectrum Prioritization) + RT-02 (Source/Organism/Patient Analysis) + QA-02 (Challenging Broad-Spectrum Use)
```

### Lab and Diagnostic Interpretation
```
NE-11 (Calculations/Sensitivity/Specificity) + RT-03 (Decision Tree/Patterns) + DS-06 (Critical vs. Non-Critical) + ST-02 (Systematic Interpretation) + QA-04 (Uncertainty/Test Limitations)
```

### Clinical Teaching and Medical Education
```
RP-03 (Multi-Persona/Perspectives) + ST-02 (Structured Teaching Models) + CM-02 (Learner Level Adaptation) + RT-03 (Diagnostic Reasoning Teaching) + NE-01 (Socratic Method)
```

---

## Authoring Stance (v2)

Prompts in this library do not include disclaimer headers, "support not replace" framing, or scope-limitation boilerplate in the prompt body. The model is asked to respond as a senior attending in the relevant specialty writing for a peer colleague. Output is direct, prescriptive, and specific: drug names with doses, durations, and monitoring; differentials with concrete next steps; assessment lines that commit to an answer rather than hedging.

**What replaces safety overlay in the prompt body:**

- **Real clinical reasoning content.** Time windows, contraindications, age-specific physiology, drug-class interactions, validated decision-rule populations — these belong in the reasoning steps and output, not as warnings.
- **Structured output.** Multi-step output formats (assessment → plan → monitoring → contingencies) make the model commit to specific reasoning that can be evaluated.
- **Worked examples.** Each prompt includes one fully-worked input → output illustration so test evaluators can compare model output against a reference.

**What downstream consumers handle separately:**

- Clinician-in-the-loop verification
- Real-time patient data integration
- Local formulary / guideline reconciliation
- Deployment-time disclaimers and escalation pathways

See `EXPANSION_ROADMAP.md` for full lane scope, authoring standards, and technique stack.

---

*Last Updated: 2026-05-08 (v2 framing)*
*Part of the Prompting Guides repository expansion into domain-specific applications*


## Specialty Micro-Guides

- `medicine_behavioral_health_coordination_micro_guide.md`
- `medicine_clinical_visual_education_micro_guide.md`
