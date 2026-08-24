---
name: pdf-statement-extractor
description: Extracts transactions from bank and credit-card statement PDFs (or text/CSV exports) into a normalized transactions CSV and a polished Excel workbook. Use this skill when converting statements to a spreadsheet, "extract my bank statements", "turn these PDFs into Excel", "parse a credit card statement", "statement to CSV", or preparing financial records for review. Bundles deterministic Python parsers; routes scanned PDFs through OCR.
license: MIT
compatibility: Python 3.8+. PDF input requires pdfplumber; Excel output requires openpyxl; scanned PDFs require ocrmypdf. Text/CSV input and CSV output need only the standard library.
metadata:
  tags: [finance, pdf, bank-statement, extraction, excel, csv, openpyxl, pdfplumber]
  updated: "2026-06-09"
---

# PDF Statement Extractor

Converts a single bank or credit-card statement into a normalized transactions
CSV (the canonical, machine-readable source of truth) and a formatted Excel
workbook for review.

## Purpose

Statements arrive as PDFs that are useless for analysis. This skill turns each
statement into clean, structured rows using deterministic parsing — no guessing,
no silent data loss — so every downstream stage (verification, categorization,
flagging) works from reliable data.

## When to Use This Skill

Use this skill when you need to:
- Convert one or more statement PDFs into Excel/CSV
- Normalize transactions to a single schema across different banks
- Produce a workbook with Transactions, Summary, and Reconciliation tabs
- Prepare financial records for organizing, bookkeeping, or attorney review

## When NOT to Use This Skill

Do NOT use this skill when:
- You only need to *verify* an already-extracted CSV → use `statement-reconciliation-verifier`
- You need to *categorize* transactions → use `transaction-categorizer`
- You need to *flag* transactions for a legal matter → use `divorce-financial-flagger`
- The document is not a financial statement (use a generic PDF/markdown tool)

## Prerequisites

- Python 3.8+
- `pip install pdfplumber openpyxl` (PDF input + Excel output)
- For scanned/image PDFs: `ocrmypdf` (`apt-get install ocrmypdf` or `pip install ocrmypdf`)
- Text (`.txt`) and CSV (`.csv`) exports work with the standard library alone.

## Quick Start

### Step 1: Extract transactions from one statement

**Purpose:** Produce `<stem>_transactions.csv`, `<stem>_raw.txt`, and `<stem>_meta.json`.

**Skip if:** You already have a verified transactions CSV for this statement.

```bash
python scripts/extract_statement.py path/to/statement.pdf --out output/
# Credit-card statement:
python scripts/extract_statement.py amex_apr.pdf --account-type credit --out output/
# Scanned (image) PDF:
python scripts/extract_statement.py scanned.pdf --ocr --out output/
```

**Expected output:**
```
[extract] OK: 47 transactions -> output/statement_transactions.csv
[extract] opening=5234.50 closing=8901.23 period='01/01/2024 - 01/31/2024' account='****6789'
```

**If this fails:**
1. `0 transactions parsed` → the layout is non-standard. Add a pattern in `institutions.yaml` (see `references/statement_formats.md`) and retry.
2. `no extractable text` → it is a scanned PDF; re-run with `--ocr`.
3. `pdfplumber required` → `pip install pdfplumber`, or export the statement to CSV/OFX and pass that.

**Validation:**
- [ ] Transaction count looks right for the statement
- [ ] `opening` and `closing` balances were detected (printed above)
- [ ] Spot-check 2–3 rows in the CSV against the PDF

### Step 2: Verify before doing anything else (hard gate)

**Purpose:** Confirm every transaction transferred correctly. **Never categorize or flag an unverified statement.**

```bash
python ../statement-reconciliation-verifier/scripts/reconcile_statement.py output/statement_transactions.csv
```

Proceed only when `RESULT: VERIFIED`. See the `statement-reconciliation-verifier` skill.

### Step 3: Build the Excel workbook

**Purpose:** Produce a formatted `.xlsx` with Transactions / Summary / Reconciliation (and Flags, once flagged) tabs.

```bash
# One statement:
python scripts/build_workbook.py output/statement_transactions.csv --out output/statement.xlsx
# All statements in a folder, into one master workbook:
python scripts/build_workbook.py --inputs output/ --out output/master_workbook.xlsx
```

**Validation:**
- [ ] Workbook opens; tabs present
- [ ] Reconciliation tab shows VERIFIED for each statement
- [ ] If `openpyxl` is missing, a combined CSV is written instead (install openpyxl for the formatted workbook)

## Common Issues

### Issue: Amounts are correct but descriptions contain stray numbers
The parser keys on cents-bearing amounts (`.dd`). Store numbers like `#123` are kept in the description; that is expected and harmless. If a bank embeds dates mid-description, add an institution pattern.

### Issue: Debits/credits have the wrong sign
The parser derives signs from the running-balance column when present. If your statement has no running balance, pass `--account-type credit` for card statements (purchases are outflows) and spot-check signs.

### Issue: Multi-page statement drops a page
pdfplumber processes pages sequentially. If a page is missing, the verifier's Layer 3 reports a "Page X of Y" gap. Re-export the PDF or split and re-run.

## Deep Dive References

- **Adding bank-specific parse rules:** `references/statement_formats.md`
- **The canonical transaction schema:** `references/transaction_schema.md`

## Safety & Constraints

**NEVER:**
- Categorize or flag a statement that has not passed verification
- Edit the raw PDF; treat it as read-only evidence
- Commit raw statements or extracted PII to a shared/public repository

**ALWAYS:**
- Run `reconcile_statement.py` immediately after extraction
- Keep the original PDFs alongside outputs for spot-checking
- Spot-check a few rows per statement against the source

## Reference Files

| Resource | Purpose |
|----------|---------|
| `scripts/extract_statement.py` | PDF/text/CSV → normalized transactions CSV + raw text + meta |
| `scripts/build_workbook.py` | Transaction CSV(s) → formatted Excel workbook |
| `references/statement_formats.md` | How to add per-institution parsing patterns |
| `references/transaction_schema.md` | Canonical column schema shared across the pipeline |

## Related Skills

- `statement-reconciliation-verifier` — verify every transaction transferred (run next)
- `transaction-categorizer` — assign Plaid categories + research unknown merchants
- `divorce-financial-flagger` — flag transactions for attorney review
