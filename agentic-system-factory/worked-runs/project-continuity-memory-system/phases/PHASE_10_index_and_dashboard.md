# Phase 10 — Search/Index Acceleration & Global Dashboard

| | |
|---|---|
| **Phase** | 10 of 10 (post-MVP, last) |
| **Prerequisites** | Phase 6 (MVP-trust). Only build when exact search proves insufficient at scale (plan §18 Phase 7). |
| **Plan sections** | §14 (global dashboard), §18 Phase 7 + Phase 8, §20 task 18, §22 Q4 + Q7 |
| **Ships** | SQLite FTS (optionally vectors) as a **disposable** accelerator, plus a multi-project dashboard |
| **Session size** | Medium–large (consider splitting 10A index / 10B dashboard into two sessions) |

---

## Objective

Add the two scale features the plan deliberately saved for last: a search **index** (never source of truth) and a **global dashboard** for users juggling many projects. Both must obey the no-daemon, generated-≠-canonical, no-secret-leak principles.

> Suggested split into two sessions: **10A — Index acceleration**, **10B — Global dashboard**. They're independent.

---

## Part 10A — Search/Index acceleration (plan §18 Phase 7, §20 task 18)

### Tasks
1. **SQLite FTS** over canonical records: `build-index` command populates `index/` (always gitignored except README, per Phase 1).
2. **Index integrity rules** (§18 Phase 7):
   - index is ignored,
   - each indexed row stores source file **path + content hash**,
   - **invalidate on hash mismatch** (rebuild affected rows),
   - **never** treat a search result as source-of-truth without opening the canonical record.
3. **Wire guard/resume/search to optionally use the index** when present, falling back to the Phase 5 in-memory deterministic search when absent. Behavior must be identical, only faster.
4. **Audit integration:** index built from wrong/old commit → audit flags it (§15 threat 8, reuse Phase 6 drift logic).
5. **Vectors (only if exact search insufficient):** add an embeddings/vector index as a further disposable accelerator. Same rules: ignored, hash-tracked, never source of truth. Gate this on demonstrated need (plan §1 non-goal 1, §23 "vectors if still needed").

### 10A acceptance
- [ ] `build-index` creates an FTS index under `index/` (gitignored).
- [ ] Index rows carry source path + hash; mismatch triggers invalidation/rebuild.
- [ ] Guard/resume/search produce identical results with or without the index.
- [ ] Audit flags a stale/wrong-commit index.
- [ ] Vectors only added if justified; same disposability rules; documented rationale.

---

## Part 10B — Global multi-project dashboard (plan §14, §20 task 18)

### Tasks
6. **Global registry** `~/.continuity/registry.yml` + `dashboard-cache.json`. Projects **opt in** via `continuity register .` (nothing background-scans the filesystem — §14, §2.4).
7. Commands: `register`, `dashboard`, `recent`, `where-was-i`.
8. **Dashboard rebuild (no daemon, §14 cache freshness):** `dashboard`/`recent` re-read each registered project's `current.md` + `handoff.md` on demand and refresh the cache. Cache is a disposable projection, never source of truth.
9. Each cached row carries the source project's last-touched timestamp/commit (stale entries visible, not silently trusted); unreadable/missing project path shown as `unavailable`, not dropped.
10. Dashboard output table (§14): Project · Path · Current focus · Last touched · Next action · Stale?.
11. **Privacy (plan §22 Q4):** registry stores pointers + summaries only, **no secrets**; decide how `local-private` memory participates without leaking details (recommend: dashboard shows only `repo-safe` current/handoff fields; private content never enters the global cache). Record the decision.

### 10B acceptance
- [ ] `register .` adds a project to `~/.continuity/registry.yml` (opt-in only).
- [ ] `dashboard`/`recent`/`where-was-i` rebuild from each project's current/handoff on demand.
- [ ] Cache is disposable; rows show last-touched + `unavailable` for missing paths.
- [ ] Registry/cache hold pointers + summaries only — no secrets, no private content.
- [ ] Local-private participation policy (§22 Q4) implemented + documented.

---

## Implementation tracker

| # | Task | Status | Notes |
|---|---|---|---|
| 1 | build-index (SQLite FTS) | ☐ | 10A |
| 2 | index path+hash + invalidate-on-mismatch | ☐ | 10A |
| 3 | guard/resume/search use index w/ fallback | ☐ | 10A |
| 4 | audit flags stale/wrong-commit index | ☐ | 10A |
| 5 | vectors (only if justified) | ☐ | 10A |
| 6 | ~/.continuity registry + cache | ☐ | 10B |
| 7 | register/dashboard/recent/where-was-i | ☐ | 10B |
| 8 | on-demand cache rebuild (no daemon) | ☐ | 10B |
| 9 | last-touched + unavailable handling | ☐ | 10B |
| 10 | dashboard table output | ☐ | 10B |
| 11 | privacy/local-private policy (§22 Q4) | ☐ | 10B |
| 12 | acceptance (10A + 10B) green | ☐ | |

## Decisions resolved this phase
- _Local-private in dashboard (§22 Q4):_ _(record)_
- _`sessions/` retention/rollup (§22 Q7):_ _(does dashboard/index argue for an archival rollup command? record)_
- _Vectors added? (justification):_ _(record yes/no + why)_

## Handoff
- This is the final planned phase. Update the master tracker; record any remaining §22 questions and whether a v2 schema bump is warranted.
