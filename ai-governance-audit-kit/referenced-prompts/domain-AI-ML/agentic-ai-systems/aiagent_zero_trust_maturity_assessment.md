---
title: "AI Agent Zero Trust Maturity Assessment"
category: AI-ML/agentic-ai-systems
description: "Assess an agent deployment's security maturity against a three-tier Zero Trust model across eight control domains, surface the per-domain gap, and name the single highest-leverage next move."
techniques:
  - ST-47
  - AG-44
  - ST-02
  - CM-02
  - QA-08
difficulty: advanced
tags:
  - zero-trust
  - maturity-model
  - agent-security
  - governance
  - blast-radius
updated: "2026-06-19"
related_prompts:
  - domain-AI-ML/agentic-ai-systems/aiagent_safety_sandboxing.md
  - domain-AI-ML/agentic-ai-systems/aiagent_runtime_guardrails_policy.md
  - domain-AI-ML/agentic-ai-systems/aiagent_privacy_data_governance.md
---

# AI Agent Zero Trust Maturity Assessment

**Objective:** Score an agent deployment against a three-tier Zero Trust maturity model (Foundation → Enterprise → Advanced) across eight control domains, where each tier strengthens — never replaces — the one below it, and produce a per-domain current tier, a gap report, and the single highest-leverage next move.

**When to Use:**
- You operate one or more agents that take real actions or touch sensitive data and want to know where your security posture actually sits.
- You face compliance pressure (HIPAA, FINRA, GDPR, FedRAMP, EU AI Act, ISO 42001) that already imposes Zero-Trust-aligned requirements.
- You need to prioritize a security roadmap and justify investment by blast radius rather than by checklist completeness.

**When NOT to Use:**
- The agent is a throwaway prototype with no production credentials and no untrusted input — note that conclusion and revisit before any real deployment.
- You only need per-tool scoping (use `aiagent_least_agency_scoping.md`) or a runtime policy layer (use `aiagent_runtime_guardrails_policy.md`).

**Source:** Framework adapted from Anthropic "Zero Trust for AI Agents" (2026), a vendor report, plus NIST SP 800-207 and the CISA Zero Trust Maturity Model — facts attributed inline; no source text reproduced.

## Inputs / Context

Provide what you can; the assessment degrades gracefully if some are missing:
- **Deployment profile** — how many agents, what they do, who relies on them, expected scale.
- **Stakes & blast radius** — worst-case impact if an agent or its tools were hijacked.
- **Current controls per domain** — how identity, access, observability, monitoring, I/O validation, integrity/recovery, governance policy, and supply chain are handled today.
- **Regulatory context** — frameworks or contractual obligations in scope (and any 2027 federal Zero Trust adoption deadline that applies).
- **Adversary profile** — opportunistic vs. sophisticated/targeted threat actors.

## Constraints

**Must:**
- Anchor every judgment to the three foundational Zero Trust principles — never trust / always verify, assume breach, and least privilege — and treat them as the lens, not as separate scores.
- Score each of the eight control domains independently against the three tiers, respecting the "raised floor": some controls that once passed no longer qualify as even Foundation.
- Apply the impossible-vs-tedious test to every control: a control that merely adds friction (an attacker can still get through, just slower) does not count as a real control.

**Must Not:**
- Award a higher tier in a domain while a lower-tier prerequisite in that same domain is missing — tiers stack, they do not substitute.
- Treat static API keys, SMS-based MFA, or friction-only controls as acceptable Foundation — the raised floor disqualifies them.
- Recommend more than one "highest-leverage next move" — the value is in forcing a single priority.

**Instructions:**

1. **Establish the foundational lens.** Restate the three principles (never trust/always verify; assume breach; least privilege) and confirm they will be applied to every domain, then record the deployment's stakes, scale, and blast radius.

2. **Select the target tier.** Choose by stakes and blast radius: Foundation for small teams and initial deployments; Enterprise for most organizations operating at scale; Advanced for highly regulated, national-security, or sophisticated-adversary contexts. State why.

3. **Apply the raised floor.** Verify the deployment clears the new minimum bar before scoring anything as Foundation — short-lived identity-provider tokens (no static API keys anywhere), cryptographically-rooted persistent agent identity, identity-based isolation, sandboxing for any agent processing untrusted input, automated first-pass alert triage, and FIDO2/passkeys for human authentication.

4. **Score the eight control domains.** For each, assign current tier and note the evidence: (1) agent identity & authentication; (2) access control & privilege management; (3) observability & auditing; (4) behavioral monitoring & response; (5) input validation & output controls; (6) integrity & recovery; (7) AI governance policies; (8) supply-chain integrity.

5. **Run the impossible-vs-tedious test per control.** For each control claimed, ask whether it makes the attack impossible or merely tedious. Downgrade any control that only slows an attacker.

6. **Run the two acid tests.** Answer plainly: "Would we know within an hour if an agent went rogue?" and "Can the team take time off without worrying about undetected agent misbehavior?" A "no" to either marks a real gap regardless of domain scores.

7. **Map compliance pressure.** Note which in-scope frameworks (HIPAA, FINRA, GDPR, FedRAMP, EU AI Act, ISO 42001) already require Zero-Trust-aligned controls, and flag the federal-agency Zero Trust adoption deadline (2027) where relevant.

8. **Name the single highest-leverage next move.** From the gaps, choose the one change that most reduces blast radius or closes an acid-test failure. Justify it over the runners-up.

**Output Format:**

A markdown maturity assessment:
- **Deployment Profile & Target Tier** — stakes, blast radius, chosen tier + rationale
- **Raised-Floor Check** — pass/fail on each new Foundation minimum
- **Domain Scorecard** — table: Domain | Current Tier | Evidence | Gap to target
- **Acid-Test Results** — the two readiness questions answered
- **Compliance Mapping** — frameworks in scope and what they require
- **Highest-Leverage Next Move** — one move, with justification over alternatives
- **INSUFFICIENT EVIDENCE** — an enumerated Current Tier value. A domain whose controls are described in a design document but never exercised has not demonstrated a tier; the assessment routinely mistakes intended architecture for enforced architecture. Name the unblocking datum: the enforcement evidence — a denied action in a log, a policy test, a rejected credential.

## Verification

- [ ] All three foundational principles are applied as the lens across every domain.
- [ ] All eight control domains are scored with evidence, not assertion.
- [ ] The raised floor is checked; static keys, SMS MFA, and friction-only controls are not counted as Foundation.
- [ ] No domain is scored above a tier whose lower-tier prerequisite is unmet.
- [ ] Both acid-test questions are answered explicitly.
- [ ] Exactly one highest-leverage next move is named and justified.
- [ ] Domains whose tier rests on design documents rather than exercised controls are scored INSUFFICIENT EVIDENCE, with the enforcement evidence named.

## False-Positive Prevention

❌ **DON'T:**
- Mark a domain "Enterprise" because one flashy control exists while the Foundation prerequisites under it are missing.
- Count a control that only slows an attacker (friction) as a passed control.
- Treat "we have MFA" as sufficient without checking it is FIDO2/passkeys rather than SMS.
- Produce a roadmap of ten priorities — that is the absence of a priority.

✅ **DO:**
- Require lower-tier prerequisites before crediting a higher tier in the same domain.
- Apply the impossible-vs-tedious test to each control and downgrade friction-only ones.
- Verify human auth and agent identity meet the raised floor specifically.
- Force the single highest-leverage move and defend it against the runners-up.

## Example Output

```markdown
## Zero Trust Maturity Assessment: Customer-Ops Agent Fleet

### Deployment Profile & Target Tier
12 agents handling refunds and account changes at scale; blast radius = unauthorized
payouts + PII exposure. Target tier: Enterprise (most-orgs-at-scale + FINRA exposure).

### Raised-Floor Check
- Short-lived IdP tokens: FAIL (one tool still uses a static API key)
- Persistent cryptographic agent identity: PASS
- Identity-based isolation: PARTIAL
- Sandboxing for untrusted input: FAIL (email-parsing agent unsandboxed)
- Automated first-pass alert triage: PASS
- FIDO2/passkeys for humans: FAIL (SMS MFA in use)

### Domain Scorecard
| Domain | Current Tier | Evidence | Gap to target |
|---|---|---|---|
| Identity & auth | Below Foundation | static key + SMS MFA | replace both |
| Access control | Foundation | scoped per agent | add JIT elevation |
| Observability & auditing | Enterprise | full action logs | meets target |
| Behavioral monitoring | Foundation | triage only | add anomaly response |
| Input/output controls | Below Foundation | unsandboxed parser | sandbox it |
| Integrity & recovery | Foundation | backups exist | add tamper detection |
| Governance policies | Foundation | written policy | add review cadence |
| Supply-chain integrity | Foundation | pinned deps | add provenance checks |

### Acid-Test Results
- Rogue within an hour? No — email-parser actions are not anomaly-monitored.
- Team can take leave safely? No — same gap.

### Compliance Mapping
FINRA + GDPR both require ZT-aligned access and audit controls; the static key and SMS
MFA are likely audit findings today.

### Highest-Leverage Next Move
Sandbox the email-parsing agent and route its actions through behavioral monitoring.
It closes both acid-test failures at once — higher leverage than the key/MFA swaps,
which are urgent but do not by themselves restore "would we know within an hour."
```

**Techniques Used:**
- **ST-47 (Maturity / Capability Model):** scores the deployment against the three stacked Zero Trust tiers.
- **AG-44 (Agent Threat / Risk Assessment):** ties tier selection and priority to blast radius and adversary profile.
- **ST-02 (Structured Sequential Instructions):** lens → tier → raised floor → domain scoring → priority.
- **CM-02 (Constraint Specification):** the raised floor and tier-stacking rules are the governing constraints.
- **QA-08 (Self-Audit / Acid-Test Checks):** the two readiness questions force an honest detection-capability check.

**Related Prompts:**
- `aiagent_safety_sandboxing.md` — the containment that domains 4–6 of this model assess.
- `aiagent_runtime_guardrails_policy.md` — the enforcement layer behind the governance and I/O domains.
- `aiagent_privacy_data_governance.md` — the data-handling controls behind the compliance mapping.
