# ARCHITECTURE — nightly-csv-report (Gate-0 WORKFLOW-STOP fixture)

> Regression fixture for the Gate-0 **WORKFLOW-STOP** terminal: Stage 0
> correctly talked this use case *down* the complexity ladder — a deterministic
> workflow wins, no agent is built, and the factory ends successfully here.
> `check_gate.py --gate 0` must **PASS** on this directory. It is intentionally
> **not** a full bundle (`validate_bundle.py` fails it by design; no other gate
> applies because nothing past Stage 0 is ever produced).

## §2 Justification (complexity ladder)

**Use case:** "email me a nightly CSV report of yesterday's orders."

**Ladder walk:** fixed schedule, fixed query, fixed recipient, no branching on
unstructured input, no runtime tool selection, no open-ended goal. A cron job +
parameterized SQL + SMTP script does this deterministically; an agent adds
nondeterminism, cost, and a new attack surface with zero added capability.
Stop at the **workflow** rung.

<!-- GATE-0: WORKFLOW-STOP -->

**Terminal artifact:** the workflow spec above. Build that instead — per
`prompts/stage-0-justify.md`, a workflow-stop is a *win*, not a failure.
