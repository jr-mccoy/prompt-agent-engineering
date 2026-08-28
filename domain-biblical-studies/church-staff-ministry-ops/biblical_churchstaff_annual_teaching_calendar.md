---
title: "Annual Teaching Calendar — Map Your Church's Preaching & Teaching Year"
category: biblical-studies/church-staff-ministry-ops
description: "Map a church's annual preaching and teaching calendar integrating sermon series, holidays, guest speakers, special events, and teaching-ministry rhythms — producing a month-by-month plan with series arcs, open weeks, and coordination notes."
techniques:
  - ST-01
  - ST-02
  - RT-02
  - NE-14
difficulty: beginner
tags:
  - calendar
  - planning
  - church-staff
  - preaching
  - annual
updated: "2026-06-25"
related_prompts:
  - domain-biblical-studies/sermon-devotional/biblical_sermon_series_planner.md
  - domain-biblical-studies/church-staff-ministry-ops/biblical_churchstaff_curriculum_scope_sequence.md
  - domain-biblical-studies/church-staff-ministry-ops/biblical_churchstaff_multi_service_coordination.md
---

# Annual Teaching Calendar

**Objective:** Produce a month-by-month teaching calendar for a church year that maps sermon series, standalone messages, holidays, guest speakers, baptism/communion Sundays, and open weeks — giving the teaching team a shared view of the year and preventing the common failure of planning series one at a time with no big-picture rhythm.

**When to use:**
- You are planning a new ministry year (or calendar year) of preaching and teaching.
- You want to see the full year at a glance before committing to individual series.
- You need to coordinate preaching with holidays, events, and guest speakers.

**When NOT to use:**
- You are planning one sermon series — use `biblical_sermon_series_planner.md`.
- You are building a multi-year curriculum scope-and-sequence — use `biblical_churchstaff_curriculum_scope_sequence.md`.

**Audience:** Lead pastors and teaching-team leads (P).

---

## Inputs / Context

1. **Year or season.** Calendar year, ministry year (Sep–Aug), or a defined window.
2. **Fixed dates.** Holidays, church traditions (Easter, Advent, missions month, etc.), and any dates already committed.
3. **Guest speakers.** Dates reserved for guests, if any.
4. **Series preferences.** Any series the pastor already wants to do (book, topic, or theme).
5. **Congregation rhythm.** Summer attendance patterns, school year, etc.
6. **Declared tradition (optional).** May shape holiday emphasis (liturgical calendar, Reformed, etc.).

---

## Constraints

### Must
- Map every Sunday (or primary teaching day) for the defined window.
- Mark holidays, communion/baptism Sundays, guest-speaker dates, and special events.
- Include open or buffer weeks between series for flexibility.
- Note where series arcs land relative to holidays and attendance patterns.
- Flag any month that is overloaded (too many special events competing with a series arc).

### Must Not
- Fabricate attendance statistics, church-calendar norms, or denominational requirements.
- Plan individual sermon outlines — this is a calendar, not sermon prep.
- Assume a liturgical calendar unless the user declares one.

### Tradition-neutral stance (Must / Must Not)
- **Must:** respect the user's declared holiday and calendar traditions.
- **Must Not:** impose a liturgical calendar on a non-liturgical church or vice versa.

---

## Instructions

### Step 1 — Confirm the window and fixed dates
Restate the year/season, all fixed dates (holidays, guests, events), and any pre-committed series. Flag conflicts (e.g., a guest speaker landing mid-series).

### Step 2 — Lay out the calendar skeleton
Map every primary teaching day in the window. Mark holidays, guest dates, and special events. Identify open weeks.

### Step 3 — Place series arcs
Fit the user's preferred series into the calendar, noting start/end dates, number of weeks, and how each series relates to the surrounding calendar (e.g., a series on hope ending before Advent).

### Step 4 — Fill remaining weeks
Suggest categories for unplanned weeks: standalone messages, topical one-offs, congregational response Sundays, or buffer weeks.

### Step 5 — Rhythm and balance check
Review the calendar for rhythm: series length variation, topical vs. expository balance, OT/NT spread, and pacing (no two 12-week series back-to-back). Flag imbalances.

---

## Output Format

```
# Annual Teaching Calendar — [year or season]

## Fixed dates
| Date | Event |
|------|-------|
| [..] | [..] |

## Month-by-month calendar
| Month | Week | Type | Series / Topic | Notes |
|-------|------|------|----------------|-------|
| Jan   | 1    | Series start | [..] | [..] |
| Jan   | 2    | Series | [..] | Communion Sunday |

## Series summary
| Series | Weeks | Dates | Type (expository/topical) | Book/Theme |
|--------|-------|-------|---------------------------|------------|
| [..]   | [N]   | [..–..] | [..] | [..] |

## Rhythm check
- Series length variation: [..] | OT/NT balance: [..] | Open weeks: [N]
```

---

## Verification

- [ ] Every primary teaching day in the window is accounted for.
- [ ] Holidays, guest speakers, and special events are marked.
- [ ] Open/buffer weeks exist between series.
- [ ] Series arcs don't conflict with holidays or low-attendance periods.
- [ ] No fabricated statistics or denominational norms.

---

## False-Positive Prevention

DON'T:
- Plan sermon content — this is a calendar, not a sermon outline.
- Assume liturgical-calendar observance without the user declaring it.
- Pack the calendar with no buffer weeks.

DO:
- Mark every Sunday with its type (series, standalone, guest, special).
- Flag overloaded months and pacing imbalances.
- Leave room for the pastor to adjust mid-year.
