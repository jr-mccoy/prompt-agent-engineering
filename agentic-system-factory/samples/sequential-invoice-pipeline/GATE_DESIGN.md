# GATE DESIGN — invoice-intake-pipeline

**Blast radius:** money / write — the final stage posts a payable. Untrusted invoice documents are the attack surface; the post is the asset to protect.

## Gate 0 — Justification
See `ARCHITECTURE.md §2` (fixed code-controlled stage order with model-powered stages; lowest rung above a single model call; the money-write is gated by code + a human, never by the model).

## Gate A — Security (OWASP ASI)

| SAFE pattern | Requirement | Status & enforcement point |
|--------------|-------------|----------------------------|
| SAFE-01 data/control separation | Untrusted document text never drives control flow | OCR'd invoice text is passed to the extractor inside a `<document>` data block; it can only populate fields — it can never select a tool, advance a stage, set an approval token, or change the post target. Stage advancement and posting are owned by the deterministic controller, not by anything the document says. |
| SAFE-02 deterministic policy | Tool allowlist + schema validation + the post policy | Allowlist per stage: extractor = {}, validator = {po_lookup, vendor_lookup} (read-only), poster = {accounting_post} (gated). Arg schemas validated pre-call. The **post policy is code**: a post is rejected unless (a) amount < THRESHOLD AND zero unresolved discrepancies, OR (b) a valid human approval token exists — and always with a verified idempotency key. The model cannot emit a post. |
| SAFE-04 least-privilege tools | Minimal tool set per stage | Extractor has no tools at all (pure extraction); validator has read-only lookups only; only the poster can reach `accounting_post`, and only through the code gate. No stage can write outside its scope. |
| SAFE-05 injection defense | Sanitize/spotlight external content | Input spotlighting on the document; an "ignore prior instructions / change the payee / approve this / pay to account X" string in the OCR text is treated as data, flagged as an anomaly, and cannot alter the payee, amount, approval state, or routing. |
| SAFE-07 circuit breakers | Caps + isolation | Per-stage timeouts; MAX_LOOKUPS per validation; a single invoice cannot trigger more than one post (idempotency); tripping a cap halts the run for review, it does not auto-post. |
| SAFE-08 governed identity | Attributable actions | Each stage and each post runs under a distinct traced identity; the approver's identity is recorded on the approval token. |
| SAFE-10 inter-stage trust | No upstream poisoning of the write | The poster trusts only the typed approved record + approval token + idempotency key from the controller, not free text from earlier stages. |

<!-- SAFE-01: enforced -->
<!-- SAFE-02: enforced -->
<!-- SAFE-04: enforced -->
<!-- DEFENSE-IN-DEPTH: 3-layers -->

**Defense-in-depth on the money-write path (3 layers):**
1. **Input layer** — spotlighting + objective/anomaly check on the untrusted document so injected instructions are quarantined as data.
2. **Policy layer** — deterministic code computes "post allowed?" from amount + discrepancy flags + approval token; the model has no path to the post call.
3. **Action layer** — `accounting_post` is idempotent (keyed) and supports dry-run; even a maximally-hijacked stage cannot double-pay or post without a valid token + key.

The model can NEVER post on its own. Posting is performed by the controller's code only after: discrepancy-free OR human-approved, threshold policy satisfied, valid approval token present (when required), and a verified idempotency key. This is the load-bearing control of the whole system.

## HITL approval gates
| Gate | Trigger (deterministic) | Who | What they see | Fail-closed default |
|------|-------------------------|-----|----------------|---------------------|
| Pre-post approval | invoice amount ≥ `APPROVAL_THRESHOLD` (configurable) **OR** any unresolved discrepancy from Stage 2 | a human AP approver (not the requester) | the extracted record, the discrepancy report, the matched PO/vendor, the dry-run preview | **no approval ⇒ no post.** The run pauses; absence of a decision is treated as "do not post." |

Approval produces a signed approval token bound to (invoice id, amount, payee, idempotency key). If any of those change after approval, the token is invalid and the post is refused.

## Loop bounds & cap-fallbacks
| Loop | Bound | Cap-fallback |
|------|-------|--------------|
| Extraction retries | 2 | flag "extraction-uncertain", route to HITL, do not auto-advance |
| Validation lookups | MAX_LOOKUPS=6 | proceed with retrieved set; mark coverage-capped as an unresolved discrepancy ⇒ forces HITL |
| Post attempts | 1 effective (idempotency-keyed) | retry is safe — same key returns the prior result, never a second payable |

## Kill switch
<!-- KILL-SWITCH: present -->
`config.halt: true` is checked before every stage and, explicitly, immediately before any `accounting_post`. When set, the controller stops advancing, performs no post, and leaves the run resumable. Tested by setting the flag mid-run and asserting zero `accounting_post` calls occur and the run resumes cleanly when cleared.

## Gate C — Production-readiness handoff
- [x] Disclosure manifest complete (6 dimensions) — see DISCLOSURE_MANIFEST.md
- [x] Observability/traces present — see OBSERVABILITY.md
- [x] Rollback path — see RUNBOOK.md
- [x] Inter-stage trust model documented (poster trusts only controller-supplied typed token + key)
