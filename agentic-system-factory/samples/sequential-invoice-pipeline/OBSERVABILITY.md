# OBSERVABILITY PLAN — invoice-intake-pipeline

- **Spans:** one per stage (extractor, validator, poster) + the deterministic gate decision + a whole-run trajectory span. The pre-post approval and the post itself each get their own span.
- **Event schema:** `{run_id, invoice_id, stage, tool, args_hash, amount, discrepancy_count, hitl_required:bool, approval_token_id, approver_id, idempotency_key, dry_run:bool, posted:bool, allowed:bool, tokens, latency_ms}` per stage/tool call.
- **Key metrics:**
  - *Outcome:* extraction accuracy (sampled vs human), decision accuracy (auto/HITL/hold matches policy), discrepancy catch rate.
  - *Process:* lookups/invoice, HITL rate, time-in-approval.
  - *Cost:* tokens/invoice.
  - *Safety (load-bearing):* count of posts without a valid approval token when HITL was required (must be 0), count of non-allowlisted call attempts (must be 0), duplicate-key collisions resolved by idempotency (a healthy non-zero is fine — it means retries are safe), self-approval rejections.
- **Dashboards:** per-run extract→validate→post timeline with the gate decision; rolling HITL rate and approval latency; idempotency-dedupe count; allowlist-deny rate.
- **Alerts:**
  - Any post lacking a valid token while HITL was required — page immediately (this is the load-bearing invariant).
  - Any non-allowlisted action attempt (should be zero).
  - Spike in injection-anomaly flags on documents (possible vendor-side attack campaign).
  - Idempotency-key reuse with differing amount/payee (tampering signal) — block + alert.
  - Tokens/invoice above budget.
- **Trace retention:** full trajectory retained for adversarial/financial-controls review; every post attributable to a run, an approver, and an idempotency key.
