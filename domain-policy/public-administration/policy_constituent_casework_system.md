---
title: "Constituent Correspondence and Casework Response System — Intake Triage, Privacy Release, Response Templates, Tracking, Escalation Ladder, and Tone"
category: policy/public-administration
description: "Design how an elected office or public agency answers the public: separate views mail from casework, triage by urgency with same-day handling for safety and hard deadlines, require a privacy release before acting on anyone's behalf, set acknowledgement and status-update service levels, write templates whose tone is calibrated against bad examples, define tracking fields and close-out codes, build an escalation ladder that respects what the office may and may not do, and size staff to the volume — distinct from commercial support-ticket triage (support_ticket_triage_and_routing) and from a member of the public writing their own complaint (advocacy_regulator_complaint_drafter)."
techniques:
  - AG-11
  - DS-36
  - NE-04
  - DD-05
difficulty: intermediate
tags:
  - constituent-services
  - casework
  - correspondence-management
  - public-sector-customer-service
  - privacy-release
  - escalation-ladder
  - answer-constituent-mail
  - help-residents-with-problems
  - track-constituent-requests
updated: "2026-10-03"
reasoning:
  styles: [structural, communicative, procedural]
  stakes: medium
  horizon: months
  uncertainty: risk
  evidence_quality: mixed
  domain_complexity: regulated
  collaboration: small_team
  output_format: [structured, prose]
  user_role: [chief_of_staff, caseworker, district_director, agency_customer_service_lead]
  mode: [design, communicate]
related_prompts:
  - domain-sales-customer/support/support_ticket_triage_and_routing.md
  - domain-written-advocacy/institutions-and-records/advocacy_regulator_complaint_drafter.md
  - domain-policy/public-administration/policy_agency_performance_measures.md
---

# Constituent Correspondence and Casework Response System

**Objective:** Give an office a working system for every letter, email, call and
walk-in: what kind of contact it is, how fast it must be handled, what the office is
allowed to do, what the reply says and how it sounds, who chases it, and when it goes
up the ladder — so nobody's urgent problem waits behind a postcard campaign.

**Audience:** Chiefs of staff, district directors and caseworkers in legislators'
and councillors' offices; customer-service and ombuds leads in public agencies.

**When to Use:**
- A new office is setting up, or a backlog has built and nobody knows what is in it.
- An urgent case was missed and you need a triage rule that would have caught it.
- Replies are inconsistent in tone, slow, or promise outcomes the office cannot deliver.
- **Not this prompt if** you run **commercial customer support** —
  `domain-sales-customer/support/support_ticket_triage_and_routing.md` covers queues,
  SLAs and routing for a company. If you are the resident writing to complain, use
  `domain-written-advocacy/institutions-and-records/advocacy_regulator_complaint_drafter.md`.
  Measuring the office's results over a year is
  `domain-policy/public-administration/policy_agency_performance_measures.md`.

## Inputs / Context

1. **Office type and remit**: legislator, councillor, mayor, agency; the
   jurisdiction's rules on what the office may do for constituents.
2. **Volume and mix**: contacts per month by channel and type, recent campaigns.
3. **Staff**: number, hours, languages, and the case-management or CRM tool.
4. **Agencies most often involved** and whether liaison contacts exist.
5. **Privacy and records rules**: required consent forms, records-retention and
   public-records exposure of correspondence.
6. **The official's approved positions** on live issues, and who approves new ones.
7. **Two or three recent replies**, good and bad, to calibrate tone.

Rules on privacy releases, ethics and records are taken from the office's own
counsel or ethics guidance; where not supplied they are marked `[verify — ethics/counsel]`.

## Method

1. **Classify every contact (AG-11).** Four types: **views** (opinion on an issue),
   **casework** (a personal problem with a government agency), **service request**
   (pothole, certificate, meeting, tour), **other** (media, threats, solicitations).
   Each type has its own owner and template set.
2. **Triage by urgency.** **Same day**: risk to life or safety, loss of housing or
   utilities within 72 hours, a hard legal or benefit deadline within 7 days.
   **Priority**: deadline within 30 days, vulnerable person, repeat contact.
   **Routine**: everything else. Threats go immediately to the security or police
   protocol, not the queue.
3. **Consent before action.** Casework does not start until a signed or recorded
   privacy release names the person, the agency and the information to be shared.
   Collect only what the inquiry needs.
4. **Set service levels.** Acknowledge within 2 business days (same day for
   urgent); casework status update at least every 14 days; views replies within
   15 business days or batched for campaigns.
5. **Write templates and calibrate tone (NE-04).** For each type: acknowledgement,
   status, close-out, and "we can't help with this, here is who can". Show a bad and
   a good version: plain language, a specific next step, no promise of an outcome
   the agency decides, and no jargon or acronyms.
6. **Define what the office can and cannot do (DD-05).** Checkable rules: may
   inquire, ask for a status or a review, and explain the process; may not direct an
   agency's decision, intervene in a court case or active investigation, or give
   legal advice. Judgement items (pushing harder on a sympathetic case) go to a
   named senior staffer. Donor or political status never affects handling.
7. **Build the escalation ladder (DS-36).** Caseworker → agency liaison → senior
   staff → the official's direct contact with agency leadership, each with a trigger
   (no agency response in 21 days, an error on the agency's side, imminent harm).
8. **Track and close.** Required fields: type, urgency, agency, issue code, consent
   date, every contact, outcome code (resolved favourably, resolved — explained,
   referred, no jurisdiction, withdrawn). Recurring issue codes feed a monthly
   systemic-issues note to policy staff.
9. **Size the staff.** Hours needed = contacts × average handling time by type;
   compare with available hours after leave and admin.

## Output Format

```
# Casework and correspondence system — [office]

## 1. Contact types and owners
## 2. Triage rules
| Level | Criteria | Response time | Who |
## 3. Consent and privacy
## 4. Service levels
## 5. Templates (each with bad → good tone pair)
## 6. Can / cannot do (checkable) · judgement items → [named role]
## 7. Escalation ladder
| Step | Trigger | Who | Max wait |
## 8. Tracking fields and close-out codes
## 9. Workload and staffing
| Type | Contacts/mo | Hours each | Hours/mo |
Capacity: [..] h/mo → gap [..] → fix [..]
```

## Verification

- [ ] Every contact type has an owner and a template set.
- [ ] Same-day triage criteria are concrete (hours, days, named harms).
- [ ] No casework action is possible before consent is recorded.
- [ ] Templates promise process, not outcomes the agency decides.
- [ ] The can/cannot list covers courts, investigations, legal advice and political favour.
- [ ] Workload arithmetic recomputes and the gap has a fix.

## False-Positive Prevention

1. **Volume as priority.** Two thousand campaign emails are one issue; one eviction
   notice is an emergency. Triage by harm and deadline, never by count.
2. **Promising outcomes.** "We will get your benefits restored" sets up a broken
   promise; "we have asked the agency to review your file and will update you by
   [date]" does not.
3. **Acting without consent.** Sharing someone's details with an agency without a
   release breaches privacy rules and trust, even with good intent.
4. **Closing without an outcome code.** "Closed" hides whether the person was
   helped; outcome codes make the record honest.
5. **Treating every complaint as a case.** A policy opinion is views mail; opening
   a case on it wastes casework hours.
6. **Ignoring the pattern.** Fifty identical agency delays are a systemic problem
   for policy staff, not fifty individual wins.

## Example Output

```
# Casework and correspondence system — State Representative, District 41 office
Staff: 1 caseworker, 1 correspondence aide, 0.5 district director. Contacts: 420/month.

## 2. Triage
| Same day | Shut-off notice, eviction ≤ 72 h, benefit appeal deadline ≤ 7 d, safety | 4 business hours | Caseworker; director backup |
| Priority | Deadline ≤ 30 d, older or disabled person, 3rd contact | 2 days | Caseworker |
| Routine  | All else | 2 days ack; 15 days reply | Aide / caseworker |
Threats → building security + police liaison immediately; logged, never answered by staff.

## 5. Templates — casework acknowledgement
Bad: "Thank you for contacting the Representative. We will look into your
unemployment issue and resolve it ASAP."
Good: "Thank you for writing about your unemployment claim. With your signed release
(attached form), we will ask the Department of Labor to review your file. The
Department decides the claim; we can make sure it is looked at and keep you informed.
You will hear from Maria Lopez, caseworker, by Friday 16 October."

## 6. Cannot do
Direct the agency's decision · contact a judge or intervene in a court case ·
interfere in an active investigation · give legal advice (refer to legal aid list) ·
prioritise by party, donation or endorsement.

## 7. Escalation
| 1 | Case opened | Caseworker → agency portal | 10 business days |
| 2 | No reply in 10 d or agency error | Caseworker → agency liaison | 10 business days |
| 3 | No resolution in 21 d, or imminent harm | District director → deputy director | 5 business days |
| 4 | Systemic or ignored | Representative → agency head | — |

## 9. Workload
| Views (incl. 240 campaign postcards)  | 300 | 0.1 (batched) | 30  |
| Casework                              | 85  | 2.5           | 212 |
| Service requests                      | 35  | 0.5           | 18  |
Total 260 h/mo vs capacity 1.5 FTE × 140 h = 210 h → gap 50 h/mo.
Fix: agency-liaison direct lines for unemployment and Medicaid (est. 2.5 → 1.8 h/case
saves 60 h, [estimate — measure after 3 months]); campaign replies approved once and
batched. Systemic note: 31 of 85 cases are unemployment-claim delays > 6 weeks →
policy staff for the committee hearing.
```

## Techniques Used

- **AG-11 Taxonomy-Based Classification Systems** — contact types, urgency levels and close-out codes.
- **DS-36 Blocker Escalation Framework** — the ladder with triggers, owners and maximum waits.
- **NE-04 Good vs Bad Example Calibration** — each template shown against the reply that over-promises.
- **DD-05 Human Review Flags** — checkable can/cannot rules separated from judgement items routed to a named role.

## Related Prompts

- `domain-sales-customer/support/support_ticket_triage_and_routing.md` — the commercial-support equivalent for a company's queue.
- `domain-written-advocacy/institutions-and-records/advocacy_regulator_complaint_drafter.md` — the resident's side, writing the complaint.
- `domain-policy/public-administration/policy_agency_performance_measures.md` — measuring the office's service outcomes over time.
