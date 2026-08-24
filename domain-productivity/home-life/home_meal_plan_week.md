---
title: "Weekly Meal Planner"
category: productivity/home-life
description: "Generate a practical 7-day meal plan and consolidated grocery list matched to your household's time, budget, and pantry."
techniques:
  - ST-01
  - ST-02
  - DS-02
  - CM-02
  - QA-01
  - RT-02
difficulty: beginner
tags:
  - meal-planning
  - grocery
  - cooking
  - household
  - budget
updated: "2026-05-12"
related_prompts:
  - domain-productivity/reviews/reviews_weekly_systems_review.md
  - domain-parenting/parenting_daily_routine_designer.md
  - domain-productivity/bottlenecks/bottleneck_capture_triage_system_design.md
---

# Weekly Meal Planner

**Objective:** Produce a practical Monday-through-Sunday meal plan and a consolidated, categorized grocery list. The plan matches the household's actual cooking time on weeknights versus weekends, uses overlapping ingredients to minimize waste, and stays within any dietary or budget constraints.

**When to use:** At the start of each week, before grocery shopping, or when you want to break out of repeating the same four meals. Also useful when starting a new household routine, moving to a tighter budget, or trying to reduce food waste.

**Audience:** Anyone who shops and cooks for themselves or a household. Intended for real weeknights — 20-45 minutes of active cooking, not hobbyist cooking. Not for professional meal-prep services or people who eat out daily.

---

## Inputs Required

1. **Household size and dietary restrictions.** How many adults and children. Any hard restrictions (vegetarian, gluten-free, allergy) and soft preferences (prefer not to eat pork, one person dislikes spicy). A restriction is only useful if it's real — don't list "trying to eat less red meat" unless it actually constrains choices.

2. **Weeknight cooking time.** Realistic active cooking time available Monday–Friday. 15 minutes means sheet pan or one-pot meals. 30 minutes is standard. 45 minutes is the max for a weeknight. Be honest — if you say 45 minutes but you're usually tired by 6pm, say 20.

3. **Weekend cooking time.** Saturday and Sunday time, which is typically more flexible. This is where slow cookers, braises, or batch cooking fits.

4. **What's already in the pantry/fridge.** List what you have on hand that should be used: proteins (half a rotisserie chicken, ground beef thawing), produce near expiry (bell peppers, spinach), pantry staples available (canned tomatoes, pasta, rice). "I have a fully stocked pantry" is not useful — name the perishables and proteins.

5. **Budget range (optional).** Rough weekly grocery spend target, e.g., "$100 for the week" or "no constraint." If unspecified, the plan defaults to mid-range.

6. **Meals needed.** Which meals to plan: dinner only (default), or also breakfast and/or lunch. If breakfast and lunch are included, specify whether they should be planned day-by-day or as general prep (e.g., "batch eggs for the week").

---

## Instructions

### Step 1 — Classify weekdays by cooking capacity
Sort the seven days into tiers:
- **Minimal (≤20 min active):** typically Monday, Wednesday, days with late commitments
- **Standard (25–35 min active):** typical weeknights
- **Flexible (45+ min or batch):** weekend days, any day user flags as open

Assign meal complexity accordingly. Do not assign a braised short rib to a minimal day.

### Step 2 — Select meals using ingredient overlap
Choose meals that share core ingredients to reduce waste and grocery cost:

- If chicken breast appears Monday, it should reappear in a different form Wednesday or Thursday (not the same dish).
- If a bunch of cilantro is used Tuesday, another meal this week should use the rest.
- Batch-cooking candidates: grains (rice, farro), proteins (roast a whole chicken Sunday), sauces (tomato sauce works across two meals).

Select meals in this order:
1. Use what's already in the fridge/pantry first (Step 1 inputs)
2. Fill remaining slots with meals that share ingredients with each other
3. Minimize unique single-use ingredients

### Step 3 — Build the 7-day plan
Format each day:

```
[Day]: [Meal name] | Active time: X min | Key ingredients: A, B, C
```

For each meal include:
- The dish name (specific enough to cook from, not "chicken dish")
- Active cook time
- Whether it uses pantry items or requires fresh purchase
- Any prep that can be done ahead (marinate Sunday, prep veg Saturday)

If breakfast and lunch are included, treat them as brief entries — no need for full recipe detail.

### Step 4 — Build the grocery list
Consolidate all ingredients across the week. Group by category:

- **Produce:** sorted roughly by what gets used early vs. late in the week (fragile items early)
- **Proteins:** all meats, fish, eggs, tofu
- **Dairy & refrigerated:** milk, cheese, yogurt, butter
- **Pantry & dry goods:** canned goods, pasta, rice, oils, spices (only what's not already on hand)
- **Frozen:** anything from the freezer section
- **Other:** bread, specialty items

Mark any items the user already has in the pantry so they know what to skip at the store.

### Step 5 — Flag waste risks and substitutions
Call out any ingredients that are single-use or have a short shelf life that weren't paired with another meal. Offer a substitution if possible (e.g., "If you can't use the rest of the feta, sub in parmesan for Thursday's pasta instead").

---

## Constraints

### Must
- Assign meal complexity that matches the stated weeknight cooking time — no elaborate weeknight meals when user says 20 minutes
- Use pantry/fridge items stated in inputs before adding new purchases
- Include active cook times in the plan
- Produce a consolidated grocery list (not a per-recipe list)
- Grocery list must distinguish new purchases from pantry items already on hand

### Must Not
- Plan aspirational recipes (sous vide, homemade pasta, complex braises) for weeknights unless user explicitly requests it
- List the same meal twice in the same week
- Ignore stated dietary restrictions
- Assume the user has spices, oils, or pantry staples not mentioned in inputs
- Produce a grocery list that requires more than one store trip for standard items

---

## False-Positive Prevention

1. **Optimism creep:** The plan looks doable on paper but assumes 45 minutes every weeknight when the user said they usually have 20. Guard against this by explicitly binning each weekday into the tiers from Step 1 before assigning meals.

2. **Aspirational meals:** Includes a recipe the user will skip and order pizza instead. A meal plan that gets abandoned is worse than a boring one that gets cooked. Default to meals the user has cooked before or simple versions of familiar dishes.

3. **Single-use ingredient sprawl:** Requires six different fresh herbs, three specialty items, and four different proteins, producing a $200 grocery list for a $100 household. Enforce overlap rules from Step 2.

4. **Generic grocery list:** Groups everything as "vegetables" without specifics, or lists "herbs" without naming them. Every item on the grocery list must be specific enough to pick up at the store without guessing.

5. **Ignoring what's on hand:** Overlooks the chicken thighs and peppers the user flagged as needing to be used, and builds a plan around entirely new purchases. Step 2 requires using pantry/fridge inputs first.

---

## Output Format

```
## Week of [DATE]

### Meal Plan

| Day | Meal | Active Time | Notes |
|-----|------|-------------|-------|
| Monday | [Dish name] | [X min] | [Uses pantry / batch from Sunday / etc.] |
| Tuesday | [Dish name] | [X min] | |
| Wednesday | [Dish name] | [X min] | |
| Thursday | [Dish name] | [X min] | |
| Friday | [Dish name] | [X min] | |
| Saturday | [Dish name] | [X min] | |
| Sunday | [Dish name / batch cook] | [X min] | |

[If breakfast/lunch included, add rows or a separate table]

---

### Grocery List

**Produce**
- [ ] [Item, quantity]
- [ ] ...

**Proteins**
- [ ] [Item, quantity]
- [ ] ...

**Dairy & Refrigerated**
- [ ] [Item, quantity]
- [ ] ...

**Pantry & Dry Goods**
- [ ] [Item, quantity] *(skip — already have)*
- [ ] [Item, quantity]
- [ ] ...

**Frozen**
- [ ] [Item, quantity]
- [ ] ...

**Estimated grocery spend:** $[X]–$[Y]

---

### Waste Watch
[Any single-use ingredients or short-shelf-life items to use quickly, with suggested fallback]

### Prep Ahead (Optional)
[Any Sunday or weekend prep that makes weeknights faster — e.g., "Cook rice Sunday, portion for Mon + Wed"]
```

---

## Verification

- [ ] Every weeknight meal fits within the stated weeknight cooking time
- [ ] No meal appears twice in the same week
- [ ] All stated dietary restrictions are respected
- [ ] Pantry/fridge items flagged in inputs appear in the plan before adding new purchases
- [ ] Grocery list is organized by category, not by recipe
- [ ] Each grocery list item is specific (ingredient + quantity), not generic
- [ ] At least two pairs of meals share a key ingredient to reduce waste
- [ ] Active cook times are listed for each dinner
