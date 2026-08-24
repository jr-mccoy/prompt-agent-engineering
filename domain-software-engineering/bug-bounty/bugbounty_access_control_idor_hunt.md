---
title: "Access Control & IDOR Hunting"
category: bug-bounty/hunting
description: "Black-box test plan for broken access control: IDOR/BOLA, horizontal and vertical privilege escalation, and forced-browsing on in-scope targets, with exploitability verification"
techniques:
  - ST-01
  - ST-02
  - QA-02
  - RT-05
  - DD-07
difficulty: intermediate
tags:
  - bug-bounty
  - idor
  - broken-access-control
  - bola
  - privilege-escalation
updated: "2026-06-18"
related_prompts:
  - domain-software-engineering/bug-bounty/bugbounty_api_graphql_hunt.md
  - domain-software-engineering/bug-bounty/bugbounty_finding_triage_validation.md
  - domain-software-engineering/bug-bounty/bugbounty_recon_attack_surface_map.md
---

# Access Control & IDOR Hunting

**Objective:** Systematically hunt broken-access-control bugs on an in-scope target — the most common and among the best-paid classes — by reasoning about who *should* be able to do what, then testing where that boundary is unenforced.

## When to Use
- The target has object-bearing endpoints (`/users/123`, `/orders/abc`), multiple roles, or multi-tenant data.
- You've mapped the attack surface and want a concrete access-control test plan.
- You found a candidate IDOR and want to confirm it's real before reporting.

## Inputs / Context
- **In-scope endpoints** with object identifiers or role-gated actions (from recon).
- **At least two test accounts** you control (per RoE; use required test markers), ideally different roles/tenants.
- **RoE limits** on data access (you may only confirm access to *your own* test objects unless the program permits otherwise).

## Instructions

1. **Authorization gate.** Confirm the endpoints are in scope and that you are using **your own test accounts**. NEVER access another real user's data to "prove" an IDOR — create a second test account and use its objects as the target. If the program forbids accessing any cross-account data, prove the bug via the difference in responses (status/length) without reading real PII.

2. **Model the intended access matrix:** enumerate roles (anonymous, user, admin, tenant A vs B) and the objects/actions each *should* reach. Bugs live where the implementation diverges from this model.

3. **Hunt horizontal IDOR/BOLA:** with account A's session, attempt to read/modify account B's objects by manipulating identifiers (sequential IDs, UUIDs leaked elsewhere, encoded/hashed IDs, IDs in different locations: path, query, body, headers, JSON fields).

4. **Hunt vertical privilege escalation:** as a low-privilege user, attempt admin-only actions (call admin endpoints directly, flip role/permission fields in requests, mass-assignment of privilege attributes).

5. **Hunt forced browsing & function-level gaps:** access admin/internal endpoints without UI links; test whether authorization is enforced server-side or only hidden in the client.

6. **Test the bypass variations** that frequently re-open "fixed" checks: HTTP method swap (GET↔POST↔PUT), trailing slashes/extensions, case changes, parameter pollution, wrapping IDs in arrays/objects, and accessing via an alternate endpoint that hits the same object.

7. **CRITICAL — verify each candidate is a real, in-scope, exploitable access-control failure:**
   - Reproduce with two of *your own* accounts; confirm account A genuinely affected account B's object (not its own, not a public resource).
   - Confirm the action had a real effect (data returned that A shouldn't see, or a state change), not just a 200 with empty/identical content.
   - Rule out that the object is intentionally shared/public.
   - Capture the exact request/response delta proving the boundary was crossed.
   - Assign a confidence level (High/Medium/Low) and state what would change it.

## False-Positive Prevention (MUST follow)
- ❌ Do NOT report a 200 response as IDOR without confirming the response actually contains data A is not authorized to see.
- ❌ Do NOT access a *real* user's data to demonstrate the bug — use a second test account.
- ❌ Do NOT flag access to intentionally public/shared resources as access control failure.
- ❌ Do NOT assume an ID change "worked" because the request didn't error — verify the returned object belongs to the other account.
- ✅ DO prove the boundary crossing with a request/response delta between your two accounts.
- ✅ DO confirm a real read or state-change effect.
- ✅ DO note when proof relies only on response-length/status differences (program PII limits).

## Output Format
```
## Authorization & Account Setup
[In-scope endpoints; test accounts A/B with markers]

## Intended Access Matrix
| Role/Tenant | Should access | Should NOT access |

## Test Plan & Results
| # | Technique | Endpoint | Request manipulation | Expected (secure) | Observed | Verdict |

## Verified Findings
### [Finding] — confidence: High/Med/Low
- Boundary crossed: A's session → B's object
- Proof (request/response delta): ...
- Real effect: [data exposed / state changed]
- What would change confidence: ...

## Self-Audit
[Two own accounts used; effect confirmed; no real-user data accessed]
```

## Example Output
```
## Authorization & Account Setup
In-scope: api.acme.com/v1/orders/{id}. Accounts: bbtest+a@…, bbtest+b@… (both standard users, header tag set).

## Intended Access Matrix
| Role | Should access | Should NOT access |
|------|---------------|-------------------|
| user A | A's own orders | B's orders, admin endpoints |
| user B | B's own orders | A's orders |

## Test Plan & Results
| # | Technique | Endpoint | Manipulation | Secure expectation | Observed | Verdict |
|---|-----------|----------|--------------|--------------------|----------|---------|
| 1 | Horizontal IDOR | GET /v1/orders/{id} | A's session, B's order id | 403/404 | 200 + B's order JSON | VULN |
| 2 | Method swap | DELETE /v1/orders/{B-id} | A's session | 403 | 403 | secure |
| 3 | Vertical | GET /v1/admin/users | A's session | 403 | 403 | secure |
| 4 | Mass-assign role | PATCH /v1/me {"role":"admin"} | A's session | ignored | role unchanged | secure |

## Verified Findings
### Horizontal IDOR on GET /v1/orders/{id} — confidence: High
- Boundary crossed: account A's session read account B's order (id from B's own session, both my accounts).
- Proof: A's request to /v1/orders/8842 (B's order) returned HTTP 200 with B's shipping address and
  item list; A's account has no relationship to order 8842. Request/response captured.
- Real effect: cross-account PII read (name, address, items).
- What would change confidence: if 8842 were a demo/shared order — confirmed it's exclusively B's.

## Self-Audit
Both accounts are mine (bbtest+ markers); the returned order is B's, not A's or public; effect is a
genuine cross-account read. No real customer data was accessed.
```

## Techniques Used
- **ST-01 (Clear Objective Statement)** — hunt framed around the intended-vs-enforced access boundary.
- **ST-02 (Structured Sequential Instructions)** — model matrix → horizontal → vertical → forced browse → bypasses.
- **QA-02 (Adversarial Thinking)** — bypass-variation step probes the ways access checks are commonly evaded.
- **RT-05 (Evidence-Based Reasoning)** — findings require a request/response delta proving the crossing.
- **DD-07 (Self-Audit Table)** — verification ensures two own accounts and a real effect, no real-user data.
