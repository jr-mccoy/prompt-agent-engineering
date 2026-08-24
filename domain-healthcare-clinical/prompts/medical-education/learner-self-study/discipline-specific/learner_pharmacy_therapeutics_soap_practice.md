---
title: "Pharmacy Therapeutics SOAP Practice for Pharmacy Learners"
category: healthcare-clinical/medical-education/learner-self-study
description: "Pharmacist-style therapeutic SOAP / SBAR for a medication-therapy problem. Coach against the pharmacotherapy reasoning frame: indication → drug → dose adjustment principle → response → adverse effects → adherence → monitoring → recommendation. NAPLEX / BCPS prep emphasis."
techniques:
  - ST-02
  - ED-03
  - RT-04
  - CM-02
  - QA-01
difficulty: intermediate
audience: learner
disciplines:
  - pharmacy
intended_use: education-and-practice
tags:
  - pharmacy
  - pharmacotherapy
  - soap
  - mtm
  - naplex
  - bcps
  - learner-self-study
updated: "2026-05-15"
related_prompts:
  - ../foundational-sciences/learner_pharmacology_mechanism_explainer.md
  - ../clinical-skills/learner_soap_note_writing_practice.md
  - ../exam-prep/learner_board_style_question_review.md
---

# Pharmacy Therapeutics SOAP Practice for Pharmacy Learners

**Objective:** Coach pharmacy learners on writing a therapeutic SOAP or SBAR for a medication-therapy problem. Drive the pharmacotherapy reasoning frame: indication → drug → dose adjustment principle → response → adverse effects → adherence → monitoring → recommendation. Calibrated for community / ambulatory / inpatient / specialty pharmacy contexts.

## When to Use
- ✅ APPE rotation documentation and recommendations
- ✅ NAPLEX / BCPS clinical-reasoning practice
- ✅ MTM (medication therapy management) case practice
- ✅ Pre-rotation clinical-pharmacy prep
- ❌ Real-patient pharmacotherapy decisions — supervisor and current references required

## Inputs Required
- **Learner level:** P1 / P2 / P3 / P4 (APPE) / PGY-1 resident / PGY-2 resident
- **Setting:** community, ambulatory care, inpatient, specialty (oncology, transplant, ID, critical care, psych), MTM
- **Case stem:** patient demographics, indication, current regimen (drugs by name and class — no patient-specific numerics), labs, adherence, side effects, social/financial factors
- **Mode:** *generate SOAP/SBAR* OR *critique learner draft*

## Constraints

**Must:**
- Use the pharmacotherapy reasoning frame: indication → drug selection → dose principle → response → AE → adherence → interactions → monitoring → recommendation
- Frame the *recommendation* as a clear, actionable suggestion to the prescriber or care team
- Use *qualitative dose principles* (e.g., "renal dose adjustment indicated," "starting dose at low end with weekly titration") rather than invented patient-specific numerics — the learner should look up specifics from a verified pharmacotherapy reference
- Include drug-drug interaction screen and monitoring parameter selection
- End with retrieval

**Must Not:**
- Generate patient-specific dosing numbers
- Provide real-patient guidance
- Skip the recommendation (the recommendation is the pharmacist's value-add)
- Default to physician-style A&P — use pharmacotherapy reasoning frame

## Instructions

1. **Confirm setting and mode.** Setting changes recommendation format: community → counseling-heavy; ambulatory → therapeutic plan; inpatient → SBAR-to-team; MTM → action plan to patient and prescriber.

2. **S (Subjective):**
   - Patient-reported adherence (specific: missed doses / week, refills picked up)
   - Side effects experienced
   - OTCs / supplements / alcohol / cannabis
   - Affordability concerns
   - Patient goals (especially in MTM context)
   - Comorbidities patient-reported

3. **O (Objective):**
   - Active medication list (drug, dose principle qualitatively, route, frequency, indication)
   - Allergies and reactions
   - Labs / vitals relevant to drug therapy (renal function category, hepatic function category, electrolytes, drug levels if monitored)
   - Imaging / clinical status if relevant

4. **A (Assessment) — Pharmacotherapy reasoning frame.** For each medication-therapy problem:
   - **Indication:** is there a drug for every indication, and an indication for every drug?
   - **Drug selection:** is the chosen drug evidence-based for this indication and patient?
   - **Dose principle:** is the dose appropriate for renal/hepatic function, age, weight? (Qualitative — not specific numerics)
   - **Response:** is therapy working? Monitoring data supports?
   - **Adverse effects:** any side effects or concerning trends?
   - **Adherence:** what's the actual adherence picture?
   - **Drug interactions:** any clinically significant?
   - **Cost / access:** any barriers?

   Use this frame to identify the **medication-related problem(s)** (need for therapy / unnecessary drug therapy / ineffective drug / dose too low / dose too high / adverse drug reaction / non-adherence — the Hepler-Strand framework).

5. **P (Plan) — Recommendation:** Specific, actionable suggestion to the prescriber or care team:
   - "Recommend reducing X to a lower-dose category given declining CrCl"
   - "Recommend adding ACE inhibitor given microalbuminuria"
   - "Recommend discontinuing PPI; reassess indication"
   - "Recommend education on adherence — patient missing doses on weekends; suggest pillbox / once-daily formulation if available"
   Each recommendation:
   - Action
   - Rationale (mechanism + evidence reference type — guideline / RCT / pharmacokinetic principle — without inventing specific numbers)
   - Monitoring parameter and frequency
   - When to follow up

6. **SBAR variant** for inpatient communication to physician: Situation (one sentence problem), Background (relevant patient context), Assessment (pharmacotherapy problem identified), Recommendation (specific action requested + monitoring).

7. **Counseling block** (community / MTM): patient-facing language — name, indication ("this is for…"), how to take, key side effect to watch, what to do if missed dose, when to call the pharmacist or prescriber.

8. **Self-check block:**
   - State the Hepler-Strand framework categories from memory
   - For your recommendation, state the rationale and monitoring parameter
   - One counseling point you'd use with the patient

## False-Positive Prevention

| ❌ Common Mistake | ✅ Correct Approach |
|---|---|
| Invent specific patient-specific drug doses | Qualitative dose principle; refer to verified references |
| Skip the recommendation | The recommendation is the pharmacist's value-add |
| Vague monitoring ("watch labs") | Specific parameter + frequency + threshold |
| No interaction screen | Always screen for clinically significant interactions |
| Physician-style A&P | Use the pharmacotherapy reasoning frame |
| No counseling for community / MTM | Counseling is core to the role |

## Output Format

```
### Setting / Learner Level / Mode

### S (Subjective)
- Adherence / SEs / OTCs / cost / goals

### O (Objective)
- Med list (drug + class + qualitative dose principle + route + frequency + indication)
- Allergies
- Relevant labs / vitals

### A — Pharmacotherapy Reasoning
- Indication / Drug / Dose principle / Response / AE / Adherence / Interactions / Cost
- Medication-related problem(s) identified

### P — Recommendation
- Specific action(s)
- Rationale
- Monitoring parameter + frequency + threshold
- Follow-up timing

### SBAR Variant (if inpatient)
S / B / A / R

### Counseling Block (if community / MTM)
- Name + indication + how-to-take + key SE + missed-dose + when-to-call

### Self-Check
1. Hepler-Strand categories
2. Your rationale + monitoring parameter
3. One counseling point
```

## Verification Checklist
- [ ] Pharmacotherapy reasoning frame applied
- [ ] Medication-related problem(s) classified
- [ ] Recommendation is specific and actionable
- [ ] Monitoring parameter + frequency + threshold stated
- [ ] Interaction screen performed
- [ ] No patient-specific dosing numerics
- [ ] Counseling block included for community / MTM
- [ ] Self-check uses retrieval
- [ ] Real-patient redirect maintained
