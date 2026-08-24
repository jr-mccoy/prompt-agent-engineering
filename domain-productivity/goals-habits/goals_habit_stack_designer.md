---
title: "Habit Stack Designer"
category: productivity/goals-habits
description: "Anchor a new habit to an existing routine by designing an explicit habit stack with cue, routine, and a 30-day starter plan."
techniques:
  - ST-01
  - ST-03
  - DS-01
  - CM-02
  - QA-01
  - RT-02
difficulty: beginner
tags:
  - habits
  - habit-stacking
  - behavior-design
  - routine
  - starter-plan
updated: "2026-05-12"
related_prompts:
  - domain-productivity/goals-habits/goals_habit_repair.md
  - domain-productivity/goals-habits/goals_personal_tracking_dashboard.md
  - domain-productivity/bottlenecks/bottleneck_procrastination_systems_diagnostic.md
  - domain-personal-development/prompts/agency/agency_habit_loop_repair.md
---

# Habit Stack Designer

**Objective:** Design a habit stack that anchors a new behavior to an existing reliable routine. Produces the stack structure (anchor → cue → routine → optional reward) and a concrete 30-day starter plan with graduated difficulty.

**When to use:** When someone wants to start a new habit and hasn't started yet, or has tried and failed to make it stick through willpower alone. Use this when there is an existing daily routine to anchor to. If the habit has already been built and broken, use `goals_habit_repair.md` instead.

**Audience:** Anyone trying to establish a new personal habit — health, learning, creative practice, professional development. Not for team behavioral change or organizational culture work. Not for habits requiring major infrastructure (gym membership required, equipment not owned) — those logistics must be sorted before designing the stack.

---

## Inputs Required

1. **The specific habit you want to build.** Must be specific enough to be observable: not "exercise" but "do 10 pushups"; not "read more" but "read for 15 minutes." If the input is vague, this prompt will challenge it before proceeding.
2. **Your existing daily routine.** What do you reliably do every day? List morning, midday, and evening anchors — things you do without thinking (brew coffee, brush teeth, sit down at your desk, eat lunch, get into bed). Include approximate times.
3. **How long the new habit should take in its starter form.** The starter version — not the aspirational version. If you want to meditate 20 minutes eventually, the starter might be 2 minutes. Name the starter duration.
4. **Previous attempts (if any) and why they failed.** What broke the habit last time? Specific circumstances — travel, schedule change, forgetting, the routine becoming effortful. If no previous attempts, say so.

---

## Instructions

### Step 1 — Gate: Force specificity on the habit
If the habit is vague (a category rather than a behavior), stop and ask: "What specifically will you do? Describe the action in terms someone could observe from outside the room. How long will it take?"

Do not proceed until the habit is specific and has a defined duration.

### Step 2 — Select the anchor
From the existing routine the user provided, identify the best anchor for this habit. Selection criteria (in priority order):

1. **Reliability:** The anchor must happen nearly every day without decision. Brush teeth beats "when I feel like it."
2. **Temporal fit:** The anchor should occur at roughly the right time of day for the new habit. Don't anchor a morning habit to an evening routine.
3. **Contextual fit:** The anchor should occur in or near the physical context where the new habit will happen. Don't anchor "do pushups" to "sit down at my desk" if you do pushups in a different room.
4. **Cognitive state fit:** The anchor should precede a moment when cognitive load is manageable — don't attach a focus-requiring new habit to the end of a depleting anchor.

State which anchor was selected and why. If no good anchor exists in their routine, say so and ask them to identify one reliable daily behavior first.

### Step 3 — Design the stack
Produce the full stack:

- **Anchor:** [The existing habit]
- **Cue:** [The specific moment or signal that transitions from anchor to new habit — "as soon as I finish X" or "immediately after X"]
- **Routine:** [The new habit in its minimum startable form, exactly as the user will do it]
- **Reward (optional):** [A brief acknowledgment or small reward that closes the loop — not a food reward if the habit is health-related. Can be as simple as checking a box or saying "done."]

### Step 4 — Build the 30-day starter plan
Divide into three phases:

**Week 1 (Days 1–7): Minimum version**
A reduced version of the habit — easier than the user's stated starter duration. If they said 10 pushups, Week 1 is 5 pushups. The goal is to establish the anchor-to-routine trigger, not to accomplish the full habit. Consistency over completeness.

**Weeks 2–3 (Days 8–21): Standard version**
The full starter version the user named. Same anchor, same cue, now the full routine.

**Week 4 (Days 22–30): Evaluate and adjust**
A structured evaluation — not automatic escalation. At day 22, the user assesses: Is the stack running reliably? If yes, decide whether to extend duration or intensity. If no, diagnose what's breaking before adding difficulty.

### Step 5 — Name the failure modes
Based on the user's previous attempts and the stack design, name 2–3 specific ways this stack is likely to break, and a pre-planned response for each. Not generic warnings — specific to this habit and this person's described routine.

---

## Constraints

### Must
- Require specificity on the habit before proceeding
- Select the anchor from the user's actual stated routine — not a generic suggestion
- Start Week 1 below the user's stated starter difficulty
- Name specific failure modes based on their history and routine
- Distinguish between the anchor (existing habit), cue (transition moment), and routine (new habit)

### Must Not
- Prescribe a habit the user didn't ask for (no "you should also try meditation")
- Recommend a tracking app as the solution — the deliverable is the stack design
- Use willpower or motivation as a design element
- Start Week 1 at full difficulty
- Add aspirational scaling (week 5, week 6, etc.) — the 30-day plan ends at 30 days with an evaluation

---

## False-Positive Prevention

1. **Anchor that isn't actually reliable:** "After lunch" is not reliable if the user skips lunch, eats at their desk, or has meetings through lunch 3 days a week. Push for an anchor that happens 6–7 out of 7 days.
2. **Stack that requires travel between contexts:** If the anchor ends in one room and the new habit happens in another, the transition itself becomes a failure point. Either move the anchor or redesign around a single location.
3. **Week 1 that isn't easier than Week 2:** If Week 1 and Week 2 are the same, the ramp doesn't exist. Force Week 1 to be visibly simpler.
4. **Failure modes that are generic:** "You might get busy" is not a failure mode — it's a non-answer. Name the specific circumstance from the user's history or routine that will cause the break.
5. **Reward that undermines the habit:** Don't suggest food rewards for fitness habits, or phone-check rewards for focus habits.

---

## Output Format

```
HABIT STACK DESIGN
Generated: [Date]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
THE STACK

  Anchor:  [Existing habit — e.g., "Brew morning coffee"]
  Cue:     [Transition moment — e.g., "As soon as the coffee is poured"]
  Routine: [New habit, minimum startable form — e.g., "Do 10 pushups in the kitchen"]
  Reward:  [Optional — e.g., "Check the box on my calendar"]

Full sentence: "After I [anchor], I will immediately [routine]."
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

30-DAY STARTER PLAN

  Week 1 (Days 1–7) — Minimum version
  Action: [Reduced form of the habit]
  Goal: Run the trigger reliably, not complete the full habit.

  Weeks 2–3 (Days 8–21) — Standard version
  Action: [Full starter version as named by user]
  Goal: Consistency at full starter difficulty.

  Week 4 (Days 22–30) — Evaluate
  Action: [Same as Weeks 2–3]
  Evaluation questions to answer on Day 22:
    1. Did the stack run on ≥5 of the past 7 days?
    2. Does the anchor still reliably precede the routine?
    3. Am I ready to increase difficulty, or do I need another week at this level?
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

LIKELY FAILURE MODES AND PRE-PLANNED RESPONSES

  Failure Mode 1: [Specific scenario — e.g., "Travel disrupts the morning anchor"]
  Pre-planned response: [Specific action — e.g., "Switch to hotel room equivalent: same routine, skip quantity expectation"]

  Failure Mode 2: [Specific scenario]
  Pre-planned response: [Specific action]

  Failure Mode 3: [Specific scenario, if applicable]
  Pre-planned response: [Specific action]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

---

## Verification

- [ ] The habit is specific and observable — not a category
- [ ] The anchor was selected from the user's actual stated routine
- [ ] The anchor occurs 6–7 days/week without conscious decision
- [ ] The anchor and the new habit share the same or adjacent physical context
- [ ] Week 1 is visibly easier than Weeks 2–3
- [ ] Failure modes are specific to this person's history and routine — not generic
- [ ] No tracking app was recommended as the primary solution
- [ ] No additional habits were prescribed beyond what the user requested
