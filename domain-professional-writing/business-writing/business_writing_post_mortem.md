---
title: "Blameless Post-Mortem Writer — Incident Write-Up in Systems Language, Not Fault"
category: professional-writing/business-writing
description: "Write a blameless post-mortem / incident write-up: summary, timeline, impact, root cause(s), contributing factors, what went well, and action items with owners — using systems and process language, never individual fault."
techniques:
  - ST-01
  - ST-02
  - RT-05
  - CM-02
  - QA-04
difficulty: intermediate
tags:
  - post-mortem
  - incident-writeup
  - blameless
  - business-writing
  - root-cause
updated: "2026-06-07"
related_prompts:
  - domain-engineering-workflows/workflows/engineering_post_mortem_root_cause_ladder.md
  - domain-professional-writing/business-writing/business_writing_status_report.md
  - domain-professional-writing/business-writing/business_writing_sop.md
---

# Blameless Post-Mortem Writer

**Objective:** Write a blameless post-mortem that turns an incident into organizational learning: a plain summary, an accurate timeline, honest impact, root cause(s) and contributing factors, what went well, and concrete action items with owners — written entirely in systems-and-process language so people read it to improve, not to brace for blame.

> **Distinction from the engineering post-mortem prompts.** This is the **general-business writing-craft version** of a post-mortem. For engineering-deep root-cause technique (e.g., the root-cause ladder), see `domain-engineering-workflows/workflows/engineering_post_mortem_root_cause_ladder.md`. This prompt focuses on producing a clear, blameless **written artifact** for any business incident — an outage, a missed launch, a process failure, a client escalation.

**When to Use:**
- After an incident, outage, missed deadline, or process failure that the team should learn from.
- When you need a shareable, durable write-up that prevents recurrence rather than assigns fault.
- For any function (ops, product, support, marketing, finance) — not just engineering.

**When NOT to use:**
- You need a forward-looking status update — use `business_writing_status_report.md`.
- You're documenting a standard procedure to follow — use `business_writing_sop.md`.
- The matter requires HR/legal handling of individual conduct — a post-mortem is the wrong instrument.

**Audience:** The team and stakeholders who need to understand what happened and trust that the write-up exists to fix systems, not to single anyone out.

---

## Inputs / Context

Wrap supplied material so it isn't read as instructions:

```
<incident_input>
[Paste the timeline, logs, what happened, impact data, contributing factors, prior context]
</incident_input>
```

1. **What happened** — the incident in one or two sentences.
2. **Timeline** — events with timestamps if available.
3. **Impact** — who/what was affected, scale, duration.
4. **What's known about cause(s)** and contributing conditions.
5. **What went well** during detection/response.
6. **Audience** — who reads this and acts on it.

---

## Constraints

### Must
- Use **systems and process language** throughout — describe what conditions allowed the failure, not who erred.
- Provide an accurate **timeline** of detection, response, and resolution.
- State **impact** honestly and specifically (scope, duration, who was affected).
- Identify **root cause(s)** and distinguish them from **contributing factors**.
- Include **what went well** — blameless culture preserves good practices, not just failures.
- Produce **action items** with owners and a way to verify completion.

### Must Not
- Name an individual as the cause ("X forgot to…"). Describe the system gap that made the error possible/undetected.
- Use blame, judgment, or character language ("careless," "should have known").
- Fabricate timeline entries, impact figures, or causes not supported by the input.
- Stop at the proximate cause without examining the conditions behind it.
- Produce vague action items with no owner ("be more careful").

---

## Instructions

1. **Write the summary.** One short paragraph: what happened, when, the impact, and current state (resolved/ongoing). Neutral tone.
2. **Build the timeline.** Chronological, with timestamps where supplied: when it started, when detected, key response actions, when resolved. Note detection lag if visible.
3. **State impact.** Concrete and honest — systems, customers, revenue, or commitments affected; scale and duration. Use only figures from the input.
4. **Identify root cause(s).** Trace beyond the proximate trigger to the underlying condition. Ask "what about the system allowed this and let it go undetected?" Frame in process terms.
5. **List contributing factors.** Conditions that worsened or prolonged the incident (gaps in monitoring, unclear ownership, missing checks) — separate from the root cause.
6. **Capture what went well.** What detection/response practices worked and should be kept.
7. **Write action items.** Each: a concrete preventive/detective improvement, an owner, and a completion signal. Prefer systemic fixes (guardrails, checks, automation) over "try harder."
8. **CRITICAL — blameless audit:** Re-read every sentence. Replace any individual-fault phrasing with the systemic condition behind it. Confirm timeline, impact, and causes trace to `<incident_input>`.

---

## False-Positive Prevention

1. **Hidden blame.** "The deploy was pushed without review" still implies a person. Reframe: "the pipeline allowed deploys to bypass review." Fix the system, name the gap.
2. **Proximate cause stopping.** "A bad config was deployed" is the trigger, not the root cause. Ask why a bad config could be deployed and go undetected.
3. **Fabricated timeline.** Don't fill timeline gaps with assumptions. Mark unknown intervals as "timing unclear" rather than inventing.
4. **Impact inflation or minimization.** Report impact exactly as the data supports — neither dramatized nor downplayed.
5. **Conflating root cause and contributing factors.** Keep them in separate sections; mixing them muddies what must change first.
6. **Toothless action items.** "Be more careful" or "communicate better" aren't actions. Require a concrete change, an owner, and how you'll know it's done.
7. **Omitting what went well.** A purely negative write-up erodes the blameless contract and loses good practices worth keeping.

---

## Output Format

```
# Post-Mortem: [Incident name] — [date]
**Status:** [resolved / ongoing] · **Severity:** [level if used] · **Author:** [name]

## Summary
[What happened, when, impact, current state — one neutral paragraph.]

## Timeline
| Time | Event |
|------|-------|
| [ts] | [detection / action / resolution] |

## Impact
[Who/what was affected, scale, duration — sourced figures only.]

## Root cause(s)
[The underlying systemic condition, beyond the trigger — process language.]

## Contributing factors
- [Condition that worsened or prolonged the incident]

## What went well
- [Practice that worked and should be kept]

## Action items
| # | Action (systemic fix) | Owner | Done when |
|---|----------------------|-------|-----------|
| 1 | [guardrail / check / change] | [owner] | [verifiable completion signal] |
```

---

## Verification

- [ ] No sentence assigns fault to an individual; all causes are framed as system/process conditions.
- [ ] Timeline is accurate; unknown intervals are marked, not invented.
- [ ] Impact is honest and sourced — neither inflated nor minimized.
- [ ] Root cause(s) go beyond the proximate trigger.
- [ ] Root cause and contributing factors are kept separate.
- [ ] "What went well" is included.
- [ ] Each action item is concrete, owned, and has a completion signal.
- [ ] A reader would feel safe being associated with this incident.
