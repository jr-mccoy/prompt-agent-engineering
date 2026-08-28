---
title: "Weekly Review That Compounds Effort into a System"
category: personal-development/agency
description: "A 20–40 minute weekly review that turns individual sessions into a durable system: what shipped, what didn't and why, what the next week's single most important move is, and one repeatable pattern harvested from the week's data."
techniques:
  - ST-01
  - ST-02
  - RT-02
  - QA-01
  - QA-04
difficulty: intermediate
tags:
  - agency
  - weekly-review
  - reflection
  - pattern-detection
  - system-building
updated: "2026-04-20"
related_prompts:
  - domain-personal-development/prompts/agency/agency_ai_session_weekly_reflection.md
  - domain-engineering-workflows/ai-patterns/ai_pattern_rule_extraction_from_decisions.md
  - domain-productivity/bottlenecks/bottleneck_observation_capture_habits.md
  - domain-personal-development/prompts/agency/agency_end_of_session_review.md
---

# Weekly Review That Compounds Effort into a System

**Objective:** A weekly review that does three things every time, without drifting into daydreaming or backlog-grooming: (1) settle the books on what shipped, (2) diagnose why non-shipments didn't ship, (3) extract one reusable pattern from the week's data so the next week is slightly smarter. 20–40 minutes, same shape every week.

**When to use:** End of week, same day each week. Or at the end of a bounded sprint. Also usable at the end of a month to compound weekly reviews into a month-view, by replaying the four weekly reviews back-to-back.

**Audience:** The user doing self-directed work. Designed to be run on one's own, though the output is structured enough to share with an accountability partner.

---

## Inputs Required

1. **The week being reviewed.** Date range.
2. **End-of-session reviews from the week**, if the user runs them (see `agency_end_of_session_review.md`). If not, the user's best recall of the week.
3. **What the user said at the start of the week** was going to be the week's focus — the one thing that mattered most. If they don't remember, flag it as a finding itself.
4. **Artifacts shipped this week.** Files, commits, posts, messages to real recipients, conversations closed.
5. **Calendar check:** number of days worked, and roughly what share of time was focused project work vs reactive / meetings / admin.

If the user didn't work on their project at all this week, skip to a shorter review: acknowledge what happened in their life, set one minimum move for the coming week, and stop. Do not fake a review.

---

## Instructions

### Step 1 — Settle the books

List what shipped this week. Concrete artifacts with pointers. If "nothing shipped," write that plainly. This section has no interpretation.

List what was planned but didn't ship. Two columns: what was planned, where it got stuck.

### Step 2 — Diagnose non-shipments

For each non-shipment, assign one of the following causes. Use only these:

- **Scope was wrong** (too big, too vague, underestimated).
- **External dependency** (waiting on another person, a tool, a decision).
- **Avoidance** (the work was available, the user chose something else — see `agency_planning_masquerade_detector.md`).
- **Energy** (illness, life, legitimate exhaustion).
- **Priorities shifted** (something else genuinely mattered more; flag whether that was right).
- **Execution was partial** (significant work done, didn't reach ship state).

Assign exactly one cause per non-shipment. If two feel equally true, pick the earliest in the causal chain.

Aggregated: is there a dominant cause this week?

### Step 3 — Compare intent vs result

Quote or paraphrase the start-of-week focus. Compare to what actually happened. Note:

- Did the top focus advance, stall, or get displaced?
- If displaced, what displaced it?
- Is the displacement a signal about the priority or a signal about execution?

This is the central question of the review. Do not skip it.

### Step 4 — Extract one reusable pattern

From the week's data, pull exactly one pattern worth carrying forward. Formats that work:

- **Time signature.** "Tasks like X actually take ~N hours; I've been budgeting ~M."
- **Context precondition.** "Sessions after Y go better than sessions after Z."
- **Decision rule.** "When X happens mid-session, the right move is to [specific action]."
- **Anti-rule.** "Trying to X on Y days doesn't work; stop scheduling it."

One pattern. Not three. A single pattern the user actually uses is worth more than a long list that doesn't get applied.

### Step 5 — Define next week's single most important move

Not a full plan. One sentence answering: "If next week moves only one thing, what should it be?"

This is written before the next-week's task list is built — because the task list, once built, will include many things and obscure the priority.

### Step 6 — Flag dangerous drift

One short paragraph or bullets answering: is anything this week suggesting I've drifted off the actual project? Signs:

- Same non-shipments repeating weeks in a row.
- The top focus keeps being displaced by the same thing.
- Shipped artifacts are further from the project's named direction each week.
- Hours worked went up and output didn't.

If the answer is "no drift," say so. If yes, be specific about which signal.

### Step 7 — Uncertainty note

One line: what this review cannot tell you from the data on hand. (E.g., "can't tell if the essay is stalled because of scope or avoidance; next week's first session will tell.")

---

## Constraints

### Must
- Use the fixed cause taxonomy in Step 2.
- Extract exactly one pattern.
- Produce exactly one "most important move" for next week.
- Address whether the week drifted.
- Acknowledge uncertainty where the data doesn't support a conclusion.

### Must Not
- Grade the week. No "B+ week." No "great week." No "bad week."
- Turn into a task list for next week — one move is enough at this level.
- Pad with invented insights when the data is thin.
- Recommend a new productivity system.
- Recount the week narratively. Structured sections, not prose.

---

## False-Positive Prevention

1. **Don't moralize about non-shipments.** The cause taxonomy is diagnostic, not judgmental. "Avoidance" is a category, not a character claim.
2. **Don't fabricate patterns.** If the week genuinely has no clear pattern, say so; next week's data will clarify. Forced patterns are worse than no patterns.
3. **Don't confuse busy weeks with productive weeks.** High hours + no shipments is a signal, not an excuse.
4. **Don't collapse legitimate priority shifts into avoidance.** Sometimes the right work really did displace the planned work. The test: would a reasonable outside observer agree?
5. **Don't turn review into planning.** The next-week move is one sentence; building the full plan for next week is a separate activity.

---

## Output Format

```
# Weekly review — [date range]

## Shipped this week
- [Artifact + pointer]
- [Artifact + pointer]
  (or: Nothing shipped)

## Planned-but-not-shipped
| Planned | Got stuck because (cause) |
|---------|---------------------------|
| [Item]  | [One cause from taxonomy] |

Dominant cause this week: [category, or "no dominant cause"].

## Intent vs result
Start-of-week focus: [what was said]
What happened to it: [advanced / stalled / displaced by Y]
Signal: [priority-signal or execution-signal]

## Pattern (one)
[Single sentence in time-signature / precondition / decision-rule / anti-rule form.]

## Next week's one most important move
[One sentence.]

## Drift check
[No drift / specific drift signal and what to watch.]

## Uncertainty
[What the data doesn't yet tell you.]
```

---

## Verification

- [ ] Causes come only from the fixed taxonomy.
- [ ] Exactly one pattern extracted.
- [ ] Exactly one "most important move" for next week.
- [ ] No grading language.
- [ ] Drift question was answered one way or the other.
- [ ] Uncertainty acknowledged where present.
- [ ] Output fits on one to two screens.
