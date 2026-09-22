# Verticals

The pipeline pre-configured for one trade. Five exemplars ship here; the pattern is
documented below so the rest are mechanical.

*Not legal, tax, accounting or insurance advice. Every number in every config is a
worked example, not a benchmark — see the warning below.*

## Why verticals exist

`client-services-studio/` is deliberately trade-agnostic: it sequences qualification,
scoping, pricing, proposal, contract, delivery, invoicing and close-out for anyone who
sells expertise. That generality is what makes it reusable and what makes it a blank page
on day one.

A vertical closes the blank page. It supplies a starter practice config with the trade's
typical cost and capacity shape, names the deliverable writer that trade already has in
this repository, and lists the contract clauses and disqualifiers that bite in that
trade specifically.

## What is here

| Vertical | Deliverable writer it pairs with | Distinctive risk |
|---|---|---|
| [`hvac/`](hvac/) | `domain_writing_hvac_estimate.md` | Site unseen before quoting; landlord/tenant payer ambiguity |
| [`architect/`](architect/) | `domain_writing_architect_proposal.md` | Consent risk outside your control; long estimate variance |
| [`cpa/`](cpa/) | `domain_writing_cpa_tax_strategy.md` | Statutory deadlines; unreconcilable prior-year records |
| [`management-consultant/`](management-consultant/) | `domain_writing_consultant_executive_summary.md` | Undiagnosed scope; sponsor above the contact |
| [`landscaper/`](landscaper/) | `domain_writing_landscaper_proposal.md` | Weather; ground conditions discovered on the day |

The remaining client-services-shaped writers in
`domain-professional-writing/domain-specific/` — electrician, plumber, realtor,
financial adviser, insurance, wedding planner, counselor, dentist, veterinarian, and
the contractor remodel writer — have no pack yet. Adding one follows the pattern below.

## ⚠ Every number in every config is invented

The configs carry plausible-looking cost, capacity and rate figures. **They are worked
examples so the gates have something to run against, and they are not benchmarks, market
data, or advice.** A gate result computed from someone else's invented numbers is
meaningless.

Run [`../prompts/stage-0-practice-config.md`](../prompts/stage-0-practice-config.md)
and replace every value with your own. The vertical saves you the blank page; it does not
save you the arithmetic.

## The pattern — adding a vertical

### 1. Create the directory

```
verticals/<trade>/
├── README.md        # the only prose file permitted — see the naming constraint
└── practice.json
```

### 2. The naming constraint, and why it is load-bearing

**Every prose file in a vertical must be named exactly `README.md`.**

`README.md` is in `META_DOC_FILENAMES` in `scripts/pae_registry/membership.py`, so it is
excluded from the registry wherever it appears. `.json` is not Markdown, so `discover()`
never sees it. Together that means a verticals tree adds **zero** registry resources and
needs no membership change.

Any other prose filename — `notes.md`, `guide.md`, `pricing.md` — falls through
`classify()` to rule 10 and becomes a first-class `prompt` resource with a UID, a public
ID and a permanent identity in the ledger. If a vertical genuinely needs more prose than
one README, add `client-services-studio/verticals/` to `NON_RESOURCE_PREFIXES` first and
regenerate the registry.

### 3. Derive the config, do not copy it

Run Stage 0 for the trade, then verify the stored rate matches the computed one:

```bash
python3 skills/engagement-economics/scripts/economics.py --floor verticals/<trade>/practice.json
```

`walk_away_day_rate` in the file must equal the computed `walk_away_day_rate`. They are
stored separately so Gate 0 runs without recomputing, which means they can drift — the
test suite checks every vertical for this, so a mismatch fails CI rather than silently
producing wrong Gate 0 results.

The fields that actually differ by trade:

| Field | What drives it |
|---|---|
| `capacity.billable_fraction` | Trades with travel and site time run lower than desk-based advisory; trades with repeat maintenance contracts run higher |
| `risk.typical_overrun` | Design and discovery work overruns far more than repeatable installation work |
| `risk.bad_debt_rate` | Consumer-facing and construction-adjacent trades carry materially more |
| `positioning_premium` | Advisory and licensed professions sustain more than commodity installation |
| `concentration_limit_pct` | Lower where one client can dominate a small book |

### 4. Write the trade's disqualifiers

Keep the three common ones — no written scope, no named decision-maker, prior vendors all
blamed — and add two or three that are specific to the trade. The trade-specific ones are
the point; the common ones are table stakes.

### 5. Name the contract red flags that bite in this trade

Gate B's ten flags are general. Each trade has clauses that matter more: retention in
construction, consent conditions in design, statutory deadlines in accountancy,
unlimited liability in advisory. List them in the README and point at the reviewing
prompt in `domain-legal/contracts-transactional/`.

### 6. Register nothing, and check

No membership change, no `VENDORED.tsv` entry, no `REPO_FACTS` movement. Confirm it:

```bash
python3 scripts/generate_registry.py --check      # from the repo root
python3 scripts/generate_repo_facts.py --check
```

Both should pass unchanged. If `--check` reports drift, a prose file is misnamed.

## Using a vertical

```bash
cd client-services-studio
# Replace the invented numbers first.
python3 skills/engagement-economics/scripts/economics.py --floor verticals/hvac/practice.json
# Then run the pipeline against it.
python3 skills/scope-ledger/scripts/scope_ledger.py --gate0 <lead.json> \
    --config verticals/hvac/practice.json
```

Every gate takes `--config`, so a vertical config substitutes for `config/practice.json`
throughout the pipeline.
