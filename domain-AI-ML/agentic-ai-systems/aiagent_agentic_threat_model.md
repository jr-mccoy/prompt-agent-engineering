---
title: "Agentic AI System Threat Model"
category: AI-ML/agentic-ai-systems
description: "Build a defensive threat model for an agentic system using a five-category attack taxonomy, scoring each threat for applicability, likelihood, and impact, and attaching a concrete mitigation per applicable threat."
techniques:
  - RT-02
  - DS-06
  - AG-44
  - CM-02
  - QA-12
difficulty: advanced
tags:
  - threat-model
  - prompt-injection
  - tool-poisoning
  - memory-poisoning
  - supply-chain
updated: "2026-06-19"
related_prompts:
  - domain-AI-ML/agentic-ai-systems/aiagent_prompt_injection_untrusted_content_defense.md
  - domain-AI-ML/agentic-ai-systems/aiagent_failure_mode_analysis.md
  - domain-AI-ML/agentic-ai-systems/aiagent_safety_sandboxing.md
---

# Agentic AI System Threat Model

**Objective:** Produce a defensive threat model for a specific agentic system by walking a five-category agentic attack taxonomy, judging each threat's applicability to *this* system, scoring likelihood and impact, and attaching a concrete mitigation — so the security work is targeted, not generic.

**When to Use:**
- You are building or hardening an agent that processes external content, calls tools, retains memory, or depends on third-party models/frameworks.
- You need a structured, authorized review of how this specific system could be attacked.
- Before granting autonomy or production credentials, to drive the containment work.

**When NOT to Use:**
- The system is a closed, read-only agent with no untrusted input, no tools, and no external dependencies — note that narrow surface and stop.
- You only need the maturity score (use `aiagent_zero_trust_maturity_assessment.md`) or per-tool caps (use `aiagent_least_agency_scoping.md`).

**Source:** Framework adapted from Anthropic "Zero Trust for AI Agents" (2026), a vendor report, OWASP agentic threat taxonomy, and Anthropic research on backdoor persistence through safety training — facts attributed inline; no source text reproduced.

## Inputs / Context

This prompt is for defensive, authorized security review only. Provide what you can:
- **System architecture** — the agent loop, its tools, memory stores, and external dependencies.
- **Untrusted input surfaces** — web pages, emails, documents, third-party tool outputs the agent ingests.
- **Tool & connector inventory** — what each tool can do and where its descriptors come from.
- **Memory & retrieval** — vector stores, shared/multi-tenant context, long-term memory.
- **Supply chain** — model provenance, frameworks, and dependencies in use.

## Constraints

**Must:**
- Walk all five taxonomy categories and explicitly state for each threat whether it applies to *this* system and why.
- Treat indirect prompt injection (malicious instructions hidden in external data the agent processes) as a first-class threat, since models cannot reliably distinguish informational context from actionable instructions.
- Attach a concrete, system-specific mitigation to every applicable threat, and apply the impossible-vs-tedious lens to each.

**Must Not:**
- Produce attack instructions, working exploits, or payloads — this is defensive modeling, not an offensive playbook.
- Assume "access control handles it" — tool/resource misuse can occur entirely within authorized privileges.
- Dismiss a threat as low-likelihood without noting its impact; some algorithmic injection attacks reach near-100% success and transfer across model families.

**Instructions:**

1. **Confirm scope and intent.** State that this is a defensive, authorized review of the named system, and summarize its architecture and trust boundaries.

2. **Category 1 — Prompt injection & instruction manipulation.** Assess direct injection (instruction overrides, encoding schemes such as Base64/hex, adversarial suffixes) and the more insidious indirect injection (malicious instructions embedded in fetched web pages, emails, or documents). Note that models cannot reliably separate context from instructions, and that some algorithmic attacks reach near-100% success and transfer across model families.

3. **Category 2 — Tool & resource misuse.** Assess threats that work even within authorized privileges: tool poisoning (falsified tool descriptors, schemas, or metadata); rug pull (a legitimate tool secretly replaced with a malicious version — documented in the wild as malicious tool servers impersonating legit services and copying data); tool chaining (combining legitimate tools into a harmful sequence that host monitoring sees only as trusted binaries with valid credentials); and resource exhaustion / loop amplification (denial of service, billing spikes).

4. **Category 3 — Identity & privilege abuse.** Assess unscoped privilege inheritance (a high-privilege agent delegating without re-scoping), the confused-deputy problem amplified by routine delegation, and memory-based privilege retention (cached credentials pulled across session boundaries).

5. **Category 4 — Memory & context poisoning.** Assess RAG poisoning (malicious data injected into vector stores), shared-context poisoning (in multi-tenant deployments), and long-term memory drift (subtle corruption where no single change appears malicious).

6. **Category 5 — Supply chain.** Assess the model supply chain (poisoned weights and backdoors that persist through safety training — research shows roughly 250 malicious documents can backdoor models across sizes) and the tool/framework supply chain (dependency confusion; roughly 100 malicious models found on a major platform).

7. **Score and prioritize.** For each applicable threat, rate likelihood and impact, and rank so the highest-severity threats drive mitigation order.

8. **Attach mitigations.** Give each applicable threat one concrete mitigation tied to this system, and run the impossible-vs-tedious test on it — if it only slows the attack, strengthen it.

**Output Format:**

A markdown threat register:
- **Scope & Intent** — defensive/authorized statement + system summary
- **Threat Register** — table: Category | Threat | Attack mechanism (described, not weaponized) | Applies here? (why) | Likelihood | Impact | Mitigation
- **Priority Order** — highest-severity applicable threats first
- **Residual Risk Notes** — what remains after mitigations and why

## Verification

- [ ] All five taxonomy categories are walked, each threat marked applicable or not with a reason.
- [ ] Indirect injection is treated as a first-class threat, not folded into direct injection.
- [ ] Tool/resource and identity threats are assessed even where access is authorized.
- [ ] Every applicable threat has one concrete, system-specific mitigation.
- [ ] Likelihood and impact are scored; near-100%/transferable injection is not understated.
- [ ] No exploit code, payloads, or attack instructions appear anywhere.

## False-Positive Prevention

❌ **DON'T:**
- Mark a threat "not applicable" because the demo never triggered it — model for the adversarial case.
- Assume authorized access means no misuse — tool chaining and confused-deputy work within granted scopes.
- Treat supply-chain risk as out of scope because "we trust the vendor" — backdoors can survive safety training.
- Write a generic mitigation ("validate inputs") with no tie to a specific surface in this system.

✅ **DO:**
- Assess each threat against this system's actual surfaces and dependencies.
- Flag indirect injection and in-the-wild rug-pull/tool-poisoning as live, not theoretical.
- Score impact even for low-likelihood threats; some injection attacks are both high-success and transferable.
- Make each mitigation concrete and apply the impossible-vs-tedious test to it.

## Example Output

```markdown
## Threat Model: Research Assistant Agent (web + RAG + tools)
Defensive, authorized review. Agent fetches web pages, retrieves from a shared vector
store, and calls a summarize tool and an email-draft tool.

### Threat Register
| Category | Threat | Attack mechanism | Applies here? | Likelihood | Impact | Mitigation |
|---|---|---|---|---|---|---|
| 1 Injection | Indirect injection | malicious instructions in fetched pages | Yes — agent ingests arbitrary web | High | High | treat fetched text as data; fixed tool registry; no scope widening from content |
| 2 Tool misuse | Tool poisoning | falsified tool descriptor | Yes — external connector | Med | High | pin & verify descriptors; provenance check |
| 2 Tool misuse | Resource exhaustion | loop amplification → billing spike | Yes | Med | Med | per-tool rate caps + loop guard |
| 3 Identity | Confused deputy | delegation reuses high-priv creds | Yes — multi-tool | Med | High | re-scope on delegate; per-tool credentials |
| 4 Memory | RAG poisoning | malicious docs into shared store | Yes — shared store | Med | High | source allow-list + write review on store |
| 5 Supply chain | Dependency confusion | malicious framework package | Yes | Low | High | lockfiles + provenance + scanning |

### Priority Order
1. Indirect injection (high/high). 2. RAG poisoning + confused deputy (med/high).
3. Tool poisoning. 4. Resource exhaustion. 5. Supply chain.

### Residual Risk Notes
Indirect injection cannot be fully eliminated — mitigations bound its blast radius
(content can never invoke privileged tools or widen scope) rather than prevent attempts.
```

**Techniques Used:**
- **RT-02 (Adversarial / Red-Team Reasoning):** drives the systematic search for how this system can be attacked.
- **DS-06 (Prioritization & Severity Guidance):** likelihood × impact ranks the threats for mitigation order.
- **AG-44 (Agent Threat / Risk Assessment):** the five-category taxonomy is applied to the specific deployment.
- **CM-02 (Constraint Specification):** the defensive-only and per-threat-mitigation rules bound the output.
- **QA-12 (False Positives Identification):** separates real, applicable threats from theoretical ones for this system.

**Related Prompts:**
- `aiagent_prompt_injection_untrusted_content_defense.md` — deepens the Category 1 mitigations.
- `aiagent_failure_mode_analysis.md` — the failure modes these threats can trigger.
- `aiagent_safety_sandboxing.md` — the containment that bounds the modeled blast radius.
