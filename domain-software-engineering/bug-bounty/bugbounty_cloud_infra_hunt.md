---
title: "Cloud & Infrastructure Hunting"
category: bug-bounty/hunting
description: "Black-box test plan for in-scope cloud/infra exposure: subdomain takeover, exposed storage and secrets, CORS misconfiguration, and secrets leaked in client-side code"
techniques:
  - ST-01
  - ST-02
  - QA-02
  - RT-05
  - DD-07
difficulty: advanced
tags:
  - bug-bounty
  - cloud
  - subdomain-takeover
  - exposed-secrets
  - cors
updated: "2026-06-18"
related_prompts:
  - domain-software-engineering/bug-bounty/bugbounty_recon_attack_surface_map.md
  - domain-software-engineering/bug-bounty/bugbounty_ssrf_hunt.md
  - domain-software-engineering/bug-bounty/bugbounty_finding_triage_validation.md
---

# Cloud & Infrastructure Hunting

**Objective:** Find externally-observable cloud and infrastructure exposure on in-scope assets — dangling DNS, public storage, leaked secrets, and permissive CORS — and confirm each safely, without touching out-of-scope cloud accounts or other tenants.

## When to Use
- Recon surfaced DNS records, cloud-hosted assets, or client-side code worth auditing.
- The program scope includes cloud assets or wildcard domains that may have dangling records.
- You want quick, high-confidence wins (subdomain takeover, exposed buckets) that are easy to prove.

## Inputs / Context
- **In-scope domains/subdomains and cloud assets** (from recon).
- **Client-side bundles** (JS) for the in-scope apps.
- **RoE limits** — and a clear understanding that you may only act on the *program's* assets, never another customer's cloud resources.

## Instructions

1. **Authorization gate.** Confirm assets are in scope. Cloud findings can blur boundaries — you may only claim/test resources that belong to the **program**. Do NOT register/claim infrastructure or access cloud accounts that aren't clearly the in-scope target's, and never read other tenants' data. For storage, prove *exposure* with minimal access, not bulk download.

2. **Subdomain takeover:** for in-scope subdomains with dangling DNS (CNAME to a deprovisioned service — storage bucket, PaaS app, CDN), confirm the fingerprint of an unclaimed service. **Prove safely:** demonstrate the dangling pointer and the takeover *possibility*; only claim the resource if the program explicitly permits, and if you do, host a benign proof page, never malicious content.

3. **Exposed storage:** check in-scope cloud storage (buckets/blobs) for public list/read/write. Confirm with a single benign object access (or a benign write to a uniquely-named test object if read isn't enough and the program allows) — do NOT enumerate/download all contents.

4. **Secrets in client-side code:** grep in-scope JS bundles and responses for API keys, tokens, cloud credentials, and internal endpoints. Verify whether a found secret is *live and privileged* against an in-scope asset before reporting (many client keys are intentionally public).

5. **CORS misconfiguration:** test whether sensitive in-scope endpoints reflect arbitrary `Origin` with `Access-Control-Allow-Credentials: true`, enabling cross-origin theft of authenticated data. Confirm with a request showing the reflected origin + credentials combination.

6. **Other infra exposure:** open `.git`/`.env`/backup files, exposed dashboards/metrics, verbose server headers, and misconfigured caches — confirm sensitivity before reporting.

7. **CRITICAL — verify exposure and ownership, minimally:**
   - Confirm the asset is the program's (not a third party/other tenant) before any interaction.
   - For takeover, confirm the dangling record + unclaimed service; bound the proof to a benign demonstration.
   - For storage/secrets, confirm real, sensitive exposure with the *minimum* access; never bulk-extract.
   - For CORS, confirm the reflected-origin + credentials combination actually returns sensitive data cross-origin.
   - Assign confidence (High/Med/Low) and note what would change it.

## False-Positive Prevention (MUST follow)
- ❌ Do NOT claim/register infrastructure or access cloud accounts unless they're clearly the in-scope target's and the program permits it.
- ❌ Do NOT report a "public bucket" without confirming it holds sensitive data and belongs to the target — and never download it all.
- ❌ Do NOT report a client-side key as a leak without verifying it's live and privileged (many are public by design).
- ❌ Do NOT report reflected-Origin CORS without `Allow-Credentials: true` AND sensitive data actually returned.
- ✅ DO confirm asset ownership before touching anything.
- ✅ DO prove exposure with minimal, benign access.
- ✅ DO verify secrets are actually privileged against an in-scope asset.

## Output Format
```
## Authorization & Ownership Note
[In-scope assets confirmed as the program's; minimal-proof stance]

## Checks & Results
| Area (takeover/storage/secrets/CORS/files) | Asset | Observation | Sensitive + owned? | Verdict |

## Verified Findings
### [Finding] — confidence: High/Med/Low
- What: ...
- Ownership confirmed: ...
- Proof (minimal): ...
- Impact: ...
- What would change confidence: ...

## Self-Audit
[Ownership confirmed; minimal proof; nothing out-of-scope claimed or bulk-extracted]
```

## Example Output
```
## Authorization & Ownership Note
In-scope: *.acme.com (excl. blog/cdn third-party), acme app JS. Minimal proof only; no bulk download.

## Checks & Results
| Area | Asset | Observation | Sensitive+owned? | Verdict |
|------|-------|-------------|------------------|---------|
| Takeover | promo.acme.com | CNAME → unclaimed PaaS app ("no app found") | yes, acme-owned DNS | VULN (possible) |
| Storage | acme-uploads bucket | public list of user uploads | yes, acme bucket | VULN |
| Secrets | app.js maps key | maps key restricted to acme referrer | public-by-design | not a finding |
| CORS | api.acme.com/v1/me | reflects Origin + Allow-Credentials:true | returns my profile cross-origin | VULN |

## Verified Findings
### Subdomain takeover of promo.acme.com — confidence: High
- What: promo.acme.com CNAMEs to a PaaS app slug that is unregistered (service shows "no such app").
- Ownership confirmed: the DNS record is under acme.com (in scope); the dangling target is unclaimed.
- Proof (minimal): documented the CNAME and the unclaimed-service fingerprint. Program permits claiming
  for proof; I registered the slug and served a benign page reading "bug bounty PoC – <handle>".
- Impact: an attacker could serve arbitrary content on an acme subdomain (phishing, cookie scoping, etc.).
- What would change confidence: if the slug were actually claimed by acme — confirmed it was not.

## Self-Audit
DNS record confirmed acme-owned and in scope; takeover proven with a benign page only; the maps key was
verified as intentionally public (not reported); no bucket contents bulk-downloaded.
```

## Techniques Used
- **ST-01 (Clear Objective Statement)** — targets externally-observable, ownership-bounded cloud exposure.
- **ST-02 (Structured Sequential Instructions)** — takeover → storage → secrets → CORS → files.
- **QA-02 (Adversarial Thinking)** — checks the misconfigurations attackers scan for first.
- **RT-05 (Evidence-Based Reasoning)** — requires verifying ownership and that secrets are actually live/privileged.
- **DD-07 (Self-Audit Table)** — verification enforces ownership confirmation and minimal, benign proof.
