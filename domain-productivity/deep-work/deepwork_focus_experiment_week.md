---
title: "Set Up and Review a One-Week Focus Experiment"
category: productivity/deep-work
description: "Design a one-week experiment that tests a single focus-system change against a measurable signal, log data across the week, and produce a keep/adjust/drop verdict — avoiding the usual pattern of trying five changes at once and learning nothing."
techniques:
  - ST-01
  - ST-02
  - DS-01
  - CM-02
  - QA-01
  - RT-02
difficulty: intermediate
tags:
  - deep-work
  - experiment
  - focus
  - evaluation
  - review
updated: "2026-04-20"
related_prompts:
  - domain-productivity/deep-work/deepwork_focus_parameters_estimator.md
  - domain-productivity/deep-work/deepwork_reload_ritual_design.md
  - domain-productivity/deep-work/deepwork_message_triage_system.md
---

# Set Up and Review a One-Week Focus Experiment

**Objective:** Design a one-week test of a single focus-system change, specify what gets measured, and after seven days produce a keep/adjust/drop verdict tied to the measurement. The experiment must isolate one variable — not bundle five.

**When to use:** Before committing to a new focus habit, schedule, or tool for the long term. After a diagnostic (focus parameters, calendar audit, self-interruption audit) that suggests a specific change.

**Audience:** An individual running an experiment on themselves. Not a team-wide rollout.

---

## Inputs Required

1. **The single change to test.** Stated in one sentence. "Block 9–11am for deep work with notifications off." Not "fix my focus."
2. **The diagnostic finding it targets.** Which measured problem (e.g., "median attention span 34 min, interruption rate 2.4/hr") this change is expected to move.
3. **The one measurable signal.** A number that can be observed daily. Example: minutes of uninterrupted focus per day, or count of self-interruptions.
4. **Baseline for that signal** from the last week or two.
5. **What week the experiment runs.** Exact start and end dates.
6. **Known confounds.** Travel, sick day, unusual workload, anything that will make week N weird. If more than one confound exists, pick a different week.

---

## Instructions

### Phase 1 — Setup (run this on day 0)

1. **Write a one-sentence hypothesis.** "If I [change], then [signal] will [direction and rough magnitude]." Example: "If I block 9–11 am with notifications off, uninterrupted focus minutes will rise from ~60/day to ≥ 120/day."

2. **Specify the measurement protocol.** Who records, when, where. Daily logging is required; end-of-week recall is unreliable.

3. **Define the bailout condition.** What would make you stop the experiment early? A genuine emergency or sustained signal collapse (e.g., if on day 2 work output cratered). Bailout is not "I don't feel like it."

4. **Freeze other variables.** Name 2–3 other focus practices the user must not change during the week. An experiment that changes two things teaches nothing.

5. **Write day-1 opening check.** Single question to answer on morning of day 1 to confirm setup is real (e.g., "notifications are actually off: yes/no").

### Phase 2 — Review (run this on day 7)

6. **Lay out the signal across 7 days.** Table. Do not average yet.

7. **Flag outlier days.** Sick, travel, one-off crisis. Mark but don't delete.

8. **Compute median signal for non-outlier days.** Compare to baseline. State delta in absolute and percentage terms.

9. **Answer the hypothesis:** confirmed / partially confirmed / refuted / insufficient data. Insufficient is a valid answer.

10. **Verdict:**
    - **Keep** — signal improved and the change felt sustainable. Promote to default practice.
    - **Adjust** — signal moved but not enough, or sustainability is shaky. Name the single adjustment.
    - **Drop** — signal didn't move or moved wrong direction. Stop; try a different change.

11. **Name one learning independent of the verdict.** What the experiment taught beyond keep/adjust/drop. Often the most durable output.

---

## Output Format

### Setup (Phase 1)
```
## Experiment
- Change: [one sentence]
- Targets: [diagnostic finding]
- Signal: [name and unit]
- Baseline: [value]
- Week: [start → end]
- Known confounds: [list or "none"]

## Hypothesis
If [change], then [signal] [direction] [magnitude].

## Protocol
- Recorded: [when, where]
- Bailout condition: [specific]
- Variables held fixed: [list]
- Day-1 opening check: [question]
```

### Review (Phase 2)
```
## Daily Signal
| Day | Value | Outlier? | Note |
|---|---|---|---|
| Mon | ... | | ... |
| ... |

## Analysis
- Baseline: [value]
- Median (non-outlier): [value]
- Delta: [abs, %]
- Hypothesis verdict: confirmed / partially / refuted / insufficient data

## Verdict
[Keep / Adjust / Drop] — because [one sentence]
[If Adjust: single named adjustment]

## Independent Learning
[One sentence.]
```

---

## Constraints

**Must:**
- Test exactly one change.
- Use a single quantifiable signal.
- Record daily, not retrospectively.
- Produce a verdict keyed to the signal, not to feelings.

**Must not:**
- Bundle changes ("new block + new triage + new ritual") — that's a relaunch, not an experiment.
- Use a signal that can't be measured daily.
- Treat "it felt good" as confirmation without the signal moving.
- Extend the experiment beyond 7 days "to see more" — restart with an adjustment instead.

---

## False-Positive Prevention

- **Bundle sneak:** The user will want to "also try" a second thing. Refuse. Insist on one change.
- **Feelings-as-evidence:** If the signal didn't move but the week "felt better," that's data, but it's not the verdict. Keep signal and feelings separate.
- **Outlier laundering:** Excluding Tuesday because "it was weird" without a concrete reason is cherry-picking. Require a specific note.
- **Observer effect:** Logging a signal often moves the signal by 10–20% just from attention. Factor in.
- **Sample size:** Seven days is minimal; a single bad Tuesday can dominate. If verdict relies on 1–2 days, mark insufficient data.

---

## Self-Verification (before finalizing)

**Setup phase:**
- [ ] Exactly one change tested.
- [ ] Single quantifiable signal named.
- [ ] Baseline stated.
- [ ] Bailout and held-fixed variables specified.

**Review phase:**
- [ ] Signal laid out per day.
- [ ] Outliers flagged with a reason.
- [ ] Delta in absolute and percentage.
- [ ] Verdict matches signal movement.
- [ ] Independent learning stated.
