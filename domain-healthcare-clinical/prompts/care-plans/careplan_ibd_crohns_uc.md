---
title: "IBD (Crohn's / Ulcerative Colitis) Care Plan"
category: domain-healthcare-clinical/care-plans
description: "Build an inflammatory bowel disease management plan: risk-stratified induction and maintenance, biologic/small-molecule selection, treat-to-target monitoring, and health maintenance with named drugs."
techniques:
  - ST-02
  - ST-03
  - CM-01
  - RT-02
  - RT-05
  - DS-02
difficulty: advanced
tags:
  - gastroenterology
  - ibd
  - crohns
  - ulcerative-colitis
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

Produce an IBD care plan for Crohn's disease or ulcerative colitis: risk-stratify, select induction and maintenance therapy (including biologics/small molecules), set treat-to-target monitoring with objective endpoints, and install the IBD health-maintenance bundle. Output is an induction → maintenance plan with monitoring.

## Inputs

- Diagnosis: Crohn's (location/behavior — inflammatory/stricturing/penetrating, perianal) vs UC (extent — proctitis/left-sided/extensive; severity)
- Activity: symptoms, endoscopic/histologic findings, biomarkers (CRP, fecal calprotectin), imaging
- Risk factors for aggressive disease: young age at onset, extensive disease, deep ulcers, perianal/fistulizing, early steroid need, prior surgery
- Prior therapies and response, infections screen (TB, HBV) before biologics, vaccination status, malignancy history
- Comorbidities, pregnancy plans

## Role

Gastroenterologist managing IBD.

## Reasoning Steps

1. **Classify and risk-stratify.** High-risk features → early effective therapy (biologic/small molecule) rather than step-up delay ("top-down" for high-risk Crohn's).

2. **Ulcerative colitis:**
   - **Mild–moderate, distal:** topical (mesalamine suppository/enema) ± oral 5-ASA (mesalamine ≥2.4 g); optimize 5-ASA before escalating.
   - **Moderate–severe or 5-ASA-refractory:** biologic/small molecule — anti-TNF (infliximab, adalimumab), anti-integrin (vedolizumab, gut-selective), anti-IL12/23 (ustekinumab), or JAK inhibitor (tofacitinib, upadacitinib), or S1P modulator (ozanimod).
   - **Acute severe UC (hospitalized):** IV steroids; if no response by day 3–5 → infliximab or cyclosporine rescue; surgery if refractory.

3. **Crohn's disease:**
   - 5-ASA has limited efficacy; **don't rely on it** for moderate-severe Crohn's.
   - Biologics: anti-TNF (esp. fistulizing/perianal — infliximab), ustekinumab, vedolizumab, risankizumab; small molecule upadacitinib. Combine anti-TNF + immunomodulator (thiopurine/MTX) to reduce immunogenicity in selected patients.
   - Perianal/fistulizing: anti-TNF + surgical/abscess drainage + antibiotics.

4. **Limit corticosteroids** to induction only (budesonide for ileocecal Crohn's/mild UC; systemic for flares) — **not maintenance**; steroid dependence signals need to escalate maintenance therapy.

5. **Pre-biologic screening:** latent TB (IGRA/PPD), HBV serologies, vaccinations updated (live vaccines before immunosuppression), skin cancer counseling.

6. **Treat-to-target:** target is clinical remission + objective healing (normalized CRP/calprotectin, endoscopic/mucosal healing) — not symptoms alone. Proactively monitor biomarkers and reassess endoscopically; therapeutic drug monitoring for anti-TNF (trough/antibodies) to optimize/dose-escalate.

7. **Health maintenance:** colorectal cancer surveillance colonoscopy (dysplasia surveillance in long-standing colitis), bone health (steroid exposure), vaccinations (non-live), VTE awareness during flares, smoking cessation (Crohn's — smoking worsens; UC differs), nutrition/iron, mental health, dermatologic/ophthalmologic extraintestinal manifestations.

8. **Monitor:** symptoms + calprotectin/CRP, endoscopy at intervals, drug levels, infection surveillance, side effects.

## False-Positive Prevention

❌ **DON'T:**
- Describe extent and severity in free text — use Montreal location/behaviour (with perianal modifier) for Crohn's and Montreal extent plus a named activity score for UC (Mayo; Truelove-Witts for acute severe UC; HBI/CDAI for Crohn's), computed from the supplied findings.
- Carry a biologic dose from memory — check each infliximab induction and maintenance mg/kg and interval against the label for the indication, including the worked example's maintenance dose.
- Combine a thiopurine with anti-TNF in a young male without stating the hepatosplenic T-cell lymphoma consideration and the methotrexate alternative.
- Choose a JAK inhibitor or S1P modulator without its label sequencing and boxed-warning screen (prior TNF exposure where required, age, cardiovascular and VTE risk; conduction and macular checks for S1P).
- Read faecal calprotectin against another assay's cutoff, or call remission on a single value.

✅ **DO:**
- Before induction, verify each screen is a result, not an order: IGRA, HBsAg/anti-HBc/anti-HBs, varicella immunity, TPMT/NUDT15 before a thiopurine, pregnancy status before methotrexate.
- Give drug-level targets only from the reporting lab's ranges or tagged `[VERIFY: AGA therapeutic drug monitoring guidance]`, and record that each level is a trough.
- Compute the colorectal surveillance start date from the onset date and extent, and flag primary sclerosing cholangitis as surveillance-changing.
- Check every treat-to-target endpoint has a date and a measurement method before calling the monitoring plan complete.

## Output Format

```
DIAGNOSIS (CD location/behavior or UC extent/severity) / RISK STRATIFICATION:
ACTIVITY (symptoms + CRP/calprotectin + endoscopy):

INDUCTION:
- [agent, route, dose by disease + severity]

MAINTENANCE:
- [biologic/small molecule/immunomodulator selection + rationale]
- Steroid-sparing emphasis

PRE-BIOLOGIC SCREENING:
- TB, HBV, vaccines

TREAT-TO-TARGET MONITORING:
- Biomarker + endoscopic targets; therapeutic drug monitoring

HEALTH MAINTENANCE:
- CRC surveillance, bone, vaccines, smoking, nutrition, EIMs

PITFALLS:
- [5-ASA for moderate-severe Crohn's, steroids as maintenance, skipping TB/HBV screen, treating symptoms not targets]
```

## Worked Example

**Input:** 24 y/o M, newly diagnosed ileocolonic Crohn's, deep ulcers on colonoscopy, perianal fistula, CRP 45, calprotectin high, weight loss. High-risk features. TB IGRA negative, HBV non-immune, never treated.

**Output:**

```
DIAGNOSIS / RISK: ileocolonic Crohn's, stricturing/penetrating risk, perianal fistulizing — HIGH RISK (young, deep ulcers, perianal). Top-down therapy indicated.
ACTIVITY: active (CRP 45, high calprotectin, endoscopic deep ulcers, fistula).

INDUCTION:
- Anti-TNF: infliximab 5 mg/kg IV at weeks 0, 2, 6 — best evidence for perianal/fistulizing Crohn's.
- Coordinate surgical evaluation for the perianal fistula (exam under anesthesia / drainage of any abscess, seton) + antibiotics (ciprofloxacin/metronidazole).
- Short course systemic/budesonide only if needed for symptom bridge — induction, not maintenance.

MAINTENANCE:
- Continue infliximab maintenance (8 mg/kg q8w, dose-optimize by levels).
- Combine with an immunomodulator (thiopurine — after TPMT/NUDT15, or methotrexate) to reduce anti-drug antibodies and improve durability in this high-risk patient.
- No reliance on 5-ASA (ineffective for moderate-severe Crohn's).

PRE-BIOLOGIC SCREENING:
- TB IGRA negative — OK.
- HBV non-immune → vaccinate (and ensure not active before/with immunosuppression).
- Update non-live vaccines now; live vaccines before deeper immunosuppression if any due.

TREAT-TO-TARGET MONITORING:
- Target: clinical remission + CRP/calprotectin normalization + endoscopic healing + fistula response.
- Reassess calprotectin/CRP periodically; infliximab trough levels/antibodies to optimize; endoscopy in ~6–9 months.

HEALTH MAINTENANCE:
- Smoking cessation (worsens Crohn's), nutrition/iron, bone health if steroids used, mental health, monitor extraintestinal manifestations, future CRC surveillance for colonic involvement.

PITFALLS:
- Don't treat this with 5-ASA or steroids-as-maintenance — high-risk Crohn's needs early biologic.
- Address the perianal fistula surgically alongside the anti-TNF.
- Complete TB/HBV screening before/with biologic (done).
```
