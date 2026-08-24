# Agency, Ownership, and Execution

Prompts for self-directed work: moving vague goals into owned projects, diagnosing stuckness, shipping on a schedule, repairing broken habits, and turning individual sessions into a durable system. Written for an individual doing the work themselves — not for managers assigning work, not for coaches facilitating someone else's session.

## When to use these

Use this subfolder when:

- You can state a goal but haven't moved on it.
- You've been "working on" something for weeks with no artifact.
- You keep breaking habits you've rebuilt before.
- You need a short, specific next step, not a roadmap.
- You're about to ship something and want to extract signal from reactions.
- You want a weekly review that compounds rather than drains.

**Not the right subfolder when:**

- You're a manager assigning work to other people — see `domain-engineering-workflows/workflows/` or `domain-business-strategy/`.
- You're coaching someone else through their goals — this is first-person writing, not facilitation.
- You're building a formal curriculum or training program — see `domain-education-teaching/`.
- The problem is clinical (depression, anxiety) — this is personal-development, not mental health care.

## Prompts in this subfolder

| Prompt | One-line description |
|---|---|
| `agency_project_ownership_converter.md` | Convert a vague goal into a named project with a first deliverable and a single owner of record. |
| `agency_next_action_spec.md` | Cut a mental pile down to one physical next action defined at keystroke level. |
| `agency_planning_masquerade_detector.md` | Audit recent activity for research/tool-shopping/outlining that produces the feeling of progress without the artifact. |
| `agency_ship_sprint_design.md` | Design a 2–10 day sprint that forces a real deliverable into public view. |
| `agency_end_of_session_review.md` | A 5–10 minute session-close that captures what shipped and pre-stages the next session. |
| `agency_proof_of_work_portfolio.md` | Plan a 3–12 month portfolio of shipped artifacts that tells one coherent story. |
| `agency_feedback_extraction.md` | Convert messy reactions into classified signal and concrete change candidates. |
| `agency_weekly_review.md` | A 20–40 minute weekly review that compounds into a system instead of a diary. |
| `agency_stuck_diagnosis.md` | Classify "stuck" into one of 12 blocker types, each with its own unblock move. |
| `agency_skill_gap_reframe.md` | Separate a claimed skill gap from the project, so learning stops being a substitute for shipping. |
| `agency_habit_loop_repair.md` | Diagnose a broken habit and pick a repair sized to the break — repair over rebuild. |
| `agency_foundation_session.md` | Run a rare 2–4 hour session that establishes a project's foundation, with context capture so the work compounds. |
| `agency_rapid_start_mode.md` | A 60-second protocol from "at the desk" to "producing an artifact," for low-energy starts. |
| `agency_accountability_partner_design.md` | Pick the one accountability mechanism matched to the user's track record of follow-through, and produce the exact first message to set it up today. |
| `agency_personal_project_scope_creep.md` | Reconstruct a project's original commitment, classify everything added since, and re-cut to a shippable core with one next action. |

## How the prompts relate

The agency cluster is a small system, not 13 independent prompts. Expected compositions:

- **Starting a new project:** `agency_project_ownership_converter.md` → `agency_foundation_session.md` → `agency_next_action_spec.md` at the end of day 1.
- **You're stuck:** `agency_stuck_diagnosis.md` first. Its output will point to the specific follow-up prompt (`agency_next_action_spec.md`, `agency_planning_masquerade_detector.md`, `agency_skill_gap_reframe.md`, etc.).
- **Every work session:** Optional `agency_rapid_start_mode.md` at the start, `agency_end_of_session_review.md` at the end.
- **Every week:** `agency_weekly_review.md`.
- **Pushing to finish:** `agency_personal_project_scope_creep.md` to re-cut to a shippable core, then `agency_ship_sprint_design.md` for a bounded push, `agency_feedback_extraction.md` after.
- **Can't follow through alone:** `agency_accountability_partner_design.md` to arrange a structure matched to what actually makes the user deliver.
- **Long arc:** `agency_proof_of_work_portfolio.md` to shape a 3–12 month cadence.
- **When the habit breaks:** `agency_habit_loop_repair.md`.

## Shared design principles

These prompts share a small set of constraints:

- **Physical-motion level.** Actions are named at the level of "open file X, type Y," not "think about Z."
- **Artifacts over activity.** The honest test of a session is what exists that didn't exist before.
- **Fixed taxonomies over open menus.** Where a diagnosis or classification is needed, a small fixed set of options is used so the prompt converges.
- **Owner of record.** Personal projects have one owner — the user. Shared ownership is flagged as a failure mode, not a feature.
- **No motivational language.** The prompts state structure and ask for commitment; they don't cheerlead.
- **Rest is legitimate.** Depletion is a real category; the answer to tiredness is rest, not reframing.

## Related domains in this repo

- `domain-productivity/deep-work/` — focus, calendar audits, meeting replacement (complementary).
- `domain-productivity/validation/` — reality-check prompts for decisions (complementary).
- `domain-personal-development/prompts/goals/` — goal system design and skill breakdown (upstream of agency work).
- `domain-engineering-workflows/ai-patterns/` — cross-references for weekly reflection and rule extraction when working with AI assistance.
- `domain-prompt-engineering/delegation/` — cross-references for specifying intent when handing a task off.
