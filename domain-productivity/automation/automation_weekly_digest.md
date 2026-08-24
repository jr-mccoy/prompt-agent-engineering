---
title: "Weekly Digest Email — Scheduled Multi-Source Summary with Empty-State Handling"
category: productivity/automation
description: "Specify a scheduled automation that pulls filtered data from one or more sources, compiles it into a readable digest, and emails it on a fixed cadence — with correct date windows, an always-send empty state, and failure handling."
techniques:
  - ST-01
  - ST-03
  - CM-02
  - DS-06
  - QA-01
difficulty: intermediate
tags:
  - automation
  - digest
  - scheduling
  - reporting
  - email
updated: "2026-06-07"
related_prompts:
  - domain-productivity/automation/automation_daily_accountability.md
  - domain-productivity/automation/automation_content_monitoring.md
  - domain-productivity/automation/automation_data_sync.md
---

# Weekly Digest Email

**Objective:** Specify a scheduled automation that, on a fixed cadence, pulls filtered data from one or more sources for the correct date window, compiles it into a readable sectioned digest, and emails it to recipients — always sending (with an explicit empty state) and handling pull/send failures.

**When to use:**
- Recurring team status updates or weekly metrics reports.
- Content roundups or project-progress summaries on a rhythm.
- Any "people expect this every week" report you want to stop assembling by hand.

**When NOT to use:**
- One-off reports — build it manually instead of automating.
- Real-time alerting — use an event-triggered notification (see `automation_form_notification.md`).
- Reports requiring heavy analysis/judgment the automation can't encode — automate the data pull, write the narrative yourself.

**Audience:** Individuals and small teams building automations in Zapier, Make, n8n, or similar no-code/low-code platforms.

---

## Inputs / Context

Supply the following before generating the spec:

1. **Cadence** — day of week + send time + explicit timezone.
2. **Data source(s)** — for each: app, the fields to pull, and the filter (including the date window).
3. **Date window definition** — what "last 7 days" means relative to send time (and timezone).
4. **Sections** — the digest's section headings and which source feeds each.
5. **Recipients** — addresses or distribution list, and the subject line pattern.
6. **Empty-state policy** — confirm the digest still sends when there's no data.
7. **Available integrations** — confirm each source and the email sender are connected.

---

## Constraints

### Must
- Use only sources and an email sender that are connected on the chosen platform (or flag the gap).
- Schedule in the user's **explicit local timezone**, not UTC.
- Compute the date window relative to send time in that timezone (no off-by-one weeks).
- **Always send**, even with no data — show an explicit empty-state message to preserve the rhythm.
- Define what happens if a data pull fails (send with a partial/notice section vs. abort + alert).
- Format the email so it's readable in plain text and HTML clients.

### Must Not
- Assume the data sources or email integration are connected.
- Skip sending when a section is empty (breaks the expected cadence).
- Let a single failed source silently produce a blank or misleading digest.
- Use a date window that double-counts or misses items at week boundaries.

---

## Instructions

1. **Restate the digest.** One line: what is summarized, from where, for whom, how often.
2. **Define the schedule trigger.** Day + time + explicit timezone.
3. **Define each data pull.** Source, fields, filter, and the date window expressed relative to send time in the stated timezone.
4. **Define the compile step.** Map each source's results into its section; specify ordering and formatting (lists, metrics).
5. **Write the email.** Subject pattern with the week range; greeting; sections; sign-off; an "auto-generated" note.
6. **Define the empty state.** Per section and overall: explicit "nothing to report this week" text; still send.
7. **Define failure handling.** Source unreachable / query error → send digest with a "data unavailable for [section]" notice and alert maintainer; email-send failure → retry then alert.
8. **Self-check before output.** Confirm: integrations confirmed; timezone explicit; date window correct relative to send; empty state sends; each source failure has a path; subject reflects the week range. Then emit the spec.

---

## False-Positive Prevention

❌ **DON'T:**
- Assume the data sources and email sender are connected.
- Leave the schedule in UTC and assume it fires locally.
- Compute "last 7 days" without anchoring to send time + timezone (causes boundary errors).
- Suppress the email when there's no data (people notice the missing rhythm).
- Let one failed source produce a blank digest with no explanation.

✅ **DO:**
- Confirm each integration and flag any that need setup.
- Set an explicit local timezone and verify the fire time.
- Anchor the date window to send time in that timezone.
- Always send; show a clear empty-state line per section.
- Add a per-source failure notice plus a send-retry-then-alert path.

---

## Output Format

```
AUTOMATION: Weekly [DIGEST NAME]
INTEGRATIONS REQUIRED: [source app(s), email sender] — [confirmed / NEEDS SETUP]

TRIGGER — Schedule
- Day/time: [day] at [HH:MM] local
- Timezone: [explicit timezone]
- Date window: [definition relative to send time]

DATA PULLS
- Source 1: pull [fields] from [app] where [filter incl. date window] → Section [X]
- Source 2: ... → Section [Y]

COMPILE
- Section [X]: [format — list/metric block]
- Section [Y]: ...

ACTION — Send email via [sender]
- To: [recipients]
- Subject: "[DIGEST NAME] — Week of {start}–{end}"
- Body: greeting + sections + sign-off + auto-generated note

EMPTY STATE
- Per section: "[no items] to report this week."
- Always send (do not skip)

FAILURE HANDLING
- Source pull fails → section shows "data unavailable" + alert maintainer; still send
- Email send fails → retry once after [interval], then alert maintainer

TESTING CHECKLIST
- [ ] ...
```

---

## Example Output

```
AUTOMATION: Weekly Team Status Digest
INTEGRATIONS REQUIRED: Airtable "Projects" (CONFIRMED), Google Analytics (CONFIRMED), Gmail (CONFIRMED)

TRIGGER — Schedule
- Day/time: Friday at 16:00 local
- Timezone: America/Chicago
- Date window: items from the Monday 00:00 → Friday 16:00 of the current week (Central)

DATA PULLS
- Source 1: pull [Task, Owner, Status] from Airtable "Projects" where Status = "Done" AND Completed within this week → Section "Completed This Week"
- Source 2: pull [Sessions, Signups] from Google Analytics for this week vs. prior week → Section "Key Metrics"

COMPILE
- "Completed This Week": bullet list "✅ {Task} — {Owner}"
- "Key Metrics": "- Sessions: {n} ({Δ% vs last week}) / - Signups: {n} ({Δ%})"

ACTION — Send email via Gmail
- To: team@company.com
- Subject: "Team Status — Week of {Mon}–{Fri}"
- Body:
  "Hi team,
   Here's the status digest for the week of {start}–{end}.

   **Completed This Week**
   {completed list}

   **Key Metrics**
   {metrics block}

   Have a great weekend!
   — Ops
   (Auto-generated. Reply with questions.)"

EMPTY STATE
- "Completed This Week" empty → "No tasks marked Done this week."
- Metrics unavailable → "Metrics unavailable this week."
- Always send.

FAILURE HANDLING
- Airtable query fails → "Completed This Week: data unavailable" + DM maintainer; still send
- Gmail send fails → retry once after 10 min, then alert maintainer via Slack

TESTING CHECKLIST
- [ ] Run manually → data pulls return this-week items only (not last week's)
- [ ] Subject shows the correct Mon–Fri range
- [ ] Email renders cleanly in Gmail and Outlook
- [ ] Force zero completed tasks → empty-state line shows and email still sends
- [ ] Force an Airtable error → "data unavailable" notice + maintainer alerted, email still sends
- [ ] Confirm the 16:00 fire time is Central, not UTC
```

---

## Verification

- [ ] Every named integration is confirmed available or flagged as needing setup.
- [ ] Schedule uses an explicit local timezone.
- [ ] Date window is anchored to send time in that timezone (no boundary errors).
- [ ] Each source feeds a defined section with specified formatting.
- [ ] Empty state is explicit per section and the email always sends.
- [ ] Per-source pull failures and email-send failures have defined paths.
- [ ] Subject line reflects the correct week range.

---

## Techniques Used

- **ST-01 (Clear Objective Statement):** Fixes the digest's purpose, cadence, and audience so scope stays bounded.
- **ST-03 (Output Format Specification):** Locks the schedule→pulls→compile→send→empty-state→failure layout into a copy-ready spec.
- **CM-02 (Constraint Specification):** Encodes Must/Must-Not rules (explicit timezone, always-send, correct date window, no silent blanks) as constraints.
- **DS-06 (Prioritization and Severity Guidance):** Sectioning and metric emphasis order the digest so the most important items lead; failure notices flag degraded sections.
- **QA-01 (Self-Verification):** A pre-output check confirms timezone, date window, empty-state, and per-source failure paths before emitting.

---

## Related Prompts

- `domain-productivity/automation/automation_daily_accountability.md` — Daily scheduled message (vs. weekly summary) pattern.
- `domain-productivity/automation/automation_content_monitoring.md` — Capture items during the week to roll up into the digest.
- `domain-productivity/automation/automation_data_sync.md` — Keep the source data the digest reads from in sync.
