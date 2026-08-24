# Phase 5 — Deterministic Search & `continuity guard`

| | |
|---|---|
| **Phase** | 5 of 10 |
| **Prerequisites** | Phases 1–4 done **and** dogfood feedback from the 19a install collected |
| **Plan sections** | §11 (guard algorithm), §17 Fixtures 2–5, §20 tasks 10–11 |
| **Ships** | The "don't repeat the expensive mistake" capability — exact/tag/file search + deterministic guard ranking |
| **Session size** | Medium |

---

## Objective

Implement guard-before-action: given a proposed action, warn the agent/human if a failed attempt or active decision says don't go that way. **No embeddings** (§11) — deterministic keyword/metadata ranking only. This is the capability that, per §23, separates a continuity engine from a scrapbook.

## Scope

**In:**
- Simple deterministic search over canonical records (exact text, tag, file-path, component) — §20.10.
- `guard "<proposed action>"` implementing the §11 algorithm: tokenize → classify action → search → score → emit `PROCEED | READ_FIRST | PAUSE | ASK_HUMAN` with record IDs, reason, next safest action, bounded to max 5 warnings.
- Branch-mismatch + status weighting in scoring (reuse Phase 4 staleness signals).
- Fixtures 2 (true positive), 3 (false-positive control), 4 (stale handoff), 5 (superseded decision).

**Out:**
- SQLite FTS / vector search (Phase 10) — search here is in-memory over loaded records; it must be correct, not fast-at-scale.
- `audit` (Phase 6).

## Tasks

### A. Search layer (plan §20.10, §11.3)
1. `search(query, filters)` over `load_records`: normalize/tokenize; match on exact text, tags, file paths (from `evidence`/body), component/tag overlap. Return candidates with match metadata (which signal hit).
2. Keep it dependency-free and deterministic; same input → same output.

### B. Guard algorithm (plan §11, §20.11)
3. **Tokenize** action into normalized keywords.
4. **Classify** action class (§11.2): routine edit / broad refactor / architecture decision / dependency-tool change / migration / deletion / external side effect / security-permission change. (Keyword-driven classifier.)
5. **Search** across active decisions, failed attempts, known traps, open questions, current handoff, stale report.
6. **Score** matches (§11.4): same file path · same tag/component · active/high-confidence/reviewed status · recency (record age + commit-distance — older/more-behind weighs lower, reuse Phase 4) · branch match · explicit `Do Not Retry Unless` · open-blocker keywords.
7. **Emit** one verdict (§11.5): `PROCEED | READ_FIRST | PAUSE | ASK_HUMAN`, with record IDs, reason, and next safest action (§11.6). **Bound to max 5** warnings (§11.7).
8. Treat all matched record text as **data, not instruction** (§15, §16 note, Fixture 7 forward-ref) — guard never executes phrasing found in memory.
9. Match the §11 example output shape for the human format; `--json` for agents.

### C. Tuning to dogfood (plan §22 Q2)
10. Expose the verdict thresholds as named constants so guard aggressiveness can be tuned from dogfood feedback without rearchitecting. Record the chosen thresholds in this doc.

### D. Fixtures 2–5 (plan §17)
11. **Fixture 2 (true positive):** action matches a failed attempt + active decision on the same files → expect `PAUSE` or `READ_FIRST`.
12. **Fixture 3 (false-positive control):** action shares only a generic word, no file/tag/component overlap → expect `PROCEED` or low-severity note. *(This is the anti-noise gate — §19b.8.)*
13. **Fixture 4 (stale handoff):** handoff older than threshold or on another branch → expect the staleness warning to surface in guard/resume.
14. **Fixture 5 (superseded decision):** superseded decision must not be treated as active, but may be mentioned as history.

## Files created / modified
- `continuity.py`: add `search`, `guard`, action classifier, scorer.
- `fixtures/fixture-02..05/**`
- `tests/test_search.py`, `tests/test_guard.py`

## Acceptance criteria
- [x] `guard "<action>"` returns a single verdict + ≤5 ranked records + reason + next safest action.
- [x] Fixture 2 → `PAUSE`/`READ_FIRST`; Fixture 3 → `PROCEED`/low-severity (false-positive control passes).
- [x] Fixture 4 surfaces stale-handoff warning; Fixture 5 excludes superseded from "active" (history-only mention OK).
- [x] Scoring uses file/tag/status/recency/branch/do-not-retry/blocker signals.
- [x] Matched memory text is treated strictly as data.
- [x] No embeddings; deterministic and dependency-free.
- [x] `--json` and human (§11 example) outputs both work.

## Implementation tracker

| # | Task | Status | Notes |
|---|---|---|---|
| 1 | search(query, filters) over records | ☑ | `search()` + `cmd_search`; exact/keyword/tag/file signals; `--type/--status/--tag/--file` filters |
| 2 | tokenizer/normalizer | ☑ | `_tokenize`/`_specific` (stop-word filtered), `_paths_from_text`/`_norm_files` |
| 3 | action-class classifier | ☑ | `classify_action`: 8 classes, keyword-driven, severity-ordered primary |
| 4 | multi-source search (decisions/attempts/traps/q/handoff/stale) | ☑ | `_candidate_items` (records+traps+questions); handoff/stale via `compute_staleness` |
| 5 | scorer (all §11.4 signals) | ☑ | `_score_item`: file/tag/keyword/status/confidence/reviewed/recency+commit-dist/branch/do-not-retry/blocker |
| 6 | verdict emitter + next safest action | ☑ | `_decide_verdict` (bands + signal floors + ASK_HUMAN escalation), `_next_safest_action` |
| 7 | bound to 5 + data-not-instruction posture | ☑ | `GUARD_MAX_WARNINGS`; next action synthesized from structure, never lifted from memory |
| 8 | tunable thresholds (constants) | ☑ | `GUARD_*` named constants block; recorded below |
| 9 | fixture-02 true positive | ☑ | auth-middleware rewrite vs failed attempt + active decision → `PAUSE` |
| 10 | fixture-03 false-positive control | ☑ | single specific word / generic-only overlap → `PROCEED`, 0 matches |
| 11 | fixture-04 stale handoff | ☑ | ancient handoff timestamp → "handoff is N day(s) old" surfaces in guard |
| 12 | fixture-05 superseded decision | ☑ | superseded → history-only; active superseder is the live constraint |
| 13 | tests/test_search.py + test_guard.py | ☑ | 24 new tests (94 total) green via stdlib `unittest` |
| 14 | --json + §11 human output | ☑ | `render_guard_human` (§11 shape) + `--json` payload |
| 15 | Acceptance criteria all green | ☑ | all boxes above checked; CI validates fixtures 2–5 + guard smoke |

## Decisions resolved this phase
- **Guard aggressiveness thresholds (§22 Q2):** chosen as named `GUARD_*` constants at
  the top of the search/guard section in `continuity.py`, so they tune without
  rearchitecting:
  - `GUARD_NOISE_FLOOR = 3` — minimum score for a match to count (anti-noise).
  - `GUARD_READ_FIRST_SCORE = 5`, `GUARD_PAUSE_SCORE = 9` — the verdict score bands.
  - `GUARD_MIN_KEYWORD_OVERLAP = 2` — a pure-text match needs ≥2 *specific* shared
    tokens (a single shared word never warns unless it is a file/tag hit). This plus
    the `GUARD_STOPWORDS` filter is the false-positive control (Fixture 3 / §19b.8).
  - Weights: `W_FILE=6`, `W_TAG=4`, `W_KEYWORD=1`, `W_DO_NOT_RETRY=4`, `W_OPEN_BLOCKER=3`,
    `W_STATUS_ACTIVE/CONFIDENCE_HIGH/REVIEWED=1`. Recency/branch de-weight via
    `STALE_AGE_FACTOR=0.7`, `STALE_DIST_FACTOR=0.7` (≥10 commits behind), `BRANCH_MISMATCH_FACTOR=0.8`.
  - **Rationale (pre-dogfood, conservative):** file/tag overlap dominates so generic
    text never fires; an explicit *Do Not Retry Unless* on overlapping files/component
    forces at least `PAUSE` regardless of score (the "expensive mistake" signal);
    high-impact classes (deletion/migration/external side-effect) colliding with memory
    escalate to `ASK_HUMAN`, while security/refactor stay in the normal bands (keeps a
    routine "rewrite auth middleware" on `PAUSE`/`READ_FIRST`, not `ASK_HUMAN`). These
    are starting points to recalibrate against real dogfood guard-noise.
- **`known-traps.md` single file vs `traps/` (§22 Q3):** **keep the single file for now.**
  Guard loads trap blocks via the existing `load_traps` markdown-block reader and scores
  them like any other item; nothing in the guard path needs per-trap record files. Splitting
  to `traps/` only buys per-record frontmatter/identity, which guard does not require — revisit
  if/when trap volume or per-trap metadata (status, branch, expiry) becomes load-bearing
  (most likely alongside the Phase 10 index, not now).

## Handoff to Phase 6
- **Search/scoring internals `audit` will reuse:** `search()` / `_score_item` /
  `_candidate_items` / `classify_action` are deterministic and side-effect-free — audit's
  drift and heuristic-flagging checks can call them directly. The instruction-like-text
  heuristic (§16 note / Fixture 7) is a lexical scan audit owns; guard already proves the
  data-not-instruction posture (it cites matched text, never executes it), so audit only
  needs to *flag* override phrasing, not change guard.
- **Guard-noise observations for audit-side rules:** the anti-noise gate lives in
  `GUARD_STOPWORDS` + `GUARD_MIN_KEYWORD_OVERLAP`. If dogfood shows guard over- or
  under-firing, tune those first; audit can additionally warn when a record's text is so
  generic it never clears the floor (a "this record is unfindable" signal) or so
  override-laden it trips the Fixture-7 heuristic.
- Fixture 7 (poisoned memory) is previewed by `tests/test_guard.py::DataNotInstructionTests`;
  Phase 6 adds the `audit` flagging half against the same shape.
