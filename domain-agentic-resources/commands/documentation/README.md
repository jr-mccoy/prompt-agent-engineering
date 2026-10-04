# Documentation Commands

> Commands for documentation generation and for verifying that existing docs and changelogs still match the code.

## Commands

| Command | Syntax | Description |
|---------|--------|-------------|
| [doc_generate.md](./doc_generate.md) | `/doc-generate` | Generate comprehensive documentation from code including API docs and architecture diagrams |
| [docs_drift_check.md](./docs_drift_check.md) | `/docs_drift_check` | Verify checkable claims in docs (CLI flags, env vars, config keys, endpoints, signatures, paths, sample imports) against current code; CONFIRMED / DRIFTED / MISSING / UNCHECKABLE with evidence. Read-only |
| [changelog_reconcile.md](./changelog_reconcile.md) | `/changelog_reconcile` | Pre-tag check of a changelog section against the commit range: MISSING, PHANTOM, MISCLASSIFIED, BREAKING-UNFLAGGED, DUPLICATE; drafts entries for gaps. Read-only |

## Usage

These commands are invoked using slash syntax: `/command-name [arguments]`

## Related Resources

- [Commands Index](../README.md)
- [Agents Index](../../agents/README.md)
