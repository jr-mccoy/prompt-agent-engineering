# Canonical Transaction Schema

Every stage of the pipeline reads and writes this exact column order. Do not
rename or reorder columns — the verifier, categorizer, and flagger all depend on
these names.

| Column | Meaning | Set by |
|--------|---------|--------|
| `source_file` | Original statement filename | extractor |
| `statement_period` | Statement period string, if detected | extractor |
| `account_id` | Masked account number, if detected | extractor |
| `date` | Transaction date as printed on the statement | extractor |
| `description_raw` | Description exactly as parsed | extractor |
| `description_clean` | Uppercased, whitespace-collapsed description (used for matching) | extractor |
| `amount` | Signed amount, 2 decimals. Negative = money out (debit), positive = money in (credit) | extractor |
| `direction` | `debit` or `credit` | extractor |
| `running_balance` | Account balance after this transaction, if printed | extractor |
| `category` | Plaid primary category (e.g. `FOOD_AND_DRINK`) or `UNKNOWN` | categorizer |
| `subcategory` | Plaid detailed subcategory | categorizer |
| `flags` | `;`-joined flag codes like `CASH:LARGE_CASH|HIGH` | flagger |
| `confidence` | 0–1 confidence in the row (extraction × categorization) | extractor / categorizer |
| `needs_review` | `TRUE`/`FALSE` — set when confidence is low or a HIGH-priority flag fires | all stages |
| `notes` | Free-text notes (e.g. researched merchant identity) | any stage / human |

## Sign convention

The amount sign is chosen so that, when a running balance is present:

```
running_balance[i] == running_balance[i-1] + amount[i]
```

This makes verification account-type-agnostic: it works for checking accounts
(deposits +, withdrawals −) and credit cards alike, because the sign always
follows the statement's own balance progression.

## Why `description_clean` is uppercased

Categorization and flagging match against `description_clean`. Uppercasing and
collapsing whitespace makes matching deterministic and case-insensitive while
preserving `description_raw` as the faithful original.
