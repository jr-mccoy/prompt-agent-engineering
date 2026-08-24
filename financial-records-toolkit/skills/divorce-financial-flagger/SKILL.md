---
name: divorce-financial-flagger
description: Flags categorized transactions across divorce/custody-relevant dimensions (asset & property tracing, income tracing, child & custody expenses, cash & undocumented flows) and produces a prioritized review queue for an attorney. Use this skill to "flag transactions for divorce", "organize financial records for my lawyer", "find large transfers / cash withdrawals / asset movements", "build a review queue for the attorney", or to surface transactions worth a forensic look. Organizes facts only — it is not legal advice and makes no claims about intent.
license: MIT
compatibility: Python 3.8+ and PyYAML. Standard library otherwise.
metadata:
  tags: [finance, divorce, custody, family-law, forensic, flagging, attorney-prep, asset-tracing]
  updated: "2026-06-09"
---

# Divorce Financial Flagger

Tags transactions that an attorney or forensic reviewer may want to examine,
across four dimensions, and produces a prioritized review queue. It is the final
stage of the pipeline: extract → verify → categorize → **flag**.

> **What this skill is.** A tool that helps *you* organize *your own* financial
> records so *your* attorney can review them efficiently. It surfaces facts and
> patterns. It does **not** give legal advice, predict outcomes, or assert that
> any transaction was improper. Every flag means only: "a human should look at
> this."

## Purpose

In a divorce, the financial record is large and the relevant signal is buried.
This skill applies transparent, configurable rules to mark transactions in
categories that commonly matter — so nothing important is overlooked and your
attorney's time goes to judgment, not data entry.

## When to Use This Skill

Use this skill when you need to:
- Organize categorized transactions for a divorce/custody matter
- Surface large transfers, asset movements, crypto/brokerage activity
- Build an income picture from deposits and payroll
- Identify child/custody-related spending
- Find cash withdrawals and other undocumented flows worth explaining
- Produce a prioritized review queue for your attorney

## When NOT to Use This Skill

Do NOT use this skill:
- On unverified or uncategorized data → run verify, then categorize, first
- As a source of legal advice or conclusions about the other party
- To accuse, characterize, or infer intent — it organizes facts for counsel

## Prerequisites

- Python 3.8+, `pip install pyyaml`
- A **verified** and **categorized** transactions CSV
- A flag rules file — copy `assets/flag_rules.example.yaml` to `flag_rules.yaml`
  and tune thresholds with your situation (and ideally your attorney) in mind

## Quick Start

### Step 1: Tune the rules to your normal finances

**Purpose:** Keep the review queue signal-rich. A $500 cash threshold is noise
for one household and meaningful for another.

Edit `flag_rules.yaml`: adjust `min_amount` / `min_abs_amount` thresholds and add
merchant/regex patterns specific to your accounts. See `references/divorce_flag_framework.md`.

### Step 2: Flag the transactions

```bash
python scripts/flag_transactions.py output/statement_transactions.csv \
    --rules config/flag_rules.yaml
```

**Expected output:**
```
[flag] OK: 6/47 row(s) flagged (10 flag hits).
[flag] review queue -> output/statement_review_queue.csv
[flag] REMINDER: flags organize facts for YOUR ATTORNEY's review - not legal conclusions.
```

The `flags` column is filled with codes like `CASH:LARGE_CASH|HIGH`, and a
prioritized `<stem>_review_queue.csv` lists only the flagged rows.

### Step 3: Build the attorney workbook

```bash
python ../pdf-statement-extractor/scripts/build_workbook.py --inputs output/ \
    --out output/attorney_review.xlsx
```

The workbook gains a **Flags** tab (flagged rows highlighted) alongside
Transactions / Summary / Reconciliation.

**Validation:**
- [ ] Flagged rows match the dimensions you care about
- [ ] HIGH-priority rows are marked `needs_review = TRUE`
- [ ] The review queue is sorted with HIGH items first
- [ ] You can explain (or want your attorney to ask about) each HIGH item

## Common Issues

### Issue: Too many flags / too much noise
Thresholds are too low for your finances. Raise `min_amount`/`min_abs_amount`
and remove rules that don't apply to you.

### Issue: A clearly innocent transaction is flagged
That is expected — a flag is "look at this," not "this is wrong." Leave it for
the attorney, or tighten the specific rule.

### Issue: Something important wasn't flagged
Add a rule. The rules file is plain YAML; every dimension is extensible. Discuss
with your attorney what categories matter for your jurisdiction.

## Deep Dive References

- **The four dimensions and what each flag means:** `references/divorce_flag_framework.md`
- **Handling sensitive financial data safely:** `references/privacy_and_handling.md`

## Safety & Constraints

**NEVER:**
- Present a flag as a legal conclusion or evidence of wrongdoing
- Infer or assert the other party's intent
- Characterize, accuse, or editorialize in the `notes` — record facts only
- Fabricate a merchant identity or transaction detail
- Commit the raw statements, outputs, or review queues to a shared/public repo

**ALWAYS:**
- Frame output as "for your attorney's review"
- Run only on verified + categorized data
- Keep rules transparent and tuned to your real finances
- Let your attorney decide what matters and how to use it
- Follow `references/privacy_and_handling.md` for storage and deletion

## Reference Files

| Resource | Purpose |
|----------|---------|
| `scripts/flag_transactions.py` | Applies the 4-dimension rules; writes flags + prioritized review queue |
| `assets/flag_rules.example.yaml` | Tunable rules for all four dimensions — copy and adjust |
| `references/divorce_flag_framework.md` | What each dimension/flag captures and how to tune it |
| `references/privacy_and_handling.md` | Local-only processing, .gitignore, secure deletion |

## Related Skills

- `transaction-categorizer` — must run before flagging
- `statement-reconciliation-verifier` — verification underpins everything
- `pdf-statement-extractor` — `build_workbook.py` assembles the attorney workbook
