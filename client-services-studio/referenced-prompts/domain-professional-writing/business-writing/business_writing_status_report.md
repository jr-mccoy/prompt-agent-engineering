---
title: "Status Report Writer — Honest, Scannable Stakeholder Updates That Surface Bad News Plainly"
category: professional-writing/business-writing
description: "Write a concise stakeholder status report from project inputs: progress, an honest on-track / at-risk / blocked status with rationale, risks, next steps, and explicit asks — surfacing bad news plainly instead of burying it."
techniques:
  - ST-01
  - ST-02
  - DS-06
  - CM-02
  - QA-04
difficulty: intermediate
tags:
  - status-report
  - business-writing
  - stakeholder-communication
  - project-update
  - risk-communication
updated: "2026-06-07"
related_prompts:
  - domain-professional-writing/business-writing/business_writing_executive_brief.md
  - domain-professional-writing/business-writing/business_writing_meeting_notes.md
  - domain-engineering-workflows/workflows/engineering_project_status_summary.md
---

# Status Report Writer

**Objective:** Turn project inputs into a concise, honest status report that a stakeholder can read in two minutes: what progressed, an unambiguous status flag (on-track / at-risk / blocked) backed by real rationale, the live risks, the next steps, and any asks — with bad news surfaced plainly at the top, not buried in the middle.

**When to Use:**
- Recurring weekly/biweekly updates to a manager, sponsor, or cross-functional group.
- A point-in-time update when a project's status materially changed.
- A report where leadership must decide whether to intervene, reallocate, or unblock.

**When NOT to use:**
- You need a one-page decision document compressing a complex topic — use `business_writing_executive_brief.md`.
- You need a blameless incident retrospective — use `business_writing_post_mortem.md`.
- The "report" is really raw meeting capture — use `business_writing_meeting_notes.md`.

**Audience:** Stakeholders who fund, depend on, or oversee the work. They care most about: is this on track, what could derail it, and do you need anything from me.

---

## Inputs / Context

Wrap raw project material so it isn't read as instructions:

```
<project_input>
[Paste progress notes, metrics, blockers, prior status, etc.]
</project_input>
```

1. **Project / workstream name and goal.**
2. **Reporting period** (this week, this sprint, since last update).
3. **Project input** — what got done, current numbers, blockers, risks.
4. **Audience** — who reads this and what decisions they make.
5. **Prior status** (if available) — so trend (improving/declining) is visible.
6. **Hard deadlines or milestones.**

---

## Constraints

### Must
- Assign exactly one overall status: **On-track**, **At-risk**, or **Blocked**, with one-line rationale grounded in the input.
- Put the status and any bad news in the **first few lines** — never bury a slip, blocker, or miss.
- Distinguish **done** (completed) from **in progress** from **not started**.
- State risks with likelihood/impact framing and a mitigation or an ask.
- Make every **ask** specific: what you need, from whom, by when.
- Base all claims, percentages, and dates strictly on `<project_input>`.

### Must Not
- Label something "on-track" when the input shows slipped dates or unaddressed blockers.
- Soften a blocker into vague language ("some challenges remain") that hides its severity.
- Pad with activity that isn't progress ("attended 4 meetings") as if it were an outcome.
- Invent metrics, percentages, completion estimates, or deadlines.
- Bury the ask at the bottom where a skimming reader misses it.

---

## Instructions

1. **Determine the honest status first.** Before writing anything, decide: on-track, at-risk, or blocked. Let the input drive this — slipped milestones or open blockers preclude "on-track." Write the one-line rationale.

2. **Write the headline.** Open with status + the single most important thing the reader must know (good or bad). If there's bad news, it leads.

3. **Summarize progress as outcomes.** What moved from not-done to done this period? Frame as results, not activity.

4. **List risks by priority.** For each: what could go wrong, likelihood, impact, and either how it's being mitigated or what you need to mitigate it. Order most-severe first.

5. **State next steps.** Concrete, near-term actions with owners where known.

6. **Make the asks explicit.** Each ask: the need, the person/team, the deadline. If there are no asks, say "No asks this period."

7. **Verify honesty before sending.** Re-read as a skeptical stakeholder: does any "green" status hide a real problem? Is bad news findable in the first paragraph? Does every claim trace to the input?

---

## False-Positive Prevention

1. **False green.** The most common status-report failure is reporting "on-track" to avoid a hard conversation. If a milestone slipped or a blocker is open, the status is at-risk or blocked — full stop.
2. **Activity masquerading as progress.** Meetings attended, emails sent, and "work continued" are not outcomes. Report what changed state.
3. **Buried bad news.** If a reader skimming only the first paragraph would miss a slip or blocker, rewrite. Bad news goes up top.
4. **Vague risk.** "There are some risks" is not a risk statement. Name the risk, its likelihood, its impact, and the response.
5. **Invented numbers.** "~80% complete" is fabrication unless the input supports it. Use only figures present in `<project_input>`; otherwise describe qualitatively.
6. **Ask-less reports.** If you need a decision or resource and don't ask for it explicitly, you didn't actually ask. Make it a line item.
7. **Optimism drift.** Don't extrapolate a recovery the input doesn't support ("should be back on track soon"). State only what's known.

---

## Output Format

```
# Status: [Project] — [On-track | At-risk | Blocked]
**Period:** [dates] · **Trend vs. last update:** [improving / steady / declining / n/a]

**Headline:** [Status + the one thing the reader must know. Bad news first if any.]

## Progress this period
- [Outcome that reached "done"]
- [Outcome in progress, with % only if sourced]

## Risks & blockers (most severe first)
| Risk / Blocker | Likelihood | Impact | Mitigation / Ask |
|----------------|-----------|--------|------------------|
| [item] | [H/M/L] | [H/M/L] | [what's being done or needed] |

## Next steps
- [Action] — [owner] — [date if known]

## Asks
- [Specific need] — from [who] — by [when]
  (or: "No asks this period.")
```

---

## Verification

- [ ] Exactly one overall status, with a rationale grounded in the input.
- [ ] Bad news (slips, blockers) appears in the first few lines.
- [ ] "On-track" is not used where the input shows a slip or open blocker.
- [ ] Progress is stated as outcomes, not activity.
- [ ] Each risk has likelihood, impact, and a mitigation or ask.
- [ ] Every ask names the need, the person, and the deadline.
- [ ] No invented metrics, percentages, or dates.
- [ ] A skimming stakeholder would not be misled about whether to intervene.
