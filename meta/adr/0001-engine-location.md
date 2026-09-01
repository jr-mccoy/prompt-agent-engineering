# ADR-0001 — The PAE Engine lives at `pae-engine/`

## Status

Accepted. Implemented in Phase 3, with the import-path amendment recorded
below. See [ADR-0017](0017-engine-package-identity.md) for the naming that
superseded the illustrative `src/pae/` layout.

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

## Amendment (Phase 3) — the import path is `src/pae_engine/`

The layout above was illustrative and used `src/pae/`. That import namespace is
owned by an unrelated project on PyPI, so it is not available to this one. The
directory decision is unchanged; only the package name inside it moves:

```text
pae-engine/
├── pyproject.toml
├── LICENSE            # byte-identical to the repository LICENSE, checked in CI
├── README.md
├── src/pae_engine/
├── tests/
└── docs/
```

`benchmarks/` was not created: Phase 3 measures performance during
implementation and reports the numbers, rather than standing up a benchmark
suite whose access patterns search has not yet defined.

`structure.yml` was amended as this ADR required — one literal `pae-engine`
case, not a `pae-*` or `*-engine` pattern. The reasoning holds: a catch-all
would retire the contract to save a line.

The naming decision itself is recorded separately in
[ADR-0017](0017-engine-package-identity.md).
