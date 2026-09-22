---
name: propose
description: Render the proposal and SOW input from the engagement record, then run Gate B over the contract summary. Use this command when scope has passed Gate A and you need the client-facing document, or when a contract has arrived and you need the red-flag scan before signature. Blocks on unlimited liability, uncapped IP indemnity, unbounded assignment, long payment terms, uncompensated convenience termination, unilateral scope change or set-off, and missing counsel review.
version: "1.0.0"
category: orchestration
tags: [client-services, proposal, sow, contract-review, gate-b, consulting]
agents_used: [contract-risk-reviewer]
---

# /propose — Stages 5 and 6

*Not legal advice. Gate B is a structural scan over a summary you extracted by
reading the contract. Have a lawyer review before signature — the absence of that
review is itself a Gate B finding.*

Runs [`prompts/stage-5-proposal-and-sow.md`](../prompts/stage-5-proposal-and-sow.md)
and [`prompts/stage-6-contract-risk-review.md`](../prompts/stage-6-contract-risk-review.md).

## What it does

1. Renders the proposal deterministically from the record, with the proposal → SOW
   correspondence table:
   ```bash
   python3 skills/proposal-assembler/scripts/assemble.py --render <engagement.json>
   ```
2. Drafts the three prose sections the renderer cannot: the problem in the client's
   words, what success looks like, and pre-emption of the two or three objections
   discovery said would be raised.
3. Gates the draft through
   `domain-professional-writing/content-quality/quality_slop_client_deliverable.md`.
4. Runs Gate B over the contract summary:
   ```bash
   python3 skills/proposal-assembler/scripts/assemble.py --gateB <engagement.json>
   ```
5. Ranks the negotiating asks by resistance rather than by importance.

## Notes

Deliverable and acceptance language transfers to the SOW **verbatim**. If it has to
be rewritten to be contractual, it was not precise enough for the proposal either.

A blocking Gate B finding can be accepted, but only with a recorded rationale — so
that carrying a known risk is a decision with a name on it.
