# AGENT SPEC — poster (Stage 3)

**System:** invoice-intake-pipeline · **Role:** poster (final stage — the money-write)

> **This stage uses NO model.** "Poster" is the deterministic controller code that performs the post. There is no LLM in the post path — by design, so that a model can never move money.

## Identity & authority
- Governed identity: traced `poster-<run_id>` (and the post call carries the approver identity).
- Model: **none — deterministic code.**
- Authority: Can-Do = call `accounting_post` exactly when policy permits. Ask-First = the post itself, via the mandatory HITL gate. **Never** = post on a model's say-so, post without a verified idempotency key, post a record whose payee/amount differs from the approved one, or post twice for the same key.

## Post policy (deterministic — the load-bearing control)
A post is performed **only if all hold:**
1. `config.halt` is not set (kill switch clear).
2. Either (a) `amount < APPROVAL_THRESHOLD` **and** `unresolved_discrepancies == 0`, **or** (b) a valid human **approval token** is present.
3. The approval token (when required) is bound to (invoice id, amount, payee, idempotency key) and was signed by an approver **different from the requester**; if any bound field changed since approval, the token is invalid ⇒ refuse.
4. A verified **idempotency key** is attached; if the key is already marked posted, return the prior result (no second payable).
Otherwise: **do not post** (fail-closed) — pause the run for HITL or hold.

## Dry-run
If `dry_run` is set (default in shadow mode), `accounting_post` returns a full preview of the payable it *would* create and writes nothing. The HITL approver reviews this preview before approving a real post.

## Tools
| Tool | Scope | Spec |
|------|-------|------|
| accounting_post | **gated write** (idempotent, dry-run capable) | tools/accounting_post.md |

## Memory & state
Reads only the controller-supplied typed approved record + approval token + idempotency key (SAFE-10) — never upstream free text. Writes the post result + the key's posted-status to the external state store.

## Guardrails
- Code-gated post (model has no path to it).
- Idempotency: one effective post per key; retries are safe.
- Pre-post `config.halt` check; post args verified against the approved record.

## Loop & bounds
Post attempts: 1 effective per idempotency key. A crash-and-retry returns the first result via the key — it never double-pays.
