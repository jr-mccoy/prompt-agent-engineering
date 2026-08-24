# Bug Bounty Hunting

Prompts that support the **bug bounty hunter** workflow: choosing programs, reading scope, mapping
attack surface, hunting vulnerabilities by class, validating findings, scoring impact, building proofs
of concept, and writing the disclosure reports that get paid.

This is the **offensive-but-authorized** counterpart to `domain-software-engineering/analysis/security/`
(which is defensive — reviewing code *you own*). Bug bounty work is black-box testing of **live targets
you do not own the source for**, performed under a program that has granted explicit permission.

---

## ⚠️ Load-bearing convention: authorization + responsible disclosure

A bug bounty program is a **standing grant of permission** to test the assets it lists, under the rules
it publishes. That permission is the entire legal and ethical basis for this work. Every prompt in this
directory enforces the following, and you must too:

1. **Authorization gate.** Before producing any testing guidance, confirm the target is an **in-scope
   asset of a program you are authorized to test** (a public/private bug bounty program, a VDP, or a
   signed pentest engagement). No authorization → no testing. Testing systems you have not been
   permitted to test is illegal in most jurisdictions, regardless of intent.
2. **Stay in scope.** Never test out-of-scope assets, third-party services, or other customers' data.
   Out-of-scope findings are unpaid at best and a ban (or a referral) at worst.
3. **Non-destructive.** No denial-of-service or stress testing, no destructive payloads, no lateral
   movement, and **no data exfiltration beyond the minimal proof the program permits**. Respect the
   rules of engagement (RoE).
4. **Responsible disclosure.** Report through the program's official channel, follow its disclosure
   timeline, and do not publicly disclose or weaponize a finding.
5. **Methodology, not malware.** These prompts produce test *plans*, reasoning, severity assessments,
   and report drafts — not turnkey exploitation against arbitrary targets.

If a request would take you outside an authorized scope, stop and re-confirm authorization first.

---

## How to use this set

The prompts follow the natural lifecycle of a finding. A typical loop:

```
Pick a program → read its scope → recon the attack surface → hunt by vuln class
   → triage/validate → score impact → build a PoC → write the report → learn from the outcome
```

If you are new, start with **`bugbounty_getting_started_orientation.md`**. Before your first hunt, get
the *non-hacking* setup right: use **`bugbounty_platform_selection.md`** to pick a platform and earning
track (open bounty vs. vetted PTaaS/contractor work), and **`bugbounty_payment_kyc_operations.md`** to
clear KYC, tax, and payout so valid findings actually convert to money. Then run the scope analyzer on
your first program.

## Routing table

| You want to… | Prompt |
|---|---|
| Understand how bounty hunting works and plan a first 90 days | `bugbounty_getting_started_orientation.md` |
| Choose which platform(s) + earning track (bounty vs. PTaaS) to commit to | `bugbounty_platform_selection.md` |
| Set up payment / KYC / tax / invoicing so findings convert to money | `bugbounty_payment_kyc_operations.md` |
| Parse a program policy into in/out-of-scope + a compliant test plan | `bugbounty_program_scope_analyzer.md` |
| Decide which programs are worth your limited time (ROI) | `bugbounty_program_selection_roi.md` |
| Map and prioritize a target's attack surface | `bugbounty_recon_attack_surface_map.md` |
| Turn a fingerprinted tech stack into a ranked threat profile | `bugbounty_tech_stack_threat_profile.md` |
| Hunt broken access control / IDOR / privilege escalation | `bugbounty_access_control_idor_hunt.md` |
| Hunt authentication / session / OAuth / JWT / MFA flaws | `bugbounty_authentication_session_hunt.md` |
| Hunt SSRF (incl. cloud metadata, internal services) | `bugbounty_ssrf_hunt.md` |
| Hunt injection (SQLi / command / SSTI / NoSQL) | `bugbounty_injection_hunt.md` |
| Hunt XSS (reflected / stored / DOM) and escalate impact | `bugbounty_xss_hunt.md` |
| Hunt business-logic flaws (low duplicate, high payout) | `bugbounty_business_logic_hunt.md` |
| Test REST/GraphQL APIs (BOLA/BFLA, mass assignment, introspection) | `bugbounty_api_graphql_hunt.md` |
| Test a mobile app and its backend | `bugbounty_mobile_app_hunt.md` |
| Hunt cloud/infra issues (subdomain takeover, exposed secrets) | `bugbounty_cloud_infra_hunt.md` |
| Validate a finding and kill false positives before reporting | `bugbounty_finding_triage_validation.md` |
| Score severity (CVSS) and articulate business impact | `bugbounty_severity_cvss_impact.md` |
| Build a minimal, safe, reproducible proof of concept | `bugbounty_poc_builder.md` |
| Write a high-signal disclosure report | `bugbounty_disclosure_report_writer.md` |
| Build a measurable skill-development plan | `bugbounty_skill_development_plan.md` |
| Run a post-mortem on an accepted/rejected/duplicate report | `bugbounty_report_postmortem.md` |

## Conventions for these prompts

All prompts here are Tier-1: complete YAML frontmatter, numbered instructions, a CRITICAL verification
step, a False-Positive Prevention block, a locked output format, an example output, and 3–5 listed
techniques. Every prompt opens with the authorization/scope gate described above.

**Related (defensive) resources:** `domain-software-engineering/analysis/security/`,
`domain-software-engineering/testing/testing_security_testing.md`,
`domain-software-engineering/testing/testing_property_based_fuzzing.md`.
