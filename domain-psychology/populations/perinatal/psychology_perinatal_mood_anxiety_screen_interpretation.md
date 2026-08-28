---
title: "Perinatal Mood and Anxiety Screen Interpretation (EPDS / PHQ-9 / GAD-7)"
category: psychology/populations/perinatal
description: "Interpret perinatal depression and anxiety screens (EPDS, PHQ-9, GAD-7) with population-appropriate cutoffs, the EPDS item-10 self-harm flag, and a structured disposition pathway."
techniques:
  - ST-04
  - RT-02
  - DT-02
  - QA-04
  - CM-02
difficulty: intermediate
intended_use: model-testing
tags:
  - perinatal
  - postpartum
  - EPDS
  - PHQ-9
  - GAD-7
  - screening
  - PMAD
  - suicide-risk
  - pregnancy
  - lactation
updated: "2026-06-08"
related_prompts:
  - domain-psychology/populations/perinatal/psychology_perinatal_options_pregnancy_lactation.md
  - domain-psychology/populations/perinatal/psychology_postpartum_psychosis_referral.md
  - domain-psychology/risk-crisis/psychology_columbia_suicide_risk_assessment.md
  - domain-psychology/documentation/psychology_intake_assessment_note.md
---

# Perinatal Mood and Anxiety Screen Interpretation (EPDS / PHQ-9 / GAD-7)

## Objective

Interpret validated screening instruments for perinatal mood and anxiety disorders (PMADs) in a pregnant or postpartum patient and produce a structured interpretation note that:

1. Applies population-appropriate cutoffs for the Edinburgh Postnatal Depression Scale (EPDS), PHQ-9, and GAD-7.
2. Treats EPDS item 10 (self-harm thoughts) as a mandatory standalone risk flag regardless of total score.
3. Distinguishes anxiety-predominant presentations (the EPDS over-indexes anxiety items 3–5) from depression-predominant presentations.
4. Differentiates normative perinatal adjustment ("baby blues") from a clinically significant disorder.
5. Routes the patient to a disposition tier with an explicit follow-up interval.
6. Flags presentations requiring same-day risk assessment or escalation.

## When to Use

- Universal screening visits during pregnancy and postpartum (ACOG/USPSTF-aligned perinatal depression screening).
- Postpartum well-child or maternal visits where an EPDS or PHQ-9 was administered.
- Interpreting a positive or borderline screen forwarded by an OB, midwife, pediatrician, or home-visiting nurse.
- Re-screening a patient with a prior positive screen to assess trajectory.

## When NOT to Use

- For acute psychosis, delirium, or rapidly waxing/waning sensorium: use `psychology_postpartum_psychosis_referral.md` — postpartum psychosis is a psychiatric emergency, not a screening interpretation.
- For full medication/therapy treatment planning across pregnancy and lactation: use `psychology_perinatal_options_pregnancy_lactation.md`.
- For a completed suicide risk formulation when item 10 is positive: escalate to `domain-psychology/risk-crisis/psychology_columbia_suicide_risk_assessment.md`.
- For non-perinatal adult depression/anxiety screening (general PHQ-9/GAD-7 cutoffs apply without perinatal calibration).

## Inputs / Context Required

- **Patient and timing:** Initials/MRN, perinatal stage (trimester / weeks postpartum), parity, delivery date if postpartum.
- **Instrument(s) administered:** EPDS, PHQ-9, GAD-7 — total scores, subscale/item data where available, and date administered.
- **EPDS item 10 response** (self-harm thoughts): explicit value (0–3). This is required — do not interpret an EPDS without it.
- **Clinical context:** Sleep deprivation level, feeding method, prior psychiatric history, prior PMAD, current symptoms in patient's words.
- **Safety baseline:** Any current suicidal ideation, infant-directed intrusive thoughts, prior attempts, access to means.
- `[clinician input required: prior history of bipolar disorder or postpartum psychosis — a positive bipolar history changes the screening pathway and contraindicates unopposed antidepressant initiation]`

## Constraints

### Must

- Apply EPDS cutoffs explicitly: total **≥10** = possible depression / further evaluation; total **≥13** = probable major depression (higher specificity threshold). State which cutoff is being used and why.
- Treat **EPDS item 10 ≥1** as a positive self-harm flag that triggers same-session risk assessment regardless of total score (a patient can score low overall and still endorse item 10).
- Interpret the EPDS anxiety cluster (items 3, 4, 5) when elevated; note anxiety-predominant presentation even when the depression threshold is not met.
- Apply PHQ-9 severity bands (5–9 mild, 10–14 moderate, 15–19 moderately severe, 20–27 severe) and treat PHQ-9 **item 9 ≥1** as a standalone suicide flag.
- Apply GAD-7 severity bands (5–9 mild, 10–14 moderate, ≥15 severe).
- Distinguish normative "baby blues" (onset days 2–5, peaks ~day 5, resolves by ~2 weeks, no functional impairment) from a screen-positive disorder (persistent ≥2 weeks, functional impairment).
- Assign a disposition tier with a concrete follow-up interval.
- Screen, in every interpretation, for bipolar history before recommending antidepressant initiation (route that recommendation to the treatment-options prompt).
- Flag all `[clinician input required: ...]` gaps; do not fabricate scores or item-level data.

### Must Not

- Do not interpret an EPDS total without the item-10 value.
- Do not treat a sub-threshold total as "negative" when item 9 (PHQ-9) or item 10 (EPDS) is positive.
- Do not reproduce copyrighted instrument item text; reference items by number and construct only.
- Do not diagnose bipolar disorder, MDD, or an anxiety disorder from a screen alone — screens stratify risk and trigger evaluation; they do not diagnose.
- Do not recommend a specific medication or characterize drug safety here — route to the treatment-options prompt.
- Do not minimize anxiety-predominant or OCD-spectrum (intrusive-thought) presentations because the depression total is low.

## EPDS Cutoff and Interpretation Table

| EPDS Total | Interpretation | Action |
|------------|----------------|--------|
| 0–9 | Below screening threshold | Routine re-screen per schedule; reassess if clinical concern. Still check item 10. |
| 10–12 | Possible depression (sensitive threshold) | Clinical evaluation; brief follow-up interval; consider PHQ-9 to corroborate. |
| ≥13 | Probable major depression (specific threshold) | Diagnostic evaluation; treatment planning; structured follow-up. |
| Item 10 ≥1 (any total) | Self-harm thoughts endorsed | **Same-session suicide risk assessment regardless of total.** |
| Items 3–5 elevated (anxiety cluster) | Anxiety-predominant presentation | Corroborate with GAD-7; note even if depression threshold not met. |

## Instructions

1. **Confirm timing and instrument provenance.** Record perinatal stage and the date each instrument was administered. Distinguish antenatal vs. postpartum interpretation.

2. **Capture the item-10 / item-9 flags first.** Before computing totals, record EPDS item 10 and PHQ-9 item 9. If either is ≥1, mark the interpretation as requiring same-session risk assessment.

3. **Apply EPDS cutoffs.** State whether the ≥10 (sensitive) or ≥13 (specific) threshold is being applied and the rationale (e.g., universal screening favors ≥10 sensitivity).

4. **Evaluate the anxiety cluster.** Inspect EPDS items 3–5 and corroborate with GAD-7. Note anxiety-predominant presentation, including perinatal OCD-spectrum intrusive thoughts, even when the depression total is sub-threshold.

5. **Apply PHQ-9 and GAD-7 bands.** Record severity bands and any incongruence between instruments (e.g., low EPDS, elevated GAD-7).

6. **Differentiate baby blues from a disorder.** Apply the onset/duration/impairment criteria.

7. **Bipolar screen.** Confirm whether any history of bipolar disorder, prior postpartum psychosis, or antidepressant-induced activation exists before any treatment routing.

8. **Assign disposition tier and follow-up interval** using the output template.

9. **Run verification.**

## Output Format

```
=== PERINATAL MOOD/ANXIETY SCREEN INTERPRETATION ===

Patient: [Initials/MRN]    Date: [YYYY-MM-DD]
Perinatal stage: [Trimester N / N weeks postpartum]    Parity: [G_P_]    Delivery date: [YYYY-MM-DD / N/A]
Feeding method: [Breast / Formula / Mixed / N/A]    Sleep: [Hours/24h; fragmentation]

─────────────────────────────────────────
SCREEN RESULTS
─────────────────────────────────────────
EPDS total: [N/30]    Cutoff applied: [≥10 sensitive / ≥13 specific — rationale]
  EPDS item 10 (self-harm thoughts): [0/1/2/3]  → Flag: [POSITIVE — same-session risk assessment / Negative]
  EPDS anxiety cluster (items 3–5): [Elevated — describe / Not elevated]
PHQ-9 total: [N/27]    Severity band: [None / Mild / Moderate / Mod-severe / Severe]
  PHQ-9 item 9 (death/self-harm): [0/1/2/3]  → Flag: [POSITIVE / Negative]
GAD-7 total: [N/21]    Severity band: [Minimal / Mild / Moderate / Severe]

Instrument congruence: [Concordant / Discordant — describe, e.g., low EPDS but GAD-7 = 16]
Presentation type: [Depression-predominant / Anxiety-predominant / Mixed / Intrusive-thought (OCD-spectrum) prominent]

─────────────────────────────────────────
NORMATIVE vs CLINICAL DIFFERENTIATION
─────────────────────────────────────────
Baby blues criteria (onset days 2–5, resolves ≤2 wks, no impairment): [Consistent / Inconsistent]
Duration of symptoms: [N days/weeks]
Functional impairment: [None / Mild / Moderate / Severe — domains: self-care / infant care / relationships]
Determination: [Likely normative adjustment / Screen-positive PMAD requiring evaluation]

─────────────────────────────────────────
RISK FLAGS / SAFETY
─────────────────────────────────────────
Self-harm flag triggered (EPDS-10 or PHQ-9-9 ≥1): [Yes — risk assessment initiated / No]
Suicidal ideation (current): [Absent / Passive / Active — plan / intent / means]
Infant-directed intrusive thoughts: [Absent / Present — ego-dystonic (distressing, unwanted) vs ego-syntonic — describe]
  [Note: ego-syntonic infant-harm ideation, command quality, or psychotic features → escalate to postpartum psychosis prompt]
Prior attempts / prior PMAD / prior postpartum psychosis: [...]
Risk-reassessment hook: [Re-administer EPDS + C-SSRS at: ____; sooner if symptoms escalate]

─────────────────────────────────────────
BIPOLAR / PSYCHOSIS SCREEN (pre-treatment routing)
─────────────────────────────────────────
History of bipolar disorder or manic/hypomanic episodes: [Yes / No / Unknown — [clinician input required]]
Prior postpartum psychosis (personal or first-degree relative): [Yes / No / Unknown]
  [If yes → do NOT route to unopposed antidepressant initiation; flag for psychiatric evaluation]

─────────────────────────────────────────
DISPOSITION
─────────────────────────────────────────
Tier: [
  Tier 0 — Below threshold: routine re-screen [interval]
  Tier 1 — Mild / possible: brief intervention + re-screen in [1–4 wks]
  Tier 2 — Moderate / probable MDD or anxiety: diagnostic evaluation + treatment planning (route to treatment-options prompt)
  Tier 3 — Severe or any positive self-harm flag: same-session risk assessment; urgent psychiatric linkage
  Tier 4 — Psychotic features / waxing-waning sensorium / command ideation: EMERGENCY → postpartum psychosis prompt
]
Follow-up interval: [Concrete date/interval]
Referrals: [Psychiatry / therapy / lactation / OB / crisis line 988 / PSI HelpLine 1-833-852-6262]
Routed to: [psychology_perinatal_options_pregnancy_lactation.md / C-SSRS / postpartum psychosis prompt — as applicable]

─────────────────────────────────────────
BILLING NOTE
─────────────────────────────────────────
Screening administration: [96127 (brief emotional/behavioral assessment, per instrument)]
If interpretation occurs within an E/M or psychotherapy encounter, bundle per encounter rules.
[clinician input required: payer-specific perinatal screening coverage]
```

## Verification

- [ ] Perinatal stage and administration date recorded for each instrument.
- [ ] EPDS item 10 value captured; item-10 ≥1 triggers same-session risk assessment regardless of total.
- [ ] PHQ-9 item 9 captured; ≥1 triggers standalone suicide flag.
- [ ] EPDS cutoff stated explicitly (≥10 sensitive vs ≥13 specific) with rationale.
- [ ] Anxiety cluster (EPDS items 3–5) and GAD-7 evaluated; anxiety-predominant presentation noted even if depression total sub-threshold.
- [ ] Baby blues vs. clinical PMAD differentiated using onset/duration/impairment.
- [ ] Intrusive infant-directed thoughts assessed and characterized (ego-dystonic vs ego-syntonic); psychotic features route to emergency prompt.
- [ ] Bipolar/postpartum-psychosis history screened before any treatment routing.
- [ ] Disposition tier assigned with concrete follow-up interval.
- [ ] Risk-reassessment hook specified.
- [ ] No copyrighted item text reproduced; items referenced by number/construct only.
- [ ] No fabricated scores or item-level data; gaps flagged with `[clinician input required: ...]`.
