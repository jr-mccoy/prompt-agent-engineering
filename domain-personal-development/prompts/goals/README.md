# Goals: Setting, Systems, and Skill Decomposition

Prompts for turning aspirations into structured, trackable goals — and for breaking a single skill into a practiceable path. Written for an individual planning and pursuing their own goals, not for a manager assigning objectives or a coach facilitating someone else's planning.

## When to use these

Use this subfolder when:

- You have wishes and aspirations but no system, and want to *build* one (SMART goals, trackers, review ritual, accountability).
- You already have goals and need a recurring *review-and-adjust* loop that compounds instead of drains.
- You want to learn a specific skill and feel overwhelmed by its scope — you need it decomposed into atomic, drillable sub-skills.

**Not the right subfolder when:**

- You can state a goal but keep failing to *act* on it — that's an execution problem; see `../agency/` (start with `agency_stuck_diagnosis.md`).
- You're a manager setting team objectives — see `domain-engineering-workflows/workflows/` or `domain-business-strategy/`.
- You're building a formal curriculum or training program for others — see `domain-education-teaching/`.
- The blocker is energy/scheduling, not goals — see `../productivity/`.

## Prompts in this subfolder

| Prompt | One-line description |
|---|---|
| `goals_goal_system_designer.md` | **Create** a goal system from raw aspirations: ≤5 SMART goals + per-goal trackers + Friday review ritual + accountability structure. |
| `goals_goal_setting_and_reflection_loop.md` | **Review and adjust** an existing goal system on a weekly/monthly/quarterly cadence — honest progress check, adjust/pause/drop, celebrate, set next review. |
| `goals_skill_breakdown_blueprint.md` | Decompose a **clearly named skill** into 7–9 sub-skills with a fully scheduled day-by-day 8-week plan, learning-path diagram, and pitfall section. |
| `goals_decompose_learning_task.md` | Decompose a still-**fuzzy learning goal** into 7–9 sub-skills with a lighter practice arc — front-loads goal clarification before scheduling. |
| `goals_annual_planning_and_theme.md` | Plan a **year or quarter from evidence**, not resolutions: ≤2 themes + 2–3 keystone goals derived from what last period actually produced/abandoned, plus one anti-resolution guardrail. |
| `goals_goal_conflict_resolver.md` | When **2+ goals compete** for the same finite resource (time/money/energy/attention), quantify the overrun and force one decision — rank or sequence — via a fixed cost-of-delay rule. |
| `goals_anti_goals_avoidance_list.md` | Define what you'll deliberately **NOT pursue** this period + the failure states to avoid, converting each into a tripwire that protects the keystone goals. |
| `goals_values_to_goals_derivation.md` | Derive **1–2 goals from your operating values** to close the values→action gap; defers values-surfacing to `identity_values_clarification.md`. |
| `goals_progress_stall_diagnostic.md` | A goal that **isn't moving**: classify the stall against a fixed 6-cause taxonomy (wrong goal/size, no next action, capacity, motivation, hidden conflict) and prescribe one unblock move. |
| `goals_scope_right_sizer.md` | **Right-size** a goal that's too big to start or too small to pull, calibrated to real weekly capacity and horizon via a dual-failure sizing test. |

## The two sibling pairs (read this before picking)

This folder contains two deliberately distinct pairs. They are **not** duplicates — pick by *where you are in the process*:

**Pair 1 — system creation vs. system review:**
- `goals_goal_system_designer.md` → use when **creating** the system for the first time (aspirations → structured system).
- `goals_goal_setting_and_reflection_loop.md` → use when the system **already exists** and you only need to review/adjust it on a cadence.

**Pair 2 — skill decomposition, by input sharpness:**
- `goals_skill_breakdown_blueprint.md` → use when the **skill is already clearly named** and you want the heavier, fully scheduled blueprint (Mon/Wed/Fri cadence, learning-path visualization, top-3 pitfalls).
- `goals_decompose_learning_task.md` → use when the input is a **fuzzy learning goal** that first needs goal-clarification, and you want a lighter practice arc.

Each prompt's `## When to Use` section restates its boundary against its sibling.

## Suggested composition / sequencing

- **New quarter from scratch:** `goals_goal_system_designer.md` → (if any goal is skill-based) `goals_skill_breakdown_blueprint.md` → run `goals_goal_setting_and_reflection_loop.md` weekly thereafter.
- **Learning something new:** start with `goals_decompose_learning_task.md` to sharpen the goal, then graduate to `goals_skill_breakdown_blueprint.md` once the target capability is named; fold the result into `goals_goal_system_designer.md` if it's one of several goals.
- **Ongoing:** `goals_goal_setting_and_reflection_loop.md` on a fixed cadence; escalate to `goals_goal_system_designer.md` only when the system itself needs a redesign.

## Shared design principles

- **Observable capabilities over topics.** Goals and skills are stated as things you can watch yourself *do*, not "understand X."
- **Fits stated time.** Schedules and systems are sized to the hours the user actually has; the prompts refuse to schedule against guessed capacity.
- **Honest triage.** Reviews are neither flattering nor punitive (dual-failure tested); dropping a dead goal is legitimate.
- **No fabrication.** The prompts refuse to invent goals, metrics, progress numbers, or schedules the user didn't supply.
- **Verification by prediction.** Where a plan is produced, the prompt states what should be observably true after week 1–2 so the user can tell if it's working.

## Related domains in this repo

- `../agency/` — execution and ownership: once a goal is set, agency prompts move it (stuck diagnosis, next-action spec, ship sprints). Upstream goal-setting feeds downstream agency work.
- `../productivity/` — energy, meetings, automation, open-loop capture (complementary; optimizes *when* and *how* you work on goals).
- `../thinking/` — reframing and blind-spot checks for your approach.
- `domain-learning/` — domain-agnostic learning craft (curriculum design, deliberate practice) at greater depth.
- `domain-personal-development/major-decisions/` — for high-stakes one-off decisions rather than recurring goals.
