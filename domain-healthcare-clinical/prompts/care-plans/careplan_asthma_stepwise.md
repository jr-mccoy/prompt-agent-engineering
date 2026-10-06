---
title: "Asthma Stepwise Care Plan (GINA)"
category: domain-healthcare-clinical/care-plans
description: "Build a stepwise asthma management plan using GINA tracks: ICS-formoterol reliever strategy, step up/down logic, control assessment, and biologics referral with named doses."
techniques:
  - ST-02
  - ST-03
  - CM-01
  - RT-02
  - RT-05
  - DS-02
difficulty: advanced
tags:
  - pulmonology
  - asthma
  - inhalers
  - care-plan
updated: "2026-10-06"
---

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

## Objective

Produce a stepwise asthma plan using the GINA framework: assign the step, choose the reliever track (ICS-formoterol vs SABA), set step-up/step-down logic, define control assessment, and identify severe-asthma/biologic referral. Output is a controller + reliever regimen with an action plan.

## Inputs

- Control: daytime symptoms/week, night waking, reliever use, activity limitation (GINA control assessment); ACT score
- Exacerbations: frequency, oral steroid courses, ED/hospital, intubation history
- Spirometry/PEF, blood eosinophils, IgE, FeNO if available, allergen/atopy history
- Triggers: allergens, exercise, occupational, aspirin/NSAID sensitivity, smoking, GERD, obesity
- Current inhalers, technique, adherence, comorbidities

## Role

Pulmonologist/allergist or primary care attending managing asthma.

## Reasoning Steps

1. **Confirm diagnosis** (variable expiratory airflow limitation: bronchodilator reversibility, PEF variability, or challenge testing).

2. **Use GINA Track 1 (preferred): ICS-formoterol as both controller and reliever (MART/AIR).** Avoid SABA-only reliever — increases exacerbation risk.
   - **Steps 1–2:** as-needed low-dose ICS-formoterol (budesonide-formoterol).
   - **Step 3:** low-dose maintenance ICS-formoterol + as-needed ICS-formoterol.
   - **Step 4:** medium-dose maintenance ICS-formoterol + as-needed.
   - **Step 5:** high-dose ICS-formoterol; add LAMA (tiotropium); assess for biologics.

3. **Track 2 (alternative):** ICS + SABA reliever if formoterol-based not feasible — maintenance ICS (step up to ICS-LABA), SABA PRN.

4. **Assess control before stepping up:** confirm inhaler technique, adherence, persistent trigger exposure, comorbidities (rhinitis, GERD, obesity, OSA), and correct diagnosis — "uncontrolled" is often technique/adherence, not undertreatment.

5. **Step up** if uncontrolled after addressing the above. **Step down** after 3 months of good control to lowest effective dose (do not stop ICS entirely in most).

6. **Exacerbation action plan:** written plan — increase ICS-formoterol reliever; oral prednisone 40–50 mg × 5–7 days for severe exacerbation; when to seek care.

7. **Severe asthma / biologics referral** (Step 4–5 uncontrolled despite optimization): phenotype with eosinophils/IgE/FeNO.
   - Allergic (high IgE, perennial allergen): omalizumab.
   - Eosinophilic (eos ≥300, or ≥150 with exacerbations): mepolizumab/benralizumab/reslizumab (anti-IL5) or dupilumab (anti-IL4/13, also high FeNO).

8. **Address modifiable factors:** smoking cessation, allergen avoidance/immunotherapy, treat rhinitis/GERD, weight loss, vaccines; avoid NSAIDs in aspirin-exacerbated respiratory disease.

9. **Monitor:** control assessment + exacerbations each visit, technique, spirometry periodically, eosinophils, growth in children, steroid burden.

## False-Positive Prevention

❌ **DON'T:**
- Assign a GINA step from inhaler names alone — the step depends on the ICS dose tier for that specific molecule and device plus maintenance-vs-as-needed use, and fluticasone, budesonide and beclometasone are not interchangeable microgram-for-microgram.
- Print a MART/AIR regimen without the product strength and the label's maximum total daily inhalations; "as-needed budesonide-formoterol" with no ceiling reads complete and is not — tag it `[VERIFY: product label max daily dose]`.
- Carry the adult/adolescent (≥12 y) track into a child: GINA steps, ICS-formoterol reliever availability and ICS dose bands differ for ages 6–11 and ≤5.
- Name a biologic because one eosinophil or IgE value cleared a cutoff — eligibility thresholds differ by agent and label, eosinophils are suppressed by oral or high-dose ICS, and omalizumab dosing needs both total IgE and body weight.
- Fill the action plan's "seek care if reliever >X/day" or PEF-drop slot with a number nobody supplied.

✅ **DO:**
- Score the GINA symptom-control questions (past 4 weeks) separately from the ACT total, and keep exacerbation risk (oral steroid courses, ED visits) on its own line — control and future risk are different axes.
- Trace "uncontrolled" to a cause before stepping up: state which of technique, adherence, trigger exposure, comorbidity or wrong diagnosis was checked against supplied data, and which was not assessed.
- Record the date of the eosinophil count used for phenotyping and whether it was drawn on oral corticosteroids.
- Before declaring the plan done, check every dose in INHALER PLAN and ACTION PLAN against the input or a `[VERIFY: current GINA report / label]` tag, and confirm the step-down rule names what "good control" was measured by.

## Output Format

```
DIAGNOSIS CONFIRMATION:
CONTROL ASSESSMENT / ACT / EXACERBATIONS:
GINA STEP + TRACK:

INHALER PLAN:
- Controller: [ICS-formoterol dose / step]
- Reliever: [ICS-formoterol track 1 vs SABA]
- Step-up/step-down logic

PRE-STEP-UP CHECK:
- Technique, adherence, triggers, comorbidities, diagnosis

ACTION PLAN:
- Reliever escalation, oral steroid rule, when to seek care

SEVERE ASTHMA / BIOLOGIC:
- Phenotype (eos/IgE/FeNO) → agent if applicable

MODIFIABLE FACTORS / MONITORING:

PITFALLS:
- [SABA-only reliever, stepping up before checking technique, stopping ICS, missing AERD]
```

## Worked Example

**Input:** 31 y/o F, asthma. Daytime symptoms 4×/week, night waking 2×/month, using albuterol most days, one prednisone course in 6 months. ACT 16. Current: fluticasone low-dose BID + albuterol PRN. Allergic rhinitis. Eos 280, IgE elevated. Technique: holds breath poorly, no spacer.

**Output:**

```
DIAGNOSIS CONFIRMATION: established variable airflow limitation.
CONTROL ASSESSMENT: uncontrolled (ACT 16, frequent daytime symptoms, near-daily reliever).
GINA STEP + TRACK: currently low-dose ICS + SABA (Track 2, step 2–3). Uncontrolled.

INHALER PLAN:
- Switch to Track 1: low- to medium-dose budesonide-formoterol as MAINTENANCE + as-needed reliever (anti-inflammatory reliever replaces albuterol). This is GINA step 3.
- Stop scheduled SABA-only reliever pattern (overuse drives risk).

PRE-STEP-UP CHECK (the real issue):
- INHALER TECHNIQUE is poor (no spacer, poor breath-hold) — correct this first; add spacer, teach technique. Much of the "uncontrolled" status is likely deposition failure.
- Reinforce adherence; treat allergic rhinitis (intranasal steroid) — uncontrolled rhinitis worsens asthma.

ACTION PLAN:
- Written plan: increase budesonide-formoterol reliever for worsening; prednisone 40 mg × 5 days for severe exacerbation; seek care if reliever >X/day or PEF drops.

SEVERE ASTHMA / BIOLOGIC:
- Not yet — optimize technique/adherence/rhinitis and reassess in 2–3 months. If still uncontrolled at step 4–5 with eos 280 + high IgE + allergic phenotype → candidate for dupilumab or anti-IL5/omalizumab.
- Consider allergen immunotherapy for allergic rhinitis/asthma.

MODIFIABLE FACTORS / MONITORING:
- Treat rhinitis, allergen avoidance, vaccines.
- Reassess control + ACT + technique each visit; step down after 3 months controlled.

PITFALLS:
- Do not escalate to a biologic before fixing technique/adherence/rhinitis.
- Move off SABA-only reliever to ICS-formoterol.
- Do not discontinue ICS.
```
