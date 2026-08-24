# ARCHITECTURE — support-ticket-triage

**System:** support-ticket-triage · **Author/date:** factory sample, 2026-06-20 · **Status:** approved (sample) · **Topology:** TP-02 single agent

## 1. Use case & scope
- **One-sentence use case:** Given one inbound support ticket, classify it, look up the customer's recent order when relevant, draft a reply, and either auto-send a low-risk reply or escalate a sensitive ticket to a human.
- **Job-to-be-done:** Clear the front of the support queue — resolve simple, unambiguous tickets end-to-end and route the risky ones to a person with context attached.
- **Success criteria (observable gates):**
  - [ ] Every ticket is classified into exactly one category.
  - [ ] Sensitive categories (refund, legal, security, self-harm) are NEVER auto-sent — they hit the HITL gate.
  - [ ] A CRM lookup happens only when the ticket is order-related; no lookup leaks data for a different customer.
  - [ ] Each ticket sends at most one reply (idempotent on send).
- **Inputs:** ticket metadata — ticket_id, customer_id, channel (TRUSTED); **the ticket free-text body (UNTRUSTED).**
- **Outputs:** a category label + either a sent reply (low-risk) or an escalation record with a draft attached (sensitive).
- **Autonomy level:** acts (can send a message via `send_reply`) on low-risk categories; recommends-only (escalates) on sensitive categories.
- **Blast radius:** one read-only CRM lookup + one outbound customer message per ticket. No refunds, no account mutation, no money movement — the agent has no refund tool; "refund" is a category that escalates.
- **Out of scope:** issuing refunds/credits, modifying orders or accounts, multi-ticket batch actions, anything requiring authentication beyond the scoped CRM read.

## 2. Step-0 justification (the gate)

<!-- GATE-0: JUSTIFIED -->
<!-- JUSTIFICATION-START -->
A single agent (a bounded tool loop) is required because the CRM order lookup is conditional on what the ticket body actually asks, and the subsequent send-versus-escalate decision depends on the lookup result — so the control flow is content-dependent and only knowable at runtime. A single model call cannot perform the conditional lookup-then-decide; a deterministic workflow cannot, because the branch set (lookup or not, which category, send or escalate) is determined by the untrusted ticket content, not fixable in advance.
<!-- JUSTIFICATION-END -->

- **Rung chosen:** TP-02 single agent.
- **Rejected lower rungs:** single model call (can't do the conditional CRM lookup and act on its result); deterministic workflow (branch set is content-dependent — category + lookup-needed + send-vs-escalate can't be hard-coded).
- **Rejected higher rung:** TP-06 multi-agent / orchestrator-workers — one ticket at a time, no parallel breadth to fan out; an orchestrator would add coordination cost with no work to parallelize.
- **Accepted cost:** a short tool loop (classify → maybe lookup → draft → send/escalate) per ticket vs a single turn — justified by the conditional tool use and the safety branch.

## 3. Topology & primitives
- **Topology:** TP-02 single agent (aliases: tool-using agent; one ReAct/loop agent with a fixed tool set).
- **Selection variables:** control = model decides next step within a bounded loop; structure = serial single agent; plan = implicit (classify → lookup? → draft → send/escalate).
- **Primitives:** 1 agent (`triage_agent`); tools = `crm_order_lookup` (read-only) + `send_reply` (write/messaging, gated); no sub-agents, no peer channel; per-ticket trace span; mandatory HITL approval before any send on sensitive categories; idempotency key on send.

## 4. Architecture
### 4.1 Component map
```
ticket (trusted meta + UNTRUSTED body)
   → TRIAGE_AGENT
        → classify(category)
        → if order-related: crm_order_lookup(customer_id)   [read-only, customer-scoped]
        → draft reply
        → if category ∈ {refund, legal, security, self-harm} OR low-confidence:
              → ESCALATE (write escalation record + draft, NO send)
          else:
              → HITL/policy check passes → send_reply(idempotency_key)  [at-most-once]
```
### 4.2 Seams
| Seam | From → To | Crosses | Validation |
|------|-----------|---------|------------|
| S1 | ticket body → agent | UNTRUSTED free text | body passed as a `<ticket_body>` data block; never selects a tool or sets a category by itself (SAFE-01) |
| S2 | agent → crm_order_lookup | customer_id from TRUSTED metadata | lookup keyed only on the trusted `customer_id`; never on an id parsed out of the body (privacy boundary) |
| S3 | agent → send decision | category + confidence | deterministic policy: sensitive category OR low confidence ⇒ escalate; send path requires approval token (SAFE-02) |
| S4 | agent → send_reply | outbound customer message | idempotency key = ticket_id; at-most-once; approval token required for sensitive |
### 4.3 Context / durability
Single context per ticket: trusted metadata + untrusted body (spotlighted) + lookup result (if any) + draft. State (`classified`, `looked_up`, `sent`/`escalated`) persisted keyed by ticket_id so a crash mid-loop resumes without re-sending.
### 4.4 Cost / model right-sizing
| Component | Model | Why |
|-----------|-------|-----|
| triage_agent | mid-to-strong | classification + drafting are routine, but the safety branch (sensitive-category detection) wants the stronger model's judgment |

## 6. Gates summary
- Gate 0: done (§2) · Gate A: GATE_DESIGN.md · Gate B: EVAL_HARNESS.md · Gate C: DISCLOSURE_MANIFEST.md · Kill switch: `config.halt` checked before any `send_reply` / `crm_order_lookup`.

## 8. Referenced existing prompts
`aiagent_complexity_ladder_gate`, `aiagent_human_in_the_loop_design`, `aiagent_prompt_injection_untrusted_content_defense`, `aiagent_tool_design`, `aiagent_privacy_data_governance`.
