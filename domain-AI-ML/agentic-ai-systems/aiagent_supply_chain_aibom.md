---
title: "AI Agent Supply Chain & AI-BOM Audit"
category: AI-ML/agentic-ai-systems
description: "Audit the supply chain of an agent system — software dependencies plus AI-specific components (models, datasets, fine-tuning) — by building an AI Bill of Materials, scoring dependency health, and sequencing remediation including build-vs-buy and vendoring decisions."
techniques:
  - ST-02
  - DS-06
  - CM-02
  - QA-08
  - AG-44
difficulty: advanced
tags:
  - supply-chain
  - ai-bom
  - dependency-health
  - model-provenance
  - signing
updated: "2026-06-19"
related_prompts:
  - domain-AI-ML/agentic-ai-systems/aiagent_safety_sandboxing.md
  - domain-AI-ML/agentic-ai-systems/aiagent_privacy_data_governance.md
  - domain-AI-ML/agentic-ai-systems/aiagent_deployment_serving_architecture.md
---

# AI Agent Supply Chain & AI-BOM Audit

**Objective:** Audit the full supply chain behind an agent system — both its software dependencies and its AI-specific components (models, training data, fine-tuning parameters) — by building an AI Bill of Materials (AI-BOM), automatically scoring dependency health, and producing a prioritized remediation sequence that includes build-vs-buy and "AI vendoring" decisions, so trust in third-party code and models is verified rather than assumed.

**When to Use:**
- The agent depends on third-party models, model hosts, datasets, or open-source packages whose provenance you have not verified.
- You are introducing tool/connector servers, or you want a recurring CI gate on supply-chain integrity.
- Before granting an agent production credentials that ride on top of unaudited dependencies.

**When NOT to Use:**
- The agent uses only first-party code and a single self-hosted, integrity-verified model with no external packages — note that conclusion and skip.
- You only need runtime sandboxing of actions (use `aiagent_safety_sandboxing.md`) or data-handling governance (use `aiagent_privacy_data_governance.md`).

**Source:** Framework adapted from Anthropic "Zero Trust for AI Agents" (2026), a vendor report — facts attributed inline; no source text reproduced.

## Inputs / Context

Provide what you can; the audit degrades gracefully if some are missing:
- **Dependency manifest / lockfile** — the resolved software dependency tree (direct and transitive).
- **Model inventory** — every model used, its provider/host, weights origin, and whether it was fine-tuned.
- **Dataset lineage** — training/fine-tuning data sources, licensing, and how they were ingested.
- **Tool/connector servers** — any third-party servers the agent talks to and where they run.
- **Build & deploy pipeline** — how artifacts are built, signed, and verified before and during production.
- **Vendor/FOSS posture** — provider security practices, update mechanisms, SLA (or absence of one), incident history.

## Constraints

**Must:**
- Build an AI-BOM that extends software composition analysis to AI: model provenance, training-dataset lineage, and fine-tuning parameters (OWASP's AI-BOM extends the CycloneDX ML-BOM).
- Score each dependency on objective health signals (OpenSSF Scorecard checks branch protection, fuzzing coverage, signed releases, and maintainer activity) and run that scoring in CI alongside AI-BOM generation.
- Verify cryptographic signatures at every stage through production AND at runtime — deploy-time-only verification misses later tampering.

**Must Not:**
- Treat a model from a major platform as trustworthy because it is popular — poisoned weights and backdoors are real and platform presence is not provenance.
- Depend on a tool/connector server you have not reviewed, self-hosted, signed yourself, and re-verify on every update.
- Patch every flagged item indiscriminately — narrow remediation with reachability so effort lands where it changes risk.

**Instructions:**

1. **Inventory software and AI components together.** Enumerate the dependency tree from the lockfile and, in the same pass, the AI-specific components: each model's provenance (weights origin, host), training-dataset lineage, and fine-tuning parameters. This combined list is the AI-BOM (OWASP AI-BOM extends the CycloneDX ML-BOM).

2. **Score dependency health automatically.** Run OpenSSF Scorecard (or equivalent) over each dependency, capturing branch protection, fuzzing coverage, signed releases, and maintainer activity. Wire this into CI next to AI-BOM generation so the picture refreshes on every build, not once a quarter.

3. **Audit the tree for redundancy.** Point a frontier model at the lockfile and ask which dependencies overlap — duplicate HTTP clients, redundant JSON parsers, etc. Removing duplicates cuts attack surface for no functional loss.

4. **Narrow remediation with reachability.** Fix the smallest set that actually matters: prioritize dependencies whose vulnerable paths are reachable from the agent. Pair fixes with continuous delivery plus regression tests so patches deploy fast rather than queuing.

5. **Decide build-vs-buy / AI vendoring per weak dependency.** For small, unmaintained, low-Scorecard dependencies, consider having a frontier model reimplement only the subset of functionality you actually use ("AI vendoring") instead of carrying the package. Treat this as a standard response, not an exotic one.

6. **Enforce signing with runtime verification.** Require cryptographic signing at every stage through production, and verify signatures at runtime — not only at deploy — so tampering introduced after deployment is caught.

7. **Assess vendors, FOSS, and tool/connector servers.** Review each provider's security practices, update mechanism, and incident history. For tool/connector servers, run and host them yourself on an immutable platform after verifying the code, sign it yourself, and re-verify on every update.

8. **Account for model supply-chain risk explicitly.** Flag poisoned weights and backdoors that persist through safety training (research shows roughly 250 malicious documents can backdoor a model), and note that around 100 malicious models have been found on major platforms — some initiating reverse shells on load. Record that most agent supply chains are mostly open source with no SLA.

**Output Format:**

A markdown supply-chain audit:
- **AI-BOM Table** — Component | Type (pkg/model/dataset) | Provenance/source | Version/hash | Signed? | Notes
- **Dependency-Health Triage** — Dependency | Scorecard signals | Reachable? | Risk | Action
- **Redundancy Findings** — overlapping dependencies and consolidation recommendation
- **Model Supply-Chain Risks** — provenance gaps, poisoning/backdoor exposure, mitigations
- **Signing & Verification Plan** — per-stage signing + runtime verification rules
- **Prioritized Remediation Sequence** — ordered list with build / buy / vendoring decision per item

## Verification

- [ ] The AI-BOM covers software dependencies AND model provenance, dataset lineage, and fine-tuning parameters.
- [ ] Dependency health is scored on objective signals and the scoring runs in CI.
- [ ] Redundant dependencies are identified and consolidation is proposed.
- [ ] Remediation is narrowed by reachability, not "patch everything."
- [ ] Signing is enforced at every stage AND verified at runtime, not just at deploy.
- [ ] Tool/connector servers are self-hosted, code-verified, self-signed, and re-verified on update.
- [ ] Model poisoning/backdoor exposure and the "no SLA" reality are stated.

## False-Positive Prevention

❌ **DON'T:**
- Equate "downloaded from a major model platform" with "trusted provenance" — malicious models have shipped there.
- Verify signatures only at deploy time and assume the artifact stays intact afterward.
- Patch every flagged CVE regardless of whether the vulnerable path is reachable.
- Pull in an unmaintained, low-Scorecard package just because it is convenient.

✅ **DO:**
- Establish provenance for every model and dataset, and treat unverified weights as potentially backdoored.
- Verify signatures at runtime as well as through the build pipeline.
- Use reachability to focus remediation on dependencies that can actually be exercised.
- Reimplement the small subset you use ("AI vendoring") for weak, unmaintained dependencies.

## Example Output

```markdown
## Supply-Chain Audit: Research-Assistant Agent

### AI-BOM Table
| Component | Type | Provenance/source | Version/hash | Signed? | Notes |
|---|---|---|---|---|---|
| summarizer-7b | model | self-hosted, weights from vendor X | sha256:ab… | yes (self-signed) | integrity re-verified at load |
| retrieval-emb | model | public platform | sha256:cd… | NO | provenance unverified — quarantine until checked |
| corpus-2026 | dataset | internal + 2 scraped feeds | manifest:ef… | n/a | scraped feeds = poisoning risk |
| http-client-a | pkg | npm/pypi | 4.2.1 | yes | duplicate of http-client-b |

### Dependency-Health Triage
| Dependency | Scorecard signals | Reachable? | Risk | Action |
|---|---|---|---|---|
| tiny-parser | no branch protection, no fuzzing, 1 maintainer, unsigned | yes | high | AI-vendor the 2 functions used |
| http-client-a | good | yes | low | consolidate onto http-client-b |

### Redundancy Findings
http-client-a and http-client-b both ship; standardize on b, drop a → removes one transitive tree.

### Model Supply-Chain Risks
retrieval-emb provenance unverified; ~100 malicious models seen on major platforms (some open reverse shells on load). Hold in quarantine; verify weights + host before use. Scraped corpus feeds carry poisoning risk (~250 malicious docs can backdoor a model).

### Signing & Verification Plan
Sign at build, publish, and deploy; verify signature + weight hash at runtime on every model/artifact load.

### Prioritized Remediation Sequence
1. Quarantine + verify retrieval-emb (BUY only after provenance verified). 2. AI-vendor tiny-parser (BUILD). 3. Consolidate http clients. 4. Wire Scorecard + AI-BOM into CI.
```

**Techniques Used:**
- **ST-02 (Structured Sequential Instructions):** inventory → health-score → redundancy → reachability → vendoring → signing → vendor review → model risk.
- **DS-06 (Prioritization & Severity Guidance):** reachability and Scorecard signals rank what to remediate first.
- **CM-02 (Constraint Specification):** AI-BOM coverage, runtime signature verification, and self-hosted tool servers are the governing constraints.
- **QA-08 (Evidence & Citation Requirements):** provenance, hashes, and Scorecard signals are the evidence each finding rests on.
- **AG-44 (Agent Supply-Chain Integrity):** the AI-BOM and signing/verification regime are the core deliverable.

**Related Prompts:**
- `aiagent_safety_sandboxing.md` — the runtime containment that bounds what a compromised dependency can reach.
- `aiagent_privacy_data_governance.md` — governs the datasets whose lineage this audit traces.
- `aiagent_deployment_serving_architecture.md` — the immutable platform on which verified, signed artifacts are served.
