# Phase 7 — Packaging & Distribution (pipx)

| | |
|---|---|
| **Phase** | 7 of 10 (post-MVP) |
| **Prerequisites** | Phase 6 done (MVP-trust) **and** dogfood validated (§18 Phase 3) |
| **Plan sections** | §18 Phase 4, §20 task 15, §22 resolved (Python end-to-end) |
| **Ships** | A `pipx install continuity-kit` package exposing the `continuity` binary |
| **Session size** | Small–medium |

---

## Objective

Turn the single-file `continuity.py` into a properly packaged, `pipx`-installable tool with a `continuity` entry point — **only after** dogfooding proved the CLI semantics worth shipping (plan §20.15: "Only then design package distribution").

## Scope / Tasks
1. **Package structure:** convert `continuity.py` into a package (`continuity_kit/`) if it has grown; keep stdlib-first. Add `pyproject.toml` with a `continuity` console-script entry point.
2. **Naming:** package `continuity-kit`, binary `continuity` (plan §1).
3. **Versioning:** semantic version; embed schema_version compatibility note (the manifest carries `schema_version: 1`).
4. **`pipx install continuity-kit`** path works locally from source (`pipx install .`) and from build artifact.
5. **Bundle templates/fixtures** as package data so `init` finds `templates/project-memory/` post-install (don't rely on repo-relative paths).
6. **Smoke test installed binary:** `continuity init/remember/capture/resume/guard/audit/validate` run from a `pipx`-installed environment, not just `python continuity.py`.
7. **Docs:** install section in README; note the deliberate **no-npx** stance (plan §18 Phase 4 — `npx` reach is a separately-justified future decision, not a default migration).

## Acceptance criteria
- [x] `pipx install .` yields a working `continuity` on PATH. _(Verified via `pip install .` into an isolated venv — the same mechanism pipx uses; pipx itself unavailable in the build env. Console script `continuity` lands on PATH.)_
- [x] `init` locates bundled templates post-install. _(Templates ship as package data under `continuity_kit/templates/`; `init` from a wheel-installed binary in a fresh dir creates the full tree incl. the 4 `.gitkeep`-backed record dirs.)_
- [x] All MVP commands smoke-test green from the installed binary. _(`init/validate/remember/capture/resume/search/guard/audit/scan-secrets` + `--version` all run from `/tmp/cv/bin/continuity`.)_
- [x] `pyproject.toml` declares entry point, version, schema-compat note, packaged data.
- [x] README install + distribution docs updated. _(New **Install** section: pipx primary, pip fallback, version+schema note, explicit no-npx stance, two-invocation-forms note.)_

## Implementation tracker

| # | Task | Status | Notes |
|---|---|---|---|
| 1 | package layout / pyproject.toml | ✅ | `continuity.py` → `continuity_kit/cli.py`; added `__init__.py`, `__main__.py`; root `continuity.py` is now a compat shim. `pyproject.toml` (setuptools, stdlib-only, zero deps). |
| 2 | console-script entry `continuity` | ✅ | `[project.scripts] continuity = "continuity_kit.cli:main"`. Also `python -m continuity_kit`. |
| 3 | template/fixture package data | ✅ | Templates bundled as package data (17 files incl. 4 `.gitkeep`). Fixtures **not** bundled (test-only, 100+ files) — decision below. |
| 4 | pipx install from source works | ✅ | `pip install .` (source) **and** built-wheel install both green into isolated venvs. |
| 5 | installed-binary smoke tests | ✅ | Local smoke test of all 10 commands + new CI `package` job (build wheel → assert bundled templates → install → run MVP commands from the binary). |
| 6 | versioning + schema-compat note | ✅ | SemVer `0.1.0`; `continuity --version` prints package version **and** record `schema_version`; pyproject carries the package-vs-record-schema note. |
| 7 | README install/distribution docs | ✅ | Install section + Status table row + cli-spec template-path note updated. |

## Decisions resolved this phase
- **Package vs keep single-file:** **Convert to a package** (`continuity_kit/`). The
  single file had grown to ~3.5k lines, and the hard "bundle templates as package
  data" criterion is clean only with a real package directory (a single-module
  distribution can't ship importable data robustly — exactly the repo-relative
  fragility the criterion warns against). To keep blast radius minimal the bulk
  moved verbatim via `git mv continuity.py → continuity_kit/cli.py` (one-line
  `TEMPLATE_DIR` change + `--version`); a thin root `continuity.py` shim re-exports
  every public/private name so `python continuity.py …` (CI/docs) and `import
  continuity` (138-test suite) keep working unchanged.
- **npx reach revisited?** **No** (unchanged default). The tool stays Python /
  `pipx`-`pip` only; an `npx` wrapper remains a separately-justified future
  decision, documented as such in the README's "No `npx` (deliberate)" note.

## Handoff
- **Packaged-data path resolution (reuse this for Phase 8/9):** package data is
  resolved **package-relative**, not repo-relative —
  `TEMPLATE_DIR = Path(__file__).resolve().parent / "templates" / "project-memory"`
  inside `continuity_kit/cli.py`. This works in a source checkout and from an
  installed wheel because pipx/pip extract package data to real files next to the
  module. MCP (Phase 8) and adapters (Phase 9) should resolve any of their own
  bundled assets the same way (or via `importlib.resources` for zip-safety), and
  declare them under `[tool.setuptools.package-data] continuity_kit = [...]` with
  explicit depth-1/depth-2 globs (avoid `**` for older-setuptools robustness;
  include dotfiles like `.gitkeep` explicitly).
- **Entry points to extend:** new surfaces add `[project.scripts]` entries (e.g. a
  future `continuity-mcp`) or `python -m continuity_kit.<module>`; the console
  script target is `continuity_kit.cli:main`.
- **Version source of truth:** package version lives in `pyproject.toml` +
  `continuity_kit/__init__.__version__` (kept in sync; `get_version()` prefers
  installed metadata, falls back to `_FALLBACK_VERSION` for source runs). The
  record `schema_version` (manifest) is independent and moves only on a breaking
  record-format change.
