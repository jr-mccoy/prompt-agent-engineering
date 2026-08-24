---
title: PACU Medication Profile
category: pacu/pharmacology
task_type: CREATE
audience: PACU nurse (novice to experienced)
updated: "2026-04-16"
tags:
  - pacu
  - pharmacology
  - medication-profile
techniques:
  - ST-01
  - ST-02
  - RT-02
  - QA-02
  - ED-02
  - DS-06
difficulty: intermediate
related_prompts:
  - ../../domain-healthcare-clinical/prompts/nursing_medication_administration_safety.md
  - ../../domain-healthcare-clinical/prompts/medicine_medication_reconciliation.md
  - prompts/pacu_topic_primer.md
  - prompts/pacu_red_flag_card.md
  - prompts/pacu_complication_deep_dive.md
references:
  - Drain's PeriAnesthesia Nursing Practice (7th ed.) — pharmacology chapters
  - ASPAN Standards of Perianesthesia Nursing Practice
  - Hospital pharmacy monograph (facility-specific; confirm current version)
---

# PACU Medication Profile

> Safety reminder: Educational reference only — every dose, route, and interval is confirmed by provider order and facility protocol before administration.

## Objective

Produce a **single-medication profile** optimized for PACU relevance: mechanism, PACU-visible effects, monitoring, common interactions, and reversal/antagonist (where applicable).

## Inputs

- **Medication (generic name):** {{...}}
- **Context of use in PACU:** {{e.g., reversal agent, analgesic adjunct, antiemetic, hemodynamic}}
- **Source chapters:** {{Drain's pharm chapter; hospital pharmacy monograph}}

## Audience

- PACU nurses of any experience level.
- Assumes baseline pharmacology; does not re-teach receptor basics unless relevant.

## Output requirements

```markdown
# {Generic name} — PACU Profile

> Safety reminder: Verify dose, route, and contraindications against provider order and pharmacy monograph.

## Class & mechanism
- Class: ...
- How it works: ... (1–3 sentences, mechanism-level)

## PACU-relevant effects
- Therapeutic effects you want to see: ...
- Adverse effects you watch for: ...
- Onset / peak / duration: ... (cited; or "per pharmacy monograph")

## Dose (reference only — order and facility protocol govern)
- Typical adult IV (per source): {{range}} — source cited
- Common pediatric (per source): {{range}} or "per order"
- Any dose > threshold → escalate per facility

## Monitoring in PACU
- Every {{interval}}: VS, ...
- Specific assessment: ...
- When to reassess: ... min after dose

## Reversal / antagonist (if applicable)
- Agent: ...
- Class: ...
- Pairing rationale: ...

## Common interactions / cautions in PACU
- With {drug class}: ...
- In {patient population}: ...
- With {anesthesia technique}: ...

## Red flags that require escalation
- ... → call {role}
- ... → call {role}

## Teaching pearls
- ...

## Sources
- *Drain's PeriAnesthesia Nursing*, Ch. XX
- Hospital pharmacy monograph (facility-specific; confirm current version)
```

## Must / Must not

**Must:**
- Dose ranges quoted from source with citation, or marked *per order*.
- Onset / peak / duration cited or marked *per pharmacy monograph*.
- ≥ 2 red-flag escalation rows.
- Reversal section included whenever a reversal agent exists — even if only to state "no reversal".

**Must not:**
- No unsourced doses.
- No facility-specific concentrations (those vary by pharmacy).
- No "always safe" language.

## Quality signals

- A nurse receiving a new order for this med would know what to watch for in the next 30 minutes.
- Red flags link directly to an escalation role.
- Reversal pairing is unambiguous.

## Verification

Before returning, verify:

- [ ] Every numeric dose value carries either a source citation (chapter + section) or is replaced by "per order."
- [ ] Onset / peak / duration values are cited, or explicitly deferred to "per pharmacy monograph."
- [ ] Monitoring block specifies an interval AND the specific assessment (not just "monitor VS").
- [ ] Reversal section is always present — even if only to state "no pharmacologic reversal available."
- [ ] Red flag rows link trigger → escalation role (by role, not name, not pager).
- [ ] No "always safe" or "completely reversible" language.

## False-Positive Prevention

Do **not** fabricate:

- **No invented dose ranges.** If the source chapter doesn't give one, write "per order" or "per pharmacy monograph." Do not interpolate from general pharmacology knowledge.
- **No invented onset / peak / duration figures.** If not in source, defer to pharmacy monograph.
- **No invented facility-specific concentrations** (e.g., "100 mcg/mL" fentanyl). Concentrations vary by pharmacy — never assume.
- **No invented pediatric dose ranges.** Always mark "per order" for pediatric unless source is pediatric-specific and cited.
- **No invented drug-drug interaction rates or severity** — describe the class interaction qualitatively and defer specifics to pharmacy.
- **No invented contraindication thresholds** (e.g., "avoid if CrCl < 30") unless source supplies them.
- **No fabricated pharmacy monograph quotations.** If a line reads like it's from a monograph, it must actually be from a sourced reference.
- **No brand-name-only references** without the generic name; brand availability varies.

## Worked Example

<details>
<summary>Example: Medication = Ondansetron (click to expand, abbreviated)</summary>

```markdown
# Ondansetron — PACU Profile

> Safety reminder: Verify dose, route, and contraindications against provider order and pharmacy monograph.

## Class & mechanism
- Class: 5-HT3 receptor antagonist.
- How it works: Blocks serotonin (5-HT3) receptors centrally (chemoreceptor trigger zone) and peripherally (GI vagal afferents) — reducing post-op nausea and vomiting signaling.

## PACU-relevant effects
- Therapeutic effects you want to see: reduced nausea, reduced emesis, patient tolerating oral intake if discharge goal.
- Adverse effects you watch for: headache, constipation, QT prolongation (class effect — check recent ECG / potassium trend if available per order), rare hypersensitivity.
- Onset / peak / duration: per pharmacy monograph — typically rapid IV onset; defer specifics.

## Dose (reference only — order and facility protocol govern)
- Typical adult IV: per order (commonly cited range in pharmacy monograph; confirm per facility).
- Pediatric: per order, weight-based.
- Any dose above facility max → confirm with provider before administration.

## Monitoring in PACU
- Every 15 min × 2, then per facility PACU policy: nausea score, VS, HR trend.
- Specific assessment: ask patient about nausea intensity and new-onset headache.
- Reassess 10–15 min after dose: response or need for rescue agent per order.

## Reversal / antagonist
- No pharmacologic reversal. Supportive management if adverse effect emerges.

## Common interactions / cautions in PACU
- With other QT-prolonging agents: additive risk — confirm with pharmacy/provider before combining.
- With serotonergic agents (e.g., tramadol, SSRI): serotonin-syndrome risk — rare but relevant in polypharmacy.
- With known QT prolongation / hypokalemia: caution — per order.

## Red flags that require escalation
- New or worsening palpitations, syncope, or dysrhythmia on monitor → call anesthesiologist / rapid response per facility.
- Hypersensitivity reaction (rash, wheeze, facial swelling) → call anesthesiologist on call immediately; prepare airway support.

## Teaching pearls
- Works best given before nausea becomes severe; don't wait for emesis to dose.
- If ineffective after one dose, escalate to a different class rather than repeating same agent.

## Sources
- *Drain's PeriAnesthesia Nursing*, Ch. on PONV Management
- Hospital pharmacy monograph (facility-specific; confirm current version)
```

Notes: no specific mg dose written (all "per order" or "per monograph"); onset/peak/duration deferred to monograph; reversal section explicitly states "none"; red flags link to roles.
</details>

## Self-check

- [ ] Doses sourced or marked *per order*.
- [ ] Onset/peak/duration present.
- [ ] Monitoring block has an interval and specific assessment.
- [ ] Red flags have escalation role.
- [ ] Reversal section present (agent or explicit "no reversal").
- [ ] Safety reminder at top.
- [ ] Verification section passed.
- [ ] False-Positive Prevention section passed — no invented doses, concentrations, interactions, or monograph quotes.
