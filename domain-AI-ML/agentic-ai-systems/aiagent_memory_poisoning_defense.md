---
title: "AI Agent Memory & Context Poisoning Defense"
category: AI-ML/agentic-ai-systems
description: "Defend an agent's memory and context against poisoning that persists across sessions — RAG poisoning, shared-context contamination, and long-term memory drift — with isolation, per-retrieval integrity validation, and retention/rollback policy."
techniques:
  - ST-02
  - CM-02
  - QA-12
  - DS-06
  - AG-44
difficulty: advanced
tags:
  - memory-poisoning
  - rag-security
  - context-integrity
  - session-isolation
  - retention
updated: "2026-06-19"
related_prompts:
  - domain-AI-ML/agentic-ai-systems/aiagent_memory_design.md
  - domain-AI-ML/agentic-ai-systems/aiagent_prompt_injection_untrusted_content_defense.md
  - domain-AI-ML/agentic-ai-systems/aiagent_context_engineering_at_scale.md
---

# AI Agent Memory & Context Poisoning Defense

**Objective:** Defend an agent's memory and retrieved context against poisoning that persists across sessions — RAG poisoning, shared-context contamination in multi-tenant deployments, and slow long-term memory drift — by designing memory isolation, per-retrieval integrity validation, and retention/rollback policy so contaminated context cannot silently steer later behavior.

**When to Use:**
- The agent reads from a vector store / RAG pipeline, retains long-term memory, or runs in a multi-tenant environment where sessions share infrastructure.
- The agent updates stored knowledge from summaries, peer-agent feedback, or external inputs over time.
- Before trusting persisted memory to influence high-stakes decisions or actions.

**When NOT to Use:**
- The agent is fully stateless with no retrieval and no persisted memory — note that and skip.
- You only need input-time prompt-injection defense for a single turn (use `aiagent_prompt_injection_untrusted_content_defense.md`) or general memory architecture (use `aiagent_memory_design.md`).

**Source:** Framework adapted from Anthropic "Zero Trust for AI Agents" (2026), a vendor report — facts attributed inline; no source text reproduced.

## Inputs / Context

Provide what you can; the design degrades gracefully if some are missing:
- **Memory inventory** — what is stored (conversation history, summaries, learned facts, goal weights) and where.
- **Retrieval pipeline** — vector stores / RAG sources and how data enters them (poisoned sources, direct uploads, automated ingestion).
- **Tenancy model** — single-user vs. multi-tenant; what context, if any, is shared across sessions or users.
- **Update sources** — how stored memory changes over time (summaries, peer-agent feedback, tool outputs).
- **Existing controls** — current validation, logging, retention/TTL, and rollback capability.

## Constraints

**Must:**
- Enforce strict memory isolation between sessions and users so one conversation cannot affect another.
- Validate context integrity at EVERY retrieval (not only at storage) using cryptographic hashes and source attribution; store hashes in tamper-resistant logs kept SEPARATE from the content.
- Apply retention policies with TTLs and shorter retention for high-risk context (external inputs, unverified tool outputs), and maintain versioned, rollback-capable memory stores.

**Must Not:**
- Let injected or unverified data enter shared context that later sessions inherit.
- Proceed on an integrity-validation failure — reject the element and alert instead.
- Treat slow, subtle memory drift as benign because no single change looks malicious.

**Instructions:**

1. **Map the memory threat surface.** Identify where poisoning can enter: RAG poisoning (malicious data reaching vector stores via poisoned sources, direct uploads, or over-trusted ingestion pipelines, then retrieved as contaminated context); shared-context poisoning (in multi-tenant setups, injected data influencing later sessions that inherit poisoned context); and long-term memory drift (summaries and peer-agent feedback gradually shifting stored knowledge or goal weighting, with no single change appearing malicious).

2. **Design memory isolation.** Establish strict boundaries between sessions and between users so one conversation cannot affect another. In multi-tenant environments, ensure no path lets one tenant's input land in another's retrievable context.

3. **Tag every memory element at write time.** Record its source and the conditions under which it was added, so provenance travels with the data and unverified or external-origin elements are distinguishable.

4. **Compute and store integrity hashes separately.** Hash each stored element cryptographically and keep the hashes in tamper-resistant logs separate from the content itself, so an attacker who edits content cannot quietly fix the hash.

5. **Validate integrity on every retrieval.** Re-check hashes and source attribution at each retrieval, not just at storage time. On any validation failure, reject the element and alert — do not proceed with suspect context.

6. **Set retention and TTL policies by risk.** Assign TTLs, auto-expire unverified memory, and apply shorter retention to high-risk context (external inputs, unverified tool outputs) so contamination has a bounded lifespan.

7. **Make memory versioned and rollback-capable.** Keep versioned memory stores so you can roll back to a known-good state, and define quarantine procedures that preserve poisoned data for forensics rather than deleting it.

8. **Pre-define and test recovery.** Specify criteria for a full purge versus targeted remediation, and test the rollback path BEFORE an incident — an untested rollback is not a control.

**Output Format:**

A markdown defense design:
- **Memory Threat Surface** — RAG poisoning, shared-context poisoning, long-term drift, and where each can enter
- **Isolation Design** — session/user boundaries; multi-tenant separation
- **Integrity-Validation Rules** — tagging, separate hash storage, per-retrieval check, fail-closed behavior
- **Retention & TTL Policy** — TTLs by risk tier; auto-expiry of unverified memory
- **Rollback & Quarantine** — versioning, quarantine for forensics, purge-vs-remediate criteria, pre-incident test

## Verification

- [ ] Sessions and users are strictly isolated; one conversation cannot affect another.
- [ ] Integrity is validated at every retrieval, not just at storage.
- [ ] Each memory element is tagged with source and conditions of addition.
- [ ] Hashes are stored in tamper-resistant logs separate from the content.
- [ ] Validation failure rejects and alerts rather than proceeding.
- [ ] Retention is shorter for high-risk context; unverified memory auto-expires.
- [ ] Versioned stores exist and rollback is tested before incidents.

## False-Positive Prevention

❌ **DON'T:**
- Validate integrity only at storage time and trust the data forever after.
- Store hashes alongside the content they protect, where an attacker can edit both.
- Assume multi-tenant sessions are isolated because they "feel" separate — verify no shared-context path exists.
- Dismiss gradual memory drift because no single update looks malicious.

✅ **DO:**
- Re-validate hashes and source attribution on every retrieval and fail closed on mismatch.
- Keep integrity hashes in tamper-resistant logs separate from the content.
- Enforce hard session/user boundaries so injected data cannot reach later sessions.
- Use versioned stores plus a tested rollback and quarantine procedure for forensics.

## Example Output

```markdown
## Memory Defense: Customer-Support Agent (multi-tenant)

### Memory Threat Surface
- RAG poisoning: KB articles auto-ingested from a partner feed → contaminated retrieval.
- Shared-context poisoning: per-tenant summaries written to a shared store → tenant A influences tenant B.
- Long-term drift: nightly summary rollups gradually reshape "known good" answers.

### Isolation Design
Per-tenant namespaces in the vector store; session memory keyed by {tenant_id, session_id}; no cross-namespace retrieval path.

### Integrity-Validation Rules
Each element tagged {source, ingest_conditions, ts}. SHA-256 stored in a separate append-only log. On retrieval, recompute + compare and check source; mismatch → reject + alert SIEM, do not answer from it.

### Retention & TTL Policy
External-feed context: 7-day TTL, unverified auto-expires. Verified internal KB: 90 days. Unverified tool outputs: single-session only.

### Rollback & Quarantine
Daily versioned snapshots; suspect elements quarantined (not deleted) for forensics. Targeted remediation if scope is one source; full purge if integrity log shows tampering. Rollback drill run monthly.
```

**Techniques Used:**
- **ST-02 (Structured Sequential Instructions):** threat map → isolation → tagging → hashing → per-retrieval validation → retention → rollback → recovery test.
- **CM-02 (Constraint Specification):** isolation boundaries, per-retrieval validation, and risk-tiered retention are the governing constraints.
- **QA-12 (False Positives Identification):** distinguishes real integrity controls from storage-time-only checks that miss later tampering.
- **DS-06 (Prioritization & Severity Guidance):** high-risk context (external/unverified) gets shorter retention and tighter scrutiny.
- **AG-44 (Agent Supply-Chain Integrity):** memory and retrieved context are treated as an integrity-critical supply chain into the model.

**Related Prompts:**
- `aiagent_memory_design.md` — the memory architecture this defense hardens.
- `aiagent_prompt_injection_untrusted_content_defense.md` — input-time defense complementary to persisted-memory defense.
- `aiagent_context_engineering_at_scale.md` — how validated context is assembled and managed at scale.
