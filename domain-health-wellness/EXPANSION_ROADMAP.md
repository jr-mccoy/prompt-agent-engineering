# Expansion Roadmap — `domain-health-wellness/`

**Status as of 2026-10-03:** Waves 1, 2 and 3 shipped — 13 prompts across
`foundations/`, `fitness/`, `nutrition/`, and `sleep-recovery/`. Wave 1 was built from the
`domain-health-wellness/` row of [`../meta/COVERAGE_ROADMAP.md`](../meta/COVERAGE_ROADMAP.md).
That file is the authoritative source for scope and guards; this one records local status.

**Guard carried into every wave:** the Safety Guard in [`README.md`](README.md) is
load-bearing. Any new prompt opens with the Readiness gate block and consumes the Readiness
Profile from `foundations/wellness_readiness_and_red_flag_screen.md`; anything touching
eating carries the STRONG-GUARD block.

## Wave 1 — shipped

| Subdirectory | Prompts |
|---|---|
| `foundations/` | `wellness_readiness_and_red_flag_screen.md` (entry gate), `wellness_sustainable_routine_designer.md` |
| `fitness/` | `fitness_beginner_training_plan.md`, `fitness_program_progression_review.md`, `fitness_endurance_event_build_plan.md` |
| `nutrition/` | `nutrition_eating_pattern_audit.md`, `nutrition_meal_structure_planner.md` (both STRONG-GUARD) |
| `sleep-recovery/` | `sleep_routine_and_environment_audit.md` |

## Wave 2 — shipped (2026-10-02)

| Prompt | Folder | Guard as built |
|---|---|---|
| `fitness_mobility_and_flexibility_routine.md` | `fitness/` | Per-area pain screen after the readiness gate; painful, numb, unstable, or recently injured areas get no routine; no rehab |
| `fitness_return_after_break_plan.md` | `fitness/` | Enumerated events void the pre-break profile and force a re-screen; injury returns, post-viral chest symptoms, and post-effort crashes route to a clinician |
| `fitness_active_ageing_plan.md` | `fitness/` | Falls screen (STEADI key questions + dizziness on standing + osteoporosis/fragility fracture) → CLINICIAN-FIRST; GO-WITH-LIMITS runs only with clinician limits recorded verbatim; power work only under GO or explicit clinician agreement |
| `nutrition_hydration_and_heat_plan.md` | `nutrition/` | STRONG-GUARD (adds fluid restriction, deliberate dehydration, water-loading to suppress hunger); heat-illness and over-drinking signs → emergency, given even when the guard fires; no electrolyte, salt, supplement, or fixed-volume numbers; no weighing |

## Wave 3 — shipped (2026-10-03, coverage Wave 9)

| Prompt | Folder | Guard as built |
|---|---|---|
| `sleep_shift_work_and_jet_lag_timing_plan.md` | `sleep-recovery/` | Readiness gate; drowsy driving or dozing at work, apnea signs, the insomnia pattern (CBT-I prompt only with or after clinician review), bipolar or seizure disorder, and clock-timed medicines across time zones route out before any plan; no melatonin, sleep-aid, stimulant, or medication timing; meal timing routed to the STRONG-GUARD planner. Distinct from `sleep_routine_and_environment_audit.md` (ordinary schedule) |

## Explicitly not planned

- Rehabilitation, condition-specific diets, supplement or medication guidance, and any
  content for minors or pregnancy — these belong with clinicians, not in a self-use domain.
- Weight-loss programmes with targets — incompatible with the nutrition STRONG-GUARD.
