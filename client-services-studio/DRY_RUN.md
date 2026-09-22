# Dry Run — every gate, firing

*Not legal, tax, or accounting advice. All fixtures are fictional.*

A worked run over [`samples/`](samples/), showing each gate passing **and** blocking.
Every transcript below is real output from the shipped scripts against the shipped
fixtures. Reproduce it by running the commands as written from the toolkit root.

---

## Gate 0 — qualify

### Passes

```console
$ python3 skills/scope-ledger/scripts/scope_ledger.py \
      --gate0 samples/lead_pass.json --config config/practice.json
Gate 0 (qualify): PASS
$ echo $?
0
```

Northwind: a named decision-maker, confirmed budget authority, a defined outcome, and
£30,000 over 20 days — an implied £1,500/day against a walk-away of £787.09.

### Blocks

```console
$ python3 skills/scope-ledger/scripts/scope_ledger.py \
      --gate0 samples/lead_blocked.json --config config/practice.json
Gate 0 (qualify): BLOCKED
  FAIL  decision_maker: no named decision-maker
  FAIL  budget_authority: contact does not hold budget authority
  FAIL  outcome_defined: desired outcome is not defined
  FAIL  rate_floor: indicative budget implies a rate below the practice floor
  FAIL  no_written_scope_wanted: pressure to start without a written scope
  WARN  prior_vendors_all_blamed: probe: prior suppliers described as incompetent with no self-implication
$ echo $?
1
```

Five blocking failures and one warning. £6,000 over 20 days is £300/day against a
£787.09 floor. The prior-vendor signal is `probe` tier, so it warns rather than
blocks — the tier system is what stops the gate becoming a rule that gets overridden
the first time the pipeline is thin.

---

## Gate A — priceable scope

### Passes

```console
$ python3 skills/scope-ledger/scripts/scope_ledger.py --gateA samples/engagement_priceable.json
Gate A (priceable scope): PASS
$ echo $?
0
```

Two deliverables with formats and testable acceptance criteria, two assumptions,
three exclusions, and two client inputs each with an owner, a date and a consequence.

### Blocks

```console
$ python3 skills/scope-ledger/scripts/scope_ledger.py --gateA samples/engagement_vague.json
Gate A (priceable scope): BLOCKED
  FAIL  exclusions: exclusions is empty or absent
  FAIL  deliverable[D1]: no acceptance criterion — cannot be judged complete
  FAIL  client_input[access to the platform]: no due date
  FAIL  client_input[access to the platform]: no stated consequence if late
$ echo $?
1
```

`engagement_vague.json` carries a £45,000 fee against "Strategic review of the data
platform" with no acceptance criterion, no exclusions, and an input with no date and
no consequence. This is the scope that becomes an open commitment. The gate refuses
to let a price sit on it.

---

## Scope drift — Stage 7

```console
$ python3 skills/scope-ledger/scripts/scope_ledger.py \
      --drift samples/engagement_priceable.json --delivered samples/delivered_drifted.json
Scope drift: 2 finding(s)
  HIGH   Implementation of the recommendations: delivered work appears on the exclusion list → raise a change order before any further work
  MEDIUM effort: effort 22 exceeds agreed 16 by more than 15% → review scope before continuing
$ echo $?
1
```

Six days of implementation work were delivered against an engagement that explicitly
excluded implementation. High severity, because it was named as out. The effort
finding is separate: 22 days against an agreed 16.

---

## Gate B — signature risk

### Passes

```console
$ python3 skills/proposal-assembler/scripts/assemble.py --gateB samples/engagement_priceable.json
Gate B (signature risk cleared): PASS
$ echo $?
0
```

Capped liability, capped IP indemnity, assignment limited to deliverables, net-30,
compensated convenience termination, no unilateral variation, a suspension right,
set-off limited to admitted sums, priced and capped transition assistance, an
undisputed-portion clause — and a recorded counsel review.

### Blocks

```console
$ python3 skills/proposal-assembler/scripts/assemble.py --gateB samples/engagement_contract_blocked.json
Gate B (signature risk cleared): BLOCKED
  CRITICAL  unlimited_liability: no limitation of liability, or an unlimited cap
  CRITICAL  uncapped_ip_indemnity: IP indemnity is uncapped
  HIGH      unbounded_ip_assignment: assignment extends beyond engagement deliverables to all work product
  HIGH      payment_terms_long: payment terms beyond 60 days
  HIGH      no_termination_compensation: client may terminate for convenience with no compensation
  CRITICAL  unilateral_scope_change: client may vary scope unilaterally
  MEDIUM    no_suspension_right: no right to suspend work for non-payment
  HIGH      unilateral_set_off: client may set off sums it alone determines are owed
  MEDIUM    unpriced_transition_assistance: transition assistance obligation with no rate and no cap
  MEDIUM    no_undisputed_portion_clause: a small dispute can hold an entire invoice
  HIGH      counsel_review: no record of review by a lawyer before signature
$ echo $?
1
```

All eleven findings on a £24,000 retainer. Note the three medium findings are
reported rather than suppressed: unpriced transition assistance is frequently the
largest number in a long engagement and nobody resists capping it.

### Acceptance requires a rationale

A blocking flag can be carried deliberately, but only on the record:

```json
"accepted_risks": [
  { "flag": "payment_terms_long", "rationale": "offset by a 40% deposit" }
]
```

An entry **without** a `rationale` does not unblock — asserted in
`tests/test_gates.py::GateBSignatureRisk::test_acceptance_requires_a_recorded_rationale`.

---

## Gate C — close-out

### Passes

```console
$ python3 skills/engagement-economics/scripts/economics.py --gateC samples/closeout_complete.json
Gate C (close-out complete): PASS
$ echo $?
0
```

### Blocks

```console
$ python3 skills/engagement-economics/scripts/economics.py --gateC samples/closeout_open.json
Gate C (close-out complete): BLOCKED
  FAIL  final_invoice: 6000 still outstanding and not written off — the engagement is not closed
  FAIL  unbilled_effort: unbilled effort not recorded — margin cannot be computed
  FAIL  estimate: original estimate not recorded — estimate error cannot be updated
  FAIL  case_study_consent: case-study consent not recorded (grant, decline, or not-asked)
  FAIL  client_verdict: no repeat/decline verdict — disqualifier list cannot be updated
$ echo $?
1
```

An engagement with money outstanding is not closed; it is in collections.

---

## The economics

```console
$ python3 skills/engagement-economics/scripts/economics.py --floor config/practice.json
{
  "total_cost": 112000.0,
  "present_days": 220,
  "billable_days": 132.0,
  "breakeven_day_rate": 848.48,
  "walk_away_day_rate": 787.09,
  "floor_day_rate": 983.86,
  "standard_day_rate": 1131.44,
  "floor_hourly_rate": 122.98,
  "sensitivity": {
    "0.5": 1180.64,
    "0.6": 983.86,
    "0.7": 843.31,
    "0.8": 737.9
  }
}
```

The sensitivity table is the point. The same practice needs £737.90/day at 80%
billable and £1,180.64 at 50% — a 60% swing from an assumption, not from a cost.
That is why `billable_fraction` must be measured.

```console
$ python3 skills/engagement-economics/scripts/economics.py \
      --postcalc samples/closeout_complete.json --config config/practice.json
{
  "collected_revenue": 29000,
  "direct_costs": 4000,
  "net_revenue": 25000,
  "total_effort_days": 22,
  "realised_day_rate": 1136.36,
  "estimate_ratio": 1.375,
  "against_floor": "at or above standard",
  "thresholds": { "walk_away": 787.09, "floor": 983.86, "standard": 1131.44 }
}
```

£30,000 invoiced, £1,000 written off, £4,000 of subcontractor cost, 18 billed days
**plus 4 unbilled** — 22 total. Dropping the unbilled days would report £1,388.89/day
instead of £1,136.36, which is the rate you wished you had earned. The engagement ran
37.5% over estimate, and that ratio goes into the series.

---

## The escalation ladder refuses

```console
$ python3 skills/receivables-tracker/scripts/receivables.py --rung samples/invoice_disputed.json
{
  "action": "refuse",
  "reason": "cause is dispute — resolve the substance before escalating; escalation hardens the position and stalls the undisputed portion"
}
```

52 days overdue, rungs 1 and 2 already fired, a contractual suspension right and
ongoing work — every condition for escalation present except one. The cause is
dispute, so the ladder refuses. Escalating here would harden the position and stall
the undisputed portion of the invoice.

---

## The suite

```console
$ for s in skills/*/scripts/*.py; do python3 "$s" --self-check; done
economics.py self-check: PASS
assemble.py self-check: PASS
receivables.py self-check: PASS
scope_ledger.py self-check: PASS

$ python3 -m unittest discover -s tests
....................................
----------------------------------------------------------------------
Ran 37 tests in 0.005s

OK
```

The suite loads each skill script from its path, so it exercises the same code the
pipeline runs. There is no test-only implementation of any gate.
