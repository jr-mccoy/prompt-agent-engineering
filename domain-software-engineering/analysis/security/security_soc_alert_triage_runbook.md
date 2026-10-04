---
title: "SOC Alert Triage Runbook Design — Per-Detection Runbooks, Dispositions, Escalation, and Queue Health for an Engineering-Run Security On-Call"
category: analysis/security
description: "Design the triage layer for a security operations function staffed by engineers on rotation: a runbook template every detection must link to, a fixed disposition vocabulary, severity-based acknowledgement and triage clocks, an escalation hand-off into incident response, automated enrichment that saves analyst minutes, and queue-health metrics that feed tuning back to detection owners."
techniques:
  - RT-10
  - DS-06
  - DS-36
  - AG-12
  - QA-12
difficulty: intermediate
tags:
  - soc
  - alert-triage
  - security-on-call
  - runbook
  - incident-escalation
  - alert-enrichment
  - security-alerts-piling-up
  - who-handles-security-alerts
  - on-call-for-security
updated: "2026-10-03"
related_prompts:
  - domain-risk/risk_security_alert_triage_runbook.md
  - domain-AI-ML/agentic-ai-systems/aiagent_secops_autonomous_defense.md
  - domain-software-engineering/analysis/security/security_detection_engineering_review.md
---

# SOC Alert Triage Runbook Design

**Objective:** Give an engineering-run security on-call a consistent way to take any alert
from "fired" to one of four dispositions within a stated clock — with a runbook per
detection, a clean hand-off to incident response, and queue metrics that tell detection
owners what to fix.

**When to Use:**
- Security engineers share an on-call rotation (often alongside build work) and each one
  triages the same alert differently.
- Alerts arrive with no context, so every triage starts with ten minutes of lookups.
- Escalations to incident response arrive missing the facts needed to act.
- You are writing the runbook standard that a detection-as-code repository will enforce.
- **Not this prompt if** your team has no security engineers and alerts land with an office
  manager or IT generalist — use `domain-risk/risk_security_alert_triage_runbook.md`, which
  is deliberately manual and symptom-based for non-specialists. If you are putting a model
  or agentic SOAR at the front of the queue, use
  `domain-AI-ML/agentic-ai-systems/aiagent_secops_autonomous_defense.md`. If the problem is
  the rules themselves (noise, gaps), fix them first with
  `security_detection_engineering_review.md`. Once an incident is declared, the incident
  commander process in `domain-agentic-resources/agents/devops/incident_responder.md` takes over.

## Inputs / Context

1. **Detections in scope** and their owners; whether they live in a repository.
2. **Alert volume** by detection and severity, by hour of day, over 30–90 days.
3. **On-call model**: rotation size, hours covered, follow-the-sun or pager, other duties.
4. **Tooling**: SIEM/EDR consoles, case management, chat-ops, SOAR or scripting available
   for enrichment, identity and asset lookups.
5. **Incident response interface**: who declares, paging path, severity scheme.
6. **Authority**: which containment actions on-call may take alone (disable user, isolate
   host, revoke tokens) and which need approval.

## Method

1. **Fix the disposition vocabulary.** Every alert closes as exactly one of: *true positive
   — malicious* (escalate), *true positive — benign* (expected activity; tuning signal),
   *false positive* (logic fired on the wrong thing; tuning signal), *undetermined* (could
   not decide; requires a second look within 24 h and counts against the detection).
2. **Set clocks by severity (DS-06).** Example: Critical — acknowledge 5 min, triage
   decision 30 min, 24×7 paging; High — 15 min / 2 h, paging in hours, next-morning queue
   overnight with a stated risk acceptance; Medium/Low — business-day queue, 1 day.
   Check the clocks against volume: alerts/shift × median handle time must fit inside
   ~50% of an engineer's shift if they also carry build work.
3. **Write the runbook template (RT-10).** Every detection links to one, kept next to the
   rule. Sections: *what fired and why it matters* (one paragraph, ATT&CK id); *auto-enriched
   context* (what the alert payload already contains); *decision checks* (3–6 ordered
   questions, each with the query or console link and the answer that branches);
   *known benign patterns* (with examples); *containment allowed at this step*;
   *escalate when*; *close notes required*. "Can't determine" at any check routes to
   escalation or undetermined, never to false positive.
4. **Automate enrichment, not decisions.** Pre-attach to the alert: asset owner and
   criticality, user's role and manager, recent sign-ins, related alerts on the same entity
   in 7 days, geo/ASN for IPs, file reputation. Measure each enrichment's saving in handle
   time; drop ones nobody reads.
5. **Fix the escalation hand-off (DS-36).** A fixed block: entity(ies), timeline of what was
   observed (UTC), checks run and results, containment already taken, what is unknown,
   recommended severity. The incident commander should be able to act without a call-back.
6. **Queue-health metrics (AG-12).** Per detection and overall: mean time to acknowledge,
   time to disposition, % undetermined, % TP-benign, % FP, escalation rate, alerts per
   on-call shift, after-hours pages per week. Thresholds trigger work for the detection
   owner, e.g. FP + TP-benign > 80% over 30 days with > 10 alerts → tuning ticket.
7. **Close the loop with detection owners (QA-12).** Weekly 30-minute review: top 5
   detections by on-call minutes consumed, every undetermined, every escalation that
   turned out benign and every incident first found by something other than an alert.

## Output Format

```
# Security triage design — [team], [date]
Rotation: [...] · Hours: [...] · Paging: [...] · Containment authority: [...]

## Disposition vocabulary (with definitions)
## Severity clocks
| Severity | Ack | Disposition | Hours | Paging | Capacity check |

## Runbook template
[sections with one-line guidance each]

## Worked runbook — [one high-volume detection]
## Enrichment spec
| Field | Source | Added at | Minutes saved (est.) |

## Escalation block (fixed fields)
## Queue-health metrics and thresholds
| Metric | Threshold | Triggered action | Owner |

## Weekly tuning review agenda
## Gaps and assumptions
```

## Verification

- [ ] Four dispositions only; "undetermined" has a follow-up clock and counts against the rule.
- [ ] Severity clocks are checked against measured volume and handle time.
- [ ] Every runbook check has a link or query and an explicit branch for "can't determine".
- [ ] Containment allowed without approval is listed per runbook.
- [ ] The escalation block lists unknowns explicitly.
- [ ] Every metric threshold maps to an action and an owner.

## False-Positive Prevention

1. **TP-benign merged into false positive.** They need different fixes (allow-list the
   expected actor vs. rewrite the logic); merging them hides which.
2. **"Can't determine" closed as FP.** The most common path from a real intrusion to a
   closed ticket. It must escalate or stay open as undetermined.
3. **Runbooks written per alert name, not per decision.** A wall of background text is not a
   runbook; the ordered checks with branches are.
4. **Enrichment that decides.** Auto-closing on "known IP" or "user on VPN" turns an
   attacker on the VPN into a closed alert; enrich, then let a check decide.
5. **Clocks the rotation cannot meet.** A 30-minute triage SLA on 400 alerts/day for one
   engineer guarantees silent breaches; fix volume or staffing, not the number in the doc.
6. **Measuring speed alone.** Fast acknowledgement with rising undetermined rates is worse
   triage, not better.

## Example Output

```
# Security triage design — Ferrovia Payments Security Eng (9 engineers), 2026-10-01
Rotation: 1 primary + 1 secondary weekly · Hours: 24×7 pager for Critical, 08–20 UTC queue
Containment authority: on-call may disable a workforce user, revoke sessions, isolate a laptop;
production host isolation and customer-account actions require the IC.

## Severity clocks
| Critical | 5 min  | 30 min | 24×7  | page | 0.6/day × 25 min = 15 min/day ✓ |
| High     | 15 min | 2 h    | 08–20 | chat | 7/day × 12 min = 84 min/day ✓ |
| Med/Low  | 1 day  | 1 day  | 08–20 | queue | 46/day × 4 min = 184 min/day ✗ (> 50% of 7 h shift with build work) → tune top 3 rules |

## Worked runbook — D-044 "New long-lived cloud access key created"
What fired: an IAM user access key created outside the provisioning pipeline (T1098.001).
Auto-enriched: creator principal, source IP/ASN, MFA state, owner of target user, CI run id if any.
Checks:
 1. Is there a CI run id or change ticket? → yes, matches pipeline service account: TP-benign, close.
    → no: go to 2.
 2. Creator signed in with MFA from a known corporate ASN in last 12 h? → no or can't tell: escalate (High).
 3. Ask creator in a call/huddle (not by the account's own chat) whether they created it.
    → confirmed and justified: TP-benign, ticket to move to role-based access.
    → denied or no answer in 30 min: disable key, escalate.
Close notes required: creator, justification link, key id.

## Escalation block
Entities · UTC timeline · checks + results · containment done · unknowns · recommended severity

## Queue-health (Sept)
MTTA Critical 3.8 min · undetermined 6% (target ≤ 3%) · D-131 Encoded PowerShell:
190 alerts, 97% FP + TP-benign, 11 on-call hours → tuning ticket to owner (EDR team).
```

## Techniques Used

- **RT-10 Troubleshooting Decision Tree** — ordered checks with explicit branches, including "can't determine".
- **DS-06 Prioritization and Severity Guidance** — severity clocks checked against capacity.
- **DS-36 Blocker Escalation Framework** — the fixed escalation block into incident response.
- **AG-12 Quantitative Success Metrics** — queue-health metrics with thresholds that trigger owner work.
- **QA-12 False Positives Identification** — separating TP-benign from FP and routing each to the right fix.

## Related Prompts

- `domain-risk/risk_security_alert_triage_runbook.md` — the manual, symptom-based version for teams without security engineers.
- `domain-AI-ML/agentic-ai-systems/aiagent_secops_autonomous_defense.md` — adding model-assisted triage once this layer is stable.
- `security_detection_engineering_review.md` — fixing the detections that the queue metrics flag.
