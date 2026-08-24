# Stage 3 Prompt — Flag for Attorney Review + Build Workbook

Copy-paste this to Codex / Claude. Run only on verified + categorized statements.

---

You are organizing **facts** for my attorney. Flags mean "look at this for
review" — never a legal conclusion, and never a statement about anyone's intent.
Do not characterize the other party.

1. **Confirm thresholds first.** Open `config/flag_rules.yaml`. The large-amount
   and cash thresholds should match my normal finances so the review queue stays
   useful. If they look like defaults, ask me to confirm or adjust them before
   flagging.

2. **Flag** each categorized CSV:
   ```
   python skills/divorce-financial-flagger/scripts/flag_transactions.py data/output/<STEM>_transactions.csv --rules config/flag_rules.yaml
   ```
   This fills the `flags` column and writes a prioritized
   `data/output/<STEM>_review_queue.csv` across four dimensions:
   asset & property tracing, income tracing, child & custody expenses, and
   cash & undocumented flows.

3. **Build the master workbook:**
   ```
   python skills/pdf-statement-extractor/scripts/build_workbook.py --inputs data/output/ --out data/output/master_workbook.xlsx
   ```
   Tabs: Transactions, Summary, Reconciliation, Flags.

Reference: `skills/divorce-financial-flagger/references/divorce_flag_framework.md`.

When done, give me:
- Flag counts by dimension, and the HIGH-priority items.
- The location of `master_workbook.xlsx` and the per-statement review queues.
- A reminder that these organize facts for my attorney's review.

Keep all data local and out of git (see
`skills/divorce-financial-flagger/references/privacy_and_handling.md`).
