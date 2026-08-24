---
title: "Brier Tracker Design — Personal Forecasting Log Spec"
category: reasoning-craft/forecasting
description: "Design a personal forecasting log for someone starting calibration practice. Specifies what to log per forecast, what to log at resolution, review cadence, metrics tracked (Brier, calibration curve, resolution counts), and how to act on the log. Output is a template the user can copy into a spreadsheet or notes app."
techniques:
  - ST-01
  - ST-02
  - RT-02
  - DS-01
  - CM-02
  - QA-01
difficulty: beginner
tags:
  - forecasting
  - tracker
  - brier
  - logging
  - habit-design
updated: "2026-05-10"
reasoning:
  styles: [structured, habit-design]
  stakes: low
  horizon: months_to_years
  uncertainty: not_applicable
  evidence_quality: not_applicable
  domain_complexity: variable
  collaboration: solo
  output_format: log_template
  user_role: [forecaster, analyst, individual, student]
  mode: [design, document]
related_prompts:
  - domain-reasoning-craft/forecasting/forecasting_calibration_self_audit.md
  - domain-reasoning-craft/forecasting/forecasting_probabilistic_question_design.md
  - domain-reasoning-craft/forecasting/forecasting_what_would_change_my_mind.md
---

# Brier Tracker Design

**Objective:** Design a personal forecasting log so the user can build a calibration track record over time. Specify per-forecast logging fields, resolution-time fields, review cadence, metrics, and how to act on the log. Output is a copy-pasteable template for spreadsheet or notes app.

**When to use:**
- Someone starting a personal calibration practice.
- Operationalizing a team's prediction tracking.
- Building a forecast log specifically for a domain (markets, projects, hires, product launches).

**When NOT to use:**
- Casual occasional predictions (overhead exceeds value).
- One-shot forecasts that won't repeat.

**Audience:** Forecasters, analysts, individuals, students building epistemic discipline.

---

## Inputs / Context

1. **Domain(s)** the user wants to forecast in.
2. **Cadence** the user can sustain (daily / weekly / ad-hoc).
3. **Tooling preference** (spreadsheet, Notion, Obsidian, dedicated app, paper).
4. **Whether forecasts will be shared** (team) or private.

---

## Constraints

### Must
- Specify **per-forecast fields**: question (operationalized via `forecasting_probabilistic_question_design.md`), probability assigned, reasoning (1–3 sentences), domain tag, expected resolution date, what would update the forecast.
- Specify **resolution fields**: actual outcome (yes/no/value), resolution date (when resolved), brief post-mortem (was the forecast process good even if outcome surprised), Brier contribution.
- Specify **review cadence**: daily during ramp-up (first 30 days), then weekly, monthly, and quarterly deep-audit using `forecasting_calibration_self_audit.md`.
- Specify **metrics**: Brier score, calibration curve, resolution counts per probability bin, domain breakdown.
- Specify **action rules**: what calibration patterns trigger what behavior changes.
- Output as a **table template** the user can copy into chosen tool.

### Must Not
- Over-engineer the log; high friction kills the practice.
- Skip the reasoning field; numbers without reasoning are uninspectable.
- Make resolution review optional; without it, the log is half-data.
- Mix questions of different stakes / time horizons in the same review without flagging.

---

## Instructions

### Step 1 — Per-forecast log fields
| Field | Required? | Notes |
|-------|-----------|-------|
| Forecast ID | yes | sequential |
| Date logged | yes | |
| Question | yes | operationalized; resolves cleanly |
| Probability | yes | 5% increments |
| Reasoning | yes | 1–3 sentences |
| Domain tag | yes | for breakdown |
| Expected resolution date | yes | |
| What would update | yes | observable that would meaningfully shift this |
| Notes | no | source / context |

Estimate the fill time for this field set (target: < 5 minutes per forecast); trim optional fields if it exceeds that.

### Step 2 — Resolution fields
| Field | Required? | Notes |
|-------|-----------|-------|
| Resolved date | yes | |
| Outcome | yes | yes / no / value |
| Brier contribution | computed | (probability − outcome)² |
| Surprise factor | yes | not surprising / mildly / strongly |
| Process post-mortem | yes | 1–2 sentences: was the reasoning sound regardless of outcome? |
| Lessons | optional | for future similar forecasts |

### Step 3 — Review cadence
- **Daily** (during ramp-up, first 30 days): check what resolved yesterday; record outcomes.
- **Weekly:** review what's resolving this week; pre-commit to recording outcomes.
- **Monthly:** light calibration check (recent 30 forecasts).
- **Quarterly:** deep audit using `forecasting_calibration_self_audit.md`.

### Step 4 — Metrics dashboard
- Total forecasts logged
- Total resolved
- Brier score (overall, recent 30, by domain)
- Calibration curve (probability bin × resolution rate)
- Surprise pattern (where is reality consistently surprising you)

### Step 5 — Action rules
- Brier > 0.25 in a domain → reduce confidence in that domain; do more outside-view work.
- Systematic overconfidence at 80%+ → require stronger evidence before assigning 80%+.
- Systematic underconfidence at low probabilities (events resolve even less often than your stated 20%) → trust the analysis and assign more extreme low probabilities (e.g., 5–10% instead of 20%).
- Surprise pattern in domain X → skill gap; targeted learning needed.

### Step 6 — Tool-specific template
Provide a copy-pasteable table for the user's chosen tool (spreadsheet / Notion / etc.).

---

## False-Positive Prevention

1. **High-friction logging.** If the log takes >5 minutes per forecast, the user will abandon it.
2. **Reasoning skipped.** Numbers without reasoning prevent post-mortem learning.
3. **No resolution discipline.** Without resolution recording, the log is half-data.
4. **Over-frequent deep audits.** Monthly is enough for pattern emergence; daily Brier obsession is noise.
5. **Mixing stakes.** A market forecast log and a personal-prediction log can be combined, but should be domain-tagged.

---

## Output Format

```
# Brier tracker — personal forecasting log

## Per-forecast fields
| Field | Required | Notes |
|-------|----------|-------|
| ID | yes | sequential |
| Date logged | yes | |
| Question | yes | operationalized |
| Probability | yes | 5% increments |
| Reasoning | yes | 1–3 sentences |
| Domain | yes | tag |
| Expected resolution date | yes | |
| What would update | yes | observable |
| Notes | no | |

## Resolution fields
| Field | Required | Notes |
|-------|----------|-------|
| Resolved date | yes | |
| Outcome | yes | yes / no / value |
| Brier contribution | computed | |
| Surprise factor | yes | not / mildly / strongly |
| Process post-mortem | yes | 1–2 sentences |
| Lessons | optional | |

## Review cadence
- Daily (first 30 days): outcomes
- Weekly: resolutions due this week
- Monthly: light calibration check
- Quarterly: deep audit

## Metrics
- Brier (overall, recent 30, by domain)
- Calibration curve (bin × resolution rate)
- Surprise pattern by domain

## Action rules
| Pattern | Action |
|---------|--------|
| Brier > 0.25 in domain | reduce confidence; outside-view work |
| Overconfidence at 80%+ | stronger evidence required |
| Underconfidence at low probabilities | assign more extreme low values |
| Surprise pattern in domain | targeted learning |

## Tool template (spreadsheet / Notion)
[Copy-pasteable table headers]
```

---

## Verification

- [ ] Per-forecast fields specified with required/optional.
- [ ] Resolution fields specified.
- [ ] Cadence stated for daily / weekly / monthly / quarterly.
- [ ] Metrics enumerated.
- [ ] Action rules tied to patterns.
- [ ] Tool template ready to copy.
- [ ] Total log time per forecast < 5 minutes.
