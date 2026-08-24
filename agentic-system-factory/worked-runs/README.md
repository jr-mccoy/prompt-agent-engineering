# worked-runs/ — real end-to-end factory outputs (NOT fixtures)

Tracked outputs of real factory runs, kept as worked examples. Unlike
`samples/`, **nothing here is wired into the scripts' `--self-check`** — these
are illustrations of what a full run produces, at the point in time it ran.
(The pinned regression fixtures live in `samples/`; the narrated reference run
is [`../GOLD_STANDARD_RUN.md`](../GOLD_STANDARD_RUN.md).)

## Contents

### `project-continuity-memory-system/`
The phased **implementation plan** (Phases 1–10) produced for a project
continuity / memory system ("continuity-kit"): foundation → record engine →
capture/resume → search/guard → audit → packaging → MCP server → hooks →
dashboard. Plan-only output — the built kit itself lives outside this repo.

## Conventions

- Worked runs are added here **manually**, one directory per run, with the
  emitted bundle kept runnable against the live gate scripts where possible.
- Never wire a worked run into `--self-check` — promote a *reduced, stable*
  copy into `samples/` instead if it earns fixture status (the pattern
  `VALIDATION.md` established).
- Keep PII and private material out — these directories are tracked and
  public with the repo.
