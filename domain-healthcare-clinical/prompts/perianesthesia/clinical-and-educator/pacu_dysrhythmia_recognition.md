---
title: PACU Dysrhythmia Recognition & Escalation
category: pacu/complications
task_type: LEARN
audience: PACU orientee (mid/late) or preceptor for huddle
updated: "2026-07-06"
tags:
  - pacu
  - dysrhythmia
  - cardiac
  - rhythm-recognition
  - escalation
techniques:
  - ST-01
  - ST-02
  - RT-02
  - QA-02
  - ED-02
  - DS-06
difficulty: intermediate
related_prompts:
  - pacu_complication_deep_dive.md
  - pacu_post_op_hypertension.md
  - pacu_hypothermia_shivering.md
  - pacu_red_flag_card.md
references:
  - Drain's PeriAnesthesia Nursing Practice (7th ed.) — cardiovascular chapters
  - ASPAN Standards of Perianesthesia Nursing Practice
  - ASPAN Core Curriculum for PeriAnesthesia Nursing Practice — cardiovascular module
  - ACLS (facility-required certification)
---

# Dysrhythmia Recognition & Escalation — PACU Deep Dive

> Safety reminder: This artifact builds recognition-and-escalation judgment, not independent rhythm-management authority. Treat the patient, not the monitor; hunt reversible causes; escalate. Antiarrhythmics and all pharmacology are per provider order / ACLS. This prompt states no doses. See `../SAFETY_PREAMBLE.md`.

## Objective

Produce a structured deep dive that helps the orientee (1) recognize the common PACU dysrhythmias, (2) distinguish stable from unstable, (3) hunt the reversible cause (most PACU dysrhythmias are secondary), and (4) escalate correctly — without pretending to teach full ECG mastery.

## Inputs

- **Monitoring/telemetry on your unit:** {{continuous 3/5-lead, spot 12-lead availability}}
- **Higher-risk patients:** {{cardiac history, electrolyte issues, long cases, older adults}}
- **Source chapters:** {{Drain's cardiovascular chapters, ASPAN Core Curriculum}}

## Audience

- Orientee weeks 4–10 building cardiac-monitoring judgment.
- Preceptor building a cardiovascular huddle.

## Output requirements

```markdown
# Dysrhythmia Recognition & Escalation — PACU Deep Dive

> Safety reminder: Treat the patient not the monitor; find the reversible cause; escalate. Pharmacology per order/ACLS.

## Why it matters
[One paragraph — many PACU rhythm changes are secondary to a correctable cause (pain, hypoxia, hypovolemia, electrolytes, hypothermia, meds); recognizing stable vs unstable and hunting the cause drives the response.]

## First principle: treat the patient, not the monitor
- Confirm it's real (artifact? lead? patient moving?) and assess the patient: consciousness, BP, perfusion, symptoms.
- Stable vs unstable (hypotension, chest pain, dyspnea, altered mentation, signs of shock) determines urgency.

## Common PACU rhythms (recognition + usual driver)
| Rhythm | Recognize | Common reversible driver to hunt |
|---|---|---|
| Sinus tachycardia | Fast, narrow, regular, P before each QRS | Pain, hypovolemia, hypoxia, fever, anxiety, meds |
| Sinus bradycardia | Slow, narrow, regular | Meds, vagal, neuraxial, hypoxia (late/ominous) |
| Atrial fibrillation ± RVR | Irregularly irregular, no clear P | Electrolytes, fluid shifts, cardiac history, pain/stress |
| PACs / PVCs | Early beats, wide (PVC) or early P (PAC) | Electrolytes, catecholamines, hypoxia, irritation |
| SVT | Fast, narrow, very regular | Re-entry; assess stability urgently |
| Ventricular tachycardia | Wide, fast | Emergency — assess stability, escalate/ACLS |

## Reversible-cause hunt (do this on any new rhythm)
- Oxygenation (SpO₂, work of breathing), pain, volume status/bleeding, electrolytes (labs if ordered), temperature, medications, bladder distension.

## Immediate management
1. Confirm rhythm is real; assess patient stability → reassess continuously.
2. Support oxygenation/perfusion; treat obvious reversible causes within scope (O₂ per order, pain per order, warm the patient) → reassess after each.
3. Obtain 12-lead if available/ordered; notify {provider by role} with rhythm + patient status → reassess after intervention.
4. If unstable or a dangerous rhythm (VT/SVT with instability): call rapid response / activate ACLS per facility; bring the code cart.

## Escalation
- Call {provider by role} for any new dysrhythmia, or a known rhythm now symptomatic/unstable.
- Rapid response / code + ACLS per facility for instability, VT, or arrest.

## Pharm / equipment likely used
- O₂, monitor/12-lead, code cart/defibrillator.
- Antiarrhythmics/other agents per order/ACLS (no dose here).

## After it resolves
- Continued monitoring; document rhythm, cause found, response → interval per facility/provider.
- Charting: rhythm, patient status, reversible causes checked, interventions, escalation.
- Handoff: rhythm event, cause, current status, telemetry needs.

## Teaching pearls
- Most PACU dysrhythmias are secondary — find the pain, hypoxia, volume, or electrolyte driver.
- The patient's stability, not the rhythm's name, sets the urgency.

## Common orientee mistakes
- Fixating on naming the rhythm instead of assessing the patient.
- Missing sinus tach as a sign of hypovolemia/bleeding or pain.

## Sources
- ...
```

## Must / Must not

**Must:**
- Lead with "treat the patient, not the monitor" and stable-vs-unstable.
- Frame most PACU dysrhythmias as secondary; include the reversible-cause hunt.
- Keep recognition practical; escalate/ACLS for instability.

**Must not:**
- No antiarrhythmic/other doses — "per order/ACLS."
- No invented rate cutoffs or ECG interval values.
- No scope creep — no nurse-initiated antiarrhythmic decisions; defibrillation/ACLS per certification/role.
- No facility-specific protocol/pager invented.

## Quality signals

- Orientee assesses the patient and hunts a cause before naming the rhythm.
- Orientee escalates on instability regardless of rhythm label.

## Verification

- [ ] "Treat the patient, not the monitor" leads.
- [ ] Stable-vs-unstable determination present.
- [ ] Common rhythms table pairs recognition with a reversible driver.
- [ ] Reversible-cause hunt present.
- [ ] Escalation by role + ACLS pathway for instability; no doses.

## False-Positive Prevention

Do **not** fabricate or invent:

- **No antiarrhythmic or other drug doses.** Per order/ACLS only.
- **No invented numeric rate cutoffs or ECG interval thresholds.** Describe qualitatively / per provider.
- **No invented facility telemetry/code criteria or pager paths.**
- **No fabricated chapter citations.** Mark `{{confirm}}`.
- **No scope creep** — advanced cardiac interventions per certification/role.

## Worked Example

<details>
<summary>Example: new sinus tachycardia — hunt the cause (click to expand)</summary>

```markdown
## Reversible-cause hunt (worked)

A post-op patient's monitor shows a new, fast, narrow, regular rhythm with a P before each QRS — sinus tachycardia. Before treating "tachycardia":

- Assess the patient: awake, BP trending down slightly, pale, incisional dressing with new bleeding.
- Hunt the driver: this looks like hypovolemia/pain, not a primary cardiac problem. Check the dressing/output, assess pain, apply O₂ per order.
- Notify the provider by role with rhythm + falling BP + bleeding findings; this may need volume and source control, not a rhythm drug.
```

Notes: patient assessed before rhythm treated; secondary cause (bleeding/hypovolemia) surfaced; escalation by role; no doses/cutoffs invented.
</details>

## Self-check

- [ ] Treat-the-patient framing leads.
- [ ] Stable vs unstable present.
- [ ] Rhythms paired with reversible drivers.
- [ ] Reversible-cause hunt + escalation by role/ACLS.
- [ ] No invented doses/cutoffs/facility specifics.
- [ ] Safety reminder at top.
- [ ] Verification + False-Positive Prevention passed.
