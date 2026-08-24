# Phase 1 — Foundation & `continuity init`

| | |
|---|---|
| **Phase** | 1 of 10 |
| **Prerequisites** | None (this phase creates the repo) |
| **Plan sections** | §5 (layout + tracking policy), §6 (taxonomy), §7 (manifest), §8 (templates — scaffold the empty/stub forms), §18 Phase 0 + Phase 2, §20 tasks 1–4 |
| **Ships** | A standalone repo whose `continuity.py init` produces a valid, git-policy-correct `.project-memory/` in any target project |
| **Session size** | Medium |

---

## Objective

Stand up the `continuity-kit` repository skeleton and implement the one command that everything else depends on: `init`. After this phase, a user can run `init` in any project and get a complete, correctly-tracked `.project-memory/` directory with a manifest recording the chosen policies.

## Scope

**In:**
- Create standalone repo `continuity-kit` with the layout from plan §18 Phase 0.
- Author `docs/` (architecture, record-schema, cli-spec, mcp-spec, security) — initial versions, distilled from the plan.
- Author `templates/project-memory/` — the full file tree from §5 with template content.
- Implement `continuity.py init` including manifest creation, `.gitignore` rule writing, and the session-tracking / generated-projection policy choices.
- Decide and document the **non-git fallback** for git-derived fields (plan §22 open Q5) — this decision is consumed by all later phases.
- Establish the CLI entry skeleton (`argparse`) with the global flags (`--json`, `--plain`, `--verbose`, `--project`) so later phases bolt on subcommands.

**Out (later phases):**
- Frontmatter parsing / record loading / `validate` (Phase 2).
- Writing actual records / sessions (Phase 3).
- `resume`, `guard`, `audit` (Phases 4–6).

## Tasks

### A. Repo scaffold (plan §18 Phase 0, §20.1)
1. Create repo `continuity-kit` with:
   ```text
   continuity-kit/
     README.md            # product definition (§1 north-star) + non-goals (§2) + quickstart
     LICENSE
     continuity.py        # single-file CLI entry (Phase 1: argparse skeleton + init)
     docs/
       architecture.md
       record-schema.md
       cli-spec.md
       mcp-spec.md
       security.md
     templates/
       project-memory/    # the full §5 tree as templates
     fixtures/            # empty dir w/ README (populated Phases 4–6)
     tests/               # test harness skeleton
     .gitignore
   ```
2. `README.md`: copy the north-star statement (§1), working name (§1), non-goals (§2), and a 4-line quickstart (`init` → `remember` → `capture` → `resume`). Mark unbuilt commands as "(planned)".

### B. Docs (plan §20.3)
3. `docs/architecture.md`: principles (§3), source-of-truth rules (§9), record taxonomy (§6), build philosophy (§23).
4. `docs/record-schema.md`: canonical frontmatter (§7), record identity (filename-canonical), field population table, status/privacy meanings, body templates (§8).
5. `docs/cli-spec.md`: command table (§10) with MVP vs later split, global flags, `--fast` semantics.
6. `docs/mcp-spec.md`: stub — list MCP resources/prompts/tools from §13 marked "Phase 8".
7. `docs/security.md`: threat surfaces + required controls (§15), validation posture (§16), privacy labels (§7).

### C. Templates (plan §5, §8, §20.2)
8. Build `templates/project-memory/` mirroring §5 exactly:
   - `README.md` (explains the directory to humans/agents; mirrors the AGENTS.md protocol idea from §13 but project-local).
   - `manifest.yml` template with `<placeholder>` tokens (§7 manifest).
   - `current.md`, `handoff.md` (use §8 handoff template), `open-questions.md`, `known-traps.md`.
   - `decisions/.gitkeep`, `attempts/.gitkeep`, `sessions/.gitkeep`, `ideas/.gitkeep`.
   - `evidence/refs.yml` (empty list scaffold).
   - `generated/README.md` (explains projections are not source of truth), plus placeholder `resume-packet.md`, `stale-report.md`, `memory-index.md`.
   - `private/README.md` (explains local-only policy), `index/README.md` (explains disposable index).
9. Keep `<angle-bracket>` tokens as placeholders (plan §7: never emit literals like `abc1234`).

### D. `continuity init` (plan §5, §7, §10, §20.4)
10. CLI skeleton in `continuity.py`: `argparse` with subcommand dispatch; global flags `--json --plain --verbose --project <path>`. Resolve project root (default cwd; `--project` overrides).
11. `init` behavior:
    - Refuse to clobber an existing `.project-memory/` unless `--force`; otherwise copy the template tree in.
    - Auto-derive `project` (repo/dir name), `created_at` (ISO-8601 with tz), `schema_version: 1`.
    - **Session-tracking policy**: prompt, or accept `--session-tracking <full|distillate>` (default prompt → `full` for non-interactive). Record in `manifest.yml`.
    - **Generated-projection policy**: default `commit_generated_projections: true`; accept `--no-commit-generated`. Record in `manifest.yml`.
    - Write `.gitignore` rules to match the policies (plan §5 git-tracking policy + §5 "Tracking policy chosen at init"). Indexes (`index/**`) always ignored except `index/README.md`. `private/**` always ignored.
    - Honor `--json` (emit a machine summary of what was created + chosen policies).
12. **Non-git fallback decision (plan §22 open Q5):** detect whether the project is a git repo. If not, set git-derived fields (`branch`, `commit`, `dirty_files`) to a defined sentinel — **recommend** `branch: "(no-git)"`, `commit: "(no-git)"`, `dirty_files: []` — and have `init` print a notice. Document this in `docs/record-schema.md` so Phases 3–6 use the same sentinels.

### E. Tests
13. `tests/test_init.py`: running `init` on a temp dir creates the full §5 tree, a manifest with both policies set, and `.gitignore` rules matching the policy. Test both `full` and `distillate`, both git and non-git temp projects.

## Files created
- `continuity.py` (skeleton + `init`)
- `README.md`, `LICENSE`, `.gitignore`
- `docs/{architecture,record-schema,cli-spec,mcp-spec,security}.md`
- `templates/project-memory/**` (full tree)
- `tests/test_init.py`, `fixtures/README.md`

## Acceptance criteria
- [x] `python continuity.py init` in an empty git repo produces the exact §5 tree.
- [x] `manifest.yml` records `schema_version`, `project`, `created_at`, `session_tracking`, `commit_generated_projections`.
- [x] `.gitignore` correctly ignores `private/**`, `index/**` (except README), and (only when `--no-commit-generated`) `generated/*.md`; honors `distillate` by ignoring `sessions/`. _(verified with `git check-ignore`.)_
- [x] `--session-tracking distillate` and `--no-commit-generated` flow through to manifest + gitignore.
- [x] Running on a non-git folder succeeds, prints a notice, and uses the documented sentinels.
- [x] `init` is idempotent-safe (refuses to overwrite without `--force`; managed `.gitignore` block is rewritten, not duplicated).
- [x] `tests/test_init.py` passes (9 tests, full/distillate × git/non-git).

> **Build location note:** per explicit user direction this phase was built as a
> standalone kit at the repo root: **`continuity-kit/`** inside `Prompting-guides`
> (rather than a separate `jr-mccoy/continuity-kit` repo). The kit is fully
> self-contained — `Prompting-guides`' own `.gitignore` ignores `.project-memory/`
> and no real memory store is installed into `Prompting-guides`.

## Implementation tracker

| # | Task | Status | Notes |
|---|---|---|---|
| 1 | Create repo scaffold + dir tree | ☑ | built at `continuity-kit/` (repo root, per user direction) |
| 2 | README (north-star, non-goals, quickstart) | ☑ | unbuilt cmds marked "(planned)" |
| 3 | docs/architecture.md | ☑ | principles, SoT rules, taxonomy, build philosophy |
| 4 | docs/record-schema.md (incl. non-git sentinels) | ☑ | §7 documents `(no-git)` sentinels |
| 5 | docs/cli-spec.md | ☑ | command table + MVP/later split + `--fast` |
| 6 | docs/mcp-spec.md (stub) | ☑ | resources/prompts/tools marked Phase 8 |
| 7 | docs/security.md | ☑ | threat surfaces, deterministic-validate posture, privacy labels |
| 8 | templates/project-memory/** full tree | ☑ | mirrors §5 exactly; angle-bracket placeholders only |
| 9 | argparse skeleton + global flags + project-root resolution | ☑ | parent-parser pattern; `--json/--plain/--verbose/--project` |
| 10 | `init`: template copy + clobber guard | ☑ | refuses without `--force` |
| 11 | `init`: manifest write (both policies) | ☑ | overwrites copied template with computed values |
| 12 | `init`: .gitignore policy writer | ☑ | idempotent managed block; verified w/ `git check-ignore` |
| 13 | `init`: session-tracking prompt/flag | ☑ | flag, else prompt; non-tty default `full` |
| 14 | non-git fallback decision + notice | ☑ | sentinels documented + notice printed |
| 15 | tests/test_init.py (full/distillate × git/non-git) | ☑ | 9 tests passing |
| 16 | Acceptance criteria all green | ☑ | all 7 verified |

## Decisions resolved this phase
- **Non-git fallback sentinels (§22 Q5):** `branch: "(no-git)"`, `commit: "(no-git)"`,
  `dirty_files: []`. Defined in `continuity.py` (`NO_GIT_BRANCH` / `NO_GIT_COMMIT`)
  and documented in `docs/record-schema.md` §7. Phases 3–6 must consume these exact
  values; records carrying them must **not** be flagged as branch mismatches, and
  commit-distance staleness degrades to age-only when present.
- **Generated-projection default:** committed (`true`) per §5.
- **`.gitignore` integration:** init writes a single delimited "managed block" into
  the *project root* `.gitignore` (markers `continuity.GITIGNORE_BEGIN/END`),
  preserving any pre-existing user content and rewriting only the block on re-init.
- **Build location:** standalone kit at `continuity-kit/` in the repo root (per user
  direction), not a separate GitHub repo. Templates are resolved relative to
  `continuity.py` via `TEMPLATE_DIR = <script dir>/templates/project-memory`.

## Handoff to Phase 2
- **Where to register `validate`:** in `continuity.py::build_parser()`. A `global_parser`
  (parent) carries the four global flags; each subcommand is added via
  `sub.add_parser(..., parents=[global_parser])` and wired with `set_defaults(func=...)`.
  Add `validate` the same way `init` is added; `main()` already dispatches `args.func`.
- **Where the manifest is read:** Phase 1 only *writes* it. Constants for Phase 2:
  `continuity.SCHEMA_VERSION` (== 1), `continuity.MEMORY_DIRNAME` (== `.project-memory`).
  `validate` should read `<root>/.project-memory/manifest.yml` and check
  `schema_version` against `SCHEMA_VERSION`. The manifest is flat `key: value` YAML
  (with `#` comments) — a minimal parser suffices (see `tests/test_init.py::parse_manifest`
  for a working reference) until the Phase 2 frontmatter parser lands.
- **Deviation from the §5 template tree:** none. The tree matches §5 exactly
  (verified: 17 files incl. the four `.gitkeep`s and `index/README.md`).
- **Reusable helpers available to Phase 2:** `now_iso()`, `is_git_repo(root)`,
  `resolve_root(arg)`, `derive_project_name(root)`.
