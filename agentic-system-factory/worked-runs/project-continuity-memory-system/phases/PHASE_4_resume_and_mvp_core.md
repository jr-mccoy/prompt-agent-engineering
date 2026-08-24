# Phase 4 — `continuity resume` & MVP-Core (19a) 🚩

| | |
|---|---|
| **Phase** | 4 of 10 |
| **Prerequisites** | Phases 1–3 done (init, record engine + validate, capture/remember) |
| **Plan sections** | §12 (resume packet), §19a (MVP-core acceptance), §17 Fixture 1, §20 task 9 |
| **Ships** | 🚩 **MVP-core (19a)** — the complete capture→resume value loop. After this phase the tool is worth installing; **dogfooding starts.** |
| **Session size** | Medium |

---

## Objective

Close the loop: turn captured memory into a **bounded, paste-anywhere resume packet** that tells a human or agent what's going on and what to do next, with **computed** staleness warnings (not just authored ones). This is the phase that makes 19a real and triggers dogfooding.

## Scope

**In:**
- `continuity resume` → generates `generated/resume-packet.md` and prints it.
- Bounded packet (3k–5k tokens, §12) with all required sections.
- **Computed staleness** (§12, §15): handoff/current age + commit-distance; aged-unresolved open questions & active decisions; branch mismatch; expired (`expires_at`) and low-confidence records.
- `resume --fast` → git snapshot + current focus + next action + staleness only (§12).
- Source-header stamping on the generated packet (commit/hash/timestamp, §3, §15).
- Plain-file fallback verification (the cloud-agent story, §4, §19a.7, Fixture 9 preview).
- **Fixture 1** (fresh resume) wired into CI (§17, §19a.6).

**Out:**
- `guard` ranking (Phase 5) — resume prioritizes but does not match a proposed action.
- `audit` drift detection (Phase 6) — resume *stamps* source info; audit later *flags* drift.

## Tasks

### A. Resume packet assembly (plan §12, §20.9)
1. Gather inputs: `current.md`, `handoff.md`, active `decisions/`, instructive `attempts/`, `known-traps.md`, `open-questions.md`, git state.
2. Render the §12 packet sections: Project · Current Focus · Next Action · Active Decisions (id + 1-line rationale) · Failed Attempts To Avoid (id + do-not-retry) · Known Traps · Open Questions/Blockers · Likely Relevant Files · Verification Commands · Stale/Risk Warnings.
3. **Prioritization for bounding** (§12, Fixture 10 forward-ref): current/handoff/active-decisions rank above old session observations; cap each section; enforce overall 3k–5k token budget (approximate tokens via a cheap heuristic, e.g. chars/4). Never include raw transcripts.
4. Stamp a source header: generating commit, short hash of inputs, timestamp (§3, §15) so audit/Phase 6 can detect drift.

### B. Computed staleness (plan §12, §15, §20.9)
5. **Age + commit-distance** of `handoff.md`/`current.md`: compare `updated_at`/`commit` vs now/HEAD; emit e.g. "handoff is 6 days old, written 14 commits behind current HEAD." This is the primary "train of thought went cold" signal.
6. **Aged-unresolved** scan: open questions and active decisions older than a staleness threshold (configurable; default e.g. 21 days) with no update since → flag ("is this still true / did I ever fix this?").
7. **Branch mismatch** (§15 definition): record `branch` ≠ current HEAD branch (incl. detached HEAD, since-merged branch) → surface as possibly-stale, not hidden.
8. **Expired / low-confidence**: `expires_at` in the past; `confidence: low` records get a caveat.

### C. `--fast` and output modes
9. `resume --fast`: only git snapshot + Current Focus + Next Action + computed staleness warnings.
10. `--json` emits the structured packet (sections + warnings list) for agent ingestion; default is Markdown.

### D. Plain-file fallback (plan §4, §19a.7)
11. Verify the cloud-agent path: with the CLI unavailable, the committed `generated/resume-packet.md` (policy `commit_generated_projections: true`) + the plain files under `.project-memory/` support manual resume. Document this in `README.md`/`docs`.

### E. Fixture 1 + CI (plan §17, §19a.6)
12. Build `fixtures/fixture-01-fresh-resume/` — a sample `.project-memory/` with a project, active decision, failed attempt, open question, handoff/next-action.
13. Test: `resume` against fixture 1 answers all six questions (§17 Fixture 1): what is the project / what's active / what was decided / what failed before / what's next / what not to retry.
14. Wire fixtures into CI (GitHub Actions or chosen CI): run `validate` + Fixture 1 on push. (Fixtures 2–10 added Phase 6.)

## Files created / modified
- `continuity.py`: add `resume`, packet assembly, staleness computations, token-bounding.
- `fixtures/fixture-01-fresh-resume/**`
- `tests/test_resume.py`
- CI config (`.github/workflows/ci.yml` or equivalent) running `validate` + Fixture 1.

## Acceptance criteria (this is 19a — verify the whole list, §19a)
- [x] `init` (Ph1), `remember decision`/`attempt` (Ph3), `capture session` incl. `--fast` (Ph3) all work end-to-end.
- [x] `resume` prints a bounded packet with: current focus, next action, active decisions, failed attempts, questions, traps, branch/commit, verification commands, **and computed staleness warnings** (age+commit-distance, aged-unresolved).
- [x] Packet stays within 3k–5k tokens even with many records (prioritization works). — per-section caps + 5k-token trim; `TokenBoundTests` synthesizes 40 decisions and asserts `approx_tokens <= 5000`.
- [x] `resume --fast` prints the reduced reorientation view (print-only; does not overwrite the committed packet).
- [x] Packet carries a source commit/hash/timestamp header (`source_commit` / `inputs_hash` / `generated_at`, under the `GENERATED PROJECTION` marker).
- [x] **Fixture 1 runs in CI** and answers all six questions (`.github/workflows/ci.yml`).
- [x] **Plain-file fallback works without the CLI** (committed `generated/resume-packet.md` + plain files; `CloudFallbackTests`, README "Plain-file fallback").
- [x] No raw transcripts in output (`FixtureSixQuestionsTests.test_no_raw_transcripts`).

## Implementation tracker

| # | Task | Status | Notes |
|---|---|---|---|
| 1 | gather resume inputs | ☑ | `build_resume_packet` reads current/handoff/active decisions+attempts/traps/questions/git via reusable accessors |
| 2 | render §12 packet sections | ☑ | `render_packet_markdown` — all 10 §12 sections |
| 3 | prioritization + token bounding | ☑ | `SECTION_CAPS` + `TRIM_ORDER` + 5k `TOKEN_BUDGET_MAX`; `_bound_packet` |
| 4 | source-header stamping | ☑ | `source_commit` / `inputs_hash` (sha256[:12]) / `generated_at`; keeps `GENERATED PROJECTION` marker |
| 5 | staleness: age + commit-distance | ☑ | `compute_staleness` + `git_commit_distance`; "⚠" when age>threshold or dist≥10 |
| 6 | staleness: aged-unresolved scan | ☑ | active decisions + open questions older than `--stale-days` (default 21) |
| 7 | staleness: branch mismatch | ☑ | handoff + record branch ≠ HEAD; detached-HEAD note |
| 8 | staleness: expired/low-confidence | ☑ | past `expires_at` + `confidence: low` caveats |
| 9 | resume --fast | ☑ | reduced view; print-only (won't clobber committed packet) |
| 10 | --json structured packet | ☑ | full structured dict incl. `warnings`, `omitted`, `approx_tokens` |
| 11 | plain-file fallback verified + documented | ☑ | `CloudFallbackTests`; README "Plain-file fallback"; cli-spec |
| 12 | fixture-01-fresh-resume | ☑ | committed; 13/13 validate checks pass |
| 13 | tests/test_resume.py (six questions) | ☑ | 11 tests, full suite 70 pass |
| 14 | CI: validate + Fixture 1 | ☑ | `.github/workflows/ci.yml` (unittest + validate + resume six-question assert) |
| 15 | **19a acceptance list all green** | ☑ | all 8 criteria checked above |

## Decisions resolved this phase
- **Staleness thresholds (age days / commit-distance):** aged-unresolved default = **21 days**, exposed as `--stale-days N`. The handoff age/commit-distance line is emphasized (`⚠`) when handoff age > the threshold **or** commit-distance ≥ **10**. Commit-distance has no fixed alarm of its own — it is reported whenever computable and degrades silently when the recorded commit is unknown to the checkout (e.g. rebased) or git is absent.
- **Token-bounding heuristic:** approximate tokens as **chars/4** (`approx_tokens`, rounded up). Hard ceiling **5,000 tokens** (`TOKEN_BUDGET_MAX`). Bounding is two-stage: per-section caps (`SECTION_CAPS`) cut item counts first, then the packet is trimmed lowest-priority-section-first (`TRIM_ORDER`: verification → files → questions → traps → attempts → decisions) until it fits. Project / Current Focus / Next Action / Stale warnings are never trimmed. Omissions are surfaced inline (`_(… N more omitted …)_`) — never silently dropped.
- **`--fast` write policy:** `--fast` is **print-only** and does not write `generated/resume-packet.md`, so the committed cloud-fallback artifact always reflects the full packet rather than a reduced one.

## 🚩 Gate: 19a ships → DOGFOOD
After this phase, **install in 2–3 real projects where context is actually lost** (plan §18 Phase 3 — **not** `Prompting-guides`). Collect friction on: capture time, resume usefulness, branch-mismatch handling, staleness quality. Feed findings into §22 open questions and the Phase 5/6 docs **before** building the trust toolchain.

## Handoff to Phase 5
- **Reusable section/record accessors guard will rank against** (all deterministic, side-effect-free, in `continuity.py`):
  - `active_decisions(memory_dir)` / `active_attempts(memory_dir)` — parseable records with `status: active`, newest-first (`active_records` + `_by_recency`).
  - `load_traps(memory_dir)` — `## trap_*` blocks from `known-traps.md` (HTML-comment template examples stripped via `_strip_html_comments`).
  - `load_open_questions(memory_dir)` — `## Q:` blocks → `{question, opened, status, body}`.
  - `parse_handoff_meta(text)` — branch / commit / updated_at from the handoff header; `split_md_sections` for handoff/current bodies.
  - One-line extractors guard can reuse for match context: `_decision_rationale`, `_attempt_do_not_retry`, `_evidence_refs`, `_first_line`.
  - Staleness surface guard should also emit: `compute_staleness(...)`, `git_commit_distance(...)`, `_age_days(...)`.
- Record dogfood findings that should shape guard aggressiveness (§22 Q2): _______
