---
name: statement-reconciliation-verifier
description: Verifies that an extracted statement is complete and correct before any downstream use — proving every transaction transferred with the right amount. Use this skill after extracting a statement, when you need to "verify the extraction", "reconcile the statement", "check the balance", "make sure no transactions were missed", or as a hard gate before categorizing or flagging. Runs balance arithmetic, running-balance, structure, anomaly, and coverage checks; exits non-zero on any hard failure.
license: MIT
compatibility: Python 3.8+, standard library only (no third-party dependencies).
metadata:
  tags: [finance, verification, reconciliation, bank-statement, quality-gate, audit]
  updated: "2026-06-09"
---

# Statement Reconciliation Verifier

The hard gate of the pipeline. It proves, with evidence, that every transaction
on a statement made it into the CSV with the correct amount — so you never
categorize, flag, or hand an attorney data that silently dropped a row.

## Purpose

Extraction can drop, duplicate, or misread rows. Before anyone relies on the
data, this skill answers one question with checks, not vibes: *did everything
transfer correctly?* If not, it fails loudly and names what is wrong.

## When to Use This Skill

Use this skill when you need to:
- Confirm an extracted transactions CSV matches the source statement
- Reconcile opening + transactions = closing balance
- Prove no transaction-like line in the statement was missed (coverage)
- Gate categorization/flagging on a clean extraction

## When NOT to Use This Skill

Do NOT use this skill when:
- You have not extracted the statement yet → use `pdf-statement-extractor`
- You want to assign categories → use `transaction-categorizer`
- The CSV did not come from this pipeline (the schema/raw-text siblings may be missing)

## Prerequisites

- Python 3.8+ (standard library only)
- The extractor's outputs alongside the CSV: `<stem>_meta.json` (for balances)
  and `<stem>_raw.txt` (for the coverage check). Both are produced automatically
  by `extract_statement.py`.

## Quick Start

### Step 1: Verify a statement

```bash
python scripts/reconcile_statement.py output/statement_transactions.csv
# Loosen tolerance for OCR'd statements; show every warning:
python scripts/reconcile_statement.py output/statement_transactions.csv --tolerance 0.05 -v
```

**Expected output (success):**
```
=== RECONCILIATION: statement_transactions.csv ===
  Layer 1 balance:     PASS
  Layer 2 consistency: PASS
  Layer 3 structure:   PASS
  Layer 4 anomaly:     INFO
  Coverage check:      PASS
  RESULT: VERIFIED
```

**Expected output (failure — fails loudly):**
```
  Layer 1 balance:     FAIL
  Coverage check:      FAIL
  RESULT: DISCREPANCY
  ERROR: Balance mismatch: opening 5234.50 + sum -4130.20 = 1104.30, but statement closing is 1904.30 (off by -800.00).
  ERROR: Coverage gap: 1 transaction-like line(s) in the statement did not map to an extracted row.
```

**If this fails:**
1. **Balance mismatch** → a row was dropped, duplicated, or misread. Open `<stem>_reconciliation.json`, compare totals, fix extraction (or add an institution rule), re-extract, re-verify.
2. **Coverage gap** → the report lists the exact unmatched raw lines (with line numbers). Those transactions are missing from the CSV.
3. **Layer 1 SKIPPED** → opening/closing balance wasn't detected in the statement text; rely on the coverage check and add balance patterns if possible.

**Validation:**
- [ ] `RESULT: VERIFIED`
- [ ] Exit code is `0` (`echo $?`)
- [ ] No entries under `unmatched_raw_lines` in the JSON report

### Step 2: Use the exit code as a gate

```bash
if python scripts/reconcile_statement.py output/stmt_transactions.csv; then
  echo "verified — safe to categorize"
else
  echo "DISCREPANCY — stop and fix extraction"
fi
```

## Common Issues

### Issue: Balance check is SKIPPED
The statement's opening/closing balance wasn't found in the text. The coverage
check still guards completeness. Add balance-line patterns to extraction if you
need the arithmetic check.

### Issue: Coverage FAIL on a line that isn't a transaction
The coverage check requires a date plus a cents amount and skips balance lines.
If a summary line still trips it, it is usually a sign the extractor should skip
that line too — add it to `skip_patterns` in `institutions.yaml`.

### Issue: Anomaly layer flags a huge but legitimate transaction
Layer 4 is INFO only and never fails the run. It exists to draw a human's eye,
not to block.

## Deep Dive References

- **What each layer checks and why:** `references/reconciliation_methods.md`

## Safety & Constraints

**NEVER:**
- Treat `DISCREPANCY` as acceptable and continue the pipeline
- Widen `--tolerance` beyond a cent or two to "make it pass" — investigate instead

**ALWAYS:**
- Require `RESULT: VERIFIED` before categorizing/flagging
- Keep the JSON report (`<stem>_reconciliation.json`) — it is your audit trail
- Re-verify after any re-extraction

## Reference Files

| Resource | Purpose |
|----------|---------|
| `scripts/reconcile_statement.py` | 4-layer + coverage verification; writes JSON report; exit 0/1 |
| `references/reconciliation_methods.md` | Detailed explanation of each verification layer |

## Related Skills

- `pdf-statement-extractor` — produces the CSV/meta/raw inputs this skill checks
- `transaction-categorizer` — run only after `RESULT: VERIFIED`
