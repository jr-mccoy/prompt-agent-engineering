---
title: "Troubleshoot a Lost Focus Day"
category: productivity/deep-work
description: "Diagnose a single day that was supposed to produce deep work and didn't — walking the day hour by hour against a fixed set of failure modes (calendar, triage, self-interruption, fatigue, wrong task, external shock) — so the user learns from the specific day rather than filing it under 'just a bad day.'"
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
  - troubleshooting
  - post-mortem
  - focus
updated: "2026-04-20"
related_prompts:
  - domain-productivity/deep-work/deepwork_self_interruption_audit.md
  - domain-productivity/deep-work/deepwork_calendar_audit.md
  - domain-productivity/deep-work/deepwork_focus_parameters_estimator.md
  - domain-productivity/deep-work/deepwork_focus_block_async_summary.md
---

# Troubleshoot a Lost Focus Day

**Objective:** Diagnose a specific day that was planned as a deep-work day but produced little, by walking it chronologically against a fixed set of failure modes. Output must name the dominant cause and one intervention — not a general lecture on focus.

**When to use:** End of a day that felt wasted. The day after, if the user still has clear memory. Run before the user writes the day off as "bad energy."

**Audience:** The individual reviewing their own day, not a manager post-morteming team output.

---

## Inputs Required

1. **The day's plan, as it existed at morning.** Tasks, blocks, order.
2. **What actually happened, hour by hour.** Rough — 30- or 60-minute granularity is fine.
3. **First moment the plan derailed.** Time and description.
4. **How the user felt physically at start of day** (tired / rested / off) and at 3 pm (different, same).
5. **External shocks.** Emergency, surprise meeting, bad news, anything unplanned.
6. **The one task the day was supposed to produce.** Did it? yes/no/partial.

If the user cannot reconstruct the timeline at this level, say so and ask them to return after 15 minutes of walking through the day.

---

## Instructions

1. **Compare plan vs actual hour-by-hour.** Highlight the first point of divergence (from input 3) and every subsequent point.

2. **Classify the day against a fixed set of failure modes.** More than one may apply; pick the dominant one.

   - **Calendar sabotage** — meetings or blocks destroyed focus time that should have existed
   - **Triage spiral** — the user started with email/Slack and never exited
   - **Self-interruption loop** — repeated self-initiated context switches inside blocks
   - **Fatigue / physical** — the body was not capable of the planned cognitive load
   - **Wrong task** — the planned task was blocked, too vague, or secretly avoided
   - **External shock** — something happened that made the plan irrelevant
   - **Plan-reality mismatch** — the plan assumed focus parameters the user doesn't have

3. **Cite 2–3 concrete moments from input 2** that support the chosen failure mode. No invented details.

4. **Separate one-off shock from pattern.** A true external shock should not produce a system change. A recurring failure mode (third "triage spiral" Monday in a row) should.

5. **Propose exactly one intervention** targeted to the dominant failure mode. Name which prompt in this folder is appropriate (e.g., triage spiral → `deepwork_message_triage_system.md`). Do not produce a general focus overhaul.

6. **Name what the user should not conclude.** Common wrong lessons: "I have no discipline," "I need to start earlier," "I should get a new tool." If any of these are tempting, reject with reason.

---

## Output Format

```
## Day Under Review
- Date / planned top outcome: [...]
- Was top outcome produced? yes / no / partial

## Plan vs Actual
| Block | Planned | Actual | Divergence? |
|---|---|---|---|
| 9:00 | Deep work on X | Email + news | first divergence: input 3 |
| ...  |

## Dominant Failure Mode
[one from fixed set] — evidence:
- [moment from input 2]
- [moment from input 2]

## One-Off or Pattern?
- This time: [one-off / nth occurrence]
- Implication: [system change warranted / no change, move on]

## One Intervention
- Target: [failure mode]
- Specific move: [...]
- Related prompt: [filename]

## Wrong Lessons to Avoid
- [specific tempting but wrong conclusion, with reason to reject]
```

---

## Constraints

**Must:**
- Walk the day chronologically.
- Choose exactly one dominant failure mode.
- Cite concrete moments from input 2 for the diagnosis.
- Separate one-off shock from recurring pattern.
- Name at most one intervention.

**Must not:**
- Turn the review into a character assessment ("I'm undisciplined").
- Propose 3+ interventions. One-day review licenses one change.
- Move past the evidence. If inputs are thin, name insufficient data.
- Use language like "bad day" or "off energy" as diagnosis — those aren't mechanisms.

---

## False-Positive Prevention

- **Discipline story:** The default reflexive diagnosis is "I didn't try hard enough." It is rarely correct and always useless. Insist on a structural failure mode.
- **Shock inflation:** Not every unusual event is a shock. A surprise meeting is only a shock if it genuinely disrupted the planned block — otherwise it's a calendar issue.
- **Pattern over-read from one day:** One day doesn't establish a pattern. If the user has no prior data, mark "one-off, watch for next 2 weeks."
- **Tool-shopping:** The user will be tempted to download an app. Block this — the intervention is about structure, not tools.

---

## Self-Verification (before finalizing)

- [ ] Plan vs actual walked hour-by-hour.
- [ ] Exactly one dominant failure mode named.
- [ ] Two or three concrete moments cited as evidence.
- [ ] One-off vs pattern is stated.
- [ ] Exactly one intervention proposed.
- [ ] Wrong lessons section names tempting but incorrect conclusions.
- [ ] No character- or discipline-based diagnosis.
