---
title: "Meeting Notes Writer — Turn Raw Input into Scannable Decisions, Actions, and Open Questions"
category: professional-writing/business-writing
description: "Convert raw meeting input (notes, transcript, bullets) into clean, scannable meeting notes: TL;DR, decisions, action items with owner and due date, and open questions — without inventing anything not in the input."
techniques:
  - ST-01
  - ST-02
  - CM-02
  - QA-04
  - RT-05
difficulty: beginner
tags:
  - meeting-notes
  - business-writing
  - documentation
  - action-items
  - summarization
updated: "2026-06-07"
related_prompts:
  - domain-professional-writing/business-writing/business_writing_status_report.md
  - domain-professional-writing/business-writing/business_writing_executive_brief.md
  - domain-productivity/automation/automation_daily_accountability.md
---

# Meeting Notes Writer

**Objective:** Transform a block of raw meeting input — handwritten notes, a transcript, or scattered bullets — into clean, scannable meeting notes that a busy reader (including someone who wasn't there) can absorb in under a minute: a TL;DR, the decisions made, action items with owner and due date, and open questions still unresolved.

**When to Use:**
- You captured rough notes or a transcript and need a shareable, professional write-up.
- A teammate who missed the meeting needs to catch up quickly.
- You want a durable record that pins down who agreed to do what by when.

**When NOT to use:**
- You need a real-time live-note system or template before a meeting — this is a post-meeting writing tool.
- The input is empty or so sparse that there is nothing concrete to summarize (ask for more first).
- You want a status report rolled up across many meetings — use `business_writing_status_report.md`.

**Audience:** Attendees, absent stakeholders, and anyone who needs the record later. Write for the reader who skims, not the reader who studies.

---

## Inputs / Context

Provide whatever you have. Wrap the raw material in a named tag so it is never mistaken for instructions:

```
<meeting_input>
[Paste raw notes, transcript, or bullets here]
</meeting_input>
```

1. **Meeting input** (required) — the raw material above.
2. **Meeting title / purpose** (if known).
3. **Date and attendees** (only if stated or supplied — do not guess).
4. **Audience for the notes** — attendees only, or wider distribution?
5. **Known due-date conventions** — e.g., "EOW means end of this week."

---

## Constraints

### Must
- Draw every decision, action, owner, and date **only** from `<meeting_input>` or explicitly supplied context.
- Mark any item lacking an owner as **Owner: unassigned** and any lacking a date as **Due: not specified**.
- Lead with a 1–3 sentence TL;DR that captures the meeting's net outcome.
- Separate **decisions** (settled) from **open questions** (unresolved) — never blur the two.
- Keep each line scannable: one decision or one action per bullet.
- Preserve the original meaning of statements; tighten wording, do not reinterpret.

### Must Not
- Invent attendees, decisions, owners, due dates, or numbers not present in the input.
- Promote a discussion point to a "decision" if the input shows it was only debated.
- Assign an owner because they "probably" own it — leave it unassigned.
- Add commentary, recommendations, or editorializing the meeting didn't produce.
- Smooth over disagreement into false consensus.

---

## Instructions

1. **Read the full input first.** Identify the meeting's overall arc before extracting anything. Note the apparent purpose.

2. **Extract decisions.** A decision is something the group settled on. For each, quote or tightly paraphrase the decision and, if present, the rationale. If something was discussed but not resolved, it is NOT a decision — route it to open questions.

3. **Extract action items.** For each commitment to do something, capture:
   - The action (start with a verb).
   - The **owner** — only if a specific person was named or clearly volunteered. Otherwise: `unassigned`.
   - The **due date** — only if stated. Otherwise: `not specified`.

4. **Extract open questions.** Anything raised but unresolved, deferred, or needing follow-up.

5. **Write the TL;DR last.** In 1–3 sentences, state what the meeting accomplished and the single most important next step.

6. **Verify against the input before finalizing.** Re-scan and confirm every decision, owner, and date traces to a specific point in `<meeting_input>`. Strike anything you cannot trace.

7. **Flag gaps.** If critical info is missing (no owners for major actions, no dates, ambiguous decisions), list these under "Clarifications needed" rather than filling them in.

---

## False-Positive Prevention

1. **Discussion ≠ decision.** "We talked about migrating to the new vendor" is an open question, not a decision, unless the input shows the group committed.
2. **Named ≠ owner.** Someone being mentioned in a discussion does not make them the action owner. Require an explicit assignment or volunteer.
3. **Implied dates are not dates.** "Soon," "next sprint," or "ASAP" map to `Due: not specified` with the raw phrase quoted — do not convert to a calendar date.
4. **No phantom attendees.** If the input never names who was present, the attendee field stays `not specified`. Do not infer from who spoke unless speakers are labeled.
5. **No invented metrics.** Numbers, percentages, and dollar figures appear only if they are in the input, verbatim.
6. **Don't resolve open questions.** If the meeting left something unsettled, the notes leave it unsettled. Your job is to record, not to decide.
7. **Don't manufacture consensus.** If two people disagreed and nothing was settled, the notes say so.

---

## Output Format

```
# Meeting Notes — [Title / Purpose]
**Date:** [date or "not specified"] · **Attendees:** [names or "not specified"]

## TL;DR
[1–3 sentences: net outcome + most important next step]

## Decisions
- [Decision] — [rationale, if stated]
- [Decision]

## Action Items
| # | Action | Owner | Due |
|---|--------|-------|-----|
| 1 | [verb-first action] | [name / unassigned] | [date / not specified] |
| 2 | ... | ... | ... |

## Open Questions
- [Unresolved item]
- [Deferred item]

## Clarifications Needed (gaps in the source)
- [What's missing and who could fill it]
```

---

## Verification

- [ ] Every decision traces to a specific point in `<meeting_input>`.
- [ ] No attendee, owner, date, or number was invented.
- [ ] Decisions and open questions are cleanly separated.
- [ ] Each action item starts with a verb and has owner + due fields (even if "unassigned"/"not specified").
- [ ] TL;DR captures the net outcome in 1–3 sentences.
- [ ] Discussion points were not silently upgraded to decisions.
- [ ] Disagreements are preserved, not smoothed into consensus.
- [ ] Gaps are listed under "Clarifications needed," not filled with guesses.
