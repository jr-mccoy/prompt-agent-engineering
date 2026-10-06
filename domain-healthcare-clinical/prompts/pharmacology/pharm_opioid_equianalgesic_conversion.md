---
title: "Opioid Equianalgesic Conversion"
category: domain-healthcare-clinical/pharmacology
description: "Convert between opioid agents and routes using a structured equianalgesic table, apply incomplete cross-tolerance reductions, account for methadone's nonlinear conversion ratios, transdermal fentanyl bracketing, and breakthrough dosing; output a complete prescription with monitoring and naloxone counseling."
techniques:
  - ST-02
  - ST-03
  - CM-01
  - RT-02
  - RT-05
  - QA-01
difficulty: advanced
tags:
  - palliative-care
  - pain-management
  - opioids
  - dosing
  - safety
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

Convert a patient's opioid regimen safely between agents and/or routes. Compute morphine milligram equivalents (MME), apply incomplete-cross-tolerance reduction (typically 25–50%), respect methadone's nonlinear and dose-dependent conversion ratio, bracket transdermal fentanyl conversions, divide into appropriate scheduled and breakthrough doses, specify monitoring, and append naloxone counseling. Output is a complete prescription with rationale and self-check.

## Inputs

- Current opioid regimen (agent, dose, route, frequency; including PRN use over last 24–72 h)
- Reason for conversion (toxicity, opioid rotation for tolerance, change in route, transition to long-acting, hospice initiation, conversion at discharge)
- Patient context: age, renal/hepatic function, frailty, opioid-naive vs opioid-tolerant, prior intolerances or allergies, current sedatives (benzodiazepines, gabapentinoids, alcohol), prior overdose history, OUD history
- Goals: target pain rating (e.g., 4/10 at rest, tolerable with activity), function-based outcomes (sleep, ambulation, eating), tolerable side-effect threshold
- Setting: outpatient transition, inpatient titration, hospice / EOL

## Role

Senior palliative-care / pain-medicine physician writing the conversion order, applying incomplete cross-tolerance reduction, and verifying the calculation step by step.

## Reasoning Steps

1. **Compute total daily MME of current regimen.**
   - Standard equianalgesic table (oral morphine = 1× reference):
     - **Morphine PO**: 30 mg = baseline (factor 1.0)
     - **Morphine IV/SC**: 10 mg = 30 mg PO morphine (PO:IV ratio ~3:1)
     - **Oxycodone PO**: 20 mg ≈ 30 mg PO morphine (oxycodone:morphine ~1.5:1; oxycodone MME factor 1.5)
     - **Hydrocodone PO**: 30 mg ≈ 30 mg PO morphine (factor 1.0)
     - **Hydromorphone PO**: 7.5 mg ≈ 30 mg PO morphine (factor 4)
     - **Hydromorphone IV/SC**: 1.5 mg ≈ 30 mg PO morphine (factor 20)
     - **Oxymorphone PO**: 10 mg ≈ 30 mg PO morphine (factor 3)
     - **Tapentadol PO**: 75 mg ≈ 30 mg PO morphine (factor 0.4; conservative)
     - **Tramadol PO**: factor 0.1 in the CDC 2016 table (300 mg ≈ 30 mg PO morphine); the CDC 2022 guideline revised the factor upward (0.2) — name the source used (very rough; metabolism CYP2D6-dependent) [VERIFY: CDC 2022 Clinical Practice Guideline MME conversion table]
     - **Codeine PO**: 200 mg ≈ 30 mg PO morphine (factor 0.15; CYP2D6 ultra-rapid metabolizers convert more rapidly to morphine — pediatric warning)
     - **Fentanyl transdermal patch (µg/h)**: 25 µg/h patch ≈ 50–100 mg/day oral morphine (CDC table uses 25 µg/h = 60–134 MME/day, midpoint ~100; many use 25 µg/h ≈ 50 MME conservative; methods vary)
     - **Buprenorphine TD patch (Butrans 5 µg/h)**: 5 µg/h ≈ 10–15 mg/day oral morphine (conservative); buprenorphine has unique pharmacology (high-affinity partial agonist) — direct conversion is approximate and often replaced by induction protocols.
     - **Methadone PO**: dose-dependent ratio — see step 3.
   - Verify: sum components of regimen → total daily MME.

2. **Choose the new opioid, route, and frequency.**
   - Consider clearance (renal: avoid morphine metabolites M3G/M6G in CKD; prefer fentanyl, methadone, buprenorphine); hepatic (caution with methadone, oxycodone CYP3A4); allergy (rare true allergy; pseudo-allergic with morphine histamine release — use hydromorphone or fentanyl); tolerance pattern; cost; route availability (NPO, SC, IV, TD); pill burden.
   - Once converted, decide split: typically 60–70% as scheduled long-acting; 30–40% as breakthrough (immediate-release) divided into doses, each 10–20% of the 24h scheduled dose, available q3–4h prn for breakthrough.

3. **Apply incomplete cross-tolerance reduction.**
   - When changing opioids, reduce the calculated equianalgesic dose by **25–50%** to account for incomplete cross-tolerance.
     - 25% reduction: well-controlled pain, modest dose, comfortable conversion, escalating regimen.
     - 50% reduction: poorly controlled pain on current opioid (suggesting tolerance is non-uniform), high MME (>200 MME/day), older / frail / renal-hepatic compromise, or any concern for opioid-induced hyperalgesia.
   - Exception: **methadone** uses a dose-dependent ratio (see step 4) AND additional reduction; net reduction in many published algorithms is 75–90% from naive equianalgesic.

4. **Methadone conversion (nonlinear, requires extra caution).**
   - Methadone potency increases at higher background MME because of NMDA antagonism and accumulation; conversion ratio is dose-dependent:
     - **<60 MME/day morphine equivalent**: ratio morphine:methadone ≈ 4:1 (i.e., 60 mg morphine = 15 mg methadone)
     - **60–199 MME/day**: ratio ≈ 8:1
     - **200–499 MME/day**: ratio ≈ 12:1
     - **≥500 MME/day**: ratio ≈ 15:1 or more; methadone initiation in this range should be by an experienced clinician.
   - Then apply a *further* 25–50% reduction for incomplete cross-tolerance.
   - Start with low total daily dose typically not exceeding 30–40 mg/day in conversion regardless of computed dose; some protocols cap initial methadone at 30 mg/day for opioid-naive or modest conversion.
   - QTc baseline EKG before initiating methadone; repeat at steady state (5–7 days). Avoid concurrent QT-prolonging agents (ondansetron, fluoroquinolones, antipsychotics — at least be aware). Use TID dosing for analgesia (methadone t½ for analgesia 6–8 h despite plasma t½ 15–60 h).

5. **Transdermal fentanyl special considerations.**
   - Equianalgesic bracketing: use a range (e.g., 100 MME/day morphine ≈ 25–50 µg/h patch; CDC tables conservative; old "Janssen" tables more liberal). Pick the *lower* end for the conservative conversion, then titrate.
   - 12-hour delay to onset; do not stop prior opioid abruptly. Common bridge: keep previous immediate-release opioid available q3–4h prn for first 12–24 h, then titrate down as patch achieves steady state at 24–48 h.
   - Heat, fever, hot showers, exercise → increased absorption. Cachexia → reduced subcutaneous fat → variable absorption.
   - Removing the patch: reservoir in skin continues to release for 12–24 h; do not start another opioid at full conversion dose immediately on removal.

6. **Breakthrough dose calculation.**
   - Typical breakthrough = 10–20% of the total 24-h scheduled dose, prn q3–4h (oral) or q1–2h (IV/SC).
   - If chronic regimen plus frequent breakthrough use (>3 doses/day), recalculate and convert the breakthrough use into the scheduled long-acting dose.

7. **Verify the conversion calculation step by step.**
   - Step 1: total daily MME of current regimen (sum each component × factor).
   - Step 2: target opioid equianalgesic dose (divide MME by the new agent's factor).
   - Step 3: cross-tolerance reduction (multiply by 0.50–0.75).
   - Step 4: divide into scheduled + breakthrough doses; round to available product strength.
   - Sanity check: is the new MME plausibly less than the old? Is breakthrough <20% of scheduled? Are renal/hepatic adjustments incorporated? Is naloxone prescribed?

8. **Address adjuncts and safety.**
   - Co-prescribe naloxone (nasal 4 mg or 8 mg, or auto-injector) for anyone on ≥50 MME/day, anyone on concurrent benzodiazepine, anyone with prior overdose, or any patient receiving opioid for the first time at any reasonable dose (CDC, SAMHSA guidance).
   - Bowel regimen: senna 8.6 mg PO BID + PRN escalation; consider PAMORA (methylnaltrexone, naloxegol) if opioid-induced constipation refractory.
   - Antiemetic: prochlorperazine, metoclopramide, or ondansetron prn initially; tolerance typically develops in 3–5 days.
   - Sedation review: continue benzodiazepine only after explicit risk/benefit; consider taper.
   - Driving / operating machinery: counsel against during initial 5–7 days or after dose increase.
   - Follow-up: 1 week initially, then 2–4 week intervals; PDMP check, urine drug screen, function review.

## False-Positive Prevention

❌ **DON'T:**
- Mix conversion sources within one calculation (CDC MME factor for fentanyl, the label's patch table, the 2:1 rule) or take a factor from memory when the source revised it (tramadol 0.1 vs 0.2).
- Label the plan "25% cross-tolerance reduction" when the patch strength chosen actually delivers a much larger reduction.
- Choose the smaller reduction when this file's own 50% criteria (>200 MME/day, older age, renal impairment, sedation) are met, without saying why.
- Round to a patch strength without confirming that strength is stocked `[VERIFY: local formulary]`.

✅ **DO:**
- Recompute in `SELF-CHECK`: old MME, new scheduled MME, actual reduction = 1 − (new ÷ old); the stated percentage must match.
- Add up every opioid available at once during the bridge (scheduled patch plus all prn agents at their maximum frequency) and report the worst-case daily MME.
- Apply renal and hepatic dose reductions to the breakthrough agent at the supplied eGFR, not only to the scheduled agent.
- Write the conversion source and version beside each factor used so a pharmacist can re-derive the number.

## Output Format

```
CURRENT REGIMEN AND DAILY MME:
- [Agent 1] [dose] [route] [frequency] = [×factor] = [MME contribution]
- [Agent 2] [...] = [...]
TOTAL DAILY MME = [sum]

CONVERSION CALCULATION:
Step 1: total daily MME = [X]
Step 2: equianalgesic dose of new agent = [X / new agent factor] mg/day
Step 3: cross-tolerance reduction [25-50%]: [X × 0.5 or 0.75] = [Y] mg/day (new agent)
Step 4: split: scheduled long-acting = [Z] mg/day; breakthrough = [W] mg q[time] prn

NEW REGIMEN:
- Long-acting: [drug, dose, route, frequency] — total daily [Z] mg/day
- Breakthrough: [drug, dose, route, max frequency] — typically 10–20% of scheduled
- Adjuncts: [bowel regimen, antiemetic, naloxone]

DOSE-DEPENDENT CONSIDERATIONS (if methadone or fentanyl patch):
- [Methadone: applied ratio, EKG baseline, QTc check at steady state, dose cap]
- [Fentanyl patch: bracketed range, bridge plan for 12–24 h]

CROSS-TOLERANCE RATIONALE:
[Why 25% vs 50% reduction chosen for this patient]

MONITORING:
- Reassessment at [time]: pain score, function (sleep, ambulation, ADLs), side effects (constipation, sedation, mental status, respiratory rate), breakthrough use count
- Renal / hepatic labs as appropriate
- EKG for methadone

NALOXONE COUNSELING (REQUIRED if ≥50 MME/day, concurrent benzo, prior overdose, OUD risk):
- Naloxone nasal 4 mg, dispense 2; train patient and household contacts on use and CPR
- 911 call after administration; repeat dose if no response in 2–3 min

WHY NOT [ALTERNATIVE]:
[E.g., morphine avoided in CKD due to M3G/M6G accumulation; tramadol unreliable in CYP2D6 variability]

SELF-CHECK:
- New regimen total MME: [number] vs prior [number]
- Reduction applied: [Y%]
- Breakthrough is [W%] of scheduled (target 10–20%)
- Renal/hepatic dose adjustments [yes/no]
- Naloxone prescribed [yes/no]
- Bowel regimen prescribed [yes/no]
```

## Worked Example

**Input:** 74-year-old man with metastatic prostate cancer to bone, eGFR 38 mL/min, on oxycodone IR 20 mg PO q4h scheduled (6 doses/day = 120 mg/day) plus oxycodone IR 10 mg q3h prn (using 4 doses/day = 40 mg/day). Pain control inadequate, severe constipation, increasing somnolence. Convert to a long-acting regimen with appropriate adjustment for CKD; add breakthrough.

**Output:**

```
CURRENT REGIMEN AND DAILY MME:
- Oxycodone IR 20 mg PO q4h scheduled × 6 = 120 mg/day × 1.5 = 180 MME/day
- Oxycodone IR 10 mg PO q3h prn × 4 used/day = 40 mg/day × 1.5 = 60 MME/day
TOTAL DAILY MME = 240 MME/day

CHOICE OF NEW AGENT:
- Morphine PO: avoid given eGFR 38 (CKD stage 3b) — M3G and M6G accumulate, increased neurotoxicity and sedation.
- Hydromorphone: acceptable in CKD (metabolites less neurotoxic, though hydromorphone-3-glucuronide can accumulate); good option.
- Fentanyl TD patch: ideal for CKD (no active metabolites, hepatic metabolism); favorable for opioid rotation in renal disease and for tolerance.
- Methadone: also CKD-friendly but more complex; reserve for later if rotation needed; QTc, drug interactions, requires more clinical attention.
- Given chronic stable cancer pain, established tolerance, CKD, and quality-of-life goals at home: **fentanyl transdermal patch** + short-acting breakthrough is most appropriate.

CONVERSION CALCULATION:
Step 1: total daily MME = 240 MME/day.
Step 2: Convert to transdermal fentanyl using one conversion throughout — 100 MME/day ≈ 25 µg/h [VERIFY: fentanyl TD product-label conversion table; do not mix with other MME tables]. So 240 MME/day × 25/100 = 60 µg/h equianalgesic.
Step 3: Apply **50%** cross-tolerance reduction — this file's 50% criteria are met: >200 MME/day (240), age 74, renal impairment (eGFR 38), and poorly controlled pain with somnolence:
   - 60 µg/h × 0.5 = 30 µg/h → round down to the nearest standard strength (12, 25, 50, 75, 100 µg/h) given somnolence and CKD: **start 25 µg/h patch**.
   - Actual reduction (same conversion): 25 µg/h ≈ 100 MME/day → 1 − 100/240 ≈ 58% (50% planned; the extra comes from rounding down to an available strength).
Step 4: Breakthrough dose:
   - Scheduled ≈ 100 MME/day (same conversion as Step 2); 10–15% → ~10–15 MME.
   - In CKD, prefer **hydromorphone IR 2 mg PO q4h prn** (= 8 MME, ≈8% of scheduled — deliberately at/below the low end of the 10–20% band given somnolence, age and eGFR 38; increase if breakthrough relief is inadequate). Avoid morphine for metabolites; oxycodone could continue but rotation is the point.

NEW REGIMEN:
- **Fentanyl transdermal patch 25 µg/h, apply q72h** (rotate site, apply to hairless clean skin).
- **Hydromorphone IR 2 mg PO q4h prn** for breakthrough pain (max ~6 doses/day; reassess if needed >4 doses/day = recalculate scheduled).
- Bridge to patch onset: continue **oxycodone IR 10 mg PO q4h prn** for the first 24 hours after patch placement (fentanyl reaches steady state in ~24–48 h); then transition entirely to hydromorphone IR for breakthrough.

CROSS-TOLERANCE RATIONALE:
- 50% reduction applied (actual ≈58% after rounding to the 25 µg/h strength): baseline >200 MME/day, age 74, eGFR 38, and somnolence with poorly controlled pain all meet this file's 50% criteria; breakthrough use will guide upward titration.

MONITORING:
- Daily phone or home-visit check during first 3–5 days for somnolence, respiratory rate (target ≥10), pain score (target ≤4/10 rest, function-based for activity), constipation, nausea.
- Stop both opioids and call urgently if RR <8 or unresponsive.
- Reassess at 7 days: pain control, breakthrough utilization, side effects.
- Renal function recheck at 4 weeks.

ADJUNCTS:
- Bowel regimen: senna 8.6 mg PO BID + polyethylene glycol 17 g PO daily; escalate to bisacodyl 10 mg PO daily if needed. Consider methylnaltrexone 8–12 mg SC every 1–2 days if refractory (PAMORA).
- Antiemetic prn: prochlorperazine 5–10 mg PO q6h prn.
- Pruritus from opioids: low-dose loratadine; consider rotation if severe.

NALOXONE COUNSELING:
- Naloxone nasal 4 mg, dispense 2 sprays. Train patient and wife on use. Provide written instructions. Call 911 after administration. Repeat in 2–3 min if no response.

WHY NOT:
- Methadone: more complex conversion, QTc and drug interaction monitoring; reserve for inadequate response to fentanyl rotation.
- Morphine ER (MS Contin): M3G / M6G accumulation in CKD; avoid.
- Oxycodone ER (OxyContin): continued same drug class would not address tolerance buildup the rotation is trying to break.
- Buprenorphine TD: would require additional washout and induction; not the best fit for acute conversion of cancer pain at this MME.

SELF-CHECK:
- New scheduled regimen MME (fentanyl 25 µg/h ≈ 100 MME/day by the Step 2 conversion) vs prior 240 MME/day → actual reduction 1 − 100/240 ≈ 58%, matching the planned 50% plus rounding down. (Tables that put 25 µg/h as low as 60 MME/day would make this a 75% reduction — another reason to track breakthrough use and consider titrating to a higher patch strength at next visit.)
- Breakthrough hydromorphone 2 mg q4h prn = 12 mg/day max = 48 MME/day (at factor 4); if all doses used, total daily MME ~148. Still less than prior 240 — appropriate buffer for tolerance + side-effect resolution.
- Renal-friendly choices: fentanyl + hydromorphone (both acceptable in CKD).
- Naloxone prescribed: yes.
- Bowel regimen: yes (senna + PEG).
- EKG for methadone: not applicable (no methadone in regimen).
- Re-evaluation timing: 7-day follow-up.
```
