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
updated: "2026-06-19"
---

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

**Input:** Hospital Day 3, CAP patient from prior example. Overnight: afebrile x24h, weaned to room air, cough improving, ate breakfast. Tmax 37.2, HR 78–88, BP 120s–130s/70s–80s, RR 16, SpO2 95% RA. WBC down 16.2 → 9.8. Blood cultures no growth at 48h; sputum culture growing Strep pneumoniae sensitive to ceftriaxone. Glucose 140s–180s on sliding scale. Exam: lungs improved air entry, fewer crackles.

**Output:**

```
Medicine Progress Note — Hospital Day 3

S (Subjective):
Patient reports feeling significantly better. Afebrile overnight, cough less frequent and less productive, no dyspnea at rest or with ambulation to the bathroom. Tolerated breakfast. No new complaints.

O (Objective):
- Vitals: T 37.2 (Tmax 37.2), HR 78–88, BP 120s–130s/70s–80s, RR 16, SpO2 95% on room air (weaned off O2).
- I/O: adequate urine output, net even.
- Devices/Drips: none; peripheral IV only.
- Exam: General — comfortable, no distress. Pulmonary — improved air entry bilaterally, fewer right basilar crackles, no wheeze. Cardiac — RRR.
- New results: WBC down 16.2 → 9.8 (resolving leukocytosis). Blood cultures no growth at 48h. Sputum culture: Streptococcus pneumoniae, sensitive to ceftriaxone. Glucose 140s–180s on sliding scale.

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
Code status: Full.
```
