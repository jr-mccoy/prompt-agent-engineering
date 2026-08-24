---
title: "Mission Planning Template"
category: meta
description: ""
tags:
  - meta
updated: "2025-12-24"
---

# Mission Planning Template

Use this before starting any new agent task. Forces you to think through the job clearly before hitting send.

## Purpose

This is a meta-prompt for writing better instructions for any agent. Not for specific tools—it's a template for structuring any delegation.

## Techniques Used
- **ST-07**: Actionable Output Requirements - Deliverable specification
- **ST-03**: Constraint Specification - Boundaries and scope
- **DS-02**: Evidence-Based Decision Making - Source prioritization
- **RT-02**: Explicit Uncertainty Quantification - Ambiguity handling
- **NE-03**: Input Template Scaffolding - Structured confirmation request

## The Prompt

```
I need to [DESCRIBE THE TASK IN ONE SENTENCE].

Before you start, confirm your understanding by answering:

1. **Deliverable**: What specific output will you produce?
   - Format (spreadsheet, document, app, automation?)
   - Structure (what sections, columns, or components?)
   - Length or scope (how many items, how much detail?)

2. **Sources**: What will you use to complete this?
   - What sources are acceptable?
   - What sources should you avoid?
   - What's the priority order if sources conflict?

3. **Boundaries**: What will you explicitly NOT do?
   - What's out of scope?
   - What decisions require my input vs. your judgment?

4. **Success criteria**: How will I know the job is done right?
   - What must be true for me to trust the output?
   - What evidence will you provide?

5. **Ambiguity handling**: What will you do if something is unclear?
   - At what point should you ask me vs. make a judgment call?
   - What assumptions are you making?

If any part of my request is ambiguous, ask ONE clarifying question before proceeding. Do not guess on important details.

---

Once you've confirmed understanding, proceed with the task.
```

## When to Use

- Starting any complex agent task
- Delegating to AI for the first time
- Tasks where misunderstanding would be costly
- Setting up recurring workflows

## Why This Works

Forces explicit agreement on:
1. **What** you're getting (deliverable)
2. **How** it will be created (sources)
3. **What's off limits** (boundaries)
4. **What good looks like** (success criteria)
5. **How to handle unknowns** (ambiguity)

## Customization

Replace `[DESCRIBE THE TASK IN ONE SENTENCE]` with your specific task, then use the agent's responses to refine your request.
