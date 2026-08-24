---
title: PACU Ambulatory & Day-Surgery Considerations (Population-Specialty Teaching)
category: pacu/population-specialty
task_type: LEARN
audience: PACU orientee or preceptor recovering ambulatory / day-surgery / fast-track patients discharging home the same day
updated: "2026-07-07"
tags:
  - pacu
  - ambulatory
  - day-surgery
  - population-specialty
  - fast-track
  - discharge-readiness
techniques:
  - ST-01
  - ST-02
  - RT-02
  - QA-02
  - ED-02
  - DS-06
difficulty: intermediate
related_prompts:
  - pacu_handoff_script.md
  - pacu_oliguria_urinary_retention.md
  - pacu_drug_antiemetics_reference.md
  - pacu_drug_analgesics_reference.md
  - pacu_bariatric_osa_considerations.md
  - pacu_topic_primer.md
  - pacu_complication_deep_dive.md
references:
  - Drain's PeriAnesthesia Nursing Practice (7th ed.) — ambulatory / Phase II chapters
  - ASPAN Standards of Perianesthesia Nursing Practice — Phase II / discharge criteria
  - ASPAN Core Curriculum for PeriAnesthesia Nursing Practice — ambulatory module
  - PADSS (Post-Anesthetic Discharge Scoring System) — Chung (validated discharge-readiness scale)
---

# PACU Ambulatory & Day-Surgery Considerations

> Safety reminder: The ambulatory patient's defining feature is that they go home — often with a lay caregiver as the only observer. The margin for a missed teaching point, an unrecognized retention, or an under-controlled symptom is smaller because there is no next shift to catch it. All discharge thresholds, criteria, and medications are per facility protocol and provider order; this teaching prompt states no scores, thresholds, or doses. Verify against current facility discharge policy and provider orders. See `../SAFETY_PREAMBLE.md`.

## Objective

Produce an **ambulatory/day-surgery-specific PACU considerations teaching artifact** for a nurse recovering fast-track and same-day-discharge patients. Covers fast-track pathways (bypass framing), Phase II / PADSS discharge-readiness logic, escort and discharge-teaching requirements, and the criteria for recognizing when a day-surgery patient must convert to admission — plus the adult-inpatient-PACU habits that fail when the patient is going home.

## When to use

- Orientation to an ambulatory surgery center or a day-surgery / Phase II recovery area.
- Cross-training an inpatient-PACU-trained nurse onto fast-track / same-day-discharge care.
- Refresher on PADSS-style discharge-readiness and discharge teaching.
- Pre-read before an ambulatory-focused simulation.

## When not to use

- For general (Phase I / inpatient) PACU orientation — use `pacu_topic_primer.md`.
- For a specific complication once it appears — use the relevant `pacu_*` deep-dive.
- For the handoff to an inpatient unit on conversion-to-admission — use `pacu_handoff_script.md`.
- For facility-specific discharge scoring cutoffs — those live in facility policy, not here.

## Inputs

- **Setting:** {{freestanding ambulatory surgery center | hospital-based day surgery / Phase II | fast-track / PACU-bypass pathway}}
- **Discharge scoring tool used:** {{PADSS | modified PADSS | facility Phase II criteria}}
- **Learner background:** {{Phase 1 orientee | inpatient-PACU-trained RN cross-training | new-to-ambulatory RN}}
- **Common case mix:** {{e.g., minor general/ortho/GI/GU/plastics/ophthalmology/dental — for tailoring examples}}
- **Source chapters available:** {{Drain's ambulatory/Phase II chapters, ASPAN Phase II/discharge module, facility discharge policy}}

## Audience / Scope

- **Primary:** PACU / Phase II nurse recovering ambulatory, same-day-discharge patients.
- **Scope:** Differences from inpatient recovery when the patient goes home. Not a facility discharge-policy substitute; not a directive to discharge without meeting facility criteria and provider order.

## Output requirements

```markdown
# Ambulatory / Day-Surgery PACU Considerations — {setting}

> Safety reminder: This patient goes home today, often observed only by a lay escort. Discharge criteria, scoring cutoffs, and take-home medications are per facility policy and provider order. Discharge teaching is a safety intervention, not paperwork — the escort is your extension of monitoring.

## What's different from inpatient recovery (at a glance)
| Domain | Inpatient PACU default | Ambulatory / day-surgery difference |
|---|---|---|
| End state | Transfer to a monitored unit | Discharge home — no next shift to catch a miss |
| Recovery model | Phase I → floor | Fast-track / Phase II; some patients bypass Phase I per criteria |
| Discharge readiness | "Stable for floor" | Formal discharge-readiness scoring (PADSS / facility criteria) — home-specific domains |
| PONV | Manage, continue as inpatient | Must be controlled before discharge — nausea/vomiting is a top cause of delayed discharge and readmission |
| Pain | Titrate on the unit | Must be controllable on the ordered oral/take-home regimen — not just IV-controlled |
| Voiding | Often not gating | Voiding may be a discharge criterion per facility/procedure (esp. neuraxial, pelvic/GU) |
| Escort | Not required | A responsible adult escort (and often a caregiver at home) is required per facility |
| Teaching | Handoff to staff | Teach-back with patient + escort: activity, meds, wound, red flags, follow-up, who to call |
| Ambulation / intake | Paced over stay | Ambulation and tolerating intake are often discharge gates per facility |

## Fast-track / PACU-bypass framing
- **Fast-tracking** moves a qualifying patient from OR toward Phase II (or discharge readiness) with reduced or bypassed Phase I, per **facility criteria and provider order** — not a nurse's independent call.
- **Bypass is criteria-driven:** a patient only fast-tracks if they meet the facility's readiness criteria on arrival. A patient who does not meet them recovers in the standard pathway — do not force the fast track.
- **The speed is the risk:** faster throughput compresses the window to catch a problem. Assess deliberately even when the pathway is quick.

## Discharge readiness — PADSS logic
The Post-Anesthetic Discharge Scoring System (PADSS) is a validated tool that scores home-specific readiness domains — commonly vital-sign stability, ambulation, nausea/vomiting, pain, and surgical bleeding. Higher total indicates readiness; the **passing threshold and exact domain scoring are per the validated tool and facility policy** (not stated here).
- **Score-and-trend, don't score-once:** readiness is a trajectory. Re-score per facility interval.
- **A single failing domain gates discharge** even if the total looks close — uncontrolled PONV, unmanaged pain, ongoing bleeding, or inability to ambulate each independently delays discharge.
- **The score supports judgment; it does not replace it.** A patient who scores "ready" but looks wrong is not ready — reassess and escalate.

## PONV and pain — must be home-ready, not just unit-ready
- **PONV must be controlled before discharge** — it is a leading cause of delayed discharge, unplanned admission, and return visits. Multimodal antiemetics are per order; rescue is often a *different class*, not a repeat. See `pacu_drug_antiemetics_reference.md`.
- **Pain must be controllable on the take-home regimen** — being comfortable on IV opioids is not the same as being ready to go home on the ordered oral/multimodal plan. See `pacu_drug_analgesics_reference.md`.
- **Confirm the patient understands the take-home analgesia plan** (what, when, non-opioid adjuncts, and what to do if it isn't working) as part of teaching.

## Voiding, ambulation, intake (facility/procedure-dependent gates)
- **Voiding** may be required before discharge per facility/procedure — especially after neuraxial anesthesia or pelvic/GU/hernia surgery. Distinguish true retention from simply not-yet-voided; bladder-scan-first per facility. See `pacu_oliguria_urinary_retention.md`.
- **Ambulation** to the facility standard (steady, safe, no orthostatic symptoms) is a common gate.
- **Tolerating oral intake** may be a gate per facility/procedure — do not assume; check the criteria.

## Escort and discharge teaching (a safety intervention)
- **A responsible adult escort is required** per facility — confirm early, because no escort means no discharge, and finding out at the end wastes the patient's day and the unit's slot.
- **Teach-back with patient AND escort**, because sedation impairs the patient's retention. Cover, in plain language:
  - **Activity restrictions** (driving, work, lifting, alcohol, signing legal documents) for the ordered window.
  - **Medication plan** (take-home analgesia, antiemetics, resuming home meds) per order.
  - **Wound / site care** and expected vs abnormal appearance.
  - **Red flags and who to call** — the specific symptoms that mean call the office / return / go to the ED, with the facility-provided contact path.
  - **Follow-up** appointment and instructions.
- **Give written instructions** to reinforce verbal teaching per facility — the patient will not remember everything said today.

## When a day-surgery patient must convert to admission
Escalate for a possible conversion-to-admission when, despite appropriate care and time:
- **Uncontrolled PONV** that will not be manageable at home.
- **Pain not controllable** on the ordered take-home regimen.
- **Airway or respiratory concern** (e.g., OSA patient not safe for unmonitored discharge per facility — see `pacu_bariatric_osa_considerations.md`).
- **Bleeding, hemodynamic instability, or a new dysrhythmia.**
- **Urinary retention** unresolved per facility criteria.
- **Excessive/prolonged sedation** or failure to meet readiness criteria within the expected window.
- **No safe escort / no safe home situation.**
Conversion is a **provider decision**; the nurse recognizes the trigger, escalates by role, and (if admitted) hands off via `pacu_handoff_script.md`.

## Common inpatient-PACU habits that miss in ambulatory recovery
- **Treating discharge teaching as paperwork.** For a patient going home, teaching *is* the monitoring plan — teach-back with the escort.
- **Calling pain "controlled" because IV opioids worked.** The bar is comfort on the take-home regimen.
- **Under-weighting PONV.** It is a top driver of delayed discharge and return visits — treat it as a discharge gate, not a nuisance.
- **Skipping the escort check until the end.** Confirm the responsible adult early.
- **Forcing the fast track.** A patient who doesn't meet bypass criteria recovers the standard way.
- **Scoring readiness once.** Re-score and trend; a passing total with one failing domain is not ready.
- **Hesitating to escalate a conversion trigger** to keep the schedule moving — the patient's safety outranks throughput.

## When to call (escalation by role)
- **Anesthesia / surgical provider by role** for uncontrolled PONV or pain, a respiratory/airway concern, bleeding, a new rhythm, unresolved retention, or any criterion the patient cannot meet — i.e., a possible conversion-to-admission.
- **Charge nurse** for a bed/admission if conversion is decided, a staffing need for extended monitoring, or an escort/social-situation problem.
- **Case management / social work per facility** for no-escort or unsafe-home-situation issues.

## Sources / reference
- *Drain's PeriAnesthesia Nursing*, ambulatory / Phase II chapters.
- ASPAN *Standards of Perianesthesia Nursing Practice* — Phase II / discharge criteria.
- ASPAN *Core Curriculum for PeriAnesthesia Nursing Practice* — ambulatory module.
- PADSS — Chung (validated discharge-readiness scale; threshold and scoring per tool/facility).
- Facility discharge policy, fast-track criteria, and escort policy: {{per facility protocol}}.
```

## Must / Must not

**Must:**
- Center the defining feature: the patient goes home, often observed only by a lay escort.
- Distinguish explicitly from inpatient recovery.
- Name PADSS as the discharge-readiness frame without stating the passing threshold or domain point values.
- Frame fast-track/bypass as criteria-and-order-driven, not a nurse's independent call.
- Treat PONV and pain as home-ready gates (controllable on the take-home regimen), not just unit-controlled.
- Cover escort requirement and teach-back discharge teaching (activity, meds, wound, red flags, follow-up, who to call) with the escort included.
- Provide explicit conversion-to-admission triggers, framed as a provider decision the nurse recognizes and escalates.
- Name common inpatient-PACU habits that fail in ambulatory recovery.
- Cross-reference `pacu_handoff_script.md`, `pacu_drug_antiemetics_reference.md`, and `pacu_oliguria_urinary_retention.md`.

**Must not:**
- State PADSS passing thresholds, domain point values, specific discharge-criteria numbers, or doses — all "per facility" / "per order" / "per tool."
- Fabricate readmission/delayed-discharge rates or timelines.
- Direct discharge without facility criteria being met and a provider order.
- Frame conversion-to-admission as a nurse's independent decision (it is a provider decision).
- Invent facility-specific discharge policies, escort rules, or contact paths.
- Reference race, religion, national origin, or other protected characteristics as clinical or performance signals.
- Include patient-identifying information.

## Quality signals

- A nurse reading this treats discharge teaching (with the escort, teach-back) as a safety intervention.
- PADSS is named; no threshold or point values are invented.
- PONV and pain are framed as home-ready gates, not unit-ready.
- Fast-track is criteria-driven, not forced.
- Conversion-to-admission triggers are explicit and escalation-framed.
- At least three inpatient-PACU habits that fail in ambulatory recovery are named.

## Verification

Before returning, verify:

- [ ] Goes-home / lay-escort defining feature is centered.
- [ ] Inpatient-vs-ambulatory contrast table present and covers end state, discharge readiness, PONV, pain, voiding, escort, teaching.
- [ ] PADSS named without invented threshold/point values.
- [ ] Fast-track/bypass framed as criteria-and-order-driven.
- [ ] PONV and pain framed as home-ready gates.
- [ ] Escort requirement + teach-back teaching (with red flags and who-to-call) present.
- [ ] Conversion-to-admission triggers explicit and escalation-framed as a provider decision.
- [ ] All thresholds / criteria / doses are "per facility" / "per order" — no specific values.
- [ ] Common inpatient-PACU habits that fail are named explicitly.
- [ ] Escalation named by role.
- [ ] Cross-references to handoff, antiemetics, and retention prompts present.

## False-Positive Prevention

Do **not** fabricate:

- **No invented PADSS thresholds, domain point values, or discharge-criteria numbers.** Per the tool / facility.
- **No invented take-home medication doses.** Always "per order."
- **No invented readmission / delayed-discharge rates or recovery timelines.**
- **No invented ASPAN section / Drain's chapter citations.** Mark `{{confirm}}` when unknown.
- **No invented facility discharge policies, fast-track criteria, escort rules, or contact paths.**
- **No patient-identifying information.**
- **No protected-characteristic references** used as clinical or performance signals.
- **No discharge without facility criteria + provider order;** conversion-to-admission is a provider decision, not a nurse's independent call.

## Worked Example

<details>
<summary>Example: "Common inpatient-PACU habits that miss in ambulatory recovery" section for an inpatient-trained RN cross-training onto day surgery (click to expand)</summary>

```markdown
## Common inpatient-PACU habits that miss in ambulatory recovery

1. **Treating the discharge instructions as a form to sign.** For a patient going home today, the teaching IS the monitoring plan. Do teach-back with the escort present — sedation blunts what the patient will remember — covering activity, meds, wound, red flags, who to call, and follow-up.

2. **Calling pain "controlled" because the IV fentanyl worked.** The real bar is comfort on the ordered oral/multimodal take-home plan. Confirm the patient can achieve and understand that plan before discharge.

3. **Shrugging off the nausea.** PONV is a leading reason day-surgery patients don't get to leave — and come back. Treat it as a discharge gate; rescue is often a different antiemetic class, per order.

4. **Confirming the escort at the very end.** No responsible adult means no discharge — verify it early so you're not unwinding a full day's plan at 3 pm.

5. **Forcing the fast track.** If the patient doesn't meet bypass criteria on arrival, they recover the standard way — the pathway serves the patient, not the schedule.

6. **Scoring readiness once and moving on.** Re-score and trend per facility; a near-passing total with one failing domain (bleeding, PONV, can't ambulate, can't void where required) is not ready — escalate rather than discharge.
```

Notes: each habit names the inpatient default + the ambulatory correction; scope-appropriate; no specific scores, thresholds, or doses; conversion framed as escalation; cross-references to antiemetics, retention, and handoff prompts implied.
</details>

## Self-check

- [ ] Goes-home / lay-escort defining feature centered.
- [ ] Inpatient-vs-ambulatory contrast table present.
- [ ] PADSS named; no invented threshold/point values.
- [ ] Fast-track/bypass criteria-and-order-driven.
- [ ] PONV and pain framed as home-ready gates.
- [ ] Escort requirement + teach-back teaching (red flags, who-to-call) present.
- [ ] Conversion-to-admission triggers explicit, escalation-framed as provider decision.
- [ ] All thresholds / criteria / doses "per facility" / "per order" — no specific values.
- [ ] Common inpatient-habit failures named.
- [ ] Escalation by role.
- [ ] Cross-references to handoff, antiemetics, and retention prompts.
- [ ] No invented thresholds, rates, or facility policies.
- [ ] No patient-identifying information.
- [ ] No protected-characteristic references as signals.
- [ ] Safety reminder at top.
- [ ] Verification section passed.
- [ ] False-Positive Prevention section passed.
