---
title: PACU Drug Monograph — Antiemetics Reference (Multimodal PONV, by Class)
category: pacu/pharmacology
task_type: LEARN
audience: PACU orientee (any phase) or preceptor for huddle
updated: "2026-07-07"
tags:
  - pacu
  - pharmacology
  - antiemetics
  - PONV
  - multimodal
techniques:
  - ST-01
  - ST-02
  - RT-02
  - QA-02
  - ED-02
  - DS-06
difficulty: intermediate
related_prompts:
  - pacu_drug_analgesics_reference.md
  - pacu_medication_profile.md
  - pacu_red_flag_card.md
references:
  - Drain's PeriAnesthesia Nursing Practice (7th ed.) — PONV / pharmacology chapters
  - ASPAN Standards of Perianesthesia Nursing Practice
  - Hospital pharmacy monograph (facility-specific; confirm current version)
---

# Antiemetics — PACU Drug Class Reference

> Safety reminder: This is a **class-level** reference for multimodal PONV management — not a dosing calculator. The core teaching point is that rescue PONV is treated by **switching to a different class**, not repeating the same agent. All doses, routes, and intervals are per provider order and facility protocol; this reference states no doses. See `../SAFETY_PREAMBLE.md`.

## Objective

Produce a PACU-focused, by-class antiemetic reference that teaches multimodal (different-mechanism) PONV management, the signature adverse effect of each class, and the safety cautions an orientee must know — with all pharmacology provider-ordered.

## Inputs

- **Antiemetic classes on your formulary:** {{5-HT3 antagonist, corticosteroid, phenothiazine/antihistamine, transdermal anticholinergic, butyrophenone, prokinetic}}
- **Facility PONV protocol / order set:** {{prophylaxis + rescue pathway}}
- **Populations of note:** {{QT-risk, older adults, glaucoma, PONV-high-risk (Apfel factors)}}

## Audience

- Orientee at any phase — high-frequency PACU pharmacology.
- Preceptor building a PONV-management huddle.

## Output requirements

```markdown
# Antiemetics — PACU Class Reference

> Safety reminder: Rescue = switch class, don't repeat. All dosing per order.

## The multimodal principle
- PONV is managed with agents from **different classes / mechanisms** to hit multiple pathways. If a prophylactic agent has already been given and nausea breaks through, **rescue with a different class** — repeating the same class within its window adds risk without much benefit.

## By class (mechanism → PACU-relevant effects → signature caution)

### 5-HT3 receptor antagonists (e.g., ondansetron)
- Mechanism: block serotonin (5-HT3) receptors centrally and in GI vagal afferents.
- Effects: reduce nausea/emesis; generally non-sedating.
- Signature caution: QT prolongation (class effect) — relevant with other QT-prolonging agents or hypokalemia; headache, constipation.

### Corticosteroids (e.g., dexamethasone)
- Mechanism: antiemetic effect (incompletely understood; anti-inflammatory contribution); best as prophylaxis given early.
- Effects: prophylactic PONV reduction; also analgesic-adjunct effect.
- Signature caution: transient blood-glucose elevation (watch in diabetics); perineal itching/burning on IV push (a known infusion-related effect); single-dose perioperative use is generally well tolerated but confirm per order.

### Phenothiazines / antihistaminic dopamine antagonists (e.g., promethazine)
- Mechanism: dopamine (and histamine/anticholinergic) receptor antagonism.
- Effects: antiemetic and sedating.
- Signature caution: **severe tissue injury on extravasation / arterial exposure** — a high-alert IV administration concern (dilution, patent large-bore line, watch the site, per facility); also sedation, hypotension, extrapyramidal symptoms, anticholinergic effects.

### Transdermal anticholinergic (e.g., scopolamine patch)
- Mechanism: central muscarinic antagonism; applied preoperatively for sustained effect.
- Effects: prophylactic antiemetic.
- Signature caution: anticholinergic effects — dry mouth, blurred vision, urinary retention, and **confusion/delirium especially in older adults**; caution with glaucoma; remember to note the patch on assessment and handoff.

### Butyrophenones (e.g., droperidol, haloperidol) — if on formulary
- Mechanism: dopamine antagonism.
- Effects: antiemetic; sedating.
- Signature caution: QT prolongation; sedation; extrapyramidal symptoms.

### Prokinetic dopamine antagonist (e.g., metoclopramide) — if on formulary
- Mechanism: dopamine antagonism + GI prokinetic.
- Signature caution: extrapyramidal symptoms / akathisia (restlessness); caution in bowel obstruction.

## Monitoring in PACU
- Reassess a nausea score + VS on the facility interval and 10–15 min after any rescue dose (response, or need to switch class).
- Specific assessments by class: rhythm/QT awareness (5-HT3, butyrophenone), IV-site integrity + sedation/BP (promethazine), glucose in diabetics (corticosteroid), mental status in older adults (scopolamine), restlessness/EPS (dopamine antagonists).
- Reassess aspiration risk in the actively vomiting patient — positioning and suction per facility (see the aspiration deep dive).

## Red flags that require escalation
- New palpitations, syncope, or dysrhythmia on the monitor → call {anesthesia provider by role} / rapid response per facility.
- Hypersensitivity (rash, wheeze, facial/airway swelling) → call {provider by role} immediately; prepare airway support.
- Extravasation of a vesicant antiemetic (e.g., promethazine) with site pain/change → stop, follow facility extravasation protocol, notify {provider by role}.
- Acute dystonia / severe akathisia → call {provider by role}.

## Common orientee mistakes
- Repeating the same class when the first dose failed instead of switching class.
- Giving promethazine casually IV without the extravasation precautions.
- Missing anticholinergic confusion from a scopolamine patch in an older adult (and forgetting to hand off the patch).
- Treating "nausea" without checking for a treatable driver (hypotension, opioid, pain, movement, hypoxia).

## Teaching pearls
- Rescue by mechanism: different class, not a repeat.
- Every class has a signature caution — know the one for each agent your unit stocks.

## Sources
- *Drain's PeriAnesthesia Nursing*, PONV / pharmacology chapters
- Hospital pharmacy monograph (facility-specific; confirm current version)
```

## Must / Must not

**Must:**
- Teach multimodal PONV as different-class rescue, not repeat-dosing.
- Give each class its signature caution (QT for 5-HT3, extravasation for promethazine, anticholinergic delirium for scopolamine, glucose for corticosteroid, EPS for dopamine antagonists).
- Include a monitoring block and a "check for a treatable driver" prompt.

**Must not:**
- No antiemetic doses, routes-by-number, or concentrations.
- No claim that any agent is "always safe."
- No nurse-initiated dosing decisions (provider-scope).
- No invented QT thresholds or incidence statistics.

## Quality signals

- Orientee rescues breakthrough PONV with a different class, applies each agent's signature caution, and looks for a treatable nausea driver first.

## Verification

- [ ] Multimodal (different-class rescue) principle stated explicitly.
- [ ] Each covered class has a signature caution.
- [ ] Promethazine extravasation + scopolamine anticholinergic-delirium cautions present.
- [ ] Monitoring block has reassess interval + class-specific assessments.
- [ ] Red flags link trigger → escalation role.
- [ ] No doses/routes-by-number/concentrations anywhere.

## False-Positive Prevention

Do **not** fabricate or invent:

- **No antiemetic doses, concentrations, or numeric routes/intervals.** Per order only.
- **No invented QT thresholds** (e.g., specific QTc cutoffs) — describe the caution qualitatively.
- **No invented incidence statistics** for PONV, EPS, or extravasation — qualitative only.
- **No "always safe" language.**
- **No invented facility protocols, extravasation steps, or pager paths** — defer to facility.
- **No fabricated chapter/monograph citations.** Mark `{{confirm}}`.
- **No brand-only references** — name the class + a generic exemplar.

## Worked Example

<details>
<summary>Example: breakthrough PONV after a prophylactic 5-HT3 agent (click to expand)</summary>

```markdown
## Rescue by switching class

Your patient got a 5-HT3 antagonist for PONV prophylaxis in the OR and is now nauseated in PACU. The instinct is to give another dose of the same drug.

Instead, rescue with a **different class** per order — repeating the 5-HT3 within its window adds QT risk without much added benefit. Before dosing, check for a treatable driver: is she hypotensive, in pain, recently repositioned, hypoxic, or freshly opioid-dosed? Then, when you do give the rescue agent, apply its signature caution — if it's promethazine, use the extravasation precautions; if a scopolamine patch is already on, factor its anticholinergic load, especially if she's older. Reassess the nausea score 10–15 minutes after the dose.
```

Notes: different-class rescue, treatable-driver check, class-specific cautions, no doses, escalation by role.
</details>

## Self-check

- [ ] Different-class rescue principle taught.
- [ ] Each class has its signature caution.
- [ ] Monitoring block has interval + class-specific assessments.
- [ ] Red flags have escalation role.
- [ ] Safety reminder at top.
- [ ] No invented doses/QT thresholds/incidence/facility specifics.
- [ ] Verification + False-Positive Prevention passed.
