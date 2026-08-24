# Financial Records Toolkit

A staged, tool-agnostic pipeline for turning bank and credit-card statements into
organized, **verified**, categorized, and flagged spreadsheets — built to be
driven by **Claude Code** or **Codex** (or run by hand). Designed for someone
organizing **their own** financial records for **their own** attorney.

> **This toolkit organizes facts. It is not legal advice.** Flags mean "a human
> should look at this," never that a transaction was improper. Your attorney
> decides what matters.

## The pipeline

```
PDF statements
   │  1. EXTRACT      pdf-statement-extractor   → transactions CSV (+ raw text + meta)
   ▼
   │  2. VERIFY       statement-reconciliation-verifier  → PASS/FAIL (HARD GATE)
   ▼   (only verified statements continue)
   │  3. CATEGORIZE   transaction-categorizer   → Plaid categories + research queue
   │                  (unknown merchants researched, then learned permanently)
   ▼
   │  4. FLAG         divorce-financial-flagger → 4-dimension flags + review queue
   ▼
master_workbook.xlsx  +  prioritized review queue for your attorney
```

**Verification is a hard gate.** Stage 2 proves *every transaction transferred
correctly* (balance reconciliation + a line-by-line coverage check). Nothing gets
categorized or flagged until it passes.

The four flag dimensions: **asset & property tracing**, **income tracing**,
**child & custody expenses**, and **cash & undocumented flows**.

## What's in here

| Path | What it is |
|------|------------|
| `skills/` | Four Claude Code skills (each self-contained: `SKILL.md` + `scripts/` + `references/` + `assets/`) |
| `agents/` | `financial-records-orchestrator` (drives the pipeline) + `transaction-research-agent` (identifies unknown merchants) |
| `commands/` | `process_financials.md` — the `/process-financials` slash command |
| `config/` | Working `category_rules.yaml`, `flag_rules.yaml`, `institutions.yaml` — tune these |
| `prompts/` | Plain stage prompts for Codex / manual use |
| `data/` | `input_pdfs/` (put statements here) and `output/` (results) — both git-ignored |
| `AGENTS.md` | Entry point for Codex |
| `requirements.txt` | Python dependencies (mostly optional — core is stdlib) |

## Setup

```bash
pip install -r requirements.txt        # pdfplumber (PDF), openpyxl (xlsx), pyyaml
# Optional: pip install ocrmypdf rapidfuzz     # scanned PDFs / better fuzzy matching
```

The data layer is pure standard library: only PDF reading needs `pdfplumber` and
only the `.xlsx` workbook needs `openpyxl`. Everything degrades gracefully with a
clear message if a library is missing.

## Quick start (manual / any tool)

```bash
# Put your statements in data/input_pdfs/, then for one statement:
python skills/pdf-statement-extractor/scripts/extract_statement.py \
    data/input_pdfs/chase_jan.pdf --out data/output/

python skills/statement-reconciliation-verifier/scripts/reconcile_statement.py \
    data/output/chase_jan_transactions.csv          # must say RESULT: VERIFIED

python skills/transaction-categorizer/scripts/categorize_transactions.py \
    data/output/chase_jan_transactions.csv --rules config/category_rules.yaml

python skills/divorce-financial-flagger/scripts/flag_transactions.py \
    data/output/chase_jan_transactions.csv --rules config/flag_rules.yaml

python skills/pdf-statement-extractor/scripts/build_workbook.py \
    --inputs data/output/ --out data/output/master_workbook.xlsx
```

Scanned PDF? add `--ocr`. Credit card? add `--account-type credit`.

## Using with Claude Code

Copy the resources into your repo's Claude config, then let the orchestrator run:

```bash
mkdir -p .claude/skills .claude/agents .claude/commands
cp -r skills/*    .claude/skills/
cp    agents/*    .claude/agents/
cp    commands/*  .claude/commands/
```

Then: `/process-financials` (point it at `data/input_pdfs/` and `data/output/`),
or just ask Claude to "process all the statements in data/input_pdfs."

## Using with Codex

See **`AGENTS.md`** — it gives Codex the exact staged workflow and script
invocations. The `prompts/` folder has a copy-paste prompt for each stage.

## Tuning

- `config/category_rules.yaml` — add merchants/regex; the categorizer learns
  researched merchants here permanently (`--merge`).
- `config/flag_rules.yaml` — set large-amount and cash thresholds to **your**
  normal finances so the review queue stays signal-rich. Discuss with your attorney.
- `config/institutions.yaml` — only needed if a bank's layout won't parse.

## Privacy — read before you start

This data is sensitive. The pipeline runs **locally**; the only optional network
step is merchant research, which searches a *merchant name*, never your PII.

If you drive this from a **private GitHub repo**:
- Confirm the repo is **private** before pushing.
- The included `.gitignore` keeps raw PDFs and all outputs **out of git** — commit
  only the tooling.
- When done: download what you need, then **delete the repo** and local copies.

Full details: `skills/divorce-financial-flagger/references/privacy_and_handling.md`.

## A word on good faith

These tools help you produce a **complete and honest** financial picture for your
attorney. Full disclosure is the expectation in family-law matters — use this to
organize and disclose thoroughly, not to hide anything.
