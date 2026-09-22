# Record schemas

Three JSON records. All fields are optional unless a gate requires them; the gates
are the specification.

## Lead record — input to Gate 0

```json
{
  "client": "Northwind",
  "decision_maker": "A. Patel",
  "budget_authority": true,
  "outcome_defined": true,
  "indicative_budget": 30000,
  "indicative_days": 20,
  "client_current_revenue_pct": 0,
  "client_added_revenue_pct": 12,
  "disqualifiers_observed": ["prior_vendors_all_blamed"]
}
```

| Field | Gate 0 effect |
|---|---|
| `decision_maker` | Must be non-empty |
| `budget_authority` | Must be exactly `true` |
| `outcome_defined` | Must be exactly `true` |
| `indicative_budget` / `indicative_days` | If **both** present, `budget / days` must be ≥ `walk_away_day_rate`. Unknown budget is a discovery question, not a failure |
| `client_current_revenue_pct` + `client_added_revenue_pct` | Must not exceed `concentration_limit_pct` |
| `disqualifiers_observed` | Each id is looked up in the practice config. `decline` tier blocks; anything else warns. An unknown id warns |

## Engagement record — input to Gate A, render, Gate B, drift

```json
{
  "name": "Pipeline assessment",
  "client": "Northwind",
  "problem_statement": "Deploy failures are rising and nobody can say why.",
  "lead": { "decision_maker": "A. Patel" },
  "scope": {
    "deliverables": [
      {
        "id": "D1",
        "name": "Pipeline assessment",
        "format": "written report",
        "acceptance": "covers the seven named pipelines against the six criteria",
        "estimated_days": 10
      }
    ],
    "assumptions": ["read access granted in week 1"],
    "exclusions": ["implementation of the recommendations"],
    "client_inputs": [
      {
        "input": "read access to the CI system",
        "owner": "A. Patel",
        "due": "2026-10-01",
        "if_late": "the clock continues; the end date moves day for day"
      }
    ]
  },
  "commercial": {
    "structure": "fixed",
    "fee": 30000,
    "payment_schedule": [
      { "label": "Deposit", "amount": 12000, "trigger": "signature",
        "issue_date": "2026-10-01" }
    ]
  },
  "payment_machinery": {
    "terms_days": 30,
    "approval_window_days": 5,
    "payment_run_day_of_month": 25,
    "cutoff_days_before_run": 10,
    "po_required": true,
    "po_number": "PO-4471"
  },
  "contract": {
    "liability_cap": 250000,
    "ip_indemnity_capped": true,
    "ip_assignment_scope": "deliverables",
    "payment_terms_days": 30,
    "termination_for_convenience": true,
    "termination_compensation": "work performed plus committed costs",
    "unilateral_scope_change": false,
    "suspension_right": true,
    "set_off": "admitted_only",
    "transition_assistance": "at standard rates, capped at 10 days",
    "undisputed_portion_payable": true,
    "counsel_reviewed": true,
    "accepted_risks": [
      { "flag": "payment_terms_long", "rationale": "offset by a 40% deposit" }
    ]
  }
}
```

Gate A requires: `scope.deliverables`, `scope.assumptions`, `scope.exclusions` and
`scope.client_inputs` all non-empty; every deliverable to have `name`, `format` and
`acceptance`; every client input to have `owner`, `due` and `if_late`; and
`lead.decision_maker` to be present.

`contract` is a **summary a human produced by reading the contract**. The scan does
not parse contracts.

## Delivered record — input to drift

```json
{
  "items": [
    { "id": "D1", "name": "Pipeline assessment", "days": 12 },
    { "id": "X1", "name": "Implementation of the recommendations", "days": 6 }
  ]
}
```

An item whose `id` is not an agreed deliverable is a change-order trigger. If its
`name` matches an entry on the exclusion list (case-insensitive) the finding is
high severity. Total effort exceeding agreed estimated effort by more than 15%
raises a separate finding.
