---
name: scope-ledger
description: Hold the engagement record of truth for a client-services engagement and enforce the two gates in front of a price. Use this skill to "qualify a lead", "check whether this scope can be priced", "run Gate 0", "run Gate A", "detect scope creep", "has this engagement drifted", or "do I need a change order". Blocks a lead that fails the practice's disqualifier rules, refuses to price a scope missing deliverables, acceptance criteria, assumptions, exclusions or dated client inputs, and diffs delivered work against agreed scope to name change-order triggers. Structural checks only — it verifies that an acceptance criterion exists, not that it is a good one.
license: MIT
compatibility: Standard library only, Python 3.9+. `scripts/scope_ledger.py` implements Gate 0, Gate A and drift detection over JSON records; `--self-check` proves both gates block and pass on planted fixtures, including each individual failure mode. No dependencies, no network, no writes.
metadata:
  tags: [client-services, scope, gate, qualification, change-order, consulting, freelance]
  updated: "2026-09-21"
---

# Scope Ledger

The engagement record of truth. Every other stage in this toolkit reads from the
record this skill maintains, and two of the pipeline's four gates live here.

## Purpose

Services engagements fail in two places, and both are upstream of delivery. The
first is taking work that should have been declined in the first ten minutes. The
second is quoting a price against a scope that was never specified well enough to
be priced — which is how a fixed fee becomes an open commitment.

This skill makes both failures loud and machine-checkable.

- **Gate 0 (qualify)** blocks a lead with no named decision-maker, no budget
  authority, no defined outcome, an implied rate below the practice floor, or a
  concentration breach — plus any `decline`-tier disqualifier the practice has
  declared in its config.
- **Gate A (priceable scope)** refuses to let a price be quoted while the scope
  record lacks deliverables, assumptions, exclusions or client inputs; while any
  deliverable has no format or no acceptance criterion; while any client input has
  no owner, no due date, or no stated consequence for lateness; or while no
  decision-maker is named.
- **Drift detection** diffs delivered work against agreed deliverables. Work that
  is not an agreed deliverable is a change-order trigger; work that appears on the
  exclusion list is a high-severity finding, because it was explicitly out.

## When to Use This Skill

- A new inquiry has arrived and you are deciding whether to spend discovery time
- Scope has been written and a number is about to be quoted
- An engagement is running and you suspect it has drifted
- You are about to say yes to "one small extra thing"

Do **not** use it to judge whether a scope is *good*. It checks that an acceptance
criterion exists; whether the criterion is objectively testable is a human
judgement, and `domain-engineering-workflows/workflows/workflow_definition_of_done_builder.md`
is the resource for sharpening it.

## Usage

```bash
python scripts/scope_ledger.py --gate0 lead.json --config ../../config/practice.json
python scripts/scope_ledger.py --gateA engagement.json
python scripts/scope_ledger.py --drift engagement.json --delivered delivered.json
python scripts/scope_ledger.py --self-check
```

Exit code 0 means pass; 1 means the gate is blocked or drift was found.

## Records

See [`references/record-schema.md`](references/record-schema.md) for the lead,
engagement and delivered record shapes, and `../../samples/` for worked fixtures
including the negative cases.

## Boundaries

- **Structural, not substantive.** A scope can pass Gate A and still be a bad scope.
- **Not legal advice.** Nothing here interprets a contract.
- **Disqualifiers are base rates, not verdicts.** A `probe`-tier signal warns; the
  probe result decides.
