---
title: "User Story Splitting — Vertical Slices That Each Deliver Value"
category: product-management/prompts
description: "Split an oversized user story into slices that are each independently valuable, testable and shippable: nine named splitting patterns applied in order of preference, a vertical-slice check that rejects layer-based splits, acceptance criteria per slice, and a stated first slice that could ship alone. Refuses horizontal splits by technical layer and slices whose value cannot be stated."
techniques:
  - ST-02
  - CM-03
  - NE-09
  - QA-04
  - OC-03
difficulty: intermediate
tags:
  - user-stories
  - story-splitting
  - vertical-slice
  - backlog-refinement
  - acceptance-criteria
updated: "2026-09-22"
related_prompts:
  - domain-idea-to-product/stage-7-prd-authoring/prd_to_epic_feature_decomposer.md
  - domain-product-management/prompts/product_create_prd.md
  - domain-engineering-workflows/workflows/workflow_definition_of_done_builder.md
---

# User Story Splitting

**Objective:** Split a story too large for one iteration into slices that are each
**independently valuable, testable and shippable** — using nine named patterns tried in
order of preference, a vertical-slice check that rejects splits by technical layer,
acceptance criteria per slice, and a nominated first slice that could ship on its own.
Horizontal splits and slices with no statable value are refused.

**When to Use:**
- A story will not fit in one iteration and needs breaking down.
- Refinement keeps producing stories called "backend work" and "frontend work".
- A team is blocked because three stories must all land before anything is usable.
- An epic has been decomposed into features and the features are still too big.

**When NOT to use:**
- You are decomposing at the level **above** stories — a PRD into epics and features —
  that is
  `../../domain-idea-to-product/stage-7-prd-authoring/prd_to_epic_feature_decomposer.md`.
  This prompt is the next level down and picks up where it stops.
- You are writing the spec — that is `product_create_prd.md`.
- You need testable acceptance criteria as such — that is
  `../../domain-engineering-workflows/workflows/workflow_definition_of_done_builder.md`,
  which this prompt calls for the per-slice criteria.
- You are doing a learning exercise in reconstructing stories from a system — that is
  `../../domain-learning-coding/learning_user_story_reconstruction.md`.
- You need sprint capacity planning — that is `product_delivery_sprint_planner.md`.

---

## Context Gathering

1. **The story as it stands**
   - "The story, its acceptance criteria if any, and the estimate that made you split
     it."
   - "Who is the user, and what are they trying to accomplish?"

2. **Where the size is**
   - "Which part is big — the number of cases, the unknowns, the integrations, the data
     migration, the UI?"
   - "What is genuinely uncertain, versus merely large?"

3. **The value**
   - "If the user got only the simplest version of this working, would that be useful to
     them?"
   - "Which case matters most? Which is rarest?"

4. **Constraints**
   - "Anything that must ship together for legal, contractual or data-integrity
     reasons?"
   - "Is there a release the whole thing is committed to?"

The distinction between *uncertain* and *large* decides the pattern. A large, well-
understood story splits by workflow step or by case. An uncertain one splits by spiking
the unknown first, and that slice's value is knowledge rather than function — which is
legitimate, and must be labelled.

---

## Method

### Step 1 — Check it actually needs splitting

Two stories genuinely do not: a story whose parts cannot be separated without breaking
a data-integrity or legal constraint, and a story that is already small and merely
poorly estimated. Splitting a story that does not need it creates coordination cost and
a set of slices nobody can ship alone.

If a hard constraint forces one release, say so and split the *work* for tracking while
keeping one release gate — but be honest that this is work breakdown, not story
splitting.

### Step 2 — Apply the patterns in order of preference

Try them in this order. The earlier patterns tend to produce slices with clearer
independent value.

| # | Pattern | Split by | Good when |
|---|---|---|---|
| 1 | **Workflow steps** | The sequence the user moves through | A multi-step process; ship the happy path end to end first |
| 2 | **Business rule variations** | The rules that apply | Many conditions; ship the common rule, add the exceptions |
| 3 | **Happy path / edge cases** | Success first, then the failures | Lots of error handling; the happy path is often most of the value |
| 4 | **Data variations** | Types, formats, sources | "Supports all file formats" → support the one they actually use |
| 5 | **Effort of operations** | Create, read, update, delete | CRUD-shaped work; read-only first is frequently shippable |
| 6 | **Simple / complex** | The simplest version that works | A general solution where a specific one would already help |
| 7 | **Defer performance** | Correct first, fast second | Optimisation is a separate, measurable slice |
| 8 | **Defer interface polish** | Function first, then the designed UI | Only where a plain interface is genuinely usable |
| 9 | **Spike** | Learn, then build | Real uncertainty. The slice's output is a decision, and it is time-boxed |

Two notes on the last two. Pattern 8 is frequently abused to produce an unusable slice
that "works but looks bad" and ships to nobody — apply it only when the plain version is
genuinely usable by a real user. Pattern 9 is a legitimate slice whose deliverable is
knowledge; it must be time-boxed and must state the decision it will produce, or it
becomes open-ended research.

### Step 3 — Run the vertical-slice check on every slice

**This is the check that makes splitting worth doing.** Each slice must cut through
every layer it needs — data, logic, interface — so that someone can use it.

| Horizontal (refused) | Vertical (accepted) |
|---|---|
| "Create the database schema" | "A user can save one draft and see it on their next visit" |
| "Build the API endpoints" | "A user can search by name and get exact matches" |
| "Add the frontend" | "A user can export the current view as CSV" |
| "Write the validation layer" | "A user is told which field is wrong before submitting" |

The test, stated as a question to ask of each slice: **when this slice is done, what can
a user do that they could not do before?** If the answer is "nothing yet, but the next
slice needs it", the split is horizontal. Horizontal slices produce the pattern where
three stories must all land before anything is usable, which is the problem splitting
was supposed to solve.

The one exception is the spike, whose answer is "we now know X", stated as a decision.

### Step 4 — Give each slice acceptance criteria and independent value

Per slice:

| Slice | What a user can now do | Acceptance criteria | Depends on | Could ship alone? |
|---|---|---|---|---|

Use `../../domain-engineering-workflows/workflows/workflow_definition_of_done_builder.md`
for the criteria — it converts fuzzy deliverables into testable Given/When/Then
conditions, and a slice with untestable criteria will be argued about at review.

The **depends on** column should be mostly empty. If every slice depends on the previous
one, you have sequenced tasks rather than split a story, and none of them can be
reordered, dropped or shipped early — which are the three benefits splitting buys.

### Step 5 — Nominate the first slice, and say what it would prove

One slice that could ship alone, first. State what shipping it would teach you: whether
anyone uses it, whether the approach holds, whether the integration works. A first slice
with nothing to learn is a first slice chosen by convenience.

### Step 6 — Check the slices still add up

Two failure modes to look for:

- **Lost scope.** Compare the union of slices against the original story. Anything
  missing is either deliberately descoped (record it) or accidentally dropped.
- **Gained scope.** Splitting invites elaboration; each slice acquires refinements the
  original never asked for. Compare the total estimate against the original — if it has
  grown materially, the elaboration is the cause.

---

## Output Format

```markdown
## Story split — [original story]

**Original:** As a [user], I want [capability], so that [value]
**Estimate:** [x] · **Where the size is:** [cases / unknowns / integrations / data / UI]
**Genuinely uncertain, or merely large:** [which]

### Needs splitting?
[yes / no — if a hard constraint forces one release, say so: this is then work breakdown]

### Pattern applied
**[#n — name]** — because [reason]
*Patterns tried and rejected:* [n: why]

### Slices
| # | Slice | What a user can now do | Acceptance criteria | Depends on | Ships alone? |
|---|---|---|---|---|---|

### Vertical-slice check
| Slice | "What can a user now do?" answered? | Verdict |
|---|---|---|
*Any slice answering "nothing yet" is horizontal and must be re-split.*

### First slice
**[#n]** — ships first because [reason]
**What shipping it would teach us:** [the specific learning]

### Adds-up check
- Union of slices vs original: [complete / descoped: ... / dropped: ...]
- Total estimate vs original: [x vs y — if grown, the elaboration is: ...]
```

---

## Verification

- [ ] The need to split was checked, not assumed
- [ ] Patterns were tried in order and the chosen one is named with a reason
- [ ] Every slice answers "what can a user now do?" — or is a time-boxed spike stating
      the decision it produces
- [ ] No slice is a technical layer
- [ ] Every slice has testable acceptance criteria
- [ ] The dependency column is mostly empty
- [ ] A first slice is nominated with a stated learning
- [ ] The union of slices is compared against the original for lost scope
- [ ] Total estimate is compared against the original for gained scope

**False-positive prevention.** The dominant failure is the horizontal split, and it
survives because it is the easiest one to produce — the layers are already visible in
the codebase. It converts one too-large story into four stories that must all complete
before anyone benefits, which is strictly worse than not splitting: same delivery date,
more coordination, and a burn-down chart that looks like progress. Apply the
"what can a user now do?" test to every slice, out loud, and re-split any slice whose
answer is about the next slice.

The second failure is the unusable simplest version. Pattern 8 — defer the interface —
produces a slice that technically functions and that no real user can use, so it ships
behind a flag and waits for the polish anyway. The value was never independent. Only use
it where the plain version is genuinely usable.

The third is over-splitting. Eight slices for a two-week story produces coordination
overhead exceeding the benefit, and a review meeting per slice. Three to five is usually
right; if you have more, some belong merged.

The fourth is silent scope growth. Each slice acquires refinements during splitting, and
the total quietly exceeds the original estimate by half. Run the adds-up check and name
the elaboration.

---

## Related

- `../../domain-idea-to-product/stage-7-prd-authoring/prd_to_epic_feature_decomposer.md` — the level above this
- `product_create_prd.md` — the spec the story came from
- `../../domain-engineering-workflows/workflows/workflow_definition_of_done_builder.md` — per-slice acceptance criteria
- `product_delivery_sprint_planner.md` — sequencing the slices into an iteration
- `product_planning_coding_roadmap.md` — the larger sequence
