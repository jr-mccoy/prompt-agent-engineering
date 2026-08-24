# Phase 9 — Hooks & Agent Adapters

| | |
|---|---|
| **Phase** | 9 of 10 (post-MVP) |
| **Prerequisites** | Phase 6 (MVP-trust); Phase 8 recommended (for `.mcp.json`) |
| **Plan sections** | §13 (signposts, hooks), §15 (executable-config review), §18 Phase 6, §20 task 17 |
| **Ships** | Opt-in, reviewable agent signpost files + hook templates with manual fallbacks |
| **Session size** | Medium |

---

## Objective

Generate the thin **signpost** files and optional **hooks** that let each agent ecosystem discover `.project-memory/` and the `continuity` commands — without ever turning those files into the memory database (plan §2.5: signposts only) and without auto-running unreviewed executable config (§15).

## Scope / Tasks

### Signpost generation (plan §13)
1. `init`/a new `adapters` subcommand generates **short** signpost files, each pointing at `.project-memory/` + the protocol (read current/handoff/records → `guard` before non-trivial work → `capture` at session end):
   - `AGENTS.md` (use the §13 snippet),
   - `CLAUDE.md`,
   - `.gemini/GEMINI.md`,
   - `.cursor/rules/project-memory.mdc`,
   - `.codex/config.toml` snippet,
   - `.mcp.json` (points at the Phase 8 server).
2. **Signposts must not duplicate memory content** (§2.5, §16.13 — audit already checks this). Keep them to the protocol + pointers.
3. **Everything opt-in and reviewable** (§18 Phase 6). Generation is explicit (flagged), never silent; existing files are not clobbered without `--force`.

### Hooks (plan §13 "Hooks last")
4. Provide **templates** (not auto-installed) for: session start → build resume packet; pre-action → guard; failed command → offer attempt record; session end → prompt capture.
5. **Every hook has a manual fallback command** (§13) — the tool never depends on hooks (§2.4).
6. **Executable config requires human review** (§15): generated hook/config files are emitted as reviewable snippets with a header noting they run commands; document the review expectation.

### High-impact enforcement (plan §22 Q6, deferred from Phase 6)
7. If dogfooding chose CI/pre-commit enforcement of high-impact memory review (§15 list), implement the pre-commit hook here (e.g. run `validate` + `audit` + flag high-impact diffs in `decisions/`/`attempts/`). If "warnings only" was chosen, ship the warning path. Record the decision.

## Acceptance criteria
- [ ] Adapter generation produces short, pointer-only signposts for all listed ecosystems.
- [ ] Signposts pass the audit no-duplication check.
- [ ] Generation is opt-in, non-clobbering without `--force`.
- [ ] Hook templates exist with documented manual fallbacks.
- [ ] Executable configs carry a review header; nothing auto-runs unreviewed.
- [ ] High-impact review path (enforced or warned, per §22 Q6) implemented.

## Implementation tracker

| # | Task | Status | Notes |
|---|---|---|---|
| 1 | AGENTS.md / CLAUDE.md generators | ☐ | |
| 2 | Gemini / Cursor / Codex snippets | ☐ | |
| 3 | .mcp.json generator (→ Phase 8 server) | ☐ | |
| 4 | no-duplication + non-clobber guards | ☐ | |
| 5 | hook templates (start/pre-action/fail/end) | ☐ | |
| 6 | manual fallback commands documented | ☐ | |
| 7 | executable-config review headers | ☐ | |
| 8 | high-impact review path (§22 Q6) | ☐ | |
| 9 | tests for adapter generation | ☐ | |

## Decisions resolved this phase
- _High-impact review: CI vs pre-commit vs warnings (§22 Q6):_ _(record final)_

## Handoff
- Note any adapter that needs index/dashboard awareness for Phase 10.
