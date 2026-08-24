---
title: "Temporal Logic & Calendar Edge Cases in Scheduling Systems"
category: algorithms
description: "Systematic review of calendar and time handling in scheduling systems covering DST, week boundaries, holidays, leap years, and custom day type classification"
tags:
  - algorithms
  - scheduling
  - calendar
  - temporal-logic
  - datetime
  - edge-cases
  - dst
techniques:
  - ST-01  # Clear Objective Statement
  - ST-02  # Structured Sequential Instructions
  - RT-02  # Multi-Dimensional Analysis
  - DT-02  # Specific Focus Areas
  - RT-05  # Evidence-Based Reasoning
  - QA-01  # Chain-of-Verification
  - QA-02  # Adversarial Stress-Test
difficulty: advanced
version: "1.0"
updated: 2026-03-04
related_prompts:
  - algorithms_constraint_satisfaction_scheduling.md
  - ../testing/testing_constraint_logic_edge_cases.md
  - quality_yaml_configuration_schema_validation.md
---

# Temporal Logic & Calendar Edge Cases in Scheduling Systems

**Objective:** Systematically audit a scheduling system's date and time handling for correctness, identifying calendar edge cases that produce valid-looking but wrong schedules — incorrect day counts, misclassified day types, broken week boundaries, or timezone-induced off-by-one errors.

**When to Use:** Use this prompt when building or reviewing any scheduling system that operates on dates. Calendar logic bugs are particularly dangerous because they often produce output that looks correct — a shift assigned on the wrong day, a week boundary computed one day off, or a holiday rotation that silently skips a day.

## Instructions

### 1. Datetime Representation Audit

Check the foundational date handling:

```python
# CORRECT: Use date objects for scheduling (no time component needed)
import datetime
schedule_date = datetime.date(2025, 3, 15)  # No timezone ambiguity

# DANGEROUS: Using datetime when only date is needed
schedule_datetime = datetime.datetime(2025, 3, 15, 0, 0, 0)
# Now timezone matters: is midnight in UTC? Local? Unspecified?

# DANGEROUS: String-based date handling
schedule_str = "2025-03-15"  # Comparison, arithmetic all need parsing
```

**Audit questions:**
- Are all schedule dates stored as `date` objects (not `datetime`)?
- If `datetime` is used, is timezone handling consistent throughout?
- Is any date arithmetic performed via string manipulation?
- Are dates ever serialized to/from strings? Is the format unambiguous (ISO 8601)?

### 2. Week Boundary Semantics

```
Week Definition Variations:
├── ISO 8601: Monday = day 1, week starts Monday
│   └── Dec 29, 2025 = Week 1 of 2026 (!)
│
├── US Convention: Sunday = first day of week
│   └── Same calendar, different week grouping
│
├── Configurable: User sets week_start_day in YAML
│   └── Must handle: "If week_start_day is Wednesday, which week is Tuesday?"
│
└── Fiscal Weeks: May not align with calendar weeks at all
```

**Critical edge cases:**
| Date | ISO Week | US Week | Why It Matters |
|------|----------|---------|----------------|
| Dec 29, 2025 (Mon) | 2026-W01 | Week of Dec 28 | Year-end week attribution |
| Jan 1, 2026 (Thu) | 2026-W01 | Week of Dec 28 | New Year week splits |
| Dec 31, 2024 (Tue) | 2025-W01 | Week of Dec 29 | Leap year year-end |

**Verify:**
- How does the scheduler compute "which week does this date belong to"?
- Is `weekly_limit` enforced using the same week definition as the configuration?
- When a schedule spans a year boundary, do weekly limits reset correctly?

### 3. DST Transition Handling

**Even if the scheduler only uses dates (not times), DST can bite:**

```python
# This is safe — date arithmetic ignores DST
from datetime import date, timedelta
d = date(2025, 3, 8)  # Day before US spring-forward
next_day = d + timedelta(days=1)  # March 9 — correct

# This is DANGEROUS — datetime arithmetic crosses DST
from datetime import datetime, timedelta
dt = datetime(2025, 3, 8, 23, 0)  # 11 PM before spring-forward
next_day = dt + timedelta(hours=24)  # March 10 at midnight, NOT March 9!
# If you derive schedule_date from this, you skip March 9 entirely
```

**Audit questions:**
- Does any code path add hours/minutes to compute the "next day"?
- Are any date comparisons done on `datetime` objects where timezone offset could vary?
- If the system exports iCal events, are DTSTART/DTEND timezone-aware?

### 4. Special Period Detection and Overlap

Special periods (holidays, on-call blocks, blackout windows) require careful boundary logic:

```
Special Period: "Christmas Block" = Dec 24-26
Schedule Horizon: Dec 22 - Dec 28 (one week)

Questions:
├── Is Dec 24 the first day OF the block or the day BEFORE the block?
├── Is the range inclusive on both ends? [Dec 24, Dec 26]?
├── If a weekly limit applies, does the Christmas block
│   count toward Week 52 or is it exempt?
└── If two special periods overlap (Christmas + New Year),
    which rules apply to the overlap days?
```

**Verify:**
- Are date ranges stored as inclusive `[start, end]` or half-open `[start, end)`?
- Is the convention documented and consistent across all range operations?
- When two special periods overlap, is there a priority/merge rule?

### 5. Day Type Classification

```
Day Type Decision Tree:
├── Is date in a configured holiday list?
│   ├── Yes → "holiday"
│   └── No ↓
├── Is date in a special period?
│   ├── Yes → special period's day type
│   └── No ↓
├── What is the weekday?
│   ├── Saturday or Sunday → "weekend"
│   └── Monday-Friday → "weekday"
│
└── CONFLICT: What if a date matches multiple classifiers?
    Example: Saturday that's also in a special period
    Resolution: priority ordering must be defined
```

**Verify:**
- Is the classification priority documented?
- Can the same date be classified differently by different code paths?
- Are "soft holidays" (day after Thanksgiving, Christmas Eve) handled?
- Does the classifier handle custom week definitions (e.g., Friday-Saturday weekends in some countries)?

### 6. Date Range Fence-Post Errors

The most common temporal bug in scheduling:

```python
# How many days in the schedule?
start = date(2025, 1, 1)
end = date(2025, 1, 31)

# Inclusive: 31 days (Jan 1 through Jan 31)
days = (end - start).days + 1  # 31

# Exclusive end: 30 days (Jan 1 through Jan 30)
days = (end - start).days      # 30

# Which does the config mean? Is it documented?
```

**Verify:**
- When the user configures `start: 2025-01-01, end: 2025-03-31`, is March 31 included?
- Is this convention consistent between: config parsing, constraint evaluation, export output?
- Are "number of weeks" calculations correct at boundaries? (Jan 1 to Jan 7 = 1 week or 2?)

### 7. Regression Test Suite — 12 Hazardous Dates

Every scheduling system should pass tests using these specific dates:

| # | Date | Hazard | What to Test |
|---|------|--------|-------------|
| 1 | 2024-02-29 | Leap day | Schedule spans Feb 28-Mar 1 in leap year |
| 2 | 2025-02-28 | Non-leap year | Same range, Feb 29 doesn't exist |
| 3 | 2025-03-09 | US DST spring-forward | Day has only 23 hours |
| 4 | 2025-11-02 | US DST fall-back | Day has 25 hours |
| 5 | 2025-12-29 | ISO week year boundary | ISO week 1 of 2026 starts here |
| 6 | 2025-12-31 | Year-end | Year transition in mid-week |
| 7 | 2026-01-01 | New Year | First day of new year — weekly limits reset? |
| 8 | 2025-12-25 | Christmas (Thursday) | Holiday + weekday combination |
| 9 | 2025-11-27 | US Thanksgiving | Configurable holiday |
| 10 | 2025-03-31 | Month-end on Monday | End of Q1, often a schedule boundary |
| 11 | 2025-06-30 | Mid-year boundary | Fiscal year split point |
| 12 | 2025-01-06 | First Monday of year | ISO week 2, but often treated as "first real week" |

## False-Positive Prevention (MUST follow)

❌ **DON'T:**
- Flag `date + timedelta(days=1)` as a DST bug — `date` arithmetic is DST-safe; only `datetime` arithmetic is affected
- Report "no timezone handling" as an issue if the system exclusively uses `date` objects — timezone is irrelevant for date-only scheduling
- Flag inclusive date ranges as "fence-post errors" if the convention is documented and consistent
- Assume ISO 8601 week numbering is "correct" and other conventions are bugs

✅ **DO:**
- Check whether the same range convention is used everywhere (config, constraints, export)
- Verify calendar logic against the specific hazardous dates in the regression table
- Test year-boundary scheduling (Dec 28 - Jan 4) for weekly limit correctness
- Confirm that day type classification handles multi-classifier conflicts

## Expected Output

1. **Datetime Representation Report** — Date vs datetime usage, timezone consistency
2. **Week Boundary Analysis** — Week definition, year-boundary handling, weekly limit behavior
3. **DST Audit** — All code paths that could be affected, with safe/dangerous classification
4. **Special Period Analysis** — Overlap rules, boundary convention, priority ordering
5. **Day Type Classification Map** — Priority rules, conflict resolution, custom day support
6. **Fence-Post Error Audit** — Range convention consistency across all components
7. **Regression Test Results** — Pass/fail on each of the 12 hazardous dates

## Quality Checklist

- [ ] All date arithmetic uses `date` objects (or documents why `datetime` is needed)
- [ ] Week definition is configurable and consistent
- [ ] At least 3 of the 12 hazardous dates are tested
- [ ] Date range convention (inclusive vs half-open) is documented
- [ ] Day type classifier has defined priority ordering

## Techniques Used

- **ST-01** (Clear Objective Statement) — Focuses on temporal correctness in scheduling
- **ST-02** (Structured Sequential Instructions) — Systematic walkthrough of temporal hazard categories
- **RT-02** (Multi-Dimensional Analysis) — Covers representation, boundaries, DST, classification, ranges
- **DT-02** (Specific Focus Areas) — Enumerates specific hazardous dates and scenarios
- **RT-05** (Evidence-Based Reasoning) — Requires concrete code examples and date calculations
- **QA-01** (Chain-of-Verification) — Self-check: "Is this range inclusive or exclusive?"
- **QA-02** (Adversarial Stress-Test) — Constructs schedules spanning known-dangerous date boundaries

## Related Prompts

- `algorithms_constraint_satisfaction_scheduling.md` — The CSP engine that relies on correct date handling
- `testing_constraint_logic_edge_cases.md` — Edge case testing that should include temporal cases
- `quality_yaml_configuration_schema_validation.md` — Config that defines week start, holidays, special periods

## Customization Guide

**For healthcare scheduling:**
- Holiday coverage is mandatory — holidays are not "days off" but require special rotation rules
- 12-hour vs 24-hour shift boundaries interact with DST: a "night shift" starting at 7 PM on DST fall-back is 13 hours, not 12

**For retail scheduling:**
- Store open/close hours mean DST transitions directly affect shift lengths
- Holiday operating hours may differ from regular hours — day type classification must drive store hours lookup

**For emergency services:**
- 24-on/48-off patterns make DST transitions relevant: the on-duty period length changes
- Shift handoff times must account for DST transitions explicitly
- Calendar week definitions may be mandated by labor regulations (varies by jurisdiction)
