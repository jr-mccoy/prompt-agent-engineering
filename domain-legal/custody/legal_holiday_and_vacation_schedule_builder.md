---
title: "Holiday and Vacation Schedule Builder"
category: legal/custody
description: "Build a detailed holiday, school-break, and vacation parenting-time schedule that slots into a parenting plan: an enumerated holiday list with an odd/even-year rotation, school-break and summer allocation, birthdays and parent-specific days, exact start/end times, a precedence hierarchy (vacation > holiday > regular), travel-notice and itinerary rules, and tie-breaker logic — child-centered and unambiguous so a third party can follow it without dispute."
techniques:
  - ST-01
  - ST-02
  - ST-03
  - CM-02
  - DS-02
  - QA-01
difficulty: beginner
tags:
  - legal
  - custody
  - family-law
  - holiday-schedule
  - parenting-time
  - vacation
updated: "2026-06-01"
related_prompts:
  - domain-legal/custody/legal_parenting_plan_drafter.md
  - domain-legal/custody/legal_high_conflict_parenting_coordination_provisions.md
  - domain-legal/custody/legal_custody_best_interests_analysis.md
  - domain-legal/custody/legal_parenting_time_enforcement_and_contempt_motion.md
  - domain-legal/divorce/legal_marital_settlement_agreement_drafter.md
---

**Purpose:** Produce a precise holiday/break/vacation parenting schedule that drops into a parenting plan and eliminates the recurring disputes vague schedules create — with an enumerated holiday list, a year-rotation, exact times, and a clear precedence hierarchy. Output is a schedule section ready for incorporation, not a memo.

**When to use:** Building or fixing the holiday/vacation portion of a parenting plan; resolving recurring holiday conflicts; replacing an ambiguous "as agreed" holiday term.

---

## Your Input

- **Jurisdiction:** [State; any local norms or court-preferred holiday schedule, if applicable]
- **Child(ren):** [Names, ages, school calendar, religious/cultural observances]
- **Parents:** [Names; distance between homes; travel constraints]
- **Holidays to allocate:** [Federal holidays, religious/cultural holidays, three-day weekends, the child's and parents' birthdays, Mother's/Father's Day]
- **School breaks:** [Winter, spring, fall breaks; summer length]
- **Summer plan:** [Whether the schedule changes for summer; vacation weeks per parent]
- **Current regular schedule:** [The base residential schedule the holidays override]
- **Travel:** [Out-of-state/international travel rules, notice, itinerary, passports]
- **Special considerations:** [Extended family traditions, religious observances, child's activities]

---

## Constraints

**Must:**
- Provide an **enumerated holiday list** with an **odd/even-year rotation** (or fixed assignment for parent-specific days like Mother's/Father's Day).
- State **exact start and end times** for every holiday and break period (e.g., "Dec 24, 12:00 pm to Dec 25, 12:00 pm"), not "Christmas."
- Allocate **school breaks and summer** with specific dates/weeks and a selection/notice procedure for summer vacation weeks.
- Establish a clear **precedence hierarchy** (e.g., vacation > holiday > regular schedule) and resolve **adjacent/overlapping** holidays and breaks.
- Assign **the child's birthday** and the **parents' birthdays/Mother's-Father's Day** consistently.
- Include **travel-notice and itinerary** rules and any passport/consent terms.
- Keep the schedule **child-centered** (school calendar, observances, activities) and **operationally unambiguous**.
- Use placeholders `[NEED: ...]` for unsupplied dates, observances, or constraints.

**Must Not:**
- Use "as agreed" or vague references for any holiday without a default rotation fallback.
- Omit exact times (the leading source of holiday disputes).
- Leave overlaps between holidays, breaks, and the regular schedule unresolved.
- Ignore religious/cultural observances the family keeps.
- Invent the family's holidays or the school calendar.

---

## Instructions

1. **Holiday list & rotation.** Enumerate holidays; assign each to a parent by odd/even year or fixed rule.
2. **Exact times.** State start/end times for each holiday and break.
3. **School breaks.** Allocate winter/spring/fall breaks with dates and rotation.
4. **Summer & vacation weeks.** Set the summer pattern and a selection/notice procedure for vacation weeks; resolve conflicts (e.g., earlier notice wins, alternate priority by year).
5. **Birthdays & special days.** Assign the child's birthday and parent-specific days.
6. **Precedence hierarchy.** State the override order and resolve adjacent-holiday/weekend overlaps.
7. **Travel rules.** Notice, itinerary, out-of-state/international, passport/consent.
8. **Assemble.** Produce the incorporation-ready schedule.

---

## Output Format

```markdown
HOLIDAY, BREAK & VACATION SCHEDULE — {Child(ren)}

## A. Holiday Rotation
| Holiday | Start | End | Even years | Odd years |
|---|---|---|---|---|
| New Year's | {Dec 31 6pm} | {Jan 1 6pm} | Parent A | Parent B |
| {Thanksgiving} | {Wed 6pm} | {Sun 6pm} | B | A |
| {Winter Break ½ / ½} | {…} | {…} | {first half A} | {first half B} |
| {Religious/cultural} | {…} | {…} | {…} | {…} |

## B. Parent-Specific & Birthdays
- Mother's Day: with mother; Father's Day: with father (exact times).
- Child's birthday: {rotation/shared}; Parents' birthdays: {…}.

## C. School Breaks
- Winter break: {split / rotation, dates}. Spring break: {rotation}. Fall break: {…}.

## D. Summer & Vacation Weeks
- Summer pattern: {…}; each parent {N} vacation weeks; selection: {Parent A selects by {date} in even years; B in odd}; conflicts resolved by {priority rule}.

## E. Precedence Hierarchy
- Vacation > Holiday > Regular schedule. Adjacent holidays/weekends resolved by {rule}.

## F. Travel
- Notice: {N days}; itinerary required; out-of-state/international: {consent}; passports held by {…}.
```

---

## Verification

- [ ] Holidays enumerated with odd/even rotation or fixed assignment.
- [ ] Exact start/end times stated for every holiday and break.
- [ ] School breaks and summer allocated with dates and a selection/notice procedure.
- [ ] Precedence hierarchy stated; overlaps and adjacencies resolved.
- [ ] Child's birthday and parent-specific days assigned.
- [ ] Travel-notice/itinerary and passport/consent rules included.
- [ ] Religious/cultural observances reflected.
- [ ] No "as agreed" without a fallback; no missing times; no unresolved overlaps.

---

## False-Positive Prevention

| Failure mode | Correction |
|---|---|
| Listing "Christmas" with no times | State exact start/end times for every holiday |
| "As agreed" with no fallback | Provide a default odd/even rotation |
| Unresolved overlap between a holiday and the regular schedule | State the precedence hierarchy and adjacency rule |
| Summer left vague | Set the summer pattern, vacation-week count, and selection/notice procedure |
| Forgetting parent-specific days | Assign Mother's/Father's Day and birthdays |
| Ignoring religious/cultural observances | Include the family's observed holidays |
| No travel notice or itinerary rule | Add notice, itinerary, and passport/consent terms |
| Schedule a third party couldn't follow | Make every entry concrete (date, time, parent) |
| Inventing the school calendar or observances | Use [NEED] placeholders for unsupplied dates |
| Conflicting vacation requests with no tie-breaker | Add a priority rule (earlier notice / alternating priority by year) |
