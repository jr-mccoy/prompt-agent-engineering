# Stage 0 — Practice Configuration

**Gate: none.** This stage produces the configuration every later gate reads.

**Output:** `config/practice.json`

---

## Purpose

Every gate in this pipeline tests an engagement against *your* practice, not against
a generic standard. Gate 0 needs your disqualifiers and your rate floor; Gate A needs
nothing from you but will not run without a decision-maker; Gate C needs your
close-out standard. This stage produces that configuration once, and revisits it
annually or when cost structure changes.

Run this before anything else. A pipeline configured with someone else's numbers
produces confident, wrong answers.

## Inputs

Work through these four prompts in order. Each produces a section of the config.

| Section | Prompt |
|---|---|
| The offer and its boundary | `domain-business-strategy/client-services/services_offer_definition_and_boundary.md` |
| Disqualifiers | `domain-business-strategy/client-services/services_ideal_client_and_disqualifiers.md` |
| Capacity and utilization | `domain-business-strategy/client-services/services_capacity_and_utilization_planner.md` |
| Rate floor | `domain-finance/corporate-finance-fpa/finance_services_rate_floor_model.md` |

Vendored copies are under `referenced-prompts/`.

## Procedure

### 1. Define the offer

Run the offer-definition prompt. You need the deliverable list, the exclusion list
and the entry conditions before you can qualify anything, because Gate 0's
disqualifiers are derived from the entry conditions.

### 2. Derive the disqualifiers

Run the ideal-client prompt. Each disqualifier enters the config as:

```json
{ "id": "snake_case_id", "tier": "decline | probe | proceed_with_protection",
  "reason": "the signal, as observed at first contact" }
```

Only `decline`-tier signals block Gate 0. Everything else warns, which is the point:
a gate that only declines gets overridden the first time the pipeline is thin.

### 3. Compute capacity

Run the capacity planner. It produces `working_days`, `absence_days` and — the
number that matters most — `billable_fraction`. Measure it. If you cannot, use 0.60
and record that it is assumed.

### 4. Compute the rate floor

Run the rate-floor model. It consumes the capacity numbers and produces the three
thresholds. `walk_away_day_rate` enters the config; Gate 0 uses it to reject a lead
whose stated budget implies a sub-floor rate.

### 5. Write and verify the config

Write `config/practice.json` following the shape in
`config/practice.json` as shipped (a worked example, not a recommendation), then
verify the arithmetic:

```bash
python3 skills/engagement-economics/scripts/economics.py --floor config/practice.json
```

Check that `walk_away_day_rate` in the config matches the computed
`walk_away_day_rate`. They are stored separately so Gate 0 can run without
recomputing, and they drift if you do not check.

## Output contract

`config/practice.json` must carry:

- `costs`: `fixed_business`, `target_income`, `employment_burden_rate`,
  `pension_and_healthcare`
- `capacity`: `working_days`, `absence_days`, `billable_fraction`,
  `billable_hours_per_day`
- `risk`: `bad_debt_rate`, `typical_overrun`
- `target_margin`, `positioning_premium`
- `walk_away_day_rate` — must equal the computed value
- `concentration_limit_pct`
- `disqualifiers` — at least three, at least one `decline` tier, each drawn from a
  real past engagement rather than from theory

## Verification

- [ ] `economics.py --floor` runs and its `walk_away_day_rate` matches the config
- [ ] `billable_fraction` is measured, or marked assumed at 0.60
- [ ] At least one disqualifier is `decline` tier
- [ ] Every disqualifier is observable at or before the first call
- [ ] The disqualifier list would not have turned away your three best engagements
- [ ] The disqualifier list would have caught your three worst at first contact

## Boundaries

Not tax or accounting advice. The employment-burden rate and the treatment of
self-funded pension and healthcare are jurisdiction-specific — see
`domain-finance/tax-planning/solo_dev_tax_strategy.md` and speak to an accountant.
