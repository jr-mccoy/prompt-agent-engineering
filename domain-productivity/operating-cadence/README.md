# Chief-of-Staff / Personal Org

Prompts for running your own operating cadence the way a chief of staff would run it for an executive — but self-directed. These are the repeatable artifacts (morning briefings, weekly reviews, authority maps, meeting protocols) that keep a knowledge worker's week legible and keep sub-agents useful.

**Audience:** Individual knowledge worker or executive managing their own agenda, delegating to AI sub-agents and/or human assistants. Not built for team-wide rollout — these are personal systems.

**When to use these prompts together:**
- **Daily cadence:** `cos_morning_briefing.md` → work → `cos_end_of_day_reconciliation.md`.
- **Around meetings:** `cos_meeting_prep_and_process.md` for both halves of every meeting ≥30 min.
- **Weekly:** `cos_weekly_review.md` to close the week and set up the next one.
- **Onboarding an AI or human sub-agent:** `cos_memory_scaffold_claude_md.md` + `cos_authority_boundaries.md` + `cos_specify_subagent_task.md`.
- **When goals or priorities feel stale:** `cos_clarify_fuzzy_goals.md` before writing next-week's plan.
- **When the head is noisy:** `cos_brain_dump_to_tasks.md`.

---

## Prompts

| Prompt | One-liner |
|--------|-----------|
| [cos_clarify_fuzzy_goals.md](cos_clarify_fuzzy_goals.md) | Turn a fuzzy goal into one crisp intent sentence and a first real move within 48 hours. |
| [cos_brain_dump_to_tasks.md](cos_brain_dump_to_tasks.md) | Parse a stream-of-consciousness dump into tasks, decisions, worries, and waiting-fors. |
| [cos_specify_subagent_task.md](cos_specify_subagent_task.md) | Write a delegation brief with intent, scope, verification, and stop conditions. |
| [cos_morning_briefing.md](cos_morning_briefing.md) | Produce a one-screen briefing of today's meetings, commitments, ship item, and derailers. |
| [cos_meeting_prep_and_process.md](cos_meeting_prep_and_process.md) | Two-part protocol: pre-meeting intent brief and post-meeting notes processor. |
| [cos_end_of_day_reconciliation.md](cos_end_of_day_reconciliation.md) | A 5–10 minute end-of-day close with reload context and one signal for the weekly review. |
| [cos_weekly_review.md](cos_weekly_review.md) | Close the week (audit commitments, waiting-fors, decisions) and open the next with one focus. |
| [cos_memory_scaffold_claude_md.md](cos_memory_scaffold_claude_md.md) | Draft a CLAUDE.md / persistent-memory file so AI agents stop re-asking the same context. |
| [cos_authority_boundaries.md](cos_authority_boundaries.md) | Produce a Can-do / Ask-first / Never authority map for a specific sub-agent. |

---

## Relationship to adjacent clusters

- **[agency/](../../domain-personal-development/prompts/agency/)** focuses on self-directed execution and ownership. The weekly review there harvests a *pattern* from the week's execution data; the weekly review here closes state and sets up next week. Run both if you run both.
- **[deep-work/](../../domain-productivity/deep-work/)** focuses on focus-block hygiene and calendar engineering. Most chief-of-staff protocols assume you have focus blocks; deep-work prompts help you get them.
- **[delegation/](../../domain-prompt-engineering/delegation/)** focuses on the mechanics of delegating a single task to AI. `cos_specify_subagent_task.md` is the user-facing front door to those; when you need more depth on intent or verification, go there.
