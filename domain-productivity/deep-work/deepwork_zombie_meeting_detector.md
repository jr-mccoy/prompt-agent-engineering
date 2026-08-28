---
title: "Zombie Meeting Detector"
category: productivity/deep-work
description: "Audit your calendar to find recurring meetings that have outlived their purpose — classifies each by decision density and recommends keep, make async, or delete"
techniques:
  - ST-01
  - ST-02
  - CM-01
  - DS-06
difficulty: beginner
tags:
  - personal-development
  - meetings
  - calendar-audit
  - productivity
  - time-management
updated: "2026-06-21"
related_prompts:
  - domain-productivity/deep-work/deepwork_meeting_killer.md
  - domain-productivity/deep-work/deepwork_personal_energy_audit.md
  - domain-productivity/automation/automation_gold_mine.md
---

# Zombie Meeting Detector

**Objective:** Analyze your recurring meetings to identify "zombies" — meetings that continue by inertia despite no longer serving their original purpose. Classifies each by decision density and recommends keep, make async, or delete, with estimated hours saved per month.

## When to Use

- Use when: you want to **sweep an entire calendar** of recurring meetings at once and triage each as keep / make-async / delete.
- Use when: your calendar feels full but unproductive, you're spending >40% of the week in meetings, or it's a quarterly calendar review.
- **Use this over its sibling `deepwork_meeting_killer.md` when** you're doing **bulk triage across many recurring meetings**. Use the meeting-killer instead for a **single-meeting deep-dive** with cost math and ready-to-send communication templates.
- Don't use when: you only have one meeting in question — go straight to `deepwork_meeting_killer.md`.

---

## Inputs / Context

**Calendar Data:** [Paste calendar export (CSV) or manually list your recurring meetings with: title, recurrence, duration, attendees, and a brief note on what typically happens]

Example:
```
Weekly Standup — Weekly, 30min, 8 people — status updates, rarely any decisions
Product Sync — Biweekly, 60min, 5 people — good discussions, actionable decisions
Team Social — Monthly, 30min, 12 people — casual, team building
```

**Refusal / insufficiency logic:** Do not classify meetings by title alone. If the user supplies only meeting names without recurrence, duration, attendees, or a note on what happens, ask for the "what typically happens" detail before assigning decision density — a title like "Sync" reveals nothing about whether it produces decisions. Never label a meeting a zombie on inference alone; ground each call in the user's note. Do not fabricate meetings or attendee counts.

---

## Instructions

### Phase 1: Meeting Classification

For each recurring meeting, assess:

| Meeting | Recurrence | Duration | Decision Density | Recommendation |
|---------|------------|----------|-----------------|----------------|
| [Title] | weekly/biweekly/monthly | [min] | high/med/low | keep / async / delete |

**Decision density criteria:**
- **High:** Produces decisions, unblocks work, requires real-time discussion
- **Medium:** Some useful discussion but could be shorter or less frequent
- **Low:** Status updates, FYIs, or discussions that rarely lead to action

### Phase 2: Zombie Identification

Flag meetings as zombies if they match 2+ of these patterns:
- No clear agenda or the agenda hasn't changed in months
- Attendees regularly multitask during the meeting
- The same information could be shared via Slack/email
- No decisions have been made in the last 4 instances
- People can miss it without consequences
- It exists "because we've always had it"

### Phase 3: Recommendations

For each meeting:
- **Keep:** High decision density, requires real-time collaboration. Suggest optimizations (shorter? fewer attendees? better agenda?).
- **Make async:** Medium density. Suggest specific async replacement (Slack thread, shared doc, Loom video).
- **Delete:** Low density zombie. Suggest how to handle any residual needs.

### Phase 4: Impact Summary

- **Total hours in meetings per month:** [Current]
- **Hours recoverable:** [After changes]
- **Estimated savings:** [Hours × average hourly rate]

---

### False-Positive Prevention

- ❌ Do NOT recommend deleting all meetings — some are genuinely valuable
- ❌ Do NOT ignore the social and cultural value of certain meetings
- ❌ Do NOT assume decision density can be perfectly measured from titles alone
- ❌ Do NOT recommend changes that would leave people feeling excluded or uninformed
- ✅ DO suggest "try async for 2 weeks" experiments rather than permanent deletion
- ✅ DO consider whether the meeting serves relationship-building even if low on decisions
- ✅ DO recommend keeping a communication channel open for meetings you suggest cutting
- ✅ DO calculate the opportunity cost of recovered time (what would you do instead?)

---

## Expected Output

```markdown
# Zombie Meeting Audit: [Date]

## Classification
| Meeting | Recurrence | Duration | Decision Density | Recommendation |
|---------|------------|----------|------------------|----------------|
| Weekly Standup | weekly | 30min | Low | Make async |
| Product Sync | biweekly | 60min | High | Keep (optimize) |
| Team Social | monthly | 30min | n/a (culture) | Keep |
| Status Review | weekly | 60min | Low | Delete |

## Zombies Flagged (2+ patterns matched)
- **Status Review** — no decision in last 4 instances; same info available in Slack;
  attendees multitask; exists "because we've always had it." → Delete.
- **Weekly Standup** — pure status updates, rarely a decision. → Make async.

## Recommendations
- **Weekly Standup → async:** Daily Slack standup bot; reserve live time only if blocked.
- **Product Sync → keep, optimize:** Cut to 45min, tighten agenda, drop 1 optional attendee.
- **Status Review → delete:** Replace with a Friday shared-doc update; keep a Slack channel open.
- **Team Social → keep:** Culture value outweighs decision density.

## Impact Summary
- Current meeting load: ~6.5 hrs/month
- Recoverable: ~3 hrs/month after changes
- Estimated savings: ~3 hrs × ~$60/hr ≈ $180/month (estimate)
- Reinvest recovered time in: [deep work block]

## Suggested Trial
Try the standup + status-review changes async for 2 weeks; reinstate if a decision stalls.
```

---

## Verification

Before delivering the audit, confirm each of these. If any fails, fix it before responding:

- [ ] Every meeting the user listed is classified with a **decision-density rating grounded in their note**, not inferred from the title.
- [ ] A meeting is flagged a **zombie only if it matches 2+ of the stated patterns** — no single-signal labels.
- [ ] Each recommendation is **keep / make-async / delete** with a concrete replacement or optimization for the residual need.
- [ ] **Culture/relationship-value meetings** are recognized and not scored purely on decisions.
- [ ] The impact summary's hours/savings derive from the user's **supplied recurrence and attendee data** and are labeled estimates.
- [ ] Cuts are framed as **time-boxed trials with a fallback channel**, not abrupt permanent deletions that leave people uninformed.
- [ ] Recovered time is tied to **what the user would do instead** (opportunity cost made concrete).

---

## Techniques Used

- **ST-01** (Clear Objective Statement) — Calendar audit with keep/async/delete verdicts
- **ST-02** (Structured Sequential Instructions) — Classify, identify zombies, recommend, summarize
- **CM-01** (Explicit Context Framing) — Real calendar data as input
- **DS-06** (Prioritization Guidance) — Ranked by recoverability and impact

---

## Related Prompts

- [deepwork_meeting_killer.md](deepwork_meeting_killer.md) — Sibling: deep-dive analysis of a *single* meeting (vs. this bulk calendar sweep).
- [deepwork_personal_energy_audit.md](deepwork_personal_energy_audit.md) — Understand how meetings affect your energy.
- [domain-productivity/automation/automation_gold_mine.md](../automation/automation_gold_mine.md) — Automate meeting-adjacent workflows.

> **Boundary note:** Calendar/meeting auditing overlaps with [`domain-productivity/deep-work/`](../deep-work/) (e.g. `deepwork_calendar_audit.md`, `deepwork_meeting_to_async_converter.md`). This prompt is the personal-development entry point; link across rather than duplicating that cluster.
