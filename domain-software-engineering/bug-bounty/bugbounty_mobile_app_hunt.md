---
title: "Mobile App Hunting (iOS / Android)"
category: bug-bounty/hunting
description: "Black-box test plan for in-scope mobile apps: insecure data storage, hardcoded secrets, transport/cert-pinning, deeplink/IPC exposure, and the API backend behind the app"
techniques:
  - ST-01
  - ST-02
  - QA-02
  - RT-05
  - DD-07
difficulty: advanced
tags:
  - bug-bounty
  - mobile
  - android
  - ios
  - insecure-storage
updated: "2026-06-18"
related_prompts:
  - domain-software-engineering/bug-bounty/bugbounty_api_graphql_hunt.md
  - domain-software-engineering/bug-bounty/bugbounty_authentication_session_hunt.md
  - domain-software-engineering/bug-bounty/bugbounty_finding_triage_validation.md
---

# Mobile App Hunting (iOS / Android)

**Objective:** Test an in-scope mobile app the way the OWASP Mobile Top 10 frames it — local data, secrets, transport, platform interfaces — and pivot to the API backend, which is often where the highest-impact bugs actually live.

## When to Use
- The program lists a mobile app (and usually its backend API) in scope.
- You want to assess the app on a device/emulator you own.
- You found something in the app and want to confirm it matters (many mobile issues are low severity unless they reach the backend or other users).

## Inputs / Context
- **In-scope app** (store link / package ID / bundle ID) and **backend API** scope.
- **A test device/emulator you own** and your own test accounts.
- **RoE limits** — and note many programs only reward mobile bugs that have real impact (e.g., backend access), not theoretical local issues on a rooted device.

## Instructions

1. **Authorization gate.** Confirm both the app and its backend are in scope. Test on a device/emulator **you own**, with **your own accounts**. Local-only issues that require a rooted/jailbroken attacker-owned device are often out of scope or low value — focus on what affects the backend or other users.

2. **Insecure local storage:** inspect what the app stores on-device (shared prefs / NSUserDefaults, SQLite, files, caches, logs) for sensitive data — tokens, PII, secrets — stored unencrypted. Severity hinges on real exposure (e.g., backup-extractable, world-readable), not mere presence.

3. **Hardcoded secrets:** examine the app package for embedded API keys, credentials, or endpoints. Distinguish *sensitive* secrets (server-side API keys granting privileged access) from *public* client identifiers (often non-issues). Confirm a hardcoded key actually grants access before reporting.

4. **Transport & cert pinning:** check for cleartext traffic, weak TLS, and whether pinning can be bypassed (on your own device) to inspect API traffic. Pinning bypass itself is usually *enabling*, not the finding — the finding is what you discover in the now-visible API traffic.

5. **Platform interfaces (IPC / deeplinks):** test exported Android components (activities/services/receivers/providers), deeplink/universal-link handlers, and custom URL schemes for unauthorized actions, parameter injection, or token leakage triggerable by another app or a crafted link.

6. **Backend pivot (usually the money):** intercept the app↔server traffic (on your own device) and run the API hunts (`bugbounty_api_graphql_hunt.md`, access-control, auth) against the in-scope backend — mobile apps often expose richer/older APIs than the web client.

7. **CRITICAL — verify impact, not just presence:**
   - For stored data/secrets, confirm they're *actually* extractable in a realistic threat model and that a secret grants real access (test it against the in-scope backend).
   - For deeplink/IPC, demonstrate a concrete unauthorized effect triggerable by a third party, not just an exported component.
   - For pinning bypass, report the downstream API finding, not the bypass alone.
   - Confirm all testing was on your own device/accounts.
   - Assign confidence (High/Med/Low) and note what would change it.

## False-Positive Prevention (MUST follow)
- ❌ Do NOT report data "stored on device" as a vuln unless it's sensitive AND realistically extractable.
- ❌ Do NOT report every hardcoded string as a secret — verify it grants privileged access against the backend.
- ❌ Do NOT report cert-pinning absence as high severity by itself — tie it to a concrete downstream finding.
- ❌ Do NOT report an exported component without demonstrating a real unauthorized action.
- ✅ DO test extracted secrets/keys against the in-scope backend to confirm access.
- ✅ DO demonstrate third-party-triggerable impact for deeplink/IPC issues.
- ✅ DO pivot to the backend API where the high-impact bugs usually are.

## Output Format
```
## Authorization & Device Note
[In-scope app + backend; own device/emulator; own accounts; mobile RoE/value note]

## Findings by Area
| Area (storage/secrets/transport/IPC/backend) | Observation | Realistic impact? | Verdict |

## Verified Findings
### [Finding] — confidence: High/Med/Low
- What: ...
- Proof (own device/accounts): ...
- Impact (incl. backend reach): ...
- What would change confidence: ...

## Self-Audit
[Impact confirmed beyond mere presence; backend access verified where claimed; own device only]
```

## Example Output
```
## Authorization & Device Note
In-scope: Acme Android app (com.acme.app) + api.acme.com backend. Tested on my own emulator, account
bbtest+a. Program rewards mobile bugs with backend/user impact.

## Findings by Area
| Area | Observation | Realistic impact? | Verdict |
|------|-------------|-------------------|---------|
| Storage | session token in plaintext SharedPrefs | extractable via adb backup | candidate (low alone) |
| Secrets | hardcoded "internal" API key in strings | grants access to /v1/internal/* | VULN if key works |
| Transport | pinning present; bypassed on my emulator | enables API inspection | enabling only |
| Backend | /v1/internal/users readable with the key | bulk PII | VULN |

## Verified Findings
### Hardcoded internal API key grants backend access — confidence: High
- What: the app ships an "x-internal-key" used for /v1/internal/* endpoints.
- Proof: extracted the key from the package; sent it to api.acme.com/v1/internal/users from my own
  client — returned a paginated user list (PII). In-scope backend; I retrieved a single page as proof
  and did not enumerate further.
- Impact: any app holder can extract the key and read internal user data → mass PII exposure.
- What would change confidence: if the key were per-user/rotating — confirmed it's static across installs.

## Self-Audit
Tested only on my own emulator/account; the "secret" was verified to actually grant backend access
(not assumed); pulled minimal proof (one page) and reported the backend finding, not the pinning bypass.
```

## Techniques Used
- **ST-01 (Clear Objective Statement)** — frames mobile testing around real impact and the backend pivot.
- **ST-02 (Structured Sequential Instructions)** — storage → secrets → transport → IPC → backend.
- **QA-02 (Adversarial Thinking)** — separates enabling conditions (pinning) from the actual finding.
- **RT-05 (Evidence-Based Reasoning)** — requires verifying secrets/keys actually grant access.
- **DD-07 (Self-Audit Table)** — verification enforces impact-over-presence and own-device testing.
