---
title: "Bug Bounty Program Scope Analyzer"
category: bug-bounty/scope
description: "Parse a bug bounty program policy into in-scope/out-of-scope assets, rules of engagement, and payout tiers, then produce a compliant test plan with a hard authorization gate"
techniques:
  - ST-01
  - ST-02
  - DS-01
  - QA-02
  - DD-07
difficulty: intermediate
tags:
  - bug-bounty
  - scope
  - rules-of-engagement
  - authorization
  - test-plan
updated: "2026-06-18"
related_prompts:
  - domain-software-engineering/bug-bounty/bugbounty_recon_attack_surface_map.md
  - domain-software-engineering/bug-bounty/bugbounty_program_selection_roi.md
  - domain-software-engineering/bug-bounty/bugbounty_getting_started_orientation.md
---

# Bug Bounty Program Scope Analyzer

**Objective:** Turn a program's published policy into an unambiguous map of what you may test, how you may test it, and what it pays — and a test plan that provably stays inside that boundary.

## When to Use
- You are about to start on a program and need to extract scope, RoE, and payout structure from its policy.
- You want a checklist that prevents accidental out-of-scope or rule-violating testing.
- You need to translate a wall of policy text into a prioritized, compliant test plan.

## Inputs / Context
- **The program policy text** (paste the scope, rules, and reward sections — or the full policy).
- **Platform** (HackerOne / Bugcrowd / Intigriti / YesWeHack / self-hosted), if known.
- **Your intended focus** (e.g., access control, API, mobile), if you have one.

## Instructions

1. **Authorization gate (do this first).** Confirm the source: is this a real program policy the user is permitted to act on (public program, private invite, or VDP)? If the policy text is missing, partial, or the user cannot confirm they are enrolled/permitted, STOP and request it. Do not produce a test plan from assumptions about scope.

2. **Extract in-scope assets** verbatim, organized by type: web domains/wildcards, API hosts, mobile apps (with store links/package IDs), source repos, cloud assets, hardware. Preserve exact hostnames and wildcard semantics (`*.example.com` vs `example.com`).

3. **Extract out-of-scope assets and exclusions** verbatim, including out-of-scope *vulnerability types* (e.g., "no self-XSS," "no missing security headers," "no rate-limiting reports," "no clickjacking on unauthenticated pages"). These are the most common cause of unpaid reports.

4. **Extract the rules of engagement (RoE):** allowed/forbidden testing techniques, automated-scanning rules, account-creation rules, test-account/marker requirements, data-handling limits, required user-agent or header tags, and any prohibition on DoS/social-engineering/physical testing.

5. **Extract the reward structure:** severity tiers and bounty ranges, what determines tier (CVSS? program-specific?), bonus criteria, and duplicate/first-reporter policy.

6. **Flag ambiguities and risk traps:** wildcard scope that may include third-party-hosted subdomains, assets that look in-scope but are excluded, vuln types explicitly not rewarded, and any disclosure-timeline obligations.

7. **Produce a compliant, prioritized test plan:** map the user's focus (or a sensible default) onto in-scope assets, listing what to test, what is explicitly forbidden, and the safety markers/limits to apply.

8. **CRITICAL — verify the plan cannot stray out of scope:**
   - Re-check every asset in the test plan against the in-scope list (exact-match or wildcard-match).
   - Confirm no test-plan item targets an out-of-scope asset or an out-of-scope vuln type.
   - Confirm RoE constraints (markers, scanning limits, data limits) are reflected in the plan.
   - Where scope is ambiguous, mark the item **"CONFIRM WITH PROGRAM"** rather than assuming it is allowed.

## False-Positive Prevention (MUST follow)
- ❌ Do NOT infer that an asset is in scope because it "belongs to the company" — only the listed assets are in scope.
- ❌ Do NOT treat a wildcard as unlimited; subdomains pointing to third parties or other tenants may be excluded.
- ❌ Do NOT omit out-of-scope *vulnerability types* — reporting them wastes effort and annoys triage.
- ❌ Do NOT produce a plan that ignores required test markers, scanning limits, or data-handling rules.
- ✅ DO quote scope and exclusions verbatim and cite which policy line each comes from.
- ✅ DO mark anything ambiguous as "CONFIRM WITH PROGRAM."
- ✅ DO reflect every RoE constraint as a concrete rule in the test plan.

## Output Format
```
## Authorization Check
[Confirmed permitted? If not, what's missing.]

## In-Scope Assets
| Asset | Type | Notes (wildcard semantics, caveats) |

## Out-of-Scope (Assets + Vuln Types)
- Assets: ...
- Vulnerability types NOT rewarded: ...

## Rules of Engagement
- Allowed: ...
- Forbidden: ...
- Required markers / limits: ...

## Reward Structure
| Severity | Range | Tier basis | Notes |

## Ambiguities & Risk Traps
- [ ] ... (CONFIRM WITH PROGRAM)

## Compliant Test Plan (prioritized)
| Priority | In-scope asset | What to test | Explicitly forbidden here | Safety markers |

## Self-Audit
[Confirmation that every plan item maps to an in-scope asset + allowed technique]
```

## Example Output
```
## Authorization Check
Confirmed: public HackerOne program, user enrolled. Policy text provided in full.

## In-Scope Assets
| Asset | Type | Notes |
|-------|------|-------|
| *.acme.com | Web (wildcard) | EXCLUDES blog.acme.com (third-party hosted) |
| api.acme.com | API host | REST + GraphQL at /graphql |
| Acme iOS app (id123) | Mobile | Backend = api.acme.com |

## Out-of-Scope (Assets + Vuln Types)
- Assets: blog.acme.com, status.acme.com, anything *.acme-staging.com
- Vuln types NOT rewarded: self-XSS, missing headers, rate-limiting, clickjacking on unauth pages,
  CSV injection, reports from automated scanners without manual validation.

## Rules of Engagement
- Allowed: manual testing, low-volume automated requests against api.acme.com.
- Forbidden: DoS/load testing, social engineering, physical, testing other users' real data.
- Required markers: prefix all test-account emails with "bbtest+"; add header X-Bug-Bounty: <handle>.

## Reward Structure
| Severity | Range | Tier basis | Notes |
|----------|-------|-----------|-------|
| Critical | $$$$ | CVSS 9.0+ | RCE, auth bypass affecting all users |
| High | $$$ | CVSS 7-8.9 | IDOR exposing PII |
| Medium | $$ | CVSS 4-6.9 | stored XSS in low-priv context |
| Low | $ | CVSS <4 | minor info leak |

## Ambiguities & Risk Traps
- [ ] Several *.acme.com subdomains resolve to a CDN/third party — CONFIRM WITH PROGRAM before testing.
- [ ] GraphQL introspection state unclear — treat findings as "needs confirmation."

## Compliant Test Plan (prioritized)
| Priority | Asset | What to test | Forbidden here | Safety markers |
|----------|-------|--------------|----------------|----------------|
| 1 | api.acme.com | IDOR/BOLA on object endpoints | no high-volume scanning | bbtest+ accounts, header tag |
| 2 | app.acme.com | broken access control between roles | no DoS | two test accounts |
| 3 | api.acme.com/graphql | BFLA, introspection (confirm) | — | header tag |

## Self-Audit
Every plan item targets a listed in-scope asset (api/app.acme.com), avoids the excluded blog/status
hosts, avoids all not-rewarded vuln types, and applies the required test markers and volume limits.
```

## Techniques Used
- **ST-01 (Clear Objective Statement)** — objective is a provably in-scope plan, not just a summary.
- **ST-02 (Structured Sequential Instructions)** — extract scope → RoE → rewards → plan, in order.
- **DS-01 (Framework Application)** — applies a consistent scope/RoE/reward taxonomy to any policy.
- **QA-02 (Adversarial Thinking)** — the risk-traps step hunts for the ways scope is commonly misread.
- **DD-07 (Self-Audit Table)** — the verification step re-checks every plan item against scope.
