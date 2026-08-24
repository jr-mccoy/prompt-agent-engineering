---
title: "Legal Intake Triage & Router"
category: legal/in-house-legalops
description: "Triage an incoming legal request: classify the request type, assign an urgency tier (P0–P3) with SLA targets, route to the right destination (self-serve, paralegal, associate, senior counsel, outside counsel), apply auto-rejection and de-duplication rules, and produce a ticketing-system-ready output mapped to Jira / ServiceNow / Ironclad fields."
techniques:
  - ST-01
  - ST-02
  - ST-03
  - CM-02
  - DS-02
  - QA-01
difficulty: intermediate
tags:
  - legal
  - legal-ops
  - intake
  - triage
  - workflow
updated: "2026-05-11"
related_prompts:
  - domain-legal/in-house-legalops/legal_playbook_builder_for_contract_type.md
  - domain-legal/in-house-legalops/legal_matter_summary_for_executive.md
  - domain-legal/client-intake-communications/legal_new_matter_intake_summary.md
---

**Purpose:** Convert a free-text intake from a business stakeholder (sales, procurement, HR, an employee, an executive) into a routed, prioritized, deduplicated ticket the legal team can act on without ambiguity. Output supports both human reviewers and automated workflow tools.

**When to use:** Standing up or refreshing a legal-intake function, batch-triaging a backlog, configuring a Jira/ServiceNow/Ironclad workflow, defining SLAs the business commits to, reducing "where does this go?" thrash, building the rules a junior legal-ops coordinator follows.

---

## Your Input

- **Raw intake content:** [Email, form submission, Slack message, ticket text — whatever the requester sent]
- **Requester context:** [Name, role, business unit, geography; previous tickets if known]
- **Subject-matter scope of the in-house team:** [Which categories the team handles in-house vs always routes to outside counsel]
- **Authority / self-serve thresholds:** [E.g., NDAs under $X self-serve via Ironclad template; vendor agreements under $Y route to commercial counsel; over $Y route to senior counsel]
- **Active matter inventory (optional):** [For de-duplication — is this an existing matter?]
- **Conflict-screen status / pre-conditions:** [If routing to outside counsel, conflict-check posture]
- **Ticketing system in use:** [Jira / ServiceNow / Ironclad / other — defines field schema]
- **Off-scope categories:** [What legal explicitly does not handle — e.g., individual personal legal matters, sales-team pricing escalations dressed up as "legal" questions]

---

## Constraints

**Must:**
- Classify the request into a **single primary type** (and optionally one secondary type). Allowed categories:
  - Contract review (new / amendment / renewal / termination)
  - Litigation matter (new / development on existing)
  - Pre-litigation dispute (demand letter received / sent)
  - Employment & labor (terminations, complaints, accommodation, policy)
  - IP (filing, enforcement, licensing)
  - Regulatory (inquiry, examination, filing, new-rule analysis)
  - Privacy / data protection (DSAR, breach notification, DPIA)
  - Corporate housekeeping (entity, governance, minutes, qualification)
  - Government / public sector (FOIA, subpoena, government contract flowdown)
  - Urgent / crisis (incident response, regulator on the phone, press inquiry)
  - Non-substantive (request for status, copy of an executed contract, signature only)
- Assign an **urgency tier**:
  - **P0** — same-day: subpoena with a return date, regulator on the line, data-breach trigger, TRO/PI threat, active media inquiry, executive deal-blocking.
  - **P1** — 48 business hours: signed-contract deadline tied to a business commitment, employment termination needing review, demand letter with response deadline.
  - **P2** — 1 week: standard contract review, routine HR question, IP filing decision.
  - **P3** — routine (2–4 weeks): non-urgent inquiry, training request, housekeeping.
- Route to a **destination**:
  - Self-serve (template, playbook, FAQ link)
  - Paralegal (intake-form completion, filings, document pulls)
  - Associate / commercial counsel (standard contract review, routine matter)
  - Senior counsel / GC (escalation triggers, novel issue, material exposure)
  - Outside counsel (specialty, jurisdictional reach, conflict, capacity)
- Apply **auto-rejection criteria** with a templated response: (a) already-signed contract (route to compliance / re-paper queue, not new review); (b) out-of-scope (personal matter, sales-team pricing); (c) wrong department (HR-policy, IT-security, finance-policy).
- Apply **de-duplication**: search active matter inventory for the same counterparty / topic / requester before opening new.
- Produce a **ticketing-system-ready field map** for the configured tool.

**Must Not:**
- Invent matter IDs, ticket numbers, counterparty names, or routing destinations not in the user-supplied org structure.
- Provide substantive legal advice — triage routes, it does not opine.
- Classify into multiple primary categories. Choose one; flag the secondary if material.
- Skip the conflict-check posture for outside-counsel routing.
- Apply a P0 tier to anything that the requester merely labeled "urgent" — urgency is defined by the criteria above, not the requester's tone.
- Generic "consult legal" disclaimer in the auto-rejection response — give the requester a specific next step (template link, correct department contact).

---

## Instructions

1. **Parse the intake.** Extract: who is asking, what they want, when they need it, the counterparty (if any), the deal size or matter materiality (if any), the requester's authority, attached documents.
2. **Classify the primary type** from the allowed list. If genuinely cross-category (e.g., an employee termination involving an IP-assignment dispute), pick the dominant category and flag the secondary.
3. **De-duplicate.** Match counterparty + topic + requester against the active matter inventory. If duplicate, link to the existing matter; do not open new.
4. **Apply auto-rejection rules.** If the request is out-of-scope, generate the specific routing response (template link, correct contact, or "this is a compliance question, route to {team}").
5. **Assign urgency.** Apply the P0–P3 criteria. Do not accept the requester's self-labeling; apply the objective criteria.
6. **Route.** Walk the destination ladder:
   - Self-serve eligible? (Template fits, under threshold, no escalation triggers)
   - Paralegal eligible? (Standard form, document task, filing)
   - Associate / commercial counsel? (Standard review, in playbook scope)
   - Senior counsel? (Escalation triggers, novel issue, material exposure)
   - Outside counsel? (Specialty, jurisdictional reach, conflict, capacity)
7. **Map to ticketing-system fields.** Produce the field schema for the configured tool (Jira / ServiceNow / Ironclad). Identify required fields the requester has not provided and the follow-up question to obtain them.
8. **Set the SLA acknowledgment.** Give the requester an acknowledgment with the assigned tier, destination, and SLA target date — no commitment to a substantive answer, only to a response by the SLA.

---

## Output Format

```markdown
# Intake Triage — {Requester Name} — {Subject Line}

## Classification
- **Primary type:** {category}
- **Secondary type (if applicable):** {category}
- **Counterparty / subject:** {name or topic}
- **Materiality flag:** {deal size / matter type / regulatory exposure}

## Urgency
- **Tier:** {P0 / P1 / P2 / P3}
- **SLA target:** {response by date/time}
- **Rationale:** {which objective criterion triggers the tier}

## De-duplication Check
- **Existing matter match:** {Yes — link to matter {ID} / No — new}
- **Notes:** {how match was determined or ruled out}

## Routing
- **Destination:** {Self-serve / Paralegal / Associate / Senior counsel / Outside counsel}
- **Specific owner:** {role, not name unless org-supplied}
- **Conflict-screen needed:** {Yes / No — if outside counsel routing}
- **Reason:** {one-sentence routing justification}

## Auto-Action (if applicable)
- **Auto-reject reason:** {already-signed / out-of-scope / wrong department}
- **Templated response to requester:** {specific next step — template link, correct contact, escalation path}

## Ticketing-System Field Map ({tool})
| Field | Value |
|---|---|
| Title | {short title} |
| Type | {Jira issue type / ServiceNow record type / Ironclad workflow} |
| Priority | {tool's priority field mapped from P-tier} |
| Owner / Assignee | {role} |
| Reporter | {requester} |
| Business unit | {BU} |
| Counterparty | {name or "n/a"} |
| Matter type | {category} |
| Deal value | {$ or "n/a"} |
| Required-by date | {date} |
| Linked matters | {matter IDs} |
| Privilege flag | {Yes / No} |
| Attachments | {document list} |

## Missing Information — Follow-Up
- {Field 1 not provided, question to requester}
- {Field 2 not provided, question to requester}

## Acknowledgment Draft (to requester)
> Thank you — your request has been logged as {ticket ID}, classified as {category}, tier {Px}, assigned to {role}. We will respond by {SLA date}. {Conditional: please provide {missing field} to begin substantive review.}
```

---

## Verification

- [ ] Exactly one primary type assigned (secondary flagged only if material).
- [ ] Urgency tier assigned per objective P0–P3 criteria, not requester self-labeling.
- [ ] De-duplication check performed against supplied matter inventory.
- [ ] Routing destination matches authority threshold and escalation triggers.
- [ ] Conflict-check posture identified for outside-counsel routing.
- [ ] Auto-rejection (if applied) gives requester a specific next step.
- [ ] Ticketing-system field map complete for the configured tool.
- [ ] Missing-information follow-up questions are specific.
- [ ] No substantive legal advice embedded in triage output.
- [ ] No invented matter IDs, counterparties, or destinations.

---

## False-Positive Prevention

| Failure mode | Correction |
|---|---|
| Accepting requester's "URGENT!!" subject line as P0 | Apply objective criteria; "deadline next week" is P1 or P2, not P0 |
| Routing a $2M MSA to self-serve because the requester said "it's standard" | Self-serve thresholds are based on objective deal size and escalation triggers, not requester assertion |
| Opening a new matter when an existing matter covers the same counterparty/topic | De-duplicate first; link to existing matter |
| Classifying a "where is my contract?" request as contract review | Non-substantive — route to records/paralegal, not commercial counsel |
| Treating an HR-policy question as employment-legal | Many HR-policy questions belong to HR ops, not legal; auto-route with specific contact |
| Generic acknowledgment without an SLA date | Acknowledgment must commit to a response-by date matched to the tier |
| Routing to outside counsel without a conflict-check posture | Always identify whether a conflict screen has run or must run |
| Auto-rejection with "please consult legal" — but the requester just did | Auto-rejection must name the correct destination (HR team, IT-security team, compliance, the specific template) |
| Substantive legal advice in the triage output | Triage routes; it does not opine. Move substantive content to the assigned owner |
| Field map missing required ticketing-system fields | Each ticketing tool has required fields; identify which the requester has not supplied and ask before opening |
| P0 used for everything to be safe | Over-tiering destroys the SLA system; reserve P0 for the criteria above |
