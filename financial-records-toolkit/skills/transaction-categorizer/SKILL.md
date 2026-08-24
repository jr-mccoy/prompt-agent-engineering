---
name: transaction-categorizer
description: Categorizes extracted bank/credit-card transactions using the Plaid personal-finance taxonomy, and routes merchants it does not recognize into a research queue so they can be identified (via web lookup) and learned permanently. Use this skill to "categorize transactions", "label my spending", "classify these transactions", "what category is this merchant", or to enrich a verified transactions CSV before analysis or flagging. Deterministic MCC/regex/fuzzy matching with a learn-back loop.
license: MIT
compatibility: Python 3.8+ and PyYAML. rapidfuzz is optional (better fuzzy matching; falls back to difflib).
metadata:
  tags: [finance, categorization, plaid-taxonomy, merchants, mcc, transactions, bookkeeping]
  updated: "2026-06-09"
---

# Transaction Categorizer

Assigns each transaction a category from the Plaid personal-finance taxonomy
(16 primary categories), using deterministic matching first and routing
unrecognized merchants to a research queue so categorization gets more complete
over time.

## Purpose

Raw descriptions like `SQ *BLUE BOTTLE` or `ACH DEBIT 8829` are not analyzable.
This skill maps them to consistent categories so spending can be summarized,
compared, and flagged. Crucially, it does not guess on unknowns — it queues them
for identification and **learns** each answer so the next statement is easier.

## When to Use This Skill

Use this skill when you need to:
- Assign spending categories to a verified transactions CSV
- Build a consistent category vocabulary across many statements
- Identify unfamiliar merchants and record what they are
- Prepare data for divorce/custody flagging or general budgeting

## When NOT to Use This Skill

Do NOT use this skill when:
- The statement has not been verified → run `statement-reconciliation-verifier` first
- You need legal/divorce flags → use `divorce-financial-flagger` (runs after this)
- You only need raw extraction → use `pdf-statement-extractor`

## Prerequisites

- Python 3.8+, `pip install pyyaml` (and optionally `rapidfuzz`)
- A rules file — copy `assets/category_rules.example.yaml` to your working `category_rules.yaml`
- A **verified** transactions CSV (`RESULT: VERIFIED`)

## Quick Start

### Step 1: Categorize a verified statement

```bash
python scripts/categorize_transactions.py output/statement_transactions.csv \
    --rules config/category_rules.yaml
```

**Expected output:**
```
[categorize] 3 unknown merchant(s) -> research queue: output/statement_research_queue.csv
[categorize] OK: 44/47 categorized; 3 unique unknown(s).
```

This fills `category`/`subcategory`/`confidence` in the CSV and writes a research
queue of merchants it could not identify.

### Step 2: Research unknown merchants

**Purpose:** Identify each queued merchant so it can be categorized accurately.

For each row in `<stem>_research_queue.csv`, identify the merchant (web search of
the descriptor, MCC lookup, or the user's own knowledge) and record findings as a
YAML list. See `references/merchant_research_protocol.md`. The
`transaction-research-agent` automates this step.

```yaml
# researched.yaml
- match: "SQ *BLUE BOTTLE"
  category: FOOD_AND_DRINK
  subcategory: COFFEE
  note: "researched: Blue Bottle Coffee (Square seller)"
- match: "WEALTHFRONT"
  category: TRANSFER_OUT
  subcategory: INVESTMENT
  note: "researched: Wealthfront automated investing"
```

### Step 3: Teach the rules, then re-categorize

**Purpose:** Make the answers permanent so every future statement benefits.

```bash
python scripts/categorize_transactions.py --merge researched.yaml --rules config/category_rules.yaml
python scripts/categorize_transactions.py output/statement_transactions.csv --rules config/category_rules.yaml
```

**Validation:**
- [ ] The previously-unknown merchants now show a category
- [ ] The research queue is empty (or only genuinely unidentifiable rows remain)
- [ ] Rows below the fuzzy threshold are marked `needs_review = TRUE`

## Common Issues

### Issue: Everything is UNKNOWN
The rules file was empty or the path was wrong. Confirm `--rules` points at a
populated YAML (start from `assets/category_rules.example.yaml`).

### Issue: A merchant is mis-categorized by a broad regex
Regex patterns are broad by design. Add a more specific `merchant_whitelist`
entry — exact/substring whitelist matches win over regex.

### Issue: Fuzzy matches are too loose/strict
Tune `--threshold` (default 0.86). Higher = stricter (fewer fuzzy matches → more
unknowns to research); lower = more aggressive guessing.

## Deep Dive References

- **The Plaid taxonomy and how matching layers work:** `references/category_taxonomy.md`
- **How to research an unknown merchant responsibly:** `references/merchant_research_protocol.md`

## Safety & Constraints

**NEVER:**
- Invent a merchant identity. If you cannot identify it, leave it `UNKNOWN` and `needs_review = TRUE`
- Categorize an unverified statement

**ALWAYS:**
- Record the basis for a researched merchant in the `note` field
- Prefer deterministic matches (MCC/whitelist/regex) over fuzzy guessing
- Keep the rules file under version control so the learned vocabulary persists

## Reference Files

| Resource | Purpose |
|----------|---------|
| `scripts/categorize_transactions.py` | Layered categorizer + research-queue + `--merge` learn-back |
| `assets/category_rules.example.yaml` | Seed Plaid rules (whitelist, regex, MCC) — copy and extend |
| `references/category_taxonomy.md` | Plaid categories + matching-layer explanation |
| `references/merchant_research_protocol.md` | Identifying unknown merchants without fabricating |

## Related Skills

- `statement-reconciliation-verifier` — must pass before categorizing
- `transaction-research-agent` (agent) — automates Step 2 research
- `divorce-financial-flagger` — runs after categorization
