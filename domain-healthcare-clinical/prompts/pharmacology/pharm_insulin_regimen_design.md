---
title: "Insulin Regimen Design"
category: domain-healthcare-clinical/pharmacology
description: "Design a basal-bolus, basal-only, premixed, or insulin-pump regimen from total daily dose estimation, basal/bolus split, insulin-to-carb ratio, correction factor, and titration logic; specify named insulins with doses, timing, and monitoring."
techniques:
  - ST-02
  - ST-03
  - CM-01
  - RT-02
  - RT-05
  - QA-01
difficulty: advanced
tags:
  - endocrinology
  - diabetes
  - insulin
  - dosing
  - inpatient
  - outpatient
updated: "2026-05-12"
---

## Objective

Design an insulin regimen tailored to a specific patient: estimate total daily dose (TDD), choose the right strategy (basal-only, basal-plus, full basal-bolus, premixed, sliding-scale supplementation, or pump), distribute the dose across basal and prandial components, compute insulin-to-carbohydrate ratio (ICR) and correction factor (CF), and write titration rules. Output names specific insulins, units, timing, monitoring, and decision rules for adjustment.

## Inputs

- Diabetes type (T1DM, T2DM, steroid-induced, gestational, post-pancreatic), age, weight, GFR, hepatic function
- Current glycemic data: A1c, fasting and postprandial fingersticks, CGM time-in-range / TBR / GMI if available, episodes of hypoglycemia (severity, awareness)
- Current regimen: oral and non-insulin injectable agents, current insulin (if any), dose
- Lifestyle: meal pattern (regular vs irregular), carbohydrate counting capability, work / sleep schedule, exercise pattern, alcohol use
- Setting: outpatient initiation, intensification, hospital (medical floor, ICU), perioperative, DKA/HHS-resolution transition, end-stage renal disease, pregnancy
- Goals: A1c target (typically <7% in most adults, <6.5% in pregnancy, individualized to ~7.5–8.5% in older / frail / hypoglycemia-prone)

## Role

Senior endocrinologist / inpatient diabetes specialist writing a prescriptive regimen with explicit titration rules.

## Reasoning Steps

1. **Estimate Total Daily Dose (TDD).**
   - **T1DM at diagnosis:** start conservatively at 0.3–0.5 units/kg/day. Honeymoon phase patients may need less.
   - **T2DM initiating insulin** (oral failure, hospitalization, A1c >9–10%): start 0.2–0.4 units/kg/day, or 10 units of basal nightly.
   - **Steroid-induced hyperglycemia:** depends on steroid dose; rough guide for prednisone equivalent — add 0.1 units/kg/day per 10 mg prednisone (peak need ~6 h after morning dose).
   - **DKA/HHS transition:** TDD ≈ 0.5–0.7 units/kg/day; transition to subcutaneous with overlap (basal insulin 1–2 h *before* stopping IV insulin drip).
   - **Pregnancy (gestational and pre-existing):** rising requirements through trimester 2 and 3 (1st trimester 0.7 u/kg/day → 3rd trimester 1.0 u/kg/day); titrate aggressively to fasting <95, 1-hour postprandial <140 or 2-hour <120.
   - **Hospital basal-bolus in T2DM** (per RABBIT-2): 0.4 units/kg/day if A1c <8% or BG <200, 0.5 if A1c 8–10%, hold 0.1 if AKI / elderly / risk of hypoglycemia.

2. **Split TDD into basal and prandial.**
   - **Basal-bolus** (T1DM and intensified T2DM): 50% basal, 50% prandial (split ~equally across 3 meals).
   - **Basal-plus**: full basal + 1 prandial dose at the largest meal; intensify to full basal-bolus if not at goal.
   - **Basal-only**: T2DM initiation; titrate basal upward; if basal >0.5 u/kg/day or fasting at goal but postprandial out of range, intensify with prandial.
   - **Premixed (70/30, 75/25, 50/50)**: simpler regimen for patients unable or unwilling to manage 4 injections; fixed ratio of intermediate + rapid. Less flexible; useful for patients with regular meal patterns.

3. **Choose specific insulins.**
   - **Basal:**
     - Glargine U-100 (Lantus, Basaglar, Semglee): 24h once daily; peak modest at 6–8 h.
     - Glargine U-300 (Toujeo): flatter, longer (~36 h); less hypoglycemia; smaller injection volume.
     - Detemir (Levemir): ~12–20 h; usually BID for full coverage.
     - Degludec (Tresiba): ultra-long-acting (>42 h); flexible timing day-to-day; lowest nocturnal hypoglycemia rates (DEVOTE).
     - NPH: intermediate (~12 h, peak at 4–8 h); BID; cheap; risk of mid-day and nocturnal hypoglycemia from peaks. Useful in steroid-induced hyperglycemia (peak aligns with prednisone effect when given AM with steroid).
   - **Prandial / rapid:**
     - Lispro (Humalog), aspart (Novolog), glulisine (Apidra): onset 10–15 min, peak 1–2 h, duration 3–5 h. Inject 0–15 min before meal.
     - Faster aspart (Fiasp), lispro-aabc (Lyumjev): faster onset (within 5 min) — may inject at start of or just after meal.
     - Regular insulin (R): onset 30 min, peak 2–4 h, duration 6–8 h. Inject 30 min before meal. IV use in DKA/ICU.
     - Inhaled insulin (Afrezza): ultra-rapid; less commonly used; pulmonary function monitoring needed.
   - **Premixed:** 70/30 NPH-regular, 70/30 aspart, 75/25 lispro, 50/50 lispro. Pre-breakfast and pre-dinner.
   - **Concentrated insulins for high-TDD patients:** U-500 regular (5× concentration; use for TDD >200 units), U-200 lispro, U-200 degludec. Insulin-resistance / severe T2DM situations.

4. **Compute insulin-to-carbohydrate ratio (ICR) and correction factor (CF).**
   - **ICR ("500 rule"):** 500 / TDD = grams of carbohydrate covered by 1 unit. Example: TDD 50 → ICR 1:10 (1 unit covers 10 g carbs).
   - **CF ("1800 rule for rapid", "1500 rule for regular"):** 1800 / TDD = mg/dL drop per 1 unit (rapid). Example: TDD 50 → CF 1:36 (1 unit drops BG by ~36 mg/dL).
   - **Target BG for correction:** typically 100–120 mg/dL pre-meal, 140–150 pre-bedtime.
   - **Mealtime calculation:** prandial dose = (grams carb / ICR) + (current BG − target) / CF (skip correction if BG < target).
   - **Verify the math** before issuing the order: divide TDD into 50/50 basal-prandial; sum should equal TDD; ICR and CF computed from TDD; targets specified.

5. **Specify monitoring and titration rules.**
   - **Glucose monitoring:** at minimum AC + HS fingersticks (4×/day) for basal-bolus; CGM strongly preferred when available — provides time-in-range, hypoglycemia detection, and trend.
   - **Basal titration:** target fasting BG 80–130 (or pregnancy <95). Titrate basal up by 1–2 units every 3 days until fasting at target. Hold or reduce by 10–20% if fasting <70 or any severe hypoglycemia.
   - **Prandial titration:** assess 2-hour postprandial; target <180 (or pregnancy <120 at 2h). Adjust ICR by reducing ratio (e.g., 1:10 → 1:8 makes the dose larger) if persistently high postprandial; loosen ratio if hypoglycemia 2–4 h after meal.
   - **Correction factor titration:** if corrections consistently overshoot (BG drops too much), widen CF (e.g., 1:30 → 1:40). If corrections undershoot, narrow CF.
   - **Patterned issues to look for:** dawn phenomenon (rising AM glucose despite adequate basal — increase basal or shift timing), Somogyi effect (nocturnal hypoglycemia followed by rebound morning hyperglycemia — reduce evening basal; harder to confirm without CGM), exercise-induced delayed hypoglycemia (often 6–12 h post-exercise → reduce subsequent basal or bolus).

6. **Address specific contexts.**
   - **Steroid-induced hyperglycemia (prednisone AM dose):** AM NPH dosed with steroid (peak aligns with steroid effect at ~6 h post-dose). For dexamethasone (24h duration), basal glargine. Add prandial coverage at largest meals.
   - **Hospital inpatient T2DM (NPO or eating):** basal-bolus (RABBIT-2 / RABBIT-2 Surgery) — TDD 0.4–0.5 u/kg/day, 50/50 split; correction-only sliding scale alone is inferior; avoid pure sliding scale.
   - **Hospital NPO:** continue basal at 50–80% of home dose; hold prandial; correction insulin q4–6h as needed; transition back when eating.
   - **ICU:** IV insulin infusion titrated to BG 140–180 (NICE-SUGAR — tighter control increased mortality).
   - **DKA transition:** start basal subq 1–2 h before stopping IV drip to avoid rebound DKA (IV insulin half-life ~5 min); 0.2–0.4 u/kg subq glargine or detemir for transition; add prandial when eating.
   - **CKD/ESRD:** reduce TDD by 25% at GFR 10–50, 50% at GFR <10; insulin clearance reduced — more hypoglycemia. Continue insulin on dialysis day; some patients need basal reduction.
   - **Hepatic impairment:** reduce TDD by 20–30%; gluconeogenesis impaired → less endogenous glucose; more hypoglycemia.
   - **Concurrent non-insulin therapy:** GLP-1 RA (semaglutide, dulaglutide, liraglutide) — reduce mealtime insulin 30–50% on initiation; SGLT2i (empagliflozin, dapagliflozin) — reduce basal 10–20%, monitor for euglycemic DKA in T1DM (off-label / cautious).
   - **Pregnancy:** rapidly escalating doses; tighter targets; avoid SGLT2i and GLP-1 RA; lispro / aspart / detemir / NPH are FDA category B for established safety; degludec less data but increasingly used.

7. **Pre-mortem the regimen for hypoglycemia and patient feasibility.**
   - Patients with hypoglycemia unawareness or recurrent severe hypoglycemia: loosen targets (A1c 7.5–8.0% or higher), use degludec (lowest nocturnal hypoglycemia), CGM with predictive low-glucose alerts.
   - Skipped meals: confirm prandial only with meals, not on standing schedule.
   - Variable schedule: prefer degludec (flexible timing) over glargine/detemir.
   - Cost: glargine U-100 has biosimilars (Basaglar, Semglee); 70/30 NPH-regular cheapest; degludec, U-300, GLP-1 RA expensive.
   - Self-management capability: assess injection technique, math comprehension, CGM literacy, social/financial supports.

## Output Format

```
PATIENT SNAPSHOT:
[Type, weight, GFR, A1c, current BG pattern, key context]

ESTIMATED TDD:
[Calculation: weight × units/kg/day, justification of multiplier]

STRATEGY:
[Basal-only / basal-plus / full basal-bolus / premixed / pump]

REGIMEN:
- Basal: [insulin name] [units] SC at [time]
- Prandial: [insulin name] [units (or ICR-based)] SC [time relative to meal]
- ICR: 1 unit per [X] g carb (computed from 500/TDD)
- CF: 1 unit drops BG by [Y] mg/dL (computed from 1800/TDD)
- Target BG: [pre-meal / bedtime / postprandial targets]

CALCULATION CHECK:
- TDD = [units]; basal = [units] (50% of TDD); prandial total = [units] (50% of TDD, split across [N] meals as [...] each)
- ICR sanity-check: typical meal of [X] g carb → [bolus units]
- CF sanity-check: BG of 250 with target 120 → correction = (250-120)/CF = [units]

MONITORING:
- BG checks: [frequency, timing]
- CGM if available: [time-in-range target ≥70%, TBR <4% goal]
- Labs / clinical: [HbA1c at 3 months, weight, BP, kidney function, hypoglycemia events]

TITRATION RULES:
- Adjust basal by [X units] every [Y days] if fasting BG persistently >[target] or <[target] (specify thresholds)
- Adjust ICR by [tightening/loosening] if persistent 2-h postprandial above/below target
- Sick-day rules: never stop basal insulin; check ketones; increase correction insulin

CONTEXT-SPECIFIC ADJUSTMENTS:
- [GFR / hepatic / steroid / pregnancy / hospital adjustments applied]

HYPOGLYCEMIA SAFETY:
- Hold prandial if BG <[threshold] / not eating
- Glucagon kit (auto-injector or nasal) for severe hypoglycemia at home
- Patient/family education on 15-15 rule
- Reassess in [N] weeks; reduce dose if [criteria]

WHY NOT [ALTERNATIVE STRATEGY]:
[E.g., premixed not chosen because flexibility needed; SGLT2i caution in T1DM]

FOLLOW-UP:
[Timing of follow-up, what data to bring, what to escalate]
```

## Worked Example

**Input:** 58-year-old man with T2DM ×12 years, weight 92 kg, GFR 64, A1c 10.4% on max metformin 1000 mg BID + glipizide 10 mg BID + empagliflozin 25 mg daily. Fingersticks: fasting 220–260, pre-dinner 260–320, occasional 1 postprandial readings 320. No documented hypoglycemia. Eats irregular meals due to work shifts. Initiate insulin.

**Output:**

```
PATIENT SNAPSHOT:
- T2DM ×12 y, weight 92 kg, GFR 64 (CKD stage 2), A1c 10.4%, on max metformin + glipizide + SGLT2i.
- Pattern: marked fasting (220–260) and pre-dinner (260–320) hyperglycemia; isolated postprandial spikes >300. No hypoglycemia; irregular shift-work meals.

CHOICE OF NEXT STEP:
- A1c 10.4% with persistent hyperglycemia across both fasting and prandial windows on triple oral → insulin indicated. Could also add GLP-1 RA (semaglutide), and many guidelines support GLP-1 RA before basal insulin for cardiometabolic benefit. Given patient preference, A1c 10.4%, and need for substantial glucose-lowering, initiate basal insulin while discussing GLP-1 RA addition next visit.
- Discontinue glipizide when basal insulin is initiated to reduce hypoglycemia (sulfonylurea + insulin together is a common cause of hospitalization). Continue metformin and SGLT2i (latter for cardiorenal benefit + modest A1c).

ESTIMATED TDD AND STRATEGY:
- Initial basal-only strategy (intensify to basal-plus if not at goal in 3 months).
- Starting basal dose: 10 units once daily (conservative initiation for outpatient T2DM) OR 0.2 u/kg = ~18 units. Use 0.2 u/kg = 18 units given high A1c and severe hyperglycemia.
- Choose degludec given irregular shift-work meal pattern (flexible timing day-to-day, ±8 h tolerated; lower nocturnal hypoglycemia than glargine).

REGIMEN:
- **Insulin degludec (Tresiba) 18 units SC once daily**, given at approximately the same time each day (±8 h flexibility tolerated). May start with bedtime dose if patient prefers; aim for consistent daily timing once established.
- Continue metformin 1000 mg PO BID.
- Continue empagliflozin 25 mg PO daily (monitor for euglycemic DKA when basal initiated and on SGLT2i; counsel sick-day rules).
- **Discontinue glipizide** when initiating basal insulin.

ICR / CF:
- Not yet — basal-only strategy. Will compute ICR / CF later if intensifying to prandial coverage. (At an expected TDD ~30–40 units once stable, projected ICR ~1:15 and CF ~1:50 if needed.)

TARGET BG:
- Fasting 80–130 mg/dL (ADA target).
- Pre-meal 80–130; bedtime 100–150.
- A1c target <7.0% (reasonable for this patient — not frail or very elderly).

MONITORING:
- Fingerstick checks: fasting AM daily, plus pre-dinner check 2–3 days per week, plus before any irregular long fast (shift work).
- Continuous Glucose Monitor (CGM) strongly recommended; check insurance / pharmacy benefit (Dexcom G7 / Freestyle Libre 3 — both covered for insulin-treated T2DM in most plans).
- Repeat A1c at 3 months.
- Renal function and electrolytes at 3 months.

TITRATION RULES (basal):
- Patient self-titrates: increase basal degludec by **2 units every 3 days** until fasting BG consistently 80–130.
- Hold or reduce by 4 units if any BG <70; immediately reassess.
- If fasting at goal but A1c remains >7% at 3 months, intensify with prandial rapid-acting insulin at largest meal (typically dinner) — basal-plus.
- If basal dose reaches 0.5 u/kg (~45 units) without achieving fasting goal, consider basal-plus or basal-bolus rather than continued basal escalation ("overbasalization").

CONTEXT-SPECIFIC NOTES:
- SGLT2i + insulin: counsel sick-day rules — hold SGLT2i during acute illness, prolonged fasting, surgery, low carb intake. Risk of euglycemic DKA. Always check urine ketones if symptomatic (nausea, malaise, dyspnea) regardless of BG.
- Shift work / irregular meals: degludec's day-to-day flexibility addresses inconsistent dosing time. If patient skips meals, basal-only minimizes hypoglycemia risk vs prandial regimen.
- Consider adding semaglutide 0.25 mg SC weekly (titrate up) at follow-up visit — cardiometabolic benefit, weight loss, improves glycemic control, allows lower insulin doses. (Or oral semaglutide if injectable refused.)

HYPOGLYCEMIA SAFETY:
- Discontinue glipizide as above (key to reducing hypoglycemia risk).
- Educate on hypoglycemia recognition and 15-15 rule (15 g rapid carbs, recheck in 15 min, repeat if BG <70).
- Glucagon nasal spray (Baqsimi) or autoinjector (Gvoke) prescription for backup at home and work.
- Carry glucose tabs.

WHY NOT [ALTERNATIVE]:
- Glargine U-100: reasonable; degludec preferred here because shift work introduces dose-timing variability, and degludec has lower nocturnal hypoglycemia.
- NPH BID: cheaper but more nocturnal hypoglycemia and less flexibility.
- Premixed 70/30: less precise titration; not a good fit for irregular meal pattern.
- Start prandial first: A1c 10.4% with fasting >200 indicates basal-first approach more efficient.

FOLLOW-UP:
- Phone or in-person check at 2 weeks to review fingerstick log and titration progress.
- Office visit in 6 weeks; full follow-up at 3 months with A1c.
- Bring: fingerstick log or CGM download, any hypoglycemia episodes, current weight, BP.
- Escalation triggers: severe hypoglycemia, recurrent BG <70, fasting BG persistently >180 despite titration to 0.5 u/kg, sick-day with positive ketones.
```
