# Clinical Decision Support Template

> Copy this template when creating clinical decision support requests.
> Customize placeholders marked with [BRACKETS].

---

```markdown
# Clinical Decision Support Request

**Important:** This output supports clinical reasoning but does not replace physician judgment. All decisions must be made by qualified healthcare professionals.

## Clinical Question

**PICO Format:**
- **P**atient: [Age, sex, relevant demographics, presenting condition]
- **I**ntervention: [Treatment/test/procedure being considered]
- **C**omparison: [Alternative options including watchful waiting]
- **O**utcome: [Desired clinical outcomes - what does success look like?]

## Patient Context

**Demographics:**
- Age: [Years]
- Sex: [Male/Female]
- Weight: [If relevant for dosing]

**Primary Condition:**
[Diagnosis or chief complaint with duration]

**Comorbidities:**
- [Condition 1 - severity/status]
- [Condition 2 - severity/status]
- [Add more as needed]

**Current Medications:**
- [Medication 1] - [dose] - [indication]
- [Medication 2] - [dose] - [indication]

**Allergies:**
- [Drug] - [Reaction type: anaphylaxis/rash/GI upset/etc.]

**Relevant Labs/Imaging:**
| Test | Result | Date | Reference Range |
|------|--------|------|-----------------|
| [Test 1] | [Value] | [Date] | [Normal range] |

**Patient Preferences (if known):**
- Treatment goals: [What patient wants to achieve]
- Concerns: [What patient wants to avoid]
- Values: [Quality of life vs. longevity, etc.]

**Social Factors:**
- Insurance/financial: [Relevant constraints]
- Support system: [Who helps with care]
- Adherence history: [Any concerns]

## Analysis Instructions

Provide decision support by:

1. **Evidence Review**
   - Identify relevant guidelines (cite organization, year)
   - Summarize key studies with evidence quality
   - Note if evidence is limited or guidelines conflict

2. **Patient-Specific Application**
   - How does evidence apply to THIS patient?
   - Factors favoring intervention
   - Factors requiring caution
   - Contraindications check (absolute and relative)

3. **Risk-Benefit Analysis**
   For each option:
   | Benefit | Magnitude | Evidence Quality |
   |---------|-----------|------------------|
   | [Outcome] | [NNT or %] | [High/Mod/Low] |

   | Risk | Frequency | Severity | Reversible? |
   |------|-----------|----------|-------------|
   | [Adverse effect] | [%] | [Mild/Mod/Severe] | [Yes/No] |

4. **Compare Alternatives**
   - Option A: [Pros, cons, best-fit scenario]
   - Option B: [Pros, cons, best-fit scenario]
   - Option C: Watchful waiting - [When appropriate]

5. **Recommendation**
   - Recommendation: [Specific guidance]
   - Confidence: [High/Moderate/Low]
   - Basis: [Guidelines/Evidence/Expert consensus]
   - What would change this recommendation: [Key factors]

6. **Implementation**
   - Dosing/approach: [Specifics]
   - Monitoring: [What to check, when]
   - Duration: [Expected treatment length]
   - Follow-up: [Timing and purpose]

7. **Shared Decision-Making Points**
   - Key benefits to discuss with patient
   - Key risks to discuss with patient
   - Patient values to explore
   - Questions patient might ask

8. **Safety Checklist**
   - [ ] Allergies reviewed
   - [ ] Drug interactions checked
   - [ ] Contraindications assessed
   - [ ] Monitoring plan established
   - [ ] Warning signs discussed
   - [ ] Follow-up scheduled

## Uncertainty Acknowledgment

**What we know with confidence:**
- [High-confidence areas with evidence]

**What we're less certain about:**
- [Area]: [Why uncertain - limited data, conflicting evidence, extrapolation]

**What we don't know:**
- [Important unknowns that could affect decision]

**If uncertain, consider:**
- [Additional testing, specialist consult, trial of therapy, close monitoring]
```

---

## Example Application

**Scenario:** Antibiotic selection for community-acquired pneumonia

```markdown
# Clinical Decision Support: CAP Antibiotic Selection

**PICO:**
- Patient: 67-year-old male with community-acquired pneumonia, COPD
- Intervention: Antibiotic therapy
- Comparison: Different antibiotic regimens
- Outcome: Clinical cure, minimizing resistance and adverse effects

**Demographics:** 67M, 80kg

**Primary Condition:** CAP - moderate severity (CURB-65 = 2)

**Comorbidities:**
- COPD - moderate, on tiotropium
- Type 2 DM - controlled, A1c 7.2%

**Current Medications:**
- Tiotropium 18mcg daily
- Metformin 1000mg BID

**Allergies:**
- Penicillin - rash (childhood, details unclear)

**Labs:**
| Test | Result | Reference |
|------|--------|-----------|
| WBC | 14.2 | 4-11 K/uL |
| Cr | 1.1 | 0.7-1.3 mg/dL |
| Procalcitonin | 0.8 | <0.1 ng/mL |

**Preferences:** Wants to avoid hospitalization if safe
```

---

## Quality Checklist

Before using this template, verify:

- [ ] All relevant patient context is included
- [ ] Clinical question is specific (PICO format)
- [ ] Request asks for evidence with quality grading
- [ ] Patient-specific factors are addressed
- [ ] Alternatives are compared
- [ ] Uncertainty is explicitly requested
- [ ] Safety checks are included
- [ ] Output supports but doesn't replace clinical judgment
