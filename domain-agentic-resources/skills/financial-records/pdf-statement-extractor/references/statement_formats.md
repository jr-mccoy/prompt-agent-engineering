# Adding Per-Institution Parsing Rules

The generic parser handles the common transaction line shape:

```
<date>   <description>   <amount>   [<running balance>]
```

It recognizes dates as `MM/DD/YYYY`, `MM/DD/YY`, `YYYY-MM-DD`, `Mon DD`, or
`MM/DD`, and reads cents-bearing amounts (`1,234.56`, `$1,234.56`, `(1,234.56)`,
`-1,234.56`, `1,234.56-`, `1,234.56 CR/DR`). When two amounts trail a line it
treats them as `(amount, running_balance)`; a single trailing amount is the
amount with no running balance.

## When the generic parser is enough

Most US checking, savings, and credit-card statements that have a real text
layer parse correctly. Always confirm with the verifier — if balance + coverage
both PASS, the parse is trustworthy.

## When you need a custom rule

If `extract_statement.py` reports `0 transactions parsed`, or the verifier's
coverage check lists unmatched lines, the layout needs a hint. Create an
`institutions.yaml` and pass it with `--config institutions.yaml --institution KEY`.

Suggested structure (extend the parser's `read_*`/`parse_transactions` hooks as needed):

```yaml
chase_checking:
  date_formats: ["%m/%d/%Y"]
  # A regex with named groups date/desc/amount/balance, applied per line:
  line_regex: '^(?P<date>\d{2}/\d{2}/\d{4})\s+(?P<desc>.+?)\s+(?P<amount>[-(]?\$?[\d,]+\.\d{2}\)?)\s+(?P<balance>[\d,]+\.\d{2})$'
  # Lines to ignore entirely:
  skip_patterns: ["DAILY BALANCE", "TOTALS", "INTEREST RATE"]

amex_card:
  date_formats: ["%m/%d/%y"]
  # Credit cards often have no running balance and use a separate sign column:
  account_type: credit
```

## Common layout gotchas

| Symptom | Cause | Fix |
|---------|-------|-----|
| 0 transactions | No text layer (scanned) | Re-run with `--ocr` |
| Wrong amount picked | Two amounts but no running balance | The parser assumes the last 2 numbers are amount+balance; for amount-only layouts, add a `line_regex` with a single `amount` group |
| Description truncated | Amount-like token inside description (`#1234.00`) | Rare with cents-required matching; if it happens, add a `skip_patterns` or tighten `line_regex` |
| Multi-line transactions | Description wraps to a second line | Add a join rule in `institutions.yaml` (continuation lines have no leading date) |
| Foreign currency | Mixed currencies in one statement | Split by currency before extracting; verify each group separately |

## Scanned statements (OCR)

`--ocr` runs `ocrmypdf --skip-text` to add a text layer, then parses normally.
OCR accuracy varies; **always verify**, and spot-check large amounts where a
misread digit changes the balance. For poor scans, consider re-scanning at
higher DPI or requesting a digital copy from the bank.
