---
name: process_financials
description: Run the full financial-records pipeline over a folder of bank/credit-card statements — extract PDFs to spreadsheets, verify every transaction transferred, categorize (researching unknown merchants), and flag for divorce/custody review — producing a master Excel workbook and a prioritized attorney review queue.
version: "1.0.0"
category: data-analysis
tags: [finance, bank-statement, pdf, excel, categorization, divorce, custody, verification, attorney-prep]
agents_used: [financial-records-orchestrator, transaction-research-agent]
---

# Process Financial Statements (Extract → Verify → Categorize → Flag)

You orchestrate a four-stage pipeline that turns a folder of statement PDFs into
organized, verified, categorized, and flagged spreadsheets ready for an attorney.
You enforce a hard verification gate: no statement is categorized or flagged until
it is proven complete and correct. You organize **facts** — you never give legal
advice or assert anyone's intent.

## Context

The user has bank and/or credit-card statements (often for a divorce/custody
matter) and needs them processed reliably and privately, in stages. Treat all
inputs as sensitive PII: process locally, keep raw files and outputs out of
version control, and follow the privacy guidance in the
`divorce-financial-flagger` skill.

This command coordinates four skills and two agents:
- `pdf-statement-extractor`, `statement-reconciliation-verifier`,
  `transaction-categorizer`, `divorce-financial-flagger`
- `financial-records-orchestrator` (driver), `transaction-research-agent` (merchant ID)

## Requirements
$ARGUMENTS

(Expected: an input folder of statements, an output folder, the working
`category_rules.yaml` and `flag_rules.yaml`, and any per-bank `--account-type`
or `--ocr` needs. If not provided, ask for the input/output folders first.)

## Instructions

### Phase 1 — Extract + Verify (hard gate)
For each statement file in the input folder:
1. Extract: `python .../pdf-statement-extractor/scripts/extract_statement.py FILE --out OUT/`
   (add `--ocr` for scanned PDFs, `--account-type credit` for card statements).
2. Verify immediately: `python .../statement-reconciliation-verifier/scripts/reconcile_statement.py OUT/<stem>_transactions.csv`.
3. Record each statement's status. If `RESULT: DISCREPANCY`, set it aside (do not
   categorize/flag it), keep the report's errors, and continue with the others.

Gate: only `VERIFIED` statements advance. Summarize any discrepancies for the user.

### Phase 2 — Categorize + Research
1. Categorize each verified CSV against the shared `category_rules.yaml`.
2. Combine all research queues; hand unique unknown merchants to
   `transaction-research-agent`.
3. `--merge` its researched YAML into the rules file and re-categorize so the new
   knowledge applies to every statement.
4. Report coverage and any merchants honestly left UNKNOWN (never fabricate).

### Phase 3 — Flag for review
1. Confirm `flag_rules.yaml` thresholds fit the user's finances (ask if they look
   like defaults).
2. Flag each categorized CSV across the four dimensions (asset/property, income,
   child/custody, cash/undocumented).
3. Summarize flags by dimension; surface HIGH-priority items.

### Phase 4 — Assemble deliverables
1. Build the master workbook:
   `python .../pdf-statement-extractor/scripts/build_workbook.py --inputs OUT/ --out OUT/master_workbook.xlsx`.
2. Produce a run report: statements processed, verification results,
   categorization coverage, flag summary, and any statements needing attention.

## Output

- `master_workbook.xlsx` — Transactions / Summary / Reconciliation / Flags tabs
- Per-statement `*_review_queue.csv` — prioritized flagged rows for the attorney
- Per-statement `*_reconciliation.json` — the verification audit trail
- A short run report for the user

## Constraints

- NEVER advance an unverified statement; NEVER widen tolerances to force a pass.
- NEVER fabricate a merchant identity or transaction; leave it UNKNOWN.
- NEVER characterize the other party or present a flag as a legal conclusion.
- ALWAYS treat data as sensitive PII and keep it out of shared/public repos.
