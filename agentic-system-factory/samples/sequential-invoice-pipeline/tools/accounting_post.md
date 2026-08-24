# TOOL SPEC (ACI) — accounting_post

**Owner agent(s):** poster (deterministic controller code only — never an LLM)

> This is the only write in the system and the only place money moves. It is built so that even a fully-hijacked upstream stage cannot cause an unapproved, altered, or duplicate payment.

## Purpose & altitude
Post an approved invoice as a payable to the accounting system (one gated, idempotent write workflow — not a raw "INSERT payment" the model can shape).

## Signature
```
accounting_post(
    approved_record: ApprovedInvoice,     # typed; payee, amount, currency, po_id bound at approval
    idempotency_key: str,                 # required, unique per invoice
    approval_token: ApprovalToken | None, # required when policy demands HITL
    dry_run: bool = False
) -> {posted: bool, payable_id: str | None, deduped: bool, preview: dict | None}
```

## Schema & validation (SAFE-02) — the deterministic post gate
The tool itself re-enforces the post policy (defense in depth; it does not trust the caller to have checked):
1. **Kill switch:** if `config.halt` is set → refuse (`posted=False`), no write.
2. **Idempotency:** if `idempotency_key` is already marked posted → return the prior `payable_id` with `deduped=True`; **no second payable** is ever created. This is what makes a retry / duplicate submission safe.
3. **Approval:** if the amount ≥ `APPROVAL_THRESHOLD` or `approved_record.unresolved_discrepancies > 0`, a valid `approval_token` is **required**. The token must be bound to (invoice id, amount, payee, idempotency_key) and signed by an approver ≠ requester. If absent or mismatched → refuse, no write.
4. **Tamper check:** the payee/amount/currency actually written must equal the values bound in `approved_record`/`approval_token`. A mismatch (e.g. an injected payee) → refuse, no write, raise an alert.
5. **Dry-run:** if `dry_run` → return `preview` of the payable, write nothing, consume no idempotency key.

Permission scope is a single, narrow "create-payable" grant — no edit/delete/disburse.

## Errors as guidance
| Condition | Message |
|-----------|---------|
| halt set | "halted — no post performed" |
| key already posted | "deduped — returning existing payable; no second payment" |
| missing/invalid token | "approval required and not present/valid — refusing post (fail-closed)" |
| bound-field mismatch | "post args differ from approved record — refusing and alerting (possible tampering)" |

## Untrusted output handling
Returns the system's own write result (trusted). The model never calls this tool and never sees a path to it; the controller calls it after the policy in `agents/poster.md` is satisfied. The post can NEVER be initiated by model output — only by deterministic code after approval + checks.
