---
title: "Meal Structure Planner — Protein, Fibre, and Plate Structure Built Around Your Constraints and Cuisine"
category: health-wellness/nutrition
description: "Design a repeatable eating structure for a healthy adult: a plate pattern in hand-sized portions, protein at each main meal, plants and fibre across the day, training-day and rest-day templates with fuelling around sessions, and swap lists drawn from the person's own cuisine, budget, and cooking time. STRONG-GUARD: stops and redirects on restriction, compensation, rapid weight-loss goals, minors, pregnancy, or diagnosed conditions; no calorie targets, no supplements. Structure only — menus and shopping go to the weekly meal planner."
techniques:
  - QA-08
  - DS-26
  - ED-04
  - CM-02
difficulty: beginner
tags:
  - health-wellness
  - nutrition
  - meal-structure
  - protein
  - fibre
  - strong-guard
  - sports-nutrition
  - eating-around-workouts
  - cheap-healthy-meals
  - no-calorie-counting
updated: "2026-09-24"
related_prompts:
  - domain-health-wellness/nutrition/nutrition_eating_pattern_audit.md
  - domain-productivity/home-life/home_meal_plan_week.md
  - domain-health-wellness/foundations/wellness_readiness_and_red_flag_screen.md
---

# Meal Structure Planner

**Objective:** Give a healthy adult a simple, repeatable structure for what goes on the
plate and when — expressed in portions and swaps from their own food culture — so that
eating supports their training and energy without counting anything.

> **Readiness gate.** Start from a Readiness Profile
> (`foundations/wellness_readiness_and_red_flag_screen.md`). No profile → ask its
> blocks 1–8 first. URGENT-CARE-NOW, CLINICIAN-FIRST, or OUT-OF-SCOPE → stop and
> restate the route. An urgent result means contacting the local emergency number
> now (e.g. 911 in the US). GO-WITH-LIMITS → every limit binds this prompt, and the
> *Nutrition guard* line must still read CLEAR (the STRONG-GUARD block below).
> If the readiness gate and the STRONG-GUARD both fire, the gate's route wins; the
> audit's redirect template is used only once the gate is GO or GO-WITH-LIMITS.

> **STRONG-GUARD prompt.** A meal structure handed to someone with a restrictive or
> compensatory pattern becomes a set of rules to fail or to tighten. This prompt
> **stops and redirects** — no modified plan, no "gentle" version — when the Readiness
> Profile's nutrition guard reads STOP, or the conversation shows any of: restriction
> for weight control or out of fear; compensation (vomiting, laxatives, diuretics,
> fasting, or exercise to "undo" food); binge or loss-of-control eating; thoughts about
> food, weight, or body shape that crowd out other things; in people who train, missed
> or stopped periods, repeated bone-stress injuries, or energy and performance falling
> while training more (signs of relative energy deficiency in sport, RED-S); a goal of
> more than about 1% of body weight a week, a large loss by a date, or an intake below
> commonly cited unsupervised floors (roughly 1,200 kcal/day for women, 1,500 for men —
> conservative guard triggers, not clinical targets); age under 18; pregnancy or
> breastfeeding; or a diagnosed condition the eating is meant to manage.
>
> **This prompt never** sets a calorie target, names or doses a supplement, or adjusts
> for a medical condition. When the guard fires, the whole response is the **Redirect
> template** in `nutrition/nutrition_eating_pattern_audit.md` (inside its STRONG-GUARD
> block), used verbatim with the same adjustments for minors, pregnancy, and diagnosed
> conditions — it names a clinician and a registered dietitian, links the eating
> self-monitoring prompt, and gives 988 in the US — then stop.

**When to Use:**
- After an eating pattern audit, to turn one to three changes into a daily shape.
- You train and want to know what to eat before and after, without tracking apps.
- You want "healthy eating" translated into the food you already cook.
- **Not this prompt if** you want a 7-day menu and a grocery list — that is
  `domain-productivity/home-life/home_meal_plan_week.md`, which handles logistics and can
  take this structure as input. For an audit of what you eat now, run
  `nutrition/nutrition_eating_pattern_audit.md` first.

## Inputs / Context

1. **Readiness Profile** — *Gate result* GO or GO-WITH-LIMITS (otherwise stop and restate
   the route; no profile → run the screen's blocks 1–8 first), and nutrition guard CLEAR.
2. **The audit's changes**, if one was run.
3. **Cuisine and staples** (ED-04): what you cook and eat most weeks, and any religious,
   cultural, ethical, or allergy constraints.
4. **Budget, cooking time, and equipment**; how often you eat out.
5. **Training days and session times**; any session over ~90 minutes.
6. **Meal rhythm** that fits your day (shift work, family dinner, fasting periods).

## Method

1. **Run the gates (QA-08).** *Gate result* GO or GO-WITH-LIMITS, else stop and restate
   the route. Then *Nutrition guard* CLEAR and no STRONG-GUARD signal in the
   conversation; otherwise give the redirect template and stop.
2. **Set the default plate (DS-26).** Hand-portion defaults, adjusted by appetite:

   | Slot | Default portion per main meal | Adjust when |
   |---|---|---|
   | Protein food | 1–2 palm-sized portions | larger frame, heavy training, persistent hunger |
   | Vegetables / fruit | about half the plate, or 1–2 fists | appetite, cuisine pattern |
   | Starch / grains | 1–2 cupped hands; more on training days | training volume, hunger, energy |
   | Fats | a thumb or two (oil, nuts, cheese, avocado) | cooking style |

   General guidance for people who train is often expressed as roughly 1.2–2.0 g of
   protein per kg of body weight a day (the 2016 ACSM / Academy of Nutrition and
   Dietetics / Dietitians of Canada joint position); portions are used here instead, so no weighing or body
   weight is needed.
3. **Spread protein.** A protein food at each main meal and, where appetite allows, one
   snack — rather than most of it at dinner.
4. **Build fibre across the day.** Plants at every meal, legumes or pulses several times a
   week, whole-grain versions for most starches where they are affordable and liked.
5. **Write training-day and rest-day templates.** Training day: a meal or snack with
   carbohydrate 1–3 h before the session; a meal with protein and carbohydrate within a
   few hours after. Sessions over ~90 min: general sports-nutrition guidance is often
   around 30–60 g of carbohydrate per hour during the session — practise it in training,
   never first on event day. Rest day: the same structure, with a smaller starch portion
   if appetite is lower. Drink to thirst; heat and heavy sweating need more (see the
   domain roadmap for a dedicated prompt).
6. **Fill slots from the person's own cuisine (ED-04).** Three to five swaps per slot,
   drawn from their staples first, then cheap additions.
7. **Constrain the language (CM-02).** No "good/bad", "clean", "cheat", or "earn"; no
   calorie numbers; no supplement names. If the person asks about a supplement, say that
   a pharmacist or clinician is the right person to ask, and why (interactions, dose, need).
8. **Hand off logistics** to `home_meal_plan_week.md` with the templates as its input.

## Output Format

```
# Meal structure — [name]
Readiness: GO | GO-WITH-LIMITS  (anything else → restate the route; nothing below)
Nutrition guard: CLEAR  (if STOP → redirect template only; nothing below)

## Your plate
| Slot | Portion | Your usual options |
|---|---|---|

## Day templates
### Training day ([session time])
| Time | Meal | Structure |
|---|---|---|
### Rest day
| Time | Meal | Structure |
|---|---|---|

## Long sessions (only if > 90 min)
[before / during / after, practised in training]

## Swap lists
Protein: [...] | Plants: [...] | Starch: [...] | Snacks: [...]

## Not included, on purpose
No calorie target · no supplements · no condition-specific advice → [who to ask]

## Next
Menu + shopping → home_meal_plan_week (paste the templates)
```

## Verification

- [ ] The readiness gate result was checked first, then the guard; any guard signal
  produced only the audit's verbatim redirect template.
- [ ] No calorie figure or supplement name appears.
- [ ] Every main meal has a protein slot and a plant slot.
- [ ] Training-day template places food before and after the actual session time.
- [ ] Swap lists come mostly from the person's own staples and budget.
- [ ] "Not included, on purpose" is present and says who to ask.

## False-Positive Prevention

1. **A structure is not a rulebook.** Present portions as a starting shape adjusted by
   appetite, not as limits to hit.
2. **Don't replace the person's cuisine.** Map the plate onto dal, rice, and sabzi, or
   tortillas and beans; do not swap them for someone else's "healthy" foods.
3. **Don't recommend protein powder by default.** It is a food convenience at most;
   if raised, food options come first and any supplement question goes to a pharmacist.
4. **Don't make carbohydrate the enemy.** Starch portions go *up* on training days.
5. **Budget is a hard constraint.** Tinned fish, eggs, legumes, frozen vegetables, and
   oats beat anything the person cannot afford twice.
6. **During-session fuelling is for long sessions only.** A 45-minute gym session does
   not need a gel.
7. **Don't slide into a menu.** Seven days of named dishes is the weekly planner's job.

## Example Output

Scenario: Leo (from the audit), 29, GO, nutrition guard CLEAR, strength 18:30 Mon/Wed/Fri, tight budget,
cooks for one, likes rice dishes and sandwiches; audit changes: 16:00 snack on gym days,
protein at lunch, one fruit a day.

```
# Meal structure — Leo
Readiness: GO
Nutrition guard: CLEAR

## Your plate
| Protein | 1–2 palms | chicken thighs, eggs, tinned tuna, lentils, Greek yoghurt |
| Plants  | half plate | frozen mixed veg, carrots, cabbage, bananas, apples |
| Starch  | 2 cupped hands (gym days), 1–2 (rest) | rice, wholemeal bread, oats, potatoes |
| Fats    | a thumb | cooking oil, peanut butter |

## Day templates
### Training day (18:30)
| 07:30 | Morning   | coffee as now; banana if hungry (the daily fruit — audit change 3) |
| 12:30 | Lunch     | sandwich with egg or tuna + carrot sticks (audit change 2) |
| 16:00 | Snack     | toast + peanut butter, or yoghurt + fruit (1–3 h pre-session; audit change 1) |
| 20:00 | Dinner    | rice + chicken or lentils + half plate veg (post-session) |
### Rest day
Same shape; dinner starch 1–2 hands; 16:00 snack optional, by hunger.

## Long sessions
Not applicable — sessions are ~50 min.

## Swap lists
Protein: eggs, tuna, chicken thighs, lentils, chickpeas, yoghurt | Plants: frozen veg, cabbage,
carrots, bananas, apples | Starch: rice, oats, bread, potatoes | Snacks: yoghurt + fruit, toast + PB

## Not included, on purpose
No calorie target · no supplements (ask a pharmacist) · no condition-specific advice (ask your GP)

## Next
Paste the training-day and rest-day templates into home_meal_plan_week for a menu and list.
```

## Techniques Used

- **QA-08 Gate-Based Verification** — the STRONG-GUARD runs before any structure is built.
- **DS-26 Safe Defaults Pattern** — hand-portion defaults with stated reasons to adjust.
- **ED-04 Personalization Hooks** — slots filled from the person's own cuisine and budget.
- **CM-02 Constraint Specification** — no calories, no supplements, no moralised language.

## Related Prompts

- `domain-health-wellness/nutrition/nutrition_eating_pattern_audit.md` — the audit whose changes this structures.
- `domain-productivity/home-life/home_meal_plan_week.md` — menus and shopping from these templates.
- `domain-health-wellness/foundations/wellness_readiness_and_red_flag_screen.md` — source of the guard line.
