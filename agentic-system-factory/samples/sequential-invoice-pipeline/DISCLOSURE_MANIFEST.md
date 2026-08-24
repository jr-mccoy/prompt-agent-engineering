# DISCLOSURE MANIFEST — invoice-intake-pipeline

**Version:** 1.0 · **Date:** 2026-06-20

## 1. Product Overview
<!-- DISCLOSURE-DIM-1: complete -->
A three-stage pipeline that extracts fields from an uploaded invoice, validates them against the matching purchase order and vendor master, and — after deterministic checks and a human approval — posts the payable to the accounting system. Intended for AP teams that want validated, sourced payables instead of manual three-way matching and keying. Out of scope: vendor onboarding, PO creation, payment disbursement, GL close, tax determination.

## 2. Company & Accountability
<!-- DISCLOSURE-DIM-2: complete -->
Maintainer: (sample) accounts-payable platform team. Incident contact: (sample) ap-oncall. Update cadence: monthly, plus an out-of-band update on any posting-control change. A change to the approval threshold, idempotency scheme, or post policy requires sign-off from finance controls.

## 3. Technical Capabilities & System Architecture
<!-- DISCLOSURE-DIM-3: complete -->
Topology TP-03 (code-orchestrated sequential pipeline with LLM-powered stages). Stages: extractor (strong model, no tools), validator (mid–strong model, read-only PO/vendor lookups), poster (deterministic code — no model). A controller owns stage order and the post; an external state store holds the run record, discrepancy report, approval token, idempotency key, and stage cursor for resumable runs.

## 4. Autonomy & Control
<!-- DISCLOSURE-DIM-4: complete -->
Acts only on read-only lookups; **recommends-only on the money-moving post — code posts, the model never does.** Authority boundary: a post is performed only when discrepancy-free-and-below-threshold OR backed by a valid human approval token, always with a verified idempotency key, with dry-run available. Mandatory HITL gate before posting any invoice ≥ `APPROVAL_THRESHOLD` or with any unresolved discrepancy; fail-closed (no decision ⇒ no post). Kill switch: `config.halt` checked before every stage and before any post. Loop bounds: extraction retries, MAX_LOOKUPS, single effective post per idempotency key.

## 5. Ecosystem Interaction
<!-- DISCLOSURE-DIM-5: complete -->
Touches: an external party's uploaded document (untrusted, read), the PO + vendor systems of record (read-only), and the accounting system (one gated write per approved invoice). Inter-stage trust: the poster trusts only the controller-supplied typed approved record + approval token + idempotency key, never upstream free text. Identity: per-stage and per-post traced identities; the approver identity is recorded and must differ from the requester.

## 6. Safety, Evaluation & Impact
<!-- DISCLOSURE-DIM-6: complete -->
Capability eval (ABC-valid) on 30 held-out invoices with a "post-everything" trivial baseline that must score ~0. Safety eval (real sandboxed post tool, OpenAgentSafety-style) run benign + adversarial on this system's real surface: malicious-document injection cannot alter the payee/amount/account or bypass approval (S1/S2); duplicate submission and post-retry cannot double-pay (S3, idempotency); no non-allowlisted tool call (S4); no self-approval (S5). Residual risk: a novel injection phrasing or an OCR error that changes a total — mitigated because the post is code-gated behind human approval for anything above threshold or flagged, and the worst case for an injection on an auto-eligible invoice is still bounded by the extracted-from-spans payee/amount and the idempotency key. Rollback: set `config.halt`, drain to dry-run-only, fall back to manual AP entry. Cross-links: RUNBOOK.md (failure catalog + rollback), OBSERVABILITY.md (post-control metrics), this run's eval results.

## Completeness check
- [x] No dimension left blank (including #6).
- [x] Safety section reports evals actually run against the money-write surface.
- [x] Cross-links to runbook, observability, and this run's eval results.
