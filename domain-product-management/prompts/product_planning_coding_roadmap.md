---
title: "Coding Roadmap — Meta-Scaffolding Bridge from Approved Spec to First Commit"
category: product-management/prompts
description: "Draft a coding roadmap before writing any code: architecture sketch, module boundaries, build sequencing, interface contracts, and a risk list. The bridge between an approved spec/PRD and the first commit — narrower than a PRD, broader than a sprint plan."
techniques:
  - ST-01
  - ST-02
  - DT-01
  - CM-02
  - DS-06
  - QA-01
difficulty: intermediate
tags:
  - technical-planning
  - architecture
  - build-sequencing
  - interface-contracts
  - pre-implementation
updated: "2026-06-07"
related_prompts:
  - domain-product-management/prompts/product_create_prd.md
  - domain-product-management/prompts/product_delivery_sprint_planner.md
  - domain-idea-to-product/stage-8-architecture-design/architecture_tech_stack_selector.md
---

# Coding Roadmap

**Objective:** Convert an approved specification or PRD into a build-ready coding roadmap — an architecture sketch, module boundaries, build sequence, interface contracts, and a ranked risk list — so the first commit is well-aimed instead of speculative.

**When to Use:**
- You have an approved spec/PRD and need to decide *how* to build before you write code.
- A solo developer or small team needs a shared mental model of module boundaries and sequencing.
- You are about to hand the build to an AI coding agent and need explicit interface contracts and a sequence it can follow.
- A previous build stalled because architecture was improvised commit-by-commit.

**When NOT to use:**
- You don't yet have an approved spec — author or score the PRD first (`product_create_prd.md`).
- You need to allocate the work across people and time — that's a sprint plan (`product_delivery_sprint_planner.md`).
- You need to choose the stack itself — use `architecture_tech_stack_selector.md` first; this roadmap assumes the stack is chosen.
- You're prototyping a throwaway spike where structure is intentionally deferred.

## Inputs / Context

The user supplies (wrap any pasted spec in `<spec>` tags):

1. **The approved spec/PRD** (pasted or summarized) — the *what* this roadmap operationalizes.
2. **Chosen tech stack** — language(s), framework(s), data store, deployment target.
3. **Team shape** — solo, small team, or AI-agent-assisted; relevant for granularity of contracts.
4. **Hard constraints** — existing systems to integrate, deadlines, performance/compliance requirements, must-reuse components.
5. **Known unknowns** — anything the user already suspects is risky or undecided.
6. **Definition of "first milestone"** — the smallest thing worth shipping or demoing.

## Constraints

### Must
- Ground every roadmap element in the supplied spec — if a module isn't traceable to a spec requirement, flag it as scope creep.
- Define **module boundaries** by responsibility, not by file layout — each module gets a one-sentence responsibility statement.
- Specify **interface contracts** between modules: inputs, outputs, error modes, and ownership — concrete enough that two modules could be built independently.
- Produce a **build sequence** ordered by dependency and risk-retirement, not by feature priority — build the riskiest load-bearing thing early.
- Produce a **ranked risk list** with severity, likelihood, and a first probe for each.
- Mark the **walking skeleton** — the thinnest end-to-end path that proves the architecture works.
- State assumptions explicitly and label each as confirmed-by-spec or inferred.

### Must Not
- Write implementation code — this is a roadmap, not a first commit.
- Invent requirements not present in the spec, or silently resolve spec ambiguities — surface them as open questions.
- Specify a microservice/distributed design when a modular monolith satisfies the spec (justify any distributed boundary against an actual requirement).
- Sequence by "easy first" — that defers risk to the end of the project.
- Produce module boundaries so fine-grained they create more interfaces than the spec warrants.

## Instructions

1. **Restate the build target.**
   - In 2–3 sentences, restate what the spec asks to be built and the first-milestone definition, in your own words. This surfaces misreadings before they cost code.

2. **Sketch the architecture.**
   - Identify the top-level components and how data/control flows between them.
   - Choose an architectural style (modular monolith, layered, event-driven, etc.) and justify it against a *specific* spec requirement, not general preference.
   - Identify the single most architecturally significant decision and its alternatives.

3. **Define module boundaries (DT-01).**
   - Decompose into modules. For each: name, one-sentence responsibility, the spec requirement(s) it serves, and what it explicitly does NOT own.
   - Check for responsibility overlap and orphaned requirements (a requirement no module owns).

4. **Write interface contracts (CM-02).**
   - For each boundary between modules: the call/data shape (inputs → outputs), error/failure modes, and which module owns the contract.
   - Make contracts concrete enough that two developers (or two agent sessions) could build the modules independently and integrate.

5. **Order the build sequence.**
   - Identify the **walking skeleton**: the thinnest end-to-end slice that exercises the real architecture (not a mock).
   - Sequence remaining modules by dependency first, then by risk-retirement (build the thing most likely to be wrong, early).
   - Mark sequence checkpoints where integration is verified before proceeding.

6. **Build the risk list (DS-06).**
   - Enumerate technical risks: unproven integrations, performance unknowns, ambiguous spec areas, third-party dependencies, data-migration hazards.
   - Rank each by severity × likelihood. For each top risk, give the cheapest first probe that would confirm or kill it.

7. **CRITICAL — verify the roadmap against the spec before reporting (QA-01).**
   - Trace each spec requirement to at least one module. List any unmapped requirements.
   - List any module or interface that does NOT map to a spec requirement (candidate scope creep).
   - Confirm the build sequence has no circular dependencies and the walking skeleton is genuinely end-to-end.
   - Assign a confidence level (High/Medium/Low) to the architecture sketch and the sequence.

## False-Positive Prevention

1. **Phantom requirements.** Do not add modules for capabilities the spec doesn't ask for ("we'll probably need auth," "let's add caching"). If it's not in the spec, list it as an open question, not a module.
2. **Premature distribution.** A boundary between two services is a cost (network, serialization, partial failure). Don't draw service boundaries unless a real requirement (independent scaling, separate deploy cadence, team ownership) forces it — a modular monolith is the default.
3. **Easy-first sequencing.** A sequence that builds simple CRUD first and defers the hard integration to the end *looks* like progress but retires no risk. Verify the riskiest load-bearing element is early.
4. **Fake walking skeleton.** A skeleton that mocks the database or the external API doesn't prove the architecture. The skeleton must touch the real load-bearing boundaries.
5. **Vague contracts.** "Module A talks to Module B" is not a contract. A contract names inputs, outputs, and error modes. If you can't write it concretely, the boundary is probably wrong.
6. **Resolving ambiguity silently.** When the spec is unclear, the roadmap must surface the ambiguity as an open question — not pick an interpretation and bury it in a module description.
7. **Confidence laundering.** Don't present an inferred decision as if the spec mandated it. Label inferred assumptions distinctly so the user can confirm them.

## Output Format

```
# Coding Roadmap — [project / feature name]

## Build target (restated)
[2–3 sentences] + First milestone: [definition]

## Assumptions
- [confirmed-by-spec | inferred] — [assumption]

## Architecture sketch
- Style: [chosen] — justified by spec requirement: [which]
- Components & data flow: [narrative or simple text diagram]
- Most significant decision: [decision] | Alternatives considered: [...]
- Confidence: [High/Medium/Low]

## Modules
| Module | Responsibility (1 sentence) | Serves spec req(s) | Does NOT own |
|--------|-----------------------------|--------------------|--------------|
| [name] | [...]                       | [REQ-x]            | [...]        |

## Interface contracts
### [Module A] → [Module B]
- Inputs: [...]
- Outputs: [...]
- Error/failure modes: [...]
- Contract owner: [module]

## Build sequence
1. **Walking skeleton:** [thinnest end-to-end slice] — proves: [which boundaries]
2. [module/step] — depends on: [...] | retires risk: [...]
3. ... 
   → Checkpoint: [integration verified before proceeding]

## Risk list (ranked)
| # | Risk | Severity | Likelihood | First probe |
|---|------|----------|------------|-------------|
| 1 | [...]| High     | Med        | [cheapest test that confirms/kills it] |

## Spec coverage check
- Unmapped spec requirements: [none | list]
- Modules/interfaces with no spec basis (scope-creep candidates): [none | list]

## Open questions (spec ambiguities to resolve before building)
- [question] — blocks: [module/decision]
```

## Verification

- [ ] Build target restated in own words; first milestone defined.
- [ ] Architecture style justified against a specific spec requirement.
- [ ] Every module has a one-sentence responsibility and a "does not own" boundary.
- [ ] Every spec requirement traces to at least one module (unmapped ones listed).
- [ ] Every module/interface traces to a spec requirement (scope-creep candidates listed).
- [ ] Each interface contract names inputs, outputs, error modes, and owner.
- [ ] Walking skeleton is genuinely end-to-end (no mocked load-bearing boundaries).
- [ ] Build sequence retires highest risk early; no circular dependencies.
- [ ] Risk list ranked by severity × likelihood, each with a first probe.
- [ ] Assumptions labeled confirmed-by-spec vs inferred; open questions surfaced.
- [ ] Confidence levels assigned to architecture and sequence.
