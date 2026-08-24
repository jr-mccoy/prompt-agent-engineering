# Habits Prompts

Behavior-change *mechanics* — the engineering of habit loops, not motivation or mindset. This cluster covers designing new habits, breaking unwanted ones, stacking onto existing routines, recovering from broken streaks, finding the one habit that cascades, shaping the environment around a habit, designing a habit from the identity it votes for, converting vague intentions into precise if-then triggers, building a sustainable tracking system, and bundling a want with a should-do so the habit pulls itself.

These prompts assume the user is willing to engineer the behavior (cue, floor-sized routine, reward, friction) rather than rely on willpower or a fresh burst of motivation. Every prompt sizes the behavior to the user's *worst realistic day*, not their best.

## Scope

**In scope:**
- Designing a new habit from cue → routine → reward + implementation intentions
- Breaking an unwanted habit via friction analysis + reward-matched substitution
- Habit stacking (anchoring a new habit onto a reliable existing routine)
- Streak recovery (re-entry after a miss without the all-or-nothing spiral)
- Keystone-habit identification (the single habit whose change cascades)
- Environment design for a specific habit (cue visibility + steps-to-start)
- Identity-based habit design (the smallest behavior that votes for "someone who X")
- Implementation-intention building (vague intention → precise if-then triggers + coping plans)
- Tracking-system design matched to the user's real logging tolerance
- Temptation bundling (pairing a want with a should-do so the reward makes the habit self-pulling)

**Out of scope (refuse and refer):**
- Substance dependency, disordered eating, self-harm, compulsive behavior causing distress → professional support / `domain-psychology/`
- Persistent harsh self-attack beyond ordinary disappointment → `identity_self_talk_audit.md` or `domain-psychology/`
- Clinical mental-health conditions → professional support
- Whole-**workspace** deep-work / focus redesign → `domain-productivity/deep-work/`

## Relationship to neighboring clusters

- **`agency/agency_habit_loop_repair.md`** handles *repair* of a habit that ran and broke over a longer period. This cluster's `habits_streak_recovery_plan.md` handles the *short* miss + spiral; it routes to the agency prompt for longer breaks. They complement, not duplicate.
- **`domain-productivity/deep-work/deepwork_environment_friction_design.md`** audits the *whole workspace* for focused work. This cluster's `habits_environment_design_for_habits.md` engineers the surroundings of *one specific habit loop*. Use one or the other for a given problem, not both.

## Composition patterns

These prompts are designed to compose. Common chains:

- **Overwhelmed-by-many-habits route:** `habits_keystone_habit_identifier` → pick one keystone → `habits_habit_design_blueprint` → optionally `habits_environment_design_for_habits`.
- **New-habit route:** `habits_habit_design_blueprint` → if a reliable anchor exists, `habits_habit_stacking_designer` → `habits_environment_design_for_habits` to remove friction → `habits_tracking_system_designer` for a sustainable measurement layer.
- **Identity-first route:** `habits_identity_based_habit_designer` (pick the vote) → `habits_habit_design_blueprint` (build the loop mechanics) → `habits_implementation_intention_builder` (tighten the if-then triggers).
- **Weak-pull route:** should-do habit keeps losing → `habits_temptation_bundling_designer` (make it self-pulling) → `habits_environment_design_for_habits` if the bundle needs exclusivity friction.
- **Breaking-a-habit route:** `habits_break_bad_habit_protocol` → `habits_environment_design_for_habits` (decrease direction) for the friction moves.
- **Miss/relapse route:** `habits_streak_recovery_plan` → if the gap is long or restarts keep failing, `agency_habit_loop_repair` → if the cause is deeper, `agency_stuck_diagnosis`.
- **Wanted-vs-borrowed route:** any design prompt → if the habit seems borrowed from an identity rather than genuinely wanted, `identity_values_clarification`.

## What the prompts refuse

- Willpower/discipline lectures and motivational pep talks
- New tracking apps, gamified systems, and 30/90-day "challenges" as the answer
- Promises that "this time it'll stick"
- Designing multiple new habits at once (focus is the point)
- Pathologizing ordinary habits — or, conversely, protocoling away genuine dependency/clinical issues (those get a referral)
- Floors sized to a good day instead of a bad day

## File map

| Prompt | Purpose |
|---|---|
| `habits_habit_design_blueprint.md` | Build a new habit: floor/target routine, classified cue, honest reward, implementation intention + obstacle plan; stress-tested against the worst day. |
| `habits_break_bad_habit_protocol.md` | Remove an unwanted habit: reverse-engineer the loop, find the real reward, raise friction, install a reward-matched substitute. |
| `habits_habit_stacking_designer.md` | Anchor a small new habit onto a reliable existing routine with a scored anchor selection and an exact "after X, I will Y" formula. |
| `habits_streak_recovery_plan.md` | Recover after a missed streak without the all-or-nothing spiral: name the distortion, kill punitive catch-up, re-enter at the floor, never miss twice. |
| `habits_keystone_habit_identifier.md` | Find the single habit whose change cascades into others; score candidates for leverage, gate by feasibility, recommend one. |
| `habits_environment_design_for_habits.md` | Engineer the surroundings of one habit (cue visibility + steps-to-start) to make it run, or hide the cue + add friction to stop it. |
| `habits_identity_based_habit_designer.md` | Design a habit from the identity it votes for ("become someone who X"): separate identity from outcome, keep only evidence-generating votes, floor-size one undeniable rep, reframe tracking as identity evidence. |
| `habits_implementation_intention_builder.md` | Convert a vague intention into precise "when [cue], I will [action] [at location]" if-thens anchored to reliably-firing cues, plus a coping if-then per predictable obstacle. |
| `habits_tracking_system_designer.md` | Design the lightest tracking system the user will actually keep — purpose-picked single metric, tolerance-matched medium, anchored logging moment, non-punitive miss-rule, and a kill condition for the tracker itself. |
| `habits_temptation_bundling_designer.md` | Pair a genuinely wanted activity with a should-do habit so the reward makes the habit self-pulling; test physical compatibility, reject undercutting/leaky bundles, set exclusivity, converge to one bundle. |
