# ADR-0043 — Subject homes for sales and customer work, business analytics, operations and consumer wellness

## Status

Accepted. Implemented in coverage Wave 1
([`../COVERAGE_ROADMAP.md`](../COVERAGE_ROADMAP.md)). The deferred routing
regression cases shipped in coverage Wave 5 — see the amendment below.

## Context

`CLAUDE.md` is the canonical router (ADR-0006). Its filing rule is **subject
decides first; audience decides among the work domains**. A prompt whose object
belongs to a discipline goes to that discipline's domain. Only prompts with no
subject home fall through to the five scope-ordered work domains.

The repository-wide coverage audit found four subjects with real demand whose
prompts had nowhere to go by subject:

| Subject | What existed | What `pae search` returned |
|---|---|---|
| Sales, customer success, support | ~5 prompts in `business-strategy/go-to-market/`, filed there by a `CLAUDE.md` worked example calling them "org" work | Solo-dev marketing prompts and marketing skills |
| Business analytics | Fragments in `AI-ML/` (model evaluation), `presentations/board-decks/` (rendering), `science/statistics/` (research inference) | Engineering SQL-performance material for analyst questions |
| Operations: process, supply chain, procurement, quality | `risk_fmea_analysis` and one vendor evaluation | `lean-canvas` for "lean six sigma" |
| Consumer training, nutrition, sleep | `home_meal_plan_week` (logistics); clinical and psychology prompts for patients | Faculty-development prompts for "strength training program" |

Each of these could have been filed under an existing domain by theme. Those
placements would all have been placements by resemblance, not by subject:
- sales under business strategy;
- analytics under science;
- operations under risk;
- wellness under productivity or healthcare.

This is the mis-filing the axis exists to prevent. The prompts would sit beside
neighbours that serve a different reader, and the router would keep returning
the neighbours.

## Decision

1. **Add four domains**, each defined by the object of its prompts:
   - `domain-sales-customer/`: a deal, pipeline, customer account, or support queue.
   - `domain-data-analytics/`: a business metric, query, dashboard, or experiment readout.
   - `domain-operations/`: a process, supplier, inventory, quality defect, or
     non-software project.
   - `domain-health-wellness/`: a healthy adult's own training, eating, or sleep.
2. **Wellness is safety-sensitive.** `domain-health-wellness` joins
   `SAFETY_SENSITIVE_ROOTS` in `scripts/pae_registry/governance.py`, so it is
   served `safety_gated` like `domain-healthcare-clinical` and
   `domain-psychology`. Its entry prompt is a red-flag screen that routes to a
   clinician. Its nutrition prompts carry a STRONG-GUARD for disordered eating.
3. **Everything else folds into existing domains.** Job search goes to
   `domain-personal-development/job-search/` (Self scope). Nonprofit and
   small-business work goes to `domain-business-strategy/`. Real estate and trades
   go to a rebuilt `domain-specialized-fields/`. A new domain is warranted only
   when both of these hold:
   - no existing domain owns the prompt's *object*; and
   - at least one wave's worth of distinct prompts is specified and survives a
     duplicate sweep.
4. **The `CLAUDE.md` worked example is revised.** Sales, customer-success and
   support work has a subject home. Marketing *strategy* remains org work in
   `domain-business-strategy/go-to-market/`.
5. **No moves in the first wave.** The five existing `go-to-market/` sales and
   CS prompts stay where they are and are cross-linked from
   `domain-sales-customer/README.md`. Relocating them through
   `meta/REORG_MAP.tsv` is scheduled for coverage Wave 2. A move adds tombstones
   and changes the relationship-count tests, and it deserves its own reviewable
   change.

## Consequences

- The domain count goes from 44 to 48. Registration takes a single line in
  `DOMAIN_DIRS` (`scripts/generate_prompt_index.py`). The registry, the facts
  generator, the naming validator and the structure gate all read `domain-*`
  from that list or from the tree.
- Until Wave 2 lands, sales and CS content exists in two places. That is
  tolerated only because each new README names the old files explicitly.
- The new domains' negative boundaries lean on `domain-agentic-resources/skills/`:
  - `marketing/` owns outbound copy, sequences, collateral, lead scoring and
    cancel flows;
  - `data-engineering/` owns KPI dashboard design and data storytelling.

  Future additions to either domain must sweep those skills first.
- Routing regression cases for the new scopes are deferred to coverage Wave 5.
  They must pass the leakage audit (ADR-0037).

## Amendment, 2026-09-24 — deferred regression cases shipped

The consequence above deferred routing regression cases for the new scopes to
coverage Wave 5. They shipped as `case-121`..`case-146` in
`pae-engine/tests/data/search_routing_regression.v1.json`, labelled
`coverage_wave_judgment`. A re-audit with `pae_eval.leakage` in the coverage
audit pass found no title-token or id-tail containment, a median
query-to-target overlap of 0.24, a maximum Jaccard of 0.33 against
`ROUTING_REFERENCE.md` phrases and 0.14 against any other case, so the ADR-0037
condition holds. The decision itself is unchanged.
