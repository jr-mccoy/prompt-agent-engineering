# Phase 3 — Capture Half: `remember` & `capture session`

| | |
|---|---|
| **Phase** | 3 of 10 |
| **Prerequisites** | Phase 2 done (record engine, identity, derive/default fields, `validate`) |
| **Plan sections** | §8 (body templates), §10 (command behavior), §7 (field population / 90-second budget), §20 tasks 7–8 |
| **Ships** | The write side of the value loop: durable decision/attempt records and session capture with git pre-fill and a `--fast` tier |
| **Session size** | Medium–large |

---

## Objective

Make memory *cheap to create*. Implement the three writers that produce durable records and session capture. The hard design constraint is the **capture budget** (§2.7, §7, §23): a routine `capture session` must take **under 90 seconds** of human effort, and `--fast` must take **~15 seconds**. Everything not prompted is auto-derived or defaulted (§7 field-population table).

## Scope

**In:**
- `remember decision` → writes `decisions/YYYY-MM-DD-slug.md` from the §8 decision template.
- `remember attempt` → writes `attempts/YYYY-MM-DD-slug.md` from the §8 attempt template.
- `capture session` → writes `sessions/YYYY-MM-DD-tool-topic.md` from the §8 session template, **auto-filling** Work Completed / Files Touched / Commands from git, then updates `handoff.md` and `current.md`.
- `capture session --fast` → git-only snapshot + one-line Next Action, no prompts, no LLM.
- A record-writer that fills frontmatter via Phase 2's `derive_fields` + `default_fields` + the prompted fields, and emits a filename that yields the right `id`/`slug`.
- Slug generation from title (kebab-case, deduped against date collisions).

**Out:**
- Any LLM narrative generation is **optional and behind a flag/absent**; the MVP path is git-prefill + human edit (plan §8, §10: `--fast` "no LLM narrative"). Do not make an LLM a hard dependency.
- `resume`, `guard`, `audit` (Phases 4–6).
- `remember idea` / `remember question` are "later commands" (§10) — optional stretch if cheap, else Phase 5+.

## Tasks

### A. Record writer core (plan §7, §8)
1. `write_record(type, title, body_sections, project_root, overrides={})`:
   - Compute date (`derive_fields`), slug from title, filename `<date>-<slug>.md` in the right dir; ensure uniqueness (append `-2` etc. on same-day slug clash).
   - Assemble frontmatter: auto-derived + defaulted + prompted (`title`, optional `tags`, `evidence`); set `updated_at == created_at`.
   - Render the matching §8 body template with the user's section content.
   - Re-run identity derivation to confirm filename↔id agreement before writing.
2. After writing, run the Phase 2 `validate` logic on the new file (fail fast if it wouldn't pass).

### B. `remember decision` / `remember attempt` (plan §8, §10, §20.7)
3. Interactive flow: prompt for `title`, then the section bodies from the §8 template (Decision: Context/Options/Decision/Rationale/Consequences/What Not To Retry/Evidence/Stale conditions; Attempt: Problem/Tried/Result/Why/Do Not Retry Unless/Evidence/Related).
4. Non-interactive support: accept section content via flags or stdin/heredoc + `--json` for agent callers.
5. Defaults keep it light: only `title` + a couple of body lines are strictly required (§7 "routine remember should require only a title and a few body lines"); empty optional sections are written as template stubs, not errors — but `validate`'s evidence-or-low-confidence rule (§16.9) still applies, so prompt for evidence or set `confidence: low`.

### C. `capture session` with git pre-fill (plan §8, §10, §20.8)
6. Determine the "since last session" window: find the newest `sessions/` record's `commit` (or repo root if none).
7. Pre-fill from git (`subprocess`):
   - **Work Completed** ← `git log --oneline <since>..HEAD`
   - **Files Touched** ← `git diff --stat <since>..HEAD` (+ purpose left for human)
   - **Commands / Verification** ← optionally captured/prompted; leave a stub.
8. Prompt human only for: confirm/edit the narrative sections + **Next Action** (required, §16.10). Target: under 90 s.
9. Update `handoff.md` (§8 handoff template): refresh `Last updated`, `Branch`, `Commit`, `Current Focus`, `Next Action`, carry over blockers/decisions/attempts/traps references. Update `current.md` with the short current state.
10. Respect `session_tracking` policy from manifest: if `distillate`, still write the session file locally (it's gitignored per Phase 1) but ensure promotions to `decisions/`/`attempts/` are the committed artifacts.

### D. `--fast` tier (plan §8, §10, §12, §20.8)
11. `capture session --fast`: no prompts, no LLM. Write a minimal session record = git snapshot (log/status/diff-stat) + a single `## Next Action` taken from `--next "..."` or a one-line prompt; update handoff's timestamp/branch/commit/next-action only. Must complete in ~15 s.

### E. Tests
12. `tests/test_remember.py`: decision + attempt creation produce valid records that pass `validate`; filename/id agreement; evidence-or-low-confidence enforced.
13. `tests/test_capture.py`: in a temp git repo with a couple of commits, `capture session` pre-fills Work Completed/Files Touched from git; handoff + current updated; `--fast` writes a minimal valid record with Next Action. Test `distillate` vs `full` behavior (file written either way; gitignore differs).
14. Timing sanity check (not a hard CI gate): `--fast` path issues no interactive prompts when `--next` supplied.

## Files created / modified
- `continuity.py`: add `remember`, `capture`, `write_record`, slug + handoff/current updaters.
- `tests/test_remember.py`, `tests/test_capture.py`

## Acceptance criteria
- [x] `remember decision` / `remember attempt` create §8-shaped records that pass `validate`.
- [x] New records have correct filename-canonical `id`/`slug` and full auto/default frontmatter (rendered in §7 key order, round-trips through the Phase 2 parser).
- [x] `capture session` auto-fills Work Completed, Files Touched, Commands from git diff/log since the last session (since-window verified; falls back to last-20-commits when no prior session).
- [x] `capture session` updates `handoff.md` and `current.md` (and the refreshed handoff still passes `validate` §16.11).
- [x] A routine capture asks the human only for narrative confirmation + Next Action (interactive prompts limited to those; everything else derived/prefilled).
- [x] `capture session --fast --next "..."` writes a valid minimal record with no prompts.
- [x] `session_tracking: distillate` keeps `sessions/` local (gitignored) while promotions remain committed — verified with `git check-ignore`.
- [x] Phase 3 tests pass; no LLM is required on any path. (59 tests total: 40 Phases 1–2 + 19 Phase 3.)

## Implementation tracker

| # | Task | Status | Notes |
|---|---|---|---|
| 1 | write_record() core + frontmatter assembly | ☑ | `write_record()` + `render_frontmatter()` (§7 key order) + `render_body()` (§8); `updated_at == created_at` |
| 2 | slug generation + same-day dedupe | ☑ | `slugify()` + `_unique_record_path()` (append `-2`, `-3`, …) |
| 3 | post-write validate gate | ☑ | `_validate_new_file()`; deletes file + errors if the new record fails |
| 4 | remember decision (interactive) | ☑ | TTY prompts for title + sections + evidence |
| 5 | remember attempt (interactive) | ☑ | same flow, attempt template |
| 6 | non-interactive/flags/--json input | ☑ | `--title`/`--set HEADING TEXT`/`--evidence TYPE REF`/`--tags`/`--confidence`/…; `--json` summary |
| 7 | evidence-or-low-confidence enforcement | ☑ | enforced pre-write (§16.9): error in non-tty, offered in tty |
| 8 | capture: since-last-session window | ☑ | `_last_session_commit()` → newest session's `commit`; range `since..HEAD` |
| 9 | capture: git pre-fill (log/diff-stat) | ☑ | `_git_prefill()`; no-since falls back to last-20 + empty-tree diff base |
| 10 | capture: prompt narrative + Next Action | ☑ | only un-supplied narrative sections + required Next Action prompted |
| 11 | capture: update handoff.md + current.md | ☑ | `update_handoff()`/`update_current()` preserve carried-over sections |
| 12 | capture: honor session_tracking policy | ☑ | file always written; distillate gitignore (Phase 1) keeps it local; notice printed |
| 13 | capture --fast tier | ☑ | `--fast --next`: git snapshot + Next Action, no prompts/LLM |
| 14 | tests/test_remember.py | ☑ | 12 tests (creation, id agreement, dedupe, evidence rule, misuse) |
| 15 | tests/test_capture.py (full/distillate, fast) | ☑ | 8 tests (prefill, since-window, handoff/current, fast, tracking policy) |
| 16 | Acceptance criteria all green | ☑ | all 8 verified; 59 tests pass |

## Decisions resolved this phase
- **LLM narrative: optional / absent in MVP — confirmed.** Every path is git-prefill
  + human edit; `--fast` is explicitly no-LLM. No code path imports or requires an LLM.
- **`sessions/` retention (§22 Q7):** noted, deferred to Phase 10 (rollup). No retention
  logic added; `capture` just appends dated session records.
- **Frontmatter authored, not just derived:** records are written with the full §7
  frontmatter *including* `id`/`type`/`slug` set to their derived values (so the file
  is self-describing and `validate` confirms agreement). The renderer round-trips
  through the Phase 2 parser; `#`-leading refs (e.g. PR `#42`) are quoted.
- **Section input contract:** `--set HEADING TEXT` matches headings case-insensitively
  against the §8 list for the type; unknown headings error (exit 2). Empty sections
  render the stub `_(not recorded)_`.

## Handoff to Phase 4
**Files `resume` will read (locations confirmed):**
- `handoff.md` — rebuilt by `update_handoff()` with header lines `_Branch:`/`_Commit:`
  and sections in `HANDOFF_SECTIONS` order (Current Focus, Next Action, Blockers,
  Active Decisions To Respect, Failed Attempts To Avoid, Known Traps, Likely Relevant
  Files, Verification Commands, Stale If).
- `current.md` — rebuilt by `update_current()` with `CURRENT_SECTIONS` (Current Focus,
  Recently Changed, Watch Out For).
- Durable records via `load_records(memory_dir, types=...)`; each `Record.sections`
  splits the §8 body on `## ` headings.

**Section-splitting contract (resume depends on it):** writers always emit the full
§8 heading set per type, so `Record.sections` keys are stable. For plain-markdown
singletons, use `split_md_sections(text)` (same `## ` contract, no frontmatter).

**Reusable helpers for Phase 4:** `write_record()`, `derive_fields()`,
`default_fields()`, `load_manifest()`, `_git_prefill()`/`_last_session_commit()`
(if resume wants a git delta), `split_md_sections()`, and the
`HANDOFF_SECTIONS`/`CURRENT_SECTIONS` constants.

After Phase 4, **19a ships and dogfooding begins** — capture ergonomics feedback
should flow back here.
