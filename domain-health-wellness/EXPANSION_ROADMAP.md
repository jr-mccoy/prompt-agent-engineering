# Expansion Roadmap — `domain-health-wellness/`

**Status as of 2026-09-24:** Wave 1 shipped (coverage roadmap) — 8 prompts across
`foundations/`, `fitness/`, `nutrition/`, and `sleep-recovery/`, built from the
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

## Wave 2 — candidates

| Candidate | Folder | Guard note |
|---|---|---|
| Mobility and flexibility routine | `fitness/` | Healthy adults only; no rehab; pain routes out |
| Return to activity after a break (illness, travel, life event — not injury) | `fitness/` | Re-runs the readiness screen first; injury returns go to a clinician |
| Active ageing for older adults | `fitness/` | Requires clinician clearance recorded in the profile; balance and falls framed with the clinician's limits |
| Hydration and heat | `nutrition/` or `sleep-recovery/` | Heat-illness warning signs route to urgent care; no electrolyte or supplement dosing |

## Explicitly not planned

- Rehabilitation, condition-specific diets, supplement or medication guidance, and any
  content for minors or pregnancy — these belong with clinicians, not in a self-use domain.
- Weight-loss programmes with targets — incompatible with the nutrition STRONG-GUARD.
