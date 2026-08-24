# Productivity: Energy, Meetings, Automation, and Open Loops

Prompts for reclaiming time and attention: auditing where your energy goes, killing meetings that have outlived their purpose, finding the highest-ROI work to automate, and emptying the mental backlog into a trusted system. Written for an individual optimizing their own working life — not for an ops team redesigning org-wide process.

## When to use these

Use this subfolder when:

- You feel busy all day but unproductive, and want to know *when* your high-value work should happen.
- Your calendar is full of recurring meetings you can't remember the purpose of.
- You're doing the same manual task repeatedly and suspect a machine could do part of it.
- Your head is full of "I should…" loops and you can't focus.
- You keep saying yes and drowning in commitments you resent.

**Not the right subfolder when:**

- The blocker is goal clarity, not time — see `../goals/`.
- Saying no is really about *one relationship's* dynamics, not your commitment pattern — see `../relationships/relationships_boundary_setting_script.md`.
- You can state the task but won't act — see `../agency/`.
- You're exhausted to the point of burnout — see `../solo-dev/solo_dev_burnout_prevention.md`; these prompts optimize scheduling, they don't treat depletion.
- You need a team/org-wide focus or meeting-norms initiative — see the deep-work cluster (below) and `domain-engineering-workflows/`.

## Prompts in this subfolder

| Prompt | One-line description |
|---|---|
| `productivity_personal_energy_audit.md` | Map a week of energy-tagged blocks to find your prime time, energy drains, and the single highest-leverage scheduling change. |
| `productivity_open_loop_audit.md` | Capture every open loop from your head, sort into buckets, and assign one physical next action each (GTD-style). |
| `productivity_automation_gold_mine.md` | Score a manual workflow by frequency × creativity × error-cost and rank the highest-ROI steps to automate first. |
| `productivity_zombie_meeting_detector.md` | **Bulk** calendar sweep: classify every recurring meeting by decision density → keep / make-async / delete. |
| `productivity_meeting_killer_prompt.md` | **Single-meeting** deep-dive: necessity verdict, true cost, optimize-or-replace path, plus ready-to-send Slack + email. |
| `productivity_overcommitment_saying_no.md` | Audit chronic overcommitment: tag *why* each recent yes was granted, price its true weekly cost, then build one decision rule + decline scripts and reverse the costliest yes. |
| `productivity_energy_by_task_type.md` | Sort task types into the energy window each needs, find the costliest mismatch (deep work stuck in a trough), and prescribe the single scheduling swap. Extends the energy audit. |
| `productivity_focus_ritual_design.md` | Design a short cue → transition → first-action ritual, tuned to what already works for you, so *starting* deep work stops taking willpower. |

## Sibling pair (read before picking a meeting prompt)

The two meeting prompts are distinct by **scope**, not duplicates:

- `productivity_zombie_meeting_detector.md` → use for **bulk triage across many recurring meetings** at once.
- `productivity_meeting_killer_prompt.md` → use for a **single-meeting deep-dive** with cost math and communication templates.

Each prompt's `## When to Use` section restates the boundary.

## Suggested composition / sequencing

- **Quarterly time reset:** `productivity_open_loop_audit.md` (clear the head) → `productivity_zombie_meeting_detector.md` (reclaim calendar) → `productivity_personal_energy_audit.md` (align work to energy) → `productivity_automation_gold_mine.md` (offload the repetitive).
- **One nagging meeting:** go straight to `productivity_meeting_killer_prompt.md`.
- **Decide what to automate:** run `productivity_open_loop_audit.md` first so you automate what actually recurs, then `productivity_automation_gold_mine.md`.
- **Stop the inflow:** if the calendar keeps refilling no matter how much you cut, run `productivity_overcommitment_saying_no.md` — cutting meetings without a saying-no rule just makes room for the next yes.
- **Fix deep-work timing, then onset:** `productivity_personal_energy_audit.md` (find the rhythm) → `productivity_energy_by_task_type.md` (put the right work in the right window) → `productivity_focus_ritual_design.md` (reliably *start* it once it's scheduled).
- **Hand off to execution:** the open-loop audit's top item feeds `../agency/agency_next_action_spec.md`; the focus ritual pairs with `../agency/agency_rapid_start_mode.md` for the first-action push.

## Shared design principles

- **Real data only.** These are *audit* prompts — they refuse to invent workflows, meetings, energy levels, or open loops the user didn't supply.
- **Estimates labeled as estimates.** Cost and ROI math is grounded in the user's numbers and never presented as precise.
- **Reversible trials over permanent cuts.** Meeting and schedule changes are framed as time-boxed experiments with a fallback.
- **One leverage move first.** The prompts surface the single highest-impact change rather than a total overhaul.
- **Human value protected.** Culture/relationship meetings and judgment-requiring tasks are flagged, not optimized away.

## Related domains in this repo

> **Boundary note — important:** this folder overlaps with [`domain-productivity/deep-work/`](../../../domain-productivity/deep-work/), which holds the deeper meeting/calendar/automation/focus toolkit (e.g. `deepwork_calendar_audit.md`, `deepwork_meeting_cost_estimator.md`, `deepwork_meeting_to_async_converter.md`, `deepwork_focus_parameters_estimator.md`). These personal-development prompts are the lightweight entry points; the deep-work cluster is the heavier system. **Link across, don't duplicate** — if a user needs depth, route them to `domain-productivity/deep-work/`.

- `../goals/` — set and decompose the goals this freed-up time should serve (upstream).
- `../agency/` — execution and ownership for the next actions surfaced here (downstream).
- `../solo-dev/` — solo-developer-specific automation audit, burnout prevention, context-switching reduction.
- `domain-productivity/bottlenecks/` and `domain-productivity/reviews/` — personal constraint diagnostics and review cadences.
