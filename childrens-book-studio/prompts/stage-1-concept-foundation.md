---
title: "Stage 1 — Concept Foundation (Protagonist, Agency, Theme; NF Source Plan)"
category: childrens-writing/pipeline
description: "Builds the story's foundation: premise, the child protagonist with non-negotiable agency, the want/need, and the theme carried by action (not preached). For nonfiction, narrows the topic and builds the source plan that the truth gate will later check against."
techniques:
  - ST-01
  - ST-02
  - CM-02
  - QA-01
  - QA-04
difficulty: intermediate
tags:
  - childrens-writing
  - pipeline
  - stage-1
  - character
  - theme
updated: "2026-06-24"
related_prompts:
  - childrens-book-studio/prompts/stage-0-project-setup.md
  - domain-childrens-writing/craft-tools/childrens_character_creation.md
---

# Stage 1 — Concept Foundation

## Objective

Establish the load-bearing foundation a children's book stands on: a premise, a child protagonist who **drives the story and resolves the problem**, a clear want/need and flaw, and a theme that will be *carried by action rather than announced*. For nonfiction, narrow the topic to one a child can hold and build the **source plan** (what facts the book asserts and where each comes from) that the truth gate (Gate B) will later verify.

## When to Use

- After Stage 0, before structuring or drafting.
- When a draft feels flat, passive, or preachy and the foundation needs a reset.

## Inputs / Context

- The Stage 0 project spec + convention contract.
- For fiction: any character/world ideas the author has.
- For nonfiction: the subject and any source material the author has gathered.

## Constraints

**Must:**
- Route to the matching workshop prompt for the form, plus `domain-childrens-writing/craft-tools/childrens_character_creation.md` for the protagonist.
- Make child agency explicit: name the climactic choice/action the **child** (not an adult) takes.
- State the theme as something the *plot demonstrates*, with no stated-moral sentence.
- For nonfiction: produce a source plan — a list of the specific facts the book will assert, each tagged with a source or marked `VERIFY` (to be found before drafting). Never supply facts from memory as if sourced.

**Must Not:**
- Hand the protagonist's victory to a parent, teacher, or rescuer.
- Phrase the theme as a lesson ("learns that kindness matters").
- For nonfiction, assert any date, quote, name, or figure without a source tag.

## Instructions

1. Route to the form's workshop prompt (e.g., `fiction-workshops/childrens_middle_grade_fiction_workshop.md`) for premise + foundation.
2. Run `craft-tools/childrens_character_creation.md` to build/audit the protagonist: want vs. need, flaw, voice, and the **agency moment** (the climactic action the child takes).
3. Draft the theme as a one-line statement of *what the story proves through events* — then confirm no character will say it aloud.
4. **If nonfiction:** narrow the topic to a single child-holdable angle; build the source plan table (claim → source | `VERIFY`).
5. **If writing across difference:** note the identities depicted and that the across-difference audit will run in Stage 4 — do not attempt to resolve authenticity here.

## Output Format

```
CONCEPT FOUNDATION
- Premise: ...
- Protagonist: name, age, want, need, flaw, voice note
- AGENCY MOMENT (child-driven climax): ...
- Theme (carried by action): ...   [confirm: no stated moral]

NONFICTION ONLY — SOURCE PLAN
| Claim the book asserts | Source | Status |
|------------------------|--------|--------|
| ...                    | ...    | sourced | VERIFY |

ROUTED TO: domain-childrens-writing/...
```

## Verification Checklist (the orchestrator gates on this)

- [ ] The climax is resolved by the **child protagonist's** choice or action, not an adult.
- [ ] The protagonist has a want, a need, and a flaw — not just a personality.
- [ ] The theme is stated as something the plot demonstrates; no character announces it.
- [ ] (NF) Every asserted fact has a source tag or is marked `VERIFY`; none supplied from memory.
- [ ] (Across difference) The audit add-on is flagged for Stage 4.

## False-Positive Prevention

- **A "strong" protagonist who is actually passive** — reacts, is rescued, or is carried by coincidence. Require a concrete climactic action the child takes.
- **A theme smuggled in as a moral.** If you can quote a character delivering the lesson, cut it; let events prove it.
- **Nonfiction "facts" that are really memory.** A plausible date is not a sourced date. Mark `VERIFY`.
- **Resolving representation here.** Authenticity is not settled by good intentions; defer to the Stage 4 audit and a human reader.
