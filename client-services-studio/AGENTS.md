# AGENTS.md — Client Services Studio

Entry point for coding agents (Codex, Claude Code, Cursor) working in this directory.

*Not legal, tax, or accounting advice. Say so in any output that touches a contract
or a number.*

## What this directory is

A gated pipeline for selling and delivering expertise: qualify → discover → scope →
price → propose → contract → deliver → invoice → close out. Four gates are enforced
in code. Read [`README.md`](README.md) first, then
[`PIPELINE_OVERVIEW.md`](PIPELINE_OVERVIEW.md).

## The rules that matter

1. **Run the gates; do not simulate them.** Each gate is a script with an exit code.
   Reporting a gate result you did not execute is the failure mode this directory
   exists to prevent.

   ```bash
   python3 skills/scope-ledger/scripts/scope_ledger.py --gate0 <lead> --config config/practice.json
   python3 skills/scope-ledger/scripts/scope_ledger.py --gateA <engagement>
   python3 skills/proposal-assembler/scripts/assemble.py --gateB <engagement>
   python3 skills/engagement-economics/scripts/economics.py --gateC <closeout>
   ```

2. **A blocked gate stops the stage.** Report which check fired and what would clear
   it. Do not offer a workaround.

3. **Orchestrate, do not duplicate.** When a stage calls for a domain prompt, read it
   from `referenced-prompts/` and use it. Do not write a new prompt that does what an
   existing one does — that is the defect the parent repository's structure exists to
   prevent.

4. **The engagement record is authoritative.** New information goes into the JSON
   record, not into prose. Schema:
   [`skills/scope-ledger/references/record-schema.md`](skills/scope-ledger/references/record-schema.md).

5. **Never edit a file under `referenced-prompts/`.** They are pinned copies checked
   byte-for-byte against their canonicals by `scripts/check_vendored_copies.py` in
   the parent repository. Edit the canonical, then run that script with `--fix`.

6. **Standard library only.** Every script runs on Python 3.9+ with no dependencies
   and no network. Keep it that way; there is no `requirements.txt` by design.

7. **Every script carries `--self-check`.** If you change a script, extend its
   self-check and the suite in `tests/`.

## Before you commit

```bash
for s in skills/*/scripts/*.py; do python3 "$s" --self-check; done
python3 -m unittest discover -s tests -v
```

From the parent repository root:

```bash
python3 scripts/validate_naming_conventions.py --ci
python3 scripts/check_relative_links.py
python3 scripts/check_vendored_copies.py
python3 scripts/generate_registry.py --check
```

## What you must not do

- Interpret a contract clause, opine on enforceability, or give tax advice.
- Quote a price before Gate A passes.
- Recommend escalating a disputed invoice.
- Propose a suspension of work without a recorded contractual right.
- Put real client data in `samples/` or `config/`. The fixtures are fictional and
  must stay that way.

## Where things live

| Need | Path |
|---|---|
| Stage instructions | `prompts/stage-N-*.md` |
| Gate implementations | `skills/*/scripts/*.py` |
| Record schema | `skills/scope-ledger/references/record-schema.md` |
| Red-flag definitions | `skills/proposal-assembler/references/red-flags.md` |
| The escalation ladder | `skills/receivables-tracker/references/ladder.md` |
| Rate-floor derivation | `skills/engagement-economics/references/method.md` |
| Worked run with every gate firing | `DRY_RUN.md` |
