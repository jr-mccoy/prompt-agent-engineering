# Bundle Manifest — Children's Book Studio

The framework-agnostic design bundle produced by running `agentic-system-factory/` on the use case: **"produce a finished, publishable children's book from an idea."** This bundle is the *specification*; the runnable implementation is the parent `childrens-book-studio/` directory (orchestrator + prompts + agents + commands).

## Use case

Given a children's-writing idea, produce a finished manuscript (board book → upper-MG/young-teen crossover; fiction or nonfiction) plus the submission package needed to query it, while enforcing the domain's craft and integrity conventions.

## Artifact index

| Artifact | Purpose | Status |
|----------|---------|--------|
| `ARCHITECTURE.md` | scope + blast radius, Gate-0 justification, topology, architecture | complete |
| `GATE_DESIGN.md` | the craft + integrity gates (Gate 0/A/B/C) and enforcement model | complete |
| `EVAL_HARNESS.md` | capability eval + safety/integrity eval | complete |
| `DISCLOSURE_MANIFEST.md` | all six disclosure dimensions | complete |
| `OBSERVABILITY.md` | what each stage logs | complete |
| `RUNBOOK.md` | how to run; failure modes; rollback | complete |
| `RUBRIC_SCORE.md` | seven-category quality score | complete |
| `agents/` | agent specs (authority boundaries) | complete |
| `tools/` | tool specs (least-privilege) | complete |

## Gate status

<!-- GATE-0: JUSTIFIED -->
<!-- GATE-A: designed -->
<!-- GATE-B: designed -->
<!-- GATE-C: designed -->

- **Gate 0 — Justification:** JUSTIFIED (agent, not workflow). See `ARCHITECTURE.md §2`.
- **Gate A — Craft integrity:** designed (enforced by orchestrator critique). See `GATE_DESIGN.md`.
- **Gate B — Truth & representation:** designed (capability + safety eval present). See `GATE_DESIGN.md`, `EVAL_HARNESS.md`.
- **Gate C — Publishing honesty / disclosure:** designed. See `DISCLOSURE_MANIFEST.md`.

## Stack decision

<!-- STACK: none -->

**Stack: none.** This is a prompt-orchestration system, not a deployed software service. There is no Stage-7 code-gen target; the framework-agnostic bundle plus the runnable prompt toolkit is the complete deliverable.

## Enforcement model

<!-- ENFORCEMENT: orchestrator-critique -->

Gates are enforced by **orchestrator critique** (each stage prompt's Verification Checklist, applied PASS/FAIL by the orchestrator), not stdlib scripts. Rationale: the blast radius is content quality/integrity, not consequential real-world action, and the gate criteria are semantic judgments. A future scripted layer is documented in `GATE_DESIGN.md` but not required.
