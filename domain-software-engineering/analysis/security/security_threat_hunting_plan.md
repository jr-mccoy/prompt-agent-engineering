---
title: "Threat Hunting Plan — Testable Hypotheses, Data Readiness, Bounded Hunts, and Graduating Findings into Detections"
category: analysis/security
description: "Plan a hypothesis-driven threat hunt in your own environment: turn a threat or gap into a falsifiable hypothesis, confirm the telemetry can actually answer it, bound the hunt in time and scope with a stop rule, record what was searched and cleared as well as what was found, and convert every result into a detection, a data-source fix, or an incident escalation."
techniques:
  - RT-05
  - RT-06
  - DP-13
  - QA-24
difficulty: advanced
tags:
  - threat-hunting
  - hypothesis-driven-hunt
  - mitre-attack
  - security-telemetry
  - log-analysis
  - detection-backlog
  - are-we-already-hacked
  - look-for-hidden-attackers
  - what-should-we-search-logs-for
updated: "2026-10-03"
related_prompts:
  - domain-software-engineering/analysis/security/security_detection_engineering_review.md
  - domain-software-engineering/analysis/security/security_stride_threat_modeling.md
  - domain-software-engineering/analysis/security/security_soc_alert_triage_runbook.md
---

# Threat Hunting Plan

**Objective:** Produce a hunt plan a security engineer can execute in a fixed time box —
hypothesis, data needed and its readiness, queries, what counts as a finding, when to stop,
and what each outcome turns into — so a hunt ends in a durable improvement rather than a
week of ad-hoc searching.

**When to Use:**
- A new threat report, vendor advisory, or peer incident describes behaviour your
  detections may not cover, and you want to know whether it already happened here.
- A detection review found priority techniques with no tested coverage.
- After an incident, to check whether the same actor left other footholds.
- You are starting a hunting practice and want each hunt to produce measurable output.
- **Not this prompt if** you are hunting for vulnerabilities in someone else's application
  for a bounty — that is offensive testing, see `domain-software-engineering/bug-bounty/bugbounty_access_control_idor_hunt.md`
  and its siblings. If an alert already fired, triage it with
  `security_soc_alert_triage_runbook.md`. If you need to rate existing rules rather than
  search for undetected activity, use `security_detection_engineering_review.md`. Designing
  threats for a system that is not built yet is `security_stride_threat_modeling.md`.

**Boundary:** Hunts run only on systems and logs your organisation owns or is authorised
to examine. Confirmed malicious activity stops the hunt and goes to incident response.

## Inputs / Context

1. **Trigger**: the threat report, gap, incident, or question that prompted the hunt.
2. **Environment**: identity provider, endpoints and OS mix, cloud accounts, network
   egress points, critical assets ("crown jewels").
3. **Telemetry inventory**: sources, fields, retention, coverage % of hosts/accounts, and
   query platform (SIEM, data lake, EDR console).
4. **Existing detections** for the relevant techniques and their test status.
5. **Time box and people**: analyst-days available, who can approve escalation.

## Method

1. **Choose the hunt type.** Frameworks such as PEAK (Prepare, Execute, Act with Knowledge)
   distinguish *hypothesis-driven* hunts (a specific behaviour), *baseline* hunts (what is
   normal, then outliers), and *model-assisted* hunts (statistical or ML scoring). Pick one;
   mixing them in one time box produces neither.
2. **Write a falsifiable hypothesis (RT-05).** Form: "An actor using [technique, ATT&CK id]
   would leave [observable] in [data source] on [scope] during [window]." Bad: "look for
   lateral movement." Good: "If an actor used stolen OAuth refresh tokens (T1550.001), we
   would see token use from an ASN never seen for that user in the last 90 days, without a
   preceding interactive sign-in."
3. **Check data readiness before querying.** For each observable, confirm the field exists,
   is populated, covers the scope (% of hosts or accounts), and is retained for the window.
   If coverage < 80% of the scope, the best outcome is "no evidence in the covered part" —
   say so up front, and log the gap as a finding in its own right.
4. **Design queries from cheap to expensive.** Start with a high-recall query and measure
   the result count; then narrow with correlating evidence (RT-06): a second, independent
   source that would also change if the hypothesis were true (e.g. sign-in log + mailbox
   rule creation + data egress volume). One source alone produces candidates, not findings.
5. **Define finding criteria and a stop rule (DP-13).** Before running: what makes a
   candidate *benign explained*, *suspicious — escalate*, or *confirmed malicious — stop and
   declare*. Stop when the time box ends, when the candidate list is exhausted, or
   immediately on confirmed malicious activity.
6. **Record searched-and-cleared (QA-24).** For every query: scope covered, rows reviewed,
   candidates, how each was cleared and by what evidence. "Found nothing" is only a result
   if the coverage behind it is written down.
7. **Convert outcomes.** Every hunt ends with at least one of: a new or improved detection
   (with the hunt query as its starting logic and the cleared benign cases as its known
   false positives), a telemetry fix, an incident ticket, or a documented "hypothesis not
   supported, coverage X%". Track hunts by this output, not by hours spent.

## Output Format

```
# Threat hunt plan — [name], [dates], time box [n analyst-days]
Trigger: [...] · Type: hypothesis / baseline / model-assisted · Approver for escalation: [...]

## Hypothesis
[actor + technique (ATT&CK id) → observable → data source → scope → window]

## Data readiness
| Observable | Source | Field(s) | Scope coverage | Retention | Ready? |

## Queries (cheap → expensive)
| # | Purpose | Source | Logic summary | Expected volume | Correlating source |

## Finding criteria
Benign explained: [...] · Suspicious → escalate: [...] · Confirmed → stop, declare: [...]
Stop rule: [...]

## Hunt log (filled during execution)
| Query | Scope covered | Rows reviewed | Candidates | Disposition + evidence |

## Outcomes
Detections to build: [...] · Telemetry fixes: [...] · Incidents raised: [...]
Hypothesis: supported / not supported in [x%] covered scope / untestable (why)
```

## Verification

- [ ] The hypothesis names a technique, an observable, a source, a scope, and a window.
- [ ] Data readiness was checked before any query; coverage % is stated.
- [ ] Finding criteria and the stop rule were written before execution.
- [ ] Each candidate disposition cites evidence from at least two sources or says why not.
- [ ] The hunt log shows scope covered for every "nothing found".
- [ ] Every hunt ends with a named output (detection, telemetry fix, incident, or documented null).

## False-Positive Prevention

1. **Absence of evidence on partial telemetry.** "No token replay found" on 55% of accounts
   is a coverage statement, not a clean bill of health.
2. **Rare = malicious.** Baseline hunts surface the unusual; most rare events are new
   employees, new vendors, or travel. Clear with a second source before escalating.
3. **Indicator hunting called threat hunting.** Sweeping for a published list of IPs or
   hashes is useful but catches only the exact tool; it does not test the technique.
4. **Unbounded hunts.** Without a stop rule, a hunt becomes a standing investigation that
   never produces a detection.
5. **Hunt results kept in a notebook.** A query that found something once and is not
   turned into a detection will not find it next time.
6. **Investigating confirmed compromise as a hunt.** The moment activity is confirmed
   malicious, incident response owns it; continuing to "hunt" delays containment.

## Example Output

```
# Threat hunt plan — OAuth refresh-token replay, 2026-10-06 → 10-08, time box 3 analyst-days
Trigger: peer SaaS company reported token theft via a compromised browser extension
Type: hypothesis-driven · Escalation approver: Head of Security Engineering

## Hypothesis
An actor holding stolen refresh tokens (T1550.001, T1528) would generate token redemptions
from an ASN not seen for that user in 90 days, with no interactive sign-in in the prior
12 h, across the 1,140 workforce accounts, between 2026-07-01 and today.

## Data readiness
| Token redemption events | IdP audit log | ip, asn, app_id, user | 100% accounts | 180 d | yes |
| Interactive sign-ins    | IdP sign-in log | user, mfa_result     | 100%          | 180 d | yes |
| Mailbox rule creation   | M365 audit      | user, rule params    | 100%          | 90 d  | yes |
| Browser extension list  | EDR inventory   | ext_id, host         | 72% laptops   | 30 d  | partial |

## Queries
| Q1 | redemptions from ASN unseen for user (90 d) | IdP audit | anti-join on user×asn history | ~400 | — |
| Q2 | Q1 ∩ no interactive sign-in in prior 12 h | IdP sign-in | join | ~40 | sign-in log |
| Q3 | Q2 users with new inbox rules or >2× mail export | M365 audit | join | <5 | mailbox audit |

## Finding criteria
Benign: ASN belongs to a known mobile carrier or the user's travel is on record.
Escalate: Q3 hit, or Q2 hit on an admin account. Confirmed: rule forwarding mail externally.
Stop: end of day 3, or any confirmed case.

## Hunt log (completed)
| Q1 | 1,140 accts | 412 events | 412 | 371 carrier ASNs → benign (ASN list) |
| Q2 | 41 events   | 41         | 9   | 7 travel (HR calendar), 2 open |
| Q3 | 2 users     | 2          | 0   | no rules, normal mail volume → benign |

## Outcomes
Detection: Q2 logic as rule D-219 (page only for admin accounts; others correlation-only);
known FPs = carrier ASNs, travel. Telemetry fix: extension inventory on remaining 28% of laptops.
Hypothesis not supported across 100% of accounts for token replay; extension vector
untestable on 28% of laptops.
```

## Techniques Used

- **RT-05 Evidence-Based Reasoning** — a falsifiable hypothesis with named observables and sources.
- **RT-06 Correlation and Cross-Analysis** — candidates become findings only with a second, independent source.
- **DP-13 Kill Signal Definition** — finding criteria and a stop rule written before the hunt runs.
- **QA-24 Dismissed-Candidates Coverage Table** — the hunt log records scope covered and how each candidate was cleared.

## Related Prompts

- `security_detection_engineering_review.md` — where hunt queries become tested, owned detections.
- `security_stride_threat_modeling.md` — a source of hypotheses for systems you built.
- `security_soc_alert_triage_runbook.md` — the triage path for the detections a hunt produces.
