# Phase 2 — Record Engine & `continuity validate`

| | |
|---|---|
| **Phase** | 2 of 10 |
| **Prerequisites** | Phase 1 done (repo, templates, manifest, `init`) |
| **Plan sections** | §7 (schema, identity, field population), §6 (taxonomy), §16 (validation rules — deterministic only), §20 tasks 5–6 |
| **Ships** | A reusable record layer (parse/load/identity) and a fully deterministic `validate` command enforcing §16.1–13 |
| **Session size** | Medium |

---

## Objective

Build the shared data layer every later command uses — frontmatter parsing, record loading, and **filename-canonical identity** — and the first quality gate, `validate`. This is pure read-side infrastructure; no records are authored here (that's Phase 3), but the engine and its tests can run against the `templates/` content and hand-built fixtures.

## Scope

**In:**
- Minimal YAML-frontmatter parser (stdlib only) supporting the schema in §7 (scalars, lists, nested `evidence` list of maps, nulls).
- A `Record` model: load a `.md` file → frontmatter dict + body; expose typed accessors.
- **Identity derivation** from filename (§7 "Record identity"): compute `id` and `slug`; flag frontmatter that disagrees.
- Manifest loader (reads `schema_version` + policies written in Phase 1).
- `continuity validate` implementing the deterministic checks §16.1–13 (+ §16.14 framing).
- Field-population helpers (auto-derive / default / prompt buckets, §7) — the **derive/default** halves, reused by Phase 3's writers.

**Out:**
- The `prompt` half of capture (interactive authoring) — Phase 3.
- Secret scan + instruction-like heuristics — those belong to `audit` (Phase 6), **not** `validate` (§16 note).
- Search/guard/resume/audit.

## Tasks

### A. Frontmatter parser (plan §18 Phase 1, §7)
1. Implement `parse_frontmatter(text) -> (meta: dict, body: str)`:
   - Split on leading `---` fences.
   - Support: `key: scalar`, `key: null`, inline empty list `[]`, block lists (`- item`), and a list-of-maps for `evidence` (`- type: commit` / `  ref: <sha>`).
   - Preserve ISO-8601 datetime strings as strings (no tz math here).
   - Be strict enough to *detect* malformed frontmatter (used by §16.3) but tolerant of field order.
2. Decide JSON-Schema-vs-convention (plan §22 Q1) **for now**: recommend Markdown-convention validation in code (deterministic checks) and defer a published JSON Schema. Record the call in this doc.

### B. Record model (plan §20.5, §6)
3. `Record` class: `path`, `meta`, `body`, `type` (from filename dir / `type-prefix`), `sections` (split body by `##` headings — reused by resume/guard).
4. `load_records(memory_dir, types=...)`: walk `decisions/`, `attempts/`, `sessions/`, `ideas/`, plus the singleton files (`current.md`, `handoff.md`, `open-questions.md`, `known-traps.md`). Return typed collections.
5. Field-population helpers (§7 table): `derive_fields(project_root)` → `{created_at, created_by, agent, project, branch, commit, dirty_files}` using system clock + git (`subprocess`) with the Phase 1 non-git sentinels; `default_fields()` → the defaulted constants. (Phase 3 adds the prompted fields.)

### C. Identity (plan §7 "Record identity")
6. From filename `<YYYY-MM-DD>-<slug>.md`: `slug` = segment after date; `id` = `<prefix>_<YYYYMMDD>_<slug>` with prefix map `decision→dec, attempt→att, idea→idea, session→ses, trap→trap, question→q`.
7. `validate` recomputes `id`/`slug` and flags frontmatter that stores a *disagreeing* value (don't trust stored id; filename wins).

### D. `validate` (plan §16, §20.6)
8. Implement checks (all deterministic; exit non-zero on failure; support `--json`):
   1. `manifest.yml` exists + supported `schema_version`.
   2. Required core files exist (`current.md`, `handoff.md`, `open-questions.md`, `known-traps.md`, `manifest.yml`).
   3. Durable records have valid frontmatter (required keys present, parse cleanly).
   4. Record IDs unique (filename-canonical makes intra-dir dupes impossible; check cross-derived collisions + id/slug/filename agreement).
   5. Status ∈ {active, superseded, stale, disputed, rejected, quarantined}.
   6. `superseded` records include non-null `superseded_by`.
   7. `privacy: local-private` records are **not** under committed/shared paths (must be under `private/`).
   8. `privacy: secret-prohibited` records **fail** validation outright.
   9. Decisions/attempts have `evidence` **or** `confidence: low`.
   10. Session records have a `## Next Action` (or explicit convergence/done marker).
   11. Handoff has branch, commit, next action, and stale conditions.
   12. Generated files not treated as canonical (presence of generated header / not required to have durable frontmatter).
   13. Adapter files (if present) don't duplicate full memory content (size/heuristic check is §6 audit; here just ensure they aren't loaded as canonical records).
9. `--json` output: list of `{check, status, path, message}`; human output: grouped pass/fail with counts.

### E. Tests / mini-fixtures
10. Hand-author small valid + invalid record fixtures under `tests/data/` (not the eval `fixtures/` yet): one good decision, one missing-evidence decision, one bad-status, one id/filename mismatch, one local-private-in-committed-path, one secret-prohibited, one superseded-without-superseded_by.
11. `tests/test_parser.py`, `tests/test_identity.py`, `tests/test_validate.py` covering each §16 check (pass and fail direction).

## Files created / modified
- `continuity.py`: add `frontmatter`, `records`, `identity`, `validate` modules/functions (single-file is fine per §18 Phase 1; keep functions cohesive).
- `tests/data/**`, `tests/test_parser.py`, `tests/test_identity.py`, `tests/test_validate.py`

## Acceptance criteria
- [x] Parser round-trips the §7 schema incl. `evidence` list-of-maps and nulls.
- [x] `id`/`slug` computed from filename; mismatching frontmatter is flagged, not trusted.
- [x] `validate` passes on a freshly `init`'d project (singleton core files are treated as non-durable; only `decisions/attempts/sessions/ideas` `*.md` are loaded as records).
- [x] `validate` fails with a clear message on each invalid fixture (one per §16 check 3–11).
- [x] `validate --json` emits structured results and a non-zero exit on failure.
- [x] `validate` performs **no** heuristic content scanning (stays deterministic, §16.14) — verified by a trap with override phrasing that does **not** fail validate.
- [x] All Phase 2 tests pass (40 total: 9 Phase 1 + 31 Phase 2).

## Implementation tracker

| # | Task | Status | Notes |
|---|---|---|---|
| 1 | frontmatter parser (scalars/lists/maps/null) | ☑ | `parse_frontmatter`; block lists of scalars + list-of-maps for `evidence`; inline `[]` |
| 2 | malformed-frontmatter detection | ☑ | `FrontmatterError` on unterminated fence + bad top-level indentation |
| 3 | Record model + section splitter | ☑ | `Record` + `.sections` (split on `## `); `Record.from_file` captures parse errors |
| 4 | load_records() over all types | ☑ | walks `decisions/attempts/sessions/ideas` `*.md`; optional `types=` filter; singletons excluded |
| 5 | derive_fields() (git + non-git sentinels) | ☑ | `git_branch/commit/dirty_files` fall back to Phase 1 `(no-git)` sentinels |
| 6 | default_fields() | ☑ | constants per §7 defaulted half |
| 7 | identity derivation (id/slug from filename) | ☑ | `derive_identity`; `TYPE_PREFIX` map; `RECORD_STEM_RE` |
| 8 | id/slug/filename agreement check | ☑ | filename wins; stored `id`/`slug`/`type` that disagree are flagged |
| 9 | manifest loader + schema_version check | ☑ | `load_manifest`; §16.1 checks supported version |
| 10 | validate checks §16.1–13 | ☑ | `run_validate` returns findings; deterministic only |
| 11 | validate --json + exit codes | ☑ | `--json`/`--plain`/human; exit 1 on fail, 2 on missing store |
| 12 | tests/data invalid fixtures | ☑ | one fixture per §16 check 3–10 + good decision/session |
| 13 | parser/identity/validate tests | ☑ | `test_parser.py`, `test_identity.py`, `test_validate.py` |
| 14 | Acceptance criteria all green | ☑ | all 7 verified; 40 tests pass |

## Decisions resolved this phase
- **Schema format (§22 Q1):** **convention-in-code now; published JSON Schema deferred.**
  The deterministic checks in `run_validate` *are* the schema. A standalone JSON
  Schema artifact is deferred until the format stabilizes during dogfood (revisit
  in Phase 6/dogfood). Documented inline in `continuity.py` above the parser.
- **Required durable-record keys (§16.3):** `title`, `status`, `created_at`, `privacy`.
  `id`/`slug` are intentionally **not** required (they are derived from the filename,
  §7). Writers in Phase 3 must always emit these four.
- **`validate` exit codes:** `0` clean, `1` problems found, `2` no `.project-memory/`.
- **Singletons are not records.** `current.md`/`handoff.md`/`open-questions.md`/
  `known-traps.md` are validated structurally (existence; handoff section presence)
  but are never loaded by `load_records` and carry no frontmatter requirement.

## Handoff to Phase 3
**Public helpers Phase 3 writers call (all in `continuity.py`):**
- `derive_fields(project_root, agent="human") -> dict` — auto-derived half:
  `created_at, updated_at, created_by, agent, project, branch, commit, dirty_files`.
  Git fields degrade to the `(no-git)` sentinels automatically.
- `default_fields() -> dict` — defaulted half: `status, confidence, privacy,
  review_status, scope, tags, supersedes, superseded_by, expires_at, reviewed_by`.
- `derive_identity(stem, rtype) -> (id, slug) | None` — compute id/slug from a
  `<YYYY-MM-DD>-<slug>` stem. Phase 3 should name files `<YYYY-MM-DD>-<slug>.md`
  and **not** author `id`/`slug` into frontmatter (or if it does, they must match —
  `validate` flags disagreement). `TYPE_PREFIX` holds the prefix map.
- `parse_frontmatter(text) -> (meta, body)` / `Record.from_file(path, rtype)` for
  read-back. `load_records(memory_dir, types=...)` to enumerate.
- `load_manifest(memory_dir) -> dict | None` for policy-aware behavior.

**Where to register the writer commands:** in `build_parser()`, same pattern as
`init`/`validate` (`sub.add_parser(..., parents=[global_parser])` +
`set_defaults(func=...)`). `remember`/`capture` (Phase 3) bolt on there.

**Frontmatter keys the parser handles loosely (stay within these):** scalars are
strings (ISO datetimes preserved verbatim — no tz coercion); `null`/`~`/empty →
`None`; `[]` and block `- item` lists → Python lists; `evidence` is the only
list-of-maps shape (`- type: …` / `  ref: …`). Inline ` # comment` is stripped
from *unquoted* scalars; quote a value (e.g. `ref: "#42"`) to keep a leading `#`.
Booleans are **not** coerced (kept as strings) for record frontmatter; the manifest
is parsed by the separate flat `load_manifest`.
