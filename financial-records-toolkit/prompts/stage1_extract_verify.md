# Stage 1 Prompt — Extract + Verify

Copy-paste this to Codex / Claude (or follow it yourself).

---

You are processing personal financial statements. For **every** file in
`data/input_pdfs/`, do the following, one statement at a time. Treat all data as
sensitive PII and keep it out of git.

1. **Extract** to `data/output/`:
   ```
   python skills/pdf-statement-extractor/scripts/extract_statement.py "data/input_pdfs/<FILE>" --out data/output/
   ```
   - Add `--ocr` if the PDF is scanned (no extractable text).
   - Add `--account-type credit` for credit-card statements.

2. **Verify** immediately (this is a hard gate):
   ```
   python skills/statement-reconciliation-verifier/scripts/reconcile_statement.py data/output/<STEM>_transactions.csv
   ```

3. Record each statement's result:
   - `RESULT: VERIFIED` → ready for Stage 2.
   - `RESULT: DISCREPANCY` → DO NOT proceed for this file. Open
     `data/output/<STEM>_reconciliation.json`, note the errors (balance mismatch
     and/or unmatched raw lines), and set it aside.

4. If extraction returns **0 transactions**, the layout needs a hint — see
   `skills/pdf-statement-extractor/references/statement_formats.md` and add an
   entry to `config/institutions.yaml`, then retry.

When done, give me a table: statement | transactions | balance check | coverage |
RESULT. List every DISCREPANCY separately with its error so I can fix it. Do not
categorize or flag anything yet.
