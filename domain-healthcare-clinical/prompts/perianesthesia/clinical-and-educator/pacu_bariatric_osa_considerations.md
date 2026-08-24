---
title: PACU Bariatric & Obstructive Sleep Apnea Considerations (Population-Specialty Teaching)
category: pacu/population-specialty
task_type: LEARN
audience: PACU orientee or preceptor recovering patients with obesity, bariatric-surgery patients, or known/suspected obstructive sleep apnea
updated: "2026-07-07"
tags:
  - pacu
  - bariatric
  - obstructive-sleep-apnea
  - population-specialty
  - airway
  - respiratory-depression
techniques:
  - ST-01
  - ST-02
  - RT-02
  - QA-02
  - ED-02
  - DS-06
difficulty: advanced
related_prompts:
  - pacu_opioid_induced_respiratory_depression.md
  - pacu_negative_pressure_pulmonary_edema.md
  - pacu_drug_naloxone.md
  - pacu_drug_analgesics_reference.md
  - pacu_topic_primer.md
  - pacu_complication_deep_dive.md
references:
  - Drain's PeriAnesthesia Nursing Practice (7th ed.) — obesity and respiratory chapters
  - ASPAN Standards of Perianesthesia Nursing Practice — respiratory and safety domains
  - ASPAN Core Curriculum for PeriAnesthesia Nursing Practice
  - STOP-BANG questionnaire — Chung et al. (validated OSA screening instrument)
---

# PACU Bariatric & OSA Considerations

> Safety reminder: Patients with obesity and/or obstructive sleep apnea are the highest-risk PACU population for opioid-induced hypoventilation, airway obstruction, and rapid desaturation. Every dose, oxygen setting, and CPAP order is per provider order and facility protocol; this teaching prompt states no doses, thresholds, or device settings. Verify against current provider order and facility protocols before any intervention. See `../SAFETY_PREAMBLE.md`.

## Objective

Produce a **bariatric/OSA-specific PACU considerations teaching artifact** for a nurse recovering patients with obesity, bariatric-surgery patients, or known/suspected OSA. Covers what differs from the default adult recovery: STOP-BANG risk framing, positioning (ramp / head-of-bed), opioid sensitivity and OIRD risk, CPAP/home-device continuation, and airway-rescue preparation — and the adult-PACU habits that fail in this population.

## When to use

- Orientation to a unit that recovers a high volume of bariatric or high-BMI patients.
- Pre-read before recovering a known-OSA or STOP-BANG-high patient.
- Refresher on opioid-sparing / OIRD surveillance for this population.
- Pre-read before a bariatric/OSA-focused simulation (`pacu_simulation_scenario_builder.md`).

## When not to use

- For general PACU orientation — use `pacu_topic_primer.md`.
- For the OIRD event itself once it is occurring — use `pacu_opioid_induced_respiratory_depression.md`.
- For a specific drug reference — use the `pacu_drug_*` monographs.
- For bariatric-surgery *surgical* complication management (leak, bleed) — that is a provider-directed clinical pathway, not this teaching artifact.

## Inputs

- **Population focus:** {{elective bariatric surgery | high-BMI patient having non-bariatric surgery | known-OSA patient | suspected/unscreened OSA}}
- **OSA status known?** {{formally diagnosed + home CPAP/BiPAP | screened high-risk (e.g., STOP-BANG) | unscreened/unknown}}
- **Home device:** {{home CPAP | home BiPAP | none | unknown — confirm settings with patient/family/order}}
- **Learner experience level:** {{Phase 1 orientee | experienced RN cross-training onto a bariatric-heavy unit}}
- **Source chapters available:** {{Drain's obesity/respiratory chapters, ASPAN respiratory/safety domains, facility OSA/bariatric protocols}}

## Audience / Scope

- **Primary:** PACU nurse recovering patients with obesity and/or OSA.
- **Scope:** Differences from the default adult recovery for this population. Not a bariatric-surgery clinical pathway; not a substitute for facility OSA policy, difficult-airway response training, or provider orders.

## Output requirements

```markdown
# Bariatric / OSA PACU Considerations — {population focus}

> Safety reminder: This is the highest-risk population for opioid-induced hypoventilation and airway obstruction. All doses, O₂ settings, and CPAP orders are per provider order and facility protocol. Sedation precedes hypoventilation — monitor the sedation trend, not just the number on the pulse oximeter.

## What's different from the default adult recovery (at a glance)
| Domain | Default adult PACU | Bariatric / OSA difference |
|---|---|---|
| Respiratory reserve | Desaturation trends over minutes | Low functional residual capacity + high O₂ demand → desaturation is faster and harder to reverse |
| Opioids | Standard multimodal, titrate to comfort | Heightened sensitivity; opioid-sparing (multimodal) strongly favored; OIRD risk elevated |
| Sedation monitoring | Periodic assessment | Sedation-scale surveillance (POSS/RASS per facility) is primary — sedation precedes hypoventilation |
| Positioning | Supine / HOB per comfort | Ramped position and elevated head-of-bed per order improve airway patency and ventilation |
| Airway equipment | Standard adjuncts at bedside | Verify appropriately-sized adjuncts, difficult-airway resources, and a plan for rapid provider assistance |
| Home respiratory device | Rarely relevant | Known-OSA patient's home CPAP/BiPAP is often continued in PACU per order — confirm the device and settings early |
| Pulse oximetry | SpO₂ trend familiar | Supplemental O₂ can mask hypoventilation on SpO₂; capnography/EtCO₂ per facility adds ventilation data |
| Discharge / disposition | Standard criteria | Extended monitoring and higher level of care are common per facility OSA protocol |

## Why this population desaturates fast (physiology adult habits miss)
- **Reduced functional residual capacity + increased oxygen consumption:** the safe-apnea window is short. The adult instinct to "trend, then act" is too slow — reposition, stimulate, add oxygen per order, and escalate earlier.
- **Airway collapsibility:** the same soft-tissue anatomy that causes OSA at night causes obstruction under residual sedation. Obstruction can look like quiet, "peaceful" sleep — it is not.
- **Blunted arousal response:** these patients may not rouse and self-correct the way a lower-risk patient does.

## OSA risk framing — STOP-BANG
STOP-BANG is a validated screen combining eight factors (snoring, daytime tiredness, observed apnea, high blood pressure, body-mass index, age, neck circumference, and sex). Higher scores indicate higher OSA risk; the specific point cutoffs are per the validated instrument and facility policy.
- **Treat an unscreened patient with OSA features as high-risk** until proven otherwise, per facility protocol.
- A **formally diagnosed OSA patient on home CPAP/BiPAP** is high-risk regardless of how well they appear on admission.

## Opioid sensitivity & OIRD surveillance
- **Opioid-sparing is the goal:** multimodal analgesia (non-opioid adjuncts + regional per order) reduces the opioid dose this population tolerates poorly. See `pacu_drug_analgesics_reference.md`.
- **Sedation precedes hypoventilation:** a rising sedation score is the early warning — reassess before the next opioid dose, and hold/escalate per facility sedation-scale protocol.
- **Supplemental oxygen masks hypoventilation:** a normal SpO₂ on oxygen does not confirm adequate ventilation. Capnography/EtCO₂ per facility gives ventilation data SpO₂ cannot.
- If OIRD develops, follow `pacu_opioid_induced_respiratory_depression.md`; reversal is per order (`pacu_drug_naloxone.md`) and titrated to respiration — with re-sedation surveillance because opioid effect often outlasts the reversal agent.

## Positioning
- **Ramped / elevated head-of-bed positioning per order** improves airway patency, ventilation, and oxygen reserve — position before problems, not after.
- **Reverse-Trendelenburg / HOB up** is frequently ordered; confirm the order and the patient's hemodynamic tolerance.
- **Plan the airway rescue position and equipment before it's needed** — verify adjuncts and provider-assistance path at admission.

## CPAP / home-device continuation
- **A known-OSA patient's home CPAP or BiPAP is often resumed in PACU per order.** Ask the patient/family what device and settings they use at home, and confirm against the order — do not guess settings.
- **Have the interface and machine ready before extubation-phase recovery** where facility practice and orders direct.
- **Document tolerance and any obstruction/desaturation episodes** so the disposition decision reflects the real recovery course.

## Airway-rescue preparation (scope-safe)
- **Anticipate a difficult airway** in this population; know where the difficult-airway resources are and the fastest path to provider assistance.
- **The nurse prepares equipment and assists the provider** — positioning, oxygen per order, suction, adjuncts, calling for help. Advanced airway placement is provider-scope.
- **Rescue starts with the basics:** reposition, jaw thrust/airway maneuver as trained, stimulate, oxygen per order, and call early.

## Common adult-PACU habits that miss in bariatric / OSA recovery
- **Waiting for SpO₂ to fall before acting.** With supplemental O₂ on, SpO₂ can look fine while ventilation fails — watch the sedation trend and respiratory pattern.
- **Titrating opioids the way you would for an average-risk adult.** This population needs opioid-sparing and closer surveillance; reassess sedation before each dose.
- **Letting the "peacefully sleeping" patient be.** Quiet obstruction is still obstruction — assess air movement, not just appearance.
- **Deferring positioning until there's a problem.** Ramp/HOB-up is prophylactic, per order, from admission.
- **Forgetting the home CPAP.** For a diagnosed OSA patient, the home device is part of the plan — surface it early.
- **Applying general discharge timing.** OSA patients often need extended monitoring per facility protocol; don't rush the disposition.

## When to call (escalation by role)
- **Anesthesia / provider by role** for any airway obstruction not relieved by repositioning and basic maneuvers, rising sedation with hypoventilation, or a CPAP/oxygen order that does not fit the patient's course.
- **Rapid response / critical-care by role** for decompensation, persistent hypoventilation, or need for a higher level of monitoring.
- **Charge nurse** for staffing to support closer surveillance, extended monitoring, or a level-of-care change.
- **Respiratory therapy per facility** for CPAP/BiPAP setup and troubleshooting where that is their role.

## Sources / reference
- *Drain's PeriAnesthesia Nursing*, obesity and respiratory chapters.
- ASPAN *Standards of Perianesthesia Nursing Practice* — respiratory and safety domains.
- ASPAN *Core Curriculum for PeriAnesthesia Nursing Practice*.
- STOP-BANG questionnaire — Chung et al. (validated OSA screen; cutoffs per instrument).
- Facility OSA, bariatric, and difficult-airway protocols: {{per facility protocol}}.
```

## Must / Must not

**Must:**
- Distinguish explicitly from the default adult recovery — the point is population-specific gap-closure.
- Name STOP-BANG as the OSA screening frame without asserting specific point cutoffs.
- Center the sedation-precedes-hypoventilation principle and OIRD surveillance.
- Explain why supplemental oxygen can mask hypoventilation on SpO₂ (capnography adds ventilation data).
- Include ramped/HOB-up positioning framing (per order).
- Include home CPAP/BiPAP continuation with "confirm settings, don't guess."
- Name common adult-PACU habits that fail in this population.
- Keep airway rescue scope-safe (nurse prepares/assists; provider places advanced airway).
- Cross-reference `pacu_opioid_induced_respiratory_depression.md` and `pacu_drug_naloxone.md`.

**Must not:**
- State specific opioid doses, oxygen flow settings, CPAP/BiPAP pressures, or STOP-BANG numeric cutoffs — all "per order" / "per instrument" / "per facility."
- Fabricate desaturation timelines, apnea-window durations, or population incidence/mortality rates.
- Invent BMI thresholds or facility OSA-protocol criteria.
- Invent facility-specific protocols, pager numbers, or rapid-response activation criteria.
- Assume the nurse is scope-extended to place an advanced airway — always "prepare equipment and assist provider."
- Reference race, religion, national origin, or other protected characteristics as clinical or performance signals; body weight/BMI is a clinical factor for the patient only, never a performance signal about an orientee.
- Include patient-identifying information.

## Quality signals

- A nurse reading this can state why this population desaturates faster and why SpO₂ can be falsely reassuring on oxygen.
- STOP-BANG is named; no numeric cutoffs are invented.
- The sedation-scale-first / opioid-sparing principle is explicit.
- Ramped positioning and home-CPAP continuation are framed as proactive and per order.
- At least three adult-PACU habits that fail in this population are named.
- Airway rescue stays scope-safe.

## Verification

Before returning, verify:

- [ ] Default-adult-vs-population contrast table present and covers respiratory reserve, opioids, sedation monitoring, positioning, home device.
- [ ] STOP-BANG named without invented numeric cutoffs.
- [ ] Sedation-precedes-hypoventilation and OIRD surveillance explicit.
- [ ] Supplemental-O₂-masks-hypoventilation point present; capnography/EtCO₂ mentioned per facility.
- [ ] Ramped / HOB-up positioning framed as per order.
- [ ] Home CPAP/BiPAP continuation with confirm-settings framing.
- [ ] All doses / O₂ / pressures are "per order" — no specific values.
- [ ] Common adult-PACU habits that fail are named explicitly.
- [ ] Escalation named by role.
- [ ] Cross-references to OIRD deep-dive and naloxone monograph present.

## False-Positive Prevention

Do **not** fabricate:

- **No invented opioid doses, O₂ flow rates, or CPAP/BiPAP pressures.** Always "per order."
- **No invented STOP-BANG cutoffs or BMI thresholds.** Cutoffs are per the validated instrument / facility policy.
- **No invented desaturation timelines, apnea-window durations, or incidence/mortality statistics.**
- **No invented ASPAN section / Drain's chapter citations.** Mark `{{confirm}}` when unknown.
- **No invented facility OSA/bariatric protocols, pager numbers, or rapid-response criteria.**
- **No patient-identifying information.**
- **No protected-characteristic references** used as clinical or performance signals.
- **No scope-creep actions** — advanced airway remains provider-scope.

## Worked Example

<details>
<summary>Example: "Common adult-PACU habits that miss in bariatric / OSA recovery" section for a Phase 1 orientee on a bariatric-heavy unit (click to expand)</summary>

```markdown
## Common adult-PACU habits that miss in bariatric / OSA recovery

1. **Watching SpO₂ instead of the sedation trend.** Your known-OSA lap-band patient is on 2 L O₂ per order and reads 97%, but their sedation score is climbing and respirations are shallow — the oxygen is masking hypoventilation. Reassess sedation before the next opioid dose and escalate per protocol; consider EtCO₂ per facility.

2. **Titrating opioids like an average adult.** This patient needs opioid-sparing — lean on the ordered multimodal adjuncts and regional, and reassess sedation before each opioid dose rather than dosing to a comfort target on a fixed interval.

3. **Letting the "peaceful sleeper" sleep.** Quiet, still, "resting comfortably" can be quiet obstruction. Assess actual air movement and chest rise, not just appearance.

4. **Deferring positioning.** Set the ramp / head-of-bed-up per order at admission — patency is easier to maintain than to rescue.

5. **Forgetting the home CPAP.** Ask early what device and settings they use at home, confirm against the order, and have it ready per facility practice — don't guess the pressure.

6. **Rushing the disposition.** OSA patients often need extended monitoring per facility protocol; the discharge clock is not the general-population clock.
```

Notes: each habit names the adult default + the population correction; scope-appropriate (no provider actions); no specific doses, O₂ settings, or pressures; cross-references to OIRD and analgesics references implied.
</details>

## Self-check

- [ ] Default-adult-vs-population contrast table present.
- [ ] STOP-BANG named; no invented cutoffs.
- [ ] Sedation-first / opioid-sparing / OIRD surveillance explicit.
- [ ] Supplemental-O₂-masks-hypoventilation point present.
- [ ] Ramped/HOB-up positioning and home-CPAP continuation framed as per order.
- [ ] All doses / O₂ / pressures "per order" — no specific values.
- [ ] Common adult-habit failures named.
- [ ] Escalation by role.
- [ ] Cross-references to OIRD deep-dive and naloxone monograph.
- [ ] No invented thresholds, timelines, or facility protocols.
- [ ] No patient-identifying information.
- [ ] No protected-characteristic references as signals.
- [ ] Airway rescue scope-safe.
- [ ] Safety reminder at top.
- [ ] Verification section passed.
- [ ] False-Positive Prevention section passed.
