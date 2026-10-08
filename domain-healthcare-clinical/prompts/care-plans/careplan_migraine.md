---
title: "Migraine Longitudinal Care Plan"
category: domain-healthcare-clinical/care-plans
description: "Build a migraine management plan: acute therapy by severity, preventive selection by comorbidity, CGRP therapies, and medication-overuse avoidance with named drugs and doses."
techniques:
  - ST-02
  - ST-03
  - CM-01
  - RT-02
  - RT-05
  - DS-02
difficulty: intermediate
tags:
  - neurology
  - migraine
  - headache
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

Produce a migraine care plan: optimize acute (abortive) therapy, decide on and select preventive therapy by comorbidity, integrate CGRP-targeted agents, and prevent medication-overuse headache. Output is an acute + preventive regimen with a headache-diary monitoring plan.

## Inputs

- Headache pattern: frequency (days/month), severity, aura, duration, disability (MIDAS/HIT-6), chronic (≥15 days/month) vs episodic
- Current treatments: acute agents and frequency of use (overuse risk), prior preventives (agent, dose, duration, response)
- Comorbidities: hypertension, depression/anxiety, obesity, epilepsy, cardiovascular/vascular disease (triptan caution), pregnancy plans
- Triggers, sleep, caffeine, analgesic use days/week

## Role

Neurologist or primary care attending managing migraine.

## Reasoning Steps

1. **Characterize** episodic vs chronic; quantify monthly headache days and acute-medication days (medication-overuse threshold: triptans/combination/opioids ≥10 days/month, simple analgesics ≥15).

2. **Acute therapy — treat early, match to severity:**
   - Mild–moderate: NSAID (naproxen, ibuprofen) or acetaminophen.
   - Moderate–severe: triptan (sumatriptan 50–100 mg, rizatriptan, eletriptan); add NSAID for efficacy. **Triptans contraindicated in CAD/stroke/uncontrolled HTN/hemiplegic or basilar migraine** → use gepant (ubrogepant, rimegepant) or lasmiditan instead.
   - Antiemetic (metoclopramide, prochlorperazine) for nausea/adjunct.
   - Limit acute use to ≤2 days/week to avoid medication-overuse headache.

3. **Decide on prevention** if ≥4 headache days/month with disability, ≥2 days/week acute use, or chronic migraine.

4. **Preventive selection by comorbidity:**
   - Hypertension → beta-blocker (propranolol, metoprolol) or candesartan.
   - Depression/insomnia/tension overlap → amitriptyline or venlafaxine.
   - Obesity/weight concern, epilepsy → topiramate (weight-neutral/loss; teratogenic — counsel). Avoid valproate in pregnancy-capable patients.
   - Start low, titrate, give an adequate 8-week trial at target dose before judging.

5. **CGRP-targeted prevention:** monoclonal antibodies (erenumab, fremanezumab, galcanezumab, eptinezumab) or oral gepants (atogepant, rimegepant) — for inadequate response/intolerance to oral preventives (often after ≥2 failures, payer-dependent); effective in chronic migraine.

6. **Chronic migraine:** onabotulinumtoxinA (Botox) every 12 weeks is evidence-based; CGRP agents also indicated.

7. **Medication-overuse headache:** identify and treat by withdrawing the overused acute agent and bridging with a preventive; expect transient worsening.

8. **Lifestyle/trigger management:** regular sleep, hydration, meals, consistent caffeine, exercise, stress management, trigger diary; treat comorbid depression/anxiety/OSA.

9. **Monitor:** headache diary (days/month, acute-med days), preventive response at 8–12 weeks, side effects, overuse pattern.

## False-Positive Prevention

❌ **DON'T:**
- Write "episodic" or "chronic" from the monthly headache-day count alone — ICHD-3 chronic migraine also needs >3 months of that pattern and ≥8 days/month with migraine features; if the input lacks duration or migraine-day counts, write `[ICHD-3 class incomplete — need 3-month diary]`.
- Clear medication overuse because each drug class sits under its own cutoff — triptan days and NSAID days taken on *different* days add up, and ≥10 combined days/month across more than one class meets the overuse criterion `[VERIFY: ICHD-3 8.2]`.
- Choose the preventive "by comorbidity" and miss the contraindication the same patient carries: propranolol with asthma, candesartan/valproate/topiramate without effective contraception, amitriptyline in an older adult with conduction disease.
- Tick "contraception counselled" for topiramate when the method is an estrogen-containing pill — at higher doses topiramate can reduce hormonal-contraceptive efficacy `[VERIFY: current label]`.
- Fill gepant or CGRP-antibody dose slots from memory — rimegepant has separate acute and every-other-day preventive regimens and eptinezumab is an IV infusion; use the clinician's order or `[VERIFY: current label]`.

✅ **DO:**
- Convert every frequency in the input to days/month and show it (e.g., "triptan ~3 days/week ≈ 13 days/month") before stating overuse status; compare that number with the threshold for the class actually used, not with the "≤2 days/week" counselling cap.
- List each prior preventive as agent / dose reached / weeks at that dose / outcome, and count it as a "failure" toward CGRP payer criteria only when all four fields are in the input; otherwise label it "trial adequacy unknown".
- Name the vascular history the triptan decision rests on (CAD, stroke/TIA, BP value, aura type) as found in the input; if a field is missing, say so instead of writing "no vascular contraindication".
- Tie each teratogenic preventive line to the pregnancy-plan and contraception fields in the input, and write the stop-before-conception step into MONITORING.

## Output Format

```
PATTERN: episodic vs chronic; headache days/mo; acute-med days/mo; disability (MIDAS/HIT-6)

ACUTE THERAPY:
- By severity: [NSAID / triptan or gepant/lasmiditan if vascular contraindication / antiemetic]
- Use-frequency cap

PREVENTION DECISION + AGENT:
- [oral preventive by comorbidity, dose, titration, 8-wk trial]
- CGRP mAb/gepant criteria
- Botox if chronic

MEDICATION-OVERUSE PLAN (if applicable):

LIFESTYLE / TRIGGERS:

MONITORING:
- Headache diary, response timing, side effects

PITFALLS:
- [triptan in vascular disease, medication-overuse headache, judging preventive too early, valproate/topiramate in pregnancy]
```

## Worked Example

**Input:** 35 y/o F, migraine without aura, 10 headache days/month, severe, MIDAS high disability. Uses sumatriptan ~3 days/week + ibuprofen. No vascular disease. Comorbid obesity (BMI 32) and mild depression. No prior preventive. Plans pregnancy "eventually, not now," reliable contraception.

**Output:**

```
PATTERN: episodic (10 days/mo, high disability). Triptan use ~3 days/week ≈ 13 days/month — already at the triptan overuse threshold (≥10 days/month). Note 13 triptan days exceeds the 10 headache days reported — reconcile with a diary.

ACUTE THERAPY:
- Continue sumatriptan 100 mg (no vascular contraindication) + naproxen for severe attacks; treat early.
- Cap acute use at ≤2 days/week — current 3 days/week risks medication-overuse headache; the preventive should reduce this.
- Antiemetic (metoclopramide) PRN for nausea.

PREVENTION DECISION + AGENT:
- Indicated (10 days/mo + disability + frequent acute use).
- Topiramate 25 mg qhs, titrate by 25 mg/week to ~100 mg/day — favorable in obesity (weight-neutral/loss). Counsel teratogenicity → reliable contraception (she has it); revisit before conception.
- Alternative if topiramate poorly tolerated: amitriptyline (also helps depression/sleep) or venlafaxine (covers depression).
- Give an 8-week trial at target dose before judging.
- If ≥2 oral preventives fail/intolerable → CGRP mAb (e.g., galcanezumab) or atogepant.

MEDICATION-OVERUSE PLAN: triptan days already meet the overuse threshold — bring them below it as the preventive takes effect; if MOH is diagnosed, withdraw overused agent and bridge with the preventive.

LIFESTYLE / TRIGGERS: regular sleep/meals/hydration, consistent caffeine, exercise, trigger diary; treat depression (the chosen preventive can do double duty).

MONITORING: headache diary (days/mo + acute-med days), preventive response at 8–12 weeks, topiramate side effects (cognitive, paresthesias, stones).

PITFALLS:
- Pre-conception: plan off topiramate/valproate before pregnancy.
- Don't judge topiramate a failure before 8 weeks at target dose.
- Drive acute-med days below the overuse threshold.
```
