# Deep Work & Focus Prompts

Personal focus-system prompts for an individual knowledge worker auditing and redesigning their own deep-work practice. Not team-wide policy or manager-imposed norms (except where a specific prompt is scoped that way).

These prompts assume the user is willing to look at their own calendar, session logs, interruption data, and outputs honestly. They resist producing generic productivity advice — every prompt forces output back to the user's actual data.

## When to Use

Use these when:
- Focus blocks are planned but repeatedly destroyed
- "Productive" weeks still don't produce shipped work
- Calendar or messages feel unwinnable
- The user wants a measurement, not encouragement

Do **not** use these for:
- Motivation or discipline issues (those belong to `domain-personal-development/`)
- Team-wide process change (except `deepwork_team_focus_audit.md`, which is scoped to a team lead)
- Decision validation (`domain-productivity/validation/`)
- Task prioritization across projects (`domain-engineering-workflows/tasks/`)

## Prompts

### Diagnose (measure what's actually happening)
- [`deepwork_focus_parameters_estimator.md`](deepwork_focus_parameters_estimator.md) — Compute attention span, reload cost, interruption rate, recovery time from the user's real session logs
- [`deepwork_calendar_audit.md`](deepwork_calendar_audit.md) — Classify a week's calendar against a fixed taxonomy of focus-destruction patterns
- [`deepwork_self_interruption_audit.md`](deepwork_self_interruption_audit.md) — Separate external from self-interruptions and classify self-interruptions into one of five functions
- [`deepwork_lost_focus_day_troubleshoot.md`](deepwork_lost_focus_day_troubleshoot.md) — Post-mortem a single lost day against fixed failure modes

### Design (build systems around the measurements)
- [`deepwork_message_triage_system.md`](deepwork_message_triage_system.md) — Route incoming messages to one of five actions, tuned to the user's actual sender mix
- [`deepwork_meeting_to_async_converter.md`](deepwork_meeting_to_async_converter.md) — Convert one specific meeting to async, or decide it must stay sync
- [`deepwork_meeting_cost_estimator.md`](deepwork_meeting_cost_estimator.md) — Compute the true person-minute cost of a meeting including prep and block destruction
- [`deepwork_reload_ritual_design.md`](deepwork_reload_ritual_design.md) — Design a ≤ 5-step, timeboxed ritual that reduces context-reload cost
- [`deepwork_team_focus_audit.md`](deepwork_team_focus_audit.md) — Team-lead-scoped audit and 3–5 proposed team norms tied to observed patterns

### Plan (match work to available time)
- [`deepwork_chunk_project_to_calendar.md`](deepwork_chunk_project_to_calendar.md) — Break a project into chunks sized to real free blocks
- [`deepwork_decompose_complex_task.md`](deepwork_decompose_complex_task.md) — Decompose one stuck task into sub-tasks with entry points and verifications
- [`deepwork_match_tasks_to_calendar.md`](deepwork_match_tasks_to_calendar.md) — Match today's tasks to today's calendar; surface which will not happen

### Reload (enter and exit focus blocks cleanly)
- [`deepwork_block_end_context_capture.md`](deepwork_block_end_context_capture.md) — Produce a reload packet at the end of a focus block
- [`deepwork_project_state_synthesis.md`](deepwork_project_state_synthesis.md) — Pull scattered project state into a reload brief
- [`deepwork_handwritten_notes_digitizer.md`](deepwork_handwritten_notes_digitizer.md) — Convert handwritten notes into decision log / action list / idea cluster
- [`deepwork_focus_block_async_summary.md`](deepwork_focus_block_async_summary.md) — Turn end-of-block output into an async update for a specific collaborator

### Evaluate (test whether a change worked)
- [`deepwork_focus_experiment_week.md`](deepwork_focus_experiment_week.md) — Design and review a one-week experiment of a single focus-system change

## Typical Sequences

**First-time audit:**
1. `deepwork_focus_parameters_estimator.md` — measure
2. `deepwork_calendar_audit.md` — structure
3. `deepwork_self_interruption_audit.md` — behavior
4. Pick the worst finding, design against it, test with `deepwork_focus_experiment_week.md`

**Daily use:**
- Morning: `deepwork_match_tasks_to_calendar.md`
- End of each block: `deepwork_block_end_context_capture.md` (for self) and/or `deepwork_focus_block_async_summary.md` (for collaborators)
- Returning to a project: `deepwork_project_state_synthesis.md` → `deepwork_reload_ritual_design.md`

**When it goes wrong:**
- `deepwork_lost_focus_day_troubleshoot.md` for a single bad day
- `deepwork_self_interruption_audit.md` if the pattern repeats

## Related

- Bottlenecks & personal constraints: [`../bottlenecks/`](../bottlenecks/)
- Agency, ownership, and execution: [`../../domain-personal-development/prompts/agency/`](../../domain-personal-development/prompts/agency/)
- Decision validation: [`../validation/`](../validation/)
- AI-augmented development workflow: [`../../domain-engineering-workflows/ai-patterns/`](../../domain-engineering-workflows/ai-patterns/)
