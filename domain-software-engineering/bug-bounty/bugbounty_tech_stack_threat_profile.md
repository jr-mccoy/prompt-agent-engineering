---
title: "Tech-Stack Threat Profile"
category: bug-bounty/recon
description: "Turn a fingerprinted technology stack into a ranked threat profile: the vulnerability classes, known-CVE areas, and misconfigurations most worth probing first on this target"
techniques:
  - ST-01
  - RT-05
  - DS-01
  - DS-06
  - DD-07
difficulty: intermediate
tags:
  - bug-bounty
  - threat-profile
  - fingerprinting
  - cve
  - prioritization
updated: "2026-06-18"
related_prompts:
  - domain-software-engineering/bug-bounty/bugbounty_recon_attack_surface_map.md
  - domain-software-engineering/bug-bounty/bugbounty_injection_hunt.md
  - domain-software-engineering/bug-bounty/bugbounty_api_graphql_hunt.md
---

# Tech-Stack Threat Profile

**Objective:** Given what you've fingerprinted about a target's stack, produce a ranked list of the vulnerability classes, known-CVE areas, and common misconfigurations most likely to pay off — so you probe the highest-probability issues first.

## When to Use
- Recon has revealed the framework/CMS/server/cloud stack and you want to know what to look for.
- You want to convert "it runs X version Y" into "therefore probe Z."
- You need to focus a limited testing window on stack-specific weak points.

## Inputs / Context
- **Fingerprint data** (from recon): server, framework/CMS + versions, frontend, API style, auth provider, CDN/WAF, cloud provider. Mark each confirmed vs. inferred.
- **In-scope assets** and RoE.
- **Your strong vuln classes.**

## Instructions

1. **Authorization note.** This prompt produces a *prioritized hypothesis list* for in-scope assets only. It does not authorize testing anything outside scope.

2. **For each stack component, derive its characteristic weaknesses:** common misconfigurations, default-credential/exposed-admin patterns, framework-specific injection/deserialization/SSTI surfaces, auth-provider pitfalls, and API-style-specific issues (e.g., GraphQL introspection, REST BOLA).

3. **Map versions to known-vulnerability areas responsibly:** where a confirmed version is end-of-life or has well-known issue classes, note the *class* to check and how to confirm it on the live in-scope target. Do not assert a specific CVE is present without verification — frame it as "version suggests checking for X; confirm by Y."

4. **Cross-reference with the target's functionality** (from recon): a deserialization-prone framework matters more on an endpoint that accepts serialized objects; SSTI matters where user input reaches templates.

5. **Rank the threat hypotheses** by: confidence the weakness applies here, expected severity if present, fit with the user's skills, and ease of safe confirmation.

6. **For each top hypothesis, give a safe confirmation step** (a non-destructive check that distinguishes "vulnerable" from "not") and the prompt to use next (e.g., `bugbounty_injection_hunt.md`).

7. **CRITICAL — verify the profile is evidence-based:**
   - Confirm each hypothesis cites the fingerprint signal it rests on, and whether that signal is confirmed or inferred.
   - Do NOT claim a specific CVE/version is exploitable without a stated way to verify it on the live target.
   - Confirm confirmation steps are non-destructive and within RoE.
   - Down-rank hypotheses resting only on inferred fingerprints.

## False-Positive Prevention (MUST follow)
- ❌ Do NOT assert "this target is vulnerable to CVE-XXXX" from a version banner alone — banners lie and patches get backported.
- ❌ Do NOT list generic OWASP categories without tying them to the actual fingerprinted stack.
- ❌ Do NOT propose destructive confirmation steps (e.g., a payload that could corrupt data) — proof must be safe.
- ❌ Do NOT treat inferred fingerprints as confirmed when ranking.
- ✅ DO frame version-based findings as "check for X, confirm via Y."
- ✅ DO connect each weakness to the target's real functionality.
- ✅ DO give a safe, in-scope confirmation step per top hypothesis.

## Output Format
```
## Authorization Note
[In-scope only; hypothesis list, not a finding]

## Stack Summary
| Component | Value | Confirmed/Inferred |

## Threat Hypotheses (ranked)
| Rank | Hypothesis | Based on (signal) | Expected severity | Safe confirmation step | Next prompt |

## Version/CVE Notes (verify before claiming)
- [component vX] → check for [class]; confirm by [safe method]; do not assume present.

## Self-Audit
[Each hypothesis cites a signal; no unverified CVE claims; confirmations are safe + in-scope]
```

## Example Output
```
## Authorization Note
For in-scope api.acme.com / app.acme.com only. This is a prioritized list of what to check, not findings.

## Stack Summary
| Component | Value | C/I |
|-----------|-------|-----|
| Server | nginx | Confirmed |
| API | Node/Express + GraphQL | Confirmed |
| Frontend | React | Confirmed |
| Auth | Auth0 (OIDC) | Inferred (login redirect) |
| Cloud | AWS (S3 + metadata signals) | Inferred |

## Threat Hypotheses (ranked)
| Rank | Hypothesis | Signal | Severity | Safe confirmation | Next prompt |
|------|-----------|--------|----------|-------------------|-------------|
| 1 | BOLA/IDOR on object endpoints | Express REST w/ numeric IDs | High | request another test account's object ID with own session | access_control_idol_hunt |
| 2 | GraphQL introspection + BFLA | /graphql present | Medium-High | send a minimal introspection query (if allowed) | api_graphql_hunt |
| 3 | SSRF via URL-import feature | server-side fetch in import flow | High | point import at a benign collaborator host you control | ssrf_hunt |
| 4 | OAuth redirect_uri / state issues | Auth0 OIDC (inferred) | Medium | inspect redirect_uri validation with own account | authentication_session_hunt |

## Version/CVE Notes (verify before claiming)
- Express version not exposed; do not assume any Express CVE. If a specific middleware version leaks,
  check its known issue class and confirm behavior on the live endpoint before reporting.

## Self-Audit
Each hypothesis cites a fingerprint signal and marks inferred ones (Auth0, AWS); no CVE is claimed
present; all confirmation steps use the hunter's own accounts/collaborator and are non-destructive.
```

## Techniques Used
- **ST-01 (Clear Objective Statement)** — converts fingerprints into a ranked, testable hypothesis list.
- **RT-05 (Evidence-Based Reasoning)** — every hypothesis is tied to a named fingerprint signal.
- **DS-01 (Framework Application)** — applies a stack-component → characteristic-weakness mapping.
- **DS-06 (Prioritization Guidance)** — ranks hypotheses by confidence, severity, fit, and ease.
- **DD-07 (Self-Audit Table)** — verification blocks unverified CVE claims and unsafe confirmations.
