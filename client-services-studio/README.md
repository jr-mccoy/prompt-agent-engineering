# Client Services Studio

*Not legal, tax, or accounting advice. Contract outputs are drafts and structural
flags for a lawyer to review before signature; financial outputs are estimates for a
conversation with an accountant. See [Boundaries](#boundaries).*

**Status: BUILT.** Ten stage prompts, four skills with working standard-library
scripts, four gates enforced in code, four slash commands, three agents, 39 vendored
referenced prompts, and a 37-test suite. [`DRY_RUN.md`](DRY_RUN.md) shows every gate
firing on the [`samples/`](samples/) fixtures, including the negative cases.

---

## What this is

A pipeline for people who **sell expertise** — consultants, freelancers, agencies —
covering the full revenue cycle from an inbound inquiry to a paid invoice and a
published case study.

```
Qualify → Discover → Scope → Price → Propose → Contract → Deliver
  ↑                                                          ↓
  └──── Close out ←── Invoice & collect ←───────────────────-┘
        (feeds the rate floor, the disqualifier list,
         and fixed-price eligibility back to the start)
```

**Four gates, enforced in code, not by judgement:**

| Gate | Stage | Refuses to |
|---|---|---|
| **Gate 0** — qualify | 1 | Spend discovery time on a lead with no named decision-maker, no budget authority, no defined outcome, a sub-floor implied rate, a concentration breach, or a decline-tier disqualifier |
| **Gate A** — priceable scope | 4 | Quote a price against a scope missing deliverables, acceptance criteria, assumptions, exclusions, or client inputs with owners, dates and consequences |
| **Gate B** — signature risk | 6 | Mark an engagement closeable while a red-flag clause is unresolved and un-rationalised, or while no lawyer has reviewed it |
| **Gate C** — close-out | 9 | Close an engagement with money outstanding, unbilled effort unrecorded, or no client verdict |

Gate A is the one that earns its keep. Pricing an under-specified scope is the most
expensive routine mistake in services work, and it feels like momentum at the time.

## What this is not

- **Not a CRM.** It holds one engagement record at a time, as JSON on your disk.
- **Not a contract reader.** Gate B scans a summary *you* produced by reading the
  contract. It flags structures; it never interprets law.
- **Not a replacement for the domain prompts.** It orchestrates 39 of them. Where a
  stage needs depth — running the discovery call, redlining a clause, holding the
  rate conversation, writing the case study — it hands off.

## Why it exists

The repository already held the components: SOW and MSA drafters, clause redlines, a
freelance rate conversation, a status-report writer, a case-study evaluator. What did
not exist anywhere was the **sequence**, with gates, plus the commercial middle
nobody covers — pricing a services offer, scoping it so it can be priced, tracking
scope against it, and getting paid. The 20 net-new prompts this ships with fill that
middle; this toolkit sequences all of it.

## Usage

Four modes, same pipeline.

| Mode | How |
|---|---|
| **Guided** | Start at [`orchestrator_client_services.md`](orchestrator_client_services.md) and let it drive |
| **Commands** | `/qualify`, `/scope`, `/propose`, `/collect` — see [`commands/`](commands/) |
| **Manual** | Work through [`prompts/`](prompts/) stage by stage; see [`PIPELINE_OVERVIEW.md`](PIPELINE_OVERVIEW.md) |
| **Surgical** | Run one skill script directly against your own JSON |

### Setup

No installation. Standard library only, Python 3.9+.

```bash
cd client-services-studio
for s in skills/*/scripts/*.py; do python3 "$s" --self-check; done
python3 -m unittest discover -s tests -v
```

Then run **Stage 0** to produce `config/practice.json`. The shipped config is a
worked example, not a recommendation — every number in it is wrong for you.

```bash
python3 skills/engagement-economics/scripts/economics.py --floor config/practice.json
```

### The four skills

| Skill | Owns |
|---|---|
| [`scope-ledger`](skills/scope-ledger/) | The engagement record; Gate 0, Gate A, drift detection |
| [`engagement-economics`](skills/engagement-economics/) | Rate floor, realised margin, estimate-error series, Gate C |
| [`proposal-assembler`](skills/proposal-assembler/) | Proposal/SOW rendering, Gate B |
| [`receivables-tracker`](skills/receivables-tracker/) | Invoice schedule, AR aging, escalation ladder |

## Self-contained

Every prompt the pipeline orchestrates is vendored under
[`referenced-prompts/`](referenced-prompts/), so this directory can be unpacked on
its own. Those are pinned copies; the maintained originals live in the parent
repository and `meta/VENDORED.tsv` records each pair, with CI enforcing that they do
not drift.

## Boundaries

- **Not legal advice.** Gate B is a structural scan over a human-written summary. It
  cannot tell you what a clause means, whether it is enforceable, or what your
  jurisdiction does with it. `counsel_reviewed: false` is itself a blocking finding —
  the scan passing is not a substitute for a lawyer.
- **Not tax or accounting advice.** Employment-burden rates, deductibility, entity
  treatment, revenue recognition and provisioning are jurisdiction-specific. The rate
  floor and the margin post-calculation are arithmetic, not counsel.
- **Structural, not substantive.** Gate A verifies that an acceptance criterion
  exists. Whether it is a *good* criterion is a human judgement.
- **Collections stops short of legal process.** The ladder's rungs 6 and 7 hand off
  to a demand letter and to advice. The tool will not draft either.
- **Your client's data is the most sensitive thing here.** Names, rates and contract
  terms live in the JSON records. Nothing in this toolkit transmits anything; keep
  `config/` and your engagement records out of any repository you publish.

## Layout

```
client-services-studio/
├── prompts/              # stage-0 … stage-9
├── commands/             # /qualify /scope /propose /collect
├── agents/               # engagement-orchestrator, scope-guardian, contract-risk-reviewer
├── skills/               # four bundles, each SKILL.md + scripts/ + references/
├── config/practice.json  # worked example — replace every number
├── samples/              # fixtures, including the negative cases
├── tests/                # 37 tests
└── referenced-prompts/   # 39 pinned copies
```
