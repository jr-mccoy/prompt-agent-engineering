---
title: "Security Incident Response Playbook — Ransomware, Email Compromise, Lost Devices, and Data Exposure for an Organisation Without a SOC"
category: risk
description: "Write the human-run response playbook a small or mid-sized organisation without a security operations centre follows in the first hour, day and week of four common incidents — ransomware, business email compromise, a lost or stolen device, and accidental data exposure — with decision authority, evidence preservation, outside help lined up in advance, and every legal notification clock routed to counsel rather than asserted; distinct from the technical SRE agent in `domain-agentic-resources/agents/devops/incident_responder.md` and the ML-failure runbook in `domain-AI-ML/production-monitoring/mlmonitor_ml_incident_response.md`."
techniques:
  - ST-02
  - AG-19
  - OC-09
  - QA-04
  - OC-03
difficulty: intermediate
tags:
  - incident-response
  - ransomware
  - business-email-compromise
  - data-breach
  - small-business
  - security-operations
updated: "2026-09-24"
reasoning:
  styles: [procedural, protective, systems, causal]
  stakes: high
  horizon: hours_to_days
  uncertainty: ambiguity
  evidence_quality: sparse
  domain_complexity: regulated
  collaboration: small_team
  output_format: structured
  user_role: [operator, founder, executive, office-manager]
  mode: [plan, respond, document]
related_prompts:
  - domain-risk/risk_business_continuity_plan.md
  - domain-risk/risk_after_action_review.md
  - domain-agentic-resources/agents/devops/incident_responder.md
---

# Security Incident Response Playbook

**Objective:** Produce a playbook a non-specialist can execute under stress for the four
incidents a small organisation most often meets — who decides, what to do in the first
hour, day and week, what not to touch, whom to call, and which questions go to counsel —
written *before* the incident, and honest about what the organisation cannot do itself.

**When to Use:**
- You run operations, finance or IT-by-default at an organisation with no security team,
  and "what do we do if we get hit?" has no written answer.
- An insurer, client or auditor has asked for an incident response plan.
- A near-miss (a spoofed invoice, a laptop left on a train) showed nobody knew who decides.

**Not this prompt if:**
- A production system is down and engineers need an incident commander — distinct from
  `domain-agentic-resources/agents/devops/incident_responder.md` (SRE, observability).
- The failure is a model or ML pipeline — `domain-AI-ML/production-monitoring/mlmonitor_ml_incident_response.md`.
- You need to keep the business running through *any* loss — `risk_business_continuity_plan.md`
  owns recovery objectives; this playbook plugs into its "loss of systems or data" section.
- You need to decide what an alert means before it becomes an incident — `risk_security_alert_triage_runbook.md`.
- The incident is over and you want to learn from it — `risk_after_action_review.md`.

**Boundary (non-negotiable):** Defensive and procedural only. No offensive tooling, no
"hack back", no instructions to access systems you do not own. **Legal notification
obligations** — to regulators, affected individuals, customers under contract, insurers —
vary by jurisdiction, sector and contract and change over time. This prompt never states a
deadline from memory; it records "[notification clock — confirm with counsel]" and names
who calls counsel, when.

## Inputs / Context

1. **Organisation shape:** headcount, locations, sector, whether you hold personal, payment
   or health data.
2. **Who does IT:** an employee, an outsourced managed service provider (MSP), or nobody.
3. **Core systems:** email/identity provider, file storage, finance/banking, line-of-business
   apps, endpoints (laptops, phones), backups and where they live.
4. **Outside help already contracted:** cyber insurance (and its required panel vendors and
   hotline), MSP, outside counsel, forensic firm, bank relationship manager.
5. **Decision-makers:** who can authorise spend, shut systems down, talk to clients or press.
6. **Past incidents or near-misses**, including ones that were "nothing in the end".

If insurance exists, ask for the policy's incident-reporting conditions — many policies
require notifying the insurer first and using panel vendors; engaging your own firm first
can jeopardise cover. Record this as a question for the broker, not a fact.

## Method

1. **Name the roles, two deep (ST-02).** Incident lead, decision authority (spend and
   shutdown), communications, record-keeper, and "caller of counsel and insurer". Roles,
   not names; current holders in an appendix. Succession two deep, because the person who
   clicked the link may be the incident lead.

2. **Write the universal first hour (AG-19).** The same for every incident type:
   - Stop the spread without destroying evidence: disconnect affected devices from the
     network (unplug or disable Wi-Fi) — **do not power off or wipe**, which destroys
     volatile evidence a forensic firm may need.
   - Open the incident log (time-stamped, on paper or an out-of-band device).
   - Call the insurer hotline and/or MSP per the policy order established in Inputs.
   - Switch to an out-of-band channel (phone tree, personal numbers) if email or chat
     may be compromised.
   - Decide who is told internally, and who is **not** told yet.

3. **Write one module per incident type**, each with first-hour / first-day / first-week
   windows:

   | Incident | First-hour signature actions | Common own-goal to prohibit |
   |---|---|---|
   | Ransomware | Isolate hosts; protect backups from being connected; photograph ransom note | Paying or negotiating without counsel and insurer; restoring over evidence |
   | Business email compromise | Reset the account's password and sessions via the identity provider; check forwarding rules; call bank if money moved | Emailing the attacker-controlled thread to warn people |
   | Lost/stolen device | Remote lock/wipe **after** recording what data was on it; revoke sessions | Assuming "it was encrypted" without checking |
   | Data exposure (misaddressed email, public link) | Revoke the link / recall; record who could have accessed what, and when | Deleting access logs while "cleaning up" |

4. **Mark every action the organisation cannot do itself (OC-09).** For each step, a
   "Can we do this in-house?" column: yes / only with MSP / only with forensic firm. A
   playbook that assumes skills the organisation lacks will stall at that step.

5. **Route legal and notification questions (QA-04).** A standing table: question, who
   asks it (role), to whom (counsel, insurer, regulator via counsel), trigger to ask. Every
   deadline cell reads "[confirm with counsel]". Separate *facts to preserve for counsel*
   (what data, whose, how many, when discovered) from *conclusions* (whether it is a
   "breach" in the legal sense), which only counsel draws.

6. **Pre-draft the first messages** — staff, clients, bank — as templates with blanks and a
   "counsel reviewed: [ ]" box. No external message leaves before that box is ticked.

7. **Define stand-down and handoff.** Who declares the incident closed, what must be true,
   and the handoff to `risk_after_action_review.md` within two weeks.

8. **Walk it through once.** Take the most likely incident and read the
   module aloud with the roles present; record every step that stalled.

## Output Format

```
# Security incident response playbook — [organisation], [date]
Owner: [role] · Held offline at: [location] · Next walkthrough: [date]

## Roles (two deep)
| Role | Primary | Second | Third | Authority |

## Outside help (numbers held offline)
| Party | Contact route | Contracted? | Must be called first? [confirm with broker] |

## Universal first hour
1. ... (numbered, imperative, one action per line)

## Module: [incident type]  (repeat ×4)
| Window | Step | Role | In-house? | Evidence to preserve | Never do |

## Legal & notification routing
| Question | Asked by | Asked of | Trigger | Deadline |
(every deadline cell: [confirm with counsel])

## Message templates  (counsel reviewed: [ ])
## Stand-down criteria and AAR handoff
## Walkthrough log: stalls found, fixes owed, owner, date
## Confidence: High / Medium / Low per module, with reason
```

## Verification

- [ ] Every role has a second and third; the incident lead is not a single person.
- [ ] Each module has first-hour, first-day and first-week windows.
- [ ] No step says "power off" or "wipe" before evidence preservation is decided.
- [ ] Every step is marked in-house / MSP / forensic firm.
- [ ] No notification deadline, regulator name or threshold is stated as fact.
- [ ] The insurer-first question is recorded for the broker, not assumed.
- [ ] External message templates require counsel review before sending.
- [ ] The playbook and contact list are available if email and file storage are down.
- [ ] One module has been walked through and the stalls recorded.

## False-Positive Prevention

1. **Asserting a notification deadline.** "You have 72 hours" is the most dangerous
   sentence in an incident plan: it may be wrong for this jurisdiction, sector or contract,
   and it anchors every later decision. Write "[confirm with counsel]" every time.
2. **"Turn it off" instinct.** Powering down destroys memory-resident evidence and can
   break decryption options. Disconnect from the network; leave power decisions to the
   forensic firm.
3. **Warning people through the compromised channel.** In BEC the attacker reads the
   mailbox. Move to phone or an out-of-band channel first.
4. **Engaging a vendor before the insurer.** Some policies restrict cover to panel vendors.
   Treat this as a question to settle in peacetime.
5. **A playbook written for a SOC you do not have.** Steps like "review EDR telemetry" are
   noise if nobody can do them. The in-house column exposes this.
6. **Calling it a "breach" in writing.** That is a legal characterisation. Record facts;
   let counsel choose words.
7. **Drifting into offence.** Tracing, "counter-phishing" or accessing the attacker's
   infrastructure is out of scope and potentially unlawful. The playbook is defence,
   preservation and escalation.

## Example Output

```
# Security incident response playbook — Harbour Dental Group (14 staff, 2 sites), 2026-09
Owner: Practice Manager · Held offline at: printed binder, both reception safes

## Roles
| Role | Primary | Second | Third | Authority |
| Incident lead | Practice Manager | Senior Dentist | Office Admin | Isolate devices, call MSP |
| Decision authority | Senior Dentist | Partner B | — (gap, see log) | Spend ≤ [limit], shutdown |
| Caller of counsel/insurer | Office Admin | Practice Manager | Senior Dentist | Notify only |

## Outside help
| Insurer hotline | on policy schedule, p.3 | Yes | Possibly — [confirm with broker] |
| MSP (BrightDesk IT) | 24h line | Yes | After insurer |
| Outside counsel | [to be retained] | No | Gap — see log |

## Module: Business email compromise
| First hour | Reset Office Admin mailbox + revoke sessions | MSP | MSP only | Export forwarding rules before deleting | Reply on the thread |
| First hour | Call bank if a payment left today | Senior Dentist | Yes | Payment reference, time | Wait for "confirmation" email |
| First day | List patients/suppliers emailed from the account | Incident lead | Yes | Sent-items export | Delete sent items |
| First week | Counsel decides whether patient data was accessed | Caller of counsel | No | Access log from MSP | Tell patients before counsel |

## Legal & notification routing
| Did health data leave our control? | Caller of counsel | Counsel | Any access to patient records | [confirm with counsel] |

## Walkthrough log
BEC module walked 2026-09-18: stalled at "revoke sessions" — nobody but MSP holds admin.
Fix: second admin credential in sealed envelope, owner Practice Manager, due 2026-10-01.
Decision authority has no third — owner Senior Dentist, due 2026-10-15.

## Confidence
BEC: Medium (walked once) · Ransomware: Low (never walked; backups untested — see BCP gap list)
```

## Techniques Used

- **ST-02 Structured Sequential Instructions** — numbered, one-action steps for a stressed reader.
- **AG-19 Time-Critical Response Protocol** — first-hour / day / week windows per module.
- **OC-09 Capability Boundary Specification** — the in-house / MSP / forensic column.
- **QA-04 Uncertainty Acknowledgment** — deadlines and legal characterisations marked for counsel.
- **OC-03 Markdown Table Specification** — module, role and routing tables.

## Related Prompts

- `risk_business_continuity_plan.md` — recovery objectives and the backup-restore test this playbook depends on.
- `risk_after_action_review.md` — the blameless review after stand-down.
- `risk_security_alert_triage_runbook.md` — deciding whether an alert is an incident.
- `risk_payment_fraud_bec_controls.md` — the preventive controls that make BEC losses rarer.
- `../domain-agentic-resources/agents/devops/incident_responder.md` — technical SRE incident command.
