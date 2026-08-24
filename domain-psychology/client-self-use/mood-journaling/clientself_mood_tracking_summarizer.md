---
title: "Mood Tracking Summarizer"
category: psychology/client-self-use/mood-journaling
description: "Take a stretch of mood-tracking entries (PHQ-9, GAD-7, daily mood log, sleep, energy, substance use, exercise) and produce a pattern summary the client can review or bring to a clinician."
techniques:
  - ST-04
  - DT-02
  - DS-04
  - QA-04
difficulty: beginner
tags:
  - client-self-use
  - mood-tracking
  - pattern-recognition
  - measurement-based-care
intended_use: model-testing
updated: "2026-05-08"
---

# Mood Tracking Summarizer

## Objective

Take a stretch of mood-tracking entries and surface patterns: trajectory, weekly cycles, correlations with sleep/exercise/substances/menstrual cycle, and outliers. Output a 1-page summary the client can read or bring to therapy.

## When to Use

- After 2+ weeks of consistent tracking.
- Before a therapy session as input.
- To check whether something is working (medication change, new sleep routine, work change).

## Inputs / Context

- Daily entries with: mood (0–10 or label), sleep hours, energy (0–10), substances used, exercise (Y/N or minutes), menstrual phase if relevant, key events.
- Any standardized measures collected (PHQ-9, GAD-7) with dates.
- Date range.
- What the client wants the summary to surface.

## Constraints

### Must

- Output sections: **Date Range**, **Trajectory**, **Weekly Pattern**, **Sleep Correlation**, **Substance Correlation**, **Exercise Correlation**, **Menstrual-Cycle Correlation (if relevant)**, **Standardized Measure Trajectory**, **Outliers and Their Context**, **What to Bring to Therapy**.
- Be honest about correlations: if there isn't a clear pattern, say so. Don't invent.
- Flag low-data periods (e.g., gaps in tracking) explicitly.
- For substance correlations, name the pattern without moralizing.

### Must Not

- Don't diagnose.
- Don't make causal claims from correlation.
- Don't moralize about substance use.
- Don't extrapolate beyond the data.

## Instructions

1. Compute mean, range, trend for mood.
2. Compute weekly cycle (does Sunday consistently look different from Wednesday?).
3. Cross-tabulate mood with sleep hours.
4. Cross-tabulate mood with substance use.
5. Cross-tabulate mood with exercise.
6. If menstrual phase tracked, cross-tabulate.
7. Plot standardized measure trajectory if collected.
8. Identify outliers; describe their context.
9. Summarize what to bring to therapy.

## Output Format

```
=== MOOD TRACKING SUMMARY ===

Date Range: [Start] – [End]
Total entries: [N of N possible days = N% adherence]
Gaps in tracking: [List or "none"]

TRAJECTORY
Mean mood (0–10): [N]
Range: [N – N]
Trend: [Improving / Stable / Worsening / Mixed — describe]

WEEKLY PATTERN
- Best day(s) of week (avg): [Day(s) — mean N]
- Worst day(s) of week (avg): [Day(s) — mean N]
- Pattern noted: [e.g., Sunday-night dip; Wednesday slump; Friday lift]
- Pattern not present: [if no clear weekly pattern, say so]

SLEEP CORRELATION
- Average sleep on best mood days: [N hrs]
- Average sleep on worst mood days: [N hrs]
- Direction: [Better mood with more sleep / no clear pattern / mixed]
- Note: correlation, not causation

SUBSTANCE CORRELATION
- Days with [substance] used: [N of N]
- Mood on those days vs other days: [...]
- Next-day mood after [substance] use: [...]
- Pattern: [Describe; do not moralize]

EXERCISE CORRELATION
- Days with exercise: [N of N]
- Mood on exercise days vs other: [...]
- Pattern: [Describe]

MENSTRUAL CYCLE CORRELATION (if tracked)
- Mood by phase: [Follicular / ovulatory / luteal / menstrual — means]
- Pattern: [PMDD-pattern hint? Coordinate with PCP / OB-GYN if so. Tracking 2–3 cycles is the standard for diagnosis.]

STANDARDIZED MEASURE TRAJECTORY (if collected)
- PHQ-9: [Date X / Date X / Date X — direction; clinically meaningful change?]
- GAD-7: [...]

OUTLIERS AND THEIR CONTEXT
- [Date — mood = N — what was happening]
- [Date — ...]

WHAT TO BRING TO THERAPY
- The summary itself (or share access)
- Specific question I want help with: [...]
- Pattern that surprised me: [...]
- What I want to try based on this: [...]

What this summary is NOT:
- A diagnosis
- A causal claim (X causes Y)
- A substitute for clinician interpretation
```

## Verification

- [ ] Date range and adherence rate stated.
- [ ] Gaps flagged.
- [ ] Trajectory described.
- [ ] Weekly pattern described or "no clear pattern."
- [ ] Sleep / substance / exercise correlations addressed.
- [ ] Menstrual-cycle section only if data present.
- [ ] Standardized measures plotted with clinically-meaningful change flagged.
- [ ] Outliers contextualized.
- [ ] No diagnosis, no causal claim, no moralizing.
