---
title: "Stage 1 — Scope the System"
category: agentic-system-factory/stage-1-scope
description: "Turn the justified use case into a bounded, checkable specification: one-sentence use case, job-to-be-done, observable success gates (not vibes), typed inputs/outputs with trust levels, autonomy level, and — most important — the blast radius, which sizes every later gate. Marks which inputs are untrusted external content."
techniques:
  - ST-01
  - ST-03
  - CM-02
difficulty: advanced
tags:
  - scoping
  - blast-radius
  - success-criteria
  - trust-boundary
updated: "2026-07-02"
related_prompts:
  - domain-engineering-workflows/done-definition/done_definition_translator.md
  - domain-engineering-workflows/ai-patterns/ai_pattern_intent_and_verification_first.md
  - agentic-system-factory/prompts/stage-0-justify.md
---

# Stage 1 — Scope the System

## Objective
Define the bounded problem before choosing any pattern, and fill `ARCHITECTURE.md §1`. The load-bearing output is the **blast radius** — the worst thing the system can do — because it sizes every gate downstream.

## When to Use
- After Gate 0 passes (`GATE-0: JUSTIFIED`).
- Before topology selection.

## Inputs / Context
- The Stage-0 justification + chosen rung.
- The user's description of the desired outcome and how success would be recognized.
- Known inputs (and which are external/untrusted) and the intended consumer of the output.

## Constraints

**Must:**
- Express success criteria as **observable, checkable gates** ("every claim cites a retrieved source"), not adjectives ("good research").
- Tag every input with a **trust level**; flag untrusted external content explicitly.
- State the **blast radius** as a concrete worst-case action (reads web only / writes files / sends email / moves money).
- State the **autonomy level** (acts vs recommends-only).

**Must Not:**
- Leave success criteria as vibes, or omit the blast radius.
- Expand scope beyond the justified job; record explicit non-goals.

## Instructions
1. **Use case in one sentence** + the underlying **job-to-be-done**.
2. **Success criteria** as a checklist of observable gates. Each must be verifiable by inspection or a test.
3. **Inputs / outputs** — types, formats, volume, trust level. Mark untrusted external content (web pages, user files, third-party API payloads).
4. **Autonomy level** — does it take action in the world, or only recommend?
5. **Blast radius** — the single worst action it can take. This is the most important line in the bundle.
6. **Out of scope** — explicit non-goals (auth'd actions, streaming, etc.).
7. **Reuse vs net-new** — which existing repo prompts/agents/tools already cover parts of this.

## Output Format
Fill `ARCHITECTURE.md §1` (Use case & scope; section layout in [`../templates/ARCHITECTURE_TEMPLATE.md`](../templates/ARCHITECTURE_TEMPLATE.md)). The orchestrator critiques it against this stage's checklist before advancing.

## Verification Checklist
- [ ] Use case is one sentence; job-to-be-done is explicit.
- [ ] Every success criterion is observable/checkable, not a vibe.
- [ ] Each input has a trust level; untrusted external content is flagged.
- [ ] Blast radius is a concrete worst-case action.
- [ ] Autonomy level (acts vs recommends) is stated.
- [ ] Out-of-scope non-goals are listed.

## False-Positive Prevention
- An adjective with a checkbox ("output is high quality ✔") is still a vibe — false checkability. Every criterion must name *what is inspected* and *what counts as pass* so a reviewer could verify it without asking you.
- The classic understated blast radius: "read-only, so low risk" while the inputs include untrusted external content. Injection through a read-only system whose output a human then acts on is a real blast radius — record it, or Stage 4 will be sized against the wrong worst case.

## References (assembled, not duplicated)
- ⭐ `domain-engineering-workflows/done-definition/done_definition_translator.md` — fuzzy → observable gates with evidence.
- `domain-engineering-workflows/ai-patterns/ai_pattern_intent_and_verification_first.md` — intent + verification + out-of-scope.
- `domain-engineering-workflows/ai-patterns/ai_pattern_outcome_language_translator.md` — implementation → outcome language.

## Produces
`ARCHITECTURE.md §1` → feeds Stage 2 (topology) and sizes Stage 4 (gates).
