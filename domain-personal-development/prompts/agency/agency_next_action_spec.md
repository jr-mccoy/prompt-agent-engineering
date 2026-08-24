---
title: "Define the Next Concrete Action for the Day"
category: personal-development/agency
description: "Force a single, unambiguous next physical action out of a mental pile of todos, intentions, and open loops — the kind of action a tired person can start within 60 seconds."
techniques:
  - ST-01
  - ST-02
  - CM-02
  - QA-01
difficulty: beginner
tags:
  - agency
  - next-action
  - execution
  - focus
  - self-directed-work
updated: "2026-04-20"
related_prompts:
  - domain-prompt-engineering/delegation/delegation_intent_specification.md
  - domain-prompt-engineering/delegation/delegation_tool_vs_colleague_decision.md
  - domain-personal-development/prompts/agency/agency_stuck_diagnosis.md
  - domain-personal-development/prompts/agency/agency_rapid_start_mode.md
---

# Define the Next Concrete Action for the Day

**Objective:** Given the user's current mental pile — goals, todos, open loops, worries — return one specific next action they can start within 60 seconds. Not the best action. Not a plan. One action, specified at the level of "open the file named X and do Y for 25 minutes."

**When to use:** The user has a list of things to do but isn't doing any of them. They describe their work in verbs like "figure out," "look at," "think through." They've been awake for hours and haven't produced an artifact.

**Audience:** An individual at their own desk with their own tools, doing self-directed work. Not someone planning their team's day.

---

## Inputs Required

1. **The current pile.** What's in their head right now — goals, tasks, obligations, worries. Brain-dump style, not curated.
2. **Available time.** The realistic block they have before the next fixed obligation (meeting, pickup, commute).
3. **Energy level.** Low / medium / high. Honest answer, not aspirational.
4. **Active project.** If they already have one named project (see `agency_project_ownership_converter.md`), state it. If not, say "none."

If the pile is empty or the time block is under 15 minutes, flag that before proceeding — this prompt's output needs both.

---

## Instructions

### Step 1 — Surface the real candidates

From the pile, extract 3–7 items that are:

- **Movable today** — can be advanced with the tools, access, and energy the user has right now.
- **Attached to something the user already committed to** — not a new idea, not a "maybe I should."
- **Not a container item** — "work on the essay" is a container; "write the opening paragraph of the essay" is a candidate.

If fewer than 3 candidates survive, name that and stop. The pile needs triage before action can be chosen.

### Step 2 — Rank by ship-pressure, not interest

Rank the candidates by a single criterion: which one has the most external consequence if it doesn't move today? (A deadline, another person waiting, a window closing, a streak being broken.) Ignore which one is most interesting. Interest is fickle; consequence is not.

If two items are tied, prefer the one that produces a visible artifact by end of session.

### Step 3 — Specify the top candidate at physical-action level

Take the top-ranked item and rewrite it so all three of these are true:

1. **Opens in one motion.** "Open [file/tool/URL]" — not "find" or "look up."
2. **First 25 minutes are defined.** What the user will type, click, or write during that window.
3. **End state is checkable.** At the 25-minute mark, either [specific output] exists or it doesn't.

If the user's energy is low, shrink the first 25 minutes to the smallest unit that still produces an artifact. A bad first draft of one paragraph beats a perfect plan for a whole essay.

### Step 4 — Name what is being declined

List the 2–4 next-most-tempting items the user will ignore for this session. Naming them defuses the pull. Include at least one item from the pile that is "productive-looking" but not the ranked winner (email triage, tool setup, reading).

### Step 5 — Produce the start-line

A single sentence the user can read as they sit down. It names the file/tool, the first physical motion, and the 25-minute end state. It does not contain "try to," "maybe," or "if."

---

## Constraints

### Must
- Return exactly one next action.
- State it at the level of a physical motion (open X, type Y, write Z).
- Define a 25-minute end state that is checkable.
- Name at least two items the user is choosing not to do right now.
- Respect the stated energy level — don't propose a high-focus task to a low-energy user.

### Must Not
- Return a list of three good options. The whole point is to cut to one.
- Propose research, reading, planning, or tool setup as the next action (unless the project is in a genuine setup phase and the user named that).
- Ask the user to "reflect on" or "think about" anything as the action itself. Thinking is not the action — writing the thinking down is.
- Use encouragement or motivation language.
- Invent new tasks that weren't in the user's pile.

---

## False-Positive Prevention

This prompt fails in the following specific ways. Check each before returning:

1. **Category-level action.** "Work on the report" is not a next action. "Open report.md and write the executive summary section header plus three bullet points" is.
2. **Planning-dressed-as-execution.** "Outline the essay" can be an action if the outline is the artifact, but only if the user hasn't used outlining as an excuse to avoid drafting before. If they have, push past outline to first sentence.
3. **Tool-setup avoidance.** "Set up my writing environment" is rarely the actual blocker; it's the comfortable blocker. Interrogate it once before accepting.
4. **Email / inbox triage.** This is almost never the most consequential action. Decline it unless the user explicitly named a specific email that has external consequence today.
5. **Someone-else-dependent item.** If the next physical motion is "wait for X to reply," that's not an action for this session — pick something else.

If the drafted action matches any of these patterns, rewrite.

---

## Output Format

```
## Next action
[Single sentence. Physical motion + 25-minute end state.]

## Why this one
[1–2 sentences on ship-pressure — what external consequence drove the pick.]

## Start-line
[One sentence the user reads as they sit down. Names the file/tool and the first motion.]

## 25-minute end state
At the timer, the following exists:
- [Specific artifact]

## Declined this session
- [Tempting item 1]
- [Tempting item 2]
- [Productive-looking-but-not-consequential item]

## If energy crashes mid-session
Minimum viable artifact: [smaller version that still counts as progress]
```

---

## Verification

Before returning:

- [ ] The action opens in one physical motion the user can perform at their desk.
- [ ] The 25-minute end state is something another person could verify by looking.
- [ ] Nothing in the output uses "figure out," "think about," "look into," "reflect on."
- [ ] Declined items include at least one productive-looking distractor.
- [ ] Energy level was respected — the action's difficulty matches.
- [ ] No motivational language.

If any fail, revise.
