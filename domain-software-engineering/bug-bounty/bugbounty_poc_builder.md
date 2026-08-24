---
title: "Proof-of-Concept Builder"
category: bug-bounty/reporting
description: "Build a minimal, safe, reproducible proof of concept for a validated finding: enough to convince a triager, non-destructive, with no exfiltration beyond minimal proof"
techniques:
  - ST-01
  - ST-02
  - QA-02
  - RT-05
  - DD-07
difficulty: intermediate
tags:
  - bug-bounty
  - proof-of-concept
  - reproduction
  - safety
  - reporting
updated: "2026-06-18"
related_prompts:
  - domain-software-engineering/bug-bounty/bugbounty_disclosure_report_writer.md
  - domain-software-engineering/bug-bounty/bugbounty_finding_triage_validation.md
  - domain-software-engineering/bug-bounty/bugbounty_severity_cvss_impact.md
---

# Proof-of-Concept Builder

**Objective:** Turn a validated finding into the smallest, safest sequence of steps that lets a triager reproduce it on demand — convincing, non-destructive, and free of any action that harms the target or real users.

## When to Use
- A finding has passed triage and severity scoring and you're assembling the report.
- You need clean, copy-pasteable reproduction steps a triager can follow without your context.
- You want to make sure the PoC proves impact without crossing into destructive or excessive testing.

## Inputs / Context
- **The validated finding** and the raw requests/responses you captured.
- **The accounts/markers** you used (test accounts, collaborator host you control).
- **Program PoC rules** (what proof is acceptable; redaction expectations; any "do not include real data" rules).

## Instructions

1. **Authorization/safety gate.** The PoC must be reproducible using **test accounts/assets** and must be **non-destructive**: no data deletion/corruption, no DoS, no exfiltration beyond the minimal proof the program allows, no actions affecting real users. If your original proof went further than necessary, pare it back to the minimum that demonstrates the bug.

2. **State preconditions plainly:** required role/account, starting state, tools (e.g., an intercepting proxy), and any setup (two test accounts). A triager should be able to recreate the starting point exactly.

3. **Write numbered reproduction steps** that are deterministic and self-contained: exact endpoint, method, headers, and the specific manipulation. Use placeholders for secrets/IDs and show the *delta* that triggers the bug.

4. **Include the minimal evidence:** the request and the response (or response delta) that proves the effect. Redact real PII to the minimum needed — replace with `[REDACTED]` while keeping enough to show the boundary was crossed.

5. **Show the "secure vs. vulnerable" contrast** where helpful (e.g., account A's own object returns 200 with A's data and B's object *should* return 403 but returns B's data).

6. **Keep escalation demonstrations bounded:** prove reachability/impact with one benign step; describe (don't perform) further exploitation. For OOB proofs, reference your own collaborator and the correlating token.

7. **CRITICAL — verify the PoC is reproducible AND safe before finalizing:**
   - Re-run the steps from a clean state to confirm they work verbatim.
   - Confirm no step is destructive, exfiltrates beyond minimal proof, or touches real users.
   - Confirm all identifiers/accounts are yours or placeholders; real PII is redacted.
   - Confirm a triager with no prior context could follow it.

## False-Positive Prevention (MUST follow)
- ❌ Do NOT include steps that delete/modify real data, cause downtime, or affect real users.
- ❌ Do NOT include full data dumps or real users' PII as "proof" — minimal, redacted evidence only.
- ❌ Do NOT leave steps that only work in your dirty session (cookies, prior state) — make it clean-state reproducible.
- ❌ Do NOT include live secrets/tokens in the PoC text; use placeholders.
- ✅ DO pare the PoC to the minimum that proves the bug.
- ✅ DO redact real PII while preserving proof of the boundary crossing.
- ✅ DO re-run from a clean state to confirm determinism.

## Output Format
```
## Summary (one line)
[What this PoC proves]

## Preconditions
- Accounts/roles: ...
- Tools/setup: ...

## Reproduction Steps
1. ...
2. ...

## Evidence (minimal, redacted)
Request:
```
[method, path, key headers, body delta]
```
Response (delta):
```
[status + the field(s) proving impact; PII redacted]
```

## Secure vs. Vulnerable Contrast
- Expected: ...
- Observed: ...

## Escalation (described, not performed)
- ...

## Safety Self-Audit
[Non-destructive; minimal proof; own accounts/placeholders; clean-state reproducible]
```

## Example Output
```
## Summary (one line)
Any authenticated user can read another user's order via IDOR on GET /v1/orders/{id}.

## Preconditions
- Accounts/roles: two standard test accounts (A = bbtest+a, B = bbtest+b).
- Tools/setup: an intercepting proxy or curl; B's order id obtained from B's own session.

## Reproduction Steps
1. Log in as B; create an order; note its id (e.g., 8842) from B's own order history.
2. Log in as A in a fresh session.
3. As A, send: GET /v1/orders/8842 with A's Authorization header.
4. Observe A receives B's order (A has no relationship to order 8842).

## Evidence (minimal, redacted)
Request:
```
GET /v1/orders/8842 HTTP/1.1
Host: api.acme.com
Authorization: Bearer [A_TOKEN]
X-Bug-Bounty: <handle>
```
Response (delta):
```
HTTP/1.1 200 OK
{ "id":8842, "owner":"bbtest+b", "name":"[REDACTED]", "address":"[REDACTED]", "items":[...] }
```

## Secure vs. Vulnerable Contrast
- Expected: A requesting B's order id → 403/404.
- Observed: 200 with B's order details.

## Escalation (described, not performed)
Order IDs appear sequential, so an attacker could enumerate across all users; not performed — single
cross-account read shown as proof.

## Safety Self-Audit
Read-only, single record; both accounts are mine; B's PII redacted to [REDACTED] while keeping owner=
bbtest+b to prove the crossing; re-ran from a fresh A session — reproduces verbatim.
```

## Techniques Used
- **ST-01 (Clear Objective Statement)** — minimal, safe, reproducible proof as the explicit goal.
- **ST-02 (Structured Sequential Instructions)** — deterministic numbered steps from clean state.
- **QA-02 (Adversarial Thinking)** — anticipates triager skepticism with a secure-vs-vulnerable contrast.
- **RT-05 (Evidence-Based Reasoning)** — includes the request/response delta that proves the effect.
- **DD-07 (Self-Audit Table)** — safety self-audit confirms non-destructive, minimal, clean-state proof.
