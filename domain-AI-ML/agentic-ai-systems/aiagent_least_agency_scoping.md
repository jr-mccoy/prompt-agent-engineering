---
title: "AI Agent Least-Agency & Blast-Radius Scoping"
category: AI-ML/agentic-ai-systems
description: "Extend least privilege from what an agent can access to what each of its tools can do, how often, and where — producing a per-tool agency table, escalation triggers, and a deny-by-default statement that bounds damage even under hijack."
techniques:
  - AG-45
  - AG-44
  - AG-13
  - CM-02
  - DS-06
difficulty: advanced
tags:
  - least-agency
  - blast-radius
  - tool-scoping
  - deny-by-default
  - agent-security
updated: "2026-06-19"
related_prompts:
  - domain-AI-ML/agentic-ai-systems/aiagent_tool_design.md
  - domain-AI-ML/agentic-ai-systems/aiagent_safety_sandboxing.md
  - domain-AI-ML/agentic-ai-systems/aiagent_human_in_the_loop_design.md
---

# AI Agent Least-Agency & Blast-Radius Scoping

**Objective:** Apply "least agency" to an agent — capping not just what it can access but what each of its tools can do, how often, and against which targets — so that a hijacked agent or poisoned tool can do bounded damage, and produce a per-tool agency table, escalation triggers, and an explicit deny-by-default rule.

**When to Use:**
- The agent has tools that take state-changing or external actions (DB writes, email, payments, API calls).
- You have already granted access scopes but want to constrain what happens *within* those scopes.
- You are splitting one agent into several and need each to be compartmentalized correctly.

**When NOT to Use:**
- The agent has no tools, or only read-only tools with no external effect — note that and skip.
- You need a full maturity assessment (use `aiagent_zero_trust_maturity_assessment.md`) or a threat taxonomy (use `aiagent_agentic_threat_model.md`).

**Source:** Framework adapted from the OWASP concept of "least agency" and Anthropic "Zero Trust for AI Agents" (2026), a vendor report — facts attributed inline; no source text reproduced.

## Inputs / Context

Provide what you can; the scoping degrades gracefully if some are missing:
- **Tool inventory** — every tool the agent can call and the underlying system it touches.
- **Granted access scopes** — what credentials each tool authenticates as today.
- **Sensitivity & value map** — which targets (records, recipients, accounts, paths) are high-value or sensitive.
- **Expected volume** — normal call rates per tool, so caps are calibrated, not arbitrary.
- **Split/compartmentalization plan** — whether functions are being divided across multiple agents.

## Constraints

**Must:**
- Cap each tool along three axes: capability (what operations it may perform), rate/quantity (how often / how much per window), and target allow-list (which paths, recipients, accounts, or resources).
- Make every tool and every target deny-by-default — anything not explicitly listed is blocked, not warned.
- Give each agent in a split a unique identity and its own credentials; reusing credentials across split agents defeats compartmentalization.

**Must Not:**
- Treat access control alone as sufficient — it does not stop misuse *within* granted access (tool poisoning, confused-deputy chains).
- Cap a tool by friction alone; if containment relies on slowing an attacker rather than stopping them, assume it fails and restrict further.
- Allow a high-value or sensitive operation to proceed without an escalation trigger or gate.

**Instructions:**

1. **Enumerate every tool and its underlying system.** For each tool, state the real-world system it acts on and the worst single action it could take today.

2. **Set the capability cap.** Constrain each tool to the minimum operation it needs: a DB tool to read-only queries with no schema change; an email tool to draft-only with sending behind separate authorization; an API tool to a minimal CRUD subset. Default to the least-powerful verb.

3. **Set the rate/quantity cap.** Define max calls per time window and any quantity ceilings (block bulk export, mass send, large-batch writes) calibrated to normal volume.

4. **Set the target allow-list.** List exactly which paths, recipients, accounts, or resources each tool may touch. Everything else is denied.

5. **State deny-by-default explicitly.** Write the rule that any tool, operation, or target not on the lists above is blocked — and confirm it is enforced in the tool/connector layer, not merely requested in the prompt.

6. **Define escalation triggers.** Name the conditions that must route to a gate or human: high-value transactions, sensitive data categories, external communications, and any cross-boundary action.

7. **Identify residual blast radius per tool.** With caps in place, assess what could still go wrong if the agent or that tool is hijacked (tool poisoning, confused-deputy chains that misuse legitimate access). Apply the impossible-vs-tedious test to any containment plan; if it relies on friction, restrict further.

8. **Verify compartmentalization.** If functions are split across agents, confirm each agent has a unique identity and its own credentials, and that no credential is shared across the split.

**Output Format:**

A markdown agency scoping:
- **Per-Tool Agency Table** — Tool | Capability cap | Rate/quantity cap | Target allow-list | Residual blast radius
- **Escalation Triggers** — conditions that route to a gate or human
- **Deny-by-Default Statement** — the explicit block rule and where it is enforced
- **Compartmentalization Check** — unique identity + own credentials per split agent

## Verification

- [ ] Every tool is capped on all three axes (capability, rate/quantity, target).
- [ ] Deny-by-default is stated and enforced at the tool/connector layer, not in the prompt.
- [ ] Each tool's residual blast radius is assessed for the hijack case, not just the happy path.
- [ ] Escalation triggers cover high-value, sensitive-data, and external-comms actions.
- [ ] Any friction-only containment is downgraded and the scope tightened.
- [ ] Split agents each have a unique identity and their own credentials.

## False-Positive Prevention

❌ **DON'T:**
- Assume a granted access scope is safe because access was approved — access does not bound *use*.
- Cap a tool with a warning prompt the model can ignore or be injected past.
- Give two split agents the same service account "to keep it simple."
- Call a tool "low risk" without tracing a confused-deputy or tool-poisoning path through it.

✅ **DO:**
- Bound each tool's capability, rate, and targets so a hijacked agent cannot exceed them.
- Enforce deny-by-default in the connector layer where the model cannot override it.
- Give every split agent a unique identity and dedicated credentials.
- Trace the residual blast radius for each tool under the assumption the model is injection-steered.

## Example Output

```markdown
## Least-Agency Scoping: Finance Reconciliation Agent

### Per-Tool Agency Table
| Tool | Capability cap | Rate/quantity cap | Target allow-list | Residual blast radius |
|---|---|---|---|---|
| ledger-db | read-only queries, no schema change | 60 reads/min | `recon.*` views only | read exposure of recon views |
| email | draft only; send needs separate auth | 5 drafts/hr | finance@ internal alias | misleading draft, not sent |
| payments-api | create-refund only, cap $500 | 10/day | allow-listed vendor IDs | bounded erroneous refunds |
| export | blocked (not granted) | — | — | none |

### Escalation Triggers
- Any refund > $500 → human approval.
- Any recipient outside the internal alias → gate.
- Any sensitive PII category in a draft → gate.

### Deny-by-Default Statement
Any tool, operation, or target not listed above is blocked by the connector layer.
The agent cannot widen scope by emitting new tool calls; the registry is fixed.

### Compartmentalization Check
Read-recon and issue-refund are split into two agents, each with its own identity and
credentials. No shared service account. Refund agent has no DB-read scope and vice versa.
```

**Techniques Used:**
- **AG-45 (Tool Permission / Scope Minimization):** caps each tool's capability, rate, and targets — the core least-agency move.
- **AG-44 (Agent Threat / Risk Assessment):** derives residual blast radius per tool under the hijack assumption.
- **AG-13 (Agent Safety & Guardrails):** deny-by-default and escalation triggers are structural guardrails.
- **CM-02 (Constraint Specification):** the three-axis caps and compartmentalization rule are the governing constraints.
- **DS-06 (Prioritization & Severity Guidance):** high-value/sensitive actions set the escalation bar.

**Related Prompts:**
- `aiagent_tool_design.md` — the per-tool contracts these caps constrain at runtime.
- `aiagent_safety_sandboxing.md` — the runtime containment that enforces deny-by-default.
- `aiagent_human_in_the_loop_design.md` — calibrate the escalation gates named here.
