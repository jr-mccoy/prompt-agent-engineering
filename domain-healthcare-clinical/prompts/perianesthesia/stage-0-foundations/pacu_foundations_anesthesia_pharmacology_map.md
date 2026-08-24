---
title: "Anesthesia Pharmacology Map — Agent Classes and How They Behave"
category: pacu-learning/stage-0-foundations
journey_stage: 0
benner_stage: "novice"
competency_domains:
  - pharmacology-reversal
  - neurologic-emergence
task_type: "primer"
audience: "learner"
intended_use: "practice-and-study"
target_users:
  - new-graduate-nurse
  - experienced-nurse-new-to-pacu
techniques: [ST-02, ED-02, DS-06, RT-02, QA-01]
difficulty: beginner
updated: "2026-07-16"
related_prompts:
  - pacu_foundations_anesthesia_types_primer.md
  - pacu_foundations_emergence_respiratory_physiology.md
  - pacu_foundations_vocabulary_acronym_builder.md
see_also_toolkit:
  - domain-healthcare-clinical/prompts/perianesthesia/clinical-and-educator/pacu_medication_profile.md
  - domain-healthcare-clinical/prompts/perianesthesia/clinical-and-educator/pacu_drug_naloxone.md
  - domain-healthcare-clinical/prompts/perianesthesia/clinical-and-educator/pacu_drug_sugammadex.md
  - domain-healthcare-clinical/prompts/perianesthesia/clinical-and-educator/pacu_drug_neostigmine_glycopyrrolate.md
references:
  - "ASPAN Core Curriculum for PeriAnesthesia Nursing Practice (current edition)"
  - "Drain's PeriAnesthesia Nursing (current edition) — pharmacology chapters"
---

# Anesthesia Pharmacology Map — Agent Classes and How They Behave

> **Boundary:** A conceptual study map, not live clinical decision support and not a dosing reference. Doses, concentrations, and reversal decisions belong to the provider order and facility protocol.

## Objective

Give the beginner a **class-level map** of the drugs a post-anesthesia patient arrives with — volatiles/inhaled agents, IV induction agents (e.g., propofol family), opioids, neuromuscular blocking agents (NMBs), and the **reversal agents** — organized by *what each class does* and *what its offset means for recovery*. This is the "why" scaffold under the toolkit's Drug Monograph Library; **no dose math lives here.**

## Your Role

You are building a mechanism map, not a med sheet. For each class you answer: *what does it do, why does it matter on emergence, and what's the nurse's observation/response?* Every dose, rate, or concentration is deliberately absent — you send the learner to the toolkit monographs and the facility's order for numbers.

## Inputs

- `classes`: default all (`inhaled, IV induction, opioids, NMBs, reversal agents`); or a subset.
- `pair_with_events` (optional, default true): link each class to the emergence problem it can cause.
- `prior_experience` (optional).

## Method

1. **For each class, give a plain "what it does" line** (sedation/analgesia/paralysis/reversal), defining acronyms.
2. **State the offset behavior qualitatively** — does it wear off fast or linger? Does it accumulate? (No half-life numbers — describe the *pattern*: "short-acting," "can outlast the surgery," "context-sensitive.")
3. **Map class → emergence consequence** the nurse watches for (e.g., opioids → sedation + respiratory drive; NMBs → residual weakness).
4. **For reversal agents, frame the nurse role**: reversal is *given by the provider/per order*; the nurse **monitors for adequacy of reversal and for re-sedation/re-curarization**, prepares equipment, and escalates. Name the beginner trap: "reversed once ≠ safe forever — watch for recurrence."
5. **Point every number to its home:** toolkit monograph or facility order.
6. **Close with the one habit:** know the *class behavior*; look up the *number*.

## Output Format

```
ANESTHESIA PHARMACOLOGY MAP (class-level, no doses)
Classes: [...]

For each class:
### [Class] (acronyms defined)
- What it does: [...]
- Offset behavior (qualitative): [...]
- Emergence consequence I watch for: [...]
- Nurse role: observe / monitor / prepare / assist / escalate — [specifics]
- Numbers live at: [toolkit monograph file | facility order]

>>> REVERSAL-AGENT SPECIAL NOTE
Given by: [provider / per order]. Nurse watches for: [adequacy + recurrence]. Escalate if: [...]

>>> THE ONE HABIT
Know the class behavior; look up the number. Never invent a dose.

Class I understand least right now: [ ]
```

## Variation Hooks

| Knob | Effect |
|---|---|
| `classes` | Focus one drug family |
| `pair_with_events` | Toggle class→emergence-problem links |
| `depth` | `orientation` (default) vs. `enriched` (adds receptor-level mechanism) |

## Verification Checklist

- [ ] Acronyms (NMB, IV) defined on first use.
- [ ] **Zero doses, rates, concentrations, or half-life numbers** anywhere — offset is described qualitatively only.
- [ ] Each class maps to a concrete emergence consequence the nurse observes.
- [ ] Reversal framed as provider-given / per order; nurse role is monitor + escalate (recurrence trap named).
- [ ] Every place a number *would* go points to a toolkit monograph or facility order.
- [ ] No provider-scope verbs (prescribe/titrate/order).

## Worked Example (compact)

**Input:** `classes = opioids, NMBs, reversal agents`.

**Output (excerpt):**
```
### Opioids
- What it does: analgesia (pain relief), with sedation as a companion effect.
- Offset behavior: varies by agent — some short-acting, some linger; effect can stack with residual anesthetic.
- Emergence consequence I watch for: sedation + reduced respiratory drive (a *trend* toward slower/shallower effort).
- Nurse role: observe drive and arousal, oxygen per order, stimulate, prepare, escalate for the comfort/sedation balance.
- Numbers live at: toolkit pacu_drug_analgesics_reference.md + facility order.

### Reversal agents (special note)
Given by provider / per order. Nurse watches for adequacy of reversal AND recurrence (re-sedation / re-weakening after an initial improvement). Escalate if effort or arousal backslides.
The trap: "reversed once ≠ safe forever."
```

> Safety reminder: A class-level map only — every dose and reversal decision comes from the provider order, toolkit monograph, and facility protocol.
