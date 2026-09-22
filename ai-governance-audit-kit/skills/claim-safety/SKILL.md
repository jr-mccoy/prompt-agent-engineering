---
name: claim-safety
description: Refuse to ship an audit report that claims more than its evidence supports. Use this skill to "check the report before it goes out", "have we overclaimed", "review this deliverable for unsupported claims", "is this ROI figure defensible", or before any governance report, case study or summary leaves the building. Runs Gate B, blocking directional claims with no interval, ROI figures, asserted quality tiers, unstamped fixture numbers and missing limitations.
license: MIT
compatibility: Standard library only, Python 3.9+. `scripts/claim_guard.py --self-check` proves each of six rules blocks its own negative fixture, that a clean report passes, and that the same forbidden sentences fenced as counter-examples do not trip the gate. No network, no writes.
metadata:
  tags: [audit, claims, adr-0040, governance, gate, reporting, evidence]
  updated: "2026-09-22"
---

# Claim Safety

## Purpose

An audit report is the single most likely place for a careful evidence standard
to be quietly forgotten, because a client is paying for a conclusion and a
conclusion wants a number attached.

`meta/adr/0040-public-performance-claim-governance.md` is Accepted and
implemented, and its consequence is stated flatly: *"Nothing in this repository
currently supports any public performance claim, and the tooling says so."*

This is the skill that says so. It is also, of the four gates, the one that
protects the person selling the engagement rather than the one buying it.

## What Gate B blocks

| Rule | Blocks |
|---|---|
| `forbidden_sentence` | the claims ADR-0040 forbids by name |
| `unlicensed_direction` | a directional word beside a quantity with no interval |
| `roi_or_money_claim` | payback, ROI, "pays for itself", a currency figure |
| `undisclosed_tier` | "is Tier N" stated as a fact |
| `fixture_figure_unstamped` | fixture-derived figures with no synthetic stamp |
| `missing_limitations` | quantities with no Limitations section, or too thin a one |

`unlicensed_direction` is narrower than it first looks, and deliberately. The
ADR's rule is that there is no code path writing "improved" *without a number
requiring it*. A directional word with no number carries nothing to mislead
with — "this gate reduces the chance of an unbacked claim" is ordinary prose,
and a gate that blocks ordinary prose gets switched off, which protects nobody.

## Fenced examples never trip the gate

Prose detectors run on text with fenced blocks and inline code spans removed,
the same anti-gaming rule as `agentic-system-factory/scripts/check_gate.py`.
Without it, `references/forbidden-claims.md` — which quotes every forbidden
sentence — could not be written. It is also the escape hatch for a report that
genuinely needs to *discuss* an ROI figure: put it in backticks.

## When to Use

- Before any report, summary, case study or slide goes to a client.
- Before publishing anything derived from a fixture or a sample run.
- When someone asks you to "just put a number on the improvement".

## When NOT to Use

- As a substitute for having evidence. The gate checks the claim against the
  shape of its support; it cannot tell you whether the underlying number is
  true.
- On prose that is not a claim-bearing deliverable. Running it over source code
  or meeting notes produces noise.

## Instructions

1. Write the report. Include a `## Limitations` section with at least the
   configured minimum number of entries, written from *this* run rather than
   remembered from a template.
2. Stamp any figure drawn from a fixture or sample corpus with
   `SYNTHETIC TEST FIXTURE — NOT INDEPENDENT BENCHMARK EVIDENCE`.
3. Run `scripts/claim_guard.py <report.md>`.
4. Fix findings by removing the claim or by adding the evidence that licenses
   it. Do not fix one by moving it into a fence unless it genuinely is a quoted
   counter-example.
5. Re-run until Gate B passes. There is no advisory tier: any finding blocks.

## Bundled Resources

- `scripts/claim_guard.py` — the six rules, Gate B, and the CLI.
- `references/forbidden-claims.md` — every forbidden sentence, the licensing
  rule for a directional word, and a rewrite for each blocked pattern.

## Safety

Read-only. The gate can be wrong in one direction only that matters: it can
block a sentence that was defensible. That is the cheap error, and the fix is
to add the evidence or rephrase.

## Troubleshooting

- A methodological sentence is blocked: it contains both a directional word and
  a two-digit number. Separate the sentence or quote the number in backticks.
- The gate blocks the report's own description of what it will not say: fence
  the examples, as `samples/reports/report_fenced_counterexamples.md` does.

## Verification

- [ ] Gate B passes with zero findings.
- [ ] Every fixture-derived figure carries the stamp.
- [ ] Limitations were written from this run, not copied from the last one.
- [ ] No sentence claims a direction the evidence cannot license.

## Related Skills

- `observed-scoring` — produces the numbers this gate governs the reporting of.
- `registry-handback` — the other place a claim can leak, as record metadata.
