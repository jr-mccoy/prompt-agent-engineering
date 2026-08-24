---
name: output-guard
description: Scan anything the loop is about to write (dossiers, alerts, orders, PRED-* journal notes) for secret-shaped strings before it lands in data/output/** or knowledge-base/**. Use this skill for "egress check", "redact before writing", "did a secret leak into an output", or any write-side defense against prompt-injection exfiltration. Implements the SECURITY.md §4d/§6 egress pass; complements (never replaces) keeping secrets in env vars / git-ignored config.
license: MIT
compatibility: Standard library only. scripts/egress_check.py is implemented — scans a file or directory and reports secret-shaped findings (cloud keys, provider tokens, PEM blocks, key=value secret assignments), with a redact() that masks them. `--self-check` proves it on planted fixtures. No dependencies, no network.
metadata:
  tags: [security, egress, secrets, exfiltration, prompt-injection, redaction, guardrail]
  updated: "2026-06-19"
---

# Output Guard (egress / secret-leak check)

The write-side security guard for the loop. Agents in this toolkit hold `Write` access to
`data/output/**` and `knowledge-base/**`. SECURITY.md §4d notes the residual risk: a
prompt-injection in an ingested filing/news/token-memo could try to smuggle a held secret
(an API key, a raw `data/input` dump) into a dossier, alert, order, or `PRED-*` note. This
skill is the egress pass that catches that **before** the file is written or committed.

## Purpose

Make the common, quiet exfiltration failure loud and machine-detectable. `egress_check.py`
scans text the loop is about to persist and flags secret-shaped content — cloud keys
(`AKIA…`), provider tokens (`ghp_…`, `xox…`, `sk-…`), PEM private-key blocks, and
`api_key|secret|token|password|bearer = <long value>` assignments — keyed to assignment
context so it does not fire on every long hash. It is a **guard, not a guarantee**: it
complements, never replaces, the discipline of keeping secrets in environment variables or
git-ignored `config/*.local.yaml` and never in prompts or tracked files.

## When to Use This Skill

Use this skill when you need to:
- Scan a freshly-written dossier / alert / order / `PRED-*` record before it is committed
- Sweep `data/output/` and `knowledge-base/` at the end of a cadence pass (the orchestrator does this)
- Redact secret-shaped substrings out of a file the loop must write anyway

## When NOT to Use This Skill

Do NOT use this skill when:
- You are deciding what the agent may *reach* (the isolation perimeter) → that is a config/scope concern, not an output scan
- You are reviewing *ingested* content for injection → that is the read-side concern in SECURITY.md §1–§5
- You need outbound-network egress control → that is required only when a live data/broker seam is wired (deferred today; see SECURITY.md §6)

## How to Run

```bash
# Scan one file or a whole output tree (exit 1 if anything secret-shaped is found):
python skills/output-guard/scripts/egress_check.py --scan data/output/
python skills/output-guard/scripts/egress_check.py --scan knowledge-base/journal/PRED-0042.md

# Prove the guard on planted fixtures:
python skills/output-guard/scripts/egress_check.py --self-check
```

`scan(path)` returns `{"clean": bool, "findings": [...], "files_scanned": int}`;
`redact(text)` returns the text with each secret-shaped substring masked as
`[REDACTED-SECRET]`. Obvious placeholders (`your-key-here`, `changeme`, `<...>`) are
ignored so the check stays low-noise.

## Where It Fits

| Stage / surface | Use |
|---|---|
| End of any cadence pass (orchestrator) | Sweep `data/output/**` + `knowledge-base/**`; refuse to commit on a finding |
| Stage 2 dossier write | Scan the dossier before persisting |
| Stage 6 order / Stage 7 `PRED-*` write | Scan the record before it joins the durable journal |
| Before wiring any live seam | NOT sufficient alone — add an outbound-host allowlist (SECURITY.md §6) |

This is the fifth skill alongside `data-source-adapter`, `pattern-knowledge-base`,
`prediction-journal`, and `paper-trade-executor` — the others enforce the value/honesty
gates; this one enforces the egress boundary.
