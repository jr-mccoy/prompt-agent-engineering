---
title: "Risk Acceptance and Exception Memo — Accepting a Risk on Purpose, With an Owner, an Expiry, and Tripwires"
category: risk/acceptance
description: "Write the formal record that turns an unmitigated risk or a policy exception into a deliberate, time-limited decision: what exactly is being accepted and against which policy or appetite limit, inherent and residual rating, compensating controls with their own owners and checks, the alternatives rejected and their cost, the approver whose authority matches the residual rating, a hard expiry, and revisit triggers that void the acceptance early; distinct from `domain-risk/risk_appetite_statement.md` (sets the limits in advance) and `domain-risk/risk_register_builder.md` (catalogues risks and mitigations)."
techniques:
  - CM-09
  - GT-05
  - QA-09
  - RT-05
  - QA-12
difficulty: intermediate
tags:
  - risk-acceptance
  - policy-exception
  - compensating-controls
  - governance
  - decision-record
  - accountability
  - cant-fix-yet
  - get-sign-off
  - temporary-workaround
updated: "2026-09-24"
reasoning:
  styles: [evaluative, structural, evidential]
  stakes: variable
  horizon: months
  uncertainty: risk
  evidence_quality: moderate
  domain_complexity: cross_domain
  collaboration: small_team
  output_format: structured_memo
  user_role: [risk-lead, operator, executive, it-lead, compliance]
  mode: [decide, document]
related_prompts:
  - domain-risk/risk_appetite_statement.md
  - domain-risk/risk_register_builder.md
  - domain-risk/risk_key_risk_indicators.md
---

# Risk Acceptance and Exception Memo

**Objective:** Make accepting a risk a decision someone signed rather than a gap everyone
forgot. The memo states precisely what is accepted, why fixing it now is worse, what
partially covers it meanwhile, who with the right authority approved it, when it expires,
and what events cancel it early.

**When to Use:**
- A register entry sits above appetite and the mitigation is too costly, too slow, or not yet possible.
- Someone needs an exception to a standard: an unsupported system kept running, a supplier
  used before due diligence finishes, a control skipped for a deadline.
- An auditor finds a known gap and asks who decided to live with it.
- A pile of "temporary" exceptions has no expiry dates and nobody knows which are still needed.

**Not this prompt if:**
- You are setting how much risk the organisation will tolerate in general — `domain-risk/risk_appetite_statement.md`.
- You are still identifying or scoring the risk — `domain-risk/risk_register_builder.md`.
- The accepted risk is a vendor-security residual inside a questionnaire review — record it
  there (`risk_vendor_security_questionnaire_review.md`) unless it breaches appetite, then use this memo.
- The question is legal liability or regulatory permission — route to counsel; this memo records
  a business decision and does not make a legal one.

## Inputs / Context

1. **The risk or exception:** what is not being done, and which policy, standard or appetite limit it departs from.
2. **Current rating:** likelihood and impact from the register, or enough to score them.
3. **Options considered:** fix now, fix later, transfer (insurance, contract), avoid (stop the activity) — with cost and time for each.
4. **Controls available in the meantime** and who would run them.
5. **Authority matrix:** who may accept which level of residual risk (from the appetite statement or delegations).
6. **External obligations** that might forbid acceptance (contract, insurer condition, regulator), as stated in those documents.

## Method

1. **State the acceptance precisely.** One sentence naming the asset or activity, the policy
   clause or limit departed from, and the scope boundary. "Keep workstation TX-04 on Windows 10
   past end of support for the tax application only" — not "accept legacy IT risk".

2. **Rate inherent and residual on the register's scales.** Inherent without the compensating
   controls; residual with them. Show the appetite limit alongside.

3. **Specify compensating controls as if they were the primary control (RT-05).** Each has an
   owner, a check (how you will know it is working) and a check frequency. A compensating
   control with no check is an assumption.

4. **Show the alternatives and why they lose.** Cost and time to remediate, transfer or avoid.
   Acceptance is justified only if it is better than these for the stated period.

5. **Match approver to residual rating (CM-09).** Use the authority matrix. The requester
   cannot approve their own exception; if residual exceeds appetite, approval sits above the
   risk owner's line.

6. **Set a hard expiry (QA-09).** A date, not "until fixed". Renewal requires a new memo with
   evidence the compensating controls held. State how reversible the position is: what it would
   take to end the exception early.

7. **Define revisit triggers (GT-05).** Events that void the acceptance before expiry: a control
   check fails, the threat changes, scope creeps, a remediation becomes available, an
   obligation changes. Each trigger names who watches for it.

8. **Log and link.** Record the memo ID on the register entry; add trigger events to the KRI set
   if they are measurable.

## Output Format

```
# Risk acceptance / exception memo — [ID]
Requested by: [role] · Risk owner: [role] · Date: [date]

## What is accepted
[one sentence: asset/activity, policy clause or appetite limit departed from, scope boundary]

## Rating
Inherent: L[ ] × I[ ] = [ ] · Residual with controls: L[ ] × I[ ] = [ ] · Appetite limit: [ ]

## Compensating controls
| Control | Owner | Check (evidence it works) | Frequency |

## Alternatives considered
| Option | Cost | Time | Why not now |

## Obligations checked
[contract / insurer / regulator — permits / forbids / unclear → counsel]

## Approval
Approver: [role, per authority matrix row ...] · Signed: [date]
Expiry: [date] · Renewal requires: [evidence]
Early-exit path: [what ending the exception would take]

## Revisit triggers (acceptance void if any occurs)
| Trigger | Watched by | Action on trigger |

Register link: [risk ID] · KRI link: [if any]
```

## Verification

- [ ] The accepted item is scoped to one asset or activity and one named policy clause or limit.
- [ ] Inherent and residual ratings use the register's scales, with the appetite limit shown.
- [ ] Every compensating control has an owner, a check and a frequency.
- [ ] At least two alternatives costed, including remediating now.
- [ ] Approver's authority matches the residual rating; requester is not the approver.
- [ ] Expiry is a date no more than 12 months out; renewal needs fresh evidence.
- [ ] Every revisit trigger names who watches it and what happens.
- [ ] External obligations checked, with unclear ones routed to counsel.

## False-Positive Prevention

1. **"Accepted" without a signature.** A risk nobody fixed is not an accepted risk; it is an unowned one.
2. **Open-ended exceptions.** "Until the upgrade" never expires. Date it.
3. **Compensating controls that are intentions.** "Staff will be careful" is not a control. Name
   an owner and a check.
4. **Self-approval.** The person who benefits from the exception cannot be the one who signs it.
5. **Scope creep under an old memo.** A memo for one workstation does not cover the second one
   installed last month. New scope, new memo.
6. **Renewal by default.** Renewing without evidence that the controls held turns a temporary
   exception into policy.
7. **Business acceptance of a legal prohibition.** If a contract or regulator forbids the position,
   no internal signature makes it acceptable. Check first.

## Example Output

```
# Risk acceptance / exception memo — RA-2026-07
Requested by: IT Manager · Risk owner: Operations Director · Date: 2026-09-24

## What is accepted
Keep workstation TX-04 on Windows 10 after end of vendor support, solely to run the legacy
tax-preparation application, departing from IT Standard 4.2 (supported operating systems only).

## Rating
Inherent: L4 × I4 = 16 · Residual with controls: L2 × I4 = 8 · Appetite limit: residual ≤ 6 without partner approval

## Compensating controls
| Isolated network segment, no internet or email | IT Manager | Firewall rule export reviewed | Monthly |
| Application allowlisting (tax app only) | IT Manager | Blocked-execution log reviewed | Weekly |
| Offline backup of client files | Office Manager | Test restore of one file set | Monthly |
| No client files stored locally beyond 30 days | Tax Lead | Folder audit | Monthly |

## Alternatives considered
| Upgrade to vendor's cloud version now | $48k | 5 months (mid-season migration) | Risk of missing filing deadlines |
| Stop offering this return type | $120k lost fees | Immediate | Exceeds cost of controls by far |
| Compensating controls (this memo) | $6k | 2 weeks | Chosen until migration after filing season |

## Obligations checked
Cyber insurance schedule: requires "supported software or documented exception" — permits.
Client engagement letters: silent — no action.

## Approval
Approver: Managing Partner (authority matrix: residual 7–12 requires partner) · Signed: 2026-09-26
Expiry: 2027-04-30 · Renewal requires: 6 months of passed control checks + migration plan dated
Early-exit path: migrate to cloud version — 5 months, $48k (budgeted for 2027-05)

## Revisit triggers
| Actively exploited vulnerability for Windows 10 published | IT Manager | Disconnect TX-04 same day; partner decides |
| Any monthly check fails | Control owner | Report within 24h; memo suspended |
| Second machine needed for the application | IT Manager | New memo |
| Insurer changes the software condition | Office Manager | Re-check before renewal |

Register link: R-14 · KRI link: "% unsupported endpoints" (target 1 of 38)
```

## Techniques Used

- **CM-09 Authority Boundary Specification** — approver matched to residual rating; no self-approval.
- **GT-05 Freshness with Enumerated Disarm Events** — expiry plus triggers that void the acceptance.
- **QA-09 Reversibility Assessment** — the early-exit path and its cost.
- **RT-05 Evidence-Based Reasoning** — each compensating control carries a check.
- **QA-12 False Positives Identification** — what looks like acceptance but is not.

## Related Prompts

- `domain-risk/risk_appetite_statement.md` — the limits and authority matrix the memo applies.
- `domain-risk/risk_register_builder.md` — the entry the memo is linked to.
- `domain-risk/risk_key_risk_indicators.md` — measurable triggers become KRIs.
- `domain-risk/risk_board_risk_report.md` — open acceptances and expiries reported upward.
