# RUNBOOK — invoice-intake-pipeline

## Rollout
- Shadow mode: run extract + validate on live invoices but force **dry-run** on the post for the first cohort; compare the pipeline's post/hold decisions against the AP team's manual decisions before enabling any real post.
- Canary: enable real posts for one low-value vendor segment with `APPROVAL_THRESHOLD` set deliberately low (most invoices route to HITL); watch the post-control metrics before raising the threshold.
- Promote only after the safety gate (S1–S5) passes on the canary traffic with zero unapproved/altered posts and zero double-pays.

## Rollback
<!-- ROLLBACK: present -->
Rollback is staged and fail-closed:
1. Set `config.halt: true` (kill switch) — the controller stops advancing and performs no further posts; in-flight runs pause resumably.
2. Or, less drastically, flip the poster to **dry-run-only** — extraction/validation continue, but `accounting_post` returns previews and writes nothing; AP keys approved invoices manually.
3. Reversing a payable that was already posted is an **out-of-band, human-only** accounting action (void/credit memo) — never automated by this system. The runbook points the operator to the finance controls process; the idempotency log identifies exactly which keys posted, so there is no ambiguity about what to reverse.
Because the only state-modifying action is the gated post, rollback removes the ability to post without unwinding read paths.

## Failure-mode catalog (seed)
| Failure | Mitigation | Detected by |
|---------|-----------|-------------|
| Injection in invoice document (alter payee/amount/approval) | spotlighting + post args bound to extracted-from-spans values + code-gated post | injection-anomaly flag; post-args-vs-extraction mismatch alert |
| Duplicate submission / post retry | idempotency key — second attempt returns first result | idempotency-dedupe count; payable-count==1 check |
| Post without approval when HITL required | deterministic policy refuses post absent a valid token (fail-closed) | "post without token" alert (must be 0) |
| Bad extraction (wrong total) | extraction retries + source-span requirement + HITL for above-threshold | extraction-uncertain flag; sampled accuracy below floor |
| Validation lookup gap | MAX_LOOKUPS cap-fallback marks coverage-capped ⇒ forces HITL | unresolved-discrepancy count; coverage-capped flag |
| Stage crash mid-run | external state + resume-from-last-completed-stage; never re-post a posted key | missing stage span; resume event |
| Self-approval attempt | approver-must-differ-from-requester check | self-approval rejection event |
