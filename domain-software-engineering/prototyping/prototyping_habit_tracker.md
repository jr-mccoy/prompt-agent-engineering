---
title: "Habit and Goal Tracker Dashboard — Streaks, Weekly Grid, and Stats MVP"
category: software-engineering/prototyping
description: "Spec a mobile-first habit/goal tracker: a data model for habits and daily logs, a daily check-in with streaks, a weekly grid view, a stats section, and habit management — all local-first with JSON export."
techniques:
  - ST-01
  - ST-03
  - CM-02
  - DS-06
  - QA-01
difficulty: beginner
tags:
  - prototyping
  - habit-tracker
  - mvp
  - mobile-first
  - app-spec
updated: "2026-06-07"
related_prompts:
  - domain-software-engineering/prototyping/prototyping_personal_crm.md
  - domain-software-engineering/prototyping/prototyping_inventory_tracker.md
  - domain-software-engineering/prototyping/prototyping_landing_page.md
---

# Habit and Goal Tracker Dashboard

**Objective:** Produce a build-ready spec for a mobile-first habit/goal tracker — a habits + daily-logs data model, a daily check-in with streaks, a weekly grid, a stats section, and habit management (add/edit/archive/delete) — local-first, offline-capable, with JSON export.

**When to use:**
- A personal habit or daily-routine tracker you'll use mostly on your phone.
- Visualizing consistency and streaks to stay motivated.
- A quick, no-account tool to validate a tracking idea before building more.

**When NOT to use:**
- Multi-user/team habit programs with accountability partners — needs accounts and a backend.
- Complex goal frameworks (OKRs, projects with subtasks) — out of MVP scope.
- Anything needing cross-device sync — local-first MVP won't sync.

**Audience:** Individuals generating apps with Lovable, Bolt, v0, or similar AI app builders.

---

## Inputs / Context

Supply the following (or accept the defaults in the spec):

1. **Habits to track** — names and target frequency (daily, weekdays, X/week).
2. **Categories (optional)** — grouping labels (Health, Work, Learning, Personal) and whether colors are auto or user-picked.
3. **Streak definition** — how a streak counts for non-daily frequencies (e.g., weekday-only skips weekends).
4. **Stats wanted** — completion trend, best streak, consistency score, etc.
5. **Theme** — light/dark/both; mobile-first confirmed.
6. **Persistence scope** — confirm local storage, offline, JSON export (no backend).

---

## Constraints

### Must
- Define two entities: Habit and Daily Log, with the fields needed to compute streaks and stats.
- Compute streaks correctly for the habit's frequency (don't break a weekday streak over a weekend).
- Provide a daily check-in (tappable), a weekly grid (toggle cells), and a stats section.
- Support archive (data preserved, hidden) distinct from delete (with confirmation).
- Be mobile-first and offline-capable with local storage and JSON export.

### Must Not
- Invent habits, categories, or stats the user didn't request (offer sensible defaults, marked as such).
- Break streak logic for non-daily frequencies.
- Hard-delete on archive, or delete without confirmation.
- Over-scope with accounts, social features, or sync in an MVP.

---

## Instructions

1. **Confirm scope.** Restate it as a local-first, mobile-first MVP (flag if sync/accounts are actually needed).
2. **Specify the data model.** Habit (name, frequency, category, created date, active) and Daily Log (date, habit ID, completed, optional note).
3. **Specify the dashboard / daily check-in.** Current date; today's applicable habits as large toggles; per-habit current streak; week completion %.
4. **Specify the weekly grid.** Habits × days matrix; cell states (done / not done / N/A); toggle on click; current day highlighted; week navigation.
5. **Specify the stats section.** Completion trend over recent weeks; best (all-time) streak per habit; consistency score over a defined window; state how each is computed.
6. **Specify habit management.** Add (modal), edit, archive (preserve data, hide from daily), delete (confirm).
7. **Specify design + technical.** Motivating, clean, mobile-first; category colors; subtle completion feedback; light/dark; local storage; offline; JSON export; page structure (Dashboard / History / Settings).
8. **Self-check before output.** Confirm: streak logic respects frequency; archive ≠ delete; daily/grid/stats all present; local-first + export; mobile-first; no invented content beyond defaults. Then emit the spec.

---

## False-Positive Prevention

❌ **DON'T:**
- Add accounts, social/accountability features, or cloud sync to an MVP.
- Break weekday/X-per-week streaks by treating every gap as a miss.
- Make archive delete the underlying log data.
- Invent specific habits or stats the user never mentioned without marking them defaults.
- Build desktop-first when daily phone use is the point.

✅ **DO:**
- Scope to local-first, offline, single-user with JSON export.
- Define streak rules explicitly per frequency type.
- Keep archive non-destructive and require confirmation for delete.
- Offer defaults clearly labeled as suggestions, easy to change.
- Design mobile-first with satisfying-but-subtle completion feedback.

---

## Output Format

```
APP: Habit & Goal Tracker
SCOPE: [local-first, mobile-first MVP / flag if sync/accounts needed]

DATA MODEL
- Habit: name, frequency (daily | weekdays | X/week), category, created date, active(bool)
- Daily Log: date, habit ID, completed(bool), note (optional)

DASHBOARD / DAILY CHECK-IN
- Current date; today's habits as toggles; per-habit streak; week completion %

WEEKLY GRID
- Habits × days; cell = done | not done | N/A; click to toggle; current day highlighted; week nav

STATS
- Completion trend (last N weeks); best streak per habit; consistency score (window) — [computation notes]

HABIT MANAGEMENT
- Add (modal: name, frequency, category); Edit; Archive (preserve+hide); Delete (confirm)

STREAK LOGIC
- [rules per frequency type]

DESIGN / TECHNICAL
- Mobile-first; category colors; subtle completion feedback; light/dark; local storage; offline; JSON export
- Pages: Dashboard / History / Settings

VERIFICATION NOTES
- [assumptions / defaults flagged]
```

---

## Example Output

```
APP: Habit & Goal Tracker
SCOPE: Local-first, mobile-first MVP. No accounts/sync (single device).

DATA MODEL
- Habit: { name, frequency: daily|weekdays|"3/week", category, createdDate, active }
- Daily Log: { date, habitId, completed, note? }

DASHBOARD / DAILY CHECK-IN
- Header: "Saturday, Jun 7" + week completion "78%"
- Today's applicable habits as large tappable rows: [checkbox] {name} · 🔥{streak}d
- Checking a habit plays a brief, subtle success animation
- "..." menu reveals an optional note field

WEEKLY GRID
- Rows = habits, columns = Mon–Sun of current week
- Cell: ● done / ○ not done / – N/A (frequency doesn't apply that day)
- Click a cell to toggle; today's column highlighted; ◀ ▶ to view other weeks

STATS
- Line chart: completion rate over last 4 weeks
- Best streak (all time) per habit
- Consistency score = completed ÷ applicable days over last 30 days
- (Computation: "applicable days" excludes N/A days for non-daily habits)

HABIT MANAGEMENT
- "Add Habit" modal: Name, Frequency, Category
- Edit: tap a habit name in any view
- Archive: moves to "Archived" (hidden from daily, logs preserved)
- Delete: removes habit + its logs, with a confirm dialog

STREAK LOGIC
- daily: consecutive calendar days completed
- weekdays: consecutive Mon–Fri completed; weekends are N/A and do NOT break the streak
- X/week: streak counts consecutive weeks where the target count was met

DESIGN / TECHNICAL
- Mobile-first, app-like; auto-assigned category colors (overridable)
- Subtle completion celebration (no noise/spam)
- Dark mode toggle; local storage; works offline; "Export JSON" in Settings
- Pages: Dashboard / History (grid) / Settings (manage + archived + export)

VERIFICATION NOTES
- The four habits and categories shown are placeholders — user supplies their own.
- Assumption: single device; flag if cross-device sync is needed (requires backend).
```

---

## Verification

- [ ] Habit and Daily Log models support streak + stats computation.
- [ ] Streak logic is defined per frequency and doesn't break weekday streaks on weekends.
- [ ] Daily check-in, weekly grid, and stats section are all specified.
- [ ] Archive preserves data and is distinct from delete (which confirms).
- [ ] Mobile-first, offline, local storage, JSON export.
- [ ] Stats computations are stated explicitly.
- [ ] No invented habits/stats beyond clearly-flagged defaults; no accounts/sync in MVP.

---

## Techniques Used

- **ST-01 (Clear Objective Statement):** Fixes the app to a single-user, local-first habit MVP so scope stays tight.
- **ST-03 (Output Format Specification):** Locks the model / views / management / technical spec into a copy-ready build brief.
- **CM-02 (Constraint Specification):** Encodes Must/Must-Not rules (correct streaks, non-destructive archive, no accounts) as explicit constraints.
- **DS-06 (Prioritization and Severity Guidance):** Separates core MVP views (check-in, grid, stats) from polish (animations) so the build prioritizes function first.
- **QA-01 (Self-Verification):** A pre-output check confirms streak logic, archive-vs-delete, and local-first scope before emitting.

---

## Related Prompts

- `domain-software-engineering/prototyping/prototyping_personal_crm.md` — Similar local-first list/detail CRUD with export.
- `domain-software-engineering/prototyping/prototyping_inventory_tracker.md` — Shared data-model + views + stats pattern.
- `domain-software-engineering/prototyping/prototyping_landing_page.md` — Build a page to promote the tracker.
