---
title: "Chunk a Project So Pieces Fit Available Calendar Blocks"
category: productivity/deep-work
description: "Break a project into chunks sized to the user's real free calendar blocks — not ideal 2-hour blocks — so each week's actual available time maps to a concrete piece of the project and the user stops trying to fit 90-minute work into 40-minute gaps."
techniques:
  - ST-01
  - ST-02
  - DS-01
  - CM-02
  - RT-02
  - QA-01
difficulty: intermediate
tags:
  - deep-work
  - chunking
  - project-planning
  - calendar
updated: "2026-04-20"
related_prompts:
  - domain-productivity/deep-work/deepwork_calendar_audit.md
  - domain-productivity/deep-work/deepwork_decompose_complex_task.md
  - domain-productivity/deep-work/deepwork_match_tasks_to_calendar.md
  - domain-engineering-workflows/ai-patterns/ai_pattern_agent_task_first_delegation_spec.md
---

# Chunk a Project So Pieces Fit Available Calendar Blocks

**Objective:** Take a project and a calendar and output a chunking plan where every chunk is sized to a real free block on the user's calendar within the next 2 weeks. Chunks the calendar cannot accommodate are rejected and rechunked.

**When to use:** When a project has been "in progress" for weeks but never advances. When chunks feel too big to start. Before committing a delivery date against a fixed calendar.

**Audience:** The individual doing the work, not a project manager planning for a team.

---

## Inputs Required

1. **Project name and definition of done.** One sentence each. "Done" must be something the user could point at as finished.
2. **An inventory of the free blocks on the user's calendar for the next 2 weeks.** Length and day of each. From `deepwork_calendar_audit.md` if available.
3. **Usable attention span and context-reload cost** from the focus-parameters prompt.
4. **The user's first-pass list of what this project involves.** Any level of detail.
5. **External deadlines or dependencies.** Dates, not vibes.

If input 2 shows fewer than 4 free blocks in 2 weeks, say so and state that chunking cannot compensate for a destroyed calendar — that must be fixed first.

---

## Instructions

1. **Compute the chunk-size ceiling.** Max = largest free block − reload cost. Ceiling for this project is the smaller of (attention span) and (max free block − reload).

2. **Take input 4 and restate each item as a chunk with three fields:** name, expected minutes, physical output. Expected minutes must be ≤ ceiling. If larger, split.

3. **Order chunks by dependency, not priority.** A chunk that unblocks others goes first even if less important.

4. **Assign each chunk to a specific free block** on the calendar by day and time. Leave a named buffer of reload cost between chunks on the same day.

5. **Identify chunks that don't fit anywhere in the next 2 weeks.** These are overflow. Either:
   - Shrink the chunk further
   - Push to the following period with a named trigger date
   - Drop from scope — explicitly

   Do not pretend an overflow chunk will "find time."

6. **Write the "if a block is lost" rule.** When a block disappears (meeting added, sickness), which chunk drops or defers? Decide in advance so the plan degrades gracefully.

7. **State the one assumption most likely to kill the plan.** Often it's "the chunks will take the minutes I estimated." Make the risk visible.

---

## Output Format

```
## Chunk Ceiling
- Usable attention span: NN min
- Max reload-adjusted block this period: NN min
- Ceiling per chunk: NN min

## Chunk Plan
| # | Chunk | Est min | Physical output | Depends on | Block (day/time) |
|---|---|---|---|---|---|
| 1 | ... | ... | ... | — | Tue 9:00–9:40 |
| ... |

## Overflow
- [chunk] — reason — trigger for rescheduling: [...]
- (or: "None.")

## Dropped From Scope
- [chunk or sub-goal dropped, stated plainly]

## If-A-Block-Is-Lost Rule
[Rank the chunks by drop order. First lost block drops chunk X.]

## Loadbearing Assumption
[The one thing that, if wrong, breaks this plan.]
```

---

## Constraints

**Must:**
- Every scheduled chunk fits in its assigned block with reload buffer.
- Every chunk has a physical output, not a verb-noun ("continue design").
- Overflow and dropped scope are stated explicitly.
- Dependency order trumps priority order.

**Must not:**
- Assume "I'll find time somewhere" for unscheduled chunks.
- Plan beyond 2 weeks — uncertainty eats further planning.
- Split a chunk so small it produces no physical output.
- Schedule chunks into blocks marked non-negotiable or protected for other projects.

---

## False-Positive Prevention

- **Ideal-block fantasy:** The user will be tempted to say "I just need a 3-hour block for this." Reject. Either the block exists in input 2 or the chunk is wrong.
- **Estimation optimism:** Self-estimates run 30–100% low. If the user insists a chunk is 30 min, allocate 45 and mark the excess as buffer. Name the adjustment.
- **Silent scope expansion:** A chunk that appears in the list but not in input 4 is scope creep. Flag it.
- **Uniform chunking:** Not every chunk is the same size. Forcing "all 45-min chunks" will hide complexity. Let chunks vary within the ceiling.

---

## Self-Verification (before finalizing)

- [ ] Chunk ceiling computed from real inputs.
- [ ] Every scheduled chunk ≤ ceiling.
- [ ] Each chunk has a physical output.
- [ ] Dependencies ordered correctly.
- [ ] Overflow or dropped scope stated explicitly.
- [ ] If-a-block-is-lost rule present.
- [ ] Loadbearing assumption named.
