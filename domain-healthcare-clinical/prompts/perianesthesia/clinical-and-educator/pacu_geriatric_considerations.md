---
title: PACU Geriatric Considerations (Older-Adult Recovery)
category: pacu/population-specialty
task_type: LEARN
audience: PACU orientee or preceptor caring for geriatric post-op patients
updated: "2026-04-16"
tags:
  - pacu
  - geriatric
  - older-adult
  - population-specialty
  - delirium
  - polypharmacy
techniques:
  - ST-01
  - ST-02
  - RT-02
  - QA-02
  - ED-02
  - DS-06
difficulty: intermediate
related_prompts:
  - prompts/pacu_topic_primer.md
  - prompts/pacu_complication_deep_dive.md
  - prompts/pacu_medication_profile.md
  - prompts/pacu_patient_education_sheet.md
  - prompts/pacu_emergence_agitation_deescalation.md
  - prompts/pacu_simulation_scenario_builder.md
references:
  - Drain's PeriAnesthesia Nursing Practice (7th ed.) — geriatric chapters
  - ASPAN Standards of Perianesthesia Nursing Practice — geriatric population
  - American Geriatrics Society Beers Criteria (awareness of PIMs — potentially inappropriate medications)
  - CAM / CAM-ICU / Nu-DESC delirium-screening tools
---

# PACU Geriatric Considerations

> Safety reminder: Geriatric post-op recovery is high-stakes for delirium, falls, polypharmacy interactions, hypothermia, and functional decline. All doses and thresholds are per provider order and facility protocol. The Beers Criteria list of potentially inappropriate medications (PIMs) is referenced for awareness; it is not a substitute for provider prescribing.

## Objective

Produce a **geriatric-specific PACU considerations teaching artifact** for a PACU nurse caring for older-adult post-op patients. Covers what differs from general adult PACU: emergence / postoperative delirium (POD) recognition and screening (CAM, CAM-ICU, Nu-DESC), polypharmacy awareness (Beers Criteria framework), fall risk, hypothermia recovery, frailty-adjusted pain management, and the specific handoff implications of a geriatric patient.

## When to use

- Orientation teaching for a PACU orientee caring for older-adult post-op patients.
- Refresher or cross-training for experienced PACU RNs rotating into a surgical service with high geriatric volume (orthopedics, urology, general surgery).
- Pre-read before a geriatric-focused simulation (`pacu_simulation_scenario_builder.md`).

## When not to use

- For younger-adult general PACU — use `pacu_topic_primer.md`.
- For a specific geriatric complication deep dive (e.g., hip-fracture delirium) — use `pacu_complication_deep_dive.md` with geriatric context.
- For dementia-care-specific guidance beyond PACU scope — refer to facility geriatric / memory-care resources.

## Inputs

- **Surgical service context:** {{orthopedic (hip fracture, joint replacement) | urology | general surgery | cardiovascular | neurosurgical | mixed}}
- **Age range focus:** {{65–74 | 75–84 | 85+ | mixed older adult}}
- **Learner's PACU experience level:** {{Phase 1 orientee | experienced PACU RN}}
- **Baseline cognitive status available in handoff:** {{cognitively intact | known MCI / dementia | unknown}}
- **Source chapters available:** {{Drain's geriatric chapters, ASPAN geriatric module, facility geriatric protocols}}

## Audience / Scope

- **Primary:** PACU nurse caring for older-adult post-op patients.
- **Scope:** Differences from general adult PACU. Not a comprehensive geriatric nursing textbook; not a substitute for facility geriatric-specific orientation or NICHE-aligned programs.

## Output requirements

```markdown
# Geriatric PACU Considerations — {surgical context, age range}

> Safety reminder: Geriatric recovery is high-risk for delirium, falls, hypothermia, and polypharmacy interactions. Doses are weight-adjusted and per order; renal / hepatic function often impaired. Verify everything against facility geriatric protocols and provider orders.

## What's different from general adult PACU (at a glance)
| Domain | General adult default | Geriatric difference |
|---|---|---|
| Emergence & cognition | Brief disorientation expected; resolves quickly | Post-op delirium risk higher; screen with CAM / CAM-ICU / Nu-DESC; distinguish emergence delirium from POD |
| Pharmacology | Adult doses common | Altered pharmacokinetics (reduced renal clearance, altered volume of distribution, longer half-life for many agents); Beers Criteria awareness |
| Pain | Numeric rating + multimodal | Pain under-reported; functional pain assessment important; frailty-adjusted dosing per order |
| Fall risk | Standard ambulation criteria | Higher fall risk; orthostatic BP assessment; ambulate with caution per order |
| Thermal regulation | Rewarming usually routine | Slower rewarming; higher hypothermia risk at baseline; monitor active warming per facility |
| Skin integrity | Standard monitoring | Fragile skin, pressure-injury risk higher, especially at heels and sacrum; reposition per facility interval |
| Sensory | Standard | Vision, hearing, and sensory deficits common; ensure hearing aids / glasses returned ASAP |
| Hydration | Standard I/O | Dehydration risk higher; urine output trends matter; confirm baseline kidney function per chart |
| Discharge planning | Standard criteria | Functional return to baseline + caregiver availability + home-environment safety considered |

## Post-op delirium (POD) — the central geriatric PACU risk

**Definition (functional):** acute change in attention + altered level of consciousness or disorganized thinking, developing over hours-to-days post-op, fluctuating in course.

**Screening tools (name them, use per facility):**
- **CAM (Confusion Assessment Method)** — for general ward / PACU patients.
- **CAM-ICU** — for intubated / non-verbal patients.
- **Nu-DESC (Nursing Delirium Screening Scale)** — PACU-friendly, brief.
- **Use the facility's chosen tool consistently** — inconsistency defeats trend-detection.

**POD vs. emergence delirium (ED):**
- **Emergence delirium:** occurs in the first minutes-to-hour after emergence, often from volatile anesthesia; pattern is disinhibited / agitated / thrashing; self-limited in most cases.
- **Post-op delirium (POD):** develops over hours-to-days; can be hypoactive (quiet, withdrawn, misdiagnosed as "sleeping well") or hyperactive (agitated); hypoactive is both more common in older adults and more often missed.
- **Hypoactive delirium is not "the good kind"** — it carries equal or worse outcomes and is easily missed.

**Reversible contributors to check first (before labeling delirium):**
- Hypoxia, hypercapnia.
- Hypoglycemia (especially in diabetic patients after altered NPO / insulin timing).
- Urinary retention.
- Pain (under-treated).
- Medication effect (anticholinergic burden, benzodiazepine, sedation — see Beers).
- Electrolyte derangement (sodium, calcium).
- Infection (early sign in older adults may be delirium rather than fever).
- Constipation / fecal impaction.

## Polypharmacy awareness (Beers Criteria framing)
- **Beers Criteria** lists potentially inappropriate medications (PIMs) for older adults. PACU nurses should be aware of common PIMs to flag concerns to the prescribing provider when orders surface — not to override provider orders.
- Commonly flagged in PACU: certain long-acting benzodiazepines, first-generation antihistamines (diphenhydramine), certain anticholinergics, certain muscle relaxants.
- **What PACU nurses do with this awareness:**
  - If an ordered med is on a PIM list, confirm the order is intentional and document response closely.
  - If the patient becomes agitated and the reflex thought is "benzodiazepine," consider non-pharmacologic de-escalation first per `pacu_emergence_agitation_deescalation.md` — benzodiazepines can worsen delirium in older adults.
  - Never silently refuse or delay an ordered medication; if concern exists, raise it with the prescribing provider.
- **Specific agent and dose decisions are per provider order.** This prompt does not list specific PIM agents or doses; the Beers Criteria is a living reference — consult current facility pharmacy resources.

## Frailty-adjusted pain management
- **Pain is under-reported in older adults.** Use functional cues (grimacing, splinting, reduced mobility) alongside numeric reports.
- **Multimodal is especially valuable:** scheduled acetaminophen + adjunct + rescue opioid (per order) is often lower-risk than opioid-monotherapy in frail older adults.
- **Start-low-go-slow on opioids** is a provider-order principle — nurses verify and monitor response; do not invent reduction ratios.
- **Watch for respiratory depression carefully** — altered pharmacokinetics mean peak effect may be later than expected; monitor per facility interval.
- **Adjuncts are per order.** This prompt does not invent regimens.

## Fall risk
- **Orthostatic BP** before ambulation — older adults decompensate rapidly with position change.
- **Sensory deficits** (vision, hearing) compound fall risk — return glasses / hearing aids before ambulation.
- **Baseline mobility matters** — a pre-op ambulator who now requires assistance is a signal, not a new baseline.
- **Bladder urgency** drives rushed ambulation attempts — proactive toileting assistance per facility.
- **Environmental:** clutter, loose floor mats, IV lines trailing behind — address before ambulation.

## Thermal regulation
- Older adults baseline lower body temperatures; post-op hypothermia is common and slower to resolve.
- Active warming per facility protocol; monitor temp on admission and at intervals.
- Shivering increases oxygen demand — respiratory assessment matters.

## Skin integrity and positioning
- Heels and sacrum are high-risk pressure points during extended PACU stays.
- Reposition per facility interval; offload heels.
- Fragile skin tears easily — gentle transfers and careful tape / dressing removal.

## Sensory and communication
- Hearing aids and glasses should be returned as soon as the patient is alert enough.
- Speak clearly at normal-to-slightly-elevated volume (not shouting); face the patient for lip-reading.
- Written communication (whiteboard / paper) for patients with significant hearing loss.
- Interpreter (in-person or telephonic per facility) for non-English-speaking patients.

## Handoff to floor / home
- **Baseline cognitive status vs. current:** explicit in SBAR — a slight change is a real signal.
- **Delirium screening results:** CAM / Nu-DESC status and trend.
- **Ambulation status + orthostatic findings.**
- **Next pain meds due + response to last dose.**
- **Hydration / urine output trend.**
- **Home environment + caregiver support** if discharging home (often the limiting factor for safe discharge in older adults).
- **Skin integrity on admission and at discharge from PACU.**
- **Returned items:** glasses, hearing aids, dentures, mobility aids.

Use `pacu_handoff_script.md` SBAR structure with geriatric context layered in.

## Common general-adult-PACU habits that miss in geriatric PACU
- **Assuming disorientation will resolve on its own.** Hypoactive POD is often missed because the patient seems "calm." Screen with CAM / Nu-DESC.
- **Reflexively reaching for a benzodiazepine for agitation.** In older adults, benzodiazepines can worsen delirium — non-pharmacologic de-escalation first (see `pacu_emergence_agitation_deescalation.md`), then per order.
- **Using standard ambulation criteria without orthostatic check.** Orthostatic drop is common and is the immediate fall-risk cue.
- **Under-treating pain because the patient "looks fine."** Functional cues + numeric reports together; under-treated pain is itself a delirium driver.
- **Delaying return of glasses / hearing aids.** Sensory deprivation contributes to delirium.
- **Sending home without confirming caregiver and home safety.** Discharge planning is often the rate-limiter, and "home alone without ambulation assistance" is a readmission pattern.
- **Skipping the baseline vs. current cognitive comparison in handoff.**

## When to call (escalation by role)
- **Prescribing provider** for any new delirium, significant pain, or concern about an ordered medication (including PIM concern).
- **Charge nurse** for staffing / 1:1 needs for severe agitation or fall-risk patient.
- **Social work / discharge planner** for home-safety or caregiver-support concerns.
- **Geriatric consult service** (if facility has one) for complex delirium or polypharmacy.
- **Rapid response** for decompensation — older adults decompensate quickly and subtly.

## Sources / reference
- *Drain's PeriAnesthesia Nursing*, geriatric chapters.
- ASPAN *Standards of Perianesthesia Nursing Practice* — geriatric population.
- American Geriatrics Society Beers Criteria — current edition (reference only; provider prescribes).
- CAM / CAM-ICU (Inouye et al.) / Nu-DESC (Gaudreau et al.) — delirium screening tools.
- Facility geriatric / NICHE program resources: {{per facility protocol}}.
```

## Must / Must not

**Must:**
- Distinguish emergence delirium from post-op delirium (POD) — different time courses, different management.
- Name CAM / CAM-ICU / Nu-DESC as delirium screening tools.
- Emphasize hypoactive delirium as equally serious and more often missed.
- List reversible contributors to delirium (hypoxia, hypoglycemia, urinary retention, pain, meds, electrolytes, infection, constipation) to rule out first.
- Reference Beers Criteria for awareness without invented specifics.
- Treat pain assessment as functional + numeric combined.
- Include orthostatic BP + sensory-deficit + caregiver framing in fall risk and discharge.
- Cross-reference `pacu_emergence_agitation_deescalation.md` and `pacu_handoff_script.md`.

**Must not:**
- Invent specific PIM lists by agent and dose — Beers Criteria updates; defer to current facility pharmacy resource.
- Invent specific geriatric opioid reduction ratios or dose-adjustment formulas.
- Invent specific temperature thresholds for hypothermia action.
- Invent facility-specific fall-risk cutoffs or orthostatic criteria.
- Reference age as a performance signal in an orientee-evaluation context (age is relevant to the patient).
- Conflate dementia with delirium — they're different; dementia is a baseline that raises delirium risk.
- Use ageist framing ("he's just confused because he's old") — describe behavior, screen, escalate.
- Invent ASPAN / Drain's / Beers section numbers. Mark `{{confirm}}` if unknown.
- Include patient-identifying information.
- Substitute for facility geriatric orientation or NICHE / geriatric-consult resources.

## Quality signals

- A PACU nurse reading this can name three specific adult-PACU habits that fail in older-adult care.
- CAM / Nu-DESC are named and the hypoactive-vs-hyperactive distinction is clear.
- The reversible-contributors list (hypoxia, hypoglycemia, retention, pain, meds, electrolytes, infection, constipation) is explicit.
- Beers Criteria is named as an awareness framework, not a dose list.
- Discharge framing includes home / caregiver / environment, not just clinical criteria.

## Verification

Before returning, verify:

- [ ] Contrast table with general adult PACU present.
- [ ] Emergence delirium vs. POD distinguished.
- [ ] CAM / CAM-ICU / Nu-DESC named.
- [ ] Hypoactive delirium framed as serious and missed.
- [ ] Reversible contributors list present.
- [ ] Beers Criteria referenced as awareness framework; no invented PIM agents or doses.
- [ ] Frailty-adjusted pain management framing.
- [ ] Orthostatic + sensory + caregiver fall-risk framing.
- [ ] Handoff includes baseline cognition, delirium screening, ambulation, returned items, caregiver.
- [ ] Cross-references to de-escalation and handoff prompts present.

## False-Positive Prevention

Do **not** fabricate:

- **No invented PIM lists with specific agents or doses.** Beers Criteria updates; reference current facility pharmacy resource.
- **No invented geriatric dose-reduction ratios or formulas.**
- **No invented hypothermia thresholds or rewarming rates.**
- **No invented fall-risk cutoffs** (TUG seconds, Morse Fall Scale cutoffs beyond what source supplies).
- **No invented CAM / Nu-DESC cutoff scores beyond what the original validation studies supply** — cite Inouye / Gaudreau when scoring detail is required.
- **No invented facility geriatric protocols or consult-service activation criteria.**
- **No invented ASPAN / Drain's citations.** Mark `{{confirm}}` if unknown.
- **No ageist framing.** Age is not a trait; describe behavior.
- **No patient-identifying information.**
- **No protected-characteristic references** used as performance signals in orientee evaluation.
- **No scope-creep.** Nurses flag; providers prescribe.

## Worked Example

<details>
<summary>Example: "Reversible contributors" checklist applied to a Week 6 orientee assessing an 82yo post-op patient who seems "just sleepy" (click to expand)</summary>

```markdown
## Applying the reversible-contributors framework

Scenario: 82-year-old post-op open cholecystectomy, 4 hours post-emergence, lying quietly, eyes closed, answers briefly when spoken to but drifts back. Preceptor asks orientee to walk through the hypoactive-delirium differential.

Checklist (orientee verbalizes):
- [x] Hypoxia — SpO₂ 96% on 2L, RR 14, appears adequate; not explanatory alone.
- [x] Hypercapnia — not directly measurable; RR pattern normal.
- [x] Hypoglycemia — bedside glucose per facility order showed 82 mg/dL (not low-threshold but on the lower end — recheck per order).
- [x] Urinary retention — palpable bladder? Bladder scan per facility.
- [x] Pain — asked patient, denied; but grimaces when turning. Under-treated pain is possible.
- [x] Meds — received opioid + antiemetic per order in last hour; sedation-related contribution likely.
- [x] Electrolytes — last check on admission within normal; trending if ordered.
- [x] Infection — temp 36.4, no known source.
- [x] Constipation — per chart, has not had BM since pre-op; symptom possible.

Orientee's verbalization:
"I think the leading contributor is recent opioid effect plus possible under-treated pain signaled by grimacing on turning. But I want to rule out bladder retention and recheck glucose before I call this 'just sleepy.' I'll run CAM — if attention is impaired and there's fluctuation, this could be hypoactive POD and I'll escalate to the prescribing provider."

Preceptor affirms: the reflex of "she's just sleeping it off" is the missed-hypoactive-delirium failure mode. The orientee named it before action.
```

Notes: applies reversible-contributors framework; names CAM as the next action; distinguishes hypoactive POD from sedation; no invented doses; escalation by role.
</details>

## Self-check

- [ ] Contrast table with general adult PACU present.
- [ ] Emergence vs. POD distinguished.
- [ ] CAM / CAM-ICU / Nu-DESC named.
- [ ] Hypoactive delirium framed as serious and missed.
- [ ] Reversible contributors list explicit.
- [ ] Beers Criteria as awareness framework; no invented specifics.
- [ ] Pain assessment as functional + numeric.
- [ ] Orthostatic + sensory + caregiver in fall / discharge framing.
- [ ] Handoff includes baseline-vs-current cognition, delirium screening results, returned items, caregiver.
- [ ] Cross-references present.
- [ ] No ageist framing, no invented PIM agents, no invented thresholds.
- [ ] No patient-identifying information.
- [ ] No protected-characteristic references as performance signals.
- [ ] Safety reminder at top.
- [ ] Verification section passed.
- [ ] False-Positive Prevention section passed.
