# ADR-0002 — Root `tests/` stays the prompt/technique experimentation area

## Status

Accepted.

## Context

The repository's top-level `tests/` directory is not a software test suite. It
holds the prompting-technique comparison work: `established/`, `experimental/`,
`results/`, `TASK_DEFINITION.md`, and `SCORING_RUBRIC.md` — Markdown artifacts
recording prompt experiments and their scored outputs.

A conventional Python project would want that path for unit tests. Taking it
would either relocate real experimental records or bury them under an unrelated
convention.

The repository's two existing Python packages already show the alternative: both
`continuity-kit/` and `ai-investment-research-toolkit/` run
`python -m unittest discover -s tests` from inside their own directory.

## Decision

Leave root `tests/` alone. It remains the prompt/technique experimentation area.

Engine tests live at `pae-engine/tests/`, following the existing per-package
convention.

Initial test framework: the standard library's `unittest`, matching
`continuity-kit/`. `pytest` may be added later as a deliberate development
dependency if an implementation demonstrates a concrete need; it is not required
for the product to be credible.

## Consequences

- No experimental records are moved or renamed.
- Engine tests are discovered from the engine directory, consistent with the
  other two packages, and CI gains one more `unittest discover` job rather than a
  new framework.
- Anyone expecting root `tests/` to be a Python suite will be briefly surprised;
  `ARCHITECTURE.md` states the distinction.
