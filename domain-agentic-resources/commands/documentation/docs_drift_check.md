---
name: docs_drift_check
description: Find documentation that has fallen out of sync with the code. Extracts checkable claims from READMEs and docs (CLI commands and flags, environment variables, config keys and defaults, API endpoints, function and class names and signatures, file paths, import lines in code samples, version numbers) and verifies each against the current source, classifying it CONFIRMED, DRIFTED, MISSING, or UNCHECKABLE with the code evidence and a suggested correction. Read-only by default. Distinct from doc-generate (writes new docs), the documentation-coverage analysis (finds undocumented code), and docs-cleaner (merges redundant docs).
version: "1.0.0"
category: documentation
tags: [documentation, docs, drift, readme, staleness, verification, code-sync, maintenance]
agents_used: []
---

# Docs Drift Check

Verify that what the documentation says about the code is still true. Every
finding cites the doc location and the code evidence; nothing is reported as
drift on a hunch.

[Extended thinking: Documentation drifts one rename at a time — a flag is
renamed, an env var gets a prefix, an endpoint moves to /v2, a default changes,
a quickstart imports a module that no longer exists. Readers hit these first.
Most such claims are mechanically checkable against the source with search, so
the command extracts claims, checks each, and separates what it could verify
from what it could not. Prose claims about behaviour are listed as UNCHECKABLE
rather than guessed at.]

## Requirements
$ARGUMENTS

Expected: the docs to check (default: `README*`, `docs/**`, `CONTRIBUTING*`,
and other `*.md` outside vendored or generated directories) and the code root.
Optional: a narrower scope ("only the CLI reference"), and `--reverse` to also
list public surface in code that the docs never mention.

## When NOT to use

- Generating documentation from code → `/doc-generate`
  (`commands/documentation/doc_generate.md`)
- Measuring which code has no docs at all (coverage, not correctness) →
  `domain-software-engineering/analysis/quality/quality_code_documentation_coverage_analysis.md`
- Consolidating redundant or overlapping doc files → `skills/document-processing/docs-cleaner/`
- AI model and data documentation versus the deployed model →
  `domain-AI-ML/responsible-ai-governance/rai_documentation_freshness_audit.md`
- Checking a changelog against a commit range → `/changelog_reconcile`
  (`commands/documentation/changelog_reconcile.md`)

## Configuration

- `--reverse`: also report public surface (CLI flags, exported functions, env
  vars read by the code, routes) with no mention in the docs
- `--paths <glob>`: restrict the docs scanned
- `--suggest-patch`: include a suggested diff for each DRIFTED/MISSING claim
  (still read-only — the patch is printed, not applied)

## Instructions

### Phase 1 — Inventory claims
Scan the docs and extract claims that can be checked against source:

| Claim type | Examples | How to verify |
|------------|----------|---------------|
| CLI command / flag | `mytool sync --dry-run` | Find the argument parser / command registration |
| Environment variable | `export APP_TOKEN=...` | Search for reads of the variable name |
| Config key and default | `timeout: 30` (default) | Find the config schema/loader and its default |
| API endpoint | `POST /v1/orders` | Find the route definition and method |
| Symbol / signature | `client.fetch(id, retries=3)` | Find the definition; compare parameters and defaults |
| File / directory path | `see src/plugins/` | Check the path exists |
| Code sample imports | `from pkg.utils import parse` | Check the module and symbol exist and are exported |
| Version / requirement | "requires Node 18+" | Compare with manifest/engines/CI matrix |

Skip vendored, generated, and archived directories; say which you skipped.

### Phase 2 — Verify each claim
Use search (`Grep`/`rg`) and file reads. For each claim record:
- **CONFIRMED** — found and matches
- **DRIFTED** — found but differs (renamed flag, changed default, different method, extra required parameter)
- **MISSING** — not found anywhere in the code root
- **UNCHECKABLE** — behavioural or prose claim that search cannot settle

A useful secondary signal: compare the last commit date of the doc with that of
the code it describes (`git log -1 --format=%ci -- <path>`). Older docs about
recently changed code raise priority; date alone is never a finding.

Gate: before reporting MISSING, search for likely renames (case variants,
prefixes, moved modules). A symbol that moved is DRIFTED, not MISSING.

### Phase 3 — Reverse check (only with `--reverse`)
List user-facing surface present in code but absent from docs. Report it as
UNDOCUMENTED, separately — it is a gap, not drift.

### Phase 4 — Report
Prioritise by reader impact: quickstart/install steps and copy-paste commands
first, then reference pages, then internal docs.

## Output

```markdown
# Docs Drift Report: <repo/scope>
Docs scanned: <n files> · Claims extracted: <n> · Skipped dirs: <list>

## Summary
CONFIRMED <n> · DRIFTED <n> · MISSING <n> · UNCHECKABLE <n> (· UNDOCUMENTED <n>)

## Drift (highest reader impact first)
| Doc location | Claim | Status | Code evidence | Suggested correction |
|--------------|-------|--------|---------------|----------------------|
| README.md:42 | `--dry-run` flag | DRIFTED | cli.py:88 defines `--dryrun` | Change to `--dryrun` (or restore alias) |

## Unverifiable claims (need a human or a test)
- <doc:line> — <claim>

## Undocumented surface (--reverse)
- <symbol/flag/route> — <code location>
```

## Success Criteria

- Every DRIFTED/MISSING finding cites both the doc line and the code evidence
- Renames were searched before anything was called MISSING
- UNCHECKABLE claims are listed, not silently dropped or guessed
- No files were modified

## Constraints

- Read-only: NEVER edit docs or code in this command; patches are printed only
- NEVER report drift from date heuristics alone
- NEVER treat example placeholder values (`<your-token>`, `example.com`) as claims
