# AGENTS.md — Financial Records Toolkit (Codex / agent entry point)

You are processing personal bank and credit-card statements into verified,
categorized, and flagged spreadsheets for the user's attorney. Work in **stages**
and **enforce the verification gate**. You organize facts — you do **not** give
legal advice or assert anyone's intent.

## Ground rules

1. **Verification is a hard gate.** A statement that fails verification is NOT
   categorized or flagged. Report it for the user to fix; never widen tolerances
   to force a pass.
2. **Never fabricate.** If a merchant can't be identified, leave it `UNKNOWN`.
   Never invent transactions, amounts, categories, or merchant identities.
3. **Facts only.** Flags are "look at this for review," not conclusions. Never
   characterize the other party.
4. **Privacy.** Treat everything as sensitive PII. Keep raw PDFs and outputs out
   of git (the repo's `.gitignore` already does this). Only optional merchant
   research touches the network, and it searches a merchant *name* only.

## Layout

- Statements in: `data/input_pdfs/`   →   results in: `data/output/`
- Scripts live inside each skill: `skills/<skill>/scripts/<script>.py`
- Tunable rules: `config/category_rules.yaml`, `config/flag_rules.yaml`, `config/institutions.yaml`

## Setup

```bash
pip install -r requirements.txt   # pdfplumber, openpyxl, pyyaml (rapidfuzz/ocrmypdf optional)
```

## Stage 1 — Extract + Verify (per statement)

For each file in `data/input_pdfs/`:

```bash
# Extract (add --ocr for scanned PDFs; --account-type credit for card statements)
python skills/pdf-statement-extractor/scripts/extract_statement.py \
    "data/input_pdfs/STATEMENT.pdf" --out data/output/

# Verify — REQUIRED before anything else. Exit code 0 = VERIFIED, 1 = DISCREPANCY.
python skills/statement-reconciliation-verifier/scripts/reconcile_statement.py \
    data/output/STATEMENT_transactions.csv
```

If the verifier prints `RESULT: DISCREPANCY` (or exits non-zero): record the
errors from `data/output/STATEMENT_reconciliation.json`, set this statement aside,
and continue with the others. Do not advance it.

See `skills/pdf-statement-extractor/references/statement_formats.md` if extraction
returns 0 transactions (add an `institutions.yaml` rule).

## Stage 2 — Categorize + research unknown merchants

```bash
python skills/transaction-categorizer/scripts/categorize_transactions.py \
    data/output/STATEMENT_transactions.csv --rules config/category_rules.yaml
```

This writes a `STATEMENT_research_queue.csv` of merchants it couldn't identify.
For each unknown: normalize the descriptor, web-search the merchant, classify to
the Plaid taxonomy (payment apps and brokerages are TRANSFER_IN/OUT, not
spending), and record findings in a `researched.yaml`:

```yaml
- match: "SQ *BLUE BOTTLE"
  category: FOOD_AND_DRINK
  subcategory: COFFEE
  note: "researched: Blue Bottle Coffee (Square seller)"
```

Then teach the rules and re-categorize so it learns permanently:

```bash
python skills/transaction-categorizer/scripts/categorize_transactions.py \
    --merge researched.yaml --rules config/category_rules.yaml
python skills/transaction-categorizer/scripts/categorize_transactions.py \
    data/output/STATEMENT_transactions.csv --rules config/category_rules.yaml
```

See `skills/transaction-categorizer/references/merchant_research_protocol.md`.

## Stage 3 — Flag for attorney review

First confirm `config/flag_rules.yaml` thresholds suit the user's finances (ask if
unsure). Then:

```bash
python skills/divorce-financial-flagger/scripts/flag_transactions.py \
    data/output/STATEMENT_transactions.csv --rules config/flag_rules.yaml
```

Produces a prioritized `STATEMENT_review_queue.csv` across four dimensions:
asset/property, income, child/custody, cash/undocumented. See
`skills/divorce-financial-flagger/references/divorce_flag_framework.md`.

## Stage 4 — Assemble the workbook

```bash
python skills/pdf-statement-extractor/scripts/build_workbook.py \
    --inputs data/output/ --out data/output/master_workbook.xlsx
```

Tabs: Transactions, Summary, Reconciliation, Flags.

## Final report to the user

- Statements processed, and verification result for each (flag any DISCREPANCY).
- Categorization coverage; merchants left honestly UNKNOWN.
- Flag counts by dimension; HIGH-priority items.
- Where the workbook and review queues are, and the reminder that flags are for
  the attorney's review — not legal conclusions.
