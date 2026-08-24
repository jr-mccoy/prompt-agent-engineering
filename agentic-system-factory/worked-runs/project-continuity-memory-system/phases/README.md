# Continuity-Kit — Phased Build Plan & Master Tracker

> **What this is.** The [`IMPLEMENTATION_PLAN.md`](../IMPLEMENTATION_PLAN.md) one directory up is the authoritative product/architecture spec for the Project Continuity Memory System (`continuity-kit`). This folder breaks that single spec into **session-sized build phases**, each with its own plan document and an implementation tracker, so the work can be executed across many separate agent/human sessions without losing the thread.
>
> Read the plan first; these phase docs reference it by section (e.g. "§11") rather than duplicating it.

---

## 0. Critical framing (read before any phase)

- **Build target is a separate repo.** Per plan §5 and §18 Phase 0, the deliverable is a new standalone repository — recommended `jr-mccoy/continuity-kit`. These phase documents live inside `Prompting-guides` only because `Prompting-guides` is the design forge (plan §1). **Do not build the tool inside `Prompting-guides`, and do not install `.project-memory/` into `Prompting-guides` as a real store.** (Plan §1, §18 Phase 3: "Do not start with `Prompting-guides` as the target.")
- **Language is decided: Python end-to-end** (plan §18 Phase 4, §22 resolved). Prototype → CLI → MCP are all Python. No TypeScript rewrite fork.
- **Stdlib-first.** Phases 1–6 should use only the Python standard library if feasible (`argparse`, `pathlib`, `datetime`, `json`, `re`, `subprocess`). YAML frontmatter is parsed by a small vendored subset parser, not a dependency, unless a dependency is explicitly justified (plan §18 Phase 1).
- **Build order is load-bearing** (plan §23): plain files → deterministic CLI → validation/audit → guard → fixtures/evals → dogfood → packaging → MCP → hooks → search/index → vectors. The phases below follow this order. Do not pull a later phase forward.
- **Two ship gates inside the MVP** (plan §19): **19a MVP-core** (capture→resume value loop) ships and dogfoods *before* **19b MVP-trust** (guard/audit/validate) is built.

---

## 1. Phase map

| Phase | Document | Delivers | Plan refs | Ship gate |
|---|---|---|---|---|
| **1** | [PHASE_1_foundation_and_init.md](PHASE_1_foundation_and_init.md) | Repo scaffold, docs, templates, manifest, `continuity init` | §5, §7 (manifest), §18 Ph0/Ph2, §20.1–4 | — |
| **2** | [PHASE_2_record_engine_and_validate.md](PHASE_2_record_engine_and_validate.md) | Frontmatter parser, record model, filename-canonical identity, `validate` | §7, §16, §20.5–6 | — |
| **3** | [PHASE_3_capture_remember_and_session.md](PHASE_3_capture_remember_and_session.md) | `remember decision`, `remember attempt`, `capture session` (git prefill + `--fast`) | §8, §10, §20.7–8 | — |
| **4** | [PHASE_4_resume_and_mvp_core.md](PHASE_4_resume_and_mvp_core.md) | `resume` bounded packet, computed staleness, Fixture 1, plain-file fallback | §12, §19a, §20.9 | **🚩 19a MVP-core → DOGFOOD** |
| **5** | [PHASE_5_search_and_guard.md](PHASE_5_search_and_guard.md) | Deterministic search, `guard` ranking, Fixtures 2–5 | §11, §20.10–11 | — |
| **6** | [PHASE_6_audit_fixtures_and_mvp_trust.md](PHASE_6_audit_fixtures_and_mvp_trust.md) | `audit` (incl. secret + instruction-like heuristics), Fixtures 6–10, CI | §15, §16, §17, §19b, §20.12–13 | **🚩 19b MVP-trust** |
| **—** | *(dogfood — not a coding session)* | Install in 2–3 real projects; collect friction | §18 Ph3, §22 open Qs | gate to Ph7+ |
| **7** | [PHASE_7_packaging.md](PHASE_7_packaging.md) | `pipx`-installable package, `continuity` entry point | §18 Ph4, §20.15 | post-dogfood |
| **8** | [PHASE_8_mcp_server.md](PHASE_8_mcp_server.md) | Python MCP server: resources, prompts, tools | §13 (MCP), §18 Ph5, §20.16 | post-dogfood |
| **9** | [PHASE_9_hooks_and_adapters.md](PHASE_9_hooks_and_adapters.md) | Agent signposts (AGENTS/CLAUDE/Cursor/Gemini), `.mcp.json`, hook templates | §13, §18 Ph6, §20.17 | post-dogfood |
| **10** | [PHASE_10_index_and_dashboard.md](PHASE_10_index_and_dashboard.md) | SQLite FTS (+ optional vectors), global multi-project dashboard | §14, §18 Ph7/Ph8, §20.18 | post-dogfood |

---

## 2. Dependency graph

```text
        Phase 1  (foundation + init)
            │
        Phase 2  (record engine + validate)
            │
        Phase 3  (remember + capture)
            │
        Phase 4  (resume)  ── 🚩 19a ships ──►  DOGFOOD (2–3 real projects)
            │                                        │
        Phase 5  (search + guard)                    │  friction feedback
            │                                        │  informs §22 open Qs
        Phase 6  (audit + fixtures)  ── 🚩 19b ──────┘
            │
   ┌────────┼─────────────┬──────────────┐
Phase 7   Phase 8      Phase 9        Phase 10
(package) (MCP)      (hooks/adapt.)  (index/dashboard)
   └─ Phases 7–10 are independent of each other but all depend on 6 + dogfood feedback.
```

Phases **1→6 are strictly sequential** (each builds on the prior). Phases **7–10 are parallelizable** after dogfood but each can be its own session.

---

## 3. How to run one phase in a fresh session

Each phase doc is written to be self-bootstrapping. A session executing a phase should:

1. Read **this README** (phase map + framing) and the **target phase doc**.
2. Read the **referenced plan sections** (the phase doc lists them) — those are authoritative.
3. Confirm **prerequisites** (prior phases' "Definition of done" all checked).
4. Work the phase's **task list**, updating the **implementation tracker** checkboxes in the phase doc as you go (commit the tracker updates).
5. Verify **acceptance criteria** + run that phase's **fixtures/tests**.
6. Fill in the **handoff note** at the bottom of the phase doc and update the **master tracker** below.
7. Commit. Stop. (Plan + repo Token-Efficiency rules: stop when done; no "just in case" passes.)

> Because the build target is the separate `continuity-kit` repo, a session executing Phase 1 **creates** that repo; sessions for Phases 2+ **work inside it**. If your environment is scoped only to `Prompting-guides`, treat the phase docs as the spec to hand to whoever has the `continuity-kit` repo, and keep tracker/handoff updates here.

---

## 4. Master tracker

Status legend: ☐ not started · ◐ in progress · ☑ done · ⊘ blocked

| Phase | Status | Owner / session | Started | Completed | Notes |
|---|---|---|---|---|---|
| 1 — Foundation & `init` | ☑ | claude (web session) | 2026-06-25 | 2026-06-25 | Built at repo-root `continuity-kit/` per user direction; 9 tests passing; non-git sentinels `(no-git)` resolved |
| 2 — Record engine & `validate` | ☑ | claude (web session) | 2026-06-25 | 2026-06-25 | parser + Record + identity + field helpers + deterministic `validate` (§16.1–13); 40 tests pass; §22 Q1 resolved (convention-in-code, JSON Schema deferred) |
| 3 — Capture (`remember` + `capture`) | ☑ | claude (web session) | 2026-06-25 | 2026-06-25 | `remember decision/attempt` + `capture session` (git pre-fill, `--fast`, handoff/current updaters); no-LLM on every path; 59 tests pass |
| 4 — `resume` & **19a** | ☐ | | | | ship gate |
| *Dogfood* | ☐ | | | | 2–3 real projects |
| 5 — Search & `guard` | ☐ | | | | |
| 6 — `audit`, fixtures & **19b** | ☐ | | | | ship gate |
| 7 — Packaging (pipx) | ☐ | | | | |
| 8 — MCP server | ☐ | | | | |
| 9 — Hooks & adapters | ☐ | | | | |
| 10 — Index & dashboard | ☐ | | | | |

---

## 5. Cross-phase conventions (apply in every phase)

- **CLI surface is stable from Phase 1.** Every command supports `--json`, `--plain`, `--verbose`, `--project <path>`; capture/resume also support `--fast` (plan §10). Add flags as commands land; don't change established flag semantics.
- **Determinism by default.** `validate` is fully deterministic (plan §16.14). Heuristics (secret scan, instruction-like text) live in `audit`, never gate `validate` (plan §16 note).
- **Memory is advisory.** Nothing the tool emits may be framed as overriding user instruction, code, tests, build output, or authoritative docs (plan §9.5).
- **No secrets in committed memory** (plan §2.6, §15). The secret heuristic must exist before any "commit memory" workflow is recommended in docs.
- **Git-optional.** Several frontmatter fields are git-derived (`branch`, `commit`, `dirty_files`). Define and use a graceful fallback when git is absent (plan §22 open Q5) — decided in Phase 1, honored everywhere after.
- **Generated ≠ canonical.** Resume packet, stale report, memory-index, FTS/vector indexes are rebuildable projections carrying a source commit/hash header (plan §3, §15).
- **Bounded output.** Resume packet 3k–5k tokens; guard warnings default max 5 (plan §11.7, §12).

---

## 6. Open design questions carried through the phases

These are unresolved in the plan (§22) and should be **decided during dogfood**, then back-filled into the affected phase doc + a `decisions/` record in the tool's own dogfood project:

1. ~~Schema format: JSON Schema vs Markdown convention vs both.~~ **Resolved Phase 2:** convention-in-code now (the deterministic `validate` checks are the schema); published JSON Schema deferred to dogfood/Phase 6. *(touched Phase 2)*
2. Guard aggressiveness threshold before users ignore it. *(Phase 5)*
3. `known-traps.md` single file vs `traps/` records. *(Phases 1, 5)*
4. Local-private memory in the global dashboard without leaking. *(Phase 10)*
5. Non-git project fallback for git-derived fields. *(decided Phase 1, used everywhere)*
6. High-impact review enforcement: CI vs pre-commit vs warnings. *(Phases 6, 9)*
7. `sessions/` retention/rollup over months. *(Phases 3, 10)*

When one is resolved, record the resolution in the relevant phase doc's "Decisions resolved" section and tick it here.
