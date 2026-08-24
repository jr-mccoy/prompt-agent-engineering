---
title: "Clinical Decision Support Reasoner"
category: healthcare-clinical/reasoning
description: "Provide structured, evidence-graded clinical reasoning for a treatment decision — guideline recommendations, patient-specific factors, contraindications, risk-benefit trade-offs, alternatives, and shared-decision points — explicitly flagging uncertainty as support for, not a replacement of, clinician judgment."
techniques:
  - ST-01
  - RT-02
  - DS-02
  - QA-01
  - QA-20
  - CM-02
difficulty: advanced
tags:
  - clinical-decision-support
  - evidence-based-medicine
  - risk-benefit
  - shared-decision-making
  - guidelines
updated: "2026-06-07"
related_prompts:
  - domain-healthcare-clinical/prompts/reasoning/medicine_differential_diagnosis_generator.md
  - domain-healthcare-clinical/prompts/pharmacology/medicine_drug_interaction_checker.md
  - domain-healthcare-clinical/prompts/education/medicine_literature_synthesizer.md
---

# Clinical Decision Support Reasoner

**Objective:** Provide structured clinical reasoning for treatment decisions, explicitly stating evidence quality, guideline recommendations, patient-specific factors, contraindications, and risk-benefit trade-offs while flagging areas of uncertainty.

**Important Disclaimer:** This tool supports clinical reasoning but does not replace physician judgment. All treatment decisions must be made by qualified healthcare professionals considering the complete clinical picture and patient preferences.

**When to use:**
- Working through a treatment-selection, testing, or management decision for a defined patient.
- Reconciling guideline recommendations with patient-specific factors and preferences.
- Preparing the evidence and risk-benefit framing for a shared-decision-making conversation.
- Surfacing contraindications, monitoring needs, and uncertainty before committing to a plan.

**When NOT to use:**
- As a substitute for clinician judgment, examination, or the full clinical picture.
- For emergent decisions where time-critical action is needed — stabilize and act first.
- When required patient context (comorbidities, organ function, meds, allergies) is unavailable.

**Audience:** Licensed clinicians, residents, advanced-practice providers, and clinical pharmacists; health-professions learners under supervision.

---

## Inputs / Context

Provide the clinical question and patient context below. Paste raw clinical data wrapped in a `<patient_context>` tag so it can be referenced by name; reason only from what is supplied and name any missing inputs that materially affect the recommendation.



### Clinical Question

**Decision Type:**
- [ ] Treatment selection
- [ ] Diagnostic test ordering
- [ ] Procedure recommendation
- [ ] Medication management
- [ ] Preventive care decision
- [ ] Specialist referral

**Specific Question:**
- [What clinical decision needs to be made?]

### Patient Context

**Demographics:**
- Age, Sex, Weight (if relevant)

**Primary Condition:**
- [Diagnosis or clinical presentation]

**Comorbidities:**
- [List relevant comorbid conditions]

**Current Medications:**
- [Complete medication list]

**Relevant Labs/Results:**
- [Pertinent test results]

**Allergies:**
- [Drug allergies and reactions]

**Patient Preferences (if known):**
- [Values, concerns, treatment goals]

**Social Factors:**
- [Insurance, cost concerns, adherence history, support system]

---

## Constraints

### Must
- Ground every recommendation in established evidence; cite the guideline/source TYPE (professional-society guideline, clinical decision rule, primary literature, expert consensus) rather than inventing a citation.
- State **recommendation strength** and **evidence quality** (GRADE-style) and a confidence level for each recommendation.
- Surface **contraindications, drug interactions, and monitoring needs**, and flag every point where clinician verification is required.
- Present **alternatives** (including conservative management) and explicit **shared-decision-making points**.
- Never fabricate dosages, interactions, effect sizes, decision-rule thresholds, or citations; if a figure is uncertain, say so and give a qualitative range.

### Must Not
- Do not present output as a definitive diagnosis/decision or replace clinician judgment.
- Do not overstate confidence or hide uncertainty and evidence gaps.
- Do not give a one-sided recommendation that omits risks, alternatives, or contraindications.
- Do not produce time-critical recommendations for emergent situations as a substitute for immediate clinical action.

---

## Clinical Reasoning Framework

### Step 1: Frame the Clinical Question

Structure the question using PICO format:

- **P**atient: Who is the patient and what are their characteristics?
- **I**ntervention: What treatment/test is being considered?
- **C**omparison: What are the alternatives?
- **O**utcome: What outcomes matter most?

```
CLINICAL QUESTION
=================
In a [patient description] with [condition],
should we [intervention]
compared to [alternative(s)]
to achieve [desired outcome]?
```

### Step 2: Identify Relevant Evidence

#### Guidelines

**Professional Society Guidelines:**
- Source: [Organization name, year]
- Recommendation: [Specific recommendation]
- Strength: [Strong/Conditional/Weak]
- Evidence Quality: [High/Moderate/Low/Very Low]

**Applicability Assessment:**
- Does this patient match the guideline population?
- Are there exclusion criteria that apply?
- How recent is the guideline?

#### Primary Literature

**Key Studies:**
- Study: [Name/Author, Year]
- Design: [RCT/Cohort/Case-control/Meta-analysis]
- Population: [Who was studied]
- Key Finding: [Result with numbers]
- Limitations: [Important caveats]

#### Clinical Decision Rules (if applicable)

- Rule name: [e.g., Wells Score, HEART Score]
- Patient's score: [Calculated value]
- Risk category: [Low/Moderate/High]
- Recommendation: [Based on score]

### Step 3: Apply Evidence to This Patient

#### Patient-Specific Factors

**Factors Favoring Treatment A:**
- [Factor 1 - how it applies]
- [Factor 2 - how it applies]

**Factors Favoring Treatment B:**
- [Factor 1 - how it applies]
- [Factor 2 - how it applies]

**Factors Requiring Caution:**
- [Factor 1 - specific concern]
- [Factor 2 - specific concern]

#### Contraindications Assessment

**Absolute Contraindications:**
- [Contraindication]: [Present/Absent]

**Relative Contraindications:**
- [Contraindication]: [Present/Absent] - [If present, how to weigh]

### Step 4: Risk-Benefit Analysis

#### Benefits of Recommended Approach

| Benefit | Magnitude | Time to Benefit | Evidence Quality |
|---------|-----------|-----------------|------------------|
| [Outcome 1] | [NNT or %] | [Timeframe] | [High/Mod/Low] |
| [Outcome 2] | [NNT or %] | [Timeframe] | [High/Mod/Low] |

#### Risks of Recommended Approach

| Risk | Frequency | Severity | Reversible? |
|------|-----------|----------|-------------|
| [Risk 1] | [%] | [Mild/Mod/Severe] | [Yes/No] |
| [Risk 2] | [%] | [Mild/Mod/Severe] | [Yes/No] |

#### Net Benefit Assessment

**For typical patient matching this profile:**
- Estimated benefit: [Description with numbers if available]
- Estimated risk: [Description with numbers if available]
- Net benefit: [Positive/Neutral/Negative/Uncertain]

**For this specific patient:**
- Factors increasing benefit: [List]
- Factors increasing risk: [List]
- Adjusted assessment: [Description]

### Step 5: Consider Alternatives

#### Option 1: [Treatment/Approach Name]

**Mechanism:** [How it works]
**Evidence:** [Summary of evidence]
**For this patient:**
- Pros: [List]
- Cons: [List]
- Monitoring required: [List]

#### Option 2: [Treatment/Approach Name]

**Mechanism:** [How it works]
**Evidence:** [Summary of evidence]
**For this patient:**
- Pros: [List]
- Cons: [List]
- Monitoring required: [List]

#### Option 3: Watchful Waiting / Conservative Management

**When appropriate:** [Criteria]
**For this patient:**
- Pros: [List]
- Cons: [List]
- Triggers for intervention: [List]

---

## Output Format

```
CLINICAL DECISION SUPPORT SUMMARY
=================================

CLINICAL QUESTION
-----------------
[PICO-formatted question]

RECOMMENDATION
--------------
[Primary recommendation]

Strength: [Strong/Conditional/Weak]
Confidence: [High/Moderate/Low]
Basis: [Guidelines/Evidence/Expert consensus]

EVIDENCE SUMMARY
----------------

Guidelines:
- [Guideline 1]: [Recommendation and strength]
- [Guideline 2]: [Recommendation and strength]

Key Evidence:
- [Study/finding 1]
- [Study/finding 2]

Evidence Quality: [Overall assessment]
Evidence Gaps: [What's unknown]

PATIENT-SPECIFIC CONSIDERATIONS
-------------------------------

Supports recommendation:
+ [Factor 1]
+ [Factor 2]

Requires caution:
! [Factor 1]: [How to address]
! [Factor 2]: [How to address]

Contraindications checked:
[X] No absolute contraindications identified
[X] Relative contraindications: [List and assessment]

RISK-BENEFIT ANALYSIS
---------------------

Expected Benefits:
- [Benefit 1]: [Magnitude]
- [Benefit 2]: [Magnitude]

Potential Risks:
- [Risk 1]: [Frequency and severity]
- [Risk 2]: [Frequency and severity]

Net Assessment: [Summary]

ALTERNATIVES CONSIDERED
-----------------------

1. [Alternative 1]: [Why less preferred for this patient]
2. [Alternative 2]: [Why less preferred for this patient]
3. Watchful waiting: [Assessment of appropriateness]

IMPLEMENTATION
--------------

If proceeding:
- Dose/approach: [Specific recommendation]
- Monitoring: [What to monitor and when]
- Duration: [Expected treatment duration]
- Follow-up: [Timing and purpose]

SHARED DECISION-MAKING POINTS
-----------------------------

Key points to discuss with patient:
1. [Point 1 - benefit to emphasize]
2. [Point 2 - risk to discuss]
3. [Point 3 - patient values to explore]

Patient decision aid available: [Yes/No - link if available]

UNCERTAINTY ACKNOWLEDGMENT
--------------------------

What we know well:
- [High-confidence area]

What we're less certain about:
- [Area of uncertainty]: [Why uncertain]

What to do if uncertain:
- [Suggested approach - additional testing, specialist consult, trial of therapy]

SAFETY CHECKLIST
----------------
[X] Allergies reviewed
[X] Drug interactions checked
[X] Contraindications assessed
[X] Monitoring plan established
[X] Warning signs discussed
[X] Follow-up scheduled

---
Decision support generated: [Date]
For clinical use only - verify with current guidelines and patient context
```

---

## Evidence Grading Reference

### Recommendation Strength

**Strong Recommendation:**
- Benefits clearly outweigh risks (or vice versa)
- Most patients should receive this intervention
- Clinicians should offer it to most patients

**Conditional Recommendation:**
- Benefits and risks more closely balanced
- Many patients would want this, but many wouldn't
- Discussion of values and preferences important

**Weak Recommendation:**
- Limited evidence or high uncertainty
- Clinical judgment and patient preference paramount

### Evidence Quality (GRADE)

**High:** Further research unlikely to change confidence
- Multiple high-quality RCTs with consistent results

**Moderate:** Further research may change confidence
- RCTs with limitations or consistent observational studies

**Low:** Further research likely to change confidence
- Observational studies or RCTs with serious limitations

**Very Low:** Very uncertain about the estimate
- Case reports or expert opinion only

---

## Special Considerations

### When Guidelines Conflict

- Present both perspectives
- Identify why they differ (different evidence, populations, values)
- Recommend approach to reconcile
- Suggest specialist consultation if needed

### When Evidence is Limited

- State explicitly that evidence is limited
- Describe what evidence does exist
- Present expert consensus if available
- Recommend conservative approach with close monitoring

### When Patient Preferences Differ from Guidelines

- Respect patient autonomy
- Ensure patient has accurate information
- Document discussion
- Offer compromise approaches if safe
- Know when to draw lines (unsafe requests)

### Urgent/Emergent Decisions

- Prioritize time-sensitive recommendations
- Simplify to key decision points
- Flag need for immediate action clearly
- Reserve detailed analysis for stable situations

---

## Process Guidelines

### Acknowledge Uncertainty
- Never overstate confidence
- Distinguish strong from weak evidence
- Say "we don't know" when appropriate

### Support, Don't Replace
- Present information for clinician to interpret
- Don't dictate decisions
- Respect that clinician knows patient context

### Update Regularly
- Recommendations may need revision as evidence evolves
- Flag when guidelines are outdated
- Encourage verification of current standards

---

## False-Positive Prevention

❌ **DON'T:**
- Fabricate dosages, effect sizes (NNT/NNH), interaction details, decision-rule cutoffs, or citations to sound precise.
- Cite a specific study or guideline you cannot actually support — name the source TYPE instead.
- Present a single confident recommendation while omitting risks, alternatives, or contraindications.
- Overstate evidence quality or bury the uncertainty the clinician needs to weigh.
- Hedge so heavily ("it depends, discuss with specialist") that the clinician gets no usable structure.

✅ **DO:**
- State the evidence TYPE, recommendation strength, evidence quality, and a confidence level.
- Give qualitative ranges when exact figures aren't reliable, and name what would change the recommendation.
- Surface contraindications, interactions, monitoring needs, and conservative alternatives.
- Flag every actionable conclusion as requiring clinician verification and the full clinical picture.
- Stay genuinely useful: commit to a structured, defensible recommendation with explicit trade-offs.

---

## Dual-Failure Prevention (QA-20)

This prompt must avoid **both** failure modes:

- **Failure of commission (harmful):** recommending a treatment with false confidence, omitting a contraindication or interaction, or fabricating a dose/figure/citation a clinician might rely on.
- **Failure of omission (useless):** retreating into "consult a specialist / it depends" without producing a structured, evidence-graded recommendation with trade-offs.

The correct output is decisive *and* bounded: a graded recommendation with stated evidence quality, risk-benefit trade-offs, contraindications, alternatives, shared-decision points, and explicit uncertainty — clearly framed as support for, not a replacement of, clinician judgment.

---

## Example Output

```
CLINICAL DECISION SUPPORT SUMMARY (decision support — verify with current guidelines)
=================================
CLINICAL QUESTION
In a 72-year-old man with new non-valvular AFib (CHA2DS2-VASc 4) and CKD (eGFR 35),
should we start anticoagulation, and with which agent, vs no anticoagulation,
to reduce stroke risk while limiting bleeding?

RECOMMENDATION
Offer oral anticoagulation for stroke prevention; a DOAC is generally preferred over
warfarin in eligible patients, with dose adjusted for renal function.
Strength: Strong (anticoagulation) / Conditional (agent choice)
Confidence: Moderate-High
Basis: Professional-society AFib guideline + clinical decision rule (source TYPE).

EVIDENCE SUMMARY
- Guideline: anticoagulation recommended at this stroke-risk score (strong).
- Evidence quality: Moderate-High for stroke reduction; agent choice individualized.
- Gaps: limited trial data at very low eGFR.

PATIENT-SPECIFIC CONSIDERATIONS
+ High stroke risk (CHA2DS2-VASc 4) favors anticoagulation.
! CKD (eGFR 35): requires renal dose verification and agent selection — confirm in database.

RISK-BENEFIT
Benefit: meaningful stroke-risk reduction. Risk: bleeding (assess with a bleeding-risk tool).
Net: favors anticoagulation for most patients with this profile.

ALTERNATIVES: warfarin (if DOAC unsuitable); LAA closure if anticoagulation contraindicated.

SHARED DECISION-MAKING POINTS
1. Stroke-prevention benefit vs bleeding risk. 2. Adherence/monitoring. 3. Cost/preference.

UNCERTAINTY: agent and exact dose depend on renal function and bleeding risk —
verify dosing in a current drug reference and confirm no contraindications.

NOTE: Decision support only. Confirm with current guidelines, full clinical picture,
and patient preferences before acting.
```

---

## Verification

- [ ] Recommendation states strength, evidence quality (GRADE-style), and confidence.
- [ ] Source TYPE cited for guidelines/evidence; no fabricated figures, doses, or citations.
- [ ] Contraindications, interactions, and monitoring needs surfaced.
- [ ] Alternatives (including conservative management) and shared-decision points included.
- [ ] Uncertainty and evidence gaps stated, with what would change the recommendation.
- [ ] Output framed as decision support requiring clinician verification.
- [ ] Avoids both false confidence/omission and uselessly vague hedging (QA-20).

---

## Techniques Used

- **ST-01 (Clear Objective Statement):** Opens with a single-sentence objective scoping the tool to decision support.
- **RT-02 (Multi-Dimensional Reasoning):** Reasons across evidence, patient-specific factors, contraindications, risk-benefit, and alternatives.
- **DS-02 (Evidence-Based Standards):** Anchors recommendations to guidelines, decision rules, and GRADE-style evidence quality via stated source types.
- **QA-01 (Self-Verification):** Built-in safety checklist and uncertainty acknowledgment before finalizing.
- **QA-20 (Dual-Failure Prevention):** Explicitly guards against both harmful false confidence and unhelpful over-hedging.
- **CM-02 (Constraint / Safety Framing):** Hard constraints on no fabrication, graded evidence, and clinician-verification framing.

---

## Related Prompts

- `domain-healthcare-clinical/prompts/reasoning/medicine_differential_diagnosis_generator.md` — establishes the working diagnosis this decision acts on.
- `domain-healthcare-clinical/prompts/pharmacology/medicine_drug_interaction_checker.md` — checks the medication safety of the recommended plan.
- `domain-healthcare-clinical/prompts/education/medicine_literature_synthesizer.md` — supplies the appraised evidence behind the recommendation.

---

**Critical Reminder:** Clinical decision-making requires integration of evidence, patient values, clinical expertise, and circumstances. This tool provides structured information to support that process but cannot account for all factors only known to the treating clinician.
