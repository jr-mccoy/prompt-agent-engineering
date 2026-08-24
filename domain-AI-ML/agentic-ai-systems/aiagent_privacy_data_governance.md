---
title: "AI Agent Privacy & Data-Governance Design"
category: AI-ML/agentic-ai-systems
description: "Design how an agent system handles sensitive data at runtime — PII minimization and redaction across prompts, logs, traces, and state; data-access auditing; residency and retention; and lineage — so the agent's own machinery (especially its observability) doesn't become the leak."
techniques:
  - ST-02
  - CM-02
  - DS-01
  - QA-12
  - QA-01
difficulty: advanced
tags:
  - privacy
  - data-governance
  - pii-redaction
  - data-residency
  - audit-trail
updated: "2026-06-18"
related_prompts:
  - domain-AI-ML/agentic-ai-systems/aiagent_observability_telemetry_design.md
  - domain-AI-ML/agentic-ai-systems/aiagent_runtime_guardrails_policy.md
  - domain-AI-ML/responsible-ai-governance/rai_privacy_pii_assessment.md
---

# AI Agent Privacy & Data-Governance Design

**Objective:** Design how sensitive data flows through an agent system and where it must be minimized, redacted, controlled, and audited — across the prompt context, tool calls, logs, traces, memory/state, and outputs — so that the agent's own infrastructure (its logging and observability in particular) doesn't quietly become the largest privacy exposure.

**When to Use:**
- The agent processes personal, regulated, or confidential data (customer records, health, financial, internal documents).
- You're adding observability/tracing and need to ensure traces don't capture raw sensitive payloads.
- Compliance requires demonstrable data-handling controls (access auditing, residency, retention).

**When NOT to Use:**
- The agent handles only non-sensitive, public data — governance overhead isn't warranted.
- You need a general ML data-privacy / PII assessment (not agent-runtime data flow) — use `domain-AI-ML/responsible-ai-governance/rai_privacy_pii_assessment.md` and cross-link.
- You're designing the output content-policy guardrail mechanics — use `aiagent_runtime_guardrails_policy.md` (this prompt defines *what* is sensitive and *where*; that prompt enforces it).

## Inputs / Context

Provide what you can; the design degrades gracefully if some are missing:
- **Data classes** — the categories of sensitive data and their regulatory status (PII, PHI, financial, secrets).
- **Data flow** — where data enters, which tools/agents touch it, where it's stored, where it exits.
- **Logging/observability surface** — what gets written to logs, traces, and memory (the easiest place to leak).
- **Regulatory requirements** — residency, retention limits, right-to-erasure, access-control obligations.
- **Access model** — who/what can read which data, and how that's currently controlled.

## Constraints

**Must:**
- Classify data and apply minimization: the agent (and each tool/sub-agent) receives only the sensitive data it needs for the step.
- Redact or reference (not inline-store) sensitive payloads in prompts, logs, traces, and persisted state; the observability layer must be privacy-safe by design.
- Define access control and an audit trail: which agent/tool accessed which data class, when, and under what authority.
- Define residency and retention per data class, including erasure handling, rather than indefinite default retention.

**Must Not:**
- Log full prompts, tool inputs/outputs, or traces containing raw PII "for debugging."
- Pass an entire sensitive record to a tool or sub-agent when a field or token reference suffices.
- Persist sensitive data in long-term memory/state with no retention limit or erasure path.
- Treat third-party model/tool calls as private without confirming their data-handling terms.

**Instructions:**

1. **Classify the data and map its flow.** List the sensitive data classes and trace each from entry → tools/agents → storage → exit. The flow map reveals every exposure point.

2. **Apply minimization at each hop.** For each step, reduce sensitive data to the minimum the step needs (field-level selection, tokenization, pseudonymization). Sub-agents and tools get references or redacted views by default.

3. **Make observability privacy-safe.** Specify redaction/referencing for logs, traces, and metrics so the telemetry layer (`aiagent_observability_telemetry_design.md`) never stores raw sensitive payloads; keep payloads by reference with short retention.

4. **Govern memory/state.** Define what sensitive data may persist in short/long-term memory, with retention limits and an erasure path (cross-link `aiagent_memory_design.md`).

5. **Define access control and audit.** Specify which agents/tools may access which data class, the authority that grants it, and the audit record (who/what/when/why) for every sensitive-data access.

6. **Set residency and retention.** Per data class, state where it may be stored/processed (residency) and how long (retention), plus how erasure/right-to-be-forgotten is executed across logs, traces, and state.

7. **Handle egress and third parties.** Define egress checks on outputs (cross-link injection/exfiltration defense) and verify the data-handling terms of any third-party model/tool the data passes through.

8. **Define verification of controls.** Specify how the controls are tested (e.g., scanning traces/logs for unredacted PII) so governance is demonstrable, not assumed.

**Output Format:**

A markdown design doc:
- **Data Classes & Flow Map** — class | entry → touches → storage → exit
- **Minimization** — per hop reduction (field/token/pseudonym)
- **Privacy-Safe Observability** — redaction/referencing in logs/traces
- **Memory/State Governance** — retention + erasure path
- **Access Control & Audit** — who/what | data class | audit record
- **Residency & Retention** — per data class
- **Egress & Third Parties** — checks + terms verification
- **Control Verification** — how leaks are tested for

## Verification

- [ ] Sensitive data classes are classified and their full flow is mapped.
- [ ] Each hop minimizes data; sub-agents/tools get references or redacted views by default.
- [ ] Logs, traces, and metrics never store raw sensitive payloads (redacted/referenced).
- [ ] Memory/state has retention limits and an erasure path.
- [ ] Every sensitive-data access is access-controlled and audited.
- [ ] Residency/retention are set per class; controls are verified by scanning for leaks.

## False-Positive Prevention

❌ **DON'T:**
- Log full prompts and traces with raw PII because "it helps debugging."
- Hand a whole customer record to a tool or sub-agent that needs one field.
- Keep sensitive data in long-term memory with no retention or erasure path.
- Assume a third-party model/tool keeps data private without checking its terms.

✅ **DO:**
- Map the data flow and minimize sensitive data at every hop.
- Make logs/traces privacy-safe by redacting or referencing payloads with short retention.
- Access-control and audit every sensitive-data access; set residency/retention per class.
- Verify controls by scanning the observability surface for unredacted data.

## Example Output

```markdown
## Privacy Design: Healthcare Intake Agent (handles PHI; can summarize + route)

### Data Classes & Flow Map
| Class | Entry → touches → storage → exit |
|---|---|
| PHI (name, DOB, dx) | intake form → triage agent + summarizer → EHR → routed summary |

### Minimization
Summarizer receives de-identified token references for name/DOB; only the clinical fields it needs. Routing agent sees category, not raw record.

### Privacy-Safe Observability
Traces store record_ref (not PHI); LLM call payloads referenced by blob id, PHI-redacted at write; 7-day payload retention. See `aiagent_observability_telemetry_design.md`.

### Memory/State Governance
No PHI in long-term memory; episode state holds record_ref only; erasure cascades to refs. See `aiagent_memory_design.md`.

### Access Control & Audit
Only triage agent (role-scoped creds) may resolve a ref to PHI; every resolve audited {agent, record_ref, time, purpose}.

### Residency & Retention
PHI processed/stored in-region only; retained per policy; erasure removes EHR row + trace refs + state.

### Egress & Third Parties
Outbound summary scanned for stray PHI before routing (`aiagent_prompt_injection_untrusted_content_defense.md`); model vendor BAA confirmed.

### Control Verification
Weekly scan of logs/traces for PHI patterns; any hit is a sev-1.
```

**Techniques Used:**
- **ST-02 (Structured Sequential Instructions):** classify → flow → minimize → observability → access → retention.
- **CM-02 (Constraint Specification):** minimization, residency, and retention are hard data-handling constraints.
- **DS-01 (Framework Application):** maps controls to regulatory obligations (residency, erasure, audit).
- **QA-12 (False Positives Identification):** control-verification scanning catches unredacted data leaks.
- **QA-01 (Self-Verification):** the checklist enforces privacy-safe observability and audited access.

**Related Prompts:**
- `aiagent_observability_telemetry_design.md` — the telemetry layer this prompt keeps privacy-safe.
- `aiagent_runtime_guardrails_policy.md` — enforces the content/PII rules defined here.
- `domain-AI-ML/responsible-ai-governance/rai_privacy_pii_assessment.md` — general ML data-privacy / PII assessment.
