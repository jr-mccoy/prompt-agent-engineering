---
title: "Home Alone Readiness Check — Anchored Readiness Scoring, Local Legal Guidance, Home Hazard Lockdown, and a Graduated Trial Ladder"
category: parenting/safety-risk
description: "Decide whether and how long a child (roughly 8–14) can stay home alone or mind a sibling: score readiness on anchored scales across judgment, emergency skills, rule-following, comfort, and home/neighbourhood factors; check local legal age guidance (which varies by state and country); lock down firearms, medications, and other hazards; and run a graduated trial ladder from 15 minutes to a few hours with debriefs."
techniques:
  - DP-03
  - DP-05
  - RT-02
  - QA-02
difficulty: beginner
intended_use: model-testing
tags:
  - parenting
  - safety-risk
  - home-alone
  - latchkey
  - self-care-readiness
  - sibling-babysitting
  - emergency-skills
  - is-my-kid-old-enough-to-stay-home-alone
  - leaving-child-home-after-school
updated: "2026-10-02"
related_prompts:
  - domain-parenting/caregiver-facing/ages-9-12/parenting_tween_emerging_independence_negotiation.md
  - domain-parenting/caregiver-facing/ages-9-12/parenting_first_phone_decision_framework.md
  - domain-parenting/caregiver-facing/safety-risk/parenting_home_childproofing_by_stage.md
---

# Home Alone Readiness Check

**Objective:** Produce a readiness decision for one child — a scored profile, the
local legal and agency guidance to confirm, a hazard lockdown list, house rules, an
emergency card, and a dated trial ladder with stop conditions.

**When to Use:**
- A caregiver is considering leaving a child home alone for the first time, after
  school, or for longer periods.
- An older child is being asked to watch a younger sibling.
- A child is asking to stay home alone and the caregiver is unsure.
- **Not this prompt if** the question is broader tween autonomy (walking to school,
  going to the mall, curfew) — use
  `domain-parenting/caregiver-facing/ages-9-12/parenting_tween_emerging_independence_negotiation.md`.
  If the decision is about a phone for check-ins, use
  `domain-parenting/caregiver-facing/ages-9-12/parenting_first_phone_decision_framework.md`.
  This prompt answers one question: *is this child ready to be alone in this home,
  for this long, now?*

## Safety Block

- **Legal age guidance varies.** In the US, only a few states set a minimum age in
  law (commonly cited examples: Illinois 14, Maryland 8, Oregon 10); many states and
  counties publish non-binding guidelines instead, and most rely on "reasonable
  judgment" in neglect law. Other countries differ (several have no fixed age but
  prosecute neglect). **Confirm with your state or local child-protection agency's
  current guidance before deciding** — this prompt does not give legal advice.
- **Firearms** in the home: stored unloaded, locked, with ammunition locked
  separately, keys/codes inaccessible to the child — before any time alone. If that
  cannot be guaranteed, the child is not left alone.
- **Pools and open water:** a child is never left home alone with unfenced pool
  access.
- **Medical conditions** (seizures, anaphylaxis, diabetes) require a written plan the
  child can execute and adult back-up nearby; for some children this rules out time
  alone.
- In an emergency the child calls 911 (or the local number) first, then a parent.

## Inputs / Context

1. **Child:** age, maturity, impulsivity, anxiety, ADHD/autism, medical needs.
2. **The ask:** how long, what time of day, how often, with or without siblings
   (ages of siblings).
3. **Home:** firearms, medications, alcohol, cannabis edibles, pool, gas stove,
   pets, internet access.
4. **Neighbourhood:** a reachable adult neighbour, distance of parent, safety.
5. **Communication:** phone or watch, landline, house rules about door and visitors.
6. **Jurisdiction** (state/county/country).

## Method

1. **Check jurisdiction first.** Look up the local rule or guideline; if the child
   is under it, stop. Typical US child-welfare guideline bands (not law): under 8 —
   not alone; 8–10 — brief daytime periods, about an hour; 11–12 — up to about 3
   hours, not late at night; 13–15 — longer, generally not overnight; caring for
   younger siblings — typically 13+ with training.
2. **Score readiness on anchored scales (DP-03), 0–2 each:**
   - **Judgment:** 0 = acts on impulse often; 1 = usually follows rules when
     reminded; 2 = follows rules unsupervised for weeks.
   - **Emergency skills:** 0 = cannot state address or when to call 911; 1 = knows
     them but freezes in role-play; 2 = performs fire, injury, and stranger-at-door
     drills correctly.
   - **Self-care:** 0 = cannot make a snack safely; 1 = with reminders; 2 =
     independently, including microwave safety.
   - **Comfort:** 0 = scared or reluctant; 1 = willing but anxious; 2 = wants to and
     is calm.
   - **Environment:** 0 = hazards unsecured or no adult nearby; 1 = some gaps;
     2 = hazards locked, neighbour available, parent ≤20 minutes away.
   Any 0 → not yet. Total ≤6 → not yet. 7–8 → short trials only. 9–10 → full
   ladder. An unsecured firearm or pool blocks regardless of total.
3. **Stress-test with scenarios (QA-02).** Ask the child, then role-play: smoke
   alarm goes off; someone knocks and says they're from the gas company; sibling
   falls and is bleeding; a friend wants to come over; power cut at dusk; parent
   doesn't answer. Correct answers, not just confident ones.
4. **Lock down hazards (RT-02).** Firearms (above); medications including vitamins
   and edibles locked; alcohol locked; lighters out of reach; knives rule; stove rule
   (microwave only at first); pool gate locked.
5. **Write house rules.** Door stays locked; don't open to anyone not on the list;
   don't say you're alone on the phone or online; no friends over; check-in text on
   arrival; screen and internet rules.
6. **Build the emergency card.** Address, parent numbers, neighbour, poison control
   (1-800-222-1222 US), 911, medical info.
7. **Run the trial ladder (DP-05).** 15–30 minutes while parent is nearby → 1 hour
   → after-school routine (2–3 hours) → sibling care only after separate readiness
   and a course (e.g., Red Cross babysitting / Safe Sitter, typically 11+). Debrief
   after each step; move up only if rules were kept and the child felt okay.
8. **Define stop conditions.** Rule broken with safety impact, child frightened,
   new hazard, or change in child's mental health → step back down.

## Output Format

```
# Home Alone Readiness — [child, age], [jurisdiction]

## Local rule / guideline (source to confirm)
## Readiness scores (judgment / emergency / self-care / comfort / environment)
## Scenario results
## Hazard lockdown (item → status)
## House rules
## Emergency card
## Trial ladder (step, date, duration, debrief outcome)
## Stop conditions
```

## Verification

- [ ] Jurisdiction checked and named as "confirm locally."
- [ ] Every scale scored with evidence; any 0 blocks.
- [ ] Scenarios were role-played, not only discussed.
- [ ] Firearms, medications, and pool status are explicit.
- [ ] Ladder steps have dates and debriefs; sibling care is a separate decision.

## False-Positive Prevention

| Misfire | What it looks like | Correction |
|---|---|---|
| Age as the only test | "She's 12, so yes" | Score readiness; age is a floor, not a pass. |
| Confident words, wrong actions | Child says "I'd call 911" then freezes | Role-play is the test. |
| Sibling care bundled in | Alone at 11 = minding a 4-year-old | Separate, higher bar; training first. |
| Over-restricting a ready child | Never alone at 14 | Readiness scores support graduated time. |
| Ignoring the child's fear | Pushing an anxious child | Comfort score of 0 blocks; build slowly. |
| Assuming firearms are "hidden" | Gun in a closet | Hidden is not secured; lock it or no time alone. |

## Adaptations

- **ADHD / impulsivity:** shorter steps, visual checklist by the door, check-in
  timer; stove use later.
- **Autistic child:** script for the doorbell and phone; predictable routine;
  sensory plan for alarms.
- **Anxious child:** start with parent in the garden; video call allowed.
- **Rural home:** distance to help matters more — require a reachable neighbour.

## Example Output

```
# Home Alone Readiness — Jonah, 11, Ohio (no statutory minimum;
# confirm county children services guidance)

## Scores
Judgment 2 (walks dog alone, rules kept 2 months)
Emergency 1 (knew 911 and address; opened the door in the "gas man" role-play)
Self-care 2. Comfort 2. Environment 1 (rifle in closet, unlocked)
Total 8, but environment gap → fix before trials.

## Hazard lockdown
Rifle → gun safe, ammo in separate lockbox (done 3 May).
Meds and melatonin gummies → locked cabinet. Pool: none.

## House rules
Door locked; no answering to anyone not on list; text "home" on arrival;
no friends over; microwave only.

## Trial ladder
10 May: 30 min while Mum at the shop (2 min away) — repeat door role-play
first. 17 May: 1 h. 31 May: after-school 3:15–5:30 twice a week.
Sister (5) is NOT in scope until Jonah is 13 and has done a course.

## Stop conditions
Door opened to someone off the list, friends over, or Jonah reports
feeling scared → back one step.
```

## Techniques Used

- **DP-03 Anchored Scoring Scales** — observable 0–2 anchors per readiness domain.
- **DP-05 Stakes-Based Gate Policy** — any zero blocks; ladder steps gate on debriefs.
- **RT-02 Multi-Dimensional Analysis Framework** — child, home, neighbourhood, and law assessed separately.
- **QA-02 Adversarial Stress-Test** — scenario role-plays expose gaps confidence hides.

## Related Prompts

- `domain-parenting/caregiver-facing/ages-9-12/parenting_tween_emerging_independence_negotiation.md` — wider independence steps.
- `domain-parenting/caregiver-facing/ages-9-12/parenting_first_phone_decision_framework.md` — device for check-ins.
- `domain-parenting/caregiver-facing/safety-risk/parenting_home_childproofing_by_stage.md` — the full hazard audit.
