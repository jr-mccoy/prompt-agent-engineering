---
title: "Authentication & Session Hunting"
category: bug-bounty/hunting
description: "Black-box test plan for authentication, session, OAuth/OIDC, JWT, and MFA weaknesses on in-scope targets, with exploitability verification using your own accounts"
techniques:
  - ST-01
  - ST-02
  - QA-02
  - RT-05
  - DD-07
difficulty: advanced
tags:
  - bug-bounty
  - authentication
  - session
  - oauth
  - jwt
  - mfa
updated: "2026-06-18"
related_prompts:
  - domain-software-engineering/bug-bounty/bugbounty_access_control_idor_hunt.md
  - domain-software-engineering/bug-bounty/bugbounty_finding_triage_validation.md
  - domain-software-engineering/bug-bounty/bugbounty_severity_cvss_impact.md
---

# Authentication & Session Hunting

**Objective:** Hunt weaknesses in how an in-scope target proves and maintains identity — login, session lifecycle, OAuth/OIDC flows, JWT handling, password reset, and MFA — and verify them safely with accounts you control.

## When to Use
- The target has login, registration, password reset, social login, or MFA.
- You want a structured pass over the authentication and session surface.
- You found a candidate auth flaw and need to confirm impact before reporting.

## Inputs / Context
- **In-scope auth endpoints/flows** (login, reset, OAuth callback, token endpoints).
- **Your own test accounts** (with required markers); a second account for cross-account tests.
- **RoE limits** (especially: no brute-force/credential-stuffing unless explicitly permitted).

## Instructions

1. **Authorization gate.** Confirm the flows are in scope and use only your own accounts. Do NOT brute-force, credential-stuff, or test against real users' accounts. If testing rate-limiting/lockout, do it against your own account and within RoE volume limits.

2. **Session lifecycle:** inspect session token issuance, attributes (HttpOnly, Secure, SameSite), fixation (does the session ID rotate on login?), invalidation on logout/password-change, concurrent-session handling, and predictable/insufficient-entropy tokens.

3. **Password reset & account recovery:** token entropy/expiry/reuse, host-header poisoning of reset links, reset-token leakage in referrer/logs, user-enumeration via differential responses/timing, and whether reset invalidates active sessions.

4. **OAuth/OIDC flows:** `redirect_uri` validation (open-redirect/exfil of code/token), `state` parameter presence (CSRF on the flow), token leakage via referrer, account-linking/pre-account-takeover, and scope/consent handling.

5. **JWT handling (if used):** `alg:none` acceptance, weak/guessable HMAC secret, signature-not-verified, `kid` injection, expiry not enforced, and sensitive claims trusted from the client.

6. **MFA:** bypass via response manipulation, missing enforcement on alternate endpoints, weak/brute-forceable OTP (within RoE), backup-code weaknesses, and "remember device" abuse.

7. **CRITICAL — verify each finding is real, in-scope, and impactful:**
   - Reproduce using your own account(s); for takeover-class bugs, demonstrate against your *second* test account, never a real user.
   - Confirm the security property actually fails (e.g., old session truly still valid after password change), not a misread response.
   - Articulate concrete impact (account takeover? session hijack? enumeration only?).
   - Assign confidence (High/Med/Low) and state what would change it.

## False-Positive Prevention (MUST follow)
- ❌ Do NOT brute-force or credential-stuff; do NOT test real users' accounts.
- ❌ Do NOT report a missing `Secure`/`SameSite` flag as account takeover — match the claim to the actual demonstrated impact.
- ❌ Do NOT claim "JWT alg:none works" without showing the server accepted the forged token for a protected action.
- ❌ Do NOT report user-enumeration without confirming a reliable differential (and check it isn't an out-of-scope vuln type).
- ✅ DO demonstrate takeover only against your own second account.
- ✅ DO confirm the failed security property with a concrete before/after.
- ✅ DO scale the impact claim to what you actually proved.

## Output Format
```
## Authorization & Account Setup
[In-scope flows; own accounts + markers; RoE limits noted]

## Auth Surface Tested
| Area | Tests run | Observed | Verdict |

## Verified Findings
### [Finding] — confidence: High/Med/Low
- Property that failed: ...
- Proof (own accounts): ...
- Impact: [ATO / session hijack / enumeration / ...]
- What would change confidence: ...

## Self-Audit
[Own accounts only; property failure confirmed; impact matches proof]
```

## Example Output
```
## Authorization & Account Setup
In-scope: app.acme.com login/reset, /oauth/callback. Accounts bbtest+a/+b. No brute-force per RoE.

## Auth Surface Tested
| Area | Tests | Observed | Verdict |
|------|-------|----------|---------|
| Session fixation | session id before/after login | id rotates on login | secure |
| Logout invalidation | reuse token after logout | token rejected | secure |
| Password change | reuse old session after change | OLD SESSION STILL VALID | VULN |
| OAuth redirect_uri | append &redirect_uri=evil | strict allowlist, rejected | secure |
| JWT alg | alg:none forged token on /me | rejected | secure |

## Verified Findings
### Sessions not invalidated on password change — confidence: High
- Property that failed: changing the account password should revoke other active sessions; it does not.
- Proof: logged account A in on two browsers; changed password in browser 1; browser 2's session
  continued to access /me and place orders for 30+ min. Reproduced twice with my own account A.
- Impact: after a credential compromise + reset, an attacker's stolen session persists — weakens account
  recovery. Medium severity (depends on prior compromise).
- What would change confidence: if a background job revoked sessions after a delay — confirmed still
  valid well beyond any plausible delay.

## Self-Audit
Only my account A used; property failure shown with concrete before/after; impact scoped to "stolen
session persists after reset," not over-claimed as direct takeover.
```

## Techniques Used
- **ST-01 (Clear Objective Statement)** — targets identity-proving and session-maintaining mechanisms.
- **ST-02 (Structured Sequential Instructions)** — session → reset → OAuth → JWT → MFA coverage.
- **QA-02 (Adversarial Thinking)** — each sub-area lists the concrete bypasses attackers try.
- **RT-05 (Evidence-Based Reasoning)** — findings require a demonstrated before/after of a failed property.
- **DD-07 (Self-Audit Table)** — verification enforces own-accounts-only and impact-matches-proof.
