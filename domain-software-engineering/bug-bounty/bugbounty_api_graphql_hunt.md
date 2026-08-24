---
title: "API & GraphQL Hunting"
category: bug-bounty/hunting
description: "Black-box test plan for REST and GraphQL API weaknesses on in-scope targets: BOLA/BFLA, mass assignment, introspection, excessive data exposure, and broken function-level authorization"
techniques:
  - ST-01
  - ST-02
  - QA-02
  - RT-05
  - DD-07
difficulty: advanced
tags:
  - bug-bounty
  - api
  - graphql
  - bola
  - mass-assignment
updated: "2026-06-18"
related_prompts:
  - domain-software-engineering/bug-bounty/bugbounty_access_control_idor_hunt.md
  - domain-software-engineering/bug-bounty/bugbounty_authentication_session_hunt.md
  - domain-software-engineering/bug-bounty/bugbounty_finding_triage_validation.md
---

# API & GraphQL Hunting

**Objective:** Systematically test an in-scope REST or GraphQL API for the OWASP API Top 10 weaknesses — especially object- and function-level authorization, mass assignment, and excessive data exposure — using your own accounts.

## When to Use
- The target exposes a REST API or a GraphQL endpoint (`/graphql`).
- You harvested API routes from JS or have API docs/OpenAPI/schema.
- You want an API-specific pass complementing the access-control hunt.

## Inputs / Context
- **In-scope API base URL(s)** and any discovered endpoints/operations.
- **Your own test accounts** (ideally different roles/tenants) with required markers.
- **Schema/docs** if available (OpenAPI, GraphQL introspection result — only if permitted).
- **RoE limits** on request volume and data access.

## Instructions

1. **Authorization gate.** Confirm the API is in scope and use your own accounts. As with IDOR, prove cross-account issues against your *second* test account — never real users' data. Respect RoE volume limits (APIs make automated abuse easy).

2. **Enumerate the surface:** harvest endpoints/operations from JS, docs, OpenAPI, or (for GraphQL, if allowed) introspection. Note auth requirements, parameters, and object identifiers per operation.

3. **BOLA / object-level auth (API #1):** for each object-bearing operation, attempt to access another account's object IDs with your session (the API analog of IDOR). Test all ID locations (path, query, body, GraphQL variables).

4. **BFLA / function-level auth (API #5):** call privileged/admin operations as a low-priv user; in GraphQL, try admin mutations/queries directly; test method/verb tampering on REST.

5. **Mass assignment (API #6):** add unexpected fields to write requests (`role`, `isAdmin`, `verified`, `balance`, `tenantId`) and check whether the server binds them.

6. **Excessive data exposure (API #3):** inspect responses for fields the UI never shows (internal flags, other users' PII, tokens); GraphQL often over-returns when you ask for more fields than the UI does.

7. **GraphQL-specific:** introspection enabled in production, nested/recursive queries (DoS — only *describe* the risk, do not actually run resource-exhausting queries), alias-based brute (within RoE), and authorization applied per-resolver vs. only at the gate.

8. **Other API checks:** missing rate limiting on sensitive actions (report-worthy where program allows), inconsistent auth across versions (`/v1` vs `/v2`), and verbose errors leaking internals.

9. **CRITICAL — verify each finding with your own accounts:**
   - For BOLA/BFLA, confirm you accessed your *second* account's object/function, with a request/response delta.
   - For mass assignment, confirm the injected field actually changed server state (re-fetch and observe).
   - For excessive exposure, confirm the extra fields are genuinely sensitive and not public.
   - For GraphQL DoS, describe the risk; do NOT execute queries that could degrade the service.
   - Assign confidence (High/Med/Low) and note what would change it.

## False-Positive Prevention (MUST follow)
- ❌ Do NOT report BOLA from a 200 alone — confirm the response holds your other account's data.
- ❌ Do NOT report mass assignment unless the field demonstrably changed server state (re-fetch to confirm).
- ❌ Do NOT run resource-exhausting GraphQL queries to "prove" DoS — describe the risk instead.
- ❌ Do NOT flag a verbose error or introspection as high severity without a concrete exploitation path.
- ✅ DO use your second test account for cross-account proof.
- ✅ DO re-fetch to confirm a write actually persisted.
- ✅ DO confirm exposed fields are sensitive and non-public.

## Output Format
```
## Authorization & Account Setup
[In-scope API; own accounts A/B; schema source; RoE volume]

## API Surface
| Operation | Auth required | Object IDs | Notes |

## Tests & Results
| # | OWASP API risk | Operation | Manipulation | Secure expectation | Observed | Verdict |

## Verified Findings
### [Risk] on [operation] — confidence: High/Med/Low
- Proof (own accounts): ...
- Impact: ...
- What would change confidence: ...

## Self-Audit
[Cross-account proof via own B account; writes re-fetched; no DoS executed]
```

## Example Output
```
## Authorization & Account Setup
In-scope: api.acme.com (REST) + /graphql. Accounts bbtest+a/+b. Schema via introspection (program allows).
Low request volume.

## API Surface
| Operation | Auth | Object IDs | Notes |
|-----------|------|-----------|-------|
| GET /v1/invoices/{id} | user | numeric id | BOLA candidate |
| mutation updateUser(input) | user | — | mass-assignment candidate |
| query adminStats | should be admin | — | BFLA candidate |

## Tests & Results
| # | Risk | Operation | Manipulation | Secure | Observed | Verdict |
|---|------|-----------|--------------|--------|----------|---------|
| 1 | BOLA | GET /v1/invoices/{B-id} | A's session | 403 | 200 + B's invoice | VULN |
| 2 | Mass assign | updateUser(input:{role:"admin"}) | A's session | ignored | role=admin after re-fetch | VULN |
| 3 | BFLA | query adminStats | A's session | 403 | 403 | secure |

## Verified Findings
### BOLA on GET /v1/invoices/{id} — confidence: High
- Proof: A's session fetched invoice id belonging to my account B; response contained B's billing data.
- Impact: cross-account invoice/PII disclosure across the user base.
- What would change confidence: if invoices were shared — confirmed B's invoice is private to B.

### Mass assignment of role via updateUser — confidence: High
- Proof: sending input:{role:"admin"} as user A; re-fetching /v1/me showed role=admin and unlocked
  adminStats. Reverted my account afterward.
- Impact: privilege escalation to admin from any user account.
- What would change confidence: if role were cosmetic — confirmed it gated adminStats access.

## Self-Audit
Cross-account proof used my own B account; the role write was re-fetched to confirm persistence and then
reverted; no resource-exhausting GraphQL queries were executed.
```

## Techniques Used
- **ST-01 (Clear Objective Statement)** — frames the pass around the OWASP API Top 10 priorities.
- **ST-02 (Structured Sequential Instructions)** — surface → BOLA → BFLA → mass-assign → exposure → GraphQL.
- **QA-02 (Adversarial Thinking)** — probes the authorization and binding gaps APIs commonly leave open.
- **RT-05 (Evidence-Based Reasoning)** — findings require request/response deltas and re-fetch confirmation.
- **DD-07 (Self-Audit Table)** — verification enforces second-account proof and no executed DoS.
