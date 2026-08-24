# Pattern Record Schema & Lifecycle

*For informational and research purposes only. Not financial, investment, or tax advice.*

Every pattern lives in `knowledge-base/patterns/PATTERN-<id>.md` as YAML frontmatter
plus a notes body. The template is `knowledge-base/patterns/PATTERN-TEMPLATE.md`.

## Fields

| Field | Type | Meaning / rule |
|---|---|---|
| `id` | string | `PATTERN-<zero-padded int>`, unique and stable. |
| `title` | string | One line: asset class + signal + outcome window. Specific and falsifiable. |
| `status` | enum | `hypothesis` \| `validated` \| `retired` (see lifecycle below). |
| `asset_classes` | list | `equity-microcap` \| `equity` \| `crypto` \| `options`. |
| `hypothesis` | string | Precise claim: `<signal>` predicts `<outcome>` over `<horizon>` in `<population>`. |
| `registered_on` | date | Date the hypothesis was committed — MUST predate outcome inspection. |
| `feature_definition` | string | Reproducible computation of the signal; no ambiguity. |
| `sample_frame` | string | Universe + date range the sample is drawn from. `validate_pattern.py` reads this for a non-blocking advisory when it lacks point-in-time / survivorship language. |
| `base_rate` | string/number | Outcome frequency in the sample frame **absent** the signal. |
| `in_sample_result` | map | `{ n, lift_vs_base_rate }` on the derivation sample. |
| `out_of_sample_result` | map | `{ n, lift_vs_base_rate }` on a disjoint holdout. **Required for `validated`.** |
| `multiple_comparisons_note` | string | How many features were screened to find this one. `validate_pattern.py` reads this for a non-blocking advisory when the count is high. |
| `decay_estimate` | string | Expected edge half-life / regime sensitivity. |
| `capacity_note` | string | Does the edge survive realistic size, liquidity, costs? |
| `confidence` | enum | `low` \| `medium` \| `high`. |
| `last_reviewed` | date | Last time the record was re-checked for decay. |
| `linked_predictions` | list | `PRED-*` ids that tested this pattern (filled by the journal). |

## Lifecycle

```
   register (status: hypothesis)
        │   in-sample lift only → stays hypothesis (cannot drive sizing)
        ▼
   out-of-sample test on disjoint holdout
        │   n ≥ configured minimum AND lift_vs_base_rate > 0  ── Gate A ──▶ status: validated
        │   otherwise                                                       stays hypothesis
        ▼
   periodic re-review (last_reviewed)
        │   edge decays below base rate, re-test fails, or capacity/cost kills it
        ▼
   status: retired  (keep the record; add a dated reason in the notes body)
```

- **hypothesis** — registered and falsifiable; may carry in-sample lift. Visible to the
  screener only as an *unscored* "paper-only signal." Never contributes to position sizing.
- **validated** — passed Gate A. May contribute to screener scores (Stage 4).
- **retired** — no longer usable; retained for the audit trail with a dated reason.

## Invariants

1. `registered_on` ≤ the date outcomes were first inspected.
2. `status: validated` ⇒ `out_of_sample_result.n` ≥ configured minimum AND `lift_vs_base_rate > 0`.
3. `knowledge-base/INDEX.md` row matches the record's `status`, `confidence`, `last_reviewed` (auditable via `validate_pattern.py --reconcile`, which catches INDEX↔record drift).
4. Blank is allowed; invented values are not. Unknown fields are queued for work, not guessed.

> **Note:** the advisory checks (high `multiple_comparisons_note` count; `sample_frame` missing
> point-in-time/survivorship language) are non-blocking — they print `! advisory:` and never
> change PASS/FAIL. A PASS means "eligible," not "audited clean."
