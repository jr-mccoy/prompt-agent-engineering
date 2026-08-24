# Stage 2 Prompt — Categorize + Research Unknown Merchants

Copy-paste this to Codex / Claude. Run only on statements that returned
`RESULT: VERIFIED` in Stage 1.

---

For each **verified** transactions CSV in `data/output/`:

1. **Categorize** against the shared rules:
   ```
   python skills/transaction-categorizer/scripts/categorize_transactions.py data/output/<STEM>_transactions.csv --rules config/category_rules.yaml
   ```

2. Open the `data/output/<STEM>_research_queue.csv` it produces. For each unknown
   merchant descriptor:
   - Strip processor noise (`SQ *`, `TST*`, `PP*`, `ACH DEBIT`, trailing numbers,
     city/state) to find the core name.
   - **Web-search** the core name to identify the business. **Never guess** — if
     you can't identify it, leave it `UNKNOWN`.
   - Classify to the Plaid taxonomy. Remember: Venmo/Zelle/PayPal/Cash App and
     brokerages/crypto exchanges are `TRANSFER_IN`/`TRANSFER_OUT`, not spending.

3. Save findings to `researched.yaml`:
   ```yaml
   - match: "SQ *BLUE BOTTLE"
     category: FOOD_AND_DRINK
     subcategory: COFFEE
     note: "researched: Blue Bottle Coffee (Square seller)"
   ```

4. **Teach the rules and re-categorize** so it learns for every statement:
   ```
   python skills/transaction-categorizer/scripts/categorize_transactions.py --merge researched.yaml --rules config/category_rules.yaml
   python skills/transaction-categorizer/scripts/categorize_transactions.py data/output/<STEM>_transactions.csv --rules config/category_rules.yaml
   ```

Reference: `skills/transaction-categorizer/references/merchant_research_protocol.md`
and `category_taxonomy.md`.

When done, report categorization coverage (% categorized) and list any merchants
left honestly UNKNOWN. Search only merchant names — never my account number, name,
or balances.
