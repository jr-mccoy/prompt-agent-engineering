---
title: PACU Handoff Script (SBAR)
category: pacu/communication
task_type: COMMUNICATE
audience: PACU nurse giving handoff to floor / ICU / step-down
updated: "2026-04-16"
tags:
  - pacu
  - handoff
  - sbar
  - communication
techniques:
  - ST-01
  - ST-02
  - ST-03
  - RT-02
  - DS-06
difficulty: beginner
related_prompts:
  - ../../domain-healthcare-clinical/prompts/nursing_sbar_clinical_escalation.md
  - ../../domain-healthcare-clinical/prompts/medicine_handoff_communication.md
  - prompts/pacu_red_flag_card.md
  - prompts/pacu_preceptor_debrief.md
references:
  - Drain's PeriAnesthesia Nursing Practice (7th ed.)
  - ASPAN Standards of Perianesthesia Nursing Practice — transfer of care
  - ASPAN Core Curriculum for PeriAnesthesia Nursing Practice
---

# PACU → Receiving Unit Handoff Script

> Safety reminder: Template is a communication aid — always adjust to the actual patient and follow facility handoff policy.

## Objective

Produce a **surgery-specific SBAR handoff script** the PACU nurse can read or paraphrase when transferring a patient to the floor, step-down, or ICU.

## Inputs

- **Surgery type:** {{…}}
- **Receiving unit:** {{med/surg / tele / step-down / ICU / home with caregiver}}
- **Anesthesia type used:** {{GA / MAC / spinal / regional / combined}}
- **Devices still in place at transfer:** {{Foley, drains, PCA, epidural, O2, etc.}}

## Audience

- PACU RN giving report.
- Receiving RN hearing report (sets expectation for what they'll hear).

## Output requirements

```markdown
# PACU → {Receiving unit} Handoff — {Surgery type}

> Safety reminder: Script is a prompt — confirm every detail at the bedside with the patient.

## S — Situation (one sentence)
"{Patient initials}, {age}, post-op {surgery}, now ready for transfer to {unit}."

## B — Background
- Procedure: ...
- Anesthesia: ... (with specific drugs / blocks given as ordered)
- Relevant history: ...
- Allergies: ...
- Lines/devices: ... (IV, art line, Foley, drains, PCA, epidural)

## A — Assessment (current status)
- VS trend since admission: ...
- Pain: last score, last dose, time, response.
- Nausea: ...
- Respiratory: O2 source, flow, SpO2.
- Neuro: alert / oriented / block level if spinal.
- Surgical site: dressing dry/intact; drain output (color, amount) per last check.
- I/O: in, out, fluid still hanging.
- Labs of note: ...

## R — Recommendation / what receiving unit should know
- Next pain med due at: ...
- Next VS due at: ... (per facility policy)
- Anticipate: ... (e.g., "may need anti-emetic; watch for hypotension as spinal resolves over next ~2 hours")
- Surgeon-specific orders: ...
- Red flags specific to this surgery: trigger → call {role}

## Questions from receiving RN — answers ready
- ...

## Ticket-to-ride / transport prep
- Portable monitor (per facility): ...
- O2 during transport (per facility): ...
- Vomit basin / emesis bag if at risk.
- Family location / contact.
```

## Must / Must not

**Must:**
- SBAR structure preserved with explicit S/B/A/R headings.
- Surgery-specific red flags in the R section.
- Anticipation statement in R ("watch for X over next Y hours").
- Transport prep block.

**Must not:**
- No facility-specific paging or portable-equipment specifics — use *per facility policy*.
- No doses quoted without a "time given / response" context.

## Quality signals

- Receiving nurse hears actionable anticipation, not just history.
- Transport prep removes guesswork.
- Surgery-specific red flags are present.

## Verification

Before returning, verify:

- [ ] All four SBAR headings appear in order and are labeled explicitly (S/B/A/R).
- [ ] The A section reports a **trend**, not just a snapshot.
- [ ] The R section contains at least one anticipation statement with a timeframe ("watch for X over next Y hours").
- [ ] Surgery-specific red flags in R are PACU-realistic, not generic post-op boilerplate.
- [ ] Transport prep block names O2/monitor/emesis contingencies as "per facility policy" rather than invented details.
- [ ] Patient identifiers are initials + age only; no MRN, full name, DOB, or room number.

## False-Positive Prevention

Do **not** fabricate:

- **No invented doses, drip rates, or concentrations.** If a dose must appear, pair it with "last given at {time}, response {...}, per order."
- **No invented facility-specific items** (pager numbers, transport monitor model, portable O2 tank sizes, unit-specific room assignments, charge-nurse names).
- **No invented vital-sign thresholds** in R-section anticipation ("if BP < 90" unless sourced or part of provider order). Use qualitative language.
- **No invented handoff checklists** beyond SBAR structure — do not insert facility-specific checklists ("I-PASS modified," "SHARQ") that vary by institution.
- **No invented lab values** in A section.
- **No patient-identifying information** (MRN, full name, full DOB, room number).

## Worked Example

<details>
<summary>Example: Surgery = laparoscopic cholecystectomy, Receiving = med-surg floor (click to expand)</summary>

```markdown
# PACU → Med-Surg Handoff — Laparoscopic Cholecystectomy

> Safety reminder: Script is a prompt — confirm every detail at the bedside with the patient.

## S — Situation (one sentence)
"J.R., 48F, post-op lap chole, ready for transfer to 5-North."

## B — Background
- Procedure: laparoscopic cholecystectomy, uneventful, ~90 minutes.
- Anesthesia: general with volatile + opioid + NMB; reversed; extubated in OR.
- Relevant history: HTN controlled, no prior abdominal surgery, non-diabetic.
- Allergies: NKDA.
- Lines/devices: 18g R forearm IV running LR at KVO; no drains; no Foley.

## A — Assessment (current status)
- VS trend since PACU admit: BP 128/82 → 122/78 → 118/74 (stable downward trend within expected range); HR 84 → 78; RR 16; SpO₂ 98% on 2L NC, weaned to RA x 15 min with SpO₂ 96%.
- Pain: last score 4/10 at 14:20, last dose hydromorphone per order at 14:10, responded well.
- Nausea: mild at emergence, anti-emetic per order at 14:00, resolved.
- Respiratory: RA, clear, no shoulder-tip pain reported currently.
- Neuro: A&Ox3, following commands, no residual weakness.
- Surgical site: four laparoscopic ports, dressings dry and intact; no drainage.
- I/O: IV in ~400 mL, UOP not measured (no Foley), reports tolerating small sips of water.
- Labs: no post-op labs ordered.

## R — Recommendation / what receiving unit should know
- Next pain med available at: per MAR, prn.
- Next VS due at: per facility med-surg policy.
- Anticipate: referred shoulder-tip pain from insufflation may appear in next 2–4 hours; anti-emetic available prn.
- Surgeon-specific orders: ambulate within 4 hours, advance diet as tolerated per order.
- Red flags specific to lap chole: new severe abdominal pain, bleeding through dressing, shoulder-tip pain + fever → call surgeon on call.

## Questions from receiving RN — answers ready
- Last opioid dose: 14:10.
- Last PO intake: small sips clear liquids.
- Family present: spouse in waiting area.

## Ticket-to-ride / transport prep
- Portable monitor: per facility.
- O2 during transport: per facility (currently RA).
- Vomit basin: yes.
- Family location: spouse in main waiting area.
```

Notes: uses initials only, trend in A section, anticipation with timeframe in R, surgery-specific red flag with role, transport contingencies as "per facility."
</details>

## Self-check

- [ ] All four SBAR sections present and labeled.
- [ ] VS trend, not just snapshot.
- [ ] R includes anticipation + next-action timing.
- [ ] Surgery-specific red flag with role.
- [ ] Transport prep block present.
- [ ] Safety reminder at top.
- [ ] Verification section passed.
- [ ] False-Positive Prevention section passed — no invented doses, facility specifics, or patient identifiers.
