---
title: PACU Hypothermia & Post-Anesthetic Shivering — Recognition & Response
category: pacu/complications
task_type: LEARN
audience: PACU orientee (any phase) or preceptor for huddle
updated: "2026-07-06"
tags:
  - pacu
  - hypothermia
  - shivering
  - thermoregulation
  - normothermia
techniques:
  - ST-01
  - ST-02
  - RT-02
  - QA-02
  - ED-02
  - DS-06
difficulty: beginner
related_prompts:
  - pacu_complication_deep_dive.md
  - pacu_delayed_emergence.md
  - pacu_geriatric_considerations.md
  - pacu_dysrhythmia_recognition.md
  - pacu_red_flag_card.md
references:
  - Drain's PeriAnesthesia Nursing Practice (7th ed.) — thermoregulation chapters
  - ASPAN Standards of Perianesthesia Nursing Practice
  - ASPAN Clinical Practice Guideline for the Promotion of Perioperative Normothermia
  - ASPAN Core Curriculum for PeriAnesthesia Nursing Practice
---

# Hypothermia & Post-Anesthetic Shivering — PACU Deep Dive

> Safety reminder: Perioperative hypothermia is common, consequential, and treatable. Active-warming methods and any pharmacologic shivering management are per facility protocol / provider order. Temperature thresholds are per the facility normothermia policy; this prompt states no specific values. See `../SAFETY_PREAMBLE.md`.

## Objective

Produce a structured deep dive on perioperative hypothermia and post-anesthetic shivering. Teaching goals: (1) hypothermia carries real consequences beyond discomfort, (2) shivering is not always caused by being cold, and (3) active warming is a standard intervention, not an optional comfort measure.

## Inputs

- **Your facility's normothermia policy source:** {{ASPAN normothermia guideline as adapted by facility}}
- **Active-warming methods available:** {{forced-air warmer, warmed blankets, warmed IV fluids per order}}
- **Source chapters:** {{Drain's thermoregulation chapters, ASPAN normothermia guideline}}

## Audience

- Orientee at any phase — thermoregulation is a core PACU competency.
- Preceptor building a normothermia huddle.

## Output requirements

```markdown
# Hypothermia & Post-Anesthetic Shivering — PACU Deep Dive

> Safety reminder: Active warming per facility; shivering pharmacology per order. Temperature thresholds per facility normothermia policy.

## Why it matters
[One paragraph — hypothermia increases oxygen demand (shivering), impairs coagulation and drug metabolism, delays emergence, raises wound-infection and cardiac risk, and is uncomfortable. Normothermia is an active goal.]

## Pathophysiology
[2–4 sentences: anesthesia impairs central thermoregulation and causes vasodilation/redistribution; cold OR environment and exposure add heat loss. Shivering raises metabolic rate and O₂ consumption sharply.]

## Setup (who and when)
- Long cases, large exposed surface area, cold irrigation/fluids, older adults, low body mass, neuraxial anesthesia (impaired thermoregulation below the block).

## Early cues
- Measured temperature trending below the facility normothermia range.
- Cool skin, patient reports feeling cold, peripheral vasoconstriction/pallor.
- Onset of shivering.

## Consequences to watch
- Increased O₂ demand and myocardial work from shivering (risk in cardiac patients).
- Coagulation impairment, delayed emergence, prolonged drug effect, discomfort.

## Shivering is not always "cold"
| Cause of shivering | How to tell |
|---|---|
| True hypothermia | Low measured temp; cool skin; responds to warming |
| Post-anesthetic tremor (normothermic) | Can occur at near-normal temp; still raises O₂ demand |
| Early transfusion / drug reaction | Temporal link to transfusion/drug; other reaction signs |
| Early sepsis / rigors | Fever context, source, trajectory |
| Pain / anxiety | Behavioral context |

## Immediate management
1. Measure temperature per facility method → establish trend.
2. Begin active warming per facility (forced-air warmer, warmed blankets); warmed IV fluids per order → reassess temp per facility interval.
3. For significant shivering: apply O₂ per order (metabolic demand ↑); notify {provider by role} for pharmacologic shivering management per order → reassess after intervention.
4. Reduce heat loss: cover head/exposed areas, warm environment.

## Escalation
- Call {provider by role} for shivering not settling with warming, or hypothermia with cardiac/hemodynamic concern.
- Consider other causes (transfusion/drug reaction, sepsis) if shivering is atypical → escalate accordingly.

## Pharm / equipment likely used
- Forced-air warmer, warmed blankets, warmed IV fluids (per order).
- Anti-shivering medication if ordered (per order — no dose here).
- Supplemental O₂ for increased demand.

## After it resolves
- Continue temperature monitoring to confirmed normothermia per facility.
- Charting: temps/trend, warming measures, shivering management, response.
- Handoff: current temp and warming status.

## Teaching pearls
- Shivering can spike O₂ demand — treat it, and give O₂, even in a "just cold" patient.
- Not all shivering is hypothermia; consider transfusion/drug reaction and sepsis when it doesn't fit.

## Common orientee mistakes
- Treating hypothermia as pure comfort and under-using active warming.
- Assuming every shiver means "cold" and missing a reaction or early sepsis.

## Sources
- ...
```

## Must / Must not

**Must:**
- Frame hypothermia consequences beyond comfort (O₂ demand, coagulation, emergence, infection, cardiac).
- Include the "shivering isn't always cold" differential.
- Frame active warming as standard; shivering pharmacology per order.

**Must not:**
- No specific temperature thresholds — "per facility normothermia policy."
- No anti-shivering drug doses — "per order."
- No invented incidence statistics.
- No scope creep; no facility-specific protocol/pager invented.

## Quality signals

- Orientee treats hypothermia actively and gives O₂ for shivering demand.
- Orientee considers non-cold causes of shivering.

## Verification

- [ ] Consequences beyond comfort stated.
- [ ] "Shivering isn't always cold" differential present (≥ 2 alternatives).
- [ ] Active warming framed as standard; pharmacology per order.
- [ ] Management steps have reassess intervals; escalation by role.
- [ ] No specific temperature thresholds stated.

## False-Positive Prevention

Do **not** fabricate or invent:

- **No specific temperature thresholds or normothermia cutoffs.** Per facility policy.
- **No anti-shivering drug doses.** Per order.
- **No invented incidence statistics.** Describe qualitatively.
- **No invented facility warming protocols, device settings, or pager paths.**
- **No fabricated chapter/guideline citations.** Mark `{{confirm}}`.
- **No scope creep.**

## Worked Example

<details>
<summary>Example: "Shivering is not always cold" reasoning (click to expand)</summary>

```markdown
## Shivering is not always "cold"

A patient begins shivering 20 minutes into recovery. Your first move is to measure the temperature and start active warming — but also to think about what else fits:

- Temp is at the low end but the patient just started a blood transfusion 10 minutes ago and now has flushing → consider a transfusion reaction; stop per facility protocol and escalate, don't just pile on blankets.
- If temp is clearly low, skin is cool, and there's no reaction context → treat as hypothermia: active warming per facility, warmed fluids per order, O₂ for the increased demand, and reassess temp on the facility interval.
```

Notes: warming started, but non-cold causes considered; O₂ given for shivering demand; no temperature thresholds or drug doses invented; escalation by role.
</details>

## Self-check

- [ ] Consequences beyond comfort taught.
- [ ] Non-cold causes of shivering considered.
- [ ] Active warming standard; pharmacology per order.
- [ ] Reassess intervals + escalation by role.
- [ ] No invented thresholds/doses/facility specifics.
- [ ] Safety reminder at top.
- [ ] Verification + False-Positive Prevention passed.
