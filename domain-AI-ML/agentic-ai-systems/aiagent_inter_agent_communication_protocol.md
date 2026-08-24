---
title: "AI Inter-Agent Communication Protocol Design"
category: AI-ML/agentic-ai-systems
description: "Design the protocol agents use to exchange work — message schemas, shared-state vs. message-passing, handoff contracts, schema evolution, boundary validation, and conflict reconciliation — so information survives handoffs and agents can't silently corrupt each other's state."
techniques:
  - ST-02
  - CM-02
  - AG-09
  - QA-12
  - QA-01
difficulty: advanced
tags:
  - multi-agent
  - communication-protocol
  - message-schema
  - handoff-contract
  - shared-state
updated: "2026-06-18"
related_prompts:
  - domain-AI-ML/agentic-ai-systems/aiagent_orchestration_topology_selection.md
  - domain-agentic-resources/commands/multi-agent/multiagent_coordination_via_tests_and_policy.md
  - domain-prompt-engineering/agent-workflows/agent_subagent_brief_generator.md
---

# AI Inter-Agent Communication Protocol Design

**Objective:** Specify how agents in a multi-agent system exchange information — the message schema and types, whether they share state or pass messages, the handoff contract at each boundary, how schemas evolve without breaking older agents, and how conflicting writes or claims are reconciled — so that handoffs are lossless, validated, and never silently corrupting.

**When to Use:**
- You've chosen a topology (`aiagent_orchestration_topology_selection.md`) and must now define the actual messages and shared state.
- Agents "talk" via free-form natural language and you're seeing dropped context, ambiguous handoffs, or conflicting actions.
- Two agents write to the same resource or state and you need a reconciliation rule.

**When NOT to Use:**
- It's a single agent — there is no inter-agent boundary to design.
- You only need to coordinate via a test surface and policy instead of messages — use `domain-agentic-resources/commands/multi-agent/multiagent_coordination_via_tests_and_policy.md`.
- You need the prompt that generates a self-contained sub-agent brief — use `domain-prompt-engineering/agent-workflows/agent_subagent_brief_generator.md`.

## Inputs / Context

Provide what you can; the design degrades gracefully if some are missing:
- **Topology & roles** — which agents exist and who hands off to whom.
- **Shared resources** — any state multiple agents read or write (files, DB rows, a blackboard).
- **Information that must survive a handoff** — the load-bearing facts a receiver needs and can't recover on its own.
- **Trust boundaries** — whether any agent processes untrusted/external content before passing it on.
- **Versioning reality** — whether agents deploy independently (raising version-skew risk).

## Constraints

**Must:**
- Define each message as a typed, validated schema with required and optional fields — not free chat.
- Choose explicitly between shared-state (blackboard) and message-passing for each interaction, and justify it.
- Specify validation at every receiving boundary: a message that fails its schema is rejected or quarantined, never partially consumed.
- Define a conflict-reconciliation rule for any shared resource (last-writer-wins, version/CAS, orchestrator-arbitrates, merge) and a schema-evolution rule (additive fields, version tag).

**Must Not:**
- Rely on free-form natural-language handoffs for load-bearing information.
- Let two agents write the same resource with no reconciliation rule (silent overwrite).
- Assume all agents always run the same schema version when they deploy independently.
- Pass untrusted content across a boundary as if it were trusted instruction (cross-link injection defense).

**Instructions:**

1. **Inventory the boundaries.** For the chosen topology, list every place information crosses from one agent to another, and what each receiver actually needs.

2. **Choose the exchange model per boundary.** Decide shared-state vs. message-passing: message-passing for discrete handoffs; a blackboard only where many agents genuinely need a shared evolving view. State why.

3. **Define the message schema.** For each message type, specify required/optional fields, types, and the minimal payload that makes the handoff lossless. Prefer structured artifacts (IDs + typed fields) over prose.

4. **Specify boundary validation.** Define what the receiver checks (schema conformance, referential integrity, trust level) and what happens on failure — reject, quarantine, or request resend — so a malformed message can't be half-processed.

5. **Define shared-state semantics.** For any shared resource, specify read/write access per agent, the consistency model, and the conflict-reconciliation rule (CAS/version, orchestrator arbitration, merge policy).

6. **Plan schema evolution.** State how fields are added without breaking older agents (additive-only, version tags, default handling of unknown fields) to survive version skew.

7. **Handle the untrusted path.** Where an agent forwards externally-sourced content, mark it as data (not instruction) and cross-link `aiagent_prompt_injection_untrusted_content_defense.md`.

8. **Define termination and dead-letter handling.** Specify what happens to in-flight messages when the system stops, and where unprocessable messages go.

**Output Format:**

A markdown design doc:
- **Boundary Inventory** — sender → receiver | info that must survive
- **Exchange Model** — per boundary: shared-state vs. message-passing + why
- **Message Schemas** — type | required fields | optional fields
- **Boundary Validation** — checks + failure behavior
- **Shared-State Semantics** — resource | access | consistency | conflict rule
- **Schema Evolution** — versioning/compatibility rule
- **Untrusted-Content Handling** — cross-link
- **Termination & Dead-Letter**

## Verification

- [ ] Every load-bearing handoff is a typed, validated schema, not free chat.
- [ ] Shared-state vs. message-passing is chosen per boundary with a reason.
- [ ] Each receiving boundary validates inputs and defines failure behavior.
- [ ] Every shared resource has a conflict-reconciliation rule.
- [ ] Schema evolution is specified so version skew doesn't break receivers.
- [ ] Untrusted content is marked as data and cross-linked to injection defense.

## False-Positive Prevention

❌ **DON'T:**
- Declare the protocol "designed" when handoffs are still natural-language summaries that can drop facts.
- Allow concurrent writers to a shared resource with no version or arbitration rule.
- Assume schema changes are safe because "we'll deploy all agents together" when agents deploy independently.
- Treat a tool result or retrieved document forwarded between agents as trusted instruction.

✅ **DO:**
- Make every handoff a typed message with the minimal lossless payload.
- Give each shared resource an explicit consistency model and conflict rule.
- Design additive, version-tagged schemas that tolerate unknown fields.
- Tag forwarded external content as data and route it through injection defense.

## Example Output

```markdown
## Protocol: Extractor → Synthesizer → Judge (research pipeline)

### Boundary Inventory
| Sender → Receiver | Must survive |
|---|---|
| Extractor → Synthesizer | source_id, claims[], confidence, quote spans |
| Synthesizer → Judge | draft, claim→source map |
| Judge → Orchestrator | verdict, failed_claims[] |

### Exchange Model
All three are discrete handoffs → message-passing. No blackboard (no shared evolving view needed).

### Message Schemas
- `ExtractResult`: required {source_id, claims[]:{text, confidence, span}}; optional {warnings[]}.
- `Draft`: required {text, citations[]:{claim_id, source_id}}; optional {open_questions[]}.
- `Verdict`: required {pass:bool, failed_claims[]}; optional {notes}.

### Boundary Validation
Synthesizer rejects any ExtractResult missing source_id or with a span not in the cited source → request resend (max 1), else drop + flag.

### Shared-State Semantics
Single shared resource: `brief_status` (orchestrator-owned). Only orchestrator writes; agents read. No concurrent-write conflict by construction.

### Schema Evolution
Additive-only fields; each message carries `schema_v`. Unknown fields ignored by older receivers.

### Untrusted-Content Handling
Source text in `claims[].text` is data, never instruction — see `aiagent_prompt_injection_untrusted_content_defense.md`.

### Termination & Dead-Letter
On stop, in-flight messages persisted to a dead-letter store keyed by source_id for replay.
```

**Techniques Used:**
- **ST-02 (Structured Sequential Instructions):** boundaries → exchange model → schemas → validation → state → evolution.
- **CM-02 (Constraint Specification):** schemas, access rules, and consistency models are the governing constraints.
- **AG-09 (Multi-Agent Coordination):** handoff contracts and conflict reconciliation are the core deliverable.
- **QA-12 (False Positives Identification):** boundary validation catches malformed/half-valid messages before they propagate.
- **QA-01 (Self-Verification):** the checklist enforces typed handoffs and conflict rules.

**Related Prompts:**
- `aiagent_orchestration_topology_selection.md` — choose the topology this protocol serves.
- `domain-agentic-resources/commands/multi-agent/multiagent_coordination_via_tests_and_policy.md` — coordinate via a test surface instead of chat.
- `domain-prompt-engineering/agent-workflows/agent_subagent_brief_generator.md` — generate a self-contained handoff brief.
