# Architecture

*Not legal, tax, or accounting advice.*

## The design claim

A services practice loses money in four places, and all four are upstream of the
work itself: taking the wrong engagement, pricing an unspecified scope, signing a
contract whose structure was never examined, and failing to collect. Each has a
recognisable shape, which means each can be gated.

So the toolkit is not a set of documents. It is **four gates with prompts between
them.**

## Why gates are code, not instructions

A gate written as "check that the scope is complete before quoting" is advice, and
advice loses to the client who wants a number today. A gate written as a script with
an exit code does not.

The four gates are therefore implemented in Python, run from the stage prompts, and
their failure modes are asserted in a test suite that loads the same scripts the
pipeline runs. There is no test-only implementation, and no stage reports a gate
result it did not execute.

| Gate | Script | Enforces |
|---|---|---|
| 0 | `skills/scope-ledger/scripts/scope_ledger.py` | Qualification before discovery time |
| A | `skills/scope-ledger/scripts/scope_ledger.py` | Priceable scope before a number |
| B | `skills/proposal-assembler/scripts/assemble.py` | Contract structure before signature |
| C | `skills/engagement-economics/scripts/economics.py` | Closure before close-out |

## Why the record is separate from the prose

Every gate reads one JSON engagement record. That separation is deliberate:

- **Gate A can only work if the price is not in the scope block.** If the number is
  already written down, there is nothing left for the gate to protect.
- **The proposal is rendered from the record**, not written freehand, which is what
  guarantees the proposal → SOW correspondence holds. The document the client accepts
  and the document that governs delivery come from one source.
- **Drift detection is a diff**, which requires an agreed list to diff against.

Schema: [`skills/scope-ledger/references/record-schema.md`](skills/scope-ledger/references/record-schema.md).

## Why it orchestrates rather than contains

The parent repository already held the components this pipeline needs: SOW and MSA
drafters, targeted clause redlines and a risk heatmap, a freelance rate conversation,
a discovery-call preparation workflow, a definition-of-done builder, a status-report
writer, a case-study *evaluator*.

Rebuilding any of them would have been the specific defect the repository's structure
exists to prevent — two prompts doing the same job for the same reader. So 39 of them
are vendored under `referenced-prompts/` and invoked by the stage prompts.

What genuinely did not exist, and what ships alongside this toolkit as 20 net-new
domain prompts, is the commercial middle:

| Gap | Now at |
|---|---|
| Services offer, ICP, pricing model, retainer, capacity, productization, concentration | `domain-business-strategy/client-services/` |
| Rate floor, subcontractor margin, engagement profitability | `domain-finance/corporate-finance-fpa/` |
| Invoice schedule, AR aging, collections ladder | `domain-finance/accounting-controllership/` |
| Client engagement proposal, case study generator, testimonial and referral ask | `domain-professional-writing/business-writing/` |
| Payment terms, termination economics, subcontractor flow-down | `domain-legal/contracts-transactional/` |

Those land in `domain-*` directories rather than here, because that is where
`PROMPT_INDEX.json` indexes them and where they are reusable outside this pipeline.

## Why standard library only

No `requirements.txt`, no YAML, no dependencies, no network. The config is JSON for
that reason. A practitioner should be able to clone the directory and run every gate
on a laptop with a stock Python, and a reviewer should be able to read every line
that decides whether their contract is safe to sign.

Each script carries `--self-check`, which proves its own behaviour on planted
fixtures without touching the sample files.

## Why the gates are asymmetric

Gate B has three severities and an acceptance mechanism; Gates 0, A and C are binary.

That is a judgement about the underlying risk. A scope is either specified or not,
and an engagement is either closed or not — there is nothing to weigh. Contract
terms are different: a practice will knowingly accept net-90 from a client worth
having, and the right mechanism is not to block it but to require that the
acceptance be **recorded with a rationale**, so that carrying a known risk is a
decision with a name on it rather than an oversight.

Gate 0 has the same shape at the level of its disqualifiers: `decline` blocks,
`probe` and `proceed_with_protection` warn. A gate that only ever declines is a gate
that gets switched off the first time the pipeline is thin.

## Why the loop closes

Stage 9 writes back to Stage 0. Three quantities flow:

```
typical overrun ─────────► rate floor risk loading
estimate-error CV ───────► fixed-price eligibility
client verdict ──────────► disqualifier list
```

Without the loop, the rate floor uses a guessed overrun, fixed prices are quoted on
belief, and the disqualifier list stays theoretical. This is why Gate C blocks on
unrecorded unbilled effort and a missing client verdict: those are not bookkeeping,
they are the inputs the next engagement's pricing depends on.

## What this deliberately does not do

- **Interpret contracts.** Gate B scans a summary a human produced by reading the
  document. The alternative — parsing contract text — would produce confident output
  from an unreliable extraction, on the one topic where being confidently wrong is
  most expensive.
- **Store more than one engagement.** No database, no multi-engagement state. A
  practice needing that has outgrown this and wants a CRM.
- **Touch the network or transmit anything.** Client names, rates and contract terms
  are the most sensitive data here and never leave the disk.
- **Draft legal instruments.** The collections ladder stops at rung 7 and hands off.

## Manifest

| Component | Count | Path |
|---|---|---|
| Stage prompts | 10 | `prompts/` |
| Gates enforced in code | 4 | `skills/*/scripts/` |
| Skills | 4 | `skills/` |
| Commands | 4 | `commands/` |
| Agents | 3 | `agents/` |
| Fixtures (incl. 5 negative) | 10 | `samples/` |
| Tests | 37 | `tests/` |
| Vendored prompts | 39 | `referenced-prompts/` |
| Net-new domain prompts shipped alongside | 20 | `domain-*/` |
