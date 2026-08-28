---
title: "Performance Support Job Aid Designer"
category: education-teaching/instructor/higher-ed-corporate
description: "Design an at-the-moment-of-need job aid (decision tree, checklist, quick reference card, or embedded helper) that solves a workflow problem in under 60 seconds without requiring training."
techniques:
  - ST-02
  - CM-02
  - DS-01
  - OC-01
  - QA-01
difficulty: beginner
tags:
  - performance-support
  - job-aid
  - quick-reference
  - workflow
  - corporate-training
  - moment-of-need
updated: "2026-05-09"
related_prompts:
  - domain-education-teaching/instructor/higher-ed-corporate/teaching_microlearning_module.md
  - domain-education-teaching/instructor/higher-ed-corporate/teaching_train_trainer_guide.md
  - domain-education-teaching/instructor/higher-ed-corporate/teaching_compliance_training_module.md
---

# Performance Support Job Aid Designer

## Objective

Produce a job aid that solves a real workflow problem at the moment of need — under 60 seconds, no training required, available where the work happens. Output is the artifact (decision tree / checklist / quick reference / embedded prompt) plus a placement and maintenance plan.

## When to Use

- A task is too rare to remember reliably but too consequential to wing
- New tool or process rolling out where every detail can't be memorized
- High-stakes decision points where errors are costly
- Workflows that change frequently
- Compliance moments embedded in regular work
- Roles with high turnover where institutional memory leaks

## When NOT to Use

- Foundational skill-building — use `hecorp_microlearning_module.md`
- Compliance training requiring documentation — use `hecorp_compliance_training_module.md`
- Workflow that needs deep understanding (job aid alone won't carry it)

---

## Inputs Needed

- **The moment of need:** [What is happening at the exact second this is used? Be concrete.]
- **The decision or action required:** [What does the user do?]
- **Who uses it:** [Role, frequency, current proficiency]
- **Where the work happens:** [In a software tool, on the floor, on a phone call, in the field, etc.]
- **Time available:** [Seconds, minute or two, longer]
- **Current failure mode:** [What happens when the user doesn't have this aid]
- **Update frequency:** [How often the underlying process changes]
- **Constraints:** [Mobile only, wall-postable, screen-readable, must fit one card, etc.]

---

## Instructions

### Step 1: Define the Moment Concretely

Write a one-sentence scene:

> "A customer-service rep is on a call, customer reports a fraud charge, rep must decide whether to escalate to fraud team or refund directly, has 30 seconds before customer feels stalled."

If you can't write this scene, the job aid is solving the wrong problem.

### Step 2: Choose the Right Format

Match form to moment:

| Moment characteristic | Best format |
|------------------------|-------------|
| Decision with branching | Decision tree (visual) |
| Linear procedure with skip-able steps | Checklist |
| Lookup of values, codes, or rules | Reference card (table) |
| Trigger words or scripts | Talk-track / script card |
| Action inside a tool | Embedded tooltip, hover, or in-app prompt |
| Field work, hands occupied | Voice-readable steps / mobile card with large text |
| Rare event handling | Runbook (longer, but indexed) |

### Step 3: Distill to Essentials

Cut ruthlessly. A job aid is not a manual. Test:

- [ ] Can a new user use this without explanation?
- [ ] Does every word earn its space?
- [ ] Is the most common decision visually privileged?
- [ ] Are exception paths separable from the main path?
- [ ] Is the longest reading sequence under 30 seconds?

If not, cut more.

### Step 4: Design the Artifact

For the chosen format, draft:

**Decision tree:**
```
START
  │
  ├─ [Question 1]?
  │    ├─ Yes → [Question 2]?
  │    │         ├─ Yes → ACTION A
  │    │         └─ No  → ACTION B
  │    └─ No  → ACTION C
```
Limit to ~3 levels deep. Beyond that, branch into a sub-aid.

**Checklist:** Numbered, action-verb start, one action per line, 5–9 items max.

**Reference card:** Two-column table, most-used items first, exception column on side.

**Script card:** Trigger phrase → exact words → next step.

### Step 5: Visual Hierarchy

- Most-used path: largest, top, bold
- Exceptions: smaller, side, lighter
- Warnings: distinct (color, icon, or border)
- White space: protect it — density kills usability

### Step 6: Placement Plan

A perfect job aid hidden in a SharePoint folder is useless. Specify placement:

| Workflow location | Placement |
|--------------------|-----------|
| In a software tool | Embedded help, tooltip, in-app guide |
| Desk work | Pinned tab, browser bookmark, sticky on monitor |
| Phone work | Second screen, headset card, dashboard sidebar |
| Field work | Mobile card, laminated card, voice-accessible |
| Floor / production | Posted at station, laminated, in language(s) used |
| Customer-facing | Privacy: don't post if customer can see — use earpiece or back-of-house card |

### Step 7: Test the Aid in Situ

Before deploying:

- Watch a real or simulated user attempt the moment with only the aid
- Note where they hesitate, scan twice, ask a colleague
- Time them — does it actually fit the time budget?
- Revise based on observation, not opinion

If the aid takes longer than the moment allows, redesign.

### Step 8: Maintenance Plan

Job aids decay. Specify:

- Owner (named role)
- Update trigger: process change, regulation change, tool change, error rate spike
- Version on the artifact (small, but present)
- Review cadence (quarterly, semi-annual, annual)
- Retirement plan if the underlying process automates the decision away

### Step 9: Accessibility

- Color is not the only carrier of meaning
- Font size readable in placement context
- Language(s) match workforce
- Reading level appropriate
- Translation reviewed by qualified speakers
- Mobile-readable if mobile-placed
- Screen-reader friendly if digital

### Step 10: Pair With Just-Enough Training

Sometimes the aid alone works. Sometimes a 60-second walkthrough seeds the habit. Decide:

- Is this a tool people will discover and use? Pair with mention in onboarding or team meeting
- Will people forget it exists? Add a manager reminder cadence
- Is this for an emergency? Make sure people know it's there before the emergency
- Is the underlying skill deeper? Pair with microlearning (use `hecorp_microlearning_module.md`)

---

## Output Format

1. Moment-of-need scene (one sentence)
2. Format choice with rationale
3. Distilled essentials (post-cut)
4. Drafted artifact (in chosen format)
5. Visual hierarchy notes
6. Placement plan
7. In-situ test plan
8. Maintenance & ownership plan
9. Accessibility checklist
10. Pairing-with-training decision

---

## False-Positive Prevention

❌ **DON'T:**
- Build a manual and call it a job aid
- Hide the aid where the work doesn't happen
- Use color or icons as the sole carrier of meaning
- Design without watching a user try it
- Skip the version stamp — outdated aids are dangerous
- Confuse "we made it" with "people use it"

✅ **DO:**
- Anchor on the concrete moment
- Cut to essentials
- Place where the moment occurs
- Test in situ and revise
- Assign an owner and review cadence
- Pair with just-enough training when needed

---

## Quality Indicators

- [ ] Moment described in one sentence
- [ ] Format matches moment
- [ ] Artifact fits time budget
- [ ] Placement plan concrete
- [ ] Tested with real user before deployment
- [ ] Owner and update cadence assigned
- [ ] Accessible and translated as needed

---

## Techniques Used

| Technique | How It's Applied |
|-----------|-----------------|
| **ST-02** | Moment → format → distill → draft → test → place → maintain pipeline. |
| **CM-02** | Time and space constraints (60 sec, one card) drive ruthless distillation. |
| **DS-01** | Performance-support frame (moment-of-need, not training) drives format choice. |
| **OC-01** | Format-specific templates produce paste-ready artifact. |
| **QA-01** | In-situ user test verifies the aid solves the actual moment. |
