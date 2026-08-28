---
title: "Status Update Writer"
category: productivity/workplace
description: "Write a clear, audience-calibrated project status update for stakeholders."
techniques:
  - ST-01
  - ST-02
  - DS-01
  - CM-02
  - QA-01
  - RT-06
difficulty: beginner
tags:
  - status-update
  - communication
  - stakeholders
  - reporting
  - workplace
updated: "2026-05-12"
related_prompts:
  - domain-productivity/workplace/work_follow_up_email_drafter.md
  - domain-productivity/reviews/reviews_weekly_systems_review.md
  - domain-product-management/prompts/product_delivery_sprint_planner.md
  - domain-productivity/workplace/work_meeting_agenda_builder.md
---

# Status Update Writer

**Objective:** Write a project status update that is calibrated to the audience's needs — right level of detail, right format, no information that the reader can't act on or doesn't need.

**When to use:** Weekly status reports, pre-meeting briefings, stakeholder emails, Slack updates, project management tool status fields, or any time you need to communicate where a project stands to people who are not doing the work.

**Audience:** Anyone writing a project update — individual contributors, project managers, team leads, or executives updating a board. Not for internal team working-session notes or personal task tracking.

---

## Inputs Required

1. **Project name and one-line description.** What is this project? One sentence for the reader who doesn't know the background.
2. **Audience.** Choose one: executive/leadership, immediate team, external client, or all-hands. Each gets a different format and depth.
3. **Update format.** Email, Slack message, project management tool field (e.g., Jira, Asana, Linear), or verbal briefing notes.
4. **What happened since the last update.** List completed work, milestones hit, or decisions made. Be specific — "completed the API design" not "made progress."
5. **What is in progress.** Current work with a rough % complete or milestone indicator.
6. **Risks or blockers.** What could delay the project, or what is already delaying it? Include severity and your proposed mitigation.
7. **Decisions or inputs needed from this audience.** What do you need from the reader? If nothing, say so explicitly.
8. **Next milestone.** The single most important thing that must happen next, with a target date.

---

## Instructions

### Step 1 — Set the status signal
Choose one of three signals based on honest assessment:
- **Green:** On track. No significant risks to timeline, scope, or quality.
- **Yellow:** At risk. A known issue could affect delivery if not addressed. Escalation or decision may be needed.
- **Red:** Off track. The current trajectory will miss a committed deadline, scope, or budget. Immediate action or re-planning required.

Do not default to Green to avoid difficult conversations. Yellow is not failure — it is useful information. Red that is surfaced early is recoverable; Red that is hidden until the last minute causes crises.

### Step 2 — Calibrate to the audience
Apply these rules strictly:

**Executive/Leadership:**
- 3–5 bullets maximum
- Status signal, one sentence on what's complete, one sentence on what's at risk, one sentence on what decision or input is needed
- No implementation details, no task-level status, no technical jargon
- Time to read: under 60 seconds

**Immediate Team:**
- Full detail on what's in progress, blockers, and who owns what
- Include task-level status where relevant
- Surface handoff dependencies explicitly
- Time to read: 2–4 minutes

**External Client:**
- Frame everything in business impact, not internal process
- Do not mention internal team names, tool names, or internal processes
- Be direct about risks — clients prefer early bad news to late surprises
- Include what you need from them (decisions, content, approvals) with clear due dates
- Time to read: 2–3 minutes

**All-Hands:**
- Brief and high-energy; focus on progress and momentum
- One concrete win, one clear next goal
- Avoid anything that sounds like a problem without a solution

### Step 3 — Write the update
Use the output format for the relevant audience. Fill in each section from your inputs. Do not pad. Do not editorialize.

### Step 4 — Check for buried reds
Before finalizing: if there is a risk or blocker in the inputs, make sure it is visible in the update — not softened into the middle of a paragraph. A risk that can't be seen can't be acted on.

---

## Constraints

### Must
- Open with the status signal (Green / Yellow / Red or equivalent) before any narrative.
- State what decisions or inputs are needed from the audience, or explicitly say "no decisions needed."
- Name the next milestone with a target date.
- Match the length and depth to the audience type.

### Must Not
- Write more than 5 bullets for an executive audience.
- Include technical implementation details in a client or executive update.
- Use "we're making progress" or similar vague phrases without a specific milestone or metric.
- Hide a Yellow or Red risk inside a Green summary narrative.
- Open with "I hope you're doing well" or similar filler.

---

## False-Positive Prevention

1. **The optimism trap:** Writing Green when the project is Yellow because nothing has gone wrong yet, while ignoring a known upcoming risk. Status should reflect both current state and forward-looking risk.
2. **The detail dump:** Giving an executive audience every task-level update the team sees. Executives need the signal, not the log.
3. **The vague risk:** Listing "timeline risk" without stating what might slip, by how much, and what would prevent it. A risk without a mitigation is just worry.
4. **No decision, no action:** Writing a status update that surfaces a problem but doesn't tell the reader what it needs from them. Every Yellow or Red must include a specific ask.
5. **The milestone-free update:** Describing current activity without naming what success looks like next. "Working on the integration" is not a milestone. "Integration complete by May 19" is.

---

## Output Format

**Executive/Leadership:**
```
PROJECT: [Name] | STATUS: [GREEN / YELLOW / RED]
As of: [date]

Complete: [Most recent milestone or deliverable — one sentence]
In Progress: [Current work and target date — one sentence]
Risk: [What's at risk, why, and proposed mitigation — one sentence; omit if Green]
Need from you: [Specific decision or input needed, with date; or "No decision needed"]
Next milestone: [Name] by [date]
```

**Immediate Team:**
```
PROJECT: [Name] | STATUS: [GREEN / YELLOW / RED]
As of: [date]

COMPLETE (since last update)
- [Item] — [owner]
- [Item] — [owner]

IN PROGRESS
- [Item] — [owner] — [% or milestone indicator] — target: [date]
- [Item] — [owner] — [% or milestone indicator] — target: [date]

RISKS / BLOCKERS
- [Risk or blocker] — severity: [low/medium/high] — mitigation: [action]

DECISIONS NEEDED
- [Decision] from [person] by [date]
- [or: No decisions needed this cycle]

NEXT MILESTONE
[Milestone name] — [date]
```

**External Client:**
```
Subject: [Project name] — Status Update, [date]

[Project name] is [on track / at risk / off track] as of [date].

Since our last update:
- [Business-impact statement of what was completed]
- [Business-impact statement of what was completed]

Currently in progress:
- [What's being worked on in business terms] — expected by [date]

[If risk exists:]
One item to flag: [plain-language risk description]. We are [mitigation action]. If [condition], we will [escalation action].

What we need from you:
- [Specific deliverable or decision] by [date]
- [or: Nothing needed from your side this week]

Next milestone: [Name] — [date]

[Your name]
```

---

## Verification

- [ ] Status signal (Green/Yellow/Red) appears at the top
- [ ] Length and depth match the stated audience
- [ ] At least one specific milestone or deliverable is named with a date
- [ ] Risks are visible, not buried — each has a mitigation
- [ ] Decisions needed are explicit (or explicitly stated as "none")
- [ ] No vague progress language ("making progress," "moving forward")
- [ ] No internal jargon in client or executive versions
