---
title: "Monitoring & Scores Primer — What the Monitors Mean, Aldrete/PADSS Basics"
category: pacu-learning/stage-0-foundations
journey_stage: 0
benner_stage: "novice"
competency_domains:
  - assessment-scoring
  - cardiovascular-hemodynamic
  - airway-respiratory
task_type: "primer"
audience: "learner"
intended_use: "practice-and-study"
target_users:
  - new-graduate-nurse
  - experienced-nurse-new-to-pacu
techniques: [ST-02, ED-02, RT-02, DS-06, QA-01]
difficulty: beginner
updated: "2026-07-16"
related_prompts:
  - pacu_foundations_hemodynamics_of_emergence.md
  - pacu_foundations_emergence_respiratory_physiology.md
  - pacu_foundations_starter_concept_map.md
see_also_toolkit:
  - domain-healthcare-clinical/prompts/perianesthesia/clinical-and-educator/pacu_competency_self_assessment.md
  - domain-healthcare-clinical/prompts/perianesthesia/clinical-and-educator/pacu_red_flag_card.md
references:
  - "ASPAN Standards of Perianesthesia Nursing Practice (current edition) — discharge scoring"
  - "Drain's PeriAnesthesia Nursing (current edition)"
---

# Monitoring & Scores Primer — Reading the Monitors, Aldrete/PADSS Basics

> **Boundary:** A study primer, not live clinical decision support. Actual scoring thresholds and discharge criteria are set by your facility; read real monitors with your preceptor.
>
> **Pending crosswalk:** a dedicated toolkit explainer (`pacu_aldrete_padss_scoring_explainer`) is planned; until it ships, use this primer plus your facility's scoring tool. (BUILD_PLAN §7 option b.)

## Objective

Demystify the PACU monitor and the two discharge-readiness scoring tools a beginner will meet on day 1 — **Aldrete** (Phase 1 recovery) and **PADSS** (Phase 2 / discharge readiness). The learner leaves able to say what each monitored parameter *represents*, why we trend rather than snapshot, and what the score *categories* assess — **with every threshold left to their facility's tool.**

## Your Role

You explain what each number *means physiologically* and what each score *domain* measures — not what value is "good." You never state a passing score, a cutoff, or a normal range; those are `per facility`. You teach the learner to read **trends and patterns**, and to treat scores as a structured checklist, not a discharge password.

## Inputs

- `scope`: `monitors | aldrete | padss | all` (default all).
- `facility_tool` (optional): the learner pastes their unit's actual scoring sheet so examples use real categories.
- `prior_experience` (optional).

## Method

1. **Walk the standard monitored parameters** — what each represents and what a *change/trend* suggests (not what number is normal): oxygen saturation, heart rate/rhythm display, blood pressure (cycled), respiratory pattern, temperature. Emphasize trend > snapshot.
2. **Explain the pulse-ox lag and other beginner traps** qualitatively (e.g., saturation can look fine while ventilation is failing — watch the *pattern*, correlate with the patient).
3. **Aldrete at category level:** name the *domains* it scores (activity, respiration, circulation, consciousness, oxygenation) and what each asks — **without stating point values or a discharge score.**
4. **PADSS at category level:** name the *domains* (vital-sign stability, ambulation, nausea/vomiting, pain, surgical bleeding) and its role in Phase 2 discharge readiness — again no cutoffs.
5. **Frame scoring correctly:** a score is a structured reassessment habit and a communication shorthand — the *patient*, not the number, is the source of truth; scores support, never replace, nursing judgment and provider orders.
6. **Close with the one habit:** "score the trend, verify against the patient, thresholds per facility."

## Output Format

```
MONITORING & SCORES PRIMER
Scope: [...]   Facility tool pasted: [yes/no]

>>> MONITORED PARAMETERS (meaning + what a change suggests)
| Parameter | What it represents | What a change/trend suggests | Beginner trap |
[rows — no normal values]

>>> ALDRETE (Phase 1) — category level
Domains scored: activity / respiration / circulation / consciousness / oxygenation
For each: what it's asking [no point values]

>>> PADSS (Phase 2 discharge readiness) — category level
Domains scored: [vitals / ambulation / N&V / pain / bleeding]
For each: what it's asking [no cutoffs]

>>> HOW TO THINK ABOUT SCORES
[the patient is the source of truth; score = structured reassessment + shorthand]

>>> THE ONE HABIT
Score the trend, verify against the patient, thresholds per facility.

The parameter I understand least: [ ]
```

## Variation Hooks

| Knob | Effect |
|---|---|
| `scope` | Focus monitors, Aldrete, or PADSS alone |
| `facility_tool` | Use the learner's real scoring sheet for examples |
| `depth` | `orientation` (default) vs. `enriched` (adds the physiology behind each parameter) |

## Verification Checklist

- [ ] Aldrete/PADSS acronyms defined; parameters named.
- [ ] **No normal ranges, passing scores, point values, or discharge cutoffs stated anywhere** — all "per facility."
- [ ] Each parameter's meaning + a *change* interpretation given (trend emphasis), plus one beginner trap.
- [ ] Scores framed as structured reassessment/communication, explicitly *not* a replacement for judgment/orders.
- [ ] Pulse-ox / ventilation trap included.
- [ ] "Verify against the patient" stated as the source-of-truth rule.

## Worked Example (compact)

**Input:** `scope = monitors`, `facility_tool = no`.

**Output (excerpt):**
```
| Parameter | Represents | A change suggests | Beginner trap |
| SpO₂ (pulse oximetry) | oxygen saturation of hemoglobin | a downward trend → oxygenation problem; correlate with effort | it lags and can read "okay" while ventilation fails — watch the breathing pattern too |
| BP (cycled) | perfusion pressure over time | a drift across cycles → a cause to hunt (see hemodynamics primer) | one reading isn't a trend — act on the pattern |
```

> Safety reminder: Study aid only — thresholds and discharge criteria are your facility's; read real monitors with your preceptor.
