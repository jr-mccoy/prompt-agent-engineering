---
title: "Translate a Brain Dump into a Clean Task List"
category: productivity/operating-cadence
description: "Turn a stream-of-consciousness brain dump into a structured task list with owners, time estimates, and a surfaced priority — while separating real tasks from feelings, nagging worries, and decisions in disguise."
techniques:
  - ST-01
  - ST-02
  - CM-02
  - DS-01
  - QA-01
difficulty: beginner
tags:
  - chief-of-staff
  - task-management
  - brain-dump
  - triage
  - personal-org
updated: "2026-04-20"
related_prompts:
  - domain-productivity/operating-cadence/cos_clarify_fuzzy_goals.md
  - domain-productivity/deep-work/deepwork_decompose_complex_task.md
  - domain-personal-development/prompts/agency/agency_next_action_spec.md
---

# Translate a Brain Dump into a Clean Task List

**Objective:** Convert an unsorted brain dump (raw text, bullet notes, voice-memo transcript) into a structured task list that separates (1) real tasks with owners, (2) decisions disguised as tasks, (3) worries disguised as tasks, and (4) waiting-fors that depend on someone else. Produce one clear "do next" item.

**When to use:** Start of a work block when the user has accumulated mental load and cannot tell what is actually on their plate. End of a heavy week. After a long meeting that generated many follow-ups. When the user says "I have a million things in my head."

**Audience:** Individual knowledge worker or executive managing their own workload. The user is both the brain dumper and the person who will execute.

---

## Inputs Required

1. **The raw brain dump.** Paste as given. Do not ask the user to pre-clean it.
2. **Today's date and how much focused time the user has in the next 48 hours.**
3. **Any hard deadlines already on calendar** the user wants this pass to respect.
4. **The user's current top-level priority, if they know it.** If not, flag it.

If the brain dump is empty or one line, refuse to process. The exercise needs real raw input to be useful.

---

## Instructions

### Step 1 — Parse each item into one of four buckets

Read every line. Assign one and only one label per item:

- **Task.** An action the user can take themselves that has a recognizable "done."
- **Decision.** A choice the user must make; no action is available until the choice is made.
- **Worry.** A feeling, fear, or open loop without a clear action. ("What if we lose the deal.")
- **Waiting-for.** The ball is in someone else's court; the user's action is to track or nudge.

If a line contains two things, split it. Do not collapse.

### Step 2 — Normalize each task

For every item tagged **Task**, produce:
- A verb-first one-liner. ("Send proposal to Alice" not "proposal.")
- An estimate bucket: **<15m**, **30m**, **1–2h**, **half-day**, **multi-session**.
- A "done when" test. Observable. ("Alice replies" or "draft in Drafts folder.")
- Owner: always the user unless the raw item explicitly names someone else.

If a task is **multi-session**, flag it — it does not belong in this list and should be routed to a project breakdown (see `deepwork_decompose_complex_task.md`).

### Step 3 — Surface decisions

For every item tagged **Decision**, produce:
- The choice, phrased as "[A] or [B]" or "whether to [X]."
- Who else needs to be involved, if anyone.
- The soonest the user can make this decision with current information, or what information is missing.

Do not recommend a choice. That is a separate exercise.

### Step 4 — Quarantine worries

For every item tagged **Worry**, write it back to the user in one line. Do not convert to a task unless the user can specify an action. A worry without an action is allowed to exist — it just does not belong on the task list.

Offer one re-entry question per worry: "What would you need to see in the next week to stop worrying about this?" That question is the user's to answer later.

### Step 5 — Log waiting-fors

For every item tagged **Waiting-for**, produce:
- Who the ball is with.
- When you expect it back.
- What the user will do if it's not back by then (nudge, escalate, proceed without).

### Step 6 — Pick the single "do next"

From the Task list, pick exactly one item the user should do in their next available block. Criteria, in order:
1. Fits inside the user's available time.
2. Unblocks the most downstream work.
3. Breaks the most expensive streak of avoidance.

Name which criterion drove the pick. If two tasks tie, say so and let the user choose.

---

## Constraints

### Must
- Use exactly the four buckets: Task, Decision, Worry, Waiting-for.
- Attach an estimate and a "done when" to every Task.
- Quarantine worries — do not convert them into tasks by inference.
- Produce exactly one "do next" item.
- Preserve the user's original line next to each parsed item (for audit).

### Must Not
- Merge, reword, or invent tasks. One line in → one or more labeled items out.
- Prioritize beyond the single "do next."
- Recommend how to resolve decisions.
- Silently upgrade worries to tasks with invented actions.
- Add tasks the user did not mention (no "and also you should…").

---

## False-Positive Prevention

1. **Don't convert worries to tasks.** "Budget is tight" becomes a worry, not "redo the budget." The task only exists if the user actually proposed the action.
2. **Don't inflate estimates to look thorough.** If a task is <15m, say so. Overestimating makes the list useless.
3. **Don't over-split.** If a line is "Email Alice re: proposal, then call Bob if she says yes," keep them as one conditional task ("Email Alice re: proposal; branch on her reply") unless the user clearly wants two.
4. **Don't hide the dud.** If the brain dump is mostly worry and decision with very few real tasks, say so clearly. That is the most valuable finding.
5. **Don't recommend a task management system.** Output is a list for this dump, not a tool migration.

---

## Output Format

```
# Brain dump parse — [date]

## Tasks ([count])
| Task (verb-first)                  | Est      | Done when                  | Original line |
|------------------------------------|----------|----------------------------|---------------|
| [One-liner]                        | 30m      | [Observable]               | "[raw]"       |

[Note any multi-session items to route to project breakdown.]

## Decisions ([count])
- [Whether to X / A or B] — involves: [people]. Ready when: [info needed or "now"].

## Worries ([count])
- [One-line quoted] — re-entry: "What would you need to see to stop worrying about this?"

## Waiting-fors ([count])
| With        | Expected by | If not back: |
|-------------|-------------|--------------|

## Do next
- [Single task from above]
- Chose because: [fits available time / unblocks most / breaks avoidance streak]
```

---

## Verification

- [ ] Every raw line appears exactly once across the four buckets.
- [ ] Every Task has verb, estimate, and "done when."
- [ ] No worry was silently converted to a task.
- [ ] Exactly one "do next" is named, with the reason.
- [ ] Multi-session items are flagged for project breakdown, not left in the list.
- [ ] Output fits on one to two screens.
