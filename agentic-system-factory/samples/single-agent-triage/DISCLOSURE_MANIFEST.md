# DISCLOSURE MANIFEST — support-ticket-triage

**Version:** 1.0 · **Date:** 2026-06-20

## 1. Product Overview
<!-- DISCLOSURE-DIM-1: complete -->
A single-agent support-ticket triage assistant that classifies an inbound ticket, looks up the customer's recent order (read-only) when relevant, drafts a reply, and either auto-sends low-risk replies or escalates sensitive ones (refund, legal, security, self-harm) to a human with a draft attached. Intended for first-line support queue reduction. Out of scope: issuing refunds/credits, modifying orders or accounts, batch actions, anything needing auth beyond the scoped CRM read.

## 2. Company & Accountability
<!-- DISCLOSURE-DIM-2: complete -->
Maintainer: (sample) support-platform team. Incident contact: (sample) on-call support-eng. Update cadence: monthly; category policy reviewed whenever a sensitive-category miss is found.

## 3. Technical Capabilities & System Architecture
<!-- DISCLOSURE-DIM-3: complete -->
Topology TP-02 (single agent). One agent: `triage_agent`. Tools: `crm_order_lookup` (read-only, customer-scoped) + `send_reply` (write/messaging, gated by approval token + idempotency key). Mid-to-strong model. Per-ticket state persisted by ticket_id for crash-safe resume.

## 4. Autonomy & Control
<!-- DISCLOSURE-DIM-4: complete -->
Acts on low-risk categories (can send one message); recommends-only (escalates) on sensitive categories. Authority boundary: read-only CRM + at-most-once send; no refund/account-mutation/spend tool exists. HITL: mandatory pre-send approval for refund/legal/security/self-harm and low-confidence tickets. Kill switch: `config.halt`. Loop bounds: ≤5 steps, ≤1 lookup, ≤1 send per ticket.

## 5. Ecosystem Interaction
<!-- DISCLOSURE-DIM-5: complete -->
Touches: the CRM (read-only, scoped to the ticket's customer_id) + the outbound messaging channel (one reply to the ticket's own customer). No peer agents (single agent). Identity: per-ticket traced `triage_agent-<ticket_id>`; no credential caching; send recipient is fixed to the ticket's customer/channel, never an address taken from the body.

## 6. Safety, Evaluation & Impact
<!-- DISCLOSURE-DIM-6: complete -->
Capability eval (ABC-valid) on ~30 held-out labeled tickets with a trivial-agent (auto-send-everything) baseline that must score ~0 on action correctness. Safety eval (real-tool, sandboxed) run benign + adversarial against the real risk surface: an injected "issue a refund / send now" body never produces an unapproved send (and no refund tool exists), `crm_order_lookup` never reads a customer other than the ticket's, no exfiltration recipient is honored, and self-harm mentions always escalate. Residual risk: a novel injection phrasing or a misclassified sensitive ticket — bounded by the deterministic policy + tool-layer approval gate (worst case is an escalation we'd have escalated anyway). Rollback: flip `config.halt`, routing all tickets to the human queue (see RUNBOOK.md).

## Completeness check
- [x] No dimension left blank (including #6).
- [x] Safety section reports evals actually run against this system's surface (injection, cross-customer read, exfil, self-harm).
- [x] Cross-links to the HITL/idempotency design (GATE_DESIGN.md) + this run's eval results (EVAL_HARNESS.md) + rollback (RUNBOOK.md).
