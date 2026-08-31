# ADR-0001 — The PAE Engine lives at `pae-engine/`

## Status

Accepted. Not yet implemented — the directory does not exist.

## Context

The executable layer needs a home. Three constraints collided:

1. `.github/workflows/structure.yml` derives an allowlist of permitted top-level
   directory *shapes* from the layout and fails on anything else. A top-level
   `src/` — the shape the original specification proposed — is rejected, as are
   `docs/` and `benchmarks/`.
2. The repository root already has a `tests/` directory with different
   semantics (see [ADR-0002](0002-preserve-root-tests.md)), so a conventional
   Python project laid out at the root would collide with it.
3. Product code has dependencies the corpus does not, and mixing them at the
   root makes the boundary invisible.

## Decision

The engine lives in a single dedicated top-level directory:

```text
pae-engine/
├── pyproject.toml
├── src/pae/
├── tests/
├── docs/
└── benchmarks/
```

Subdirectories get created when a phase needs them, not up front.

`structure.yml` will be amended to permit **exactly** `pae-engine/`. The
amendment must not relax the gate into a permissive catch-all, and the engine
must not be renamed into an unrelated `*-kit` / `*-factory` shape merely to
avoid touching CI. The gate is the repository's contract; changing it is the
honest move, and it stays reviewable because the change is one literal name.

Nested `docs/`, `tests/`, and `benchmarks/` are invisible to the gate, which
inspects depth 1 only.

## Consequences

- One reviewed CI change is required before any engine code lands.
- The engine gets a conventional internal Python layout, so `pip install -e .`,
  `python -m build`, and standard tooling all behave normally.
- Product dependencies stay isolated from the corpus validators, whose only
  third-party dependency is PyYAML.
- The corpus keeps root `tests/` unchanged.
