---
title: "Pre-Code Planning Canvas — One-Page Thinking Before You Open the Editor"
category: engineering
description: "A lightweight, personal, one-page planning artifact produced before writing code: problem statement, acceptance criteria, key risks and unknowns, a minimal test plan, and a minimal architecture sketch (modules + boundaries). Smaller than a PRD or sprint plan — it's the thing you fill in first."
techniques:
  - ST-01
  - ST-02
  - DT-01
  - CM-02
  - QA-01
difficulty: beginner
tags:
  - planning
  - pre-coding
  - acceptance-criteria
  - test-plan
  - architecture-sketch
updated: "2026-06-07"
related_prompts:
  - domain-product-management/prompts/product_planning_coding_roadmap.md
  - domain-engineering-workflows/workflows/engineering_delivery_sprint_planner.md
  - domain-engineering-workflows/workflows/engineering_debugging_root_cause.md
---

# Pre-Code Planning Canvas

**Objective:** Produce a single-page plan a developer fills in *before* writing code, capturing the problem statement, acceptance criteria, key risks/unknowns, a minimal test plan, and a minimal architecture sketch — just enough thinking to start coding deliberately instead of discovering the design by accident.

**When to Use:**
- You are about to start a task bigger than a one-line change but smaller than a full project — a feature, a refactor, a bug fix with real design choices.
- You feel the urge to "just start typing" and suspect that urge is hiding unresolved decisions.
- You are about to hand a task to an AI coding agent and want a crisp brief that defines done before delegating.
- You keep getting halfway into implementations and realizing you misunderstood the requirement or missed an edge case.

**When NOT to use:**
- The change is trivial and fully understood (a typo, a copy tweak, a one-line config flip) — the canvas is overhead.
- You need a *team-facing* artifact with stakeholders, milestones, and estimates — use a PRD or the sprint planner ([engineering_delivery_sprint_planner.md](engineering_delivery_sprint_planner.md)) instead. This canvas is personal-scale and fits on one page.
- You need a multi-week roadmap across many features — use [product_planning_coding_roadmap.md](../../domain-product-management/prompts/product_planning_coding_roadmap.md), the heavier sibling to this prompt.

---

## Inputs / Context

Provide what you have; the canvas works even from a one-line task description by surfacing the gaps as explicit unknowns.

1. **Task / ticket** — the request in whatever form you have it (a sentence, a ticket, a Slack thread). Paste it between `<task>` tags.
2. **Codebase context (optional)** — language, framework, and the rough area of the code this touches (file/module names if known).
3. **Constraints (optional)** — deadline, performance budget, backward-compat requirements, data/migration concerns, security/privacy sensitivity.
4. **Definition of done you already have (optional)** — any acceptance criteria already written down.

```
<task>
[Paste the task description, ticket, or request here]
</task>
```

If the codebase area is known, optionally include relevant signatures or interfaces:

```
<code_context>
[Paste relevant function/type signatures, schema, or interface excerpts — not whole files]
</code_context>
```

---

## Constraints

### Must
- Fit on **one page** — this is a thinking aid, not documentation. Be terse.
- State the **problem in user/behavior terms** ("when a user does X, Y should happen"), not solution terms ("add a cache").
- Write acceptance criteria as **observable, checkable conditions** — each one must be answerable yes/no after implementation.
- Surface **unknowns explicitly** rather than assuming them away. An honest "I don't know yet: …" is more valuable than a confident wrong guess.
- Keep the architecture sketch **minimal**: name the modules/components that will change or be created, and the boundary (interface/contract) between them. No class diagrams, no exhaustive design.
- Keep the test plan **minimal but real**: the handful of cases that would actually catch the failure modes — at least one happy path, the key edge cases, and one failure/error path.
- Distinguish **decisions made** from **decisions deferred**, and for deferred ones, note the trigger that will force the decision.

### Must Not
- Expand into a PRD, design doc, or estimate spreadsheet — if it no longer fits a page, it is the wrong tool.
- Specify implementation line-by-line — the canvas sets boundaries and intent, the editor is where code happens.
- List acceptance criteria that cannot be observed or verified ("code should be clean").
- Hide an unresolved question inside a confident-sounding sentence.
- Invent constraints (performance numbers, SLAs) that were not given — mark assumed constraints as assumptions.

---

## Instructions

1. **Restate the problem in behavior terms (ST-01).** From `<task>`, write 1–3 sentences describing what should be true for the user/system after the work, and why it matters. If the task is solution-shaped ("add a queue"), reverse-engineer the underlying problem it solves and state that.

2. **Write acceptance criteria (CM-02).** List the concrete, checkable conditions that mean "done." Each is a yes/no statement. Include the negative/error behaviors, not just the happy path. If criteria are genuinely unknowable until you see the code, say so and mark them provisional.

3. **Surface risks and unknowns (QA-01).** List what could go wrong or what you don't yet know: ambiguous requirements, unfamiliar code, external dependencies, data/migration hazards, concurrency, security/privacy exposure, breaking changes. For each, note how you'll resolve it (spike, read code, ask someone) — or that you'll proceed and revisit.

4. **Sketch the minimal architecture (DT-01).** Name the modules/components touched or created and the boundary between them — the interface or contract each side relies on. One or two lines per component. Identify the single most load-bearing boundary (the one most likely to change) and keep it clean.

5. **Draft the minimal test plan (ST-02).** Pick the smallest set of tests that would actually catch the failure modes from Step 3: at least one happy-path case, the key edge cases, and one error/failure path. Note the level (unit / integration / manual) for each. These tests are also your acceptance check.

6. **Separate decided from deferred.** Mark which design decisions you are committing to now and which you are intentionally leaving open. For each deferred decision, write the trigger that will force it ("decide on caching once we measure the read path").

7. **Sanity-check the whole page.** Re-read: do the acceptance criteria, tests, and architecture line up? Does any unknown invalidate the sketch? If a risk is severe and unresolved, flag that the plan is provisional pending a spike. Then stop — the canvas is done, go write the code.

---

## False-Positive Prevention

1. **Solution disguised as problem.** "Add Redis" is not a problem statement; it's a chosen solution. If the problem section names a technology, you skipped the actual problem. Restate in behavior terms.
2. **Unverifiable acceptance criteria.** "Should be performant," "should be maintainable" cannot be checked. Replace with observable conditions ("p95 < 200ms on the search endpoint" or, if no number was given, "no slower than the current endpoint — assumption, confirm").
3. **Optimistic unknown-erasure.** Writing the plan as if everything is known is the most common failure. A short, honest unknowns list beats a confident plan that collapses on contact with the code.
4. **Architecture over-reach.** A full design with every class and method is not minimal and not the point. Stop at modules + boundaries. If you're drawing more than a handful of boxes, you're past the canvas.
5. **Happy-path-only test plan.** A plan that only tests success will pass while the feature breaks on the inputs that matter. Always include edge and error cases derived from the risks.
6. **Invented constraints.** Don't assert a deadline, throughput target, or compatibility rule that wasn't given. Mark anything you assume as an assumption to be confirmed.
7. **Canvas that became a PRD.** If it no longer fits one page, you've outgrown the tool — route to the roadmap or sprint planner. Length itself is a smell here.
8. **No deferral trigger.** "We'll decide later" with no trigger means it gets decided implicitly and badly. Every deferred decision needs a condition that forces it.

---

## Output Format

```
# Pre-Code Canvas: [task name]

## Problem (behavior + why)
[1–3 sentences: what should be true after this, and why it matters.]

## Acceptance Criteria (checkable yes/no)
- [ ] [Happy-path condition]
- [ ] [Edge condition]
- [ ] [Error/negative condition]
- [ ] [...]
(provisional criteria marked: ~[criterion]~ — confirm once code is seen)

## Risks & Unknowns
| Risk / unknown | Severity (H/M/L) | How I'll resolve it |
|----------------|------------------|---------------------|
| [...]          | [...]            | [spike / read code / ask / proceed + revisit] |

## Minimal Architecture Sketch
- [Component A] — [responsibility] — boundary to [Component B]: [interface/contract]
- [Component B] — [responsibility]
- Most load-bearing boundary: [which one, and why keep it clean]

## Minimal Test Plan
| Test | Level (unit/integration/manual) | Catches which risk |
|------|----------------------------------|--------------------|
| Happy: [...]   | [...] | [...] |
| Edge: [...]    | [...] | [...] |
| Error: [...]   | [...] | [...] |

## Decisions
- Decided now: [...]
- Deferred: [decision] — trigger: [condition that forces it]

## Status: [Ready to code] | [Provisional — needs spike on (unknown) first]
```

---

## Verification

- [ ] The whole canvas fits on one page.
- [ ] The problem is stated in behavior/user terms, not as a chosen solution.
- [ ] Every acceptance criterion is observable and answerable yes/no.
- [ ] Acceptance criteria include error/negative behavior, not only the happy path.
- [ ] Unknowns are listed explicitly with a resolution path; none are hidden in confident prose.
- [ ] The architecture sketch is minimal — modules and boundaries only, no full design.
- [ ] The test plan has at least one happy-path, edge, and error case, each tied to a risk.
- [ ] Decided vs. deferred is explicit, and each deferred decision has a trigger.
- [ ] No constraints were invented; assumed ones are marked as assumptions.
- [ ] If the artifact outgrew one page, it was routed to the PRD/roadmap/sprint planner instead.
```
