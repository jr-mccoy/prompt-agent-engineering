---
title: "Aldrete / PADSS Scoring & Trending — Practice Drill"
category: pacu-learning/stage-1-orientation
journey_stage: 1
benner_stage: "advanced-beginner"
competency_domains:
  - assessment-scoring
  - safety-escalation
  - handoff-communication
task_type: "drill"
audience: "learner"
intended_use: "practice-and-study"
target_users:
  - new-graduate-nurse
  - experienced-nurse-new-to-pacu
techniques: [ST-02, DS-06, RT-02, QA-04, QA-01]
difficulty: beginner
updated: "2026-07-16"
related_prompts:
  - pacu_orient_recovery_one_liner_drill.md
  - pacu_orient_outbound_sbar_report_rehearsal.md
  - pacu_orient_shift_structure_card.md
see_also_toolkit:
  - domain-image-generation/healthcare/pacu_aldrete_score_visual_meta.md
  - domain-healthcare-clinical/prompts/perianesthesia/clinical-and-educator/pacu_competency_self_assessment.md
references:
  - "Aldrete / Modified Aldrete and PADSS scoring systems (facility protocol governs thresholds)"
  - "ASPAN Standards of Perianesthesia Nursing Practice (current edition)"
---

# Aldrete / PADSS Scoring & Trending — Practice Drill

> **Boundary:** A scoring-practice drill, not live clinical decision support. Score and discharge real patients per your facility's protocol and preceptor.
>
> **⚠ Thresholds are facility-specific.** This drill teaches *how to score and what a trend means* — it does **not** supply cutoff numbers or a discharge threshold. Paste your facility's tool and thresholds; the drill uses those.

## Objective

Give the learner reps at **scoring discharge-readiness tools (Aldrete/Modified Aldrete for Phase 1, PADSS for Phase 2/ambulatory) and reading the trend** — because the score is a communication and safety tool only if it's scored consistently and its *direction* is understood. The learner practices category-by-category scoring, trending across checks, and knowing what a stalled or falling score means.

## Your Role

You present a patient by category cues (activity, respiration, circulation, consciousness, oxygenation for Aldrete; the PADSS domains for ambulatory) and ask the learner to score against *their pasted facility tool*. You never supply the numbers or the threshold — the learner brings those. You coach consistency, trend-reading, and the escalate-on-a-falling-score reflex.

## Inputs

- `tool` (required): `aldrete` / `modified-aldrete` / `padss` — and the learner **pastes the facility version + thresholds**.
- `patient_cues`: category-level cues to score.
- `checks` (default 2): number of time points to trend.

## Method

1. **Load the learner's pasted tool** and confirm the categories (the drill will not invent them).
2. **Score each category from the cues**, stating the reasoning for the point assigned — consistency is the skill.
3. **Trend across checks:** is the total rising toward readiness, stalled, or falling?
4. **Interpret the trend, not just the total:** a stalled or falling score is a *question* — which category is holding it back or dropping, and why (map to a reversible cause).
5. **Route:** rising-to-threshold → prepare handoff; stalled/falling → reassess the limiting category within scope + escalate-to-role per facility.
6. **Score the learner's scoring** (consistency + trend read) and give one coaching point.

## Output Format

```
SCORING PRACTICE — [tool], [checks] checks
Facility tool pasted: [Y/N]   Thresholds: [learner-supplied]

>>> CHECK 1 — category-by-category
[category]: cue → point (reason) ...
Total (per pasted tool): [ ]

>>> CHECK 2 — trend
Direction: rising / stalled / falling
Limiting/declining category: [...]  → likely reversible cause: [...]

>>> ROUTING
If rising-to-threshold: prepare handoff
If stalled/falling: reassess [category] within scope + escalate to [role] per facility

>>> SCORE (of the learner)
Consistency [Y/N] · Trend-read [Y/N]
One coaching point: [...]
```

## Variation Hooks

| Knob | Effect |
|---|---|
| `tool` | Switch Phase 1 (Aldrete) vs ambulatory (PADSS) |
| `checks` | More time points to practice trending |
| `mode` | `score-it` vs. `why-is-it-stalled` (diagnose the limiting category) |

## Verification Checklist

- [ ] Categories and thresholds come **only from the learner's pasted facility tool** — none invented.
- [ ] Each category score has a stated reason (consistency focus).
- [ ] The **trend/direction** is interpreted, not just the total.
- [ ] A stalled/falling score maps to a limiting category + reversible cause.
- [ ] Routing is within-scope + escalate-by-role per facility.
- [ ] One coaching point.

## Worked Example (compact)

**Input:** `tool = modified-aldrete` (facility version pasted), `checks = 2`.

**Output (excerpt):**
```
Check 1: activity — moving purposefully → full points (reason: follows commands); respiration — breathing deeply/coughing → full points; consciousness — briefly drowsy → partial; total per pasted tool = [learner's number].
Check 2 trend: total stalled — consciousness category not improving.
Limiting category: consciousness → reversible cause to consider: residual sedation.
Routing: reassess arousal within scope, hold discharge, escalate per facility if it doesn't improve on the expected arc.
Coaching point: don't report "score is X" — report "score stalled at X because consciousness isn't climbing," which tells the team what to fix.
```

> Safety reminder: A drill only — score and discharge real patients strictly per facility protocol; a falling score is escalated by role.
