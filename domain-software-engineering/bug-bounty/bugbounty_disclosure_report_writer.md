---
title: "Vulnerability Disclosure Report Writer"
category: bug-bounty/reporting
description: "Draft a high-signal vulnerability disclosure report — title, summary, reproduction, impact, and remediation — that triages fast and lands the right payout"
techniques:
  - ST-01
  - ST-03
  - DS-01
  - RT-05
  - DD-07
difficulty: intermediate
tags:
  - bug-bounty
  - report-writing
  - disclosure
  - triage
  - remediation
updated: "2026-06-18"
related_prompts:
  - domain-software-engineering/bug-bounty/bugbounty_poc_builder.md
  - domain-software-engineering/bug-bounty/bugbounty_severity_cvss_impact.md
  - domain-software-engineering/bug-bounty/bugbounty_report_postmortem.md
---

# Vulnerability Disclosure Report Writer

**Objective:** Produce a disclosure report that a triager can validate quickly and tier correctly — the single biggest lever on payout speed and amount after the bug itself.

## When to Use
- A finding has passed triage, has a CVSS/impact assessment, and a safe PoC.
- You want a clean, professional report structured the way triagers expect.
- You want to maximize the chance of fast acceptance and correct severity.

## Inputs / Context
- **The validated finding**, its **CVSS/impact** (`bugbounty_severity_cvss_impact.md`), and **PoC** (`bugbounty_poc_builder.md`).
- **The program's report template/fields** if it has one (use them).
- **Scope reference** so you can cite the affected in-scope asset.

## Instructions

1. **Authorization/accuracy gate.** Report only what you actually proved on an in-scope asset. Do not embellish, do not include real users' PII beyond minimal redacted proof, and do not threaten public disclosure — follow the program's coordinated-disclosure process.

2. **Write a precise title:** `[Vuln class] in [specific endpoint/feature] allows [concrete impact]`. Triagers skim titles; vague titles get queued behind clear ones.

3. **Write a 2–4 sentence summary** stating what the bug is, where, who can exploit it, and the impact — enough for a triager to grasp severity before reading the PoC.

4. **State the affected asset and scope** explicitly (the in-scope host/endpoint), plus prerequisites (account/role).

5. **Include the steps to reproduce** from the PoC: numbered, deterministic, clean-state, with the request/response evidence and redactions intact.

6. **Write the impact section** from the severity work: the business consequence and the CVSS vector/score. Separate proven impact from realistic escalation (clearly labeled).

7. **Add remediation guidance:** a concise, correct fix recommendation (e.g., enforce object-level authorization server-side; validate `redirect_uri` against an allowlist). This signals competence and helps the vendor, which builds reputation.

8. **Keep tone professional and concise:** no hype, no filler, no adversarial framing toward the vendor. Match the program's template fields if provided.

9. **CRITICAL — verify the report is accurate, complete, and self-contained:**
   - Confirm every claim is backed by evidence in the report (no unsupported assertions).
   - Confirm proven vs. potential impact is clearly separated.
   - Confirm the PoC is reproducible from the report alone, with real PII redacted.
   - Confirm the affected asset is the in-scope one and the title matches the demonstrated impact.

## False-Positive Prevention (MUST follow)
- ❌ Do NOT overstate impact in the title/summary beyond the PoC (triagers down-tier inflated reports).
- ❌ Do NOT include unredacted real-user PII or live secrets in the report.
- ❌ Do NOT submit a report whose steps can't be followed without your private context.
- ❌ Do NOT threaten or pressure the vendor, or mention public disclosure timelines as leverage.
- ✅ DO make the title and summary match exactly what you proved.
- ✅ DO label escalation as potential, not proven.
- ✅ DO include accurate remediation and follow the program's template.

## Output Format
```
## Title
[Vuln class] in [endpoint/feature] allows [impact]

## Summary
[2-4 sentences]

## Affected Asset (in scope)
[host/endpoint] · Prerequisites: [account/role]

## Severity
CVSS: [vector] = [score] ([band]) · Program tier expectation: [band]

## Steps to Reproduce
1. ...
[request/response evidence, redacted]

## Impact
- Proven: ...
- Potential (escalation): ...

## Remediation
[Concise, correct fix]

## Notes
[Anything the triager should know: timing, dependencies]
```

## Example Output
```
## Title
IDOR in GET /v1/orders/{id} allows any authenticated user to read other users' order PII

## Summary
The order-detail endpoint does not verify that the requested order belongs to the authenticated user.
Any user with a free account can retrieve another user's order — including name, shipping address, and
items — by changing the numeric order id. IDs are sequential, enabling enumeration across the customer base.

## Affected Asset (in scope)
api.acme.com — GET /v1/orders/{id}. Prerequisites: any authenticated standard account.

## Severity
CVSS: CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:N/A:N = 6.5 (Medium). Tier expectation: High (mass-PII IDOR).

## Steps to Reproduce
1. As test account B, create an order; note its id (8842) from B's history.
2. Log in as test account A (fresh session).
3. As A, send GET /v1/orders/8842 with A's bearer token.
4. A receives B's order details, though A has no relationship to it.
Request/response (redacted):
GET /v1/orders/8842 → 200 { "owner":"bbtest+b", "name":"[REDACTED]", "address":"[REDACTED]", ... }

## Impact
- Proven: cross-account read of another account's full order PII (demonstrated A→B with my test accounts).
- Potential: sequential IDs allow enumeration of all users' orders (not performed).

## Remediation
Enforce object-level authorization server-side: verify the order's owner matches the authenticated
user before returning it (return 403/404 otherwise). Consider non-sequential identifiers as defense-in-depth.

## Notes
Both accounts used are mine (bbtest+ markers); only one record was accessed as proof; B's PII redacted.
```

## Techniques Used
- **ST-01 (Clear Objective Statement)** — a fast-to-triage, correctly-tiered report as the goal.
- **ST-03 (Output Format Specification)** — locks the triager-expected report structure.
- **DS-01 (Framework Application)** — applies the standard title/summary/repro/impact/remediation frame.
- **RT-05 (Evidence-Based Reasoning)** — every claim is backed by in-report evidence.
- **DD-07 (Self-Audit Table)** — verification ensures accuracy, redaction, and self-contained reproduction.
