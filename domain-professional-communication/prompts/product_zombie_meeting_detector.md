---
title: "Zombie Meeting Detector — Audit Recurring Meetings for Keep / Shrink / Async / Kill"
category: professional-communication/product-management
description: "Audit a calendar of recurring meetings to flag low-decision-density 'zombie' meetings. Scores each on decision density, attendee cost, and recurrence, then returns keep / shrink / async / kill recommendations with reasoning."
techniques:
  - ST-01
  - ST-02
  - RT-02
  - DS-06
  - QA-04
difficulty: intermediate
tags:
  - meetings
  - calendar-audit
  - productivity
  - async-conversion
  - time-management
updated: "2026-06-07"
related_prompts:
  - domain-professional-communication/prompts/product_automation_gold_mine.md
  - domain-productivity/deep-work/deepwork_calendar_audit.md
  - domain-productivity/deep-work/deepwork_meeting_to_async_converter.md
---

# Zombie Meeting Detector

**Objective:** Audit a list of recurring meetings, score each on decision density, attendee cost, and recurrence, and return a clear per-meeting recommendation — KEEP, SHRINK, ASYNC, or KILL — so the calendar's low-value "zombie" meetings get surfaced and dealt with.

**When to Use:**
- Your (or your team's) calendar is full of recurring meetings and you want to cut the dead weight.
- You're a manager reclaiming team focus time and need a defensible case for which meetings to change.
- You want to convert status/update meetings to async but need to identify which ones qualify.
- You're doing a periodic calendar hygiene pass.

**When NOT to use:**
- You want to redesign a single specific meeting's agenda — that's a facilitation task, not an audit.
- You're auditing repetitive *workflow steps* for automation — use `product_automation_gold_mine.md`.
- You want a broad personal focus/calendar diagnostic beyond meetings — use `domain-productivity/deep-work/deepwork_calendar_audit.md`.

---

## Inputs / Context

1. **The meeting list** — paste a list or CSV of recurring meetings. Wrap it in `<calendar>...</calendar>`.
   - Ideal columns: meeting name, recurrence (daily/weekly/biweekly/monthly), duration, number of attendees, and (if known) attendee roles/seniority and the meeting's stated purpose.
   - If you only have names and times, the audit still works at lower confidence — gaps will be flagged.
2. **Whose calendar / which team** — so attendee-cost weighting reflects the right people.
3. **Purpose hints (optional)** — for each meeting, what it's *supposed* to accomplish (decide, inform, coordinate, build relationships).
4. **Constraints** — meetings that are contractually, culturally, or legally required to stay live (e.g., regulated review boards, 1:1s leadership wants kept).

---

## Constraints

### Must
- Score each meeting on three factors, 1–5 each:
  - **Decision density** — how many real decisions or unblocking outcomes happen per meeting (5 = decisions every time; 1 = pure status broadcast).
  - **Attendee cost** — total human time consumed (attendees × duration × recurrence), weighted by seniority when known. Higher cost = higher score on this factor (it raises the stakes of keeping it).
  - **Recurrence load** — how often it repeats and thus how much cumulative calendar it occupies.
- Produce exactly one recommendation per meeting: **KEEP**, **SHRINK**, **ASYNC**, or **KILL**.
- Justify each recommendation in one to two lines tied to the scores.
- Respect required-meeting constraints — never recommend KILL/ASYNC for a meeting the user flagged as mandated; recommend SHRINK or note it as locked.
- Distinguish "broadcast / status" meetings (strong async candidates) from "decision / negotiation" meetings (keep live).
- Summarize estimated time reclaimed if recommendations are adopted, labeling the estimate's assumptions.

### Must Not
- Recommend KILL for a meeting whose purpose is unknown — flag it for purpose-clarification instead.
- Treat all low-decision-density meetings as KILL; relationship/1:1/morale meetings have legitimate non-decision value — note this.
- Invent attendee counts, durations, or purposes not provided; mark inferences.
- Recommend ASYNC for meetings that require live negotiation, sensitive feedback, or real-time conflict resolution.
- Override user-flagged mandatory meetings.

---

## Instructions

1. **Parse the meeting list.** Normalize into a per-meeting record. Note which fields are missing — missing duration/attendee data lowers confidence for that meeting.

2. **Classify each meeting's primary purpose.** Decide, Inform/Status, Coordinate, or Relationship/Morale. Use stated purpose hints; if absent, infer from the name and mark it inferred. Purpose drives the default recommendation channel (Inform → ASYNC candidate; Decide/Negotiate → KEEP live).

3. **Score the three factors (RT-02), 1–5 each:**
   - **Decision density:** low = zombie risk. This is the headline signal.
   - **Attendee cost:** attendees × duration × recurrence, seniority-weighted if known.
   - **Recurrence load:** how much cumulative calendar it eats.

4. **Apply the constraint filter.** Flag user-mandated meetings as locked-to-KEEP (or SHRINK at most). Flag sensitive/negotiation meetings as live-required.

5. **Derive the recommendation (DS-06):**
   - **KEEP:** High decision density, right-sized, purpose requires live.
   - **SHRINK:** Valuable but over-attended or over-long — cut duration, attendees, or frequency.
   - **ASYNC:** Primarily informational/status with low decision density — convert to a written update, dashboard, or recorded brief.
   - **KILL:** Low decision density, no legitimate relationship/coordination value, and not mandated.
   - For unknown-purpose meetings, recommend **clarify-then-decide** rather than guessing KILL.

6. **Estimate reclaimed time.** Sum the calendar hours freed if SHRINK/ASYNC/KILL recommendations are adopted. Label every assumption (counts, durations).

7. **Attach confidence (QA-04).** High only where attendee/duration/purpose data was provided; Low where the recommendation leaned on inference from the meeting name alone.

---

## False-Positive Prevention

1. **Killing relationship meetings.** 1:1s, team morale, and onboarding meetings have low decision density by design but real value. Do not flag them KILL purely on the decision-density score — weigh purpose.
2. **Async-ing live-required meetings.** Sensitive feedback, negotiation, brainstorming, and conflict resolution lose their value async. Never recommend ASYNC for these even if decision density looks low on paper.
3. **Guessing purpose from the title.** A meeting named "Sync" might be a critical decision forum. If purpose is unknown, recommend clarification, not a verdict — and mark the inference.
4. **Fabricated attendance/cost.** Don't assert "12 people × 60 min" unless the data supports it. Estimate explicitly and lower confidence.
5. **Overriding mandates.** A regulated review board or a 1:1 leadership requires cannot be killed by an audit. Respect the constraint and pivot to SHRINK.
6. **Confusing busy with valuable.** A meeting that always fills its hour is not necessarily productive — fullness is not decision density. Judge by outcomes, not by whether time gets used.
7. **Inflated reclaimed-time claims.** Reclaimed-time totals are estimates built on assumed counts/durations. Present them as such, never as hard savings.

---

## Output Format

```
# Zombie Meeting Audit: [calendar owner / team]

## Per-meeting findings
| Meeting | Purpose | Decision density | Attendee cost | Recurrence load | Recommendation | Why |
|---------|---------|------------------|---------------|-----------------|----------------|-----|
| [name]  | [type]  | [1–5]            | [1–5]         | [1–5]           | KEEP/SHRINK/ASYNC/KILL | [1 line] |
| ...     | ...     | ...              | ...           | ...             | ...            | ... |

(Mark inferred purposes and estimated figures with *(inferred)*.)

## Locked / required meetings
[Any user-mandated meetings, noted as KEEP or SHRINK-only.]

## Needs purpose clarification
[Meetings where the verdict was withheld pending purpose info.]

## Estimated time reclaimed
[Total hours/week or /month if recommendations adopted — assumptions labeled.]

## Confidence
High | Medium | Low — [tied to how much real meeting data was provided]
```

---

## Verification

- [ ] Every meeting parsed; missing fields noted.
- [ ] Primary purpose classified per meeting (inferred ones marked).
- [ ] All three factors scored 1–5.
- [ ] Exactly one recommendation per meeting (or clarify-then-decide for unknowns).
- [ ] Relationship/1:1/morale meetings not killed on decision density alone.
- [ ] Live-required meetings not recommended for ASYNC.
- [ ] User-mandated meetings respected (not killed/async'd).
- [ ] Reclaimed-time estimate provided with assumptions labeled.
- [ ] Confidence stated and tied to data completeness.
- [ ] No fabricated attendee counts, durations, or purposes.
