---
title: "Type 1 Diabetes Longitudinal Care Plan"
category: domain-healthcare-clinical/care-plans
description: "Design a type 1 diabetes management plan: basal-bolus or pump dosing, carb ratios, correction factors, CGM targets, and hypoglycemia/DKA prevention with named doses."
techniques:
  - ST-02
  - ST-03
  - CM-01
  - RT-02
  - RT-05
  - DS-02
difficulty: advanced
tags:
  - endocrine
  - diabetes
  - type-1
  - care-plan
updated: "2026-06-19"
---

## Objective

Produce a longitudinal type 1 diabetes plan: total daily dose and basal/bolus split, insulin-to-carb ratio (ICR), correction (sensitivity) factor, CGM targets and time-in-range goals, hypoglycemia and DKA prevention, and complication surveillance. Output is a usable insulin regimen plus a monitoring/escalation plan.

## Inputs

- Glycemic data: A1c, CGM time-in-range / mean glucose / GMI, frequency and severity of hypoglycemia, hypoglycemia awareness
- Current regimen: MDI vs pump, basal insulin/rate, ICR, correction factor, total daily dose, adherence
- Patient: weight, age, duration, occupation/driving, exercise pattern, pregnancy plans, comorbid autoimmune disease (thyroid, celiac)
- Renal function, retinopathy status, prior DKA episodes

## Role

Endocrinologist managing T1DM, writing a regimen the patient and team can follow.

## Reasoning Steps

1. **Set targets.** A1c <7% for most; CGM time-in-range (70–180) >70%, time-below-range (<70) <4%, time <54 <1%. Loosen in hypoglycemia unawareness or limited life expectancy.

2. **Estimate total daily dose (TDD).** Typically 0.4–0.6 units/kg/day; lower in honeymoon, higher in puberty/insulin resistance. Split ~50% basal, 50% bolus.

3. **Basal:** glargine U-100/U-300 or degludec once daily (degludec flattest, most forgiving of timing); or pump basal rate(s). Verify basal adequacy with a fasting/overnight CGM trace — glucose should stay flat when fasting.

4. **Insulin-to-carb ratio (bolus for food):** start with 500 rule — ICR = 500 ÷ TDD (1 unit per X g carbs). Refine by postprandial CGM.

5. **Correction factor (sensitivity):** 1800 rule for rapid analogs — CF = 1800 ÷ TDD (1 unit drops glucose X mg/dL). Target correction to ~120.

6. **Choose prandial analog:** lispro/aspart/glulisine, or ultra-rapid (faster aspart, lispro-aabc) for postprandial spikes. Dose 10–15 min before meals.

7. **Hypoglycemia plan:** glucagon prescription (nasal or autoinjector) for everyone; treat lows with 15 g fast carbs, recheck 15 min; reduce basal/bolus and review pattern if recurrent; CGM low alerts; address unawareness by relaxing targets 2–3 weeks to restore counterregulation.

8. **DKA prevention:** sick-day rules — never stop basal insulin, check ketones when glucose >250 or ill, supplemental correction q3–4h, hydration, when to seek care. Pump users: ketone risk higher (only rapid insulin) — backup pen + infusion-set troubleshooting.

9. **Technology:** consider CGM for all; automated insulin delivery (hybrid closed-loop) for time-in-range and hypoglycemia reduction.

10. **Surveillance:** annual TSH, celiac screen if symptoms, annual UACR/eGFR and dilated retina after 5 years duration, lipid panel, BP <130/80, foot exam.

## Output Format

```
TARGETS: A1c [ ], TIR >70%, TBR <4%

INSULIN REGIMEN:
- TDD estimate: [units/kg → total]
- Basal: [drug/rate, timing] (≈50% TDD)
- Prandial: [analog], ICR = 1:[g], dose timing
- Correction factor: 1 unit per [mg/dL], target 120
- Pump vs MDI rationale

CGM / MONITORING:
- TIR/TBR review cadence
- Pattern-management rules

HYPOGLYCEMIA PLAN:
- Glucagon Rx
- 15/15 rule, recurrent-low adjustments
- Unawareness protocol

DKA PREVENTION / SICK-DAY RULES:
- Never stop basal; ketone checks; supplemental dosing

SURVEILLANCE:
- TSH, UACR/eGFR, retina, lipids, BP, foot, celiac

ADJUSTMENTS THIS VISIT:
- [concrete dose changes]
```

## Worked Example

**Input:** 27 y/o F, T1DM 12 years, 65 kg, MDI. A1c 7.9%. CGM: TIR 58%, TBR 6%, mean glucose 168, frequent overnight lows and pre-lunch highs. Current: glargine 28 units qAM, aspart ICR 1:10, CF 1:40. Active (runs 4×/week). Has glucagon. No complications.

**Output:**

```
TARGETS: A1c <7%, TIR >70%, TBR <4% (currently 6% — too many lows).

INSULIN REGIMEN:
- TDD ~ 0.6 u/kg historically (~40 u). Current basal 28 is high relative to bolus → likely overbasalized, driving overnight lows.
- Basal: reduce glargine 28 → 24 units; consider switch to degludec for flatter profile and exercise forgiveness, or split-dose glargine. Move dose timing review.
  - Better: verify with overnight CGM after reduction; basal correct when fasting trace flat.
- Prandial: aspart. Pre-lunch highs suggest breakfast ICR too weak — tighten breakfast ICR 1:10 → 1:8; keep lunch/dinner 1:10 pending data.
- Correction factor 1:40, target 120 — reasonable; recheck after basal fix.
- Recommend hybrid closed-loop (AID) pump given variability + exercise — automates overnight basal reduction, would directly address the overnight lows.

CGM / MONITORING:
- Review CGM AGP every 2 weeks during titration.
- Set low alert 80, urgent-low 70.

HYPOGLYCEMIA PLAN:
- Glucagon current — confirm not expired.
- Exercise rule: reduce basal 20% or set temp target on run days; 15–30 g carbs pre-run.
- TBR 6% → the basal reduction is the primary fix.

DKA PREVENTION / SICK-DAY RULES:
- Never stop basal; check ketones if glucose >250 or ill; correct q3–4h; hydrate.

SURVEILLANCE:
- Annual TSH (autoimmune cluster), UACR/eGFR, dilated retina (due — 12 y duration), lipids, BP, foot exam today.

ADJUSTMENTS THIS VISIT:
- Glargine 28 → 24 units (or transition to degludec 24).
- Breakfast ICR 1:10 → 1:8.
- Pre-run basal/temp-target counseling; refer for AID pump eval.
- Recheck CGM AGP in 2 weeks.
```
