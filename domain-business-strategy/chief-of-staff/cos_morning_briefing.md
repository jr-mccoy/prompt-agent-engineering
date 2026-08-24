---
title: "Generate a Morning Briefing from Calendar, Commitments, and Waiting-Fors"
category: business-strategy/chief-of-staff
description: "Produce a one-screen morning briefing that tells the user what the day actually demands — today's meetings with prep status, open commitments coming due, waiting-fors to nudge, and the single most important thing to ship before end of day."
techniques:
  - ST-01
  - ST-02
  - CM-02
  - DS-01
  - ST-03
difficulty: beginner
tags:
  - chief-of-staff
  - morning-briefing
  - calendar
  - commitments
  - daily-routine
updated: "2026-04-20"
related_prompts:
  - domain-business-strategy/chief-of-staff/cos_brain_dump_to_tasks.md
  - domain-business-strategy/chief-of-staff/cos_end_of_day_reconciliation.md
  - domain-productivity/deep-work/deepwork_match_tasks_to_calendar.md
---

# Generate a Morning Briefing from Calendar, Commitments, and Waiting-Fors

**Objective:** Produce a one-screen morning briefing, same structure every day, that makes today's demands legible in under 90 seconds of reading: meetings (with prep status), commitments due today, waiting-fors to act on, one most-important ship item, and a single flag for what could derail the day.

**When to use:** First 10 minutes of the workday, after coffee, before email. Replaces "let me just check Slack." Run daily on a workday cadence.

**Audience:** Individual knowledge worker or executive. The user both runs the briefing and executes the day. Same shape every day — consistency is the point.

---

## Inputs Required

1. **Today's calendar.** Meeting titles, times, other attendees, whether a prep doc exists or not.
2. **Open commitments the user is tracking.** From their list, doc, or tool of choice, whatever it is.
3. **Waiting-fors.** Items the user is expecting back from others, with when they were expected.
4. **The single most important thing to ship before end of day**, if the user knows it. If not, flag it — the briefing is going to force naming it.
5. **Known constraints for the day.** Energy (late night, sick, traveling), hard external deadlines.

If inputs 1–3 aren't supplied, refuse to produce a briefing. The user must provide actual data; this exercise does not invent today's meetings.

---

## Instructions

### Step 1 — Classify today's time

Add up meeting time and split the day into three buckets:
- **Meeting time** (hours on calendar with others).
- **Focus time** (blocks of ≥45 min with nothing scheduled).
- **Fragmented time** (gaps <45 min between meetings).

Report the split as three numbers. If focus time is <90 minutes, flag it explicitly — the day is structurally not a ship day.

### Step 2 — Meeting-by-meeting prep check

For each meeting, in time order:
- **What it is** (title + who called it).
- **What the user is there for** (decide / present / listen / support).
- **Prep status**: ready / light prep needed (<15m) / heavy prep needed / cancel-or-decline candidate.
- **One-line prep task** if prep is needed.

If the user is "there to listen" on a meeting they called, flag that as likely wasted time.

### Step 3 — Commitments coming due

List commitments due today or within 48 hours:
- What it is, who it's to, when it's due.
- Whether the user can still deliver on time given the day's calendar.
- If not: propose a specific move — renegotiate now, deliver a partial, pull a meeting.

### Step 4 — Waiting-fors to act on

List items the user is waiting on from others:
- Whom, what, when last nudged, when expected back.
- If overdue by the user's own rule (default 48 hours unless noted): recommend one action — nudge, escalate, proceed without.

Keep this short. Waiting-fors that aren't actionable today don't appear on the briefing.

### Step 5 — Name the one ship item

Exactly one item the user will ship today. Criteria:
- It fits in today's available focus time.
- If it doesn't ship today, tomorrow is worse.
- It is a shippable unit, not a category ("work on the proposal" is not valid; "send the proposal to Alice" is).

If the user didn't name one in inputs, force a candidate from the commitments list. If there is no reasonable candidate, say so — "today is a coordination day; no ship item."

### Step 6 — Flag one derailer

One specific thing that could derail the day. Examples: the 3pm meeting is likely to run long; energy is low and the afternoon will fall off; a pending decision from [person] could land and reshuffle everything. One, not three. The point is to see it coming.

---

## Constraints

### Must
- Produce exactly one ship item (or explicitly state "no ship item today" with reason).
- Flag exactly one derailer.
- Keep the briefing to one screen.
- Preserve the same structure every day.
- Use the user's actual calendar and commitments; don't generalize.

### Must Not
- Rewrite the user's day. Scheduling is a separate activity.
- Pad the briefing with motivational language.
- Recommend more than one nudge per waiting-for.
- Upgrade "listen to" meetings into prep items.
- Invent commitments or meetings not provided.

---

## False-Positive Prevention

1. **Don't produce a clean briefing for a broken day.** If focus time is <90 min and there's an ambitious ship item, the briefing must flag the structural problem, not smooth it over.
2. **Don't manufacture a ship item.** If nothing ships today, say so — calling a coordination day a "ship day" sets up a dishonest end-of-day reconciliation.
3. **Don't let prep status drift to "ready" by default.** If no prep doc exists for a meeting the user called, prep is needed.
4. **Don't add research/reading to the briefing.** Those are not morning-briefing items; they are focus-block items.
5. **Keep the derailer real.** "You might get distracted" is not a derailer; "the 3pm will almost certainly run 30 min over" is.

---

## Output Format

```
# Morning briefing — [date]

## Day shape
- Meetings: [X h]  Focus: [Y h]  Fragmented: [Z h]
- [Flag if focus < 90 min]

## Meetings
| Time  | Meeting           | I'm there to | Prep status       | Prep task (if needed) |
|-------|-------------------|--------------|-------------------|-----------------------|
| 10:00 | Ops review        | Decide       | Light prep        | Review dashboard      |

## Commitments due today / <48h
- [What, to whom, by when] — deliverable risk: [green/yellow/red + move if red]

## Waiting-fors to act on
- [Whom / what / action today: nudge/escalate/proceed without]

## One ship item
- [Specific shippable] — fits in [which focus block]
  (or: No ship item today. Reason: [coordination day / low energy / etc.])

## One derailer to watch
- [Specific thing + what to do if it lands]
```

---

## Verification

- [ ] Day shape is three numbers and a structural flag if warranted.
- [ ] Every meeting has prep status and, if needed, a concrete prep task.
- [ ] Commitments include a delivery-risk signal.
- [ ] Exactly one ship item or an honest "no ship item."
- [ ] Exactly one derailer is named.
- [ ] Briefing fits on one screen.
