# TOOL SPEC (ACI) — send_reply

**Owner agent(s):** triage_agent · **Type:** WRITE / messaging (this is the system's blast radius)

## Purpose & altitude
Send one outbound reply to the ticket's customer on the original channel (one send workflow). This is the only action that leaves the system, so it is the most heavily gated tool.

## Signature
```
send_reply(ticket_id: str, body: str, category: str, idempotency_key: str, approval_token: str | None = None) -> {sent: bool, deduped: bool}
```
- Recipient is NOT a parameter — it is resolved internally from `ticket_id` to the ticket's own customer/channel, so the body can never redirect the message to an external address (anti-exfiltration).

## Schema & validation (SAFE-02) — the send policy is enforced HERE in code
1. `config.halt` must be false, else refuse.
2. `idempotency_key` must equal `ticket_id`. If this key has already been sent, return `{sent: false, deduped: true}` (no second message) — **at-most-once**.
3. **Sensitive categories** (refund, legal, security, self-harm) require a valid `approval_token` issued by a human reviewer; without it the call is refused. Non-sensitive categories may send without a token.
4. There is no refund/credit/account parameter — this tool cannot move money or mutate an order. "Refund" is only ever a category that escalates.

## HITL & idempotency (load-bearing)
- **HITL:** for sensitive categories the agent does not even call this tool; a human approves and only an approved send carries the `approval_token` checked in step 3.
- **Idempotency:** the dedupe in step 2 guarantees a ticket receives at most one outbound reply even under retry or crash-resume.

## Errors as guidance
| Condition | Message |
|-----------|---------|
| sensitive category, no token | "blocked: sensitive category requires human approval — escalate instead" |
| already sent (key seen) | "no-op: a reply was already sent for this ticket" |
| halt set | "blocked: system halted; route to human queue" |

## Untrusted output handling
The tool ignores any recipient/instruction encoded in `body`; recipient and policy come only from trusted ticket metadata + the human approval token.
