# TOOL SPEC — (deliberate absence of any external tool)

**System:** marketing-copy-evaluator-optimizer

## Statement of deliberate tool absence
This system has **no external tools**. Both roles — the generator and the critic — operate purely on in-context content: the product brief, the brand rules, and the current draft. There is no search, no fetch, no file I/O, no network, no code execution, no messaging, and no spend.

This absence is itself the least-privilege design statement. The system is **read-only by construction**: with no tool that can write, fetch, execute, or send, there is no privilege to abuse, no untrusted-action surface, and no blast radius beyond the text returned to the caller.

## Why SAFE-04 is "na" (not applicable), not "enforced"
SAFE-04 (least-privilege tools) asks that an agent's tool set be minimized to exactly what the task requires. Here the minimal tool set is the **empty set** — there are no tools to scope, allowlist, or strip down. Because there is no tool privilege to minimize, SAFE-04 is marked not-applicable with a reason in `GATE_DESIGN.md`:

```
<!-- SAFE-04: na: no external tools exist — generator/critic operate only on in-context content, so there is no tool privilege to minimize -->
```

The real risk surface is the **content** (unsubstantiated claims, off-brand text), which is covered by the 3-layer defense-in-depth on the claims path (generator self-check → independent critic → final claims-substantiation guardrail) documented in `GATE_DESIGN.md` and evaluated in `EVAL_HARNESS.md` (Gate B-safety).

## Invariant to preserve
If a future revision introduces any external tool (e.g. a live fact-check fetch), this file and the SAFE-04 marker MUST change: SAFE-04 flips from `na` to `enforced`, a real allowlist + schema validation must be added, and the blast-radius / disclosure sections must be revisited. The `na` branch is valid only while the tool set stays empty.
