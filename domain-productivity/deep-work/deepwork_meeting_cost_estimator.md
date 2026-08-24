---
title: "Estimate the True Cost of a Meeting"
category: productivity/deep-work
description: "Compute the real cost of a specific meeting — wall-clock time × attendees, plus prep, plus context-switch tax on both sides, plus focus-block destruction if it lands mid-block — so decisions to keep, shrink, or kill the meeting are grounded in a number, not a vibe."
techniques:
  - ST-01
  - ST-02
  - DS-01
  - CM-02
  - OC-01
  - QA-01
difficulty: beginner
tags:
  - deep-work
  - meetings
  - cost
  - estimation
updated: "2026-04-20"
related_prompts:
  - domain-productivity/deep-work/deepwork_meeting_to_async_converter.md
  - domain-productivity/deep-work/deepwork_calendar_audit.md
  - domain-productivity/deep-work/deepwork_team_focus_audit.md
---

# Estimate the True Cost of a Meeting

**Objective:** For one specific meeting, produce a concrete cost estimate that includes wall-clock time, prep, context-switch tax, and focus-block destruction. Output a single bottom-line number of person-minutes per instance and per year, plus a one-sentence judgment.

**When to use:** Before deciding to keep, shrink, or kill a meeting. When proposing a meeting change and needing a number to argue with. When a meeting's cost is suspected to be invisible because it's "just an hour."

**Audience:** The individual or team lead evaluating a specific meeting, not a blanket meeting-culture audit.

---

## Inputs Required

1. **Meeting name, frequency, duration.**
2. **Attendee count and rough role mix.** Role mix allows sanity-checking attendee necessity but not dollar costs (out of scope).
3. **Prep expected per attendee** — realistic minutes, not the advertised "no prep needed." Ask the user; do not assume.
4. **Whether the meeting typically lands mid-focus-block for any attendees.** Yes/sometimes/no.
5. **Typical context-switch / reload cost** for attendees (use focus-parameters value or 15 min default).
6. **Last 3 instances' actual outcomes** — what decision or artifact resulted. If nothing, note that.

---

## Instructions

1. **Compute wall-clock cost per instance:** duration × attendees. Report in person-minutes.

2. **Compute prep cost per instance:** prep × attendees. Prep is commonly forgotten — include even when small.

3. **Compute context-switch cost per instance:**
   - Every attendee pays at least one reload-cost (entry into meeting context).
   - Attendees for whom the meeting lands mid-focus-block pay an additional reload-cost (returning to work after).
   - Compute from inputs 4 and 5.

4. **Compute focus-block destruction.** A meeting landing inside a focus block doesn't just cost its duration; it can wipe the whole block. For each attendee with a mid-block landing, add (attention span − remaining block time after meeting), if positive.

5. **Total per instance.** Sum of all four components, in person-minutes.

6. **Annualize.** Instances per year × per-instance cost.

7. **Compare against outcome.** Using input 6, compute rough output per instance. Is the total cost reasonable for the observed output? Answer is yes, no, or "outcome too variable to say."

8. **Write a one-sentence judgment** grounded in the number. "At ~N person-hours per week for [output], the cost is [appropriate / questionable / high]." Do not soft-sell.

---

## Output Format

```
## Meeting
[name] — [frequency] — [duration] — [attendees]

## Per-Instance Cost Breakdown
| Component | Formula | Person-minutes |
|---|---|---|
| Wall-clock | N × N | NN |
| Prep | N × N | NN |
| Context-switch in | N × N | NN |
| Mid-block destruction | ... | NN |

Per-instance total: NN person-min

## Annualized
- Instances/year: N
- Annual cost: NN person-hours

## Outcome Observed (last 3 instances)
- [brief]

## Judgment
[One sentence tying cost to observed output.]
```

---

## Constraints

**Must:**
- Include all four components — omitting prep or mid-block destruction is the default failure.
- Show the formula for each component so the user can audit.
- Ground the judgment in the computed number, not adjectives.
- Output person-minutes (not dollars, not "FTE-weeks").

**Must not:**
- Convert to dollar cost (out of scope, requires salary data that isn't the point).
- Add speculative costs (morale, team cohesion, etc.) without a number.
- Pad with recommendations — the judgment is the endpoint.
- Round down. Round up to the nearest 5 minutes on each component.

---

## False-Positive Prevention

- **Prep invisibility:** Users will say "no prep" even when three attendees read the doc for 20 minutes. Probe. Prep is almost never zero.
- **Block destruction undercount:** The standard mistake is counting the 60-min meeting as 60 min. If it lands in the middle of a 3-hour block, the true cost may be 180 min for that attendee.
- **Outcome inflation:** "We align" is not an outcome. If input 6 is fuzzy, flag "outcome too variable to say" rather than invent a justification.
- **Asymmetric attendance:** If some attendees are required and others are optional, do not weight equally without saying so. Offer a split ("required cost: NN; optional cost: NN").

---

## Self-Verification (before finalizing)

- [ ] All four components computed and shown with formulas.
- [ ] Prep is included (even when small) and sourced to input 3.
- [ ] Mid-block destruction handled per input 4.
- [ ] Annualized figure shown as person-hours.
- [ ] Judgment is one sentence and references the computed number.
- [ ] No dollar conversion; no speculative cost.
