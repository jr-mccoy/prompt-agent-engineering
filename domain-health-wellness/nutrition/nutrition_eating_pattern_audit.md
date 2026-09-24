---
title: "Eating Pattern Audit — What Your Meals Actually Look Like, and the One to Three Changes Worth Making"
category: health-wellness/nutrition
description: "Audit a healthy adult's eating pattern from a plain-language food and timing log — regularity, protein spread, plant foods and fibre, fuelling around training, alcohol, hunger and energy — and return strengths, the one to three highest-leverage changes, and what to leave alone. STRONG-GUARD: stops and redirects on restriction, compensation, rapid weight-loss goals, minors, pregnancy, or diagnosed conditions; sets no calorie targets and prescribes no supplements."
techniques:
  - QA-08
  - RT-02
  - CM-02
  - QA-20
difficulty: beginner
tags:
  - health-wellness
  - nutrition
  - eating-pattern
  - food-log
  - strong-guard
  - disordered-eating-guard
updated: "2026-09-24"
related_prompts:
  - domain-health-wellness/foundations/wellness_readiness_and_red_flag_screen.md
  - domain-health-wellness/nutrition/nutrition_meal_structure_planner.md
  - domain-psychology/client-self-use/crisis-self-triage/clientself_am_i_in_crisis_self_triage.md
---

# Eating Pattern Audit

**Objective:** Read what someone actually eats across a few ordinary days and return
what is already working, the one to three changes most likely to help their energy,
training, and long-term health, and what they should not bother changing.

> **STRONG-GUARD prompt.** Nutrition advice is where a wellness prompt most easily
> does harm: it can feed restriction, reward compensation, or lend a plan to someone
> whose goal is itself the symptom. This prompt therefore **stops and redirects** —
> it does not soften, modify, or offer a "safer" diet — when any of these appear, in
> the Readiness Profile or anywhere in the conversation:
> - **Restriction:** deliberately skipping meals or cutting food groups to control
>   weight or out of fear; rigid food rules that cause distress; eating very little
>   and describing it as discipline.
> - **Compensation:** vomiting, laxatives, diuretics, fasting, or exercise used to
>   "undo" or "earn" food.
> - **Rapid weight-loss goals:** more than about 1% of body weight a week, a large
>   amount by a fixed date, or a request for an intake below commonly cited
>   unsupervised floors (roughly 1,200 kcal/day for women, 1,500 for men).
> - **Minors** (under 18), **pregnancy or breastfeeding**, or a **diagnosed condition**
>   the eating is meant to manage (diabetes, kidney disease, an eating disorder, and so on).
>
> **This prompt never** sets a calorie target, gives a weight-loss rate, names or doses
> a supplement, or infers a deficiency from symptoms. The redirect is short, plain, and
> kind: what was noticed in the person's own words, that it is worth talking to a
> clinician (primary care, and a registered dietitian — ideally one experienced with
> eating concerns), and, if they feel unsafe or overwhelmed, the crisis route in
> `domain-psychology/client-self-use/crisis-self-triage/clientself_am_i_in_crisis_self_triage.md`
> (in the US, call or text 988). Then it stops.

**When to Use:**
- You eat "fine" but run out of energy mid-afternoon or in training.
- You have started training and wonder whether your eating supports it.
- You want an honest outside read of your pattern, not a diet.
- **Not this prompt if** you want a structure to eat *toward* (use
  `nutrition/nutrition_meal_structure_planner.md` after this), you want a shopping list
  and weekly menu (`domain-productivity/home-life/home_meal_plan_week.md`), or you are
  managing a diagnosed condition (clinician or registered dietitian).

## Inputs / Context

1. **Readiness Profile** — the *Nutrition guard* line must read CLEAR. STOP, or no
   profile and a *yes* to gate block 7 → redirect as above.
2. **3–7 ordinary days, in plain words:** what, roughly how much ("a bowl", "two slices"),
   and when. No weighing or calorie counts needed — do not ask for them.
3. **Training days** marked, with session time.
4. **Energy and hunger:** when energy dips; whether they arrive at meals ravenous.
5. **Constraints:** budget, cooking time and skill, cultural or religious pattern,
   allergies or foods avoided, who else eats with them.
6. **What they want from the audit**, in their words.

## Method

1. **Run the guard (QA-08).** Check the profile line and read the log and goal for any
   STRONG-GUARD signal. One signal is enough. If it fires, write the redirect and stop.
2. **Describe before judging.** Summarise the pattern back: meal times, typical meals,
   training days. Ask the person to correct it.
3. **Audit six dimensions (RT-02).** For each: what the log shows, whether it plausibly
   matters for *this* person's goal, and confidence.
   - **Regularity** — long gaps, a skipped meal followed by a large late one.
   - **Protein spread** — a protein source at each main meal, or all of it at dinner.
   - **Plants and fibre** — vegetables, fruit, legumes, whole grains across the day.
   - **Fuelling around training** — something with carbohydrate in the few hours before
     a session; a meal with protein within a few hours after.
   - **Alcohol** — frequency and amount, stated neutrally, and its link to sleep.
   - **Hunger and energy** — do dips line up with gaps or with a carbohydrate-only meal?
4. **Pick one to three changes.** Rank by likely effect on the person's stated goal,
   times ease within their constraints. Each change is an *addition or a move* where
   possible ("add yoghurt to breakfast", "eat lunch before 13:30"), not a removal.
5. **Name what to leave alone.** At least one thing that is fine and should not be
   changed — this is part of the output, not politeness.
6. **Constrain the language (CM-02).** No "good/bad", "clean", "cheat", "junk", or
   "earn". No numbers for calories or weight.
7. **Dual-failure check (QA-20).** Did a guard signal get audited instead of redirected?
   Did a clean audit get so hedged it tells the person nothing? Fix whichever happened.

## Output Format

```
# Eating pattern audit — [name]
Nutrition guard: CLEAR  (if STOP → redirect only; nothing below)

## Your pattern, as I read it
[3–5 lines; "correct me if this is off"]

## Six dimensions
| Dimension | What the log shows | Matters for your goal? | Confidence |
|---|---|---|---|

## What's already working
- [...]

## The changes (1–3), ranked
1. [change] — why: [link to log + goal] — how, within your constraints: [...]

## Leave alone
- [...]

## Next
Structure → nutrition_meal_structure_planner | Shopping → home_meal_plan_week
```

## Verification

- [ ] The guard was run first; any signal produced a redirect and nothing else.
- [ ] No calorie, weight, or supplement figure appears anywhere.
- [ ] Every change cites something in the log and the person's goal.
- [ ] At most three changes; at least one "leave alone".
- [ ] No moralised food words.
- [ ] Constraints (budget, culture, time) shape every change.

## False-Positive Prevention

1. **Don't audit a guard signal.** "They only mentioned fasting after a big meal once"
   is still compensation; redirect.
2. **Don't infer deficiency.** Tiredness is not low iron; route persistent symptoms to a
   clinician, never to a supplement.
3. **Don't moralise processed food.** Describe the share, link it to the goal, or leave it.
4. **Don't import a diet.** Keto, intermittent fasting, "clean eating" — none is the
   default; audit the pattern the person has.
5. **Don't override culture.** Rice at every meal, late family dinners, or a fasting
   month are the frame, not the problem.
6. **Don't over-prescribe.** Seven changes is a diet; one to three is an audit.
7. **Low confidence is an answer.** A three-day log cannot show a weekly pattern; say so.
8. **The redirect is not a lecture.** Four or five sentences, warm, then stop.

## Example Output

Scenario: 29, GO, nutrition guard CLEAR, strength training 18:30 Mon/Wed/Fri; five-day
log; goal "stop crashing at 4 pm and have energy for the gym"; tight budget, cooks for one.

```
# Eating pattern audit — Leo
Nutrition guard: CLEAR

## Your pattern, as I read it
Coffee only until ~12:30; lunch is a sandwich from work; nothing until dinner ~20:00 after
the gym; dinner is large (pasta or rice with chicken); beer on 2 evenings. Correct me if off.

## Six dimensions
| Regularity   | 7.5 h gap lunch → dinner on gym days | yes — lines up with 4 pm crash | High |
| Protein      | mostly at dinner; little at breakfast (none) or lunch | yes, for training | Medium |
| Plants/fibre | veg at dinner 3/5 days; fruit 0/5 | some | Medium |
| Fuelling     | last food ~6 h before 18:30 session | yes | High |
| Alcohol      | 2 evenings, 2–3 beers | possibly sleep; not the crash | Low |
| Hunger/energy| ravenous at dinner; flat in sessions | consistent with gaps | Medium |

## What's already working
- A cooked dinner with protein and starch every day — keep it.

## The changes, ranked
1. Add a 16:00 snack on gym days (banana + yoghurt, or toast with peanut butter) —
   closes the 7.5-h gap behind both the crash and flat sessions; cheap, no cooking.
2. Add a protein food at lunch (egg, tuna, or bean-based sandwich filling) — spreads
   protein across the day; same shop.
3. Add one piece of fruit a day — easiest fibre step; buy in bulk, keep at work.

## Leave alone
- Dinner size and timing — it fits your evening and your training.

## Next
Structure → nutrition_meal_structure_planner | Shopping → home_meal_plan_week
```

## Techniques Used

- **QA-08 Gate-Based Verification** — the STRONG-GUARD runs as a binary gate before any audit.
- **RT-02 Multi-Dimensional Analysis Framework** — six fixed dimensions with relevance and confidence.
- **CM-02 Constraint Specification** — no calorie, weight, or supplement figures; no moralised language.
- **QA-20 Dual-Failure Quality Test** — neither audit through a guard signal nor hedge a clean audit into nothing.

## Related Prompts

- `domain-health-wellness/foundations/wellness_readiness_and_red_flag_screen.md` — source of the nutrition guard line.
- `domain-health-wellness/nutrition/nutrition_meal_structure_planner.md` — turn the changes into a structure.
- `domain-psychology/client-self-use/crisis-self-triage/clientself_am_i_in_crisis_self_triage.md` —
  the crisis route when the guard fires and the person feels unsafe.
