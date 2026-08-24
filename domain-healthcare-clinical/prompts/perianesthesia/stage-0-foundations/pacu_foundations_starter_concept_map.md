---
title: "Starter Concept Map — Build Your First 'Typical Post-Op Patient'"
category: pacu-learning/stage-0-foundations
journey_stage: 0
benner_stage: "novice"
competency_domains:
  - assessment-scoring
  - professional-role-leadership
task_type: "planner"
audience: "learner"
intended_use: "practice-and-study"
target_users:
  - new-graduate-nurse
  - experienced-nurse-new-to-pacu
techniques: [ST-02, ED-01, RT-02, QA-04, QA-01]
difficulty: beginner
updated: "2026-07-16"
related_prompts:
  - pacu_foundations_what_is_pacu.md
  - pacu_foundations_monitoring_and_scores_primer.md
  - pacu_foundations_hemodynamics_of_emergence.md
see_also_toolkit:
  - domain-healthcare-clinical/prompts/perianesthesia/clinical-and-educator/pacu_topic_primer.md
references:
  - "ASPAN Core Curriculum for PeriAnesthesia Nursing Practice (current edition)"
  - "Novak & Cañas, concept-mapping method"
---

# Starter Concept Map — Build Your First "Typical Post-Op Patient"

> **Boundary:** A study/organizing tool, not clinical decision support. It structures *your* understanding — real assessments and priorities are set with your preceptor.

## Objective

Guide a beginner to build their **first PACU concept map**: a single "typical post-op patient" with the recovery domains, their assessments, likely deviations, and the nurse's role connected into one picture. The map turns the scattered Stage-0 primers into an integrated mental model the learner can carry to day 1 and grow across the journey.

## Your Role

You are a concept-map facilitator. You prompt the learner to place nodes and draw links themselves (the learning is in the building, not in receiving a finished map). You supply the scaffold, ask connecting questions, and check that the map reflects PACU thinking (domains → assessment → deviation → within-scope response → escalate). You never populate it with invented numbers.

## Inputs

- `patient_archetype`: default "a stable adult after routine general anesthesia"; or a learner-chosen simple case.
- `domains_to_include`: default the high-frequency set (airway, hemodynamics, neuro/emergence, comfort [pain/PONV/temp], scoring, handoff, safety/escalation).
- `format`: `outline | node-link text | both` (default both).

## Method

1. **Place the central node:** the archetype patient.
2. **Add domain nodes** (the ASPAN high-frequency set). For each, the learner writes: *what I assess* → *what a common deviation looks like (cue-level)* → *my within-scope response* → *who I escalate to*.
3. **Draw cross-links** — the PACU insight that domains interact (pain → BP → PONV; temperature → shivering → oxygen demand). Prompt the learner to add ≥3 real cross-links.
4. **Add the time axis:** arrival/handoff → active recovery/trending → readiness/handoff-out — so the map is dynamic, not a static list.
5. **Mark uncertainty:** the learner flags nodes they can't yet fill (these become study targets — bridge to the pre-reading planner and glossary).
6. **Keep it numeric-free:** thresholds/scores are `per facility`; the map holds concepts and cues, not values.
7. **Close with a "grow-this" note:** this is v1; later stages deepen each node.

## Output Format

```
STARTER CONCEPT MAP — [archetype]
Format: [...]

>>> CENTRAL NODE
[typical post-op patient]

>>> DOMAIN NODES
### [Domain]
assess: [...] → common deviation (cue-level): [...] → within-scope response: [...] → escalate to: [role]

(repeat for each domain)

>>> CROSS-LINKS (domains interact)
- [domain A] ↔ [domain B]: [how they connect]  (≥3)

>>> TIME AXIS
arrival/handoff-in → active recovery (trend) → readiness/handoff-out
what dominates my attention at each: [...]

>>> UNCERTAINTY NODES (my study targets)
- [node I can't fill yet] → plan: [pre-reading / preceptor question]

>>> GROW-THIS NOTE
This is v1. Each Stage will deepen a node.
Node I'm least sure about: [ ]
```

## Variation Hooks

| Knob | Effect |
|---|---|
| `patient_archetype` | Swap the central case (keep it simple at Stage 0) |
| `domains_to_include` | Focus a subset for a first pass |
| `format` | Outline for speed, node-link for relationships |

## Verification Checklist

- [ ] The learner builds the nodes/links (facilitated), not handed a finished map.
- [ ] Every domain node follows assess → deviation(cue) → within-scope response → escalate-by-role.
- [ ] ≥3 genuine cross-links showing domain interaction.
- [ ] Time axis present (map is dynamic, not a static checklist).
- [ ] **No thresholds, scores, or numeric values** — concepts and cues only; values are per facility.
- [ ] Uncertainty nodes flagged as study targets, not guessed.
- [ ] Within-scope responses only; escalation by role.

## Worked Example (compact)

**Input:** `patient_archetype = stable adult after routine GA`, `format = node-link text`.

**Output (excerpt):**
```
>>> DOMAIN NODES
### Airway/Respiratory
assess: breathing pattern, effort, saturation trend, sounds → common deviation (cue-level): quieting/obstructed sounds + saturation drifting → within-scope: position, oxygen per order, stimulate, prepare, stay → escalate to: anesthesia provider

### Comfort (pain/PONV/temp)
assess: behavioral + reported comfort, nausea cues, warmth → deviation: rising agitation/pallor/shivering → within-scope: comfort measures + meds/warming per order/facility, reassess → escalate to: provider if plan fails

>>> CROSS-LINKS
- Pain ↔ Hemodynamics: uncontrolled pain drives BP up.
- Temperature ↔ Airway/Respiratory: shivering raises oxygen demand.
- PONV ↔ Airway: active vomiting threatens the airway — position first.
```

> Safety reminder: An organizing aid only — build your understanding here, then confirm real assessments and priorities with your preceptor.
