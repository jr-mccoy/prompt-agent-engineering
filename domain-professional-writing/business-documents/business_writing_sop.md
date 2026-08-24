# SOP / Process Document (Standard Operating Procedure)

**Source:** BUSINESS_WRITING_PROMPTS.md

**Category:** Business Writing / Process Documentation

## Prompt

```
You are writing a standard operating procedure that enables someone to execute a repeatable process consistently and correctly.

CONTEXT:
Process name: [WHAT PROCESS THIS DOCUMENTS]
Process owner: [WHO MAINTAINS THIS PROCESS]
Who executes this: [ROLE/TEAM WHO DOES THIS WORK]
Frequency: [HOW OFTEN THIS RUNS - e.g. "daily" or "when customer requests X" or "quarterly"]
Why this matters: [IMPACT IF DONE WRONG]

INPUT PROVIDED:
[PASTE YOUR CURRENT PROCESS STEPS, TOOLS USED, DECISION POINTS, EDGE CASES, EXAMPLES HERE]

YOUR TASK:
Create an SOP that someone can follow to complete this process without asking questions. This will be used by people with varying experience levels, so clarity and completeness matter more than brevity.

REQUIRED STRUCTURE:
1. **Purpose** (Why this process exists and what it accomplishes - 2 sentences)
2. **Scope** (When to use this SOP vs. when NOT to use it)
3. **Roles & Responsibilities** (Who does what in this process)
4. **Prerequisites** (What must be true before starting - access, tools, information)
5. **Step-by-Step Procedure** (Numbered steps with decision points and expected outcomes)
6. **Edge Cases** (The 5 most common variations and how to handle them)
7. **Quality Checks** (How to verify the process was completed correctly)
8. **Troubleshooting** (Common problems and specific fixes)
9. **Process Metadata** (Owner, last updated, review schedule)

CONSTRAINTS:
- Total length: 1200 words maximum
- Purpose: Must state the outcome, not just describe the activity
- Scope: Must explicitly state what this does NOT cover (prevents scope confusion)
- Prerequisites: Must include actual tool names, permission levels, and information requirements from inputs
- Procedure: Each step must have a verb (action) and expected outcome
- Decision points: Must be formatted as "IF [condition] THEN [action] ELSE [alternative action]"
- Edge cases: Must use actual scenarios from inputs, not invented examples
- Quality checks: Must be verifiable (not "make sure it looks good" but "verify field X contains Y")
- DO NOT make steps dependent on tribal knowledge ("as usual" or "the normal way")
- DO NOT skip error handling (what to do when step fails)
- Use only information from inputs - do not invent process steps or edge cases

TONE:
- Instructional and precise, not conversational
- Use imperative voice ("Click the X button" not "You should click" or "The user clicks")
- State decisions explicitly (if/then), not implicitly ("usually" or "typically")
- Assume reader is executing this for the first time

QUALITY CHECKS - Before outputting, verify:
- [ ] Purpose states the outcome (what's accomplished), not the activity
- [ ] Scope includes both what IS and what IS NOT covered
- [ ] Every prerequisite references actual tools/permissions from inputs
- [ ] Every procedure step begins with a verb (action word)
- [ ] Every procedure step states expected outcome
- [ ] All decision points use IF/THEN/ELSE format
- [ ] Edge cases address actual scenarios from inputs (not generic variations)
- [ ] Quality checks are pass/fail verifiable
- [ ] No step relies on "knowing how we usually do this"
- [ ] Process owner and last updated date are specified
- [ ] Total word count is under 1200 words

If any check fails, revise before outputting.
```

## Usage Notes

**Purpose:** SOPs exist to ensure consistency and quality when multiple people execute the same process. The structure forces operational precision.

**Customization Options:**
- Adjust for process maturity (early-stage, mature, regulated, critical)
- Modify for organization (process automation, efficiency tracking, approvals, regular reviews)
- Add sections for different process types (customer-facing, data, financial, security, onboarding)

**Common Pitfalls:**
- Assumes tribal knowledge (only experts can follow)
- Missing scope boundaries (used for wrong situations)
- Vague steps (no clear action or success criteria)
- No edge case handling
- No quality verification
- Outdated (no owner or review schedule)
- Ambiguous decision points buried in narrative
