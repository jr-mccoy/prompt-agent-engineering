---
title: PACU Cardiac Recovery Considerations (Population-Specialty Teaching)
category: pacu/population-specialty
task_type: LEARN
audience: PACU orientee or preceptor recovering post-cardiac / high-acuity cardiac-history patients (facility-dependent scope)
updated: "2026-07-07"
tags:
  - pacu
  - cardiac
  - high-acuity
  - population-specialty
  - hemodynamics
  - dysrhythmia
techniques:
  - ST-01
  - ST-02
  - RT-02
  - QA-02
  - ED-02
  - DS-06
difficulty: advanced
related_prompts:
  - pacu_dysrhythmia_recognition.md
  - pacu_post_op_hypertension.md
  - pacu_drug_vasopressors_reference.md
  - pacu_geriatric_considerations.md
  - pacu_topic_primer.md
  - pacu_complication_deep_dive.md
references:
  - Drain's PeriAnesthesia Nursing Practice (7th ed.) — cardiovascular chapters
  - ASPAN Standards of Perianesthesia Nursing Practice — cardiovascular domain
  - ASPAN Core Curriculum for PeriAnesthesia Nursing Practice — cardiovascular module
---

# PACU Cardiac Recovery Considerations

> Safety reminder: Cardiac recovery is scope-and-facility-dependent — some facilities recover open-heart / high-acuity cardiac cases in PACU, others route them to a dedicated CVICU. Do not assume a scope your unit and your competency-validation do not grant. Every drip, threshold, pacing setting, and hemodynamic target is per provider order and facility protocol; this teaching prompt states no doses, rates, or settings. Verify against current provider order and facility protocols. See `../SAFETY_PREAMBLE.md`.

## Objective

Produce a **cardiac-recovery-specific PACU considerations teaching artifact** — scoped to whichever of two realities matches the unit: (a) the facility recovers post-cardiac / high-acuity cardiac cases in PACU, or (b) the more common case, a **cardiac-history patient recovering from non-cardiac surgery in general PACU**. Covers hemodynamic lability, lines and monitoring awareness, rhythm surveillance, chest-tube/pacing awareness (where in scope), and the adult-PACU habits that under-monitor this population.

## When to use

- Orientation to a unit that recovers post-cardiac or high-acuity cardiac cases (facility-dependent).
- Recovering a **cardiac-history** patient (CAD, heart failure, valvular disease, arrhythmia, prior CABG/PCI, ICD/pacemaker) after non-cardiac surgery — the far more common scenario.
- Refresher on hemodynamic lability and rhythm surveillance before a cardiac-focused simulation.

## When not to use

- For general PACU orientation — use `pacu_topic_primer.md`.
- For a dysrhythmia once it appears — use `pacu_dysrhythmia_recognition.md`.
- For post-op hypertension as an event — use `pacu_post_op_hypertension.md`.
- For dedicated CVICU orientation or advanced hemodynamic-monitoring certification — those are separate programs; this prompt does not substitute for them.

## Inputs

- **Scope reality:** {{facility recovers post-cardiac/high-acuity cardiac cases in PACU | cardiac-history patient in general PACU after non-cardiac surgery}}
- **Cardiac history (if patient-in-general-PACU):** {{CAD/prior MI | heart failure | valvular disease | arrhythmia/AF | ICD or pacemaker | prior CABG/PCI | none stated}}
- **Monitoring in place:** {{standard PACU monitor | arterial line | central line | telemetry | temporary pacing | per order}}
- **Learner experience level:** {{Phase 1 orientee | experienced RN cross-training | ICU-background RN}}
- **Source chapters available:** {{Drain's cardiovascular chapters, ASPAN cardiovascular module, facility cardiac-recovery protocols}}

## Audience / Scope

- **Primary:** PACU nurse recovering a cardiac-history or (facility-dependent) post-cardiac patient.
- **Scope:** Differences from the default adult recovery for this population, bounded by the unit's validated scope. Not a CVICU curriculum; not advanced-hemodynamic-monitoring certification; not a substitute for facility cardiac-recovery protocols or provider orders.

## Output requirements

```markdown
# Cardiac PACU Considerations — {scope reality}

> Safety reminder: Recover only within your unit's validated scope. All drips, thresholds, pacing settings, and hemodynamic targets are per provider order and facility protocol. This population decompensates on a rhythm/pressure axis faster than a healthy adult — surveillance is closer and escalation is earlier.

## What's different from the default adult recovery (at a glance)
| Domain | Default adult PACU | Cardiac / cardiac-history difference |
|---|---|---|
| Hemodynamics | Pressure trends predictable, wide reserve | Labile pressure and rate; small changes tolerated poorly; targets per order |
| Rhythm | Occasional benign dysrhythmia | Higher arrhythmia risk; continuous telemetry per facility; new rhythm change is escalated early |
| Lines / access | Peripheral IV | Arterial and/or central lines may be present — know what each reads and its safety/zeroing/patency needs per facility |
| Fluids | Standard replacement | Narrow tolerance — over- or under-resuscitation both harmful; fluid targets per order |
| Devices | None | Possible ICD/pacemaker (history) or temporary epicardial pacing (post-cardiac, if in scope); chest tubes (post-cardiac, if in scope) |
| Medications | Standard | Vasoactive/antihypertensive agents by order; home cardiac meds held/resumed per order; anticoagulation status matters |
| Anticoagulation / bleeding | Routine watch | Bleeding and antiplatelet/anticoagulant status are load-bearing for the plan |
| Escalation threshold | Trend, then act | Lower threshold — a new rhythm, a sustained pressure change, or a rate change is escalated earlier |

## Hemodynamic lability — why adult "trend it" is too slow here
- **Narrow reserve:** a cardiac-history patient has less capacity to compensate for hypotension, hypertension, tachycardia, or hypovolemia. Changes that a healthy adult rides out can spiral here.
- **Rate and rhythm drive pressure:** new atrial fibrillation with rapid ventricular response, new bradycardia, or frequent ectopy can drop cardiac output quickly. Recognize and escalate — interpretation mastery is not the bar; recognition + escalation is. See `pacu_dysrhythmia_recognition.md`.
- **Pressure targets are per order** and often tighter than the general population (both a ceiling and a floor). Do not assume a general-population range.

## Lines and monitoring awareness (scope-safe)
- **Know what each line reads and what it needs.** Arterial line: continuous pressure + sampling access; requires zeroing/leveling and patency care per facility. Central line: access + (per facility) central pressures. Confirm your unit's competency scope for each.
- **A number is only as good as the setup.** A damped arterial waveform, an unleveled transducer, or a positional line produces misleading data — correlate with a cuff pressure and the patient before acting on a number.
- **Advanced monitoring interpretation and line manipulation are scope- and competency-bounded** — do only what your validation and facility policy authorize; escalate the rest.

## Rhythm surveillance
- **Continuous telemetry per facility** for this population; know your unit's baseline-and-change documentation expectation.
- **A new rhythm change is escalated early**, especially new AF/RVR, new bradycardia, sustained tachycardia, or increasing ectopy — pair the rhythm with the patient (pressure, symptoms, perfusion), not the monitor alone.
- **Reversible causes first:** hypoxia, pain, electrolyte derangement, hypovolemia, and hypercarbia drive many PACU dysrhythmias — hunt the cause while escalating. See `pacu_dysrhythmia_recognition.md`.

## Chest tubes & temporary pacing (only where in facility scope)
- **Chest tubes (post-cardiac, if your unit recovers these):** monitor output trend, character, and site per facility; a sudden change in output (a surge or an abrupt stop) is escalated. Specific management is per facility protocol and provider order.
- **Temporary epicardial pacing (if in scope):** settings (rate, output, sensitivity) are per order; the nurse monitors capture/sensing and escalates loss of capture — reprogramming is provider/authorized-role scope.
- **If your unit does not recover these devices, that is the correct scope** — this section is descriptive awareness, not a directive to take them on.

## Medications & anticoagulation (framing only — no doses)
- **Vasoactive and antihypertensive agents are per order** (see `pacu_drug_vasopressors_reference.md` for the ephedrine-vs-phenylephrine cause-first framing). No drip math here.
- **Home cardiac medications** (beta-blockers, antihypertensives, antiarrhythmics, anticoagulants) are held or resumed per order — surface the reconciliation, don't assume.
- **Anticoagulant / antiplatelet status is load-bearing** for bleeding risk and for line/drain management — know it and factor it into the surveillance plan.

## Common adult-PACU habits that miss in cardiac recovery
- **Trending a pressure or rate change across several cycles before acting.** Narrow reserve means earlier recognition and earlier escalation.
- **Reading the arterial-line number without checking the setup.** Level, zero, and correlate before you treat a number.
- **Treating a new rhythm as "probably nothing."** New AF/RVR or new bradycardia in this population changes output — escalate and hunt the reversible cause.
- **Applying a general-population blood-pressure range.** Targets are per order and often tighter, in both directions.
- **Overlooking anticoagulation status** when a line, drain, or bleeding question comes up.
- **Taking on a device or line outside validated scope.** Escalate; do not exceed competency validation.

## When to call (escalation by role)
- **Anesthesia / surgical or cardiac provider by role** for a new or sustained rhythm change, a pressure outside the ordered target, loss of pacing capture, a chest-tube output change (where in scope), or a device concern.
- **Rapid response / critical-care by role** for hemodynamic decompensation or a need for a higher level of monitoring/care than your unit provides.
- **Charge nurse** for staffing to support closer surveillance, a 1:1, or a level-of-care/transfer decision.
- **Cardiology / electrophysiology per facility** for ICD/pacemaker questions where that is the consulting path.

## Sources / reference
- *Drain's PeriAnesthesia Nursing*, cardiovascular chapters.
- ASPAN *Standards of Perianesthesia Nursing Practice* — cardiovascular domain.
- ASPAN *Core Curriculum for PeriAnesthesia Nursing Practice* — cardiovascular module.
- Facility cardiac-recovery, telemetry, arterial-line, and temporary-pacing protocols: {{per facility protocol}}.
- Facility scope-of-practice and competency-validation policy for cardiac recovery: {{per facility}}.
```

## Must / Must not

**Must:**
- Open by scoping to the unit's reality — post-cardiac recovery vs cardiac-history-in-general-PACU — and honor validated scope throughout.
- Distinguish explicitly from the default adult recovery.
- Center hemodynamic lability and the earlier-escalation threshold (narrow reserve).
- Frame line/monitoring awareness scope-safely (know what it reads and needs; interpretation/manipulation are competency-bounded).
- Cover rhythm surveillance with reversible-cause-first framing.
- Treat chest tubes and temporary pacing as descriptive awareness bounded by facility scope.
- Surface anticoagulation status as load-bearing.
- Name common adult-PACU habits that fail in this population.
- Cross-reference `pacu_dysrhythmia_recognition.md`, `pacu_post_op_hypertension.md`, and `pacu_drug_vasopressors_reference.md`.

**Must not:**
- State specific drip rates, doses, hemodynamic-target numbers, pacing settings, or chest-tube-output thresholds — all "per order" / "per facility."
- Fabricate arrhythmia incidence, decompensation timelines, or mortality statistics.
- Direct the nurse to manipulate lines, reprogram pacing, or interpret advanced hemodynamics beyond validated scope.
- Assume a facility recovers post-cardiac cases in PACU — scope is facility-defined.
- Invent facility-specific protocols, pager numbers, or rapid-response criteria.
- Reference race, religion, national origin, or other protected characteristics as clinical or performance signals.
- Include patient-identifying information.

## Quality signals

- The artifact is scoped to the unit's reality and never exceeds validated scope.
- Hemodynamic lability and the earlier-escalation threshold are explicit.
- Line/monitoring awareness is scope-safe (know-what-it-reads, not interpret-and-manipulate).
- Rhythm surveillance uses reversible-cause-first framing.
- Anticoagulation status is surfaced as load-bearing.
- At least three adult-PACU habits that fail in this population are named.

## Verification

Before returning, verify:

- [ ] Scope reality (post-cardiac vs cardiac-history-in-general-PACU) stated up front and honored throughout.
- [ ] Default-adult-vs-population contrast table present and covers hemodynamics, rhythm, lines, fluids, devices, anticoagulation.
- [ ] Hemodynamic lability + earlier-escalation threshold explicit.
- [ ] Line/monitoring awareness framed scope-safely.
- [ ] Rhythm surveillance with reversible-cause-first framing.
- [ ] Chest tubes / temporary pacing framed as facility-scope-bounded awareness.
- [ ] Anticoagulation status surfaced.
- [ ] All doses / rates / targets / settings are "per order" — no specific values.
- [ ] Common adult-PACU habits that fail are named explicitly.
- [ ] Escalation named by role.
- [ ] Cross-references to dysrhythmia, post-op HTN, and vasopressor prompts present.

## False-Positive Prevention

Do **not** fabricate:

- **No invented drip rates, doses, hemodynamic targets, pacing settings, or chest-tube-output thresholds.** Always "per order."
- **No invented arrhythmia incidence, decompensation timelines, or mortality statistics.**
- **No invented ASPAN section / Drain's chapter citations.** Mark `{{confirm}}` when unknown.
- **No invented facility cardiac-recovery protocols, pager numbers, or rapid-response criteria.**
- **No assumed facility scope** — whether PACU recovers post-cardiac cases is facility-defined.
- **No patient-identifying information.**
- **No protected-characteristic references** used as clinical or performance signals.
- **No scope-creep actions** — line manipulation, pacing reprogramming, and advanced hemodynamic interpretation remain competency-/provider-bounded.

## Worked Example

<details>
<summary>Example: "Common adult-PACU habits that miss in cardiac recovery" section for an RN recovering a cardiac-history patient after non-cardiac surgery (click to expand)</summary>

```markdown
## Common adult-PACU habits that miss in cardiac recovery

1. **Trending the rate before acting.** Your patient with prior CABG and known AF develops a rapid ventricular response with a falling pressure. Narrow reserve means you escalate now and hunt the reversible cause (pain, hypoxia, hypovolemia, electrolytes) at the same time — you don't wait three cycles.

2. **Reading the arterial-line number at face value.** Before you treat a low art-line pressure, check that the transducer is leveled and zeroed and correlate with a cuff — a positional or damped line lies.

3. **Calling a new rhythm "probably nothing."** New AF/RVR or new bradycardia in this population changes cardiac output; pair the rhythm with pressure, symptoms, and perfusion and escalate per protocol.

4. **Using a general-population BP range.** This patient's targets are per order — often a tighter window, top and bottom — because both extremes are poorly tolerated.

5. **Missing the anticoagulation picture.** On antiplatelet + anticoagulant therapy, bleeding risk and any line/drain question change — know the status before it becomes urgent.

6. **Reaching past your validated scope.** If a device, line, or interpretation is beyond your competency validation, escalate — that is the correct action, not a gap.
```

Notes: each habit names the adult default + the population correction; scope-appropriate (no line manipulation or pacing reprogramming); no specific rates, targets, or settings; cross-references to dysrhythmia and vasopressor references implied.
</details>

## Self-check

- [ ] Scope reality stated and honored (no assumed post-cardiac scope).
- [ ] Default-adult-vs-population contrast table present.
- [ ] Hemodynamic lability + earlier-escalation threshold explicit.
- [ ] Line/monitoring awareness scope-safe.
- [ ] Rhythm surveillance with reversible-cause-first framing.
- [ ] Chest tubes / pacing framed as facility-scope-bounded awareness.
- [ ] Anticoagulation status surfaced.
- [ ] All doses / rates / targets / settings "per order" — no specific values.
- [ ] Common adult-habit failures named.
- [ ] Escalation by role.
- [ ] Cross-references to dysrhythmia, post-op HTN, and vasopressor prompts.
- [ ] No invented statistics, timelines, or facility protocols.
- [ ] No patient-identifying information.
- [ ] No protected-characteristic references as signals.
- [ ] No scope-creep actions.
- [ ] Safety reminder at top.
- [ ] Verification section passed.
- [ ] False-Positive Prevention section passed.
