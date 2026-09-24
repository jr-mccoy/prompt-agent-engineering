---
title: "Payment Fraud and BEC Controls — Callback Verification, Dual Approval, and Vendor Bank-Change Rules a Small Finance Team Can Actually Run"
category: risk
description: "Design the handful of payment controls that stop business-email-compromise and invoice fraud at a small or mid-sized organisation — callback verification on a number already on file, dual approval above a threshold, a locked vendor bank-change procedure with a cooling-off hold, urgency and secrecy treated as red flags, and a same-day bank-recall path — sized to a two-to-six-person finance function; distinct from `domain-finance/accounting-controllership/finance_sox_internal_controls_designer.md` (SOX control matrices for public-company reporting) and `risk_phishing_awareness_program.md` (training people, not the payment process)."
techniques:
  - CM-02
  - DP-04
  - QA-02
  - ST-02
  - OC-03
difficulty: intermediate
tags:
  - payment-fraud
  - business-email-compromise
  - internal-controls
  - accounts-payable
  - vendor-management
  - small-business
  - ceo-fraud
  - wire-transfer
  - fake-invoice
updated: "2026-09-24"
reasoning:
  styles: [adversarial, procedural, protective, systems]
  stakes: high
  horizon: weeks
  uncertainty: risk
  evidence_quality: moderate
  domain_complexity: cross_domain
  collaboration: small_team
  output_format: structured
  user_role: [operator, finance, founder, office-manager]
  mode: [design, audit, plan]
related_prompts:
  - domain-finance/accounting-controllership/finance_sox_internal_controls_designer.md
  - domain-risk/risk_phishing_awareness_program.md
  - domain-risk/risk_security_incident_response_playbook.md
---

# Payment Fraud and BEC Controls

**Objective:** Produce a short, enforceable payment-controls standard — who can pay, who
must approve, how bank-detail changes are verified, what counts as a red flag, and what
happens in the first hour if money goes to the wrong place — that holds even when a
well-trained person has been convincingly fooled.

**When to Use:**
- Payments and supplier bank changes are requested and approved by email.
- One person can create a supplier, change its bank details and release payment.
- You received (or paid) a "we've changed banks" invoice that turned out to be fraud.
- An insurer's crime/social-engineering cover or a client asks what payment controls exist.

**Not this prompt if:**
- You are a public company designing SOX control matrices with assertions and ITGCs —
  `domain-finance/accounting-controllership/finance_sox_internal_controls_designer.md`.
- You need staff awareness training — `risk_phishing_awareness_program.md` (complementary:
  training reduces attempts that succeed; these controls stop the payment when one does).
- Money has already gone — `risk_security_incident_response_playbook.md` (BEC module) now,
  and design controls afterwards.
- You were personally scammed as a consumer — `domain-legal/personal-self-advocacy/consumer-scams/legalprep_scam_fraud_report_preparer.md`.

**Boundary:** Preventive and detective controls only. Recovery, reporting to law enforcement
and any legal duties to notify are routed to the bank, counsel and the insurer; this prompt
states no recovery odds, timelines or legal obligations as fact.

## Inputs / Context

1. **Payment flow today:** who creates suppliers, edits bank details, raises, approves and
   releases payments; which banking platform and its approval features.
2. **Team size and absences:** can two people genuinely approve on any given day?
3. **Volume and size:** payments per month, typical and largest amounts.
4. **Channels requests arrive through:** email, portal, phone, messaging apps.
5. **Past attempts or losses**, and what nearly worked.
6. **Insurance:** whether crime/social-engineering cover exists and its stated conditions
   (quote the policy; do not paraphrase from memory).

## Method

1. **Map where one person can move money alone (ST-02).** Walk the flow step by step and
   mark every point where a single person, or a single email, is sufficient. Those points
   are the design brief.

2. **Write the five core controls as must/must-not rules (CM-02, DP-04).**

   | Control | Must | Must not |
   |---|---|---|
   | **Callback verification** | Verify any new supplier or bank-detail change by calling a number already on file or independently sourced | Use a number, link or contact in the request itself |
   | **Bank-change hold** | Hold the first payment to new details for a stated cooling-off period, and notify the old contact of the change | Pay to new details on the same day as the change request |
   | **Dual approval** | Require a second approver in the banking platform above a threshold, and for any new payee | Allow approval by forwarding an email "OK" |
   | **Segregation** | Separate supplier master-data edits from payment release | Let the same person change details and release payment |
   | **Urgency/secrecy stop** | Treat "urgent", "confidential", "CEO is travelling", "new bank" as a stop signal requiring callback | Let seniority of the requester bypass any control |

3. **Size to the team.** If only two finance people exist, name the out-of-finance second
   approver (a director) and the absence rule: when an approver is away, payments above the
   threshold wait — they are not approved by the remaining person "just this once".

4. **Attack the design (QA-02).** Run five scenarios against the controls and record which
   control stops each: spoofed CEO requesting an urgent transfer; compromised real supplier
   mailbox sending changed details; fake new supplier invoice below threshold, repeated; an
   insider editing a supplier's bank account then releasing payment; an approver on holiday.
   If a scenario passes every control, add or tighten one.

5. **Write the first-hour recall path.** Bank fraud line (held offline), who calls, what
   information the bank will want (payment reference, amount, time, beneficiary details),
   then hand to the IR playbook. Record "recall window — [confirm with bank]"; never assert one.

6. **Evidence and review (OC-03).** A change log for every bank-detail change (who requested,
   who called back, which number, result), and a quarterly spot-check of a sample by someone
   outside the payment chain.

## Output Format

```
# Payment controls standard — [organisation], [date]
Owner: [role] · Applies to: [entities, bank accounts] · Review: quarterly

## Single-person paths found (before)
| Step | Who alone can do it | Fixed by control # |

## Controls
| # | Control | Rule (must) | Prohibited (must not) | Threshold / hold | Evidence kept |

## Approvers and absence rule
| Role | Can approve up to | Backup | If both absent |

## Scenario test
| Scenario | Stopped by | Residual gap |

## First-hour recall path
Bank fraud line: [held at ...] · Caller: [role] · Info to give: ... · Then: IR playbook BEC module
Recall window: [confirm with bank]

## Change log columns and quarterly spot-check
## Confidence: High / Medium / Low per control, with reason
```

## Verification

- [ ] No remaining path lets one person or one email move money to new details.
- [ ] Callback uses a number on file or independently sourced — never from the request.
- [ ] The first payment to changed details is held for a stated period.
- [ ] Dual approval is enforced in the banking platform, not by email.
- [ ] The absence rule makes payments wait rather than drop to one approver.
- [ ] All five attack scenarios are stopped or their residual gap is owned.
- [ ] The recall path is held offline and asserts no recovery window.
- [ ] Insurance conditions are quoted from the policy, not assumed.

## False-Positive Prevention

1. **Calling the number in the email.** It reaches the fraudster. The callback must use a
   number sourced before the request existed.
2. **Email "approval" as dual control.** If the approver's mailbox is compromised, or the
   request is forwarded, the second approval is forged or skipped. Use platform approvals.
3. **Threshold splitting.** Fraudsters send several invoices just under the threshold. Apply
   dual approval to **any new payee** regardless of amount.
4. **Seniority override.** Controls that the CEO can waive by email will be waived by an
   email that looks like the CEO.
5. **Controls that assume a full team.** Holidays are when fraud lands. The absence rule is
   the control.
6. **Training as a substitute.** A convinced, well-meaning employee is the attack's goal;
   the process must hold without their scepticism.
7. **Asserting recovery odds.** Whether money can be recalled depends on the banks involved
   and timing; say "call the bank now" and nothing more certain.

## Example Output

```
# Payment controls standard — Meridian Events Ltd (3-person finance), 2026-09-24
Owner: Finance Manager · Applies to: operating + client-deposit accounts

## Single-person paths found
| Supplier bank edit + payment release | AP Clerk | #2, #4 |
| Director emails "please pay today" | Anyone | #5 |

## Controls
| 1 | Callback | New supplier / changed bank → call number in supplier file dated before request | Number in the request | — | Call log entry |
| 2 | Bank-change hold | 5 working-day hold on first payment + email to old contact | Same-day payment | 5 days | Change log |
| 3 | Dual approval | Platform second approval ≥ [threshold] and any new payee | Email "OK" | [threshold] | Platform audit trail |
| 4 | Segregation | AP Clerk edits master data; Finance Manager releases | Same person both | — | Role config screenshot |
| 5 | Urgency stop | "Urgent/confidential/new bank" → callback before anything | Seniority bypass | — | Call log |

## Approvers and absence rule
| Finance Manager | all | Operations Director | Payments ≥ threshold wait; no single approval |

## Scenario test
| Spoofed CEO urgent transfer | #5, #3 | none |
| Real supplier mailbox compromised | #1 (old number), #2 | if old number also changed by attacker earlier → quarterly spot-check |
| Repeated sub-threshold fake supplier | #3 (new payee) | none |
| Insider edit + release | #4 | none |
| Finance Manager on leave | absence rule | slower payments — accepted by MD |

## First-hour recall path
Bank fraud line: printed card in safe + Finance Manager's phone · Caller: Finance Manager, backup Ops Director
Recall window: [confirm with bank] · Then: IR playbook BEC module

## Confidence
#3, #4 High (platform-enforced) · #1, #2 Medium (depend on people following the log) · #5 Medium
```

## Techniques Used

- **CM-02 Constraint Specification** — each control as a must rule.
- **DP-04 Must-Not Constraints** — the prohibited shortcut paired with every control.
- **QA-02 Adversarial Stress-Test** — five fraud scenarios run against the design.
- **ST-02 Structured Sequential Instructions** — flow mapping to recall path in order.
- **OC-03 Markdown Table Specification** — controls, approvers and scenario tables.

## Related Prompts

- `risk_phishing_awareness_program.md` — the money-movers training track.
- `risk_security_incident_response_playbook.md` — the BEC module when a payment has gone.
- `risk_security_alert_triage_runbook.md` — handling bank fraud alerts as they arrive.
- `../domain-finance/accounting-controllership/finance_sox_internal_controls_designer.md` — full control matrices for public-company reporting.
