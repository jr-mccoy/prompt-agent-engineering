---
title: "SSRF Hunting"
category: bug-bounty/hunting
description: "Black-box test plan for server-side request forgery on in-scope targets: discovery via server-side fetch features, safe out-of-band confirmation, and impact escalation to cloud metadata or internal services"
techniques:
  - ST-01
  - ST-02
  - QA-02
  - RT-05
  - DD-07
difficulty: advanced
tags:
  - bug-bounty
  - ssrf
  - cloud-metadata
  - out-of-band
  - escalation
updated: "2026-06-18"
related_prompts:
  - domain-software-engineering/bug-bounty/bugbounty_cloud_infra_hunt.md
  - domain-software-engineering/bug-bounty/bugbounty_poc_builder.md
  - domain-software-engineering/bug-bounty/bugbounty_severity_cvss_impact.md
---

# SSRF Hunting

**Objective:** Find and safely confirm server-side request forgery on an in-scope target — where the application can be made to send requests to a destination of your choosing — and assess realistic escalation without crossing into out-of-scope internal systems or destructive actions.

## When to Use
- The target has features that fetch URLs server-side: webhooks, URL preview/unfurl, document/image import, PDF/HTML rendering, integrations, or "import from URL."
- You suspect a parameter is fetched by the server and want to confirm SSRF safely.
- You have a confirmed SSRF and need to assess escalation/impact responsibly.

## Inputs / Context
- **In-scope endpoints** that accept URLs or hostnames.
- **An out-of-band (OOB) collaborator host you control** (DNS/HTTP logging) for safe confirmation.
- **RoE limits** and the program's stance on internal-network/metadata testing (some restrict it — check).

## Instructions

1. **Authorization gate.** Confirm the endpoint is in scope. SSRF can reach internal infrastructure; **do not** pivot into systems or networks outside the program's scope, and respect any RoE that limits metadata/internal testing. Use a collaborator host *you control* for confirmation — never a third party's server.

2. **Identify candidate sinks:** any parameter that becomes a server-side request — full URLs, hostnames, IPs, or even file paths/schemes. Check webhooks, import-from-URL, link preview, avatar-by-URL, XML/SVG/PDF processors (XXE-adjacent), and integration callbacks.

3. **Confirm out-of-band first (safest signal):** point the parameter at your collaborator host and watch for an inbound DNS/HTTP hit from the target's infrastructure. An OOB callback is strong, non-intrusive proof the server made the request.

4. **Probe blind vs. full SSRF:** determine whether you get the response back (full SSRF) or only an OOB signal (blind). Test redirect-following, supported schemes (`http`, `https`, `gopher`, `file`, `dict`), and response reflection.

5. **Assess escalation responsibly:** consider what an SSRF *could* reach (cloud metadata endpoints, internal-only services, link-local addresses) and demonstrate the *minimum* needed to prove impact — e.g., a single benign read of a metadata path *if the program permits it*. Do not enumerate internal networks or exfiltrate credentials beyond minimal proof; document what's reachable rather than fully exploiting it.

6. **Test filter bypasses** that re-open patched SSRF: alternate IP encodings (decimal/octal/hex), `[::]`/IPv6, DNS rebinding, redirect chains, and `@`/userinfo tricks — only to confirm the bypass, not to reach further.

7. **CRITICAL — verify the finding and bound the impact:**
   - Confirm the OOB hit originated from the target's infrastructure (correlate timing/source), not your own client.
   - Distinguish full SSRF (response returned) from blind SSRF (OOB only) — they score differently.
   - For escalation, document *reachability* with minimal proof; do not over-exploit.
   - Confirm you stayed within scope and RoE (no internal-network roaming).
   - Assign confidence (High/Med/Low) and note what would change it.

## False-Positive Prevention (MUST follow)
- ❌ Do NOT call a finding SSRF because a URL field exists — confirm the *server* (not your browser) made the request.
- ❌ Do NOT pivot through an SSRF into out-of-scope internal systems or other tenants.
- ❌ Do NOT dump cloud credentials or roam the internal network — minimal proof of reachability only.
- ❌ Do NOT use a third party's server as your collaborator; use infrastructure you control.
- ✅ DO confirm via an OOB callback correlated to the target's infrastructure.
- ✅ DO classify blind vs. full SSRF accurately.
- ✅ DO bound escalation to the minimum proof and document the rest.

## Output Format
```
## Authorization & Scope Note
[In-scope endpoint; collaborator host you control; metadata/internal RoE stance]

## Candidate Sinks Tested
| Endpoint | Parameter | Server-side fetch? | OOB hit? | Type (blind/full) |

## Verified Finding
### SSRF on [endpoint] — confidence: High/Med/Low
- Confirmation: OOB callback from [target infra] at [time], correlated to my request.
- Type: blind / full (response returned: yes/no)
- Reachability (minimal proof): ...
- Impact bound: [what it could reach vs. what I demonstrated]
- What would change confidence: ...

## Escalation Assessment (documented, not over-exploited)
- Potentially reachable: ...
- Demonstrated (minimal): ...

## Self-Audit
[Server-made request confirmed; stayed in scope; minimal-proof escalation]
```

## Example Output
```
## Authorization & Scope Note
In-scope: api.acme.com/v1/import?url=. Collaborator: oob.myhandle.example (I control it). Program allows
confirming metadata reachability with a single benign read; no internal roaming.

## Candidate Sinks Tested
| Endpoint | Param | Server fetch? | OOB hit? | Type |
|----------|-------|---------------|----------|------|
| /v1/import | url | yes | yes (DNS+HTTP from AWS egress IP) | blind |
| /v1/avatar | url | only client-side preview | no | n/a |

## Verified Finding
### Blind SSRF on POST /v1/import?url= — confidence: High
- Confirmation: setting url=http://oob.myhandle.example/abc produced an inbound HTTP request to my
  collaborator from an AWS egress IP within 2s of my request — correlated by unique path token.
- Type: blind (response body not returned to me).
- Reachability (minimal proof): url=http://169.254.169.254/latest/meta-data/ returned HTTP 200 length
  in the app's status field, indicating the metadata service is reachable. I did NOT read credentials.
- Impact bound: could likely reach instance metadata/internal services; I demonstrated only reachability.
- What would change confidence: if the OOB hit came from my own browser — confirmed it was server-side
  (AWS IP, no client involvement).

## Escalation Assessment (documented, not over-exploited)
- Potentially reachable: 169.254.169.254 metadata, internal http services.
- Demonstrated (minimal): metadata endpoint returns 200; stopped before any credential path.

## Self-Audit
Server-side origin confirmed via collaborator I control; remained within api.acme.com scope; proved
metadata reachability with one benign request and did not exfiltrate credentials.
```

## Techniques Used
- **ST-01 (Clear Objective Statement)** — defines SSRF as server-made requests to attacker-chosen destinations.
- **ST-02 (Structured Sequential Instructions)** — sinks → OOB confirm → blind/full → bounded escalation → bypasses.
- **QA-02 (Adversarial Thinking)** — filter-bypass step mirrors how SSRF protections are evaded.
- **RT-05 (Evidence-Based Reasoning)** — proof requires an OOB callback correlated to target infrastructure.
- **DD-07 (Self-Audit Table)** — verification bounds escalation and confirms scope/RoE compliance.
