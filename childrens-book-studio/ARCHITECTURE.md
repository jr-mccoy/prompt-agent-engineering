# Children's Book Studio — Architecture

This document explains *why the studio is built the way it is*. It is the human-readable companion to the machine-oriented [`design-bundle/`](design-bundle/), which is the formal output of running the [`agentic-system-factory/`](../agentic-system-factory/) on the use case "produce a finished, publishable children's book from an idea."

For *how to run* the studio, see [`README.md`](README.md) and [`PIPELINE_OVERVIEW.md`](PIPELINE_OVERVIEW.md). The authoritative design spec is in [`design-bundle/`](design-bundle/); this file summarizes the reasoning behind it.

---

## 1. The factory decisions (summary)

The studio was designed by walking the factory's stages. The load-bearing conclusions:

### Gate 0 — Is an agent justified? **Yes.**

Walking the complexity ladder honestly:
1. Deterministic function? No — this is creative generation.
2. Single model call? No — a finished book requires ideation, structure, drafting, multi-pass revision, and publishing prep.
3. **Fixed code-controlled workflow?** Almost — but two things require runtime dynamism:
   - **Form-conditioned routing.** A board book, a verse novel, and a nonfiction STEM book traverse *different* stage sequences and craft passes. Which stages run depends on the project, decided at runtime.
   - **The Stage 4 revision loop.** Which craft tools fire, how many passes run, and when revision is "done" depend entirely on what the diagnostic surfaces in *this* manuscript. The step count, order, and tool selection are data-dependent.
4. → **Agent justified.** Not inflated beyond this: the bulk of the pipeline is sequential.

### Topology

- **TP-04 (routing/handoff)** at the top: the orchestrator classifies the project's form and entry stage and routes accordingly.
- **TP-03 (sequential chaining)** for the spine: Stages 0→6 run in order for a given project.
- **TP-07 (evaluator-optimizer)** inside Stage 4: diagnose → fix → re-check against Gate A, looping until it passes.

### Blast radius (why the gates matter)

The studio's worst-case actions are low-severity versus money or security systems, but real for a **child audience**:
- A nonfiction kids' book stating **fabricated facts as true** (misinformation to children).
- **Over-certifying** a write-across-difference portrayal as "authentic/safe," giving a writer false confidence.
- **Age-inappropriate content** leaking into a young-child product.
- A publishing package with **invented comps/agents** sending an author into the market on false information.
- **Overwriting the author's own draft** file.

These five worst-cases are exactly what Gates 0/A/B/C contain. The gates are not generic safety theater — each one closes a specific blast-radius item.

---

## 2. Why gates are orchestrator-critique, not scripts

The factory's reference toolkits (`ai-investment-research-toolkit/`, `financial-records-toolkit/`) enforce gates with stdlib Python ("code-not-trust") because their blast radius includes money movement and irreversible data loss, where a script must mechanically block an action.

This studio's blast radius is **content quality and integrity**, not consequential real-world action. Its gate criteria — "does the child drive the climax," "is the theme preached," "is this portrayal certified or merely flagged" — are **semantic judgments** that a lexical script can only approximate. So enforcement lives where the judgment is: in the orchestrator, checking each stage's Verification Checklist PASS/FAIL and refusing to advance on any FAIL (the `domain-idea-to-product/` model).

`design-bundle/GATE_DESIGN.md` records this as a deliberate design choice and documents what a future scripted layer *would* check (word-count band, Flesch-Kincaid vs. age, preaching/comp/certification lexical scans) if the studio ever needed mechanical enforcement.

---

## 3. Why it references the domain instead of rebuilding it

The 22 prompts in [`domain-childrens-writing/`](../domain-childrens-writing/) are already Tier-1, cross-linked, and convention-bearing. The studio's stage prompts are **thin orchestration glue**: each one frames the stage, names which domain prompt(s) to run, and carries the Verification Checklist the orchestrator gates on. The mapping is indexed in [`referenced-prompts/README.md`](referenced-prompts/README.md). This keeps a single source of truth and avoids drift.

---

## 4. The seams

| Boundary | What crosses | Control |
|----------|--------------|---------|
| Orchestrator → stage prompt | the project spec + prior stage output | orchestrator decides which stage, by form + entry classification |
| Stage prompt → domain prompt | the manuscript-in-progress | the stage prompt names the exact domain file |
| Stage 4 internal loop | the fix queue | the craft reviewer agent re-checks Gate A each pass |
| Stage → next stage | the gated artifact | orchestrator refuses to pass a FAILed checklist |
| Studio → author | draft files | the author owns the files; the studio proposes edits, never silently overwrites (Stage prompts instruct save-as-new-version) |

---

## 5. What the design bundle contains

[`design-bundle/`](design-bundle/) is the factory's formal output — the framework-agnostic spec proving the system was designed, not improvised: `BUNDLE_MANIFEST.md`, `ARCHITECTURE.md` (scope/justification/topology/architecture), `GATE_DESIGN.md`, `EVAL_HARNESS.md` (capability + safety evals), `DISCLOSURE_MANIFEST.md`, `OBSERVABILITY.md`, `RUNBOOK.md`, `RUBRIC_SCORE.md`, plus `agents/` and `tools/` specs. The runnable studio (this directory's `orchestrator_*.md`, `prompts/`, `agents/`, `commands/`) is the *implementation* of that spec.
