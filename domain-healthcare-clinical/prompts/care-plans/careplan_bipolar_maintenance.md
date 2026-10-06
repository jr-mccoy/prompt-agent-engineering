---
title: "Bipolar Disorder Maintenance Care Plan"
category: domain-healthcare-clinical/care-plans
description: "Build a bipolar maintenance plan: mood stabilizer selection, lithium/valproate monitoring, antidepressant cautions, and relapse-prevention with named drugs, doses, and target levels."
techniques:
  - ST-02
  - ST-03
  - CM-01
  - RT-02
  - RT-05
  - DS-02
difficulty: advanced
tags:
  - psychiatry
  - bipolar
  - mood-stabilizer
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

Produce a bipolar disorder maintenance care plan: select a maintenance mood stabilizer matched to the illness pole/polarity, set therapeutic drug monitoring, define antidepressant policy, and build relapse prevention. Output is a maintenance regimen with monitoring schedule.

## Inputs

- Diagnosis: bipolar I vs II, predominant polarity (manic vs depressive), rapid cycling, mixed features, psychosis history
- Course: number/severity of episodes, most recent episode, current state (euthymic/sub-syndromal), suicide history
- Prior treatments: mood stabilizers/antipsychotics tried, response, tolerability, levels
- Labs: renal/thyroid (lithium), LFTs/CBC (valproate), metabolic; pregnancy plans (valproate teratogenicity)
- Comorbidities, substance use, adherence history

## Role

Psychiatrist managing bipolar maintenance.

## Reasoning Steps

1. **Confirm bipolar type and predominant polarity** — drives agent choice. Assess current mood state, mixed features, rapid cycling, and suicide risk.

2. **Maintenance mood stabilizer selection:**
   - **Lithium** — first-line; best anti-manic + anti-suicidal evidence. Target level 0.6–0.8 mEq/L maintenance (up to 1.0 if needed). Avoid in significant renal disease; teratogenic (Ebstein anomaly — counsel).
   - **Valproate** — manic/mixed/rapid cycling; level ~50–100 µg/mL. **Contraindicated in pregnancy/people who may become pregnant** (neural tube defects, neurodevelopmental harm) unless no alternative + reliable contraception.
   - **Lamotrigine** — best for bipolar **depression** prevention (weak anti-manic); slow titration to avoid SJS (25 mg → increase q2 weeks to 200 mg; adjust with valproate/OCPs).
   - **Atypical antipsychotics** — quetiapine (covers both poles incl. depression), aripiprazole/risperidone LAI (anti-manic, adherence), lurasidone/cariprazine (bipolar depression), olanzapine (effective but metabolic burden).

3. **Match to polarity:** predominant mania → lithium, valproate, aripiprazole; predominant depression → lamotrigine, quetiapine, lurasidone; mixed/rapid cycling → valproate, atypicals, avoid antidepressants.

4. **Antidepressant policy:** avoid antidepressant monotherapy (manic switch, cycle acceleration); if used for breakthrough depression, only with a mood stabilizer and cautiously; first optimize the stabilizer or use bipolar-depression agents.

5. **Combination** for inadequate monotherapy (e.g., lithium + atypical; lithium + lamotrigine for mixed-pole protection).

6. **Therapeutic drug monitoring:**
   - Lithium: level 5 days after start/change (trough, 12 h post-dose), then q3–6 months when stable; renal function + TSH + calcium q6–12 months; watch NSAID/ACEi/thiazide/dehydration interactions and toxicity signs.
   - Valproate: level, CBC, LFTs periodically.
   - Metabolic monitoring for antipsychotics (weight, glucose, lipids).

7. **Relapse prevention:** psychoeducation, mood charting, sleep regularity (sleep loss precipitates mania), substance reduction, early-warning-sign action plan, adherence support (consider LAI), psychotherapy (CBT/IPSRT/family-focused).

8. **Monitor:** mood state, adherence, levels/labs, suicidality, side effects, pregnancy planning.

## False-Positive Prevention

❌ **DON'T:**
- Call a lithium level therapeutic without its timing — a sample drawn well before the 12-hour trough, or before steady state after a dose change, misstates exposure; and the target band is often lower in older adults.
- Copy one lamotrigine titration into a plan whose medication list includes valproate (raises lamotrigine levels) or an estrogen-containing contraceptive (lowers them) — each needs its own schedule `[VERIFY: lamotrigine label titration table]`.
- Treat "not currently pregnant" as closing the valproate question; anyone who could become pregnant needs the current label/regulator pregnancy-prevention requirements recorded.
- Label predominant polarity from the most recent episode — it is a count across the whole episode history, and the wrong pole picks the wrong maintenance agent.
- Leave an antidepressant already on the patient's list unaddressed because the policy line says "no monotherapy".

✅ **DO:**
- Before finalising THERAPEUTIC DRUG MONITORING, run every drug on the input list against lithium (NSAIDs, ACEi/ARB, thiazides) and against valproate/lamotrigine, and state the level recheck each start or stop triggers.
- Attribute each lab interval to the drug that requires it — renal/TSH/calcium to lithium, CBC/LFTs to valproate, weight/glucose/lipids to antipsychotics — so the schedule can be audited.
- Check every reported level carries units (lithium mmol/L ≡ mEq/L; valproate µg/mL ≡ mg/L) and flag any that does not.
- For a cross-taper, state at each step which agent is providing relapse protection, so the sequence never leaves a window with neither at an effective dose.

## Output Format

```
DIAGNOSIS (I/II) / PREDOMINANT POLARITY / CURRENT STATE:

MAINTENANCE REGIMEN:
- Mood stabilizer: [agent, dose, target level]
- Combination if needed
- Antidepressant policy

THERAPEUTIC DRUG MONITORING:
- [drug levels + interval; renal/thyroid/metabolic schedule]

RELAPSE PREVENTION:
- Psychoeducation, sleep, mood charting, action plan, psychotherapy, adherence/LAI

MONITORING:
- Mood, levels/labs, suicidality, side effects, pregnancy

PITFALLS:
- [antidepressant monotherapy switch, lithium toxicity/interactions, valproate in pregnancy, lamotrigine rash, missed metabolic monitoring]
```

## Worked Example

**Input:** 38 y/o F, bipolar I, predominant manic polarity, two prior manic episodes (one with psychosis), now euthymic 4 months on quetiapine 300 mg with daytime sedation she dislikes. Normal renal/thyroid. Not currently pregnant but wants to conceive in the next year. No substance use.

**Output:**

```
DIAGNOSIS / POLARITY / STATE: bipolar I, predominant mania (psychotic features history), currently euthymic.

MAINTENANCE REGIMEN:
- Predominant-manic + pregnancy planning: lithium is the strongest anti-manic/anti-suicidal maintenance and is preferable to valproate here (valproate contraindicated with conception plans). Cross-titrate from quetiapine to lithium; target 0.6–0.8 mEq/L.
- Counsel lithium in pregnancy: small Ebstein-anomaly risk — plan with OB, fetal echo, dose management across trimesters; still often preferred over valproate (which is firmly contraindicated).
- Avoid valproate given conception plans.
- Quetiapine: taper as lithium establishes (addresses her sedation complaint); could retain low-dose or an alternative atypical if breakthrough.

ANTIDEPRESSANT POLICY: no antidepressant monotherapy. Breakthrough depression → optimize lithium, add lamotrigine or quetiapine/lurasidone rather than an antidepressant.

THERAPEUTIC DRUG MONITORING:
- Lithium level 5 days after start/change (12-h trough), then q3–6 months stable.
- Renal function + TSH + calcium at baseline and q6–12 months.
- Counsel interactions (NSAIDs, ACEi, thiazides, dehydration) and toxicity signs.

RELAPSE PREVENTION:
- Psychoeducation, sleep regularity (sleep loss → mania), mood charting, early-warning action plan, IPSRT/CBT, adherence support.
- Preconception counseling and coordinated pregnancy plan.

MONITORING: mood state, adherence, lithium level/renal/thyroid, suicidality, side effects, contraception/pregnancy timing.

PITFALLS:
- Do not use valproate in someone planning pregnancy.
- Do not add an antidepressant alone.
- Lithium toxicity risk with NSAIDs/dehydration — counsel explicitly.
```
