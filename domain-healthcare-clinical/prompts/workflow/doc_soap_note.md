---
title: "SOAP Progress Note"
category: domain-healthcare-clinical/workflow
description: "Generate a daily SOAP progress note from overnight events and current data — interval history, focused exam, and a problem-based assessment and plan."
techniques:
  - ST-02
  - ST-03
  - CM-01
  - RT-02
  - RT-05
difficulty: intermediate
tags:
  - documentation
  - soap-note
  - progress-note
  - clinical-notes
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

Produce a daily progress note in SOAP format that captures the interval change since the last note, the current objective data, and an updated problem-based assessment and plan. A good progress note shows movement — what changed overnight, how the patient responded, and what the plan does today — not a copy-forward of yesterday.

## Inputs

- Interval events since last note (overnight course, new symptoms, events, patient-reported status)
- Current vitals (including ranges/trends), I/O, relevant device settings (drips, O2, lines)
- Focused exam findings today
- New labs, imaging, micro, and study results since last note
- The active problem list and yesterday's plan
- Service/setting and day of admission

## Role

Treating clinician rounding and documenting the daily note that drives today's decisions.

## Reasoning Steps

1. **Subjective — capture the interval, not the whole history.** How did the patient do overnight, what are they reporting now, any new complaints, how is the target symptom trending (pain better, dyspnea resolved, still febrile). This is interval history, focused.

2. **Objective — current data with trends.** Vitals with overnight ranges (Tmax, BP range), not a single snapshot. I/O, weight if relevant, device settings. Focused exam on the systems in play. New results since the last note, with the meaningful ones called out.

3. **Assessment — a brief synthesis and updated problem framing.** One or two sentences on overall trajectory (improving, stable, worsening), then carry the problem list forward with status updates. Note resolved problems and any new ones.

4. **Plan — by problem, with today's specific actions.** For each active problem: where it stands and what changes today (continue, escalate, de-escalate, add, stop), with named drugs/doses. Avoid carrying forward a plan that no longer matches the data — if antibiotics can narrow, narrow them; if a drip can wean, say so.

5. **Update the housekeeping:** lines/tubes/drains (and whether any can come out), VTE prophylaxis, dispo trajectory, code status if changed. These prevent the most common omissions.

6. **Keep it current and honest.** Don't reproduce stale exam findings or a fully-negative ROS that wasn't reassessed. Document the day, not the template.

## False-Positive Prevention

❌ **DON'T:**
- Write patient-reported statements ("feels significantly better", "no dyspnea walking to the bathroom") when the input gives no patient report — S is the patient's voice, not an inference from improved vitals.
- Fill I/O, "devices: peripheral IV only" or a net-balance figure that today's input does not contain.
- Report Tmax equal to the current temperature unless the 24-hour maximum was supplied.
- Change an antibiotic course length or stop date from the previous plan without saying it changed and why.

✅ **DO:**
- Compute hospital day and antibiotic day from the admission and first-dose dates, not by adding one to yesterday's note.
- Back every "down", "improved" or "resolving" with two dated values (WBC 16.2 → 9.8); with only one value, report it without a trend word.
- Compare today's plan with yesterday's item by item — each continued, changed or stopped with a reason, none vanishing silently — and keep "no growth at 48 h" listed as pending until the culture is final.

## Output Format

```
[Service] Progress Note — Hospital Day [#]

S (Subjective):
[interval history, patient-reported status, new complaints, target-symptom trend]

O (Objective):
- Vitals: T [current/Tmax], HR [range], BP [range], RR, SpO2 [+support]
- I/O: [in/out], weight: [if relevant]
- Devices/Drips: [settings]
- Exam: [focused findings by system]
- New results: [labs/imaging/micro since last note, salient items interpreted]

A (Assessment):
[1–2 line trajectory], then:
# [Problem] — [status update]

P (Plan, by problem):
# [Problem 1]: [today's action — continue/change/add/stop + drug/dose]
# [Problem 2]: ...

Lines/tubes/drains: [status, removal candidates]
VTE prophylaxis: [...]
Dispo: [trajectory]
Code status: [...]
```

## Worked Example

**Input:** Hospital Day 3, CAP patient from prior example (on ceftriaxone + azithromycin, enoxaparin 40 mg SC daily; code status full, unchanged). Overnight: afebrile x24h, weaned to room air, cough improving (less frequent, less productive), ate breakfast. Patient says he feels "much better"; no dyspnea at rest or walking to the bathroom; no new complaints. T 36.9 this AM, Tmax 37.2, HR 78–88, BP 120s–130s/70s–80s, RR 16, SpO2 95% RA. I/O: net even, adequate urine output. Peripheral IV only, no drips. WBC down 16.2 → 9.8. Blood cultures no growth at 48h; sputum culture growing Strep pneumoniae sensitive to ceftriaxone. Glucose 140s–180s on sliding scale. Exam: comfortable, no distress; lungs improved air entry bilaterally, fewer right basilar crackles, no wheeze; heart RRR.

**Output:**

```
Medicine Progress Note — Hospital Day 3

S (Subjective):
Patient reports feeling "much better." Afebrile overnight, cough less frequent and less productive, no dyspnea at rest or with ambulation to the bathroom. Tolerated breakfast. No new complaints.

O (Objective):
- Vitals: T 36.9 (Tmax 37.2), HR 78–88, BP 120s–130s/70s–80s, RR 16, SpO2 95% on room air (weaned off O2).
- I/O: adequate urine output, net even.
- Devices/Drips: no drips; peripheral IV only.
- Exam: General — comfortable, no distress. Pulmonary — improved air entry bilaterally, fewer right basilar crackles, no wheeze. Cardiac — RRR.
- New results: WBC down 16.2 → 9.8 (resolving leukocytosis). Blood cultures no growth at 48h (not yet final — still pending). Sputum culture: Streptococcus pneumoniae, sensitive to ceftriaxone. Glucose 140s–180s on sliding scale.

A (Assessment):
68 y/o M with CAP, clinically improving — afebrile, off oxygen, downtrending WBC, culture-confirmed pneumococcal pneumonia sensitive to current therapy. On trajectory toward discharge.

P (Plan, by problem):
# Community-acquired pneumonia (S. pneumoniae): Clinically improving. Stop azithromycin (no atypical coverage needed given identified pathogen). Transition ceftriaxone IV → oral amoxicillin (or per sensitivities) to complete a 5–7 day total course given good response. Discharge when stable on oral therapy x24h, off oxygen (achieved).
# COPD: Continue tiotropium; PRN albuterol-ipratropium; no systemic steroids needed (no bronchospasm).
# Hyperglycemia/T2DM: Resume metformin now that acutely improving and eating; continue glucose monitoring; reduce sliding scale.
# HTN: Continue lisinopril, controlled.

Lines/tubes/drains: PIV — remove with IV-to-PO conversion.
VTE prophylaxis: Continue enoxaparin 40 mg SC daily; D/C with discharge once ambulatory.
Dispo: Anticipate discharge tomorrow on oral antibiotics with PCP follow-up in 1 week.
Code status: Full (unchanged).
```
