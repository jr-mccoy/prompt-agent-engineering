---
title: "Module Scope and Sequence — Ordering a Formation Curriculum"
category: discipleship/curriculum-architecture
description: "Sequence discipleship modules across a pathway with explicit prerequisites, deliberate revisits of foundational material, contested-practice flags, and a stated rationale for the ordering — sized to a real participant time budget."
techniques:
  - ST-02
  - ED-01
  - OC-03
  - CM-02
  - QA-01
difficulty: intermediate
tags:
  - discipleship
  - curriculum-architecture
  - scope-and-sequence
  - module-design
  - pacing
updated: "2026-08-04"
related_prompts:
  - domain-discipleship/curriculum-architecture/discipleship_curriculum_architecture.md
  - domain-discipleship/curriculum-architecture/discipleship_curriculum_balance_audit.md
  - domain-discipleship/session-and-lesson/discipleship_lesson_builder.md
  - domain-biblical-studies/church-staff-ministry-ops/biblical_churchstaff_curriculum_scope_sequence.md
  - domain-biblical-studies/study-methods-teaching/biblical_reading_plan_designer.md
---

# Module Scope and Sequence

**Objective:** Take a set of discipleship modules and order them into a defensible sequence — with
stated prerequisites, deliberate revisits of foundations, honest time sizing, and flags on every module
that touches a contested practice — so that the pathway builds rather than merely accumulates.

> **Boundary guardrail.** Sequencing decides what a participant meets and when. Where a module handles
> weighty material — suffering, sexuality, forgiveness after harm, family conflict — the sequence must
> note that it needs a prepared facilitator and an established relationship, and that participants in
> acute distress route to licensed professionals rather than into the module.

**When to use:** You have modules — from `discipleship_curriculum_architecture.md`, an existing
program, or a brainstorm — and need to order them into terms or a calendar.

**When NOT to use:**
- You don't have modules yet — use `discipleship_curriculum_architecture.md` first.
- You are sequencing a *church teaching program* across quarters and services — use
  `domain-biblical-studies/church-staff-ministry-ops/biblical_churchstaff_curriculum_scope_sequence.md`.
- You are building a Bible reading plan — use
  `domain-biblical-studies/study-methods-teaching/biblical_reading_plan_designer.md`.
- You want to check an existing curriculum for gaps rather than reorder it — use
  `discipleship_curriculum_balance_audit.md`.

**Audience:** Curriculum designers and program leads with a module inventory in hand.

---

## Inputs / Context

**Required:**

1. **Module inventory.** The modules to be sequenced, each with at least a title and the question it
   answers. Supply them in a `<module_inventory>` block. Incomplete entries are fine; guesses are not.
2. **Pathway shape.** Total duration, term or block structure if any, and the number of sessions
   available.
3. **Participant time budget.** Realistic weekly time, split between meeting time and between-meeting
   time.
4. **Participant starting point.** What can be assumed known, and what cannot.

**Optional:**

5. **Declared tradition (optional).** May shape ordering conventions — catechetical sequences,
   lectionary alignment, sacramental preparation timing — which are then labelled as that stream's
   convention rather than the natural order.
6. **Fixed points.** Anything that must land at a particular time: a retreat, a baptism season, an
   academic calendar, a program launch.

**If any required input is missing:** Ask clarifying questions before proceeding. Do not invent modules
to fill out a sequence — if the inventory has a hole, name the hole and say what kind of module belongs
there.

---

## Constraints

### Must

- State an explicit **prerequisite relationship** for every module: what must have been covered before
  it, and why.
- Place at least one **deliberate revisit** of foundational material at greater depth later in the
  sequence, and say what changes on the second pass.
- Size the sequence to the **stated time budget**, then name what was cut and what would return first.
- Flag every module that touches a **contested practice**, with the disagreement and the streams
  holding each position.
- Flag every module needing a **prepared facilitator or established relationship** before it can be
  taught safely.
- Give the rationale for the ordering in prose — not just the order, but why this order rather than a
  plausible alternative.
- Identify the sequence's **load-bearing modules**: the ones whose removal or failure breaks everything
  downstream.

### Must Not

- Invent modules, Scripture references, or content not present in the supplied inventory. Name gaps
  instead.
- Quote Scripture text from memory; addresses only.
- Present a tradition's conventional ordering (catechism order, systematic-theology order, canonical
  order) as the natural or biblical sequence.
- Front-load doctrinally contested material before any relational trust exists.
- Produce a sequence that exceeds the stated time budget without saying so explicitly.
- Assume a participant's week has more discretionary time than stated.

### Tradition-neutral stance (Must / Must Not)

- **Must:** note where an ordering choice reflects a tradition-specific commitment (baptism before or
  after instruction, confirmation timing, when the sacraments are taught, when doctrine precedes
  practice) and offer the alternative ordering.
- **Must Not:** embed one stream's catechetical sequence as the default, or imply that a different
  order is theologically deficient.

---

## Instructions

### Step 1 — Inventory and normalize

List every supplied module with its question, estimated sessions, and any Scripture addresses given.
Mark entries that are underspecified. Do not fill them in — flag them.

### Step 2 — Build the dependency map

For each module, identify what a participant must already have met to engage it. Distinguish **hard
prerequisites** (the module is incoherent without them) from **soft prerequisites** (it lands better
after). Detect and report any circular dependency.

### Step 3 — Identify the load-bearing modules

Name the modules that everything else rests on. These get earliest placement, most session time, and
the most careful facilitation. State what breaks downstream if each one lands badly.

### Step 4 — Sequence into terms

Lay the modules into the pathway's term or block structure, respecting hard prerequisites and honoring
fixed points. Where two orderings are both defensible, pick one and say why.

### Step 5 — Insert revisits

Choose foundational material to revisit later at depth. For each revisit, state what is different on
the second pass — new questions, harder passages, application under pressure — so it is a deepening,
not a repetition.

### Step 6 — Size against the time budget

Total the sessions and between-meeting load. Compare to the stated budget. If it overruns, cut and say
what was cut and why; if it underruns, say what could be added.

### Step 7 — Flag and verify

Mark contested-practice modules, facilitator-readiness modules, and gaps in the inventory. Then check
the sequence against the four ordering failures:

- **Doctrine-before-trust** — contested or confronting material arrives before relationship supports it.
- **Foundations abandoned** — basics are covered once and never revisited.
- **Accumulation without dependency** — modules are merely adjacent, not building.
- **Calendar fiction** — the sequence only fits if the participant has more time than they said.

---

## Output Format

Produce exactly this structure. Use `[..]` where a value depends on user input.

```
# Scope and Sequence — [pathway name], [duration]

## Inventory Status
| Module | Question it answers | Sessions | Status |
|---|---|---|---|
| [..] | [..] | [..] | complete / underspecified / gap flagged |

**Gaps in the inventory:** [what kind of module is missing and where it would belong]

## Dependency Map
| Module | Hard prerequisites | Soft prerequisites | Why |
|---|---|---|---|

**Circular dependencies detected:** [none | description]

## Load-Bearing Modules
| Module | What rests on it | What breaks if it lands badly |
|---|---|---|

## The Sequence
### Term / Block [n]: [name]
| Order | Module | Sessions | Prerequisites met | Flags |
|---|---|---|---|---|

## Deliberate Revisits
| Foundation revisited | First pass | Second pass — what is different |
|---|---|---|

## Ordering Rationale
[Prose: why this order and not the plausible alternative. Name the alternative.]

## Flags
| Module | Flag | Detail |
|---|---|---|
| [..] | contested practice | [disagreement, streams and positions] |
| [..] | facilitator readiness | [what the facilitator needs first] |

## Time Budget Reconciliation
- Stated budget: [..]
- Sequence requires: [..]
- Cut to fit: [..]
- First additions if time expands: [..]

## Ordering Failure Check
| Failure | Present? | Where | Fix applied |
|---|---|---|---|
| Doctrine-before-trust | [..] | [..] | [..] |
| Foundations abandoned | [..] | [..] | [..] |
| Accumulation without dependency | [..] | [..] | [..] |
| Calendar fiction | [..] | [..] | [..] |
```

---

## Verification

- [ ] Every module has a stated prerequisite relationship, or is explicitly marked as having none.
- [ ] No module appears before a hard prerequisite; circular dependencies are reported, not silently resolved.
- [ ] At least one deliberate revisit is present with a stated second-pass difference.
- [ ] Total sessions reconcile against the stated time budget, with cuts named.
- [ ] Every contested-practice module is flagged with the streams and their positions.
- [ ] No module, Scripture reference, or content was invented to fill a gap.

---

## False-Positive Prevention

❌ **DON'T:**
- Order modules by the logic of systematic theology and call it a formation sequence. What is
  logically prior is often not what is pastorally first.
- Treat canonical order as pedagogical order. Genesis to Revelation is a table of contents, not a
  curriculum.
- Put marriage, sexuality, money, or suffering early because they are "practical." They are the modules
  that most need established trust.
- Silently drop modules to make the calendar work. An unstated cut looks like an oversight to whoever
  inherits the design.
- Invent a module to bridge a dependency gap. The gap is a finding.
- Call it a revisit when the second pass covers identical material with the same questions.

✅ **DO:**
- Separate hard from soft prerequisites — conflating them over-constrains the sequence and produces a
  rigid pathway that cannot flex.
- Put the load-bearing modules where a facilitator is freshest and the relationship has room to
  recover from a bad session.
- State the alternative ordering you rejected. The next designer will consider it, and should see why
  you didn't.
- Make the revisit's second pass genuinely harder — same foundation, applied under pressure or against
  harder passages.
- Reconcile against the *stated* time budget, not a hoped-for one, and put the arithmetic in the output.
- Flag facilitator-readiness separately from contested practice. They call for different preparation.

---

## Techniques Used

- **ST-02 (Structured Sequential Instructions):** the seven steps move inventory → dependencies →
  load-bearing → sequence → revisits → sizing → flags, so ordering decisions are made against an
  explicit dependency map rather than intuition.
- **ED-01 (Iterative Scaffolding):** hard/soft prerequisites plus mandatory deliberate revisits encode
  spiral rather than linear curriculum design, directly countering the foundations-abandoned failure.
- **OC-03 (Markdown Table Specification):** the dependency map and sequence tables make a circular or
  violated prerequisite visible structurally, where prose would hide it.
- **CM-02 (Constraint Specification):** the no-invented-modules constraint turns inventory gaps into
  reported findings instead of silently filled holes.
- **QA-01 (Self-Verification):** the four-failure ordering check runs against the finished sequence,
  catching doctrine-before-trust and calendar fiction before the pathway is published.

---

## Related Prompts

- [`discipleship_curriculum_architecture.md`](discipleship_curriculum_architecture.md) — produces the
  module inventory this sequences
- [`discipleship_curriculum_balance_audit.md`](discipleship_curriculum_balance_audit.md) — check the
  sequenced curriculum for domain imbalance
- [`../session-and-lesson/discipleship_lesson_builder.md`](../session-and-lesson/discipleship_lesson_builder.md) —
  build the sessions inside a sequenced module
- [`domain-biblical-studies/church-staff-ministry-ops/biblical_churchstaff_curriculum_scope_sequence.md`](../../domain-biblical-studies/church-staff-ministry-ops/biblical_churchstaff_curriculum_scope_sequence.md) —
  the church-teaching-program counterpart
- [`domain-biblical-studies/study-methods-teaching/biblical_reading_plan_designer.md`](../../domain-biblical-studies/study-methods-teaching/biblical_reading_plan_designer.md) —
  the Scripture reading plan that runs alongside a sequence
