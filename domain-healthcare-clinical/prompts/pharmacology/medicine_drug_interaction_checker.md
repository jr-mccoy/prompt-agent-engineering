---
title: "Drug Interaction and Contraindication Checker"
category: healthcare-clinical/pharmacology
description: "Systematically review a medication list against patient conditions and organ function for drug-drug interactions, drug-disease contraindications, dosing appropriateness, and monitoring needs — prioritized by clinical significance — without fabricating interactions, severities, or doses, and always routed to pharmacist/database verification."
techniques:
  - ST-01
  - RT-02
  - DS-02
  - QA-01
  - QA-20
  - CM-02
difficulty: advanced
tags:
  - medication-safety
  - drug-interactions
  - contraindications
  - dose-adjustment
  - pharmacovigilance
updated: "2026-06-07"
related_prompts:
  - domain-healthcare-clinical/prompts/reasoning/medicine_clinical_decision_support.md
  - domain-healthcare-clinical/prompts/communication/medicine_patient_education_adapter.md
  - domain-healthcare-clinical/prompts/quality/medicine_adverse_event_analyzer.md
---

# Drug Interaction and Contraindication Checker

**Objective:** Systematically evaluate a medication list against patient conditions for interactions, contraindications, dosing considerations, and monitoring requirements, prioritizing findings by clinical significance.

**Important Disclaimer:** This tool provides educational support for medication review. It does not replace pharmacist consultation, official drug interaction databases, or clinical judgment. All medication decisions must be verified against current drug references and individualized to patient context.

**When to use:**
- Reviewing a medication regimen for drug-drug interactions and drug-disease contraindications.
- Checking dosing appropriateness for renal/hepatic function, age, and special populations.
- Building a monitoring plan for high-risk medications.
- Pre-screening a new medication before adding it, or reconciling at transitions of care.

**When NOT to use:**
- As a replacement for an official interaction database (Lexicomp, Micromedex, Clinical Pharmacology) or pharmacist review.
- For autonomous prescribing or dose changes without clinician/pharmacist verification.
- For emergent toxicity — manage clinically and consult poison control/pharmacy first.

**Audience:** Licensed clinicians, prescribers, clinical pharmacists, residents, and pharmacy/medicine learners under supervision.

---

## Inputs / Context

Provide the patient and medication data below. Paste the full medication list and relevant labs wrapped in a `<med_list>` tag so it can be referenced by name; review only what is supplied, note that OTC/herbal products and the data cutoff may limit findings, and flag every finding for verification against a current drug database.

---

## Input Required

### Patient Information

**Demographics:**
- Age: [Years]
- Sex: [Male/Female]
- Weight: [kg]
- Height: [cm] (for BSA calculations if needed)

**Relevant Conditions:**
- [Condition 1]
- [Condition 2]
- [Condition 3]

**Organ Function:**
- Renal: CrCl/eGFR [value] mL/min or [Normal/Mild/Moderate/Severe impairment/ESRD]
- Hepatic: [Normal/Child-Pugh A/B/C]
- Cardiac: [EF if relevant]

**Allergies:**
- [Drug]: [Reaction type]

**Current Medications:**
```
1. [Drug name] [Dose] [Route] [Frequency]
2. [Drug name] [Dose] [Route] [Frequency]
3. [Drug name] [Dose] [Route] [Frequency]
[Continue for all medications...]
```

**Indication for Review:**
- [ ] New medication being added: [Drug name]
- [ ] Comprehensive medication review
- [ ] Adverse event investigation
- [ ] Discharge reconciliation
- [ ] Transition of care

---

## Constraints

### Must
- Ground every interaction, contraindication, and dosing statement in established pharmacology; cite the source TYPE (drug database, package insert, guideline, Beers criteria, primary literature) rather than inventing a citation.
- Assign a **severity** (contraindicated / major / moderate / minor) and a **documentation level** (established / probable / suspected) to each interaction, and prioritize by clinical significance.
- **Never fabricate** interactions, severities, mechanisms, dose thresholds, or monitoring parameters; if uncertain, say so and route to the database/pharmacist.
- Flag the OTC/herbal/supplement blind spot and the knowledge-cutoff limitation explicitly.
- Make every actionable finding require **pharmacist or current-database verification** before acting.

### Must Not
- Do not present output as a definitive medication decision or replace pharmacist/database review.
- Do not invent a drug interaction, contraindication, dose adjustment, or monitoring threshold to appear complete.
- Do not under-flag (miss a major interaction) or over-flag trivial interactions into noise.
- Do not give patient-specific dose numbers as final orders — frame as ranges/considerations to verify.

---

## Systematic Review Framework

### Step 1: Medication Reconciliation

**Verify Each Medication:**

| Drug | Dose | Route | Freq | Indication | Appropriate? |
|------|------|-------|------|------------|--------------|
| [Name] | [Dose] | [PO/IV] | [Daily] | [Reason] | [Yes/No/Clarify] |

**Identify:**
- [ ] Medications without clear indication
- [ ] Duplicate therapies
- [ ] Missing therapies for documented conditions
- [ ] Inappropriate formulations

### Step 2: Drug-Drug Interaction Analysis

**Interaction Categories:**

| Severity | Definition | Action Required |
|----------|------------|-----------------|
| **Contraindicated** | Avoid combination | Do not use together |
| **Major** | May be life-threatening | Avoid or use alternative |
| **Moderate** | May worsen condition | Monitor closely or modify |
| **Minor** | Limited clinical effect | Be aware |

**Interaction Assessment:**

```
DRUG-DRUG INTERACTIONS

[Drug A] + [Drug B]
═══════════════════════════════════════════════════════════════
Severity: [Contraindicated/Major/Moderate/Minor]
Mechanism: [How the interaction occurs]
Clinical Effect: [What happens to the patient]
Onset: [Immediate/Delayed]
Documentation: [Established/Probable/Suspected/Possible]

Evidence:
- [Supporting evidence/literature]

Management:
- [Recommended action]
- [Alternative if available]
- [Monitoring if continued]

───────────────────────────────────────────────────────────────

[Repeat for each identified interaction]
```

**Common High-Risk Interaction Categories:**

| Category | Examples | Risk |
|----------|----------|------|
| QT Prolongation | Antipsychotics + Fluoroquinolones | Torsades de pointes |
| Serotonin Syndrome | SSRIs + MAOIs + Tramadol | Hyperthermia, seizures |
| Bleeding | Anticoagulants + NSAIDs + Antiplatelets | Hemorrhage |
| Hypoglycemia | Sulfonylureas + Fluoroquinolones | Severe hypoglycemia |
| Hyperkalemia | ACEi + K-sparing diuretics + K supplements | Cardiac arrhythmia |
| CNS Depression | Opioids + Benzodiazepines + Gabapentinoids | Respiratory depression |
| Nephrotoxicity | NSAIDs + ACEi + Diuretics ("Triple Whammy") | AKI |

### Step 3: Drug-Disease Contraindication Analysis

**Contraindication Assessment:**

```
DRUG-DISEASE CONTRAINDICATIONS

[Drug] in patient with [Condition]
═══════════════════════════════════════════════════════════════
Contraindication Type: [Absolute/Relative]
Risk: [What could happen]
Mechanism: [Why this is problematic]

Recommendation:
- [Action required]
- [Alternative therapy if available]
- [Monitoring if use necessary]

───────────────────────────────────────────────────────────────
```

**Common Drug-Disease Contraindications:**

| Drug Class | Condition | Risk |
|------------|-----------|------|
| NSAIDs | CKD, CHF, GI bleed history | AKI, fluid retention, bleeding |
| Beta-blockers | Severe asthma/COPD, severe bradycardia | Bronchospasm, heart block |
| Metformin | eGFR <30, acute illness, contrast | Lactic acidosis |
| ACE inhibitors | Bilateral renal artery stenosis, angioedema history | AKI, angioedema |
| Anticholinergics | BPH, narrow-angle glaucoma, dementia | Retention, acute glaucoma, cognitive decline |
| Sulfonylureas | Severe hepatic impairment | Hypoglycemia |
| Fluoroquinolones | Myasthenia gravis, QT prolongation | Exacerbation, arrhythmia |

### Step 4: Dosing Assessment

**Renal Dosing Review:**

```
RENAL DOSE ADJUSTMENTS

Current eGFR/CrCl: [Value] mL/min

[Drug Name]
- Current dose: [Dose]
- Recommended for renal function: [Appropriate dose]
- Assessment: [Appropriate / Needs adjustment / Contraindicated]
- Action: [None / Reduce dose / Extend interval / Discontinue]

[Repeat for renally-cleared medications]
```

**Hepatic Dosing Review:**

```
HEPATIC DOSE ADJUSTMENTS

Current hepatic function: [Normal / Child-Pugh A/B/C]

[Drug Name]
- Current dose: [Dose]
- Hepatic metabolism: [High/Moderate/Low]
- Assessment: [Appropriate / Needs adjustment / Contraindicated]
- Action: [None / Reduce dose / Avoid]

[Repeat for hepatically-metabolized medications]
```

**Age-Related Considerations:**

```
GERIATRIC CONSIDERATIONS (if age ≥65)

Beers Criteria Medications Present:
- [Drug]: [Risk] → [Recommendation]
- [Drug]: [Risk] → [Recommendation]

Anticholinergic Burden:
- Total ACB score: [X]
- High-burden medications: [List]
- Recommendation: [Action]

Fall Risk Medications:
- [Drug]: [Mechanism of fall risk]
- Recommendation: [Action]
```

### Step 5: Monitoring Requirements

**Required Monitoring:**

```
MONITORING PLAN

[Drug Name]
═══════════════════════════════════════════════════════════════
Efficacy Monitoring:
- Parameter: [What to monitor]
- Target: [Goal value/outcome]
- Frequency: [How often]

Safety Monitoring:
- Parameter: [What to monitor]
- Threshold for action: [When to intervene]
- Frequency: [How often]

Labs Required:
| Test | Baseline | Ongoing Frequency |
|------|----------|-------------------|
| [Test] | [Yes/No] | [Frequency] |

───────────────────────────────────────────────────────────────
```

**Common Monitoring Requirements:**

| Drug Class | Key Monitoring |
|------------|----------------|
| Anticoagulants | INR, anti-Xa, CBC, signs of bleeding |
| ACE/ARB | K+, Cr, BP |
| Diuretics | K+, Na+, Cr, BP |
| Digoxin | Level, K+, Cr, heart rate |
| Methotrexate | CBC, LFTs, Cr |
| Lithium | Level, TSH, Cr |
| Aminoglycosides | Trough/peak levels, Cr, audiometry |
| Vancomycin | Trough levels, Cr |
| Clozapine | ANC weekly, metabolic panel |

---

## Output Format

### Medication Review Summary

```
═══════════════════════════════════════════════════════════════
MEDICATION SAFETY REVIEW
═══════════════════════════════════════════════════════════════

Patient: [Identifier]
Review Date: [Date]
Medications Reviewed: [Number]

───────────────────────────────────────────────────────────────
SUMMARY OF FINDINGS
───────────────────────────────────────────────────────────────

Total Issues Identified: [Number]
- Contraindicated combinations: [Number]
- Major interactions: [Number]
- Dosing concerns: [Number]
- Monitoring gaps: [Number]

OVERALL RISK LEVEL: [HIGH / MODERATE / LOW]

───────────────────────────────────────────────────────────────
CRITICAL ALERTS (Immediate Action Required)
───────────────────────────────────────────────────────────────

🚨 [Issue 1]
   Drugs involved: [List]
   Risk: [Description]
   Action: [Required action]

🚨 [Issue 2]
   Drugs involved: [List]
   Risk: [Description]
   Action: [Required action]

───────────────────────────────────────────────────────────────
SIGNIFICANT CONCERNS (Action Recommended)
───────────────────────────────────────────────────────────────

⚠️ [Issue 1]
   Details: [Description]
   Recommendation: [Action]

⚠️ [Issue 2]
   Details: [Description]
   Recommendation: [Action]

───────────────────────────────────────────────────────────────
MONITORING RECOMMENDATIONS
───────────────────────────────────────────────────────────────

| Drug | Parameter | Frequency | Next Due |
|------|-----------|-----------|----------|
| [Drug] | [Test] | [Freq] | [Date] |

───────────────────────────────────────────────────────────────
OPTIMIZATION OPPORTUNITIES
───────────────────────────────────────────────────────────────

💡 [Recommendation 1]
   Current: [What's happening now]
   Suggested: [Improvement]
   Rationale: [Why]

💡 [Recommendation 2]
   Current: [What's happening now]
   Suggested: [Improvement]
   Rationale: [Why]

───────────────────────────────────────────────────────────────
MEDICATIONS REVIEWED - NO CONCERNS
───────────────────────────────────────────────────────────────

✓ [Drug 1] - Appropriate dose, no interactions
✓ [Drug 2] - Appropriate dose, no interactions

───────────────────────────────────────────────────────────────
LIMITATIONS
───────────────────────────────────────────────────────────────

- This review should be verified against current drug databases
- Patient-specific factors may not be fully captured
- Consult pharmacy for complex medication questions
- OTC medications and supplements may not be included

───────────────────────────────────────────────────────────────
Reviewed by: [Assistant designation]
Verify with: [Clinical pharmacist / Official drug database]
═══════════════════════════════════════════════════════════════
```

---

## Special Populations

### Pregnancy

**Category Assessment:**
- FDA pregnancy categories (historical)
- Current pregnancy/lactation labeling
- Teratogenicity risk
- Trimester-specific concerns

### Pediatrics

- Weight-based dosing verification
- Age-appropriate formulations
- Off-label use documentation
- Growth and development considerations

### Dialysis

- Dialyzability
- Supplemental dosing post-dialysis
- Timing around dialysis sessions

### Transplant

- Immunosuppressant interactions (especially CYP3A4)
- Nephrotoxicity risk with calcineurin inhibitors
- Infection risk with added immunosuppression

---

## Pharmacokinetic Considerations

### CYP450 Interactions

| Enzyme | Major Inhibitors | Major Inducers |
|--------|-----------------|----------------|
| CYP3A4 | Ketoconazole, Ritonavir, Clarithromycin, Grapefruit | Rifampin, Carbamazepine, Phenytoin, St. John's Wort |
| CYP2D6 | Paroxetine, Fluoxetine, Bupropion, Quinidine | (Few clinically significant inducers) |
| CYP2C9 | Fluconazole, Amiodarone | Rifampin |
| CYP2C19 | Omeprazole, Fluoxetine | Rifampin |
| CYP1A2 | Fluvoxamine, Ciprofloxacin | Smoking, Charbroiled meat |

### P-glycoprotein Interactions

- Inhibitors: Verapamil, Amiodarone, Cyclosporine, Ritonavir
- Inducers: Rifampin, St. John's Wort
- Substrates: Digoxin, Dabigatran, DOACs

---

## Quality Verification

### Self-Audit Checklist

Before finalizing review:

- [ ] All medications reviewed against allergy list
- [ ] Drug-drug interactions systematically checked
- [ ] Drug-disease contraindications assessed
- [ ] Renal dosing evaluated for appropriate medications
- [ ] Hepatic dosing evaluated for appropriate medications
- [ ] Geriatric considerations applied if applicable
- [ ] Monitoring requirements identified
- [ ] Prioritization reflects clinical significance
- [ ] Recommendations are actionable

### Limitations to Acknowledge

- Cannot account for all patient-specific factors
- OTC and herbal products may not be captured
- Database knowledge has cutoff date
- Rare interactions may not be identified
- Clinical judgment required for all recommendations

---

## False-Positive Prevention

❌ **DON'T:**
- Invent an interaction, contraindication, severity grade, mechanism, or dose threshold to look thorough.
- State a precise renal/hepatic dose as a final order when the database value should be verified.
- Cite a specific study or monograph you cannot support — name the source TYPE instead.
- Drown the review in trivial minor interactions, obscuring the major/contraindicated ones.
- Hedge into "check with pharmacy" for everything without doing the structured analysis first.

✅ **DO:**
- Assign severity + documentation level and rank by clinical significance.
- Name the source TYPE (database, package insert, Beers, guideline) behind each finding.
- Give dose adjustments as considerations/ranges flagged for database confirmation.
- Explicitly note the OTC/herbal and knowledge-cutoff blind spots.
- Stay genuinely useful: deliver a prioritized, actionable findings list the team can verify and act on.

---

## Dual-Failure Prevention (QA-20)

This prompt must avoid **both** failure modes:

- **Failure of commission (harmful):** asserting a fabricated interaction, wrong severity, invented dose threshold, or false reassurance ("no interactions") — any of which can cause direct medication harm.
- **Failure of omission (useless):** burying findings in trivial noise, or retreating to "verify everything with pharmacy" without performing the structured review.

The correct output is rigorous *and* bounded: a severity-ranked, source-typed findings list with dosing and monitoring considerations and explicit blind spots — framed as input requiring pharmacist/current-database verification, never as a final medication order.

---

## Example Output

```
═══════════════════════════════════════════════════════════════
MEDICATION SAFETY REVIEW (decision support — verify with pharmacy/database)
═══════════════════════════════════════════════════════════════
Patient: 74F, eGFR 28, on warfarin, amiodarone, NSAID (newly added)
Medications Reviewed: 6

OVERALL RISK LEVEL: HIGH

🚨 CRITICAL ALERTS (Immediate Action Required)
- Warfarin + Amiodarone
   Severity: Major | Documentation: Established
   Mechanism: CYP2C9 inhibition → increased INR / bleeding risk
   Source TYPE: drug database + package insert
   Action: Anticipate warfarin dose reduction; check INR sooner. VERIFY in database.

- NSAID + Warfarin (+ reduced renal function)
   Severity: Major | Documentation: Established
   Mechanism: Additive bleeding risk + nephrotoxicity ("triple whammy" risk)
   Action: Reconsider NSAID; if essential, gastroprotection + close monitoring.

⚠️ SIGNIFICANT CONCERNS
- NSAID in eGFR 28: relative contraindication (AKI risk). Consider alternative analgesia.

DOSING (CONSIDERATIONS — confirm in database)
- Several renally-cleared agents: review for eGFR 28 adjustment.

MONITORING
| Drug | Parameter | Frequency |
| Warfarin | INR | Sooner after amiodarone/NSAID change |
| Renal panel | Cr/eGFR, K+ | With NSAID exposure |

BLIND SPOTS
- OTC/herbal use not provided. Knowledge cutoff applies. Rare interactions may be missed.

Verify with: clinical pharmacist + current drug database before any change.
═══════════════════════════════════════════════════════════════
```

---

## Verification

- [ ] Every finding has a severity and documentation level and is ranked by significance.
- [ ] Source TYPE stated for each interaction/contraindication; no fabricated citations.
- [ ] Renal/hepatic/geriatric dosing addressed as considerations to verify, not final orders.
- [ ] No fabricated interactions, severities, mechanisms, or dose thresholds.
- [ ] OTC/herbal and knowledge-cutoff blind spots flagged.
- [ ] Major/contraindicated items not buried under trivial minor interactions.
- [ ] Output framed as decision support requiring pharmacist/database verification.
- [ ] Avoids both fabrication/under-flagging and uselessly vague "ask pharmacy" output (QA-20).

---

## Techniques Used

- **ST-01 (Clear Objective Statement):** Opens with a single-sentence objective scoping the tool to structured, verifiable medication review.
- **RT-02 (Multi-Dimensional Reasoning):** Reasons across drug-drug, drug-disease, dosing, special-population, and monitoring dimensions.
- **DS-02 (Evidence-Based Standards):** Anchors findings to drug databases, package inserts, Beers criteria, and guidelines via stated source types.
- **QA-01 (Self-Verification):** Self-audit checklist and limitations review before finalizing.
- **QA-20 (Dual-Failure Prevention):** Guards against both harmful fabrication/under-flagging and uselessly vague output.
- **CM-02 (Constraint / Safety Framing):** Hard constraints on no fabrication, severity grading, blind-spot disclosure, and pharmacist/database verification.

---

## Related Prompts

- `domain-healthcare-clinical/prompts/reasoning/medicine_clinical_decision_support.md` — weighs the medication options this review flags into a treatment decision.
- `domain-healthcare-clinical/prompts/communication/medicine_patient_education_adapter.md` — translates medication safety findings into plain-language patient instructions.
- `domain-healthcare-clinical/prompts/quality/medicine_adverse_event_analyzer.md` — investigates medication-related adverse events at the system level.

---

**Critical Reminder:** Medication safety review is a critical patient safety activity. This tool supports but does not replace comprehensive pharmacy review, official drug interaction databases (Lexicomp, Micromedex, Clinical Pharmacology), or clinical pharmacist consultation. All significant findings should be verified and discussed with the healthcare team.
