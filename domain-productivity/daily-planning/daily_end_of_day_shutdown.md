---
title: "Daily End-of-Day Shutdown"
category: productivity/daily-planning
description: "A structured workday-close routine that captures open loops, produces tomorrow's starter task, and cleanly closes the mental workspace."
techniques:
  - ST-01
  - ST-02
  - CM-02
  - QA-01
  - OC-06
difficulty: beginner
tags:
  - daily-planning
  - shutdown-ritual
  - open-loops
  - transition
  - end-of-day
updated: "2026-05-12"
related_prompts:
  - domain-productivity/daily-planning/daily_morning_planning_sequence.md
  - domain-productivity/deep-work/deepwork_future_self_handoff.md
  - domain-productivity/deep-work/deepwork_block_end_context_capture.md
  - domain-personal-development/prompts/agency/agency_end_of_session_review.md
---

# Daily End-of-Day Shutdown

**Objective:** Run a structured end-of-workday routine that captures open loops, assesses what got done, logs any new commitments made during the day, and produces tomorrow's starter task. Closes the mental workspace so the evening is actually off.

**When to use:** At the end of each workday — the last 10 minutes before you stop working. Works best when used at a consistent time. Also useful after a chaotic or interrupted day when you need to take stock before transitioning. Pairs directly with the Daily Morning Planning Sequence.

**Audience:** Anyone who ends the day unsure what they finished, anxious about what's still open, or unable to mentally leave work. Not a weekly review (that's separate). Not for mid-day breaks — this is specifically a day-close. Not needed on days with no future commitments (e.g., last day before a long vacation — just write a handoff instead).

---

## Inputs Required

1. **What got done today.** A quick list of what you completed — even partially. "Finished the proposal, got through half my inbox, had a hard call with the client" is enough. Don't filter for impressive items — include small completions.

2. **What's still open.** Anything you started but didn't finish, promised but haven't done, or know is waiting for you. Be specific: "The contract draft is 80% done, just needs the payment terms section" beats "still working on contract."

3. **New commitments made today.** Any promises, agreements, or new tasks that emerged from conversations, messages, or meetings today that weren't on your original list. Easy to forget; expensive if forgotten.

4. **Tomorrow's calendar (if known).** Any fixed commitments for tomorrow — meetings, appointments, deadlines. Used to set up the starter task in a realistic slot.

---

## Instructions

### Step 1 — Tally the Day

From the "what got done" input, produce a brief honest accounting:
- What was on the MIT list, and did the MIT get done?
- What else got completed?
- What was started but not finished?

Do not evaluate the day as good or bad — just establish what happened. If the MIT didn't get done, note it without judgment and carry it forward as tomorrow's first candidate.

### Step 2 — Capture Open Loops

From the "still open" input, write a clean capture list. For each open loop:
- Name it specifically (not "the report" — "the executive summary section of the Q2 report")
- Note its current state ("80% done — needs payment terms")
- Flag any time sensitivity ("client expects it by Wednesday")

Open loops that aren't captured will surface as 2am anxiety. Write them down now.

### Step 3 — Log New Commitments

From the "new commitments made today" input, create a commitments log. For each:
- What did you commit to?
- Who did you commit to?
- When do they expect it?

If the commitment has a hard deadline, add it to the open loop list with that deadline attached. Do not let "I'll get to it" commitments vanish into the void.

### Step 4 — Name Tomorrow's Starter Task

From the open loops and commitments, identify the single best task to start with tomorrow morning. Criteria:
- High importance or time-sensitive
- Has a clear first action (not a fuzzy task requiring 20 minutes of setup before real work begins)
- Is yours to do (not blocked on someone else)

State the starter task as: "Tomorrow starts with: [task name]. First action: [specific physical step]."

This is not a full tomorrow plan — that is the morning's job. The starter task ensures the morning begins with momentum rather than with planning paralysis.

### Step 5 — Write the Close Statement

Write one sentence that marks the end of the workday. This is not a performance assessment. It is a psychological close — a signal to the brain that work is done for today.

Examples of functional close statements:
- "The work for today is captured. Tomorrow is set up. Done."
- "Everything that needed attention today has a home. Closing."

Examples of non-functional close statements (too evaluative, too vague):
- "Good day overall, need to do better tomorrow."
- "I guess that's it for now."

---

## Constraints

### Must
- Capture every open loop and new commitment — the value of shutdown is completeness, not speed
- Name tomorrow's starter task with a specific first action
- Write a close statement that marks a clean end
- State whether the MIT was completed (yes, no, or partially — with current state)

### Must Not
- Turn the shutdown into a self-critique session — the purpose is capture and close, not evaluation
- Carry forward tasks that have become irrelevant — each open loop must be re-examined, not automatically forwarded
- Leave open loops as categories ("finish work stuff") rather than specific named items
- Make the close statement conditional ("done, assuming nothing comes up tonight")
- Omit new commitments made during the day — these are the most common source of dropped balls

---

## False-Positive Prevention

1. **The incomplete-close trap:** Shutdown that ends with "I'll figure out tomorrow in the morning" is not shutdown — it is a delay. The starter task must be named before the session ends, or the morning will begin with decision overhead instead of execution.

2. **The selective capture trap:** People naturally remember what they finished and forget what they started. The "still open" section requires active retrieval — prompt for messages you haven't replied to, files left open, conversations that ended without resolution.

3. **The commitment-omission trap:** New commitments made in passing during the day ("sure, I'll send that to you") are the most commonly forgotten items. These must be explicitly elicited and logged.

4. **The evaluation creep trap:** Shutdown is not a performance review. Statements like "I should have done more" or "wasted too much time" are not part of this protocol. If they appear, redirect to the factual capture.

5. **The open-loop vagueness trap:** "Still working on the project" is not a captured open loop. It is an anxious placeholder. Require specific task names, current states, and next actions for each open item.

---

## Output Format

```
## End-of-Day Shutdown — [Date]

### Today's Accounting

**MIT ([Task name]):** [Done / Partially done — current state / Not started — reason]

**Other completions:**
- [Task completed]
- [Task completed]
- ...

---

### Open Loops (captured)

| Item | Current State | Time-Sensitive? |
|------|---------------|-----------------|
| [Specific task name] | [80% done / waiting on X / not started] | [By [date] / No] |
| ... | | |

---

### New Commitments Made Today

| Commitment | For whom | Expected by |
|------------|----------|-------------|
| [What you agreed to do] | [Name] | [Date/time] |
| ... | | |

---

### Tomorrow Starts With

**Task:** [Specific task name]
**First action:** [Exact physical step to begin — open this file, call this person, write this thing]
**Approximate time:** [~X minutes / blocks]

---

### Close

[One sentence. Work is done. Tomorrow is set up.]
```

---

## Verification

- [ ] MIT completion status is stated (done / partial with current state / not started)
- [ ] All open loops are named specifically — not as categories
- [ ] New commitments made during the day are captured
- [ ] Each open loop has a current state and a time-sensitivity flag
- [ ] Tomorrow's starter task is named with a specific first action
- [ ] A close statement is written and marks a definite end
- [ ] No open loop is listed as a vague category ("the project," "email stuff")
