# RUNBOOK — support-ticket-triage

## Rollout
- Shadow mode first: agent classifies and drafts, but every send is suppressed and queued for a human to compare against the agent's send/escalate decision. Measure category accuracy + action correctness before enabling auto-send.
- Canary auto-send on one low-risk category (e.g. order_status) for one cohort; watch the unapproved-sensitive-send counter (must stay zero) and the cross-customer-read counter (must stay zero) before widening categories.

## Rollback
<!-- ROLLBACK: present -->
Rollback = flip `config.halt: true` (kill switch): the agent stops calling tools and routes all tickets to the human queue with their metadata. Because `send_reply` is idempotent (keyed on ticket_id) and escalation writes no customer-visible message, rollback cannot double-send or undo a needed message — in-flight tickets simply land in the human queue. A narrower rollback (disable auto-send only, keep classify+draft) is available by forcing every category to the escalate path.

## Failure-mode catalog (seed)
| Failure | Mitigation | Detected by |
|---------|-----------|-------------|
| Injection in ticket body ("issue a refund / send now") | 3-layer defense: spotlighting + deterministic escalate-on-sensitive policy + tool-layer approval token (no refund tool exists) | unapproved-sensitive-send counter; injection eval |
| Cross-customer CRM read | lookup keyed only on TRUSTED metadata customer_id | lookup_customer_id ≠ ticket customer_id alert |
| Duplicate / double send | idempotency key = ticket_id; at-most-once | duplicate-send-prevented counter |
| Sensitive ticket auto-sent | classifier routes refund/legal/security/self-harm to escalate; tool refuses unapproved sensitive send | escalation-rate-by-category dip; safety eval |
| Classifier drift (over-auto-sending) | auto-send-rate alert; fall back to escalate-all via config | auto-send rate spike |
| Loop stall | ≤5-step cap → escalate with current draft | missing/late ticket span |
