---
title: "Clinical Handoff Communication Template"
category: healthcare-clinical/templates
description: "Fill-in template for standardized clinical handoff communications based on the SBAR framework, with critical safety information, medications, lines and devices, contingency plans, and read-back verification."
techniques:
  - DS-01
  - ST-03
  - ST-04
  - OC-03
  - QA-01
difficulty: intermediate
tags:
  - handoff
  - sbar
  - patient-safety
  - clinical-documentation
  - care-team-communication
updated: "2026-10-06"
---

# Clinical Handoff Communication Template

> **Medical disclaimer — read before use.** This prompt is a decision-support and
> teaching aid for **licensed clinicians**. It is **not medical advice** and is not for
> patients to diagnose or treat themselves. Drug doses, thresholds and guideline
> references in it and in its worked example may be incomplete, outdated or wrong:
> verify each one against the current guideline, the product label and your local
> formulary, and follow your institution's protocols. It does not replace examination
> or clinical judgment. **Medical emergency: call your local emergency number (911 in
> the US).**
>
> **Review status:** AI-assisted content, reviewed by AI only (2026-10-06);
> **not yet reviewed by a licensed clinician.**

> Copy this template for creating standardized clinical handoff communications.
> Based on SBAR framework with healthcare-specific extensions.

---

```markdown
# Clinical Handoff: [Patient Identifier]

**Handoff Type:**
- [ ] Shift change (same unit)
- [ ] Unit transfer (different care area)
- [ ] Discharge to outpatient
- [ ] Referral to specialist
- [ ] Code/emergency handoff

**Handoff From:** [Name, Role]
**Handoff To:** [Name, Role]
**Date/Time:** [DateTime]

---

## Patient Identifiers

- **Name:** [Patient Name]
- **MRN:** [Medical Record Number]
- **DOB:** [Date of Birth]
- **Location:** [Room/Bed]

---

## S - SITUATION
*What is happening right now?*

**One-Sentence Summary:**
[Patient name] is a [age][sex] admitted for [primary reason], currently [stable/guarded/critical].

**Stability Status:**
- [ ] Stable - No immediate concerns
- [ ] Guarded - Requires close monitoring
- [ ] Critical - Active issues requiring intervention

**Why Handoff Now:**
[Shift change / Transfer for [reason] / Discharge because...]

**Immediate Concerns:**
[What I'm worried about in the next [timeframe]]

---

## B - BACKGROUND
*What is the clinical context?*

**Admission Information:**
- Admission Date: [Date]
- Admission Diagnosis: [Diagnosis]
- Attending Physician: [Name]
- Primary Team: [Service]

**Pertinent Medical History:**
- [Condition 1 - relevant because...]
- [Condition 2 - relevant because...]

**Key Events This [Shift/Hospitalization]:**
- [Event 1 with time]
- [Event 2 with time]

**Current Treatment Plan:**
[Brief summary of current management approach]

---

## A - ASSESSMENT
*What do I think is going on?*

**Current Vital Signs:**
| Vitals | Value | Trend |
|--------|-------|-------|
| Temp | [°F/C] | [↑ ↓ →] |
| HR | [bpm] | [↑ ↓ →] |
| BP | [mmHg] | [↑ ↓ →] |
| RR | [/min] | [↑ ↓ →] |
| O2 Sat | [%] on [RA/O2 amount] | [↑ ↓ →] |
| Pain | [0-10] | [↑ ↓ →] |

**Active Problems (by priority):**

1. **[Problem 1 - Highest Priority]**
   - Current status: [Description]
   - Current management: [What we're doing]
   - What I'm watching for: [Concerning changes]

2. **[Problem 2]**
   - Current status: [Description]
   - Current management: [What we're doing]
   - What I'm watching for: [Concerning changes]

3. **[Problem 3]**
   - Current status: [Description]
   - Current management: [What we're doing]

**My Assessment:**
[Clinical impression - what I think is happening and trajectory]

---

## R - RECOMMENDATION
*What needs to happen next?*

**Immediate Tasks (This Shift):**
- [ ] [Task 1] - Due [time]
- [ ] [Task 2] - Due [time]
- [ ] [Task 3] - Due [time]

**Follow-Up Items:**
| Item | Expected Time | Action if Abnormal |
|------|--------------|-------------------|
| [Lab/Result 1] | [When] | [What to do] |
| [Lab/Result 2] | [When] | [What to do] |

**Contingency Plans:**
- **If [Scenario 1]** → [Action to take]
- **If [Scenario 2]** → [Action to take]
- **If rapid decompensation** → [Who to call, what to do]

**Outstanding Consultations:**
- [Consult 1] - [Status: pending/following]
- [Consult 2] - [Status: pending/following]

---

## CRITICAL INFORMATION

**Allergies:**
| Allergen | Reaction |
|----------|----------|
| [Drug/substance] | [Reaction type] |

**Code Status:**
- [ ] Full Code
- [ ] DNR
- [ ] DNR/DNI
- [ ] Comfort Care Only
- [ ] Other: [Specify]

**Isolation Precautions:**
- [ ] None
- [ ] Contact
- [ ] Droplet
- [ ] Airborne
- [ ] Other: [Specify]

**Safety Alerts:**
- [ ] Fall risk - Precautions: [Specify]
- [ ] Suicide precautions - Level: [1:1/q15/etc.]
- [ ] Restraints - Type: [Specify] - Order expires: [Time]
- [ ] Aspiration risk - Precautions: [Specify]
- [ ] Other: [Specify]

---

## MEDICATIONS
*Key medications and timing*

**Critical Medications:**
| Medication | Dose | Route | Frequency | Last Given | Next Due |
|------------|------|-------|-----------|------------|----------|
| [Critical med 1] | [Dose] | [Route] | [Freq] | [Time] | [Time] |
| [Critical med 2] | [Dose] | [Route] | [Freq] | [Time] | [Time] |

**PRN Medications Used:**
- [PRN 1] given at [time] for [indication] - Effect: [Response]

**Medication Changes This Shift:**
- [Change 1 and reason]

---

## LINES, DRAINS, AND DEVICES

| Device | Location | Date Placed | Notes |
|--------|----------|-------------|-------|
| [IV/Central line] | [Site] | [Date] | [Flush schedule, issues] |
| [Foley/drain] | [Location] | [Date] | [Output, character] |

---

## FAMILY/SOCIAL

**Primary Contact:** [Name] - [Relationship] - [Phone]

**Family Updated:** [Yes/No] - Last update: [Time]

**Discharge Planning Notes:**
[Disposition plans, barriers, care coordination needs]

---

## READ-BACK VERIFICATION

**Receiving Clinician Confirms:**
- [ ] I have received the handoff report
- [ ] I have had opportunity to ask questions
- [ ] I understand the plan of care
- [ ] I know who to contact if issues arise

**Questions Asked:** [Document any clarifying questions]

**Handoff Completed:** [Time]
```

---

## Quick SBAR Template (For Verbal/Phone Handoff)

```markdown
# Quick SBAR Handoff

**S - Situation:**
"I'm calling about [Patient Name] in [Room]. [He/She] is a [age][sex] who [one-sentence summary]. I'm concerned because [specific concern]."

**B - Background:**
"[He/She] was admitted on [date] for [diagnosis]. Relevant history includes [1-2 key items]. [He/She] has been [brief trajectory]."

**A - Assessment:**
"I think [what's happening]. Vital signs are [key vitals]. [He/She] is currently [stable/declining/improving]."

**R - Recommendation:**
"I think we need to [specific action]. Are you available to [request]?"
```

---

## False-Positive Prevention

When filling this template:

❌ **DON'T:**
- Copy the Allergies table, Code Status or Isolation Precautions forward from the previous shift's handoff; a carried-over "Full Code" or empty allergy row still satisfies the "critical safety information included" checklist line while being stale.
- Draw a Trend arrow (↑ ↓ →) from a single set of vitals; an arrow needs at least two timed values, otherwise write "single value".
- Fill the "Action if Abnormal" column with a potassium, troponin or glucose cutoff from memory; use the ordered parameter, or write `per provider order` / `per facility protocol`.
- Compute "Last Given / Next Due" from the scheduled frequency; held, refused or late doses make that arithmetic wrong.
- Drop an ordered-but-unresulted lab, image or consult because the Follow-Up Items table only shows two rows.

✅ **DO:**
- Reconcile every Critical Medications row against the MAR, every Lines/Drains row against the current LDA record, and the allergy list against the chart's allergy field, not against the last handoff.
- Count pending items: each lab, imaging study and consult ordered and not yet resulted in the chart must appear in Follow-Up Items or Outstanding Consultations, so the two counts match.
- Check the restraint "Order expires" time and the suicide-precaution level against the active order, and re-time them if the order was renewed this shift.
- Mark any field you could not confirm as `[not verified — source]` instead of leaving a plausible default ticked.

---

## Quality Checklist

- [ ] Patient correctly identified (2 identifiers)
- [ ] All critical safety information included (allergies, code status, isolation)
- [ ] Active problems prioritized
- [ ] Contingency plans documented ("if X, then Y")
- [ ] Pending tasks clearly listed with timeframes
- [ ] Expected results documented with action thresholds
- [ ] Receiving clinician has opportunity for questions
- [ ] Read-back completed and documented
