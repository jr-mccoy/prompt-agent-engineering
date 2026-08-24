---
title: PACU Drug Monograph — Analgesics Reference (Multimodal Pain, by Class)
category: pacu/pharmacology
task_type: LEARN
audience: PACU orientee (any phase) or preceptor for huddle
updated: "2026-07-07"
tags:
  - pacu
  - pharmacology
  - analgesics
  - multimodal
  - pain-management
techniques:
  - ST-01
  - ST-02
  - RT-02
  - QA-02
  - ED-02
  - DS-06
difficulty: intermediate
related_prompts:
  - pacu_drug_naloxone.md
  - pacu_opioid_induced_respiratory_depression.md
  - pacu_last_recognition_response.md
references:
  - Drain's PeriAnesthesia Nursing Practice (7th ed.) — pain / pharmacology chapters
  - ASPAN Standards of Perianesthesia Nursing Practice
  - Hospital pharmacy monograph (facility-specific; confirm current version)
---

# Analgesics — PACU Drug Class Reference (Multimodal Pain)

> Safety reminder: This is a **class-level, multimodal** reference — not a dosing calculator and no mg/kg. The goal is comfort **and function**, not a pain score of zero; opioids demand sedation-first monitoring, and every dose/route/interval is per provider order. See `../SAFETY_PREAMBLE.md`.

## Objective

Produce a PACU-focused, by-class analgesic reference that teaches opioid-sparing multimodal analgesia, the signature caution of each class, and the sedation-first monitoring that opioids require — with all pharmacology provider-ordered.

## Inputs

- **Analgesic classes on your formulary / order sets:** {{opioid, acetaminophen, NSAID, local anesthetic / regional adjunct, other adjuncts}}
- **Facility multimodal pain protocol:** {{prophylaxis + rescue pathway}}
- **Populations of note:** {{OSA/obesity, older adults, renal impairment, opioid-tolerant, bleeding-risk surgery}}
- **Sedation scale used on your unit:** {{POSS | RASS | facility scale}}

## Audience

- Orientee at any phase — core PACU pain pharmacology.
- Preceptor building a multimodal-analgesia / pain-safety huddle.

## Output requirements

```markdown
# Analgesics — PACU Class Reference (Multimodal)

> Safety reminder: Comfort + function, not zero. Opioids → sedation-first monitoring. All dosing per order.

## The multimodal principle
- Combine analgesics from **different mechanisms** so each does part of the work and the opioid requirement (and its risks) falls — this is opioid-sparing multimodal analgesia. Target comfort **and function** (breathing, moving, participating), not a pain score of zero.

## By class (mechanism → PACU-relevant effects → signature caution)

### Opioids (e.g., morphine, hydromorphone, fentanyl)
- Mechanism: mu-opioid receptor agonists.
- Effects: analgesia; also sedation, respiratory depression, nausea/vomiting, pruritus, hypotension, ileus, urinary retention.
- Signature caution: **respiratory depression preceded by sedation** — monitor the sedation level, not just RR/SpO₂ (see the OIRD deep dive); titrate to comfort/function; naloxone is the reversal (per order).

### Acetaminophen
- Mechanism: central analgesic/antipyretic (mechanism incompletely understood).
- Effects: opioid-sparing baseline analgesia; well tolerated.
- Signature caution: **cumulative total daily dose across all sources/routes** (hepatic) — account for combination products and other departments' doses; caution in hepatic impairment.

### NSAIDs (e.g., ketorolac, ibuprofen)
- Mechanism: cyclooxygenase inhibition (anti-inflammatory analgesia).
- Effects: opioid-sparing, especially for inflammatory/somatic pain.
- Signature caution: bleeding risk, renal effects (avoid in renal impairment / hypovolemia), GI effects; caution in certain surgeries, aspirin-sensitive asthma, and some older adults — per provider.

### Local anesthetics / regional adjuncts (nerve blocks, neuraxial, infiltration)
- Mechanism: sodium-channel blockade interrupting nerve conduction.
- Effects: excellent site-specific, opioid-sparing analgesia.
- Signature caution: **local anesthetic systemic toxicity (LAST)** and block-level effects — monitor for prodrome→CNS→cardiac progression and assess block level/motor-sensory return (see the LAST deep dive).

### Other adjuncts (if used: gabapentinoids, low-dose ketamine, alpha-2 agonists)
- Mechanism: varied (calcium-channel modulation; NMDA antagonism; central alpha-2).
- Signature caution: **additive sedation** (gabapentinoids stacked with opioids), dissociation/psychomimetic effects (ketamine), bradycardia/sedation/hypotension (alpha-2) — per provider.

## Monitoring in PACU
- Reassess a pain score **and function** (breathing depth, ability to move/participate) plus sedation level on the facility interval and after any analgesic — especially after opioids.
- Specific assessments by class: sedation-first + RR/pattern/SpO₂ (opioids), cumulative acetaminophen tally, bleeding/renal/urine-output awareness (NSAID), block level + LAST prodrome (regional), added sedation (adjuncts).
- Reassess the response 10–15 min (or per order) after a dose: did comfort/function improve, or is escalation/multimodal add-on needed?

## Red flags that require escalation
- Rising sedation with hypoventilation, or apnea, after opioids → call {anesthesia provider by role}; support ventilation (BVM ready); naloxone per order.
- LAST prodrome (perioral numbness, tinnitus, metallic taste, agitation) progressing to CNS/cardiac signs → call {provider by role}; LAST/lipid-rescue support per facility/ASRA.
- New bleeding, oliguria, or signs of NSAID-related harm → call {provider by role}.
- Uncontrolled pain despite the ordered regimen → call {provider by role} for plan revision.

## Common orientee mistakes
- Opioid-only thinking — reaching for more opioid instead of leveraging the multimodal plan.
- Missing the **cumulative acetaminophen** total across combination products / other sources.
- Giving an NSAID to a contraindicated patient (renal impairment, active bleeding risk) without checking.
- Chasing a pain score of zero instead of comfort + function — and over-sedating to get there.

## Teaching pearls
- Different mechanisms, lower opioid load — that's the whole point of multimodal.
- The target is a patient who is comfortable enough to breathe, move, and participate — not a zero.

## Sources
- *Drain's PeriAnesthesia Nursing*, pain / pharmacology chapters
- Hospital pharmacy monograph (facility-specific; confirm current version)
```

## Must / Must not

**Must:**
- Teach opioid-sparing multimodal analgesia and the comfort-and-function (not zero) goal.
- Give each class its signature caution (sedation-first for opioids, cumulative dose for acetaminophen, bleeding/renal for NSAID, LAST/block-level for regional).
- Include sedation-first monitoring for opioids and a per-class monitoring block.

**Must not:**
- No analgesic doses, mg/kg, ceilings-by-number, or concentrations.
- No "pain score must be zero" framing.
- No nurse-initiated dosing decisions (provider-scope).
- No invented acetaminophen ceilings, CrCl thresholds, or incidence statistics.

## Quality signals

- Orientee uses the multimodal plan, tracks cumulative acetaminophen, applies each class's caution, and monitors sedation-first after opioids while targeting function.

## Verification

- [ ] Multimodal / opioid-sparing principle + comfort-and-function goal stated.
- [ ] Each class has a signature caution.
- [ ] Opioid sedation-first monitoring + acetaminophen cumulative-dose + NSAID renal/bleeding + LAST/block-level all present.
- [ ] Monitoring block has reassess interval + class-specific assessments.
- [ ] Red flags link trigger → escalation role.
- [ ] No doses/mg-kg/ceilings/concentrations anywhere.

## False-Positive Prevention

Do **not** fabricate or invent:

- **No analgesic doses, mg/kg, numeric ceilings, or concentrations.** Per order only — including no invented acetaminophen maximum figure (state "cumulative total per order / monograph").
- **No invented renal (CrCl) or hepatic thresholds** — describe cautions qualitatively.
- **No invented incidence statistics** for OIRD, LAST, or NSAID harm — qualitative only.
- **No "pain must be zero" or "completely safe" language.**
- **No invented facility protocols or pager paths.**
- **No fabricated chapter/monograph citations.** Mark `{{confirm}}`.
- **No brand-only references** — name the class + a generic exemplar.

## Worked Example

<details>
<summary>Example: escalating pain without defaulting to more opioid (click to expand)</summary>

```markdown
## Leaning on the multimodal plan

An orientee's post-op patient rates pain high, and the reflex is "give more opioid."

Before that, work the multimodal plan per order: is the scheduled acetaminophen due (and what's the cumulative total across combination products)? Is an NSAID appropriate, or is this a renal-impaired / bleeding-risk patient where it isn't? Was there a regional block — is the level receding, and any LAST prodrome? If an opioid dose is warranted, titrate it to comfort **and function**, monitor sedation-first afterward (sedation precedes respiratory depression), and reassess in 10–15 minutes. The goal is a patient comfortable enough to breathe, move, and participate — not a zero, and not an over-sedated patient.
```

Notes: multimodal-first, cumulative-acetaminophen check, NSAID caution, sedation-first monitoring, comfort-and-function goal, no doses, escalation by role.
</details>

## Self-check

- [ ] Multimodal / opioid-sparing + comfort-and-function goal taught.
- [ ] Each class has its signature caution.
- [ ] Opioid sedation-first monitoring present.
- [ ] Monitoring block has interval + class-specific assessments.
- [ ] Red flags have escalation role.
- [ ] Safety reminder at top.
- [ ] No invented doses/ceilings/thresholds/incidence/facility specifics.
- [ ] Verification + False-Positive Prevention passed.
