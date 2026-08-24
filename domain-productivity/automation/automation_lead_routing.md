---
title: "Lead Routing and Assignment — Condition-Based Distribution with Round-Robin and SLA"
category: productivity/automation
description: "Specify an automation that assigns incoming leads or requests to the right owner using ordered conditions, round-robin fallback, owner notification, an audit log, and SLA follow-up reminders."
techniques:
  - ST-01
  - ST-03
  - DS-06
  - CM-02
  - QA-01
difficulty: intermediate
tags:
  - automation
  - lead-routing
  - assignment
  - round-robin
  - sla
updated: "2026-06-07"
related_prompts:
  - domain-productivity/automation/automation_form_notification.md
  - domain-productivity/automation/automation_data_sync.md
  - domain-productivity/automation/automation_content_monitoring.md
---

# Lead Routing and Assignment

**Objective:** Specify an automation that assigns each incoming lead or request to the correct owner using ordered, mutually-clear conditions (with a round-robin fallback for unmatched cases), updates the record, notifies the owner with the reason, logs the decision, and optionally enforces an SLA with follow-up reminders.

**When to use:**
- Distributing sales leads to reps by territory, size, or vertical.
- Routing support/service requests to the right queue or person.
- Balancing workload fairly across a team via round-robin.
- Adding SLA accountability (contact within N hours) to incoming work.

**When NOT to use:**
- Single-owner intake — a plain notification is enough (see `automation_form_notification.md`).
- Routing that depends on judgment a rules engine can't encode — keep a human triage step.
- Very high volume needing a real queueing/assignment system rather than a no-code flow.

**Audience:** Individuals and small teams building automations in Zapier, Make, n8n, or similar no-code/low-code platforms.

---

## Inputs / Context

Supply the following before generating the spec:

1. **Source** — where leads/requests arrive (CRM, form, inbox) and the record type.
2. **Routing criteria** — the fields and value bands that decide the owner (size, region, industry, etc.).
3. **Owners/teams** — who receives each route, plus any round-robin pool.
4. **Default handling** — what happens when nothing matches (round-robin, triage queue, default owner).
5. **Notification target** — how owners are told (Slack DM, email) and what the message says.
6. **SLA (optional)** — required first-contact time and escalation behavior.
7. **Available integrations** — confirm the source, notifier, and any counter/log store are connected.

---

## Constraints

### Must
- Use only integrations that are connected on the chosen platform (or flag the gap).
- Evaluate conditions in an explicit order; **first match wins** and the order is documented.
- Provide a **default route** so no lead is ever unassigned.
- Notify the assigned owner with the routing reason and a link to the record.
- Log every routing decision (lead, matched condition, owner, timestamp) for audit.
- Handle missing required fields by routing to a triage queue, not by guessing.

### Must Not
- Assume an integration exists — flag any source/notifier/store that needs setup.
- Leave overlapping conditions ambiguous about which one applies.
- Assign a lead and never tell the owner.
- Silently drop leads that match no route or have missing data.

---

## Instructions

1. **Restate the routing goal.** One line: what is routed, by which criteria, to whom.
2. **Define the trigger.** Source app + record type; any filter for which records enter routing.
3. **Order the routes.** For each: condition, owner/team, lead type/label, priority. State that the first matching route wins.
4. **Define the default.** Round-robin pool (with a tracked counter and skip-if-unavailable) or a triage queue / default owner; flag for review.
5. **Specify post-assignment actions.** Update the record (owner, routed date, reason); notify the owner (reason + link); append to the routing log.
6. **Specify SLA (optional).** If not contacted within N hours → remind owner; within 2N → alert manager and optionally reassign.
7. **Handle edge cases.** Multiple matches → first wins; missing required field → triage queue + flag; owner unavailable → backup or queue.
8. **Self-check before output.** Confirm: integrations confirmed; route order is unambiguous and first-match documented; a default exists; every assignment notifies and logs; missing-data and unavailable-owner paths exist. Then emit the spec.

---

## False-Positive Prevention

❌ **DON'T:**
- Assume the CRM, notifier, or round-robin counter store is connected.
- Write overlapping conditions without specifying evaluation order.
- Omit a default route, leaving some leads unassigned.
- Assign silently without notifying the owner or logging the decision.
- Route a lead with missing qualifying data as if the data were present.

✅ **DO:**
- Confirm integrations and flag any that need setup.
- Order routes explicitly and document first-match-wins.
- Always include a default (round-robin or triage) so nothing is dropped.
- Notify the owner with the reason and log every decision.
- Send incomplete records to a triage queue with a data-completion flag.

---

## Output Format

```
AUTOMATION: Route Incoming [LEADS/REQUESTS] to Owner
PURPOSE: [one line]
INTEGRATIONS REQUIRED: [source, notifier, log/counter store] — [confirmed / NEEDS SETUP]

TRIGGER
- Source: New [record type] in [source app]
- Filter: [enter routing only if ... | all]

ROUTING (first match wins, in order)
ROUTE 1: [condition] → owner [A]; type "[label]"; priority [P]
ROUTE 2: [condition] → owner [B]; type "[label]"; priority [P]
ROUTE 3: [condition] → owner [C]; type "[label]"; priority [P]
DEFAULT (no match): [round-robin pool | triage queue | default owner]; flag for review

ROUND ROBIN (if used)
- Pool: [assignees]; counter in [store]; reset [cadence]; skip if unavailable

POST-ASSIGNMENT ACTIONS
1. Update record: Owner, Routed Date, Routing Reason
2. Notify owner ([Slack DM | email]): name / company / key field / reason / link / "follow up within [SLA]"
3. Log: [lead ID, name, condition, owner, timestamp]

SLA (optional)
- Not contacted in [N] h → remind owner
- Not contacted in [2N] h → alert manager + [reassign?]

EDGE CASES
- Multiple matches → first route wins
- Required field missing → triage queue + flag
- Owner unavailable → [backup | queue]

TESTING CHECKLIST
- [ ] ...
```

---

## Example Output

```
AUTOMATION: Route Incoming Sales Leads to Owner
PURPOSE: Send each new lead to the right rep by company size, region, and vertical; balance the rest fairly.
INTEGRATIONS REQUIRED: HubSpot (CONFIRMED), Slack (CONFIRMED), Google Sheets "RR Counter" + "Routing Log" (CONFIRMED)

TRIGGER
- Source: New contact in HubSpot with Lifecycle Stage = "Lead"
- Filter: enter routing only if Email is present (else → triage)

ROUTING (first match wins, in order)
ROUTE 1: Company size > 500 → owner Dana (Enterprise); type "Enterprise"; priority High
ROUTE 2: Region = EMEA → owner Liam (EMEA); type "EMEA"; priority Normal
ROUTE 3: Industry = Healthcare → owner Priya (Vertical); type "Vertical"; priority Normal
DEFAULT (no match): round-robin among [Sam, Alex, Jordan]; type "General"; flag for review

ROUND ROBIN
- Pool: Sam, Alex, Jordan; counter in "RR Counter" sheet; reset weekly; skip anyone marked OOO

POST-ASSIGNMENT ACTIONS
1. Update HubSpot: Owner = assignee; Routed Date = now(); Routing Reason = matched condition
2. Notify owner via Slack DM:
   "🆕 New {type} lead assigned to you:
    *Name:* {name}   *Company:* {company}   *Size:* {size}
    *Why you got this:* {routing reason}
    → <{HubSpot record URL}|Open lead>
    Please follow up within 4 business hours."
3. Append to "Routing Log": [lead ID, name, company, condition, owner, now()]

SLA
- Not contacted in 4 h → remind owner via Slack
- Not contacted in 8 h → alert manager #sales-mgmt + reassign to round-robin

EDGE CASES
- Lead matches both Route 1 and Route 2 → Route 1 wins (size before region)
- Missing Company size → route to "Triage" queue + flag "needs enrichment"
- Assigned rep OOO → skip in round robin / reassign to backup

TESTING CHECKLIST
- [ ] Lead with size 800 → assigned to Dana (Enterprise)
- [ ] EMEA lead under 500 employees → assigned to Liam
- [ ] Lead matching no route → enters round robin, counter advances
- [ ] Lead with blank size → lands in Triage with flag
- [ ] Owner notification arrives with correct reason + working link
- [ ] Run 10 test leads → routing log has 10 complete rows
- [ ] Leave a lead uncontacted past 4 h → reminder fires
```

---

## Verification

- [ ] Every named integration is confirmed available or flagged as needing setup.
- [ ] Routes are ordered and first-match-wins is documented.
- [ ] A default route guarantees no lead is unassigned.
- [ ] Round-robin (if used) tracks a counter and skips unavailable owners.
- [ ] Each assignment updates the record, notifies the owner with reason + link, and logs the decision.
- [ ] Missing-required-field leads go to triage with a flag.
- [ ] SLA reminders/escalation (if specified) are defined.

---

## Techniques Used

- **ST-01 (Clear Objective Statement):** Fixes the goal — assign each lead to the right owner with accountability — so the routing logic stays purposeful.
- **ST-03 (Output Format Specification):** Locks the trigger→routes→default→actions→SLA layout into a copy-ready spec.
- **DS-06 (Prioritization and Severity Guidance):** Ordered first-match routing, priority labels, and SLA escalation triage which leads get attention first.
- **CM-02 (Constraint Specification):** Encodes Must/Must-Not rules (default route required, notify+log every assignment, no silent drops) as explicit constraints.
- **QA-01 (Self-Verification):** A pre-output check confirms route order, default coverage, notification/logging, and edge-case paths before emitting.

---

## Related Prompts

- `domain-productivity/automation/automation_form_notification.md` — Simpler single-channel alert when no assignment logic is needed.
- `domain-productivity/automation/automation_data_sync.md` — Mirror routed records into another system of record.
- `domain-productivity/automation/automation_content_monitoring.md` — Capture-and-triage pattern with the same logging/failure discipline.
