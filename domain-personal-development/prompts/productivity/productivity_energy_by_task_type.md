---
title: "Match Task Types to Your Real Energy Rhythm and Make One Scheduling Change"
category: personal-development/productivity
description: "Take the user's energy rhythm and their actual task mix, sort every task type into the energy window it truly needs, expose the most expensive mismatch (a demanding task stuck in a trough), and prescribe the single scheduling swap that fixes it."
techniques:
  - ST-01
  - ST-02
  - RT-05
  - DS-06
  - QA-12
difficulty: intermediate
tags:
  - productivity
  - energy-management
  - task-scheduling
  - deep-work
  - biological-prime-time
updated: "2026-07-23"
related_prompts:
  - domain-personal-development/prompts/productivity/productivity_personal_energy_audit.md
  - domain-personal-development/prompts/productivity/productivity_focus_ritual_design.md
  - domain-personal-development/prompts/productivity/productivity_open_loop_audit.md
  - domain-personal-development/prompts/agency/agency_rapid_start_mode.md
---

# Match Task Types to Your Real Energy Rhythm and Make One Scheduling Change

**Objective:** Sort the user's real task types into the energy window each one requires, find the costliest mismatch, and prescribe one scheduling swap — not a redesigned day.

**When to use:** The user already knows roughly when they have energy (or has run `productivity_personal_energy_audit.md`) but keeps doing their hardest work at the wrong time. Useful when deep work feels like grinding, or when easy admin somehow eats the best hours. Not for discovering the energy rhythm in the first place — do the energy audit first, then bring the rhythm here.

**Audience:** An individual scheduling their own work. Not for prescribing a schedule to a team, and not clinical. If low energy is constant with no peak window at all — flat exhaustion rather than a rhythm — that is depletion, not scheduling; see `../solo-dev/solo_dev_burnout_prevention.md` and, if persistent, `domain-psychology/` and a professional.

---

## Inputs Required

1. **Energy rhythm.** The user's real daily energy shape: peak window(s), trough window(s), and any secondary lift (e.g., "peak 8–11am, hard trough 1:30–3pm, small second wind ~5pm"). If they ran `productivity_personal_energy_audit.md`, paste its heat map. If not, ask for at least a rough peak and trough grounded in the last week — do not assume a morning default.
2. **Task-type inventory.** The recurring kinds of work in a typical week, not individual tasks. 5–10 types (e.g., "writing new code," "code review," "email," "1:1s," "planning," "expense admin," "creative drafting," "data cleanup"). For each: rough hours/week.
3. **Current timing.** For each task type, roughly when the user does it now.
4. **The task that feels hardest lately.** One specific task type that has felt disproportionately draining or slow, and when they've been doing it.
5. **Fixed constraints.** Blocks the user cannot move (standing meetings, school pickup, a shared-calendar window). Required so the swap is real, not idealized.

If the task-type inventory has fewer than 4 types with timing, refuse and ask for more — a two-item list can't reveal a mismatch worth fixing.

---

## Instructions

### Step 1 — Classify each task type by its energy demand

Tag every task type from input 2 with exactly one **demand class** from this fixed taxonomy:

| Demand class | Signature | Needs |
|---|---|---|
| **Deep-create** | Novel output, sustained focus, ambiguity (writing, designing, hard coding) | Peak |
| **Deep-analyze** | Rigorous judgment, high error-cost, no creativity (review, debugging, decisions) | Peak or strong secondary |
| **Social** | Presence and warmth more than raw cognition (meetings, 1:1s, calls) | Mid / post-peak |
| **Shallow-admin** | Low-stakes, low-focus, mechanical (email, expenses, filing, data cleanup) | Trough — this is what troughs are for |
| **Learning** | Absorbing, not producing; tolerates lower energy if not urgent | Secondary lift or mild trough |

### Step 2 — Overlay demand on the rhythm

Build a table mapping each task type to: its demand class, its needed window, its current window (input 3), and a **fit verdict**:

- **Fit** — currently done in the window it needs.
- **Wasteful** — a Deep task placed in a peak, fine — but a Shallow/Social task is *also* eating a peak, crowding it.
- **Mismatch** — a Deep-create or Deep-analyze task is running in a trough, or a demanding task collides with a fixed low-energy block.

Every verdict cites the specific rhythm window and current timing.

### Step 3 — Rank mismatches by cost

Cost = (weekly hours of the task) × (severity of the mismatch). A five-hour deep-create block stuck in the afternoon trough outranks a one-hour one. Peak hours spent on shallow-admin are a second, quieter cost — flag them but they rank below deep-work-in-trough.

### Step 4 — Diagnose the input-4 task

Locate the "hardest lately" task on the Step 2 table. Confirm or correct the user's instinct: it usually feels hard because it's a Deep class running in a trough or against a fixed block — not because the user is slipping. Name the exact window collision in one sentence.

### Step 5 — Prescribe the one swap

Pick the single highest-cost mismatch and design one **swap**: move the demanding task into a peak/secondary window, and move whatever currently sits there (usually shallow-admin) into the vacated trough. Respect every fixed constraint from input 5 — if the peak is blocked, use the strongest available secondary window and say so. State the swap as a concrete calendar change with exact times, plus what moves out to make room. One swap, not a rebuilt week.

---

## Constraints

### Must
- Tag every task type with exactly one demand class from the fixed taxonomy.
- Ground every fit verdict in the user's stated rhythm window and current timing.
- Rank mismatches by (hours × severity) and act on the top one only.
- Honor every fixed constraint from input 5 in the prescribed swap.
- Produce exactly one swap, stated as a specific calendar change with times.

### Must Not
- Assume a morning-peak default; use the user's actual rhythm.
- Redesign the whole day or output an "ideal schedule" — one swap.
- Recommend adding more deep-work hours; this reallocates existing hours.
- Treat energy as purely physical — social and creative demand differ, per the taxonomy.
- Moralize about the user "wasting" their peak; observe and reassign.

---

## False-Positive Prevention

1. **Don't force a peak-only prescription.** Not every task needs the peak. Shallow-admin belongs in the trough on purpose — moving it to the peak is the mistake, not the fix.
2. **Don't misread urgency as demand.** An urgent email is still shallow-admin; urgency dictates *when it must ship*, not *what energy it needs*. Keep the two axes separate.
3. **Don't assume the hardest-feeling task is the biggest mismatch.** Sometimes it's genuinely hard work done in the right window. Check the table before validating the user's instinct.
4. **Don't ignore fixed constraints to make the swap elegant.** A swap into a window the user can't actually use is a fantasy; fall back to the best real window.
5. **Don't override a night-owl or split-rhythm shape.** Two-peak and evening-peak people exist; the taxonomy maps to *their* windows, not a canonical 9am.
6. **Don't prescribe a swap when the real problem is starting, not timing.** If the deep task is in the right window but never gets *begun*, that's a focus-onset problem — route to `productivity_focus_ritual_design.md` and `agency_rapid_start_mode.md`.

---

## Output Format

```
## Task types by energy demand
| Task type | Demand class | Needs | Does it now | Verdict |
|---|---|---|---|---|
| ... | Deep-create/Deep-analyze/Social/Shallow-admin/Learning | ... | ... | Fit/Wasteful/Mismatch |

## Mismatches, ranked by cost
1. [task] — [hrs/wk] in [current window] but needs [window] → cost: [high/med]
2. ...

## Your hardest-lately task (input 4)
[task] feels hard because it's a [class] running in your [window]. The collision: [one sentence].

## The one swap
Move: [demanding task] → [peak/secondary window, exact times]
Displaces: [shallow task] → [trough window, exact times]
Respects fixed blocks: [list from input 5]

Predicted check: after one week, [demanding task] finishes faster / with less grind, and [displaced task] still gets done in the trough.
```

---

## Verification

- [ ] Every task type carries exactly one demand class from the taxonomy.
- [ ] Fit verdicts cite the user's real rhythm windows, not a morning default.
- [ ] Mismatches are ranked by hours × severity; only the top one is acted on.
- [ ] The input-4 task is located on the table and its window collision named.
- [ ] Exactly one swap is prescribed, with exact times and what displaces what.
- [ ] Every fixed constraint from input 5 is honored in the swap.
- [ ] No whole-day redesign, no added hours, no moralizing.
