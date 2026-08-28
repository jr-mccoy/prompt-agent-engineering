---
title: "Personal Energy Audit"
category: productivity/deep-work
description: "Map your daily energy patterns to optimize task scheduling — identifies peak hours, energy drains, and leverage moves to align high-value work with your biological prime time"
techniques:
  - ST-01
  - ST-02
  - RT-02
  - CM-01
  - DS-06
difficulty: beginner
tags:
  - personal-development
  - energy-management
  - productivity
  - scheduling
  - biological-prime-time
updated: "2026-06-21"
related_prompts:
  - domain-productivity/bottlenecks/bottleneck_open_loop_audit.md
  - domain-productivity/deep-work/deepwork_zombie_meeting_detector.md
  - domain-personal-development/prompts/solo-dev/solo_dev_burnout_prevention.md
---

# Personal Energy Audit

**Objective:** Analyze your daily energy patterns over a week to identify your biological prime time, energy drains, and specific scheduling changes that realign your highest-value work with your highest-energy periods.

## When to Use

- Use when: you feel busy all day but unproductive, or suspect you're doing deep work at the wrong times.
- Use when: you're constantly tired despite reasonable hours, or starting a new role and want to align high-value work with peak energy from the start.
- Use this once you have an **energy-tagged schedule log** to analyze. To first clear the mental clutter that drains energy, run `domain-productivity/bottlenecks/bottleneck_open_loop_audit.md`. To reclaim energy lost to meetings, pair with `deepwork_zombie_meeting_detector.md`.
- Don't use when: the issue is sustained depletion / exhaustion edging toward burnout — route to `solo_dev_burnout_prevention.md`; this prompt optimizes scheduling, it does not treat burnout.

---

## Inputs / Context

**7-Day Schedule Log:** [Paste hourly or block-level notes for the past week. For each block: activity + perceived energy level 1-5]

Example: `Mon 9-11am: Deep coding (energy: 5), Mon 11-12pm: Meetings (energy: 2)`

**Your Role:** [Types of tasks in a typical day]
**Biggest Frustration:** [What feels wrong about your current schedule]

**Refusal / insufficiency logic:** This audit depends on real logged data. If the schedule log is missing or has no energy ratings, do not infer a generic "everyone peaks at 9am" pattern — ask the user to log at least a few days with 1–5 energy tags first. Less than ~3 days of data yields a heat map that is noise; say so and recommend continuing to log rather than over-fitting to one day. Never fabricate energy levels the user didn't report.

---

## Instructions

### Phase 1: Pattern Detection

**Energy Heat Map:**

| Day | High-Energy Blocks (4-5) | Low-Energy Blocks (1-2) |
|-----|--------------------------|-------------------------|
| Mon | ... | ... |
| Tue | ... | ... |

Surface: consistent peak times, consistent dips, energy-boosting activities, energy-draining activities, physiological patterns (post-meal, post-exercise).

### Phase 2: Task-Energy Alignment

| Task Type | Energy Needed | When You Do It Now | Best Time |
|-----------|---------------|--------------------|-----------|
| Deep work | High creative | ... | Peak hours |
| Meetings | Medium social | ... | Post-peak |
| Admin | Low | ... | Energy dips |

### Phase 3: Leverage Moves

Identify 2-4 scheduling changes ranked by impact:
- **What to change** — specific adjustment
- **Expected impact** — High/Medium/Low
- **How to implement** — practical steps

### Phase 4: Redesigned Day Template

Design an ideal day template based on the analysis.

---

### False-Positive Prevention

- ❌ Do NOT assume everyone peaks in the morning — night owls are real
- ❌ Do NOT recommend changes that ignore meeting-heavy cultures
- ❌ Do NOT treat energy as purely physical — emotional and social energy matter
- ❌ Do NOT create an "ideal schedule" impossible in the user's context
- ✅ DO identify the single highest-leverage change, not a complete overhaul
- ✅ DO distinguish between controllable and uncontrollable blocks
- ✅ DO suggest a 1-week experiment rather than permanent restructuring

---

## Expected Output

```markdown
# Personal Energy Audit: [Week of DATE]

## Energy Heat Map
| Day | High-Energy Blocks (4-5) | Low-Energy Blocks (1-2) |
|-----|--------------------------|-------------------------|
| Mon | 9-11am deep work (5)     | 2-4pm admin (2)         |
| Tue | 9-11am deep work (4)     | 1-2pm post-lunch (1)    |
| ... | ...                      | ...                     |

**Patterns:** Consistent peak 9-11am; reliable post-lunch dip 1-2pm;
meetings consistently rated 2 regardless of time of day.

## Task–Energy Alignment
| Task Type | Energy Needed | When You Do It Now | Best Time |
|-----------|---------------|--------------------|-----------|
| Deep work | High creative | scattered          | 9-11am    |
| Meetings  | Medium social | mornings (peak!)   | post-peak (after 2pm) |
| Admin     | Low           | mornings           | 1-2pm dip |

## Leverage Moves (ranked by impact)
1. **Protect 9-11am for deep work** — High impact. Decline/move morning meetings.
2. **Batch admin into the 1-2pm dip** — Medium impact. Reclaims peak hours.
3. **Cluster meetings after 2pm** — Medium impact.

## Redesigned Day Template
- 9-11am: Deep work (no meetings, notifications off)
- 11-12pm: Email / shallow tasks
- 1-2pm: Admin batch (the energy dip)
- 2-5pm: Meetings + collaborative work

## Try This for One Week
Move only Leverage Move #1. Re-log energy. Keep if peak-hour output rises.
```

---

## Verification

Before delivering the audit, confirm each of these. If any fails, fix it before responding:

- [ ] The heat map is built **only from the user's logged energy ratings** — no peak/dip was invented or assumed from a stereotype (morning-person default checked against the data).
- [ ] Peak and dip times are **grounded in the user's data**, and night-owl / non-standard patterns are respected.
- [ ] The task–energy alignment table reflects the user's **actual current timing**, not an idealized version.
- [ ] Leverage moves are **ranked by impact** and distinguish **controllable vs. uncontrollable** blocks (e.g. meeting-heavy culture).
- [ ] Exactly **one highest-leverage change** is highlighted to try first — not a full schedule overhaul.
- [ ] The redesigned template is **achievable in the user's real context**, not an impossible ideal.
- [ ] The recommendation is framed as a **1-week experiment with a re-log step**, not a permanent restructuring.

---

## Techniques Used

- **ST-01** (Clear Objective Statement) — Energy pattern analysis with actionable output
- **ST-02** (Structured Sequential Instructions) — Detection, alignment, leverage moves, template
- **RT-02** (Multi-Dimensional Analysis) — Physical, creative, social energy types
- **CM-01** (Explicit Context Framing) — Real schedule data as input
- **DS-06** (Prioritization Guidance) — Leverage moves ranked by impact

---

## Related Prompts

- [domain-productivity/bottlenecks/bottleneck_open_loop_audit.md](../bottlenecks/bottleneck_open_loop_audit.md) — Clear mental clutter that drains energy.
- [deepwork_zombie_meeting_detector.md](deepwork_zombie_meeting_detector.md) — Reclaim energy from unnecessary meetings.
- [solo_dev_burnout_prevention.md](../../domain-personal-development/prompts/solo-dev/solo_dev_burnout_prevention.md) — Prevent sustained depletion from becoming burnout (route here if exhaustion, not scheduling, is the issue).

> **Boundary note:** Energy/calendar optimization overlaps with [`domain-productivity/deep-work/`](../deep-work/) (e.g. `deepwork_calendar_audit.md`, `deepwork_focus_parameters_estimator.md`). This prompt is the personal-development entry point; link across rather than duplicating that cluster.
