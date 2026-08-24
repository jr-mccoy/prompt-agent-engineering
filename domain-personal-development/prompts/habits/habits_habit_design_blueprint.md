---
title: "Design a New Habit From Cue, Routine, Reward, and Implementation Intention"
category: personal-development/habits
description: "Turn a vague intention ('I want to exercise more') into a concretely engineered habit loop — a specific cue, a floor-sized routine, an honest reward, and an if-then implementation intention — that can actually run on a low-motivation day."
techniques:
  - ST-01
  - ST-02
  - DS-01
  - NE-09
  - QA-20
  - QA-01
difficulty: intermediate
tags:
  - habits
  - behavior-change
  - habit-design
  - implementation-intentions
  - cue-routine-reward
updated: "2026-06-21"
related_prompts:
  - domain-personal-development/prompts/habits/habits_habit_stacking_designer.md
  - domain-personal-development/prompts/habits/habits_environment_design_for_habits.md
  - domain-personal-development/prompts/habits/habits_keystone_habit_identifier.md
  - domain-personal-development/prompts/agency/agency_habit_loop_repair.md
  - domain-personal-development/prompts/goals/goals_goal_system_designer.md
---

# Design a New Habit From Cue, Routine, Reward, and Implementation Intention

**Objective:** Convert a stated intention into a fully specified habit loop — cue, routine, reward, and an if-then implementation intention — sized so the floor version still runs on the user's worst realistic day.

## When to Use

- Use when: the user wants to *start* a new repeatable behavior (exercise, writing, flossing, reading, language practice) and has not yet built it.
- Use when: a previous attempt failed vaguely ("I just stopped") and the user wants the behavior engineered rather than willed.
- Use when: the user can name the outcome they want but not the specific daily action that produces it.
- **Don't use when:** the habit already ran and recently broke — that is a *repair* problem; route to `agency_habit_loop_repair.md`.
- **Don't use when:** the user wants to *remove* a behavior — route to `habits_break_bad_habit_protocol.md`.
- **Don't use when:** the real goal is multi-habit life redesign — start with `habits_keystone_habit_identifier.md` to find the one habit that cascades first.

## Inputs / Context

Collect from the user:

1. **The behavior they want to build.** One sentence, as an action ("do 10 push-ups"), not an outcome ("get fit").
2. **Their honest daily rhythm.** When they wake, work, eat, wind down; where the dead time and the existing anchors are.
3. **The worst realistic day.** Sick, slammed, traveling, low mood — what a *bad* day looks like for them.
4. **What they've tried before for this behavior and what happened.** Verbatim if possible.
5. **Why this matters to them now.** One sentence. (Used to size the reward and sanity-check the habit is wanted, not borrowed from someone else.)

**Refusal logic:** If the user gives only an outcome ("be healthier") with no candidate action, do not invent five habits. Ask them to name one behavior they believe would move the outcome, or offer 2–3 concrete candidate actions and ask them to pick one. If inputs 2 and 3 are missing, ask for them — a habit designed without a real cue slot and a worst-day floor is guesswork. Design exactly **one** habit per run.

## Instructions

### Step 1 — Lock the routine at the floor, not the aspiration

Define two sizes of the behavior:

- **Floor version:** The smallest version that still counts as "done" and that survives the worst realistic day (e.g., "one push-up," "open the doc and write one sentence"). The floor is the actual commitment.
- **Target version:** What a good day looks like. The target is allowed, never required.

Apply scope-reduction pressure (NE-09): if the floor would not survive input 3 (the worst day), it is too big. Shrink it until it would.

### Step 2 — Find a real cue

A cue must be something that already reliably happens. Classify the chosen cue:

| Cue type | Example | Reliability check |
|---|---|---|
| Time | "7:00am" | Only if the user's mornings are actually stable. |
| Preceding action | "after I pour my morning coffee" | Strongest type; the anchor already fires daily. |
| Location | "when I sit at my desk" | Works if the location is daily and singular. |
| Emotional/state | "when I feel the afternoon slump" | Weakest; states are unreliable cues — use only as backup. |

Prefer a **preceding-action cue** anchored to an existing routine. If the user has many stable routines, hand off to `habits_habit_stacking_designer.md` for a fuller stack; here, pick one anchor.

### Step 3 — Specify the reward honestly

The reward is what makes the loop self-reinforcing. Classify:

- **Intrinsic-immediate:** The behavior itself feels good right after (a stretch, a clear inbox). Best — name it explicitly so the user notices it.
- **Designed-immediate:** A small added reward delivered right after (mark a tracker, a song, a checkmark). Use when intrinsic reward is delayed.
- **Delayed-only:** The payoff is weeks away (weight, skill). Flag this as a risk — delayed-only rewards do not reinforce loops. Pair with a designed-immediate reward.

Reject rewards that undercut the behavior (e.g., "ice cream after the run" for a fitness habit).

### Step 4 — Write the implementation intention

Produce one if-then sentence in the exact form:

> **"When [cue], I will [floor-version routine] [in/at location]."**

Then write the **obstacle plan** — a second if-then for the most likely failure:

> **"If [most likely obstacle], then I will [pre-decided fallback that still counts as the floor]."**

### Step 5 — Set the first-week tracking rule (lightweight)

Define what the user marks and when. Keep it to a single binary mark per day ("did the floor: yes/no"). Do not recommend an app. Specify the streak-recovery stance up front: "missing once is data, not failure — see `habits_streak_recovery_plan.md` if you miss."

### Step 6 — Verify the design against the worst day

Re-read input 3 and confirm the floor version + cue + obstacle plan would actually fire on that day. If not, return to Step 1.

## Constraints

**Must:**
- Design exactly one habit per run.
- Produce a distinct floor version and target version.
- Anchor the cue to something that already reliably happens.
- Output an implementation-intention sentence and an obstacle if-then.
- Confirm the floor survives the user's stated worst day.

**Must Not:**
- Recommend a tracking app, gamification platform, or new system.
- Stack multiple new habits at once (route to the stacking prompt instead).
- Promise the habit "will stick this time."
- Set a 30-day or 90-day challenge as the design.
- Moralize, shame, or lecture about discipline or willpower.
- Provide clinical or therapeutic framing. If the user ties the habit to acute distress (e.g., "I need this or I'll spiral"), gently note that behavior design is not mental-health care and point toward appropriate support (`domain-psychology/`).

## False-Positive Prevention

1. **Don't accept an outcome as a routine.** "Get fit" is not a habit; "do 10 squats after coffee" is. If the user only gave an outcome, do not proceed until a specific action exists.
2. **Don't approve an aspirational floor.** If the floor is "30 minutes of cardio," it is a target masquerading as a floor. The floor must survive the worst day — test it against input 3 explicitly.
3. **Don't attach the habit to an unreliable cue.** A time cue on someone with chaotic mornings, or an emotional-state cue, will silently fail. Verify the cue actually fires daily.
4. **Don't ignore delayed-only rewards.** If the only payoff is weeks out, the loop has no reinforcement; flag it and add a designed-immediate reward rather than assuming motivation will carry it.
5. **Don't design around motivation.** Any plan that requires the user to "feel like it" is a false design. The floor + cue + obstacle plan must work on a zero-motivation day.
6. **Don't conflate wanting the identity with wanting the behavior.** If input 5 reveals the user wants to *be a runner* more than they want to run, name that — borrowed habits rarely survive.

## Dual-Failure Prevention (QA-20)

- **Harmful failure:** Designing a floor so demanding it guarantees failure and reinforces "I can't keep habits." Guard by stress-testing the floor against the worst day.
- **Unhelpful failure:** Over-hedging the design into vagueness ("just try to do a little when you can") so the user has nothing concrete to execute. Guard by always emitting one specific if-then sentence.

## Expected Output

A single habit blueprint: floor/target, classified cue, classified reward, the implementation-intention sentence, the obstacle plan, a one-line tracking rule, and a worst-day check.

### Output Template

```
# Habit Blueprint: [behavior]

## The loop
- Cue: [chosen cue] — type: [Time / Preceding action / Location / State] — why it's reliable: [...]
- Routine (floor): [smallest version that still counts]
- Routine (target): [good-day version — allowed, not required]
- Reward: [classified: Intrinsic-immediate / Designed-immediate / Delayed-only (+ paired immediate reward)]

## Implementation intention
"When [cue], I will [floor routine] [at location]."

## Obstacle plan
"If [most likely obstacle], then I will [pre-decided fallback that still counts]."

## Tracking
Mark once a day: did the floor — yes/no. Nothing else. (No app.)

## Worst-day check
On a [user's worst-day description] day, this still runs because: [reason].

## Wanted-or-borrowed note
[One line: is this the user's behavior, or an identity they're chasing?]
```

## Example Output

```
# Habit Blueprint: daily strength movement

## The loop
- Cue: "after I pour my morning coffee" — type: Preceding action — why it's reliable:
  user pours coffee every single day, including bad days, at a fixed spot.
- Routine (floor): 5 bodyweight squats next to the kitchen counter.
- Routine (target): a 12-minute mobility + strength circuit in the spare room.
- Reward: Intrinsic-immediate (user reports feeling "switched on" right after movement)
  + Designed-immediate (a single check on the fridge whiteboard).

## Implementation intention
"When I pour my morning coffee, I will do 5 squats at the kitchen counter."

## Obstacle plan
"If I'm running late and skip the full circuit, then I will still do the 5 squats
while the coffee brews — that counts."

## Tracking
Mark once a day on the fridge whiteboard: floor done — yes/no. No app.

## Worst-day check
On a sick, low-energy, late-for-work day, 5 squats by the counter still runs
because it costs under 30 seconds and the coffee cue still fires.

## Wanted-or-borrowed note
User's stated reason ("I want energy for my kids in the evening") is concrete and
personal, not a borrowed "should." Genuinely wanted.
```

## Verification

- [ ] Exactly one habit was designed.
- [ ] Floor version and target version are distinct, and the floor is genuinely small.
- [ ] The floor was explicitly tested against the user's stated worst day.
- [ ] The cue is something that already reliably happens (preferably a preceding action).
- [ ] The reward is classified, and any delayed-only reward was flagged and paired.
- [ ] An implementation-intention sentence and an obstacle if-then are both present.
- [ ] No app, no 30/90-day challenge, no willpower lecture appears.
- [ ] A wanted-or-borrowed note is included.

## Techniques Used

- **ST-01 (Clear Objective Statement):** Fixes the deliverable as one fully-specified loop, not generic habit advice.
- **ST-02 (Structured Sequential Instructions):** Six ordered steps move from floor → cue → reward → intention → tracking → verification.
- **DS-01 (Framework Application):** Applies the cue–routine–reward loop plus implementation-intention framework as the design scaffold.
- **NE-09 (Scope Reduction Pressure):** Step 1 actively shrinks the floor until it survives the worst day.
- **QA-20 (Dual-Failure Quality Test):** Guards against both an over-demanding floor and a uselessly vague one.
- **QA-01 (Chain-of-Verification):** Step 6 and the verification checklist confirm the design holds before it ships.

## Related Prompts

- [habits_habit_stacking_designer.md](habits_habit_stacking_designer.md) — When the user has several stable anchors and wants a chain, not one loop.
- [habits_environment_design_for_habits.md](habits_environment_design_for_habits.md) — Engineer the surroundings so the cue and floor are even easier to fire.
- [habits_keystone_habit_identifier.md](habits_keystone_habit_identifier.md) — Pick *which* habit to design first when several compete.
- [agency_habit_loop_repair.md](../agency/agency_habit_loop_repair.md) — When a designed habit has broken and needs repair, not fresh design.
- [goals_goal_system_designer.md](../goals/goals_goal_system_designer.md) — When the habit should connect to a larger goal system.
