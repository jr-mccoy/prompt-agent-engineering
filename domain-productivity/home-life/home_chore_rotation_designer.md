---
title: "Household Chore Rotation Designer"
category: productivity/home-life
description: "Design a sustainable chore rotation — who does what, how often — for a solo person, couple, or family with kids."
techniques:
  - ST-01
  - ST-03
  - DS-01
  - CM-02
  - QA-01
  - AG-11
difficulty: beginner
tags:
  - chores
  - household
  - family
  - scheduling
  - systems
updated: "2026-05-12"
related_prompts:
  - domain-productivity/reviews/reviews_weekly_systems_review.md
  - domain-parenting/parenting_daily_routine_designer.md
  - domain-parenting/parenting_transitions_and_warnings_protocol.md
  - domain-productivity/bottlenecks/bottleneck_capture_triage_system_design.md
---

# Household Chore Rotation Designer

**Objective:** Produce a sustainable, fair chore rotation schedule for a household — specifying who does which tasks, at what frequency, and with a ready-to-use weekly reference. Classifies chores by effort and frequency, distributes load equitably, and accounts for hard constraints.

**When to use:** Setting up a new household system, when the current arrangement feels unfair or chaotic, when adding a new household member (partner moving in, child old enough for chores), or when tasks are falling through the cracks with no clear owner.

**Audience:** Solo adults managing their own home, couples, and families with children. Designed for households that want a repeatable system, not a one-time cleaning list. Not for professional cleaning services or households with house managers.

---

## Inputs Required

1. **Household composition.** Who lives in the house: adults (with names or initials), children (with ages). For children, ages matter — a 5-year-old and a 12-year-old have very different chore capacities.

2. **Chore inventory.** List the tasks that need to happen — everything you can think of. Don't filter yet. Examples: dishes, vacuuming, laundry, bathrooms, trash/recycling, grocery shopping, meal cooking, lawn, car maintenance, bills/finances. Include tasks you currently forget or that cause friction.

3. **Time available per person per week for chores.** Realistic estimate per household member: "Parent A has maybe 2 hours total spread across the week; Parent B has 3 hours on weekends; kids can do 20 minutes each on school nights." Be honest — the system will break if it's built on optimistic time estimates.

4. **Hard constraints.** Tasks a specific person cannot or will not do, with a brief reason if relevant (bad back, can't do heights, severe allergy, just relocated and doesn't know where things are yet). These are non-negotiable — the rotation must route around them.

5. **Friction points (optional).** Anything that has caused conflict or consistently doesn't get done. "Laundry gets done but never folded and put away." "Whoever cleans the bathroom first always cleans it forever." These often reveal the real design problem.

---

## Instructions

### Step 1 — Classify every chore by frequency and effort
Sort the chore inventory into six buckets:

| Class | Frequency | Effort per session | Examples |
|-------|-----------|-------------------|----------|
| Daily-light | Every day | 5–10 min | Dishes, wipe counters, sweep high-traffic |
| Daily-medium | Every day | 15–20 min | Cooking dinner, school pickup logistics |
| Weekly-light | Once/week | 10–15 min | Trash/recycling, surface tidy |
| Weekly-medium | Once/week | 20–40 min | Vacuuming, bathrooms, laundry |
| Monthly | Once/month | 30–60 min | Deep clean surfaces, floors, windows |
| Seasonal/ad-hoc | Quarterly or less | Variable | Garage, gutters, car, HVAC filter |

For each chore: assign a class and estimate minutes per session.

### Step 2 — Calculate load per person
Sum the weekly time commitment implied by the chore inventory:
- Daily tasks: (minutes per session) × 7
- Weekly tasks: minutes per session × 1
- Monthly tasks: (minutes per session) ÷ 4 (prorated to weekly)

Divide total weekly chore-minutes by number of household members who can contribute (adults and capable children). This is the target load per person. Flag if any person's available time is below their fair-share load — that's a signal the household needs to simplify, lower standards on some tasks, or hire out.

### Step 3 — Assign chores to people
Assign ownership (not "help with" — one person owns each task):

1. Apply hard constraints first: remove ineligible tasks from a person's options
2. Match task effort to available time per person
3. Give each person full ownership of a task category where possible (one person owns all bathrooms, another owns all laundry) — this is clearer than splitting the same task
4. For families with children: assign age-appropriate tasks (see table below)

**Age-appropriate child chore guide:**
- Age 4–6: Put away toys, set table, wipe low surfaces, sort laundry (darks/lights)
- Age 7–9: Vacuum with supervision, empty dishwasher, fold simple laundry, feed pets
- Age 10–12: Full laundry cycle, bathroom cleaning (with instruction first time), meal prep assistance, outdoor sweeping
- Age 13+: Any adult task with training; can own a category

### Step 4 — Build the rotation schedule
Produce two outputs:

**A. The master rotation:** Each task, its owner, and its frequency.

**B. A weekly snapshot template:** A Monday-through-Sunday grid showing which tasks happen which days and who does them. Design it so it fits on one page or could be printed and stuck to a fridge.

For rotating tasks (tasks that move between people week-to-week), specify the rotation pattern explicitly: "A this week, B next week — alternates." Don't leave rotation implicit.

### Step 5 — Address friction points
Return to any friction points listed in the inputs. For each:
- Identify the structural cause (task has no clear owner, task is defined too broadly, there's no completion signal)
- Adjust the rotation to fix the structure, not just re-assign blame

---

## Constraints

### Must
- Every task has a single named owner (no "shared" ownership without explicit alternation schedule)
- Load distribution must account for each person's available time — don't assign more than someone has
- Include age-appropriate chore assignments for any children listed
- Weekly snapshot template must be usable without the full document

### Must Not
- Assign the same task to multiple people without specifying who does it which week
- Assume equal available time across all adults unless explicitly stated
- Include tasks the user didn't list without flagging them as suggestions
- Moralize about who "should" be doing more housework
- Create a system so complex it requires a spreadsheet to track

---

## False-Positive Prevention

1. **Invisible load omission:** The rotation covers visible tasks (vacuuming, dishes) but misses invisible tasks (managing school forms, scheduling appointments, noticing when the soap is out and buying it). If the user lists mental-load tasks, assign them just like physical tasks. If they didn't list them, flag this as a gap.

2. **Equal-share illusion:** Divides tasks equally by count but not by time — Person A owns two 5-minute tasks, Person B owns one 60-minute task. Load must be balanced by time, not task count.

3. **Over-rotation:** Rotates every task weekly "to be fair" but this causes confusion about ownership. Stability (same person, same task, long-term) is usually better than constant rotation. Only rotate tasks where there's a genuine equity reason.

4. **Children overloaded or underloaded:** Assigns a 6-year-old tasks they can't do, or ignores a 14-year-old entirely. Assignments must match the age guide in Step 3.

5. **The "help" problem:** Assigns one person as task owner and another as "helper" — but helper assignments always drift to zero. Every task must have exactly one owner. Others may be mentioned as resources, but they're not co-owners.

---

## Output Format

```
## Household Chore Rotation
### [Household name / date]

---

### Task Classification

| Task | Class | Time/session | Owner | Frequency |
|------|-------|-------------|-------|-----------|
| Dishes | Daily-light | 10 min | [Name] | Daily |
| Vacuuming | Weekly-medium | 30 min | [Name] | Weekly |
| Bathrooms | Weekly-medium | 25 min | [Name] | Weekly |
| Laundry (wash + dry) | Weekly-medium | 20 min active | [Name] | Weekly |
| Laundry (fold + put away) | Weekly-light | 20 min | [Name] | Weekly |
| Trash/recycling | Weekly-light | 10 min | [Name] | Weekly (trash day) |
| [Additional tasks...] | | | | |

---

### Load Summary

| Person | Weekly chore-minutes assigned | Available time | Status |
|--------|------------------------------|----------------|--------|
| [Name A] | [X min] | [Y min] | OK / Over / Under |
| [Name B] | [X min] | [Y min] | OK / Over / Under |
| [Child, age] | [X min] | [Y min] | OK |

---

### Weekly Snapshot

| Day | Task | Who |
|-----|------|-----|
| Monday | Dishes | [Name] |
| Monday | [Other daily task] | [Name] |
| Tuesday | Dishes | [Name] |
| ... | | |
| Saturday | Vacuuming | [Name] |
| Saturday | Bathrooms | [Name] |
| Sunday | Laundry (wash + dry) | [Name] |
| Sunday | Laundry (fold + put away) | [Name] |

---

### Monthly & Seasonal Tasks

| Task | Month/timing | Owner |
|------|-------------|-------|
| [Deep clean X] | First Saturday of month | [Name] |
| [Seasonal task] | [Season/month] | [Name] |

---

### Friction Points Addressed

[If friction points were provided: what the structural fix is for each]

---

### Notes

[Any tasks near the edge of a child's capability, rotating tasks with the alternation schedule spelled out, or tasks flagged as candidates for hiring out]
```

---

## Verification

- [ ] Every task has exactly one owner (no "shared" without an alternation schedule)
- [ ] Load is balanced by minutes, not task count
- [ ] Hard constraints are respected — no task assigned to someone who can't do it
- [ ] Children are assigned only age-appropriate tasks per the guide
- [ ] Weekly snapshot fits on one page and is usable standalone
- [ ] Any friction points from inputs are addressed structurally
- [ ] Monthly and seasonal tasks are included with timing
- [ ] Load summary flags anyone who is over or under their available time
