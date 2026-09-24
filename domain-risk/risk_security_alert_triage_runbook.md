---
title: "Security Alert Triage Runbook — Human-Run Steps for a Small Team Deciding Noise, Watch, or Incident"
category: risk
description: "Write the manual triage runbook a two-to-five-person team without a SOC uses on the alerts and reports it actually receives — staff phishing reports, sign-in and MFA warnings, antivirus/endpoint detections, vendor breach notices, 'my account is sending spam' — organised by what the person sees, with a severity ladder, a fixed decision of close / watch / escalate to incident, a named on-duty owner, and a weekly tuning review; distinct from `domain-AI-ML/agentic-ai-systems/aiagent_secops_autonomous_defense.md` (designing automated SOC triage) and `domain-software-engineering/devops/monitoring_solo_dev_alerting.md` (application uptime alerts)."
techniques:
  - IT-23
  - RT-10
  - DS-06
  - DS-36
  - QA-12
difficulty: intermediate
tags:
  - alert-triage
  - security-operations
  - runbook
  - small-team
  - escalation
  - phishing-reports
updated: "2026-09-24"
reasoning:
  styles: [diagnostic, procedural, abductive, protective]
  stakes: variable
  horizon: hours
  uncertainty: ambiguity
  evidence_quality: sparse
  domain_complexity: single_domain
  collaboration: small_team
  output_format: structured
  user_role: [operator, office-manager, it-generalist, team-lead]
  mode: [diagnose, triage, document]
related_prompts:
  - domain-AI-ML/agentic-ai-systems/aiagent_secops_autonomous_defense.md
  - domain-risk/risk_security_incident_response_playbook.md
  - domain-software-engineering/devops/monitoring_solo_dev_alerting.md
---

# Security Alert Triage Runbook

**Objective:** Give the person on duty a one-page-per-symptom runbook that gets every
security alert or report to one of three outcomes — **close**, **watch**, or **escalate to
incident** — within a stated time, using only checks they are able and authorised to do.

**When to Use:**
- Security emails (sign-in warnings, "new device", antivirus detections, vendor notices)
  land in a shared inbox and nobody knows which matter.
- Staff report suspicious messages and the reports sit unread.
- An MSP forwards alerts to you and expects you to decide.
- `risk_phishing_awareness_program.md` is live and the report volume needs a handling path.

**Not this prompt if:**
- You are designing automated or AI-assisted triage, SOAR playbooks or a SOC —
  `domain-AI-ML/agentic-ai-systems/aiagent_secops_autonomous_defense.md`. This runbook is
  deliberately human-run with no automation design.
- The alerts are about application uptime and latency — `domain-software-engineering/devops/monitoring_solo_dev_alerting.md`.
- It is already an incident — go straight to `risk_security_incident_response_playbook.md`.

**Boundary:** Checks use only the organisation's own admin consoles, logs and staff. Never
click suspicious links or open attachments to "see what happens", never investigate outside
systems, and never contact a suspected attacker.

## Inputs / Context

1. **Alert sources in use:** email/identity provider security alerts, endpoint protection,
   backup job reports, bank fraud alerts, vendor notices, staff reports, MSP tickets.
2. **Monthly volume per source** (rough) and how many are later judged real.
3. **Who is on duty**, their admin rights, and working hours coverage.
4. **Who to escalate to:** MSP, incident lead, insurer hotline (from the IR playbook).
5. **Recent examples** of alerts — real and false — with what actually happened.

## Method

1. **Organise by symptom, not by threat (IT-23).** The person on duty sees "a sign-in from
   another country", not "credential stuffing". One card per symptom:
   - Staff report of suspicious email
   - Unusual sign-in / MFA prompt the user did not trigger
   - Endpoint/antivirus detection
   - Account sending mail the user did not write
   - Vendor or bank notice of a problem on their side
   - Backup job failed or files suddenly renamed/unreadable

2. **Write each card as a short decision tree (RT-10).** Symptom → two to four checks the
   duty person can actually do → outcome. Example checks: "Did the user do this? (call them,
   do not email)", "Is the same sign-in seen for other users?", "Did the detection say
   *blocked* or *allowed*?". Any "don't know" at a check routes one step up, not down.

3. **Define the severity ladder and clocks (DS-06).**

   | Severity | Meaning | Triage within | Outcome options |
   |---|---|---|---|
   | S1 | Possible active compromise, money or data moving | 15 min | Escalate to incident |
   | S2 | Credible single-account or single-device concern | 2 working hours | Contain + watch, or escalate |
   | S3 | Likely noise, no sign of success | 1 working day | Close with note |

   Automatic S1 triggers regardless of checks: files being encrypted/renamed, a payment or
   bank-detail change linked to the alert, an admin account involved, the user reports they
   entered a password or approved a prompt.

4. **Fix the escalation format (DS-36).** When escalating: what was seen, when, which account
   or device, what checks were done and their results, what has already been contained, who
   has been told. Same five lines every time, so the MSP or incident lead can act without a call-back.

5. **Record every alert in one log** — source, symptom card, severity, outcome, time taken,
   who. The log is what makes tuning possible.

6. **Weekly 20-minute tuning review.** Which alert types were always noise (ask the MSP or
   provider to adjust, do not just ignore), which were slow, and whether any S3 closure later
   turned out to be real. Reporters of real catches get thanked by name if they agree.

## Output Format

```
# Security alert triage runbook — [organisation], [date]
On duty: [role/rota] · Hours covered: [...] · Out of hours: [route]
Escalate to: [MSP line] → [incident lead] → [insurer hotline per IR playbook]

## Severity ladder
| S | Meaning | Triage within | Outcomes | Automatic triggers |

## Symptom cards  (one per symptom)
### [Symptom]
Checks:
 1. [check] → yes: ... / no: ... / don't know: go up one level
Outcome: close / watch (until ..., re-check ...) / escalate
Never: [action to avoid]

## Escalation message (five lines)
## Alert log columns
## Weekly tuning review agenda
## Confidence notes: which cards are untested
```

## Verification

- [ ] Every card starts from what the duty person observes.
- [ ] Every check is something the duty person can do with their actual access.
- [ ] "Don't know" always routes up, never to close.
- [ ] Automatic S1 triggers are listed and override the checks.
- [ ] Every outcome is one of close / watch / escalate; "watch" has an end date.
- [ ] The escalation message has the same five fields every time.
- [ ] No step involves opening the suspicious item or contacting the sender.
- [ ] No automation or tooling design has crept in.

## False-Positive Prevention

1. **Threat-named cards.** "Credential stuffing" helps nobody at 16:55; "sign-in from
   somewhere unexpected" does.
2. **Closing on uncertainty.** A missing answer at a check is the most common route from a
   real compromise to a closed ticket.
3. **Checking with the user by email.** If the account is compromised, the attacker answers.
   Call or ask in person.
4. **"Blocked" read as "safe".** A blocked detection may be one of several attempts; check
   whether the same file or sender reached other devices.
5. **Ignoring noisy sources instead of tuning them.** Alert fatigue ends in a missed S1.
   Fix the source with the provider.
6. **Indefinite "watch".** Watch without an end date is a silent close.
7. **Investigating like a SOC.** Detailed forensics are out of scope; the runbook's job is a
   fast, correct routing decision.

## Example Output

```
# Security alert triage runbook — Kestrel Logistics (60 staff), 2026-09
On duty: Office Manager (Mon–Fri 08–18), IT Coordinator backup · Out of hours: MSP 24h line
Escalate to: MSP (TriPoint) → Ops Director (IR lead) → insurer hotline

### Unusual sign-in / MFA prompt the user did not trigger
Checks:
 1. Call the user: did they sign in or approve a prompt?
    → they approved a prompt they didn't start: S1, escalate now
    → no, and they did not approve: go to 2
    → can't reach them in 15 min: treat as S2, go to 2
 2. In the identity console, are there successful sign-ins from the same location for other users?
    → yes: S1, escalate · → no: go to 3 · → can't tell: S2, ask MSP
 3. Reset the user's password and sign out all sessions (Office Manager has this right).
Outcome: watch 7 days — re-check sign-in log on [date]; close if clean.
Never: ask the user "was this you?" by email or chat.

## Alert log (week 38 excerpt)
| Mon 09:12 | identity alert | Unusual sign-in | S2 | reset, watch to 09-29 | 25 min | OM |
| Tue 14:40 | staff report | Suspicious email | S3 | closed: sim campaign | 5 min | OM |
| Thu 11:05 | endpoint | Detection "allowed" | S1 | escalated to TriPoint 11:12 | 7 min | IT Coord |

## Tuning (week 38): 11 "new device" alerts from warehouse tablets = noise → ask TriPoint to
exclude managed tablets; Thursday S1 turned out benign but correctly escalated (checks said "allowed").
## Confidence: backup-failure card untested — schedule in next tabletop.
```

## Techniques Used

- **IT-23 Symptom-Based Troubleshooting Organization** — one card per thing the duty person sees.
- **RT-10 Troubleshooting Decision Tree** — check → branch → outcome, with "don't know" routed up.
- **DS-06 Prioritization and Severity Guidance** — S1–S3 ladder with clocks and automatic triggers.
- **DS-36 Blocker Escalation Framework** — the fixed five-line escalation message.
- **QA-12 False Positives Identification** — what not to conclude from "blocked" or silence.

## Related Prompts

- `risk_security_incident_response_playbook.md` — where S1 escalations go.
- `risk_phishing_awareness_program.md` — the source of most staff reports.
- `risk_tabletop_exercise_designer.md` — to exercise untested cards.
- `../domain-AI-ML/agentic-ai-systems/aiagent_secops_autonomous_defense.md` — automated triage design, out of scope here.
