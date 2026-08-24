---
title: "Android Estimation & Milestone Plan"
category: mobile-development
description: "Turn an MVP scope and feature specs into an estimable work breakdown and a realistic, risk-adjusted milestone timeline for Android — vertical-slice tasks, estimation-method selection, Android-specific cost drivers, critical path, MVP→V1→V2 milestones with exit criteria, confidence ranges, solo vs team capacity, and AI-agent impact on estimates."
techniques:
  - ST-01
  - ST-02
  - RT-02
  - DS-06
  - AG-12
  - NE-02
difficulty: intermediate
tags:
  - android
  - mobile-development
  - estimation
  - planning
  - milestones
  - roadmap
  - solo-developer
  - project-management
updated: "2026-06-06"
related_prompts:
  - android_mvp_scope_and_release_roadmap.md
  - android_feature_specification.md
  - android_ai_agent_workflow.md
---

# Android Estimation & Milestone Plan

**Objective:** Convert a defined MVP scope and a set of feature specifications into (a) an estimable work breakdown of vertical-slice tasks, (b) effort estimates produced with an explicitly chosen estimation method, (c) a dependency-sequenced critical path, and (d) a realistic, risk-adjusted milestone timeline tied to the MVP→V1→V2 roadmap with exit criteria per milestone. Estimates are delivered as confidence ranges, not single numbers, and account for Android-specific cost drivers that are routinely under-estimated.

**When to Use:** Use this prompt once you have an MVP scope and feature specs and need to answer "how long, in what order, and with what confidence?" — for a solo developer planning evenings/weekends or a small team planning sprints. Use it again whenever scope changes materially or actuals diverge from estimates (re-estimation cadence). Do **not** use it to invent scope; it consumes scope, it does not create it.

**Sequence Map:** Use after `android_mvp_scope_and_release_roadmap.md` (which defines what's in/out and the MVP→V1→V2 cut lines) and `android_feature_specification.md` (which defines each feature in enough detail to estimate); use before sustained build work and sprint commitments.

**Important context:** Software estimates are forecasts under uncertainty, not promises. The most common Android estimation failure is estimating only the "happy-path feature code" while ignoring the surrounding tax: Gradle/CI setup, multi-module wiring, release signing and Play review latency, the device/OS QA matrix, offline sync, and the empty/error/loading states that quietly double a screen's cost. The second most common failure is the single-number estimate that hides its own uncertainty. This prompt forces vertical slices (so each task is independently shippable and testable), an explicit estimation method, named Android cost drivers, and confidence ranges. It treats AI-agent assistance as a real but bounded multiplier — fast on boilerplate and near code, slow/risky on ambiguous or novel work.

---

## Context Gathering

1. **Inputs available:**
   - "Do you have an MVP scope doc (in/out, cut lines) and feature specs? Paste or summarize them."
   - "What is the MVP→V1→V2 split already decided in the roadmap?"

2. **Capacity:**
   - "Solo or team? If solo, how many *focused* hours/week realistically (not calendar hours)?"
   - "If team, how many engineers, their Android experience, and any shared/part-time allocation?"
   - "Any hard deadline or external date (event, contract, store feature window)?"

3. **Project shape & risk:**
   - "Greenfield or existing codebase? Existing CI/CD, signing, and module structure, or starting from zero?"
   - "Which features involve unfamiliar tech, third-party SDKs, payments, or background/offline sync?"
   - "Will an AI coding agent be part of the workflow? For which kinds of tasks?"

4. **Estimation appetite:**
   - "Do you want t-shirt sizing (fast, coarse), story points (relative, team), or ideal-engineering-days (calendarable)?"

---

## Instructions

Proceed in phases with **CHECKPOINT** gates. Present each artifact before continuing.

---

### Phase 1: Work Breakdown into vertical slices

Decompose each feature spec into **estimable vertical-slice tasks** — each slice cuts through UI + logic + data so it is independently demonstrable, not a horizontal "do all the UI" / "do all the backend" layer. A good slice is testable and shippable behind a flag.

| Feature | Vertical slice (task) | Includes (UI / logic / data) | Independently testable? |
|---|---|---|---|
| Auth | Email/password sign-in (happy path) | Login screen + VM + auth repo call | Yes |
| Auth | Sign-in error & loading states | Error/empty/loading UI + retry | Yes |
| Feed | List render from cache | List screen + VM + Room read | Yes |
| Feed | Pull-to-refresh + network merge | Refresh + sync + conflict rules | Yes |

**Rules:**
- Split any task estimated larger than ~2 ideal-engineering-days; large estimates hide unknowns.
- Each user-facing screen produces *at least* a happy-path slice **and** an empty/error/loading slice — never one task per screen.
- Add explicit slices for cross-cutting setup (see Phase 3 cost drivers); do not fold them invisibly into feature tasks.

**CHECKPOINT 1:** Present the full slice list before estimating. Confirm nothing material is missing.

---

### Phase 2: Choose an estimation method

Pick one primary method; the choice drives everything downstream.

| Method | What it is | Best when | Watch out for |
|---|---|---|---|
| **T-shirt sizing (S/M/L/XL)** | Coarse buckets, optionally mapped to day ranges | Very early, solo, high uncertainty, fast triage | Too coarse for a committed timeline; map to ranges before scheduling |
| **Story points (relative)** | Fibonacci-ish relative effort, velocity-based | Small team with shared history/velocity | Meaningless without a stable team velocity; don't equate points to hours |
| **Ideal engineering-days** | Effort in uninterrupted dev-days | Need a calendar date; mature understanding of tasks | "Ideal" ≠ calendar — apply capacity/focus factor (Phase 6) |

Map your chosen unit to a range per slice (e.g., S = 0.25–0.5 day, M = 0.5–1.5 days, L = 1.5–3 days, XL = split it). Estimate **ranges, not points** — record low / likely / high.

---

### Phase 3: Add Android-specific cost drivers (the under-estimated tax)

Explicitly estimate these as their own line items. They are the usual reason Android projects slip.

| Cost driver | Why it's under-estimated | Plan as |
|---|---|---|
| Gradle / build / CI setup | "It's just config" until version catalogs, variants, and caching fight you | Dedicated slice, range, front-loaded |
| Multi-module wiring | DI graph, navigation, and API/impl boundaries across modules | Per-module wiring slice |
| Release & signing | Keystore, Play App Signing, upload key, flavors | One-time slice + buffer |
| **Play review latency** | Calendar time you don't control (review can take hours to days; policy/closed-test phases add days) | Calendar buffer in milestones, **not** effort |
| Device / OS / QA matrix | Multiple OS versions, screen sizes, foldables, OEM quirks | QA slice per milestone scaled to matrix size |
| Offline / sync | Conflict resolution, retries, partial failures, migrations | Higher range + risk flag |
| Empty / error / loading states | Designed and discussed only for the happy path | Already its own slice (Phase 1) |
| Edge cases & permissions | Runtime permission flows, denial paths, deep links | Per-feature edge-case slice |
| Migrations (Room/data/proto) | Discovered late, blocking releases | Slice per schema change |

---

### Phase 4: Dependency sequencing & critical path

Order slices by dependency, then identify the critical path (the longest chain of dependent work that sets the floor on timeline).

```
[Project/Gradle/CI setup]
        │
        ▼
[Core module + DI + navigation skeleton]
        │
   ┌────┴─────────────┐
   ▼                  ▼
[Auth happy path]   [Design system / theme]   (parallel)
   │                  │
   ▼                  ▼
[Auth states]       [Feed list from cache]
   └────────┬─────────┘
            ▼
   [Feed refresh + sync]  ◀── critical path runs through sync (highest risk)
            ▼
   [Release/signing + QA matrix]
```

- Mark which slices are parallelizable (matters for team capacity, irrelevant for solo).
- Flag the riskiest slice on the critical path — it deserves the widest range and the earliest spike.

---

### Phase 5: Milestones tied to MVP→V1→V2, with exit criteria

Bind slices to release milestones from the roadmap. Every milestone gets explicit **exit criteria** (a definition of done), not just a date.

| Milestone | Scope (slice groups) | Exit criteria | Effort (low–high) | Calendar buffer |
|---|---|---|---|---|
| **M0 — Foundation** | Gradle/CI, signing, core/DI/nav, design system | App builds in CI; signed debug+release; one screen renders; tests run green | _x–y days_ | — |
| **M1 — MVP (internal)** | Auth + 1 core feature, all states, offline read | All MVP slices demoable; crash-free on QA matrix; a11y/i18n plan honored | _x–y days_ | QA cycle |
| **M2 — MVP (Play closed test)** | Store listing, release build, telemetry | Uploaded; closed testers active; **Play review/closed-test latency** absorbed | _x–y days_ | **+ review latency** |
| **M3 — V1 (public)** | Polish, remaining states, perf pass | Public release exit criteria met; rollback plan ready | _x–y days_ | + staged rollout |
| **M4 — V2** | Deferred features, scale work | Per roadmap V2 cut line | _x–y days_ | — |

**CHECKPOINT 2:** Present milestones with exit criteria and ranges before risk-adjustment.

---

### Phase 6: Risk-adjusted estimates & capacity

Convert effort ranges into a calendar forecast.

1. **Confidence ranges, not single numbers.** Report each milestone as low / likely / high (e.g., 12 / 18 / 28 days). State the assumptions behind "likely."
2. **Capacity / velocity factor:**
   - **Solo:** convert *focused* hours/week to ideal-days/week (focus factor typically ~0.5–0.7 of calendar time after meetings, life, context-switching). Calendar weeks = ideal-days ÷ (focused ideal-days per week).
   - **Team:** use observed velocity if it exists; otherwise estimate conservatively for the first 1–2 sprints, then re-estimate from actuals. Account for ramp-up, code review, and coordination overhead (team output is sub-linear in headcount).
3. **Risk uplift:** widen ranges for slices flagged risky (sync, payments, unfamiliar SDKs). Do not collapse a wide range to its optimistic end to fit a date.
4. **Calendar buffers separate from effort:** Play review latency, QA cycles, and staged rollout are *calendar* costs added to milestone dates, not effort added to tasks.

---

### Phase 7: AI-agent impact & re-estimation cadence

- **AI-agent assistance adjusts — does not erase — estimates.** It tends to *compress* boilerplate, well-specified, "near existing code" tasks (scaffolding, tests for clear specs, repetitive UI, migrations from a pattern) and *adds little or even adds risk/review overhead* on ambiguous, novel, cross-cutting, or judgment-heavy tasks (architecture, tricky sync, subtle UX, security). Apply the multiplier per slice, not globally. See `android_ai_agent_workflow.md` for how the agent work-loop affects which slices are AI-friendly.
- Tag each slice: **AI-accelerated / AI-assisted / human-led**, and adjust its range accordingly (review time counts).
- **Re-estimation cadence:** re-estimate remaining work at every milestone boundary and after any slice finishes ≥ ~40% over/under its likely estimate. Track actual vs. estimate to calibrate future ranges. Estimates are living, not signed in stone.

---

## Expected Output

1. **Vertical-slice work breakdown** — feature → estimable, testable slices including state slices and setup slices.
2. **Estimation method choice** — with unit-to-range mapping.
3. **Android cost-driver line items** — explicit estimates for the usually-forgotten tax.
4. **Dependency graph & critical path** — with parallelizable slices and the riskiest path slice flagged.
5. **Milestone plan** — MVP→V1→V2 milestones with exit criteria and effort ranges.
6. **Risk-adjusted forecast** — low/likely/high per milestone, capacity factor applied, calendar buffers separated.
7. **AI-impact tagging & re-estimation cadence** — per-slice AI tag and the cadence/trigger rules.

---

## CRITICAL: Verification Requirements

- [ ] Tasks are vertical slices (UI+logic+data), each independently testable — not horizontal layers.
- [ ] Every user-facing screen has both a happy-path slice and an empty/error/loading slice.
- [ ] An estimation method is chosen explicitly and mapped to ranges.
- [ ] Android cost drivers (Gradle/CI, multi-module wiring, signing/release, Play review latency, device/QA matrix, offline-sync, edge/permission states, migrations) appear as explicit line items.
- [ ] A dependency-sequenced critical path is identified, with the riskiest slice flagged.
- [ ] Milestones are tied to MVP→V1→V2 and each has concrete exit criteria, not just dates.
- [ ] Estimates are confidence ranges (low/likely/high), never single numbers.
- [ ] Capacity/velocity factor is applied (focus factor for solo; conservative velocity + coordination overhead for team).
- [ ] Play review latency and QA/rollout are treated as calendar buffers, not effort.
- [ ] Each slice is tagged for AI-agent impact, and a re-estimation cadence/trigger is defined.

## False-Positive Prevention

- ❌ Do NOT estimate only happy-path feature code — the surrounding Android tax (CI, signing, states, sync, QA matrix) is most of the slip.
- ❌ Do NOT deliver single-number estimates; they hide uncertainty and become false promises.
- ❌ Do NOT treat ideal-engineering-days as calendar days — apply the capacity/focus factor.
- ❌ Do NOT assume team output scales linearly with headcount (coordination + review overhead are real).
- ❌ Do NOT fold Play review latency into task effort — it's calendar time you don't control.
- ❌ Do NOT assume AI assistance uniformly speeds everything; it can add review/risk overhead on ambiguous or novel work.
- ❌ Do NOT freeze estimates — re-estimate at milestone boundaries and on large variances.
- ✅ DO break work into independently testable vertical slices and split anything over ~2 ideal-days.
- ✅ DO name Android cost drivers as their own line items.
- ✅ DO report low/likely/high ranges with stated assumptions.
- ✅ DO tie milestones to exit criteria and the MVP→V1→V2 roadmap.
- ✅ DO separate effort from calendar buffers and apply per-slice AI tagging.

## Techniques Used

- **ST-01** (Clear Objective Statement): Singular goal — scope/specs → estimated breakdown + milestone timeline.
- **ST-02** (Sequential Instructions): Breakdown → method → cost drivers → critical path → milestones → risk → AI/cadence.
- **RT-02** (Multi-Dimensional Analysis): Each slice analyzed across effort, dependency, risk, capacity, and AI-fit.
- **DS-06** (Prioritized Findings/Output): Slices sequenced by dependency/critical path; cost drivers surfaced by impact.
- **AG-12** (Quantitative Metrics): Confidence ranges, capacity/focus factors, and milestone effort bands.
- **NE-02** (Phased Workflow Architecture): Checkpoint gates between breakdown, milestones, and risk-adjustment.

## Related Prompts

- [android_mvp_scope_and_release_roadmap.md](android_mvp_scope_and_release_roadmap.md) — Defines the MVP→V1→V2 scope this plan estimates.
- [android_feature_specification.md](android_feature_specification.md) — Provides the per-feature detail required to estimate slices.
- [android_ai_agent_workflow.md](android_ai_agent_workflow.md) — Describes the AI-agent work loop that informs per-slice AI tagging.
