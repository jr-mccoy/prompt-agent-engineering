---
title: "Incident Status Update — One-to-Many Outage Communication from a Single Fact Sheet, on a Clock You Keep"
category: sales-customer/support
description: "Draft the customer-facing updates for a live incident affecting many customers — investigating, identified, monitoring, resolved — from one fact sheet tagged confirmed or suspected, with impact in customer terms, what is not affected, a workaround only if confirmed, what is not known, and a next-update time on a cadence set by severity; plus the channel map (status page, in-app banner, email, support macro, internal account-team talking points) and a per-update consistency check — distinct from the one-customer escalation reply (support_escalation_response_drafter) and from the engineering postmortem."
techniques:
  - AG-19
  - NE-14
  - CM-02
  - QA-01
difficulty: intermediate
tags:
  - support
  - incident-communication
  - status-page
  - outage
  - customer-communication
  - customer-support
updated: "2026-09-24"
related_prompts:
  - domain-sales-customer/support/support_escalation_response_drafter.md
  - domain-sales-customer/support/support_ticket_triage_and_routing.md
  - domain-engineering-workflows/workflows/engineering_postmortem_blueprint.md
---

# Incident Status Update

**Objective:** Keep every affected customer accurately informed during an
incident — the same facts in every channel, nothing said that later has to be
retracted, and every "next update" time kept.

**When to Use:**
- Triage has declared an incident (a cluster, a regional outage, a degraded core
  feature) and customers need to hear from you before they ask.
- Updates so far have been "we're investigating" with no time and no scope.
- The status page, in-app banner, support macro and account managers are each
  saying something slightly different.
- **Not this prompt if** one customer has escalated and needs a personal reply and
  an internal handoff — `support_escalation_response_drafter.md` (reuse this
  prompt's fact sheet for it). Incident detection and severity come from
  `support_ticket_triage_and_routing.md`. The engineering postmortem is
  `domain-engineering-workflows/workflows/engineering_postmortem_blueprint.md`;
  a public post-incident summary is promised here only if someone owns writing it.
  The broad incident-response command in
  `domain-agentic-resources/commands/troubleshooting/incident_response.md` covers
  the whole response; this prompt covers only the customer updates.

## Inputs / Context

1. **Incident record:** ID, severity, start time, affected product areas, regions,
   account count or segment, current status.
2. **Engineering facts,** each tagged `[confirmed]` or `[suspected]`, and whether
   the incident commander has approved it for customers.
3. **What is not affected** (as confirmed facts — often the most reassuring line).
4. **Workarounds** tested by support or engineering.
5. **Channels you use** and who posts to each.
6. **Cadence policy** by severity, if you have one. Default: SEV-1 every 30 min until
   identified, then 60 min; SEV-2 every 60 min; 60–120 min once in monitoring.
7. **Commitments allowed:** can a post-incident summary be promised, by whom, when?

## Method

1. **Build the fact sheet first (CM-02).** Three bins: confirmed and approved to
   share; known but not approved; unknown. Every update draws only from the first
   bin. The fact sheet is versioned with each update.

2. **Set the clock (AG-19).** First update within 15 minutes of declaring the
   incident, even if it only says what is affected and when you will update next.
   Every update ends with a next-update time, and that time is kept even when
   there is nothing new — "no change; next update at…" is an update.

3. **Write each update in customer terms.** Order: what is affected (feature,
   region, who) → since when → what is **not** affected → workaround (confirmed
   only) → what we don't know yet → next update time. No internal service names,
   no percentages that are not confirmed, no cause until confirmed and approved,
   no fix ETA unless engineering commits to one.

4. **Use the stage labels honestly.**
   - **Investigating** — impact known, cause not.
   - **Identified** — cause confirmed and a fix or rollback under way.
   - **Monitoring** — fix applied, customer impact appears to have stopped.
   - **Resolved** — impact ended and stable for the monitoring window; state the
     impact window, what customers must do (if anything), and whether any data was affected.

5. **Fit each channel (NE-14).** Status page: every update, full text. In-app
   banner: one line, affected users only. Email: first and last update only, to
   admins of affected accounts. Support macro: links to the status page and tags
   inbound tickets to the incident. Account-team talking points: internal, same
   facts, plus which key accounts are affected.

6. **Check consistency on every update (QA-01).** Every statement is in the
   confirmed bin; the posted time is at or before the promised time; channels
   updated together; nothing said earlier is contradicted without saying so.

## Output Format

```
## Fact sheet v[n] — [incident] — [time]
Confirmed & approved | Known, not approved | Unknown

## Update [n] — [stage] — [time]
[status page text]
Banner: [one line]   Email: [yes/no]   Macro: [updated?]

## Channel map
| Channel | Audience | Which updates | Owner |

## Account-team talking points (internal)

## Consistency check
| Update | Posted vs promised | Unconfirmed claims | Channels in sync |
```

## Verification

- [ ] First update within 15 minutes of declaration, with scope and next-update time.
- [ ] Every update ends with a next-update time, and every promised time was kept.
- [ ] No `[suspected]` or unapproved fact appears in any customer-facing text.
- [ ] "Identified" appears only after the cause is confirmed and approved.
- [ ] The resolved update states the impact window, customer action needed, and data status.
- [ ] Banner, email, macro and talking points match the status-page facts.

## False-Positive Prevention

1. **"Some users may be experiencing issues" is not an update.** Say which feature,
   which region, since when.
2. **A missed update time is a second incident.** Customers watching a stale status
   page assume the worst; post "no change" on time.
3. **A suspected cause becomes the story.** Say the cause only when it is
   confirmed and approved; a retracted cause costs more trust than silence.
4. **A fix ETA from hope is a promise you will break.** Commit to update times,
   which you control.
5. **"Resolved" is not "fixed in production five minutes ago".** Use Monitoring
   until impact has stayed gone for the monitoring window.
6. **What is not affected matters.** "No data has been lost" — once confirmed — is
   often the sentence that stops the tickets.
7. **Emailing every update is noise.** Email the first and last; the status page
   carries the rest.
8. **Do not promise a public summary nobody owns.** Promise it only with an owner
   and a date.

## Example Output

```
## Fact sheet v5 (final) — Incident C-7 — SEV-1 — 11:50 UTC, 2026-09-22
Confirmed & approved: dashboards for EU-hosted accounts failed to load 08:40–10:42
UTC; 214 accounts [telemetry]; 09:00 scheduled reports delayed, all sent by 11:26; vehicle and fuel
data collection unaffected, no data lost (09:30); US and APAC unaffected; mobile app
unaffected; cause — a database change in our EU region this morning, rolled back
10:38 (IC approved 10:02).
Known, not approved: specific migration step that failed.
Unknown: none customer-relevant.

## Update 1 — Investigating — 09:05 UTC
Since 08:40 UTC, dashboards for customers on our EU region are failing to load or
timing out, and scheduled reports due at 09:00 UTC have not been sent. The mobile
app and customers in the US and Asia-Pacific are not affected. We don't yet know
the cause or whether data collection is affected. Next update: 09:35 UTC.
Banner: "Dashboards are unavailable in the EU region — updates on our status page."
Email: yes (admins of 214 accounts)   Macro: updated, tag C-7

## Update 2 — Investigating — 09:35 UTC
Dashboards in the EU region are still unavailable. Vehicle and fuel data is being
collected normally and no data has been lost. We haven't identified the cause yet.
Next update: 10:05 UTC.

## Update 3 — Identified — 10:05 UTC
We've found the cause: a change we made this morning to our EU reporting database.
We're rolling it back now. Dashboards will stay unavailable until the rollback
finishes. Next update: 11:05 UTC, or sooner if it's done.

## Update 4 — Monitoring — 10:50 UTC
Dashboards have been loading normally for all EU customers since 10:42 UTC. The
reports due at 09:00 are being sent now and should all arrive by 11:30 UTC. We're
watching closely. Next update: 11:50 UTC.

## Update 5 — Resolved — 11:50 UTC
Resolved. Between 08:40 and 10:42 UTC, dashboards were unavailable for customers
on our EU region, and reports due at 09:00 UTC were sent late (all by 11:26 UTC).
No vehicle or fuel data was lost, and you don't need to do anything. If a
scheduled report is still missing, use **Resend** on the report or reply to this
email. We'll publish a summary of what happened and what we're changing by Friday
25 September.
Email: yes (same 214 admins)   Banner: removed   Macro: switched to "resolved" text

## Channel map
| Status page | All customers | 1–5 | Support Lead (Sam Ortiz) |
| In-app banner | EU users | 1–4 | Support Lead |
| Email | Admins, 214 EU accounts | 1, 5 | Support Lead |
| Support macro | Inbound tickets | every update | Tier 1 lead |
| Talking points | Account managers, CSMs | every update | Support Lead → CS channel |

## Account-team talking points (internal)
Same facts as the status page; 11 of the 214 are named key accounts (list in
incident channel). Do not add cause detail beyond Update 3. Credit questions go to
the account manager's normal approval path — no commitments in the incident.

## Consistency check
| 1 | declared 08:52, posted 09:05 (≤15 min) | 0 | yes |
| 2 | promised 09:35, posted 09:35 | 0 | yes |
| 3 | promised 10:05, posted 10:05; cause approved 10:02 | 0 | yes |
| 4 | promised 11:05, posted 10:50 | 0 | yes |
| 5 | promised 11:50, posted 11:50; summary owner: Head of Eng, due 09-25 | 0 | yes |
```

## Techniques Used

- **AG-19 Time-Critical Response Protocol** — first update in 15 minutes, and every next-update time kept.
- **NE-14 Multi-Audience Documentation Targeting** — one fact sheet, five channels, each fitted to its reader.
- **CM-02 Constraint Specification** — confirmed-and-approved only; no suspected cause, no fix ETA.
- **QA-01 Self-Verification** — per-update check on timing, claims and channel sync.

## Related Prompts

- `domain-sales-customer/support/support_escalation_response_drafter.md` — the
  one-customer reply and handoff, built from the same fact sheet.
- `domain-sales-customer/support/support_ticket_triage_and_routing.md` — where a
  ticket cluster becomes an incident with a severity.
- `domain-engineering-workflows/workflows/engineering_postmortem_blueprint.md` —
  the engineering review behind the promised summary.
