---
title: "Estimate Personal Focus Parameters"
category: productivity/deep-work
description: "Produce a numeric, personal profile of the user's focus system (attention span, context-reload cost, interruption rate, recovery time) from real session data rather than generic averages, so subsequent deep-work design decisions have concrete numbers to fit to."
techniques:
  - ST-01
  - ST-02
  - RT-02
  - DS-01
  - CM-02
  - QA-01
difficulty: intermediate
tags:
  - deep-work
  - focus
  - diagnostics
  - self-knowledge
  - metrics
updated: "2026-04-20"
related_prompts:
  - domain-productivity/deep-work/deepwork_calendar_audit.md
  - domain-productivity/deep-work/deepwork_self_interruption_audit.md
  - domain-productivity/deep-work/deepwork_reload_ritual_design.md
  - domain-productivity/deep-work/deepwork_focus_experiment_week.md
---

# Estimate Personal Focus Parameters

**Objective:** From session logs the user supplies, produce a compact numeric profile of how the user's focus actually behaves: usable attention span, context-reload cost, interruption rate, and recovery time after interruption. Do not give population averages; all numbers must be derived from the user's own data.

**When to use:** Before (re)designing any focus system. Also when the user suspects their current system is built for a fictional version of themselves ("I plan 4-hour deep-work blocks and never hit them").

**Audience:** An individual knowledge worker auditing their own focus. Not a manager profiling a team.

---

## Inputs Required

1. **A log of 5–10 recent work sessions.** For each: start time, end time, what they intended to work on, what they actually did, and every interruption (self or external) with a one-line cause.
2. **Subjective quality rating per session.** A 1–5 scale. 5 = "flow, useful output." 1 = "burned an hour producing nothing."
3. **Sample of two specific context switches.** For each: the task they left, the task they returned to, and how long before they felt productive on the new task.
4. **One concrete recent example of a "lost" morning.** Free text.

If fewer than 5 sessions are provided, say so and refuse to produce parameters — state that fewer than 5 sessions cannot distinguish signal from noise.

---

## Instructions

1. **Compute four parameters from the logs, nothing else.** For each parameter, show the calculation explicitly:
   - **Usable attention span (minutes):** median continuous span ending in a quality rating ≥ 3. Not longest span; median.
   - **Context-reload cost (minutes):** average of the two reported "time to productive" values from input 3.
   - **Interruption rate (per hour):** total interruptions across all sessions ÷ total session hours.
   - **Recovery time (minutes):** average gap between an interruption and the next useful work, inferred from session logs.

2. **Classify each parameter as reliable or tentative.**
   - Reliable if ≥ 5 datapoints contribute.
   - Tentative if fewer. Flag tentative parameters as "needs more data," do not round up confidence.

3. **Identify two contradictions between the numbers and the user's self-story.** Examples: "You said you 'usually focus for 2 hours'; median is 34 minutes," or "You said interruptions are rare; rate is 2.4/hr." If none exist, say so.

4. **Output one design implication per parameter.** A design implication is a concrete constraint on a future system — e.g., "Block length ≤ 40 min" or "Any triage system must cost ≤ 6 min of reload." Do not give lifestyle advice.

5. **Refuse to recommend specific apps, timer lengths, or routines.** That is a different prompt's job. This prompt ends at parameters + implications.

---

## Output Format

```
## Your Focus Parameters

| Parameter | Value | Confidence | Basis |
|---|---|---|---|
| Usable attention span | NN min | reliable/tentative | N sessions |
| Context-reload cost | NN min | reliable/tentative | N switches |
| Interruption rate | N.N / hr | reliable/tentative | N interruptions over N hrs |
| Recovery time | NN min | reliable/tentative | N datapoints |

## Contradictions With Your Self-Story
- [contradiction 1 with specific numbers]
- [contradiction 2 with specific numbers]
- (or: "None found.")

## Design Implications (one per parameter)
1. [constraint on future focus system]
2. ...

## What Would Sharpen These Numbers
- [specific data you'd need to log next week]
```

---

## Constraints

**Must:**
- Use the user's actual session data for every number.
- Show the calculation for each parameter.
- Distinguish reliable vs tentative.
- Cap output at the structure above.

**Must not:**
- Quote population averages ("most people focus for 25 minutes") even as context.
- Recommend specific tools, apps, or techniques — design is out of scope.
- Produce confident numbers from <5 sessions.
- Interpret low ratings as a motivation or discipline problem.

---

## False-Positive Prevention

This prompt is at high risk of producing plausible-sounding but generic productivity advice. Specific guards:

- **Generic-number test:** If any value would be the same for a different user, recheck — it should be derived, not canned.
- **Self-story trap:** The user's stated focus abilities usually overstate reality. Trust the logs, not the narrative, and name the gap explicitly.
- **Interpretation creep:** Do not explain *why* the numbers are what they are. A low attention span could be sleep, meds, job fit, or noise — that is the subject of a different diagnostic. State the numbers; leave causality alone.
- **False confidence:** If logs are incomplete, say so and stop. Do not extrapolate.

---

## Self-Verification (before finalizing)

Check each box before returning output:

- [ ] Every parameter value is tied to a calculation shown to the user.
- [ ] Confidence label matches datapoint count.
- [ ] At least one contradiction is stated, or a statement that none exist.
- [ ] Each design implication is a constraint, not a recommendation.
- [ ] No app, timer, or routine is named.
- [ ] No population average appears anywhere.

If any check fails, revise before returning.
