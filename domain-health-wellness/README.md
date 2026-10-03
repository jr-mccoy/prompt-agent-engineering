# Domain: Health & Wellness (Healthy Adults — Training, Eating, Sleep)

Thirteen prompts for a **healthy adult looking after their own body**: starting to train,
returning after a break, building toward a first event, staying strong and steady in
later life, working on mobility, reading a training log, auditing and structuring what
they eat, drinking and training through heat, fixing the routine and bedroom
factors that cost them sleep, and timing sleep around night shifts and time-zone travel. The person
holds the prompt; the subject is their own training, eating, and sleep.

The domain is built around one idea: **a precise gate, then genuinely useful content.**
Every prompt starts from the same Readiness Profile. If the profile says *go*, the prompts
give specific, practitioner-grade guidance — RPE targets, progression rules, ramp limits,
plate portions, sleep-timing experiments — without burying it in disclaimers. If the
profile says *not yet*, nothing is produced except the route to the right person.

> ## Safety Guard — load-bearing, read before extending this domain
>
> This domain is registered as **safety-sensitive** and is served safety-gated. These rules
> apply to every prompt in it and to every prompt added later.
>
> 1. **The readiness screen runs first.** `foundations/wellness_readiness_and_red_flag_screen.md`
>    is the entry gate. Every other prompt opens with a *Readiness gate* block that consumes
>    its Readiness Profile, or asks its questions, before doing anything else.
> 2. **Five routes, fixed rules.** `URGENT-CARE-NOW` (chest pain or pressure, fainting,
>    sudden severe breathlessness, stroke signs → emergency services, stop) ·
>    `CLINICIAN-FIRST` (exertional symptoms; known heart, lung, kidney, liver, or metabolic
>    disease without clearance; pregnancy or postpartum; recent surgery or movement-changing
>    injury; heart-rate or blood-sugar medication) · `OUT-OF-SCOPE` (under 18; a goal of
>    treating a diagnosed condition) · `GO-WITH-LIMITS` · `GO`. The first three produce
>    **no plan of any kind** — no "gentle version", no workaround until the appointment.
> 3. **Clinician limits bind verbatim.** Once a clinician has set limits, they are copied
>    into the profile word-for-word and no later prompt may loosen them.
> 4. **No diagnosis, no treatment of diagnosed conditions, no medication or supplement
>    dosing.** Symptoms are never interpreted ("probably reflux"); they are routed.
> 5. **Minors and pregnancy:** "see a clinician" is the whole answer.
> 6. **Nutrition is STRONG-GUARD.** All three `nutrition/` prompts carry a `> **STRONG-GUARD
>    prompt.**` block and stop — not soften — on restriction, compensation, rapid
>    weight-loss goals (more than ~1% of body weight a week, or an intake below the
>    commonly cited ~1,200 / ~1,500 kcal unsupervised floors — conservative guard
>    triggers, not clinical targets), minors, pregnancy or breastfeeding, or a
>    diagnosed condition. They never set a calorie target. The
>    redirect is short and kind, names a clinician and registered dietitian, and gives
>    the crisis route (`domain-psychology/client-self-use/crisis-self-triage/clientself_am_i_in_crisis_self_triage.md`;
>    988 in the US) if the person feels unsafe.
> 7. **Pain is not a training problem.** Sharp or joint pain, pain that changes movement,
>    bone-spot pain, or very dark urine with severe muscle pain after a hard session route
>    out of the fitness prompts (the last one to same-day urgent care).
> 8. **Sleep disorders are referrals.** Snoring with witnessed pauses, dozing while
>    driving, and a chronic insomnia pattern go to a clinician (insomnia to the CBT-I
>    prompt only with or after clinician review — sleep restriction raises daytime
>    sleepiness) before any sleep-hygiene advice. Only for the insomnia pattern may the
>    routine audit run alongside that referral.
> 9. **Dual failure is a defect in both directions.** Softening a flag into a modified plan
>    is harmful; padding a clean GO with warnings trains people to ignore warnings. Each
>    prompt checks for both (QA-20 where listed).

---

## What this domain covers

- **Foundations** — the readiness and red-flag gate, and a weekly routine that fits
  training, an eating rhythm, and a sleep anchor into measured capacity.
- **Fitness** — an eight-week beginner plan, a log-based progression review (stalls,
  overreaching, deloads), a first-event endurance build (5K to century ride), a mobility
  and flexibility routine, a return-after-a-break plan (deconditioning, not injury), and
  an active ageing plan for older adults (falls screen, balance, strength, power).
- **Nutrition** — an eating pattern audit, a meal structure planner, and a hydration and
  heat plan, all STRONG-GUARD, expressed in portions, thirst, and the person's own
  cuisine, never in calories or electrolyte doses.
- **Sleep & recovery** — a routine and environment audit with a two-week experiment, and a
  shift-work and jet-lag timing plan (sleep windows, naps, light, caffeine cut-offs).

## Directory map

| Subdirectory | Prefix | Prompts |
|---|---|---|
| `foundations/` | `wellness_` | `wellness_readiness_and_red_flag_screen.md` (**entry gate**), `wellness_sustainable_routine_designer.md` |
| `fitness/` | `fitness_` | `fitness_beginner_training_plan.md`, `fitness_program_progression_review.md`, `fitness_endurance_event_build_plan.md`, `fitness_mobility_and_flexibility_routine.md`, `fitness_return_after_break_plan.md`, `fitness_active_ageing_plan.md` |
| `nutrition/` | `nutrition_` | `nutrition_eating_pattern_audit.md` (**STRONG-GUARD**), `nutrition_meal_structure_planner.md` (**STRONG-GUARD**), `nutrition_hydration_and_heat_plan.md` (**STRONG-GUARD**) |
| `sleep-recovery/` | `sleep_` | `sleep_routine_and_environment_audit.md`, `sleep_shift_work_and_jet_lag_timing_plan.md` |

## Quick routing

| You're saying | Use |
|---|---|
| "Is it safe for me to start?" | `foundations/wellness_readiness_and_red_flag_screen.md` |
| "I trained before, then stopped for a few months" | `fitness/fitness_return_after_break_plan.md` (after checking the profile still stands) |
| "I keep trying to do everything and it collapses in week two" | `foundations/wellness_sustainable_routine_designer.md` |
| "I've never lifted and want a plan" | `fitness/fitness_beginner_training_plan.md` |
| "My numbers stopped going up" / "Do I need a deload?" | `fitness/fitness_program_progression_review.md` |
| "I signed up for my first half marathon" / "first century ride" | `fitness/fitness_endurance_event_build_plan.md` |
| "My hips and ankles are stiff" / "I can't touch my toes" | `fitness/fitness_mobility_and_flexibility_routine.md` |
| "I'm 70 and want to stay strong and steady on my feet" | `fitness/fitness_active_ageing_plan.md` |
| "Is the way I eat actually okay?" / "I crash at 4 pm" | `nutrition/nutrition_eating_pattern_audit.md` |
| "What should I eat around training, in food I actually cook?" | `nutrition/nutrition_meal_structure_planner.md` |
| "How much should I drink?" / "A heat wave is coming and I have a race" | `nutrition/nutrition_hydration_and_heat_plan.md` |
| "I sleep but wake up tired" / "does my coffee matter?" | `sleep-recovery/sleep_routine_and_environment_audit.md` |
| "I work nights and I'm wrecked on my days off" / "flying to Tokyo next week" | `sleep-recovery/sleep_shift_work_and_jet_lag_timing_plan.md` |

## How the prompts compose

`wellness_readiness_and_red_flag_screen` emits a **Readiness Profile** (gate result, rules
fired, limits, nutrition guard, sleep flags, starting point, capacity, goal). Every other
prompt reads it. `wellness_sustainable_routine_designer` decides *when*; the fitness,
nutrition, and sleep prompts decide *what*. The beginner plan hands off to the
progression review at week 8; the return-after-a-break plan hands back to the normal plan
and that same review; the endurance build hands stalls to the same review, long-session
fuelling to the meal structure planner, and hot-weather training to the hydration and heat
plan; the eating pattern audit's one to
three changes become the meal structure planner's input, which in turn hands menus and
shopping to `domain-productivity/home-life/home_meal_plan_week.md`.

## Not here (negative boundaries)

| If the prompt is… | It lives in | Not here, because |
|---|---|---|
| Held by a clinician about a patient | `domain-healthcare-clinical/` | This domain's user is the healthy adult, not their clinician |
| Mental health, including sleep as an insomnia treatment and exercise as a depression tool | `domain-psychology/client-self-use/` (e.g. `coping-by-concern/clientself_sleep_cbt_i_sleep_restriction_calculator.md`, `habit-lifestyle/clientself_exercise_as_antidepressant_plan.md`) | The goal there is mood or a disorder, not physical health |
| Weekly menus, shopping lists, and pantry logistics | `domain-productivity/home-life/home_meal_plan_week.md` | Logistics only; `nutrition_meal_structure_planner` supplies it with structure |
| Designing one habit's cue, routine, and reward | `domain-personal-development/prompts/habits/` | Habit design in general; this domain schedules the whole week |
| Emotional regulation and resilience | `domain-personal-development/prompts/emotional-fitness/` | Emotional, not physical, fitness |
| Researching treatment options for a diagnosed condition | `domain-personal-development/major-decisions/personal_health_decision_research.md` | Decisions with a clinician about a condition; this domain does not treat conditions |
| Eating disorder treatment protocols | `domain-psychology/specialty-clinical/` (clinician-held) | Specialist clinical work; this domain only redirects |
| Rehabilitation after injury or surgery | a clinician or physiotherapist | No rehab content in this domain |
| Falls-risk assessment, or a supervised falls-prevention programme | a clinician or physiotherapist (clinician-held geriatric review: `domain-psychology/populations/geriatric/psychology_geriatric_intake_with_polypharmacy_review.md`) | `fitness_active_ageing_plan` screens for falls and routes; it never assesses risk |
| Electrolyte, salt, or sweat-rate planning for an individual athlete | a registered sports dietitian | `nutrition_hydration_and_heat_plan` is thirst-led and gives no doses |

## Conventions

- **Frontmatter:** repo-standard fields; `category: health-wellness/<subdirectory>`; 3–5
  verified technique IDs; exactly three `related_prompts`, at least one intra-domain.
- **Body:** Objective, the gate block (Readiness gate or STRONG-GUARD), When to Use with a
  "Not this prompt if…" line, then Inputs / Context, Method, Output Format, Verification,
  False-Positive Prevention, Example Output, Techniques Used, Related Prompts.
- **Numbers are general guidance,** labeled as such (public-health activity guidance,
  common coaching practice), never as a personal prescription.
- **Form and technique** are routed to a qualified coach; text gives at most two check-cues.

## Companion domains

- `domain-psychology/client-self-use/` — mood, anxiety, insomnia treatment, crisis self-triage.
- `domain-personal-development/prompts/habits/` — making any one of these behaviors stick.
- `domain-productivity/home-life/` — the meal logistics layer.
- `domain-healthcare-clinical/` — the clinician's side of the conversations this domain routes to.

Roadmap: [`EXPANSION_ROADMAP.md`](EXPANSION_ROADMAP.md) ·
repo-wide plan: [`../meta/COVERAGE_ROADMAP.md`](../meta/COVERAGE_ROADMAP.md)
