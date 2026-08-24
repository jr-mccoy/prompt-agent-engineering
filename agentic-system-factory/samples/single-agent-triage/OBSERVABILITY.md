# OBSERVABILITY PLAN — support-ticket-triage

- **Spans:** one per ticket (`triage_agent-<ticket_id>`) covering classify → lookup? → draft → send/escalate, plus a child span per tool call.
- **Event schema:** `{ticket_id, customer_id, category, confidence, tool, args_hash, lookup_customer_id, sent:bool, escalated:bool, approval_token:bool, idempotency_key, tokens, latency_ms}` per step.
- **Key metrics:** classification accuracy (outcome), escalation rate by category (process), auto-send rate (process), tokens + tool calls / ticket (cost), cross-customer-read count (safety signal, must be zero), unapproved-sensitive-send count (safety signal, must be zero), duplicate-send-prevented count (idempotency working).
- **Dashboards:** per-ticket category + action + cost; rolling escalation rate by category; auto-send vs escalate split; safety-signal counters.
- **Alerts:** any unapproved send on a sensitive category (page immediately — should be zero); any `crm_order_lookup` whose `lookup_customer_id` ≠ the ticket's trusted `customer_id` (page — privacy breach); auto-send rate spike (possible classifier drift); duplicate-send attempts above baseline (idempotency / retry storm).
- **Trace retention:** full per-ticket trajectory retained for adversarial review; every lookup and send attributable to the ticket-scoped identity and tied to its idempotency key.
