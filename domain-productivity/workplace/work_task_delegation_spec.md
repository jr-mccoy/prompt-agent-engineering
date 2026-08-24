---
title: "Task Delegation Spec"
category: productivity/workplace
description: "Specify a task clearly enough to hand it off successfully to a colleague, assistant, or report."
techniques:
  - ST-01
  - ST-02
  - DS-02
  - CM-02
  - QA-01
  - OC-06
difficulty: intermediate
tags:
  - delegation
  - management
  - specification
  - communication
  - leadership
updated: "2026-05-12"
related_prompts:
  - domain-productivity/workplace/work_1on1_prep.md
  - domain-productivity/workplace/work_deadline_juggler.md
  - domain-personal-development/prompts/agency/agency_next_action_spec.md
  - domain-professional-communication/prompts/product_delivery_sprint_planner.md
---

# Task Delegation Spec

**Objective:** Produce a delegation brief that gives the person you're handing off to everything they need to complete the task without a follow-up meeting. Covers outcome, authority, resources, constraints, and escalation triggers.

**When to use:** Before delegating any task that takes more than 2 hours of the delegate's time, involves judgment calls, produces a deliverable someone else will review, or where ambiguity about ownership could create problems. Use it especially when you're delegating to someone new to you, new to the role, or working without close oversight.

**Audience:** Managers, leads, and individual contributors who delegate work to colleagues, direct reports, contractors, or assistants. Not for one-line task assignments ("can you book the room?") where a message suffices, and not for multi-sprint engineering epics that require a project plan rather than a delegation brief.

---

## Inputs Required

1. **Task description.** What is the task? Describe it in terms of what needs to exist or happen when it's done — not just what the person should do. "Produce a competitive analysis of the top 3 vendors" not "research competitors."

2. **Delegate.** Who is doing this? Their role, their relevant experience or familiarity with this type of work, and how independently they can operate. A first-time delegate on a new task type needs more spec than an experienced person who has done it before.

3. **Due date.** When must this be complete? Be specific. If there is an intermediate check-in point (e.g., "draft by Tuesday, final by Friday"), include both.

4. **Desired outcome.** What does done look like? Describe the end state in terms that the delegate can evaluate themselves against. Include format, quality standard, and audience if relevant. "A slide deck" is not an outcome spec. "A 5-slide executive summary, formatted to match our standard template, that can be presented by the VP without additional editing" is.

5. **Constraints.** What must be true about how this is done? Required tools, required process steps, required stakeholders to loop in, budget limits, confidentiality restrictions, or anything the delegate must not do.

6. **Decision authority.** Explicitly list what decisions the delegate can make independently vs. what requires escalation back to you. This is the most commonly missing piece of a delegation brief, and its absence is the most common source of either micromanagement or dropped balls.

7. **Resources.** What does the delegate have access to? Relevant documents, contacts, tools, prior work examples, subject-matter experts they can consult.

8. **Check-in cadence.** When will you hear from them? A single check-in point at the midpoint for long tasks, or end-state delivery for short tasks. Specify the format (Slack message, drafted version, verbal update).

---

## Instructions

### Step 1 — Write the outcome spec before anything else

The most common delegation failure is an outcome spec that describes activity instead of outcome. "Research the vendors" is activity. "Produce a comparison table that includes pricing, integration complexity, and SLA terms for Vendor A, B, and C" is an outcome. Outcome specs let the delegate know when they're done and allow them to course-correct independently.

Test your outcome spec: could the delegate read it and decide for themselves whether their deliverable meets it? If yes, proceed. If not, rewrite it.

### Step 2 — Specify decision authority explicitly

Write three lists:

**Can decide independently:**
Things the delegate can choose, modify, or handle without coming back to you. The more experienced the delegate, the longer this list.

**Ask first:**
Things that require your input before the delegate proceeds. Keep this list short — every item is an interruption in your schedule and a bottleneck in theirs.

**Never:**
Hard lines that must not be crossed regardless of circumstances. These are non-negotiable.

### Step 3 — Identify the failure modes for this specific task

What are the three most likely ways this delegation goes wrong? For each:
- Name the failure mode
- State what would cause it
- State how to prevent it

Common delegation failure modes: delegate doesn't know enough context, delegate makes a decision you would have made differently, deliverable is in the right format but at the wrong level of detail, delegate waits too long to escalate a blocker.

### Step 4 — Write the brief

Assemble the delegation brief in the output format. The brief must be readable in under 5 minutes. If it takes longer, it's too long.

### Step 5 — Confirm the handoff

When you hand off the brief, ask the delegate two questions:
1. "What are you going to do first?"
2. "What would make you come back to me before the check-in?"

Their answers reveal whether the brief was clear. If the answers are vague, clarify before they start.

---

## Constraints

### Must
- Define outcome in terms of what done looks like, not just what to do
- Include an explicit decision authority section (can decide / ask first / never)
- Name at least one check-in point with a format
- Specify the audience or consumer of the deliverable — who receives it and what they'll do with it
- Name the resources the delegate can use

### Must Not
- Use vague task descriptions like "handle the client report" or "look into the API issue"
- Leave decision authority ambiguous — both "decide everything yourself" and "ask me about everything" are failures
- Set a due date without also specifying what an acceptable check-in looks like
- Delegate a task that hasn't been defined well enough for the delegator to do it themselves

---

## False-Positive Prevention

1. **The activity spec:** Describing what the delegate should do instead of what they should produce. "Research the competitive landscape" is an activity. "Produce a 1-page competitive summary covering Vendor A, B, C with a recommendation for which to pilot" is an outcome. Activity specs leave the delegate guessing about what done looks like.

2. **The implicit authority assumption:** Assuming the delegate knows what decisions they're authorized to make. Senior people make more decisions than you wanted; junior people escalate more than you expected. Write it down.

3. **The context gap:** Handing off a task without the background that explains why it matters or who will use the output. A delegate who doesn't understand the purpose of their work can't make good tradeoffs when something unexpected comes up.

4. **The single-point-of-failure delegation:** Handing off a task without identifying blockers the delegate might hit and how to handle them. If the delegate needs data from a system they can't access, or approval from someone who travels, the task stalls — and you won't find out until the deadline.

5. **The re-delegation by default:** Producing a brief for a task you should be doing yourself because only you have the context, authority, or relationship to do it well. Delegation is appropriate when the delegate can do it to the required standard. If they can't yet, the brief should include a heavier mentoring component or the task should stay with you.

---

## Output Format

```
DELEGATION BRIEF
================
Task: [Name of task]
Delegate: [Name / role]
Assigned by: [Your name]
Assigned on: [date]
Due: [date]
Check-in: [date / format — e.g., "draft via Slack by Tuesday EOD"]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
CONTEXT (why this matters)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
[2–3 sentences: what the task is in service of, who will use the output, why it matters now]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
OUTCOME SPEC (what done looks like)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
[Specific description of the deliverable: format, length, audience, quality standard]
[What the deliverable must be capable of doing — e.g., "must be readable without additional context by someone who wasn't in the meeting"]

Success criteria:
- [ ] [Criterion 1]
- [ ] [Criterion 2]
- [ ] [Criterion 3]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
DECISION AUTHORITY
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Can decide independently:
- [Decision type or example]
- [Decision type or example]

Ask first:
- [Decision type or example — include how to reach me and response time to expect]
- [Decision type or example]

Never (hard lines):
- [Action or decision that is off-limits]
- [Action or decision that is off-limits]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
RESOURCES
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
- [Document / link / prior example]
- [Contact: name, role, what to ask them, how to reach them]
- [Tool access or system permission needed — confirm they have it]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
CONSTRAINTS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
- Must use: [tool / format / process]
- Must loop in: [person / team] before [action]
- Must not: [restriction]
- Budget: [if applicable]
- Confidentiality: [if applicable]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
ESCALATION TRIGGERS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Come back to me immediately if:
- [Condition that changes the task or makes it impossible]
- [Decision that will materially affect the outcome and wasn't covered above]
- [Risk that puts the deadline at risk]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
HANDOFF CONFIRMATION QUESTIONS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Ask the delegate after sharing this brief:
1. "What are you going to do first?"
2. "What would make you come back to me before the [date] check-in?"
```

---

## Verification

- [ ] Outcome spec describes what done looks like, not just what to do
- [ ] Decision authority is written in three explicit lists (decide / ask / never)
- [ ] At least one check-in point is named with a date and format
- [ ] The audience or consumer of the deliverable is identified
- [ ] Resources are listed with enough detail to be usable
- [ ] Escalation triggers name specific conditions, not just "if anything goes wrong"
- [ ] The brief can be read and acted on in under 5 minutes
- [ ] Confirmation questions are included to verify the brief was understood
