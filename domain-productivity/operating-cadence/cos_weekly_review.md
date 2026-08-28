---
title: "Weekly Review: Clean State and Next-Week Setup"
category: productivity/operating-cadence
description: "A 30–60 minute weekly review that produces a clean state — zero stale commitments, a current waiting-for list, surfaced decisions deferred — and sets up next week with one named focus, a short list of non-negotiables, and decisions the user will make Monday morning."
techniques:
  - ST-01
  - ST-02
  - CM-02
  - RT-02
  - QA-01
  - QA-04
difficulty: intermediate
tags:
  - chief-of-staff
  - weekly-review
  - planning
  - reflection
  - personal-org
updated: "2026-04-20"
related_prompts:
  - domain-personal-development/prompts/agency/agency_weekly_review.md
  - domain-productivity/operating-cadence/cos_end_of_day_reconciliation.md
  - domain-productivity/operating-cadence/cos_morning_briefing.md
---

# Weekly Review: Clean State and Next-Week Setup

**Objective:** A repeatable 30–60 minute weekly review that does two distinct things. (1) Close the week: every commitment, waiting-for, and deferred decision from the past week is resolved, parked with an owner, or explicitly carried forward. (2) Open the next: one named focus for the week, a short list of non-negotiables on the calendar, and any decisions the user will make Monday morning.

**When to use:** End of week or Sunday evening, same day and time each week. Distinct from `agency_weekly_review.md` (which harvests a pattern from the week's execution data); this review is about state hygiene and next-week setup.

**Audience:** Individual knowledge worker or executive running their own week. The review produces an artifact the user reads Monday morning; if it would not be useful Monday morning, it was done wrong.

---

## Inputs Required

1. **End-of-day reconciliations from the week** if the user runs them. If not, calendar + commitments list + inbox.
2. **The original intent for the week** (what Monday's focus was). If no record, flag it.
3. **Current commitments list.** What the user has promised others.
4. **Current waiting-fors.** What the user is expecting from others.
5. **Deferred decisions.** Items parked "to decide later" from meetings or conversations.
6. **Known constraints for next week.** Vacation, travel, pre-scheduled meetings.

If the user has no records and cannot recall the week in any structured way, produce a reduced review: skip Step 2 and Step 3, flag the missing data, and recommend one system change before next week (e.g., start running the end-of-day reconciliation).

---

## Instructions

### Part A — Close the week

#### A1. Commitments audit
For every commitment on the list:
- **Delivered** — mark done, remove.
- **Still open, on track** — carry forward with date.
- **Still open, at risk** — name the risk and one move to derisk.
- **Slipped** — decide: renegotiate (with whom, what proposed), deliver late (when), drop (notify whom).
- **Stale** — on the list >21 days with no movement. Propose removal or revival.

No commitment leaves the audit without a disposition.

#### A2. Waiting-fors audit
For every waiting-for:
- **Landed** — remove, note any follow-on action.
- **Still expected, within window** — keep.
- **Overdue** — decide: nudge today / escalate / proceed without.
- **Stale** — chase once more or drop.

#### A3. Deferred decisions audit
For every "to decide later":
- Is the user now ready to decide? If yes, state the decision or schedule a 30-minute block to make it.
- If no, name what information is still missing and when it will be available.
- If the decision has been deferred 3+ times, flag it — recurring deferral is itself a decision.

### Part B — Open the next week

#### B1. Name the focus
One sentence: "If next week moves only one thing, it should be [X]." Specific enough that an observer could tell whether it moved.

Do not write "be more strategic" or "ship the product." Write "send the final proposal to Alice and Bob" or "complete the data migration for the US region."

#### B2. Non-negotiables on calendar
Up to five items that must happen next week regardless of whatever else comes up. Each one anchored to a specific day/block:
- Focus blocks for the named focus (at least 2).
- Hard external deadlines.
- Standing meetings that are actually non-negotiable (most aren't — be honest).
- One non-work non-negotiable if it matters (family, health, etc.).

If the calendar can't fit this list, the list is too long or the calendar is too full. Pick one to cut.

#### B3. Monday-morning decisions
List any decisions the user will make first thing Monday. Not "maybe later in the week" — Monday morning. This front-loads decisions before the week's momentum takes over.

#### B4. Stop-doing candidate
One thing from this week the user will stop doing next week. Specific. Examples: "stop joining the 9am ops sync as listener," "stop reviewing every Slack thread in [channel]," "stop checking email between 9 and 11."

One. Not a list.

#### B5. Uncertainty note
One line: what about next week is genuinely uncertain that might change the plan. Examples: "waiting to hear if [customer] signs — if yes, this plan shifts." Not a worry — a scouted unknown.

---

## Constraints

### Must
- Every commitment, waiting-for, and deferred decision gets a disposition — nothing left unlabeled.
- Name exactly one focus for next week.
- Non-negotiables capped at 5.
- Produce exactly one stop-doing candidate.
- Acknowledge uncertainty where the data doesn't support a plan.

### Must Not
- Grade the past week (no "productive week," "bad week").
- Produce a 40-item todo list for next week. The review sets scaffolding; execution details come Monday.
- Invent commitments or deferred decisions the user didn't supply.
- Recommend a new productivity system.
- Let deferred decisions hide inside the focus — if the focus depends on a decision that hasn't been made, surface that.

---

## False-Positive Prevention

1. **Don't confuse a clean-looking commitments list with a real one.** If a commitment was on the list three weeks ago and is still there with no movement, "on track" is probably wrong. Mark it stale.
2. **Don't let the focus be a category.** "Sales pipeline" is a category; "close the [X] deal" is a focus. Check the observer test.
3. **Don't pad non-negotiables.** If something on the list is actually negotiable, removing it is more valuable than defending it.
4. **Don't collapse Monday-morning decisions into the focus.** Decisions and execution are different work.
5. **If the past week has no records,** don't reconstruct it from memory and treat that as audit data. Flag the gap and change the system.

---

## Output Format

```
# Weekly review — [week of date]

## Closing the week

### Commitments
| Who to    | What                    | Disposition                         |
|-----------|-------------------------|-------------------------------------|
| [Name]    | [Thing]                 | Delivered / On track (date) / At risk (move) / Slipped (action) / Stale (remove/revive) |

### Waiting-fors
| Whom from | What                    | Disposition                         |
|-----------|-------------------------|-------------------------------------|
| [Name]    | [Thing]                 | Landed / Expected / Overdue (action) / Stale (chase/drop) |

### Deferred decisions
- [Decision] — ready now: Y/N. If N: missing [X], available by [when]. Deferred [N] times.

## Opening next week

### The one focus
[One sentence, observer-testable.]

### Non-negotiables (≤5)
- [Day/block] — [Item]

### Monday-morning decisions
- [Decision to make first thing]

### Stop-doing candidate (one)
- [Specific thing]

### Uncertainty
[One line: scouted unknown that could change the plan.]
```

---

## Verification

- [ ] Every commitment, waiting-for, and deferred decision has a disposition.
- [ ] The named focus passes the observer test.
- [ ] Non-negotiables are ≤5 and anchored to specific days.
- [ ] Exactly one stop-doing candidate.
- [ ] Monday-morning decisions are named separately, not blended into execution.
- [ ] No grading of the past week.
- [ ] Output is useful to read Monday morning.
