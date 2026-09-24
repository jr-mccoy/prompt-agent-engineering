---
title: "NPC and Enemy AI Decision Architecture"
category: game-development/ai
description: "Choose and design the decision layer for NPCs and enemies — FSM/HFSM, behavior tree, utility AI, GOAP, or a hybrid — against behaviour count, designer authorship, readability to the player, and a per-frame CPU budget, then specify the behaviours, scoring curves, tick rates and failure modes; distinct from the general state-machine pattern prompt and from ML/LLM agents."
techniques:
  - RT-02
  - DS-01
  - NE-11
  - DP-07
difficulty: advanced
tags:
  - game-ai
  - behavior-trees
  - utility-ai
  - goap
  - npc
  - enemy-design
updated: "2026-09-24"
related_prompts:
  - domain-game-development/architecture/architecture_state_machine_design.md
  - domain-game-development/performance/performance_frame_budget_analysis.md
  - domain-game-development/design/design_mechanics_design.md
---

# NPC and Enemy AI Decision Architecture

**Objective:** Pick the decision architecture an NPC archetype actually needs,
specify its behaviours so designers can tune them and players can read them, and
show that the whole population fits inside the AI frame budget.

**When to Use:**
- A new enemy or NPC archetype is being designed and the team is arguing BT vs
  utility vs GOAP.
- Existing AI is a tangle of flags, dithers between actions, or blows the frame budget.
- Designers cannot tune AI without an engineer.

**When NOT to use:**
- Game-flow or character-controller state machines —
  `architecture/architecture_state_machine_design.md` owns FSM/HFSM/pushdown
  patterns in general; this prompt is distinct because it compares FSMs against
  BT, utility and GOAP for agent decision-making specifically.
- Machine-learned or LLM-driven agents — `domain-AI-ML/`.
- Pathfinding and navmesh generation — a navigation problem, referenced here only
  as a budget line.

## Inputs

1. **Archetype and role**: what the player should feel facing it (threatened,
   outwitted, amused) and its role in combat or the world.
2. **Behaviour list**: everything it must do, including idle and failure states.
3. **Population**: max simultaneous agents, and how many are typically active.
4. **AI CPU budget**: ms per frame at target frame rate, from the frame budget.
5. **Authors**: who tunes it (designer in editor, engineer in code).
6. **Engine**: built-in BT (Unreal), plugin, or custom.

## Method

1. **Score the candidates on the same axes (RT-02, DS-01).**
   | Axis | FSM/HFSM | Behavior tree | Utility | GOAP |
   |---|---|---|---|---|
   | Behaviour count it stays readable at | <10 | 10–50 | any, flat | any |
   | Designer-authorable | High | High | Medium (curves) | Low |
   | Player predictability | High | High | Medium | Low |
   | Emergent/novel sequences | None | Little | Some | High |
   | Debuggability | High | High | Medium (log scores) | Low (plan traces) |
   | Runtime cost | Lowest | Low | Low–Medium | Highest (planning) |
   Pick the simplest one that meets the archetype's needs; hybrids (BT with a
   utility selector at one node) are normal.
2. **Specify behaviours.** For each: trigger or score inputs, action, interrupt
   rules, and the **tell** — how the player sees what the agent is about to do.
3. **Write the scoring maths if utility is used (NE-11).** Each consideration is a
   normalised 0–1 input through a named curve (linear, quadratic, logistic);
   action score = product of considerations × weight. Add **momentum**: a bonus to
   the current action so agents do not flip every tick.
4. **Set tick rates and compute the budget (NE-11).**
   `cost/frame = Σ over tiers (agents × tick Hz ÷ fps × cost per tick)`, plus
   perception and path requests. Tier by relevance (combat, alert, idle, off-screen).
5. **Predict failure modes (DP-07).** Dithering, clumping, getting stuck,
   omniscience (acting on info the player can see it should not have), and
   pathological loops. For each: symptom, cause, guard.
6. **Define the debug view.** What a designer sees in-editor: current node or top
   three scores, perception cones, blackboard values.

## Output Format

```
## Recommendation   — architecture (or hybrid) and the axis that decided it
## Behaviour spec   — table: behaviour | inputs/trigger | action | interrupt | tell
## Scoring model    — (utility only) considerations, curves, weights, momentum
## Budget           — tier table with arithmetic, total vs budget
## Failure modes    — symptom | cause | guard
## Debug view       — what designers see
## Confidence       — per section; which numbers are [measure]
```

## Verification

- [ ] The chosen architecture is justified by at least one axis, not by habit.
- [ ] Every behaviour has an interrupt rule and a player-visible tell.
- [ ] Utility scores in the example are reproducible from the stated curves.
- [ ] Budget arithmetic sums; per-tick costs are marked `[measure]` until profiled.
- [ ] Each failure mode has a guard that can be tested.

## False-Positive Prevention

1. **Smarter is not better.** Players read enemies; an unreadable enemy feels
   unfair, not intelligent. Reject GOAP for a grunt that needs four behaviours.
2. **FSMs are not legacy.** For fewer than ten well-defined states they are the
   most debuggable option; do not recommend a BT rewrite for fashion.
3. **Utility dithering is a tuning bug, not an architecture flaw.** Fix it with
   momentum or hysteresis before proposing a new architecture.
4. **Do not invent per-tick costs.** Use `[measure]` and give the profiling step;
   the budget table is a model until then.
5. **Cheating AI is a design decision.** Omniscient spawn-direction knowledge may
   be intended; flag it only when it produces behaviour the player reads as unfair.
6. **Do not budget off-screen agents at full rate.** If the design already LODs AI,
   count the tiers it has, not a worst case it never reaches.

## Example

**Input:** Stealth-action guard. Behaviours: patrol, investigate noise, search,
alert allies, take cover, flank, suppress, flee at low HP, return to post.
Population: 40 max, typically 12 in combat, 28 idle/patrol. AI budget: 1.5 ms at 60 fps.

```markdown
## Recommendation
Behavior tree at the top level (patrol → investigate → search → combat → return)
with a utility selector inside the Combat branch. Nine behaviours exceed a
readable FSM; GOAP rejected on predictability — stealth players must learn patterns.

## Behaviour spec (excerpt)
| Behaviour | Trigger | Action | Interrupt | Tell |
|---|---|---|---|---|
| Investigate | noise ≥ 0.4 within 15 m | walk to noise origin | sight of player | "Huh?" bark + head turn |
| Alert allies | confirmed sight, no ally alerted in 5 s | shout, 20 m radius | taking damage | 1.2 s raised-arm anim |
| Flee | HP < 25% and allies < 2 | path away from player | cornered → fight | drops weapon stance |

## Scoring model (Combat selector)
| Action | Considerations (0–1) | Product × weight |
|---|---|---|
| Take cover | low-health 0.8 × exposed 0.9 × cover-available 1.0 | 0.72 × 1.0 = 0.72 |
| Flank | allies-present 0.7 × path-short 0.6 | 0.42 × 1.2 = 0.50 |
| Suppress | has-LOS 1.0 × ammo 0.9 × ally-flanking 0.6 | 0.54 × 1.0 = 0.54 |
Momentum +0.10 to the current action. Current = Suppress → 0.64 vs Take cover 0.72
→ switch to Take cover. Next tick, if exposure drops to 0.7 (cover 0.56 + 0.10 =
0.66 vs Suppress 0.54), the guard stays in cover instead of flipping back.

## Budget (per-tick costs [measure])
| Tier | Agents | Hz | Ticks/frame (÷60) | ms/tick | ms/frame |
|---|---|---|---|---|---|
| Combat (BT + utility) | 12 | 10 | 2.00 | 0.06 | 0.120 |
| Idle/patrol (BT) | 28 | 2 | 0.93 | 0.02 | 0.019 |
| Perception (4 rays each) | 40 | 5 | 3.33 × 4 = 13.3 rays | 0.01/ray | 0.133 |
| Path requests (queued) | — | — | 2 | 0.25 | 0.500 |
| **Total** | | | | | **0.772 of 1.5 ms** |
Headroom 0.73 ms. Worst case all 40 in combat: 40×10/60 × 0.06 = 0.40 ms for
decisions, no idle tier → 0.40 + 0.133 + 0.50 = 1.033 ms, still within budget.

## Failure modes
| Symptom | Cause | Guard |
|---|---|---|
| Guards flip cover↔suppress each tick | near-equal scores | momentum 0.10 (above) |
| Whole squad flanks the same side | shared path choice | claim flank slots on blackboard |
| Guard knows player position after losing sight | reading live position | search uses last-known position only |

## Debug view
Overlay: BT active node, top three utility scores with considerations, perception
cone coloured by awareness, last-known player position marker.

## Confidence
Recommendation: High. Scoring: Medium — curves need playtest tuning.
Budget: Low until per-tick costs are profiled on target hardware.
```

## Techniques Used

- **RT-02 (Multi-Dimensional Analysis Framework):** one axis table for all four architectures.
- **DS-01 (Framework Application):** FSM, BT, utility and GOAP applied as named frameworks.
- **NE-11 (Embedded Calculation Formulas):** utility products and the per-frame budget.
- **DP-07 (Failure Mode Prediction):** dithering, clumping and omniscience predicted with guards.

## Related Prompts

- `domain-game-development/architecture/architecture_state_machine_design.md` — FSM/HFSM patterns in depth.
- `domain-game-development/performance/performance_frame_budget_analysis.md` — where the 1.5 ms comes from.
- `domain-game-development/design/design_mechanics_design.md` — the combat mechanics the AI must exercise.
