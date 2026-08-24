# Phase 8 — MCP Server (Python)

| | |
|---|---|
| **Phase** | 8 of 10 (post-MVP) |
| **Prerequisites** | Phase 6 (MVP-trust); Phase 7 recommended (packaging). CLI semantics must be **stable** (plan §18 Phase 5). |
| **Plan sections** | §13 (MCP resources/prompts/tools), §18 Phase 5, §20 task 16 |
| **Ships** | A Python MCP server exposing memory as resources, prompts, and tools |
| **Session size** | Medium |

---

## Objective

Expose the now-stable memory engine over MCP so agents can read/record/guard without shelling out — **a thin wrapper over the Phase 1–6 functions**, not a reimplementation. Python MCP SDK (plan §22 resolved: no TS rewrite).

## Scope / Tasks (all from plan §13)

### Resources
1. Implement read-only resources:
   `memory://current`, `memory://handoff`, `memory://resume-packet`, `memory://decisions`, `memory://decisions/{id}`, `memory://attempts/{id}`, `memory://open-questions`, `memory://known-traps`.

### Prompts
2. Implement MCP prompts mapping to CLI flows: `resume_project`, `capture_session`, `remember_decision`, `remember_attempt`, `guard_before_action`, `audit_project_memory`.

### Tools
3. Implement MCP tools over existing functions:
   `memory_search(query, filters)`, `memory_record(type, payload)`, `memory_guard_before_action(action, files?)`, `memory_build_resume_packet(task?)`, `memory_validate()`, `memory_mark_status(id, status, reason)`, `memory_scan_secrets()`.
4. **Reuse, don't fork:** each tool calls the same core functions the CLI uses (search/guard/resume/validate/audit/record). One source of behavior.
5. **Safety posture:** memory content returned over MCP is data, not instruction (§15); `memory_record` writes go through the same `validate` gate; `memory_scan_secrets` available before commit workflows.
6. **Graceful degradation:** server is optional; everything still works via CLI/plain files if MCP is absent (§3, §13 "MCP later", §2.4 no-daemon baseline).

## Acceptance criteria
- [ ] Server starts and registers all §13 resources, prompts, tools.
- [ ] Reading `memory://*` returns the same content the CLI/plain files show.
- [ ] `memory_guard_before_action` matches CLI `guard` verdicts on the fixtures.
- [ ] `memory_record` writes valid records (passes `validate`).
- [ ] Tools wrap existing functions (no behavior fork).
- [ ] Tool/resource output documented in `docs/mcp-spec.md` (upgraded from Phase 1 stub).

## Implementation tracker

| # | Task | Status | Notes |
|---|---|---|---|
| 1 | MCP server skeleton (Python SDK) | ☑ | `continuity_kit/mcp_server.py` (FastMCP binding) + `mcp_core.py` (stdlib adapter layer) |
| 2 | resources (8) | ☑ | all `memory://*` bound; return verbatim file / CLI-identical packet |
| 3 | prompts (6) | ☑ | map 1:1 to CLI flows; guidance-only, no authority over user/code/tests |
| 4 | tools (7) wrapping core fns | ☑ | each calls `cli.search/guard/build_resume_packet/run_validate/scan_secrets/write_record/set_record_status` |
| 5 | record-through-validate gate | ☑ | `memory_record` + `memory_mark_status` reuse `_validate_new_file`; invalid writes reverted |
| 6 | data-not-instruction + secret-scan posture | ☑ | documented in `mcp-spec.md` §Safety; `memory_scan_secrets` exposed |
| 7 | graceful-degradation verified | ☑ | module imports w/o SDK; `build_server`/`main` give install hint + non-zero exit; tests cover it |
| 8 | docs/mcp-spec.md upgraded | ☑ | full implemented surface, output shapes, install/run, Phase 9 handoff |
| 9 | MCP integration tests | ☑ | `tests/test_mcp.py` (19 tests): resource parity, guard==CLI on all 10 fixtures, write-gate, degradation |

## Decisions resolved this phase
- **Python MCP SDK choice/version:** official `mcp` SDK via `FastMCP`
  (`mcp.server.fastmcp`), pinned as the **optional** extra
  `continuity-kit[mcp] = ["mcp>=1.2; python_version >= '3.10']`. Kept out of core
  `dependencies` so the package stays standard-library-only and degrades
  gracefully (CLI/plain files work with no SDK). Server transport: stdio default.
- **`memory_mark_status` backing:** added `cli.set_record_status` +
  `cli.find_record_by_id` (filename-canonical id, §7) as shared core fns —
  validate-gated, so no behavior fork and a future CLI command can reuse them.

## Handoff
- Phase 9 generates `.mcp.json` pointing at this server. Invocation command:
  `continuity-mcp` (console script) or `python -m continuity_kit.mcp_server`,
  with `CONTINUITY_PROJECT` set to the project root (server defaults to cwd).
  See `docs/mcp-spec.md` §"Handoff to Phase 9" for the ready-to-emit JSON block.
