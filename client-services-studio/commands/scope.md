---
name: scope
description: Turn a discovery record into a scope that can be priced, then run Gate A. Use this command after a discovery call, when you need deliverables with testable acceptance criteria, assumptions, exclusions and dated client inputs before any number is quoted. Refuses to let a price be set against an under-specified scope.
version: "1.0.0"
category: orchestration
tags: [client-services, scoping, gate-a, acceptance-criteria, consulting]
agents_used: [scope-guardian]
---

# /scope — Stage 3 and Gate A

*Not legal, tax, or accounting advice.*

Runs [`prompts/stage-3-scope-and-estimate.md`](../prompts/stage-3-scope-and-estimate.md)
then the gate in [`prompts/stage-4-price-and-package.md`](../prompts/stage-4-price-and-package.md).

## What it does

1. Builds deliverables with formats, acceptance criteria and per-deliverable effort
   estimates, applying the **stranger test** to each criterion: could someone holding
   only this sentence tell whether it had been delivered?
2. Converts every unresolved item from the discovery record into a resolved fact or a
   written assumption.
3. Writes the exclusion list against the six standard axes.
4. Writes client inputs with owner, date and a real consequence for lateness.
5. Executes Gate A:
   ```bash
   python3 skills/scope-ledger/scripts/scope_ledger.py --gateA <engagement.json>
   ```

## Output

The `scope` block of the engagement record. **No price appears in it** — that
separation is what lets Gate A refuse to price an under-specified scope.

## Notes

For fuzzy deliverables, delegate to
`domain-engineering-workflows/workflows/workflow_definition_of_done_builder.md`
(vendored under `referenced-prompts/`). It exists for exactly this.

If the client is pressing for a number before scope is finished, propose a **paid
discovery phase** rather than a qualified guess.
