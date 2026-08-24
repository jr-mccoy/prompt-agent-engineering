# Financial Records Skills

A four-stage pipeline that turns bank and credit-card statements into organized,
**verified**, categorized, and flagged spreadsheets — built for someone organizing
their **own** financial records for their **own** attorney (e.g. a divorce/custody
matter). Tool-agnostic: the engine is plain Python, wrapped as Claude Code skills
and runnable from Codex (see the portable `financial-records-toolkit/`).

> These skills organize **facts**. They are not legal advice and make no claim
> about anyone's intent. Flags mean "a human should review this."

## The pipeline (run in order)

| Stage | Skill | Does | Key guarantee |
|-------|-------|------|---------------|
| 1 | [`pdf-statement-extractor`](pdf-statement-extractor/) | PDF/text/CSV → normalized transactions CSV + Excel | deterministic parsing, no silent loss |
| 2 | [`statement-reconciliation-verifier`](statement-reconciliation-verifier/) | proves every transaction transferred | **hard gate** (balance + coverage) |
| 3 | [`transaction-categorizer`](transaction-categorizer/) | Plaid categories; researches unknown merchants | learns merchants permanently |
| 4 | [`divorce-financial-flagger`](divorce-financial-flagger/) | flags across 4 divorce/custody dimensions | prioritized attorney review queue |

The four flag dimensions: **asset & property tracing**, **income tracing**,
**child & custody expenses**, **cash & undocumented flows**.

## Orchestration

- Agent `financial-records-orchestrator` drives all four stages over a folder of
  statements and enforces the verification gate.
- Agent `transaction-research-agent` identifies unknown merchants for Stage 3.
- Command `/process-financials` runs the whole pipeline.

(Agents live in `domain-agentic-resources/agents/business-operations/`; the command
in `domain-agentic-resources/commands/data-analysis/`.)

## Dependencies

Core data layer is pure standard library. Only PDF reading needs `pdfplumber`,
only the `.xlsx` workbook needs `openpyxl`, and the categorize/flag rules need
`pyyaml`. Scanned PDFs need `ocrmypdf`; `rapidfuzz` improves fuzzy matching
(optional). Everything degrades gracefully with an actionable message.

## Privacy

This is sensitive PII. Process locally, keep raw statements and outputs out of
version control, and delete working copies when done. See
[`divorce-financial-flagger/references/privacy_and_handling.md`](divorce-financial-flagger/references/privacy_and_handling.md).

## Portable bundle

A self-contained copy (skills + agents + command + config + Codex `AGENTS.md` +
stage prompts) lives at repo root: [`financial-records-toolkit/`](../../../financial-records-toolkit/).
Copy it into a private repo to process statements with Claude Code or Codex.
