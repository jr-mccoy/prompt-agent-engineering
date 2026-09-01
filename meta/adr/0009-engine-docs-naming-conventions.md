# ADR-0009 — `pae-engine/` is intentionally outside the corpus naming conventions

## Status

Accepted. Recorded now so it is a decision rather than an accident later.

## Context

`scripts/validate_naming_conventions.py` enforces the corpus's Markdown naming
rules: `snake_case` lowercase prompt filenames with no articles, `SHOUTING` for
guide/entry docs, a maximum filename length, and no special characters.

Its scope is **derived from the layout**, not hardcoded: it checks top-level
directories matching `domain-*`, the bundle suffixes (`-toolkit`, `-kit`,
`-studio`, `-library`, `-system`, `-factory`), plus `techniques` and `authoring`.

`pae-engine` matches none of those patterns. So the moment the directory is
created, its Markdown is unvalidated by that script — as a side effect of the
name, not as anyone's decision. Had the engine been named `pae-kit`, the corpus
rules would have applied to it and a conventional `docs/getting-started.md` would
have been a violation.

## Decision

The exclusion is deliberate and stands. Engine documentation follows ordinary
software-project conventions (`README.md`, `docs/getting-started.md`,
`CONTRIBUTING.md`, kebab-case filenames) rather than the corpus's prompt naming
rules, which exist to make thousands of prompt files sortable and predictable —
a problem the engine does not have.

`scripts/check_relative_links.py` walks **every** Markdown file in the
repository, so engine documentation links are still validated. That coverage must
be preserved when the directory is created.

If engine Markdown should later be naming-checked, the change is to add
`pae-engine` to the `always` set in `_check_directories()` — an explicit edit,
which is the point of recording this.

## Consequences

- Engine docs read like a normal Python project's docs.
- One validator has a documented blind spot rather than an unnoticed one.
- Broken links in engine docs still fail CI.
- Reviewers of the future `pae-engine/` addition should confirm
  `check_relative_links.py` still covers it and that no other validator silently
  skips it.
