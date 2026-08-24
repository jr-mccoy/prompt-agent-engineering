---
title: "Code Evolution Visualization — Teach a Codebase's History Through Timelines and Heatmaps"
category: "learning-coding"
description: "Turn a codebase's version-control history into accurate, teachable visualizations — phase timelines, activity heatmaps, metric trends, and architecture snapshots — so a new contributor understands how and why the project evolved."
techniques:
  - ST-01
  - ST-02
  - RT-05
  - DS-02
  - QA-01
difficulty: intermediate
tags:
  - learning-coding
  - code-evolution
  - visualization
  - onboarding
  - version-control
updated: "2026-06-07"
related_prompts:
  - domain-learning-coding/learning_codebase_trivia_game.md
  - domain-learning-coding/learning_mini_lesson_generation.md
  - domain-software-engineering/analysis/evolution/evolution_code_churn_analysis.md
  - domain-software-engineering/analysis/evolution/evolution_technical_debt_estimation.md
---

# Code Evolution Visualization

**Objective:** Turn a codebase's real version-control history into accurate, teachable visualizations — phase timelines, activity heatmaps, metric trends, and architecture snapshots — so a new contributor understands how and why the project evolved.

**When to use:**
- Onboarding someone who needs historical context for a long-running project.
- Preparing for a major refactor or modernization and needing to see how the code got here.
- Documenting a legacy codebase you've inherited.
- Explaining the ROI of past technical investment to stakeholders.

**When NOT to use:**
- Brand-new projects with little history to visualize.
- When you have no access to git history or metrics and would have to fabricate dates/numbers.
- Real-time performance analysis (use performance prompts).

**Audience:** New team members, tech leads, architects, and engineers inheriting legacy code.

---

## Inputs / Context

The user supplies:
1. **History data** — git log output, churn/metric reports, release tags, or a repo reference, pasted wrapped in a named tag, e.g. `<history>...</history>`.
2. **Optional architecture snapshots** or ADRs at key points.
3. **Audience and purpose** (onboarding, refactor planning, exec summary).
4. **Time window** of interest.
5. **Optional:** known milestones, incidents, or refactor names to anchor the narrative.

Reference the supplied data by its tag name when stating any date, count, or metric.

---

## Constraints

### Must
- Base every date, count, and metric on the supplied history data; if a figure isn't available, mark it **"unconfirmed — derive from repo"** rather than inventing it.
- Group the history into a small number of meaningful phases with evidence for each boundary.
- Render visualizations as readable ASCII/markdown (timelines, heatmaps, tables) unless another format is requested.
- Add narrative context (the "why") for each major milestone, tied to evidence.
- Include "questions a new contributor would ask" answered from the history.

### Must Not
- Fabricate commit counts, contributor numbers, LOC figures, or dates.
- Invent incidents, refactor codenames, or rationale not supported by the data.
- Present speculation as documented fact (label inferences as inferences).
- Bury the learning value under decoration.

---

## Instructions

1. **Read the history.** From `<history>`, extract the timeline, commit/contributor activity, file/module churn, and release/tag points. Flag gaps.
2. **Segment into phases.** Identify 3–5 phases (e.g., MVP, Growth, Scale, Modernize) and cite the evidence for each boundary (a migration, a release, an activity shift).
3. **Build the timeline.** Render a chronological view of milestones with the metrics that changed at each.
4. **Build activity heatmaps.** Show which files/modules changed most in each phase, from churn data.
5. **Plot metric trends.** Track LOC, file count, test coverage, dependency count over phases — only where data exists.
6. **Snapshot architecture.** Render the architecture at key points (if snapshots/ADRs supplied), and note what migration changed it.
7. **Add the "why."** For each milestone, give the business/technical rationale, tied to evidence; mark inferences clearly.
8. **Answer new-contributor questions.** List the "why is this like this?" questions the history explains.
9. **Self-check (verification).** Does every figure trace to the supplied data? Are inferences labeled? Are unconfirmed figures marked?

---

## False-Positive Prevention

❌ **DON'T:**
- State a commit count, LOC, coverage %, or date that isn't in the supplied data.
- Invent an incident, refactor name, or decision rationale to make the story compelling.
- Present an inference about "why" as a documented fact.
- Assume the architecture changed in a way the snapshots don't show.
- Drown the learning in ASCII art.

✅ **DO:**
- Trace every number and date to the supplied history.
- Mark missing figures "unconfirmed — derive from repo."
- Clearly distinguish documented facts from your inferences.
- Tie each phase boundary to specific evidence.
- Keep the focus on what a new contributor needs to understand.

---

## Output Format

```
# Codebase Evolution — [project]

## Summary
- Lifespan, total commits, contributors, current size [from data, or marked unconfirmed]
- Phases: [names + date ranges]

## Phase N: [name] ([dates])
### Timeline
[ASCII timeline of milestones]
### Key Metrics
| Metric | Start | End |
### Activity Heatmap
[most-changed files with bars]
### Architecture at phase end
[ASCII diagram if available]
### Why this happened
[rationale, inferences labeled]

## Questions New Contributors Ask
1. [question] → [answer from history]
```

---

## Example Output

```markdown
# Codebase Evolution — E-Commerce Platform

## Summary
- Lifespan: Mar 2021 – Present (~3.5 yrs)  | Total commits: 4,847  | Contributors: 23
- Current size: ~156,000 LOC / 892 files
- Phases: MVP (Mar–Sep 2021) → Growth (Oct 2021–Jun 2022) → Scale (Jul 2022–Mar 2023) → Modernize (Apr 2023–Present)

## Phase 1: MVP (Mar – Sep 2021)

### Timeline
Mar        Apr         May         Jun         Jul         Aug        Sep
[Init]   [Auth]   [Catalog]   [Cart]   [Checkout]   [Admin]   [v1.0 Launch]

### Key Metrics
| Metric | Start | End |
|--------|-------|-----|
| Lines of Code | 0 | 12,400 |
| Files | 0 | 89 |
| Test Coverage | 0% | 45% |
| Dependencies | 12 | 34 |

### Architecture at phase end
┌─────────────────────────────────────────┐
│            Express Monolith              │
├────────┬─────────┬────────┬─────────────┤
│  Auth  │ Product │  Cart  │    Admin     │
├────────┴─────────┴────────┴─────────────┤
│          PostgreSQL Database             │
└─────────────────────────────────────────┘

### Why this happened
Single monolith chosen for speed to first launch (inferred from commit cadence and lack of service boundaries — verify against ADR-001 if present).

## Phase 2: Growth (Oct 2021 – Jun 2022)

### Activity Heatmap (most-changed files)
controllers/productController.ts  ████████████████ 156 changes
controllers/orderController.ts    ████████████░░░░ 134 changes
services/searchService.ts (NEW)   ███████████████░ 147 changes

### Warning signs (from data)
- productController.ts grew to ~1,200 lines.
- Test coverage fell 45% → 31%.

## Phase 3: Scale (Jul 2022 – Mar 2023)

### Architecture after migration
              ┌──────────────┐
              │ API Gateway  │
              └──────┬───────┘
      ┌──────────┬───┴───┬───────────┐
   Product     Order    User     Inventory
   Service    Service  Service    Service

## Questions New Contributors Ask
1. **Why is there both `/legacy` and `/services`?** → Phase 3 migration kept legacy for reference; removal tracked for a later quarter (verify ticket).
2. **Why is `productController.ts` different from the others?** → It was written first, in Phase 1, before standards existed (see churn history).
```

---

## Verification

- [ ] Every date, count, and metric traces to the supplied history data.
- [ ] Phase boundaries are each backed by specific evidence.
- [ ] Inferences about "why" are labeled as inferences, not facts.
- [ ] Missing figures are marked "unconfirmed — derive from repo."
- [ ] No incidents, codenames, or rationale were invented.
- [ ] New-contributor questions are answered from the history.

---

## Techniques Used

- **ST-01 (Clear Objective Statement):** Frames the goal as an accurate, teachable evolution story.
- **ST-02 (Structured Sequential Instructions):** Read → segment → timeline → heatmap → trends → architecture → why → verify.
- **RT-05 (Evidence-Based Reasoning):** Requires every figure to trace to the supplied data.
- **DS-02 (Metric Specification):** Defines the specific metrics tracked over phases.
- **QA-01 (Self-Verification):** Final pass checks figures, labels inferences, marks unconfirmed.

---

## Related Prompts

- `domain-learning-coding/learning_codebase_trivia_game.md` — Source historical trivia from the same data.
- `domain-learning-coding/learning_mini_lesson_generation.md` — Turn evolution insights into lessons.
- `domain-software-engineering/analysis/evolution/evolution_code_churn_analysis.md` — Identify high-change hotspots.
- `domain-software-engineering/analysis/evolution/evolution_technical_debt_estimation.md` — Quantify debt accumulated over time.
