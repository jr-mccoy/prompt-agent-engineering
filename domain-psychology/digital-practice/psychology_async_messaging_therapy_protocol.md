---
title: "Asynchronous Messaging Therapy Protocol"
category: psychology/digital-practice
description: "Design an asynchronous text/messaging therapy protocol with risk routing: response-window SLAs, scope of what async is and is not appropriate for, session-equivalence/billing, structured message format, in-text crisis detection and escalation (async is NOT for emergencies), boundary/availability framing, documentation, and criteria for converting to synchronous care."
techniques:
  - NE-02
  - CM-02
  - DT-01
  - ST-04
  - QA-04
difficulty: intermediate
intended_use: model-testing
tags:
  - asynchronous-therapy
  - messaging-therapy
  - risk-routing
  - response-SLA
  - crisis-detection
  - boundaries
  - documentation
  - digital-practice
updated: "2026-06-08"
related_prompts:
  - domain-psychology/digital-practice/psychology_telemental_health_program_design.md
  - domain-psychology/risk-crisis/psychology_crisis_de_escalation_session_plan.md
  - domain-psychology/risk-crisis/psychology_columbia_suicide_risk_assessment.md
  - domain-psychology/practice-operations/psychology_telehealth_state_of_licensure_decision_aid.md
---

# Asynchronous Messaging Therapy Protocol

## Objective

Produce a complete protocol for asynchronous (text/messaging) therapy that is clinically appropriate and safety-routed. The protocol specifies: (1) response-window service-level agreements (SLAs), (2) the scope of what asynchronous care is and is not suitable for, (3) session-equivalence and billing handling, (4) a structured message format that keeps async exchanges clinically organized, (5) in-text crisis-detection language and an escalation pathway built on the explicit premise that **asynchronous channels are not for emergencies**, (6) boundary and availability framing, (7) documentation standards, and (8) criteria for converting to synchronous (video/phone) care. A licensed clinician retains decision authority; the async channel is a structured care modality with hard safety limits, not an always-on crisis line.

## When to Use

- When a practice is adding asynchronous messaging therapy as a modality and needs an operating protocol before client enrollment.
- When an existing messaging offering lacks defined response windows, crisis routing, or conversion criteria and needs to be formalized.
- When clarifying for clients and clinicians exactly what async is appropriate for and where its boundaries are.
- When a payer, malpractice carrier, or accreditor requires a documented async-care protocol with risk-routing.
- When a clinician needs structured-message and documentation templates for async work.

## Inputs / Context Required

- **Async platform**: the HIPAA-compliant messaging platform in use (with BAA), its features (read receipts, attachments, scheduling), and whether it is integrated with the EHR.
- **Clinician availability model**: business hours, days off, coverage/backup, and the realistic response cadence.
- **Client population**: typical presentations and acuity; whether high-risk clients are being considered for async (generally contraindicated as a primary modality).
- **Billing arrangement**: how async is reimbursed or charged (subscription, per-message-bundle, time-based digital E/M, self-pay), noting that async reimbursement varies by payer.
- **Existing crisis protocol**: the practice's emergency/safety routing and per-location resources.
- **Licensure/jurisdiction**: where clients are physically located (client location governs jurisdiction; relevant if clients message while traveling).
- `[clinician input required: the clinician's committed response-window SLA and after-hours/weekend handling]`
- `[clinician input required: presentations or acuity levels the clinical director excludes from async as a primary modality]`

## Constraints

### Must

- Define explicit **response-window SLAs** (e.g., responses within one business day; specify business hours, weekends, and holidays) and require these be communicated to the client in advance and in the consent.
- State unambiguously that **asynchronous messaging is NOT for emergencies or acute crises** — in the protocol, the consent, and the platform-facing messaging — and provide the emergency alternative every time.
- Define the **scope**: what async is well-suited for (skills reinforcement, reflection, psychoeducation, between-session continuity, low-acuity check-ins) and what it is not (active risk, acute deterioration, complex assessment, time-sensitive clinical change).
- Build an **in-text crisis-detection** step: the language/signals the clinician (or any monitoring layer) watches for, and a same-day-or-faster human escalation pathway.
- Provide the **escalation ladder** with detection-to-response handling: clinician this week / clinician today (convert to synchronous) / 988 Suicide & Crisis Lifeline / 911 or nearest ED — tied to triggering signals, and routed to resources local to the client's physical location.
- Specify **session-equivalence/billing** handling honestly (how async time/exchanges map to a billable unit; note payer variability and flag specifics as `[verify current payer rule]`).
- Define **conversion criteria**: the signals that require moving from async to a synchronous (video/phone) session or in-person care.
- Preserve **clinician decision authority**: any automated keyword flagging or triage is decision-support that routes to a human; it never auto-responds to or auto-clears a risk signal.
- Specify **documentation**: how async exchanges are recorded in the clinical record, including risk-screening and any escalation.

### Must Not

- Do not present or operate async messaging as a crisis line, an emergency channel, or a substitute for real-time assessment of acute risk.
- Do not leave the response-window SLA undefined or implied; vague availability creates safety and liability risk.
- Do not enroll a client with active acute risk into async as their primary or sole modality.
- Do not let an automated keyword flag close out or auto-respond to a risk signal without a human clinician.
- Do not route a crisis to resources local to the clinician rather than to the client's physical location.
- Do not fabricate payer reimbursement rules or CPT applicability; flag billing specifics as `[verify current payer rule]`.

## Instructions

1. **Set response-window SLAs.** Specify the committed turnaround (e.g., within one business day), business hours, and explicit handling of evenings, weekends, holidays, and clinician absences (with coverage). Require these be stated in onboarding and consent, and surfaced in the platform.

2. **Define scope — good fit vs. not.** Produce the two-column boundary that clients and clinicians can apply.

   | Async is well-suited for | Async is NOT appropriate for |
   |--------------------------|------------------------------|
   | Skills practice & homework review | Active suicidal/homicidal risk |
   | Reflection / journaling between sessions | Acute deterioration or decompensation |
   | Psychoeducation and resource sharing | Complex diagnostic assessment |
   | Low-acuity check-ins / continuity of care | Time-sensitive clinical change needing real-time response |
   | Logistics and brief clarifications | Anything requiring immediate two-way interaction |

3. **Build the structured-message format.** Give the clinician a repeatable response structure so async stays clinical rather than chatty: acknowledge → reflect/validate → respond to content → assign/clarify next step → restate availability/limits. Include a parallel structure clients can use to make their messages reviewable (situation, what they tried, the specific question/ask).

4. **Insert the crisis-detection-in-text step.** Specify the signals to watch for in client messages — explicit or implied suicidality, hopelessness, self-harm, threat to others, acute deterioration, or a message indicating an emergency in progress. State that any such signal triggers immediate human review and escalation, never a routine async reply. If an automated flagging layer exists, it routes to a clinician; it does not decide.

5. **Specify the escalation ladder.** Map signals to action and to the client's local resources.

   | Signal in message | Tier | Action |
   |-------------------|------|--------|
   | Passive ideation, no plan/intent; distress within scope | Clinician this week | Reply within SLA; assess; consider scheduling synchronous session; provide 988 as standing resource |
   | Active ideation/plan/intent; acute deterioration | Clinician today — convert to synchronous | Initiate live contact (phone/video) ASAP; direct risk assessment (e.g., C-SSRS); safety planning |
   | Emergency in progress / imminent danger / message that may be a final communication | 911 / nearest ED + 988 | Direct client to call 911 or go to nearest ED at their physical location; contact emergency services/contact; do not rely on async exchange |

   State the limit plainly: because responses are not real-time, async cannot reliably detect or respond to imminent risk — hence the standing instruction to use 988/911 for emergencies, repeated in consent and platform.

6. **Handle session-equivalence and billing.** Describe how async work maps to a billable unit (e.g., time-based digital evaluation/management, message bundles, or subscription), and how time is tracked and documented. Flag that coverage varies — mark payer/CPT specifics as `[verify current payer rule]`.

7. **Frame boundaries and availability.** Define what the client can expect: the response window, that the clinician is not continuously monitoring messages, the after-hours reality, and the emergency alternative. This framing belongs in onboarding, consent, and a brief standing footer/auto-context on the channel.

8. **Set conversion criteria.** List the triggers to move from async to synchronous or in-person: any risk signal, rising acuity, a clinical question that needs real-time dialogue, repeated misunderstanding in text, or client request.

9. **Specify documentation.** Each clinically meaningful async exchange (or summary period) is recorded in the chart with: dates/times, clinical content, any risk screening and its outcome, escalations, and conversions — at the same standard as session documentation.

10. **Run verification.**

## Output Format

```
=== ASYNCHRONOUS MESSAGING THERAPY PROTOCOL ===
(Async messaging is NOT for emergencies. For a crisis: call 988, or 911 / nearest ED.)

PROGRAM CONTEXT
Platform: [Name] — BAA signed: [Y/N] — EHR-integrated: [Y/N]
Clinician availability model: [hours / days / coverage]
Population & acuity (async-eligible): [___]
Billing arrangement: [subscription / bundle / time-based digital E/M] [verify current payer rule]

────────────────────────────────────────────────────────
1. RESPONSE-WINDOW SLA
Committed turnaround: [e.g., within 1 business day]
Business hours: [___]  Evenings/weekends/holidays: [___]
Clinician absence coverage: [___]
Communicated in: onboarding + consent + platform footer.

────────────────────────────────────────────────────────
2. SCOPE
| Well-suited for | NOT appropriate for |
| [skills, reflection, psychoeducation, continuity, logistics] | [active risk, acute deterioration, complex assessment, time-sensitive change] |

────────────────────────────────────────────────────────
3. STRUCTURED MESSAGE FORMAT
Clinician reply: acknowledge → reflect/validate → respond → next step → restate availability/limits.
Client message guide: situation → what was tried → specific question/ask.

────────────────────────────────────────────────────────
4. CRISIS DETECTION IN TEXT
Watch for: SI/HI (explicit or implied), hopelessness, self-harm, threat to others, acute
deterioration, emergency-in-progress language.
Rule: any such signal → immediate human review + escalation; NEVER a routine async reply.
Automated flag (if any) → routes to clinician; does not decide.

────────────────────────────────────────────────────────
5. ESCALATION LADDER (routed to client's physical location)
| Signal | Tier | Action |
| Passive ideation, within scope | Clinician this week | Reply within SLA; assess; 988 standing |
| Active ideation/plan; deterioration | Clinician today — convert to synchronous | Live phone/video ASAP; C-SSRS; safety plan |
| Emergency / imminent danger | 911 / nearest ED + 988 | Direct to 911 or ED at client location; emergency contact |
Limit: async is not real-time → cannot reliably handle imminent risk.

────────────────────────────────────────────────────────
6. SESSION-EQUIVALENCE / BILLING
Mapping to billable unit: [time-based digital E/M / bundle / subscription]
Time tracking: [how] | Payer coverage: [verify current payer rule]

────────────────────────────────────────────────────────
7. BOUNDARIES / AVAILABILITY (client-facing)
"[Response within SLA; clinician not continuously monitoring; after-hours = not monitored;
 emergencies → 988 or 911/ED.]"

────────────────────────────────────────────────────────
8. CONVERSION CRITERIA (async → synchronous / in-person)
Any risk signal • rising acuity • needs real-time dialogue • repeated text misunderstanding • client request.

────────────────────────────────────────────────────────
9. DOCUMENTATION
Each exchange/summary: dates/times | clinical content | risk screen + outcome | escalations | conversions.
Standard equal to session documentation.
```

## Verification

- [ ] Response-window SLA is explicit, includes after-hours/weekend/holiday handling, and is communicated in onboarding, consent, and platform.
- [ ] The protocol states in multiple places that async is NOT for emergencies and always provides the emergency alternative (988 / 911-ED).
- [ ] Scope clearly separates async-appropriate uses from contraindicated uses (active risk, acute deterioration, complex assessment, time-sensitive change).
- [ ] Structured message format provided for both clinician replies and client messages.
- [ ] Crisis-detection-in-text step lists the signals and routes any signal to immediate human review, never a routine reply.
- [ ] Escalation ladder maps signals to clinician-this-week / today-convert-to-synchronous / 988 / 911-ED, routed to the client's physical location.
- [ ] Stated explicitly that, because async is not real-time, it cannot reliably detect/respond to imminent risk.
- [ ] Clinician retains decision authority; any automated flagging routes to a human and never auto-responds to or clears a risk signal.
- [ ] Session-equivalence/billing described with payer-variable specifics flagged `[verify current payer rule]`.
- [ ] Conversion criteria to synchronous/in-person care specified.
- [ ] Documentation standard equals session-level documentation, including risk screening and escalations.
- [ ] Missing inputs flagged with `[clinician input required]`.
```
