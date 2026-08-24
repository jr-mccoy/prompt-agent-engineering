# TOOL SPEC (ACI) — crm_order_lookup

**Owner agent(s):** triage_agent

## Purpose & altitude
Fetch the customer's most recent order(s) so the agent can answer order-related tickets (one read-only lookup workflow, not a raw CRM endpoint).

## Signature
```
crm_order_lookup(customer_id: str, max_orders: int = 3) -> list[{order_id, status, ordered_at, items_summary}]
```
- `customer_id` is supplied by the agent ONLY from the ticket's TRUSTED metadata — never parsed from the untrusted body.
- Returns a condensed order summary, not full PII.

## Schema & validation (SAFE-02)
Pre-execution: `customer_id` must equal the current ticket's trusted `customer_id` (the runtime rejects any other value — this is the cross-customer privacy boundary); `max_orders` ≤ 5. Permission scope: read-only.

## Errors as guidance
| Condition | Message |
|-----------|---------|
| customer_id ≠ ticket customer | "blocked: lookup must target the ticket's own customer" |
| no orders | "No recent orders found for this customer" |

## Untrusted output handling
Order records are internal/trusted data, but are still passed back to the model as a data block; they cannot select the next tool. The tool never accepts a customer_id originating from the ticket body (SAFE-01 boundary on input).
