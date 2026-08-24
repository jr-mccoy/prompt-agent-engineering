# Verification Methods

`reconcile_statement.py` runs four layers plus a coverage check. **Hard** checks
fail the run (non-zero exit); **soft** checks only warn.

## Layer 1 — Balance arithmetic (HARD, when balances are available)

The "Golden Rule":

```
opening_balance + sum(signed amounts) == closing_balance   (within --tolerance, default $0.01)
```

If opening/closing balances were detected in the statement metadata and this
fails, a row was dropped, duplicated, or misread. The report shows the computed
closing and the exact dollar difference. If balances were not detected, this
layer is SKIPPED and completeness rests on the coverage check.

## Layer 2 — Transaction consistency (SOFT)

- **Running-balance continuity:** where consecutive rows have running balances,
  `running[i]` must equal `running[i-1] + amount[i]`. Mismatches pinpoint the
  exact row where extraction diverged.
- **Numeric amounts:** every amount must parse as a number.
- **Duplicate detection:** an MD5 of `date|description_clean|amount` catches rows
  extracted twice (a common multi-page artifact).

These are warnings because some statements legitimately group transactions by
type rather than strict date/balance order.

## Layer 3 — Document structure (SOFT)

- **Page continuity:** parses "Page X of Y" markers and reports missing pages.
- **Header presence:** notes if the account number or statement period was not
  detected (often a sign of a truncated or mis-scanned document).

## Layer 4 — Statistical anomaly (INFO only, never fails)

- Amounts greater than mean + 3σ (possible OCR digit error, or a genuinely large
  transaction worth a human's attention).
- Days with more than 10× the median transaction count (possible scanning
  duplication).

## Coverage check — the "every transaction" guarantee (HARD)

This is the strongest completeness check and the reason you can trust the output.
It re-reads the raw statement text and, for every line that *looks like a
transaction* (has a date AND a cents amount, and is not a balance line), confirms
that line maps to exactly one row in the CSV — matching on `(date, amount)`.

Any raw transaction line with no corresponding CSV row is reported by line number
under `unmatched_raw_lines`, and the run fails. This catches silent drops that a
balance check alone could miss (e.g., two offsetting errors).

## Reading the JSON report

`<stem>_reconciliation.json` records every layer's status, the totals
(count, credits, debits, sum), all errors and warnings, and the final
`result` (`VERIFIED` or `DISCREPANCY`). Keep it as your audit trail — it is the
evidence that the spreadsheet faithfully represents the statement.

## Exit codes

| Code | Meaning |
|------|---------|
| 0 | VERIFIED — all hard checks passed |
| 1 | DISCREPANCY — a hard check failed (balance or coverage) |
| 2 | Bad input / arguments |
