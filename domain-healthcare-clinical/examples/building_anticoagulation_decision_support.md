# Worked Example: Building Anticoagulation Decision Support

> This example demonstrates the complete process of creating a clinical decision support prompt for anticoagulation in atrial fibrillation.

---

## The Request

**User says:** "I have a 72-year-old patient with new atrial fibrillation. She has a history of diabetes and hypertension. I'm trying to decide about anticoagulation. Can you help me think through this?"

---

## Step 1: Classification

**Task Type:** DECIDE
- User needs to make a clinical treatment choice
- Multiple options with trade-offs (anticoagulate vs. not, which agent)

**Domain:** Healthcare/Clinical
- Medical treatment decision
- Requires evidence-based reasoning
- High stakes (stroke vs. bleeding)

**Specific Area:** Anticoagulation decision-making in atrial fibrillation

---

## Step 2: Context Analysis

### What We Know
- Age: 72 years
- Sex: Female (stated "she")
- New diagnosis: Atrial fibrillation
- Comorbidities: Type 2 diabetes, hypertension

### What We're Missing (Affects Recommendation)

**Critical for Decision:**
- Renal function (CrCl) - affects DOAC dosing and selection
- Bleeding history - major predictor of future bleeding
- Fall risk - increases intracranial hemorrhage risk
- Prior stroke/TIA - dramatically increases stroke risk benefit

**Important for Implementation:**
- Current medications - drug interactions
- Weight - affects DOAC dosing
- Liver function - affects DOAC selection
- Patient preferences - values about bleeding vs. stroke

**Note:** A good clinical decision support prompt should acknowledge these gaps and provide guidance contingent on this information.

---

## Step 3: Template Selection

**Selected Template:** Clinical Decision Support Template

**Why this template:**
- This is a treatment decision requiring risk-benefit analysis
- Need to apply clinical scoring systems (CHA₂DS₂-VASc, HAS-BLED)
- Must reference guidelines with evidence levels
- Requires patient-specific factor analysis
- Should support shared decision-making

---

## Step 4: Customization for Anticoagulation

### Domain-Specific Additions

**Risk Scores to Include:**
- CHA₂DS₂-VASc (stroke risk)
- HAS-BLED (bleeding risk)
- Net clinical benefit calculation

**Guidelines to Reference:**
- 2023 AHA/ACC/HRS Atrial Fibrillation Guidelines
- 2020 ESC Atrial Fibrillation Guidelines
- NICE Atrial Fibrillation Guidelines

**Treatment Options:**
- DOACs (apixaban, rivaroxaban, dabigatran, edoxaban)
- Warfarin
- No anticoagulation (with justification)
- Left atrial appendage closure (if anticoagulation contraindicated)

**Safety Considerations:**
- Drug interactions (especially with diabetes and HTN meds)
- Renal dosing adjustments
- Monitoring requirements
- Reversal agent availability

---

## Step 5: The Complete Prompt

```markdown
# Anticoagulation Decision Support: Atrial Fibrillation

**Important Disclaimer:** This analysis supports clinical decision-making but does not replace physician judgment. All anticoagulation decisions require evaluation of the complete clinical picture and patient preferences by qualified healthcare professionals.

## Clinical Question (PICO)

**P - Patient:** 72-year-old female with newly diagnosed atrial fibrillation, type 2 diabetes mellitus, and hypertension

**I - Intervention:** Oral anticoagulation therapy

**C - Comparison:**
- Different oral anticoagulants (DOACs vs. warfarin)
- No anticoagulation / aspirin alone

**O - Outcome:** Stroke prevention balanced against major bleeding risk

## Patient Information

### Known Factors
| Factor | Value | CHA₂DS₂-VASc Impact |
|--------|-------|---------------------|
| Age | 72 | +1 point (65-74) or +2 if ≥75 |
| Sex | Female | +1 point |
| Diabetes | Yes | +1 point |
| Hypertension | Yes | +1 point |

### Information Needed (Note if Unavailable)

**Critical for Decision:**
- [ ] Renal function (Creatinine, eGFR, CrCl)
- [ ] Prior stroke, TIA, or thromboembolism
- [ ] Bleeding history (GI, intracranial, other major)
- [ ] Fall risk assessment

**Important for Agent Selection:**
- [ ] Current medications (for interaction check)
- [ ] Liver function (AST, ALT, bilirubin)
- [ ] Weight
- [ ] Coronary artery disease status

**For Shared Decision-Making:**
- [ ] Patient preferences (bleeding vs. stroke risk tolerance)
- [ ] Medication adherence history
- [ ] Cost/insurance considerations
- [ ] Lifestyle factors (diet variability for warfarin)

## Instructions

### 1. Calculate Stroke Risk (CHA₂DS₂-VASc)

**Score the Patient:**
| Risk Factor | Points | This Patient |
|-------------|--------|--------------|
| Congestive heart failure | 1 | Unknown |
| Hypertension | 1 | YES (+1) |
| Age ≥75 | 2 | NO (age 72) |
| Age 65-74 | 1 | YES (+1) |
| Diabetes | 1 | YES (+1) |
| Stroke/TIA/thromboembolism | 2 | Unknown - VERIFY |
| Vascular disease | 1 | Unknown |
| Sex (female) | 1 | YES (+1) |

**Minimum Score with Known Data:** 4 points
- Hypertension (+1)
- Age 65-74 (+1)
- Diabetes (+1)
- Female (+1)

**Annual Stroke Risk Estimate:**
- Score 4 = approximately 4.0% annual stroke risk
- Score could be higher if CHF, vascular disease, or prior stroke

**Guideline Threshold:**
- Score ≥2 in men, ≥3 in women → Anticoagulation recommended
- This patient (score ≥4) → Strong indication for anticoagulation

### 2. Calculate Bleeding Risk (HAS-BLED)

| Risk Factor | Points | This Patient |
|-------------|--------|--------------|
| Hypertension (uncontrolled, SBP >160) | 1 | Need BP data |
| Abnormal renal/liver function | 1-2 | Need labs |
| Stroke history | 1 | Unknown |
| Bleeding history/predisposition | 1 | Unknown |
| Labile INR | 1 | N/A if DOAC |
| Elderly (>65) | 1 | YES (+1) |
| Drugs/alcohol | 1-2 | Unknown |

**Minimum Score:** 1 (age >65)
**Interpretation:**
- Score ≥3 = "High" bleeding risk - warrants caution but NOT contraindication
- High HAS-BLED should trigger search for modifiable risk factors, not avoidance of anticoagulation

### 3. Apply Guidelines

**2023 AHA/ACC/HRS AF Guidelines:**
- CHA₂DS₂-VASc ≥2 (men) or ≥3 (women): Oral anticoagulation recommended (Class I)
- DOACs preferred over warfarin for eligible patients (Class I)
- Aspirin alone NOT recommended for stroke prevention in AF

**This Patient:**
- CHA₂DS₂-VASc ≥4 → Strong recommendation for anticoagulation
- No apparent DOAC contraindication → DOAC preferred

### 4. Patient-Specific Analysis

**Factors Supporting Anticoagulation:**
- CHA₂DS₂-VASc ≥4 (high stroke risk)
- Multiple modifiable stroke risk factors (DM, HTN)
- New diagnosis (opportunity to prevent first stroke)

**Factors Requiring Consideration:**
- Age 72 (bleeding risk increases with age, but so does stroke risk)
- Unknown renal function (affects DOAC selection and dosing)
- Unknown bleeding history
- Unknown fall risk

**DOAC Selection Considerations:**
| If... | Consider... | Because... |
|-------|-------------|------------|
| CrCl >50 | Any DOAC | All are effective |
| CrCl 30-50 | Apixaban or rivaroxaban | Better studied in moderate CKD |
| CrCl 15-30 | Apixaban | Only DOAC with data here |
| CrCl <15 | Warfarin (or apixaban with caution) | Limited DOAC data |
| High GI bleed risk | Apixaban | Lower GI bleeding than other DOACs |
| CAD/recent ACS | Rivaroxaban 2.5mg BID + aspirin | COMPASS trial |
| Cost concerns | Generic warfarin | Significantly less expensive |

### 5. Compare Treatment Options

**Option A: DOAC (Preferred for Most Patients)**

*Apixaban 5mg BID (or 2.5mg BID if criteria met)*
- Pros: Reduced ICH vs. warfarin, no INR monitoring, more predictable effect
- Cons: Cost, no single reliable reversal agent (andexanet alfa expensive)
- Dosing criteria for 2.5mg: ≥2 of (age ≥80, weight ≤60kg, Cr ≥1.5)

*Rivaroxaban 20mg daily (or 15mg if CrCl 15-50)*
- Pros: Once daily dosing, established reversal
- Cons: Higher GI bleeding, must take with food

**Option B: Warfarin**

- Pros: Long track record, inexpensive, vitamin K reversal, mechanical valve approved
- Cons: INR monitoring, dietary interactions, drug interactions, variable effect
- Better for: Mechanical valves, severe CKD, cost-limited patients

**Option C: No Anticoagulation**

- Consider only if: True contraindication (active major bleeding, recent ICH)
- Not appropriate for this patient based on available information

### 6. Recommendation

**Primary Recommendation:**
Initiate oral anticoagulation with a DOAC (apixaban preferred)

**Strength:** Strong recommendation
**Confidence:** High (guideline-concordant, strong evidence base)
**Evidence Basis:** Class I recommendation, multiple RCTs (ARISTOTLE, RE-LY, ROCKET-AF, ENGAGE AF-TIMI 48)

**Before Initiating, Obtain:**
- Renal function (CrCl for dosing)
- Liver function
- CBC (baseline)
- Complete medication list (interaction check)
- Bleeding history
- Patient preference discussion

**What Would Change This Recommendation:**
- Recent major bleeding → delay, address source
- CrCl <15 → warfarin preferred
- Active malignancy → individualize based on prognosis and bleeding risk
- Patient strongly prefers no anticoagulation → document shared decision-making

### 7. Shared Decision-Making Points

**Discussing Stroke Risk:**
"Without a blood thinner, your chance of having a stroke in the next year is about 1 in 25. That's higher than average because of your age, diabetes, and blood pressure. A blood thinner can reduce that risk by about two-thirds."

**Discussing Bleeding Risk:**
"Blood thinners do increase bleeding risk. The main concern is major bleeding, especially in the brain or stomach. For you, the risk of a stroke without treatment is higher than the risk of serious bleeding with treatment."

**Exploring Values:**
"Some people are more worried about stroke, which can cause permanent disability. Others are more concerned about bleeding. How do you think about these risks?"

**Practical Considerations:**
"The newer blood thinners (like apixaban) don't require regular blood tests, but they're more expensive. Warfarin is cheaper but needs regular monitoring. What matters most to you?"

### 8. Safety and Monitoring

**Before Starting:**
- [ ] Renal function checked
- [ ] Baseline CBC obtained
- [ ] Medication interactions reviewed
- [ ] Bleeding history documented
- [ ] Patient education provided

**Ongoing Monitoring:**
- Renal function: Annually (more often if CKD)
- Signs of bleeding: Each visit
- Adherence: Each visit
- Need for temporary interruption: Before procedures

**When to Stop and Reassess:**
- Major bleeding event
- New renal impairment (CrCl <30)
- Planned surgery/procedure
- Patient request

**Red Flags - Seek Immediate Evaluation:**
- Signs of stroke (face droop, arm weakness, speech difficulty)
- Major bleeding (black/bloody stool, vomiting blood, heavy bruising)
- Head injury while on anticoagulation

## Uncertainty Acknowledgment

**What We Know With Confidence:**
- This patient has a strong indication for anticoagulation (CHA₂DS₂-VASc ≥4)
- DOACs are preferred over warfarin for most AF patients
- Net clinical benefit favors anticoagulation at this stroke risk level

**What We're Less Certain About:**
- Optimal DOAC selection (depends on renal function, not available)
- Precise bleeding risk (need complete HAS-BLED)
- Patient-specific factors that might change recommendation

**What to Do With Uncertainty:**
- Obtain renal function before selecting specific agent
- Complete HAS-BLED to identify modifiable bleeding risk factors
- Discuss with patient to incorporate preferences
```

---

## Step 6: Quality Verification

### Checklist Review

**Evidence Quality:**
- [x] Cites specific guidelines (AHA/ACC/HRS 2023)
- [x] Notes evidence level (Class I recommendations)
- [x] Acknowledges limitations (missing renal function)

**Confidence Calibration:**
- [x] States confidence level (High)
- [x] Distinguishes certain from uncertain elements
- [x] Notes what would change recommendation

**Patient Factors:**
- [x] Calculates risk scores with available data
- [x] Notes missing information needed
- [x] Provides conditional recommendations

**Safety Checks:**
- [x] Lists pre-treatment requirements
- [x] Includes monitoring plan
- [x] Defines red flags and actions

**Communication:**
- [x] Includes shared decision-making talking points
- [x] Patient-friendly explanations of risk
- [x] Documents that this supports but doesn't replace judgment

---

## Key Takeaways from This Example

1. **Structure Clinical Questions:** PICO format focuses the analysis
2. **Quantify Risk:** Use validated scoring systems with numbers
3. **Acknowledge Gaps:** Note missing information and its impact
4. **Reference Guidelines:** Cite specific, current recommendations
5. **Consider Alternatives:** Don't just recommend - compare options
6. **Support Communication:** Provide talking points for patient discussion
7. **Plan for Safety:** Include monitoring and contingency plans
8. **Calibrate Confidence:** Be explicit about certainty levels

---

*This worked example demonstrates applying the Healthcare/Clinical domain principles to a common clinical scenario.*
