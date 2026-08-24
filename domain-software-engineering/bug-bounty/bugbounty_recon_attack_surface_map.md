---
title: "Recon & Attack-Surface Mapping"
category: bug-bounty/recon
description: "Plan and prioritize reconnaissance of an in-scope target: asset/subdomain/endpoint discovery and technology fingerprinting, organized into a ranked attack-surface map"
techniques:
  - ST-01
  - ST-02
  - DS-06
  - RT-02
  - DD-07
difficulty: intermediate
tags:
  - bug-bounty
  - reconnaissance
  - attack-surface
  - enumeration
  - fingerprinting
updated: "2026-06-18"
related_prompts:
  - domain-software-engineering/bug-bounty/bugbounty_program_scope_analyzer.md
  - domain-software-engineering/bug-bounty/bugbounty_tech_stack_threat_profile.md
  - domain-software-engineering/bug-bounty/bugbounty_cloud_infra_hunt.md
---

# Recon & Attack-Surface Mapping

**Objective:** Build a methodical, in-scope-only plan to discover and prioritize a target's attack surface, so hunting time goes to the assets most likely to yield bugs — not to whatever you find first.

## When to Use
- You've confirmed scope and need a recon plan before hunting.
- A wide-scope (wildcard) program needs to be reduced to a ranked list of where to look.
- You want recon organized around *what each asset enables*, not just a flat list of hosts.

## Inputs / Context
- **Confirmed in-scope assets** (from `bugbounty_program_scope_analyzer.md`).
- **RoE limits** on automated scanning / request volume.
- **Your strong vuln classes** (to weight prioritization).

## Instructions

1. **Authorization gate.** Re-confirm every asset you plan to enumerate is in scope and that the RoE permits the recon technique (passive vs. active, scanning volume). Out-of-scope subdomains discovered via wildcard recon are NOT testable — note them as "out of scope" and exclude them.

2. **Plan asset discovery** (methodology, in-scope only): subdomain enumeration of in-scope wildcards (passive sources first, then permitted active resolution), discovery of related hosts, and identification of which discovered hosts are actually in scope vs. third-party/excluded.

3. **Plan content & endpoint discovery** for each live in-scope host: directory/endpoint discovery, JavaScript file harvesting for hidden API routes/parameters, sitemap/robots, historical URLs, and parameter discovery — respecting volume limits.

4. **Plan technology fingerprinting:** web server, framework, CMS, frontend stack, CDN/WAF, auth provider, API style (REST/GraphQL/gRPC), and cloud provider signals. Note versions where observable (feeds the threat profile).

5. **Identify functionality surfaces:** authentication, file upload, payment, search, admin areas, multi-tenant boundaries, integrations/webhooks, and API endpoints — the places bugs concentrate.

6. **Rank the attack surface** by likely yield: weight by (a) functionality richness, (b) match to your strong classes, (c) apparent freshness/obscurity (less-trafficked endpoints = fewer prior hunters), and (d) sensitivity of data handled.

7. **CRITICAL — verify the map before hunting:**
   - Confirm every host in the map is in scope; move third-party/excluded hosts to an explicit "OUT OF SCOPE — do not test" list.
   - Confirm planned techniques respect RoE volume/automation limits.
   - Confirm the ranking is justified by stated factors, not just enumerated order.
   - Distinguish *observed* facts from *assumed* ones (mark fingerprints you're inferring).

## False-Positive Prevention (MUST follow)
- ❌ Do NOT include wildcard-discovered subdomains in the testable surface without confirming they're in scope and not third-party-hosted.
- ❌ Do NOT recommend high-volume automated scanning if the RoE forbids or limits it.
- ❌ Do NOT assert a technology/version as fact when it's inferred from weak signals — mark it as inferred.
- ❌ Do NOT rank by discovery order; rank by likely yield with stated reasons.
- ✅ DO separate in-scope from out-of-scope hosts explicitly.
- ✅ DO prioritize functionality-rich, fresh, sensitive surfaces.
- ✅ DO note which fingerprints are confirmed vs. inferred (they drive later hunting decisions).

## Output Format
```
## Authorization & RoE Check
[In-scope assets confirmed; scanning limits noted]

## Discovered In-Scope Hosts
| Host | Live? | Role | Tech (confirmed/inferred) |

## OUT OF SCOPE — Do Not Test
- [host] — reason (third-party / excluded)

## Functionality Surfaces
| Host | Surface (auth/upload/payment/admin/API/...) | Why interesting |

## Ranked Attack Surface
| Rank | Target | Likely vuln classes | Why ranked here |

## Recon Plan (in-scope, RoE-compliant)
1. ...

## Self-Audit
[Every mapped host is in scope; techniques within RoE]
```

## Example Output
```
## Authorization & RoE Check
In-scope: *.acme.com (excl. blog/status), api.acme.com. Active scanning allowed at low volume; no
aggressive fuzzing of production checkout.

## Discovered In-Scope Hosts
| Host | Live? | Role | Tech |
|------|-------|------|------|
| app.acme.com | yes | main SPA | React + REST api.acme.com (confirmed) |
| api.acme.com | yes | API | Node/Express; /graphql present (confirmed) |
| admin.acme.com | yes | internal admin | login gate; framework inferred Rails (inferred) |
| legacy.acme.com | yes | old portal | PHP (confirmed via headers) — looks unmaintained |

## OUT OF SCOPE — Do Not Test
- blog.acme.com — third-party (WordPress.com hosted), excluded by policy
- cdn.acme.com — third-party CDN

## Functionality Surfaces
| Host | Surface | Why interesting |
|------|---------|-----------------|
| api.acme.com | object CRUD endpoints, GraphQL | IDOR/BOLA candidate |
| app.acme.com | file upload (avatars, docs) | upload + parsing bugs |
| legacy.acme.com | login, password reset | unmaintained → auth/injection candidates |

## Ranked Attack Surface
| Rank | Target | Likely classes | Why |
|------|--------|----------------|-----|
| 1 | api.acme.com objects | IDOR/BOLA | matches your strength; rich object model; fresh API scope |
| 2 | legacy.acme.com | injection, auth | unmaintained, low-traffic → fewer prior hunters |
| 3 | app.acme.com upload | file upload, SSRF-via-import | sensitive functionality |

## Recon Plan (in-scope, RoE-compliant)
1. Passive subdomain enumeration of *.acme.com; classify each as in/out of scope.
2. Harvest JS on app.acme.com for hidden api.acme.com routes/params.
3. Fingerprint each live host (server, framework, auth, API style).
4. Map object-ID-bearing endpoints on api.acme.com for the IDOR hunt.

## Self-Audit
All mapped/testable hosts are in scope; blog/cdn moved to out-of-scope list; no high-volume scanning of
checkout planned.
```

## Techniques Used
- **ST-01 (Clear Objective Statement)** — recon framed as building a *ranked, in-scope* surface map.
- **ST-02 (Structured Sequential Instructions)** — discovery → fingerprint → functionality → rank → plan.
- **DS-06 (Prioritization Guidance)** — explicit ranking by likely yield with reasons.
- **RT-02 (Multi-Dimensional Analysis)** — weights functionality, fit, freshness, and data sensitivity.
- **DD-07 (Self-Audit Table)** — verification re-checks scope and RoE compliance before hunting.
