---
name: proposal-assembler
description: Render a client proposal and its SOW correspondence table deterministically from the engagement record, and run Gate B over the contract summary before signature. Use this skill to "draft the proposal", "generate the SOW", "check the contract for red flags", "run Gate B", "is this contract safe to sign", or "what should I push back on". Produces a proposal whose sections map one-to-one onto the statement of work, and flags unlimited liability, uncapped IP indemnity, unbounded assignment, long payment terms, uncompensated termination for convenience, unilateral scope change, unilateral set-off and unpriced transition assistance. Structural scan over a summary you have extracted — it does not read contracts and does not replace a lawyer.
license: MIT
compatibility: Standard library only, Python 3.9+. `scripts/assemble.py` renders Markdown from an engagement record and implements Gate B over a contract summary; `--self-check` proves rendering is deterministic and that each red flag blocks, that medium findings warn without blocking, and that a flag can only be accepted with a recorded rationale. No dependencies, no network, no writes.
metadata:
  tags: [client-services, proposal, sow, contract-review, gate, red-flags, consulting]
  updated: "2026-09-21"
---

# Proposal Assembler

## Purpose

Two jobs, joined because they share one failure: a proposal that does not become
the contract.

**Render.** Builds the proposal from the engagement record, with a
correspondence table mapping every proposal section onto the SOW section it
becomes — deliverables to deliverables schedule, acceptance to acceptance
criteria, exclusions to exclusions, and so on. Rendering from the record rather
than writing freehand is what guarantees the correspondence holds: the document
the client accepts and the document that governs delivery are generated from the
same source.

**Gate B (signature risk cleared).** A structural scan over a contract summary you
have already extracted. It flags ten conditions, at three severities. Critical and
high findings block; medium findings warn. A blocking flag can be accepted — but
only with a **recorded rationale**, so that carrying a known risk is a decision
with a name on it rather than an oversight. Absence of a counsel-review record is
itself a high finding.

The flags: unlimited liability, uncapped IP indemnity, assignment extending beyond
deliverables to all work product, payment terms beyond 60 days, termination for
convenience with no compensation, unilateral scope variation, no right to suspend
for non-payment, unilateral set-off, unpriced transition assistance, and no
obligation to pay the undisputed portion of a disputed invoice.

## When to Use This Skill

- Scope has passed Gate A and a proposal is being written
- A contract or SOW has been received and is about to be signed
- An existing client relationship is being renewed on rolled-forward terms

## Usage

```bash
python scripts/assemble.py --render engagement.json
python scripts/assemble.py --gateB engagement.json
python scripts/assemble.py --self-check
```

## Boundaries

- **Not legal advice, and not a contract reader.** Gate B scans a structured
  summary that a human produced by reading the contract. It cannot tell you what a
  clause means, whether it is enforceable, or what your jurisdiction does with it.
  It exists to stop known-bad structures reaching signature unnoticed.
- **Counsel review is a gate condition, not a suggestion.** The scan passing is not
  a substitute for it.
- The clause-level drafting positions live in
  `domain-legal/contracts-transactional/` — see
  [`references/red-flags.md`](references/red-flags.md) for the mapping.
